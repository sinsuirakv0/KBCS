# v15.7.3 → v15.7.4 · 最優先の変更候補 (50)

[一覧の目次](README.md)

<a id="compare-4a86b9a700c3a2390a24d76ebf663a4a"></a>

### [`00973970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973970.md) → [`00973970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00973/00973970.md) FUN_00973970

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0097ffb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097ffb0.md) · 呼出先 9件 [`00469fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469fac.md) [`007cd560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007cd/007cd560.md) [`009d6a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6a64.md) [`009d6ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d6/009d6ae4.md) [`009d750c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009d7/009d750c.md)
- 新版 呼出元 1件 [`0097ffb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097ffb0.md) · 呼出先 9件 [`00469fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469fac.md) [`007cd560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/007cd/007cd560.md) [`009d6aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d6/009d6aa8.md) [`009d6b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d6/009d6b28.md) [`009d7550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009d7/009d7550.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.91% / 新版 98.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009739cc",
      "incomplete_value": false,
      "site": "009739dc",
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
    "old": {
      "definition_site": "009739cc",
      "incomplete_value": false,
      "site": "009739dc",
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
      "009739cc",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "009739cc",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009739cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973970.md#insn-009739cc)
- 新版 `009739cc`（命令位置の公開資料なし）

~~~diff
- 009739cc ["COPY", "tmp:0:8", ["const:866:8"]]
- 009739cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009739cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009739cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009739cc ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 009739cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009739cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009739cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009739cc bytes 21982191
+ 009739cc bytes 21641f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dda0508884673c7df231c11c8446505d"></a>

### [`00973b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973b10.md) → [`00973b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00973/00973b10.md) FUN_00973b10

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`009743fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00974/009743fc.md) · 呼出先 15件 [`00428c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428c14.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0053ee5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`00975468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975468.md)
- 新版 呼出元 1件 [`009743fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00974/009743fc.md) · 呼出先 15件 [`00428c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428c14.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0053ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md) [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) [`00975468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/00975468.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.88% / 新版 94.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00973d20",
      "incomplete_value": true,
      "site": "00973d20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00973d20",
      "incomplete_value": true,
      "site": "00973d20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00973d18",
      "incomplete_value": true,
      "site": "00973d2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:324:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00973d18",
      "incomplete_value": true,
      "site": "00973d2c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:299:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 44,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00973d80",
      "incomplete_value": true,
      "site": "00973d80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00973d80",
      "incomplete_value": true,
      "site": "00973d80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 46,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00973b8c",
      "PARAM",
      [
        "storage",
        "002a6e3b",
        null,
        "string"
      ]
    ],
    [
      "00973bf0",
      "PARAM",
      [
        "storage",
        "002a88ed",
        null,
        "string"
      ]
    ],
    [
      "00973c60",
      "PARAM",
      [
        "storage",
        "002a29bb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00973b8c",
      "PARAM",
      [
        "storage",
        "002a6ed5",
        null,
        "string"
      ]
    ],
    [
      "00973bf0",
      "PARAM",
      [
        "storage",
        "002a8987",
        null,
        "string"
      ]
    ],
    [
      "00973c60",
      "PARAM",
      [
        "storage",
        "002a2a46",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00973b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973b10.md#insn-00973b8c) · [`00973bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973b10.md#insn-00973bf0) · [`00973c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973b10.md#insn-00973c60)
- 新版 `00973b8c`（命令位置の公開資料なし） · `00973bf0`（命令位置の公開資料なし） · `00973c60`（命令位置の公開資料なし）

~~~diff
- 00973b8c ["COPY", "tmp:0:8", ["const:e3b:8"]]
- 00973b8c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00973b8c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00973b8c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00973b8c ["COPY", "tmp:0:8", ["const:ed5:8"]]
+ 00973b8c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00973b8c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00973b8c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00973b8c bytes 21ec3891
+ 00973b8c bytes 21543b91
- 00973bf0 ["COPY", "tmp:0:8", ["const:8ed:8"]]
- 00973bf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00973bf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00973bf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00973bf0 ["COPY", "tmp:0:8", ["const:987:8"]]
+ 00973bf0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00973bf0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00973bf0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00973bf0 bytes 21b42391
+ 00973bf0 bytes 211c2691
- 00973c60 ["COPY", "tmp:0:8", ["const:9bb:8"]]
- 00973c60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00973c60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00973c60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00973c60 ["COPY", "tmp:0:8", ["const:a46:8"]]
+ 00973c60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00973c60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00973c60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00973c60 bytes 21ec2691
+ 00973c60 bytes 21182991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a56c455c07e0be22b6fce154b1138205"></a>

### [`009743fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00974/009743fc.md) → [`009743fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00974/009743fc.md) FUN_009743fc

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00989a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/00989a48.md) · 呼出先 16件 [`00428c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00428/00428c14.md) [`0053ee5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0053e/0053ee5c.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`00973b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973b10.md) [`00975ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975ac0.md)
- 新版 呼出元 1件 [`00989a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989a48.md) · 呼出先 16件 [`00428c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00428/00428c14.md) [`0053ee5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0053e/0053ee5c.md) [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) [`00973b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00973/00973b10.md) [`00975ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/00975ac0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_value` 4件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097444c",
      "incomplete_value": false,
      "site": "0097444c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097444c",
      "incomplete_value": false,
      "site": "0097444c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:688:8"
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
      "definition_site": "00974620",
      "incomplete_value": true,
      "site": "00974620",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00974620",
      "incomplete_value": true,
      "site": "00974620",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00974624",
      "incomplete_value": true,
      "site": "00974624",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00974624",
      "incomplete_value": true,
      "site": "00974624",
      "value": [
        "LOAD",
        "8",
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
      "0097444c",
      "DATA",
      [
        "storage",
        "00c0a688",
        null,
        "undefined *"
      ]
    ],
    [
      "009744a8",
      "PARAM",
      [
        "storage",
        "002a6e3b",
        null,
        "string"
      ]
    ],
    [
      "0097450c",
      "PARAM",
      [
        "storage",
        "002a88ed",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0097444c",
      "DATA",
      [
        "storage",
        "00c0a6d8",
        null,
        "undefined *"
      ]
    ],
    [
      "009744a8",
      "PARAM",
      [
        "storage",
        "002a6ed5",
        null,
        "string"
      ]
    ],
    [
      "0097450c",
      "PARAM",
      [
        "storage",
        "002a8987",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00974440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00974/009743fc.md#insn-00974440) · [`009744a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00974/009743fc.md#insn-009744a8) · [`0097450c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00974/009743fc.md#insn-0097450c)
- 新版 `00974440`（命令位置の公開資料なし） · `009744a8`（命令位置の公開資料なし） · `0097450c`（命令位置の公開資料なし）

~~~diff
- 00974440 ["COPY", "tmp:0:8", ["const:688:8"]]
- 00974440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00974440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00974440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00974440 ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 00974440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00974440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00974440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00974440 bytes 08211a91
+ 00974440 bytes 08611b91
- 009744a8 ["COPY", "tmp:0:8", ["const:e3b:8"]]
- 009744a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 009744a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 009744a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 009744a8 ["COPY", "tmp:0:8", ["const:ed5:8"]]
+ 009744a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 009744a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 009744a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 009744a8 bytes 21ec3891
+ 009744a8 bytes 21543b91
- 0097450c ["COPY", "tmp:0:8", ["const:8ed:8"]]
- 0097450c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0097450c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0097450c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0097450c ["COPY", "tmp:0:8", ["const:987:8"]]
+ 0097450c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0097450c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0097450c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0097450c bytes 21b42391
+ 0097450c bytes 211c2691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8fb4bf06bc66bb351227a6d47cb98268"></a>

### [`009752b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/009752b8.md) → [`009752b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/009752b8.md) FUN_009752b8

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
      "definition_site": "009752d0",
      "incomplete_value": false,
      "site": "009752dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009752d0",
      "incomplete_value": false,
      "site": "009752dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "009752dc",
      "DATA",
      [
        "storage",
        "00c0a608",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009752dc",
      "DATA",
      [
        "storage",
        "00c0a658",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009752d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/009752b8.md#insn-009752d0)
- 新版 `009752d0`（命令位置の公開資料なし）

~~~diff
- 009752d0 ["COPY", "tmp:0:8", ["const:608:8"]]
- 009752d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009752d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009752d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009752d0 ["COPY", "tmp:0:8", ["const:658:8"]]
+ 009752d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009752d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009752d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009752d0 bytes 08211891
+ 009752d0 bytes 08611991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3d45f927909ce58a621fef9670e0058"></a>

### [`00975314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975314.md) → [`00975314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/00975314.md) FUN_00975314

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097533c",
      "incomplete_value": false,
      "site": "00975340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097533c",
      "incomplete_value": false,
      "site": "00975340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "00975340",
      "DATA",
      [
        "storage",
        "00c0a608",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00975340",
      "DATA",
      [
        "storage",
        "00c0a658",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097533c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975314.md#insn-0097533c)
- 新版 `0097533c`（命令位置の公開資料なし）

~~~diff
- 0097533c ["COPY", "tmp:0:8", ["const:608:8"]]
- 0097533c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097533c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097533c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097533c ["COPY", "tmp:0:8", ["const:658:8"]]
+ 0097533c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097533c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097533c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097533c bytes 29211891
+ 0097533c bytes 29611991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e021957d7629f02b6372e4b038e1307"></a>

### [`009753ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/009753ac.md) → [`009753ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/009753ac.md) FUN_009753ac

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009753cc",
      "incomplete_value": false,
      "site": "009753d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:658:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009753cc",
      "incomplete_value": false,
      "site": "009753d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:608:8"
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
      "009753d0",
      "DATA",
      [
        "storage",
        "00c0a608",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009753d0",
      "DATA",
      [
        "storage",
        "00c0a658",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009753cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/009753ac.md#insn-009753cc)
- 新版 `009753cc`（命令位置の公開資料なし）

~~~diff
- 009753cc ["COPY", "tmp:0:8", ["const:608:8"]]
- 009753cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009753cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009753cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009753cc ["COPY", "tmp:0:8", ["const:658:8"]]
+ 009753cc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009753cc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009753cc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009753cc bytes 29211891
+ 009753cc bytes 29611991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c97f1c9c60831967aa906b1e8ed7f5da"></a>

### [`009754b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/009754b8.md) → [`009754b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/009754b8.md) FUN_009754b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00574054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574054.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 0件  · 呼出先 8件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00574054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00975684",
      "incomplete_value": true,
      "site": "00975684",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00975684",
      "incomplete_value": true,
      "site": "00975684",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:356:8"
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
      "definition_site": "00975678",
      "incomplete_value": true,
      "site": "00975688",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00975678",
      "incomplete_value": true,
      "site": "00975688",
      "value": [
        "LOAD",
        "8",
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
      "00975674",
      "READ",
      [
        "storage",
        "002a8356",
        null,
        "string"
      ]
    ],
    [
      "00975678",
      "READ",
      [
        "storage",
        "002a835d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00975674",
      "READ",
      [
        "storage",
        "002a83f0",
        null,
        "string"
      ]
    ],
    [
      "00975678",
      "READ",
      [
        "storage",
        "002a83f7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097566c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/009754b8.md#insn-0097566c)
- 新版 `0097566c`（命令位置の公開資料なし）

~~~diff
- 0097566c ["COPY", "tmp:0:8", ["const:356:8"]]
- 0097566c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097566c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097566c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097566c ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 0097566c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097566c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097566c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097566c bytes 29590d91
+ 0097566c bytes 29c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-886e7f777226a5d4d38349046466fb6a"></a>

### [`00975a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975a8c.md) → [`00975a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/00975a8c.md) FUN_00975a8c

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
      "definition_site": "00975aa0",
      "incomplete_value": false,
      "site": "00975aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00975aa0",
      "incomplete_value": false,
      "site": "00975aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:688:8"
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
      "00975aa4",
      "DATA",
      [
        "storage",
        "00c0a688",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00975aa4",
      "DATA",
      [
        "storage",
        "00c0a6d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00975aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975a8c.md#insn-00975aa0)
- 新版 `00975aa0`（命令位置の公開資料なし）

~~~diff
- 00975aa0 ["COPY", "tmp:0:8", ["const:688:8"]]
- 00975aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00975aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00975aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00975aa0 ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 00975aa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00975aa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00975aa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00975aa0 bytes 08211a91
+ 00975aa0 bytes 08611b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-48500a6d3885ac71c2ad430d2049cce9"></a>

### [`00975ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975ab0.md) → [`00975ab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/00975ab0.md) FUN_00975ab0

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
      "definition_site": "00975ab4",
      "incomplete_value": false,
      "site": "00975ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:6d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00975ab4",
      "incomplete_value": false,
      "site": "00975ab8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:688:8"
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
      "00975ab8",
      "DATA",
      [
        "storage",
        "00c0a688",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00975ab8",
      "DATA",
      [
        "storage",
        "00c0a6d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00975ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975ab0.md#insn-00975ab4)
- 新版 `00975ab4`（命令位置の公開資料なし）

~~~diff
- 00975ab4 ["COPY", "tmp:0:8", ["const:688:8"]]
- 00975ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00975ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00975ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00975ab4 ["COPY", "tmp:0:8", ["const:6d8:8"]]
+ 00975ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00975ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00975ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00975ab4 bytes 08211a91
+ 00975ab4 bytes 08611b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f79773e0f8375e6fd4d5745ce63a1aa"></a>

### [`00975af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975af8.md) → [`00975af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/00975af8.md) FUN_00975af8

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
      "definition_site": "00975b1c",
      "incomplete_value": false,
      "site": "00975b1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00975b1c",
      "incomplete_value": false,
      "site": "00975b1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:708:8"
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
      "00975b1c",
      "DATA",
      [
        "storage",
        "00c0a708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00975b1c",
      "DATA",
      [
        "storage",
        "00c0a758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00975b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975af8.md#insn-00975b18)
- 新版 `00975b18`（命令位置の公開資料なし）

~~~diff
- 00975b18 ["COPY", "tmp:0:8", ["const:708:8"]]
- 00975b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00975b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00975b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00975b18 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00975b18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00975b18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00975b18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00975b18 bytes 08211c91
+ 00975b18 bytes 08611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-023507035b97610e16085ce60f5a6631"></a>

### [`00975b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975b2c.md) → [`00975b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/00975b2c.md) FUN_00975b2c

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
      "definition_site": "00975b38",
      "incomplete_value": false,
      "site": "00975b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:758:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00975b38",
      "incomplete_value": false,
      "site": "00975b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:708:8"
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
      "00975b38",
      "DATA",
      [
        "storage",
        "00c0a708",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00975b38",
      "DATA",
      [
        "storage",
        "00c0a758",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00975b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975b2c.md#insn-00975b34)
- 新版 `00975b34`（命令位置の公開資料なし）

~~~diff
- 00975b34 ["COPY", "tmp:0:8", ["const:708:8"]]
- 00975b34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00975b34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00975b34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00975b34 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00975b34 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00975b34 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00975b34 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00975b34 bytes 29211c91
+ 00975b34 bytes 29611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e1926e342a185402f671bfcd9edbd81"></a>

### [`00975b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975b48.md) → [`00975b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/00975b48.md) FUN_00975b48

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00574054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574054.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00574054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574054.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.17% / 新版 98.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00975c74",
      "incomplete_value": true,
      "site": "00975c74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00975c74",
      "incomplete_value": true,
      "site": "00975c74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:356:8"
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
      "definition_site": "00975c68",
      "incomplete_value": true,
      "site": "00975c78",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00975c68",
      "incomplete_value": true,
      "site": "00975c78",
      "value": [
        "LOAD",
        "8",
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
      "00975c64",
      "READ",
      [
        "storage",
        "002a8356",
        null,
        "string"
      ]
    ],
    [
      "00975c68",
      "READ",
      [
        "storage",
        "002a835d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00975c64",
      "READ",
      [
        "storage",
        "002a83f0",
        null,
        "string"
      ]
    ],
    [
      "00975c68",
      "READ",
      [
        "storage",
        "002a83f7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00975c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975b48.md#insn-00975c5c)
- 新版 `00975c5c`（命令位置の公開資料なし）

~~~diff
- 00975c5c ["COPY", "tmp:0:8", ["const:356:8"]]
- 00975c5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00975c5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00975c5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00975c5c ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 00975c5c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00975c5c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00975c5c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00975c5c bytes 29590d91
+ 00975c5c bytes 29c10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35fce96dd0adad045355b2851f3c6535"></a>

### [`009763c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/009763c8.md) → [`009763c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/009763c8.md) FUN_009763c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00976040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976040.md) [`00976638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976638.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00976040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976040.md) [`00976638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976638.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "009763d4",
      "incomplete_value": false,
      "site": "009763d8",
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
      "definition_site": "009763d4",
      "incomplete_value": false,
      "site": "009763d8",
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
      "009763d4",
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
      "009763d4",
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

- 旧版 [`009763d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/009763c8.md#insn-009763d4)
- 新版 `009763d4`（命令位置の公開資料なし）

~~~diff
- 009763d4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 009763d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 009763d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 009763d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 009763d4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 009763d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 009763d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 009763d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 009763d4 bytes 000c0c91
+ 009763d4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26c4500feeb4289e830b57e9f4195335"></a>

### [`009767c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/009767c4.md) → [`009767c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/009767c4.md) _INIT_190

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 90.96% / 新版 90.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00976824",
      "incomplete_value": true,
      "site": "00976840",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00976824",
      "incomplete_value": true,
      "site": "00976840",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00976844",
      "incomplete_value": true,
      "site": "00976860",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "00976844",
      "incomplete_value": true,
      "site": "00976860",
      "value": [
        "LOAD",
        "16",
        [
          [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "009769ec",
      "incomplete_value": false,
      "site": "009769f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109e000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009769ec",
      "incomplete_value": false,
      "site": "009769f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:109e000:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "00976800",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "00976824",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "00976844",
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
      "00976800",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "00976824",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "00976844",
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

- 旧版 [`009767f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/009767c4.md#insn-009767f0) · [`009767f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/009767c4.md#insn-009767f8)
- 新版 `009767f0`（命令位置の公開資料なし） · `009767f8`（命令位置の公開資料なし）

~~~diff
- 009767f0 ["COPY", "tmp:0:8", ["const:968:8"]]
- 009767f0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 009767f0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 009767f0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 009767f0 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 009767f0 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 009767f0 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 009767f0 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 009767f0 bytes 73a22591
+ 009767f0 bytes 73a22691
- 009767f8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 009767f8 bytes 89c9ffb0
+ 009767f8 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 009767f8 bytes 89c9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b61a2b03d8693407fb367e49ddcdc5ec"></a>

### [`00976fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976fb0.md) → [`00976fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976fb0.md) FUN_00976fb0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00a2c36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a2c/00a2c36c.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00837f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00837/00837f3c.md) [`00973680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973680.md) [`00973ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973ae8.md) [`00976638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976638.md)
- 新版 呼出元 1件 [`00a2c3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a2c/00a2c3b0.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00837f3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00837/00837f3c.md) [`00973680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00973/00973680.md) [`00973ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00973/00973ae8.md) [`00976638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976638.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097711c",
      "incomplete_value": false,
      "site": "00977128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097711c",
      "incomplete_value": false,
      "site": "00977128",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "00977128",
      "DATA",
      [
        "storage",
        "00c0a788",
        null,
        "pointer"
      ]
    ],
    [
      "00977198",
      "READ",
      [
        "storage",
        "00c0a798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00977128",
      "DATA",
      [
        "storage",
        "00c0a7d8",
        null,
        "pointer"
      ]
    ],
    [
      "00977198",
      "READ",
      [
        "storage",
        "00c0a7e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976fb0.md#insn-0097711c)
- 新版 `0097711c`（命令位置の公開資料なし）

~~~diff
- 0097711c ["COPY", "tmp:0:8", ["const:788:8"]]
- 0097711c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097711c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097711c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097711c ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 0097711c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097711c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097711c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097711c bytes 08211e91
+ 0097711c bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de5336f2351349250d50815df2d80023"></a>

### [`00977828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00977/00977828.md) → [`00977828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977828.md) FUN_00977828

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073a198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a198.md) · 呼出先 11件 [`0097af60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097af60.md) [`0097af6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097af6c.md) [`0097de84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097de84.md) [`0097e4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097e4d8.md) [`0097ffb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097ffb0.md)
- 新版 呼出元 1件 [`0073a198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a198.md) · 呼出先 11件 [`0097af60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097af60.md) [`0097af6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097af6c.md) [`0097de84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097d/0097de84.md) [`0097e4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097e4d8.md) [`0097ffb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097ffb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00977978",
      "incomplete_value": false,
      "site": "00977984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00977978",
      "incomplete_value": false,
      "site": "00977984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "00977984",
      "DATA",
      [
        "storage",
        "00c0a788",
        null,
        "pointer"
      ]
    ],
    [
      "00977a3c",
      "READ",
      [
        "storage",
        "00c0a798",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00977984",
      "DATA",
      [
        "storage",
        "00c0a7d8",
        null,
        "pointer"
      ]
    ],
    [
      "00977a3c",
      "READ",
      [
        "storage",
        "00c0a7e8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00977978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00977/00977828.md#insn-00977978)
- 新版 `00977978`（命令位置の公開資料なし）

~~~diff
- 00977978 ["COPY", "tmp:0:8", ["const:788:8"]]
- 00977978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00977978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00977978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00977978 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 00977978 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00977978 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00977978 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00977978 bytes 08211e91
+ 00977978 bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd6b8b363b02888aec87bd4734c09f44"></a>

### [`009785f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/009785f0.md) → [`009785f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/009785f0.md) FUN_009785f0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`00761844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00761/00761844.md) [`009785f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/009785f0.md) [`0097c594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c594.md) [`00a3371c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a33/00a3371c.md) · 呼出先 15件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`009785f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/009785f0.md) [`0097c514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c514.md) [`0097c938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c938.md)
- 新版 呼出元 4件 [`00761844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00761/00761844.md) [`009785f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/009785f0.md) [`0097c594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c594.md) [`00a33760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a33/00a33760.md) · 呼出先 15件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) [`009785f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/009785f0.md) [`0097c514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c514.md) [`0097c938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c938.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.80% / 新版 98.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009787f8",
      "incomplete_value": false,
      "site": "00978804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009787f8",
      "incomplete_value": false,
      "site": "00978804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009788c8",
      "incomplete_value": false,
      "site": "009788c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009788c8",
      "incomplete_value": false,
      "site": "009788c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "00978804",
      "DATA",
      [
        "storage",
        "00c0a7d8",
        null,
        "undefined *"
      ]
    ],
    [
      "009788c8",
      "DATA",
      [
        "storage",
        "00c0a858",
        null,
        "undefined *"
      ]
    ],
    [
      "00978948",
      "READ",
      [
        "storage",
        "00c0a880",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00978804",
      "DATA",
      [
        "storage",
        "00c0a828",
        null,
        "undefined *"
      ]
    ],
    [
      "009788c8",
      "DATA",
      [
        "storage",
        "00c0a8a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00978948",
      "READ",
      [
        "storage",
        "00c0a8d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009787f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/009785f0.md#insn-009787f8) · [`009788c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/009785f0.md#insn-009788c0)
- 新版 `009787f8`（命令位置の公開資料なし） · `009788c0`（命令位置の公開資料なし）

~~~diff
- 009787f8 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 009787f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009787f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009787f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009787f8 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 009787f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009787f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009787f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009787f8 bytes 08611f91
+ 009787f8 bytes 08a12091
- 009788c0 ["COPY", "tmp:0:8", ["const:858:8"]]
- 009788c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009788c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009788c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009788c0 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 009788c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009788c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009788c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009788c0 bytes 08612191
+ 009788c0 bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7358ea84d4ca410742e55d76171ad89c"></a>

### [`00979104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979104.md) → [`00979104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979104.md) FUN_00979104

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 13件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`00609f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00609/00609f20.md) [`008865b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00887/008879f4.md) [`0097cac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cac8.md)
- 新版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 13件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`00609f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00609/00609f20.md) [`008865b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/008879f4.md) [`0097cac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cac8.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.20% / 新版 97.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009791ec",
      "incomplete_value": false,
      "site": "009791ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009791ec",
      "incomplete_value": false,
      "site": "009791ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "009791ec",
      "DATA",
      [
        "storage",
        "00c0a958",
        null,
        "undefined *"
      ]
    ],
    [
      "00979244",
      "READ",
      [
        "storage",
        "00c0a978",
        null,
        "pointer"
      ]
    ],
    [
      "00979244",
      "READ",
      [
        "storage",
        "00c0a980",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009791ec",
      "DATA",
      [
        "storage",
        "00c0a9a8",
        null,
        "undefined *"
      ]
    ],
    [
      "00979244",
      "READ",
      [
        "storage",
        "00c0a9c8",
        null,
        "pointer"
      ]
    ],
    [
      "00979244",
      "READ",
      [
        "storage",
        "00c0a9d0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009791e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979104.md#insn-009791e4) · [`009791e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979104.md#insn-009791e8)
- 新版 `009791e4`（命令位置の公開資料なし） · `009791e8`（命令位置の公開資料なし）

~~~diff
- 009791e4 ["COPY", "tmp:0:8", ["const:958:8"]]
- 009791e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009791e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009791e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009791e4 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 009791e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009791e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009791e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009791e4 bytes 08612591
+ 009791e4 bytes 08a12691
- 009791e8 ["INT_SUB", "register:40a8:8", ["register:40e8:8", "const:40:8"]]
- 009791e8 bytes b50301d1
+ 009791e8 ["INT_SUB", "register:40a8:8", ["register:40e8:8", "const:40:8"]]
+ 009791e8 bytes b50301d1
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63731d0d634bdf313ec29766523671f0"></a>

### [`00979584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979584.md) → [`00979584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979584.md) FUN_00979584

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 15件 [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0087cfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0087c/0087cfbc.md) [`008865b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00887/008879f4.md) [`0097cb78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cb78.md)
- 新版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 15件 [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0087cfbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0087c/0087cfbc.md) [`008865b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00886/008865b0.md) [`008879f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00887/008879f4.md) [`0097cb78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cb78.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.62% / 新版 94.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009796ac",
      "incomplete_value": false,
      "site": "009796ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009796ac",
      "incomplete_value": false,
      "site": "009796ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "00979610",
      "READ",
      [
        "storage",
        "002a5dcc",
        null,
        "string"
      ]
    ],
    [
      "00979614",
      "READ",
      [
        "storage",
        "002a5ddc",
        null,
        "string"
      ]
    ],
    [
      "009796ac",
      "DATA",
      [
        "storage",
        "00c0a9d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00979610",
      "READ",
      [
        "storage",
        "002a5e57",
        null,
        "string"
      ]
    ],
    [
      "00979614",
      "READ",
      [
        "storage",
        "002a5e67",
        null,
        "string"
      ]
    ],
    [
      "009796ac",
      "DATA",
      [
        "storage",
        "00c0aa28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009795f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979584.md#insn-009795f4) · [`009796a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979584.md#insn-009796a4)
- 新版 `009795f4`（命令位置の公開資料なし） · `009796a4`（命令位置の公開資料なし）

~~~diff
- 009795f4 ["COPY", "tmp:0:8", ["const:dcc:8"]]
- 009795f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009795f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009795f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009795f4 ["COPY", "tmp:0:8", ["const:e57:8"]]
+ 009795f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009795f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009795f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009795f4 bytes 08313791
+ 009795f4 bytes 085d3991
- 009796a4 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 009796a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009796a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009796a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009796a4 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 009796a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009796a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009796a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009796a4 bytes 08612791
+ 009796a4 bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53411e12ed4c49abfc9801ebe94f4899"></a>

### [`00979d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979d0c.md) → [`00979d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979d0c.md) FUN_00979d0c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073f/0073fa38.md) · 呼出先 13件 [`00976c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976c10.md) [`00976da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00976/00976da4.md) [`0097a1a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a1a8.md) [`0097b0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097b/0097b0c8.md) [`0097cfcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cfcc.md)
- 新版 呼出元 1件 [`0073fa38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073f/0073fa38.md) · 呼出先 13件 [`00976c10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976c10.md) [`00976da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00976/00976da4.md) [`0097a1a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a1a8.md) [`0097b0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097b/0097b0c8.md) [`0097cfcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cfcc.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.23% / 新版 99.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00979ea4",
      "incomplete_value": false,
      "site": "00979ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00979ea4",
      "incomplete_value": false,
      "site": "00979ea4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "00979ea4",
      "DATA",
      [
        "storage",
        "00c0aa58",
        null,
        "undefined *"
      ]
    ],
    [
      "00979f58",
      "READ",
      [
        "storage",
        "00c0aa80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00979ea4",
      "DATA",
      [
        "storage",
        "00c0aaa8",
        null,
        "undefined *"
      ]
    ],
    [
      "00979f58",
      "READ",
      [
        "storage",
        "00c0aad0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00979e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979d0c.md#insn-00979e9c)
- 新版 `00979e9c`（命令位置の公開資料なし）

~~~diff
- 00979e9c ["COPY", "tmp:0:8", ["const:a58:8"]]
- 00979e9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00979e9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00979e9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00979e9c ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 00979e9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00979e9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00979e9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00979e9c bytes 08612991
+ 00979e9c bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7aaeeb5d0b9ed54a79c7e415d448f86"></a>

### [`0097a22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a22c.md) → [`0097a22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a22c.md) FUN_0097a22c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0086b704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0086b/0086b704.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469f7c.md) [`0046fdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0046f/0046fdf4.md) [`006ff834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/006ff/006ff834.md)
- 新版 呼出元 1件 [`0086b704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0086b/0086b704.md) · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md) [`00469f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469f7c.md) [`0046fdf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0046f/0046fdf4.md) [`006ff834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006ff/006ff834.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.73% / 新版 96.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097a2c4",
      "incomplete_value": true,
      "site": "0097a2d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f79:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097a2c4",
      "incomplete_value": true,
      "site": "0097a2d4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6:8"
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
      "definition_site": "0097a2c4",
      "incomplete_value": true,
      "site": "0097a2d4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0097a2c4",
      "incomplete_value": true,
      "site": "0097a2d4",
      "value": [
        "LOAD",
        "16",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097a2d8",
      "incomplete_value": true,
      "site": "0097a2e8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0097a2d8",
      "incomplete_value": true,
      "site": "0097a2e8",
      "value": [
        "LOAD",
        "16",
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
      "0097a2c4",
      "READ",
      [
        "storage",
        "00295006",
        null,
        null
      ]
    ],
    [
      "0097a2c4",
      "READ",
      [
        "storage",
        "00295016",
        null,
        null
      ]
    ],
    [
      "0097a2d8",
      "READ",
      [
        "storage",
        "00295026",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0097a2c4",
      "READ",
      [
        "storage",
        "00294f79",
        null,
        null
      ]
    ],
    [
      "0097a2c4",
      "READ",
      [
        "storage",
        "00294f89",
        null,
        null
      ]
    ],
    [
      "0097a2d8",
      "READ",
      [
        "storage",
        "00294f99",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097a2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a22c.md#insn-0097a2b8) · [`0097a2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a22c.md#insn-0097a2bc) · [`0097a390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a22c.md#insn-0097a390)
- 新版 `0097a2b8`（命令位置の公開資料なし） · `0097a2bc`（命令位置の公開資料なし） · `0097a390`（命令位置の公開資料なし）

~~~diff
- 0097a2b8 ["COPY", "register:4040:8", ["const:295000:8"]]
+ 0097a2b8 ["COPY", "register:4040:8", ["const:294000:8"]]
- 0097a2b8 bytes c8c8fff0
+ 0097a2b8 bytes c8c8ffd0
- 0097a2bc ["COPY", "tmp:0:8", ["const:6:8"]]
- 0097a2bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097a2bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097a2bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097a2bc ["COPY", "tmp:0:8", ["const:f79:8"]]
+ 0097a2bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097a2bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097a2bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097a2bc bytes 08190091
+ 0097a2bc bytes 08e53d91
- 0097a390 ["COPY", "tmp:0:8", ["const:bbe:8"]]
- 0097a390 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0097a390 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0097a390 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0097a390 ["COPY", "tmp:0:8", ["const:c49:8"]]
+ 0097a390 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0097a390 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0097a390 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0097a390 bytes 73fa2e91
+ 0097a390 bytes 73263191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-affa68b427c5e0e74644ae4b885aa63c"></a>

### [`0097a888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a888.md) → [`0097a888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a888.md) FUN_0097a888

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0097a22c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a22c.md) · 呼出先 22件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044d/0044d968.md) [`004512c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00451/004512c0.md) [`00469128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469128.md) [`00469e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00469/00469e20.md)
- 新版 呼出元 1件 [`0097a22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097a22c.md) · 呼出先 22件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0044d968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044d/0044d968.md) [`004512c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00451/004512c0.md) [`00469128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469128.md) [`00469e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00469/00469e20.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097aa5c",
      "incomplete_value": true,
      "site": "0097aa7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:cf6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097aa5c",
      "incomplete_value": true,
      "site": "0097aa7c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ce7:8"
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
      "definition_site": "0097aa5c",
      "incomplete_value": true,
      "site": "0097aa7c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0097aa5c",
      "incomplete_value": true,
      "site": "0097aa7c",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097acac",
      "incomplete_value": true,
      "site": "0097acac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097acac",
      "incomplete_value": true,
      "site": "0097acac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e8c:8"
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
      "0097aa5c",
      "READ",
      [
        "storage",
        "002a9ce7",
        null,
        "string"
      ]
    ],
    [
      "0097aa5c",
      "READ",
      [
        "storage",
        "002a9cf7",
        null,
        "string"
      ]
    ],
    [
      "0097ab64",
      "PARAM",
      [
        "storage",
        "00295133",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0097aa5c",
      "READ",
      [
        "storage",
        "002a9cf6",
        null,
        "string"
      ]
    ],
    [
      "0097aa5c",
      "READ",
      [
        "storage",
        "002a9d06",
        null,
        "string"
      ]
    ],
    [
      "0097ab64",
      "PARAM",
      [
        "storage",
        "002950a6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097aa54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a888.md#insn-0097aa54) · [`0097aaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a888.md#insn-0097aaa0) · [`0097ac38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097a888.md#insn-0097ac38)
- 新版 `0097aa54`（命令位置の公開資料なし） · `0097aaa0`（命令位置の公開資料なし） · `0097ac38`（命令位置の公開資料なし）

~~~diff
- 0097aa54 ["COPY", "tmp:0:8", ["const:ce7:8"]]
- 0097aa54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097aa54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097aa54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097aa54 ["COPY", "tmp:0:8", ["const:cf6:8"]]
+ 0097aa54 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097aa54 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097aa54 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097aa54 bytes 299d3391
+ 0097aa54 bytes 29d93391
- 0097aaa0 ["COPY", "tmp:0:8", ["const:133:8"]]
- 0097aaa0 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 0097aaa0 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 0097aaa0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 0097aaa0 ["COPY", "tmp:0:8", ["const:a6:8"]]
+ 0097aaa0 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 0097aaa0 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 0097aaa0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 0097aaa0 bytes b5ce0491
+ 0097aaa0 bytes b59a0291
- 0097ac38 ["COPY", "tmp:0:8", ["const:e45:8"]]
- 0097ac38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097ac38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097ac38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097ac38 ["COPY", "tmp:0:8", ["const:edf:8"]]
+ 0097ac38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097ac38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097ac38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097ac38 bytes 29153991
+ 0097ac38 bytes 297d3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa32ffe19e1a9cec5cd23ffce428661e"></a>

### [`0097af20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097af20.md) → [`0097af20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097af20.md) FUN_0097af20

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
      "definition_site": "0097af24",
      "incomplete_value": false,
      "site": "0097af28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097af24",
      "incomplete_value": false,
      "site": "0097af28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
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
      "0097af28",
      "DATA",
      [
        "storage",
        "00c0a788",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0097af28",
      "DATA",
      [
        "storage",
        "00c0a7d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097af24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097af20.md#insn-0097af24)
- 新版 `0097af24`（命令位置の公開資料なし）

~~~diff
- 0097af24 ["COPY", "tmp:0:8", ["const:788:8"]]
- 0097af24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097af24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097af24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097af24 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 0097af24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097af24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097af24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097af24 bytes 08211e91
+ 0097af24 bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6aa3083f1a7dd322485a841f7e36ec59"></a>

### [`0097af30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097af30.md) → [`0097af30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097af30.md) FUN_0097af30

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
      "definition_site": "0097af40",
      "incomplete_value": false,
      "site": "0097af48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097af40",
      "incomplete_value": false,
      "site": "0097af48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:788:8"
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
      "0097af48",
      "DATA",
      [
        "storage",
        "00c0a788",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0097af48",
      "DATA",
      [
        "storage",
        "00c0a7d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097af40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097af30.md#insn-0097af40)
- 新版 `0097af40`（命令位置の公開資料なし）

~~~diff
- 0097af40 ["COPY", "tmp:0:8", ["const:788:8"]]
- 0097af40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097af40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097af40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097af40 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 0097af40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097af40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097af40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097af40 bytes 08211e91
+ 0097af40 bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-955975cd0d5731b001c84d6c9bf4294e"></a>

### [`0097b0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097b/0097b0c8.md) → [`0097b0c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097b/0097b0c8.md) FUN_0097b0c8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`009772ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00977/009772ec.md) [`00979d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979d0c.md) [`0097af6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097a/0097af6c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`009772ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/009772ec.md) [`00979d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979d0c.md) [`0097af6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097a/0097af6c.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0097b0d4",
      "incomplete_value": false,
      "site": "0097b0d8",
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
      "definition_site": "0097b0d4",
      "incomplete_value": false,
      "site": "0097b0d8",
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
      "0097b0d4",
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
      "0097b0d4",
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

- 旧版 [`0097b0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097b/0097b0c8.md#insn-0097b0d4)
- 新版 `0097b0d4`（命令位置の公開資料なし）

~~~diff
- 0097b0d4 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0097b0d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0097b0d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0097b0d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0097b0d4 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0097b0d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0097b0d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0097b0d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0097b0d4 bytes 000c0c91
+ 0097b0d4 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8025dd1cd4d47db77fd6a5a352ac9656"></a>

### [`0097c214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c214.md) → [`0097c214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c214.md) FUN_0097c214

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00977d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00977/00977d04.md) [`00a40cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a40/00a40cb0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`00977d04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977d04.md) [`00a40cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a40/00a40cf4.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0097c220",
      "incomplete_value": true,
      "site": "0097c224",
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
            "const:39d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c220",
      "incomplete_value": true,
      "site": "0097c224",
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
      "0097c220",
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
      "0097c220",
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

- 旧版 [`0097c220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c214.md#insn-0097c220)
- 新版 `0097c220`（命令位置の公開資料なし）

~~~diff
- 0097c220 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0097c220 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0097c220 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0097c220 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0097c220 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0097c220 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0097c220 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0097c220 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0097c220 bytes 000c0c91
+ 0097c220 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-010d7478dc60d7302c168a6994b6332e"></a>

### [`0097c228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c228.md) → [`0097c228`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c228.md) FUN_0097c228

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "0097c240",
      "incomplete_value": false,
      "site": "0097c244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c240",
      "incomplete_value": false,
      "site": "0097c244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "0097c244",
      "DATA",
      [
        "storage",
        "00c0a7d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c244",
      "DATA",
      [
        "storage",
        "00c0a828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c228.md#insn-0097c240)
- 新版 `0097c240`（命令位置の公開資料なし）

~~~diff
- 0097c240 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 0097c240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097c240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097c240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097c240 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 0097c240 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c240 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c240 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097c240 bytes 08611f91
+ 0097c240 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7754210d27f2c68e44793b3f95822abc"></a>

### [`0097c2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c2b8.md) → [`0097c2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c2b8.md) FUN_0097c2b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0097c2d0",
      "incomplete_value": false,
      "site": "0097c2d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c2d0",
      "incomplete_value": false,
      "site": "0097c2d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "0097c2d4",
      "DATA",
      [
        "storage",
        "00c0a7d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c2d4",
      "DATA",
      [
        "storage",
        "00c0a828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c2b8.md#insn-0097c2d0)
- 新版 `0097c2d0`（命令位置の公開資料なし）

~~~diff
- 0097c2d0 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 0097c2d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097c2d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097c2d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097c2d0 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 0097c2d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c2d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c2d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097c2d0 bytes 08611f91
+ 0097c2d0 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdc45f14108558de9848950e7fc06504"></a>

### [`0097c344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c344.md) → [`0097c344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c344.md) FUN_0097c344

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0097c360",
      "incomplete_value": false,
      "site": "0097c370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c360",
      "incomplete_value": false,
      "site": "0097c370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "0097c370",
      "DATA",
      [
        "storage",
        "00c0a7d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c370",
      "DATA",
      [
        "storage",
        "00c0a828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c344.md#insn-0097c360)
- 新版 `0097c360`（命令位置の公開資料なし）

~~~diff
- 0097c360 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 0097c360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097c360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097c360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097c360 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 0097c360 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c360 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c360 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097c360 bytes 08611f91
+ 0097c360 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f011f8c2e272a3f95738cfc344608aa5"></a>

### [`0097c3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c3f4.md) → [`0097c3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c3f4.md) FUN_0097c3f4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

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
      "definition_site": "0097c404",
      "incomplete_value": false,
      "site": "0097c40c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c404",
      "incomplete_value": false,
      "site": "0097c40c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:7d8:8"
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
      "0097c40c",
      "DATA",
      [
        "storage",
        "00c0a7d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c40c",
      "DATA",
      [
        "storage",
        "00c0a828",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c3f4.md#insn-0097c404)
- 新版 `0097c404`（命令位置の公開資料なし）

~~~diff
- 0097c404 ["COPY", "tmp:0:8", ["const:7d8:8"]]
- 0097c404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097c404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097c404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097c404 ["COPY", "tmp:0:8", ["const:828:8"]]
+ 0097c404 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c404 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c404 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097c404 bytes 08611f91
+ 0097c404 bytes 08a12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81aae42f32228b8ecd559d1d64d6fb7b"></a>

### [`0097c764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c764.md) → [`0097c764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c764.md) FUN_0097c764

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
      "definition_site": "0097c770",
      "incomplete_value": false,
      "site": "0097c77c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c770",
      "incomplete_value": false,
      "site": "0097c77c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "0097c77c",
      "DATA",
      [
        "storage",
        "00c0a858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c77c",
      "DATA",
      [
        "storage",
        "00c0a8a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c764.md#insn-0097c770)
- 新版 `0097c770`（命令位置の公開資料なし）

~~~diff
- 0097c770 ["COPY", "tmp:0:8", ["const:858:8"]]
- 0097c770 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0097c770 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0097c770 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0097c770 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 0097c770 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0097c770 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0097c770 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0097c770 bytes 4a612191
+ 0097c770 bytes 4aa12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9d6efc824b3440b2e6450d8a377517f8"></a>

### [`0097c7a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c7a8.md) → [`0097c7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c7a8.md) FUN_0097c7a8

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
      "definition_site": "0097c7c0",
      "incomplete_value": false,
      "site": "0097c7cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c7c0",
      "incomplete_value": false,
      "site": "0097c7cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "0097c7cc",
      "DATA",
      [
        "storage",
        "00c0a858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c7cc",
      "DATA",
      [
        "storage",
        "00c0a8a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c7a8.md#insn-0097c7c0)
- 新版 `0097c7c0`（命令位置の公開資料なし）

~~~diff
- 0097c7c0 ["COPY", "tmp:0:8", ["const:858:8"]]
- 0097c7c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097c7c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097c7c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097c7c0 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 0097c7c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c7c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c7c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097c7c0 bytes 08612191
+ 0097c7c0 bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-261acc629c988702254a27593b978f13"></a>

### [`0097c804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c804.md) → [`0097c804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c804.md) FUN_0097c804

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0097c830",
      "incomplete_value": false,
      "site": "0097c830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c830",
      "incomplete_value": false,
      "site": "0097c830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "0097c830",
      "DATA",
      [
        "storage",
        "00c0a858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c830",
      "DATA",
      [
        "storage",
        "00c0a8a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c804.md#insn-0097c828)
- 新版 `0097c828`（命令位置の公開資料なし）

~~~diff
- 0097c828 ["COPY", "tmp:0:8", ["const:858:8"]]
- 0097c828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097c828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097c828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097c828 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 0097c828 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c828 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097c828 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097c828 bytes 08612191
+ 0097c828 bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8843e9fdf74b747adec724b0f2e2502e"></a>

### [`0097c88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c88c.md) → [`0097c88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097c88c.md) FUN_0097c88c

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
      "definition_site": "0097c8a8",
      "incomplete_value": false,
      "site": "0097c8a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:8a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097c8a8",
      "incomplete_value": false,
      "site": "0097c8a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:858:8"
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
      "0097c8a8",
      "DATA",
      [
        "storage",
        "00c0a858",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097c8a8",
      "DATA",
      [
        "storage",
        "00c0a8a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097c8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097c88c.md#insn-0097c8a4)
- 新版 `0097c8a4`（命令位置の公開資料なし）

~~~diff
- 0097c8a4 ["COPY", "tmp:0:8", ["const:858:8"]]
- 0097c8a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097c8a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097c8a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097c8a4 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 0097c8a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097c8a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097c8a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097c8a4 bytes 29612191
+ 0097c8a4 bytes 29a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18eb910e2863a1fcc35e8bc1bad2ccc7"></a>

### [`0097ca28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097ca28.md) → [`0097ca28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097ca28.md) FUN_0097ca28

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
      "definition_site": "0097ca3c",
      "incomplete_value": false,
      "site": "0097ca40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097ca3c",
      "incomplete_value": false,
      "site": "0097ca40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "0097ca40",
      "DATA",
      [
        "storage",
        "00c0a8d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097ca40",
      "DATA",
      [
        "storage",
        "00c0a928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097ca3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097ca28.md#insn-0097ca3c)
- 新版 `0097ca3c`（命令位置の公開資料なし）

~~~diff
- 0097ca3c ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 0097ca3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097ca3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097ca3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097ca3c ["COPY", "tmp:0:8", ["const:928:8"]]
+ 0097ca3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ca3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ca3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097ca3c bytes 08612391
+ 0097ca3c bytes 08a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4600f1b528a456b869ebe285fb43f47"></a>

### [`0097ca4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097ca4c.md) → [`0097ca4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097ca4c.md) FUN_0097ca4c

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
      "definition_site": "0097ca50",
      "incomplete_value": false,
      "site": "0097ca54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097ca50",
      "incomplete_value": false,
      "site": "0097ca54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:8d8:8"
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
      "0097ca54",
      "DATA",
      [
        "storage",
        "00c0a8d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097ca54",
      "DATA",
      [
        "storage",
        "00c0a928",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097ca50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097ca4c.md#insn-0097ca50)
- 新版 `0097ca50`（命令位置の公開資料なし）

~~~diff
- 0097ca50 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 0097ca50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097ca50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097ca50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097ca50 ["COPY", "tmp:0:8", ["const:928:8"]]
+ 0097ca50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ca50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ca50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097ca50 bytes 08612391
+ 0097ca50 bytes 08a12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f92225f6cbea8eefd4bd345f9f87ec3"></a>

### [`0097ca94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097ca94.md) → [`0097ca94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097ca94.md) FUN_0097ca94

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
      "definition_site": "0097caa8",
      "incomplete_value": false,
      "site": "0097caac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097caa8",
      "incomplete_value": false,
      "site": "0097caac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "0097caac",
      "DATA",
      [
        "storage",
        "00c0a958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097caac",
      "DATA",
      [
        "storage",
        "00c0a9a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097caa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097ca94.md#insn-0097caa8)
- 新版 `0097caa8`（命令位置の公開資料なし）

~~~diff
- 0097caa8 ["COPY", "tmp:0:8", ["const:958:8"]]
- 0097caa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097caa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097caa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097caa8 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 0097caa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097caa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097caa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097caa8 bytes 08612591
+ 0097caa8 bytes 08a12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01465ac4f8c451d216311f0427f39218"></a>

### [`0097cab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cab8.md) → [`0097cab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cab8.md) FUN_0097cab8

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
      "definition_site": "0097cabc",
      "incomplete_value": false,
      "site": "0097cac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097cabc",
      "incomplete_value": false,
      "site": "0097cac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "0097cac0",
      "DATA",
      [
        "storage",
        "00c0a958",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097cac0",
      "DATA",
      [
        "storage",
        "00c0a9a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097cabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cab8.md#insn-0097cabc)
- 新版 `0097cabc`（命令位置の公開資料なし）

~~~diff
- 0097cabc ["COPY", "tmp:0:8", ["const:958:8"]]
- 0097cabc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097cabc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097cabc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097cabc ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 0097cabc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cabc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cabc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097cabc bytes 08612591
+ 0097cabc bytes 08a12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ce2da8eb3eccdb38163e554ca998a00"></a>

### [`0097cb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cb44.md) → [`0097cb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cb44.md) FUN_0097cb44

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
      "definition_site": "0097cb58",
      "incomplete_value": false,
      "site": "0097cb5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097cb58",
      "incomplete_value": false,
      "site": "0097cb5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "0097cb5c",
      "DATA",
      [
        "storage",
        "00c0a9d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097cb5c",
      "DATA",
      [
        "storage",
        "00c0aa28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097cb58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cb44.md#insn-0097cb58)
- 新版 `0097cb58`（命令位置の公開資料なし）

~~~diff
- 0097cb58 ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 0097cb58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097cb58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097cb58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097cb58 ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 0097cb58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cb58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cb58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097cb58 bytes 08612791
+ 0097cb58 bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-036117fa74e73d6fd2521d42f0d445e5"></a>

### [`0097cb68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cb68.md) → [`0097cb68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cb68.md) FUN_0097cb68

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
      "definition_site": "0097cb6c",
      "incomplete_value": false,
      "site": "0097cb70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097cb6c",
      "incomplete_value": false,
      "site": "0097cb70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:9d8:8"
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
      "0097cb70",
      "DATA",
      [
        "storage",
        "00c0a9d8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097cb70",
      "DATA",
      [
        "storage",
        "00c0aa28",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097cb6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cb68.md#insn-0097cb6c)
- 新版 `0097cb6c`（命令位置の公開資料なし）

~~~diff
- 0097cb6c ["COPY", "tmp:0:8", ["const:9d8:8"]]
- 0097cb6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097cb6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097cb6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097cb6c ["COPY", "tmp:0:8", ["const:a28:8"]]
+ 0097cb6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cb6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cb6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097cb6c bytes 08612791
+ 0097cb6c bytes 08a12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d170cea57859db442ab873af5c03fcd4"></a>

### [`0097cc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cc18.md) → [`0097cc18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cc18.md) FUN_0097cc18

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "0097cc30",
      "incomplete_value": false,
      "site": "0097cc40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097cc30",
      "incomplete_value": false,
      "site": "0097cc40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "0097cc40",
      "DATA",
      [
        "storage",
        "00c0aa58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097cc40",
      "DATA",
      [
        "storage",
        "00c0aaa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097cc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cc18.md#insn-0097cc30)
- 新版 `0097cc30`（命令位置の公開資料なし）

~~~diff
- 0097cc30 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 0097cc30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097cc30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097cc30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097cc30 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 0097cc30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cc30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cc30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097cc30 bytes 08612991
+ 0097cc30 bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c0071a48d7a708f6eb977558f126f78"></a>

### [`0097cca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cca8.md) → [`0097cca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cca8.md) FUN_0097cca8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0097ccc0",
      "incomplete_value": false,
      "site": "0097ccd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097ccc0",
      "incomplete_value": false,
      "site": "0097ccd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "0097ccd0",
      "DATA",
      [
        "storage",
        "00c0aa58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097ccd0",
      "DATA",
      [
        "storage",
        "00c0aaa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097ccc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cca8.md#insn-0097ccc0)
- 新版 `0097ccc0`（命令位置の公開資料なし）

~~~diff
- 0097ccc0 ["COPY", "tmp:0:8", ["const:a58:8"]]
- 0097ccc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097ccc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097ccc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097ccc0 ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 0097ccc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ccc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ccc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097ccc0 bytes 08612991
+ 0097ccc0 bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee10850cebb72d8488550e3d0fae775d"></a>

### [`0097cd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cd34.md) → [`0097cd34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097c/0097cd34.md) FUN_0097cd34

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097cd64",
      "incomplete_value": false,
      "site": "0097cd64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097cd64",
      "incomplete_value": false,
      "site": "0097cd64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "0097cd64",
      "DATA",
      [
        "storage",
        "00c0aa58",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097cd64",
      "DATA",
      [
        "storage",
        "00c0aaa8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097cd5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097c/0097cd34.md#insn-0097cd5c)
- 新版 `0097cd5c`（命令位置の公開資料なし）

~~~diff
- 0097cd5c ["COPY", "tmp:0:8", ["const:a58:8"]]
- 0097cd5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097cd5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097cd5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097cd5c ["COPY", "tmp:0:8", ["const:aa8:8"]]
+ 0097cd5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cd5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097cd5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097cd5c bytes 08612991
+ 0097cd5c bytes 08a12a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6857e9aacfe862e9d26c28a6409caba"></a>

### [`0097d128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097d128.md) → [`0097d128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097d/0097d128.md) _INIT_191

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
      "definition_site": "0097d164",
      "incomplete_value": true,
      "site": "0097d180",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0097d164",
      "incomplete_value": true,
      "site": "0097d180",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0097d1c8",
      "incomplete_value": true,
      "site": "0097d1e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0097d1c8",
      "incomplete_value": true,
      "site": "0097d1e0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0097d224",
      "incomplete_value": true,
      "site": "0097d268",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0097d224",
      "incomplete_value": true,
      "site": "0097d268",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "0097d164",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0097d188",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0097d1a8",
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
      "0097d164",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0097d188",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0097d1a8",
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

- 旧版 [`0097d154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097d128.md#insn-0097d154) · [`0097d15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097d128.md#insn-0097d15c)
- 新版 `0097d154`（命令位置の公開資料なし） · `0097d15c`（命令位置の公開資料なし）

~~~diff
- 0097d154 ["COPY", "tmp:0:8", ["const:980:8"]]
- 0097d154 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 0097d154 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 0097d154 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 0097d154 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 0097d154 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 0097d154 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 0097d154 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 0097d154 bytes 73022691
+ 0097d154 bytes 73022791
- 0097d15c ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 0097d15c bytes 49c9ffd0
+ 0097d15c ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 0097d15c bytes 49c9ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d27d2f43b13b71f8d310a28eeb75889"></a>

### [`0097d4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097d4b8.md) → [`0097d4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097d/0097d4b8.md) FUN_0097d4b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`005846a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00584/005846a8.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`005857bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00585/005857bc.md) [`0097db1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097db1c.md) [`00980108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980108.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`005846a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/005846a8.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`005857bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005857bc.md) [`0097db1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097d/0097db1c.md) [`00980108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980108.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097d624",
      "incomplete_value": true,
      "site": "0097d634",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097d624",
      "incomplete_value": true,
      "site": "0097d634",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:356:8"
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
      "definition_site": "0097d638",
      "incomplete_value": true,
      "site": "0097d638",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0097d638",
      "incomplete_value": true,
      "site": "0097d638",
      "value": [
        "LOAD",
        "8",
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
      "0097d624",
      "READ",
      [
        "storage",
        "002a8356",
        null,
        "string"
      ]
    ],
    [
      "0097d62c",
      "READ",
      [
        "storage",
        "002a835d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0097d624",
      "READ",
      [
        "storage",
        "002a83f0",
        null,
        "string"
      ]
    ],
    [
      "0097d62c",
      "READ",
      [
        "storage",
        "002a83f7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097d61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097d4b8.md#insn-0097d61c)
- 新版 `0097d61c`（命令位置の公開資料なし）

~~~diff
- 0097d61c ["COPY", "tmp:0:8", ["const:356:8"]]
- 0097d61c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0097d61c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0097d61c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0097d61c ["COPY", "tmp:0:8", ["const:3f0:8"]]
+ 0097d61c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0097d61c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0097d61c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0097d61c bytes 4a590d91
+ 0097d61c bytes 4ac10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab6a2961f1ff69812c5ec337b96d46f3"></a>

### [`0097db1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097db1c.md) → [`0097db1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097d/0097db1c.md) FUN_0097db1c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`00586014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00586/00586014.md) [`0058717c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00587/0058717c.md) [`0097d4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097d4b8.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`005859d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00585/005859d8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 3件 [`00586014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/00586014.md) [`0058717c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/0058717c.md) [`0097d4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097d/0097d4b8.md) · 呼出先 7件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`005859d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00585/005859d8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.53% / 新版 98.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097db88",
      "incomplete_value": true,
      "site": "0097db88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0097db88",
      "incomplete_value": true,
      "site": "0097db88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0097db70",
      "READ",
      [
        "storage",
        "002a92b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0097db70",
      "READ",
      [
        "storage",
        "002a934c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097db6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097db1c.md#insn-0097db6c)
- 新版 `0097db6c`（命令位置の公開資料なし）

~~~diff
- 0097db6c ["COPY", "tmp:0:8", ["const:2b2:8"]]
- 0097db6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097db6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097db6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097db6c ["COPY", "tmp:0:8", ["const:34c:8"]]
+ 0097db6c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097db6c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097db6c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097db6c bytes 29c90a91
+ 0097db6c bytes 29310d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65ff84a3a5f53f340a0caca22708a29a"></a>

### [`0097deec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097deec.md) → [`0097deec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097d/0097deec.md) FUN_0097deec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`009784b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/009784b4.md) [`00978d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/00978d0c.md) [`0097ea24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ea24.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`00973ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973ae8.md) [`00973af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973af8.md) [`0097e4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097e4e8.md)
- 新版 呼出元 3件 [`009784b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/009784b4.md) [`00978d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/00978d0c.md) [`0097ea24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097ea24.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) [`00973ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00973/00973ae8.md) [`00973af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00973/00973af8.md) [`0097e4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097e4e8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.55% / 新版 98.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097e074",
      "incomplete_value": false,
      "site": "0097e080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097e074",
      "incomplete_value": false,
      "site": "0097e080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097e134",
      "incomplete_value": false,
      "site": "0097e140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097e134",
      "incomplete_value": false,
      "site": "0097e140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "0097e080",
      "DATA",
      [
        "storage",
        "00c0aae8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e140",
      "DATA",
      [
        "storage",
        "00c0ab68",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e1d0",
      "READ",
      [
        "storage",
        "00c0ab90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097e080",
      "DATA",
      [
        "storage",
        "00c0ab38",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e140",
      "DATA",
      [
        "storage",
        "00c0abb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e1d0",
      "READ",
      [
        "storage",
        "00c0abe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097e074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097deec.md#insn-0097e074) · [`0097e134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097deec.md#insn-0097e134)
- 新版 `0097e074`（命令位置の公開資料なし） · `0097e134`（命令位置の公開資料なし）

~~~diff
- 0097e074 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 0097e074 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097e074 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097e074 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097e074 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 0097e074 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e074 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e074 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097e074 bytes 08a12b91
+ 0097e074 bytes 08e12c91
- 0097e134 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 0097e134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097e134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097e134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097e134 ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 0097e134 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e134 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e134 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097e134 bytes 08a12d91
+ 0097e134 bytes 08e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da5fd3ab5a6240020a11cc37bf6e0317"></a>

### [`0097e4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097e4e8.md) → [`0097e4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097e4e8.md) FUN_0097e4e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0071bdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071bdc8.md) [`0097deec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097d/0097deec.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`00587858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00587/00587858.md) [`0076b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md)
- 新版 呼出元 2件 [`0071bdc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071b/0071bdc8.md) [`0097deec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097d/0097deec.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576268.md) [`00587858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00587/00587858.md) [`0076b910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b910.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.15% / 新版 97.15%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097e5b8",
      "incomplete_value": false,
      "site": "0097e5bc",
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
      "definition_site": "0097e5b8",
      "incomplete_value": false,
      "site": "0097e5bc",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097e648",
      "incomplete_value": false,
      "site": "0097e648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097e648",
      "incomplete_value": false,
      "site": "0097e648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097e758",
      "incomplete_value": false,
      "site": "0097e758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097e758",
      "incomplete_value": false,
      "site": "0097e758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:e8:8"
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
      "0097e5bc",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e648",
      "DATA",
      [
        "storage",
        "00c0b068",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e6bc",
      "READ",
      [
        "storage",
        "00c0b090",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097e5bc",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e648",
      "DATA",
      [
        "storage",
        "00c0b0b8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097e6bc",
      "READ",
      [
        "storage",
        "00c0b0e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097e5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097e4e8.md#insn-0097e5b0) · [`0097e640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097e4e8.md#insn-0097e640) · [`0097e750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097e4e8.md#insn-0097e750)
- 新版 `0097e5b0`（命令位置の公開資料なし） · `0097e640`（命令位置の公開資料なし） · `0097e750`（命令位置の公開資料なし）

~~~diff
- 0097e5b0 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0097e5b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097e5b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097e5b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097e5b0 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0097e5b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e5b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e5b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097e5b0 bytes 08012891
+ 0097e5b0 bytes 08412991
- 0097e640 ["COPY", "tmp:0:8", ["const:68:8"]]
- 0097e640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097e640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097e640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097e640 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 0097e640 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e640 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e640 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097e640 bytes 08a10191
+ 0097e640 bytes 08e10291
- 0097e750 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 0097e750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097e750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097e750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097e750 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 0097e750 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e750 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097e750 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097e750 bytes 08a10391
+ 0097e750 bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-090c9f46a19b7d41232967703ad6c8a5"></a>

### [`0097ea24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ea24.md) → [`0097ea24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097ea24.md) FUN_0097ea24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00977c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00977/00977c00.md) · 呼出先 15件 [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`00973ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973ae8.md) [`00973af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973af0.md) [`00975098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975098.md) [`00975120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00975/00975120.md)
- 新版 呼出元 1件 [`00977c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977c00.md) · 呼出先 15件 [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) [`00973ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00973/00973ae8.md) [`00973af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00973/00973af0.md) [`00975098`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/00975098.md) [`00975120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00975/00975120.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.12% / 新版 96.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097ea8c",
      "incomplete_value": true,
      "site": "0097ea8c",
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
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097ea8c",
      "incomplete_value": true,
      "site": "0097ea8c",
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
            "const:be8:8"
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
      "0097ea8c",
      "DATA",
      [
        "storage",
        "00c0abe8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097eae0",
      "DATA",
      [
        "storage",
        "00c0ac68",
        null,
        "undefined *"
      ]
    ],
    [
      "0097eaf8",
      "DATA",
      [
        "storage",
        "00c0ace8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097ea8c",
      "DATA",
      [
        "storage",
        "00c0ac38",
        null,
        "undefined *"
      ]
    ],
    [
      "0097eae0",
      "DATA",
      [
        "storage",
        "00c0acb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097eaf8",
      "DATA",
      [
        "storage",
        "00c0ad38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097ea84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ea24.md#insn-0097ea84) · [`0097eadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ea24.md#insn-0097eadc) · [`0097eaf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ea24.md#insn-0097eaf4)
- 新版 `0097ea84`（命令位置の公開資料なし） · `0097eadc`（命令位置の公開資料なし） · `0097eaf4`（命令位置の公開資料なし）

~~~diff
- 0097ea84 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 0097ea84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097ea84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097ea84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097ea84 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 0097ea84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ea84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ea84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097ea84 bytes 08a12f91
+ 0097ea84 bytes 08e13091
- 0097eadc ["COPY", "tmp:0:8", ["const:c68:8"]]
- 0097eadc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097eadc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097eadc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097eadc ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 0097eadc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097eadc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097eadc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097eadc bytes 08a13191
+ 0097eadc bytes 08e13291
- 0097eaf4 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 0097eaf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097eaf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097eaf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097eaf4 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 0097eaf4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097eaf4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097eaf4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097eaf4 bytes 08a13391
+ 0097eaf4 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3280e54bb8a1d935ac621dc209ac2407"></a>

### [`0097ec84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ec84.md) → [`0097ec84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097ec84.md) FUN_0097ec84

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 4件 [`0071b838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071b/0071b838.md) [`0071c4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071c4c8.md) [`009785f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00978/009785f0.md) [`0097ea24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ea24.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`005866f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00586/005866f0.md) [`0076b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md)
- 新版 呼出元 4件 [`0071b838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071b/0071b838.md) [`0071c4c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071c/0071c4c8.md) [`009785f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00978/009785f0.md) [`0097ea24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097ea24.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576268.md) [`005866f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00586/005866f0.md) [`0076b910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b910.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.11% / 新版 97.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097ed48",
      "incomplete_value": false,
      "site": "0097ed4c",
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
      "definition_site": "0097ed48",
      "incomplete_value": false,
      "site": "0097ed4c",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097edd8",
      "incomplete_value": false,
      "site": "0097edd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097edd8",
      "incomplete_value": false,
      "site": "0097edd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "definition_site": "0097eee8",
      "incomplete_value": false,
      "site": "0097eee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097eee8",
      "incomplete_value": false,
      "site": "0097eee8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "0097ed4c",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "0097edd8",
      "DATA",
      [
        "storage",
        "00c0af68",
        null,
        "undefined *"
      ]
    ],
    [
      "0097ee4c",
      "READ",
      [
        "storage",
        "00c0af90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097ed4c",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ],
    [
      "0097edd8",
      "DATA",
      [
        "storage",
        "00c0afb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097ee4c",
      "READ",
      [
        "storage",
        "00c0afe0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097ed40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ec84.md#insn-0097ed40) · [`0097edd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ec84.md#insn-0097edd0) · [`0097eedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ec84.md#insn-0097eedc)
- 新版 `0097ed40`（命令位置の公開資料なし） · `0097edd0`（命令位置の公開資料なし） · `0097eedc`（命令位置の公開資料なし）

~~~diff
- 0097ed40 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0097ed40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097ed40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097ed40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097ed40 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0097ed40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ed40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097ed40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097ed40 bytes 08012891
+ 0097ed40 bytes 08412991
- 0097edd0 ["COPY", "tmp:0:8", ["const:f68:8"]]
- 0097edd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097edd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097edd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097edd0 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 0097edd0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097edd0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097edd0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097edd0 bytes 08a13d91
+ 0097edd0 bytes 08e13e91
- 0097eedc ["COPY", "register:4040:8", ["const:c0a000:8"]]
+ 0097eedc ["COPY", "register:4040:8", ["const:c0b000:8"]]
- 0097eedc bytes 68140090
+ 0097eedc bytes 681400b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd03994b1f4b94d2821f7e47f21b05a7"></a>

### [`0097f1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f1b0.md) → [`0097f1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097f1b0.md) FUN_0097f1b0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00979d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00979/00979d0c.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00728090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00728/00728090.md) [`00973ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00973/00973ae8.md) [`0097499c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00974/0097499c.md) [`0097f740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f740.md)
- 新版 呼出元 1件 [`00979d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00979/00979d0c.md) · 呼出先 10件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00728090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00728/00728090.md) [`00973ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00973/00973ae8.md) [`0097499c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00974/0097499c.md) [`0097f740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097f740.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.46% / 新版 98.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097f30c",
      "incomplete_value": false,
      "site": "0097f30c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097f30c",
      "incomplete_value": false,
      "site": "0097f30c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "definition_site": "0097f3cc",
      "incomplete_value": false,
      "site": "0097f3cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097f3cc",
      "incomplete_value": false,
      "site": "0097f3cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "0097f30c",
      "DATA",
      [
        "storage",
        "00c0ad68",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f3cc",
      "DATA",
      [
        "storage",
        "00c0ade8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f454",
      "READ",
      [
        "storage",
        "00c0ae10",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097f30c",
      "DATA",
      [
        "storage",
        "00c0adb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f3cc",
      "DATA",
      [
        "storage",
        "00c0ae38",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f454",
      "READ",
      [
        "storage",
        "00c0ae60",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097f304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f1b0.md#insn-0097f304) · [`0097f3c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f1b0.md#insn-0097f3c4)
- 新版 `0097f304`（命令位置の公開資料なし） · `0097f3c4`（命令位置の公開資料なし）

~~~diff
- 0097f304 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 0097f304 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097f304 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097f304 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097f304 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 0097f304 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097f304 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097f304 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097f304 bytes 29a13591
+ 0097f304 bytes 29e13691
- 0097f3c4 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 0097f3c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0097f3c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0097f3c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0097f3c4 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 0097f3c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0097f3c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0097f3c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0097f3c4 bytes 29a13791
+ 0097f3c4 bytes 29e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-653f069c88e2998c43a0ad4af624286c"></a>

### [`0097f740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f740.md) → [`0097f740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097f740.md) FUN_0097f740

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`0071cb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0071c/0071cb00.md) [`0097f1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f1b0.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00576/00576268.md) [`00584fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00584/00584fe0.md) [`0076b910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076b/0076b910.md)
- 新版 呼出元 2件 [`0071cb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0071c/0071cb00.md) [`0097f1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097f1b0.md) · 呼出先 15件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`005760a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/005760a8.md) [`00576268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00576/00576268.md) [`00584fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00584/00584fe0.md) [`0076b910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076b/0076b910.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.11% / 新版 97.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097f804",
      "incomplete_value": false,
      "site": "0097f808",
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
      "definition_site": "0097f804",
      "incomplete_value": false,
      "site": "0097f808",
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
    "ordinal": 13,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0097f894",
      "incomplete_value": false,
      "site": "0097f894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097f894",
      "incomplete_value": false,
      "site": "0097f894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "definition_site": "0097f9a4",
      "incomplete_value": false,
      "site": "0097f9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0097f9a4",
      "incomplete_value": false,
      "site": "0097f9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "0097f808",
      "DATA",
      [
        "storage",
        "00bf0a10",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f894",
      "DATA",
      [
        "storage",
        "00c0ae68",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f908",
      "READ",
      [
        "storage",
        "00c0ae90",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0097f808",
      "DATA",
      [
        "storage",
        "00bf0a60",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f894",
      "DATA",
      [
        "storage",
        "00c0aeb8",
        null,
        "undefined *"
      ]
    ],
    [
      "0097f908",
      "READ",
      [
        "storage",
        "00c0aee0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0097f7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f740.md#insn-0097f7fc) · [`0097f88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f740.md#insn-0097f88c) · [`0097f99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f740.md#insn-0097f99c)
- 新版 `0097f7fc`（命令位置の公開資料なし） · `0097f88c`（命令位置の公開資料なし） · `0097f99c`（命令位置の公開資料なし）

~~~diff
- 0097f7fc ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0097f7fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097f7fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097f7fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097f7fc ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0097f7fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097f7fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097f7fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097f7fc bytes 08012891
+ 0097f7fc bytes 08412991
- 0097f88c ["COPY", "tmp:0:8", ["const:e68:8"]]
- 0097f88c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097f88c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097f88c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097f88c ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 0097f88c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097f88c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097f88c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097f88c bytes 08a13991
+ 0097f88c bytes 08e13a91
- 0097f99c ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 0097f99c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097f99c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097f99c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097f99c ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 0097f99c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097f99c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097f99c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097f99c bytes 08a13b91
+ 0097f99c bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d253bf2264e333a20d47c266875b7cc7"></a>

### [`0097fe14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097fe14.md) → [`0097fe14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097fe14.md) FUN_0097fe14

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0097fe48",
      "incomplete_value": true,
      "site": "0097fe4c",
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
      "definition_site": "0097fe48",
      "incomplete_value": true,
      "site": "0097fe4c",
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
      "0097fe4c",
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
      "0097fe4c",
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

- 旧版 [`0097fe40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097fe14.md#insn-0097fe40)
- 新版 `0097fe40`（命令位置の公開資料なし）

~~~diff
- 0097fe40 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0097fe40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097fe40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097fe40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097fe40 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0097fe40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097fe40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097fe40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097fe40 bytes 08012891
+ 0097fe40 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6774e2d0dc465bcc03ba582239befafd"></a>

### [`0097fe88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097fe88.md) → [`0097fe88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097fe88.md) FUN_0097fe88

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "0097febc",
      "incomplete_value": false,
      "site": "0097fec0",
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
      "definition_site": "0097febc",
      "incomplete_value": false,
      "site": "0097fec0",
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
      "0097fec0",
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
      "0097fec0",
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

- 旧版 [`0097feb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097fe88.md#insn-0097feb4)
- 新版 `0097feb4`（命令位置の公開資料なし）

~~~diff
- 0097feb4 ["COPY", "tmp:0:8", ["const:a00:8"]]
- 0097feb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0097feb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0097feb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0097feb4 ["COPY", "tmp:0:8", ["const:a50:8"]]
+ 0097feb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0097feb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0097feb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0097feb4 bytes 08012891
+ 0097feb4 bytes 08412991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d03cddd70ffc11d0390b5a1f2c848be5"></a>

### [`0098044c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/0098044c.md) → [`0098044c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/0098044c.md) FUN_0098044c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00980468",
      "incomplete_value": false,
      "site": "00980478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:b38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980468",
      "incomplete_value": false,
      "site": "00980478",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
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
      "00980478",
      "DATA",
      [
        "storage",
        "00c0aae8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980478",
      "DATA",
      [
        "storage",
        "00c0ab38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/0098044c.md#insn-00980468)
- 新版 `00980468`（命令位置の公開資料なし）

~~~diff
- 00980468 ["COPY", "tmp:0:8", ["const:ae8:8"]]
- 00980468 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980468 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980468 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980468 ["COPY", "tmp:0:8", ["const:b38:8"]]
+ 00980468 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980468 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980468 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980468 bytes 08a12b91
+ 00980468 bytes 08e12c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b93085ffa72d9cc9b04818dd74fe2737"></a>

### [`00980844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980844.md) → [`00980844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980844.md) FUN_00980844

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
      "definition_site": "0098085c",
      "incomplete_value": false,
      "site": "00980868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098085c",
      "incomplete_value": false,
      "site": "00980868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "00980868",
      "DATA",
      [
        "storage",
        "00c0ab68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980868",
      "DATA",
      [
        "storage",
        "00c0abb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098085c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980844.md#insn-0098085c)
- 新版 `0098085c`（命令位置の公開資料なし）

~~~diff
- 0098085c ["COPY", "tmp:0:8", ["const:b68:8"]]
- 0098085c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098085c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098085c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098085c ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 0098085c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098085c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098085c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098085c bytes 08a12d91
+ 0098085c bytes 08e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5d8cd478eb717ce40ccd8eb7f8c17fe"></a>

### [`009808a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/009808a0.md) → [`009808a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/009808a0.md) FUN_009808a0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.94% / 新版 93.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "009808bc",
      "incomplete_value": false,
      "site": "009808cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009808bc",
      "incomplete_value": false,
      "site": "009808cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "009808cc",
      "DATA",
      [
        "storage",
        "00c0ab68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009808cc",
      "DATA",
      [
        "storage",
        "00c0abb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009808bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/009808a0.md#insn-009808bc)
- 新版 `009808bc`（命令位置の公開資料なし）

~~~diff
- 009808bc ["COPY", "tmp:0:8", ["const:b68:8"]]
- 009808bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009808bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009808bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009808bc ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 009808bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009808bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009808bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009808bc bytes 08a12d91
+ 009808bc bytes 08e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57d562342d8bafee1088e92c94bb746b"></a>

### [`00980938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980938.md) → [`00980938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980938.md) FUN_00980938

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00980948",
      "incomplete_value": false,
      "site": "00980950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980948",
      "incomplete_value": false,
      "site": "00980950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "00980950",
      "DATA",
      [
        "storage",
        "00c0ab68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980950",
      "DATA",
      [
        "storage",
        "00c0abb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980938.md#insn-00980948)
- 新版 `00980948`（命令位置の公開資料なし）

~~~diff
- 00980948 ["COPY", "tmp:0:8", ["const:b68:8"]]
- 00980948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980948 ["COPY", "tmp:0:8", ["const:bb8:8"]]
+ 00980948 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980948 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980948 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980948 bytes 08a12d91
+ 00980948 bytes 08e12e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-236f290aad16dc7ae58e6fb6d2f64554"></a>

### [`00980b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980b10.md) → [`00980b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980b10.md) FUN_00980b10

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
      "definition_site": "00980b24",
      "incomplete_value": false,
      "site": "00980b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980b24",
      "incomplete_value": false,
      "site": "00980b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "00980b28",
      "DATA",
      [
        "storage",
        "00c0abe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980b28",
      "DATA",
      [
        "storage",
        "00c0ac38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980b10.md#insn-00980b24)
- 新版 `00980b24`（命令位置の公開資料なし）

~~~diff
- 00980b24 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 00980b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980b24 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00980b24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980b24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980b24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980b24 bytes 08a12f91
+ 00980b24 bytes 08e13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe0f55565f8a74d1ed3716a9bfa2eb87"></a>

### [`00980b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980b34.md) → [`00980b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980b34.md) FUN_00980b34

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
      "definition_site": "00980b38",
      "incomplete_value": false,
      "site": "00980b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:c38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980b38",
      "incomplete_value": false,
      "site": "00980b3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "00980b3c",
      "DATA",
      [
        "storage",
        "00c0abe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980b3c",
      "DATA",
      [
        "storage",
        "00c0ac38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980b34.md#insn-00980b38)
- 新版 `00980b38`（命令位置の公開資料なし）

~~~diff
- 00980b38 ["COPY", "tmp:0:8", ["const:be8:8"]]
- 00980b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980b38 ["COPY", "tmp:0:8", ["const:c38:8"]]
+ 00980b38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980b38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980b38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980b38 bytes 08a12f91
+ 00980b38 bytes 08e13091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2c704c37ab021b0221868e3bd46b716"></a>

### [`00980b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980b7c.md) → [`00980b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980b7c.md) FUN_00980b7c

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
      "definition_site": "00980ba0",
      "incomplete_value": true,
      "site": "00980ba0",
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
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980ba0",
      "incomplete_value": true,
      "site": "00980ba0",
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
            "const:c68:8"
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
      "00980ba0",
      "DATA",
      [
        "storage",
        "00c0ac68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980ba0",
      "DATA",
      [
        "storage",
        "00c0acb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980b7c.md#insn-00980b9c)
- 新版 `00980b9c`（命令位置の公開資料なし）

~~~diff
- 00980b9c ["COPY", "tmp:0:8", ["const:c68:8"]]
- 00980b9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980b9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980b9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980b9c ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 00980b9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980b9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980b9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980b9c bytes 08a13191
+ 00980b9c bytes 08e13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfd26608c4fd6186ba4bc7c5a1bc42db"></a>

### [`00980bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980bb0.md) → [`00980bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980bb0.md) FUN_00980bb0

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
      "definition_site": "00980bbc",
      "incomplete_value": false,
      "site": "00980bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980bbc",
      "incomplete_value": false,
      "site": "00980bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:c68:8"
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
      "00980bbc",
      "DATA",
      [
        "storage",
        "00c0ac68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980bbc",
      "DATA",
      [
        "storage",
        "00c0acb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980bb0.md#insn-00980bb8)
- 新版 `00980bb8`（命令位置の公開資料なし）

~~~diff
- 00980bb8 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 00980bb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00980bb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00980bb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00980bb8 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 00980bb8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00980bb8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00980bb8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00980bb8 bytes 29a13191
+ 00980bb8 bytes 29e13291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20e7ac295d72ea4786cadd0e4f70a4bd"></a>

### [`00980d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980d44.md) → [`00980d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980d44.md) FUN_00980d44

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
      "definition_site": "00980d58",
      "incomplete_value": false,
      "site": "00980d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980d58",
      "incomplete_value": false,
      "site": "00980d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "00980d5c",
      "DATA",
      [
        "storage",
        "00c0ace8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980d5c",
      "DATA",
      [
        "storage",
        "00c0ad38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980d44.md#insn-00980d58)
- 新版 `00980d58`（命令位置の公開資料なし）

~~~diff
- 00980d58 ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 00980d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980d58 ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00980d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980d58 bytes 08a13391
+ 00980d58 bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ed4599dfcb4c1f349c9d056786adbea"></a>

### [`00980d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980d68.md) → [`00980d68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980d68.md) FUN_00980d68

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
      "definition_site": "00980d6c",
      "incomplete_value": false,
      "site": "00980d70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980d6c",
      "incomplete_value": false,
      "site": "00980d70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "00980d70",
      "DATA",
      [
        "storage",
        "00c0ace8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980d70",
      "DATA",
      [
        "storage",
        "00c0ad38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980d68.md#insn-00980d6c)
- 新版 `00980d6c`（命令位置の公開資料なし）

~~~diff
- 00980d6c ["COPY", "tmp:0:8", ["const:ce8:8"]]
- 00980d6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980d6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980d6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980d6c ["COPY", "tmp:0:8", ["const:d38:8"]]
+ 00980d6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980d6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980d6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980d6c bytes 08a13391
+ 00980d6c bytes 08e13491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f790b2c95e85a18e698104657a982c0"></a>

### [`00980dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980dac.md) → [`00980dac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980dac.md) FUN_00980dac

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
      "definition_site": "00980db8",
      "incomplete_value": false,
      "site": "00980dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980db8",
      "incomplete_value": false,
      "site": "00980dc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "00980dc4",
      "DATA",
      [
        "storage",
        "00c0ad68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980dc4",
      "DATA",
      [
        "storage",
        "00c0adb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980dac.md#insn-00980db8)
- 新版 `00980db8`（命令位置の公開資料なし）

~~~diff
- 00980db8 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 00980db8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00980db8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00980db8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00980db8 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00980db8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00980db8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00980db8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00980db8 bytes 4aa13591
+ 00980db8 bytes 4ae13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-343bdae42acc616d36af74084e54c800"></a>

### [`00980df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980df0.md) → [`00980df0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980df0.md) FUN_00980df0

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
      "definition_site": "00980e08",
      "incomplete_value": false,
      "site": "00980e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980e08",
      "incomplete_value": false,
      "site": "00980e14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "00980e14",
      "DATA",
      [
        "storage",
        "00c0ad68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980e14",
      "DATA",
      [
        "storage",
        "00c0adb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980df0.md#insn-00980e08)
- 新版 `00980e08`（命令位置の公開資料なし）

~~~diff
- 00980e08 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 00980e08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980e08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980e08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980e08 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00980e08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980e08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980e08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980e08 bytes 08a13591
+ 00980e08 bytes 08e13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b07f0795ca37d37e95828c212275733"></a>

### [`00980e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980e4c.md) → [`00980e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980e4c.md) FUN_00980e4c

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
      "definition_site": "00980e78",
      "incomplete_value": false,
      "site": "00980e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980e78",
      "incomplete_value": false,
      "site": "00980e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "00980e78",
      "DATA",
      [
        "storage",
        "00c0ad68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980e78",
      "DATA",
      [
        "storage",
        "00c0adb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980e4c.md#insn-00980e70)
- 新版 `00980e70`（命令位置の公開資料なし）

~~~diff
- 00980e70 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 00980e70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980e70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980e70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980e70 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00980e70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980e70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980e70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980e70 bytes 08a13591
+ 00980e70 bytes 08e13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc4883c0f7d2f2a88ac2463d41f34e19"></a>

### [`00980edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980edc.md) → [`00980edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00980/00980edc.md) FUN_00980edc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

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
      "definition_site": "00980efc",
      "incomplete_value": true,
      "site": "00980efc",
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
            "const:db8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00980efc",
      "incomplete_value": true,
      "site": "00980efc",
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
            "const:d68:8"
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
      "00980efc",
      "DATA",
      [
        "storage",
        "00c0ad68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00980efc",
      "DATA",
      [
        "storage",
        "00c0adb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00980ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00980/00980edc.md#insn-00980ef8)
- 新版 `00980ef8`（命令位置の公開資料なし）

~~~diff
- 00980ef8 ["COPY", "tmp:0:8", ["const:d68:8"]]
- 00980ef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00980ef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00980ef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00980ef8 ["COPY", "tmp:0:8", ["const:db8:8"]]
+ 00980ef8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00980ef8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00980ef8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00980ef8 bytes 08a13591
+ 00980ef8 bytes 08e13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93598d925ec2bfbae411fbeac6cb1385"></a>

### [`00981158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981158.md) → [`00981158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981158.md) FUN_00981158

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
      "definition_site": "00981164",
      "incomplete_value": false,
      "site": "00981170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981164",
      "incomplete_value": false,
      "site": "00981170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "00981170",
      "DATA",
      [
        "storage",
        "00c0ade8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981170",
      "DATA",
      [
        "storage",
        "00c0ae38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981158.md#insn-00981164)
- 新版 `00981164`（命令位置の公開資料なし）

~~~diff
- 00981164 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 00981164 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00981164 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00981164 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00981164 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 00981164 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00981164 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00981164 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00981164 bytes 4aa13791
+ 00981164 bytes 4ae13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0aa035fa2bb5a7450dd1ca2c5184a722"></a>

### [`0098119c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/0098119c.md) → [`0098119c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/0098119c.md) FUN_0098119c

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
      "definition_site": "009811b4",
      "incomplete_value": false,
      "site": "009811c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009811b4",
      "incomplete_value": false,
      "site": "009811c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "009811c0",
      "DATA",
      [
        "storage",
        "00c0ade8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009811c0",
      "DATA",
      [
        "storage",
        "00c0ae38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009811b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/0098119c.md#insn-009811b4)
- 新版 `009811b4`（命令位置の公開資料なし）

~~~diff
- 009811b4 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 009811b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009811b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009811b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009811b4 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 009811b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009811b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009811b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009811b4 bytes 08a13791
+ 009811b4 bytes 08e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1946be39b5bf2994f4b76f3f094e667c"></a>

### [`009811f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/009811f8.md) → [`009811f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009811f8.md) FUN_009811f8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00981224",
      "incomplete_value": false,
      "site": "00981224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981224",
      "incomplete_value": false,
      "site": "00981224",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "00981224",
      "DATA",
      [
        "storage",
        "00c0ade8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981224",
      "DATA",
      [
        "storage",
        "00c0ae38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098121c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/009811f8.md#insn-0098121c)
- 新版 `0098121c`（命令位置の公開資料なし）

~~~diff
- 0098121c ["COPY", "tmp:0:8", ["const:de8:8"]]
- 0098121c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098121c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098121c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098121c ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 0098121c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098121c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098121c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098121c bytes 08a13791
+ 0098121c bytes 08e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8ea0bf9de0d17c4c43abaac1a2df4e7"></a>

### [`00981280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981280.md) → [`00981280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981280.md) FUN_00981280

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
      "definition_site": "0098129c",
      "incomplete_value": false,
      "site": "0098129c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098129c",
      "incomplete_value": false,
      "site": "0098129c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:de8:8"
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
      "0098129c",
      "DATA",
      [
        "storage",
        "00c0ade8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098129c",
      "DATA",
      [
        "storage",
        "00c0ae38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981280.md#insn-00981298)
- 新版 `00981298`（命令位置の公開資料なし）

~~~diff
- 00981298 ["COPY", "tmp:0:8", ["const:de8:8"]]
- 00981298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00981298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00981298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00981298 ["COPY", "tmp:0:8", ["const:e38:8"]]
+ 00981298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00981298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00981298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00981298 bytes 29a13791
+ 00981298 bytes 29e13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97e3100adfeebb332e2fade59e7ae003"></a>

### [`00981420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981420.md) → [`00981420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981420.md) FUN_00981420

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0097f740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097f/0097f740.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0097f740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097f/0097f740.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "00981458",
      "incomplete_value": false,
      "site": "00981460",
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
      "definition_site": "00981458",
      "incomplete_value": false,
      "site": "00981460",
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
      "00981460",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00981518",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981460",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ],
    [
      "00981518",
      "READ",
      [
        "storage",
        "00bf31a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981420.md#insn-00981458) · [`0098145c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981420.md#insn-0098145c)
- 新版 `00981458`（命令位置の公開資料なし） · `0098145c`（命令位置の公開資料なし）

~~~diff
- 00981458 ["COPY", "tmp:0:8", ["const:148:8"]]
- 00981458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00981458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00981458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00981458 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00981458 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00981458 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00981458 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00981458 bytes 08210591
+ 00981458 bytes 08610691
- 0098145c ["COPY", "register:4098:8", ["register:4000:8"]]
- 0098145c bytes f30300aa
+ 0098145c ["COPY", "register:4098:8", ["register:4000:8"]]
+ 0098145c bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-970a4e1e5e603ef91128e7cb8ac80f35"></a>

### [`00981598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981598.md) → [`00981598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981598.md) FUN_00981598

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
      "definition_site": "009815a4",
      "incomplete_value": false,
      "site": "009815b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009815a4",
      "incomplete_value": false,
      "site": "009815b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "009815b0",
      "DATA",
      [
        "storage",
        "00c0ae68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009815b0",
      "DATA",
      [
        "storage",
        "00c0aeb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009815a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981598.md#insn-009815a4)
- 新版 `009815a4`（命令位置の公開資料なし）

~~~diff
- 009815a4 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 009815a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009815a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009815a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009815a4 ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 009815a4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009815a4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009815a4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009815a4 bytes 4aa13991
+ 009815a4 bytes 4ae13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fbdd019c209eea815e8c90c9d2beb29"></a>

### [`009815dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/009815dc.md) → [`009815dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009815dc.md) FUN_009815dc

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
      "definition_site": "009815f4",
      "incomplete_value": false,
      "site": "00981600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009815f4",
      "incomplete_value": false,
      "site": "00981600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "00981600",
      "DATA",
      [
        "storage",
        "00c0ae68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981600",
      "DATA",
      [
        "storage",
        "00c0aeb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009815f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/009815dc.md#insn-009815f4)
- 新版 `009815f4`（命令位置の公開資料なし）

~~~diff
- 009815f4 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 009815f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009815f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009815f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009815f4 ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 009815f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009815f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009815f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009815f4 bytes 08a13991
+ 009815f4 bytes 08e13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-438670ffc0afca9c5ba6195711db4bab"></a>

### [`009816c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/009816c0.md) → [`009816c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009816c0.md) FUN_009816c0

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
      "definition_site": "009816dc",
      "incomplete_value": false,
      "site": "009816dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:eb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009816dc",
      "incomplete_value": false,
      "site": "009816dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:e68:8"
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
      "009816dc",
      "DATA",
      [
        "storage",
        "00c0ae68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009816dc",
      "DATA",
      [
        "storage",
        "00c0aeb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009816d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/009816c0.md#insn-009816d8)
- 新版 `009816d8`（命令位置の公開資料なし）

~~~diff
- 009816d8 ["COPY", "tmp:0:8", ["const:e68:8"]]
- 009816d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009816d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009816d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009816d8 ["COPY", "tmp:0:8", ["const:eb8:8"]]
+ 009816d8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009816d8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009816d8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009816d8 bytes 29a13991
+ 009816d8 bytes 29e13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87bc24098b743e89ac63ee1fb6705039"></a>

### [`00981858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981858.md) → [`00981858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981858.md) FUN_00981858

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
      "definition_site": "00981864",
      "incomplete_value": false,
      "site": "00981870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981864",
      "incomplete_value": false,
      "site": "00981870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "00981870",
      "DATA",
      [
        "storage",
        "00c0aee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981870",
      "DATA",
      [
        "storage",
        "00c0af38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981858.md#insn-00981864)
- 新版 `00981864`（命令位置の公開資料なし）

~~~diff
- 00981864 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 00981864 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00981864 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00981864 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00981864 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00981864 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00981864 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00981864 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00981864 bytes 4aa13b91
+ 00981864 bytes 4ae13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31f06b54dd5ea04a5a97d9d2fa0fcef6"></a>

### [`0098189c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/0098189c.md) → [`0098189c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/0098189c.md) FUN_0098189c

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
      "definition_site": "009818b4",
      "incomplete_value": false,
      "site": "009818c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009818b4",
      "incomplete_value": false,
      "site": "009818c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "009818c0",
      "DATA",
      [
        "storage",
        "00c0aee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009818c0",
      "DATA",
      [
        "storage",
        "00c0af38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009818b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/0098189c.md#insn-009818b4)
- 新版 `009818b4`（命令位置の公開資料なし）

~~~diff
- 009818b4 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 009818b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009818b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009818b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009818b4 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 009818b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009818b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009818b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009818b4 bytes 08a13b91
+ 009818b4 bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c7c8111dc396294f8b42e082d89e10b1"></a>

### [`009818f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/009818f8.md) → [`009818f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/009818f8.md) FUN_009818f8

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00981924",
      "incomplete_value": false,
      "site": "00981924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981924",
      "incomplete_value": false,
      "site": "00981924",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "00981924",
      "DATA",
      [
        "storage",
        "00c0aee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981924",
      "DATA",
      [
        "storage",
        "00c0af38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098191c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/009818f8.md#insn-0098191c)
- 新版 `0098191c`（命令位置の公開資料なし）

~~~diff
- 0098191c ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 0098191c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098191c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098191c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098191c ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 0098191c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098191c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098191c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098191c bytes 08a13b91
+ 0098191c bytes 08e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d54a21fcc9bf592a9b161f30be730f4"></a>

### [`00981980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981980.md) → [`00981980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981980.md) FUN_00981980

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
      "definition_site": "0098199c",
      "incomplete_value": false,
      "site": "0098199c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:f38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098199c",
      "incomplete_value": false,
      "site": "0098199c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:ee8:8"
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
      "0098199c",
      "DATA",
      [
        "storage",
        "00c0aee8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098199c",
      "DATA",
      [
        "storage",
        "00c0af38",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981980.md#insn-00981998)
- 新版 `00981998`（命令位置の公開資料なし）

~~~diff
- 00981998 ["COPY", "tmp:0:8", ["const:ee8:8"]]
- 00981998 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00981998 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00981998 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00981998 ["COPY", "tmp:0:8", ["const:f38:8"]]
+ 00981998 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00981998 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00981998 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00981998 bytes 29a13b91
+ 00981998 bytes 29e13c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-beb8d29342942762960fd7a900f97608"></a>

### [`00981ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981ac4.md) → [`00981ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981ac4.md) FUN_00981ac4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0097ec84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097ec84.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0097ec84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097ec84.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "00981afc",
      "incomplete_value": false,
      "site": "00981b04",
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
      "definition_site": "00981afc",
      "incomplete_value": false,
      "site": "00981b04",
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
      "00981b04",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00981bbc",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981b04",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ],
    [
      "00981bbc",
      "READ",
      [
        "storage",
        "00bf31a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981ac4.md#insn-00981afc) · [`00981b00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981ac4.md#insn-00981b00)
- 新版 `00981afc`（命令位置の公開資料なし） · `00981b00`（命令位置の公開資料なし）

~~~diff
- 00981afc ["COPY", "tmp:0:8", ["const:148:8"]]
- 00981afc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00981afc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00981afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00981afc ["COPY", "tmp:0:8", ["const:198:8"]]
+ 00981afc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00981afc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00981afc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00981afc bytes 08210591
+ 00981afc bytes 08610691
- 00981b00 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00981b00 bytes f30300aa
+ 00981b00 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00981b00 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b57300908b24cb1b289aae7c9666cb9"></a>

### [`00981c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981c3c.md) → [`00981c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981c3c.md) FUN_00981c3c

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00981c48",
      "incomplete_value": true,
      "site": "00981c54",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981c48",
      "incomplete_value": true,
      "site": "00981c54",
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
            "const:f68:8"
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
      "00981c54",
      "DATA",
      [
        "storage",
        "00c0af68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981c54",
      "DATA",
      [
        "storage",
        "00c0afb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981c3c.md#insn-00981c48)
- 新版 `00981c48`（命令位置の公開資料なし）

~~~diff
- 00981c48 ["COPY", "tmp:0:8", ["const:f68:8"]]
- 00981c48 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00981c48 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00981c48 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00981c48 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 00981c48 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00981c48 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00981c48 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00981c48 bytes 4aa13d91
+ 00981c48 bytes 4ae13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec6b25ccef1ce61f67f46b5e79347f2e"></a>

### [`00981cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981cdc.md) → [`00981cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981cdc.md) FUN_00981cdc

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00981d08",
      "incomplete_value": false,
      "site": "00981d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981d08",
      "incomplete_value": false,
      "site": "00981d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "00981d08",
      "DATA",
      [
        "storage",
        "00c0af68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981d08",
      "DATA",
      [
        "storage",
        "00c0afb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981cdc.md#insn-00981d00)
- 新版 `00981d00`（命令位置の公開資料なし）

~~~diff
- 00981d00 ["COPY", "tmp:0:8", ["const:f68:8"]]
- 00981d00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00981d00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00981d00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00981d00 ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 00981d00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00981d00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00981d00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00981d00 bytes 08a13d91
+ 00981d00 bytes 08e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70faa978f72235f9110d433a0b3d4f0c"></a>

### [`00981d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981d64.md) → [`00981d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981d64.md) FUN_00981d64

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
      "definition_site": "00981d80",
      "incomplete_value": false,
      "site": "00981d80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981d80",
      "incomplete_value": false,
      "site": "00981d80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "00981d80",
      "DATA",
      [
        "storage",
        "00c0af68",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981d80",
      "DATA",
      [
        "storage",
        "00c0afb8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981d64.md#insn-00981d7c)
- 新版 `00981d7c`（命令位置の公開資料なし）

~~~diff
- 00981d7c ["COPY", "tmp:0:8", ["const:f68:8"]]
- 00981d7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00981d7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00981d7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00981d7c ["COPY", "tmp:0:8", ["const:fb8:8"]]
+ 00981d7c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00981d7c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00981d7c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00981d7c bytes 29a13d91
+ 00981d7c bytes 29e13e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d491571a43df5df78bc4966bc36be2c"></a>

### [`00981efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981efc.md) → [`00981efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981efc.md) FUN_00981efc

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
      "definition_site": "00981f08",
      "incomplete_value": false,
      "site": "00981f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981f08",
      "incomplete_value": false,
      "site": "00981f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "00981f14",
      "DATA",
      [
        "storage",
        "00c0afe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981f14",
      "DATA",
      [
        "storage",
        "00c0b038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981efc.md#insn-00981f04) · [`00981f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981efc.md#insn-00981f08)
- 新版 `00981f04`（命令位置の公開資料なし） · `00981f08`（命令位置の公開資料なし）

~~~diff
- 00981f04 ["COPY", "register:4050:8", ["const:c0a000:8"]]
+ 00981f04 ["COPY", "register:4050:8", ["const:c0b000:8"]]
- 00981f04 bytes 4a1400b0
+ 00981f04 bytes 4a1400d0
- 00981f08 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00981f08 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00981f08 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00981f08 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00981f08 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00981f08 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00981f08 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00981f08 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00981f08 bytes 4aa13f91
+ 00981f08 bytes 4ae10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-13a7f96a70571b6d6be4ae032629977c"></a>

### [`00981f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981f40.md) → [`00981f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981f40.md) FUN_00981f40

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
      "definition_site": "00981f58",
      "incomplete_value": false,
      "site": "00981f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981f58",
      "incomplete_value": false,
      "site": "00981f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "00981f64",
      "DATA",
      [
        "storage",
        "00c0afe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981f64",
      "DATA",
      [
        "storage",
        "00c0b038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981f40.md#insn-00981f54) · [`00981f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981f40.md#insn-00981f58)
- 新版 `00981f54`（命令位置の公開資料なし） · `00981f58`（命令位置の公開資料なし）

~~~diff
- 00981f54 ["COPY", "register:4040:8", ["const:c0a000:8"]]
+ 00981f54 ["COPY", "register:4040:8", ["const:c0b000:8"]]
- 00981f54 bytes 481400b0
+ 00981f54 bytes 481400d0
- 00981f58 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00981f58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00981f58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00981f58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00981f58 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00981f58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00981f58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00981f58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00981f58 bytes 08a13f91
+ 00981f58 bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8d18fb95e73b26cdaba493c10569709"></a>

### [`00981f9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981f9c.md) → [`00981f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00981/00981f9c.md) FUN_00981f9c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00981fc8",
      "incomplete_value": false,
      "site": "00981fc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00981fc8",
      "incomplete_value": false,
      "site": "00981fc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0a000:8"
          ],
          [
            "leaf",
            "const:fe8:8"
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
      "00981fc8",
      "DATA",
      [
        "storage",
        "00c0afe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00981fc8",
      "DATA",
      [
        "storage",
        "00c0b038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00981fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981f9c.md#insn-00981fbc) · [`00981fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00981/00981f9c.md#insn-00981fc0)
- 新版 `00981fbc`（命令位置の公開資料なし） · `00981fc0`（命令位置の公開資料なし）

~~~diff
- 00981fbc ["COPY", "register:4040:8", ["const:c0a000:8"]]
+ 00981fbc ["COPY", "register:4040:8", ["const:c0b000:8"]]
- 00981fbc bytes 481400b0
+ 00981fbc bytes 481400d0
- 00981fc0 ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 00981fc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00981fc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00981fc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00981fc0 ["COPY", "tmp:0:8", ["const:38:8"]]
+ 00981fc0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00981fc0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00981fc0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00981fc0 bytes 08a13f91
+ 00981fc0 bytes 08e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1577071aac8ad408e0ae3795cb7fa64b"></a>

### [`00982024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982024.md) → [`00982024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982024.md) FUN_00982024

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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00982040",
      "incomplete_value": true,
      "site": "00982040",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00982040",
      "incomplete_value": true,
      "site": "00982040",
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
            "const:fe8:8"
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
      "00982040",
      "DATA",
      [
        "storage",
        "00c0afe8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00982040",
      "DATA",
      [
        "storage",
        "00c0b038",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00982038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982024.md#insn-00982038) · [`0098203c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982024.md#insn-0098203c)
- 新版 `00982038`（命令位置の公開資料なし） · `0098203c`（命令位置の公開資料なし）

~~~diff
- 00982038 ["COPY", "register:4048:8", ["const:c0a000:8"]]
+ 00982038 ["COPY", "register:4048:8", ["const:c0b000:8"]]
- 00982038 bytes 49140090
+ 00982038 bytes 491400b0
- 0098203c ["COPY", "tmp:0:8", ["const:fe8:8"]]
- 0098203c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0098203c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0098203c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0098203c ["COPY", "tmp:0:8", ["const:38:8"]]
+ 0098203c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0098203c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0098203c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0098203c bytes 29a13f91
+ 0098203c bytes 29e10091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abbb3317d36263ccb912de19e3dfadc7"></a>

### [`00982168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982168.md) → [`00982168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982168.md) FUN_00982168

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0097e4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0097e/0097e4e8.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00592/00592ccc.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md)
- 新版 呼出元 1件 [`0097e4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0097e/0097e4e8.md) · 呼出先 7件 [`00574ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff8.md) [`00592ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00592/00592ccc.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md)

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
      "definition_site": "009821a0",
      "incomplete_value": false,
      "site": "009821a8",
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
      "definition_site": "009821a0",
      "incomplete_value": false,
      "site": "009821a8",
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
      "009821a8",
      "DATA",
      [
        "storage",
        "00bf3148",
        null,
        "pointer"
      ]
    ],
    [
      "00982260",
      "READ",
      [
        "storage",
        "00bf3158",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009821a8",
      "DATA",
      [
        "storage",
        "00bf3198",
        null,
        "pointer"
      ]
    ],
    [
      "00982260",
      "READ",
      [
        "storage",
        "00bf31a8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009821a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982168.md#insn-009821a0) · [`009821a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982168.md#insn-009821a4)
- 新版 `009821a0`（命令位置の公開資料なし） · `009821a4`（命令位置の公開資料なし）

~~~diff
- 009821a0 ["COPY", "tmp:0:8", ["const:148:8"]]
- 009821a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009821a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009821a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009821a0 ["COPY", "tmp:0:8", ["const:198:8"]]
+ 009821a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009821a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009821a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009821a0 bytes 08210591
+ 009821a0 bytes 08610691
- 009821a4 ["COPY", "register:4098:8", ["register:4000:8"]]
- 009821a4 bytes f30300aa
+ 009821a4 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 009821a4 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d573be9a9509523b5fcf8463511b1441"></a>

### [`009822e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/009822e0.md) → [`009822e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/009822e0.md) FUN_009822e0

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
      "definition_site": "009822ec",
      "incomplete_value": false,
      "site": "009822f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009822ec",
      "incomplete_value": false,
      "site": "009822f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:68:8"
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
      "009822f8",
      "DATA",
      [
        "storage",
        "00c0b068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009822f8",
      "DATA",
      [
        "storage",
        "00c0b0b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009822ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/009822e0.md#insn-009822ec)
- 新版 `009822ec`（命令位置の公開資料なし）

~~~diff
- 009822ec ["COPY", "tmp:0:8", ["const:68:8"]]
- 009822ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009822ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009822ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009822ec ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 009822ec ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009822ec ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009822ec ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009822ec bytes 4aa10191
+ 009822ec bytes 4ae10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6da1cedb296f53b466653fb61812ae9c"></a>

### [`00982324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982324.md) → [`00982324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982324.md) FUN_00982324

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
      "definition_site": "0098233c",
      "incomplete_value": false,
      "site": "00982348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098233c",
      "incomplete_value": false,
      "site": "00982348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:68:8"
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
      "00982348",
      "DATA",
      [
        "storage",
        "00c0b068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00982348",
      "DATA",
      [
        "storage",
        "00c0b0b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098233c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982324.md#insn-0098233c)
- 新版 `0098233c`（命令位置の公開資料なし）

~~~diff
- 0098233c ["COPY", "tmp:0:8", ["const:68:8"]]
- 0098233c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098233c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098233c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098233c ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 0098233c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098233c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098233c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098233c bytes 08a10191
+ 0098233c bytes 08e10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4df5315ad6ae9ee2bd8802fb0015511"></a>

### [`00982380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982380.md) → [`00982380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982380.md) FUN_00982380

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "009823ac",
      "incomplete_value": false,
      "site": "009823ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009823ac",
      "incomplete_value": false,
      "site": "009823ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:68:8"
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
      "009823ac",
      "DATA",
      [
        "storage",
        "00c0b068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009823ac",
      "DATA",
      [
        "storage",
        "00c0b0b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009823a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982380.md#insn-009823a4)
- 新版 `009823a4`（命令位置の公開資料なし）

~~~diff
- 009823a4 ["COPY", "tmp:0:8", ["const:68:8"]]
- 009823a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 009823a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 009823a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 009823a4 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 009823a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 009823a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 009823a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 009823a4 bytes 08a10191
+ 009823a4 bytes 08e10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d90d402adc6f96322c4a190459a94af2"></a>

### [`00982408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982408.md) → [`00982408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982408.md) FUN_00982408

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
      "definition_site": "00982424",
      "incomplete_value": false,
      "site": "00982424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00982424",
      "incomplete_value": false,
      "site": "00982424",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:68:8"
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
      "00982424",
      "DATA",
      [
        "storage",
        "00c0b068",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00982424",
      "DATA",
      [
        "storage",
        "00c0b0b8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00982420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982408.md#insn-00982420)
- 新版 `00982420`（命令位置の公開資料なし）

~~~diff
- 00982420 ["COPY", "tmp:0:8", ["const:68:8"]]
- 00982420 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00982420 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00982420 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00982420 ["COPY", "tmp:0:8", ["const:b8:8"]]
+ 00982420 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00982420 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00982420 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00982420 bytes 29a10191
+ 00982420 bytes 29e10291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d12c5cac84dd211b923145f36ea4eac3"></a>

### [`009825a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/009825a0.md) → [`009825a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/009825a0.md) FUN_009825a0

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
      "definition_site": "009825ac",
      "incomplete_value": false,
      "site": "009825b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009825ac",
      "incomplete_value": false,
      "site": "009825b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
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
      "009825b8",
      "DATA",
      [
        "storage",
        "00c0b0e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009825b8",
      "DATA",
      [
        "storage",
        "00c0b138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009825ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/009825a0.md#insn-009825ac)
- 新版 `009825ac`（命令位置の公開資料なし）

~~~diff
- 009825ac ["COPY", "tmp:0:8", ["const:e8:8"]]
- 009825ac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 009825ac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 009825ac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 009825ac ["COPY", "tmp:0:8", ["const:138:8"]]
+ 009825ac ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 009825ac ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 009825ac ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 009825ac bytes 4aa10391
+ 009825ac bytes 4ae10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc419244c6404e6b5e8a027e0b0bca75"></a>

### [`00982640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982640.md) → [`00982640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982640.md) FUN_00982640

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "0098266c",
      "incomplete_value": false,
      "site": "0098266c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0098266c",
      "incomplete_value": false,
      "site": "0098266c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
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
      "0098266c",
      "DATA",
      [
        "storage",
        "00c0b0e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0098266c",
      "DATA",
      [
        "storage",
        "00c0b138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00982664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982640.md#insn-00982664)
- 新版 `00982664`（命令位置の公開資料なし）

~~~diff
- 00982664 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00982664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00982664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00982664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00982664 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 00982664 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00982664 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00982664 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00982664 bytes 08a10391
+ 00982664 bytes 08e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c62c783412acf3ba6551df104dc181d4"></a>

### [`009826c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/009826c8.md) → [`009826c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/009826c8.md) FUN_009826c8

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
      "definition_site": "009826e4",
      "incomplete_value": false,
      "site": "009826e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:138:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "009826e4",
      "incomplete_value": false,
      "site": "009826e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
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
      "009826e4",
      "DATA",
      [
        "storage",
        "00c0b0e8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "009826e4",
      "DATA",
      [
        "storage",
        "00c0b138",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`009826e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/009826c8.md#insn-009826e0)
- 新版 `009826e0`（命令位置の公開資料なし）

~~~diff
- 009826e0 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 009826e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 009826e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 009826e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 009826e0 ["COPY", "tmp:0:8", ["const:138:8"]]
+ 009826e0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 009826e0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 009826e0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 009826e0 bytes 29a10391
+ 009826e0 bytes 29e10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30e9995797fc49098b8eea0c9f98d152"></a>

### [`0098280c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/0098280c.md) → [`0098280c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/0098280c.md) _INIT_192

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418cb8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00418330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418330.md) [`00418cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418cb8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "0098288c",
      "incomplete_value": true,
      "site": "009828a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "0098288c",
      "incomplete_value": true,
      "site": "009828a8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009828ac",
      "incomplete_value": true,
      "site": "009828c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009828ac",
      "incomplete_value": true,
      "site": "009828c4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009828c8",
      "incomplete_value": true,
      "site": "009828e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "definition_site": "009828c8",
      "incomplete_value": true,
      "site": "009828e4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
      "00982848",
      "READ",
      [
        "storage",
        "002a72dd",
        null,
        "string"
      ]
    ],
    [
      "0098286c",
      "READ",
      [
        "storage",
        "002a72f0",
        null,
        "string"
      ]
    ],
    [
      "0098288c",
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
      "00982848",
      "READ",
      [
        "storage",
        "002a7377",
        null,
        "string"
      ]
    ],
    [
      "0098286c",
      "READ",
      [
        "storage",
        "002a738a",
        null,
        "string"
      ]
    ],
    [
      "0098288c",
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

- 旧版 [`00982838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/0098280c.md#insn-00982838) · [`00982840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/0098280c.md#insn-00982840)
- 新版 `00982838`（命令位置の公開資料なし） · `00982840`（命令位置の公開資料なし）

~~~diff
- 00982838 ["COPY", "tmp:0:8", ["const:998:8"]]
- 00982838 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00982838 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00982838 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00982838 ["COPY", "tmp:0:8", ["const:9d8:8"]]
+ 00982838 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00982838 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00982838 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00982838 bytes 73622691
+ 00982838 bytes 73622791
- 00982840 ["COPY", "register:4048:8", ["const:2a7000:8"]]
- 00982840 bytes 29c9ffb0
+ 00982840 ["COPY", "register:4048:8", ["const:2a7000:8"]]
+ 00982840 bytes 29c9ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-560f2f45ec6fd41176caa014fdfed3b3"></a>

### [`00982c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982c5c.md) → [`00982c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982c5c.md) FUN_00982c5c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0073496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00734/0073496c.md) · 呼出先 13件 [`009009cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00900/009009cc.md) [`0090126c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00901/0090126c.md) [`00977eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00977/00977eec.md) [`00982ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982ed4.md) [`00983570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00983/00983570.md)
- 新版 呼出元 1件 [`0073496c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00734/0073496c.md) · 呼出先 13件 [`009009cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00900/009009cc.md) [`0090126c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00901/0090126c.md) [`00977eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00977/00977eec.md) [`00982ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982ed4.md) [`00983570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00983/00983570.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.44% / 新版 98.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00982dbc",
      "incomplete_value": false,
      "site": "00982dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00982dbc",
      "incomplete_value": false,
      "site": "00982dbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c0b000:8"
          ],
          [
            "leaf",
            "const:168:8"
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
      "00982dbc",
      "DATA",
      [
        "storage",
        "00c0b168",
        null,
        "undefined *"
      ]
    ],
    [
      "00982df4",
      "READ",
      [
        "storage",
        "00c0b188",
        null,
        "pointer"
      ]
    ],
    [
      "00982df4",
      "READ",
      [
        "storage",
        "00c0b190",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00982dbc",
      "DATA",
      [
        "storage",
        "00c0b1b8",
        null,
        "undefined *"
      ]
    ],
    [
      "00982df4",
      "READ",
      [
        "storage",
        "00c0b1d8",
        null,
        "pointer"
      ]
    ],
    [
      "00982df4",
      "READ",
      [
        "storage",
        "00c0b1e0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00982db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982c5c.md#insn-00982db4)
- 新版 `00982db4`（命令位置の公開資料なし）

~~~diff
- 00982db4 ["COPY", "tmp:0:8", ["const:168:8"]]
- 00982db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00982db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00982db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00982db4 ["COPY", "tmp:0:8", ["const:1b8:8"]]
+ 00982db4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00982db4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00982db4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00982db4 bytes 08a10591
+ 00982db4 bytes 08e10691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c9aef56fae5f43e12df58b240b1e65a"></a>

### [`00982ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982ed4.md) → [`00982ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982ed4.md) FUN_00982ed4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00982c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982c5c.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00459a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045b/0045bedc.md)
- 新版 呼出元 1件 [`00982c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982c5c.md) · 呼出先 20件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00459a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00459/00459a90.md) [`0045b734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045b734.md) [`0045ba04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045ba04.md) [`0045bedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045b/0045bedc.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.29% / 新版 92.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0098341c",
      "incomplete_value": false,
      "site": "0098341c",
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
      "definition_site": "0098341c",
      "incomplete_value": false,
      "site": "0098341c",
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
    "ordinal": 37,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00983420",
      "incomplete_value": false,
      "site": "00983420",
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
      "definition_site": "00983420",
      "incomplete_value": false,
      "site": "00983420",
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
    "ordinal": 38,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0098341c",
      "incomplete_value": false,
      "site": "00983420",
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
      "definition_site": "0098341c",
      "incomplete_value": false,
      "site": "00983420",
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
      "00982f10",
      "READ",
      [
        "storage",
        "00c25038",
        null,
        "undefined1"
      ]
    ],
    [
      "00982f1c",
      "PARAM",
      [
        "storage",
        "00c25000",
        null,
        "undefined8"
      ]
    ],
    [
      "00982f24",
      "PARAM",
      [
        "storage",
        "0109e9d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00982f10",
      "READ",
      [
        "storage",
        "00c25078",
        null,
        "undefined1"
      ]
    ],
    [
      "00982f1c",
      "PARAM",
      [
        "storage",
        "00c25040",
        null,
        "undefined8"
      ]
    ],
    [
      "00982f24",
      "PARAM",
      [
        "storage",
        "0109ea10",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00982f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982ed4.md#insn-00982f0c) · [`00982f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982ed4.md#insn-00982f1c) · [`00982f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982ed4.md#insn-00982f24)
- 新版 `00982f0c`（命令位置の公開資料なし） · `00982f1c`（命令位置の公開資料なし） · `00982f24`（命令位置の公開資料なし）

~~~diff
- 00982f0c ["COPY", "tmp:0:8", ["const:38:8"]]
- 00982f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00982f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00982f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00982f0c ["COPY", "tmp:0:8", ["const:78:8"]]
+ 00982f0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00982f0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00982f0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00982f0c bytes 08e10091
+ 00982f0c bytes 08e10191
- 00982f1c ["COPY", "tmp:0:8", ["const:0:8"]]
- 00982f1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00982f1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00982f1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00982f1c ["COPY", "tmp:0:8", ["const:40:8"]]
+ 00982f1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00982f1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00982f1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00982f1c bytes 00000091
+ 00982f1c bytes 00000191
- 00982f24 ["COPY", "tmp:0:8", ["const:9d0:8"]]
- 00982f24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00982f24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00982f24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00982f24 ["COPY", "tmp:0:8", ["const:a10:8"]]
+ 00982f24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00982f24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00982f24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00982f24 bytes 21402791
+ 00982f24 bytes 21402891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-186272c6de1a85708ee757b4c6a74e94"></a>

### [`00983570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00983/00983570.md) → [`00983570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00983/00983570.md) FUN_00983570

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00982c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00982/00982c5c.md) · 呼出先 12件 [`00467074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005b3/005b3ebc.md) [`00883d5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883d5c.md) [`00883e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00883/00883e08.md) [`009846f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00984/009846f8.md)
- 新版 呼出元 1件 [`00982c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00982/00982c5c.md) · 呼出先 12件 [`00467074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00467/00467074.md) [`005b3ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/005b3/005b3ebc.md) [`00883d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883d5c.md) [`00883e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00883/00883e08.md) [`009846f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00984/009846f8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00983724",
      "incomplete_value": false,
      "site": "00983728",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d80:8"
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
      "definition_site": "00983724",
      "incomplete_value": false,
      "site": "00983728",
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
                "const:c0b000:8"
              ],
              [
                "leaf",
                "const:d30:8"
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
      "00983670",
      "DATA",
      [
        "storage",
        "00c0b1e8",
        null,
        "undefined *"
      ]
    ],
    [
      "009836cc",
      "READ",
      [
        "storage",
        "00c0b208",
        null,
        "pointer"
      ]
    ],
    [
      "009836cc",
      "READ",
      [
        "storage",
        "00c0b210",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00983670",
      "DATA",
      [
        "storage",
        "00c0b238",
        null,
        "undefined *"
      ]
    ],
    [
      "009836cc",
      "READ",
      [
        "storage",
        "00c0b258",
        null,
        "pointer"
      ]
    ],
    [
      "009836cc",
      "READ",
      [
        "storage",
        "00c0b260",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0098365c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00983/00983570.md#insn-0098365c) · [`009836dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00983/00983570.md#insn-009836dc) · [`0098371c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00983/00983570.md#insn-0098371c)
- 新版 `0098365c`（命令位置の公開資料なし） · `009836dc`（命令位置の公開資料なし） · `0098371c`（命令位置の公開資料なし）

~~~diff
- 0098365c ["COPY", "tmp:0:8", ["const:1e8:8"]]
- 0098365c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0098365c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0098365c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0098365c ["COPY", "tmp:0:8", ["const:238:8"]]
+ 0098365c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0098365c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0098365c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0098365c bytes 4aa10791
+ 0098365c bytes 4ae10891
- 009836dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:520:8"]]
- 009836dc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 009836dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:570:8"]]
+ 009836dc ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 009836dc bytes b59242f9
+ 009836dc bytes b5ba42f9
- 0098371c ["COPY", "tmp:0:8", ["const:d30:8"]]
- 0098371c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0098371c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0098371c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0098371c ["COPY", "tmp:0:8", ["const:d80:8"]]
+ 0098371c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0098371c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0098371c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0098371c bytes 08c13491
+ 0098371c bytes 08013691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

