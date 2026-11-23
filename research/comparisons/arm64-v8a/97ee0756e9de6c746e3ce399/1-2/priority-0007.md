# v15.7.3 → v15.7.4 · 最優先の変更候補 (7)

[一覧の目次](README.md)

<a id="compare-3d54cc47e328aa5a5e46e53dbd64e786"></a>

### [`0047f2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047f/0047f2d0.md) → [`0047f2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f2d0.md) _ZN5Botan19AlgorithmIdentifierC2ERKNS_3OIDERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc5a0.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdc5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc5f0.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047f318",
      "incomplete_value": true,
      "site": "0047f318",
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
      "definition_site": "0047f318",
      "incomplete_value": true,
      "site": "0047f318",
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
      "definition_site": "0047f318",
      "incomplete_value": true,
      "site": "0047f318",
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
      "definition_site": "0047f318",
      "incomplete_value": true,
      "site": "0047f318",
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
      "0047f2f8",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "0047f304",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "0047f318",
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
      "0047f2f8",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "0047f304",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "0047f318",
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

- 旧版 [`0047f2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047f/0047f2d0.md#insn-0047f2f8) · [`0047f300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047f/0047f2d0.md#insn-0047f300)
- 新版 `0047f2f8`（命令位置の公開資料なし） · `0047f300`（命令位置の公開資料なし）

~~~diff
- 0047f2f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef8:8"]]
- 0047f2f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047f2f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
+ 0047f2f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0047f2f8 bytes 087d47f9
+ 0047f2f8 bytes 08a547f9
- 0047f300 ["COPY", "register:4098:8", ["register:4000:8"]]
- 0047f300 bytes f30300aa
+ 0047f300 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 0047f300 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2919e90c030578c0a588966c3ffb40fa"></a>

### [`0047f40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047f/0047f40c.md) → [`0047f40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f40c.md) _ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdbf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf80.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7e0.md)
- 新版 呼出元 1件 [`00bdbfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfd0.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047f438",
      "incomplete_value": true,
      "site": "0047f438",
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
      "definition_site": "0047f438",
      "incomplete_value": true,
      "site": "0047f438",
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
      "0047f428",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "0047f438",
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
      "0047f428",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "0047f438",
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

- 旧版 [`0047f428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047f/0047f40c.md#insn-0047f428) · [`0047f430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047f/0047f40c.md#insn-0047f430)
- 新版 `0047f428`（命令位置の公開資料なし） · `0047f430`（命令位置の公開資料なし）

~~~diff
- 0047f428 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef8:8"]]
- 0047f428 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0047f428 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
+ 0047f428 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0047f428 bytes 087d47f9
+ 0047f428 bytes 08a547f9
- 0047f430 ["COPY", "register:4040:8", ["register:4000:8"]]
- 0047f430 bytes e80300aa
+ 0047f430 ["COPY", "register:4040:8", ["register:4000:8"]]
+ 0047f430 bytes e80300aa
~~~


<a id="compare-21c5cdaa81a7c14bc37f6935d394ea21"></a>

### [`0047f4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047f/0047f4d8.md) → [`0047f4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047f/0047f4d8.md) _ZN5Botan4OIDS6lookupERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdb7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7e0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 63.69% / 新版 63.69%

CFGの説明率　旧版 60.71% / 新版 60.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 163件, `store_value` 10件, `unresolved_branch_alignment` 43件, `unresolved_call_alignment` 178件

アドレスに依存する影響 `call_argument_candidate` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047f694",
      "incomplete_value": true,
      "site": "0047f6a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:41e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047f694",
      "incomplete_value": true,
      "site": "0047f6a4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:393:8"
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
      "definition_site": "0047f6a8",
      "incomplete_value": true,
      "site": "0047f6a8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "0047f6a8",
      "incomplete_value": true,
      "site": "0047f6a8",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 9,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0047f6fc",
      "incomplete_value": true,
      "site": "0047f70c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:593:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0047f6fc",
      "incomplete_value": true,
      "site": "0047f70c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:4f9:8"
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
      "0047f624",
      "PARAM",
      [
        "storage",
        "00298d72",
        null,
        "string"
      ]
    ],
    [
      "0047f66c",
      "PARAM",
      [
        "storage",
        "00296975",
        null,
        "string"
      ]
    ],
    [
      "0047f694",
      "READ",
      [
        "storage",
        "002a4393",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0047f624",
      "PARAM",
      [
        "storage",
        "00298ce5",
        null,
        "string"
      ]
    ],
    [
      "0047f66c",
      "PARAM",
      [
        "storage",
        "002968e8",
        null,
        "string"
      ]
    ],
    [
      "0047f694",
      "READ",
      [
        "storage",
        "002a441e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0047fb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047f/0047f4d8.md#insn-0047fb50) · [`0047fcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047f/0047f4d8.md#insn-0047fcf0) · [`0047fd24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047f/0047f4d8.md#insn-0047fd24)

~~~diff
- 0047fb50 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 0047fb50 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0047fb50 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0047fb50 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0047fb50 bytes 20010036
- 0047fcf0 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 0047fcf0 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0047fcf0 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0047fcf0 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0047fcf0 bytes 20010036
- 0047fd24 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 0047fd24 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 0047fd24 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 0047fd24 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 0047fd24 bytes 20010036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a837afe2cee59d0c70586a0c4e512a1"></a>

### [`00482154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482154.md) → [`00482154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482154.md) _ZN5Botan19AlgorithmIdentifierC1ERKNS_3OIDENS0_15Encoding_OptionE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdc880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc880.md) · 呼出先 5件 [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdc8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc8d0.md) · 呼出先 5件 [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.66% / 新版 89.66%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048219c",
      "incomplete_value": true,
      "site": "0048219c",
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
      "definition_site": "0048219c",
      "incomplete_value": true,
      "site": "0048219c",
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
      "definition_site": "0048219c",
      "incomplete_value": true,
      "site": "0048219c",
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
      "definition_site": "0048219c",
      "incomplete_value": true,
      "site": "0048219c",
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
      "0048217c",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "00482188",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "0048219c",
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
      "0048217c",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "00482188",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "0048219c",
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

- 旧版 [`0048217c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482154.md#insn-0048217c) · [`00482184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482154.md#insn-00482184)
- 新版 `0048217c`（命令位置の公開資料なし） · `00482184`（命令位置の公開資料なし）

~~~diff
- 0048217c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef8:8"]]
- 0048217c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048217c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
+ 0048217c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0048217c bytes 087d47f9
+ 0048217c bytes 08a547f9
- 00482184 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00482184 bytes f30300aa
+ 00482184 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00482184 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d43401c8ff99b5ccda5b50cb4ae923fb"></a>

### [`00482240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482240.md) → [`00482240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482240.md) _ZN5Botan19AlgorithmIdentifierC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS0_15Encoding_OptionE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf70.md) · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7e0.md)
- 新版 呼出元 1件 [`00bdbfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbfc0.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md)

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
      "definition_site": "0048225c",
      "incomplete_value": true,
      "site": "00482260",
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
      "definition_site": "0048225c",
      "incomplete_value": true,
      "site": "00482260",
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
      "00482258",
      "READ",
      [
        "storage",
        "00c1aef8",
        null,
        "pointer"
      ]
    ],
    [
      "00482260",
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
      "00482258",
      "READ",
      [
        "storage",
        "00c1af48",
        null,
        "pointer"
      ]
    ],
    [
      "00482260",
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

- 旧版 [`00482258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482240.md#insn-00482258)
- 新版 `00482258`（命令位置の公開資料なし）

~~~diff
- 00482258 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ef8:8"]]
- 00482258 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00482258 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
+ 00482258 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00482258 bytes 087d47f9
+ 00482258 bytes 08a547f9
~~~


<a id="compare-9ded2ed109f8c6b754146d0c4a005a3b"></a>

### [`00482500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482500.md) → [`00482500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482500.md) _ZN5Botan11DER_Encoder10start_consENS_8ASN1_TagES1_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb810.md) · 呼出先 6件 [`005200b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/005200b0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb840.md)
- 新版 呼出元 1件 [`00bdb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb860.md) · 呼出先 6件 [`005200b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/005200b0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb890.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.75% / 新版 97.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004825e8",
      "incomplete_value": true,
      "site": "004825e8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004825e8",
      "incomplete_value": true,
      "site": "004825e8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00482628",
      "incomplete_value": true,
      "site": "00482628",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00482628",
      "incomplete_value": true,
      "site": "00482628",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004825d8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00482618",
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
      "004825d8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00482618",
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

- 旧版 [`004825d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482500.md#insn-004825d8) · [`00482618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482500.md#insn-00482618)
- 新版 `004825d8`（命令位置の公開資料なし） · `00482618`（命令位置の公開資料なし）

~~~diff
- 004825d8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 004825d8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004825d8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 004825d8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004825d8 bytes e99643f9
+ 004825d8 bytes e9be43f9
- 00482618 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 00482618 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00482618 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 00482618 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00482618 bytes 299543f9
+ 00482618 bytes 29bd43f9
~~~


<a id="compare-92826cf5f8d1454c8b10287f173b3a0d"></a>

### [`004826c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004826c4.md) → [`004826c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004826c4.md) _ZN5Botan11DER_Encoder8end_consEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb830.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md)
- 新版 呼出元 1件 [`00bdb880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb880.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.94% / 新版 97.94%

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
      "definition_site": "004827b4",
      "incomplete_value": true,
      "site": "004827b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004827b4",
      "incomplete_value": true,
      "site": "004827b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004827fc",
      "incomplete_value": false,
      "site": "00482804",
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
            "const:46a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004827fc",
      "incomplete_value": false,
      "site": "00482804",
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
            "const:3df:8"
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
      "definition_site": "00482834",
      "incomplete_value": true,
      "site": "00482840",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00482834",
      "incomplete_value": true,
      "site": "00482840",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
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
      "004827a4",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004827fc",
      "PARAM",
      [
        "storage",
        "002a53df",
        null,
        "string"
      ]
    ],
    [
      "00482834",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004827a4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004827fc",
      "PARAM",
      [
        "storage",
        "002a546a",
        null,
        "string"
      ]
    ],
    [
      "00482834",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004827a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004826c4.md#insn-004827a4) · [`004827fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004826c4.md#insn-004827fc) · [`00482834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004826c4.md#insn-00482834)
- 新版 `004827a4`（命令位置の公開資料なし） · `004827fc`（命令位置の公開資料なし） · `00482834`（命令位置の公開資料なし）

~~~diff
- 004827a4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 004827a4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004827a4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 004827a4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004827a4 bytes 299543f9
+ 004827a4 bytes 29bd43f9
- 004827fc ["COPY", "tmp:0:8", ["const:3df:8"]]
- 004827fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004827fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004827fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004827fc ["COPY", "tmp:0:8", ["const:46a:8"]]
+ 004827fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004827fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004827fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004827fc bytes 217c0f91
+ 004827fc bytes 21a81191
- 00482834 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 00482834 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00482834 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 00482834 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00482834 bytes 218447f9
+ 00482834 bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bde702f3f568925a58b086b3f029a789"></a>

### [`00482c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482c08.md) → [`00482c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482c08.md) _ZN5Botan11BER_Decoder8end_consEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb870.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdb8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8c0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00482cc0",
      "incomplete_value": true,
      "site": "00482ccc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00482cc0",
      "incomplete_value": true,
      "site": "00482ccc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
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
      "definition_site": "00482ce8",
      "incomplete_value": false,
      "site": "00482cf0",
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
            "const:3bc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00482ce8",
      "incomplete_value": false,
      "site": "00482cf0",
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
            "const:322:8"
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
      "definition_site": "00482d24",
      "incomplete_value": true,
      "site": "00482d30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00482d24",
      "incomplete_value": true,
      "site": "00482d30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00482cc0",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "00482cc0",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00482ce8",
      "PARAM",
      [
        "storage",
        "002a9322",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00482cc0",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "00482cc0",
      "PARAM",
      [
        "storage",
        "00be93d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00482ce8",
      "PARAM",
      [
        "storage",
        "002a93bc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00482cc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482c08.md#insn-00482cc0) · [`00482ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482c08.md#insn-00482ce8) · [`00482d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482c08.md#insn-00482d24)
- 新版 `00482cc0`（命令位置の公開資料なし） · `00482ce8`（命令位置の公開資料なし） · `00482d24`（命令位置の公開資料なし）

~~~diff
- 00482cc0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 00482cc0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00482cc0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 00482cc0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00482cc0 bytes 218447f9
+ 00482cc0 bytes 21ac47f9
- 00482ce8 ["COPY", "tmp:0:8", ["const:322:8"]]
- 00482ce8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00482ce8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00482ce8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00482ce8 ["COPY", "tmp:0:8", ["const:3bc:8"]]
+ 00482ce8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00482ce8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00482ce8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00482ce8 bytes 21880c91
+ 00482ce8 bytes 21f00e91
- 00482d24 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
- 00482d24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00482d24 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
+ 00482d24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00482d24 bytes 218847f9
+ 00482d24 bytes 21b047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0370c17f771d6c1c353e2cc5ffd9b7d4"></a>

### [`00482df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482df4.md) → [`00482df4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482df4.md) _ZN5Botan9AttributeC1ERKNS_3OIDERKNSt6__ndk16vectorIhNS4_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 4件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00482e3c",
      "incomplete_value": true,
      "site": "00482e3c",
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
      "definition_site": "00482e3c",
      "incomplete_value": true,
      "site": "00482e3c",
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
      "definition_site": "00482e3c",
      "incomplete_value": true,
      "site": "00482e3c",
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
      "definition_site": "00482e3c",
      "incomplete_value": true,
      "site": "00482e3c",
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
      "00482e1c",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ],
    [
      "00482e28",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "00482e3c",
      "DATA",
      [
        "storage",
        "00be91c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00482e1c",
      "READ",
      [
        "storage",
        "00c1af68",
        null,
        "pointer"
      ]
    ],
    [
      "00482e28",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "00482e3c",
      "DATA",
      [
        "storage",
        "00be9218",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00482e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482df4.md#insn-00482e1c) · [`00482e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482df4.md#insn-00482e24)
- 新版 `00482e1c`（命令位置の公開資料なし） · `00482e24`（命令位置の公開資料なし）

~~~diff
- 00482e1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f18:8"]]
- 00482e1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00482e1c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f68:8"]]
+ 00482e1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00482e1c bytes 088d47f9
+ 00482e1c bytes 08b547f9
- 00482e24 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00482e24 bytes f30300aa
+ 00482e24 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00482e24 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cb35538ae97f70f108af6845e39b04d"></a>

### [`00482f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482f18.md) → [`00482f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482f18.md) _ZN5Botan9AttributeC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERKNS1_6vectorIhNS5_IhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdd0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd0c0.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7e0.md)
- 新版 呼出元 1件 [`00bdd110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd110.md) · 呼出先 4件 [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb830.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00482f44",
      "incomplete_value": true,
      "site": "00482f44",
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
      "definition_site": "00482f44",
      "incomplete_value": true,
      "site": "00482f44",
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
      "00482f34",
      "READ",
      [
        "storage",
        "00c1af18",
        null,
        "pointer"
      ]
    ],
    [
      "00482f44",
      "DATA",
      [
        "storage",
        "00be91c8",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00482f34",
      "READ",
      [
        "storage",
        "00c1af68",
        null,
        "pointer"
      ]
    ],
    [
      "00482f44",
      "DATA",
      [
        "storage",
        "00be9218",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00482f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482f18.md#insn-00482f34) · [`00482f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482f18.md#insn-00482f3c)
- 新版 `00482f34`（命令位置の公開資料なし） · `00482f3c`（命令位置の公開資料なし）

~~~diff
- 00482f34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f18:8"]]
- 00482f34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00482f34 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f68:8"]]
+ 00482f34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00482f34 bytes 088d47f9
+ 00482f34 bytes 08b547f9
- 00482f3c ["COPY", "register:4040:8", ["register:4000:8"]]
- 00482f3c bytes e80300aa
+ 00482f3c ["COPY", "register:4040:8", ["register:4000:8"]]
+ 00482f3c bytes e80300aa
~~~


<a id="compare-699fc87d40542a56a5902b736206fc93"></a>

### [`004830c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/004830c8.md) → [`004830c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004830c8.md) _ZN5Botan9Attribute11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`004eb16c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004eb/004eb16c.md) · 呼出先 6件 [`00482aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482aa8.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb860.md) [`00bdb870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb870.md)
- 新版 呼出元 1件 [`004eb16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004eb/004eb16c.md) · 呼出先 6件 [`00482aa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482aa8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8b0.md) [`00bdb8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8c0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.59% / 新版 94.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00483178",
      "incomplete_value": true,
      "site": "00483178",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00483178",
      "incomplete_value": true,
      "site": "00483178",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 7,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004831bc",
      "incomplete_value": true,
      "site": "004831bc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004831bc",
      "incomplete_value": true,
      "site": "004831bc",
      "value": [
        "LOAD",
        "8",
        [
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
      "00483168",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004831ac",
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
      "00483168",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004831ac",
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

- 旧版 [`00483168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/004830c8.md#insn-00483168) · [`004831ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/004830c8.md#insn-004831ac)
- 新版 `00483168`（命令位置の公開資料なし） · `004831ac`（命令位置の公開資料なし）

~~~diff
- 00483168 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00483168 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00483168 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 00483168 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00483168 bytes a99643f9
+ 00483168 bytes a9be43f9
- 004831ac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 004831ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004831ac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 004831ac ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004831ac bytes a99643f9
+ 004831ac bytes a9be43f9
~~~


<a id="compare-7ae7ed022f4af53bd93ed71572eb8ea2"></a>

### [`0048322c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/0048322c.md) → [`0048322c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/0048322c.md) _ZN5Botan18asn1_tag_to_stringENS_8ASN1_TagE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8c0.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb2c0.md)
- 新版 呼出元 1件 [`00bdb910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb910.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb310.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00483348",
      "incomplete_value": true,
      "site": "00483348",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:84e:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483348",
      "incomplete_value": true,
      "site": "00483348",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8db:8"
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
      "definition_site": "00483420",
      "incomplete_value": true,
      "site": "00483420",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:24a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483420",
      "incomplete_value": true,
      "site": "00483420",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1bf:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00483368",
      "incomplete_value": false,
      "site": "00483374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:156:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483368",
      "incomplete_value": false,
      "site": "00483374",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:bc:8"
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
      "00483334",
      "READ",
      [
        "storage",
        "002968db",
        null,
        "string"
      ]
    ],
    [
      "00483368",
      "PARAM",
      [
        "storage",
        "002a80bc",
        null,
        null
      ]
    ],
    [
      "00483394",
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
      "00483334",
      "READ",
      [
        "storage",
        "0029684e",
        null,
        "string"
      ]
    ],
    [
      "00483368",
      "PARAM",
      [
        "storage",
        "002a8156",
        null,
        null
      ]
    ],
    [
      "00483394",
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

- 旧版 [`00483290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/0048322c.md#insn-00483290) · [`004832a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/0048322c.md#insn-004832a0) · [`004832c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/0048322c.md#insn-004832c4)
- 新版 `00483290`（命令位置の公開資料なし） · `004832a0`（命令位置の公開資料なし） · `004832c4`（命令位置の公開資料なし）

~~~diff
- 00483290 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00483290 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 00483290 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 00483290 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 00483290 ["COPY", "tmp:0:8", ["const:3a5:8"]]
+ 00483290 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 00483290 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 00483290 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 00483290 bytes 4a2d0c91
+ 00483290 bytes 4a950e91
- 004832a0 ["COPY", "tmp:0:8", ["const:333:8"]]
- 004832a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004832a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004832a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004832a0 ["COPY", "tmp:0:8", ["const:3be:8"]]
+ 004832a0 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004832a0 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004832a0 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004832a0 bytes 4acd0c91
+ 004832a0 bytes 4af90e91
- 004832c4 ["COPY", "tmp:0:8", ["const:60d:8"]]
- 004832c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
- 004832c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
- 004832c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
+ 004832c4 ["COPY", "tmp:0:8", ["const:6a7:8"]]
+ 004832c4 ["INT_CARRY", "register:105:1", ["register:4050:8", "tmp:0:8"]]
+ 004832c4 ["INT_SCARRY", "register:106:1", ["register:4050:8", "tmp:0:8"]]
+ 004832c4 ["INT_ADD", "tmp:1:8", ["register:4050:8", "tmp:0:8"]]
- 004832c4 bytes 4a351891
+ 004832c4 bytes 4a9d1a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6410392f958dd370b57dc88e7204170"></a>

### [`00483554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483554.md) → [`00483554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483554.md) _ZN5Botan18BER_Decoding_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bdb8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8d0.md) [`00bdb9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb9b0.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8e0.md)
- 新版 呼出元 2件 [`00bdb920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb920.md) [`00bdba00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba00.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.08% / 新版 96.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004835b8",
      "incomplete_value": true,
      "site": "004835bc",
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
      "definition_site": "004835b8",
      "incomplete_value": true,
      "site": "004835bc",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004835d8",
      "incomplete_value": true,
      "site": "004835dc",
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
      "definition_site": "004835d8",
      "incomplete_value": true,
      "site": "004835dc",
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
      "definition_site": "004835f4",
      "incomplete_value": true,
      "site": "004835f8",
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
      "definition_site": "004835f4",
      "incomplete_value": true,
      "site": "004835f8",
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
      "00483570",
      "PARAM",
      [
        "storage",
        "002937ef",
        null,
        "string"
      ]
    ],
    [
      "0048359c",
      "PARAM",
      [
        "storage",
        "002968ca",
        null,
        "string"
      ]
    ],
    [
      "004835b0",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00483570",
      "PARAM",
      [
        "storage",
        "00293762",
        null,
        "string"
      ]
    ],
    [
      "0048359c",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "004835b0",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00483570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483554.md#insn-00483570) · [`0048359c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483554.md#insn-0048359c) · [`004835b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483554.md#insn-004835b0)
- 新版 `00483570`（命令位置の公開資料なし） · `0048359c`（命令位置の公開資料なし） · `004835b0`（命令位置の公開資料なし）

~~~diff
- 00483570 ["COPY", "tmp:0:8", ["const:7ef:8"]]
- 00483570 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00483570 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00483570 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00483570 ["COPY", "tmp:0:8", ["const:762:8"]]
+ 00483570 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00483570 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00483570 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00483570 bytes 00bc1f91
+ 00483570 bytes 00881d91
- 0048359c ["COPY", "tmp:0:8", ["const:8ca:8"]]
- 0048359c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048359c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048359c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048359c ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 0048359c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048359c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048359c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048359c bytes 21282391
+ 0048359c bytes 21f42091
- 004835b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
- 004835b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004835b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
+ 004835b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004835b0 bytes 089147f9
+ 004835b0 bytes 08b947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d25e303869b12304289259d4101d5b08"></a>

### [`00483664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483664.md) → [`00483664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483664.md) _ZN5Botan14Decoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb8b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8b0.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8e0.md)
- 新版 呼出元 1件 [`00bdb900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb900.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb930.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.37% / 新版 97.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004836b4",
      "incomplete_value": true,
      "site": "004836b8",
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
      "definition_site": "004836b4",
      "incomplete_value": true,
      "site": "004836b8",
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004836d0",
      "incomplete_value": true,
      "site": "004836d4",
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
      "definition_site": "004836d0",
      "incomplete_value": true,
      "site": "004836d4",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00483698",
      "incomplete_value": false,
      "site": "004836a4",
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
            "const:83d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00483698",
      "incomplete_value": false,
      "site": "004836a4",
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
            "const:8ca:8"
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
      "00483698",
      "PARAM",
      [
        "storage",
        "002968ca",
        null,
        "string"
      ]
    ],
    [
      "004836ac",
      "READ",
      [
        "storage",
        "00c1af20",
        null,
        "pointer"
      ]
    ],
    [
      "004836b8",
      "DATA",
      [
        "storage",
        "00bea440",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00483698",
      "PARAM",
      [
        "storage",
        "0029683d",
        null,
        "string"
      ]
    ],
    [
      "004836ac",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ],
    [
      "004836b8",
      "DATA",
      [
        "storage",
        "00bea490",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00483698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483664.md#insn-00483698) · [`004836ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483664.md#insn-004836ac) · [`004836cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483664.md#insn-004836cc)
- 新版 `00483698`（命令位置の公開資料なし） · `004836ac`（命令位置の公開資料なし） · `004836cc`（命令位置の公開資料なし）

~~~diff
- 00483698 ["COPY", "tmp:0:8", ["const:8ca:8"]]
- 00483698 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00483698 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00483698 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00483698 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 00483698 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00483698 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00483698 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00483698 bytes 21282391
+ 00483698 bytes 21f42091
- 004836ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f20:8"]]
- 004836ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004836ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
+ 004836ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004836ac bytes 089147f9
+ 004836ac bytes 08b947f9
- 004836cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f28:8"]]
- 004836cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 004836cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f78:8"]]
+ 004836cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 004836cc bytes 089547f9
+ 004836cc bytes 08bd47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ad8d12c9bac0ca424301abb5ff48a42"></a>

### [`004839c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/004839c4.md) → [`004839c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/004839c4.md) _ZN5Botan11BER_Bad_TagC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagESA_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb9a0.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00bdb9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9f0.md) · 呼出先 9件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.38% / 新版 99.38%

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
      "definition_site": "00483ba4",
      "incomplete_value": true,
      "site": "00483ba8",
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
      "definition_site": "00483ba4",
      "incomplete_value": true,
      "site": "00483ba8",
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
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00483aec",
      "incomplete_value": false,
      "site": "00483af4",
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
      "definition_site": "00483aec",
      "incomplete_value": false,
      "site": "00483af4",
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
      "00483aec",
      "PARAM",
      [
        "storage",
        "002958ca",
        null,
        null
      ]
    ],
    [
      "00483ba0",
      "READ",
      [
        "storage",
        "00c1af38",
        null,
        "pointer"
      ]
    ],
    [
      "00483ba8",
      "DATA",
      [
        "storage",
        "00be9220",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00483aec",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ],
    [
      "00483ba0",
      "READ",
      [
        "storage",
        "00c1af88",
        null,
        "pointer"
      ]
    ],
    [
      "00483ba8",
      "DATA",
      [
        "storage",
        "00be9270",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00483aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/004839c4.md#insn-00483aec) · [`00483ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/004839c4.md#insn-00483ba0)
- 新版 `00483aec`（命令位置の公開資料なし） · `00483ba0`（命令位置の公開資料なし）

~~~diff
- 00483aec ["COPY", "tmp:0:8", ["const:8ca:8"]]
- 00483aec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00483aec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00483aec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00483aec ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 00483aec ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00483aec ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00483aec ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00483aec bytes 21282391
+ 00483aec bytes 21f42091
- 00483ba0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f38:8"]]
- 00483ba0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00483ba0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f88:8"]]
+ 00483ba0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00483ba0 bytes 089d47f9
+ 00483ba0 bytes 08c547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e10e597808a0796f8f1a839901a5c34"></a>

### [`004840c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/004840c4.md) → [`004840c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/004840c4.md) FUN_004840c4

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 3件 [`004c9e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004c9/004c9e38.md) [`004ce004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ce/004ce004.md) [`004ea660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004ea/004ea660.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 3件 [`004c9e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004c9/004c9e38.md) [`004ce004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ce/004ce004.md) [`004ea660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004ea/004ea660.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.00% / 新版 92.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00484164",
      "incomplete_value": false,
      "site": "0048416c",
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
            "const:311:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00484164",
      "incomplete_value": false,
      "site": "0048416c",
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
            "const:286:8"
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
      "definition_site": "004841a0",
      "incomplete_value": true,
      "site": "004841ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004841a0",
      "incomplete_value": true,
      "site": "004841ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004841c8",
      "incomplete_value": false,
      "site": "004841e8",
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
            "const:85b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004841c8",
      "incomplete_value": false,
      "site": "004841e8",
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
            "const:8e8:8"
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
      "00484164",
      "PARAM",
      [
        "storage",
        "002a4286",
        null,
        "string"
      ]
    ],
    [
      "004841a0",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004841a0",
      "PARAM",
      [
        "storage",
        "00be9250",
        "_ZTIN5Botan15Stream_IO_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00484164",
      "PARAM",
      [
        "storage",
        "002a4311",
        null,
        "string"
      ]
    ],
    [
      "004841a0",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "004841a0",
      "PARAM",
      [
        "storage",
        "00be92a0",
        "_ZTIN5Botan15Stream_IO_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00484164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/004840c4.md#insn-00484164) · [`004841a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/004840c4.md#insn-004841a0) · [`004841c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/004840c4.md#insn-004841c8)
- 新版 `00484164`（命令位置の公開資料なし） · `004841a0`（命令位置の公開資料なし） · `004841c8`（命令位置の公開資料なし）

~~~diff
- 00484164 ["COPY", "tmp:0:8", ["const:286:8"]]
- 00484164 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00484164 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00484164 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00484164 ["COPY", "tmp:0:8", ["const:311:8"]]
+ 00484164 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00484164 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00484164 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00484164 bytes 21180a91
+ 00484164 bytes 21440c91
- 004841a0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
- 004841a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004841a0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f90:8"]]
+ 004841a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004841a0 bytes 21a047f9
+ 004841a0 bytes 21c847f9
- 004841c8 ["COPY", "tmp:0:8", ["const:8e8:8"]]
- 004841c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004841c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004841c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004841c8 ["COPY", "tmp:0:8", ["const:85b:8"]]
+ 004841c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004841c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004841c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004841c8 bytes 00a02391
+ 004841c8 bytes 006c2191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0247f783f0c8819ca98563f0f301ec7f"></a>

### [`00484260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484260.md) → [`00484260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484260.md) _ZN5Botan17assertion_failureEPKcS1_S1_S1_i

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md) · 呼出先 11件 [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md) · 呼出先 11件 [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 86.27% / 新版 86.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004842a8",
      "incomplete_value": true,
      "site": "004842b8",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004842a8",
      "incomplete_value": true,
      "site": "004842b8",
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
            "const:40:8"
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
      "definition_site": "004842b0",
      "incomplete_value": true,
      "site": "004842c4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004842b0",
      "incomplete_value": true,
      "site": "004842c4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004842cc",
      "incomplete_value": true,
      "site": "004842cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:28:8"
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
      "definition_site": "004842cc",
      "incomplete_value": true,
      "site": "004842cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:28:8"
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
      "00484294",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "00484298",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "004842b0",
      "READ",
      [
        "storage",
        "00c13410",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00484294",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "00484298",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "004842b0",
      "READ",
      [
        "storage",
        "00c13460",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00484294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484260.md#insn-00484294) · [`00484298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484260.md#insn-00484298) · [`00484310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484260.md#insn-00484310)
- 新版 `00484294`（命令位置の公開資料なし） · `00484298`（命令位置の公開資料なし） · `00484310`（命令位置の公開資料なし）

~~~diff
- 00484294 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:e48:8"]]
- 00484294 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00484294 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:e98:8"]]
+ 00484294 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
- 00484294 bytes 9c2747f9
+ 00484294 bytes 9c4f47f9
- 00484298 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:d78:8"]]
- 00484298 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00484298 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:dc8:8"]]
+ 00484298 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 00484298 bytes 7bbf46f9
+ 00484298 bytes 7be746f9
- 00484310 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:d80:8"]]
- 00484310 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00484310 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:dd0:8"]]
+ 00484310 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
- 00484310 bytes 9cc346f9
+ 00484310 bytes 9ceb46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84fa4f379dfd51d990a624aa1152c851"></a>

### [`00484570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484570.md) → [`00484570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484570.md) _ZN5Botan3OIDC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7f0.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdb840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb840.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.06% / 新版 95.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048459c",
      "incomplete_value": true,
      "site": "004845a4",
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
      "definition_site": "0048459c",
      "incomplete_value": true,
      "site": "004845a4",
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
      "definition_site": "0048468c",
      "incomplete_value": true,
      "site": "00484694",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048468c",
      "incomplete_value": true,
      "site": "00484694",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f50:8"
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
      "00484594",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "004845a4",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0048468c",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00484594",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "004845a4",
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ],
    [
      "0048468c",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00484594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484570.md#insn-00484594) · [`0048468c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484570.md#insn-0048468c)
- 新版 `00484594`（命令位置の公開資料なし） · `0048468c`（命令位置の公開資料なし）

~~~diff
- 00484594 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
- 00484594 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00484594 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 00484594 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00484594 bytes 088147f9
+ 00484594 bytes 08a947f9
- 0048468c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f50:8"]]
- 0048468c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048468c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa0:8"]]
+ 0048468c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048468c bytes 21a847f9
+ 0048468c bytes 21d047f9
~~~


<a id="compare-19ecdfe6f19dc3de7bcc2157fa4d08ea"></a>

### [`00484754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484754.md) → [`00484754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484754.md) _ZN5Botan14parse_asn1_oidERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb930.md) · 呼出先 12件 [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdb980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb980.md) · 呼出先 12件 [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.17% / 新版 99.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00484a44",
      "incomplete_value": true,
      "site": "00484a4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00484a44",
      "incomplete_value": true,
      "site": "00484a4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f50:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00484ad0",
      "incomplete_value": true,
      "site": "00484ad8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fa0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00484ad0",
      "incomplete_value": true,
      "site": "00484ad8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f50:8"
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
      "00484a44",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "00484a44",
      "PARAM",
      [
        "storage",
        "00be92c8",
        "_ZTIN5Botan11Invalid_OIDE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00484ad0",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00484a44",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ],
    [
      "00484a44",
      "PARAM",
      [
        "storage",
        "00be9318",
        "_ZTIN5Botan11Invalid_OIDE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00484ad0",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00484a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484754.md#insn-00484a44) · [`00484ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484754.md#insn-00484ad0)
- 新版 `00484a44`（命令位置の公開資料なし） · `00484ad0`（命令位置の公開資料なし）

~~~diff
- 00484a44 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f50:8"]]
- 00484a44 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00484a44 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa0:8"]]
+ 00484a44 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00484a44 bytes 21a847f9
+ 00484a44 bytes 21d047f9
- 00484ad0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f50:8"]]
- 00484ad0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00484ad0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa0:8"]]
+ 00484ad0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00484ad0 bytes 21a847f9
+ 00484ad0 bytes 21d047f9
~~~


<a id="compare-fbb0772ee5e4e7a53c2471673843fc28"></a>

### [`00484e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484e1c.md) → [`00484e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484e1c.md) _ZN5BotanplERKNS_3OIDEj

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.48% / 新版 93.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00484e4c",
      "incomplete_value": true,
      "site": "00484e58",
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
      "definition_site": "00484e4c",
      "incomplete_value": true,
      "site": "00484e58",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00484e3c",
      "READ",
      [
        "storage",
        "00c1af00",
        null,
        "pointer"
      ]
    ],
    [
      "00484e58",
      "DATA",
      [
        "storage",
        "00be9278",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00484e3c",
      "READ",
      [
        "storage",
        "00c1af50",
        null,
        "pointer"
      ]
    ],
    [
      "00484e58",
      "DATA",
      [
        "storage",
        "00be92c8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00484e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484e1c.md#insn-00484e3c)
- 新版 `00484e3c`（命令位置の公開資料なし）

~~~diff
- 00484e3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
- 00484e3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00484e3c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
+ 00484e3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00484e3c bytes 088147f9
+ 00484e3c bytes 08a947f9
~~~


<a id="compare-1e119df40547da90cf4850a39e45ea5b"></a>

### [`00484f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484f50.md) → [`00484f50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00484/00484f50.md) _ZNK5Botan3OID11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 13件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.95% / 新版 97.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004852b4",
      "incomplete_value": false,
      "site": "004852cc",
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
            "const:6f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004852b4",
      "incomplete_value": false,
      "site": "004852cc",
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
            "const:780:8"
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
      "definition_site": "004852bc",
      "incomplete_value": false,
      "site": "004852cc",
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
            "const:3b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004852bc",
      "incomplete_value": false,
      "site": "004852cc",
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
            "const:316:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004852c4",
      "incomplete_value": false,
      "site": "004852cc",
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
            "const:3d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004852c4",
      "incomplete_value": false,
      "site": "004852cc",
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
    "ordinal": 9,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004852b4",
      "PARAM",
      [
        "storage",
        "00292780",
        null,
        "string"
      ]
    ],
    [
      "004852bc",
      "PARAM",
      [
        "storage",
        "002a9316",
        null,
        "string"
      ]
    ],
    [
      "004852c4",
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004852b4",
      "PARAM",
      [
        "storage",
        "002926f3",
        null,
        "string"
      ]
    ],
    [
      "004852bc",
      "PARAM",
      [
        "storage",
        "002a93b0",
        null,
        "string"
      ]
    ],
    [
      "004852c4",
      "PARAM",
      [
        "storage",
        "0029c3d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004852b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484f50.md#insn-004852b4) · [`004852bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484f50.md#insn-004852bc) · [`004852c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00484/00484f50.md#insn-004852c0)
- 新版 `004852b4`（命令位置の公開資料なし） · `004852bc`（命令位置の公開資料なし） · `004852c0`（命令位置の公開資料なし）

~~~diff
- 004852b4 ["COPY", "tmp:0:8", ["const:780:8"]]
- 004852b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004852b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004852b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004852b4 ["COPY", "tmp:0:8", ["const:6f3:8"]]
+ 004852b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004852b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004852b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004852b4 bytes 21001e91
+ 004852b4 bytes 21cc1b91
- 004852bc ["COPY", "tmp:0:8", ["const:316:8"]]
- 004852bc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 004852bc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 004852bc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 004852bc ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 004852bc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 004852bc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 004852bc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 004852bc bytes 42580c91
+ 004852bc bytes 42c00e91
- 004852c0 ["COPY", "register:4018:8", ["const:291000:8"]]
+ 004852c0 ["COPY", "register:4018:8", ["const:29c000:8"]]
- 004852c0 bytes 63f0ff90
+ 004852c0 bytes a3f0fff0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c7e3551c5803b978d68dca1ff960088"></a>

### [`004854c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/004854c8.md) → [`004854c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/004854c8.md) _ZN5Botan3OID11decode_fromERNS_11BER_DecoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 16件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00512c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512c94.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 16件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00512c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512c94.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call, call_argument_candidate, call_count, call_target, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 97.50% / 新版 97.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004857b8",
      "incomplete_value": true,
      "site": "004857b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004857b8",
      "incomplete_value": true,
      "site": "004857b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0048584c"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00485898",
      "incomplete_value": false,
      "site": "004858a0",
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
            "const:44a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00485898",
      "incomplete_value": false,
      "site": "004858a0",
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
            "const:3bf:8"
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
      "004857a8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "unmatched:0048583c",
      "PARAM",
      [
        "storage",
        "00512990",
        null,
        null
      ]
    ],
    [
      "unmatched:00485840",
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
      "004857a8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00485840",
      "PARAM",
      [
        "storage",
        "00be9300",
        "_ZTIN5Botan14Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00485898",
      "PARAM",
      [
        "storage",
        "002a544a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048584c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/004854c8.md#insn-0048584c) · [`004858e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/004854c8.md#insn-004858e4)
- 新版 `0048584c`（命令位置の公開資料なし） · `004858e4`（命令位置の公開資料なし）

~~~diff
- 0048584c ["INT_ADD", "register:40f0:8", ["const:48584c:8", "const:4:8"]]
- 0048584c ["CALL", null, ["callee:00bdb0c0:8"]]
- 0048584c bytes 09561d94
- 004858e4 ["INT_ADD", "register:40f0:8", ["const:4858e4:8", "const:4:8"]]
- 004858e4 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 0048584c ["INT_ADD", "register:40f0:8", ["const:48584c:8", "const:4:8"]]
+ 0048584c ["CALL", null, ["callee:00bdb0c0:8"]]
- 004858e4 bytes e3551d94
+ 0048584c bytes 1d561d94
+ 004858e4 ["INT_ADD", "register:40f0:8", ["const:4858e4:8", "const:4:8"]]
+ 004858e4 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 004858e4 bytes f7551d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64fb685f0523e7ab6c9b07266098e1da"></a>

### [`00485a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485a10.md) → [`00485a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485a10.md) _ZN5Botan11BER_Decoder15get_next_objectEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdb880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb880.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048cb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cb40.md) [`0048cd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cd38.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md)
- 新版 呼出元 1件 [`00bdb8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8d0.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048cb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cb40.md) [`0048cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.80% / 新版 96.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00485b60",
      "incomplete_value": false,
      "site": "00485b68",
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
            "const:384:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00485b60",
      "incomplete_value": false,
      "site": "00485b68",
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
            "const:2f9:8"
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
      "definition_site": "00485b98",
      "incomplete_value": true,
      "site": "00485ba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00485b98",
      "incomplete_value": true,
      "site": "00485ba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f68:8"
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
      "definition_site": "00485bbc",
      "incomplete_value": false,
      "site": "00485bc4",
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
            "const:384:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00485bbc",
      "incomplete_value": false,
      "site": "00485bc4",
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
            "const:2f9:8"
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
      "00485b60",
      "PARAM",
      [
        "storage",
        "002a12f9",
        null,
        "string"
      ]
    ],
    [
      "00485b98",
      "READ",
      [
        "storage",
        "00c1af68",
        null,
        "pointer"
      ]
    ],
    [
      "00485b98",
      "PARAM",
      [
        "storage",
        "00be92f8",
        "_ZTIN5Botan18BER_Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00485b60",
      "PARAM",
      [
        "storage",
        "002a1384",
        null,
        "string"
      ]
    ],
    [
      "00485b98",
      "READ",
      [
        "storage",
        "00c1afb8",
        null,
        "pointer"
      ]
    ],
    [
      "00485b98",
      "PARAM",
      [
        "storage",
        "00be9348",
        "_ZTIN5Botan18BER_Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00485b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485a10.md#insn-00485b60) · [`00485b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485a10.md#insn-00485b98) · [`00485bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485a10.md#insn-00485bbc)
- 新版 `00485b60`（命令位置の公開資料なし） · `00485b98`（命令位置の公開資料なし） · `00485bbc`（命令位置の公開資料なし）

~~~diff
- 00485b60 ["COPY", "tmp:0:8", ["const:2f9:8"]]
- 00485b60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00485b60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00485b60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00485b60 ["COPY", "tmp:0:8", ["const:384:8"]]
+ 00485b60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00485b60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00485b60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00485b60 bytes 21e40b91
+ 00485b60 bytes 21100e91
- 00485b98 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f68:8"]]
- 00485b98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00485b98 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fb8:8"]]
+ 00485b98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00485b98 bytes 21b447f9
+ 00485b98 bytes 21dc47f9
- 00485bbc ["COPY", "tmp:0:8", ["const:2f9:8"]]
- 00485bbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00485bbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00485bbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00485bbc ["COPY", "tmp:0:8", ["const:384:8"]]
+ 00485bbc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00485bbc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00485bbc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00485bbc bytes 21e40b91
+ 00485bbc bytes 21100e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c91fcd9b4c3dfcda5184c63ed627035"></a>

### [`00485cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485cc4.md) → [`00485cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485cc4.md) _ZNK5Botan14ASN1_Formatter5printEPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb100.md) [`00bdb110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb110.md) [`00bdb120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb120.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb150.md) [`00bdb160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb160.md) [`00bdb170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb170.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 87.64% / 新版 87.64%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00485d0c",
      "incomplete_value": true,
      "site": "00485d1c",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00485d0c",
      "incomplete_value": true,
      "site": "00485d1c",
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
            "const:40:8"
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
      "definition_site": "00485d14",
      "incomplete_value": true,
      "site": "00485d24",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00485d14",
      "incomplete_value": true,
      "site": "00485d24",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 15,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00485d2c",
      "incomplete_value": true,
      "site": "00485d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:8:8"
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
      "definition_site": "00485d2c",
      "incomplete_value": true,
      "site": "00485d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "INT_ADD",
            "8",
            [
              "INT_SUB",
              [
                "leaf",
                "const:8:8"
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
    "ordinal": 16,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00485cf8",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "00485cfc",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00485d14",
      "READ",
      [
        "storage",
        "00c13410",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00485cf8",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "00485cfc",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00485d14",
      "READ",
      [
        "storage",
        "00c13460",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00485cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485cc4.md#insn-00485cf8) · [`00485cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485cc4.md#insn-00485cfc) · [`00485d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485cc4.md#insn-00485d70)
- 新版 `00485cf8`（命令位置の公開資料なし） · `00485cfc`（命令位置の公開資料なし） · `00485d70`（命令位置の公開資料なし）

~~~diff
- 00485cf8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:e48:8"]]
- 00485cf8 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00485cf8 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:e98:8"]]
+ 00485cf8 ["LOAD", "register:40d8:8", ["const:1b1:8", "tmp:0:8"]]
- 00485cf8 bytes 7b2747f9
+ 00485cf8 bytes 7b4f47f9
- 00485cfc ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:d78:8"]]
- 00485cfc ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00485cfc ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:dc8:8"]]
+ 00485cfc ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00485cfc bytes 5abf46f9
+ 00485cfc bytes 5ae746f9
- 00485d70 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d80:8"]]
- 00485d70 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00485d70 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:dd0:8"]]
+ 00485d70 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 00485d70 bytes f7c246f9
+ 00485d70 bytes f7ea46f9
~~~


<a id="compare-56bc6bbc3b592ab862a083aea6c085c3"></a>

### [`00485f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485f54.md) → [`00485f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485f54.md) _ZNK5Botan14ASN1_Formatter6decodeERNSt6__ndk113basic_ostreamIcNS1_11char_traitsIcEEEERNS_11BER_DecoderEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdb9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb9d0.md) · 呼出先 36件 [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00483ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512ca8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdba20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba20.md) · 呼出先 36件 [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00483ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483ed8.md) [`00512ca8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512ca8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.13% / 新版 94.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 8件, `store_value` 11件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00486034",
      "incomplete_value": true,
      "site": "00486048",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00486034",
      "incomplete_value": true,
      "site": "00486048",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 19,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00486058",
      "incomplete_value": true,
      "site": "00486058",
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
      "definition_site": "00486058",
      "incomplete_value": true,
      "site": "00486058",
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
    "ordinal": 21,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00486058",
      "incomplete_value": true,
      "site": "00486058",
      "value": [
        "LOAD",
        "8",
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
                "const:10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00486058",
      "incomplete_value": true,
      "site": "00486058",
      "value": [
        "LOAD",
        "8",
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
                "const:10:8"
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
      "00485fc0",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048601c",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "00486034",
      "READ",
      [
        "storage",
        "00c13408",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "00485fc0",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048601c",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "00486034",
      "READ",
      [
        "storage",
        "00c13458",
        "_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00485fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485f54.md#insn-00485fc0) · [`0048601c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485f54.md#insn-0048601c) · [`00486054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485f54.md#insn-00486054)
- 新版 `00485fc0`（命令位置の公開資料なし） · `0048601c`（命令位置の公開資料なし）

~~~diff
- 00485fc0 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:728:8"]]
- 00485fc0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00485fc0 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:778:8"]]
+ 00485fc0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00485fc0 bytes 899743f9
+ 00485fc0 bytes 89bf43f9
- 0048601c ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:d78:8"]]
- 0048601c ["LOAD", "register:4058:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048601c ["INT_ADD", "tmp:0:8", ["register:4058:8", "const:dc8:8"]]
+ 0048601c ["LOAD", "register:4058:8", ["const:1b1:8", "tmp:0:8"]]
- 0048601c bytes 6bbd46f9
+ 0048601c bytes 6be546f9
- 00486054 ["COPY", "register:4040:8", ["const:c1a000:8"]]
- 00486054 bytes a83c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b85fa6f516d13644a1b1a67bf6ded181"></a>

### [`004873a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00487/004873a4.md) → [`004873a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00487/004873a4.md) _ZN5Botan4OIDS6lookupERKNS_3OIDE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdba10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba10.md) · 呼出先 5件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb960.md)
- 新版 呼出元 1件 [`00bdba60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba60.md) · 呼出先 5件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9b0.md)

変更の種類 call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, operands_and_dependencies, operation_sequence, store_value, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 69.24% / 新版 69.24%

CFGの説明率　旧版 69.07% / 新版 69.07%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 111件, `store_value` 1件, `unresolved_branch_alignment` 33件, `unresolved_call_alignment` 33件

アドレスに依存する影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048760c",
      "incomplete_value": true,
      "site": "0048760c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048760c",
      "incomplete_value": true,
      "site": "0048760c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:935:8"
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
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00487734"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00487800"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004874e4",
      "PARAM",
      [
        "storage",
        "0029693f",
        null,
        null
      ]
    ],
    [
      "00487594",
      "PARAM",
      [
        "storage",
        "0029c3ed",
        null,
        "string"
      ]
    ],
    [
      "004875a8",
      "PARAM",
      [
        "storage",
        "00297a5d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004874e4",
      "PARAM",
      [
        "storage",
        "002968b2",
        null,
        null
      ]
    ],
    [
      "00487594",
      "PARAM",
      [
        "storage",
        "0029c478",
        null,
        "string"
      ]
    ],
    [
      "004875a8",
      "PARAM",
      [
        "storage",
        "002979d0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00487734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00487/004873a4.md#insn-00487734) · [`00487800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00487/004873a4.md#insn-00487800)
- 新版 `00487734`（命令位置の公開資料なし）

~~~diff
- 00487734 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00487734 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00487734 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00487734 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00487734 bytes c0000037
+ 00487734 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
+ 00487734 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00487734 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00487734 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00487734 bytes c0000037
- 00487800 ["INT_RIGHT", "tmp:0:4", ["register:4000:4", "const:0:4"]]
- 00487800 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00487800 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00487800 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00487800 bytes 80000036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7acbc5c377b394d987ee97953af6fa53"></a>

### [`00488e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00488/00488e94.md) → [`00488e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00488/00488e94.md) _ZN5Botan11BER_Decoder6decodeERNS_6BigIntENS_8ASN1_TagES3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdba20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba20.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb880.md) [`00bdb890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb890.md) [`00bdba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md)
- 新版 呼出元 1件 [`00bdba70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba70.md) · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8d0.md) [`00bdb8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8e0.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.27% / 新版 96.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00488fc4",
      "incomplete_value": true,
      "site": "00488fc4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00488fc4",
      "incomplete_value": true,
      "site": "00488fc4",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048904c",
      "incomplete_value": true,
      "site": "0048904c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048904c",
      "incomplete_value": true,
      "site": "0048904c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048907c",
      "incomplete_value": true,
      "site": "0048907c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048907c",
      "incomplete_value": true,
      "site": "0048907c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00488fb4",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048903c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048906c",
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
      "00488fb4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048903c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048906c",
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

- 旧版 [`00488fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00488/00488e94.md#insn-00488fb4) · [`0048903c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00488/00488e94.md#insn-0048903c) · [`0048906c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00488/00488e94.md#insn-0048906c)
- 新版 `00488fb4`（命令位置の公開資料なし） · `0048903c`（命令位置の公開資料なし） · `0048906c`（命令位置の公開資料なし）

~~~diff
- 00488fb4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 00488fb4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00488fb4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 00488fb4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00488fb4 bytes c99643f9
+ 00488fb4 bytes c9be43f9
- 0048903c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 0048903c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048903c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 0048903c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048903c bytes c99643f9
+ 0048903c bytes c9be43f9
- 0048906c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 0048906c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048906c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 0048906c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048906c bytes c99643f9
+ 0048906c bytes c9be43f9
~~~


<a id="compare-b5c23b53d8d02735a506398580f8b620"></a>

### [`0048930c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/0048930c.md) → [`0048930c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/0048930c.md) _ZNK5Botan9X509_Time15readable_stringEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdba70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba70.md) · 呼出先 17件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md)
- 新版 呼出元 1件 [`00bdbac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbac0.md) · 呼出先 17件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0042e9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042e/0042e9d8.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件

アドレスに依存する影響 `store_destination` 1件, `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004894c8",
      "incomplete_value": true,
      "site": "004894d0",
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
      "definition_site": "004894c8",
      "incomplete_value": true,
      "site": "004894d0",
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004894d8",
      "incomplete_value": true,
      "site": "004894d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
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
      "definition_site": "004894d8",
      "incomplete_value": true,
      "site": "004894d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
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
    "ordinal": 17,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004894d8",
      "incomplete_value": true,
      "site": "004894d8",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004894d8",
      "incomplete_value": true,
      "site": "004894d8",
      "value": [
        "LOAD",
        "8",
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
                "const:40:8"
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
      "0048937c",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "0048937c",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004893c8",
      "PARAM",
      [
        "storage",
        "002958ca",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0048937c",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "0048937c",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "004893c8",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048937c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/0048930c.md#insn-0048937c) · [`004893c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/0048930c.md#insn-004893c8) · [`004893f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/0048930c.md#insn-004893f4)
- 新版 `0048937c`（命令位置の公開資料なし） · `004893c8`（命令位置の公開資料なし） · `004893f4`（命令位置の公開資料なし）

~~~diff
- 0048937c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 0048937c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048937c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 0048937c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048937c bytes 21f846f9
+ 0048937c bytes 212047f9
- 004893c8 ["COPY", "tmp:0:8", ["const:8ca:8"]]
- 004893c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004893c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004893c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004893c8 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 004893c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004893c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004893c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004893c8 bytes 21282391
+ 004893c8 bytes 21f42091
- 004893f4 ["COPY", "tmp:0:8", ["const:8ca:8"]]
- 004893f4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004893f4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004893f4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004893f4 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 004893f4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004893f4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004893f4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004893f4 bytes 21282391
+ 004893f4 bytes 21f42091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb007d86d45eacfd914f0f8264df9378"></a>

### [`00489628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/00489628.md) → [`00489628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489628.md) _ZNK5Botan19ASN1_Pretty_Printer6formatENS_8ASN1_TagES1_mmRKNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 18件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`004365f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00436/004365f8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`004365f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00436/004365f8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 93.12% / 新版 93.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `store_destination` 2件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "004896dc",
      "incomplete_value": true,
      "site": "004896e0",
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
            "const:40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004896dc",
      "incomplete_value": true,
      "site": "004896e0",
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
            "const:40:8"
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
      "definition_site": "004896d8",
      "incomplete_value": true,
      "site": "004896e4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "004896d8",
      "incomplete_value": true,
      "site": "004896e4",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 20,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "004896ec",
      "incomplete_value": true,
      "site": "004896ec",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:b0:8"
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
      "definition_site": "004896ec",
      "incomplete_value": true,
      "site": "004896ec",
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
                "register:8:8"
              ],
              [
                "leaf",
                "const:b0:8"
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
    "ordinal": 21,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004896c4",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "004896c8",
      "READ",
      [
        "storage",
        "00c1ad78",
        null,
        "pointer"
      ]
    ],
    [
      "004896d8",
      "READ",
      [
        "storage",
        "00c13410",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ],
  "added": [
    [
      "004896c4",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "004896c8",
      "READ",
      [
        "storage",
        "00c1adc8",
        null,
        "pointer"
      ]
    ],
    [
      "004896d8",
      "READ",
      [
        "storage",
        "00c13460",
        null,
        "pointer __((offset(0x18)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004896c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/00489628.md#insn-004896c4) · [`004896c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/00489628.md#insn-004896c8) · [`00489734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/00489628.md#insn-00489734)
- 新版 `004896c4`（命令位置の公開資料なし） · `004896c8`（命令位置の公開資料なし） · `00489734`（命令位置の公開資料なし）

~~~diff
- 004896c4 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:e48:8"]]
- 004896c4 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
+ 004896c4 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:e98:8"]]
+ 004896c4 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
- 004896c4 bytes 9c2747f9
+ 004896c4 bytes 9c4f47f9
- 004896c8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d78:8"]]
- 004896c8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004896c8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dc8:8"]]
+ 004896c8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004896c8 bytes 29bd46f9
+ 004896c8 bytes 29e546f9
- 00489734 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:d80:8"]]
- 00489734 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00489734 ["INT_ADD", "tmp:0:8", ["register:40e0:8", "const:dd0:8"]]
+ 00489734 ["LOAD", "register:40e0:8", ["const:1b1:8", "tmp:0:8"]]
- 00489734 bytes 9cc346f9
+ 00489734 bytes 9ceb46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62ca8a4fb07664ebbddd1504b1446caa"></a>

### [`00489f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/00489f78.md) → [`00489f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489f78.md) _ZN5Botan11ASN1_StringC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcac0.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0048a0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a0a0.md)
- 新版 呼出元 1件 [`00bdcb10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcb10.md) · 呼出先 2件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0048a0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a0a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00489fa4",
      "incomplete_value": true,
      "site": "00489fa8",
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
      "definition_site": "00489fa4",
      "incomplete_value": true,
      "site": "00489fa8",
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
      "00489f94",
      "READ",
      [
        "storage",
        "00c1af78",
        null,
        "pointer"
      ]
    ],
    [
      "00489fa8",
      "DATA",
      [
        "storage",
        "00be9338",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00489f94",
      "READ",
      [
        "storage",
        "00c1afc8",
        null,
        "pointer"
      ]
    ],
    [
      "00489fa8",
      "DATA",
      [
        "storage",
        "00be9388",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00489f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/00489f78.md#insn-00489f94)
- 新版 `00489f94`（命令位置の公開資料なし）

~~~diff
- 00489f94 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f78:8"]]
- 00489f94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00489f94 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc8:8"]]
+ 00489f94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00489f94 bytes 08bd47f9
+ 00489f94 bytes 08e547f9
~~~


<a id="compare-0b212fc0b8876e8cf93a7f9c056bdd25"></a>

### [`0048a0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a0a0.md) → [`0048a0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a0a0.md) FUN_0048a0a0

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00489f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/00489f78.md) [`0048a89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a89c.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0c0.md)
- 新版 呼出元 2件 [`00489f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/00489f78.md) [`0048a89c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a89c.md) · 呼出先 7件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb110.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.72% / 新版 96.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048a128",
      "incomplete_value": false,
      "site": "0048a134",
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
            "const:60a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048a128",
      "incomplete_value": false,
      "site": "0048a134",
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
            "const:57f:8"
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
      "definition_site": "0048a180",
      "incomplete_value": true,
      "site": "0048a18c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048a180",
      "incomplete_value": true,
      "site": "0048a18c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0048a128",
      "PARAM",
      [
        "storage",
        "0029e57f",
        null,
        "string"
      ]
    ],
    [
      "0048a180",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "0048a180",
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
      "0048a128",
      "PARAM",
      [
        "storage",
        "0029e60a",
        null,
        "string"
      ]
    ],
    [
      "0048a180",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "0048a180",
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

- 旧版 [`0048a128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a0a0.md#insn-0048a128) · [`0048a180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a0a0.md#insn-0048a180)
- 新版 `0048a128`（命令位置の公開資料なし） · `0048a180`（命令位置の公開資料なし）

~~~diff
- 0048a128 ["COPY", "tmp:0:8", ["const:57f:8"]]
- 0048a128 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0048a128 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0048a128 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0048a128 ["COPY", "tmp:0:8", ["const:60a:8"]]
+ 0048a128 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0048a128 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0048a128 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0048a128 bytes 42fc1591
+ 0048a128 bytes 42281891
- 0048a180 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 0048a180 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048a180 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 0048a180 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048a180 bytes 217847f9
+ 0048a180 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7fa29f21f9b2c0895e276c284c6c8b6a"></a>

### [`0048a208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a208.md) → [`0048a208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a208.md) _ZN5Botan11ASN1_StringC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdba50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba50.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)
- 新版 呼出元 1件 [`00bdbaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbaa0.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.48% / 新版 93.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048a22c",
      "incomplete_value": true,
      "site": "0048a230",
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
      "definition_site": "0048a22c",
      "incomplete_value": true,
      "site": "0048a230",
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
      "0048a220",
      "READ",
      [
        "storage",
        "00c1af78",
        null,
        "pointer"
      ]
    ],
    [
      "0048a230",
      "DATA",
      [
        "storage",
        "00be9338",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0048a220",
      "READ",
      [
        "storage",
        "00c1afc8",
        null,
        "pointer"
      ]
    ],
    [
      "0048a230",
      "DATA",
      [
        "storage",
        "00be9388",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048a220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a208.md#insn-0048a220)
- 新版 `0048a220`（命令位置の公開資料なし）

~~~diff
- 0048a220 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f78:8"]]
- 0048a220 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048a220 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc8:8"]]
+ 0048a220 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0048a220 bytes 08bd47f9
+ 0048a220 bytes 08e547f9
~~~


<a id="compare-24665aad5cd1fa18791a9eff63fd445a"></a>

### [`0048a2e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a2e8.md) → [`0048a2e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a2e8.md) _ZN5Botan14utf8_to_latin1ERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbad0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdbb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb20.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.21% / 新版 96.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048a3fc",
      "incomplete_value": false,
      "site": "0048a404",
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
            "const:82b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048a3fc",
      "incomplete_value": false,
      "site": "0048a404",
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
            "const:8b8:8"
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
      "definition_site": "0048a434",
      "incomplete_value": true,
      "site": "0048a440",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048a434",
      "incomplete_value": true,
      "site": "0048a440",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048a490",
      "incomplete_value": true,
      "site": "0048a49c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048a490",
      "incomplete_value": true,
      "site": "0048a49c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0048a3fc",
      "PARAM",
      [
        "storage",
        "002928b8",
        null,
        "string"
      ]
    ],
    [
      "0048a434",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ],
    [
      "0048a434",
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
      "0048a3fc",
      "PARAM",
      [
        "storage",
        "0029282b",
        null,
        "string"
      ]
    ],
    [
      "0048a434",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ],
    [
      "0048a434",
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

- 旧版 [`0048a3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a2e8.md#insn-0048a3fc) · [`0048a434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a2e8.md#insn-0048a434) · [`0048a490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a2e8.md#insn-0048a490)
- 新版 `0048a3fc`（命令位置の公開資料なし） · `0048a434`（命令位置の公開資料なし） · `0048a490`（命令位置の公開資料なし）

~~~diff
- 0048a3fc ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 0048a3fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048a3fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048a3fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048a3fc ["COPY", "tmp:0:8", ["const:82b:8"]]
+ 0048a3fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048a3fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048a3fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048a3fc bytes 21e02291
+ 0048a3fc bytes 21ac2091
- 0048a434 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
- 0048a434 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048a434 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
+ 0048a434 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048a434 bytes 218847f9
+ 0048a434 bytes 21b047f9
- 0048a490 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
- 0048a490 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048a490 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
+ 0048a490 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048a490 bytes 218847f9
+ 0048a490 bytes 21b047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1f0333b296ff569c9ce043d4aa5b30d"></a>

### [`0048a5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a5d8.md) → [`0048a5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a5d8.md) _ZN5Botan11DER_Encoder10add_objectENS_8ASN1_TagES1_PKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb980.md) · 呼出先 8件 [`0048f37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f37c.md) [`0048f6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f6e8.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00bdb9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9d0.md) · 呼出先 8件 [`0048f37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f37c.md) [`0048f6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f6e8.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.18% / 新版 96.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048a698",
      "incomplete_value": true,
      "site": "0048a698",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048a698",
      "incomplete_value": true,
      "site": "0048a698",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048a720",
      "incomplete_value": true,
      "site": "0048a720",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048a720",
      "incomplete_value": true,
      "site": "0048a720",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048a80c",
      "incomplete_value": true,
      "site": "0048a80c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048a80c",
      "incomplete_value": true,
      "site": "0048a80c",
      "value": [
        "LOAD",
        "8",
        [
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
      "0048a688",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048a710",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048a7fc",
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
      "0048a688",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048a710",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048a7fc",
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

- 旧版 [`0048a688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a5d8.md#insn-0048a688) · [`0048a710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a5d8.md#insn-0048a710) · [`0048a7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a5d8.md#insn-0048a7fc)
- 新版 `0048a688`（命令位置の公開資料なし） · `0048a710`（命令位置の公開資料なし） · `0048a7fc`（命令位置の公開資料なし）

~~~diff
- 0048a688 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 0048a688 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048a688 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 0048a688 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048a688 bytes 099743f9
+ 0048a688 bytes 09bf43f9
- 0048a710 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 0048a710 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048a710 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 0048a710 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048a710 bytes 099743f9
+ 0048a710 bytes 09bf43f9
- 0048a7fc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 0048a7fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048a7fc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 0048a7fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048a7fc bytes 099743f9
+ 0048a7fc bytes 09bf43f9
~~~


<a id="compare-a6107b27c7d27ca7c08a289dc88408d1"></a>

### [`0048aad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048aad4.md) → [`0048aad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048aad4.md) _ZN5Botan12ucs2_to_utf8EPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbae0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004d6338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6338.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdbb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb30.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004d6338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6338.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048ab60",
      "incomplete_value": false,
      "site": "0048ab68",
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
            "const:5df:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048ab60",
      "incomplete_value": false,
      "site": "0048ab68",
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
            "const:545:8"
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
      "definition_site": "0048ab98",
      "incomplete_value": true,
      "site": "0048aba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048ab98",
      "incomplete_value": true,
      "site": "0048aba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0048ab60",
      "PARAM",
      [
        "storage",
        "002a9545",
        null,
        "string"
      ]
    ],
    [
      "0048ab98",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ],
    [
      "0048ab98",
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
      "0048ab60",
      "PARAM",
      [
        "storage",
        "002a95df",
        null,
        "string"
      ]
    ],
    [
      "0048ab98",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ],
    [
      "0048ab98",
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

- 旧版 [`0048ab60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048aad4.md#insn-0048ab60) · [`0048ab98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048aad4.md#insn-0048ab98)
- 新版 `0048ab60`（命令位置の公開資料なし） · `0048ab98`（命令位置の公開資料なし）

~~~diff
- 0048ab60 ["COPY", "tmp:0:8", ["const:545:8"]]
- 0048ab60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048ab60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048ab60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048ab60 ["COPY", "tmp:0:8", ["const:5df:8"]]
+ 0048ab60 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048ab60 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048ab60 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048ab60 bytes 21141591
+ 0048ab60 bytes 217c1791
- 0048ab98 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
- 0048ab98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048ab98 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
+ 0048ab98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048ab98 bytes 218847f9
+ 0048ab98 bytes 21b047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-899f2c73d189bf7adeec878391ef7d16"></a>

### [`0048ac0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048ac0c.md) → [`0048ac0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ac0c.md) _ZN5Botan12ucs4_to_utf8EPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbaf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbaf0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004d6338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6338.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdbb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb40.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004d6338`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6338.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048ac98",
      "incomplete_value": false,
      "site": "0048aca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:7cf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048ac98",
      "incomplete_value": false,
      "site": "0048aca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:85c:8"
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
      "definition_site": "0048acd0",
      "incomplete_value": true,
      "site": "0048acdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048acd0",
      "incomplete_value": true,
      "site": "0048acdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0048ac98",
      "PARAM",
      [
        "storage",
        "0029485c",
        null,
        "string"
      ]
    ],
    [
      "0048acd0",
      "READ",
      [
        "storage",
        "00c1af10",
        null,
        "pointer"
      ]
    ],
    [
      "0048acd0",
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
      "0048ac98",
      "PARAM",
      [
        "storage",
        "002947cf",
        null,
        "string"
      ]
    ],
    [
      "0048acd0",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ],
    [
      "0048acd0",
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

- 旧版 [`0048ac98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048ac0c.md#insn-0048ac98) · [`0048acd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048ac0c.md#insn-0048acd0)
- 新版 `0048ac98`（命令位置の公開資料なし） · `0048acd0`（命令位置の公開資料なし）

~~~diff
- 0048ac98 ["COPY", "tmp:0:8", ["const:85c:8"]]
- 0048ac98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048ac98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048ac98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048ac98 ["COPY", "tmp:0:8", ["const:7cf:8"]]
+ 0048ac98 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048ac98 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048ac98 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048ac98 bytes 21702191
+ 0048ac98 bytes 213c1f91
- 0048acd0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
- 0048acd0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048acd0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
+ 0048acd0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048acd0 bytes 218847f9
+ 0048acd0 bytes 21b047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38ef06a1a9e31e5a21c1c766ef1ae51a"></a>

### [`0048ad44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048ad44.md) → [`0048ad44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ad44.md) _ZN5Botan9X509_TimeC1ERKNSt6__ndk16chrono10time_pointINS2_12system_clockENS2_8durationIxNS1_5ratioILl1ELl1000000EEEEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdcbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcbd0.md) · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdbb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb00.md) [`00bdbb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb10.md)
- 新版 呼出元 1件 [`00bdcc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc20.md) · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdbb50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb50.md) [`00bdbb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb60.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048ad70",
      "incomplete_value": true,
      "site": "0048ad70",
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
      "definition_site": "0048ad70",
      "incomplete_value": true,
      "site": "0048ad70",
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
      "0048ad60",
      "READ",
      [
        "storage",
        "00c1af70",
        null,
        "pointer"
      ]
    ],
    [
      "0048ad70",
      "DATA",
      [
        "storage",
        "00be9368",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "0048ad60",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ],
    [
      "0048ad70",
      "DATA",
      [
        "storage",
        "00be93b8",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048ad60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048ad44.md#insn-0048ad60)
- 新版 `0048ad60`（命令位置の公開資料なし）

~~~diff
- 0048ad60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f70:8"]]
- 0048ad60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048ad60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc0:8"]]
+ 0048ad60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0048ad60 bytes 08b947f9
+ 0048ad60 bytes 08e147f9
~~~


<a id="compare-2559bc6f1aee2d2078880728e6df1dff"></a>

### [`0048ae8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048ae8c.md) → [`0048ae8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048ae8c.md) _ZN5Botan9X509_Time6set_toERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS_8ASN1_TagE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb20.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051dea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051dea4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00bdbb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb70.md) · 呼出先 16件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051dea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051dea4.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048b40c",
      "incomplete_value": true,
      "site": "0048b410",
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
      "definition_site": "0048b40c",
      "incomplete_value": true,
      "site": "0048b410",
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
    "ordinal": 42,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048af3c",
      "incomplete_value": false,
      "site": "0048af48",
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
            "const:c8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048af3c",
      "incomplete_value": false,
      "site": "0048af48",
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
            "const:d17:8"
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
      "definition_site": "0048af50",
      "incomplete_value": false,
      "site": "0048af58",
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
            "const:87b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048af50",
      "incomplete_value": false,
      "site": "0048af58",
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
            "const:908:8"
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
      "0048af3c",
      "PARAM",
      [
        "storage",
        "00298d17",
        null,
        "string"
      ]
    ],
    [
      "0048af50",
      "PARAM",
      [
        "storage",
        "00296908",
        null,
        null
      ]
    ],
    [
      "0048afa0",
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
      "0048af3c",
      "PARAM",
      [
        "storage",
        "00298c8a",
        null,
        "string"
      ]
    ],
    [
      "0048af50",
      "PARAM",
      [
        "storage",
        "0029687b",
        null,
        null
      ]
    ],
    [
      "0048afa0",
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

- 旧版 [`0048af3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048ae8c.md#insn-0048af3c) · [`0048af50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048ae8c.md#insn-0048af50) · [`0048afa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048ae8c.md#insn-0048afa0)
- 新版 `0048af3c`（命令位置の公開資料なし） · `0048af50`（命令位置の公開資料なし） · `0048afa0`（命令位置の公開資料なし）

~~~diff
- 0048af3c ["COPY", "tmp:0:8", ["const:d17:8"]]
- 0048af3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0048af3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0048af3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0048af3c ["COPY", "tmp:0:8", ["const:c8a:8"]]
+ 0048af3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0048af3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0048af3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0048af3c bytes 005c3491
+ 0048af3c bytes 00283291
- 0048af50 ["COPY", "tmp:0:8", ["const:908:8"]]
- 0048af50 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048af50 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048af50 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048af50 ["COPY", "tmp:0:8", ["const:87b:8"]]
+ 0048af50 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048af50 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048af50 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048af50 bytes 21202491
+ 0048af50 bytes 21ec2191
- 0048afa0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 0048afa0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048afa0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 0048afa0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048afa0 bytes 217847f9
+ 0048afa0 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a5fe976f62512885e06c5653ae2c4ac"></a>

### [`0048b6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048b6ac.md) → [`0048b6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048b6ac.md) _ZNK5Botan9X509_Time11encode_intoERNS_11DER_EncoderE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.77% / 新版 96.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048b758",
      "incomplete_value": false,
      "site": "0048b760",
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
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048b758",
      "incomplete_value": false,
      "site": "0048b760",
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
            "const:7f5:8"
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
      "definition_site": "0048b790",
      "incomplete_value": true,
      "site": "0048b79c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048b790",
      "incomplete_value": true,
      "site": "0048b79c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0048b758",
      "PARAM",
      [
        "storage",
        "002937f5",
        null,
        "string"
      ]
    ],
    [
      "0048b790",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "0048b790",
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
      "0048b758",
      "PARAM",
      [
        "storage",
        "00293768",
        null,
        "string"
      ]
    ],
    [
      "0048b790",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "0048b790",
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

- 旧版 [`0048b758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048b6ac.md#insn-0048b758) · [`0048b790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048b6ac.md#insn-0048b790)
- 新版 `0048b758`（命令位置の公開資料なし） · `0048b790`（命令位置の公開資料なし）

~~~diff
- 0048b758 ["COPY", "tmp:0:8", ["const:7f5:8"]]
- 0048b758 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048b758 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048b758 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048b758 ["COPY", "tmp:0:8", ["const:768:8"]]
+ 0048b758 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048b758 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048b758 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048b758 bytes 21d41f91
+ 0048b758 bytes 21a01d91
- 0048b790 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 0048b790 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048b790 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 0048b790 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048b790 bytes 217847f9
+ 0048b790 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66dce23c7019e1e3dda8ead47bc3ffe1"></a>

### [`0048b804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048b804.md) → [`0048b804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048b804.md) _ZNK5Botan9X509_Time9to_stringEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdbb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb30.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdbb80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb80.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call, call_argument_candidate, call_count, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 92.94% / 新版 92.94%

CFGの説明率　旧版 91.67% / 新版 91.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048b8c4",
      "incomplete_value": false,
      "site": "0048b8cc",
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
            "const:343:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048b8c4",
      "incomplete_value": false,
      "site": "0048b8cc",
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
            "const:2b8:8"
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
      "definition_site": "0048b9b8",
      "incomplete_value": false,
      "site": "0048b9c0",
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
            "const:412:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048b9b8",
      "incomplete_value": false,
      "site": "0048b9c0",
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
            "const:387:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "0048b9fc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0048b8c4",
      "PARAM",
      [
        "storage",
        "002a12b8",
        null,
        null
      ]
    ],
    [
      "0048b964",
      "PARAM",
      [
        "storage",
        "002a7432",
        null,
        null
      ]
    ],
    [
      "0048b9b8",
      "PARAM",
      [
        "storage",
        "0029f387",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0048b8c4",
      "PARAM",
      [
        "storage",
        "002a1343",
        null,
        null
      ]
    ],
    [
      "0048b964",
      "PARAM",
      [
        "storage",
        "002a74cc",
        null,
        null
      ]
    ],
    [
      "0048b9b8",
      "PARAM",
      [
        "storage",
        "0029f412",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048b9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048b804.md#insn-0048b9fc) · [`0048baa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048b804.md#insn-0048baa8)
- 新版 `0048b9fc`（命令位置の公開資料なし） · `0048baa8`（命令位置の公開資料なし）

~~~diff
- 0048b9fc ["INT_ADD", "register:40f0:8", ["const:48b9fc:8", "const:4:8"]]
- 0048b9fc ["CALL", null, ["callee:00bdb0c0:8"]]
- 0048b9fc bytes 9d3d1d94
- 0048baa8 ["INT_ADD", "register:40f0:8", ["const:48baa8:8", "const:4:8"]]
- 0048baa8 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 0048b9fc ["INT_ADD", "register:40f0:8", ["const:48b9fc:8", "const:4:8"]]
+ 0048b9fc ["CALL", null, ["callee:00bdb0c0:8"]]
- 0048baa8 bytes 723d1d94
+ 0048b9fc bytes b13d1d94
+ 0048baa8 ["INT_ADD", "register:40f0:8", ["const:48baa8:8", "const:4:8"]]
+ 0048baa8 ["CALL", null, ["callee:00bdb0c0:8"]]
+ 0048baa8 bytes 863d1d94
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d14e048acc0df838f5dfe345faccaafc"></a>

### [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) → [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) FUN_0048bd8c

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 29件 [`004826c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/004826c4.md) [`00482c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00482/00482c08.md) [`0048930c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00489/0048930c.md) [`0048b804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048b804.md) [`0048be04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048be04.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md)
- 新版 呼出元 29件 [`004826c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/004826c4.md) [`00482c08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00482/00482c08.md) [`0048930c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00489/0048930c.md) [`0048b804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048b804.md) [`0048be04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048be04.md) · 呼出先 1件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md)

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
      "definition_site": "0048bda8",
      "incomplete_value": true,
      "site": "0048bda8",
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
      "definition_site": "0048bda8",
      "incomplete_value": true,
      "site": "0048bda8",
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
      "definition_site": "0048bddc",
      "incomplete_value": true,
      "site": "0048bde0",
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
      "definition_site": "0048bddc",
      "incomplete_value": true,
      "site": "0048bde0",
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
      "0048bda0",
      "READ",
      [
        "storage",
        "00c1af90",
        null,
        "pointer"
      ]
    ],
    [
      "0048bda8",
      "DATA",
      [
        "storage",
        "00bea418",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "0048bdd8",
      "READ",
      [
        "storage",
        "00c1af98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0048bda0",
      "READ",
      [
        "storage",
        "00c1afe0",
        null,
        "pointer"
      ]
    ],
    [
      "0048bda8",
      "DATA",
      [
        "storage",
        "00bea468",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "0048bdd8",
      "READ",
      [
        "storage",
        "00c1afe8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048bda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md#insn-0048bda0) · [`0048bdd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md#insn-0048bdd8)
- 新版 `0048bda0`（命令位置の公開資料なし） · `0048bdd8`（命令位置の公開資料なし）

~~~diff
- 0048bda0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
- 0048bda0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048bda0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe0:8"]]
+ 0048bda0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0048bda0 bytes 08c947f9
+ 0048bda0 bytes 08f147f9
- 0048bdd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f98:8"]]
- 0048bdd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048bdd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fe8:8"]]
+ 0048bdd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0048bdd8 bytes 08cd47f9
+ 0048bdd8 bytes 08f547f9
~~~


<a id="compare-137d63f8040cb3f08819c6291a2d26f1"></a>

### [`0048be04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048be04.md) → [`0048be04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048be04.md) _ZNK5Botan9X509_Time3cmpERKS0_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb40.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdbb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb90.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.40% / 新版 97.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048bee8",
      "incomplete_value": false,
      "site": "0048bef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:160:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048bee8",
      "incomplete_value": false,
      "site": "0048bef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:c6:8"
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
      "definition_site": "0048bf24",
      "incomplete_value": true,
      "site": "0048bf30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048bf24",
      "incomplete_value": true,
      "site": "0048bf30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
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
      "0048bee8",
      "PARAM",
      [
        "storage",
        "002a80c6",
        null,
        "string"
      ]
    ],
    [
      "0048bf24",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "0048bf24",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0048bee8",
      "PARAM",
      [
        "storage",
        "002a8160",
        null,
        "string"
      ]
    ],
    [
      "0048bf24",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "0048bf24",
      "PARAM",
      [
        "storage",
        "00be93d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048bee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048be04.md#insn-0048bee8) · [`0048bf24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048be04.md#insn-0048bf24)
- 新版 `0048bee8`（命令位置の公開資料なし） · `0048bf24`（命令位置の公開資料なし）

~~~diff
- 0048bee8 ["COPY", "tmp:0:8", ["const:c6:8"]]
- 0048bee8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048bee8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048bee8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048bee8 ["COPY", "tmp:0:8", ["const:160:8"]]
+ 0048bee8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048bee8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048bee8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048bee8 bytes 21180391
+ 0048bee8 bytes 21800591
- 0048bf24 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 0048bf24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048bf24 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 0048bf24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048bf24 bytes 218447f9
+ 0048bf24 bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27d9db7ba3742b004d1f040fdc77e077"></a>

### [`0048bf84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bf84.md) → [`0048bf84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bf84.md) _ZN5Botan9to_u32bitERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb950.md) · 呼出先 8件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md)
- 新版 呼出元 1件 [`00bdb9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9a0.md) · 呼出先 8件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.19% / 新版 95.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048c044",
      "incomplete_value": false,
      "site": "0048c050",
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
            "const:626:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048c044",
      "incomplete_value": false,
      "site": "0048c050",
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
            "const:58c:8"
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
      "definition_site": "0048c084",
      "incomplete_value": true,
      "site": "0048c090",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048c084",
      "incomplete_value": true,
      "site": "0048c090",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048c0ac",
      "incomplete_value": false,
      "site": "0048c0b8",
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
            "const:b01:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048c0ac",
      "incomplete_value": false,
      "site": "0048c0b8",
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
            "const:b95:8"
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
      "0048c044",
      "PARAM",
      [
        "storage",
        "002a958c",
        null,
        "string"
      ]
    ],
    [
      "0048c084",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "0048c084",
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
      "0048c044",
      "PARAM",
      [
        "storage",
        "002a9626",
        null,
        "string"
      ]
    ],
    [
      "0048c084",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "0048c084",
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

- 旧版 [`0048c044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bf84.md#insn-0048c044) · [`0048c084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bf84.md#insn-0048c084) · [`0048c0ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bf84.md#insn-0048c0ac)
- 新版 `0048c044`（命令位置の公開資料なし） · `0048c084`（命令位置の公開資料なし） · `0048c0ac`（命令位置の公開資料なし）

~~~diff
- 0048c044 ["COPY", "tmp:0:8", ["const:58c:8"]]
- 0048c044 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0048c044 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0048c044 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0048c044 ["COPY", "tmp:0:8", ["const:626:8"]]
+ 0048c044 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0048c044 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0048c044 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0048c044 bytes 00301691
+ 0048c044 bytes 00981891
- 0048c084 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 0048c084 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048c084 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 0048c084 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048c084 bytes 217847f9
+ 0048c084 bytes 21a047f9
- 0048c0ac ["COPY", "tmp:0:8", ["const:b95:8"]]
- 0048c0ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 0048c0ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 0048c0ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 0048c0ac ["COPY", "tmp:0:8", ["const:b01:8"]]
+ 0048c0ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 0048c0ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 0048c0ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 0048c0ac bytes 00542e91
+ 0048c0ac bytes 00042c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a451420349d00848edd281be87316a1"></a>

### [`0048c2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048c2e0.md) → [`0048c2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c2e0.md) _ZNK5Botan14calendar_point16to_std_timepointEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb60.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdbbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbb0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.61% / 新版 96.61%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048c408",
      "incomplete_value": false,
      "site": "0048c410",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048c408",
      "incomplete_value": false,
      "site": "0048c410",
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
            "const:567:8"
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
      "definition_site": "0048c444",
      "incomplete_value": true,
      "site": "0048c450",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048c444",
      "incomplete_value": true,
      "site": "0048c450",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048c46c",
      "incomplete_value": false,
      "site": "0048c474",
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
            "const:622:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048c46c",
      "incomplete_value": false,
      "site": "0048c474",
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
            "const:597:8"
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
      "0048c408",
      "PARAM",
      [
        "storage",
        "002a0567",
        null,
        "string"
      ]
    ],
    [
      "0048c444",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "0048c444",
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
      "0048c408",
      "PARAM",
      [
        "storage",
        "002a05f2",
        null,
        "string"
      ]
    ],
    [
      "0048c444",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "0048c444",
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

- 旧版 [`0048c408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048c2e0.md#insn-0048c408) · [`0048c444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048c2e0.md#insn-0048c444) · [`0048c46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048c2e0.md#insn-0048c46c)
- 新版 `0048c408`（命令位置の公開資料なし） · `0048c444`（命令位置の公開資料なし） · `0048c46c`（命令位置の公開資料なし）

~~~diff
- 0048c408 ["COPY", "tmp:0:8", ["const:567:8"]]
- 0048c408 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048c408 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048c408 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048c408 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 0048c408 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048c408 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048c408 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048c408 bytes 219c1591
+ 0048c408 bytes 21c81791
- 0048c444 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 0048c444 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048c444 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 0048c444 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048c444 bytes 217847f9
+ 0048c444 bytes 21a047f9
- 0048c46c ["COPY", "tmp:0:8", ["const:597:8"]]
- 0048c46c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048c46c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048c46c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048c46c ["COPY", "tmp:0:8", ["const:622:8"]]
+ 0048c46c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048c46c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048c46c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048c46c bytes 215c1691
+ 0048c46c bytes 21881891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f91e4c18ecc8254ce59438a019a3987"></a>

### [`0048c5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048c5ac.md) → [`0048c5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c5ac.md) _ZNK5Botan10BER_Object11assert_is_aENS_8ASN1_TagES1_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb890.md) · 呼出先 9件 [`00483974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdb8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8e0.md) · 呼出先 9件 [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.49% / 新版 96.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048c640",
      "incomplete_value": false,
      "site": "0048c64c",
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
            "const:364:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048c640",
      "incomplete_value": false,
      "site": "0048c64c",
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
            "const:2d9:8"
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
      "definition_site": "0048c66c",
      "incomplete_value": false,
      "site": "0048c674",
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
      "definition_site": "0048c66c",
      "incomplete_value": false,
      "site": "0048c674",
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
      "definition_site": "0048c6f4",
      "incomplete_value": false,
      "site": "0048c6fc",
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
      "definition_site": "0048c6f4",
      "incomplete_value": false,
      "site": "0048c6fc",
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
      "0048c640",
      "PARAM",
      [
        "storage",
        "002a12d9",
        null,
        "string"
      ]
    ],
    [
      "0048c66c",
      "PARAM",
      [
        "storage",
        "002958ca",
        null,
        null
      ]
    ],
    [
      "0048c6f4",
      "PARAM",
      [
        "storage",
        "002958ca",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "0048c640",
      "PARAM",
      [
        "storage",
        "002a1364",
        null,
        "string"
      ]
    ],
    [
      "0048c66c",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ],
    [
      "0048c6f4",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048c640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048c5ac.md#insn-0048c640) · [`0048c66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048c5ac.md#insn-0048c66c) · [`0048c6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048c5ac.md#insn-0048c6f4)
- 新版 `0048c640`（命令位置の公開資料なし） · `0048c66c`（命令位置の公開資料なし） · `0048c6f4`（命令位置の公開資料なし）

~~~diff
- 0048c640 ["COPY", "tmp:0:8", ["const:2d9:8"]]
- 0048c640 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0048c640 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0048c640 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0048c640 ["COPY", "tmp:0:8", ["const:364:8"]]
+ 0048c640 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0048c640 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0048c640 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0048c640 bytes 42640b91
+ 0048c640 bytes 42900d91
- 0048c66c ["COPY", "tmp:0:8", ["const:8ca:8"]]
- 0048c66c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048c66c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048c66c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048c66c ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 0048c66c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048c66c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048c66c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048c66c bytes 21282391
+ 0048c66c bytes 21f42091
- 0048c6f4 ["COPY", "tmp:0:8", ["const:8ca:8"]]
- 0048c6f4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048c6f4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048c6f4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048c6f4 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 0048c6f4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048c6f4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048c6f4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048c6f4 bytes 21282391
+ 0048c6f4 bytes 21f42091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87617f9c8668454bf1f612566beb750b"></a>

### [`0048c9bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048c9bc.md) → [`0048c9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048c9bc.md) _ZN5Botan11BER_Decoder10verify_endEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb80.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdbbd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbbd0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048ca7c",
      "incomplete_value": true,
      "site": "0048ca88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048ca7c",
      "incomplete_value": true,
      "site": "0048ca88",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
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
      "0048ca7c",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "0048ca7c",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0048ca7c",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "0048ca7c",
      "PARAM",
      [
        "storage",
        "00be93d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048ca7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048c9bc.md#insn-0048ca7c)
- 新版 `0048ca7c`（命令位置の公開資料なし）

~~~diff
- 0048ca7c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 0048ca7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048ca7c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 0048ca7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048ca7c bytes 218447f9
+ 0048ca7c bytes 21ac47f9
~~~


<a id="compare-da47ede3fdb092e8b18f70aca2beabb6"></a>

### [`0048cb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cb40.md) → [`0048cb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cb40.md) FUN_0048cb40

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00485a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485a10.md) [`0048cd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cd38.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 2件 [`00485a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485a10.md) [`0048cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.26% / 新版 96.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048cc48",
      "incomplete_value": false,
      "site": "0048cc50",
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
            "const:b5d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048cc48",
      "incomplete_value": false,
      "site": "0048cc50",
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
            "const:bea:8"
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
      "definition_site": "0048cc80",
      "incomplete_value": true,
      "site": "0048cc8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0048cc80",
      "incomplete_value": true,
      "site": "0048cc8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f68:8"
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
      "definition_site": "0048cca4",
      "incomplete_value": false,
      "site": "0048ccac",
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
            "const:66d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048cca4",
      "incomplete_value": false,
      "site": "0048ccac",
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
            "const:5e2:8"
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
      "0048cc48",
      "PARAM",
      [
        "storage",
        "00291bea",
        null,
        "string"
      ]
    ],
    [
      "0048cc80",
      "READ",
      [
        "storage",
        "00c1af68",
        null,
        "pointer"
      ]
    ],
    [
      "0048cc80",
      "PARAM",
      [
        "storage",
        "00be92f8",
        "_ZTIN5Botan18BER_Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0048cc48",
      "PARAM",
      [
        "storage",
        "00291b5d",
        null,
        "string"
      ]
    ],
    [
      "0048cc80",
      "READ",
      [
        "storage",
        "00c1afb8",
        null,
        "pointer"
      ]
    ],
    [
      "0048cc80",
      "PARAM",
      [
        "storage",
        "00be9348",
        "_ZTIN5Botan18BER_Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048cc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cb40.md#insn-0048cc48) · [`0048cc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cb40.md#insn-0048cc80) · [`0048cca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cb40.md#insn-0048cca4)
- 新版 `0048cc48`（命令位置の公開資料なし） · `0048cc80`（命令位置の公開資料なし） · `0048cca4`（命令位置の公開資料なし）

~~~diff
- 0048cc48 ["COPY", "tmp:0:8", ["const:bea:8"]]
- 0048cc48 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048cc48 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048cc48 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048cc48 ["COPY", "tmp:0:8", ["const:b5d:8"]]
+ 0048cc48 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048cc48 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048cc48 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048cc48 bytes 21a82f91
+ 0048cc48 bytes 21742d91
- 0048cc80 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f68:8"]]
- 0048cc80 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048cc80 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fb8:8"]]
+ 0048cc80 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048cc80 bytes 21b447f9
+ 0048cc80 bytes 21dc47f9
- 0048cca4 ["COPY", "tmp:0:8", ["const:5e2:8"]]
- 0048cca4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048cca4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048cca4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048cca4 ["COPY", "tmp:0:8", ["const:66d:8"]]
+ 0048cca4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048cca4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048cca4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048cca4 bytes 21881791
+ 0048cca4 bytes 21b41991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7b0dfd8c3507e2dc2225402b8d6c0db"></a>

### [`0048cd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cd38.md) → [`0048cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) FUN_0048cd38

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00485a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00485/00485a10.md) [`0048cd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cd38.md) · 呼出先 18件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048cb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cb40.md) [`0048cd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cd38.md) [`004d6b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004d6/004d6b48.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md)
- 新版 呼出元 2件 [`00485a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00485/00485a10.md) [`0048cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) · 呼出先 18件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048cb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cb40.md) [`0048cd38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048c/0048cd38.md) [`004d6b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d6/004d6b48.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 94.16% / 新版 94.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件, `call_target` 3件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048ced8",
      "incomplete_value": true,
      "site": "0048ced8",
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
      "definition_site": "0048ced8",
      "incomplete_value": true,
      "site": "0048ced8",
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
    "ordinal": 29,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048cfc0",
      "incomplete_value": true,
      "site": "0048cfc0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048cfc0",
      "incomplete_value": true,
      "site": "0048cfc0",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048cfec",
      "incomplete_value": true,
      "site": "0048cfec",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048cfec",
      "incomplete_value": true,
      "site": "0048cfec",
      "value": [
        "LOAD",
        "8",
        [
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
      "0048cec8",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ],
    [
      "0048ced8",
      "DATA",
      [
        "storage",
        "00bea378",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0048cf5c",
      "READ",
      [
        "storage",
        "00bea378",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "0048cec8",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "0048ced8",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ],
    [
      "0048cf5c",
      "READ",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048cec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cd38.md#insn-0048cec8) · [`0048cfb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cd38.md#insn-0048cfb0) · [`0048cfdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048c/0048cd38.md#insn-0048cfdc)
- 新版 `0048cec8`（命令位置の公開資料なし） · `0048cfb0`（命令位置の公開資料なし） · `0048cfdc`（命令位置の公開資料なし）

~~~diff
- 0048cec8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
- 0048cec8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048cec8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 0048cec8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0048cec8 bytes 08d147f9
+ 0048cec8 bytes 08f947f9
- 0048cfb0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0048cfb0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048cfb0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0048cfb0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048cfb0 bytes a99643f9
+ 0048cfb0 bytes a9be43f9
- 0048cfdc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0048cfdc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048cfdc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0048cfdc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048cfdc bytes a99643f9
+ 0048cfdc bytes a9be43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d2c4cc169663606a8f5641da028ca0f"></a>

### [`0048d518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d518.md) → [`0048d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d518.md) _ZN5Botan11BER_Decoder9push_backERKNS_10BER_ObjectE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbbc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbbc0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00520980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520980.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdbc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc10.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00520980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520980.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.92% / 新版 96.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048d5cc",
      "incomplete_value": false,
      "site": "0048d5d4",
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
            "const:ae5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048d5cc",
      "incomplete_value": false,
      "site": "0048d5d4",
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
            "const:b72:8"
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
      "definition_site": "0048d608",
      "incomplete_value": true,
      "site": "0048d614",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048d608",
      "incomplete_value": true,
      "site": "0048d614",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
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
      "0048d5cc",
      "PARAM",
      [
        "storage",
        "00299b72",
        null,
        "string"
      ]
    ],
    [
      "0048d608",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "0048d608",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0048d5cc",
      "PARAM",
      [
        "storage",
        "00299ae5",
        null,
        "string"
      ]
    ],
    [
      "0048d608",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "0048d608",
      "PARAM",
      [
        "storage",
        "00be93d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048d5cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d518.md#insn-0048d5cc) · [`0048d608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d518.md#insn-0048d608)
- 新版 `0048d5cc`（命令位置の公開資料なし） · `0048d608`（命令位置の公開資料なし）

~~~diff
- 0048d5cc ["COPY", "tmp:0:8", ["const:b72:8"]]
- 0048d5cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048d5cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048d5cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048d5cc ["COPY", "tmp:0:8", ["const:ae5:8"]]
+ 0048d5cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048d5cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048d5cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048d5cc bytes 21c82d91
+ 0048d5cc bytes 21942b91
- 0048d608 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 0048d608 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048d608 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 0048d608 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048d608 bytes 218447f9
+ 0048d608 bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-62c0aaefd5beaa70a6813bd2c8cdca0e"></a>

### [`0048d684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d684.md) → [`0048d684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d684.md) _ZN5Botan11BER_DecoderC2EPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdb8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb8a0.md) · 呼出先 2件 [`0051d4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d4f0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdb8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8f0.md) · 呼出先 2件 [`0051d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.74% / 新版 89.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0048d6c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0048d6c0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048d6c4",
      "incomplete_value": true,
      "site": "0048d6c8",
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
      "definition_site": "0048d6c4",
      "incomplete_value": true,
      "site": "0048d6c8",
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
      "0048d6bc",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ],
    [
      "0048d6c8",
      "DATA",
      [
        "storage",
        "00bea378",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "0048d6bc",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "0048d6c8",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048d6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d684.md#insn-0048d6c0) · [`0048d6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d684.md#insn-0048d6bc)
- 新版 `0048d6c0`（命令位置の公開資料なし） · `0048d6bc`（命令位置の公開資料なし）

~~~diff
- 0048d6c0 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0048d6c0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0048d6c0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0048d6c0 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0048d6c0 bytes 1f7c01a9
+ 0048d6c0 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 0048d6c0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 0048d6c0 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 0048d6c0 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 0048d6c0 bytes 1f7c01a9
- 0048d6bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
- 0048d6bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048d6bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 0048d6bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0048d6bc bytes 08d147f9
+ 0048d6bc bytes 08f947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-404e28c8c47d1f74d12713ccbaa2d201"></a>

### [`0048d760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d760.md) → [`0048d760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d760.md) _ZN5Botan11BER_DecoderC1ERKNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdb9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb9f0.md) · 呼出先 2件 [`0051d3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d3cc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdba40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba40.md) · 呼出先 2件 [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0048d79c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0048d79c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048d7a0",
      "incomplete_value": true,
      "site": "0048d7a4",
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
      "definition_site": "0048d7a0",
      "incomplete_value": true,
      "site": "0048d7a4",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0048d794",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ],
    [
      "0048d7a4",
      "DATA",
      [
        "storage",
        "00bea378",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "0048d794",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "0048d7a4",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048d79c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d760.md#insn-0048d79c) · [`0048d794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d760.md#insn-0048d794)
- 新版 `0048d79c`（命令位置の公開資料なし） · `0048d794`（命令位置の公開資料なし）

~~~diff
- 0048d79c ["COPY", "tmp:0:8", ["const:0:8"]]
- 0048d79c ["COPY", "tmp:1:8", ["const:0:8"]]
- 0048d79c ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0048d79c ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0048d79c bytes 1f7c01a9
+ 0048d79c ["COPY", "tmp:0:8", ["const:0:8"]]
+ 0048d79c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 0048d79c ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 0048d79c ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 0048d79c bytes 1f7c01a9
- 0048d794 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
- 0048d794 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048d794 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 0048d794 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0048d794 bytes 08d147f9
+ 0048d794 bytes 08f947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-451cda1fc2cea63fdb588e49ebc423a9"></a>

### [`0048d834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d834.md) → [`0048d834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d834.md) _ZN5Botan11BER_DecoderC1ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdb9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb9e0.md) · 呼出先 2件 [`0051d4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d4f0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdba30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba30.md) · 呼出先 2件 [`0051d4f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d4f0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_value, unresolved_store_alignment

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件, `unresolved_store_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0048d870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "0048d870"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0048d874",
      "incomplete_value": true,
      "site": "0048d878",
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
      "definition_site": "0048d874",
      "incomplete_value": true,
      "site": "0048d878",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0048d868",
      "READ",
      [
        "storage",
        "00c1afa0",
        null,
        "pointer"
      ]
    ],
    [
      "0048d878",
      "DATA",
      [
        "storage",
        "00bea378",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "0048d868",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "0048d878",
      "DATA",
      [
        "storage",
        "00bea3c8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048d870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d834.md#insn-0048d870) · [`0048d868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d834.md#insn-0048d868)
- 新版 `0048d870`（命令位置の公開資料なし） · `0048d868`（命令位置の公開資料なし）

~~~diff
- 0048d870 ["COPY", "tmp:0:8", ["const:0:8"]]
- 0048d870 ["COPY", "tmp:1:8", ["const:0:8"]]
- 0048d870 ["COPY", "tmp:2:8", ["tmp:1:8"]]
- 0048d870 ["COPY", "tmp:3:8", ["tmp:0:8"]]
- 0048d870 bytes 1f7c01a9
+ 0048d870 ["COPY", "tmp:0:8", ["const:0:8"]]
+ 0048d870 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 0048d870 ["COPY", "tmp:2:8", ["tmp:1:8"]]
+ 0048d870 ["COPY", "tmp:3:8", ["tmp:0:8"]]
+ 0048d870 bytes 1f7c01a9
- 0048d868 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
- 0048d868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048d868 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ff0:8"]]
+ 0048d868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 0048d868 bytes 08d147f9
+ 0048d868 bytes 08f947f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57c6e2dc83fec522b4015072bf397480"></a>

### [`0048d940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d940.md) → [`0048d940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048d940.md) _ZN5Botan11BER_Decoder11decode_nullEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048d9a4",
      "incomplete_value": true,
      "site": "0048d9a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048d9a4",
      "incomplete_value": true,
      "site": "0048d9a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048da20",
      "incomplete_value": true,
      "site": "0048da2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0048da20",
      "incomplete_value": true,
      "site": "0048da2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f68:8"
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
      "0048d994",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048da20",
      "READ",
      [
        "storage",
        "00c1af68",
        null,
        "pointer"
      ]
    ],
    [
      "0048da20",
      "PARAM",
      [
        "storage",
        "00be92f8",
        "_ZTIN5Botan18BER_Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0048d994",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048da20",
      "READ",
      [
        "storage",
        "00c1afb8",
        null,
        "pointer"
      ]
    ],
    [
      "0048da20",
      "PARAM",
      [
        "storage",
        "00be9348",
        "_ZTIN5Botan18BER_Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048d994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d940.md#insn-0048d994) · [`0048da20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048d940.md#insn-0048da20)
- 新版 `0048d994`（命令位置の公開資料なし） · `0048da20`（命令位置の公開資料なし）

~~~diff
- 0048d994 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:728:8"]]
- 0048d994 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048d994 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:778:8"]]
+ 0048d994 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 0048d994 bytes 4a9543f9
+ 0048d994 bytes 4abd43f9
- 0048da20 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f68:8"]]
- 0048da20 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048da20 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fb8:8"]]
+ 0048da20 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048da20 bytes 21b447f9
+ 0048da20 bytes 21dc47f9
~~~


<a id="compare-c8e98d0a6c36cd03344cf40182415f28"></a>

### [`0048da90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048da90.md) → [`0048da90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048da90.md) _ZN5Botan11BER_Decoder6decodeERbNS_8ASN1_TagES2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdba40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba40.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdba90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba90.md) · 呼出先 10件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.77% / 新版 95.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048db18",
      "incomplete_value": true,
      "site": "0048db18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048db18",
      "incomplete_value": true,
      "site": "0048db18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048db98",
      "incomplete_value": true,
      "site": "0048dba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0048db98",
      "incomplete_value": true,
      "site": "0048dba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f68:8"
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
      "0048db08",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048db98",
      "READ",
      [
        "storage",
        "00c1af68",
        null,
        "pointer"
      ]
    ],
    [
      "0048db98",
      "PARAM",
      [
        "storage",
        "00be92f8",
        "_ZTIN5Botan18BER_Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0048db08",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048db98",
      "READ",
      [
        "storage",
        "00c1afb8",
        null,
        "pointer"
      ]
    ],
    [
      "0048db98",
      "PARAM",
      [
        "storage",
        "00be9348",
        "_ZTIN5Botan18BER_Decoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048db08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048da90.md#insn-0048db08) · [`0048db98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048da90.md#insn-0048db98)
- 新版 `0048db08`（命令位置の公開資料なし） · `0048db98`（命令位置の公開資料なし）

~~~diff
- 0048db08 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0048db08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048db08 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0048db08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048db08 bytes 299543f9
+ 0048db08 bytes 29bd43f9
- 0048db98 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f68:8"]]
- 0048db98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048db98 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fb8:8"]]
+ 0048db98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048db98 bytes 21b447f9
+ 0048db98 bytes 21dc47f9
~~~


<a id="compare-6fdfec0334622d78497931a9f7c228d4"></a>

### [`0048dc14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048dc14.md) → [`0048dc14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048dc14.md) _ZN5Botan11BER_Decoder6decodeERmNS_8ASN1_TagES2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbbd0.md) · 呼出先 9件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdbc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc20.md) · 呼出先 9件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

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
      "definition_site": "0048dd04",
      "incomplete_value": true,
      "site": "0048dd04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048dd04",
      "incomplete_value": true,
      "site": "0048dd04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048dd48",
      "incomplete_value": false,
      "site": "0048dd50",
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
            "const:87d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048dd48",
      "incomplete_value": false,
      "site": "0048dd50",
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
            "const:90a:8"
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
      "definition_site": "0048dd80",
      "incomplete_value": true,
      "site": "0048dd8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0048dd80",
      "incomplete_value": true,
      "site": "0048dd8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f68:8"
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
      "0048dcf4",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048dd48",
      "PARAM",
      [
        "storage",
        "0029690a",
        null,
        "string"
      ]
    ],
    [
      "0048dd80",
      "READ",
      [
        "storage",
        "00c1af68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0048dcf4",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048dd48",
      "PARAM",
      [
        "storage",
        "0029687d",
        null,
        "string"
      ]
    ],
    [
      "0048dd80",
      "READ",
      [
        "storage",
        "00c1afb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048dcf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048dc14.md#insn-0048dcf4) · [`0048dd48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048dc14.md#insn-0048dd48) · [`0048dd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048dc14.md#insn-0048dd80)
- 新版 `0048dcf4`（命令位置の公開資料なし） · `0048dd48`（命令位置の公開資料なし） · `0048dd80`（命令位置の公開資料なし）

~~~diff
- 0048dcf4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0048dcf4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048dcf4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0048dcf4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048dcf4 bytes 299543f9
+ 0048dcf4 bytes 29bd43f9
- 0048dd48 ["COPY", "tmp:0:8", ["const:90a:8"]]
- 0048dd48 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048dd48 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048dd48 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048dd48 ["COPY", "tmp:0:8", ["const:87d:8"]]
+ 0048dd48 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048dd48 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048dd48 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048dd48 bytes 21282491
+ 0048dd48 bytes 21f42191
- 0048dd80 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f68:8"]]
- 0048dd80 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048dd80 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fb8:8"]]
+ 0048dd80 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048dd80 bytes 21b447f9
+ 0048dd80 bytes 21dc47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c80c1bd7714f44a1e905b7f41351ddc"></a>

### [`0048ddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048ddf0.md) → [`0048ddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048ddf0.md) _ZN5Botan11BER_Decoder26decode_octet_string_bigintERNS_6BigIntE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdbbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbbe0.md) [`00bdbbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbbf0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc30.md) [`00bdbc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc40.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048deb8",
      "incomplete_value": true,
      "site": "0048deb8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048deb8",
      "incomplete_value": true,
      "site": "0048deb8",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 2,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048dee4",
      "incomplete_value": true,
      "site": "0048dee4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048dee4",
      "incomplete_value": true,
      "site": "0048dee4",
      "value": [
        "LOAD",
        "8",
        [
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
      "0048dea8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048ded4",
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
      "0048dea8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048ded4",
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

- 旧版 [`0048dea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048ddf0.md#insn-0048dea8) · [`0048ded4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048ddf0.md#insn-0048ded4)
- 新版 `0048dea8`（命令位置の公開資料なし） · `0048ded4`（命令位置の公開資料なし）

~~~diff
- 0048dea8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 0048dea8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048dea8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 0048dea8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048dea8 bytes e99643f9
+ 0048dea8 bytes e9be43f9
- 0048ded4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 0048ded4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048ded4 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 0048ded4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048ded4 bytes e99643f9
+ 0048ded4 bytes e9be43f9
~~~


<a id="compare-4d86efed08bcd9179358712c263c29ef"></a>

### [`0048df5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048df5c.md) → [`0048df5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048df5c.md) _ZN5Botan6BigInt6decodeEPKhmNS0_4BaseE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc00.md) · 呼出先 20件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md)
- 新版 呼出元 1件 [`00bdbc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc50.md) · 呼出先 20件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.79% / 新版 96.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `call_target` 2件

アドレスに依存する影響 `call_target` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048e054",
      "incomplete_value": true,
      "site": "0048e054",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048e054",
      "incomplete_value": true,
      "site": "0048e054",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048e098",
      "incomplete_value": true,
      "site": "0048e098",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048e098",
      "incomplete_value": true,
      "site": "0048e098",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048e19c",
      "incomplete_value": true,
      "site": "0048e19c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048e19c",
      "incomplete_value": true,
      "site": "0048e19c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0048e044",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048e088",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048e18c",
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
      "0048e044",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048e088",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048e18c",
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

- 旧版 [`0048e044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048df5c.md#insn-0048e044) · [`0048e088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048df5c.md#insn-0048e088) · [`0048e18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048df5c.md#insn-0048e18c)
- 新版 `0048e044`（命令位置の公開資料なし） · `0048e088`（命令位置の公開資料なし） · `0048e18c`（命令位置の公開資料なし）

~~~diff
- 0048e044 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:728:8"]]
- 0048e044 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048e044 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:778:8"]]
+ 0048e044 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048e044 bytes 699743f9
+ 0048e044 bytes 69bf43f9
- 0048e088 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:728:8"]]
- 0048e088 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048e088 ["INT_ADD", "tmp:0:8", ["register:40d8:8", "const:778:8"]]
+ 0048e088 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048e088 bytes 699743f9
+ 0048e088 bytes 69bf43f9
- 0048e18c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0048e18c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048e18c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0048e18c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048e18c bytes 299543f9
+ 0048e18c bytes 29bd43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-add4bdaba418929258ff528bcee307a0"></a>

### [`0048e640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048e/0048e640.md) → [`0048e640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048e640.md) _ZN5Botan11BER_Decoder26decode_constrained_integerENS_8ASN1_TagES1_m

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 9件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.39% / 新版 97.39%

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
      "definition_site": "0048e798",
      "incomplete_value": true,
      "site": "0048e798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048e798",
      "incomplete_value": true,
      "site": "0048e798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048e800",
      "incomplete_value": false,
      "site": "0048e808",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048e800",
      "incomplete_value": false,
      "site": "0048e808",
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
            "const:a35:8"
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
      "definition_site": "0048e838",
      "incomplete_value": true,
      "site": "0048e844",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0048e838",
      "incomplete_value": true,
      "site": "0048e844",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f68:8"
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
      "0048e788",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048e800",
      "PARAM",
      [
        "storage",
        "00297a35",
        null,
        "string"
      ]
    ],
    [
      "0048e838",
      "READ",
      [
        "storage",
        "00c1af68",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0048e788",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048e800",
      "PARAM",
      [
        "storage",
        "002979a8",
        null,
        "string"
      ]
    ],
    [
      "0048e838",
      "READ",
      [
        "storage",
        "00c1afb8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048e788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048e/0048e640.md#insn-0048e788) · [`0048e800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048e/0048e640.md#insn-0048e800) · [`0048e838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048e/0048e640.md#insn-0048e838)
- 新版 `0048e788`（命令位置の公開資料なし） · `0048e800`（命令位置の公開資料なし） · `0048e838`（命令位置の公開資料なし）

~~~diff
- 0048e788 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0048e788 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048e788 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0048e788 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048e788 bytes 299543f9
+ 0048e788 bytes 29bd43f9
- 0048e800 ["COPY", "tmp:0:8", ["const:a35:8"]]
- 0048e800 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048e800 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048e800 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048e800 ["COPY", "tmp:0:8", ["const:9a8:8"]]
+ 0048e800 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048e800 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048e800 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048e800 bytes 21d42891
+ 0048e800 bytes 21a02691
- 0048e838 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f68:8"]]
- 0048e838 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048e838 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fb8:8"]]
+ 0048e838 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048e838 bytes 21b447f9
+ 0048e838 bytes 21dc47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e11db6824d676d6821919f7c3f1a1b9"></a>

### [`0048e994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048e/0048e994.md) → [`0048e994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048e994.md) _ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEENS_8ASN1_TagES7_S7_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbbe0.md) · 呼出先 14件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`0051e054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051e/0051e054.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdbc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc30.md) · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`0051e054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e054.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 95.97% / 新版 95.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048eaa0",
      "incomplete_value": true,
      "site": "0048eaa0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048eaa0",
      "incomplete_value": true,
      "site": "0048eaa0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048eae8",
      "incomplete_value": false,
      "site": "0048eaf0",
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
            "const:8a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048eae8",
      "incomplete_value": false,
      "site": "0048eaf0",
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
            "const:936:8"
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
      "definition_site": "0048eb24",
      "incomplete_value": true,
      "site": "0048eb30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0048eb24",
      "incomplete_value": true,
      "site": "0048eb30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0048ea90",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048eae8",
      "PARAM",
      [
        "storage",
        "00295936",
        null,
        "string"
      ]
    ],
    [
      "0048eb24",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0048ea90",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048eae8",
      "PARAM",
      [
        "storage",
        "002958a9",
        null,
        "string"
      ]
    ],
    [
      "0048eb24",
      "READ",
      [
        "storage",
        "00c1afb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048ea90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048e/0048e994.md#insn-0048ea90) · [`0048eae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048e/0048e994.md#insn-0048eae8) · [`0048eb24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048e/0048e994.md#insn-0048eb24)
- 新版 `0048ea90`（命令位置の公開資料なし） · `0048eae8`（命令位置の公開資料なし） · `0048eb24`（命令位置の公開資料なし）

~~~diff
- 0048ea90 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0048ea90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048ea90 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0048ea90 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048ea90 bytes 299543f9
+ 0048ea90 bytes 29bd43f9
- 0048eae8 ["COPY", "tmp:0:8", ["const:936:8"]]
- 0048eae8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048eae8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048eae8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048eae8 ["COPY", "tmp:0:8", ["const:8a9:8"]]
+ 0048eae8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048eae8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048eae8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048eae8 bytes 21d82491
+ 0048eae8 bytes 21a42291
- 0048eb24 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
- 0048eb24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048eb24 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fb0:8"]]
+ 0048eb24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048eb24 bytes 21b047f9
+ 0048eb24 bytes 21d847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb7c9f46c3d8807616c19d6f665fdf08"></a>

### [`0048ec7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048e/0048ec7c.md) → [`0048ec7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048e/0048ec7c.md) _ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS1_9allocatorIhEEEENS_8ASN1_TagES7_S7_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdba00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba00.md) · 呼出先 18件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051e1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051e/0051e1b4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdba50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdba50.md) · 呼出先 18件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0047c554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047c/0047c554.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051e1b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e1b4.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.89% / 新版 96.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048ee18",
      "incomplete_value": true,
      "site": "0048ee18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048ee18",
      "incomplete_value": true,
      "site": "0048ee18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 9,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048ee68",
      "incomplete_value": false,
      "site": "0048ee70",
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
            "const:8a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048ee68",
      "incomplete_value": false,
      "site": "0048ee70",
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
            "const:936:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048eea4",
      "incomplete_value": true,
      "site": "0048eeb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0048eea4",
      "incomplete_value": true,
      "site": "0048eeb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0048ee08",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048ee68",
      "PARAM",
      [
        "storage",
        "00295936",
        null,
        "string"
      ]
    ],
    [
      "0048eea4",
      "READ",
      [
        "storage",
        "00c1af60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "0048ee08",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048ee68",
      "PARAM",
      [
        "storage",
        "002958a9",
        null,
        "string"
      ]
    ],
    [
      "0048eea4",
      "READ",
      [
        "storage",
        "00c1afb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048ee08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048e/0048ec7c.md#insn-0048ee08) · [`0048ee68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048e/0048ec7c.md#insn-0048ee68) · [`0048eea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048e/0048ec7c.md#insn-0048eea4)
- 新版 `0048ee08`（命令位置の公開資料なし） · `0048ee68`（命令位置の公開資料なし） · `0048eea4`（命令位置の公開資料なし）

~~~diff
- 0048ee08 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 0048ee08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048ee08 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 0048ee08 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048ee08 bytes 299543f9
+ 0048ee08 bytes 29bd43f9
- 0048ee68 ["COPY", "tmp:0:8", ["const:936:8"]]
- 0048ee68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048ee68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048ee68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048ee68 ["COPY", "tmp:0:8", ["const:8a9:8"]]
+ 0048ee68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048ee68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048ee68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048ee68 bytes 21d82491
+ 0048ee68 bytes 21a42291
- 0048eea4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
- 0048eea4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048eea4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fb0:8"]]
+ 0048eea4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048eea4 bytes 21b047f9
+ 0048eea4 bytes 21d847f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29180a851326ce1efc13b50472e8733b"></a>

### [`0048f014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f014.md) → [`0048f014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f014.md) _ZN5Botan11DER_Encoder12DER_Sequence12get_contentsEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb850.md) · 呼出先 8件 [`0048f37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f37c.md) [`0048f6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f6e8.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`0051e3d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051e/0051e3d8.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdb8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb8a0.md) · 呼出先 8件 [`0048f37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f37c.md) [`0048f6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f6e8.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`0051e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e3d8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

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
      "definition_site": "0048f174",
      "incomplete_value": true,
      "site": "0048f174",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048f174",
      "incomplete_value": true,
      "site": "0048f174",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 4,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048f20c",
      "incomplete_value": true,
      "site": "0048f20c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048f20c",
      "incomplete_value": true,
      "site": "0048f20c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048f298",
      "incomplete_value": true,
      "site": "0048f298",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048f298",
      "incomplete_value": true,
      "site": "0048f298",
      "value": [
        "LOAD",
        "8",
        [
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
      "0048f164",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048f1fc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048f288",
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
      "0048f164",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048f1fc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048f288",
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

- 旧版 [`0048f164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f014.md#insn-0048f164) · [`0048f1fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f014.md#insn-0048f1fc) · [`0048f288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f014.md#insn-0048f288)
- 新版 `0048f164`（命令位置の公開資料なし） · `0048f1fc`（命令位置の公開資料なし） · `0048f288`（命令位置の公開資料なし）

~~~diff
- 0048f164 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 0048f164 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048f164 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 0048f164 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048f164 bytes e99643f9
+ 0048f164 bytes e9be43f9
- 0048f1fc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 0048f1fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048f1fc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 0048f1fc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048f1fc bytes e99643f9
+ 0048f1fc bytes e9be43f9
- 0048f288 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 0048f288 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048f288 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 0048f288 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048f288 bytes e99643f9
+ 0048f288 bytes e9be43f9
~~~


<a id="compare-d730bf4d8ca154ff7b7402aacb1cf226"></a>

### [`0048f37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f37c.md) → [`0048f37c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f37c.md) FUN_0048f37c

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`0048a5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048a/0048a5d8.md) [`0048f014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f014.md) · 呼出先 9件 [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051e2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051e/0051e2cc.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 2件 [`0048a5d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048a/0048a5d8.md) [`0048f014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048f014.md) · 呼出先 9件 [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051e2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e2cc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.81% / 新版 97.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048f410",
      "incomplete_value": false,
      "site": "0048f428",
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
            "const:6f3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048f410",
      "incomplete_value": false,
      "site": "0048f428",
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
            "const:780:8"
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
      "definition_site": "0048f418",
      "incomplete_value": false,
      "site": "0048f428",
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
            "const:e88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048f418",
      "incomplete_value": false,
      "site": "0048f428",
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
            "const:f15:8"
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0048f420",
      "incomplete_value": false,
      "site": "0048f428",
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
            "const:3d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048f420",
      "incomplete_value": false,
      "site": "0048f428",
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
    "ordinal": 1,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "0048f410",
      "PARAM",
      [
        "storage",
        "00292780",
        null,
        "string"
      ]
    ],
    [
      "0048f418",
      "PARAM",
      [
        "storage",
        "00298f15",
        null,
        "string"
      ]
    ],
    [
      "0048f420",
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "0048f410",
      "PARAM",
      [
        "storage",
        "002926f3",
        null,
        "string"
      ]
    ],
    [
      "0048f418",
      "PARAM",
      [
        "storage",
        "00298e88",
        null,
        "string"
      ]
    ],
    [
      "0048f420",
      "PARAM",
      [
        "storage",
        "0029c3d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048f410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f37c.md#insn-0048f410) · [`0048f418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f37c.md#insn-0048f418) · [`0048f41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048f37c.md#insn-0048f41c)
- 新版 `0048f410`（命令位置の公開資料なし） · `0048f418`（命令位置の公開資料なし） · `0048f41c`（命令位置の公開資料なし）

~~~diff
- 0048f410 ["COPY", "tmp:0:8", ["const:780:8"]]
- 0048f410 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048f410 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048f410 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048f410 ["COPY", "tmp:0:8", ["const:6f3:8"]]
+ 0048f410 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048f410 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048f410 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048f410 bytes 21001e91
+ 0048f410 bytes 21cc1b91
- 0048f418 ["COPY", "tmp:0:8", ["const:f15:8"]]
- 0048f418 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 0048f418 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 0048f418 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 0048f418 ["COPY", "tmp:0:8", ["const:e88:8"]]
+ 0048f418 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 0048f418 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 0048f418 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 0048f418 bytes 42543c91
+ 0048f418 bytes 42203a91
- 0048f41c ["COPY", "register:4018:8", ["const:291000:8"]]
+ 0048f41c ["COPY", "register:4018:8", ["const:29c000:8"]]
- 0048f41c bytes 03f0ffd0
+ 0048f41c bytes 63f0ffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c02d6fd6a1db9e40dbbef2c564641cf7"></a>

### [`0048fa0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048fa0c.md) → [`0048fa0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fa0c.md) _ZN5Botan11DER_Encoder12get_contentsEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdb900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb900.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdb950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb950.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0048bd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048b/0048bd8c.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

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
      "definition_site": "0048fa88",
      "incomplete_value": false,
      "site": "0048fa90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:17c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048fa88",
      "incomplete_value": false,
      "site": "0048fa90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:e2:8"
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
      "definition_site": "0048fac4",
      "incomplete_value": true,
      "site": "0048fad0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048fac4",
      "incomplete_value": true,
      "site": "0048fad0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
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
      "0048fa88",
      "PARAM",
      [
        "storage",
        "002a80e2",
        null,
        "string"
      ]
    ],
    [
      "0048fac4",
      "READ",
      [
        "storage",
        "00c1af08",
        null,
        "pointer"
      ]
    ],
    [
      "0048fac4",
      "PARAM",
      [
        "storage",
        "00be9388",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "0048fa88",
      "PARAM",
      [
        "storage",
        "002a817c",
        null,
        "string"
      ]
    ],
    [
      "0048fac4",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "0048fac4",
      "PARAM",
      [
        "storage",
        "00be93d8",
        "_ZTIN5Botan13Invalid_StateE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0048fa88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048fa0c.md#insn-0048fa88) · [`0048fac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048fa0c.md#insn-0048fac4)
- 新版 `0048fa88`（命令位置の公開資料なし） · `0048fac4`（命令位置の公開資料なし）

~~~diff
- 0048fa88 ["COPY", "tmp:0:8", ["const:e2:8"]]
- 0048fa88 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048fa88 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048fa88 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048fa88 ["COPY", "tmp:0:8", ["const:17c:8"]]
+ 0048fa88 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048fa88 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048fa88 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048fa88 bytes 21880391
+ 0048fa88 bytes 21f00591
- 0048fac4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f08:8"]]
- 0048fac4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048fac4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
+ 0048fac4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048fac4 bytes 218447f9
+ 0048fac4 bytes 21ac47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e74d1a1006ef195d8162c8fb2a7ee05b"></a>

### [`0048fb24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048fb24.md) → [`0048fb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fb24.md) FUN_0048fb24

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048fb8c",
      "incomplete_value": true,
      "site": "0048fb8c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048fb8c",
      "incomplete_value": true,
      "site": "0048fb8c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048fbc8",
      "incomplete_value": true,
      "site": "0048fbc8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048fbc8",
      "incomplete_value": true,
      "site": "0048fbc8",
      "value": [
        "LOAD",
        "8",
        [
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
      "0048fb7c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0048fbb8",
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
      "0048fb7c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0048fbb8",
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

- 旧版 [`0048fb7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048fb24.md#insn-0048fb7c) · [`0048fbb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048fb24.md#insn-0048fbb8)
- 新版 `0048fb7c`（命令位置の公開資料なし） · `0048fbb8`（命令位置の公開資料なし）

~~~diff
- 0048fb7c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0048fb7c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048fb7c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0048fb7c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048fb7c bytes a99643f9
+ 0048fb7c bytes a9be43f9
- 0048fbb8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 0048fbb8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048fbb8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:778:8"]]
+ 0048fbb8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048fbb8 bytes a99643f9
+ 0048fbb8 bytes a9be43f9
~~~


<a id="compare-760ec7f44a7e36952d90e8ecfdc32cd8"></a>

### [`0048fc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048fc00.md) → [`0048fc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048fc00.md) _ZN5Botan11DER_Encoder14start_explicitEt

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "0048fc68",
      "incomplete_value": false,
      "site": "0048fc70",
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
            "const:454:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0048fc68",
      "incomplete_value": false,
      "site": "0048fc70",
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
            "const:3c9:8"
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
      "definition_site": "0048fca4",
      "incomplete_value": true,
      "site": "0048fcb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0048fca4",
      "incomplete_value": true,
      "site": "0048fcb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0048fc68",
      "PARAM",
      [
        "storage",
        "0029f3c9",
        null,
        "string"
      ]
    ],
    [
      "0048fca4",
      "READ",
      [
        "storage",
        "00c1afb8",
        null,
        "pointer"
      ]
    ],
    [
      "0048fca4",
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
      "0048fc68",
      "PARAM",
      [
        "storage",
        "0029f454",
        null,
        "string"
      ]
    ],
    [
      "0048fca4",
      "READ",
      [
        "storage",
        "00c1b008",
        null,
        "pointer"
      ]
    ],
    [
      "0048fca4",
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

- 旧版 [`0048fc68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048fc00.md#insn-0048fc68) · [`0048fc98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048fc00.md#insn-0048fc98) · [`0048fca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048fc00.md#insn-0048fca4)
- 新版 `0048fc68`（命令位置の公開資料なし） · `0048fc98`（命令位置の公開資料なし） · `0048fca4`（命令位置の公開資料なし）

~~~diff
- 0048fc68 ["COPY", "tmp:0:8", ["const:3c9:8"]]
- 0048fc68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0048fc68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0048fc68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0048fc68 ["COPY", "tmp:0:8", ["const:454:8"]]
+ 0048fc68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0048fc68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0048fc68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0048fc68 bytes 21240f91
+ 0048fc68 bytes 21501191
- 0048fc98 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 0048fc98 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 0048fc98 bytes 413c00f0
+ 0048fc98 bytes 613c0090
- 0048fca4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fb8:8"]]
- 0048fca4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048fca4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:8:8"]]
+ 0048fca4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0048fca4 bytes 21dc47f9
+ 0048fca4 bytes 210440f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d20f4d502b8905901d26022ddf84c79"></a>

### [`0048ff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048ff2c.md) → [`0048ff2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048ff2c.md) _ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc70.md) · 呼出先 8件 [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdb980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb980.md) [`00bdba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md)
- 新版 呼出元 1件 [`00bdbcc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcc0.md) · 呼出先 8件 [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdb9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb9d0.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.86% / 新版 96.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0048ffa8",
      "incomplete_value": true,
      "site": "0048ffa8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0048ffa8",
      "incomplete_value": true,
      "site": "0048ffa8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0049013c",
      "incomplete_value": true,
      "site": "0049013c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0049013c",
      "incomplete_value": true,
      "site": "0049013c",
      "value": [
        "LOAD",
        "8",
        [
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
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004901e8",
      "incomplete_value": true,
      "site": "004901e8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004901e8",
      "incomplete_value": true,
      "site": "004901e8",
      "value": [
        "LOAD",
        "8",
        [
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
      "0048ff98",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0049012c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004901d8",
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
      "0048ff98",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0049012c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004901d8",
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

- 旧版 [`0048ff98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048ff2c.md#insn-0048ff98) · [`0049012c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048ff2c.md#insn-0049012c) · [`004901d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048ff2c.md#insn-004901d8)
- 新版 `0048ff98`（命令位置の公開資料なし） · `0049012c`（命令位置の公開資料なし） · `004901d8`（命令位置の公開資料なし）

~~~diff
- 0048ff98 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 0048ff98 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0048ff98 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 0048ff98 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0048ff98 bytes 499743f9
+ 0048ff98 bytes 49bf43f9
- 0049012c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 0049012c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049012c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 0049012c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0049012c bytes 499743f9
+ 0049012c bytes 49bf43f9
- 004901d8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:728:8"]]
- 004901d8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004901d8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:778:8"]]
+ 004901d8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004901d8 bytes 499743f9
+ 004901d8 bytes 49bf43f9
~~~


<a id="compare-b0cce65f01490f618094c3cae074c690"></a>

### [`00490274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490274.md) → [`00490274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490274.md) _ZN5Botan11DER_Encoder6encodeEPKhmNS_8ASN1_TagES3_S3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc90.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`0051e2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051e/0051e2cc.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdbce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbce0.md) · 呼出先 12件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`0051e2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051e/0051e2cc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.11% / 新版 98.11%

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
      "definition_site": "00490384",
      "incomplete_value": true,
      "site": "00490384",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00490384",
      "incomplete_value": true,
      "site": "00490384",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004903d0",
      "incomplete_value": false,
      "site": "004903d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:5d7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004903d0",
      "incomplete_value": false,
      "site": "004903d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:664:8"
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
      "definition_site": "00490408",
      "incomplete_value": true,
      "site": "00490414",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00490408",
      "incomplete_value": true,
      "site": "00490414",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00490374",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "004903d0",
      "PARAM",
      [
        "storage",
        "00294664",
        null,
        "string"
      ]
    ],
    [
      "00490408",
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
      "00490374",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "004903d0",
      "PARAM",
      [
        "storage",
        "002945d7",
        null,
        "string"
      ]
    ],
    [
      "00490408",
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

- 旧版 [`00490374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490274.md#insn-00490374) · [`004903d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490274.md#insn-004903d0) · [`00490408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490274.md#insn-00490408)
- 新版 `00490374`（命令位置の公開資料なし） · `004903d0`（命令位置の公開資料なし） · `00490408`（命令位置の公開資料なし）

~~~diff
- 00490374 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 00490374 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00490374 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 00490374 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00490374 bytes 299543f9
+ 00490374 bytes 29bd43f9
- 004903d0 ["COPY", "tmp:0:8", ["const:664:8"]]
- 004903d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004903d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004903d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004903d0 ["COPY", "tmp:0:8", ["const:5d7:8"]]
+ 004903d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004903d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004903d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004903d0 bytes 21901991
+ 004903d0 bytes 215c1791
- 00490408 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 00490408 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00490408 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 00490408 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00490408 bytes 217847f9
+ 00490408 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37f19cdc12456fe163217aaf2a0cb4b8"></a>

### [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) → [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) FUN_00490630

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 55件 [`0048df5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048d/0048df5c.md) [`0048ff2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0048f/0048ff2c.md) [`00490728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490728.md) [`00491f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/00491f34.md) [`00492804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/00492804.md) · 呼出先 7件 [`00513fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/00513fb0.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 55件 [`0048df5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048d/0048df5c.md) [`0048ff2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0048f/0048ff2c.md) [`00490728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490728.md) [`00491f34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/00491f34.md) [`00492804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492804.md) · 呼出先 7件 [`00513fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/00513fb0.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "004906f4",
      "incomplete_value": true,
      "site": "004906fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004906f4",
      "incomplete_value": true,
      "site": "004906fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004906f8",
      "incomplete_value": true,
      "site": "004906fc",
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
      "definition_site": "004906f8",
      "incomplete_value": true,
      "site": "004906fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004906f4",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004906f4",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004906f8",
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
      "004906f4",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "004906f4",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "004906f8",
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

- 旧版 [`004906ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md#insn-004906ec) · [`004906f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md#insn-004906f4) · [`004906f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md#insn-004906f8)
- 新版 `004906ec`（命令位置の公開資料なし） · `004906f4`（命令位置の公開資料なし） · `004906f8`（命令位置の公開資料なし）

~~~diff
- 004906ec ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 004906ec ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 004906ec bytes 423c00d0
+ 004906ec bytes 423c00f0
- 004906f4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
- 004906f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004906f4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
+ 004906f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004906f4 bytes 21d447f9
+ 004906f4 bytes 21fc47f9
- 004906f8 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:fb0:8"]]
- 004906f8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 004906f8 ["COPY", "tmp:0:8", ["register:4010:8"]]
+ 004906f8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 004906f8 bytes 42d847f9
+ 004906f8 bytes 420040f9
~~~


<a id="compare-7bf7fc4acd5a322f2549c301b66c1d07"></a>

### [`00490728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490728.md) → [`00490728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490728.md) _ZN5Botan6BigInt6encodeEPhRKS0_NS0_4BaseE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbab0.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdbb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb00.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `call_target` 1件

アドレスに依存する影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00490a1c",
      "incomplete_value": true,
      "site": "00490a1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00490a1c",
      "incomplete_value": true,
      "site": "00490a1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00490ab8",
      "incomplete_value": true,
      "site": "00490ab8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00490ab8",
      "incomplete_value": true,
      "site": "00490ab8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00490b60",
      "incomplete_value": true,
      "site": "00490b60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00490b60",
      "incomplete_value": true,
      "site": "00490b60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00490a0c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00490aa8",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00490b50",
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
      "00490a0c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00490aa8",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00490b50",
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

- 旧版 [`00490a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490728.md#insn-00490a0c) · [`00490aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490728.md#insn-00490aa8) · [`00490b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490728.md#insn-00490b50)
- 新版 `00490a0c`（命令位置の公開資料なし） · `00490aa8`（命令位置の公開資料なし） · `00490b50`（命令位置の公開資料なし）

~~~diff
- 00490a0c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 00490a0c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00490a0c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 00490a0c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00490a0c bytes 299543f9
+ 00490a0c bytes 29bd43f9
- 00490aa8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 00490aa8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00490aa8 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 00490aa8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00490aa8 bytes 299743f9
+ 00490aa8 bytes 29bf43f9
- 00490b50 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 00490b50 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00490b50 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 00490b50 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00490b50 bytes 299543f9
+ 00490b50 bytes 29bd43f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcb86323335ea378fa8ebec3e545d4f8"></a>

### [`0049100c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/0049100c.md) → [`0049100c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/0049100c.md) _ZN5Botan9SCAN_NameC1ENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bdbce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbce0.md) [`00bdbea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbea0.md) · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e41c.md) [`0045efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0045e/0045efa8.md) [`004918d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/004918d4.md)
- 新版 呼出元 2件 [`00bdbd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd30.md) [`00bdbef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbef0.md) · 呼出先 19件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0041e380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e380.md) [`0041e41c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e41c.md) [`0045efa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0045e/0045efa8.md) [`004918d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/004918d4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.56% / 新版 98.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004910a0",
      "incomplete_value": false,
      "site": "004910ac",
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
            "const:9a2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004910a0",
      "incomplete_value": false,
      "site": "004910ac",
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
            "const:a2f:8"
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
      "definition_site": "00491664",
      "incomplete_value": true,
      "site": "00491670",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00491664",
      "incomplete_value": true,
      "site": "00491670",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 28,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004916f4",
      "incomplete_value": false,
      "site": "00491700",
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
            "const:9db:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004916f4",
      "incomplete_value": false,
      "site": "00491700",
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
            "const:a6f:8"
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
      "004910a0",
      "PARAM",
      [
        "storage",
        "00295a2f",
        null,
        "string"
      ]
    ],
    [
      "00491138",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "00491664",
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
      "004910a0",
      "PARAM",
      [
        "storage",
        "002959a2",
        null,
        "string"
      ]
    ],
    [
      "00491138",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "00491664",
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

- 旧版 [`004910a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/0049100c.md#insn-004910a0) · [`00491118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/0049100c.md#insn-00491118) · [`00491664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/0049100c.md#insn-00491664)
- 新版 `004910a0`（命令位置の公開資料なし） · `00491118`（命令位置の公開資料なし） · `00491664`（命令位置の公開資料なし）

~~~diff
- 004910a0 ["COPY", "tmp:0:8", ["const:a2f:8"]]
- 004910a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004910a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004910a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004910a0 ["COPY", "tmp:0:8", ["const:9a2:8"]]
+ 004910a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004910a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004910a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004910a0 bytes 00bc2891
+ 004910a0 bytes 00882691
- 00491118 ["COPY", "tmp:0:8", ["const:866:8"]]
- 00491118 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
- 00491118 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
- 00491118 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
+ 00491118 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 00491118 ["INT_CARRY", "register:105:1", ["register:40b8:8", "tmp:0:8"]]
+ 00491118 ["INT_SCARRY", "register:106:1", ["register:40b8:8", "tmp:0:8"]]
+ 00491118 ["INT_ADD", "tmp:1:8", ["register:40b8:8", "tmp:0:8"]]
- 00491118 bytes f79a2191
+ 00491118 bytes f7661f91
- 00491664 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f10:8"]]
- 00491664 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00491664 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f60:8"]]
+ 00491664 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00491664 bytes 218847f9
+ 00491664 bytes 21b047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96fba6f38c73c29d72d2cd925b835431"></a>

### [`004918d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/004918d4.md) → [`004918d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/004918d4.md) FUN_004918d4

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`0049100c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/0049100c.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 1件 [`0049100c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/0049100c.md) · 呼出先 6件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00491a18",
      "incomplete_value": false,
      "site": "00491a1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:5c9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00491a18",
      "incomplete_value": false,
      "site": "00491a1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:53e:8"
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
      "definition_site": "00491a88",
      "incomplete_value": false,
      "site": "00491a8c",
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
            "const:ab6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00491a88",
      "incomplete_value": false,
      "site": "00491a8c",
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
            "const:b43:8"
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
      "004919c8",
      "PARAM",
      [
        "storage",
        "0029f544",
        null,
        null
      ]
    ],
    [
      "00491a18",
      "PARAM",
      [
        "storage",
        "002a253e",
        null,
        null
      ]
    ],
    [
      "00491a88",
      "PARAM",
      [
        "storage",
        "00299b43",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "004919c8",
      "PARAM",
      [
        "storage",
        "0029f5cf",
        null,
        null
      ]
    ],
    [
      "00491a18",
      "PARAM",
      [
        "storage",
        "002a25c9",
        null,
        null
      ]
    ],
    [
      "00491a88",
      "PARAM",
      [
        "storage",
        "00299ab6",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`0049196c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/004918d4.md#insn-0049196c) · [`00491a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/004918d4.md#insn-00491a18) · [`00491a88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/004918d4.md#insn-00491a88)
- 新版 `0049196c`（命令位置の公開資料なし） · `00491a18`（命令位置の公開資料なし） · `00491a88`（命令位置の公開資料なし）

~~~diff
- 0049196c ["COPY", "tmp:0:8", ["const:544:8"]]
- 0049196c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 0049196c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 0049196c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 0049196c ["COPY", "tmp:0:8", ["const:5cf:8"]]
+ 0049196c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 0049196c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 0049196c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 0049196c bytes b5121591
+ 0049196c bytes b53e1791
- 00491a18 ["COPY", "tmp:0:8", ["const:53e:8"]]
- 00491a18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00491a18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00491a18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00491a18 ["COPY", "tmp:0:8", ["const:5c9:8"]]
+ 00491a18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00491a18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00491a18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00491a18 bytes 00f81491
+ 00491a18 bytes 00241791
- 00491a88 ["COPY", "tmp:0:8", ["const:b43:8"]]
- 00491a88 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00491a88 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00491a88 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00491a88 ["COPY", "tmp:0:8", ["const:ab6:8"]]
+ 00491a88 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00491a88 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00491a88 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00491a88 bytes 210c2d91
+ 00491a88 bytes 21d82a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16ddd1b653dc2ea47e3b37927ef44bb5"></a>

### [`00491be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/00491be0.md) → [`00491be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00491/00491be0.md) _ZNK5Botan9SCAN_Name3argEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbcf0.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdbd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd40.md) · 呼出先 10件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.09% / 新版 97.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00491ce0",
      "incomplete_value": false,
      "site": "00491ce8",
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
            "const:337:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00491ce0",
      "incomplete_value": false,
      "site": "00491ce8",
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
            "const:2ac:8"
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
      "definition_site": "00491d18",
      "incomplete_value": false,
      "site": "00491d20",
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
            "const:87b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00491d18",
      "incomplete_value": false,
      "site": "00491d20",
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
            "const:908:8"
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
      "definition_site": "00491d68",
      "incomplete_value": true,
      "site": "00491d74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00491d68",
      "incomplete_value": true,
      "site": "00491d74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00491ce0",
      "PARAM",
      [
        "storage",
        "002a32ac",
        null,
        "string"
      ]
    ],
    [
      "00491d18",
      "PARAM",
      [
        "storage",
        "00296908",
        null,
        null
      ]
    ],
    [
      "00491d68",
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
      "00491ce0",
      "PARAM",
      [
        "storage",
        "002a3337",
        null,
        "string"
      ]
    ],
    [
      "00491d18",
      "PARAM",
      [
        "storage",
        "0029687b",
        null,
        null
      ]
    ],
    [
      "00491d68",
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

- 旧版 [`00491ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/00491be0.md#insn-00491ce0) · [`00491d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/00491be0.md#insn-00491d18) · [`00491d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00491/00491be0.md#insn-00491d68)
- 新版 `00491ce0`（命令位置の公開資料なし） · `00491d18`（命令位置の公開資料なし） · `00491d68`（命令位置の公開資料なし）

~~~diff
- 00491ce0 ["COPY", "tmp:0:8", ["const:2ac:8"]]
- 00491ce0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00491ce0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00491ce0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00491ce0 ["COPY", "tmp:0:8", ["const:337:8"]]
+ 00491ce0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00491ce0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00491ce0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00491ce0 bytes 21b00a91
+ 00491ce0 bytes 21dc0c91
- 00491d18 ["COPY", "tmp:0:8", ["const:908:8"]]
- 00491d18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00491d18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00491d18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00491d18 ["COPY", "tmp:0:8", ["const:87b:8"]]
+ 00491d18 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00491d18 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00491d18 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00491d18 bytes 21202491
+ 00491d18 bytes 21ec2191
- 00491d68 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 00491d68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00491d68 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 00491d68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00491d68 bytes 217847f9
+ 00491d68 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c339490326c57963bca102d4eb583a2a"></a>

### [`00492480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/00492480.md) → [`00492480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492480.md) _ZN5BotaneqERKNS_11OctetStringES2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbd10.md) · 呼出先 5件 [`0051d3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d3cc.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`010a5058`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/010a5/010a5058.md)
- 新版 呼出元 1件 [`00bdbd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd60.md) · 呼出先 5件 [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`010a5058`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/010a5/010a5058.md)

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
      "definition_site": "00492538",
      "incomplete_value": true,
      "site": "00492538",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00492538",
      "incomplete_value": true,
      "site": "00492538",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00492564",
      "incomplete_value": true,
      "site": "00492564",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00492564",
      "incomplete_value": true,
      "site": "00492564",
      "value": [
        "LOAD",
        "8",
        [
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
      "00492528",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00492554",
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
      "00492528",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00492554",
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

- 旧版 [`00492528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/00492480.md#insn-00492528) · [`00492554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/00492480.md#insn-00492554)
- 新版 `00492528`（命令位置の公開資料なし） · `00492554`（命令位置の公開資料なし）

~~~diff
- 00492528 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 00492528 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00492528 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 00492528 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00492528 bytes e99643f9
+ 00492528 bytes e9be43f9
- 00492554 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 00492554 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00492554 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 00492554 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00492554 bytes e99643f9
+ 00492554 bytes e9be43f9
~~~


<a id="compare-1191131b0f1f0d2a50770017cdcefee1"></a>

### [`004925e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/004925e8.md) → [`004925e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/004925e8.md) _ZN5BotanplERKNS_11OctetStringES2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0051d3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d3cc.md) [`0051d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d614.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0051d3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d3cc.md) [`0051d614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d614.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.83% / 新版 94.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "004926a8",
      "incomplete_value": true,
      "site": "004926a8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "004926a8",
      "incomplete_value": true,
      "site": "004926a8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0049273c",
      "incomplete_value": true,
      "site": "0049273c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0049273c",
      "incomplete_value": true,
      "site": "0049273c",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 8,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00492780",
      "incomplete_value": true,
      "site": "00492780",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00492780",
      "incomplete_value": true,
      "site": "00492780",
      "value": [
        "LOAD",
        "8",
        [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00492698",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0049272c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00492770",
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
      "00492698",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0049272c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00492770",
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

- 旧版 [`00492698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/004925e8.md#insn-00492698) · [`0049272c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/004925e8.md#insn-0049272c) · [`00492770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/004925e8.md#insn-00492770)
- 新版 `00492698`（命令位置の公開資料なし） · `0049272c`（命令位置の公開資料なし） · `00492770`（命令位置の公開資料なし）

~~~diff
- 00492698 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 00492698 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00492698 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 00492698 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00492698 bytes e99643f9
+ 00492698 bytes e9be43f9
- 0049272c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 0049272c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049272c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 0049272c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0049272c bytes e99643f9
+ 0049272c bytes e9be43f9
- 00492770 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:728:8"]]
- 00492770 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00492770 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:778:8"]]
+ 00492770 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00492770 bytes e99643f9
+ 00492770 bytes e9be43f9
~~~


<a id="compare-b2d61843f16680562dba15c884ec5405"></a>

### [`00492b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/00492b90.md) → [`00492b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492b90.md) _ZN5Botan13base64_encodeEPKhm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbd30.md) · 呼出先 6件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 1件 [`00bdbd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd80.md) · 呼出先 6件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.54% / 新版 95.54%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00492d3c",
      "incomplete_value": false,
      "site": "00492d48",
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
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00492d3c",
      "incomplete_value": false,
      "site": "00492d48",
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
            "const:a15:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00492d44",
      "incomplete_value": false,
      "site": "00492d48",
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
            "const:3d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00492d44",
      "incomplete_value": false,
      "site": "00492d48",
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
    "ordinal": 4,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00492d00",
      "PARAM",
      [
        "storage",
        "002a7528",
        null,
        "string"
      ]
    ],
    [
      "00492d0c",
      "PARAM",
      [
        "storage",
        "00299c59",
        null,
        "string"
      ]
    ],
    [
      "00492d24",
      "PARAM",
      [
        "storage",
        "0029d3f6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00492d00",
      "PARAM",
      [
        "storage",
        "002a75c2",
        null,
        "string"
      ]
    ],
    [
      "00492d0c",
      "PARAM",
      [
        "storage",
        "00299bcc",
        null,
        "string"
      ]
    ],
    [
      "00492d24",
      "PARAM",
      [
        "storage",
        "0029d481",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00492d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/00492b90.md#insn-00492d00) · [`00492d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/00492b90.md#insn-00492d0c) · [`00492d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/00492b90.md#insn-00492d24)
- 新版 `00492d00`（命令位置の公開資料なし） · `00492d0c`（命令位置の公開資料なし） · `00492d24`（命令位置の公開資料なし）

~~~diff
- 00492d00 ["COPY", "tmp:0:8", ["const:528:8"]]
- 00492d00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00492d00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00492d00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00492d00 ["COPY", "tmp:0:8", ["const:5c2:8"]]
+ 00492d00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00492d00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00492d00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00492d00 bytes 21a01491
+ 00492d00 bytes 21081791
- 00492d0c ["COPY", "tmp:0:8", ["const:c59:8"]]
- 00492d0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00492d0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00492d0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00492d0c ["COPY", "tmp:0:8", ["const:bcc:8"]]
+ 00492d0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00492d0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00492d0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00492d0c bytes 00643191
+ 00492d0c bytes 00302f91
- 00492d24 ["COPY", "tmp:0:8", ["const:3f6:8"]]
- 00492d24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00492d24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00492d24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00492d24 ["COPY", "tmp:0:8", ["const:481:8"]]
+ 00492d24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00492d24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00492d24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00492d24 bytes 00d80f91
+ 00492d24 bytes 00041291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0c96a2054a850479e089f925992d01bc"></a>

### [`00492db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/00492db0.md) → [`00492db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00492/00492db0.md) _ZN5Botan13base64_decodeEPhPKcmRmbb

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbd40.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041f/0041f354.md) [`0042cde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0042c/0042cde4.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdbd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd90.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041f354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041f/0041f354.md) [`0042cde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0042c/0042cde4.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.20% / 新版 96.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00492f8c",
      "incomplete_value": false,
      "site": "00492fa0",
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
      "definition_site": "00492f8c",
      "incomplete_value": false,
      "site": "00492fa0",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00492fb8",
      "incomplete_value": false,
      "site": "00492fc0",
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
      "definition_site": "00492fb8",
      "incomplete_value": false,
      "site": "00492fc0",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00492fd8",
      "incomplete_value": false,
      "site": "00492fe0",
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
            "const:986:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00492fd8",
      "incomplete_value": false,
      "site": "00492fe0",
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
            "const:a13:8"
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
      "00492f8c",
      "PARAM",
      [
        "storage",
        "0029e3cc",
        null,
        null
      ]
    ],
    [
      "00492fb8",
      "PARAM",
      [
        "storage",
        "002a42a8",
        null,
        null
      ]
    ],
    [
      "00492fd8",
      "PARAM",
      [
        "storage",
        "00291a13",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00492f8c",
      "PARAM",
      [
        "storage",
        "0029e457",
        null,
        null
      ]
    ],
    [
      "00492fb8",
      "PARAM",
      [
        "storage",
        "002a4333",
        null,
        null
      ]
    ],
    [
      "00492fd8",
      "PARAM",
      [
        "storage",
        "00291986",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00492f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/00492db0.md#insn-00492f8c) · [`00492fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/00492db0.md#insn-00492fb8) · [`00492fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00492/00492db0.md#insn-00492fd8)
- 新版 `00492f8c`（命令位置の公開資料なし） · `00492fb8`（命令位置の公開資料なし） · `00492fd8`（命令位置の公開資料なし）

~~~diff
- 00492f8c ["COPY", "tmp:0:8", ["const:3cc:8"]]
- 00492f8c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00492f8c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00492f8c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00492f8c ["COPY", "tmp:0:8", ["const:457:8"]]
+ 00492f8c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00492f8c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00492f8c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00492f8c bytes 21300f91
+ 00492f8c bytes 215c1191
- 00492fb8 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00492fb8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00492fb8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00492fb8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00492fb8 ["COPY", "tmp:0:8", ["const:333:8"]]
+ 00492fb8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00492fb8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00492fb8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00492fb8 bytes 21a00a91
+ 00492fb8 bytes 21cc0c91
- 00492fd8 ["COPY", "tmp:0:8", ["const:a13:8"]]
- 00492fd8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00492fd8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00492fd8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00492fd8 ["COPY", "tmp:0:8", ["const:986:8"]]
+ 00492fd8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00492fd8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00492fd8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00492fd8 bytes 214c2891
+ 00492fd8 bytes 21182691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06cb1c0849ba41d7db4daff29497f803"></a>

### [`00493150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00493/00493150.md) → [`00493150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493150.md) _ZN5Botan13base64_decodeEPhPKcmb

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbd50.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdbda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbda0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "004931cc",
      "incomplete_value": false,
      "site": "004931d4",
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
            "const:d68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004931cc",
      "incomplete_value": false,
      "site": "004931d4",
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
            "const:df5:8"
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
      "definition_site": "00493208",
      "incomplete_value": true,
      "site": "00493214",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00493208",
      "incomplete_value": true,
      "site": "00493214",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004931cc",
      "PARAM",
      [
        "storage",
        "00298df5",
        null,
        "string"
      ]
    ],
    [
      "00493208",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "00493208",
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
      "004931cc",
      "PARAM",
      [
        "storage",
        "00298d68",
        null,
        "string"
      ]
    ],
    [
      "00493208",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "00493208",
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

- 旧版 [`004931cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00493/00493150.md#insn-004931cc) · [`00493208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00493/00493150.md#insn-00493208)
- 新版 `004931cc`（命令位置の公開資料なし） · `00493208`（命令位置の公開資料なし）

~~~diff
- 004931cc ["COPY", "tmp:0:8", ["const:df5:8"]]
- 004931cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004931cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004931cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004931cc ["COPY", "tmp:0:8", ["const:d68:8"]]
+ 004931cc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004931cc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004931cc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004931cc bytes 21d43791
+ 004931cc bytes 21a03591
- 00493208 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 00493208 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00493208 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 00493208 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00493208 bytes 217847f9
+ 00493208 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d65250710fad107fde56f523a4565a0a"></a>

### [`004934f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00493/004934f4.md) → [`004934f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/004934f4.md) _ZNK5Botan6BigInt12encoded_sizeENS0_4BaseE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbaa0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdbaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbaf0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.73% / 新版 98.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049371c",
      "incomplete_value": false,
      "site": "00493724",
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
            "const:535:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "0049371c",
      "incomplete_value": false,
      "site": "00493724",
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
            "const:4aa:8"
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
      "definition_site": "00493758",
      "incomplete_value": true,
      "site": "00493764",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00493758",
      "incomplete_value": true,
      "site": "00493764",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0049371c",
      "PARAM",
      [
        "storage",
        "002a54aa",
        null,
        "string"
      ]
    ],
    [
      "00493758",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "00493758",
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
      "0049371c",
      "PARAM",
      [
        "storage",
        "002a5535",
        null,
        "string"
      ]
    ],
    [
      "00493758",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "00493758",
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

- 旧版 [`0049371c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00493/004934f4.md#insn-0049371c) · [`00493758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00493/004934f4.md#insn-00493758)
- 新版 `0049371c`（命令位置の公開資料なし） · `00493758`（命令位置の公開資料なし）

~~~diff
- 0049371c ["COPY", "tmp:0:8", ["const:4aa:8"]]
- 0049371c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 0049371c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 0049371c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 0049371c ["COPY", "tmp:0:8", ["const:535:8"]]
+ 0049371c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 0049371c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 0049371c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 0049371c bytes 21a81291
+ 0049371c bytes 21d41491
- 00493758 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 00493758 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00493758 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 00493758 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00493758 bytes 217847f9
+ 00493758 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1431f119028e373bd9db9ff0471a594"></a>

### [`00493850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00493/00493850.md) → [`00493850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493850.md) _ZN5Botan6divideERKNS_6BigIntES2_RS0_S3_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbcb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbcb0.md) · 呼出先 21件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`004989ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/004989ec.md) [`00498c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/00498c94.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051da48.md)
- 新版 呼出元 1件 [`00bdbd00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd00.md) · 呼出先 21件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`004989ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004989ec.md) [`00498c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498c94.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.14% / 新版 99.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

アドレスに依存する影響 `call_target` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "0049391c",
      "incomplete_value": true,
      "site": "00493920",
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
      "definition_site": "0049391c",
      "incomplete_value": true,
      "site": "00493920",
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00493940",
      "incomplete_value": true,
      "site": "00493944",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00493940",
      "incomplete_value": true,
      "site": "00493944",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00493a0c",
      "incomplete_value": true,
      "site": "00493a0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00493a0c",
      "incomplete_value": true,
      "site": "00493a0c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00493908",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ],
    [
      "00493920",
      "DATA",
      [
        "storage",
        "00becc50",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00493940",
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
      "00493908",
      "READ",
      [
        "storage",
        "00c1b010",
        null,
        "pointer"
      ]
    ],
    [
      "00493920",
      "DATA",
      [
        "storage",
        "00becca0",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00493940",
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

- 旧版 [`004938f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00493/00493850.md#insn-004938f4) · [`00493908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00493/00493850.md#insn-00493908) · [`00493934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00493/00493850.md#insn-00493934)
- 新版 `004938f4`（命令位置の公開資料なし） · `00493908`（命令位置の公開資料なし） · `00493934`（命令位置の公開資料なし）

~~~diff
- 004938f4 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 004938f4 ["COPY", "register:4048:8", ["const:c1b000:8"]]
- 004938f4 bytes 293c00f0
+ 004938f4 bytes 493c0090
- 00493908 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fc0:8"]]
- 00493908 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00493908 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:10:8"]]
+ 00493908 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00493908 bytes 29e147f9
+ 00493908 bytes 290940f9
- 00493934 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 00493934 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 00493934 bytes 213c00f0
+ 00493934 bytes 413c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f0f25e902bade589c205cf07ab20594d"></a>

### [`00494440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00494/00494440.md) → [`00494440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494440.md) _ZN5Botan7Charset10digit2charEh

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbcc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbcc0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdbd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd10.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

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
      "definition_site": "004944a8",
      "incomplete_value": false,
      "site": "004944b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:7ef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004944a8",
      "incomplete_value": false,
      "site": "004944b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:87c:8"
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
      "definition_site": "004944e4",
      "incomplete_value": true,
      "site": "004944f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004944e4",
      "incomplete_value": true,
      "site": "004944f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004944a8",
      "PARAM",
      [
        "storage",
        "0029487c",
        null,
        "string"
      ]
    ],
    [
      "004944e4",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "004944e4",
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
      "004944a8",
      "PARAM",
      [
        "storage",
        "002947ef",
        null,
        "string"
      ]
    ],
    [
      "004944e4",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "004944e4",
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

- 旧版 [`004944a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00494/00494440.md#insn-004944a8) · [`004944e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00494/00494440.md#insn-004944e4)
- 新版 `004944a8`（命令位置の公開資料なし） · `004944e4`（命令位置の公開資料なし）

~~~diff
- 004944a8 ["COPY", "tmp:0:8", ["const:87c:8"]]
- 004944a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004944a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004944a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004944a8 ["COPY", "tmp:0:8", ["const:7ef:8"]]
+ 004944a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004944a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004944a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004944a8 bytes 21f02191
+ 004944a8 bytes 21bc1f91
- 004944e4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 004944e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004944e4 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 004944e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004944e4 bytes 217847f9
+ 004944e4 bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c5c6114fcffda4a9f23a00e217c279c"></a>

### [`00494634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00494/00494634.md) → [`00494634`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494634.md) _ZN5Botan6BigInt11encode_1363EPhmRKS0_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbdc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbdc0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdbe10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe10.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.59% / 新版 97.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00494730",
      "incomplete_value": false,
      "site": "00494738",
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
            "const:506:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00494730",
      "incomplete_value": false,
      "site": "00494738",
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
            "const:47b:8"
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
      "definition_site": "0049476c",
      "incomplete_value": true,
      "site": "00494778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "0049476c",
      "incomplete_value": true,
      "site": "00494778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
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
      "00494730",
      "PARAM",
      [
        "storage",
        "002a547b",
        null,
        "string"
      ]
    ],
    [
      "0049476c",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "0049476c",
      "PARAM",
      [
        "storage",
        "00be92e0",
        "_ZTIN5Botan14Encoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ],
  "added": [
    [
      "00494730",
      "PARAM",
      [
        "storage",
        "002a5506",
        null,
        "string"
      ]
    ],
    [
      "0049476c",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "0049476c",
      "PARAM",
      [
        "storage",
        "00be9330",
        "_ZTIN5Botan14Encoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00494730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00494/00494634.md#insn-00494730) · [`0049476c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00494/00494634.md#insn-0049476c)
- 新版 `00494730`（命令位置の公開資料なし） · `0049476c`（命令位置の公開資料なし）

~~~diff
- 00494730 ["COPY", "tmp:0:8", ["const:47b:8"]]
- 00494730 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00494730 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00494730 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00494730 ["COPY", "tmp:0:8", ["const:506:8"]]
+ 00494730 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00494730 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00494730 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00494730 bytes 21ec1191
+ 00494730 bytes 21181491
- 0049476c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
- 0049476c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049476c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
+ 0049476c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0049476c bytes 21ac47f9
+ 0049476c bytes 21d447f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-151e4d7ced1419d6f84e36e007442390"></a>

### [`00494c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00494/00494c34.md) → [`00494c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494c34.md) _ZN5Botan7Charset10char2digitEc

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc10.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdbc60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc60.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00494cd8",
      "incomplete_value": true,
      "site": "00494ce4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00494cd8",
      "incomplete_value": true,
      "site": "00494ce4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00494cd8",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "00494cd8",
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
      "00494cd8",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "00494cd8",
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

- 旧版 [`00494cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00494/00494c34.md#insn-00494cd8)
- 新版 `00494cd8`（命令位置の公開資料なし）

~~~diff
- 00494cd8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 00494cd8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00494cd8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 00494cd8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00494cd8 bytes 217847f9
+ 00494cd8 bytes 21a047f9
~~~


<a id="compare-dc883da27dafaf91eaf95bd12cc5910e"></a>

### [`00494d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00494/00494d38.md) → [`00494d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494d38.md) _ZN5Botan6BigIntmLERKS0_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc20.md) · 呼出先 10件 [`00495978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495978.md) [`00496208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/00496208.md) [`00496308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/00496308.md) [`004b3f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b3/004b3f90.md) [`0051da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051da48.md)
- 新版 呼出元 1件 [`00bdbc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc70.md) · 呼出先 10件 [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`00496208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496208.md) [`00496308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496308.md) [`004b3f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3f90.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00495050",
      "incomplete_value": true,
      "site": "00495050",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00495050",
      "incomplete_value": true,
      "site": "00495050",
      "value": [
        "LOAD",
        "8",
        [
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
    "ordinal": 10,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "0049507c",
      "incomplete_value": true,
      "site": "0049507c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "0049507c",
      "incomplete_value": true,
      "site": "0049507c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00495040",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "0049506c",
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
      "00495040",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "0049506c",
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

- 旧版 [`00495040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00494/00494d38.md#insn-00495040) · [`0049506c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00494/00494d38.md#insn-0049506c)
- 新版 `00495040`（命令位置の公開資料なし） · `0049506c`（命令位置の公開資料なし）

~~~diff
- 00495040 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 00495040 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00495040 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 00495040 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00495040 bytes c99643f9
+ 00495040 bytes c9be43f9
- 0049506c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:728:8"]]
- 0049506c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049506c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:778:8"]]
+ 0049506c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 0049506c bytes c99643f9
+ 0049506c bytes c9be43f9
~~~


<a id="compare-b791821b0c1571556c881202c7b17b0e"></a>

### [`004950f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/004950f0.md) → [`004950f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md) _ZN5Botan6BigIntpLERKS0_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdbc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc30.md) · 呼出先 10件 [`004958dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/004958dc.md) [`00495978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495978.md) [`00495a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495a74.md) [`00495c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495c94.md) [`004b3cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b3/004b3cec.md)
- 新版 呼出元 1件 [`00bdbc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc80.md) · 呼出先 10件 [`004958dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004958dc.md) [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) [`00495a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495a74.md) [`00495c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495c94.md) [`004b3cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b3/004b3cec.md)

変更の種類 call_target, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 98.03% / 新版 98.03%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00495310",
      "incomplete_value": true,
      "site": "00495310",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00495310",
      "incomplete_value": true,
      "site": "00495310",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00495304",
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
      "00495304",
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

- 旧版 [`00495304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/004950f0.md#insn-00495304) · [`00495308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/004950f0.md#insn-00495308)
- 新版 `00495304`（命令位置の公開資料なし） · `00495308`（命令位置の公開資料なし）

~~~diff
- 00495304 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 00495304 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00495304 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 00495304 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00495304 bytes 299543f9
+ 00495304 bytes 29bd43f9
- 00495308 ["COPY", "register:4000:8", ["register:40a8:8"]]
- 00495308 bytes e00315aa
+ 00495308 ["COPY", "register:4000:8", ["register:40a8:8"]]
+ 00495308 bytes e00315aa
~~~


<a id="compare-267d64507f857730bc2ab6a5f3603d30"></a>

### [`00495378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495378.md) → [`00495378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495378.md) _ZN5BotanlsERNSt6__ndk113basic_ostreamIcNS0_11char_traitsIcEEEERKNS_6BigIntE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 94.30% / 新版 94.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `call_target` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00495410",
      "incomplete_value": true,
      "site": "00495410",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00495410",
      "incomplete_value": true,
      "site": "00495410",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00495460",
      "incomplete_value": true,
      "site": "00495460",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00495460",
      "incomplete_value": true,
      "site": "00495460",
      "value": [
        "LOAD",
        "8",
        [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00495474",
      "incomplete_value": false,
      "site": "00495480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:27d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495474",
      "incomplete_value": false,
      "site": "00495480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a8000:8"
          ],
          [
            "leaf",
            "const:1e3:8"
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
      "00495400",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00495450",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00495474",
      "PARAM",
      [
        "storage",
        "002a81e3",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00495400",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00495450",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00495474",
      "PARAM",
      [
        "storage",
        "002a827d",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00495400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495378.md#insn-00495400) · [`00495450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495378.md#insn-00495450) · [`00495474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495378.md#insn-00495474)
- 新版 `00495400`（命令位置の公開資料なし） · `00495450`（命令位置の公開資料なし） · `00495474`（命令位置の公開資料なし）

~~~diff
- 00495400 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 00495400 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00495400 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 00495400 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00495400 bytes 299743f9
+ 00495400 bytes 29bf43f9
- 00495450 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:728:8"]]
- 00495450 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00495450 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:778:8"]]
+ 00495450 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00495450 bytes 299743f9
+ 00495450 bytes 29bf43f9
- 00495474 ["COPY", "tmp:0:8", ["const:1e3:8"]]
- 00495474 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00495474 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00495474 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00495474 ["COPY", "tmp:0:8", ["const:27d:8"]]
+ 00495474 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00495474 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00495474 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00495474 bytes 218c0791
+ 00495474 bytes 21f40991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76e2417e4fa5b6bda2a1ed0f30859f62"></a>

### [`00495668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495668.md) → [`00495668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495668.md) _ZN5BotanrsERNSt6__ndk113basic_istreamIcNS0_11char_traitsIcEEEERNS_6BigIntE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00520650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00520/00520650.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00520650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00520/00520650.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004956b8",
      "incomplete_value": true,
      "site": "004956bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004956b8",
      "incomplete_value": true,
      "site": "004956bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
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
      "definition_site": "00495778",
      "incomplete_value": true,
      "site": "00495778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00495778",
      "incomplete_value": true,
      "site": "00495778",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004957d0",
      "incomplete_value": false,
      "site": "004957d8",
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
            "const:996:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004957d0",
      "incomplete_value": false,
      "site": "004957d8",
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
            "const:a23:8"
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
      "004956b8",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "004956b8",
      "PARAM",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00495768",
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
      "004956b8",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "004956b8",
      "PARAM",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00495768",
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

- 旧版 [`004956b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495668.md#insn-004956b8) · [`00495768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495668.md#insn-00495768) · [`004957d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495668.md#insn-004957d0)
- 新版 `004956b8`（命令位置の公開資料なし） · `00495768`（命令位置の公開資料なし） · `004957d0`（命令位置の公開資料なし）

~~~diff
- 004956b8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:df0:8"]]
- 004956b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004956b8 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:e40:8"]]
+ 004956b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004956b8 bytes 21f846f9
+ 004956b8 bytes 212047f9
- 00495768 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:728:8"]]
- 00495768 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00495768 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
+ 00495768 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00495768 bytes 299543f9
+ 00495768 bytes 29bd43f9
- 004957d0 ["COPY", "tmp:0:8", ["const:a23:8"]]
- 004957d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004957d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004957d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004957d0 ["COPY", "tmp:0:8", ["const:996:8"]]
+ 004957d0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004957d0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004957d0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004957d0 bytes 218c2891
+ 004957d0 bytes 21582691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1979c0b51d3de087290d18eeb7ceac82"></a>

### [`00495978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495978.md) → [`00495978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495978.md) FUN_00495978

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 8件 [`0047e47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0047e/0047e47c.md) [`00494d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00494/00494d38.md) [`004950f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/004950f0.md) [`0049731c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00497/0049731c.md) [`004b868c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b8/004b868c.md) · 呼出先 7件 [`0051345c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00513/0051345c.md) [`00bbacf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbacf0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 8件 [`0047e47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0047e/0047e47c.md) [`00494d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00494/00494d38.md) [`004950f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md) [`0049731c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/0049731c.md) [`004b868c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b8/004b868c.md) · 呼出先 7件 [`0051345c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00513/0051345c.md) [`00bbad34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bba/00bbad34.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00495a40",
      "incomplete_value": true,
      "site": "00495a48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00495a40",
      "incomplete_value": true,
      "site": "00495a48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00495a44",
      "incomplete_value": true,
      "site": "00495a48",
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
      "definition_site": "00495a44",
      "incomplete_value": true,
      "site": "00495a48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00495a40",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "00495a40",
      "PARAM",
      [
        "storage",
        "00c168a0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00495a44",
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
      "00495a40",
      "READ",
      [
        "storage",
        "00c1aff8",
        null,
        "pointer"
      ]
    ],
    [
      "00495a40",
      "PARAM",
      [
        "storage",
        "00c168f0",
        "_ZTISt9bad_alloc",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00495a44",
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

- 旧版 [`00495a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495978.md#insn-00495a38) · [`00495a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495978.md#insn-00495a40) · [`00495a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495978.md#insn-00495a44)
- 新版 `00495a38`（命令位置の公開資料なし） · `00495a40`（命令位置の公開資料なし） · `00495a44`（命令位置の公開資料なし）

~~~diff
- 00495a38 ["COPY", "register:4010:8", ["const:c1a000:8"]]
+ 00495a38 ["COPY", "register:4010:8", ["const:c1b000:8"]]
- 00495a38 bytes 223c00b0
+ 00495a38 bytes 223c00d0
- 00495a40 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
- 00495a40 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00495a40 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ff8:8"]]
+ 00495a40 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00495a40 bytes 21d447f9
+ 00495a40 bytes 21fc47f9
- 00495a44 ["INT_ADD", "tmp:0:8", ["register:4010:8", "const:fb0:8"]]
- 00495a44 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00495a44 ["COPY", "tmp:0:8", ["register:4010:8"]]
+ 00495a44 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00495a44 bytes 42d847f9
+ 00495a44 bytes 420040f9
~~~


<a id="compare-eb601b7492f1e23f34cf7bb3f2a41091"></a>

### [`00495a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495a74.md) → [`00495a74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495a74.md) FUN_00495a74

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 5件 [`004950f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/004950f0.md) [`00496ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/00496ee0.md) [`00497068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00497/00497068.md) [`004b44b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b4/004b44b8.md) [`004b4a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b4/004b4a30.md) · 呼出先 1件 [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 5件 [`004950f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md) [`00496ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496ee0.md) [`00497068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/00497068.md) [`004b44b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md) [`004b4a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4a30.md) · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.52% / 新版 96.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00495c1c",
      "incomplete_value": false,
      "site": "00495c3c",
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
      "definition_site": "00495c1c",
      "incomplete_value": false,
      "site": "00495c3c",
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
      "definition_site": "00495c24",
      "incomplete_value": false,
      "site": "00495c3c",
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
      "definition_site": "00495c24",
      "incomplete_value": false,
      "site": "00495c3c",
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
      "definition_site": "00495c2c",
      "incomplete_value": false,
      "site": "00495c3c",
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
            "const:4eb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495c2c",
      "incomplete_value": false,
      "site": "00495c3c",
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
            "const:460:8"
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
      "00495c1c",
      "PARAM",
      [
        "storage",
        "00296a5c",
        null,
        "string"
      ]
    ],
    [
      "00495c24",
      "PARAM",
      [
        "storage",
        "002a55b4",
        null,
        "string"
      ]
    ],
    [
      "00495c2c",
      "PARAM",
      [
        "storage",
        "002a4460",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00495c1c",
      "PARAM",
      [
        "storage",
        "002969cf",
        null,
        "string"
      ]
    ],
    [
      "00495c24",
      "PARAM",
      [
        "storage",
        "002a563f",
        null,
        "string"
      ]
    ],
    [
      "00495c2c",
      "PARAM",
      [
        "storage",
        "002a44eb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00495c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495a74.md#insn-00495c1c) · [`00495c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495a74.md#insn-00495c24) · [`00495c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495a74.md#insn-00495c2c)
- 新版 `00495c1c`（命令位置の公開資料なし） · `00495c24`（命令位置の公開資料なし） · `00495c2c`（命令位置の公開資料なし）

~~~diff
- 00495c1c ["COPY", "tmp:0:8", ["const:a5c:8"]]
- 00495c1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00495c1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00495c1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00495c1c ["COPY", "tmp:0:8", ["const:9cf:8"]]
+ 00495c1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00495c1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00495c1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00495c1c bytes 00702991
+ 00495c1c bytes 003c2791
- 00495c24 ["COPY", "tmp:0:8", ["const:5b4:8"]]
- 00495c24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00495c24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00495c24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00495c24 ["COPY", "tmp:0:8", ["const:63f:8"]]
+ 00495c24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00495c24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00495c24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00495c24 bytes 21d01691
+ 00495c24 bytes 21fc1891
- 00495c2c ["COPY", "tmp:0:8", ["const:460:8"]]
- 00495c2c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00495c2c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00495c2c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00495c2c ["COPY", "tmp:0:8", ["const:4eb:8"]]
+ 00495c2c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00495c2c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00495c2c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00495c2c bytes 42801191
+ 00495c2c bytes 42ac1391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3514447cdc4faceb11dd6415e3661af8"></a>

### [`00495c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495c94.md) → [`00495c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495c94.md) FUN_00495c94

採用 · 移動量 `+0x0` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`004950f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/004950f0.md) [`00495e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495e3c.md) [`004b44b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b4/004b44b8.md) [`004b4a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004b4/004b4a30.md) · 呼出先 1件 [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 4件 [`004950f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/004950f0.md) [`00495e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00495/00495e3c.md) [`004b44b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b44b8.md) [`004b4a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004b4/004b4a30.md) · 呼出先 1件 [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.23% / 新版 96.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00495e18",
      "incomplete_value": false,
      "site": "00495e38",
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
      "definition_site": "00495e18",
      "incomplete_value": false,
      "site": "00495e38",
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
      "definition_site": "00495e20",
      "incomplete_value": false,
      "site": "00495e38",
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
      "definition_site": "00495e20",
      "incomplete_value": false,
      "site": "00495e38",
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
      "definition_site": "00495e28",
      "incomplete_value": false,
      "site": "00495e38",
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
            "const:53e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00495e28",
      "incomplete_value": false,
      "site": "00495e38",
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
            "const:4b3:8"
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
      "00495e18",
      "PARAM",
      [
        "storage",
        "00296a5c",
        null,
        "string"
      ]
    ],
    [
      "00495e20",
      "PARAM",
      [
        "storage",
        "002a55b4",
        null,
        "string"
      ]
    ],
    [
      "00495e28",
      "PARAM",
      [
        "storage",
        "0029f4b3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00495e18",
      "PARAM",
      [
        "storage",
        "002969cf",
        null,
        "string"
      ]
    ],
    [
      "00495e20",
      "PARAM",
      [
        "storage",
        "002a563f",
        null,
        "string"
      ]
    ],
    [
      "00495e28",
      "PARAM",
      [
        "storage",
        "0029f53e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00495e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495c94.md#insn-00495e18) · [`00495e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495c94.md#insn-00495e20) · [`00495e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00495/00495c94.md#insn-00495e28)
- 新版 `00495e18`（命令位置の公開資料なし） · `00495e20`（命令位置の公開資料なし） · `00495e28`（命令位置の公開資料なし）

~~~diff
- 00495e18 ["COPY", "tmp:0:8", ["const:a5c:8"]]
- 00495e18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00495e18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00495e18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00495e18 ["COPY", "tmp:0:8", ["const:9cf:8"]]
+ 00495e18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00495e18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00495e18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00495e18 bytes 00702991
+ 00495e18 bytes 003c2791
- 00495e20 ["COPY", "tmp:0:8", ["const:5b4:8"]]
- 00495e20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00495e20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00495e20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00495e20 ["COPY", "tmp:0:8", ["const:63f:8"]]
+ 00495e20 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00495e20 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00495e20 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00495e20 bytes 21d01691
+ 00495e20 bytes 21fc1891
- 00495e28 ["COPY", "tmp:0:8", ["const:4b3:8"]]
- 00495e28 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00495e28 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00495e28 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00495e28 ["COPY", "tmp:0:8", ["const:53e:8"]]
+ 00495e28 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00495e28 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00495e28 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00495e28 bytes 42cc1291
+ 00495e28 bytes 42f81491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0c4c151a88eae36c6db9687d98dcc34"></a>

### [`004967a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/004967a4.md) → [`004967a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/004967a4.md) _ZN5BotanrmERKNS_6BigIntES2_

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbe00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbe00.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdbe50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe50.md) · 呼出先 11件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, call_target, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.30% / 新版 96.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_value` 1件

アドレスに依存する影響 `call_target` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00496858",
      "incomplete_value": true,
      "site": "0049685c",
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
      "definition_site": "00496858",
      "incomplete_value": true,
      "site": "0049685c",
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
    "ordinal": 12,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049687c",
      "incomplete_value": true,
      "site": "00496880",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049687c",
      "incomplete_value": true,
      "site": "00496880",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00496908",
      "incomplete_value": true,
      "site": "00496908",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00496908",
      "incomplete_value": true,
      "site": "00496908",
      "value": [
        "LOAD",
        "8",
        [
          [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00496844",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ],
    [
      "0049685c",
      "DATA",
      [
        "storage",
        "00becc50",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "0049687c",
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
      "00496844",
      "READ",
      [
        "storage",
        "00c1b010",
        null,
        "pointer"
      ]
    ],
    [
      "0049685c",
      "DATA",
      [
        "storage",
        "00becca0",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "0049687c",
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

- 旧版 [`00496830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/004967a4.md#insn-00496830) · [`00496844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/004967a4.md#insn-00496844) · [`00496870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/004967a4.md#insn-00496870)
- 新版 `00496830`（命令位置の公開資料なし） · `00496844`（命令位置の公開資料なし） · `00496870`（命令位置の公開資料なし）

~~~diff
- 00496830 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 00496830 ["COPY", "register:4048:8", ["const:c1b000:8"]]
- 00496830 bytes 293c0090
+ 00496830 bytes 293c00b0
- 00496844 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fc0:8"]]
- 00496844 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00496844 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:10:8"]]
+ 00496844 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00496844 bytes 29e147f9
+ 00496844 bytes 290940f9
- 00496870 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 00496870 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 00496870 bytes 213c0090
+ 00496870 bytes 213c00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a9410d5cf2f7f0086d0137a6a79b9b5"></a>

### [`00496a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/00496a24.md) → [`00496a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496a24.md) _ZN5Botan6BigIntrMEj

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00498c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/00498c94.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051da48.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00498c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498c94.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`0051da48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051da48.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.95% / 新版 96.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00496c20",
      "incomplete_value": true,
      "site": "00496c24",
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
      "definition_site": "00496c20",
      "incomplete_value": true,
      "site": "00496c24",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00496c28",
      "incomplete_value": true,
      "site": "00496c2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00496c28",
      "incomplete_value": true,
      "site": "00496c2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00496c00",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ],
    [
      "00496c24",
      "DATA",
      [
        "storage",
        "00becc50",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00496c28",
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
      "00496c00",
      "READ",
      [
        "storage",
        "00c1b010",
        null,
        "pointer"
      ]
    ],
    [
      "00496c24",
      "DATA",
      [
        "storage",
        "00becca0",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "00496c28",
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

- 旧版 [`00496bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/00496a24.md#insn-00496bec) · [`00496c00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/00496a24.md#insn-00496c00) · [`00496c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/00496a24.md#insn-00496c0c)
- 新版 `00496bec`（命令位置の公開資料なし） · `00496c00`（命令位置の公開資料なし） · `00496c0c`（命令位置の公開資料なし）

~~~diff
- 00496bec ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 00496bec ["COPY", "register:4048:8", ["const:c1b000:8"]]
- 00496bec bytes 293c0090
+ 00496bec bytes 293c00b0
- 00496c00 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fc0:8"]]
- 00496c00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00496c00 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:10:8"]]
+ 00496c00 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00496c00 bytes 29e147f9
+ 00496c00 bytes 290940f9
- 00496c0c ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 00496c0c ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 00496c0c bytes 213c0090
+ 00496c0c bytes 213c00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ba1f6347eb2b31b23e78d85b5f2e481"></a>

### [`004975c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00497/004975c0.md) → [`004975c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/004975c0.md) _ZN5BotanrmERKNS_6BigIntEj

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbe30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbe30.md) · 呼出先 4件 [`00498c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/00498c94.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdbe80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe80.md) · 呼出先 4件 [`00498c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498c94.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.51% / 新版 95.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00497714",
      "incomplete_value": true,
      "site": "00497718",
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
      "definition_site": "00497714",
      "incomplete_value": true,
      "site": "00497718",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049771c",
      "incomplete_value": true,
      "site": "00497720",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049771c",
      "incomplete_value": true,
      "site": "00497720",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004976f4",
      "READ",
      [
        "storage",
        "00c1afc0",
        null,
        "pointer"
      ]
    ],
    [
      "00497718",
      "DATA",
      [
        "storage",
        "00becc50",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "0049771c",
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
      "004976f4",
      "READ",
      [
        "storage",
        "00c1b010",
        null,
        "pointer"
      ]
    ],
    [
      "00497718",
      "DATA",
      [
        "storage",
        "00becca0",
        null,
        "undefined1[40]"
      ]
    ],
    [
      "0049771c",
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

- 旧版 [`004976e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00497/004975c0.md#insn-004976e0) · [`004976f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00497/004975c0.md#insn-004976f4) · [`00497700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00497/004975c0.md#insn-00497700)
- 新版 `004976e0`（命令位置の公開資料なし） · `004976f4`（命令位置の公開資料なし） · `00497700`（命令位置の公開資料なし）

~~~diff
- 004976e0 ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 004976e0 ["COPY", "register:4048:8", ["const:c1b000:8"]]
- 004976e0 bytes 093c00f0
+ 004976e0 bytes 293c0090
- 004976f4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fc0:8"]]
- 004976f4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 004976f4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:10:8"]]
+ 004976f4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 004976f4 bytes 29e147f9
+ 004976f4 bytes 290940f9
- 00497700 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 00497700 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 00497700 bytes 013c00f0
+ 00497700 bytes 213c0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1aab7422f660bcb5710f2ca8e9aa7b3e"></a>

### [`00498254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/00498254.md) → [`00498254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498254.md) _ZNK5Botan6BigInt13get_substringEmm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbe70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbe70.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 1件 [`00bdbec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbec0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.26% / 新版 99.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "0049845c",
      "incomplete_value": true,
      "site": "00498468",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "0049845c",
      "incomplete_value": true,
      "site": "00498468",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "0049845c",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "0049845c",
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
      "0049845c",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "0049845c",
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

- 旧版 [`0049845c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/00498254.md#insn-0049845c)
- 新版 `0049845c`（命令位置の公開資料なし）

~~~diff
- 0049845c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 0049845c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 0049845c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 0049845c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 0049845c bytes 217847f9
+ 0049845c bytes 21a047f9
~~~


<a id="compare-61b08ec4dc0da00d58b3fd5d0842f287"></a>

### [`004984bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/004984bc.md) → [`004984bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004984bc.md) _ZNK5Botan6BigInt9to_u32bitEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 0件  · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.04% / 新版 98.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004985e0",
      "incomplete_value": true,
      "site": "004985ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "004985e0",
      "incomplete_value": true,
      "site": "004985ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
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
      "definition_site": "00498644",
      "incomplete_value": true,
      "site": "00498650",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00498644",
      "incomplete_value": true,
      "site": "00498650",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
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
      "004985e0",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ],
    [
      "004985e0",
      "PARAM",
      [
        "storage",
        "00be92e0",
        "_ZTIN5Botan14Encoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00498644",
      "READ",
      [
        "storage",
        "00c1af58",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "004985e0",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ],
    [
      "004985e0",
      "PARAM",
      [
        "storage",
        "00be9330",
        "_ZTIN5Botan14Encoding_ErrorE",
        "pointer __((offset(0x10)))"
      ]
    ],
    [
      "00498644",
      "READ",
      [
        "storage",
        "00c1afa8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004985e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/004984bc.md#insn-004985e0) · [`00498644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/004984bc.md#insn-00498644)
- 新版 `004985e0`（命令位置の公開資料なし） · `00498644`（命令位置の公開資料なし）

~~~diff
- 004985e0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
- 004985e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004985e0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
+ 004985e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004985e0 bytes 21ac47f9
+ 004985e0 bytes 21d447f9
- 00498644 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f58:8"]]
- 00498644 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00498644 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fa8:8"]]
+ 00498644 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00498644 bytes 21ac47f9
+ 00498644 bytes 21d447f9
~~~


<a id="compare-63b39585aad6450ed8d22e377347e5a1"></a>

### [`00498858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/00498858.md) → [`00498858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498858.md) _ZN5Botan6BigInt17const_time_lookupERNSt6__ndk16vectorIjNS_16secure_allocatorIjEEEERKNS2_IS0_NS1_9allocatorIS0_EEEEm

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdbe80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbe80.md) · 呼出先 2件 [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 1件 [`00bdbed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbed0.md) · 呼出先 2件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.02% / 新版 98.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004989c8",
      "incomplete_value": false,
      "site": "004989e8",
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
            "const:5dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004989c8",
      "incomplete_value": false,
      "site": "004989e8",
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
            "const:542:8"
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
      "definition_site": "004989e0",
      "incomplete_value": false,
      "site": "004989e8",
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
            "const:3d2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004989e0",
      "incomplete_value": false,
      "site": "004989e8",
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
    "ordinal": 1,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "004989c8",
      "PARAM",
      [
        "storage",
        "002a7542",
        null,
        "string"
      ]
    ],
    [
      "004989e0",
      "PARAM",
      [
        "storage",
        "002918e1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "004989c8",
      "PARAM",
      [
        "storage",
        "002a75dc",
        null,
        "string"
      ]
    ],
    [
      "004989e0",
      "PARAM",
      [
        "storage",
        "0029c3d2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004989c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/00498858.md#insn-004989c8) · [`004989dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/00498858.md#insn-004989dc) · [`004989e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/00498858.md#insn-004989e0)
- 新版 `004989c8`（命令位置の公開資料なし） · `004989dc`（命令位置の公開資料なし） · `004989e0`（命令位置の公開資料なし）

~~~diff
- 004989c8 ["COPY", "tmp:0:8", ["const:542:8"]]
- 004989c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004989c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004989c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004989c8 ["COPY", "tmp:0:8", ["const:5dc:8"]]
+ 004989c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004989c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004989c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004989c8 bytes 00081591
+ 004989c8 bytes 00701791
- 004989dc ["COPY", "register:4018:8", ["const:291000:8"]]
+ 004989dc ["COPY", "register:4018:8", ["const:29c000:8"]]
- 004989dc bytes c3efffb0
+ 004989dc bytes 23f0ff90
- 004989e0 ["COPY", "tmp:0:8", ["const:8e1:8"]]
- 004989e0 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 004989e0 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 004989e0 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 004989e0 ["COPY", "tmp:0:8", ["const:3d2:8"]]
+ 004989e0 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 004989e0 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 004989e0 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 004989e0 bytes 63842391
+ 004989e0 bytes 63480f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5433a1584de3a2090e9580a52099967b"></a>

### [`004989ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/004989ec.md) → [`004989ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/004989ec.md) FUN_004989ec

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00493850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00493/00493850.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7c0.md) [`00bdba80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdba80.md) [`00bdbca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbca0.md) [`00bdbda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbda0.md)
- 新版 呼出元 1件 [`00493850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493850.md) · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb810.md) [`00bdbad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbad0.md) [`00bdbcf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcf0.md) [`00bdbdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbdf0.md)

変更の種類 call_target, constant, operands_and_dependencies

命令の説明率　旧版 96.13% / 新版 96.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_target` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_target",
    "new": {
      "definition_site": "00498b7c",
      "incomplete_value": true,
      "site": "00498b7c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00498b7c",
      "incomplete_value": true,
      "site": "00498b7c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00498c0c",
      "incomplete_value": true,
      "site": "00498c0c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00498c0c",
      "incomplete_value": true,
      "site": "00498c0c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00498c3c",
      "incomplete_value": true,
      "site": "00498c3c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00498c3c",
      "incomplete_value": true,
      "site": "00498c3c",
      "value": [
        "LOAD",
        "8",
        [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00498b6c",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00498bfc",
      "READ",
      [
        "storage",
        "00bea728",
        null,
        "pointer"
      ]
    ],
    [
      "00498c2c",
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
      "00498b6c",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00498bfc",
      "READ",
      [
        "storage",
        "00bea778",
        null,
        "pointer"
      ]
    ],
    [
      "00498c2c",
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

- 旧版 [`00498b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/004989ec.md#insn-00498b6c) · [`00498bfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/004989ec.md#insn-00498bfc) · [`00498c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/004989ec.md#insn-00498c2c)
- 新版 `00498b6c`（命令位置の公開資料なし） · `00498bfc`（命令位置の公開資料なし） · `00498c2c`（命令位置の公開資料なし）

~~~diff
- 00498b6c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 00498b6c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00498b6c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 00498b6c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00498b6c bytes 099743f9
+ 00498b6c bytes 09bf43f9
- 00498bfc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 00498bfc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00498bfc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 00498bfc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00498bfc bytes 099743f9
+ 00498bfc bytes 09bf43f9
- 00498c2c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:728:8"]]
- 00498c2c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00498c2c ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:778:8"]]
+ 00498c2c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00498c2c bytes 099743f9
+ 00498c2c bytes 09bf43f9
~~~


<a id="compare-cc0d2a72f3be8455db0fb7aa8831b4f0"></a>

### [`00498c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/00498c94.md) → [`00498c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00498/00498c94.md) FUN_00498c94

採用 · 移動量 `+0x0` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00493850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00493/00493850.md) [`00496a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00496/00496a24.md) [`004975c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00497/004975c0.md) [`004bb030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/004bb/004bb030.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md) [`00bdb070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb070.md)
- 新版 呼出元 4件 [`00493850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00493/00493850.md) [`00496a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00496/00496a24.md) [`004975c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00497/004975c0.md) [`004bb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004bb/004bb030.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md) [`00bdb0c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.74% / 新版 95.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00498d00",
      "incomplete_value": false,
      "site": "00498d08",
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
            "const:4f7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00498d00",
      "incomplete_value": false,
      "site": "00498d08",
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
            "const:46c:8"
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
      "definition_site": "00498d3c",
      "incomplete_value": true,
      "site": "00498d48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00498d3c",
      "incomplete_value": true,
      "site": "00498d48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00498d00",
      "PARAM",
      [
        "storage",
        "002a446c",
        null,
        "string"
      ]
    ],
    [
      "00498d3c",
      "READ",
      [
        "storage",
        "00c1aef0",
        null,
        "pointer"
      ]
    ],
    [
      "00498d3c",
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
      "00498d00",
      "PARAM",
      [
        "storage",
        "002a44f7",
        null,
        "string"
      ]
    ],
    [
      "00498d3c",
      "READ",
      [
        "storage",
        "00c1af40",
        null,
        "pointer"
      ]
    ],
    [
      "00498d3c",
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

- 旧版 [`00498d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/00498c94.md#insn-00498d00) · [`00498d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00498/00498c94.md#insn-00498d3c)
- 新版 `00498d00`（命令位置の公開資料なし） · `00498d3c`（命令位置の公開資料なし）

~~~diff
- 00498d00 ["COPY", "tmp:0:8", ["const:46c:8"]]
- 00498d00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00498d00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00498d00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00498d00 ["COPY", "tmp:0:8", ["const:4f7:8"]]
+ 00498d00 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00498d00 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00498d00 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00498d00 bytes 21b01191
+ 00498d00 bytes 21dc1391
- 00498d3c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ef0:8"]]
- 00498d3c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00498d3c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:f40:8"]]
+ 00498d3c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00498d3c bytes 217847f9
+ 00498d3c bytes 21a047f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4cbed81d9b254ee35de6db4ab29046ac"></a>

### [`00499128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499128.md) → [`00499128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499128.md) _ZN5Botan11BlockCipher15create_or_throwERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_

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
      "definition_site": "004991a0",
      "incomplete_value": false,
      "site": "004991a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:72a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004991a0",
      "incomplete_value": false,
      "site": "004991a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:7b7:8"
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
      "definition_site": "004991e0",
      "incomplete_value": true,
      "site": "004991ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "004991e0",
      "incomplete_value": true,
      "site": "004991ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "004991a0",
      "PARAM",
      [
        "storage",
        "002947b7",
        null,
        "string"
      ]
    ],
    [
      "004991e0",
      "READ",
      [
        "storage",
        "00c1afe8",
        null,
        "pointer"
      ]
    ],
    [
      "004991e0",
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
      "004991a0",
      "PARAM",
      [
        "storage",
        "0029472a",
        null,
        "string"
      ]
    ],
    [
      "004991e0",
      "READ",
      [
        "storage",
        "00c1b038",
        null,
        "pointer"
      ]
    ],
    [
      "004991e0",
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

- 旧版 [`004991a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499128.md#insn-004991a0) · [`004991d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499128.md#insn-004991d4) · [`004991e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499128.md#insn-004991e0)
- 新版 `004991a0`（命令位置の公開資料なし） · `004991d4`（命令位置の公開資料なし） · `004991e0`（命令位置の公開資料なし）

~~~diff
- 004991a0 ["COPY", "tmp:0:8", ["const:7b7:8"]]
- 004991a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004991a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004991a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004991a0 ["COPY", "tmp:0:8", ["const:72a:8"]]
+ 004991a0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004991a0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004991a0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004991a0 bytes 21dc1e91
+ 004991a0 bytes 21a81c91
- 004991d4 ["COPY", "register:4008:8", ["const:c1a000:8"]]
+ 004991d4 ["COPY", "register:4008:8", ["const:c1b000:8"]]
- 004991d4 bytes 013c00b0
+ 004991d4 bytes 013c00d0
- 004991e0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:fe8:8"]]
- 004991e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 004991e0 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:38:8"]]
+ 004991e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 004991e0 bytes 21f447f9
+ 004991e0 bytes 211c40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc00e0e660386e212ee05e8602142faf"></a>

### [`004994e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/004994e0.md) → [`004994e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/004994e0.md) _ZN5Botan8CBC_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbec0.md) · 呼出先 9件 [`00483974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00483/00483974.md) [`00490630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00512/00512990.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb050.md)
- 新版 呼出元 1件 [`00bdbf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf10.md) · 呼出先 9件 [`00483974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00483/00483974.md) [`00490630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00490/00490630.md) [`00512990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00512/00512990.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.55% / 新版 94.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00499518",
      "incomplete_value": true,
      "site": "00499518",
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
      "definition_site": "00499518",
      "incomplete_value": true,
      "site": "00499518",
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
      "definition_site": "004995e8",
      "incomplete_value": false,
      "site": "004995f0",
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
            "const:be5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004995e8",
      "incomplete_value": false,
      "site": "004995f0",
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
            "const:c72:8"
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
      "definition_site": "00499634",
      "incomplete_value": false,
      "site": "0049963c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00499634",
      "incomplete_value": false,
      "site": "0049963c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2a2000:8"
          ],
          [
            "leaf",
            "const:2cd:8"
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
      "00499508",
      "READ",
      [
        "storage",
        "00c1aff0",
        null,
        "pointer"
      ]
    ],
    [
      "00499518",
      "DATA",
      [
        "storage",
        "00be9410",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004995e8",
      "PARAM",
      [
        "storage",
        "00299c72",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00499508",
      "READ",
      [
        "storage",
        "00c1b040",
        null,
        "pointer"
      ]
    ],
    [
      "00499518",
      "DATA",
      [
        "storage",
        "00be9460",
        null,
        "undefined1[160]"
      ]
    ],
    [
      "004995e8",
      "PARAM",
      [
        "storage",
        "00299be5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`004994fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/004994e0.md#insn-004994fc) · [`00499508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/004994e0.md#insn-00499508) · [`004995e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/004994e0.md#insn-004995e8)
- 新版 `004994fc`（命令位置の公開資料なし） · `00499508`（命令位置の公開資料なし） · `004995e8`（命令位置の公開資料なし）

~~~diff
- 004994fc ["COPY", "register:4048:8", ["const:c1a000:8"]]
+ 004994fc ["COPY", "register:4048:8", ["const:c1b000:8"]]
- 004994fc bytes 093c00b0
+ 004994fc bytes 093c00d0
- 00499508 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ff0:8"]]
- 00499508 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00499508 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:40:8"]]
+ 00499508 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00499508 bytes 29f947f9
+ 00499508 bytes 292140f9
- 004995e8 ["COPY", "tmp:0:8", ["const:c72:8"]]
- 004995e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004995e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004995e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004995e8 ["COPY", "tmp:0:8", ["const:be5:8"]]
+ 004995e8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004995e8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004995e8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004995e8 bytes 21c83191
+ 004995e8 bytes 21942f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6640c4e7af7373f99b5c75cd33289929"></a>

### [`00499860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499860.md) → [`00499860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00499/00499860.md) _ZNK5Botan8CBC_Mode4nameEv

採用 · 移動量 `+0x0` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdbed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbed0.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0d0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb7b0.md)
- 新版 呼出元 1件 [`00bdbf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf20.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb120.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb800.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.37% / 新版 95.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004998a8",
      "incomplete_value": false,
      "site": "004998b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:737:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004998a8",
      "incomplete_value": false,
      "site": "004998b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:294000:8"
          ],
          [
            "leaf",
            "const:7c4:8"
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
      "definition_site": "004999e8",
      "incomplete_value": false,
      "site": "00499a08",
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
            "const:6c9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "004999e8",
      "incomplete_value": false,
      "site": "00499a08",
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
            "const:63e:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "004999f0",
      "incomplete_value": false,
      "site": "00499a08",
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
      "definition_site": "004999f0",
      "incomplete_value": false,
      "site": "00499a08",
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
      "004998a8",
      "PARAM",
      [
        "storage",
        "002947c4",
        null,
        "string"
      ]
    ],
    [
      "004999e8",
      "PARAM",
      [
        "storage",
        "0029c63e",
        null,
        "string"
      ]
    ],
    [
      "004999f0",
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
      "004998a8",
      "PARAM",
      [
        "storage",
        "00294737",
        null,
        "string"
      ]
    ],
    [
      "004999e8",
      "PARAM",
      [
        "storage",
        "0029c6c9",
        null,
        "string"
      ]
    ],
    [
      "004999f0",
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

- 旧版 [`004998a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499860.md#insn-004998a8) · [`004999e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499860.md#insn-004999e8) · [`004999f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00499/00499860.md#insn-004999f0)
- 新版 `004998a8`（命令位置の公開資料なし） · `004999e8`（命令位置の公開資料なし） · `004999f0`（命令位置の公開資料なし）

~~~diff
- 004998a8 ["COPY", "tmp:0:8", ["const:7c4:8"]]
- 004998a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004998a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004998a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004998a8 ["COPY", "tmp:0:8", ["const:737:8"]]
+ 004998a8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004998a8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004998a8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004998a8 bytes 21101f91
+ 004998a8 bytes 21dc1c91
- 004999e8 ["COPY", "tmp:0:8", ["const:63e:8"]]
- 004999e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 004999e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 004999e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 004999e8 ["COPY", "tmp:0:8", ["const:6c9:8"]]
+ 004999e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 004999e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 004999e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 004999e8 bytes 00f81891
+ 004999e8 bytes 00241b91
- 004999f0 ["COPY", "tmp:0:8", ["const:866:8"]]
- 004999f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 004999f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 004999f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 004999f0 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 004999f0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 004999f0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 004999f0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 004999f0 bytes 21982191
+ 004999f0 bytes 21641f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

