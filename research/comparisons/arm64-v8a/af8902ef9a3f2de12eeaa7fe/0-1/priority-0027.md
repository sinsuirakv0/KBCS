# v15.7.3 → v15.7.4 · 最優先の変更候補 (27)

[一覧の目次](README.md)

<a id="compare-cde565d69cd0a7964e5330aa215e6005"></a>

### [`006330dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00633/006330dc.md) → [`006330dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/006330dc.md) FUN_006330dc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00a8f660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a8f/00a8f660.md) · 呼出先 34件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)
- 新版 呼出元 1件 [`00a8f6a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a8f/00a8f6a4.md) · 呼出先 34件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 94.19% / 新版 94.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 11件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00633424",
      "incomplete_value": false,
      "site": "00633428",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00633424",
      "incomplete_value": false,
      "site": "00633428",
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
            "const:cd0:8"
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
      "definition_site": "00633554",
      "incomplete_value": true,
      "site": "00633558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00633554",
      "incomplete_value": true,
      "site": "00633558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00633628",
      "incomplete_value": false,
      "site": "00633628",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00633628",
      "incomplete_value": false,
      "site": "00633628",
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
            "const:d50:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00633428",
      "DATA",
      [
        "storage",
        "00bf6cd0",
        null,
        "undefined *"
      ]
    ],
    [
      "006334d8",
      "READ",
      [
        "storage",
        "00bf6cf8",
        null,
        "undefined *"
      ]
    ],
    [
      "00633518",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00633428",
      "DATA",
      [
        "storage",
        "00bf6d20",
        null,
        "undefined *"
      ]
    ],
    [
      "006334d8",
      "READ",
      [
        "storage",
        "00bf6d48",
        null,
        "undefined *"
      ]
    ],
    [
      "00633518",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00633424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00633/006330dc.md#insn-00633424) · [`00633518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00633/006330dc.md#insn-00633518) · [`00633550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00633/006330dc.md#insn-00633550)
- 新版 [`00633424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/006330dc.md#insn-00633424) · [`00633518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/006330dc.md#insn-00633518) · [`00633550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/006330dc.md#insn-00633550)

~~~diff
- 00633424 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00633424 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00633424 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00633424 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00633424 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00633424 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00633424 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00633424 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00633424 bytes 4a413391
+ 00633424 bytes 4a813491
- 00633518 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:520:8"]]
- 00633518 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00633518 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:570:8"]]
+ 00633518 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 00633518 bytes 7b9342f9
+ 00633518 bytes 7bbb42f9
- 00633550 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:528:8"]]
- 00633550 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00633550 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:578:8"]]
+ 00633550 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00633550 bytes 089542f9
+ 00633550 bytes 08bd42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-474f007f372633d8f53cbfe581aab893"></a>

### [`00633eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00633/00633eb0.md) → [`00633eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/00633eb0.md) FUN_00633eb0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`006330dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00633/006330dc.md) [`006388e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/006388e8.md) · 呼出先 32件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md)
- 新版 呼出元 2件 [`006330dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/006330dc.md) [`006388e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/006388e8.md) · 呼出先 32件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.06% / 新版 92.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 18件, `store_value` 14件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00633f18",
      "incomplete_value": false,
      "site": "00633f18",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00633f18",
      "incomplete_value": false,
      "site": "00633f18",
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
            "const:d98:8"
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
      "definition_site": "00633f24",
      "incomplete_value": true,
      "site": "00633f24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4058:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00633f24",
      "incomplete_value": true,
      "site": "00633f24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4058:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00633f2c",
      "incomplete_value": false,
      "site": "00633f2c",
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
            "const:dd4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00633f2c",
      "incomplete_value": false,
      "site": "00633f2c",
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
            "const:d94:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00633f18",
      "WRITE",
      [
        "storage",
        "00c26d98",
        null,
        "undefined4"
      ]
    ],
    [
      "00633f24",
      "WRITE",
      [
        "storage",
        "00c26d90",
        null,
        "undefined1"
      ]
    ],
    [
      "00633f2c",
      "WRITE",
      [
        "storage",
        "00c26d94",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00633f18",
      "WRITE",
      [
        "storage",
        "00c26dd8",
        null,
        "undefined4"
      ]
    ],
    [
      "00633f24",
      "WRITE",
      [
        "storage",
        "00c26dd0",
        null,
        "undefined1"
      ]
    ],
    [
      "00633f2c",
      "WRITE",
      [
        "storage",
        "00c26dd4",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00633f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00633/00633eb0.md#insn-00633f18) · [`00633f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00633/00633eb0.md#insn-00633f24) · [`00633f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00633/00633eb0.md#insn-00633f2c)
- 新版 [`00633f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/00633eb0.md#insn-00633f18) · [`00633f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/00633eb0.md#insn-00633f24) · [`00633f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/00633eb0.md#insn-00633f2c)

~~~diff
- 00633f18 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d98:8"]]
- 00633f18 ["COPY", "tmp:1:4", ["const:0:4"]]
- 00633f18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
+ 00633f18 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:dd8:8"]]
+ 00633f18 ["COPY", "tmp:1:4", ["const:0:4"]]
+ 00633f18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 00633f18 bytes 5f990db9
+ 00633f18 bytes 5fd90db9
- 00633f24 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00633f24 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00633f24 ["INT_ADD", "tmp:2:8", ["register:4058:8", "const:d90:8"]]
- 00633f24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00633f24 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00633f24 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00633f24 ["INT_ADD", "tmp:2:8", ["register:4058:8", "const:dd0:8"]]
+ 00633f24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00633f24 bytes 7f413639
+ 00633f24 bytes 7f413739
- 00633f2c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d94:8"]]
- 00633f2c ["COPY", "tmp:1:4", ["const:0:4"]]
- 00633f2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
+ 00633f2c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:dd4:8"]]
+ 00633f2c ["COPY", "tmp:1:4", ["const:0:4"]]
+ 00633f2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 00633f2c bytes df960db9
+ 00633f2c bytes dfd60db9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25062415c0db93aab10cbdd20bf8346f"></a>

### [`00634d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00634/00634d50.md) → [`00634d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00634/00634d50.md) FUN_00634d50

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00631e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00631/00631e1c.md) · 呼出先 34件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)
- 新版 呼出元 1件 [`00631e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00631/00631e1c.md) · 呼出先 34件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 93.93% / 新版 93.93%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 7件, `store_value` 13件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00635098",
      "incomplete_value": false,
      "site": "0063509c",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00635098",
      "incomplete_value": false,
      "site": "0063509c",
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
            "const:e50:8"
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
      "definition_site": "006351c8",
      "incomplete_value": true,
      "site": "006351cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "006351c8",
      "incomplete_value": true,
      "site": "006351cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 48,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0063529c",
      "incomplete_value": false,
      "site": "0063529c",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063529c",
      "incomplete_value": false,
      "site": "0063529c",
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
            "const:ed0:8"
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0063509c",
      "DATA",
      [
        "storage",
        "00bf6e50",
        null,
        "undefined *"
      ]
    ],
    [
      "0063514c",
      "READ",
      [
        "storage",
        "00bf6e78",
        null,
        "undefined *"
      ]
    ],
    [
      "0063518c",
      "READ",
      [
        "storage",
        "00c1b520",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0063509c",
      "DATA",
      [
        "storage",
        "00bf6ea0",
        null,
        "undefined *"
      ]
    ],
    [
      "0063514c",
      "READ",
      [
        "storage",
        "00bf6ec8",
        null,
        "undefined *"
      ]
    ],
    [
      "0063518c",
      "READ",
      [
        "storage",
        "00c1b570",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00635098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00634/00634d50.md#insn-00635098) · [`0063518c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00634/00634d50.md#insn-0063518c) · [`006351c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00634/00634d50.md#insn-006351c4)
- 新版 [`00635098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00634/00634d50.md#insn-00635098) · [`0063518c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00634/00634d50.md#insn-0063518c) · [`006351c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00634/00634d50.md#insn-006351c4)

~~~diff
- 00635098 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00635098 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00635098 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00635098 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00635098 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00635098 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00635098 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00635098 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00635098 bytes 4a413991
+ 00635098 bytes 4a813a91
- 0063518c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:520:8"]]
- 0063518c ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0063518c ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:570:8"]]
+ 0063518c ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 0063518c bytes 7b9342f9
+ 0063518c bytes 7bbb42f9
- 006351c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:528:8"]]
- 006351c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006351c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:578:8"]]
+ 006351c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006351c4 bytes 089542f9
+ 006351c4 bytes 08bd42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b34ac5e3d8e70708a90a7fcaca369512"></a>

### [`00635b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00635/00635b20.md) → [`00635b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00635/00635b20.md) FUN_00635b20

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00634d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00634/00634d50.md) [`0063935c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/0063935c.md) · 呼出先 32件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md)
- 新版 呼出元 2件 [`00634d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00634/00634d50.md) [`0063935c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/0063935c.md) · 呼出先 32件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 95.44% / 新版 95.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 4件, `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00635b88",
      "incomplete_value": false,
      "site": "00635b88",
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
            "const:dd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00635b88",
      "incomplete_value": false,
      "site": "00635b88",
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
            "const:d98:8"
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
      "definition_site": "00635b94",
      "incomplete_value": true,
      "site": "00635b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4058:8"
          ],
          [
            "leaf",
            "const:dd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00635b94",
      "incomplete_value": true,
      "site": "00635b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4058:8"
          ],
          [
            "leaf",
            "const:d90:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00635b9c",
      "incomplete_value": false,
      "site": "00635b9c",
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
            "const:dd4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00635b9c",
      "incomplete_value": false,
      "site": "00635b9c",
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
            "const:d94:8"
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00635b88",
      "WRITE",
      [
        "storage",
        "00c26d98",
        null,
        "undefined4"
      ]
    ],
    [
      "00635b94",
      "WRITE",
      [
        "storage",
        "00c26d90",
        null,
        "undefined1"
      ]
    ],
    [
      "00635b9c",
      "WRITE",
      [
        "storage",
        "00c26d94",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00635b88",
      "WRITE",
      [
        "storage",
        "00c26dd8",
        null,
        "undefined4"
      ]
    ],
    [
      "00635b94",
      "WRITE",
      [
        "storage",
        "00c26dd0",
        null,
        "undefined1"
      ]
    ],
    [
      "00635b9c",
      "WRITE",
      [
        "storage",
        "00c26dd4",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00635b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00635/00635b20.md#insn-00635b88) · [`00635b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00635/00635b20.md#insn-00635b94) · [`00635b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00635/00635b20.md#insn-00635b9c)
- 新版 [`00635b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00635/00635b20.md#insn-00635b88) · [`00635b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00635/00635b20.md#insn-00635b94) · [`00635b9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00635/00635b20.md#insn-00635b9c)

~~~diff
- 00635b88 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d98:8"]]
- 00635b88 ["COPY", "tmp:1:4", ["const:0:4"]]
- 00635b88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
+ 00635b88 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:dd8:8"]]
+ 00635b88 ["COPY", "tmp:1:4", ["const:0:4"]]
+ 00635b88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 00635b88 bytes 5f990db9
+ 00635b88 bytes 5fd90db9
- 00635b94 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00635b94 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00635b94 ["INT_ADD", "tmp:2:8", ["register:4058:8", "const:d90:8"]]
- 00635b94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00635b94 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00635b94 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00635b94 ["INT_ADD", "tmp:2:8", ["register:4058:8", "const:dd0:8"]]
+ 00635b94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00635b94 bytes 7f413639
+ 00635b94 bytes 7f413739
- 00635b9c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d94:8"]]
- 00635b9c ["COPY", "tmp:1:4", ["const:0:4"]]
- 00635b9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
+ 00635b9c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:dd4:8"]]
+ 00635b9c ["COPY", "tmp:1:4", ["const:0:4"]]
+ 00635b9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:4"]]
- 00635b9c bytes df960db9
+ 00635b9c bytes dfd60db9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ccdf091f4ae06db6fde0757d92c14685"></a>

### [`006369bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00636/006369bc.md) → [`006369bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00636/006369bc.md) FUN_006369bc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a82394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a82/00a82394.md) · 呼出先 31件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444bb0.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00444edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444edc.md)
- 新版 呼出元 1件 [`00a823d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a82/00a823d8.md) · 呼出先 31件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444bb0.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00444edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444edc.md)

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
      "definition_site": "00636edc",
      "incomplete_value": false,
      "site": "00636ee0",
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
      "definition_site": "00636edc",
      "incomplete_value": false,
      "site": "00636ee0",
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
    "ordinal": 50,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00636edc",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ],
    [
      "00636ef4",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ],
    [
      "006370cc",
      "READ",
      [
        "storage",
        "00c26d94",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00636edc",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00636ef4",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ],
    [
      "006370cc",
      "READ",
      [
        "storage",
        "00c26dd4",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00636ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00636/006369bc.md#insn-00636ed8) · [`006370cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00636/006369bc.md#insn-006370cc)
- 新版 [`00636ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00636/006369bc.md#insn-00636ed8) · [`006370cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00636/006369bc.md#insn-006370cc)

~~~diff
- 00636ed8 ["COPY", "tmp:0:8", ["const:d70:8"]]
- 00636ed8 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00636ed8 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00636ed8 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00636ed8 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 00636ed8 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00636ed8 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00636ed8 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00636ed8 bytes d6c23591
+ 00636ed8 bytes d6c23691
- 006370cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d94:8"]]
- 006370cc ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 006370cc ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
+ 006370cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd4:8"]]
+ 006370cc ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 006370cc ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
- 006370cc bytes 29954db9
+ 006370cc bytes 29d54db9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44e644e1fe33062be769f8c5e67adb94"></a>

### [`00637320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637320.md) → [`00637320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637320.md) FUN_00637320

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0062bf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0062b/0062bf80.md) · 呼出先 31件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444bb0.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00444edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444edc.md)
- 新版 呼出元 1件 [`0062bf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0062b/0062bf80.md) · 呼出先 31件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444bb0.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00444edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444edc.md)

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
      "definition_site": "00637840",
      "incomplete_value": false,
      "site": "00637844",
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
      "definition_site": "00637840",
      "incomplete_value": false,
      "site": "00637844",
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
    "ordinal": 50,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00637840",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ],
    [
      "00637858",
      "PARAM",
      [
        "storage",
        "00c24d70",
        null,
        "undefined8"
      ]
    ],
    [
      "00637a30",
      "READ",
      [
        "storage",
        "00c26d94",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00637840",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00637858",
      "PARAM",
      [
        "storage",
        "00c24db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00637a30",
      "READ",
      [
        "storage",
        "00c26dd4",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063783c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637320.md#insn-0063783c) · [`00637a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637320.md#insn-00637a30)
- 新版 [`0063783c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637320.md#insn-0063783c) · [`00637a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637320.md#insn-00637a30)

~~~diff
- 0063783c ["COPY", "tmp:0:8", ["const:d70:8"]]
- 0063783c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 0063783c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 0063783c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 0063783c ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0063783c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 0063783c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 0063783c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 0063783c bytes d6c23591
+ 0063783c bytes d6c23691
- 00637a30 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d94:8"]]
- 00637a30 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00637a30 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
+ 00637a30 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd4:8"]]
+ 00637a30 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00637a30 ["INT_ZEXT", "register:4048:8", ["tmp:1:4"]]
- 00637a30 bytes 29954db9
+ 00637a30 bytes 29d54db9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2be8611716cdf02d4476d6dedd3ee0c1"></a>

### [`00637c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637c84.md) → [`00637c84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637c84.md) FUN_00637c84

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
      "definition_site": "00637c90",
      "incomplete_value": false,
      "site": "00637c9c",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00637c90",
      "incomplete_value": false,
      "site": "00637c9c",
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
      "00637c9c",
      "DATA",
      [
        "storage",
        "00bf6cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00637c9c",
      "DATA",
      [
        "storage",
        "00bf6d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00637c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637c84.md#insn-00637c90)
- 新版 [`00637c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637c84.md#insn-00637c90)

~~~diff
- 00637c90 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00637c90 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00637c90 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00637c90 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00637c90 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00637c90 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00637c90 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00637c90 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00637c90 bytes 4a413391
+ 00637c90 bytes 4a813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2b9da5ac7ba82a8d83b2a1776651d7b"></a>

### [`00637cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637cc8.md) → [`00637cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637cc8.md) FUN_00637cc8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00637ce0",
      "incomplete_value": false,
      "site": "00637cec",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00637ce0",
      "incomplete_value": false,
      "site": "00637cec",
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
      "00637cec",
      "DATA",
      [
        "storage",
        "00bf6cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00637cec",
      "DATA",
      [
        "storage",
        "00bf6d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00637ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637cc8.md#insn-00637ce0)
- 新版 [`00637ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637cc8.md#insn-00637ce0)

~~~diff
- 00637ce0 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00637ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00637ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00637ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00637ce0 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00637ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00637ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00637ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00637ce0 bytes 08413391
+ 00637ce0 bytes 08813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-125a261e67d983e81560186530529a97"></a>

### [`00637d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637d24.md) → [`00637d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637d24.md) FUN_00637d24

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00637d4c",
      "incomplete_value": false,
      "site": "00637d50",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00637d4c",
      "incomplete_value": false,
      "site": "00637d50",
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
            "const:cd0:8"
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
      "00637d50",
      "DATA",
      [
        "storage",
        "00bf6cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00637d50",
      "DATA",
      [
        "storage",
        "00bf6d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00637d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637d24.md#insn-00637d4c)
- 新版 [`00637d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637d24.md#insn-00637d4c)

~~~diff
- 00637d4c ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00637d4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00637d4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00637d4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00637d4c ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00637d4c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00637d4c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00637d4c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00637d4c bytes 29413391
+ 00637d4c bytes 29813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee69264fd261fc60ace3af31cf75d4b8"></a>

### [`00637db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637db4.md) → [`00637db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637db4.md) FUN_00637db4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00637dd0",
      "incomplete_value": false,
      "site": "00637dd4",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00637dd0",
      "incomplete_value": false,
      "site": "00637dd4",
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
      "00637dd4",
      "DATA",
      [
        "storage",
        "00bf6cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00637dd4",
      "DATA",
      [
        "storage",
        "00bf6d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00637dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637db4.md#insn-00637dd0)
- 新版 [`00637dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637db4.md#insn-00637dd0)

~~~diff
- 00637dd0 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00637dd0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00637dd0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00637dd0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00637dd0 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 00637dd0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00637dd0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00637dd0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00637dd0 bytes 4a413391
+ 00637dd0 bytes 4a813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79179cc84ae39ab570e8ca4c66b021c0"></a>

### [`00637f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637f98.md) → [`00637f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637f98.md) FUN_00637f98

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
      "definition_site": "00637f9c",
      "incomplete_value": false,
      "site": "00637fa0",
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
            "const:da0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00637f9c",
      "incomplete_value": false,
      "site": "00637fa0",
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
      "00637fa0",
      "DATA",
      [
        "storage",
        "00bf6d50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00637fa0",
      "DATA",
      [
        "storage",
        "00bf6da0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00637f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00637/00637f98.md#insn-00637f9c)
- 新版 [`00637f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00637/00637f98.md#insn-00637f9c)

~~~diff
- 00637f9c ["COPY", "tmp:0:8", ["const:d50:8"]]
- 00637f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00637f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00637f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00637f9c ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00637f9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00637f9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00637f9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00637f9c bytes 08413591
+ 00637f9c bytes 08813691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02a15f64a50071c93415f11c99953a60"></a>

### [`00638060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638060.md) → [`00638060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638060.md) FUN_00638060

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`006330dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00633/006330dc.md) [`00633eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00633/00633eb0.md) [`00634d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00634/00634d50.md) [`00635b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00635/00635b20.md) [`00638060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638060.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 8件 [`006330dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/006330dc.md) [`00633eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00633/00633eb0.md) [`00634d50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00634/00634d50.md) [`00635b20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00635/00635b20.md) [`00638060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638060.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

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
      "definition_site": "006381b0",
      "incomplete_value": false,
      "site": "006381b8",
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
      "definition_site": "006381b0",
      "incomplete_value": false,
      "site": "006381b8",
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
      "definition_site": "006381d4",
      "incomplete_value": false,
      "site": "006381e0",
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
      "definition_site": "006381d4",
      "incomplete_value": false,
      "site": "006381e0",
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
      "definition_site": "00638308",
      "incomplete_value": false,
      "site": "00638310",
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
      "definition_site": "00638308",
      "incomplete_value": false,
      "site": "00638310",
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
      "006381b0",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "006381d4",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "00638308",
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
      "006381b0",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "006381d4",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "00638308",
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

- 旧版 [`006381b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638060.md#insn-006381b0) · [`006381d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638060.md#insn-006381d4) · [`00638308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638060.md#insn-00638308)
- 新版 [`006381b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638060.md#insn-006381b0) · [`006381d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638060.md#insn-006381d4) · [`00638308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638060.md#insn-00638308)

~~~diff
- 006381b0 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 006381b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006381b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006381b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006381b0 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 006381b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006381b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006381b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006381b0 bytes 21280c91
+ 006381b0 bytes 21900e91
- 006381d4 ["COPY", "tmp:0:8", ["const:919:8"]]
- 006381d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006381d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006381d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006381d4 ["COPY", "tmp:0:8", ["const:885:8"]]
+ 006381d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006381d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006381d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006381d4 bytes 21642491
+ 006381d4 bytes 21142291
- 00638308 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 00638308 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00638308 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00638308 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00638308 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 00638308 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00638308 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00638308 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00638308 bytes 21b80b91
+ 00638308 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef9eb252c397236e63c724c4cb3a680c"></a>

### [`00638850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638850.md) → [`00638850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638850.md) FUN_00638850

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00638874",
      "incomplete_value": false,
      "site": "00638878",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00638874",
      "incomplete_value": false,
      "site": "00638878",
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
      "00638878",
      "DATA",
      [
        "storage",
        "00bf6dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00638878",
      "DATA",
      [
        "storage",
        "00bf6e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00638874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638850.md#insn-00638874)
- 新版 [`00638874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638850.md#insn-00638874)

~~~diff
- 00638874 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 00638874 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00638874 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00638874 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00638874 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 00638874 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00638874 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00638874 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00638874 bytes 08413791
+ 00638874 bytes 08813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c37bf7638291d1daf096d41bc01fb9d"></a>

### [`00638890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638890.md) → [`00638890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638890.md) FUN_00638890

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
      "definition_site": "00638894",
      "incomplete_value": false,
      "site": "00638898",
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
            "const:e20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00638894",
      "incomplete_value": false,
      "site": "00638898",
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
      "00638898",
      "DATA",
      [
        "storage",
        "00bf6dd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00638898",
      "DATA",
      [
        "storage",
        "00bf6e20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00638894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638890.md#insn-00638894)
- 新版 [`00638894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638890.md#insn-00638894)

~~~diff
- 00638894 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 00638894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00638894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00638894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00638894 ["COPY", "tmp:0:8", ["const:e20:8"]]
+ 00638894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00638894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00638894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00638894 bytes 08413791
+ 00638894 bytes 08813891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73287ffb23305c4414e8cd05c799f9ef"></a>

### [`0063898c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/0063898c.md) → [`0063898c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/0063898c.md) FUN_0063898c

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
      "definition_site": "00638998",
      "incomplete_value": false,
      "site": "006389a4",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00638998",
      "incomplete_value": false,
      "site": "006389a4",
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
      "006389a4",
      "DATA",
      [
        "storage",
        "00bf6e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006389a4",
      "DATA",
      [
        "storage",
        "00bf6ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00638998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/0063898c.md#insn-00638998)
- 新版 [`00638998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/0063898c.md#insn-00638998)

~~~diff
- 00638998 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00638998 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00638998 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00638998 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00638998 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00638998 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00638998 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00638998 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00638998 bytes 4a413991
+ 00638998 bytes 4a813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72cd48e65c8427126f507cb13df237b2"></a>

### [`006389d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/006389d0.md) → [`006389d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/006389d0.md) FUN_006389d0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "006389e8",
      "incomplete_value": false,
      "site": "006389f4",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006389e8",
      "incomplete_value": false,
      "site": "006389f4",
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
            "const:e50:8"
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
      "006389f4",
      "DATA",
      [
        "storage",
        "00bf6e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006389f4",
      "DATA",
      [
        "storage",
        "00bf6ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006389e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/006389d0.md#insn-006389e8)
- 新版 [`006389e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/006389d0.md#insn-006389e8)

~~~diff
- 006389e8 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 006389e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006389e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006389e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006389e8 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 006389e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006389e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006389e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006389e8 bytes 08413991
+ 006389e8 bytes 08813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b39480b9779098004ec60b351679d5b"></a>

### [`00638a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638a2c.md) → [`00638a2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638a2c.md) FUN_00638a2c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00638a54",
      "incomplete_value": false,
      "site": "00638a58",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00638a54",
      "incomplete_value": false,
      "site": "00638a58",
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
            "const:e50:8"
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
      "00638a58",
      "DATA",
      [
        "storage",
        "00bf6e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00638a58",
      "DATA",
      [
        "storage",
        "00bf6ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00638a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638a2c.md#insn-00638a54)
- 新版 [`00638a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638a2c.md#insn-00638a54)

~~~diff
- 00638a54 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00638a54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00638a54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00638a54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00638a54 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00638a54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00638a54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00638a54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00638a54 bytes 29413991
+ 00638a54 bytes 29813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af303ede871b348928dff14b939ee885"></a>

### [`00638abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638abc.md) → [`00638abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638abc.md) FUN_00638abc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00638ad8",
      "incomplete_value": false,
      "site": "00638adc",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00638ad8",
      "incomplete_value": false,
      "site": "00638adc",
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
            "const:e50:8"
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
      "00638adc",
      "DATA",
      [
        "storage",
        "00bf6e50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00638adc",
      "DATA",
      [
        "storage",
        "00bf6ea0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00638ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638abc.md#insn-00638ad8)
- 新版 [`00638ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638abc.md#insn-00638ad8)

~~~diff
- 00638ad8 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00638ad8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00638ad8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00638ad8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00638ad8 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00638ad8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00638ad8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00638ad8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00638ad8 bytes 4a413991
+ 00638ad8 bytes 4a813a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86320812af3123f1180a704fe42b7613"></a>

### [`00638c7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638c7c.md) → [`00638c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638c7c.md) FUN_00638c7c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00638c90",
      "incomplete_value": false,
      "site": "00638c94",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00638c90",
      "incomplete_value": false,
      "site": "00638c94",
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
            "const:ed0:8"
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
      "00638c94",
      "DATA",
      [
        "storage",
        "00bf6ed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00638c94",
      "DATA",
      [
        "storage",
        "00bf6f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00638c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638c7c.md#insn-00638c90)
- 新版 [`00638c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638c7c.md#insn-00638c90)

~~~diff
- 00638c90 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 00638c90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00638c90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00638c90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00638c90 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00638c90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00638c90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00638c90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00638c90 bytes 08413b91
+ 00638c90 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad10e1b4c659701892bf07068e6f209d"></a>

### [`00638ca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638ca0.md) → [`00638ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638ca0.md) FUN_00638ca0

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
      "definition_site": "00638ca4",
      "incomplete_value": false,
      "site": "00638ca8",
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
            "const:f20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00638ca4",
      "incomplete_value": false,
      "site": "00638ca8",
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
      "00638ca8",
      "DATA",
      [
        "storage",
        "00bf6ed0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00638ca8",
      "DATA",
      [
        "storage",
        "00bf6f20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00638ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638ca0.md#insn-00638ca4)
- 新版 [`00638ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638ca0.md#insn-00638ca4)

~~~diff
- 00638ca4 ["COPY", "tmp:0:8", ["const:ed0:8"]]
- 00638ca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00638ca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00638ca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00638ca4 ["COPY", "tmp:0:8", ["const:f20:8"]]
+ 00638ca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00638ca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00638ca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00638ca4 bytes 08413b91
+ 00638ca4 bytes 08813c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8876e1227c89f967de674f8705804617"></a>

### [`00638d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638d6c.md) → [`00638d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638d6c.md) FUN_00638d6c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00638d90",
      "incomplete_value": false,
      "site": "00638d94",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00638d90",
      "incomplete_value": false,
      "site": "00638d94",
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
            "const:f50:8"
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
      "00638d94",
      "DATA",
      [
        "storage",
        "00bf6f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00638d94",
      "DATA",
      [
        "storage",
        "00bf6fa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00638d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638d6c.md#insn-00638d90)
- 新版 [`00638d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638d6c.md#insn-00638d90)

~~~diff
- 00638d90 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 00638d90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00638d90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00638d90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00638d90 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 00638d90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00638d90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00638d90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00638d90 bytes 08413d91
+ 00638d90 bytes 08813e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a2c79f412b0202f8cd12e0305325499"></a>

### [`00638dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638dac.md) → [`00638dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638dac.md) FUN_00638dac

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
      "definition_site": "00638db0",
      "incomplete_value": false,
      "site": "00638db4",
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
            "const:fa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00638db0",
      "incomplete_value": false,
      "site": "00638db4",
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
      "00638db4",
      "DATA",
      [
        "storage",
        "00bf6f50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00638db4",
      "DATA",
      [
        "storage",
        "00bf6fa0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00638db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638dac.md#insn-00638db0)
- 新版 [`00638db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638dac.md#insn-00638db0)

~~~diff
- 00638db0 ["COPY", "tmp:0:8", ["const:f50:8"]]
- 00638db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00638db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00638db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00638db0 ["COPY", "tmp:0:8", ["const:fa0:8"]]
+ 00638db0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00638db0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00638db0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00638db0 bytes 08413d91
+ 00638db0 bytes 08813e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecfe2385ff03f9ba32fc89f0f62da271"></a>

### [`00638e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638e0c.md) → [`00638e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638e0c.md) FUN_00638e0c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00638dd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638dd4.md) · 呼出先 15件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00632964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/00632964.md)
- 新版 呼出元 1件 [`00638dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638dd4.md) · 呼出先 15件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00632964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/00632964.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 82.33% / 新版 82.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 14件, `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00638f90",
      "incomplete_value": true,
      "site": "00638fa0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:836:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00638f90",
      "incomplete_value": true,
      "site": "00638fa0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7ab:8"
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
      "definition_site": "00638f94",
      "incomplete_value": true,
      "site": "00638fa4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00638f94",
      "incomplete_value": true,
      "site": "00638fa4",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00638fec",
      "incomplete_value": true,
      "site": "00638ffc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dd5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00638fec",
      "incomplete_value": true,
      "site": "00638ffc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e62:8"
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
      "00638efc",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00638f90",
      "READ",
      [
        "storage",
        "002a17ab",
        null,
        "string"
      ]
    ],
    [
      "00638f94",
      "READ",
      [
        "storage",
        "002a17b9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00638efc",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00638f90",
      "READ",
      [
        "storage",
        "002a1836",
        null,
        "string"
      ]
    ],
    [
      "00638f94",
      "READ",
      [
        "storage",
        "002a1844",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00638ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638e0c.md#insn-00638ef0) · [`00638f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638e0c.md#insn-00638f88) · [`00638f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00638/00638e0c.md#insn-00638f8c)
- 新版 [`00638ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638e0c.md#insn-00638ef0) · [`00638f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00638/00638e0c.md#insn-00638f88)

~~~diff
- 00638ef0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00638ef0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00638ef0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00638ef0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00638ef0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00638ef0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00638ef0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00638ef0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00638ef0 bytes 08e10091
+ 00638ef0 bytes 08e10191
- 00638f88 ["COPY", "tmp:0:8", ["const:7ab:8"]]
- 00638f88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00638f88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00638f88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00638f88 ["COPY", "tmp:0:8", ["const:836:8"]]
+ 00638f88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00638f88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00638f88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00638f88 bytes 08ad1e91
+ 00638f88 bytes 08d92091
- 00638f8c ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00638f8c bytes c9e3ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e3316b5f76665b949546ad7bc679b7c"></a>

### [`006392c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/006392c4.md) → [`006392c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/006392c4.md) FUN_006392c4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "006392e8",
      "incomplete_value": false,
      "site": "006392ec",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006392e8",
      "incomplete_value": false,
      "site": "006392ec",
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
      "006392ec",
      "DATA",
      [
        "storage",
        "00bf6fd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "006392ec",
      "DATA",
      [
        "storage",
        "00bf7020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006392e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/006392c4.md#insn-006392e4) · [`006392e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/006392c4.md#insn-006392e8)
- 新版 [`006392e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/006392c4.md#insn-006392e4) · [`006392e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/006392c4.md#insn-006392e8)

~~~diff
- 006392e4 ["COPY", "register:4040:8", ["const:bf6000:8"]]
+ 006392e4 ["COPY", "register:4040:8", ["const:bf7000:8"]]
- 006392e4 bytes e82d00b0
+ 006392e4 bytes e82d00d0
- 006392e8 ["COPY", "tmp:0:8", ["const:fd0:8"]]
- 006392e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006392e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006392e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006392e8 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 006392e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006392e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006392e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006392e8 bytes 08413f91
+ 006392e8 bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58c5fb7d087863a21ddf9b692dbc1a48"></a>

### [`00639304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/00639304.md) → [`00639304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/00639304.md) FUN_00639304

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
      "definition_site": "00639308",
      "incomplete_value": false,
      "site": "0063930c",
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
            "const:20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00639308",
      "incomplete_value": false,
      "site": "0063930c",
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
      "0063930c",
      "DATA",
      [
        "storage",
        "00bf6fd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0063930c",
      "DATA",
      [
        "storage",
        "00bf7020",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/00639304.md#insn-00639304) · [`00639308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/00639304.md#insn-00639308)
- 新版 [`00639304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/00639304.md#insn-00639304) · [`00639308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/00639304.md#insn-00639308)

~~~diff
- 00639304 ["COPY", "register:4040:8", ["const:bf6000:8"]]
+ 00639304 ["COPY", "register:4040:8", ["const:bf7000:8"]]
- 00639304 bytes e82d00b0
+ 00639304 bytes e82d00d0
- 00639308 ["COPY", "tmp:0:8", ["const:fd0:8"]]
- 00639308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00639308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00639308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00639308 ["COPY", "tmp:0:8", ["const:20:8"]]
+ 00639308 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00639308 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00639308 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00639308 bytes 08413f91
+ 00639308 bytes 08810091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4e1fbcea742d32220a49fdceba6a9e5"></a>

### [`00639404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/00639404.md) → [`00639404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/00639404.md) FUN_00639404

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00639428",
      "incomplete_value": false,
      "site": "0063942c",
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
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00639428",
      "incomplete_value": false,
      "site": "0063942c",
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
            "const:50:8"
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
      "0063942c",
      "DATA",
      [
        "storage",
        "00bf7050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0063942c",
      "DATA",
      [
        "storage",
        "00bf70a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/00639404.md#insn-00639428)
- 新版 [`00639428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/00639404.md#insn-00639428)

~~~diff
- 00639428 ["COPY", "tmp:0:8", ["const:50:8"]]
- 00639428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00639428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00639428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00639428 ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 00639428 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00639428 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00639428 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00639428 bytes 08410191
+ 00639428 bytes 08810291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7cf2c800057fb2d527c2c539439e460"></a>

### [`00639444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/00639444.md) → [`00639444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/00639444.md) FUN_00639444

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
      "definition_site": "00639448",
      "incomplete_value": false,
      "site": "0063944c",
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
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00639448",
      "incomplete_value": false,
      "site": "0063944c",
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
            "const:50:8"
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
      "0063944c",
      "DATA",
      [
        "storage",
        "00bf7050",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0063944c",
      "DATA",
      [
        "storage",
        "00bf70a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/00639444.md#insn-00639448)
- 新版 [`00639448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/00639444.md#insn-00639448)

~~~diff
- 00639448 ["COPY", "tmp:0:8", ["const:50:8"]]
- 00639448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00639448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00639448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00639448 ["COPY", "tmp:0:8", ["const:a0:8"]]
+ 00639448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00639448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00639448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00639448 bytes 08410191
+ 00639448 bytes 08810291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4d498d4194f9070714e2ee7d2e213e2"></a>

### [`006394a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/006394a4.md) → [`006394a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/006394a4.md) FUN_006394a4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0063946c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/0063946c.md) · 呼出先 15件 [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00632964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00632/00632964.md)
- 新版 呼出元 1件 [`0063946c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/0063946c.md) · 呼出先 15件 [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00632964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00632/00632964.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 85.77% / 新版 85.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_destination` 7件, `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00639628",
      "incomplete_value": true,
      "site": "00639638",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:836:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00639628",
      "incomplete_value": true,
      "site": "00639638",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7ab:8"
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
      "definition_site": "0063962c",
      "incomplete_value": true,
      "site": "0063963c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0063962c",
      "incomplete_value": true,
      "site": "0063963c",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00639684",
      "incomplete_value": true,
      "site": "00639694",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:dd5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00639684",
      "incomplete_value": true,
      "site": "00639694",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e62:8"
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
      "00639594",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00639628",
      "READ",
      [
        "storage",
        "002a17ab",
        null,
        "string"
      ]
    ],
    [
      "0063962c",
      "READ",
      [
        "storage",
        "002a17b9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00639594",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00639628",
      "READ",
      [
        "storage",
        "002a1836",
        null,
        "string"
      ]
    ],
    [
      "0063962c",
      "READ",
      [
        "storage",
        "002a1844",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00639588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/006394a4.md#insn-00639588) · [`00639620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/006394a4.md#insn-00639620) · [`00639624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/006394a4.md#insn-00639624)
- 新版 [`00639588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/006394a4.md#insn-00639588) · [`00639620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/006394a4.md#insn-00639620)

~~~diff
- 00639588 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00639588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00639588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00639588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00639588 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00639588 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00639588 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00639588 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00639588 bytes 08e10091
+ 00639588 bytes 08e10191
- 00639620 ["COPY", "tmp:0:8", ["const:7ab:8"]]
- 00639620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00639620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00639620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00639620 ["COPY", "tmp:0:8", ["const:836:8"]]
+ 00639620 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00639620 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00639620 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00639620 bytes 08ad1e91
+ 00639620 bytes 08d92091
- 00639624 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00639624 bytes a9e3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c80eae5159fc3fa77138fd318aa252a9"></a>

### [`00639cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/00639cc0.md) → [`00639cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/00639cc0.md) _INIT_80

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
      "definition_site": "00639cfc",
      "incomplete_value": true,
      "site": "00639d18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00639cfc",
      "incomplete_value": true,
      "site": "00639d18",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00639d60",
      "incomplete_value": true,
      "site": "00639d78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00639d60",
      "incomplete_value": true,
      "site": "00639d78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00639d7c",
      "incomplete_value": true,
      "site": "00639d98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00639d7c",
      "incomplete_value": true,
      "site": "00639d98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00639cfc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00639d20",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00639d40",
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
      "00639cfc",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00639d20",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00639d40",
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

- 旧版 [`00639cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/00639cc0.md#insn-00639cec) · [`00639cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00639/00639cc0.md#insn-00639cf4)
- 新版 [`00639cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/00639cc0.md#insn-00639cec) · [`00639cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00639/00639cc0.md#insn-00639cf4)

~~~diff
- 00639cec ["COPY", "tmp:0:8", ["const:d78:8"]]
- 00639cec ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00639cec ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00639cec ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00639cec ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00639cec ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00639cec ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00639cec ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00639cec bytes 73e23591
+ 00639cec bytes 73e23691
- 00639cf4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00639cf4 bytes 69e3ffd0
+ 00639cf4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00639cf4 bytes 69e3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48f0790bf1c2075ea0e92188236c9b49"></a>

### [`0063a620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063a/0063a620.md) → [`0063a620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063a/0063a620.md) FUN_0063a620

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 19件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 98.43% / 新版 98.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0063a668",
      "incomplete_value": false,
      "site": "0063a674",
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
      "definition_site": "0063a668",
      "incomplete_value": false,
      "site": "0063a674",
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
      "definition_site": "0063ac2c",
      "incomplete_value": true,
      "site": "0063ac40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:855:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063ac2c",
      "incomplete_value": true,
      "site": "0063ac40",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:7ca:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 101,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0063ac44",
      "incomplete_value": true,
      "site": "0063ac44",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0063ac44",
      "incomplete_value": true,
      "site": "0063ac44",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 102,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0063a674",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0063abf4",
      "READ",
      [
        "storage",
        "002a262c",
        null,
        "string"
      ]
    ],
    [
      "0063abf8",
      "READ",
      [
        "storage",
        "002a263a",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0063a674",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0063abf4",
      "READ",
      [
        "storage",
        "002a26b7",
        null,
        "string"
      ]
    ],
    [
      "0063abf8",
      "READ",
      [
        "storage",
        "002a26c5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063ac7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063a/0063a620.md#insn-0063ac7c) · [`0063a668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063a/0063a620.md#insn-0063a668)
- 新版 [`0063ac7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063a/0063a620.md#insn-0063ac7c) · [`0063a668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063a/0063a620.md#insn-0063a668)

~~~diff
- 0063ac7c ["COPY", "tmp:0:4", ["const:0:4"]]
- 0063ac7c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0063ac7c ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:17:8"]]
- 0063ac7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0063ac7c bytes 1f5c0039
+ 0063ac7c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0063ac7c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0063ac7c ["INT_ADD", "tmp:2:8", ["register:4000:8", "const:17:8"]]
+ 0063ac7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0063ac7c bytes 1f5c0039
- 0063a668 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0063a668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0063a668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0063a668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0063a668 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0063a668 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0063a668 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0063a668 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0063a668 bytes 08a13491
+ 0063a668 bytes 08e13591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2bb554eeb4ecca28c89e178f6f768223"></a>

### [`0063c724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c724.md) → [`0063c724`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c724.md) FUN_0063c724

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0063a620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063a/0063a620.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0063a620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063a/0063a620.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0063c730",
      "incomplete_value": false,
      "site": "0063c734",
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
      "definition_site": "0063c730",
      "incomplete_value": false,
      "site": "0063c734",
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
      "0063c730",
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
      "0063c730",
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

- 旧版 [`0063c730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c724.md#insn-0063c730)
- 新版 [`0063c730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c724.md#insn-0063c730)

~~~diff
- 0063c730 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0063c730 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0063c730 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0063c730 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0063c730 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0063c730 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0063c730 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0063c730 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0063c730 bytes 000c0c91
+ 0063c730 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3cd804c3bca429dc2f6349635eeee385"></a>

### [`0063c738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c738.md) → [`0063c738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c738.md) FUN_0063c738

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0063a620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063a/0063a620.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0063a620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063a/0063a620.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0063c744",
      "incomplete_value": false,
      "site": "0063c748",
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
      "definition_site": "0063c744",
      "incomplete_value": false,
      "site": "0063c748",
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
      "0063c744",
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
      "0063c744",
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

- 旧版 [`0063c744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c738.md#insn-0063c744)
- 新版 [`0063c744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c738.md#insn-0063c744)

~~~diff
- 0063c744 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0063c744 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0063c744 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0063c744 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0063c744 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0063c744 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0063c744 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0063c744 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0063c744 bytes 000c0c91
+ 0063c744 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e6319501cfaaa0a0e331f1afd41953e"></a>

### [`0063c74c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c74c.md) → [`0063c74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c74c.md) _INIT_81

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.96% / 新版 90.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0063c808",
      "incomplete_value": true,
      "site": "0063c824",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0063c808",
      "incomplete_value": true,
      "site": "0063c824",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0063c974",
      "incomplete_value": false,
      "site": "0063c980",
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
            "const:de0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063c974",
      "incomplete_value": false,
      "site": "0063c980",
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
            "const:da0:8"
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
      "definition_site": "0063c97c",
      "incomplete_value": false,
      "site": "0063c980",
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
      "definition_site": "0063c97c",
      "incomplete_value": false,
      "site": "0063c980",
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
      "0063c788",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0063c7ac",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0063c7cc",
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
      "0063c788",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0063c7ac",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0063c7cc",
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

- 旧版 [`0063c778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c74c.md#insn-0063c778) · [`0063c780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063c74c.md#insn-0063c780)
- 新版 [`0063c778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c74c.md#insn-0063c778) · [`0063c780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063c74c.md#insn-0063c780)

~~~diff
- 0063c778 ["COPY", "tmp:0:8", ["const:da0:8"]]
- 0063c778 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0063c778 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0063c778 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0063c778 ["COPY", "tmp:0:8", ["const:de0:8"]]
+ 0063c778 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0063c778 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0063c778 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0063c778 bytes 73823691
+ 0063c778 bytes 73823791
- 0063c780 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0063c780 bytes 49e3fff0
+ 0063c780 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0063c780 bytes 49e3fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d58d4a960ee9a8d32e5ea922981e6037"></a>

### [`0063cadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063cadc.md) → [`0063cadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063cadc.md) FUN_0063cadc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 22件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0063cb20",
      "incomplete_value": false,
      "site": "0063cb2c",
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
      "definition_site": "0063cb20",
      "incomplete_value": false,
      "site": "0063cb2c",
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
      "definition_site": "0063cb48",
      "incomplete_value": true,
      "site": "0063cb60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:88d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063cb48",
      "incomplete_value": true,
      "site": "0063cb60",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:802:8"
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
      "definition_site": "0063d650",
      "incomplete_value": true,
      "site": "0063d654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0063d650",
      "incomplete_value": true,
      "site": "0063d654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 143,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0063cb2c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0063cb48",
      "READ",
      [
        "storage",
        "0029f802",
        null,
        "string"
      ]
    ],
    [
      "0063d61c",
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
      "0063cb2c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0063cb48",
      "READ",
      [
        "storage",
        "0029f88d",
        null,
        "string"
      ]
    ],
    [
      "0063d61c",
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

- 旧版 [`0063cb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063cadc.md#insn-0063cb20) · [`0063cb3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063cadc.md#insn-0063cb3c) · [`0063d61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063c/0063cadc.md#insn-0063d61c)
- 新版 [`0063cb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063cadc.md#insn-0063cb20) · [`0063cb3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063cadc.md#insn-0063cb3c) · [`0063d61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063c/0063cadc.md#insn-0063d61c)

~~~diff
- 0063cb20 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0063cb20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0063cb20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0063cb20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0063cb20 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0063cb20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0063cb20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0063cb20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0063cb20 bytes 08a13491
+ 0063cb20 bytes 08e13591
- 0063cb3c ["COPY", "tmp:0:8", ["const:802:8"]]
- 0063cb3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0063cb3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0063cb3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0063cb3c ["COPY", "tmp:0:8", ["const:88d:8"]]
+ 0063cb3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0063cb3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0063cb3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0063cb3c bytes 29092091
+ 0063cb3c bytes 29352291
- 0063d61c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 0063d61c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0063d61c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 0063d61c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0063d61c bytes 08b946f9
+ 0063d61c bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0c2407f2c27a280a0d6e65b5f23c301"></a>

### [`0063e104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e104.md) → [`0063e104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e104.md) FUN_0063e104

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0063df80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063d/0063df80.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0063df80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063d/0063df80.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0063e110",
      "incomplete_value": false,
      "site": "0063e114",
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
      "definition_site": "0063e110",
      "incomplete_value": false,
      "site": "0063e114",
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
      "0063e110",
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
      "0063e110",
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

- 旧版 [`0063e110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e104.md#insn-0063e110)
- 新版 [`0063e110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e104.md#insn-0063e110)

~~~diff
- 0063e110 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0063e110 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0063e110 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0063e110 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0063e110 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0063e110 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0063e110 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0063e110 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0063e110 bytes 000c0c91
+ 0063e110 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb4686bb1559703024b409858cb95457"></a>

### [`0063e118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e118.md) → [`0063e118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e118.md) _INIT_82

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.96% / 新版 90.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0063e1b8",
      "incomplete_value": true,
      "site": "0063e1d0",
      "value": [
        "LOAD",
        "16",
        [
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
      "definition_site": "0063e1b8",
      "incomplete_value": true,
      "site": "0063e1d0",
      "value": [
        "LOAD",
        "16",
        [
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
      "definition_site": "0063e340",
      "incomplete_value": true,
      "site": "0063e34c",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063e340",
      "incomplete_value": true,
      "site": "0063e34c",
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
            "const:db8:8"
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
      "definition_site": "0063e348",
      "incomplete_value": false,
      "site": "0063e34c",
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
      "definition_site": "0063e348",
      "incomplete_value": false,
      "site": "0063e34c",
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
      "0063e154",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0063e178",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0063e198",
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
      "0063e154",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0063e178",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0063e198",
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

- 旧版 [`0063e144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e118.md#insn-0063e144) · [`0063e14c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e118.md#insn-0063e14c)
- 新版 [`0063e144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e118.md#insn-0063e144) · [`0063e14c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e118.md#insn-0063e14c)

~~~diff
- 0063e144 ["COPY", "tmp:0:8", ["const:db8:8"]]
- 0063e144 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0063e144 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0063e144 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0063e144 ["COPY", "tmp:0:8", ["const:df8:8"]]
+ 0063e144 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0063e144 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0063e144 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0063e144 bytes 73e23691
+ 0063e144 bytes 73e23791
- 0063e14c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0063e14c bytes 49e3ffb0
+ 0063e14c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0063e14c bytes 49e3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f8ed28ecfc533dea78eb1bda684e3b7"></a>

### [`0063e6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e6d4.md) → [`0063e6d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e6d4.md) FUN_0063e6d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 9件 [`007283fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/007283fc.md) [`0081c6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081c/0081c6a0.md) [`008b9174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b9/008b9174.md) [`009121c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00912/009121c4.md) [`0092bc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092b/0092bc08.md) · 呼出先 2件 [`007f96d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007f9/007f96d8.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 9件 [`007283fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/007283fc.md) [`0081c6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081c/0081c6a0.md) [`008b9174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b9/008b9174.md) [`009121c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00912/009121c4.md) [`0092bc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0092b/0092bc08.md) · 呼出先 2件 [`007f96d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007f9/007f96d8.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "0063e71c",
      "incomplete_value": true,
      "site": "0063e71c",
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
            "const:fb4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063e71c",
      "incomplete_value": true,
      "site": "0063e71c",
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
    "ordinal": 6,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0063e71c",
      "WRITE",
      [
        "storage",
        "00c23f64",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "0063e71c",
      "WRITE",
      [
        "storage",
        "00c23fb4",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0063e71c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063e/0063e6d4.md#insn-0063e71c)
- 新版 [`0063e71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063e/0063e6d4.md#insn-0063e71c)

~~~diff
- 0063e71c ["COPY", "tmp:0:4", ["register:4098:4"]]
- 0063e71c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:f64:8"]]
- 0063e71c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 0063e71c ["COPY", "tmp:0:4", ["register:4098:4"]]
+ 0063e71c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:fb4:8"]]
+ 0063e71c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 0063e71c bytes 13913d39
+ 0063e71c bytes 13d13e39
~~~


<a id="compare-81c2c0bc0f2e1b8ea1c9dc2e797672a2"></a>

### [`0063fa4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063f/0063fa4c.md) → [`0063fa4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063fa4c.md) FUN_0063fa4c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 12件 [`00681138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00681/00681138.md) [`0079bdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0079b/0079bdf0.md) [`0089cc84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0089c/0089cc84.md) [`008b8260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b8/008b8260.md) [`008b9174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008b9/008b9174.md) · 呼出先 12件 [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 12件 [`00681138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00681/00681138.md) [`0079bdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0079b/0079bdf0.md) [`0089cc84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0089c/0089cc84.md) [`008b8260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b8/008b8260.md) [`008b9174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008b9/008b9174.md) · 呼出先 12件 [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.11% / 新版 88.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0063fb54",
      "incomplete_value": true,
      "site": "0063fb54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7cc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063fb54",
      "incomplete_value": true,
      "site": "0063fb54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:732:8"
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
      "definition_site": "0063fbb4",
      "incomplete_value": true,
      "site": "0063fbcc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:8e4:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0063fbb4",
      "incomplete_value": true,
      "site": "0063fbcc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:859:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0063fda4",
      "incomplete_value": false,
      "site": "0063fda4",
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
      "definition_site": "0063fda4",
      "incomplete_value": false,
      "site": "0063fda4",
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
    "ordinal": 35,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0063fafc",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0063fb44",
      "READ",
      [
        "storage",
        "002a7732",
        null,
        "string"
      ]
    ],
    [
      "0063fb60",
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
      "0063fafc",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0063fb44",
      "READ",
      [
        "storage",
        "002a77cc",
        null,
        "string"
      ]
    ],
    [
      "0063fb60",
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

- 旧版 [`0063fa84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063f/0063fa4c.md#insn-0063fa84) · [`0063fb3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063f/0063fa4c.md#insn-0063fb3c) · [`0063fb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063f/0063fa4c.md#insn-0063fb60)
- 新版 [`0063fa84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063fa4c.md#insn-0063fa84) · [`0063fb3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063fa4c.md#insn-0063fb3c) · [`0063fb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063fa4c.md#insn-0063fb60)

~~~diff
- 0063fa84 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0063fa84 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 0063fa84 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 0063fa84 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 0063fa84 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0063fa84 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 0063fa84 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 0063fa84 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 0063fa84 bytes 18e30091
+ 0063fa84 bytes 18e30191
- 0063fb3c ["COPY", "tmp:0:8", ["const:732:8"]]
- 0063fb3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0063fb3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0063fb3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0063fb3c ["COPY", "tmp:0:8", ["const:7cc:8"]]
+ 0063fb3c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0063fb3c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0063fb3c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0063fb3c bytes 29c91c91
+ 0063fb3c bytes 29311f91
- 0063fb60 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0063fb60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0063fb60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0063fb60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0063fb60 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 0063fb60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0063fb60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0063fb60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0063fb60 bytes 00000091
+ 0063fb60 bytes 00000191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8c94cd055f8eb35ead1722dccecaef2"></a>

### [`00640008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640008.md) → [`00640008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640008.md) FUN_00640008

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 7件 [`007ac760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ac/007ac760.md) [`008895f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00889/008895f4.md) [`00890c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00890/00890c70.md) [`008920f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00892/008920f8.md) [`008a75e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008a7/008a75e8.md) · 呼出先 12件 [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0060d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md)
- 新版 呼出元 7件 [`007ac760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007ac/007ac760.md) [`008895f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00889/008895f4.md) [`00890c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00890/00890c70.md) [`008920f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00892/008920f8.md) [`008a75e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008a7/008a75e8.md) · 呼出先 12件 [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.14% / 新版 84.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 14件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00640110",
      "incomplete_value": true,
      "site": "00640110",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7cc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00640110",
      "incomplete_value": true,
      "site": "00640110",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:732:8"
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
      "definition_site": "006401fc",
      "incomplete_value": true,
      "site": "006401fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7cc:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006401fc",
      "incomplete_value": true,
      "site": "006401fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:732:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00640300",
      "incomplete_value": false,
      "site": "00640300",
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
      "definition_site": "00640300",
      "incomplete_value": false,
      "site": "00640300",
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
      "006400b8",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00640100",
      "READ",
      [
        "storage",
        "002a7732",
        null,
        "string"
      ]
    ],
    [
      "0064011c",
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
      "006400b8",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00640100",
      "READ",
      [
        "storage",
        "002a77cc",
        null,
        "string"
      ]
    ],
    [
      "0064011c",
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

- 旧版 [`00640040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640008.md#insn-00640040) · [`006400f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640008.md#insn-006400f8) · [`0064011c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640008.md#insn-0064011c)
- 新版 [`00640040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640008.md#insn-00640040) · [`006400f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640008.md#insn-006400f8) · [`0064011c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640008.md#insn-0064011c)

~~~diff
- 00640040 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00640040 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 00640040 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 00640040 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 00640040 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00640040 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 00640040 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 00640040 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 00640040 bytes 18e30091
+ 00640040 bytes 18e30191
- 006400f8 ["COPY", "tmp:0:8", ["const:732:8"]]
- 006400f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006400f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006400f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006400f8 ["COPY", "tmp:0:8", ["const:7cc:8"]]
+ 006400f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006400f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006400f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006400f8 bytes 29c91c91
+ 006400f8 bytes 29311f91
- 0064011c ["COPY", "tmp:0:8", ["const:0:8"]]
- 0064011c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0064011c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0064011c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0064011c ["COPY", "tmp:0:8", ["const:40:8"]]
+ 0064011c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0064011c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0064011c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0064011c bytes 00000091
+ 0064011c bytes 00000191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee304a64663094ac73300c0a18a9ed53"></a>

### [`00640490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640490.md) → [`00640490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640490.md) FUN_00640490

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0092bc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0092b/0092bc08.md) [`0094efec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094e/0094efec.md) [`00a7888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a78/00a7888c.md) · 呼出先 12件 [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)
- 新版 呼出元 3件 [`0092bc08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0092b/0092bc08.md) [`0094efec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094e/0094efec.md) [`00a788d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a78/00a788d0.md) · 呼出先 12件 [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00459a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 85.78% / 新版 85.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_destination` 7件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00640550",
      "incomplete_value": true,
      "site": "00640560",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00640550",
      "incomplete_value": true,
      "site": "00640560",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d85:8"
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
      "definition_site": "00640594",
      "incomplete_value": true,
      "site": "00640594",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00640594",
      "incomplete_value": true,
      "site": "00640594",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c44:8"
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
      "definition_site": "00640604",
      "incomplete_value": true,
      "site": "00640604",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00640604",
      "incomplete_value": true,
      "site": "00640604",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:82b:8"
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
      "0064053c",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00640550",
      "READ",
      [
        "storage",
        "00296d85",
        null,
        "string"
      ]
    ],
    [
      "00640584",
      "READ",
      [
        "storage",
        "002aec44",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0064053c",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00640550",
      "READ",
      [
        "storage",
        "00296cf8",
        null,
        "string"
      ]
    ],
    [
      "00640584",
      "READ",
      [
        "storage",
        "002aebb0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006404c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640490.md#insn-006404c4) · [`00640548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640490.md#insn-00640548) · [`0064057c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640490.md#insn-0064057c)
- 新版 [`006404c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640490.md#insn-006404c4) · [`00640548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640490.md#insn-00640548) · [`0064057c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640490.md#insn-0064057c)

~~~diff
- 006404c4 ["COPY", "tmp:0:8", ["const:38:8"]]
- 006404c4 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 006404c4 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 006404c4 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 006404c4 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 006404c4 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 006404c4 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 006404c4 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 006404c4 bytes f7e20091
+ 006404c4 bytes f7e20191
- 00640548 ["COPY", "tmp:0:8", ["const:d85:8"]]
- 00640548 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00640548 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00640548 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00640548 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 00640548 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00640548 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00640548 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00640548 bytes 29153691
+ 00640548 bytes 29e13391
- 0064057c ["COPY", "tmp:0:8", ["const:c44:8"]]
- 0064057c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0064057c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0064057c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0064057c ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 0064057c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0064057c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0064057c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0064057c bytes 29113191
+ 0064057c bytes 29c12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60f0b087c577edc070292d738201a61d"></a>

### [`00640910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640910.md) → [`00640910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640910.md) FUN_00640910

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`0094d124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0094d/0094d124.md) [`00a71a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a71/00a71a9c.md) · 呼出先 12件 [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 2件 [`0094d124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0094d/0094d124.md) [`00a71ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a71/00a71ae0.md) · 呼出先 12件 [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00459a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 81.78% / 新版 81.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_destination` 14件, `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006409d0",
      "incomplete_value": true,
      "site": "006409e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006409d0",
      "incomplete_value": true,
      "site": "006409e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:d85:8"
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
      "definition_site": "00640a14",
      "incomplete_value": true,
      "site": "00640a14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00640a14",
      "incomplete_value": true,
      "site": "00640a14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c44:8"
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
      "definition_site": "00640afc",
      "incomplete_value": true,
      "site": "00640afc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bb0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00640afc",
      "incomplete_value": true,
      "site": "00640afc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c44:8"
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
      "006409bc",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006409d0",
      "READ",
      [
        "storage",
        "00296d85",
        null,
        "string"
      ]
    ],
    [
      "00640a04",
      "READ",
      [
        "storage",
        "002aec44",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006409bc",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "006409d0",
      "READ",
      [
        "storage",
        "00296cf8",
        null,
        "string"
      ]
    ],
    [
      "00640a04",
      "READ",
      [
        "storage",
        "002aebb0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00640944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640910.md#insn-00640944) · [`006409c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640910.md#insn-006409c8) · [`006409fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00640/00640910.md#insn-006409fc)
- 新版 [`00640944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640910.md#insn-00640944) · [`006409c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640910.md#insn-006409c8) · [`006409fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00640/00640910.md#insn-006409fc)

~~~diff
- 00640944 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00640944 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 00640944 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 00640944 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 00640944 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00640944 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 00640944 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00640944 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00640944 bytes f7e20091
+ 00640944 bytes f7e20191
- 006409c8 ["COPY", "tmp:0:8", ["const:d85:8"]]
- 006409c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006409c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006409c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006409c8 ["COPY", "tmp:0:8", ["const:cf8:8"]]
+ 006409c8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006409c8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006409c8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006409c8 bytes 29153691
+ 006409c8 bytes 29e13391
- 006409fc ["COPY", "tmp:0:8", ["const:c44:8"]]
- 006409fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 006409fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 006409fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 006409fc ["COPY", "tmp:0:8", ["const:bb0:8"]]
+ 006409fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 006409fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 006409fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 006409fc bytes 29113191
+ 006409fc bytes 29c12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46c3f1629778d634e3cf2f237e638139"></a>

### [`0064104c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00641/0064104c.md) → [`0064104c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/0064104c.md) FUN_0064104c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 7件 [`006b15e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006b1/006b15e4.md) [`008d0760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d0/008d0760.md) [`008d76b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/008d7/008d76b0.md) [`00a11cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a11/00a11cc0.md) [`00a15464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a15/00a15464.md) · 呼出先 6件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 7件 [`006b15e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b15e4.md) [`008d0760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d0/008d0760.md) [`008d76b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/008d7/008d76b0.md) [`00a11d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a11/00a11d04.md) [`00a154a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a15/00a154a8.md) · 呼出先 6件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00459a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.41% / 新版 97.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00641134",
      "incomplete_value": true,
      "site": "0064114c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b24:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00641134",
      "incomplete_value": true,
      "site": "0064114c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:bb1:8"
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
      "00641134",
      "READ",
      [
        "storage",
        "00294bb1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00641134",
      "READ",
      [
        "storage",
        "00294b24",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00641128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00641/0064104c.md#insn-00641128)
- 新版 [`00641128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/0064104c.md#insn-00641128)

~~~diff
- 00641128 ["COPY", "tmp:0:8", ["const:bb1:8"]]
- 00641128 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00641128 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00641128 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00641128 ["COPY", "tmp:0:8", ["const:b24:8"]]
+ 00641128 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00641128 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00641128 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00641128 bytes 29c52e91
+ 00641128 bytes 29912c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-116eff4b35e804bfb63ef41b97b47e4d"></a>

### [`00641308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00641/00641308.md) → [`00641308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/00641308.md) FUN_00641308

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0063fed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0063f/0063fed4.md) [`00641308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00641/00641308.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f1ac.md)
- 新版 呼出元 2件 [`0063fed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0063f/0063fed4.md) [`00641308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/00641308.md) · 呼出先 22件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e430.md) [`0041f1ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f1ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.70% / 新版 98.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00641468",
      "incomplete_value": false,
      "site": "00641470",
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
      "definition_site": "00641468",
      "incomplete_value": false,
      "site": "00641470",
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
      "definition_site": "0064148c",
      "incomplete_value": false,
      "site": "00641498",
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
      "definition_site": "0064148c",
      "incomplete_value": false,
      "site": "00641498",
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
      "definition_site": "006415c0",
      "incomplete_value": false,
      "site": "006415c8",
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
      "definition_site": "006415c0",
      "incomplete_value": false,
      "site": "006415c8",
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
      "00641468",
      "PARAM",
      [
        "storage",
        "002a730a",
        null,
        null
      ]
    ],
    [
      "0064148c",
      "PARAM",
      [
        "storage",
        "002af919",
        null,
        "string"
      ]
    ],
    [
      "006415c0",
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
      "00641468",
      "PARAM",
      [
        "storage",
        "002a73a4",
        null,
        null
      ]
    ],
    [
      "0064148c",
      "PARAM",
      [
        "storage",
        "002af885",
        null,
        "string"
      ]
    ],
    [
      "006415c0",
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

- 旧版 [`00641468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00641/00641308.md#insn-00641468) · [`0064148c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00641/00641308.md#insn-0064148c) · [`006415c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00641/00641308.md#insn-006415c0)
- 新版 [`00641468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/00641308.md#insn-00641468) · [`0064148c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/00641308.md#insn-0064148c) · [`006415c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/00641308.md#insn-006415c0)

~~~diff
- 00641468 ["COPY", "tmp:0:8", ["const:30a:8"]]
- 00641468 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00641468 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00641468 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00641468 ["COPY", "tmp:0:8", ["const:3a4:8"]]
+ 00641468 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00641468 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00641468 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00641468 bytes 21280c91
+ 00641468 bytes 21900e91
- 0064148c ["COPY", "tmp:0:8", ["const:919:8"]]
- 0064148c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0064148c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0064148c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0064148c ["COPY", "tmp:0:8", ["const:885:8"]]
+ 0064148c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0064148c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0064148c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0064148c bytes 21642491
+ 0064148c bytes 21142291
- 006415c0 ["COPY", "tmp:0:8", ["const:2ee:8"]]
- 006415c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 006415c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 006415c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 006415c0 ["COPY", "tmp:0:8", ["const:379:8"]]
+ 006415c0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 006415c0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 006415c0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 006415c0 bytes 21b80b91
+ 006415c0 bytes 21e40d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b23885a3234db1a35b2d88c9f2aa1f72"></a>

### [`00641c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00641/00641c78.md) → [`00641c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/00641c78.md) _INIT_83

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
      "definition_site": "00641cb4",
      "incomplete_value": true,
      "site": "00641cd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00641cb4",
      "incomplete_value": true,
      "site": "00641cd0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00641cd8",
      "incomplete_value": true,
      "site": "00641cf4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00641cd8",
      "incomplete_value": true,
      "site": "00641cf4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00641d74",
      "incomplete_value": true,
      "site": "00641db8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "00641d74",
      "incomplete_value": true,
      "site": "00641db8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00641cb4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00641cd8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00641cf8",
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
      "00641cb4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00641cd8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00641cf8",
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

- 旧版 [`00641ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00641/00641c78.md#insn-00641ca4) · [`00641cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00641/00641c78.md#insn-00641cac)
- 新版 [`00641ca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/00641c78.md#insn-00641ca4) · [`00641cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00641/00641c78.md#insn-00641cac)

~~~diff
- 00641ca4 ["COPY", "tmp:0:8", ["const:dd0:8"]]
- 00641ca4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00641ca4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00641ca4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00641ca4 ["COPY", "tmp:0:8", ["const:e10:8"]]
+ 00641ca4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00641ca4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00641ca4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00641ca4 bytes 73423791
+ 00641ca4 bytes 73423891
- 00641cac ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00641cac bytes 29e3ffd0
+ 00641cac ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00641cac bytes 29e3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df507c98daf3194889646af14cd346ef"></a>

### [`0064214c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00642/0064214c.md) → [`0064214c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/0064214c.md) FUN_0064214c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00abf52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abf/00abf52c.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`004652a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/004652a0.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)
- 新版 呼出元 1件 [`00abf570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00abf/00abf570.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`004652a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/004652a0.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00642390",
      "incomplete_value": true,
      "site": "00642394",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00642390",
      "incomplete_value": true,
      "site": "00642394",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0064238c",
      "incomplete_value": true,
      "site": "00642398",
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
      "definition_site": "0064238c",
      "incomplete_value": true,
      "site": "00642398",
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
    "ordinal": 41,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "006423a4",
      "incomplete_value": true,
      "site": "006423a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:48:8"
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
      "definition_site": "006423a4",
      "incomplete_value": true,
      "site": "006423a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_ADD",
              [
                "leaf",
                "const:48:8"
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
    "ordinal": 42,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00642190",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "006421a8",
      "READ",
      [
        "storage",
        "002a6a36",
        null,
        "string"
      ]
    ],
    [
      "00642380",
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
      "00642190",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "006421a8",
      "READ",
      [
        "storage",
        "002a6ad0",
        null,
        "string"
      ]
    ],
    [
      "00642380",
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

- 旧版 [`00642188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00642/0064214c.md#insn-00642188) · [`006421a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00642/0064214c.md#insn-006421a4) · [`00642380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00642/0064214c.md#insn-00642380)
- 新版 [`00642188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/0064214c.md#insn-00642188) · [`006421a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/0064214c.md#insn-006421a4) · [`00642380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/0064214c.md#insn-00642380)

~~~diff
- 00642188 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00642188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00642188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00642188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00642188 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00642188 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00642188 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00642188 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00642188 bytes 08a13491
+ 00642188 bytes 08e13591
- 006421a4 ["COPY", "tmp:0:8", ["const:a36:8"]]
- 006421a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006421a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006421a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006421a4 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 006421a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006421a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006421a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006421a4 bytes 08d92891
+ 006421a4 bytes 08412b91
- 00642380 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 00642380 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00642380 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00642380 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00642380 bytes 08b946f9
+ 00642380 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6738d29fd8108c3d2cfd40b8d9848ad"></a>

### [`00642748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00642/00642748.md) → [`00642748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/00642748.md) _INIT_84

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
      "definition_site": "00642784",
      "incomplete_value": true,
      "site": "006427a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00642784",
      "incomplete_value": true,
      "site": "006427a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006427a8",
      "incomplete_value": true,
      "site": "006427c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006427a8",
      "incomplete_value": true,
      "site": "006427c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006427c8",
      "incomplete_value": true,
      "site": "006427e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006427c8",
      "incomplete_value": true,
      "site": "006427e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00642784",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006427a8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "006427c8",
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
      "00642784",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006427a8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "006427c8",
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

- 旧版 [`00642774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00642/00642748.md#insn-00642774) · [`0064277c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00642/00642748.md#insn-0064277c)
- 新版 [`00642774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/00642748.md#insn-00642774) · [`0064277c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/00642748.md#insn-0064277c)

~~~diff
- 00642774 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 00642774 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00642774 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00642774 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00642774 ["COPY", "tmp:0:8", ["const:e28:8"]]
+ 00642774 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00642774 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00642774 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00642774 bytes 73a23791
+ 00642774 bytes 73a23891
- 0064277c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0064277c bytes 29e3ffb0
+ 0064277c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0064277c bytes 29e3ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3377e59983bf0ffdeb85dd2e7b9ae709"></a>

### [`00642ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00642/00642ad8.md) → [`00642ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/00642ad8.md) FUN_00642ad8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 23件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 23件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.18% / 新版 97.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00642b1c",
      "incomplete_value": false,
      "site": "00642b28",
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
      "definition_site": "00642b1c",
      "incomplete_value": false,
      "site": "00642b28",
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
      "definition_site": "00642b60",
      "incomplete_value": true,
      "site": "00642b78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4b2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00642b60",
      "incomplete_value": true,
      "site": "00642b78",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:418:8"
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
      "definition_site": "006436b4",
      "incomplete_value": true,
      "site": "006436c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006436b4",
      "incomplete_value": true,
      "site": "006436c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e9:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 133,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00642b28",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00642b60",
      "READ",
      [
        "storage",
        "002a8418",
        null,
        "string"
      ]
    ],
    [
      "00642d8c",
      "READ",
      [
        "storage",
        "0029d664",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00642b28",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00642b60",
      "READ",
      [
        "storage",
        "002a84b2",
        null,
        "string"
      ]
    ],
    [
      "00642d8c",
      "READ",
      [
        "storage",
        "0029d6ef",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00642b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00642/00642ad8.md#insn-00642b1c) · [`00642b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00642/00642ad8.md#insn-00642b54) · [`00642d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00642/00642ad8.md#insn-00642d84)
- 新版 [`00642b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/00642ad8.md#insn-00642b1c) · [`00642b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/00642ad8.md#insn-00642b54) · [`00642d84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00642/00642ad8.md#insn-00642d84)

~~~diff
- 00642b1c ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00642b1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00642b1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00642b1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00642b1c ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00642b1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00642b1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00642b1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00642b1c bytes 08a13491
+ 00642b1c bytes 08e13591
- 00642b54 ["COPY", "tmp:0:8", ["const:418:8"]]
- 00642b54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00642b54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00642b54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00642b54 ["COPY", "tmp:0:8", ["const:4b2:8"]]
+ 00642b54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00642b54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00642b54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00642b54 bytes 29611091
+ 00642b54 bytes 29c91291
- 00642d84 ["COPY", "tmp:0:8", ["const:664:8"]]
- 00642d84 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00642d84 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00642d84 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00642d84 ["COPY", "tmp:0:8", ["const:6ef:8"]]
+ 00642d84 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00642d84 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00642d84 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00642d84 bytes 4a911991
+ 00642d84 bytes 4abd1b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd4aa7fd02f67d0be51d596ac05fec82"></a>

### [`006459ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00645/006459ac.md) → [`006459ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/006459ac.md) _INIT_85

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
      "definition_site": "006459e8",
      "incomplete_value": true,
      "site": "00645a04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006459e8",
      "incomplete_value": true,
      "site": "00645a04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00645a0c",
      "incomplete_value": true,
      "site": "00645a28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00645a0c",
      "incomplete_value": true,
      "site": "00645a28",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00645a2c",
      "incomplete_value": true,
      "site": "00645a48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00645a2c",
      "incomplete_value": true,
      "site": "00645a48",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "006459e8",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00645a0c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00645a2c",
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
      "006459e8",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00645a0c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00645a2c",
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

- 旧版 [`006459d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00645/006459ac.md#insn-006459d8) · [`006459e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00645/006459ac.md#insn-006459e0)
- 新版 [`006459d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/006459ac.md#insn-006459d8) · [`006459e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00645/006459ac.md#insn-006459e0)

~~~diff
- 006459d8 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 006459d8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006459d8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006459d8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006459d8 ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 006459d8 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006459d8 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006459d8 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006459d8 bytes 73023891
+ 006459d8 bytes 73023991
- 006459e0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006459e0 bytes 09e3ffd0
+ 006459e0 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006459e0 bytes 09e3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da407a74417d689e14d653435cbbe834"></a>

### [`00646df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646df0.md) → [`00646df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646df0.md) FUN_00646df0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00646de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646de4.md) · 呼出先 10件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00ad59a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad5/00ad59a4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00646de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646de4.md) · 呼出先 10件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00ad59e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad5/00ad59e8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00647024",
      "incomplete_value": false,
      "site": "0064702c",
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
    "old": {
      "definition_site": "00647024",
      "incomplete_value": false,
      "site": "0064702c",
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
      "00646e8c",
      "PARAM",
      [
        "storage",
        "00299b43",
        null,
        null
      ]
    ],
    [
      "00646e9c",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00646ea8",
      "PARAM",
      [
        "storage",
        "0029d68f",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00646e8c",
      "PARAM",
      [
        "storage",
        "00299ab6",
        null,
        null
      ]
    ],
    [
      "00646e9c",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00646ea8",
      "PARAM",
      [
        "storage",
        "0029d71a",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00646e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646df0.md#insn-00646e54) · [`00646e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00646/00646df0.md#insn-00646e58)
- 新版 [`00646e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646df0.md#insn-00646e54) · [`00646e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00646/00646df0.md#insn-00646e58)

~~~diff
- 00646e54 ["COPY", "tmp:0:8", ["const:394:8"]]
- 00646e54 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00646e54 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00646e54 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00646e54 ["COPY", "tmp:0:8", ["const:41f:8"]]
+ 00646e54 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00646e54 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00646e54 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00646e54 bytes d6520e91
+ 00646e54 bytes d67e1091
- 00646e58 ["COPY", "register:40b8:8", ["const:29d000:8"]]
- 00646e58 bytes b7e2fff0
+ 00646e58 ["COPY", "register:40b8:8", ["const:29d000:8"]]
+ 00646e58 bytes b7e2fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26ab41af8fd175b8b569a005d753381d"></a>

### [`00647388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00647/00647388.md) → [`00647388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00647/00647388.md) FUN_00647388

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00695904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00695/00695904.md) [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 38件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md)
- 新版 呼出元 2件 [`00695904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00695/00695904.md) [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 38件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.53% / 新版 92.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 26件, `store_destination` 25件, `store_value` 14件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006473d0",
      "incomplete_value": false,
      "site": "006473d0",
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
      "definition_site": "006473d0",
      "incomplete_value": false,
      "site": "006473d0",
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
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006473c8",
      "incomplete_value": true,
      "site": "006473d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "006473c8",
      "incomplete_value": true,
      "site": "006473d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 14,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006473d4",
      "incomplete_value": false,
      "site": "006473d4",
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
      "definition_site": "006473d4",
      "incomplete_value": false,
      "site": "006473d4",
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
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006473c8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "006473cc",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "006473d0",
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
      "006473c8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "006473cc",
      "READ",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "006473d0",
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

- 旧版 [`006473d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00647/00647388.md#insn-006473d0) · [`006473d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00647/00647388.md#insn-006473d4) · [`00647424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00647/00647388.md#insn-00647424)
- 新版 [`006473d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00647/00647388.md#insn-006473d0) · [`006473d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00647/00647388.md#insn-006473d4) · [`00647424`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00647/00647388.md#insn-00647424)

~~~diff
- 006473d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 006473d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 006473d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 006473d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 006473d0 bytes 093505f9
+ 006473d0 bytes 095505f9
- 006473d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a78:8"]]
- 006473d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 006473d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
+ 006473d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 006473d4 bytes 6a3e05f9
+ 006473d4 bytes 6a5e05f9
- 00647424 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a78:8"]]
- 00647424 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00647424 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ab8:8"]]
+ 00647424 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00647424 bytes 743e05f9
+ 00647424 bytes 745e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2ca7934e6bec52b7af448f400e3f30d"></a>

### [`00648630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00648/00648630.md) → [`00648630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00648/00648630.md) FUN_00648630

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00647388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00647/00647388.md) · 呼出先 24件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044b898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b898.md) [`0044b8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a0.md) [`0044b8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md)
- 新版 呼出元 1件 [`00647388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00647/00647388.md) · 呼出先 24件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044b898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b898.md) [`0044b8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a0.md) [`0044b8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044b8a8.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 88.90% / 新版 88.90%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 22件, `store_destination` 21件, `store_value` 15件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064870c",
      "incomplete_value": true,
      "site": "00648728",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:688:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064870c",
      "incomplete_value": true,
      "site": "00648728",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5fd:8"
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
      "definition_site": "00648844",
      "incomplete_value": true,
      "site": "00648858",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:44f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00648844",
      "incomplete_value": true,
      "site": "00648858",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3b5:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00648884",
      "incomplete_value": true,
      "site": "00648894",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:464:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00648884",
      "incomplete_value": true,
      "site": "00648894",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3ca:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00648660",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00648670",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00648678",
      "PARAM",
      [
        "storage",
        "00bf70c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00648660",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00648670",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00648678",
      "PARAM",
      [
        "storage",
        "00bf7110",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00648660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00648/00648630.md#insn-00648660) · [`00648670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00648/00648630.md#insn-00648670) · [`00648678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00648/00648630.md#insn-00648678)
- 新版 [`00648660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00648/00648630.md#insn-00648660) · [`00648670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00648/00648630.md#insn-00648670) · [`00648678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00648/00648630.md#insn-00648678)

~~~diff
- 00648660 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00648660 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00648660 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00648660 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00648660 bytes 083d45f9
+ 00648660 bytes 085d45f9
- 00648670 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00648670 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00648670 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00648670 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00648670 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00648670 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00648670 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00648670 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00648670 bytes 21203991
+ 00648670 bytes 21603a91
- 00648678 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 00648678 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00648678 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00648678 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00648678 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 00648678 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00648678 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00648678 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00648678 bytes 42000391
+ 00648678 bytes 42400491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7dbb3b921f0ce149e8f12441c6b5f11b"></a>

### [`00649518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00649/00649518.md) → [`00649518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00649/00649518.md) FUN_00649518

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00647388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00647/00647388.md) [`00649c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00649/00649c54.md) · 呼出先 15件 [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046ff30.md) [`004752f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00475/004752f8.md)
- 新版 呼出元 2件 [`00647388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00647/00647388.md) [`00649c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00649/00649c54.md) · 呼出先 15件 [`00459a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046ff30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046ff30.md) [`004752f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00475/004752f8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "006495bc",
      "incomplete_value": false,
      "site": "006495bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006495bc",
      "incomplete_value": false,
      "site": "006495bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c23000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00649790",
      "incomplete_value": true,
      "site": "006497a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b13:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00649790",
      "incomplete_value": true,
      "site": "006497a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ba7:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00649558",
      "incomplete_value": true,
      "site": "00649558",
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
      "definition_site": "00649558",
      "incomplete_value": true,
      "site": "00649558",
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
      "00649554",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00649560",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00649568",
      "PARAM",
      [
        "storage",
        "00bf70c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00649554",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00649560",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00649568",
      "PARAM",
      [
        "storage",
        "00bf7110",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006495bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00649/00649518.md#insn-006495bc) · [`00649554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00649/00649518.md#insn-00649554) · [`00649560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00649/00649518.md#insn-00649560)
- 新版 [`006495bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00649/00649518.md#insn-006495bc) · [`00649554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00649/00649518.md#insn-00649554) · [`00649560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00649/00649518.md#insn-00649560)

~~~diff
- 006495bc ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:f68:8"]]
- 006495bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
+ 006495bc ["INT_ADD", "tmp:0:8", ["register:4060:8", "const:fb8:8"]]
+ 006495bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4058:4"]]
- 006495bc bytes 8b690fb9
+ 006495bc bytes 8bb90fb9
- 00649554 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00649554 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00649554 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00649554 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00649554 bytes 083d45f9
+ 00649554 bytes 085d45f9
- 00649560 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00649560 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00649560 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00649560 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00649560 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00649560 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00649560 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00649560 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00649560 bytes 21203991
+ 00649560 bytes 21603a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ba5e2512635f5bf2c05bf6aeff55680"></a>

### [`00649c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00649/00649c54.md) → [`00649c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00649/00649c54.md) FUN_00649c54

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 20件 [`0044beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044beb4.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`00649518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00649/00649518.md) [`0064caa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064caa0.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 20件 [`0044beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`00649518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00649/00649518.md) [`0064caa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064caa0.md)

変更の種類 comparison, comparison_count, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.89% / 新版 98.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00649d78",
      "incomplete_value": false,
      "site": "00649d84",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00649d78",
      "incomplete_value": false,
      "site": "00649d84",
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
            "const:128:8"
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
      "definition_site": "00649ee8",
      "incomplete_value": false,
      "site": "00649ef0",
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
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00649ee8",
      "incomplete_value": false,
      "site": "00649ef0",
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
            "const:1a8:8"
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
      "00649d84",
      "DATA",
      [
        "storage",
        "00bf7128",
        null,
        "undefined *"
      ]
    ],
    [
      "00649ed4",
      "READ",
      [
        "storage",
        "00bf7148",
        null,
        "pointer"
      ]
    ],
    [
      "00649ed4",
      "READ",
      [
        "storage",
        "00bf7150",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00649d84",
      "DATA",
      [
        "storage",
        "00bf7178",
        null,
        "undefined *"
      ]
    ],
    [
      "00649ed4",
      "READ",
      [
        "storage",
        "00bf7198",
        null,
        "pointer"
      ]
    ],
    [
      "00649ed4",
      "READ",
      [
        "storage",
        "00bf71a0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00649d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00649/00649c54.md#insn-00649d78) · [`00649d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00649/00649c54.md#insn-00649d7c)
- 新版 [`00649d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00649/00649c54.md#insn-00649d78) · [`00649d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00649/00649c54.md#insn-00649d7c)

~~~diff
- 00649d78 ["COPY", "tmp:0:8", ["const:128:8"]]
- 00649d78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00649d78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00649d78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00649d78 ["COPY", "tmp:0:8", ["const:178:8"]]
+ 00649d78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00649d78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00649d78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00649d78 bytes 08a10491
+ 00649d78 bytes 08e10591
- 00649d7c ["COPY", "tmp:0:8", ["const:30:8"]]
- 00649d7c ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
- 00649d7c ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
- 00649d7c ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
- 00649d7c bytes f6c30091
+ 00649d7c ["COPY", "tmp:0:8", ["const:30:8"]]
+ 00649d7c ["INT_CARRY", "register:105:1", ["register:8:8", "tmp:0:8"]]
+ 00649d7c ["INT_SCARRY", "register:106:1", ["register:8:8", "tmp:0:8"]]
+ 00649d7c ["INT_ADD", "tmp:1:8", ["register:8:8", "tmp:0:8"]]
+ 00649d7c bytes f6c30091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-deb2394418aee051f888202075fa80a3"></a>

### [`0064a3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064a/0064a3cc.md) → [`0064a3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064a/0064a3cc.md) FUN_0064a3cc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 23件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`0044592c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/0044592c.md) [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 23件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`0044592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/0044592c.md) [`00445d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d04.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.55% / 新版 99.55%

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
      "definition_site": "0064a404",
      "incomplete_value": true,
      "site": "0064a404",
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
      "definition_site": "0064a404",
      "incomplete_value": true,
      "site": "0064a404",
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
      "definition_site": "0064a410",
      "incomplete_value": false,
      "site": "0064a424",
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
      "definition_site": "0064a410",
      "incomplete_value": false,
      "site": "0064a424",
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
      "definition_site": "0064a418",
      "incomplete_value": false,
      "site": "0064a424",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064a418",
      "incomplete_value": false,
      "site": "0064a424",
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
            "const:c0:8"
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
      "0064a400",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0064a410",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0064a418",
      "PARAM",
      [
        "storage",
        "00bf70c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0064a400",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0064a410",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0064a418",
      "PARAM",
      [
        "storage",
        "00bf7110",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064a400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064a/0064a3cc.md#insn-0064a400) · [`0064a410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064a/0064a3cc.md#insn-0064a410) · [`0064a418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064a/0064a3cc.md#insn-0064a418)
- 新版 [`0064a400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064a/0064a3cc.md#insn-0064a400) · [`0064a410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064a/0064a3cc.md#insn-0064a410) · [`0064a418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064a/0064a3cc.md#insn-0064a418)

~~~diff
- 0064a400 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0064a400 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0064a400 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0064a400 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0064a400 bytes 083d45f9
+ 0064a400 bytes 085d45f9
- 0064a410 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0064a410 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0064a410 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0064a410 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0064a410 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0064a410 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0064a410 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0064a410 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0064a410 bytes 21203991
+ 0064a410 bytes 21603a91
- 0064a418 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 0064a418 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0064a418 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0064a418 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0064a418 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 0064a418 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0064a418 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0064a418 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0064a418 bytes 42000391
+ 0064a418 bytes 42400491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32bbc91345ba053dc161592b55fc3a76"></a>

### [`0064b18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064b/0064b18c.md) → [`0064b18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064b/0064b18c.md) FUN_0064b18c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00647388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00647/00647388.md) · 呼出先 22件 [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md)
- 新版 呼出元 1件 [`00647388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00647/00647388.md) · 呼出先 22件 [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.54% / 新版 90.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 29件, `store_destination` 7件, `store_value` 21件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0064b1d0",
      "incomplete_value": false,
      "site": "0064b1d8",
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
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064b1d0",
      "incomplete_value": false,
      "site": "0064b1d8",
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
            "const:e8:8"
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
      "definition_site": "0064b250",
      "incomplete_value": true,
      "site": "0064b250",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0064b250",
      "incomplete_value": true,
      "site": "0064b250",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064b26c",
      "incomplete_value": true,
      "site": "0064b26c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:88a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064b26c",
      "incomplete_value": true,
      "site": "0064b26c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0064b1d8",
      "DATA",
      [
        "storage",
        "00bf70e8",
        null,
        "pointer"
      ]
    ],
    [
      "0064b224",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0064b238",
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
      "0064b1d8",
      "DATA",
      [
        "storage",
        "00bf7138",
        null,
        "pointer"
      ]
    ],
    [
      "0064b224",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0064b238",
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

- 旧版 [`0064b1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064b/0064b18c.md#insn-0064b1d0) · [`0064b1dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064b/0064b18c.md#insn-0064b1dc)
- 新版 [`0064b1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064b/0064b18c.md#insn-0064b1d0) · [`0064b1dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064b/0064b18c.md#insn-0064b1dc)

~~~diff
- 0064b1d0 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 0064b1d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0064b1d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0064b1d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0064b1d0 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0064b1d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0064b1d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0064b1d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0064b1d0 bytes 08a10391
+ 0064b1d0 bytes 08e10491
- 0064b1dc ["COPY", "register:40e0:8", ["const:c25000:8"]]
- 0064b1dc bytes dc2e00d0
+ 0064b1dc ["COPY", "register:40e0:8", ["const:c25000:8"]]
+ 0064b1dc bytes dc2e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b14a739987b9d432d42de3ddd557ff7c"></a>

### [`0064c5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c5e4.md) → [`0064c5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c5e4.md) FUN_0064c5e4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0064c804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c804.md) · 呼出先 7件 [`00444988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444988.md) [`00444eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444eb4.md) [`0064c428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c428.md) [`0064c828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c828.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`0064c804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c804.md) · 呼出先 7件 [`00444988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444988.md) [`00444eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444eb4.md) [`0064c428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c428.md) [`0064c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c828.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "0064c5fc",
      "incomplete_value": false,
      "site": "0064c600",
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
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064c5fc",
      "incomplete_value": false,
      "site": "0064c600",
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
            "const:e8:8"
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
      "0064c600",
      "DATA",
      [
        "storage",
        "00bf70e8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0064c600",
      "DATA",
      [
        "storage",
        "00bf7138",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064c5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c5e4.md#insn-0064c5fc)
- 新版 [`0064c5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c5e4.md#insn-0064c5fc)

~~~diff
- 0064c5fc ["COPY", "tmp:0:8", ["const:e8:8"]]
- 0064c5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0064c5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0064c5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0064c5fc ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0064c5fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0064c5fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0064c5fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0064c5fc bytes 08a10391
+ 0064c5fc bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d13ee3b7218fe70e8e9aab4ae283d05b"></a>

### [`0064c828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c828.md) → [`0064c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c828.md) FUN_0064c828

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 12件 [`0064c5e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c5e4.md) [`0064ca44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064ca44.md) [`006554d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00655/006554d4.md) [`006555c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00655/006555c0.md) [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 12件 [`0064c5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c5e4.md) [`0064ca44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064ca44.md) [`006554d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/006554d4.md) [`006555c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/006555c0.md) [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "0064c840",
      "incomplete_value": false,
      "site": "0064c844",
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
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064c840",
      "incomplete_value": false,
      "site": "0064c844",
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
            "const:108:8"
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
      "0064c844",
      "DATA",
      [
        "storage",
        "00bf7108",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0064c844",
      "DATA",
      [
        "storage",
        "00bf7158",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064c840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c828.md#insn-0064c840)
- 新版 [`0064c840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c828.md#insn-0064c840)

~~~diff
- 0064c840 ["COPY", "tmp:0:8", ["const:108:8"]]
- 0064c840 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0064c840 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0064c840 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0064c840 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 0064c840 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0064c840 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0064c840 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0064c840 bytes 08210491
+ 0064c840 bytes 08610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeb8e25090469fabf4b58fec94cf5c70"></a>

### [`0064ca6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064ca6c.md) → [`0064ca6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064ca6c.md) FUN_0064ca6c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0064ca80",
      "incomplete_value": false,
      "site": "0064ca84",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064ca80",
      "incomplete_value": false,
      "site": "0064ca84",
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
            "const:128:8"
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
      "0064ca84",
      "DATA",
      [
        "storage",
        "00bf7128",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0064ca84",
      "DATA",
      [
        "storage",
        "00bf7178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064ca80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064ca6c.md#insn-0064ca80)
- 新版 [`0064ca80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064ca6c.md#insn-0064ca80)

~~~diff
- 0064ca80 ["COPY", "tmp:0:8", ["const:128:8"]]
- 0064ca80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0064ca80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0064ca80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0064ca80 ["COPY", "tmp:0:8", ["const:178:8"]]
+ 0064ca80 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0064ca80 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0064ca80 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0064ca80 bytes 08a10491
+ 0064ca80 bytes 08e10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b6ae4e40340a2dee11cc8bf685b41c9"></a>

### [`0064ca90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064ca90.md) → [`0064ca90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064ca90.md) FUN_0064ca90

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
      "definition_site": "0064ca94",
      "incomplete_value": false,
      "site": "0064ca98",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064ca94",
      "incomplete_value": false,
      "site": "0064ca98",
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
            "const:128:8"
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
      "0064ca98",
      "DATA",
      [
        "storage",
        "00bf7128",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0064ca98",
      "DATA",
      [
        "storage",
        "00bf7178",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064ca94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064ca90.md#insn-0064ca94)
- 新版 [`0064ca94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064ca90.md#insn-0064ca94)

~~~diff
- 0064ca94 ["COPY", "tmp:0:8", ["const:128:8"]]
- 0064ca94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0064ca94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0064ca94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0064ca94 ["COPY", "tmp:0:8", ["const:178:8"]]
+ 0064ca94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0064ca94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0064ca94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0064ca94 bytes 08a10491
+ 0064ca94 bytes 08e10591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e357ca1bd07fb7e6072c1865723ffeb0"></a>

### [`0064cb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064cb1c.md) → [`0064cb1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064cb1c.md) FUN_0064cb1c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0064cb30",
      "incomplete_value": false,
      "site": "0064cb34",
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
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064cb30",
      "incomplete_value": false,
      "site": "0064cb34",
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
      "0064cb34",
      "DATA",
      [
        "storage",
        "00bf71a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0064cb34",
      "DATA",
      [
        "storage",
        "00bf71f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064cb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064cb1c.md#insn-0064cb30)
- 新版 [`0064cb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064cb1c.md#insn-0064cb30)

~~~diff
- 0064cb30 ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 0064cb30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0064cb30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0064cb30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0064cb30 ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 0064cb30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0064cb30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0064cb30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0064cb30 bytes 08a10691
+ 0064cb30 bytes 08e10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee1bbe6997182e9fd20a5cf12b84a2b7"></a>

### [`0064cb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064cb40.md) → [`0064cb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064cb40.md) FUN_0064cb40

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
      "definition_site": "0064cb44",
      "incomplete_value": false,
      "site": "0064cb48",
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
            "const:1f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064cb44",
      "incomplete_value": false,
      "site": "0064cb48",
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
      "0064cb48",
      "DATA",
      [
        "storage",
        "00bf71a8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0064cb48",
      "DATA",
      [
        "storage",
        "00bf71f8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064cb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064cb40.md#insn-0064cb44)
- 新版 [`0064cb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064cb40.md#insn-0064cb44)

~~~diff
- 0064cb44 ["COPY", "tmp:0:8", ["const:1a8:8"]]
- 0064cb44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0064cb44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0064cb44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0064cb44 ["COPY", "tmp:0:8", ["const:1f8:8"]]
+ 0064cb44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0064cb44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0064cb44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0064cb44 bytes 08a10691
+ 0064cb44 bytes 08e10791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-488e68b99d74ad198ff79b5c1c6211f3"></a>

### [`0064cb58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064cb58.md) → [`0064cb58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064cb58.md) FUN_0064cb58

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00448/00448034.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 0件  · 呼出先 8件 [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md) [`00448034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00448/00448034.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.38% / 新版 99.38%

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
      "definition_site": "0064cba0",
      "incomplete_value": true,
      "site": "0064cba0",
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
      "definition_site": "0064cba0",
      "incomplete_value": true,
      "site": "0064cba0",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0064cba8",
      "incomplete_value": false,
      "site": "0064cbb8",
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
      "definition_site": "0064cba8",
      "incomplete_value": false,
      "site": "0064cbb8",
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
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0064cbb0",
      "incomplete_value": false,
      "site": "0064cbb8",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0064cbb0",
      "incomplete_value": false,
      "site": "0064cbb8",
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
            "const:c0:8"
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
      "0064cb9c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "0064cba8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0064cbb0",
      "PARAM",
      [
        "storage",
        "00bf70c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0064cb9c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "0064cba8",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0064cbb0",
      "PARAM",
      [
        "storage",
        "00bf7110",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064cb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064cb58.md#insn-0064cb9c) · [`0064cba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064cb58.md#insn-0064cba8) · [`0064cbb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064cb58.md#insn-0064cbb0)
- 新版 [`0064cb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064cb58.md#insn-0064cb9c) · [`0064cba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064cb58.md#insn-0064cba8) · [`0064cbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064cb58.md#insn-0064cbb0)

~~~diff
- 0064cb9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0064cb9c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0064cb9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0064cb9c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0064cb9c bytes 003d45f9
+ 0064cb9c bytes 005d45f9
- 0064cba8 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 0064cba8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0064cba8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0064cba8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0064cba8 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 0064cba8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0064cba8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0064cba8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0064cba8 bytes 21203991
+ 0064cba8 bytes 21603a91
- 0064cbb0 ["COPY", "tmp:0:8", ["const:c0:8"]]
- 0064cbb0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0064cbb0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0064cbb0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0064cbb0 ["COPY", "tmp:0:8", ["const:110:8"]]
+ 0064cbb0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0064cbb0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0064cbb0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0064cbb0 bytes 42000391
+ 0064cbb0 bytes 42400491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-098e77621b6639f1d96c5fc7f35836d0"></a>

### [`0064d090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064d/0064d090.md) → [`0064d090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064d/0064d090.md) _INIT_87

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
      "definition_site": "0064d0cc",
      "incomplete_value": true,
      "site": "0064d0e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d0cc",
      "incomplete_value": true,
      "site": "0064d0e8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d0f0",
      "incomplete_value": true,
      "site": "0064d10c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d0f0",
      "incomplete_value": true,
      "site": "0064d10c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d110",
      "incomplete_value": true,
      "site": "0064d12c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d110",
      "incomplete_value": true,
      "site": "0064d12c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0064d0cc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0064d0f0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0064d110",
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
      "0064d0cc",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0064d0f0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0064d110",
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

- 旧版 [`0064d0bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064d/0064d090.md#insn-0064d0bc) · [`0064d0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064d/0064d090.md#insn-0064d0c4)
- 新版 [`0064d0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064d/0064d090.md#insn-0064d0bc) · [`0064d0c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064d/0064d090.md#insn-0064d0c4)

~~~diff
- 0064d0bc ["COPY", "tmp:0:8", ["const:670:8"]]
- 0064d0bc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0064d0bc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0064d0bc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0064d0bc ["COPY", "tmp:0:8", ["const:6b0:8"]]
+ 0064d0bc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0064d0bc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0064d0bc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0064d0bc bytes 73c21991
+ 0064d0bc bytes 73c21a91
- 0064d0c4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0064d0c4 bytes c9e2ffd0
+ 0064d0c4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0064d0c4 bytes c9e2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65cf4b47e18ec487cac84293128f3bb6"></a>

### [`0064d420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064d/0064d420.md) → [`0064d420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064d/0064d420.md) _INIT_88

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
      "definition_site": "0064d45c",
      "incomplete_value": true,
      "site": "0064d478",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d45c",
      "incomplete_value": true,
      "site": "0064d478",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d480",
      "incomplete_value": true,
      "site": "0064d49c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d480",
      "incomplete_value": true,
      "site": "0064d49c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d4a0",
      "incomplete_value": true,
      "site": "0064d4bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d4a0",
      "incomplete_value": true,
      "site": "0064d4bc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0064d45c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0064d480",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0064d4a0",
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
      "0064d45c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0064d480",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0064d4a0",
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

- 旧版 [`0064d44c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064d/0064d420.md#insn-0064d44c) · [`0064d454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064d/0064d420.md#insn-0064d454)
- 新版 [`0064d44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064d/0064d420.md#insn-0064d44c) · [`0064d454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064d/0064d420.md#insn-0064d454)

~~~diff
- 0064d44c ["COPY", "tmp:0:8", ["const:688:8"]]
- 0064d44c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0064d44c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0064d44c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0064d44c ["COPY", "tmp:0:8", ["const:6c8:8"]]
+ 0064d44c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0064d44c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0064d44c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0064d44c bytes 73221a91
+ 0064d44c bytes 73221b91
- 0064d454 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0064d454 bytes c9e2ffd0
+ 0064d454 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0064d454 bytes c9e2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86491d20757b48b6003ea48fed90a290"></a>

### [`0064d7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064d/0064d7b0.md) → [`0064d7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064d/0064d7b0.md) _INIT_89

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
      "definition_site": "0064d7ec",
      "incomplete_value": true,
      "site": "0064d808",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d7ec",
      "incomplete_value": true,
      "site": "0064d808",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d810",
      "incomplete_value": true,
      "site": "0064d82c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d810",
      "incomplete_value": true,
      "site": "0064d82c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d830",
      "incomplete_value": true,
      "site": "0064d84c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064d830",
      "incomplete_value": true,
      "site": "0064d84c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0064d7ec",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0064d810",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0064d830",
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
      "0064d7ec",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0064d810",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0064d830",
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

- 旧版 [`0064d7dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064d/0064d7b0.md#insn-0064d7dc) · [`0064d7e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064d/0064d7b0.md#insn-0064d7e4)
- 新版 [`0064d7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064d/0064d7b0.md#insn-0064d7dc) · [`0064d7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064d/0064d7b0.md#insn-0064d7e4)

~~~diff
- 0064d7dc ["COPY", "tmp:0:8", ["const:6a0:8"]]
- 0064d7dc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0064d7dc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0064d7dc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0064d7dc ["COPY", "tmp:0:8", ["const:6e0:8"]]
+ 0064d7dc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0064d7dc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0064d7dc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0064d7dc bytes 73821a91
+ 0064d7dc bytes 73821b91
- 0064d7e4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0064d7e4 bytes c9e2ffd0
+ 0064d7e4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0064d7e4 bytes c9e2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-197f1c159d800b36d455223dbe3b96a2"></a>

### [`0064db40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064d/0064db40.md) → [`0064db40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064d/0064db40.md) _INIT_90

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
      "definition_site": "0064db7c",
      "incomplete_value": true,
      "site": "0064db98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064db7c",
      "incomplete_value": true,
      "site": "0064db98",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064dba0",
      "incomplete_value": true,
      "site": "0064dbbc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064dba0",
      "incomplete_value": true,
      "site": "0064dbbc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064dbc0",
      "incomplete_value": true,
      "site": "0064dbdc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0064dbc0",
      "incomplete_value": true,
      "site": "0064dbdc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0064db7c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0064dba0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0064dbc0",
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
      "0064db7c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0064dba0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0064dbc0",
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

- 旧版 [`0064db6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064d/0064db40.md#insn-0064db6c) · [`0064db74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064d/0064db40.md#insn-0064db74)
- 新版 [`0064db6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064d/0064db40.md#insn-0064db6c) · [`0064db74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064d/0064db40.md#insn-0064db74)

~~~diff
- 0064db6c ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 0064db6c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0064db6c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0064db6c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0064db6c ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 0064db6c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0064db6c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0064db6c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0064db6c bytes 73e21a91
+ 0064db6c bytes 73e21b91
- 0064db74 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0064db74 bytes c9e2ffd0
+ 0064db74 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0064db74 bytes c9e2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fae59ad4ab74f3583d83dc78e47f4ae"></a>

### [`0064e108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064e/0064e108.md) → [`0064e108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064e/0064e108.md) FUN_0064e108

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md) [`0064ded0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064d/0064ded0.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 13件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md) [`0064ded0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064d/0064ded0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.52% / 新版 97.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0064e140",
      "incomplete_value": false,
      "site": "0064e14c",
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
      "definition_site": "0064e140",
      "incomplete_value": false,
      "site": "0064e14c",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0064e308",
      "incomplete_value": true,
      "site": "0064e30c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0064e308",
      "incomplete_value": true,
      "site": "0064e30c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "0064e14c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0064e2d4",
      "READ",
      [
        "storage",
        "00c1ad70",
        null,
        "pointer"
      ]
    ],
    [
      "0064e2d8",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0064e14c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0064e2d4",
      "READ",
      [
        "storage",
        "00c1adc0",
        null,
        "pointer"
      ]
    ],
    [
      "0064e2d8",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0064e140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064e/0064e108.md#insn-0064e140) · [`0064e2d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064e/0064e108.md#insn-0064e2d4) · [`0064e2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064e/0064e108.md#insn-0064e2d8)
- 新版 [`0064e140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064e/0064e108.md#insn-0064e140) · [`0064e2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064e/0064e108.md#insn-0064e2d4) · [`0064e2d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064e/0064e108.md#insn-0064e2d8)

~~~diff
- 0064e140 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0064e140 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0064e140 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0064e140 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0064e140 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0064e140 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0064e140 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0064e140 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0064e140 bytes 08a13491
+ 0064e140 bytes 08e13591
- 0064e2d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 0064e2d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0064e2d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 0064e2d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0064e2d4 bytes 08b946f9
+ 0064e2d4 bytes 08e146f9
- 0064e2d8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:d78:8"]]
- 0064e2d8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
+ 0064e2d8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:dc8:8"]]
+ 0064e2d8 ["LOAD", "register:40b0:8", ["const:1b1:8", "tmp:0:8"]]
- 0064e2d8 bytes d6be46f9
+ 0064e2d8 bytes d6e646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e49dda45734f56ce4b5e9e92889626a5"></a>

### [`0064fdf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064f/0064fdf8.md) → [`0064fdf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064f/0064fdf8.md) FUN_0064fdf8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 16件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.53% / 新版 97.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0064fe38",
      "incomplete_value": false,
      "site": "0064fe44",
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
      "definition_site": "0064fe38",
      "incomplete_value": false,
      "site": "0064fe44",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00650304",
      "incomplete_value": true,
      "site": "00650308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00650304",
      "incomplete_value": true,
      "site": "00650308",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
          ]
        ]
      ]
    },
    "ordinal": 69,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00650300",
      "incomplete_value": true,
      "site": "0065030c",
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
      "definition_site": "00650300",
      "incomplete_value": true,
      "site": "0065030c",
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
    "ordinal": 70,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0064fe44",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0064fe7c",
      "READ",
      [
        "storage",
        "002a0832",
        null,
        "string"
      ]
    ],
    [
      "006502f4",
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
      "0064fe44",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0064fe7c",
      "READ",
      [
        "storage",
        "002a08bd",
        null,
        "string"
      ]
    ],
    [
      "006502f4",
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

- 旧版 [`0064fe38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064f/0064fdf8.md#insn-0064fe38) · [`0064fe70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064f/0064fdf8.md#insn-0064fe70) · [`006502f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064f/0064fdf8.md#insn-006502f4)
- 新版 [`0064fe38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064f/0064fdf8.md#insn-0064fe38) · [`0064fe70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064f/0064fdf8.md#insn-0064fe70) · [`006502f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064f/0064fdf8.md#insn-006502f4)

~~~diff
- 0064fe38 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0064fe38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0064fe38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0064fe38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0064fe38 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0064fe38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0064fe38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0064fe38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0064fe38 bytes 08a13491
+ 0064fe38 bytes 08e13591
- 0064fe70 ["COPY", "tmp:0:8", ["const:832:8"]]
- 0064fe70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0064fe70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0064fe70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0064fe70 ["COPY", "tmp:0:8", ["const:8bd:8"]]
+ 0064fe70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0064fe70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0064fe70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0064fe70 bytes 29c92091
+ 0064fe70 bytes 29f52291
- 006502f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 006502f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 006502f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 006502f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 006502f4 bytes 08b946f9
+ 006502f4 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9edad0f4a15ae09216a8463a9903fba"></a>

### [`00650784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00650/00650784.md) → [`00650784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650784.md) FUN_00650784

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0064ded0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064d/0064ded0.md) [`00a293b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a29/00a293b0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0064ded0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064d/0064ded0.md) [`00a293f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a29/00a293f4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00650790",
      "incomplete_value": false,
      "site": "00650794",
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
      "definition_site": "00650790",
      "incomplete_value": false,
      "site": "00650794",
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
      "00650790",
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
      "00650790",
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

- 旧版 [`00650790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00650/00650784.md#insn-00650790)
- 新版 [`00650790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00650/00650784.md#insn-00650790)

~~~diff
- 00650790 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00650790 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00650790 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00650790 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00650790 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00650790 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00650790 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00650790 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00650790 bytes 000c0c91
+ 00650790 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dabe1d5fc7050f238f7ce915ac373bb3"></a>

### [`00651390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00651/00651390.md) → [`00651390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00651/00651390.md) _INIT_91

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00651430",
      "incomplete_value": true,
      "site": "00651448",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00651430",
      "incomplete_value": true,
      "site": "00651448",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0065144c",
      "incomplete_value": true,
      "site": "00651468",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0065144c",
      "incomplete_value": true,
      "site": "00651468",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "006515b8",
      "incomplete_value": false,
      "site": "006515c4",
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
            "const:710:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006515b8",
      "incomplete_value": false,
      "site": "006515c4",
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
            "const:6d0:8"
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
      "006513cc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "006513f0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00651410",
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
      "006513cc",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "006513f0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00651410",
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

- 旧版 [`006513bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00651/00651390.md#insn-006513bc) · [`006513c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00651/00651390.md#insn-006513c4)
- 新版 [`006513bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00651/00651390.md#insn-006513bc) · [`006513c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00651/00651390.md#insn-006513c4)

~~~diff
- 006513bc ["COPY", "tmp:0:8", ["const:6d0:8"]]
- 006513bc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006513bc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006513bc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006513bc ["COPY", "tmp:0:8", ["const:710:8"]]
+ 006513bc ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006513bc ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006513bc ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006513bc bytes 73421b91
+ 006513bc bytes 73421c91
- 006513c4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006513c4 bytes a9e2ffd0
+ 006513c4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006513c4 bytes a9e2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86672bdfa36f16ad9ff0d7091dcbc37a"></a>

### [`006525c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00652/006525c0.md) → [`006525c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00652/006525c0.md) FUN_006525c0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 19件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459bb4.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 19件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459bb4.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 99.23% / 新版 99.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00652700",
      "incomplete_value": true,
      "site": "00652710",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c36:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00652700",
      "incomplete_value": true,
      "site": "00652710",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cca:8"
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
      "definition_site": "00652704",
      "incomplete_value": true,
      "site": "00652714",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00652704",
      "incomplete_value": true,
      "site": "00652714",
      "value": [
        "LOAD",
        "8",
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
      "00652700",
      "READ",
      [
        "storage",
        "002aecca",
        null,
        "string"
      ]
    ],
    [
      "00652704",
      "READ",
      [
        "storage",
        "002aecda",
        null,
        "string"
      ]
    ],
    [
      "00652ad4",
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
      "00652700",
      "READ",
      [
        "storage",
        "002aec36",
        null,
        "string"
      ]
    ],
    [
      "00652704",
      "READ",
      [
        "storage",
        "002aec46",
        null,
        "string"
      ]
    ],
    [
      "00652ad4",
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

- 旧版 [`006526f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00652/006525c0.md#insn-006526f8) · [`006526fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00652/006525c0.md#insn-006526fc)
- 新版 [`006526f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00652/006525c0.md#insn-006526f8) · [`006526fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00652/006525c0.md#insn-006526fc)

~~~diff
- 006526f8 ["COPY", "tmp:0:8", ["const:cca:8"]]
- 006526f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006526f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006526f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006526f8 ["COPY", "tmp:0:8", ["const:c36:8"]]
+ 006526f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006526f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006526f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006526f8 bytes 08293391
+ 006526f8 bytes 08d93091
- 006526fc ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 006526fc bytes e9e2ffd0
+ 006526fc ["COPY", "register:4048:8", ["const:2b0000:8"]]
+ 006526fc bytes e9e2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b1230f14685134f2bcaeac7ee4d3043"></a>

### [`006534e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00653/006534e0.md) → [`006534e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00653/006534e0.md) FUN_006534e0

採用 · 移動量 `+0x0` · 根拠 `instruction_blocks_cfg_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 28件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`00444c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00444fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444fcc.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 28件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`00444c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c18.md) [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00444fcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444fcc.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 98.64% / 新版 98.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00653538",
      "incomplete_value": true,
      "site": "00653538",
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
      "definition_site": "00653538",
      "incomplete_value": true,
      "site": "00653538",
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
      "definition_site": "00653540",
      "incomplete_value": false,
      "site": "00653550",
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
      "definition_site": "00653540",
      "incomplete_value": false,
      "site": "00653550",
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
      "definition_site": "00653548",
      "incomplete_value": false,
      "site": "00653550",
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
            "const:268:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00653548",
      "incomplete_value": false,
      "site": "00653550",
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
            "const:218:8"
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
      "00653528",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00653540",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00653548",
      "PARAM",
      [
        "storage",
        "00bf7218",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00653528",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00653540",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00653548",
      "PARAM",
      [
        "storage",
        "00bf7268",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00653528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00653/006534e0.md#insn-00653528) · [`00653540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00653/006534e0.md#insn-00653540) · [`00653548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00653/006534e0.md#insn-00653548)
- 新版 [`00653528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00653/006534e0.md#insn-00653528) · [`00653540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00653/006534e0.md#insn-00653540) · [`00653548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00653/006534e0.md#insn-00653548)

~~~diff
- 00653528 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00653528 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00653528 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00653528 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00653528 bytes 003d45f9
+ 00653528 bytes 005d45f9
- 00653540 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00653540 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00653540 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00653540 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00653540 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00653540 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00653540 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00653540 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00653540 bytes 21203991
+ 00653540 bytes 21603a91
- 00653548 ["COPY", "tmp:0:8", ["const:218:8"]]
- 00653548 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00653548 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00653548 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00653548 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 00653548 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00653548 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00653548 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00653548 bytes 42600891
+ 00653548 bytes 42a00991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b6a9a23c0fc4f5fdad1cd5a121caaab"></a>

### [`00654084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00654/00654084.md) → [`00654084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00654/00654084.md) FUN_00654084

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00651720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00651/00651720.md) · 呼出先 13件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0072e62c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072e/0072e62c.md) [`007cf4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cf/007cf4b0.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`00651720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00651/00651720.md) · 呼出先 13件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0072e62c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072e/0072e62c.md) [`007cf4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cf/007cf4b0.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 84.58% / 新版 84.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 57件, `store_destination` 25件, `store_value` 29件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006540dc",
      "incomplete_value": false,
      "site": "006540e4",
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
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006540dc",
      "incomplete_value": false,
      "site": "006540e4",
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
            "const:240:8"
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
      "definition_site": "00654198",
      "incomplete_value": true,
      "site": "00654198",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00654198",
      "incomplete_value": true,
      "site": "00654198",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bad:8"
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
      "definition_site": "0065419c",
      "incomplete_value": true,
      "site": "0065419c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0065419c",
      "incomplete_value": true,
      "site": "0065419c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 41,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "006540e4",
      "DATA",
      [
        "storage",
        "00bf7240",
        null,
        "pointer"
      ]
    ],
    [
      "00654150",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00654170",
      "READ",
      [
        "storage",
        "002a268e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006540e4",
      "DATA",
      [
        "storage",
        "00bf7290",
        null,
        "pointer"
      ]
    ],
    [
      "00654150",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00654170",
      "READ",
      [
        "storage",
        "002a2719",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006540dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00654/00654084.md#insn-006540dc) · [`006540e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00654/00654084.md#insn-006540e8)
- 新版 [`006540dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00654/00654084.md#insn-006540dc) · [`006540e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00654/00654084.md#insn-006540e8)

~~~diff
- 006540dc ["COPY", "tmp:0:8", ["const:240:8"]]
- 006540dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006540dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006540dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006540dc ["COPY", "tmp:0:8", ["const:290:8"]]
+ 006540dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006540dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006540dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006540dc bytes 08010991
+ 006540dc bytes 08410a91
- 006540e8 ["COPY", "register:40c8:8", ["const:c25000:8"]]
- 006540e8 bytes 992e00b0
+ 006540e8 ["COPY", "register:40c8:8", ["const:c25000:8"]]
+ 006540e8 bytes 992e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c74ae79fe8b061ab68bcb8ae8e78dbd1"></a>

### [`006555c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00655/006555c0.md) → [`006555c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/006555c0.md) FUN_006555c0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0064c428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c428.md) [`0064c828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c828.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0064c428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c428.md) [`0064c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c828.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "006555dc",
      "incomplete_value": false,
      "site": "006555e0",
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
            "const:290:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006555dc",
      "incomplete_value": false,
      "site": "006555e0",
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
            "const:240:8"
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
      "006555e0",
      "DATA",
      [
        "storage",
        "00bf7240",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "006555e0",
      "DATA",
      [
        "storage",
        "00bf7290",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006555dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00655/006555c0.md#insn-006555dc)
- 新版 [`006555dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/006555c0.md#insn-006555dc)

~~~diff
- 006555dc ["COPY", "tmp:0:8", ["const:240:8"]]
- 006555dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006555dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006555dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006555dc ["COPY", "tmp:0:8", ["const:290:8"]]
+ 006555dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006555dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006555dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006555dc bytes 08010991
+ 006555dc bytes 08410a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf833dc5ff09f0f4b8a770cb397eca3e"></a>

### [`006556b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00655/006556b4.md) → [`006556b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/006556b4.md) _INIT_92

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "006556f0",
      "incomplete_value": true,
      "site": "0065570c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006556f0",
      "incomplete_value": true,
      "site": "0065570c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00655714",
      "incomplete_value": true,
      "site": "00655730",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00655714",
      "incomplete_value": true,
      "site": "00655730",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00655754",
      "incomplete_value": true,
      "site": "0065576c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00655754",
      "incomplete_value": true,
      "site": "0065576c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "006556f0",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00655714",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00655734",
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
      "006556f0",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00655714",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00655734",
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

- 旧版 [`006556e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00655/006556b4.md#insn-006556e0) · [`006556e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00655/006556b4.md#insn-006556e8)
- 新版 [`006556e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/006556b4.md#insn-006556e0) · [`006556e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/006556b4.md#insn-006556e8)

~~~diff
- 006556e0 ["COPY", "tmp:0:8", ["const:6e8:8"]]
- 006556e0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 006556e0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 006556e0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 006556e0 ["COPY", "tmp:0:8", ["const:728:8"]]
+ 006556e0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 006556e0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 006556e0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 006556e0 bytes 73a21b91
+ 006556e0 bytes 73a21c91
- 006556e8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 006556e8 bytes 89e2ffd0
+ 006556e8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 006556e8 bytes 89e2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-255ce3c19284dc5fa189e630c7fdc865"></a>

### [`00655a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00655/00655a44.md) → [`00655a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/00655a44.md) FUN_00655a44

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 20件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 20件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.08% / 新版 97.08%

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
      "definition_site": "00655a88",
      "incomplete_value": false,
      "site": "00655a94",
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
      "definition_site": "00655a88",
      "incomplete_value": false,
      "site": "00655a94",
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
      "definition_site": "00655ae8",
      "incomplete_value": true,
      "site": "00655ae8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6ff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00655ae8",
      "incomplete_value": true,
      "site": "00655ae8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:701:8"
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
      "definition_site": "00656038",
      "incomplete_value": true,
      "site": "0065603c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00656038",
      "incomplete_value": true,
      "site": "0065603c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:10:8"
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
      "00655a94",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00655ad8",
      "READ",
      [
        "storage",
        "0029b701",
        null,
        "string"
      ]
    ],
    [
      "00656028",
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
      "00655a94",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00655ad8",
      "READ",
      [
        "storage",
        "0029b6ff",
        null,
        "string"
      ]
    ],
    [
      "00656028",
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

- 旧版 [`00655a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00655/00655a44.md#insn-00655a88) · [`00655acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00655/00655a44.md#insn-00655acc) · [`00656028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00655/00655a44.md#insn-00656028)
- 新版 [`00655a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/00655a44.md#insn-00655a88) · [`00655acc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/00655a44.md#insn-00655acc) · [`00656028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/00655a44.md#insn-00656028)

~~~diff
- 00655a88 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00655a88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00655a88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00655a88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00655a88 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00655a88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00655a88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00655a88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00655a88 bytes 08a13491
+ 00655a88 bytes 08e13591
- 00655acc ["COPY", "tmp:0:8", ["const:701:8"]]
- 00655acc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00655acc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00655acc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00655acc ["COPY", "tmp:0:8", ["const:6ff:8"]]
+ 00655acc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00655acc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00655acc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00655acc bytes 29051c91
+ 00655acc bytes 29fd1b91
- 00656028 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 00656028 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00656028 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 00656028 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00656028 bytes 08b946f9
+ 00656028 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1cac01fe46de80c5ba4c4265bfe0036"></a>

### [`006564f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/006564f4.md) → [`006564f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/006564f4.md) FUN_006564f4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00655a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00655/00655a44.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00655a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00655/00655a44.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00656500",
      "incomplete_value": false,
      "site": "00656504",
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
      "definition_site": "00656500",
      "incomplete_value": false,
      "site": "00656504",
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
      "00656500",
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
      "00656500",
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

- 旧版 [`00656500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/006564f4.md#insn-00656500)
- 新版 [`00656500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/006564f4.md#insn-00656500)

~~~diff
- 00656500 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00656500 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00656500 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00656500 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00656500 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00656500 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00656500 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00656500 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00656500 bytes 000c0c91
+ 00656500 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c502a30ea51227eebe2f43367223b5e6"></a>

### [`00656508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/00656508.md) → [`00656508`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/00656508.md) FUN_00656508

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0065644c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/0065644c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md)
- 新版 呼出元 1件 [`0065644c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/0065644c.md) · 呼出先 1件 [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md)

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
      "definition_site": "00656514",
      "incomplete_value": false,
      "site": "00656518",
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
      "definition_site": "00656514",
      "incomplete_value": false,
      "site": "00656518",
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
      "00656514",
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
      "00656514",
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

- 旧版 [`00656514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/00656508.md#insn-00656514)
- 新版 [`00656514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/00656508.md#insn-00656514)

~~~diff
- 00656514 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00656514 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00656514 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00656514 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00656514 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00656514 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00656514 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00656514 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00656514 bytes 000c0c91
+ 00656514 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e88d676fb2495f82e1e8f66d794f8aaf"></a>

### [`0065651c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/0065651c.md) → [`0065651c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/0065651c.md) _INIT_93

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.83% / 新版 89.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0065659c",
      "incomplete_value": true,
      "site": "006565b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0065659c",
      "incomplete_value": true,
      "site": "006565b8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "006565bc",
      "incomplete_value": true,
      "site": "006565d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006565bc",
      "incomplete_value": true,
      "site": "006565d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006565d8",
      "incomplete_value": true,
      "site": "006565f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "006565d8",
      "incomplete_value": true,
      "site": "006565f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00656558",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0065657c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0065659c",
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
      "00656558",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0065657c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0065659c",
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

- 旧版 [`00656548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/0065651c.md#insn-00656548) · [`00656554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/0065651c.md#insn-00656554) · [`00656570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/0065651c.md#insn-00656570)
- 新版 [`00656548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/0065651c.md#insn-00656548) · [`00656554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/0065651c.md#insn-00656554) · [`00656570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/0065651c.md#insn-00656570)

~~~diff
- 00656548 ["COPY", "tmp:0:8", ["const:700:8"]]
- 00656548 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00656548 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00656548 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00656548 ["COPY", "tmp:0:8", ["const:740:8"]]
+ 00656548 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00656548 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00656548 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00656548 bytes 73021c91
+ 00656548 bytes 73021d91
- 00656554 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00656554 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00656554 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00656554 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00656554 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00656554 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00656554 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00656554 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00656554 bytes 29750b91
+ 00656554 bytes 29dd0d91
- 00656570 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 00656570 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00656570 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00656570 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00656570 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 00656570 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00656570 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00656570 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00656570 bytes 4ac10b91
+ 00656570 bytes 4a290e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-676be1bdba33013704f6c4c11da07bf7"></a>

### [`006568ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/006568ac.md) → [`006568ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/006568ac.md) FUN_006568ac

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`009a3a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a3/009a3a30.md) [`009a5abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009a5/009a5abc.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465680.md)
- 新版 呼出元 2件 [`009a3a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a3/009a3a30.md) [`009a5abc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009a5/009a5abc.md) · 呼出先 15件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465680.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 91.56% / 新版 91.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 9件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006568f4",
      "incomplete_value": false,
      "site": "006568f8",
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
      "definition_site": "006568f4",
      "incomplete_value": false,
      "site": "006568f8",
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
      "definition_site": "00656918",
      "incomplete_value": true,
      "site": "0065692c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:79c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00656918",
      "incomplete_value": true,
      "site": "0065692c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:711:8"
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
      "definition_site": "00656968",
      "incomplete_value": true,
      "site": "0065697c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:31:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00656968",
      "incomplete_value": true,
      "site": "0065697c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:be:8"
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
      "006568f8",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00656918",
      "READ",
      [
        "storage",
        "0029e711",
        null,
        "string"
      ]
    ],
    [
      "00656968",
      "READ",
      [
        "storage",
        "002990be",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "006568f8",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00656918",
      "READ",
      [
        "storage",
        "0029e79c",
        null,
        "string"
      ]
    ],
    [
      "00656968",
      "READ",
      [
        "storage",
        "00299031",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`006568f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/006568ac.md#insn-006568f4) · [`00656910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/006568ac.md#insn-00656910) · [`00656960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/006568ac.md#insn-00656960)
- 新版 [`006568f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/006568ac.md#insn-006568f4) · [`00656910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/006568ac.md#insn-00656910) · [`00656960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/006568ac.md#insn-00656960)

~~~diff
- 006568f4 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 006568f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006568f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006568f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006568f4 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 006568f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006568f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006568f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006568f4 bytes 08a13491
+ 006568f4 bytes 08e13591
- 00656910 ["COPY", "tmp:0:8", ["const:711:8"]]
- 00656910 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00656910 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00656910 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00656910 ["COPY", "tmp:0:8", ["const:79c:8"]]
+ 00656910 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00656910 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00656910 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00656910 bytes 29451c91
+ 00656910 bytes 29711e91
- 00656960 ["COPY", "tmp:0:8", ["const:be:8"]]
- 00656960 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00656960 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00656960 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00656960 ["COPY", "tmp:0:8", ["const:31:8"]]
+ 00656960 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00656960 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00656960 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00656960 bytes 29f90291
+ 00656960 bytes 29c50091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea0a5f120b753fe48c8be47af01c5d68"></a>

### [`00656e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/00656e0c.md) → [`00656e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/00656e0c.md) FUN_00656e0c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006568ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/006568ac.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`006568ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/006568ac.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00656e18",
      "incomplete_value": false,
      "site": "00656e1c",
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
      "definition_site": "00656e18",
      "incomplete_value": false,
      "site": "00656e1c",
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
      "00656e18",
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
      "00656e18",
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

- 旧版 [`00656e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/00656e0c.md#insn-00656e18)
- 新版 [`00656e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/00656e0c.md#insn-00656e18)

~~~diff
- 00656e18 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00656e18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00656e18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00656e18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00656e18 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00656e18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00656e18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00656e18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00656e18 bytes 000c0c91
+ 00656e18 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-018995e883844487e1ffb12cec7dad33"></a>

### [`00656e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/00656e20.md) → [`00656e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/00656e20.md) _INIT_94

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 88.70% / 新版 88.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00656e80",
      "incomplete_value": true,
      "site": "00656e9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00656e80",
      "incomplete_value": true,
      "site": "00656e9c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00656ea0",
      "incomplete_value": true,
      "site": "00656ebc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00656ea0",
      "incomplete_value": true,
      "site": "00656ebc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00656ec0",
      "incomplete_value": true,
      "site": "00656ed8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00656ec0",
      "incomplete_value": true,
      "site": "00656ed8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00656e5c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00656e80",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00656ea0",
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
      "00656e5c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00656e80",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00656ea0",
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

- 旧版 [`00656e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/00656e20.md#insn-00656e4c) · [`00656e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/00656e20.md#insn-00656e58) · [`00656e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00656/00656e20.md#insn-00656e74)
- 新版 [`00656e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/00656e20.md#insn-00656e4c) · [`00656e58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/00656e20.md#insn-00656e58) · [`00656e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00656/00656e20.md#insn-00656e74)

~~~diff
- 00656e4c ["COPY", "tmp:0:8", ["const:718:8"]]
- 00656e4c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00656e4c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00656e4c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00656e4c ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00656e4c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00656e4c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00656e4c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00656e4c bytes 73621c91
+ 00656e4c bytes 73621d91
- 00656e58 ["COPY", "tmp:0:8", ["const:2dd:8"]]
- 00656e58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00656e58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00656e58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00656e58 ["COPY", "tmp:0:8", ["const:377:8"]]
+ 00656e58 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00656e58 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00656e58 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00656e58 bytes 29750b91
+ 00656e58 bytes 29dd0d91
- 00656e74 ["COPY", "tmp:0:8", ["const:2f0:8"]]
- 00656e74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00656e74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00656e74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00656e74 ["COPY", "tmp:0:8", ["const:38a:8"]]
+ 00656e74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00656e74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00656e74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00656e74 bytes 4ac10b91
+ 00656e74 bytes 4a290e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ac25f03f585e3dba347acbf07fcb0b7"></a>

### [`006571b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/006571b0.md) → [`006571b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/006571b0.md) FUN_006571b0

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006584d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006584d8.md) · 呼出先 15件 [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0060d/0060d83c.md) [`00657e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/00657e7c.md) [`00658090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/00658090.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md)
- 新版 呼出元 1件 [`006584d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006584d8.md) · 呼出先 15件 [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`0060d83c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0060d/0060d83c.md) [`00657e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/00657e7c.md) [`00658090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/00658090.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 92.18% / 新版 92.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 21件, `store_value` 10件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "006571e8",
      "incomplete_value": false,
      "site": "006571f8",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "006571e8",
      "incomplete_value": false,
      "site": "006571f8",
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
            "const:260:8"
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
      "definition_site": "00657310",
      "incomplete_value": true,
      "site": "00657310",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:88a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657310",
      "incomplete_value": true,
      "site": "00657310",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:7ff:8"
              ]
            ]
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
      "definition_site": "00657314",
      "incomplete_value": true,
      "site": "00657314",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00657314",
      "incomplete_value": true,
      "site": "00657314",
      "value": [
        "LOAD",
        "8",
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
      "006571f8",
      "DATA",
      [
        "storage",
        "00bf7260",
        null,
        "pointer"
      ]
    ],
    [
      "006572c8",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "006572e8",
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
      "006571f8",
      "DATA",
      [
        "storage",
        "00bf72b0",
        null,
        "pointer"
      ]
    ],
    [
      "006572c8",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "006572e8",
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

- 旧版 [`006571e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/006571b0.md#insn-006571e8) · [`00657224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/006571b0.md#insn-00657224) · [`006572e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/006571b0.md#insn-006572e4)
- 新版 [`006571e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/006571b0.md#insn-006571e8) · [`00657224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/006571b0.md#insn-00657224) · [`006572e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/006571b0.md#insn-006572e4)

~~~diff
- 006571e8 ["COPY", "tmp:0:8", ["const:260:8"]]
- 006571e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006571e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006571e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006571e8 ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 006571e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006571e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006571e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006571e8 bytes 08810991
+ 006571e8 bytes 08c10a91
- 00657224 ["COPY", "tmp:0:8", ["const:38:8"]]
- 00657224 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
- 00657224 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
- 00657224 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
+ 00657224 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00657224 ["INT_CARRY", "register:105:1", ["register:40c8:8", "tmp:0:8"]]
+ 00657224 ["INT_SCARRY", "register:106:1", ["register:40c8:8", "tmp:0:8"]]
+ 00657224 ["INT_ADD", "tmp:1:8", ["register:40c8:8", "tmp:0:8"]]
- 00657224 bytes 39e30091
+ 00657224 bytes 39e30191
- 006572e4 ["COPY", "tmp:0:8", ["const:895:8"]]
- 006572e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 006572e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 006572e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 006572e4 ["COPY", "tmp:0:8", ["const:920:8"]]
+ 006572e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 006572e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 006572e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 006572e4 bytes 08552291
+ 006572e4 bytes 08812491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c17a53a263d49204ce55e8ffb8ea8a8"></a>

### [`00657e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/00657e7c.md) → [`00657e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/00657e7c.md) FUN_00657e7c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 13件 [`006571b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/006571b0.md) [`00689eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00689/00689eb0.md) [`007118bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00711/007118bc.md) [`0072a6fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072a/0072a6fc.md) [`0072dfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0072d/0072dfbc.md) · 呼出先 10件 [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md) [`00acdd78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acdd78.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 13件 [`006571b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/006571b0.md) [`00689eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00689/00689eb0.md) [`007118bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00711/007118bc.md) [`0072a6fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072a/0072a6fc.md) [`0072dfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0072d/0072dfbc.md) · 呼出先 10件 [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md) [`00acddbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00acd/00acddbc.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 80.70% / 新版 80.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 7件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00657eac",
      "incomplete_value": false,
      "site": "00657eb0",
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
      "definition_site": "00657eac",
      "incomplete_value": false,
      "site": "00657eb0",
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00657ef0",
      "incomplete_value": true,
      "site": "00657ef0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:717:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00657ef0",
      "incomplete_value": true,
      "site": "00657ef0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:719:8"
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
      "definition_site": "00658014",
      "incomplete_value": true,
      "site": "00658014",
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
      "definition_site": "00658014",
      "incomplete_value": true,
      "site": "00658014",
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
    "ordinal": 19,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00657eb0",
      "DATA",
      [
        "storage",
        "00bf7298",
        null,
        "pointer"
      ]
    ],
    [
      "00657ec0",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00657ee0",
      "READ",
      [
        "storage",
        "0029b719",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00657eb0",
      "DATA",
      [
        "storage",
        "00bf72e8",
        null,
        "pointer"
      ]
    ],
    [
      "00657ec0",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00657ee0",
      "READ",
      [
        "storage",
        "0029b717",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00657eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/00657e7c.md#insn-00657eac) · [`00657eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00657/00657e7c.md#insn-00657eb4)
- 新版 [`00657eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/00657e7c.md#insn-00657eac) · [`00657eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00657/00657e7c.md#insn-00657eb4)

~~~diff
- 00657eac ["COPY", "tmp:0:8", ["const:298:8"]]
- 00657eac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00657eac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00657eac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00657eac ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 00657eac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00657eac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00657eac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00657eac bytes 08610a91
+ 00657eac bytes 08a10b91
- 00657eb4 ["COPY", "register:4040:8", ["const:c25000:8"]]
- 00657eb4 bytes 682e00d0
+ 00657eb4 ["COPY", "register:4040:8", ["const:c25000:8"]]
+ 00657eb4 bytes 682e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42193f3fb3da52c1d4e16479116333f4"></a>

### [`006584d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006584d8.md) → [`006584d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006584d8.md) FUN_006584d8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 30件 [`0041be0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041c/0041c8f8.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 30件 [`0041be0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041be0c.md) [`0041c8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041c/0041c8f8.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 98.41% / 新版 98.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件, `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00658534",
      "incomplete_value": true,
      "site": "00658534",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00658534",
      "incomplete_value": true,
      "site": "00658534",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0065852c",
      "incomplete_value": true,
      "site": "00658534",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ab8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065852c",
      "incomplete_value": true,
      "site": "00658534",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a78:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00658538",
      "incomplete_value": true,
      "site": "00658538",
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
            "const:ab8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00658538",
      "incomplete_value": true,
      "site": "00658538",
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
            "const:a78:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0065852c",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00658530",
      "READ",
      [
        "storage",
        "00c24a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00658534",
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
      "0065852c",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00658530",
      "READ",
      [
        "storage",
        "00c24aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00658534",
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

- 旧版 [`00658534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006584d8.md#insn-00658534) · [`00658538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006584d8.md#insn-00658538) · [`00658560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006584d8.md#insn-00658560)
- 新版 [`00658534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006584d8.md#insn-00658534) · [`00658538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006584d8.md#insn-00658538) · [`00658560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006584d8.md#insn-00658560)

~~~diff
- 00658534 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 00658534 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00658534 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:aa8:8"]]
+ 00658534 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00658534 bytes 093505f9
+ 00658534 bytes 095505f9
- 00658538 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
- 00658538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00658538 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ab8:8"]]
+ 00658538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00658538 bytes ca3e05f9
+ 00658538 bytes ca5e05f9
- 00658560 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a78:8"]]
- 00658560 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
+ 00658560 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ab8:8"]]
+ 00658560 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00658560 bytes d53e05f9
+ 00658560 bytes d55e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d731b60bd51c2f1b7c3da6a34bd4ba12"></a>

### [`00658d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/00658d14.md) → [`00658d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/00658d14.md) FUN_00658d14

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 3件 [`006584d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006584d8.md) [`00659a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00659/00659a7c.md) [`00996eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00996/00996eec.md) · 呼出先 31件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00424bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044ba98.md)
- 新版 呼出元 3件 [`006584d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006584d8.md) [`00659a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00659/00659a7c.md) [`00996eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00996/00996eec.md) · 呼出先 31件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00424bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00424/00424bb4.md) [`004253b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00425/004253b4.md) [`0044ba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044ba98.md)

変更の種類 branch_value, call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 96.24% / 新版 96.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00658f38",
      "incomplete_value": true,
      "site": "00658f38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:70c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00658f38",
      "incomplete_value": true,
      "site": "00658f38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:70e:8"
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
      "definition_site": "00658f90",
      "incomplete_value": true,
      "site": "00658f90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:74c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00658f90",
      "incomplete_value": true,
      "site": "00658f90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c1:8"
              ]
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
    "kind": "store_value",
    "new": {
      "definition_site": "00658f98",
      "incomplete_value": true,
      "site": "00658f98",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00658f98",
      "incomplete_value": true,
      "site": "00658f98",
      "value": [
        "LOAD",
        "8",
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
      "00658d60",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00658d74",
      "PARAM",
      [
        "storage",
        "00bf7270",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00658d7c",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00658d60",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00658d74",
      "PARAM",
      [
        "storage",
        "00bf72c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00658d7c",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00658d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/00658d14.md#insn-00658d60) · [`00658d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/00658d14.md#insn-00658d6c) · [`00658d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/00658d14.md#insn-00658d74)
- 新版 [`00658d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/00658d14.md#insn-00658d60) · [`00658d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/00658d14.md#insn-00658d6c) · [`00658d74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/00658d14.md#insn-00658d74)

~~~diff
- 00658d60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 00658d60 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00658d60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00658d60 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00658d60 bytes 003d45f9
+ 00658d60 bytes 005d45f9
- 00658d6c ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00658d6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00658d6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00658d6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00658d6c ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00658d6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00658d6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00658d6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00658d6c bytes 08213991
+ 00658d6c bytes 08613a91
- 00658d74 ["COPY", "tmp:0:8", ["const:270:8"]]
- 00658d74 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00658d74 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00658d74 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00658d74 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 00658d74 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00658d74 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00658d74 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00658d74 bytes 42c00991
+ 00658d74 bytes 42000b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9cb2bd0ad18f745606e37592eeb5d02"></a>

### [`00659a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00659/00659a7c.md) → [`00659a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00659/00659a7c.md) FUN_00659a7c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00824/00824eb0.md) · 呼出先 27件 [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`0044a8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a8d8.md) [`0044beb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044beb4.md) [`0044bf2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044b/0044bf2c.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md)
- 新版 呼出元 1件 [`00824eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00824/00824eb0.md) · 呼出先 27件 [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`0044a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a8d8.md) [`0044beb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044beb4.md) [`0044bf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044b/0044bf2c.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 97.04% / 新版 97.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `store_destination` 7件, `store_value` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0065aaac",
      "incomplete_value": false,
      "site": "0065aaac",
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
      "definition_site": "0065aaac",
      "incomplete_value": false,
      "site": "0065aaac",
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
    "ordinal": 147,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0065aab0",
      "incomplete_value": false,
      "site": "0065aab0",
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
      "definition_site": "0065aab0",
      "incomplete_value": false,
      "site": "0065aab0",
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
    "ordinal": 148,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0065aaac",
      "incomplete_value": false,
      "site": "0065aab0",
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
      "definition_site": "0065aaac",
      "incomplete_value": false,
      "site": "0065aab0",
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
    "ordinal": 148,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00659ac8",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ],
    [
      "00659ae8",
      "PARAM",
      [
        "storage",
        "00be8e48",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00659af0",
      "PARAM",
      [
        "storage",
        "00bf7270",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00659ac8",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ],
    [
      "00659ae8",
      "PARAM",
      [
        "storage",
        "00be8e98",
        null,
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00659af0",
      "PARAM",
      [
        "storage",
        "00bf72c0",
        null,
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00659ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00659/00659a7c.md#insn-00659ac8) · [`00659ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00659/00659a7c.md#insn-00659ae8) · [`00659af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00659/00659a7c.md#insn-00659af0)
- 新版 [`00659ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00659/00659a7c.md#insn-00659ac8) · [`00659ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00659/00659a7c.md#insn-00659ae8) · [`00659af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00659/00659a7c.md#insn-00659af0)

~~~diff
- 00659ac8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a78:8"]]
- 00659ac8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00659ac8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ab8:8"]]
+ 00659ac8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00659ac8 bytes 203d45f9
+ 00659ac8 bytes 205d45f9
- 00659ae8 ["COPY", "tmp:0:8", ["const:e48:8"]]
- 00659ae8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00659ae8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00659ae8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00659ae8 ["COPY", "tmp:0:8", ["const:e98:8"]]
+ 00659ae8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00659ae8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00659ae8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00659ae8 bytes 21203991
+ 00659ae8 bytes 21603a91
- 00659af0 ["COPY", "tmp:0:8", ["const:270:8"]]
- 00659af0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00659af0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00659af0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00659af0 ["COPY", "tmp:0:8", ["const:2c0:8"]]
+ 00659af0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00659af0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00659af0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00659af0 bytes 42c00991
+ 00659af0 bytes 42000b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d91f15e5c0e792932f87d17d6349410c"></a>

### [`0065aad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065a/0065aad8.md) → [`0065aad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065a/0065aad8.md) FUN_0065aad8

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00827/00827ba0.md) · 呼出先 41件 [`00444c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00444/00444c88.md) [`00445d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d04.md) [`00445d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00446/004460b0.md)
- 新版 呼出元 1件 [`00827ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00827/00827ba0.md) · 呼出先 41件 [`00444c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c54.md) [`00444c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00444/00444c88.md) [`00445d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d04.md) [`00445d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00445/00445d88.md) [`004460b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00446/004460b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.91% / 新版 97.91%

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
      "definition_site": "0065ab28",
      "incomplete_value": true,
      "site": "0065ab28",
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
      "definition_site": "0065ab28",
      "incomplete_value": true,
      "site": "0065ab28",
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
      "definition_site": "0065ab38",
      "incomplete_value": true,
      "site": "0065ab38",
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
      "definition_site": "0065ab38",
      "incomplete_value": true,
      "site": "0065ab38",
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
      "definition_site": "0065abc4",
      "incomplete_value": true,
      "site": "0065abc4",
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
      "definition_site": "0065abc4",
      "incomplete_value": true,
      "site": "0065abc4",
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
      "0065ab18",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0065ab24",
      "READ",
      [
        "storage",
        "00c25030",
        null,
        "undefined8"
      ]
    ],
    [
      "0065ab34",
      "READ",
      [
        "storage",
        "00c24a78",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0065ab18",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0065ab24",
      "READ",
      [
        "storage",
        "00c25070",
        null,
        "undefined8"
      ]
    ],
    [
      "0065ab34",
      "READ",
      [
        "storage",
        "00c24ab8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065ab04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065a/0065aad8.md#insn-0065ab04) · [`0065ab24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065a/0065aad8.md#insn-0065ab24) · [`0065ab34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065a/0065aad8.md#insn-0065ab34)
- 新版 [`0065ab04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065a/0065aad8.md#insn-0065ab04) · [`0065ab24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065a/0065aad8.md#insn-0065ab24) · [`0065ab34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065a/0065aad8.md#insn-0065ab34)

~~~diff
- 0065ab04 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0065ab04 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
- 0065ab04 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
- 0065ab04 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
+ 0065ab04 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0065ab04 ["INT_CARRY", "register:105:1", ["register:40c0:8", "tmp:0:8"]]
+ 0065ab04 ["INT_SCARRY", "register:106:1", ["register:40c0:8", "tmp:0:8"]]
+ 0065ab04 ["INT_ADD", "tmp:1:8", ["register:40c0:8", "tmp:0:8"]]
- 0065ab04 bytes 18e30091
+ 0065ab04 bytes 18e30191
- 0065ab24 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:30:8"]]
- 0065ab24 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0065ab24 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:70:8"]]
+ 0065ab24 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0065ab24 bytes e01a40f9
+ 0065ab24 bytes e03a40f9
- 0065ab34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a78:8"]]
- 0065ab34 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0065ab34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 0065ab34 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0065ab34 bytes 003d45f9
+ 0065ab34 bytes 005d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aab0a0077f677b8e2d7b708f3605b950"></a>

### [`0065bcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bcc8.md) → [`0065bcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bcc8.md) FUN_0065bcc8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0065bec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bec4.md) · 呼出先 6件 [`0044c104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044c/0044c104.md) [`006582c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00658/006582c8.md) [`0065bee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bee8.md) [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`0065bec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bec4.md) · 呼出先 6件 [`0044c104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044c/0044c104.md) [`006582c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00658/006582c8.md) [`0065bee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bee8.md) [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.85% / 新版 96.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0065bcdc",
      "incomplete_value": false,
      "site": "0065bce4",
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
            "const:2b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065bcdc",
      "incomplete_value": false,
      "site": "0065bce4",
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
            "const:260:8"
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
      "definition_site": "0065be7c",
      "incomplete_value": false,
      "site": "0065be80",
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
      "definition_site": "0065be7c",
      "incomplete_value": false,
      "site": "0065be80",
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
      "0065bce4",
      "DATA",
      [
        "storage",
        "00bf7260",
        null,
        "pointer"
      ]
    ],
    [
      "0065be80",
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
      "0065bce4",
      "DATA",
      [
        "storage",
        "00bf72b0",
        null,
        "pointer"
      ]
    ],
    [
      "0065be80",
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

- 旧版 [`0065bcdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bcc8.md#insn-0065bcdc) · [`0065be7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bcc8.md#insn-0065be7c)
- 新版 [`0065bcdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bcc8.md#insn-0065bcdc) · [`0065be7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bcc8.md#insn-0065be7c)

~~~diff
- 0065bcdc ["COPY", "tmp:0:8", ["const:260:8"]]
- 0065bcdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065bcdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065bcdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065bcdc ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 0065bcdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065bcdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065bcdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065bcdc bytes 08810991
+ 0065bcdc bytes 08c10a91
- 0065be7c ["COPY", "tmp:0:8", ["const:298:8"]]
- 0065be7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065be7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065be7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065be7c ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 0065be7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065be7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065be7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065be7c bytes 08610a91
+ 0065be7c bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa2b964b37fa49cf89ba386a8bd3f60c"></a>

### [`0065bf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bf90.md) → [`0065bf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bf90.md) FUN_0065bf90

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0065bfa8",
      "incomplete_value": false,
      "site": "0065bfac",
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
      "definition_site": "0065bfa8",
      "incomplete_value": false,
      "site": "0065bfac",
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
      "0065bfac",
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
      "0065bfac",
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

- 旧版 [`0065bfa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bf90.md#insn-0065bfa8)
- 新版 [`0065bfa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bf90.md#insn-0065bfa8)

~~~diff
- 0065bfa8 ["COPY", "tmp:0:8", ["const:298:8"]]
- 0065bfa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065bfa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065bfa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065bfa8 ["COPY", "tmp:0:8", ["const:2e8:8"]]
+ 0065bfa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065bfa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065bfa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065bfa8 bytes 08610a91
+ 0065bfa8 bytes 08a10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14f6c54b8504929c3a1c9ba6f9cc5c69"></a>

### [`0065bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md) → [`0065bff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md) FUN_0065bff4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 27件 [`0065bcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bcc8.md) [`0065bf34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bf34.md) [`0065bf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bf90.md) [`0065c110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065c/0065c110.md) [`00691178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00691/00691178.md) · 呼出先 4件 [`0064c828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0064c/0064c828.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 27件 [`0065bcc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bcc8.md) [`0065bf34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bf34.md) [`0065bf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bf90.md) [`0065c110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065c/0065c110.md) [`00691178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00691/00691178.md) · 呼出先 4件 [`0064c828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0064c/0064c828.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.18% / 新版 97.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0065c010",
      "incomplete_value": true,
      "site": "0065c014",
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
            "const:308:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065c010",
      "incomplete_value": true,
      "site": "0065c014",
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
            "const:2b8:8"
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
      "0065c014",
      "DATA",
      [
        "storage",
        "00bf72b8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0065c014",
      "DATA",
      [
        "storage",
        "00bf7308",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065c010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065b/0065bff4.md#insn-0065c010)
- 新版 [`0065c010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065b/0065bff4.md#insn-0065c010)

~~~diff
- 0065c010 ["COPY", "tmp:0:8", ["const:2b8:8"]]
- 0065c010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065c010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065c010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065c010 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 0065c010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065c010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065c010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065c010 bytes 08e10a91
+ 0065c010 bytes 08210c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b8e5b79d32eb09c7d58cad89dd48093"></a>

### [`0065c278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065c/0065c278.md) → [`0065c278`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065c/0065c278.md) _INIT_95

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.14% / 新版 88.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0065c2b4",
      "incomplete_value": true,
      "site": "0065c2d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0065c2b4",
      "incomplete_value": true,
      "site": "0065c2d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0065c2d8",
      "incomplete_value": true,
      "site": "0065c2f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0065c2d8",
      "incomplete_value": true,
      "site": "0065c2f4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0065c318",
      "incomplete_value": true,
      "site": "0065c330",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0065c318",
      "incomplete_value": true,
      "site": "0065c330",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0065c2b4",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0065c2d8",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0065c2f8",
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
      "0065c2b4",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0065c2d8",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0065c2f8",
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

- 旧版 [`0065c2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065c/0065c278.md#insn-0065c2a4) · [`0065c2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065c/0065c278.md#insn-0065c2ac)
- 新版 [`0065c2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065c/0065c278.md#insn-0065c2a4) · [`0065c2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065c/0065c278.md#insn-0065c2ac)

~~~diff
- 0065c2a4 ["COPY", "tmp:0:8", ["const:730:8"]]
- 0065c2a4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0065c2a4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0065c2a4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0065c2a4 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 0065c2a4 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0065c2a4 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0065c2a4 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0065c2a4 bytes 73c21c91
+ 0065c2a4 bytes 73c21d91
- 0065c2ac ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0065c2ac bytes 49e2fff0
+ 0065c2ac ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0065c2ac bytes 49e2fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37eb247abc46f8b150bf4a2883621fa0"></a>

### [`0065c7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065c/0065c7b4.md) → [`0065c7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065c/0065c7b4.md) FUN_0065c7b4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00659a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00659/00659a7c.md) · 呼出先 20件 [`00419064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459efc.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md)
- 新版 呼出元 1件 [`00659a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00659/00659a7c.md) · 呼出先 20件 [`00419064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00419/00419064.md) [`00449aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00449/00449aec.md) [`00457e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00457/00457e1c.md) [`00459efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459efc.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 98.37% / 新版 98.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0065d0c4",
      "incomplete_value": false,
      "site": "0065d0c4",
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
      "definition_site": "0065d0c4",
      "incomplete_value": false,
      "site": "0065d0c4",
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
    "ordinal": 69,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0065d008",
      "incomplete_value": false,
      "site": "0065d020",
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
      "definition_site": "0065d008",
      "incomplete_value": false,
      "site": "0065d020",
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
    "ordinal": 73,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0065d09c",
      "incomplete_value": false,
      "site": "0065d0a0",
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
      "definition_site": "0065d09c",
      "incomplete_value": false,
      "site": "0065d0a0",
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
    "ordinal": 80,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0065cf68",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "0065cfe4",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "0065d008",
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
      "0065cf68",
      "READ",
      [
        "storage",
        "00c1aeb0",
        null,
        "pointer"
      ]
    ],
    [
      "0065cfe4",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "0065d008",
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

- 旧版 [`0065cf68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065c/0065c7b4.md#insn-0065cf68) · [`0065cfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065c/0065c7b4.md#insn-0065cfe0) · [`0065d008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065c/0065c7b4.md#insn-0065d008)
- 新版 [`0065cf68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065c/0065c7b4.md#insn-0065cf68) · [`0065cfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065c/0065c7b4.md#insn-0065cfe0) · [`0065d008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065c/0065c7b4.md#insn-0065d008)

~~~diff
- 0065cf68 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:e60:8"]]
- 0065cf68 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 0065cf68 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:eb0:8"]]
+ 0065cf68 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 0065cf68 bytes f73247f9
+ 0065cf68 bytes f75a47f9
- 0065cfe0 ["COPY", "tmp:0:8", ["const:38:8"]]
- 0065cfe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065cfe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065cfe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065cfe0 ["COPY", "tmp:0:8", ["const:78:8"]]
+ 0065cfe0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065cfe0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065cfe0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065cfe0 bytes 08e10091
+ 0065cfe0 bytes 08e10191
- 0065d008 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0065d008 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0065d008 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0065d008 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0065d008 ["COPY", "tmp:0:8", ["const:40:8"]]
+ 0065d008 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0065d008 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0065d008 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0065d008 bytes 00000091
+ 0065d008 bytes 00000191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7791bccfc5a657682260490e1336fb35"></a>

### [`0065d980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065d/0065d980.md) → [`0065d980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065d/0065d980.md) _INIT_96

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "0065d9bc",
      "incomplete_value": true,
      "site": "0065d9d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0065d9bc",
      "incomplete_value": true,
      "site": "0065d9d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0065d9e0",
      "incomplete_value": true,
      "site": "0065d9fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0065d9e0",
      "incomplete_value": true,
      "site": "0065d9fc",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0065da20",
      "incomplete_value": true,
      "site": "0065da38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0065da20",
      "incomplete_value": true,
      "site": "0065da38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0065d9bc",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0065d9e0",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0065da00",
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
      "0065d9bc",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0065d9e0",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0065da00",
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

- 旧版 [`0065d9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065d/0065d980.md#insn-0065d9ac) · [`0065d9b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065d/0065d980.md#insn-0065d9b4)
- 新版 [`0065d9ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065d/0065d980.md#insn-0065d9ac) · [`0065d9b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065d/0065d980.md#insn-0065d9b4)

~~~diff
- 0065d9ac ["COPY", "tmp:0:8", ["const:748:8"]]
- 0065d9ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0065d9ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0065d9ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0065d9ac ["COPY", "tmp:0:8", ["const:788:8"]]
+ 0065d9ac ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0065d9ac ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0065d9ac ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0065d9ac bytes 73221d91
+ 0065d9ac bytes 73221e91
- 0065d9b4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0065d9b4 bytes 49e2ffd0
+ 0065d9b4 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0065d9b4 bytes 49e2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd983949fbc13a27528d2aba66114dee"></a>

### [`0065dd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065d/0065dd10.md) → [`0065dd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065d/0065dd10.md) _INIT_97

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 91.53% / 新版 91.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0065de0c",
      "incomplete_value": true,
      "site": "0065de50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "old": {
      "definition_site": "0065de0c",
      "incomplete_value": true,
      "site": "0065de50",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "ordinal": 40,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0065df38",
      "incomplete_value": false,
      "site": "0065df44",
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
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065df38",
      "incomplete_value": false,
      "site": "0065df44",
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
            "const:760:8"
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
      "definition_site": "0065df40",
      "incomplete_value": false,
      "site": "0065df44",
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
      "definition_site": "0065df40",
      "incomplete_value": false,
      "site": "0065df44",
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
      "0065dd4c",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0065dd70",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0065dd90",
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
      "0065dd4c",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0065dd70",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0065dd90",
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

- 旧版 [`0065dd3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065d/0065dd10.md#insn-0065dd3c) · [`0065dd44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065d/0065dd10.md#insn-0065dd44)
- 新版 [`0065dd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065d/0065dd10.md#insn-0065dd3c) · [`0065dd44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065d/0065dd10.md#insn-0065dd44)

~~~diff
- 0065dd3c ["COPY", "tmp:0:8", ["const:760:8"]]
- 0065dd3c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0065dd3c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0065dd3c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0065dd3c ["COPY", "tmp:0:8", ["const:7a0:8"]]
+ 0065dd3c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0065dd3c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0065dd3c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0065dd3c bytes 73821d91
+ 0065dd3c bytes 73821e91
- 0065dd44 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0065dd44 bytes 49e2ffd0
+ 0065dd44 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0065dd44 bytes 49e2ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6a69e9d4e3fdf075457c99cf9d4acd48"></a>

### [`0065e23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065e23c.md) → [`0065e23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065e23c.md) FUN_0065e23c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ac9054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ac9/00ac9054.md) · 呼出先 11件 [`00464a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a54.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md) [`0065e0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065e0a0.md) [`0066b744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066b/0066b744.md)
- 新版 呼出元 1件 [`00ac9098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ac9/00ac9098.md) · 呼出先 11件 [`00464a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a54.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md) [`0065e0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065e0a0.md) [`0066b744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066b/0066b744.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.34% / 新版 91.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0065e274",
      "incomplete_value": false,
      "site": "0065e278",
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
      "definition_site": "0065e274",
      "incomplete_value": false,
      "site": "0065e278",
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
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0065e398",
      "incomplete_value": true,
      "site": "0065e39c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0065e398",
      "incomplete_value": true,
      "site": "0065e39c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0065e394",
      "incomplete_value": true,
      "site": "0065e3a0",
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
      "definition_site": "0065e394",
      "incomplete_value": true,
      "site": "0065e3a0",
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
      "0065e278",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0065e290",
      "READ",
      [
        "storage",
        "002a0851",
        null,
        "string"
      ]
    ],
    [
      "0065e298",
      "READ",
      [
        "storage",
        "002a0858",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0065e278",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0065e290",
      "READ",
      [
        "storage",
        "002a08dc",
        null,
        "string"
      ]
    ],
    [
      "0065e298",
      "READ",
      [
        "storage",
        "002a08e3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065e274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065e23c.md#insn-0065e274) · [`0065e28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065e23c.md#insn-0065e28c) · [`0065e388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065e23c.md#insn-0065e388)
- 新版 [`0065e274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065e23c.md#insn-0065e274) · [`0065e28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065e23c.md#insn-0065e28c) · [`0065e388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065e23c.md#insn-0065e388)

~~~diff
- 0065e274 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0065e274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065e274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065e274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065e274 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0065e274 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065e274 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065e274 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065e274 bytes 08a13491
+ 0065e274 bytes 08e13591
- 0065e28c ["COPY", "tmp:0:8", ["const:851:8"]]
- 0065e28c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0065e28c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0065e28c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0065e28c ["COPY", "tmp:0:8", ["const:8dc:8"]]
+ 0065e28c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0065e28c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0065e28c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0065e28c bytes 29452191
+ 0065e28c bytes 29712391
- 0065e388 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 0065e388 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0065e388 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 0065e388 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0065e388 bytes 08b946f9
+ 0065e388 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbe913b39383567d47ebb65bd1730a06"></a>

### [`0065ef18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065ef18.md) → [`0065ef18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065ef18.md) FUN_0065ef18

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00a17ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a17/00a17ce0.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041fdf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041fdf0.md) [`0066c150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0066c/0066c150.md)
- 新版 呼出元 1件 [`00a17d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a17/00a17d24.md) · 呼出先 3件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041fdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041fdf0.md) [`0066c150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0066c/0066c150.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0065efa8",
      "incomplete_value": false,
      "site": "0065efac",
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
            "const:65a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065efa8",
      "incomplete_value": false,
      "site": "0065efac",
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
      "0065efa8",
      "PARAM",
      [
        "storage",
        "002a35cf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0065efa8",
      "PARAM",
      [
        "storage",
        "002a365a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0065efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065e/0065ef18.md#insn-0065efa8)
- 新版 [`0065efa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065e/0065ef18.md#insn-0065efa8)

~~~diff
- 0065efa8 ["COPY", "tmp:0:8", ["const:5cf:8"]]
- 0065efa8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0065efa8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0065efa8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0065efa8 ["COPY", "tmp:0:8", ["const:65a:8"]]
+ 0065efa8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0065efa8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0065efa8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0065efa8 bytes 003c1791
+ 0065efa8 bytes 00681991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ec018e8e47bb58b500ad85c79a4ef20"></a>

### [`0065f7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f7b4.md) → [`0065f7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f7b4.md) FUN_0065f7b4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`006612ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006612ac.md) · 呼出先 20件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/0046555c.md) [`00465780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00465/00465780.md)
- 新版 呼出元 1件 [`006612ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/006612ac.md) · 呼出先 20件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00464f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464f48.md) [`0046555c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/0046555c.md) [`00465780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00465/00465780.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.70% / 新版 94.70%

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
      "definition_site": "0065f7f8",
      "incomplete_value": false,
      "site": "0065f7fc",
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
      "definition_site": "0065f7f8",
      "incomplete_value": false,
      "site": "0065f7fc",
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
      "definition_site": "0065f814",
      "incomplete_value": true,
      "site": "0065f828",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:818:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065f814",
      "incomplete_value": true,
      "site": "0065f828",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:77e:8"
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
      "definition_site": "0065fad8",
      "incomplete_value": true,
      "site": "0065fadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0065fad8",
      "incomplete_value": true,
      "site": "0065fadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "0065f7fc",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0065f814",
      "READ",
      [
        "storage",
        "002a777e",
        null,
        "string"
      ]
    ],
    [
      "0065fac8",
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
      "0065f7fc",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0065f814",
      "READ",
      [
        "storage",
        "002a7818",
        null,
        "string"
      ]
    ],
    [
      "0065fac8",
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

- 旧版 [`0065f7f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f7b4.md#insn-0065f7f8) · [`0065f80c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f7b4.md#insn-0065f80c) · [`0065fac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065f7b4.md#insn-0065fac8)
- 新版 [`0065f7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f7b4.md#insn-0065f7f8) · [`0065f80c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f7b4.md#insn-0065f80c) · [`0065fac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065f7b4.md#insn-0065fac8)

~~~diff
- 0065f7f8 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0065f7f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065f7f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065f7f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065f7f8 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0065f7f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065f7f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065f7f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065f7f8 bytes 08a13491
+ 0065f7f8 bytes 08e13591
- 0065f80c ["COPY", "tmp:0:8", ["const:77e:8"]]
- 0065f80c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0065f80c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0065f80c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0065f80c ["COPY", "tmp:0:8", ["const:818:8"]]
+ 0065f80c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0065f80c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0065f80c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0065f80c bytes 29f91d91
+ 0065f80c bytes 29612091
- 0065fac8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 0065fac8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0065fac8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 0065fac8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0065fac8 bytes 08b946f9
+ 0065fac8 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7842c31e29eabf07055330f9d9b51eda"></a>

### [`0065fcc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065fcc0.md) → [`0065fcc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065fcc0.md) FUN_0065fcc0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`006612ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006612ac.md) · 呼出先 18件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464b8c.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md)
- 新版 呼出元 1件 [`006612ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/006612ac.md) · 呼出先 18件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464b8c.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

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
      "definition_site": "0065fd04",
      "incomplete_value": false,
      "site": "0065fd0c",
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
      "definition_site": "0065fd04",
      "incomplete_value": false,
      "site": "0065fd0c",
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
      "definition_site": "0065fd24",
      "incomplete_value": true,
      "site": "0065fd38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:b73:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0065fd24",
      "incomplete_value": true,
      "site": "0065fd38",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:c00:8"
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
      "definition_site": "0065ff60",
      "incomplete_value": true,
      "site": "0065ff64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "0065ff60",
      "incomplete_value": true,
      "site": "0065ff64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0065fd0c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "0065fd24",
      "READ",
      [
        "storage",
        "00294c00",
        null,
        "string"
      ]
    ],
    [
      "0065ff50",
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
      "0065fd0c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "0065fd24",
      "READ",
      [
        "storage",
        "00294b73",
        null,
        "string"
      ]
    ],
    [
      "0065ff50",
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

- 旧版 [`0065fd04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065fcc0.md#insn-0065fd04) · [`0065fd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065fcc0.md#insn-0065fd1c) · [`0065ff50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0065f/0065fcc0.md#insn-0065ff50)
- 新版 [`0065fd04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065fcc0.md#insn-0065fd04) · [`0065fd1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065fcc0.md#insn-0065fd1c) · [`0065ff50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0065f/0065fcc0.md#insn-0065ff50)

~~~diff
- 0065fd04 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 0065fd04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0065fd04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0065fd04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0065fd04 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 0065fd04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0065fd04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0065fd04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0065fd04 bytes 08a13491
+ 0065fd04 bytes 08e13591
- 0065fd1c ["COPY", "tmp:0:8", ["const:c00:8"]]
- 0065fd1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0065fd1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0065fd1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0065fd1c ["COPY", "tmp:0:8", ["const:b73:8"]]
+ 0065fd1c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0065fd1c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0065fd1c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0065fd1c bytes 29013091
+ 0065fd1c bytes 29cd2d91
- 0065ff50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d70:8"]]
- 0065ff50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0065ff50 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dc0:8"]]
+ 0065ff50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0065ff50 bytes 08b946f9
+ 0065ff50 bytes 08e146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e09f426808f086aa0847c58868c92aa"></a>

### [`00660120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660120.md) → [`00660120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660120.md) FUN_00660120

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`006612ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00661/006612ac.md) · 呼出先 16件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00464/00464ca8.md)
- 新版 呼出元 1件 [`006612ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00661/006612ac.md) · 呼出先 16件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`00464a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a44.md) [`00464a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464a64.md) [`00464ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00464/00464ca8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 90.40% / 新版 90.40%

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
      "definition_site": "00660164",
      "incomplete_value": false,
      "site": "0066016c",
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
      "definition_site": "00660164",
      "incomplete_value": false,
      "site": "0066016c",
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
      "definition_site": "00660188",
      "incomplete_value": true,
      "site": "00660198",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:722:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00660188",
      "incomplete_value": true,
      "site": "00660198",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:724:8"
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
      "definition_site": "0066019c",
      "incomplete_value": true,
      "site": "0066019c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0066019c",
      "incomplete_value": true,
      "site": "0066019c",
      "value": [
        "LOAD",
        "8",
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
      "0066016c",
      "DATA",
      [
        "storage",
        "00be7d28",
        null,
        "undefined *"
      ]
    ],
    [
      "00660188",
      "READ",
      [
        "storage",
        "0029b724",
        null,
        "string"
      ]
    ],
    [
      "0066018c",
      "READ",
      [
        "storage",
        "0029b733",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0066016c",
      "DATA",
      [
        "storage",
        "00be7d78",
        null,
        "undefined *"
      ]
    ],
    [
      "00660188",
      "READ",
      [
        "storage",
        "0029b722",
        null,
        "string"
      ]
    ],
    [
      "0066018c",
      "READ",
      [
        "storage",
        "0029b731",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00660164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660120.md#insn-00660164) · [`00660180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660120.md#insn-00660180) · [`00660184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00660/00660120.md#insn-00660184)
- 新版 [`00660164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660120.md#insn-00660164) · [`00660180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00660/00660120.md#insn-00660180)

~~~diff
- 00660164 ["COPY", "tmp:0:8", ["const:d28:8"]]
- 00660164 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00660164 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00660164 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00660164 ["COPY", "tmp:0:8", ["const:d78:8"]]
+ 00660164 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00660164 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00660164 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00660164 bytes 29a13491
+ 00660164 bytes 29e13591
- 00660180 ["COPY", "tmp:0:8", ["const:724:8"]]
- 00660180 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00660180 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00660180 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00660180 ["COPY", "tmp:0:8", ["const:722:8"]]
+ 00660180 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00660180 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00660180 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00660180 bytes 08911c91
+ 00660180 bytes 08891c91
- 00660184 ["COPY", "register:4048:8", ["const:2b0000:8"]]
- 00660184 bytes 89e2ff90
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

