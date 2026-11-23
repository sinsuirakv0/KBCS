# v15.7.3 → v15.7.4 · 最優先の変更候補 (3)

[一覧の目次](README.md)

<a id="compare-2e934fabb9797b187824701170857525"></a>

### [`0043785c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/0043785c.md) → [`0043785c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/0043785c.md) FUN_0043785c

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
      "definition_site": "00437870",
      "incomplete_value": false,
      "site": "00437874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437870",
      "incomplete_value": false,
      "site": "00437874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "00437874",
      "DATA",
      [
        "storage",
        "00be68f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00437874",
      "DATA",
      [
        "storage",
        "00be6940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/0043785c.md#insn-00437870)
- 新版 `00437870`（命令位置の公開資料なし）

~~~diff
- 00437870 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00437870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00437870 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00437870 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00437870 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00437870 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437870 bytes 08c12391
+ 00437870 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b41f36dc4f1b48278990adc1a241f20"></a>

### [`00437880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437880.md) → [`00437880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437880.md) FUN_00437880

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
      "definition_site": "00437884",
      "incomplete_value": false,
      "site": "00437888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437884",
      "incomplete_value": false,
      "site": "00437888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "00437888",
      "DATA",
      [
        "storage",
        "00be68f0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00437888",
      "DATA",
      [
        "storage",
        "00be6940",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437880.md#insn-00437884)
- 新版 `00437884`（命令位置の公開資料なし）

~~~diff
- 00437884 ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00437884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00437884 ["COPY", "tmp:0:8", ["const:940:8"]]
+ 00437884 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00437884 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00437884 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437884 bytes 08c12391
+ 00437884 bytes 08012591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6819c0209ad06c05daa860ce0ee2b38e"></a>

### [`00437898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437898.md) → [`00437898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437898.md) FUN_00437898

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00573e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573e38.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 91.72% / 新版 91.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004379c4",
      "incomplete_value": true,
      "site": "004379c4",
      "value": [
        "LOAD",
        "8",
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
                "const:50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004379c4",
      "incomplete_value": true,
      "site": "004379c4",
      "value": [
        "LOAD",
        "8",
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
                "const:50:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004379b8",
      "incomplete_value": true,
      "site": "004379c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004379b8",
      "incomplete_value": true,
      "site": "004379c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00437a34",
      "incomplete_value": true,
      "site": "00437a34",
      "value": [
        "LOAD",
        "8",
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
                "const:58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437a34",
      "incomplete_value": true,
      "site": "00437a34",
      "value": [
        "LOAD",
        "8",
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
                "const:58:8"
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
      "004379a8",
      "READ",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "004379b8",
      "READ",
      [
        "storage",
        "00c24b98",
        null,
        "undefined8"
      ]
    ],
    [
      "004379d4",
      "READ",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "004379a8",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "004379b8",
      "READ",
      [
        "storage",
        "00c24bd8",
        null,
        "undefined8"
      ]
    ],
    [
      "004379d4",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004379a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437898.md#insn-004379a4) · [`004379b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437898.md#insn-004379b8) · [`004379d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437898.md#insn-004379d0)
- 新版 `004379a4`（命令位置の公開資料なし） · `004379b8`（命令位置の公開資料なし） · `004379d0`（命令位置の公開資料なし）

~~~diff
- 004379a4 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 004379a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004379a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004379a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004379a4 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 004379a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004379a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004379a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004379a4 bytes 08812e91
+ 004379a4 bytes 08812f91
- 004379b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b98:8"]]
- 004379b8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 004379b8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd8:8"]]
+ 004379b8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 004379b8 bytes 00cd45f9
+ 004379b8 bytes 00ed45f9
- 004379d0 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 004379d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004379d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004379d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004379d0 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 004379d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004379d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004379d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004379d0 bytes 08812e91
+ 004379d0 bytes 08812f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ca57e2496a7c516ae3b161b94f03970"></a>

### [`00437bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437bb4.md) → [`00437bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437bb4.md) FUN_00437bb4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`0042eef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eef4.md)
- 新版 呼出元 0件  · 呼出先 1件 [`0042eef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eef4.md)

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
      "definition_site": "00437bbc",
      "incomplete_value": false,
      "site": "00437bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437bbc",
      "incomplete_value": false,
      "site": "00437bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "00437bbc",
      "DATA",
      [
        "storage",
        "00be6970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00437bbc",
      "DATA",
      [
        "storage",
        "00be69c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437bb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437bb4.md#insn-00437bb8)
- 新版 `00437bb8`（命令位置の公開資料なし）

~~~diff
- 00437bb8 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00437bb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437bb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437bb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00437bb8 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00437bb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00437bb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00437bb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437bb8 bytes 08c12591
+ 00437bb8 bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ece5a2dd841370d5be93693c8ab7b75e"></a>

### [`00437bc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437bc4.md) → [`00437bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437bc4.md) FUN_00437bc4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`0042eef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042eef4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 2件 [`0042eef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042eef4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00437bdc",
      "incomplete_value": false,
      "site": "00437bdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437bdc",
      "incomplete_value": false,
      "site": "00437bdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "00437bdc",
      "DATA",
      [
        "storage",
        "00be6970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00437bdc",
      "DATA",
      [
        "storage",
        "00be69c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437bc4.md#insn-00437bd4)
- 新版 `00437bd4`（命令位置の公開資料なし）

~~~diff
- 00437bd4 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00437bd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437bd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437bd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00437bd4 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00437bd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00437bd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00437bd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437bd4 bytes 08c12591
+ 00437bd4 bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad09ab3db1e8e662bc6b95459835d0b7"></a>

### [`00437bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437bf4.md) → [`00437bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437bf4.md) FUN_00437bf4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00438418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438418.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00438418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438418.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00437c18",
      "incomplete_value": false,
      "site": "00437c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437c18",
      "incomplete_value": false,
      "site": "00437c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "00437c18",
      "DATA",
      [
        "storage",
        "00be6970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00437c18",
      "DATA",
      [
        "storage",
        "00be69c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437bf4.md#insn-00437c14)
- 新版 `00437c14`（命令位置の公開資料なし）

~~~diff
- 00437c14 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00437c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00437c14 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00437c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00437c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00437c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437c14 bytes 08c12591
+ 00437c14 bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e35c0588fa31713eb2b8cd5b6c3151e5"></a>

### [`00437c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437c48.md) → [`00437c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437c48.md) FUN_00437c48

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00438418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438418.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00438418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438418.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00437c54",
      "incomplete_value": false,
      "site": "00437c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437c54",
      "incomplete_value": false,
      "site": "00437c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:970:8"
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
      "00437c54",
      "DATA",
      [
        "storage",
        "00be6970",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00437c54",
      "DATA",
      [
        "storage",
        "00be69c0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437c48.md#insn-00437c50)
- 新版 `00437c50`（命令位置の公開資料なし）

~~~diff
- 00437c50 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00437c50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00437c50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00437c50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00437c50 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00437c50 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00437c50 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00437c50 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00437c50 bytes 29c12591
+ 00437c50 bytes 29012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d45cce55a65a3f45917f97056c0abe9d"></a>

### [`00437c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437c94.md) → [`00437c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/00437c94.md) FUN_00437c94

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042d878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042d878.md) [`0042fd7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042f/0042fd7c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`004389d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/004389d4.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042d878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042d878.md) [`0042fd7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042f/0042fd7c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`004389d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/004389d4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00437f7c",
      "incomplete_value": false,
      "site": "00437f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00437f7c",
      "incomplete_value": false,
      "site": "00437f7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00438074",
      "incomplete_value": false,
      "site": "00438088",
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
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438074",
      "incomplete_value": false,
      "site": "00438088",
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
            "const:b98:8"
          ]
        ]
      ]
    },
    "ordinal": 31,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00438204",
      "incomplete_value": false,
      "site": "00438208",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438204",
      "incomplete_value": false,
      "site": "00438208",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "ordinal": 47,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00437e14",
      "READ",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00437f7c",
      "DATA",
      [
        "storage",
        "00be69e0",
        null,
        "undefined *"
      ]
    ],
    [
      "00438074",
      "PARAM",
      [
        "storage",
        "00c24b98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00437e14",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "00437f7c",
      "DATA",
      [
        "storage",
        "00be6a30",
        null,
        "undefined *"
      ]
    ],
    [
      "00438074",
      "PARAM",
      [
        "storage",
        "00c24bd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00437e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437c94.md#insn-00437e10) · [`00437f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437c94.md#insn-00437f74) · [`00437f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/00437c94.md#insn-00437f78)
- 新版 `00437e10`（命令位置の公開資料なし） · `00437f74`（命令位置の公開資料なし）

~~~diff
- 00437e10 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00437e10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00437e10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00437e10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00437e10 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 00437e10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00437e10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00437e10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00437e10 bytes 08812e91
+ 00437e10 bytes 08812f91
- 00437f74 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 00437f74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00437f74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00437f74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00437f74 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 00437f74 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00437f74 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00437f74 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00437f74 bytes 29812791
+ 00437f74 bytes 29c12891
- 00437f78 ["COPY", "register:40b0:8", ["register:4000:8"]]
- 00437f78 bytes f60300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c3113c901bf00d93b72062f505d442b"></a>

### [`00438788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438788.md) → [`00438788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438788.md) FUN_00438788

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004387a0",
      "incomplete_value": false,
      "site": "004387ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004387a0",
      "incomplete_value": false,
      "site": "004387ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "004387ac",
      "DATA",
      [
        "storage",
        "00be69e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004387ac",
      "DATA",
      [
        "storage",
        "00be6a30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004387a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438788.md#insn-004387a0)
- 新版 `004387a0`（命令位置の公開資料なし）

~~~diff
- 004387a0 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 004387a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004387a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004387a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004387a0 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 004387a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004387a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004387a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004387a0 bytes 08812791
+ 004387a0 bytes 08c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b85e20700030b13d7c49b7d99da7a84"></a>

### [`00438874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438874.md) → [`00438874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438874.md) FUN_00438874

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.55% / 新版 96.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043888c",
      "incomplete_value": false,
      "site": "00438898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043888c",
      "incomplete_value": false,
      "site": "00438898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "00438898",
      "DATA",
      [
        "storage",
        "00be69e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00438898",
      "DATA",
      [
        "storage",
        "00be6a30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043888c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438874.md#insn-0043888c)
- 新版 `0043888c`（命令位置の公開資料なし）

~~~diff
- 0043888c ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 0043888c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043888c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043888c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043888c ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 0043888c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043888c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043888c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043888c bytes 08812791
+ 0043888c bytes 08c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50fddc04222a96260d18885aa592b4f8"></a>

### [`0043895c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/0043895c.md) → [`0043895c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/0043895c.md) FUN_0043895c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00438c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00438c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

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
      "definition_site": "00438980",
      "incomplete_value": false,
      "site": "00438980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438980",
      "incomplete_value": false,
      "site": "00438980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "00438980",
      "DATA",
      [
        "storage",
        "00be69e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00438980",
      "DATA",
      [
        "storage",
        "00be6a30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043897c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/0043895c.md#insn-0043897c)
- 新版 `0043897c`（命令位置の公開資料なし）

~~~diff
- 0043897c ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 0043897c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043897c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043897c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043897c ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 0043897c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043897c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043897c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043897c bytes 08812791
+ 0043897c bytes 08c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f3d02965db74b0a5e1d7c8b5d6c2c33"></a>

### [`004389b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/004389b0.md) → [`004389b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/004389b0.md) FUN_004389b0

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00438c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438c24.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00438c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438c24.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "004389bc",
      "incomplete_value": false,
      "site": "004389bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004389bc",
      "incomplete_value": false,
      "site": "004389bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:9e0:8"
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
      "004389bc",
      "DATA",
      [
        "storage",
        "00be69e0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004389bc",
      "DATA",
      [
        "storage",
        "00be6a30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004389b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/004389b0.md#insn-004389b8)
- 新版 `004389b8`（命令位置の公開資料なし）

~~~diff
- 004389b8 ["COPY", "tmp:0:8", ["const:9e0:8"]]
- 004389b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004389b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004389b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004389b8 ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 004389b8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004389b8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004389b8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004389b8 bytes 29812791
+ 004389b8 bytes 29c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-312b760e2daf7dc192a632f0073e10e0"></a>

### [`004389fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/004389fc.md) → [`004389fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/004389fc.md) FUN_004389fc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042dad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042d/0042dad8.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0073a038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073a/0073a038.md) [`0073eb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073eb44.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042dad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042d/0042dad8.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0073a038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073a/0073a038.md) [`0073eb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073eb44.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.12% / 新版 96.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00438b64",
      "incomplete_value": false,
      "site": "00438b68",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438b64",
      "incomplete_value": false,
      "site": "00438b68",
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
            "const:ba0:8"
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
      "definition_site": "00438b74",
      "incomplete_value": false,
      "site": "00438b78",
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
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438b74",
      "incomplete_value": false,
      "site": "00438b78",
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
            "const:ba0:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00438a44",
      "READ",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00438b64",
      "PARAM",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "00438b74",
      "PARAM",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00438a44",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "00438b64",
      "PARAM",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "00438b74",
      "PARAM",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/004389fc.md#insn-00438a40) · [`00438b64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/004389fc.md#insn-00438b64) · [`00438b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/004389fc.md#insn-00438b74)
- 新版 `00438a40`（命令位置の公開資料なし） · `00438b64`（命令位置の公開資料なし） · `00438b74`（命令位置の公開資料なし）

~~~diff
- 00438a40 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00438a40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00438a40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00438a40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00438a40 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 00438a40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00438a40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00438a40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00438a40 bytes 08812e91
+ 00438a40 bytes 08812f91
- 00438b64 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00438b64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00438b64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00438b64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00438b64 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 00438b64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00438b64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00438b64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00438b64 bytes 00802e91
+ 00438b64 bytes 00802f91
- 00438b74 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 00438b74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00438b74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00438b74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00438b74 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 00438b74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00438b74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00438b74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00438b74 bytes 00802e91
+ 00438b74 bytes 00802f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-813c4edd6ee9671cf496b31498d2b1c7"></a>

### [`00438eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438eb4.md) → [`00438eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438eb4.md) FUN_00438eb4

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
      "definition_site": "00438eb8",
      "incomplete_value": false,
      "site": "00438ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438eb8",
      "incomplete_value": false,
      "site": "00438ebc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "00438ebc",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00438ebc",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438eb4.md#insn-00438eb8)
- 新版 `00438eb8`（命令位置の公開資料なし）

~~~diff
- 00438eb8 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 00438eb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00438eb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00438eb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00438eb8 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 00438eb8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00438eb8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00438eb8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00438eb8 bytes 08012a91
+ 00438eb8 bytes 08412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4810f1482dfd208fc3a4edebb069d4e1"></a>

### [`00438ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438ec4.md) → [`00438ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438ec4.md) FUN_00438ec4

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
      "definition_site": "00438ed4",
      "incomplete_value": false,
      "site": "00438edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438ed4",
      "incomplete_value": false,
      "site": "00438edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "00438edc",
      "DATA",
      [
        "storage",
        "00be6a80",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00438edc",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438ec4.md#insn-00438ed4)
- 新版 `00438ed4`（命令位置の公開資料なし）

~~~diff
- 00438ed4 ["COPY", "tmp:0:8", ["const:a80:8"]]
- 00438ed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00438ed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00438ed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00438ed4 ["COPY", "tmp:0:8", ["const:ad0:8"]]
+ 00438ed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00438ed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00438ed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00438ed4 bytes 08012a91
+ 00438ed4 bytes 08412b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98362036204d668c3dadd23ab1c371c1"></a>

### [`00438f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438f04.md) → [`00438f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f04.md) FUN_00438f04

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00438f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438f54.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00438f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f54.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00438f14",
      "incomplete_value": false,
      "site": "00438f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438f14",
      "incomplete_value": false,
      "site": "00438f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "00438f18",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00438f18",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438f14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438f04.md#insn-00438f14)
- 新版 `00438f14`（命令位置の公開資料なし）

~~~diff
- 00438f14 ["COPY", "tmp:0:8", ["const:ad0:8"]]
- 00438f14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00438f14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00438f14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00438f14 ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 00438f14 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00438f14 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00438f14 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00438f14 bytes 29412b91
+ 00438f14 bytes 29812c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3427c7e725877a8485cde0729ae7cff5"></a>

### [`00438f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438f20.md) → [`00438f20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f20.md) FUN_00438f20

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 5件 [`00572b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00572/00572e44.md) [`0073cdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073c/0073cdfc.md) [`0076e98c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0076e/0076e98c.md) [`00ad021c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad0/00ad021c.md) · 呼出先 2件 [`00438f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438f54.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 5件 [`00572b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572b04.md) [`00572e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00572/00572e44.md) [`0073cdfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073c/0073cdfc.md) [`0076e98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0076e/0076e98c.md) [`00ad0260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad0/00ad0260.md) · 呼出先 2件 [`00438f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438f54.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

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
      "definition_site": "00438f3c",
      "incomplete_value": false,
      "site": "00438f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438f3c",
      "incomplete_value": false,
      "site": "00438f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ad0:8"
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
      "00438f3c",
      "DATA",
      [
        "storage",
        "00be6ad0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00438f3c",
      "DATA",
      [
        "storage",
        "00be6b20",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438f20.md#insn-00438f34)
- 新版 `00438f34`（命令位置の公開資料なし）

~~~diff
- 00438f34 ["COPY", "tmp:0:8", ["const:ad0:8"]]
- 00438f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00438f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00438f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00438f34 ["COPY", "tmp:0:8", ["const:b20:8"]]
+ 00438f34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00438f34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00438f34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00438f34 bytes 08412b91
+ 00438f34 bytes 08812c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2c08ce121d15a567150fd31e4cfd69c"></a>

### [`00438fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438fbc.md) → [`00438fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00438/00438fbc.md) FUN_00438fbc

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
      "definition_site": "00438fc8",
      "incomplete_value": false,
      "site": "00438fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00438fc8",
      "incomplete_value": false,
      "site": "00438fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b30:8"
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
      "00438fd4",
      "DATA",
      [
        "storage",
        "00be6b30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00438fd4",
      "DATA",
      [
        "storage",
        "00be6b80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00438fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00438/00438fbc.md#insn-00438fc8)
- 新版 `00438fc8`（命令位置の公開資料なし）

~~~diff
- 00438fc8 ["COPY", "tmp:0:8", ["const:b30:8"]]
- 00438fc8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00438fc8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00438fc8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00438fc8 ["COPY", "tmp:0:8", ["const:b80:8"]]
+ 00438fc8 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00438fc8 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00438fc8 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00438fc8 bytes 4ac12c91
+ 00438fc8 bytes 4a012e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01f02d225bb9f51e9f318a6fad01a6fd"></a>

### [`00439000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439000.md) → [`00439000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439000.md) FUN_00439000

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
      "definition_site": "00439018",
      "incomplete_value": false,
      "site": "00439024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439018",
      "incomplete_value": false,
      "site": "00439024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b30:8"
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
      "00439024",
      "DATA",
      [
        "storage",
        "00be6b30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439024",
      "DATA",
      [
        "storage",
        "00be6b80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439000.md#insn-00439018)
- 新版 `00439018`（命令位置の公開資料なし）

~~~diff
- 00439018 ["COPY", "tmp:0:8", ["const:b30:8"]]
- 00439018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00439018 ["COPY", "tmp:0:8", ["const:b80:8"]]
+ 00439018 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00439018 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00439018 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439018 bytes 08c12c91
+ 00439018 bytes 08012e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7204f6fce02d31c6e105ef516a6020a"></a>

### [`0043905c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/0043905c.md) → [`0043905c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/0043905c.md) FUN_0043905c

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
      "definition_site": "00439088",
      "incomplete_value": false,
      "site": "00439088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439088",
      "incomplete_value": false,
      "site": "00439088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b30:8"
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
      "00439088",
      "DATA",
      [
        "storage",
        "00be6b30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439088",
      "DATA",
      [
        "storage",
        "00be6b80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/0043905c.md#insn-00439080)
- 新版 `00439080`（命令位置の公開資料なし）

~~~diff
- 00439080 ["COPY", "tmp:0:8", ["const:b30:8"]]
- 00439080 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439080 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439080 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00439080 ["COPY", "tmp:0:8", ["const:b80:8"]]
+ 00439080 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00439080 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00439080 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439080 bytes 08c12c91
+ 00439080 bytes 08012e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05ffa93937147747f61d1efafd618a4d"></a>

### [`004390e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/004390e4.md) → [`004390e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004390e4.md) FUN_004390e4

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
      "definition_site": "00439100",
      "incomplete_value": false,
      "site": "00439100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439100",
      "incomplete_value": false,
      "site": "00439100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:b30:8"
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
      "00439100",
      "DATA",
      [
        "storage",
        "00be6b30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439100",
      "DATA",
      [
        "storage",
        "00be6b80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004390fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/004390e4.md#insn-004390fc)
- 新版 `004390fc`（命令位置の公開資料なし）

~~~diff
- 004390fc ["COPY", "tmp:0:8", ["const:b30:8"]]
- 004390fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004390fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004390fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004390fc ["COPY", "tmp:0:8", ["const:b80:8"]]
+ 004390fc ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004390fc ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004390fc ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004390fc bytes 29c12c91
+ 004390fc bytes 29012e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee49455bb1a1c80a879626d2e492505d"></a>

### [`004391e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/004391e0.md) → [`004391e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004391e0.md) FUN_004391e0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "00439228",
      "incomplete_value": true,
      "site": "00439228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00439228",
      "incomplete_value": true,
      "site": "00439228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004393ac",
      "incomplete_value": true,
      "site": "004393c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:63e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004393ac",
      "incomplete_value": true,
      "site": "004393c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6cb:8"
              ]
            ]
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
      "00439204",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "004393ac",
      "READ",
      [
        "storage",
        "002926cb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00439204",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "004393ac",
      "READ",
      [
        "storage",
        "0029263e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004391fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/004391e0.md#insn-004391fc) · [`004393a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/004391e0.md#insn-004393a4)
- 新版 `004391fc`（命令位置の公開資料なし） · `004393a4`（命令位置の公開資料なし）

~~~diff
- 004391fc ["COPY", "tmp:0:8", ["const:5da:8"]]
- 004391fc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004391fc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004391fc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004391fc ["COPY", "tmp:0:8", ["const:674:8"]]
+ 004391fc ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004391fc ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004391fc ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004391fc bytes 4a691791
+ 004391fc bytes 4ad11991
- 004393a4 ["COPY", "tmp:0:8", ["const:6cb:8"]]
- 004393a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 004393a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 004393a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 004393a4 ["COPY", "tmp:0:8", ["const:63e:8"]]
+ 004393a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 004393a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 004393a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 004393a4 bytes 292d1b91
+ 004393a4 bytes 29f91891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf84c64e4ecac8548a7717b6d408847f"></a>

### [`0043980c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/0043980c.md) → [`0043980c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/0043980c.md) FUN_0043980c

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
      "definition_site": "00439818",
      "incomplete_value": false,
      "site": "00439824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439818",
      "incomplete_value": false,
      "site": "00439824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "00439824",
      "DATA",
      [
        "storage",
        "00be6bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439824",
      "DATA",
      [
        "storage",
        "00be6c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/0043980c.md#insn-00439818)
- 新版 `00439818`（命令位置の公開資料なし）

~~~diff
- 00439818 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00439818 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00439818 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00439818 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00439818 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 00439818 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00439818 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00439818 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00439818 bytes 4a012f91
+ 00439818 bytes 4a413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5809baf0617a3b85a277cfd0707240e0"></a>

### [`00439850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439850.md) → [`00439850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439850.md) FUN_00439850

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
      "definition_site": "00439868",
      "incomplete_value": false,
      "site": "00439874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439868",
      "incomplete_value": false,
      "site": "00439874",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "00439874",
      "DATA",
      [
        "storage",
        "00be6bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439874",
      "DATA",
      [
        "storage",
        "00be6c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439850.md#insn-00439868)
- 新版 `00439868`（命令位置の公開資料なし）

~~~diff
- 00439868 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 00439868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00439868 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 00439868 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00439868 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00439868 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439868 bytes 08012f91
+ 00439868 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f86d0706dddfa25ba4447df598a5642c"></a>

### [`004398ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/004398ac.md) → [`004398ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/004398ac.md) FUN_004398ac

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
      "definition_site": "004398d8",
      "incomplete_value": false,
      "site": "004398d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004398d8",
      "incomplete_value": false,
      "site": "004398d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "004398d8",
      "DATA",
      [
        "storage",
        "00be6bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "004398d8",
      "DATA",
      [
        "storage",
        "00be6c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004398d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/004398ac.md#insn-004398d0)
- 新版 `004398d0`（命令位置の公開資料なし）

~~~diff
- 004398d0 ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 004398d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 004398d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 004398d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 004398d0 ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 004398d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 004398d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 004398d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 004398d0 bytes 08012f91
+ 004398d0 bytes 08413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d18913a9d709e4db17b4cb4275971483"></a>

### [`00439934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439934.md) → [`00439934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439934.md) FUN_00439934

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
      "definition_site": "00439950",
      "incomplete_value": false,
      "site": "00439950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439950",
      "incomplete_value": false,
      "site": "00439950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "00439950",
      "DATA",
      [
        "storage",
        "00be6bc0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439950",
      "DATA",
      [
        "storage",
        "00be6c10",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043994c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439934.md#insn-0043994c)
- 新版 `0043994c`（命令位置の公開資料なし）

~~~diff
- 0043994c ["COPY", "tmp:0:8", ["const:bc0:8"]]
- 0043994c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043994c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043994c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043994c ["COPY", "tmp:0:8", ["const:c10:8"]]
+ 0043994c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043994c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043994c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043994c bytes 29012f91
+ 0043994c bytes 29413091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01d725394ef006f706979c1b8ce51fce"></a>

### [`00439eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439eb4.md) → [`00439eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439eb4.md) FUN_00439eb4

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00439bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439bc0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`00439bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439bc0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "00439ec0",
      "incomplete_value": false,
      "site": "00439ec4",
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
      "definition_site": "00439ec0",
      "incomplete_value": false,
      "site": "00439ec4",
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
      "00439ec0",
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
      "00439ec0",
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

- 旧版 [`00439ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439eb4.md#insn-00439ec0)
- 新版 `00439ec0`（命令位置の公開資料なし）

~~~diff
- 00439ec0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 00439ec0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00439ec0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00439ec0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00439ec0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 00439ec0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00439ec0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00439ec0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00439ec0 bytes 000c0c91
+ 00439ec0 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb5701e78760d34bf56569799de5ae9a"></a>

### [`00439ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439ec8.md) → [`00439ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439ec8.md) FUN_00439ec8

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
      "definition_site": "00439ed4",
      "incomplete_value": false,
      "site": "00439ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439ed4",
      "incomplete_value": false,
      "site": "00439ee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "00439ee0",
      "DATA",
      [
        "storage",
        "00be6c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439ee0",
      "DATA",
      [
        "storage",
        "00be6ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439ec8.md#insn-00439ed4)
- 新版 `00439ed4`（命令位置の公開資料なし）

~~~diff
- 00439ed4 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 00439ed4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00439ed4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00439ed4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00439ed4 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 00439ed4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00439ed4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00439ed4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00439ed4 bytes 4a413191
+ 00439ed4 bytes 4a813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e17ecf62fb3ecaf1412183d69c1fed0"></a>

### [`00439f0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439f0c.md) → [`00439f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439f0c.md) FUN_00439f0c

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
      "definition_site": "00439f24",
      "incomplete_value": false,
      "site": "00439f30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439f24",
      "incomplete_value": false,
      "site": "00439f30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "00439f30",
      "DATA",
      [
        "storage",
        "00be6c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439f30",
      "DATA",
      [
        "storage",
        "00be6ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439f0c.md#insn-00439f24)
- 新版 `00439f24`（命令位置の公開資料なし）

~~~diff
- 00439f24 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 00439f24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439f24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439f24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00439f24 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 00439f24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00439f24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00439f24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439f24 bytes 08413191
+ 00439f24 bytes 08813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a8d1001bcd13ade4d90ae0791717b16"></a>

### [`00439f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439f68.md) → [`00439f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439f68.md) FUN_00439f68

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
      "definition_site": "00439f94",
      "incomplete_value": false,
      "site": "00439f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00439f94",
      "incomplete_value": false,
      "site": "00439f94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:c50:8"
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
      "00439f94",
      "DATA",
      [
        "storage",
        "00be6c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00439f94",
      "DATA",
      [
        "storage",
        "00be6ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00439f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439f68.md#insn-00439f8c)
- 新版 `00439f8c`（命令位置の公開資料なし）

~~~diff
- 00439f8c ["COPY", "tmp:0:8", ["const:c50:8"]]
- 00439f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00439f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00439f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00439f8c ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 00439f8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00439f8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00439f8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00439f8c bytes 08413191
+ 00439f8c bytes 08813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8903c3b035b3608e48057d3e22940b7f"></a>

### [`00439ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439ff0.md) → [`00439ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00439/00439ff0.md) FUN_00439ff0

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
      "definition_site": "0043a00c",
      "incomplete_value": false,
      "site": "0043a00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a00c",
      "incomplete_value": false,
      "site": "0043a00c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "0043a00c",
      "DATA",
      [
        "storage",
        "00be6c50",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043a00c",
      "DATA",
      [
        "storage",
        "00be6ca0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00439/00439ff0.md#insn-0043a008)
- 新版 `0043a008`（命令位置の公開資料なし）

~~~diff
- 0043a008 ["COPY", "tmp:0:8", ["const:c50:8"]]
- 0043a008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043a008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043a008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043a008 ["COPY", "tmp:0:8", ["const:ca0:8"]]
+ 0043a008 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043a008 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043a008 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043a008 bytes 29413191
+ 0043a008 bytes 29813291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bcd4afb12cb72ec7011b6e03ddcc047"></a>

### [`0043a0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a0ec.md) → [`0043a0ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a0ec.md) FUN_0043a0ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 92.68% / 新版 92.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 2件, `store_destination` 6件, `store_value` 2件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043a140",
      "incomplete_value": true,
      "site": "0043a140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0043a140",
      "incomplete_value": true,
      "site": "0043a140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043a270",
      "incomplete_value": true,
      "site": "0043a284",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:63e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a270",
      "incomplete_value": true,
      "site": "0043a284",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:6cb:8"
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
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043a444",
      "incomplete_value": false,
      "site": "0043a444",
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
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a444",
      "incomplete_value": false,
      "site": "0043a444",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "ordinal": 27,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043a10c",
      "PARAM",
      [
        "storage",
        "00c24be0",
        null,
        null
      ]
    ],
    [
      "0043a12c",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0043a270",
      "READ",
      [
        "storage",
        "002926cb",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043a10c",
      "PARAM",
      [
        "storage",
        "00c24c20",
        null,
        null
      ]
    ],
    [
      "0043a12c",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "0043a270",
      "READ",
      [
        "storage",
        "0029263e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a0ec.md#insn-0043a444) · [`0043a63c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a0ec.md#insn-0043a63c) · [`0043a640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a0ec.md#insn-0043a640)
- 新版 `0043a444`（命令位置の公開資料なし） · `0043a63c`（命令位置の公開資料なし） · `0043a640`（命令位置の公開資料なし）

~~~diff
- 0043a444 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
- 0043a444 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 0043a444 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c58:8"]]
+ 0043a444 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 0043a444 bytes 140d06f9
+ 0043a444 bytes 142d06f9
- 0043a63c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
- 0043a63c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0043a63c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c58:8"]]
+ 0043a63c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0043a63c bytes 130d06f9
+ 0043a63c bytes 132d06f9
- 0043a640 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0043a640 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0043a640 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:c30:8"]]
- 0043a640 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0043a640 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0043a640 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0043a640 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:c70:8"]]
+ 0043a640 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0043a640 bytes 3fc13039
+ 0043a640 bytes 3fc13139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdef9efe1603b91aeb90afa2cba2b2f3"></a>

### [`0043a8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a8b8.md) → [`0043a8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a8b8.md) FUN_0043a8b8

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
      "definition_site": "0043a8c4",
      "incomplete_value": false,
      "site": "0043a8d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a8c4",
      "incomplete_value": false,
      "site": "0043a8d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "0043a8d0",
      "DATA",
      [
        "storage",
        "00be6cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043a8d0",
      "DATA",
      [
        "storage",
        "00be6d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a8b8.md#insn-0043a8c4)
- 新版 `0043a8c4`（命令位置の公開資料なし）

~~~diff
- 0043a8c4 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0043a8c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043a8c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043a8c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043a8c4 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 0043a8c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043a8c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043a8c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043a8c4 bytes 4a413391
+ 0043a8c4 bytes 4a813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c3be61a38ce8c357f115413e5a3e674"></a>

### [`0043a8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a8fc.md) → [`0043a8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a8fc.md) FUN_0043a8fc

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
      "definition_site": "0043a914",
      "incomplete_value": false,
      "site": "0043a920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a914",
      "incomplete_value": false,
      "site": "0043a920",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "0043a920",
      "DATA",
      [
        "storage",
        "00be6cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043a920",
      "DATA",
      [
        "storage",
        "00be6d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a8fc.md#insn-0043a914)
- 新版 `0043a914`（命令位置の公開資料なし）

~~~diff
- 0043a914 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0043a914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043a914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043a914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043a914 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 0043a914 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043a914 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043a914 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043a914 bytes 08413391
+ 0043a914 bytes 08813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2ee05ac77260c881e92737ce7bd5bd1"></a>

### [`0043a958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a958.md) → [`0043a958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a958.md) FUN_0043a958

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
      "definition_site": "0043a984",
      "incomplete_value": false,
      "site": "0043a984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a984",
      "incomplete_value": false,
      "site": "0043a984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "0043a984",
      "DATA",
      [
        "storage",
        "00be6cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043a984",
      "DATA",
      [
        "storage",
        "00be6d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a958.md#insn-0043a97c)
- 新版 `0043a97c`（命令位置の公開資料なし）

~~~diff
- 0043a97c ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0043a97c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043a97c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043a97c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043a97c ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 0043a97c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043a97c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043a97c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043a97c bytes 08413391
+ 0043a97c bytes 08813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f07c9c5145ec4754bcbe7e6d749b7a5"></a>

### [`0043a9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a9e0.md) → [`0043a9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043a9e0.md) FUN_0043a9e0

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
      "definition_site": "0043a9fc",
      "incomplete_value": false,
      "site": "0043a9fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043a9fc",
      "incomplete_value": false,
      "site": "0043a9fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
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
      "0043a9fc",
      "DATA",
      [
        "storage",
        "00be6cd0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043a9fc",
      "DATA",
      [
        "storage",
        "00be6d20",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043a9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043a9e0.md#insn-0043a9f8)
- 新版 `0043a9f8`（命令位置の公開資料なし）

~~~diff
- 0043a9f8 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 0043a9f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043a9f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043a9f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043a9f8 ["COPY", "tmp:0:8", ["const:d20:8"]]
+ 0043a9f8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043a9f8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043a9f8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043a9f8 bytes 29413391
+ 0043a9f8 bytes 29813491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f54c3f404db379c6c9f958672840b75"></a>

### [`0043aadc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043aadc.md) → [`0043aadc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043aadc.md) FUN_0043aadc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`009bd60c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/009bd/009bd60c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`009bd618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/009bd/009bd618.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.10% / 新版 93.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043abf0",
      "incomplete_value": false,
      "site": "0043abf0",
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
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043abf0",
      "incomplete_value": false,
      "site": "0043abf0",
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
            "const:c18:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043abf4",
      "incomplete_value": false,
      "site": "0043abf4",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043abf4",
      "incomplete_value": false,
      "site": "0043abf4",
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
            "const:c30:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0043ab38",
      "incomplete_value": true,
      "site": "0043ab38",
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
      "definition_site": "0043ab38",
      "incomplete_value": true,
      "site": "0043ab38",
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
      "0043ab30",
      "READ",
      [
        "storage",
        "00c24c10",
        null,
        "undefined8"
      ]
    ],
    [
      "0043ab30",
      "READ",
      [
        "storage",
        "00c24c18",
        null,
        "undefined8"
      ]
    ],
    [
      "0043ab9c",
      "READ",
      [
        "storage",
        "00c24c10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043ab30",
      "READ",
      [
        "storage",
        "00c24c50",
        null,
        "undefined8"
      ]
    ],
    [
      "0043ab30",
      "READ",
      [
        "storage",
        "00c24c58",
        null,
        "undefined8"
      ]
    ],
    [
      "0043ab9c",
      "READ",
      [
        "storage",
        "00c24c50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043abf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043aadc.md#insn-0043abf0) · [`0043abf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043aadc.md#insn-0043abf4) · [`0043ab2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043aadc.md#insn-0043ab2c)
- 新版 `0043abf0`（命令位置の公開資料なし） · `0043abf4`（命令位置の公開資料なし） · `0043ab2c`（命令位置の公開資料なし）

~~~diff
- 0043abf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c18:8"]]
- 0043abf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0043abf0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c58:8"]]
+ 0043abf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0043abf0 bytes 130d06f9
+ 0043abf0 bytes 132d06f9
- 0043abf4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0043abf4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0043abf4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:c30:8"]]
- 0043abf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0043abf4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0043abf4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0043abf4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:c70:8"]]
+ 0043abf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0043abf4 bytes 3fc13039
+ 0043abf4 bytes 3fc13139
- 0043ab2c ["COPY", "tmp:0:8", ["const:c10:8"]]
- 0043ab2c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 0043ab2c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 0043ab2c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 0043ab2c ["COPY", "tmp:0:8", ["const:c50:8"]]
+ 0043ab2c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 0043ab2c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 0043ab2c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 0043ab2c bytes d6423091
+ 0043ab2c bytes d6423191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53f8d8466664ca5aafd3f0becb3c3189"></a>

### [`0043af94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043af94.md) → [`0043af94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043af94.md) FUN_0043af94

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0043aca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043aca0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 1件 [`0043aca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043aca0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0043afa0",
      "incomplete_value": false,
      "site": "0043afa4",
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
      "definition_site": "0043afa0",
      "incomplete_value": false,
      "site": "0043afa4",
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
      "0043afa0",
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
      "0043afa0",
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

- 旧版 [`0043afa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043af94.md#insn-0043afa0)
- 新版 `0043afa0`（命令位置の公開資料なし）

~~~diff
- 0043afa0 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0043afa0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0043afa0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0043afa0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0043afa0 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0043afa0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0043afa0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0043afa0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0043afa0 bytes 000c0c91
+ 0043afa0 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8bebb69e50e5f43a3f9999e5718659d1"></a>

### [`0043afac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043afac.md) → [`0043afac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043afac.md) FUN_0043afac

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
      "definition_site": "0043afd0",
      "incomplete_value": false,
      "site": "0043afd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043afd0",
      "incomplete_value": false,
      "site": "0043afd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:d60:8"
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
      "0043afd0",
      "DATA",
      [
        "storage",
        "00be6d60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043afd0",
      "DATA",
      [
        "storage",
        "00be6db0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043afcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043afac.md#insn-0043afcc)
- 新版 `0043afcc`（命令位置の公開資料なし）

~~~diff
- 0043afcc ["COPY", "tmp:0:8", ["const:d60:8"]]
- 0043afcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043afcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043afcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043afcc ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0043afcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043afcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043afcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043afcc bytes 08813591
+ 0043afcc bytes 08c13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-beb360024a8055c805eeb32edc35d848"></a>

### [`0043afe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043afe0.md) → [`0043afe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043afe0.md) FUN_0043afe0

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
      "definition_site": "0043afec",
      "incomplete_value": false,
      "site": "0043afec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:db0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043afec",
      "incomplete_value": false,
      "site": "0043afec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:d60:8"
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
      "0043afec",
      "DATA",
      [
        "storage",
        "00be6d60",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043afec",
      "DATA",
      [
        "storage",
        "00be6db0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043afe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043afe0.md#insn-0043afe8)
- 新版 `0043afe8`（命令位置の公開資料なし）

~~~diff
- 0043afe8 ["COPY", "tmp:0:8", ["const:d60:8"]]
- 0043afe8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043afe8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043afe8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043afe8 ["COPY", "tmp:0:8", ["const:db0:8"]]
+ 0043afe8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043afe8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043afe8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043afe8 bytes 29813591
+ 0043afe8 bytes 29c13691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2e8c21fcec5675fce4d3ddc662884006"></a>

### [`0043affc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043affc.md) → [`0043affc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043a/0043affc.md) FUN_0043affc

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb240.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb290.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.91% / 新版 93.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 1件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043b050",
      "incomplete_value": true,
      "site": "0043b050",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0043b050",
      "incomplete_value": true,
      "site": "0043b050",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b3dc",
      "incomplete_value": false,
      "site": "0043b3dc",
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
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b3dc",
      "incomplete_value": false,
      "site": "0043b3dc",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b3e0",
      "incomplete_value": false,
      "site": "0043b3e0",
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
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b3e0",
      "incomplete_value": false,
      "site": "0043b3e0",
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
            "const:c88:8"
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
      "0043b01c",
      "PARAM",
      [
        "storage",
        "00c24c34",
        null,
        null
      ]
    ],
    [
      "0043b03c",
      "READ",
      [
        "storage",
        "002a65da",
        null,
        "string"
      ]
    ],
    [
      "0043b164",
      "READ",
      [
        "storage",
        "00c24c68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043b01c",
      "PARAM",
      [
        "storage",
        "00c24c74",
        null,
        null
      ]
    ],
    [
      "0043b03c",
      "READ",
      [
        "storage",
        "002a6674",
        null,
        "string"
      ]
    ],
    [
      "0043b164",
      "READ",
      [
        "storage",
        "00c24ca8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043affc.md#insn-0043b3dc) · [`0043b3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043affc.md#insn-0043b3e0) · [`0043b46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043a/0043affc.md#insn-0043b46c)
- 新版 `0043b3dc`（命令位置の公開資料なし） · `0043b3e0`（命令位置の公開資料なし） · `0043b46c`（命令位置の公開資料なし）

~~~diff
- 0043b3dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c70:8"]]
- 0043b3dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0043b3dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb0:8"]]
+ 0043b3dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0043b3dc bytes 133906f9
+ 0043b3dc bytes 135906f9
- 0043b3e0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0043b3e0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0043b3e0 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:c88:8"]]
- 0043b3e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0043b3e0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0043b3e0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0043b3e0 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:cc8:8"]]
+ 0043b3e0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0043b3e0 bytes 3f213239
+ 0043b3e0 bytes 3f213339
- 0043b46c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c70:8"]]
- 0043b46c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0043b46c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb0:8"]]
+ 0043b46c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0043b46c bytes 133906f9
+ 0043b46c bytes 135906f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b809a00239c8139b77d31fbcc56f5f6b"></a>

### [`0043b598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b598.md) → [`0043b598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b598.md) FUN_0043b598

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
      "definition_site": "0043b5bc",
      "incomplete_value": false,
      "site": "0043b5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b5bc",
      "incomplete_value": false,
      "site": "0043b5bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:de0:8"
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
      "0043b5bc",
      "DATA",
      [
        "storage",
        "00be6de0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043b5bc",
      "DATA",
      [
        "storage",
        "00be6e30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b598.md#insn-0043b5b8)
- 新版 `0043b5b8`（命令位置の公開資料なし）

~~~diff
- 0043b5b8 ["COPY", "tmp:0:8", ["const:de0:8"]]
- 0043b5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043b5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043b5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b5b8 ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 0043b5b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b5b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b5b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043b5b8 bytes 08813791
+ 0043b5b8 bytes 08c13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf0f5e51cbd5d3d8116a61286b1f4d13"></a>

### [`0043b5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b5cc.md) → [`0043b5cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b5cc.md) FUN_0043b5cc

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
      "definition_site": "0043b5d8",
      "incomplete_value": false,
      "site": "0043b5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:e30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b5d8",
      "incomplete_value": false,
      "site": "0043b5d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:de0:8"
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
      "0043b5d8",
      "DATA",
      [
        "storage",
        "00be6de0",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043b5d8",
      "DATA",
      [
        "storage",
        "00be6e30",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b5d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b5cc.md#insn-0043b5d4)
- 新版 `0043b5d4`（命令位置の公開資料なし）

~~~diff
- 0043b5d4 ["COPY", "tmp:0:8", ["const:de0:8"]]
- 0043b5d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043b5d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043b5d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043b5d4 ["COPY", "tmp:0:8", ["const:e30:8"]]
+ 0043b5d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043b5d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043b5d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043b5d4 bytes 29813791
+ 0043b5d4 bytes 29c13891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab4bda8a77a6d0c11fc52f5139cc3cd5"></a>

### [`0043b5e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b5e8.md) → [`0043b5e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b5e8.md) FUN_0043b5e8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0073e6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073e6dc.md) [`0073ed78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0073e/0073ed78.md) [`0081f580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0081f/0081f580.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0073e6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073e6dc.md) [`0073ed78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0073e/0073ed78.md) [`0081f580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0081f/0081f580.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b6f0",
      "incomplete_value": false,
      "site": "0043b6f0",
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
            "const:cb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b6f0",
      "incomplete_value": false,
      "site": "0043b6f0",
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
            "const:c70:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "0043b6f4",
      "incomplete_value": false,
      "site": "0043b6f4",
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
            "const:cc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b6f4",
      "incomplete_value": false,
      "site": "0043b6f4",
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
            "const:c88:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "0043b650",
      "incomplete_value": true,
      "site": "0043b650",
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
      "definition_site": "0043b650",
      "incomplete_value": true,
      "site": "0043b650",
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
      "0043b648",
      "READ",
      [
        "storage",
        "00c24c68",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b648",
      "READ",
      [
        "storage",
        "00c24c70",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b69c",
      "READ",
      [
        "storage",
        "00c24c68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043b648",
      "READ",
      [
        "storage",
        "00c24ca8",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b648",
      "READ",
      [
        "storage",
        "00c24cb0",
        null,
        "undefined8"
      ]
    ],
    [
      "0043b69c",
      "READ",
      [
        "storage",
        "00c24ca8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b5e8.md#insn-0043b6f0) · [`0043b6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b5e8.md#insn-0043b6f4) · [`0043b644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b5e8.md#insn-0043b644)
- 新版 `0043b6f0`（命令位置の公開資料なし） · `0043b6f4`（命令位置の公開資料なし） · `0043b644`（命令位置の公開資料なし）

~~~diff
- 0043b6f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:c70:8"]]
- 0043b6f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 0043b6f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cb0:8"]]
+ 0043b6f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 0043b6f0 bytes 133906f9
+ 0043b6f0 bytes 135906f9
- 0043b6f4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 0043b6f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 0043b6f4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:c88:8"]]
- 0043b6f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 0043b6f4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 0043b6f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 0043b6f4 ["INT_ADD", "tmp:2:8", ["register:4048:8", "const:cc8:8"]]
+ 0043b6f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 0043b6f4 bytes 3f213239
+ 0043b6f4 bytes 3f213339
- 0043b644 ["COPY", "tmp:0:8", ["const:c68:8"]]
- 0043b644 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 0043b644 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 0043b644 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 0043b644 ["COPY", "tmp:0:8", ["const:ca8:8"]]
+ 0043b644 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 0043b644 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 0043b644 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 0043b644 bytes d6a23191
+ 0043b644 bytes d6a23291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ed23eb534da6236c9721e8e3da07910"></a>

### [`0043b790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b790.md) → [`0043b790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b790.md) FUN_0043b790

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0043c490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c490.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`0043bd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bd0c.md) [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`0043c490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c490.md) · 呼出先 6件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`0043bd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bd0c.md) [`00574ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 93.38% / 新版 93.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043b83c",
      "incomplete_value": true,
      "site": "0043b84c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:42b:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b83c",
      "incomplete_value": true,
      "site": "0043b84c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3a0:8"
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
      "definition_site": "0043b9b4",
      "incomplete_value": true,
      "site": "0043b9c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:387:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043b9b4",
      "incomplete_value": true,
      "site": "0043b9c8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:2fc:8"
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
      "definition_site": "0043b9b4",
      "incomplete_value": true,
      "site": "0043b9c8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "0043b9b4",
      "incomplete_value": true,
      "site": "0043b9c8",
      "value": [
        "LOAD",
        "16",
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
      "0043b83c",
      "READ",
      [
        "storage",
        "002a53a0",
        null,
        "string"
      ]
    ],
    [
      "0043b9b4",
      "READ",
      [
        "storage",
        "0029d2fc",
        null,
        "string"
      ]
    ],
    [
      "0043b9b4",
      "READ",
      [
        "storage",
        "0029d30c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043b83c",
      "READ",
      [
        "storage",
        "002a542b",
        null,
        "string"
      ]
    ],
    [
      "0043b9b4",
      "READ",
      [
        "storage",
        "0029d387",
        null,
        "string"
      ]
    ],
    [
      "0043b9b4",
      "READ",
      [
        "storage",
        "0029d397",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043b834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b790.md#insn-0043b834) · [`0043b9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b790.md#insn-0043b9ac) · [`0043b9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b790.md#insn-0043b9b0)
- 新版 `0043b834`（命令位置の公開資料なし） · `0043b9ac`（命令位置の公開資料なし）

~~~diff
- 0043b834 ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 0043b834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043b834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043b834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043b834 ["COPY", "tmp:0:8", ["const:42b:8"]]
+ 0043b834 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043b834 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043b834 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043b834 bytes 29810e91
+ 0043b834 bytes 29ad1091
- 0043b9ac ["COPY", "tmp:0:8", ["const:2fc:8"]]
- 0043b9ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043b9ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043b9ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043b9ac ["COPY", "tmp:0:8", ["const:387:8"]]
+ 0043b9ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b9ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043b9ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043b9ac bytes 08f10b91
+ 0043b9ac bytes 081d0e91
- 0043b9b0 ["COPY", "register:4048:8", ["const:2b1000:8"]]
- 0043b9b0 bytes a9f3ffd0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fecd0473d4ff13dc7c9feeb618f168a"></a>

### [`0043bd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bd0c.md) → [`0043bd0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bd0c.md) FUN_0043bd0c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`0043b790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b790.md) · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00574ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00574/00574ff4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`0043b790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b790.md) · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00574ff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00574/00574ff4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 85.16% / 新版 85.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043bd58",
      "incomplete_value": true,
      "site": "0043bd58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c3f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043bd58",
      "incomplete_value": true,
      "site": "0043bd58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ccc:8"
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
      "definition_site": "0043bd5c",
      "incomplete_value": true,
      "site": "0043bd5c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0043bd5c",
      "incomplete_value": true,
      "site": "0043bd5c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043bdc4",
      "incomplete_value": true,
      "site": "0043bdc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:43d:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043bdc4",
      "incomplete_value": true,
      "site": "0043bdc4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b2:8"
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
      "0043bd48",
      "READ",
      [
        "storage",
        "00298ccc",
        null,
        "string"
      ]
    ],
    [
      "0043bd4c",
      "READ",
      [
        "storage",
        "00298cd2",
        null,
        "string"
      ]
    ],
    [
      "0043bdb0",
      "READ",
      [
        "storage",
        "002a53b2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043bd48",
      "READ",
      [
        "storage",
        "00298c3f",
        null,
        "string"
      ]
    ],
    [
      "0043bd4c",
      "READ",
      [
        "storage",
        "00298c45",
        null,
        "string"
      ]
    ],
    [
      "0043bdb0",
      "READ",
      [
        "storage",
        "002a543d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043bd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bd0c.md#insn-0043bd40) · [`0043bd44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bd0c.md#insn-0043bd44)
- 新版 `0043bd40`（命令位置の公開資料なし） · `0043bd44`（命令位置の公開資料なし）

~~~diff
- 0043bd40 ["COPY", "tmp:0:8", ["const:ccc:8"]]
- 0043bd40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043bd40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043bd40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043bd40 ["COPY", "tmp:0:8", ["const:c3f:8"]]
+ 0043bd40 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043bd40 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043bd40 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043bd40 bytes 29313391
+ 0043bd40 bytes 29fd3091
- 0043bd44 ["COPY", "register:40b0:8", ["register:4000:8"]]
- 0043bd44 bytes f60300aa
+ 0043bd44 ["COPY", "register:40b0:8", ["register:4000:8"]]
+ 0043bd44 bytes f60300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d13db291796c4cb3ee45f33e94440ea"></a>

### [`0043bf44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bf44.md) → [`0043bf44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bf44.md) FUN_0043bf44

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
      "definition_site": "0043bf48",
      "incomplete_value": false,
      "site": "0043bf4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043bf48",
      "incomplete_value": false,
      "site": "0043bf4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "0043bf4c",
      "DATA",
      [
        "storage",
        "00be6e60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0043bf4c",
      "DATA",
      [
        "storage",
        "00be6eb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043bf48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bf44.md#insn-0043bf48)
- 新版 `0043bf48`（命令位置の公開資料なし）

~~~diff
- 0043bf48 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 0043bf48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043bf48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043bf48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043bf48 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 0043bf48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043bf48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043bf48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043bf48 bytes 08813991
+ 0043bf48 bytes 08c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b8f1954575ff22fc7d537b434945eedc"></a>

### [`0043bf54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bf54.md) → [`0043bf54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bf54.md) FUN_0043bf54

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
      "definition_site": "0043bf64",
      "incomplete_value": false,
      "site": "0043bf6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:eb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043bf64",
      "incomplete_value": false,
      "site": "0043bf6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:e60:8"
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
      "0043bf6c",
      "DATA",
      [
        "storage",
        "00be6e60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0043bf6c",
      "DATA",
      [
        "storage",
        "00be6eb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043bf64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bf54.md#insn-0043bf64)
- 新版 `0043bf64`（命令位置の公開資料なし）

~~~diff
- 0043bf64 ["COPY", "tmp:0:8", ["const:e60:8"]]
- 0043bf64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043bf64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043bf64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043bf64 ["COPY", "tmp:0:8", ["const:eb0:8"]]
+ 0043bf64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043bf64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043bf64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043bf64 bytes 08813991
+ 0043bf64 bytes 08c13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6494830ba0bc32bdedd8c7b30b9811b8"></a>

### [`0043bf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bf90.md) → [`0043bf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bf90.md) FUN_0043bf90

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdafc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafc0.md) [`00bdb230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb230.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb010.md) [`00bdb280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb280.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 84.21% / 新版 84.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043bfb4",
      "incomplete_value": true,
      "site": "0043bfb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "0043bfb4",
      "incomplete_value": true,
      "site": "0043bfb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "0043bfa8",
      "READ",
      [
        "storage",
        "00c1ae10",
        null,
        "pointer"
      ]
    ],
    [
      "0043bfb4",
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
      "0043bfa8",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "0043bfb4",
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

- 旧版 [`0043bfa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bf90.md#insn-0043bfa8)
- 新版 `0043bfa8`（命令位置の公開資料なし）

~~~diff
- 0043bfa8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 0043bfa8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043bfa8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
+ 0043bfa8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0043bfa8 bytes 080947f9
+ 0043bfa8 bytes 083147f9
~~~


<a id="compare-7c8d40d7c7608d6a9d655b83b055af81"></a>

### [`0043bfdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bfdc.md) → [`0043bfdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bfdc.md) FUN_0043bfdc

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
      "definition_site": "0043c000",
      "incomplete_value": true,
      "site": "0043c000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "0043c000",
      "incomplete_value": true,
      "site": "0043c000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "0043bff4",
      "READ",
      [
        "storage",
        "00c1ae10",
        null,
        "pointer"
      ]
    ],
    [
      "0043c000",
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
      "0043bff4",
      "READ",
      [
        "storage",
        "00c1ae60",
        null,
        "pointer"
      ]
    ],
    [
      "0043c000",
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

- 旧版 [`0043bff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bfdc.md#insn-0043bff4)
- 新版 `0043bff4`（命令位置の公開資料なし）

~~~diff
- 0043bff4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e10:8"]]
- 0043bff4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043bff4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e60:8"]]
+ 0043bff4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0043bff4 bytes 080947f9
+ 0043bff4 bytes 083147f9
~~~


<a id="compare-266cff6dd90d0b639a1912f16a196370"></a>

### [`0043c03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c03c.md) → [`0043c03c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c03c.md) FUN_0043c03c

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`0043bf84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043bf84.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00437/004377f0.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb450.md)
- 新版 呼出元 1件 [`0043bf84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043bf84.md) · 呼出先 12件 [`004377f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00437/004377f0.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4a0.md)

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
      "definition_site": "0043c0e0",
      "incomplete_value": true,
      "site": "0043c0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "0043c0e0",
      "incomplete_value": true,
      "site": "0043c0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "0043c0bc",
      "incomplete_value": true,
      "site": "0043c0c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0043c0bc",
      "incomplete_value": true,
      "site": "0043c0c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0043c0bc",
      "READ",
      [
        "storage",
        "00c1ae18",
        null,
        "pointer"
      ]
    ],
    [
      "0043c0bc",
      "PARAM",
      [
        "storage",
        "00c12eb8",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0043c0dc",
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
      "0043c0bc",
      "READ",
      [
        "storage",
        "00c1ae68",
        null,
        "pointer"
      ]
    ],
    [
      "0043c0bc",
      "PARAM",
      [
        "storage",
        "00c12f08",
        "_ZTINSt6__ndk112future_errorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "0043c0dc",
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

- 旧版 [`0043c0bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c03c.md#insn-0043c0bc) · [`0043c0dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c03c.md#insn-0043c0dc)
- 新版 `0043c0bc`（命令位置の公開資料なし） · `0043c0dc`（命令位置の公開資料なし）

~~~diff
- 0043c0bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e18:8"]]
- 0043c0bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043c0bc ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e68:8"]]
+ 0043c0bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0043c0bc bytes 210c47f9
+ 0043c0bc bytes 213447f9
- 0043c0dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e20:8"]]
- 0043c0dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043c0dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e70:8"]]
+ 0043c0dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0043c0dc bytes 081147f9
+ 0043c0dc bytes 083947f9
~~~


<a id="compare-62e11710c971b21c232f9ed33eba55ad"></a>

### [`0043c260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c260.md) → [`0043c260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c260.md) FUN_0043c260

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
      "definition_site": "0043c26c",
      "incomplete_value": false,
      "site": "0043c278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c26c",
      "incomplete_value": false,
      "site": "0043c278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "0043c278",
      "DATA",
      [
        "storage",
        "00be6f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c278",
      "DATA",
      [
        "storage",
        "00be6f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c260.md#insn-0043c26c)
- 新版 `0043c26c`（命令位置の公開資料なし）

~~~diff
- 0043c26c ["COPY", "tmp:0:8", ["const:f08:8"]]
- 0043c26c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043c26c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043c26c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043c26c ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 0043c26c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043c26c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043c26c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043c26c bytes 4a213c91
+ 0043c26c bytes 4a613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d9a3ec6da9c49c83063d0c19ecf5dcd"></a>

### [`0043c2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c2a4.md) → [`0043c2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c2a4.md) FUN_0043c2a4

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
      "definition_site": "0043c2bc",
      "incomplete_value": false,
      "site": "0043c2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c2bc",
      "incomplete_value": false,
      "site": "0043c2c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "0043c2c8",
      "DATA",
      [
        "storage",
        "00be6f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c2c8",
      "DATA",
      [
        "storage",
        "00be6f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c2a4.md#insn-0043c2bc)
- 新版 `0043c2bc`（命令位置の公開資料なし）

~~~diff
- 0043c2bc ["COPY", "tmp:0:8", ["const:f08:8"]]
- 0043c2bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c2bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c2bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043c2bc ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 0043c2bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c2bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c2bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c2bc bytes 08213c91
+ 0043c2bc bytes 08613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-993e8a1c8b99199ed943de30c2a43446"></a>

### [`0043c300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c300.md) → [`0043c300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c300.md) FUN_0043c300

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "0043c32c",
      "incomplete_value": false,
      "site": "0043c32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c32c",
      "incomplete_value": false,
      "site": "0043c32c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "0043c32c",
      "DATA",
      [
        "storage",
        "00be6f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c32c",
      "DATA",
      [
        "storage",
        "00be6f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c300.md#insn-0043c324)
- 新版 `0043c324`（命令位置の公開資料なし）

~~~diff
- 0043c324 ["COPY", "tmp:0:8", ["const:f08:8"]]
- 0043c324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043c324 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 0043c324 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c324 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c324 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c324 bytes 08213c91
+ 0043c324 bytes 08613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d6db04878c70714b7d87de3aff66c92"></a>

### [`0043c390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c390.md) → [`0043c390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c390.md) FUN_0043c390

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c3b0",
      "incomplete_value": false,
      "site": "0043c3b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c3b0",
      "incomplete_value": false,
      "site": "0043c3b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f08:8"
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
      "0043c3b0",
      "DATA",
      [
        "storage",
        "00be6f08",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c3b0",
      "DATA",
      [
        "storage",
        "00be6f58",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c390.md#insn-0043c3ac)
- 新版 `0043c3ac`（命令位置の公開資料なし）

~~~diff
- 0043c3ac ["COPY", "tmp:0:8", ["const:f08:8"]]
- 0043c3ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c3ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c3ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043c3ac ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 0043c3ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c3ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c3ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c3ac bytes 08213c91
+ 0043c3ac bytes 08613d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6332ee8f038db8aa9a850715b37522ed"></a>

### [`0043c490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c490.md) → [`0043c490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c490.md) FUN_0043c490

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0043b790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043b/0043b790.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 5件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0043b790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043b/0043b790.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.00% / 新版 98.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043c53c",
      "incomplete_value": true,
      "site": "0043c53c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:653:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c53c",
      "incomplete_value": true,
      "site": "0043c53c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e0:8"
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
      "0043c528",
      "READ",
      [
        "storage",
        "002926e0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043c528",
      "READ",
      [
        "storage",
        "00292653",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c490.md#insn-0043c520)
- 新版 `0043c520`（命令位置の公開資料なし）

~~~diff
- 0043c520 ["COPY", "tmp:0:8", ["const:6e0:8"]]
- 0043c520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043c520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043c520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043c520 ["COPY", "tmp:0:8", ["const:653:8"]]
+ 0043c520 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043c520 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043c520 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043c520 bytes 29811b91
+ 0043c520 bytes 294d1991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ceef66af01f88b2c8f038d659de525b1"></a>

### [`0043c754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c754.md) → [`0043c754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c754.md) FUN_0043c754

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
      "definition_site": "0043c760",
      "incomplete_value": false,
      "site": "0043c76c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c760",
      "incomplete_value": false,
      "site": "0043c76c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "0043c76c",
      "DATA",
      [
        "storage",
        "00be6f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c76c",
      "DATA",
      [
        "storage",
        "00be6fd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c754.md#insn-0043c760)
- 新版 `0043c760`（命令位置の公開資料なし）

~~~diff
- 0043c760 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 0043c760 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043c760 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043c760 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043c760 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 0043c760 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043c760 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043c760 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043c760 bytes 4a213e91
+ 0043c760 bytes 4a613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-693a0f10ec7831e84826f2504cdecf36"></a>

### [`0043c798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c798.md) → [`0043c798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c798.md) FUN_0043c798

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
      "definition_site": "0043c7b0",
      "incomplete_value": false,
      "site": "0043c7bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c7b0",
      "incomplete_value": false,
      "site": "0043c7bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "0043c7bc",
      "DATA",
      [
        "storage",
        "00be6f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c7bc",
      "DATA",
      [
        "storage",
        "00be6fd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c798.md#insn-0043c7b0)
- 新版 `0043c7b0`（命令位置の公開資料なし）

~~~diff
- 0043c7b0 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 0043c7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043c7b0 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 0043c7b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c7b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c7b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c7b0 bytes 08213e91
+ 0043c7b0 bytes 08613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e8905c4d0254f2cdbc64d86702ade15"></a>

### [`0043c7f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c7f4.md) → [`0043c7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c7f4.md) FUN_0043c7f4

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
      "definition_site": "0043c820",
      "incomplete_value": false,
      "site": "0043c820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c820",
      "incomplete_value": false,
      "site": "0043c820",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "0043c820",
      "DATA",
      [
        "storage",
        "00be6f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c820",
      "DATA",
      [
        "storage",
        "00be6fd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c7f4.md#insn-0043c818)
- 新版 `0043c818`（命令位置の公開資料なし）

~~~diff
- 0043c818 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 0043c818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043c818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043c818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043c818 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 0043c818 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c818 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043c818 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043c818 bytes 08213e91
+ 0043c818 bytes 08613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b54e79311c067fd4b92865cad655a989"></a>

### [`0043c87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c87c.md) → [`0043c87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043c87c.md) FUN_0043c87c

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
      "definition_site": "0043c898",
      "incomplete_value": false,
      "site": "0043c898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043c898",
      "incomplete_value": false,
      "site": "0043c898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:be6000:8"
          ],
          [
            "leaf",
            "const:f88:8"
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
      "0043c898",
      "DATA",
      [
        "storage",
        "00be6f88",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043c898",
      "DATA",
      [
        "storage",
        "00be6fd8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043c894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043c87c.md#insn-0043c894)
- 新版 `0043c894`（命令位置の公開資料なし）

~~~diff
- 0043c894 ["COPY", "tmp:0:8", ["const:f88:8"]]
- 0043c894 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043c894 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043c894 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043c894 ["COPY", "tmp:0:8", ["const:fd8:8"]]
+ 0043c894 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043c894 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043c894 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043c894 bytes 29213e91
+ 0043c894 bytes 29613f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe5114b93dcd5bfda8e8620dc08c592f"></a>

### [`0043ca28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043ca28.md) → [`0043ca28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043ca28.md) FUN_0043ca28

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
      "definition_site": "0043ca3c",
      "incomplete_value": false,
      "site": "0043ca40",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ca3c",
      "incomplete_value": false,
      "site": "0043ca40",
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
            "const:8:8"
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
      "0043ca40",
      "DATA",
      [
        "storage",
        "00be7008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043ca40",
      "DATA",
      [
        "storage",
        "00be7058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043ca3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043ca28.md#insn-0043ca3c)
- 新版 `0043ca3c`（命令位置の公開資料なし）

~~~diff
- 0043ca3c ["COPY", "tmp:0:8", ["const:8:8"]]
- 0043ca3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043ca3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043ca3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043ca3c ["COPY", "tmp:0:8", ["const:58:8"]]
+ 0043ca3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043ca3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043ca3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043ca3c bytes 08210091
+ 0043ca3c bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9c46ebfd40e16ab2f988740b1e4b016a"></a>

### [`0043ca84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043ca84.md) → [`0043ca84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043ca84.md) FUN_0043ca84

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
      "definition_site": "0043ca9c",
      "incomplete_value": false,
      "site": "0043caa0",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ca9c",
      "incomplete_value": false,
      "site": "0043caa0",
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
            "const:8:8"
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
      "0043caa0",
      "DATA",
      [
        "storage",
        "00be7008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043caa0",
      "DATA",
      [
        "storage",
        "00be7058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043ca9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043ca84.md#insn-0043ca9c)
- 新版 `0043ca9c`（命令位置の公開資料なし）

~~~diff
- 0043ca9c ["COPY", "tmp:0:8", ["const:8:8"]]
- 0043ca9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043ca9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043ca9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043ca9c ["COPY", "tmp:0:8", ["const:58:8"]]
+ 0043ca9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043ca9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043ca9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043ca9c bytes 08210091
+ 0043ca9c bytes 08610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-510d23b0f279ea3e72d88f06df38c6e5"></a>

### [`0043cae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cae0.md) → [`0043cae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cae0.md) FUN_0043cae0

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
      "definition_site": "0043cb04",
      "incomplete_value": false,
      "site": "0043cb04",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cb04",
      "incomplete_value": false,
      "site": "0043cb04",
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
            "const:8:8"
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
      "0043cb04",
      "DATA",
      [
        "storage",
        "00be7008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043cb04",
      "DATA",
      [
        "storage",
        "00be7058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cae0.md#insn-0043cb00)
- 新版 `0043cb00`（命令位置の公開資料なし）

~~~diff
- 0043cb00 ["COPY", "tmp:0:8", ["const:8:8"]]
- 0043cb00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043cb00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043cb00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043cb00 ["COPY", "tmp:0:8", ["const:58:8"]]
+ 0043cb00 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043cb00 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043cb00 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043cb00 bytes 29210091
+ 0043cb00 bytes 29610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c63be6af9c0d1e4e824679f23bf88b0"></a>

### [`0043cb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cb30.md) → [`0043cb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cb30.md) FUN_0043cb30

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
      "definition_site": "0043cb3c",
      "incomplete_value": false,
      "site": "0043cb3c",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cb3c",
      "incomplete_value": false,
      "site": "0043cb3c",
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
            "const:8:8"
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
      "0043cb3c",
      "DATA",
      [
        "storage",
        "00be7008",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043cb3c",
      "DATA",
      [
        "storage",
        "00be7058",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cb30.md#insn-0043cb38)
- 新版 `0043cb38`（命令位置の公開資料なし）

~~~diff
- 0043cb38 ["COPY", "tmp:0:8", ["const:8:8"]]
- 0043cb38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043cb38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043cb38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043cb38 ["COPY", "tmp:0:8", ["const:58:8"]]
+ 0043cb38 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043cb38 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043cb38 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043cb38 bytes 29210091
+ 0043cb38 bytes 29610191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31036e25536164e2bc0034e3e4315f3e"></a>

### [`0043ccc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043ccc4.md) → [`0043ccc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043ccc4.md) FUN_0043ccc4

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
      "definition_site": "0043ccd0",
      "incomplete_value": false,
      "site": "0043ccdc",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ccd0",
      "incomplete_value": false,
      "site": "0043ccdc",
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
            "const:88:8"
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
      "0043ccdc",
      "DATA",
      [
        "storage",
        "00be7088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043ccdc",
      "DATA",
      [
        "storage",
        "00be70d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043ccd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043ccc4.md#insn-0043ccd0)
- 新版 `0043ccd0`（命令位置の公開資料なし）

~~~diff
- 0043ccd0 ["COPY", "tmp:0:8", ["const:88:8"]]
- 0043ccd0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043ccd0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043ccd0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043ccd0 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 0043ccd0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043ccd0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043ccd0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043ccd0 bytes 4a210291
+ 0043ccd0 bytes 4a610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c599da727e201a8de887ba2bb6e78775"></a>

### [`0043cd08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cd08.md) → [`0043cd08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cd08.md) FUN_0043cd08

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
      "definition_site": "0043cd20",
      "incomplete_value": false,
      "site": "0043cd2c",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cd20",
      "incomplete_value": false,
      "site": "0043cd2c",
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
            "const:88:8"
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
      "0043cd2c",
      "DATA",
      [
        "storage",
        "00be7088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043cd2c",
      "DATA",
      [
        "storage",
        "00be70d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cd20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cd08.md#insn-0043cd20)
- 新版 `0043cd20`（命令位置の公開資料なし）

~~~diff
- 0043cd20 ["COPY", "tmp:0:8", ["const:88:8"]]
- 0043cd20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043cd20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043cd20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043cd20 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 0043cd20 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cd20 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cd20 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043cd20 bytes 08210291
+ 0043cd20 bytes 08610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cc4c8ca91527db8dc648f1f2e32c116"></a>

### [`0043cd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cd64.md) → [`0043cd64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cd64.md) FUN_0043cd64

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
      "definition_site": "0043cd90",
      "incomplete_value": false,
      "site": "0043cd90",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cd90",
      "incomplete_value": false,
      "site": "0043cd90",
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
            "const:88:8"
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
      "0043cd90",
      "DATA",
      [
        "storage",
        "00be7088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043cd90",
      "DATA",
      [
        "storage",
        "00be70d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cd88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cd64.md#insn-0043cd88)
- 新版 `0043cd88`（命令位置の公開資料なし）

~~~diff
- 0043cd88 ["COPY", "tmp:0:8", ["const:88:8"]]
- 0043cd88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043cd88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043cd88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043cd88 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 0043cd88 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cd88 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cd88 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043cd88 bytes 08210291
+ 0043cd88 bytes 08610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88f8fe2015f1c9b9d041d77d2423e127"></a>

### [`0043cdec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cdec.md) → [`0043cdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cdec.md) FUN_0043cdec

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
      "definition_site": "0043ce08",
      "incomplete_value": false,
      "site": "0043ce08",
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
            "const:d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ce08",
      "incomplete_value": false,
      "site": "0043ce08",
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
            "const:88:8"
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
      "0043ce08",
      "DATA",
      [
        "storage",
        "00be7088",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043ce08",
      "DATA",
      [
        "storage",
        "00be70d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043ce04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cdec.md#insn-0043ce04)
- 新版 `0043ce04`（命令位置の公開資料なし）

~~~diff
- 0043ce04 ["COPY", "tmp:0:8", ["const:88:8"]]
- 0043ce04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043ce04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043ce04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043ce04 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 0043ce04 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043ce04 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043ce04 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043ce04 bytes 29210291
+ 0043ce04 bytes 29610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-210fc9c3d665b924c095180cdf135a43"></a>

### [`0043cf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cf30.md) → [`0043cf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cf30.md) FUN_0043cf30

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
      "definition_site": "0043cf3c",
      "incomplete_value": false,
      "site": "0043cf48",
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
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cf3c",
      "incomplete_value": false,
      "site": "0043cf48",
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
            "const:108:8"
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
      "0043cf48",
      "DATA",
      [
        "storage",
        "00be7108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043cf48",
      "DATA",
      [
        "storage",
        "00be7158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cf3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cf30.md#insn-0043cf3c)
- 新版 `0043cf3c`（命令位置の公開資料なし）

~~~diff
- 0043cf3c ["COPY", "tmp:0:8", ["const:108:8"]]
- 0043cf3c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043cf3c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043cf3c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043cf3c ["COPY", "tmp:0:8", ["const:158:8"]]
+ 0043cf3c ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043cf3c ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043cf3c ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043cf3c bytes 4a210491
+ 0043cf3c bytes 4a610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc0f4682e2010644dc71a9530d9e6555"></a>

### [`0043cf74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cf74.md) → [`0043cf74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cf74.md) FUN_0043cf74

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
      "definition_site": "0043cf8c",
      "incomplete_value": false,
      "site": "0043cf98",
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
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cf8c",
      "incomplete_value": false,
      "site": "0043cf98",
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
            "const:108:8"
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
      "0043cf98",
      "DATA",
      [
        "storage",
        "00be7108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043cf98",
      "DATA",
      [
        "storage",
        "00be7158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cf8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cf74.md#insn-0043cf8c)
- 新版 `0043cf8c`（命令位置の公開資料なし）

~~~diff
- 0043cf8c ["COPY", "tmp:0:8", ["const:108:8"]]
- 0043cf8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043cf8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043cf8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043cf8c ["COPY", "tmp:0:8", ["const:158:8"]]
+ 0043cf8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cf8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cf8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043cf8c bytes 08210491
+ 0043cf8c bytes 08610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82aa33d7e99e97dc9503fb427f6cdf8d"></a>

### [`0043cfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cfd0.md) → [`0043cfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043c/0043cfd0.md) FUN_0043cfd0

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
      "definition_site": "0043cffc",
      "incomplete_value": false,
      "site": "0043cffc",
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
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043cffc",
      "incomplete_value": false,
      "site": "0043cffc",
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
      "0043cffc",
      "DATA",
      [
        "storage",
        "00be7108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043cffc",
      "DATA",
      [
        "storage",
        "00be7158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043cff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043c/0043cfd0.md#insn-0043cff4)
- 新版 `0043cff4`（命令位置の公開資料なし）

~~~diff
- 0043cff4 ["COPY", "tmp:0:8", ["const:108:8"]]
- 0043cff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043cff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043cff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043cff4 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 0043cff4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cff4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043cff4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043cff4 bytes 08210491
+ 0043cff4 bytes 08610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a35ccd380ed0dea5f65e5994a803156"></a>

### [`0043d058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d058.md) → [`0043d058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d058.md) FUN_0043d058

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
      "definition_site": "0043d074",
      "incomplete_value": false,
      "site": "0043d074",
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
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d074",
      "incomplete_value": false,
      "site": "0043d074",
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
            "const:108:8"
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
      "0043d074",
      "DATA",
      [
        "storage",
        "00be7108",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043d074",
      "DATA",
      [
        "storage",
        "00be7158",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d058.md#insn-0043d070)
- 新版 `0043d070`（命令位置の公開資料なし）

~~~diff
- 0043d070 ["COPY", "tmp:0:8", ["const:108:8"]]
- 0043d070 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043d070 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043d070 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043d070 ["COPY", "tmp:0:8", ["const:158:8"]]
+ 0043d070 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043d070 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043d070 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043d070 bytes 29210491
+ 0043d070 bytes 29610591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51d75199431f5559daa1b5ab60f82a81"></a>

### [`0043d1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d1f8.md) → [`0043d1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d1f8.md) FUN_0043d1f8

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
      "definition_site": "0043d20c",
      "incomplete_value": false,
      "site": "0043d210",
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
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d20c",
      "incomplete_value": false,
      "site": "0043d210",
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
            "const:188:8"
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
      "0043d210",
      "DATA",
      [
        "storage",
        "00be7188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043d210",
      "DATA",
      [
        "storage",
        "00be71d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d20c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d1f8.md#insn-0043d20c)
- 新版 `0043d20c`（命令位置の公開資料なし）

~~~diff
- 0043d20c ["COPY", "tmp:0:8", ["const:188:8"]]
- 0043d20c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043d20c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043d20c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043d20c ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 0043d20c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d20c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d20c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043d20c bytes 08210691
+ 0043d20c bytes 08610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d5f75592f519bd09b4ea6c55d568706"></a>

### [`0043d21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d21c.md) → [`0043d21c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d21c.md) FUN_0043d21c

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
      "definition_site": "0043d220",
      "incomplete_value": false,
      "site": "0043d224",
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
            "const:1d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d220",
      "incomplete_value": false,
      "site": "0043d224",
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
      "0043d224",
      "DATA",
      [
        "storage",
        "00be7188",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043d224",
      "DATA",
      [
        "storage",
        "00be71d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d21c.md#insn-0043d220)
- 新版 `0043d220`（命令位置の公開資料なし）

~~~diff
- 0043d220 ["COPY", "tmp:0:8", ["const:188:8"]]
- 0043d220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043d220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043d220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043d220 ["COPY", "tmp:0:8", ["const:1d8:8"]]
+ 0043d220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043d220 bytes 08210691
+ 0043d220 bytes 08610791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9aa524a5cda7bff93930692cbad6e4c"></a>

### [`0043d234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d234.md) → [`0043d234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d234.md) FUN_0043d234

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00573e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00573/00573e38.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00573e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00573/00573e38.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.77% / 新版 91.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 3件, `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043d360",
      "incomplete_value": true,
      "site": "0043d360",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:421:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d360",
      "incomplete_value": true,
      "site": "0043d360",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:396:8"
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
    "kind": "call_target",
    "new": {
      "definition_site": "0043d3fc",
      "incomplete_value": true,
      "site": "0043d3fc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0043d3fc",
      "incomplete_value": true,
      "site": "0043d3fc",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 11,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0043d3ec",
      "incomplete_value": true,
      "site": "0043d3fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d3ec",
      "incomplete_value": true,
      "site": "0043d3fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0043d350",
      "READ",
      [
        "storage",
        "002a5396",
        null,
        "string"
      ]
    ],
    [
      "0043d398",
      "READ",
      [
        "storage",
        "00c24ba0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043d3a4",
      "READ",
      [
        "storage",
        "00c24b98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "0043d350",
      "READ",
      [
        "storage",
        "002a5421",
        null,
        "string"
      ]
    ],
    [
      "0043d398",
      "READ",
      [
        "storage",
        "00c24be0",
        null,
        "undefined1"
      ]
    ],
    [
      "0043d3a4",
      "READ",
      [
        "storage",
        "00c24bd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d234.md#insn-0043d348) · [`0043d394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d234.md#insn-0043d394) · [`0043d3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d234.md#insn-0043d3a4)
- 新版 `0043d348`（命令位置の公開資料なし） · `0043d394`（命令位置の公開資料なし） · `0043d3a4`（命令位置の公開資料なし）

~~~diff
- 0043d348 ["COPY", "tmp:0:8", ["const:396:8"]]
- 0043d348 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043d348 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043d348 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043d348 ["COPY", "tmp:0:8", ["const:421:8"]]
+ 0043d348 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043d348 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043d348 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043d348 bytes 29590e91
+ 0043d348 bytes 29851091
- 0043d394 ["COPY", "tmp:0:8", ["const:ba0:8"]]
- 0043d394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043d394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043d394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043d394 ["COPY", "tmp:0:8", ["const:be0:8"]]
+ 0043d394 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d394 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d394 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043d394 bytes 08812e91
+ 0043d394 bytes 08812f91
- 0043d3a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b98:8"]]
- 0043d3a4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 0043d3a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bd8:8"]]
+ 0043d3a4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 0043d3a4 bytes 00cd45f9
+ 0043d3a4 bytes 00ed45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5860ef5d05d8efc2a6e9d63c7cc82781"></a>

### [`0043d694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d694.md) → [`0043d694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d694.md) FUN_0043d694

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
      "definition_site": "0043d6a0",
      "incomplete_value": false,
      "site": "0043d6ac",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d6a0",
      "incomplete_value": false,
      "site": "0043d6ac",
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
            "const:208:8"
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
      "0043d6ac",
      "DATA",
      [
        "storage",
        "00be7208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043d6ac",
      "DATA",
      [
        "storage",
        "00be7258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d694.md#insn-0043d6a0)
- 新版 `0043d6a0`（命令位置の公開資料なし）

~~~diff
- 0043d6a0 ["COPY", "tmp:0:8", ["const:208:8"]]
- 0043d6a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043d6a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043d6a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043d6a0 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 0043d6a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043d6a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043d6a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043d6a0 bytes 4a210891
+ 0043d6a0 bytes 4a610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3015808e20704abc89b74c0086088e4e"></a>

### [`0043d6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d6d8.md) → [`0043d6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d6d8.md) FUN_0043d6d8

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
      "definition_site": "0043d6f0",
      "incomplete_value": false,
      "site": "0043d6fc",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d6f0",
      "incomplete_value": false,
      "site": "0043d6fc",
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
            "const:208:8"
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
      "0043d6fc",
      "DATA",
      [
        "storage",
        "00be7208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043d6fc",
      "DATA",
      [
        "storage",
        "00be7258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d6d8.md#insn-0043d6f0)
- 新版 `0043d6f0`（命令位置の公開資料なし）

~~~diff
- 0043d6f0 ["COPY", "tmp:0:8", ["const:208:8"]]
- 0043d6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043d6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043d6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043d6f0 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 0043d6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043d6f0 bytes 08210891
+ 0043d6f0 bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e364667941b2ed2a15c3d2677c317388"></a>

### [`0043d734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d734.md) → [`0043d734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d734.md) FUN_0043d734

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
      "definition_site": "0043d760",
      "incomplete_value": false,
      "site": "0043d760",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d760",
      "incomplete_value": false,
      "site": "0043d760",
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
            "const:208:8"
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
      "0043d760",
      "DATA",
      [
        "storage",
        "00be7208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043d760",
      "DATA",
      [
        "storage",
        "00be7258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d734.md#insn-0043d758)
- 新版 `0043d758`（命令位置の公開資料なし）

~~~diff
- 0043d758 ["COPY", "tmp:0:8", ["const:208:8"]]
- 0043d758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043d758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043d758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043d758 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 0043d758 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d758 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043d758 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043d758 bytes 08210891
+ 0043d758 bytes 08610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8873cfe52805f0c8777c579408a9efbe"></a>

### [`0043d7bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d7bc.md) → [`0043d7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d7bc.md) FUN_0043d7bc

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
      "definition_site": "0043d7d8",
      "incomplete_value": false,
      "site": "0043d7d8",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043d7d8",
      "incomplete_value": false,
      "site": "0043d7d8",
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
            "const:208:8"
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
      "0043d7d8",
      "DATA",
      [
        "storage",
        "00be7208",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043d7d8",
      "DATA",
      [
        "storage",
        "00be7258",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043d7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d7bc.md#insn-0043d7d4)
- 新版 `0043d7d4`（命令位置の公開資料なし）

~~~diff
- 0043d7d4 ["COPY", "tmp:0:8", ["const:208:8"]]
- 0043d7d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043d7d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043d7d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043d7d4 ["COPY", "tmp:0:8", ["const:258:8"]]
+ 0043d7d4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043d7d4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043d7d4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043d7d4 bytes 29210891
+ 0043d7d4 bytes 29610991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d059b9489495e6edb122cf62d576246"></a>

### [`0043d8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d8b8.md) → [`0043d8b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043d/0043d8b8.md) FUN_0043d8b8

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/00436e9c.md) [`0043e5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e5d8.md) [`0043e7f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e7f8.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e54c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e54c.md) [`00436e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/00436e9c.md) [`0043e5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e5d8.md) [`0043e7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e7f8.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.41% / 新版 97.41%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0043da40",
      "incomplete_value": true,
      "site": "0043da4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:270:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043da40",
      "incomplete_value": true,
      "site": "0043da4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e5:8"
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
      "definition_site": "0043dbac",
      "incomplete_value": true,
      "site": "0043dbbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:687:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043dbac",
      "incomplete_value": true,
      "site": "0043dbbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5ed:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "0043dbc0",
      "incomplete_value": true,
      "site": "0043dbc0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0043dbc0",
      "incomplete_value": true,
      "site": "0043dbc0",
      "value": [
        "LOAD",
        "8",
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
      "0043da40",
      "READ",
      [
        "storage",
        "002a21e5",
        null,
        "string"
      ]
    ],
    [
      "0043dbac",
      "READ",
      [
        "storage",
        "002a65ed",
        null,
        "string"
      ]
    ],
    [
      "0043dbb4",
      "READ",
      [
        "storage",
        "002a65f2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0043da40",
      "READ",
      [
        "storage",
        "002a2270",
        null,
        "string"
      ]
    ],
    [
      "0043dbac",
      "READ",
      [
        "storage",
        "002a6687",
        null,
        "string"
      ]
    ],
    [
      "0043dbb4",
      "READ",
      [
        "storage",
        "002a668c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043da3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d8b8.md#insn-0043da3c) · [`0043dba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d8b8.md#insn-0043dba4) · [`0043dc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043d/0043d8b8.md#insn-0043dc48)
- 新版 `0043da3c`（命令位置の公開資料なし） · `0043dba4`（命令位置の公開資料なし） · `0043dc48`（命令位置の公開資料なし）

~~~diff
- 0043da3c ["COPY", "tmp:0:8", ["const:1e5:8"]]
- 0043da3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043da3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043da3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043da3c ["COPY", "tmp:0:8", ["const:270:8"]]
+ 0043da3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043da3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043da3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043da3c bytes 08950791
+ 0043da3c bytes 08c10991
- 0043dba4 ["COPY", "tmp:0:8", ["const:5ed:8"]]
- 0043dba4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043dba4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043dba4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043dba4 ["COPY", "tmp:0:8", ["const:687:8"]]
+ 0043dba4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043dba4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043dba4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043dba4 bytes 4ab51791
+ 0043dba4 bytes 4a1d1a91
- 0043dc48 ["COPY", "tmp:0:8", ["const:34a:8"]]
- 0043dc48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043dc48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043dc48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043dc48 ["COPY", "tmp:0:8", ["const:3d5:8"]]
+ 0043dc48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043dc48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043dc48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043dc48 bytes 08290d91
+ 0043dc48 bytes 08550f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-433d4ee511b1a5abc540e38ac6cf3127"></a>

### [`0043e788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e788.md) → [`0043e788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e788.md) FUN_0043e788

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0043e5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e5d8.md) [`0043eef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043eef0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 2件 [`0043e5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e5d8.md) [`0043eef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043eef0.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0043e794",
      "incomplete_value": false,
      "site": "0043e798",
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
      "definition_site": "0043e794",
      "incomplete_value": false,
      "site": "0043e798",
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
      "0043e794",
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
      "0043e794",
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

- 旧版 [`0043e794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e788.md#insn-0043e794)
- 新版 `0043e794`（命令位置の公開資料なし）

~~~diff
- 0043e794 ["COPY", "tmp:0:8", ["const:303:8"]]
- 0043e794 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0043e794 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0043e794 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0043e794 ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0043e794 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0043e794 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0043e794 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0043e794 bytes 000c0c91
+ 0043e794 bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89db704c9c3f29fe1f6f422d1dd95092"></a>

### [`0043eb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043eb40.md) → [`0043eb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043eb40.md) FUN_0043eb40

採用 · 移動量 `+0x0` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`0043e940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043e940.md) [`0043ec60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043ec60.md) [`00989584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00989/00989584.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c38.md)
- 新版 呼出元 3件 [`0043e940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043e940.md) [`0043ec60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043e/0043ec60.md) [`00989584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00989/00989584.md) · 呼出先 1件 [`00418c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c38.md)

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
      "definition_site": "0043eb4c",
      "incomplete_value": false,
      "site": "0043eb50",
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
      "definition_site": "0043eb4c",
      "incomplete_value": false,
      "site": "0043eb50",
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
      "0043eb4c",
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
      "0043eb4c",
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

- 旧版 [`0043eb4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043e/0043eb40.md#insn-0043eb4c)
- 新版 `0043eb4c`（命令位置の公開資料なし）

~~~diff
- 0043eb4c ["COPY", "tmp:0:8", ["const:303:8"]]
- 0043eb4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0043eb4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0043eb4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0043eb4c ["COPY", "tmp:0:8", ["const:39d:8"]]
+ 0043eb4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0043eb4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0043eb4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0043eb4c bytes 000c0c91
+ 0043eb4c bytes 00740e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-810ea3905b93703d385f1079682daaf1"></a>

### [`0043f158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f158.md) → [`0043f158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f158.md) FUN_0043f158

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
      "definition_site": "0043f164",
      "incomplete_value": false,
      "site": "0043f170",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f164",
      "incomplete_value": false,
      "site": "0043f170",
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
            "const:288:8"
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
      "0043f170",
      "DATA",
      [
        "storage",
        "00be7288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f170",
      "DATA",
      [
        "storage",
        "00be72d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f158.md#insn-0043f164)
- 新版 `0043f164`（命令位置の公開資料なし）

~~~diff
- 0043f164 ["COPY", "tmp:0:8", ["const:288:8"]]
- 0043f164 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043f164 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043f164 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043f164 ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 0043f164 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043f164 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043f164 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043f164 bytes 4a210a91
+ 0043f164 bytes 4a610b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-442824efcaf4f1bbae024e40cd28be8f"></a>

### [`0043f19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f19c.md) → [`0043f19c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f19c.md) FUN_0043f19c

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
      "definition_site": "0043f1b4",
      "incomplete_value": false,
      "site": "0043f1c0",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f1b4",
      "incomplete_value": false,
      "site": "0043f1c0",
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
            "const:288:8"
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
      "0043f1c0",
      "DATA",
      [
        "storage",
        "00be7288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f1c0",
      "DATA",
      [
        "storage",
        "00be72d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f19c.md#insn-0043f1b4)
- 新版 `0043f1b4`（命令位置の公開資料なし）

~~~diff
- 0043f1b4 ["COPY", "tmp:0:8", ["const:288:8"]]
- 0043f1b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f1b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f1b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043f1b4 ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 0043f1b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f1b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f1b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f1b4 bytes 08210a91
+ 0043f1b4 bytes 08610b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c4b6133bf2610622b45017d1cf80740"></a>

### [`0043f1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f1f8.md) → [`0043f1f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f1f8.md) FUN_0043f1f8

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
      "definition_site": "0043f224",
      "incomplete_value": false,
      "site": "0043f224",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f224",
      "incomplete_value": false,
      "site": "0043f224",
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
            "const:288:8"
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
      "0043f224",
      "DATA",
      [
        "storage",
        "00be7288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f224",
      "DATA",
      [
        "storage",
        "00be72d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f1f8.md#insn-0043f21c)
- 新版 `0043f21c`（命令位置の公開資料なし）

~~~diff
- 0043f21c ["COPY", "tmp:0:8", ["const:288:8"]]
- 0043f21c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f21c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f21c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043f21c ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 0043f21c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f21c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f21c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f21c bytes 08210a91
+ 0043f21c bytes 08610b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68fad48db4d226d96fd2bd48d2bf3acf"></a>

### [`0043f280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f280.md) → [`0043f280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f280.md) FUN_0043f280

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
      "definition_site": "0043f29c",
      "incomplete_value": false,
      "site": "0043f29c",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f29c",
      "incomplete_value": false,
      "site": "0043f29c",
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
            "const:288:8"
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
      "0043f29c",
      "DATA",
      [
        "storage",
        "00be7288",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f29c",
      "DATA",
      [
        "storage",
        "00be72d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f280.md#insn-0043f298)
- 新版 `0043f298`（命令位置の公開資料なし）

~~~diff
- 0043f298 ["COPY", "tmp:0:8", ["const:288:8"]]
- 0043f298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043f298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043f298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043f298 ["COPY", "tmp:0:8", ["const:2d8:8"]]
+ 0043f298 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f298 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f298 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043f298 bytes 29210a91
+ 0043f298 bytes 29610b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58a94f8f9725fb9df67c312531eed518"></a>

### [`0043f4e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f4e8.md) → [`0043f4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f4e8.md) FUN_0043f4e8

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
      "definition_site": "0043f4f4",
      "incomplete_value": false,
      "site": "0043f500",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f4f4",
      "incomplete_value": false,
      "site": "0043f500",
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
            "const:308:8"
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
      "0043f500",
      "DATA",
      [
        "storage",
        "00be7308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f500",
      "DATA",
      [
        "storage",
        "00be7358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f4e8.md#insn-0043f4f4)
- 新版 `0043f4f4`（命令位置の公開資料なし）

~~~diff
- 0043f4f4 ["COPY", "tmp:0:8", ["const:308:8"]]
- 0043f4f4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043f4f4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043f4f4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043f4f4 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0043f4f4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043f4f4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043f4f4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043f4f4 bytes 4a210c91
+ 0043f4f4 bytes 4a610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2e28d773de3cb0bea32ded1b0994c3c"></a>

### [`0043f52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f52c.md) → [`0043f52c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f52c.md) FUN_0043f52c

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
      "definition_site": "0043f544",
      "incomplete_value": false,
      "site": "0043f550",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f544",
      "incomplete_value": false,
      "site": "0043f550",
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
            "const:308:8"
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
      "0043f550",
      "DATA",
      [
        "storage",
        "00be7308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f550",
      "DATA",
      [
        "storage",
        "00be7358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f52c.md#insn-0043f544)
- 新版 `0043f544`（命令位置の公開資料なし）

~~~diff
- 0043f544 ["COPY", "tmp:0:8", ["const:308:8"]]
- 0043f544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043f544 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0043f544 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f544 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f544 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f544 bytes 08210c91
+ 0043f544 bytes 08610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8f7f0fe388abe75b1ca99ed4c7876ce"></a>

### [`0043f588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f588.md) → [`0043f588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f588.md) FUN_0043f588

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
      "definition_site": "0043f5b4",
      "incomplete_value": false,
      "site": "0043f5b4",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f5b4",
      "incomplete_value": false,
      "site": "0043f5b4",
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
            "const:308:8"
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
      "0043f5b4",
      "DATA",
      [
        "storage",
        "00be7308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f5b4",
      "DATA",
      [
        "storage",
        "00be7358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f588.md#insn-0043f5ac)
- 新版 `0043f5ac`（命令位置の公開資料なし）

~~~diff
- 0043f5ac ["COPY", "tmp:0:8", ["const:308:8"]]
- 0043f5ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f5ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f5ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043f5ac ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0043f5ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f5ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f5ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f5ac bytes 08210c91
+ 0043f5ac bytes 08610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-052e3e4e797e6c477d89fd8d8c49a487"></a>

### [`0043f610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f610.md) → [`0043f610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f610.md) FUN_0043f610

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
      "definition_site": "0043f62c",
      "incomplete_value": false,
      "site": "0043f62c",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f62c",
      "incomplete_value": false,
      "site": "0043f62c",
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
            "const:308:8"
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
      "0043f62c",
      "DATA",
      [
        "storage",
        "00be7308",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f62c",
      "DATA",
      [
        "storage",
        "00be7358",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f610.md#insn-0043f628)
- 新版 `0043f628`（命令位置の公開資料なし）

~~~diff
- 0043f628 ["COPY", "tmp:0:8", ["const:308:8"]]
- 0043f628 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043f628 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043f628 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043f628 ["COPY", "tmp:0:8", ["const:358:8"]]
+ 0043f628 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f628 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f628 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043f628 bytes 29210c91
+ 0043f628 bytes 29610d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a787f8cd90430c7313e51a3ed09a5ff"></a>

### [`0043f7a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f7a8.md) → [`0043f7a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f7a8.md) FUN_0043f7a8

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
      "definition_site": "0043f7b4",
      "incomplete_value": false,
      "site": "0043f7c0",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f7b4",
      "incomplete_value": false,
      "site": "0043f7c0",
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
            "const:388:8"
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
      "0043f7c0",
      "DATA",
      [
        "storage",
        "00be7388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f7c0",
      "DATA",
      [
        "storage",
        "00be73d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f7a8.md#insn-0043f7b4)
- 新版 `0043f7b4`（命令位置の公開資料なし）

~~~diff
- 0043f7b4 ["COPY", "tmp:0:8", ["const:388:8"]]
- 0043f7b4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043f7b4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043f7b4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043f7b4 ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 0043f7b4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043f7b4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043f7b4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043f7b4 bytes 4a210e91
+ 0043f7b4 bytes 4a610f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa4ec3901fa2f8d9080b40b0fa327a50"></a>

### [`0043f7ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f7ec.md) → [`0043f7ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f7ec.md) FUN_0043f7ec

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
      "definition_site": "0043f804",
      "incomplete_value": false,
      "site": "0043f810",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f804",
      "incomplete_value": false,
      "site": "0043f810",
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
            "const:388:8"
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
      "0043f810",
      "DATA",
      [
        "storage",
        "00be7388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f810",
      "DATA",
      [
        "storage",
        "00be73d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f7ec.md#insn-0043f804)
- 新版 `0043f804`（命令位置の公開資料なし）

~~~diff
- 0043f804 ["COPY", "tmp:0:8", ["const:388:8"]]
- 0043f804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043f804 ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 0043f804 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f804 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f804 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f804 bytes 08210e91
+ 0043f804 bytes 08610f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46c3c9a5c8c49b5301398649063d6324"></a>

### [`0043f848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f848.md) → [`0043f848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f848.md) FUN_0043f848

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
      "definition_site": "0043f874",
      "incomplete_value": false,
      "site": "0043f874",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f874",
      "incomplete_value": false,
      "site": "0043f874",
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
      "0043f874",
      "DATA",
      [
        "storage",
        "00be7388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f874",
      "DATA",
      [
        "storage",
        "00be73d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f848.md#insn-0043f86c)
- 新版 `0043f86c`（命令位置の公開資料なし）

~~~diff
- 0043f86c ["COPY", "tmp:0:8", ["const:388:8"]]
- 0043f86c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043f86c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043f86c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043f86c ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 0043f86c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f86c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043f86c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043f86c bytes 08210e91
+ 0043f86c bytes 08610f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0798f66cb0d5821f67e5adec65ed1ab9"></a>

### [`0043f8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f8d0.md) → [`0043f8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043f8d0.md) FUN_0043f8d0

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
      "definition_site": "0043f8ec",
      "incomplete_value": false,
      "site": "0043f8ec",
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
            "const:3d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043f8ec",
      "incomplete_value": false,
      "site": "0043f8ec",
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
            "const:388:8"
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
      "0043f8ec",
      "DATA",
      [
        "storage",
        "00be7388",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043f8ec",
      "DATA",
      [
        "storage",
        "00be73d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043f8e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043f8d0.md#insn-0043f8e8)
- 新版 `0043f8e8`（命令位置の公開資料なし）

~~~diff
- 0043f8e8 ["COPY", "tmp:0:8", ["const:388:8"]]
- 0043f8e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043f8e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043f8e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043f8e8 ["COPY", "tmp:0:8", ["const:3d8:8"]]
+ 0043f8e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f8e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043f8e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043f8e8 bytes 29210e91
+ 0043f8e8 bytes 29610f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e1a72fa2ef058c368c9e3966a81e7d1"></a>

### [`0043fa68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043fa68.md) → [`0043fa68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fa68.md) FUN_0043fa68

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
      "definition_site": "0043fa74",
      "incomplete_value": false,
      "site": "0043fa80",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fa74",
      "incomplete_value": false,
      "site": "0043fa80",
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
            "const:408:8"
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
      "0043fa80",
      "DATA",
      [
        "storage",
        "00be7408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043fa80",
      "DATA",
      [
        "storage",
        "00be7458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043fa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043fa68.md#insn-0043fa74)
- 新版 `0043fa74`（命令位置の公開資料なし）

~~~diff
- 0043fa74 ["COPY", "tmp:0:8", ["const:408:8"]]
- 0043fa74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043fa74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043fa74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043fa74 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0043fa74 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043fa74 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043fa74 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043fa74 bytes 4a211091
+ 0043fa74 bytes 4a611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0992effafd78f870dc999c280c63e56"></a>

### [`0043faac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043faac.md) → [`0043faac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043faac.md) FUN_0043faac

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
      "definition_site": "0043fac4",
      "incomplete_value": false,
      "site": "0043fad0",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fac4",
      "incomplete_value": false,
      "site": "0043fad0",
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
            "const:408:8"
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
      "0043fad0",
      "DATA",
      [
        "storage",
        "00be7408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043fad0",
      "DATA",
      [
        "storage",
        "00be7458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043fac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043faac.md#insn-0043fac4)
- 新版 `0043fac4`（命令位置の公開資料なし）

~~~diff
- 0043fac4 ["COPY", "tmp:0:8", ["const:408:8"]]
- 0043fac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043fac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043fac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043fac4 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0043fac4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043fac4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043fac4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043fac4 bytes 08211091
+ 0043fac4 bytes 08611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a5cd00cf2bbbc7119364c4a42e36e33"></a>

### [`0043fb08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043fb08.md) → [`0043fb08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fb08.md) FUN_0043fb08

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
      "definition_site": "0043fb34",
      "incomplete_value": false,
      "site": "0043fb34",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fb34",
      "incomplete_value": false,
      "site": "0043fb34",
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
            "const:408:8"
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
      "0043fb34",
      "DATA",
      [
        "storage",
        "00be7408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043fb34",
      "DATA",
      [
        "storage",
        "00be7458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043fb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043fb08.md#insn-0043fb2c)
- 新版 `0043fb2c`（命令位置の公開資料なし）

~~~diff
- 0043fb2c ["COPY", "tmp:0:8", ["const:408:8"]]
- 0043fb2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043fb2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043fb2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043fb2c ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0043fb2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043fb2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043fb2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043fb2c bytes 08211091
+ 0043fb2c bytes 08611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a8215c821b94dd3fdc35e408927d178"></a>

### [`0043fb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043fb90.md) → [`0043fb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fb90.md) FUN_0043fb90

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
      "definition_site": "0043fbac",
      "incomplete_value": false,
      "site": "0043fbac",
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
            "const:458:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fbac",
      "incomplete_value": false,
      "site": "0043fbac",
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
            "const:408:8"
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
      "0043fbac",
      "DATA",
      [
        "storage",
        "00be7408",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043fbac",
      "DATA",
      [
        "storage",
        "00be7458",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043fba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043fb90.md#insn-0043fba8)
- 新版 `0043fba8`（命令位置の公開資料なし）

~~~diff
- 0043fba8 ["COPY", "tmp:0:8", ["const:408:8"]]
- 0043fba8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 0043fba8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 0043fba8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 0043fba8 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 0043fba8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 0043fba8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 0043fba8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 0043fba8 bytes 29211091
+ 0043fba8 bytes 29611191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2020bd2a18f5f22c0b96424455e40cbd"></a>

### [`0043fee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043fee4.md) → [`0043fee4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043fee4.md) FUN_0043fee4

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
      "definition_site": "0043fef0",
      "incomplete_value": false,
      "site": "0043fefc",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043fef0",
      "incomplete_value": false,
      "site": "0043fefc",
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
            "const:488:8"
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
      "0043fefc",
      "DATA",
      [
        "storage",
        "00be7488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043fefc",
      "DATA",
      [
        "storage",
        "00be74d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043fef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043fee4.md#insn-0043fef0)
- 新版 `0043fef0`（命令位置の公開資料なし）

~~~diff
- 0043fef0 ["COPY", "tmp:0:8", ["const:488:8"]]
- 0043fef0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 0043fef0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 0043fef0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 0043fef0 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 0043fef0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 0043fef0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 0043fef0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 0043fef0 bytes 4a211291
+ 0043fef0 bytes 4a611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd5776ec82381208e87ce524716c4e45"></a>

### [`0043ff28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043ff28.md) → [`0043ff28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0043f/0043ff28.md) FUN_0043ff28

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
      "definition_site": "0043ff40",
      "incomplete_value": false,
      "site": "0043ff4c",
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
            "const:4d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0043ff40",
      "incomplete_value": false,
      "site": "0043ff4c",
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
            "const:488:8"
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
      "0043ff4c",
      "DATA",
      [
        "storage",
        "00be7488",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "0043ff4c",
      "DATA",
      [
        "storage",
        "00be74d8",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0043ff40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0043f/0043ff28.md#insn-0043ff40)
- 新版 `0043ff40`（命令位置の公開資料なし）

~~~diff
- 0043ff40 ["COPY", "tmp:0:8", ["const:488:8"]]
- 0043ff40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 0043ff40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 0043ff40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 0043ff40 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 0043ff40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 0043ff40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 0043ff40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 0043ff40 bytes 08211291
+ 0043ff40 bytes 08611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

