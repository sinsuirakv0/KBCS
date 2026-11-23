# v15.7.3 → v15.7.4 · 最優先の変更候補 (77)

[一覧の目次](README.md)

<a id="compare-c6ad72c8b3382cc3c0256fa5921f883a"></a>

### [`00ba3f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3f4c.md) → [`00ba3f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba3f90.md) FUN_00ba3f90

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba3fb4",
      "incomplete_value": true,
      "site": "00ba3fb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3f70",
      "incomplete_value": true,
      "site": "00ba3f74",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d70:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba3fc0",
      "incomplete_value": true,
      "site": "00ba3fc4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3f7c",
      "incomplete_value": true,
      "site": "00ba3f80",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba3fe8",
      "incomplete_value": true,
      "site": "00ba3fec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba3fa4",
      "incomplete_value": true,
      "site": "00ba3fa8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d70:8"
              ]
            ]
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
      "00ba3fb4",
      "READ",
      [
        "storage",
        "00c1bd70",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3fb8",
      "DATA",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3fbc",
      "READ",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba3fb4",
      "READ",
      [
        "storage",
        "00c1bdc0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba3fb8",
      "DATA",
      [
        "storage",
        "010a2910",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba3fbc",
      "READ",
      [
        "storage",
        "010a2910",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba3fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3f4c.md#insn-00ba3fa8) · [`00ba3f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3f4c.md#insn-00ba3f70) · [`00ba3f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba3f4c.md#insn-00ba3f98)
- 新版 `00ba3fec`（命令位置の公開資料なし） · `00ba3fb4`（命令位置の公開資料なし） · `00ba3fdc`（命令位置の公開資料なし）

~~~diff
- 00ba3fa8 ["INT_ADD", "register:40f0:8", ["const:ba3fa8:8", "const:4:8"]]
- 00ba3fa8 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba3fec ["INT_ADD", "register:40f0:8", ["const:ba3fec:8", "const:4:8"]]
+ 00ba3fec ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba3fa8 bytes baf30094
+ 00ba3fec bytes bdf30094
- 00ba3f70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d70:8"]]
- 00ba3f70 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba3fb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc0:8"]]
+ 00ba3fb4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba3f70 bytes 94ba46f9
+ 00ba3fb4 bytes 94e246f9
- 00ba3f98 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba3fdc ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba3f98 bytes 628b0a10
+ 00ba3fdc bytes 628b0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7587278708756b7f51996e971614a63"></a>

### [`00ba4078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4078.md) → [`00ba40bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba40bc.md) FUN_00ba40bc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 1件 [`00be18b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18b0.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 1件 [`00be1900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1900.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba40ec",
      "incomplete_value": true,
      "site": "00ba40ec",
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
      "definition_site": "00ba40a8",
      "incomplete_value": true,
      "site": "00ba40a8",
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
      "00ba40dc",
      "READ",
      [
        "storage",
        "00c1bf28",
        null,
        "pointer"
      ]
    ],
    [
      "00ba40ec",
      "DATA",
      [
        "storage",
        "00c15718",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00ba40dc",
      "READ",
      [
        "storage",
        "00c1bf78",
        null,
        "pointer"
      ]
    ],
    [
      "00ba40ec",
      "DATA",
      [
        "storage",
        "00c15768",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba4098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4078.md#insn-00ba4098) · [`00ba409c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4078.md#insn-00ba409c) · [`00ba40a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4078.md#insn-00ba40a0)
- 新版 `00ba40dc`（命令位置の公開資料なし）

~~~diff
- 00ba4098 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f28:8"]]
- 00ba4098 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba40dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f78:8"]]
+ 00ba40dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba4098 bytes 089547f9
+ 00ba40dc bytes 08bd47f9
- 00ba409c ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00ba409c bytes f50300aa
- 00ba40a0 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00ba40a0 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b363be8b7e61d2380b66af049a5358c4"></a>

### [`00ba415c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba415c.md) → [`00ba41a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba41a0.md) FUN_00ba41a0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba41c4",
      "incomplete_value": true,
      "site": "00ba41c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba4180",
      "incomplete_value": true,
      "site": "00ba4184",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d68:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba41d0",
      "incomplete_value": true,
      "site": "00ba41d4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba418c",
      "incomplete_value": true,
      "site": "00ba4190",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba41f8",
      "incomplete_value": true,
      "site": "00ba41fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba41b4",
      "incomplete_value": true,
      "site": "00ba41b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d68:8"
              ]
            ]
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
      "00ba41c4",
      "READ",
      [
        "storage",
        "00c1bd68",
        null,
        "pointer"
      ]
    ],
    [
      "00ba41c8",
      "DATA",
      [
        "storage",
        "010a28e0",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba41cc",
      "READ",
      [
        "storage",
        "010a28e0",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba41c4",
      "READ",
      [
        "storage",
        "00c1bdb8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba41c8",
      "DATA",
      [
        "storage",
        "010a2920",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba41cc",
      "READ",
      [
        "storage",
        "010a2920",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba41b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba415c.md#insn-00ba41b8) · [`00ba4180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba415c.md#insn-00ba4180) · [`00ba41a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba415c.md#insn-00ba41a8)
- 新版 `00ba41fc`（命令位置の公開資料なし） · `00ba41c4`（命令位置の公開資料なし） · `00ba41ec`（命令位置の公開資料なし）

~~~diff
- 00ba41b8 ["INT_ADD", "register:40f0:8", ["const:ba41b8:8", "const:4:8"]]
- 00ba41b8 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba41fc ["INT_ADD", "register:40f0:8", ["const:ba41fc:8", "const:4:8"]]
+ 00ba41fc ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba41b8 bytes 36f30094
+ 00ba41fc bytes 39f30094
- 00ba4180 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
- 00ba4180 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba41c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db8:8"]]
+ 00ba41c4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba4180 bytes 94b646f9
+ 00ba41c4 bytes 94de46f9
- 00ba41a8 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba41ec ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba41a8 bytes e27a0a10
+ 00ba41ec bytes e27a0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-861264fe36f0d5679c0defab56b25392"></a>

### [`00ba4288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4288.md) → [`00ba42cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba42cc.md) FUN_00ba42cc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 1件 [`00be18c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18c0.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 1件 [`00be1910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1910.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba42fc",
      "incomplete_value": true,
      "site": "00ba42fc",
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
      "definition_site": "00ba42b8",
      "incomplete_value": true,
      "site": "00ba42b8",
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
      "00ba42ec",
      "READ",
      [
        "storage",
        "00c1bf30",
        null,
        "pointer"
      ]
    ],
    [
      "00ba42fc",
      "DATA",
      [
        "storage",
        "00c157a0",
        null,
        "undefined1[112]"
      ]
    ]
  ],
  "added": [
    [
      "00ba42ec",
      "READ",
      [
        "storage",
        "00c1bf80",
        null,
        "pointer"
      ]
    ],
    [
      "00ba42fc",
      "DATA",
      [
        "storage",
        "00c157f0",
        null,
        "undefined1[112]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba42a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4288.md#insn-00ba42a8) · [`00ba42ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4288.md#insn-00ba42ac) · [`00ba42b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4288.md#insn-00ba42b0)
- 新版 `00ba42ec`（命令位置の公開資料なし）

~~~diff
- 00ba42a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f30:8"]]
- 00ba42a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba42ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f80:8"]]
+ 00ba42ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba42a8 bytes 089947f9
+ 00ba42ec bytes 08c147f9
- 00ba42ac ["COPY", "register:40a8:8", ["register:4000:8"]]
- 00ba42ac bytes f50300aa
- 00ba42b0 ["COPY", "register:4098:8", ["register:4000:8"]]
- 00ba42b0 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-281a5038a9af8d033898c76fdf8c501f"></a>

### [`00ba436c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba436c.md) → [`00ba43b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba43b0.md) FUN_00ba43b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba43d4",
      "incomplete_value": true,
      "site": "00ba43d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba4390",
      "incomplete_value": true,
      "site": "00ba4394",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba43e0",
      "incomplete_value": true,
      "site": "00ba43e4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba439c",
      "incomplete_value": true,
      "site": "00ba43a0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba4408",
      "incomplete_value": true,
      "site": "00ba440c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba43c4",
      "incomplete_value": true,
      "site": "00ba43c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b0:8"
              ]
            ]
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
      "00ba43d4",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba43d8",
      "DATA",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba43dc",
      "READ",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba43d4",
      "READ",
      [
        "storage",
        "00c1b500",
        null,
        "pointer"
      ]
    ],
    [
      "00ba43d8",
      "DATA",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba43dc",
      "READ",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba43c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba436c.md#insn-00ba43c8) · [`00ba4390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba436c.md#insn-00ba4390) · [`00ba43b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba436c.md#insn-00ba43b8)
- 新版 `00ba440c`（命令位置の公開資料なし） · `00ba43d4`（命令位置の公開資料なし） · `00ba43fc`（命令位置の公開資料なし）

~~~diff
- 00ba43c8 ["INT_ADD", "register:40f0:8", ["const:ba43c8:8", "const:4:8"]]
- 00ba43c8 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba440c ["INT_ADD", "register:40f0:8", ["const:ba440c:8", "const:4:8"]]
+ 00ba440c ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba43c8 bytes b2f20094
+ 00ba440c bytes b5f20094
- 00ba4390 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4b0:8"]]
- 00ba4390 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba43d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:500:8"]]
+ 00ba43d4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba4390 bytes 945a42f9
+ 00ba43d4 bytes 948242f9
- 00ba43b8 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba43fc ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba43b8 bytes 626a0a10
+ 00ba43fc bytes 626a0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27689be3a87802f7eccb26b2e1a77a0b"></a>

### [`00ba4498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4498.md) → [`00ba44dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba44dc.md) FUN_00ba44dc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba4500",
      "incomplete_value": true,
      "site": "00ba4504",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba44bc",
      "incomplete_value": true,
      "site": "00ba44c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba450c",
      "incomplete_value": true,
      "site": "00ba4510",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba44c8",
      "incomplete_value": true,
      "site": "00ba44cc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba4534",
      "incomplete_value": true,
      "site": "00ba4538",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba44f0",
      "incomplete_value": true,
      "site": "00ba44f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
              ]
            ]
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
      "00ba4500",
      "READ",
      [
        "storage",
        "00c1be70",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4504",
      "DATA",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba4508",
      "READ",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba4500",
      "READ",
      [
        "storage",
        "00c1bec0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4504",
      "DATA",
      [
        "storage",
        "010a28c0",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba4508",
      "READ",
      [
        "storage",
        "010a28c0",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba44f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4498.md#insn-00ba44f4) · [`00ba44bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4498.md#insn-00ba44bc) · [`00ba44e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4498.md#insn-00ba44e4)
- 新版 `00ba4538`（命令位置の公開資料なし） · `00ba4500`（命令位置の公開資料なし） · `00ba4528`（命令位置の公開資料なし）

~~~diff
- 00ba44f4 ["INT_ADD", "register:40f0:8", ["const:ba44f4:8", "const:4:8"]]
- 00ba44f4 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba4538 ["INT_ADD", "register:40f0:8", ["const:ba4538:8", "const:4:8"]]
+ 00ba4538 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba44f4 bytes 67f20094
+ 00ba4538 bytes 6af20094
- 00ba44bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e70:8"]]
- 00ba44bc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba4500 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ec0:8"]]
+ 00ba4500 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba44bc bytes 943a47f9
+ 00ba4500 bytes 946247f9
- 00ba44e4 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba4528 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba44e4 bytes 02610a10
+ 00ba4528 bytes 02610a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2863266895fdb795254363fa66fc84c"></a>

### [`00ba45c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba45c4.md) → [`00ba4608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4608.md) FUN_00ba4608

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba462c",
      "incomplete_value": true,
      "site": "00ba4630",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba45e8",
      "incomplete_value": true,
      "site": "00ba45ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba4638",
      "incomplete_value": true,
      "site": "00ba463c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba45f4",
      "incomplete_value": true,
      "site": "00ba45f8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba4660",
      "incomplete_value": true,
      "site": "00ba4664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba461c",
      "incomplete_value": true,
      "site": "00ba4620",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
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
      "00ba462c",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4630",
      "DATA",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba4634",
      "READ",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba462c",
      "READ",
      [
        "storage",
        "00c1b508",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4630",
      "DATA",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba4634",
      "READ",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba4620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba45c4.md#insn-00ba4620) · [`00ba45e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba45c4.md#insn-00ba45e8) · [`00ba4610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba45c4.md#insn-00ba4610)
- 新版 `00ba4664`（命令位置の公開資料なし） · `00ba462c`（命令位置の公開資料なし） · `00ba4654`（命令位置の公開資料なし）

~~~diff
- 00ba4620 ["INT_ADD", "register:40f0:8", ["const:ba4620:8", "const:4:8"]]
- 00ba4620 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba4664 ["INT_ADD", "register:40f0:8", ["const:ba4664:8", "const:4:8"]]
+ 00ba4664 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba4620 bytes 1cf20094
+ 00ba4664 bytes 1ff20094
- 00ba45e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4b8:8"]]
- 00ba45e8 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba462c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
+ 00ba462c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba45e8 bytes 945e42f9
+ 00ba462c bytes 948642f9
- 00ba4610 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba4654 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba4610 bytes a2570a10
+ 00ba4654 bytes a2570a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e273879d3c750a9038c6755fcdca5f06"></a>

### [`00ba46f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba46f0.md) → [`00ba4734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4734.md) FUN_00ba4734

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba4758",
      "incomplete_value": true,
      "site": "00ba475c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba4714",
      "incomplete_value": true,
      "site": "00ba4718",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba4764",
      "incomplete_value": true,
      "site": "00ba4768",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba4720",
      "incomplete_value": true,
      "site": "00ba4724",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba478c",
      "incomplete_value": true,
      "site": "00ba4790",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba4748",
      "incomplete_value": true,
      "site": "00ba474c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
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
      "00ba4758",
      "READ",
      [
        "storage",
        "00c1be90",
        null,
        "pointer"
      ]
    ],
    [
      "00ba475c",
      "DATA",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba4760",
      "READ",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba4758",
      "READ",
      [
        "storage",
        "00c1bee0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba475c",
      "DATA",
      [
        "storage",
        "010a28e0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba4760",
      "READ",
      [
        "storage",
        "010a28e0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba474c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba46f0.md#insn-00ba474c) · [`00ba4714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba46f0.md#insn-00ba4714) · [`00ba473c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba46f0.md#insn-00ba473c)
- 新版 `00ba4790`（命令位置の公開資料なし） · `00ba4758`（命令位置の公開資料なし） · `00ba4780`（命令位置の公開資料なし）

~~~diff
- 00ba474c ["INT_ADD", "register:40f0:8", ["const:ba474c:8", "const:4:8"]]
- 00ba474c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba4790 ["INT_ADD", "register:40f0:8", ["const:ba4790:8", "const:4:8"]]
+ 00ba4790 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba474c bytes d1f10094
+ 00ba4790 bytes d4f10094
- 00ba4714 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e90:8"]]
- 00ba4714 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba4758 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ee0:8"]]
+ 00ba4758 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba4714 bytes 944a47f9
+ 00ba4758 bytes 947247f9
- 00ba473c ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba4780 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba473c bytes 424e0a10
+ 00ba4780 bytes 424e0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0b764592779356d471ceb3781dc0deb"></a>

### [`00ba481c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba481c.md) → [`00ba4860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4860.md) FUN_00ba4860

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba4884",
      "incomplete_value": true,
      "site": "00ba4888",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba4840",
      "incomplete_value": true,
      "site": "00ba4844",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba4890",
      "incomplete_value": true,
      "site": "00ba4894",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba484c",
      "incomplete_value": true,
      "site": "00ba4850",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba48b8",
      "incomplete_value": true,
      "site": "00ba48bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba4874",
      "incomplete_value": true,
      "site": "00ba4878",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea0:8"
              ]
            ]
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
      "00ba4884",
      "READ",
      [
        "storage",
        "00c1bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4888",
      "DATA",
      [
        "storage",
        "010a2930",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba488c",
      "READ",
      [
        "storage",
        "010a2930",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba4884",
      "READ",
      [
        "storage",
        "00c1bef0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4888",
      "DATA",
      [
        "storage",
        "010a2970",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba488c",
      "READ",
      [
        "storage",
        "010a2970",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba4878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba481c.md#insn-00ba4878) · [`00ba4840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba481c.md#insn-00ba4840) · [`00ba4868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba481c.md#insn-00ba4868)
- 新版 `00ba48bc`（命令位置の公開資料なし） · `00ba4884`（命令位置の公開資料なし） · `00ba48ac`（命令位置の公開資料なし）

~~~diff
- 00ba4878 ["INT_ADD", "register:40f0:8", ["const:ba4878:8", "const:4:8"]]
- 00ba4878 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba48bc ["INT_ADD", "register:40f0:8", ["const:ba48bc:8", "const:4:8"]]
+ 00ba48bc ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba4878 bytes 86f10094
+ 00ba48bc bytes 89f10094
- 00ba4840 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ea0:8"]]
- 00ba4840 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba4884 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ef0:8"]]
+ 00ba4884 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba4840 bytes 945247f9
+ 00ba4884 bytes 947a47f9
- 00ba4868 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba48ac ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba4868 bytes e2440a10
+ 00ba48ac bytes e2440a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30702e9477a919fae1a8250d5aff4ea0"></a>

### [`00ba4948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4948.md) → [`00ba498c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba498c.md) FUN_00ba498c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) · 呼出先 5件 [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00be0e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0e90.md)
- 新版 呼出元 2件 [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) · 呼出先 5件 [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00be0ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ee0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba49b0",
      "incomplete_value": true,
      "site": "00ba49b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba496c",
      "incomplete_value": true,
      "site": "00ba4970",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba49bc",
      "incomplete_value": true,
      "site": "00ba49c0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba4978",
      "incomplete_value": true,
      "site": "00ba497c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba49e4",
      "incomplete_value": true,
      "site": "00ba49e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba49a0",
      "incomplete_value": true,
      "site": "00ba49a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb0:8"
              ]
            ]
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
      "00ba49b0",
      "READ",
      [
        "storage",
        "00c1beb0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba49b4",
      "DATA",
      [
        "storage",
        "010a2940",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba49b8",
      "READ",
      [
        "storage",
        "010a2940",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba49b0",
      "READ",
      [
        "storage",
        "00c1bf00",
        null,
        "pointer"
      ]
    ],
    [
      "00ba49b4",
      "DATA",
      [
        "storage",
        "010a2980",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba49b8",
      "READ",
      [
        "storage",
        "010a2980",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba49a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4948.md#insn-00ba49a4) · [`00ba496c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4948.md#insn-00ba496c) · [`00ba4994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4948.md#insn-00ba4994)
- 新版 `00ba49e8`（命令位置の公開資料なし） · `00ba49b0`（命令位置の公開資料なし） · `00ba49d8`（命令位置の公開資料なし）

~~~diff
- 00ba49a4 ["INT_ADD", "register:40f0:8", ["const:ba49a4:8", "const:4:8"]]
- 00ba49a4 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba49e8 ["INT_ADD", "register:40f0:8", ["const:ba49e8:8", "const:4:8"]]
+ 00ba49e8 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba49a4 bytes 3bf10094
+ 00ba49e8 bytes 3ef10094
- 00ba496c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:eb0:8"]]
- 00ba496c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba49b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f00:8"]]
+ 00ba49b0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba496c bytes 945a47f9
+ 00ba49b0 bytes 948247f9
- 00ba4994 ["COPY", "register:4010:8", ["const:bb9104:8"]]
+ 00ba49d8 ["COPY", "register:4010:8", ["const:bb9148:8"]]
- 00ba4994 bytes 823b0a10
+ 00ba49d8 bytes 823b0a10
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0388f1130929a20019453053d3950bca"></a>

### [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) → [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) FUN_00ba4ab8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00ba81ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba81ec.md) [`00ba833c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba833c.md) · 呼出先 40件 [`00ba06ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba06ac.md) [`00ba2d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2d1c.md) [`00ba2e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2e48.md) [`00ba2f74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba2f74.md) [`00ba30a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba3/00ba30a0.md)
- 新版 呼出元 2件 [`00ba8230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8230.md) [`00ba8380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8380.md) · 呼出先 40件 [`00ba06f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba06f0.md) [`00ba2d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2d60.md) [`00ba2e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2e8c.md) [`00ba2fb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba2fb8.md) [`00ba30e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba3/00ba30e4.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 89.19% / 新版 89.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 13件

アドレスに依存する影響 `store_value` 7件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba4aec",
      "incomplete_value": false,
      "site": "00ba4aec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba4aa8",
      "incomplete_value": false,
      "site": "00ba4aa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "definition_site": "00ba4c7c",
      "incomplete_value": true,
      "site": "00ba4c7c",
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
      "definition_site": "00ba4c38",
      "incomplete_value": true,
      "site": "00ba4c38",
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
    "ordinal": 30,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba4cb4",
      "incomplete_value": true,
      "site": "00ba4cb8",
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
      "definition_site": "00ba4c70",
      "incomplete_value": true,
      "site": "00ba4c74",
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
      "00ba4aec",
      "DATA",
      [
        "storage",
        "00c138c8",
        null,
        "undefined *"
      ]
    ],
    [
      "00ba4c74",
      "READ",
      [
        "storage",
        "00c1beb8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4c7c",
      "DATA",
      [
        "storage",
        "00c15bd8",
        null,
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00ba4aec",
      "DATA",
      [
        "storage",
        "00c13918",
        null,
        "undefined *"
      ]
    ],
    [
      "00ba4c74",
      "READ",
      [
        "storage",
        "00c1bf08",
        null,
        "pointer"
      ]
    ],
    [
      "00ba4c7c",
      "DATA",
      [
        "storage",
        "00c15c28",
        null,
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba4bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md#insn-00ba4bf4) · [`00ba4c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md#insn-00ba4c30) · [`00ba4de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md#insn-00ba4de4)
- 新版 `00ba4c38`（命令位置の公開資料なし） · `00ba4c74`（命令位置の公開資料なし） · `00ba4e28`（命令位置の公開資料なし）

~~~diff
- 00ba4bf4 ["INT_ADD", "register:40f0:8", ["const:ba4bf4:8", "const:4:8"]]
- 00ba4bf4 ["CALL", null, ["callee:00ba2fb8:8"]]
+ 00ba4c38 ["INT_ADD", "register:40f0:8", ["const:ba4c38:8", "const:4:8"]]
+ 00ba4c38 ["CALL", null, ["callee:00ba2fb8:8"]]
- 00ba4bf4 bytes e0f8ff97
+ 00ba4c38 bytes e0f8ff97
- 00ba4c30 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:eb8:8"]]
- 00ba4c30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba4c74 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f08:8"]]
+ 00ba4c74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba4c30 bytes 085d47f9
+ 00ba4c74 bytes 088547f9
- 00ba4de4 ["INT_ADD", "register:40f0:8", ["const:ba4de4:8", "const:4:8"]]
- 00ba4de4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ba4e28 ["INT_ADD", "register:40f0:8", ["const:ba4e28:8", "const:4:8"]]
+ 00ba4e28 ["CALL", null, ["callee:00bdb040:8"]]
- 00ba4de4 bytes 83d80094
+ 00ba4e28 bytes 86d80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f0db446b65a190be02beaa394c0fbf1"></a>

### [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) → [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) FUN_00ba5108

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00ba83b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba83b4.md) · 呼出先 33件 [`00ba06ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba0/00ba06ac.md) [`00ba5428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5428.md) [`00ba556c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba556c.md) [`00ba56b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba56b0.md) [`00ba57f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba57f4.md)
- 新版 呼出元 1件 [`00ba83f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba83f8.md) · 呼出先 33件 [`00ba06f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba0/00ba06f0.md) [`00ba546c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba546c.md) [`00ba55b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba55b0.md) [`00ba56f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba56f4.md) [`00ba5838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5838.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.82% / 新版 98.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba5138",
      "incomplete_value": false,
      "site": "00ba5138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba50f4",
      "incomplete_value": false,
      "site": "00ba50f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "00ba5138",
      "DATA",
      [
        "storage",
        "00c138c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ba5138",
      "DATA",
      [
        "storage",
        "00c13918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba50e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md#insn-00ba50e8) · [`00ba5168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md#insn-00ba5168) · [`00ba5184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md#insn-00ba5184)
- 新版 `00ba512c`（命令位置の公開資料なし） · `00ba51ac`（命令位置の公開資料なし） · `00ba51c8`（命令位置の公開資料なし）

~~~diff
- 00ba50e8 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00ba50e8 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ba50e8 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ba50e8 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ba512c ["COPY", "tmp:0:8", ["const:918:8"]]
+ 00ba512c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ba512c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ba512c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ba50e8 bytes 29212391
+ 00ba512c bytes 29612491
- 00ba5168 ["INT_ADD", "register:40f0:8", ["const:ba5168:8", "const:4:8"]]
- 00ba5168 ["CALL", null, ["callee:00ba06f0:8"]]
+ 00ba51ac ["INT_ADD", "register:40f0:8", ["const:ba51ac:8", "const:4:8"]]
+ 00ba51ac ["CALL", null, ["callee:00ba06f0:8"]]
- 00ba5168 bytes 51edff97
+ 00ba51ac bytes 51edff97
- 00ba5184 ["INT_ADD", "register:40f0:8", ["const:ba5184:8", "const:4:8"]]
- 00ba5184 ["CALL", null, ["callee:00bb8a78:8"]]
+ 00ba51c8 ["INT_ADD", "register:40f0:8", ["const:ba51c8:8", "const:4:8"]]
+ 00ba51c8 ["CALL", null, ["callee:00bb8a78:8"]]
- 00ba5184 bytes 2c4e0094
+ 00ba51c8 bytes 2c4e0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6993b2c4aed8bbfd030cdd23ddf6b107"></a>

### [`00ba5428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5428.md) → [`00ba546c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba546c.md) FUN_00ba546c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba5490",
      "incomplete_value": true,
      "site": "00ba5494",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba544c",
      "incomplete_value": true,
      "site": "00ba5450",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba549c",
      "incomplete_value": true,
      "site": "00ba54a0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5458",
      "incomplete_value": true,
      "site": "00ba545c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba54c4",
      "incomplete_value": true,
      "site": "00ba54c8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:580:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5480",
      "incomplete_value": true,
      "site": "00ba5484",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:530:8"
              ]
            ]
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
      "00ba5490",
      "READ",
      [
        "storage",
        "00c1b530",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5494",
      "DATA",
      [
        "storage",
        "010a2810",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5498",
      "READ",
      [
        "storage",
        "010a2810",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba5490",
      "READ",
      [
        "storage",
        "00c1b580",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5494",
      "DATA",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5498",
      "READ",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17collateIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5428.md#insn-00ba5484) · [`00ba54b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5428.md#insn-00ba54b0) · [`00ba544c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5428.md#insn-00ba544c)
- 新版 `00ba54c8`（命令位置の公開資料なし） · `00ba54f4`（命令位置の公開資料なし） · `00ba5490`（命令位置の公開資料なし）

~~~diff
- 00ba5484 ["INT_ADD", "register:40f0:8", ["const:ba5484:8", "const:4:8"]]
- 00ba5484 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba54c8 ["INT_ADD", "register:40f0:8", ["const:ba54c8:8", "const:4:8"]]
+ 00ba54c8 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba5484 bytes 83ee0094
+ 00ba54c8 bytes 86ee0094
- 00ba54b0 ["INT_ADD", "register:40f0:8", ["const:ba54b0:8", "const:4:8"]]
- 00ba54b0 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba54f4 ["INT_ADD", "register:40f0:8", ["const:ba54f4:8", "const:4:8"]]
+ 00ba54f4 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba54b0 bytes 5cc60094
+ 00ba54f4 bytes 5bc60094
- 00ba544c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00ba544c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba5490 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
+ 00ba5490 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba544c bytes 949a42f9
+ 00ba5490 bytes 94c242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2dd574a1e8ed274537a2ab4e3a65835d"></a>

### [`00ba556c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba556c.md) → [`00ba55b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba55b0.md) FUN_00ba55b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba55d4",
      "incomplete_value": true,
      "site": "00ba55d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5590",
      "incomplete_value": true,
      "site": "00ba5594",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba55e0",
      "incomplete_value": true,
      "site": "00ba55e4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba559c",
      "incomplete_value": true,
      "site": "00ba55a0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5608",
      "incomplete_value": true,
      "site": "00ba560c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba55c4",
      "incomplete_value": true,
      "site": "00ba55c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
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
      "00ba55d4",
      "READ",
      [
        "storage",
        "00c1bd88",
        null,
        "pointer"
      ]
    ],
    [
      "00ba55d8",
      "DATA",
      [
        "storage",
        "010a2820",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba55dc",
      "READ",
      [
        "storage",
        "010a2820",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba55d4",
      "READ",
      [
        "storage",
        "00c1bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba55d8",
      "DATA",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba55dc",
      "READ",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17collateIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba55c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba556c.md#insn-00ba55c8) · [`00ba55f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba556c.md#insn-00ba55f4) · [`00ba5590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba556c.md#insn-00ba5590)
- 新版 `00ba560c`（命令位置の公開資料なし） · `00ba5638`（命令位置の公開資料なし） · `00ba55d4`（命令位置の公開資料なし）

~~~diff
- 00ba55c8 ["INT_ADD", "register:40f0:8", ["const:ba55c8:8", "const:4:8"]]
- 00ba55c8 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba560c ["INT_ADD", "register:40f0:8", ["const:ba560c:8", "const:4:8"]]
+ 00ba560c ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba55c8 bytes 32ee0094
+ 00ba560c bytes 35ee0094
- 00ba55f4 ["INT_ADD", "register:40f0:8", ["const:ba55f4:8", "const:4:8"]]
- 00ba55f4 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba5638 ["INT_ADD", "register:40f0:8", ["const:ba5638:8", "const:4:8"]]
+ 00ba5638 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba55f4 bytes 0bc60094
+ 00ba5638 bytes 0ac60094
- 00ba5590 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
- 00ba5590 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba55d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd8:8"]]
+ 00ba55d4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba5590 bytes 94c646f9
+ 00ba55d4 bytes 94ee46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad8227cdd499553989502cac3d3d4c29"></a>

### [`00ba56b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba56b0.md) → [`00ba56f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba56f4.md) FUN_00ba56f4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba5718",
      "incomplete_value": true,
      "site": "00ba571c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00ba56d4",
      "incomplete_value": true,
      "site": "00ba56d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 6,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba5724",
      "incomplete_value": true,
      "site": "00ba5728",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba56e0",
      "incomplete_value": true,
      "site": "00ba56e4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba574c",
      "incomplete_value": true,
      "site": "00ba5750",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00ba5708",
      "incomplete_value": true,
      "site": "00ba570c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00ba5718",
      "READ",
      [
        "storage",
        "00c1adf0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba571c",
      "DATA",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5720",
      "READ",
      [
        "storage",
        "010a2ad0",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba5718",
      "READ",
      [
        "storage",
        "00c1ae40",
        null,
        "pointer"
      ]
    ],
    [
      "00ba571c",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5720",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk15ctypeIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba570c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba56b0.md#insn-00ba570c) · [`00ba5738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba56b0.md#insn-00ba5738) · [`00ba56d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba56b0.md#insn-00ba56d4)
- 新版 `00ba5750`（命令位置の公開資料なし） · `00ba577c`（命令位置の公開資料なし） · `00ba5718`（命令位置の公開資料なし）

~~~diff
- 00ba570c ["INT_ADD", "register:40f0:8", ["const:ba570c:8", "const:4:8"]]
- 00ba570c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba5750 ["INT_ADD", "register:40f0:8", ["const:ba5750:8", "const:4:8"]]
+ 00ba5750 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba570c bytes e1ed0094
+ 00ba5750 bytes e4ed0094
- 00ba5738 ["INT_ADD", "register:40f0:8", ["const:ba5738:8", "const:4:8"]]
- 00ba5738 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba577c ["INT_ADD", "register:40f0:8", ["const:ba577c:8", "const:4:8"]]
+ 00ba577c ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba5738 bytes bac50094
+ 00ba577c bytes b9c50094
- 00ba56d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
- 00ba56d4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba5718 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e40:8"]]
+ 00ba5718 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba56d4 bytes 94fa46f9
+ 00ba5718 bytes 942247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45375b49d8041f318f448c9ed31ddc54"></a>

### [`00ba57f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba57f4.md) → [`00ba5838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5838.md) FUN_00ba5838

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba585c",
      "incomplete_value": true,
      "site": "00ba5860",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5818",
      "incomplete_value": true,
      "site": "00ba581c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba5868",
      "incomplete_value": true,
      "site": "00ba586c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5824",
      "incomplete_value": true,
      "site": "00ba5828",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5890",
      "incomplete_value": true,
      "site": "00ba5894",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba584c",
      "incomplete_value": true,
      "site": "00ba5850",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
              ]
            ]
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
      "00ba585c",
      "READ",
      [
        "storage",
        "00c1bcc0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5860",
      "DATA",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5864",
      "READ",
      [
        "storage",
        "010a2ac0",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba585c",
      "READ",
      [
        "storage",
        "00c1bd10",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5860",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5864",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk15ctypeIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba57f4.md#insn-00ba5850) · [`00ba587c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba57f4.md#insn-00ba587c) · [`00ba5818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba57f4.md#insn-00ba5818)
- 新版 `00ba5894`（命令位置の公開資料なし） · `00ba58c0`（命令位置の公開資料なし） · `00ba585c`（命令位置の公開資料なし）

~~~diff
- 00ba5850 ["INT_ADD", "register:40f0:8", ["const:ba5850:8", "const:4:8"]]
- 00ba5850 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba5894 ["INT_ADD", "register:40f0:8", ["const:ba5894:8", "const:4:8"]]
+ 00ba5894 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba5850 bytes 90ed0094
+ 00ba5894 bytes 93ed0094
- 00ba587c ["INT_ADD", "register:40f0:8", ["const:ba587c:8", "const:4:8"]]
- 00ba587c ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba58c0 ["INT_ADD", "register:40f0:8", ["const:ba58c0:8", "const:4:8"]]
+ 00ba58c0 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba587c bytes 69c50094
+ 00ba58c0 bytes 68c50094
- 00ba5818 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc0:8"]]
- 00ba5818 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba585c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d10:8"]]
+ 00ba585c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba5818 bytes 946246f9
+ 00ba585c bytes 948a46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee1e6d661cf2e798ac4f0327965c3c78"></a>

### [`00ba5938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5938.md) → [`00ba597c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba597c.md) FUN_00ba597c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba59a0",
      "incomplete_value": true,
      "site": "00ba59a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba595c",
      "incomplete_value": true,
      "site": "00ba5960",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a60:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba59ac",
      "incomplete_value": true,
      "site": "00ba59b0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5968",
      "incomplete_value": true,
      "site": "00ba596c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba59d4",
      "incomplete_value": true,
      "site": "00ba59d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5990",
      "incomplete_value": true,
      "site": "00ba5994",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a60:8"
              ]
            ]
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
      "00ba59a0",
      "READ",
      [
        "storage",
        "00c1ba60",
        null,
        "pointer"
      ]
    ],
    [
      "00ba59a4",
      "DATA",
      [
        "storage",
        "010a2ae0",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba59a8",
      "READ",
      [
        "storage",
        "010a2ae0",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba59a0",
      "READ",
      [
        "storage",
        "00c1bab0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba59a4",
      "DATA",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba59a8",
      "READ",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIcc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5938.md#insn-00ba5994) · [`00ba59c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5938.md#insn-00ba59c0) · [`00ba595c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5938.md#insn-00ba595c)
- 新版 `00ba59d8`（命令位置の公開資料なし） · `00ba5a04`（命令位置の公開資料なし） · `00ba59a0`（命令位置の公開資料なし）

~~~diff
- 00ba5994 ["INT_ADD", "register:40f0:8", ["const:ba5994:8", "const:4:8"]]
- 00ba5994 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba59d8 ["INT_ADD", "register:40f0:8", ["const:ba59d8:8", "const:4:8"]]
+ 00ba59d8 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba5994 bytes 3fed0094
+ 00ba59d8 bytes 42ed0094
- 00ba59c0 ["INT_ADD", "register:40f0:8", ["const:ba59c0:8", "const:4:8"]]
- 00ba59c0 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba5a04 ["INT_ADD", "register:40f0:8", ["const:ba5a04:8", "const:4:8"]]
+ 00ba5a04 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba59c0 bytes 18c50094
+ 00ba5a04 bytes 17c50094
- 00ba595c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a60:8"]]
- 00ba595c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba59a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ab0:8"]]
+ 00ba59a0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba595c bytes 943245f9
+ 00ba59a0 bytes 945a45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12e8b0f0ab2339bbd29edcab7f1392dc"></a>

### [`00ba5a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5a7c.md) → [`00ba5ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5ac0.md) FUN_00ba5ac0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba5ae4",
      "incomplete_value": true,
      "site": "00ba5ae8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5aa0",
      "incomplete_value": true,
      "site": "00ba5aa4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba5af0",
      "incomplete_value": true,
      "site": "00ba5af4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5aac",
      "incomplete_value": true,
      "site": "00ba5ab0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5b18",
      "incomplete_value": true,
      "site": "00ba5b1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5ad4",
      "incomplete_value": true,
      "site": "00ba5ad8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
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
      "00ba5ae4",
      "READ",
      [
        "storage",
        "00c1bda8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5ae8",
      "DATA",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5aec",
      "READ",
      [
        "storage",
        "010a2b00",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba5ae4",
      "READ",
      [
        "storage",
        "00c1bdf8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5ae8",
      "DATA",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5aec",
      "READ",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk17codecvtIDsc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5a7c.md#insn-00ba5ad8) · [`00ba5b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5a7c.md#insn-00ba5b04) · [`00ba5aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5a7c.md#insn-00ba5aa0)
- 新版 `00ba5b1c`（命令位置の公開資料なし） · `00ba5b48`（命令位置の公開資料なし） · `00ba5ae4`（命令位置の公開資料なし）

~~~diff
- 00ba5ad8 ["INT_ADD", "register:40f0:8", ["const:ba5ad8:8", "const:4:8"]]
- 00ba5ad8 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba5b1c ["INT_ADD", "register:40f0:8", ["const:ba5b1c:8", "const:4:8"]]
+ 00ba5b1c ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba5ad8 bytes eeec0094
+ 00ba5b1c bytes f1ec0094
- 00ba5b04 ["INT_ADD", "register:40f0:8", ["const:ba5b04:8", "const:4:8"]]
- 00ba5b04 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba5b48 ["INT_ADD", "register:40f0:8", ["const:ba5b48:8", "const:4:8"]]
+ 00ba5b48 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba5b04 bytes c7c40094
+ 00ba5b48 bytes c6c40094
- 00ba5aa0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:da8:8"]]
- 00ba5aa0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba5ae4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df8:8"]]
+ 00ba5ae4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba5aa0 bytes 94d646f9
+ 00ba5ae4 bytes 94fe46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86a240612d1b7cebdc7cedad476f5ea7"></a>

### [`00ba5bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5bc0.md) → [`00ba5c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5c04.md) FUN_00ba5c04

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba5c28",
      "incomplete_value": true,
      "site": "00ba5c2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5be4",
      "incomplete_value": true,
      "site": "00ba5be8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba5c34",
      "incomplete_value": true,
      "site": "00ba5c38",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5bf0",
      "incomplete_value": true,
      "site": "00ba5bf4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5c5c",
      "incomplete_value": true,
      "site": "00ba5c60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5c18",
      "incomplete_value": true,
      "site": "00ba5c1c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
              ]
            ]
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
      "00ba5c28",
      "READ",
      [
        "storage",
        "00c1bdb8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5c2c",
      "DATA",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5c30",
      "READ",
      [
        "storage",
        "010a2b20",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba5c28",
      "READ",
      [
        "storage",
        "00c1be08",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5c2c",
      "DATA",
      [
        "storage",
        "010a2b60",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5c30",
      "READ",
      [
        "storage",
        "010a2b60",
        "_ZNSt6__ndk17codecvtIDic9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5bc0.md#insn-00ba5c1c) · [`00ba5c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5bc0.md#insn-00ba5c48) · [`00ba5be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5bc0.md#insn-00ba5be4)
- 新版 `00ba5c60`（命令位置の公開資料なし） · `00ba5c8c`（命令位置の公開資料なし） · `00ba5c28`（命令位置の公開資料なし）

~~~diff
- 00ba5c1c ["INT_ADD", "register:40f0:8", ["const:ba5c1c:8", "const:4:8"]]
- 00ba5c1c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba5c60 ["INT_ADD", "register:40f0:8", ["const:ba5c60:8", "const:4:8"]]
+ 00ba5c60 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba5c1c bytes 9dec0094
+ 00ba5c60 bytes a0ec0094
- 00ba5c48 ["INT_ADD", "register:40f0:8", ["const:ba5c48:8", "const:4:8"]]
- 00ba5c48 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba5c8c ["INT_ADD", "register:40f0:8", ["const:ba5c8c:8", "const:4:8"]]
+ 00ba5c8c ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba5c48 bytes 76c40094
+ 00ba5c8c bytes 75c40094
- 00ba5be4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db8:8"]]
- 00ba5be4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba5c28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e08:8"]]
+ 00ba5c28 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba5be4 bytes 94de46f9
+ 00ba5c28 bytes 940647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c921d8a20386ad918a2506b6d1a0bfc3"></a>

### [`00ba5d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5d04.md) → [`00ba5d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5d48.md) FUN_00ba5d48

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba5d6c",
      "incomplete_value": true,
      "site": "00ba5d70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5d28",
      "incomplete_value": true,
      "site": "00ba5d2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba5d78",
      "incomplete_value": true,
      "site": "00ba5d7c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5d34",
      "incomplete_value": true,
      "site": "00ba5d38",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5da0",
      "incomplete_value": true,
      "site": "00ba5da4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5d5c",
      "incomplete_value": true,
      "site": "00ba5d60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc8:8"
              ]
            ]
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
      "00ba5d6c",
      "READ",
      [
        "storage",
        "00c1bdc8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5d70",
      "DATA",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5d74",
      "READ",
      [
        "storage",
        "010a2b10",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba5d6c",
      "READ",
      [
        "storage",
        "00c1be18",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5d70",
      "DATA",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5d74",
      "READ",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk17codecvtIDsDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5d04.md#insn-00ba5d60) · [`00ba5d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5d04.md#insn-00ba5d8c) · [`00ba5d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5d04.md#insn-00ba5d28)
- 新版 `00ba5da4`（命令位置の公開資料なし） · `00ba5dd0`（命令位置の公開資料なし） · `00ba5d6c`（命令位置の公開資料なし）

~~~diff
- 00ba5d60 ["INT_ADD", "register:40f0:8", ["const:ba5d60:8", "const:4:8"]]
- 00ba5d60 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba5da4 ["INT_ADD", "register:40f0:8", ["const:ba5da4:8", "const:4:8"]]
+ 00ba5da4 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba5d60 bytes 4cec0094
+ 00ba5da4 bytes 4fec0094
- 00ba5d8c ["INT_ADD", "register:40f0:8", ["const:ba5d8c:8", "const:4:8"]]
- 00ba5d8c ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba5dd0 ["INT_ADD", "register:40f0:8", ["const:ba5dd0:8", "const:4:8"]]
+ 00ba5dd0 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba5d8c bytes 25c40094
+ 00ba5dd0 bytes 24c40094
- 00ba5d28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc8:8"]]
- 00ba5d28 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba5d6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e18:8"]]
+ 00ba5d6c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba5d28 bytes 94e646f9
+ 00ba5d6c bytes 940e47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b8a86f9440d8d6d69ce50e1a10bd562"></a>

### [`00ba5e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5e48.md) → [`00ba5e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5e8c.md) FUN_00ba5e8c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba5eb0",
      "incomplete_value": true,
      "site": "00ba5eb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5e6c",
      "incomplete_value": true,
      "site": "00ba5e70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba5ebc",
      "incomplete_value": true,
      "site": "00ba5ec0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5e78",
      "incomplete_value": true,
      "site": "00ba5e7c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5ee4",
      "incomplete_value": true,
      "site": "00ba5ee8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5ea0",
      "incomplete_value": true,
      "site": "00ba5ea4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dd8:8"
              ]
            ]
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
      "00ba5eb0",
      "READ",
      [
        "storage",
        "00c1bdd8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5eb4",
      "DATA",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5eb8",
      "READ",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba5eb0",
      "READ",
      [
        "storage",
        "00c1be28",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5eb4",
      "DATA",
      [
        "storage",
        "010a2b70",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5eb8",
      "READ",
      [
        "storage",
        "010a2b70",
        "_ZNSt6__ndk17codecvtIDiDu9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5e48.md#insn-00ba5ea4) · [`00ba5ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5e48.md#insn-00ba5ed0) · [`00ba5e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5e48.md#insn-00ba5e6c)
- 新版 `00ba5ee8`（命令位置の公開資料なし） · `00ba5f14`（命令位置の公開資料なし） · `00ba5eb0`（命令位置の公開資料なし）

~~~diff
- 00ba5ea4 ["INT_ADD", "register:40f0:8", ["const:ba5ea4:8", "const:4:8"]]
- 00ba5ea4 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba5ee8 ["INT_ADD", "register:40f0:8", ["const:ba5ee8:8", "const:4:8"]]
+ 00ba5ee8 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba5ea4 bytes fbeb0094
+ 00ba5ee8 bytes feeb0094
- 00ba5ed0 ["INT_ADD", "register:40f0:8", ["const:ba5ed0:8", "const:4:8"]]
- 00ba5ed0 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba5f14 ["INT_ADD", "register:40f0:8", ["const:ba5f14:8", "const:4:8"]]
+ 00ba5f14 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba5ed0 bytes d4c30094
+ 00ba5f14 bytes d3c30094
- 00ba5e6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd8:8"]]
- 00ba5e6c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba5eb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e28:8"]]
+ 00ba5eb0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba5e6c bytes 94ee46f9
+ 00ba5eb0 bytes 941647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5622acfdb4935cff59fc3bf4ee9365b"></a>

### [`00ba5f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5f8c.md) → [`00ba5fd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5fd0.md) FUN_00ba5fd0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba5ff4",
      "incomplete_value": true,
      "site": "00ba5ff8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5fb0",
      "incomplete_value": true,
      "site": "00ba5fb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba6000",
      "incomplete_value": true,
      "site": "00ba6004",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba5fbc",
      "incomplete_value": true,
      "site": "00ba5fc0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6028",
      "incomplete_value": true,
      "site": "00ba602c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba5fe4",
      "incomplete_value": true,
      "site": "00ba5fe8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
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
      "00ba5ff4",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5ff8",
      "DATA",
      [
        "storage",
        "010a2af0",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5ffc",
      "READ",
      [
        "storage",
        "010a2af0",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba5ff4",
      "READ",
      [
        "storage",
        "00c1bd78",
        null,
        "pointer"
      ]
    ],
    [
      "00ba5ff8",
      "DATA",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba5ffc",
      "READ",
      [
        "storage",
        "010a2b30",
        "_ZNSt6__ndk17codecvtIwc9mbstate_tE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba5fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5f8c.md#insn-00ba5fe8) · [`00ba6014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5f8c.md#insn-00ba6014) · [`00ba5fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba5f8c.md#insn-00ba5fb0)
- 新版 `00ba602c`（命令位置の公開資料なし） · `00ba6058`（命令位置の公開資料なし） · `00ba5ff4`（命令位置の公開資料なし）

~~~diff
- 00ba5fe8 ["INT_ADD", "register:40f0:8", ["const:ba5fe8:8", "const:4:8"]]
- 00ba5fe8 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba602c ["INT_ADD", "register:40f0:8", ["const:ba602c:8", "const:4:8"]]
+ 00ba602c ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba5fe8 bytes aaeb0094
+ 00ba602c bytes adeb0094
- 00ba6014 ["INT_ADD", "register:40f0:8", ["const:ba6014:8", "const:4:8"]]
- 00ba6014 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba6058 ["INT_ADD", "register:40f0:8", ["const:ba6058:8", "const:4:8"]]
+ 00ba6058 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba6014 bytes 83c30094
+ 00ba6058 bytes 82c30094
- 00ba5fb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
- 00ba5fb0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba5ff4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d78:8"]]
+ 00ba5ff4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba5fb0 bytes 949646f9
+ 00ba5ff4 bytes 94be46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0fe78f8a55854fc864107adc972b4d1"></a>

### [`00ba60d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba60d0.md) → [`00ba6114`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba6/00ba6114.md) FUN_00ba6114

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6138",
      "incomplete_value": true,
      "site": "00ba613c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba60f4",
      "incomplete_value": true,
      "site": "00ba60f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba6144",
      "incomplete_value": true,
      "site": "00ba6148",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6100",
      "incomplete_value": true,
      "site": "00ba6104",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba616c",
      "incomplete_value": true,
      "site": "00ba6170",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6128",
      "incomplete_value": true,
      "site": "00ba612c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d60:8"
              ]
            ]
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
      "00ba6138",
      "READ",
      [
        "storage",
        "00c1bd60",
        null,
        "pointer"
      ]
    ],
    [
      "00ba613c",
      "DATA",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6140",
      "READ",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6138",
      "READ",
      [
        "storage",
        "00c1bdb0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba613c",
      "DATA",
      [
        "storage",
        "010a28f0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6140",
      "READ",
      [
        "storage",
        "010a28f0",
        "_ZNSt6__ndk110moneypunctIcLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba612c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba60d0.md#insn-00ba612c) · [`00ba6158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba60d0.md#insn-00ba6158) · [`00ba60f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba60d0.md#insn-00ba60f4)
- 新版 `00ba6170`（命令位置の公開資料なし） · `00ba619c`（命令位置の公開資料なし） · `00ba6138`（命令位置の公開資料なし）

~~~diff
- 00ba612c ["INT_ADD", "register:40f0:8", ["const:ba612c:8", "const:4:8"]]
- 00ba612c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba6170 ["INT_ADD", "register:40f0:8", ["const:ba6170:8", "const:4:8"]]
+ 00ba6170 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba612c bytes 59eb0094
+ 00ba6170 bytes 5ceb0094
- 00ba6158 ["INT_ADD", "register:40f0:8", ["const:ba6158:8", "const:4:8"]]
- 00ba6158 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba619c ["INT_ADD", "register:40f0:8", ["const:ba619c:8", "const:4:8"]]
+ 00ba619c ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba6158 bytes 32c30094
+ 00ba619c bytes 31c30094
- 00ba60f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d60:8"]]
- 00ba60f4 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6138 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
+ 00ba6138 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba60f4 bytes 94b246f9
+ 00ba6138 bytes 94da46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02b8f0569890155dfed43742bc428107"></a>

### [`00ba6214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6214.md) → [`00ba6258`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba6/00ba6258.md) FUN_00ba6258

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba627c",
      "incomplete_value": true,
      "site": "00ba6280",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6238",
      "incomplete_value": true,
      "site": "00ba623c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba6288",
      "incomplete_value": true,
      "site": "00ba628c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6244",
      "incomplete_value": true,
      "site": "00ba6248",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba62b0",
      "incomplete_value": true,
      "site": "00ba62b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:da8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba626c",
      "incomplete_value": true,
      "site": "00ba6270",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d58:8"
              ]
            ]
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
      "00ba627c",
      "READ",
      [
        "storage",
        "00c1bd58",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6280",
      "DATA",
      [
        "storage",
        "010a28c0",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6284",
      "READ",
      [
        "storage",
        "010a28c0",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba627c",
      "READ",
      [
        "storage",
        "00c1bda8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6280",
      "DATA",
      [
        "storage",
        "010a2900",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6284",
      "READ",
      [
        "storage",
        "010a2900",
        "_ZNSt6__ndk110moneypunctIcLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6214.md#insn-00ba6270) · [`00ba629c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6214.md#insn-00ba629c) · [`00ba6238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6214.md#insn-00ba6238)
- 新版 `00ba62b4`（命令位置の公開資料なし） · `00ba62e0`（命令位置の公開資料なし） · `00ba627c`（命令位置の公開資料なし）

~~~diff
- 00ba6270 ["INT_ADD", "register:40f0:8", ["const:ba6270:8", "const:4:8"]]
- 00ba6270 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba62b4 ["INT_ADD", "register:40f0:8", ["const:ba62b4:8", "const:4:8"]]
+ 00ba62b4 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba6270 bytes 08eb0094
+ 00ba62b4 bytes 0beb0094
- 00ba629c ["INT_ADD", "register:40f0:8", ["const:ba629c:8", "const:4:8"]]
- 00ba629c ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba62e0 ["INT_ADD", "register:40f0:8", ["const:ba62e0:8", "const:4:8"]]
+ 00ba62e0 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba629c bytes e1c20094
+ 00ba62e0 bytes e0c20094
- 00ba6238 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d58:8"]]
- 00ba6238 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba627c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:da8:8"]]
+ 00ba627c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6238 bytes 94ae46f9
+ 00ba627c bytes 94d646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-933df2b526f6cf58c9724ca7af2330e3"></a>

### [`00ba6358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6358.md) → [`00ba639c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba6/00ba639c.md) FUN_00ba639c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba63c0",
      "incomplete_value": true,
      "site": "00ba63c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba637c",
      "incomplete_value": true,
      "site": "00ba6380",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d70:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba63cc",
      "incomplete_value": true,
      "site": "00ba63d0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6388",
      "incomplete_value": true,
      "site": "00ba638c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba63f4",
      "incomplete_value": true,
      "site": "00ba63f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:dc0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba63b0",
      "incomplete_value": true,
      "site": "00ba63b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d70:8"
              ]
            ]
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
      "00ba63c0",
      "READ",
      [
        "storage",
        "00c1bd70",
        null,
        "pointer"
      ]
    ],
    [
      "00ba63c4",
      "DATA",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba63c8",
      "READ",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba63c0",
      "READ",
      [
        "storage",
        "00c1bdc0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba63c4",
      "DATA",
      [
        "storage",
        "010a2910",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba63c8",
      "READ",
      [
        "storage",
        "010a2910",
        "_ZNSt6__ndk110moneypunctIwLb0EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba63b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6358.md#insn-00ba63b4) · [`00ba63e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6358.md#insn-00ba63e0) · [`00ba637c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6358.md#insn-00ba637c)
- 新版 `00ba63f8`（命令位置の公開資料なし） · `00ba6424`（命令位置の公開資料なし） · `00ba63c0`（命令位置の公開資料なし）

~~~diff
- 00ba63b4 ["INT_ADD", "register:40f0:8", ["const:ba63b4:8", "const:4:8"]]
- 00ba63b4 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba63f8 ["INT_ADD", "register:40f0:8", ["const:ba63f8:8", "const:4:8"]]
+ 00ba63f8 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba63b4 bytes b7ea0094
+ 00ba63f8 bytes baea0094
- 00ba63e0 ["INT_ADD", "register:40f0:8", ["const:ba63e0:8", "const:4:8"]]
- 00ba63e0 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba6424 ["INT_ADD", "register:40f0:8", ["const:ba6424:8", "const:4:8"]]
+ 00ba6424 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba63e0 bytes 90c20094
+ 00ba6424 bytes 8fc20094
- 00ba637c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d70:8"]]
- 00ba637c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba63c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dc0:8"]]
+ 00ba63c0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba637c bytes 94ba46f9
+ 00ba63c0 bytes 94e246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c840f3520783044ac68e8fecf9180eb"></a>

### [`00ba649c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba649c.md) → [`00ba64e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba6/00ba64e0.md) FUN_00ba64e0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6504",
      "incomplete_value": true,
      "site": "00ba6508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba64c0",
      "incomplete_value": true,
      "site": "00ba64c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d68:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba6510",
      "incomplete_value": true,
      "site": "00ba6514",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba64cc",
      "incomplete_value": true,
      "site": "00ba64d0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6538",
      "incomplete_value": true,
      "site": "00ba653c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba64f4",
      "incomplete_value": true,
      "site": "00ba64f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d68:8"
              ]
            ]
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
      "00ba6504",
      "READ",
      [
        "storage",
        "00c1bd68",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6508",
      "DATA",
      [
        "storage",
        "010a28e0",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba650c",
      "READ",
      [
        "storage",
        "010a28e0",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6504",
      "READ",
      [
        "storage",
        "00c1bdb8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6508",
      "DATA",
      [
        "storage",
        "010a2920",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba650c",
      "READ",
      [
        "storage",
        "010a2920",
        "_ZNSt6__ndk110moneypunctIwLb1EE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba64f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba649c.md#insn-00ba64f8) · [`00ba6524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba649c.md#insn-00ba6524) · [`00ba64c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba649c.md#insn-00ba64c0)
- 新版 `00ba653c`（命令位置の公開資料なし） · `00ba6568`（命令位置の公開資料なし） · `00ba6504`（命令位置の公開資料なし）

~~~diff
- 00ba64f8 ["INT_ADD", "register:40f0:8", ["const:ba64f8:8", "const:4:8"]]
- 00ba64f8 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba653c ["INT_ADD", "register:40f0:8", ["const:ba653c:8", "const:4:8"]]
+ 00ba653c ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba64f8 bytes 66ea0094
+ 00ba653c bytes 69ea0094
- 00ba6524 ["INT_ADD", "register:40f0:8", ["const:ba6524:8", "const:4:8"]]
- 00ba6524 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba6568 ["INT_ADD", "register:40f0:8", ["const:ba6568:8", "const:4:8"]]
+ 00ba6568 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba6524 bytes 3fc20094
+ 00ba6568 bytes 3ec20094
- 00ba64c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
- 00ba64c0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6504 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db8:8"]]
+ 00ba6504 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba64c0 bytes 94b646f9
+ 00ba6504 bytes 94de46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94af30e3f3dcfe3211dc85b69bdde8ed"></a>

### [`00ba65e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba65e0.md) → [`00ba6624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba6/00ba6624.md) FUN_00ba6624

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6648",
      "incomplete_value": true,
      "site": "00ba664c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6604",
      "incomplete_value": true,
      "site": "00ba6608",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba6654",
      "incomplete_value": true,
      "site": "00ba6658",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6610",
      "incomplete_value": true,
      "site": "00ba6614",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba667c",
      "incomplete_value": true,
      "site": "00ba6680",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6638",
      "incomplete_value": true,
      "site": "00ba663c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e28:8"
              ]
            ]
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
      "00ba6648",
      "READ",
      [
        "storage",
        "00c1be28",
        null,
        "pointer"
      ]
    ],
    [
      "00ba664c",
      "DATA",
      [
        "storage",
        "010a28f0",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6650",
      "READ",
      [
        "storage",
        "010a28f0",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6648",
      "READ",
      [
        "storage",
        "00c1be78",
        null,
        "pointer"
      ]
    ],
    [
      "00ba664c",
      "DATA",
      [
        "storage",
        "010a2930",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6650",
      "READ",
      [
        "storage",
        "010a2930",
        "_ZNSt6__ndk19money_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba663c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba65e0.md#insn-00ba663c) · [`00ba6668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba65e0.md#insn-00ba6668) · [`00ba6604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba65e0.md#insn-00ba6604)
- 新版 `00ba6680`（命令位置の公開資料なし） · `00ba66ac`（命令位置の公開資料なし） · `00ba6648`（命令位置の公開資料なし）

~~~diff
- 00ba663c ["INT_ADD", "register:40f0:8", ["const:ba663c:8", "const:4:8"]]
- 00ba663c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba6680 ["INT_ADD", "register:40f0:8", ["const:ba6680:8", "const:4:8"]]
+ 00ba6680 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba663c bytes 15ea0094
+ 00ba6680 bytes 18ea0094
- 00ba6668 ["INT_ADD", "register:40f0:8", ["const:ba6668:8", "const:4:8"]]
- 00ba6668 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba66ac ["INT_ADD", "register:40f0:8", ["const:ba66ac:8", "const:4:8"]]
+ 00ba66ac ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba6668 bytes eec10094
+ 00ba66ac bytes edc10094
- 00ba6604 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e28:8"]]
- 00ba6604 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6648 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e78:8"]]
+ 00ba6648 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6604 bytes 941647f9
+ 00ba6648 bytes 943e47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fda5607f5631608c74664928e43c6bb"></a>

### [`00ba6724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6724.md) → [`00ba6768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba6/00ba6768.md) FUN_00ba6768

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba678c",
      "incomplete_value": true,
      "site": "00ba6790",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6748",
      "incomplete_value": true,
      "site": "00ba674c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e38:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba6798",
      "incomplete_value": true,
      "site": "00ba679c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6754",
      "incomplete_value": true,
      "site": "00ba6758",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba67c0",
      "incomplete_value": true,
      "site": "00ba67c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba677c",
      "incomplete_value": true,
      "site": "00ba6780",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e38:8"
              ]
            ]
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
      "00ba678c",
      "READ",
      [
        "storage",
        "00c1be38",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6790",
      "DATA",
      [
        "storage",
        "010a2900",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6794",
      "READ",
      [
        "storage",
        "010a2900",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba678c",
      "READ",
      [
        "storage",
        "00c1be88",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6790",
      "DATA",
      [
        "storage",
        "010a2940",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6794",
      "READ",
      [
        "storage",
        "010a2940",
        "_ZNSt6__ndk19money_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6724.md#insn-00ba6780) · [`00ba67ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6724.md#insn-00ba67ac) · [`00ba6748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6724.md#insn-00ba6748)
- 新版 `00ba67c4`（命令位置の公開資料なし） · `00ba67f0`（命令位置の公開資料なし） · `00ba678c`（命令位置の公開資料なし）

~~~diff
- 00ba6780 ["INT_ADD", "register:40f0:8", ["const:ba6780:8", "const:4:8"]]
- 00ba6780 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba67c4 ["INT_ADD", "register:40f0:8", ["const:ba67c4:8", "const:4:8"]]
+ 00ba67c4 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba6780 bytes c4e90094
+ 00ba67c4 bytes c7e90094
- 00ba67ac ["INT_ADD", "register:40f0:8", ["const:ba67ac:8", "const:4:8"]]
- 00ba67ac ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba67f0 ["INT_ADD", "register:40f0:8", ["const:ba67f0:8", "const:4:8"]]
+ 00ba67f0 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba67ac bytes 9dc10094
+ 00ba67f0 bytes 9cc10094
- 00ba6748 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e38:8"]]
- 00ba6748 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba678c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e88:8"]]
+ 00ba678c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6748 bytes 941e47f9
+ 00ba678c bytes 944647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da6b5368ec904239f83d985a39865229"></a>

### [`00ba6868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6868.md) → [`00ba68ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba6/00ba68ac.md) FUN_00ba68ac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba68d0",
      "incomplete_value": true,
      "site": "00ba68d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba688c",
      "incomplete_value": true,
      "site": "00ba6890",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e48:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba68dc",
      "incomplete_value": true,
      "site": "00ba68e0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6898",
      "incomplete_value": true,
      "site": "00ba689c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6904",
      "incomplete_value": true,
      "site": "00ba6908",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba68c0",
      "incomplete_value": true,
      "site": "00ba68c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e48:8"
              ]
            ]
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
      "00ba68d0",
      "READ",
      [
        "storage",
        "00c1be48",
        null,
        "pointer"
      ]
    ],
    [
      "00ba68d4",
      "DATA",
      [
        "storage",
        "010a2910",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba68d8",
      "READ",
      [
        "storage",
        "010a2910",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba68d0",
      "READ",
      [
        "storage",
        "00c1be98",
        null,
        "pointer"
      ]
    ],
    [
      "00ba68d4",
      "DATA",
      [
        "storage",
        "010a2950",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba68d8",
      "READ",
      [
        "storage",
        "010a2950",
        "_ZNSt6__ndk19money_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba68c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6868.md#insn-00ba68c4) · [`00ba68f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6868.md#insn-00ba68f0) · [`00ba688c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6868.md#insn-00ba688c)
- 新版 `00ba6908`（命令位置の公開資料なし） · `00ba6934`（命令位置の公開資料なし） · `00ba68d0`（命令位置の公開資料なし）

~~~diff
- 00ba68c4 ["INT_ADD", "register:40f0:8", ["const:ba68c4:8", "const:4:8"]]
- 00ba68c4 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba6908 ["INT_ADD", "register:40f0:8", ["const:ba6908:8", "const:4:8"]]
+ 00ba6908 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba68c4 bytes 73e90094
+ 00ba6908 bytes 76e90094
- 00ba68f0 ["INT_ADD", "register:40f0:8", ["const:ba68f0:8", "const:4:8"]]
- 00ba68f0 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba6934 ["INT_ADD", "register:40f0:8", ["const:ba6934:8", "const:4:8"]]
+ 00ba6934 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba68f0 bytes 4cc10094
+ 00ba6934 bytes 4bc10094
- 00ba688c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e48:8"]]
- 00ba688c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba68d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e98:8"]]
+ 00ba68d0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba688c bytes 942647f9
+ 00ba68d0 bytes 944e47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-668678012d7d710d089036be6546bc84"></a>

### [`00ba69ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba69ac.md) → [`00ba69f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba6/00ba69f0.md) FUN_00ba69f0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6a14",
      "incomplete_value": true,
      "site": "00ba6a18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba69d0",
      "incomplete_value": true,
      "site": "00ba69d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba6a20",
      "incomplete_value": true,
      "site": "00ba6a24",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba69dc",
      "incomplete_value": true,
      "site": "00ba69e0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6a48",
      "incomplete_value": true,
      "site": "00ba6a4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6a04",
      "incomplete_value": true,
      "site": "00ba6a08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
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
      "00ba6a14",
      "READ",
      [
        "storage",
        "00c1be58",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6a18",
      "DATA",
      [
        "storage",
        "010a2920",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6a1c",
      "READ",
      [
        "storage",
        "010a2920",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6a14",
      "READ",
      [
        "storage",
        "00c1bea8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6a18",
      "DATA",
      [
        "storage",
        "010a2960",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6a1c",
      "READ",
      [
        "storage",
        "010a2960",
        "_ZNSt6__ndk19money_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba69ac.md#insn-00ba6a08) · [`00ba6a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba69ac.md#insn-00ba6a34) · [`00ba69d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba69ac.md#insn-00ba69d0)
- 新版 `00ba6a4c`（命令位置の公開資料なし） · `00ba6a78`（命令位置の公開資料なし） · `00ba6a14`（命令位置の公開資料なし）

~~~diff
- 00ba6a08 ["INT_ADD", "register:40f0:8", ["const:ba6a08:8", "const:4:8"]]
- 00ba6a08 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba6a4c ["INT_ADD", "register:40f0:8", ["const:ba6a4c:8", "const:4:8"]]
+ 00ba6a4c ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba6a08 bytes 22e90094
+ 00ba6a4c bytes 25e90094
- 00ba6a34 ["INT_ADD", "register:40f0:8", ["const:ba6a34:8", "const:4:8"]]
- 00ba6a34 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba6a78 ["INT_ADD", "register:40f0:8", ["const:ba6a78:8", "const:4:8"]]
+ 00ba6a78 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba6a34 bytes fbc00094
+ 00ba6a78 bytes fac00094
- 00ba69d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e58:8"]]
- 00ba69d0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6a14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ea8:8"]]
+ 00ba6a14 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba69d0 bytes 942e47f9
+ 00ba6a14 bytes 945647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7656db669fe56a7b55b3aec61ca0469"></a>

### [`00ba6af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6af0.md) → [`00ba6b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba6/00ba6b34.md) FUN_00ba6b34

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6b58",
      "incomplete_value": true,
      "site": "00ba6b5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6b14",
      "incomplete_value": true,
      "site": "00ba6b18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba6b64",
      "incomplete_value": true,
      "site": "00ba6b68",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6b20",
      "incomplete_value": true,
      "site": "00ba6b24",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6b8c",
      "incomplete_value": true,
      "site": "00ba6b90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6b48",
      "incomplete_value": true,
      "site": "00ba6b4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
              ]
            ]
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
      "00ba6b58",
      "READ",
      [
        "storage",
        "00c1bd38",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6b5c",
      "DATA",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6b60",
      "READ",
      [
        "storage",
        "010a2b40",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6b58",
      "READ",
      [
        "storage",
        "00c1bd88",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6b5c",
      "DATA",
      [
        "storage",
        "010a2b80",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6b60",
      "READ",
      [
        "storage",
        "010a2b80",
        "_ZNSt6__ndk18numpunctIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6af0.md#insn-00ba6b4c) · [`00ba6b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6af0.md#insn-00ba6b78) · [`00ba6b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6af0.md#insn-00ba6b14)
- 新版 `00ba6b90`（命令位置の公開資料なし） · `00ba6bbc`（命令位置の公開資料なし） · `00ba6b58`（命令位置の公開資料なし）

~~~diff
- 00ba6b4c ["INT_ADD", "register:40f0:8", ["const:ba6b4c:8", "const:4:8"]]
- 00ba6b4c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba6b90 ["INT_ADD", "register:40f0:8", ["const:ba6b90:8", "const:4:8"]]
+ 00ba6b90 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba6b4c bytes d1e80094
+ 00ba6b90 bytes d4e80094
- 00ba6b78 ["INT_ADD", "register:40f0:8", ["const:ba6b78:8", "const:4:8"]]
- 00ba6b78 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba6bbc ["INT_ADD", "register:40f0:8", ["const:ba6bbc:8", "const:4:8"]]
+ 00ba6bbc ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba6b78 bytes aac00094
+ 00ba6bbc bytes a9c00094
- 00ba6b14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d38:8"]]
- 00ba6b14 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6b58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d88:8"]]
+ 00ba6b58 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6b14 bytes 949e46f9
+ 00ba6b58 bytes 94c646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1fda9e450daf4ba07de8075868d29b5"></a>

### [`00ba6c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6c34.md) → [`00ba6c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba6/00ba6c78.md) FUN_00ba6c78

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6c9c",
      "incomplete_value": true,
      "site": "00ba6ca0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6c58",
      "incomplete_value": true,
      "site": "00ba6c5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba6ca8",
      "incomplete_value": true,
      "site": "00ba6cac",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6c64",
      "incomplete_value": true,
      "site": "00ba6c68",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6cd0",
      "incomplete_value": true,
      "site": "00ba6cd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6c8c",
      "incomplete_value": true,
      "site": "00ba6c90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
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
      "00ba6c9c",
      "READ",
      [
        "storage",
        "00c1bd48",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6ca0",
      "DATA",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6ca4",
      "READ",
      [
        "storage",
        "010a2b50",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6c9c",
      "READ",
      [
        "storage",
        "00c1bd98",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6ca0",
      "DATA",
      [
        "storage",
        "010a2b90",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6ca4",
      "READ",
      [
        "storage",
        "010a2b90",
        "_ZNSt6__ndk18numpunctIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6c34.md#insn-00ba6c90) · [`00ba6cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6c34.md#insn-00ba6cbc) · [`00ba6c58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6c34.md#insn-00ba6c58)
- 新版 `00ba6cd4`（命令位置の公開資料なし） · `00ba6d00`（命令位置の公開資料なし） · `00ba6c9c`（命令位置の公開資料なし）

~~~diff
- 00ba6c90 ["INT_ADD", "register:40f0:8", ["const:ba6c90:8", "const:4:8"]]
- 00ba6c90 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba6cd4 ["INT_ADD", "register:40f0:8", ["const:ba6cd4:8", "const:4:8"]]
+ 00ba6cd4 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba6c90 bytes 80e80094
+ 00ba6cd4 bytes 83e80094
- 00ba6cbc ["INT_ADD", "register:40f0:8", ["const:ba6cbc:8", "const:4:8"]]
- 00ba6cbc ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba6d00 ["INT_ADD", "register:40f0:8", ["const:ba6d00:8", "const:4:8"]]
+ 00ba6d00 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba6cbc bytes 59c00094
+ 00ba6d00 bytes 58c00094
- 00ba6c58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d48:8"]]
- 00ba6c58 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6c9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
+ 00ba6c9c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6c58 bytes 94a646f9
+ 00ba6c9c bytes 94ce46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d4963b0fe51a02787d188813bfc7d7e"></a>

### [`00ba6d78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6d78.md) → [`00ba6dbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba6/00ba6dbc.md) FUN_00ba6dbc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6de0",
      "incomplete_value": true,
      "site": "00ba6de4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6d9c",
      "incomplete_value": true,
      "site": "00ba6da0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba6dec",
      "incomplete_value": true,
      "site": "00ba6df0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6da8",
      "incomplete_value": true,
      "site": "00ba6dac",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6e14",
      "incomplete_value": true,
      "site": "00ba6e18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6dd0",
      "incomplete_value": true,
      "site": "00ba6dd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c90:8"
              ]
            ]
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
      "00ba6de0",
      "READ",
      [
        "storage",
        "00c1bc90",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6de4",
      "DATA",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6de8",
      "READ",
      [
        "storage",
        "010a2830",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6de0",
      "READ",
      [
        "storage",
        "00c1bce0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6de4",
      "DATA",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6de8",
      "READ",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6dd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6d78.md#insn-00ba6dd4) · [`00ba6e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6d78.md#insn-00ba6e00) · [`00ba6d9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6d78.md#insn-00ba6d9c)
- 新版 `00ba6e18`（命令位置の公開資料なし） · `00ba6e44`（命令位置の公開資料なし） · `00ba6de0`（命令位置の公開資料なし）

~~~diff
- 00ba6dd4 ["INT_ADD", "register:40f0:8", ["const:ba6dd4:8", "const:4:8"]]
- 00ba6dd4 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba6e18 ["INT_ADD", "register:40f0:8", ["const:ba6e18:8", "const:4:8"]]
+ 00ba6e18 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba6dd4 bytes 2fe80094
+ 00ba6e18 bytes 32e80094
- 00ba6e00 ["INT_ADD", "register:40f0:8", ["const:ba6e00:8", "const:4:8"]]
- 00ba6e00 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba6e44 ["INT_ADD", "register:40f0:8", ["const:ba6e44:8", "const:4:8"]]
+ 00ba6e44 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba6e00 bytes 08c00094
+ 00ba6e44 bytes 07c00094
- 00ba6d9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c90:8"]]
- 00ba6d9c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6de0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ce0:8"]]
+ 00ba6de0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6d9c bytes 944a46f9
+ 00ba6de0 bytes 947246f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de827de6f02fe2baa698cd1a106db548"></a>

### [`00ba6ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6ebc.md) → [`00ba6f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba6/00ba6f00.md) FUN_00ba6f00

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba6f24",
      "incomplete_value": true,
      "site": "00ba6f28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6ee0",
      "incomplete_value": true,
      "site": "00ba6ee4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba6f30",
      "incomplete_value": true,
      "site": "00ba6f34",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6eec",
      "incomplete_value": true,
      "site": "00ba6ef0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba6f58",
      "incomplete_value": true,
      "site": "00ba6f5c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba6f14",
      "incomplete_value": true,
      "site": "00ba6f18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc8:8"
              ]
            ]
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
      "00ba6f24",
      "READ",
      [
        "storage",
        "00c1bcc8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6f28",
      "DATA",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6f2c",
      "READ",
      [
        "storage",
        "010a2840",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba6f24",
      "READ",
      [
        "storage",
        "00c1bd18",
        null,
        "pointer"
      ]
    ],
    [
      "00ba6f28",
      "DATA",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba6f2c",
      "READ",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk17num_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba6f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6ebc.md#insn-00ba6f18) · [`00ba6f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6ebc.md#insn-00ba6f44) · [`00ba6ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba6/00ba6ebc.md#insn-00ba6ee0)
- 新版 `00ba6f5c`（命令位置の公開資料なし） · `00ba6f88`（命令位置の公開資料なし） · `00ba6f24`（命令位置の公開資料なし）

~~~diff
- 00ba6f18 ["INT_ADD", "register:40f0:8", ["const:ba6f18:8", "const:4:8"]]
- 00ba6f18 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba6f5c ["INT_ADD", "register:40f0:8", ["const:ba6f5c:8", "const:4:8"]]
+ 00ba6f5c ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba6f18 bytes dee70094
+ 00ba6f5c bytes e1e70094
- 00ba6f44 ["INT_ADD", "register:40f0:8", ["const:ba6f44:8", "const:4:8"]]
- 00ba6f44 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba6f88 ["INT_ADD", "register:40f0:8", ["const:ba6f88:8", "const:4:8"]]
+ 00ba6f88 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba6f44 bytes b7bf0094
+ 00ba6f88 bytes b6bf0094
- 00ba6ee0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cc8:8"]]
- 00ba6ee0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba6f24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d18:8"]]
+ 00ba6f24 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba6ee0 bytes 946646f9
+ 00ba6f24 bytes 948e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cc567e6437b48882605834ad0620deb"></a>

### [`00ba7000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7000.md) → [`00ba7044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7044.md) FUN_00ba7044

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba7068",
      "incomplete_value": true,
      "site": "00ba706c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7024",
      "incomplete_value": true,
      "site": "00ba7028",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba7074",
      "incomplete_value": true,
      "site": "00ba7078",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba7030",
      "incomplete_value": true,
      "site": "00ba7034",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba709c",
      "incomplete_value": true,
      "site": "00ba70a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7058",
      "incomplete_value": true,
      "site": "00ba705c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
              ]
            ]
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
      "00ba7068",
      "READ",
      [
        "storage",
        "00c1b9f0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba706c",
      "DATA",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba7070",
      "READ",
      [
        "storage",
        "010a2850",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba7068",
      "READ",
      [
        "storage",
        "00c1ba40",
        null,
        "pointer"
      ]
    ],
    [
      "00ba706c",
      "DATA",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba7070",
      "READ",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba705c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7000.md#insn-00ba705c) · [`00ba7088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7000.md#insn-00ba7088) · [`00ba7024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7000.md#insn-00ba7024)
- 新版 `00ba70a0`（命令位置の公開資料なし） · `00ba70cc`（命令位置の公開資料なし） · `00ba7068`（命令位置の公開資料なし）

~~~diff
- 00ba705c ["INT_ADD", "register:40f0:8", ["const:ba705c:8", "const:4:8"]]
- 00ba705c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba70a0 ["INT_ADD", "register:40f0:8", ["const:ba70a0:8", "const:4:8"]]
+ 00ba70a0 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba705c bytes 8de70094
+ 00ba70a0 bytes 90e70094
- 00ba7088 ["INT_ADD", "register:40f0:8", ["const:ba7088:8", "const:4:8"]]
- 00ba7088 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba70cc ["INT_ADD", "register:40f0:8", ["const:ba70cc:8", "const:4:8"]]
+ 00ba70cc ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba7088 bytes 66bf0094
+ 00ba70cc bytes 65bf0094
- 00ba7024 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
- 00ba7024 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba7068 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a40:8"]]
+ 00ba7068 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba7024 bytes 94fa44f9
+ 00ba7068 bytes 942245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f07bef2f8f219dc9f97ebfb4df7034bd"></a>

### [`00ba7144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7144.md) → [`00ba7188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7188.md) FUN_00ba7188

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba71ac",
      "incomplete_value": true,
      "site": "00ba71b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7168",
      "incomplete_value": true,
      "site": "00ba716c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba71b8",
      "incomplete_value": true,
      "site": "00ba71bc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba7174",
      "incomplete_value": true,
      "site": "00ba7178",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba71e0",
      "incomplete_value": true,
      "site": "00ba71e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba719c",
      "incomplete_value": true,
      "site": "00ba71a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd8:8"
              ]
            ]
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
      "00ba71ac",
      "READ",
      [
        "storage",
        "00c1bcd8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba71b0",
      "DATA",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba71b4",
      "READ",
      [
        "storage",
        "010a2860",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba71ac",
      "READ",
      [
        "storage",
        "00c1bd28",
        null,
        "pointer"
      ]
    ],
    [
      "00ba71b0",
      "DATA",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba71b4",
      "READ",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk17num_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba71a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7144.md#insn-00ba71a0) · [`00ba71cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7144.md#insn-00ba71cc) · [`00ba7168`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7144.md#insn-00ba7168)
- 新版 `00ba71e4`（命令位置の公開資料なし） · `00ba7210`（命令位置の公開資料なし） · `00ba71ac`（命令位置の公開資料なし）

~~~diff
- 00ba71a0 ["INT_ADD", "register:40f0:8", ["const:ba71a0:8", "const:4:8"]]
- 00ba71a0 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba71e4 ["INT_ADD", "register:40f0:8", ["const:ba71e4:8", "const:4:8"]]
+ 00ba71e4 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba71a0 bytes 3ce70094
+ 00ba71e4 bytes 3fe70094
- 00ba71cc ["INT_ADD", "register:40f0:8", ["const:ba71cc:8", "const:4:8"]]
- 00ba71cc ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba7210 ["INT_ADD", "register:40f0:8", ["const:ba7210:8", "const:4:8"]]
+ 00ba7210 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba71cc bytes 15bf0094
+ 00ba7210 bytes 14bf0094
- 00ba7168 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd8:8"]]
- 00ba7168 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba71ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
+ 00ba71ac ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba7168 bytes 946e46f9
+ 00ba71ac bytes 949646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe162dcbaf9fa55f0918739b6d2a54c7"></a>

### [`00ba7288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7288.md) → [`00ba72cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba72cc.md) FUN_00ba72cc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba72f0",
      "incomplete_value": true,
      "site": "00ba72f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba72ac",
      "incomplete_value": true,
      "site": "00ba72b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba72fc",
      "incomplete_value": true,
      "site": "00ba7300",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba72b8",
      "incomplete_value": true,
      "site": "00ba72bc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba7324",
      "incomplete_value": true,
      "site": "00ba7328",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba72e0",
      "incomplete_value": true,
      "site": "00ba72e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b0:8"
              ]
            ]
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
      "00ba72f0",
      "READ",
      [
        "storage",
        "00c1b4b0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba72f4",
      "DATA",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba72f8",
      "READ",
      [
        "storage",
        "010a2870",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba72f0",
      "READ",
      [
        "storage",
        "00c1b500",
        null,
        "pointer"
      ]
    ],
    [
      "00ba72f4",
      "DATA",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba72f8",
      "READ",
      [
        "storage",
        "010a28b0",
        "_ZNSt6__ndk18time_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba72e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7288.md#insn-00ba72e4) · [`00ba7310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7288.md#insn-00ba7310) · [`00ba72ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7288.md#insn-00ba72ac)
- 新版 `00ba7328`（命令位置の公開資料なし） · `00ba7354`（命令位置の公開資料なし） · `00ba72f0`（命令位置の公開資料なし）

~~~diff
- 00ba72e4 ["INT_ADD", "register:40f0:8", ["const:ba72e4:8", "const:4:8"]]
- 00ba72e4 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba7328 ["INT_ADD", "register:40f0:8", ["const:ba7328:8", "const:4:8"]]
+ 00ba7328 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba72e4 bytes ebe60094
+ 00ba7328 bytes eee60094
- 00ba7310 ["INT_ADD", "register:40f0:8", ["const:ba7310:8", "const:4:8"]]
- 00ba7310 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba7354 ["INT_ADD", "register:40f0:8", ["const:ba7354:8", "const:4:8"]]
+ 00ba7354 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba7310 bytes c4be0094
+ 00ba7354 bytes c3be0094
- 00ba72ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4b0:8"]]
- 00ba72ac ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba72f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:500:8"]]
+ 00ba72f0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba72ac bytes 945a42f9
+ 00ba72f0 bytes 948242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71e51023b09a730d02f508ca599f32a1"></a>

### [`00ba73cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba73cc.md) → [`00ba7410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7410.md) FUN_00ba7410

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba7434",
      "incomplete_value": true,
      "site": "00ba7438",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba73f0",
      "incomplete_value": true,
      "site": "00ba73f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba7440",
      "incomplete_value": true,
      "site": "00ba7444",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba73fc",
      "incomplete_value": true,
      "site": "00ba7400",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba7468",
      "incomplete_value": true,
      "site": "00ba746c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7424",
      "incomplete_value": true,
      "site": "00ba7428",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e70:8"
              ]
            ]
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
      "00ba7434",
      "READ",
      [
        "storage",
        "00c1be70",
        null,
        "pointer"
      ]
    ],
    [
      "00ba7438",
      "DATA",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba743c",
      "READ",
      [
        "storage",
        "010a2880",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba7434",
      "READ",
      [
        "storage",
        "00c1bec0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba7438",
      "DATA",
      [
        "storage",
        "010a28c0",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba743c",
      "READ",
      [
        "storage",
        "010a28c0",
        "_ZNSt6__ndk18time_getIwNS_19istreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba73cc.md#insn-00ba7428) · [`00ba7454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba73cc.md#insn-00ba7454) · [`00ba73f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba73cc.md#insn-00ba73f0)
- 新版 `00ba746c`（命令位置の公開資料なし） · `00ba7498`（命令位置の公開資料なし） · `00ba7434`（命令位置の公開資料なし）

~~~diff
- 00ba7428 ["INT_ADD", "register:40f0:8", ["const:ba7428:8", "const:4:8"]]
- 00ba7428 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba746c ["INT_ADD", "register:40f0:8", ["const:ba746c:8", "const:4:8"]]
+ 00ba746c ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba7428 bytes 9ae60094
+ 00ba746c bytes 9de60094
- 00ba7454 ["INT_ADD", "register:40f0:8", ["const:ba7454:8", "const:4:8"]]
- 00ba7454 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba7498 ["INT_ADD", "register:40f0:8", ["const:ba7498:8", "const:4:8"]]
+ 00ba7498 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba7454 bytes 73be0094
+ 00ba7498 bytes 72be0094
- 00ba73f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e70:8"]]
- 00ba73f0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba7434 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ec0:8"]]
+ 00ba7434 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba73f0 bytes 943a47f9
+ 00ba7434 bytes 946247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c714472e59befed6a2f65ff29b189b0"></a>

### [`00ba7510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7510.md) → [`00ba7554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7554.md) FUN_00ba7554

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba7578",
      "incomplete_value": true,
      "site": "00ba757c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7534",
      "incomplete_value": true,
      "site": "00ba7538",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba7584",
      "incomplete_value": true,
      "site": "00ba7588",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba7540",
      "incomplete_value": true,
      "site": "00ba7544",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba75ac",
      "incomplete_value": true,
      "site": "00ba75b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7568",
      "incomplete_value": true,
      "site": "00ba756c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
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
      "00ba7578",
      "READ",
      [
        "storage",
        "00c1b4b8",
        null,
        "pointer"
      ]
    ],
    [
      "00ba757c",
      "DATA",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba7580",
      "READ",
      [
        "storage",
        "010a2890",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba7578",
      "READ",
      [
        "storage",
        "00c1b508",
        null,
        "pointer"
      ]
    ],
    [
      "00ba757c",
      "DATA",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba7580",
      "READ",
      [
        "storage",
        "010a28d0",
        "_ZNSt6__ndk18time_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba756c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7510.md#insn-00ba756c) · [`00ba7598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7510.md#insn-00ba7598) · [`00ba7534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7510.md#insn-00ba7534)
- 新版 `00ba75b0`（命令位置の公開資料なし） · `00ba75dc`（命令位置の公開資料なし） · `00ba7578`（命令位置の公開資料なし）

~~~diff
- 00ba756c ["INT_ADD", "register:40f0:8", ["const:ba756c:8", "const:4:8"]]
- 00ba756c ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba75b0 ["INT_ADD", "register:40f0:8", ["const:ba75b0:8", "const:4:8"]]
+ 00ba75b0 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba756c bytes 49e60094
+ 00ba75b0 bytes 4ce60094
- 00ba7598 ["INT_ADD", "register:40f0:8", ["const:ba7598:8", "const:4:8"]]
- 00ba7598 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba75dc ["INT_ADD", "register:40f0:8", ["const:ba75dc:8", "const:4:8"]]
+ 00ba75dc ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba7598 bytes 22be0094
+ 00ba75dc bytes 21be0094
- 00ba7534 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4b8:8"]]
- 00ba7534 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba7578 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
+ 00ba7578 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba7534 bytes 945e42f9
+ 00ba7578 bytes 948642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60c4b559bbb797b2171e574c0631afa7"></a>

### [`00ba7654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7654.md) → [`00ba7698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7698.md) FUN_00ba7698

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba76bc",
      "incomplete_value": true,
      "site": "00ba76c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7678",
      "incomplete_value": true,
      "site": "00ba767c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba76c8",
      "incomplete_value": true,
      "site": "00ba76cc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba7684",
      "incomplete_value": true,
      "site": "00ba7688",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba76f0",
      "incomplete_value": true,
      "site": "00ba76f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba76ac",
      "incomplete_value": true,
      "site": "00ba76b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e90:8"
              ]
            ]
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
      "00ba76bc",
      "READ",
      [
        "storage",
        "00c1be90",
        null,
        "pointer"
      ]
    ],
    [
      "00ba76c0",
      "DATA",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba76c4",
      "READ",
      [
        "storage",
        "010a28a0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba76bc",
      "READ",
      [
        "storage",
        "00c1bee0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba76c0",
      "DATA",
      [
        "storage",
        "010a28e0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba76c4",
      "READ",
      [
        "storage",
        "010a28e0",
        "_ZNSt6__ndk18time_putIwNS_19ostreambuf_iteratorIwNS_11char_traitsIwEEEEE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba76b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7654.md#insn-00ba76b0) · [`00ba76dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7654.md#insn-00ba76dc) · [`00ba7678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7654.md#insn-00ba7678)
- 新版 `00ba76f4`（命令位置の公開資料なし） · `00ba7720`（命令位置の公開資料なし） · `00ba76bc`（命令位置の公開資料なし）

~~~diff
- 00ba76b0 ["INT_ADD", "register:40f0:8", ["const:ba76b0:8", "const:4:8"]]
- 00ba76b0 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba76f4 ["INT_ADD", "register:40f0:8", ["const:ba76f4:8", "const:4:8"]]
+ 00ba76f4 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba76b0 bytes f8e50094
+ 00ba76f4 bytes fbe50094
- 00ba76dc ["INT_ADD", "register:40f0:8", ["const:ba76dc:8", "const:4:8"]]
- 00ba76dc ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba7720 ["INT_ADD", "register:40f0:8", ["const:ba7720:8", "const:4:8"]]
+ 00ba7720 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba76dc bytes d1bd0094
+ 00ba7720 bytes d0bd0094
- 00ba7678 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e90:8"]]
- 00ba7678 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba76bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ee0:8"]]
+ 00ba76bc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba7678 bytes 944a47f9
+ 00ba76bc bytes 947247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e11b0da7fb49ca5d09275de5156231fe"></a>

### [`00ba7798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7798.md) → [`00ba77dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba77dc.md) FUN_00ba77dc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba7800",
      "incomplete_value": true,
      "site": "00ba7804",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba77bc",
      "incomplete_value": true,
      "site": "00ba77c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba780c",
      "incomplete_value": true,
      "site": "00ba7810",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba77c8",
      "incomplete_value": true,
      "site": "00ba77cc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba7834",
      "incomplete_value": true,
      "site": "00ba7838",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba77f0",
      "incomplete_value": true,
      "site": "00ba77f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ea0:8"
              ]
            ]
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
      "00ba7800",
      "READ",
      [
        "storage",
        "00c1bea0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba7804",
      "DATA",
      [
        "storage",
        "010a2930",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba7808",
      "READ",
      [
        "storage",
        "010a2930",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba7800",
      "READ",
      [
        "storage",
        "00c1bef0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba7804",
      "DATA",
      [
        "storage",
        "010a2970",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba7808",
      "READ",
      [
        "storage",
        "010a2970",
        "_ZNSt6__ndk18messagesIcE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba77f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7798.md#insn-00ba77f4) · [`00ba7820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7798.md#insn-00ba7820) · [`00ba77bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7798.md#insn-00ba77bc)
- 新版 `00ba7838`（命令位置の公開資料なし） · `00ba7864`（命令位置の公開資料なし） · `00ba7800`（命令位置の公開資料なし）

~~~diff
- 00ba77f4 ["INT_ADD", "register:40f0:8", ["const:ba77f4:8", "const:4:8"]]
- 00ba77f4 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba7838 ["INT_ADD", "register:40f0:8", ["const:ba7838:8", "const:4:8"]]
+ 00ba7838 ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba77f4 bytes a7e50094
+ 00ba7838 bytes aae50094
- 00ba7820 ["INT_ADD", "register:40f0:8", ["const:ba7820:8", "const:4:8"]]
- 00ba7820 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba7864 ["INT_ADD", "register:40f0:8", ["const:ba7864:8", "const:4:8"]]
+ 00ba7864 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba7820 bytes 80bd0094
+ 00ba7864 bytes 7fbd0094
- 00ba77bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ea0:8"]]
- 00ba77bc ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba7800 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ef0:8"]]
+ 00ba7800 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba77bc bytes 945247f9
+ 00ba7800 bytes 947a47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-615f86c3cf28f99f5ed346003e8df7da"></a>

### [`00ba78dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba78dc.md) → [`00ba7920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7920.md) FUN_00ba7920

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba50c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 呼出先 6件 [`00b890a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b89/00b890a4.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bb9104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb9104.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba5108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba5/00ba5108.md) · 呼出先 6件 [`00b890e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b89/00b890e8.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bb9148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9148.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_value

命令の説明率　旧版 91.43% / 新版 91.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba7944",
      "incomplete_value": true,
      "site": "00ba7948",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7900",
      "incomplete_value": true,
      "site": "00ba7904",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb0:8"
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba7950",
      "incomplete_value": true,
      "site": "00ba7954",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba790c",
      "incomplete_value": true,
      "site": "00ba7910",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_ADD",
            "8",
            [
              "LOAD",
              [
                "leaf",
                "const:1:8"
              ]
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
      "definition_site": "00ba7978",
      "incomplete_value": true,
      "site": "00ba797c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7934",
      "incomplete_value": true,
      "site": "00ba7938",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb0:8"
              ]
            ]
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
      "00ba7944",
      "READ",
      [
        "storage",
        "00c1beb0",
        null,
        "pointer"
      ]
    ],
    [
      "00ba7948",
      "DATA",
      [
        "storage",
        "010a2940",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba794c",
      "READ",
      [
        "storage",
        "010a2940",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba7944",
      "READ",
      [
        "storage",
        "00c1bf00",
        null,
        "pointer"
      ]
    ],
    [
      "00ba7948",
      "DATA",
      [
        "storage",
        "010a2980",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ],
    [
      "00ba794c",
      "READ",
      [
        "storage",
        "010a2980",
        "_ZNSt6__ndk18messagesIwE2idE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba78dc.md#insn-00ba7938) · [`00ba7964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba78dc.md#insn-00ba7964) · [`00ba7900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba78dc.md#insn-00ba7900)
- 新版 `00ba797c`（命令位置の公開資料なし） · `00ba79a8`（命令位置の公開資料なし） · `00ba7944`（命令位置の公開資料なし）

~~~diff
- 00ba7938 ["INT_ADD", "register:40f0:8", ["const:ba7938:8", "const:4:8"]]
- 00ba7938 ["CALL", null, ["callee:00be0ee0:8"]]
+ 00ba797c ["INT_ADD", "register:40f0:8", ["const:ba797c:8", "const:4:8"]]
+ 00ba797c ["CALL", null, ["callee:00be0ee0:8"]]
- 00ba7938 bytes 56e50094
+ 00ba797c bytes 59e50094
- 00ba7964 ["INT_ADD", "register:40f0:8", ["const:ba7964:8", "const:4:8"]]
- 00ba7964 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba79a8 ["INT_ADD", "register:40f0:8", ["const:ba79a8:8", "const:4:8"]]
+ 00ba79a8 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba7964 bytes 2fbd0094
+ 00ba79a8 bytes 2ebd0094
- 00ba7900 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:eb0:8"]]
- 00ba7900 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba7944 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:f00:8"]]
+ 00ba7944 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba7900 bytes 945a47f9
+ 00ba7944 bytes 948247f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-894a9f51b0d8f4040cc61e792d0385d5"></a>

### [`00ba7a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7a20.md) → [`00ba7a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7a64.md) FUN_00ba7a64

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00ba845c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba845c.md) · 呼出先 10件 [`00bb8a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a1c.md) [`00bb8a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8a34.md) [`00bb8b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8b90.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00ba84a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba84a0.md) · 呼出先 10件 [`00bb8a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8a60.md) [`00bb8a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8a78.md) [`00bb8bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8bd4.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 98.25% / 新版 98.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba7a94",
      "incomplete_value": false,
      "site": "00ba7a94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7a50",
      "incomplete_value": false,
      "site": "00ba7a50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "00ba7a94",
      "DATA",
      [
        "storage",
        "00c138c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ba7a94",
      "DATA",
      [
        "storage",
        "00c13918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7a20.md#insn-00ba7a48) · [`00ba7a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7a20.md#insn-00ba7a4c)
- 新版 `00ba7a8c`（命令位置の公開資料なし） · `00ba7a90`（命令位置の公開資料なし）

~~~diff
- 00ba7a48 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00ba7a48 ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
- 00ba7a48 ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
- 00ba7a48 ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
+ 00ba7a8c ["COPY", "tmp:0:8", ["const:918:8"]]
+ 00ba7a8c ["INT_CARRY", "register:105:1", ["register:4058:8", "tmp:0:8"]]
+ 00ba7a8c ["INT_SCARRY", "register:106:1", ["register:4058:8", "tmp:0:8"]]
+ 00ba7a8c ["INT_ADD", "tmp:1:8", ["register:4058:8", "tmp:0:8"]]
- 00ba7a48 bytes 6b212391
+ 00ba7a8c bytes 6b612491
- 00ba7a4c ["COPY", "register:4098:8", ["register:4000:8"]]
- 00ba7a4c bytes f30300aa
+ 00ba7a90 ["COPY", "register:4098:8", ["register:4000:8"]]
+ 00ba7a90 bytes f30300aa
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78262302886d671fe2b8cf5aad0fb91a"></a>

### [`00ba7cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7cf4.md) → [`00ba7d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7d38.md) FUN_00ba7d38

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ba7dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7dc8.md) · 呼出先 3件 [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 1件 [`00ba7e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7e0c.md) · 呼出先 3件 [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

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
      "definition_site": "00ba7d58",
      "incomplete_value": false,
      "site": "00ba7d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:918:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7d14",
      "incomplete_value": false,
      "site": "00ba7d1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c13000:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "00ba7d60",
      "DATA",
      [
        "storage",
        "00c138c8",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00ba7d60",
      "DATA",
      [
        "storage",
        "00c13918",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7cf4.md#insn-00ba7d60) · [`00ba7d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7cf4.md#insn-00ba7d14) · [`00ba7d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7cf4.md#insn-00ba7d74)
- 新版 `00ba7da4`（命令位置の公開資料なし） · `00ba7d58`（命令位置の公開資料なし） · `00ba7db8`（命令位置の公開資料なし）

~~~diff
- 00ba7d60 ["INT_ADD", "register:40f0:8", ["const:ba7d60:8", "const:4:8"]]
- 00ba7d60 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00ba7da4 ["INT_ADD", "register:40f0:8", ["const:ba7da4:8", "const:4:8"]]
+ 00ba7da4 ["CALL", null, ["callee:00bd6e90:8"]]
- 00ba7d60 bytes 3cbc0094
+ 00ba7da4 bytes 3bbc0094
- 00ba7d14 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00ba7d14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ba7d14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ba7d14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ba7d58 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 00ba7d58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ba7d58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ba7d58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ba7d14 bytes 08212391
+ 00ba7d58 bytes 08612491
- 00ba7d74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ba7d74 ["INT_ADD", "register:40f0:8", ["const:ba7d74:8", "const:4:8"]]
- 00ba7d74 ["CALLIND", null, ["register:0:8"]]
+ 00ba7db8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ba7db8 ["INT_ADD", "register:40f0:8", ["const:ba7db8:8", "const:4:8"]]
+ 00ba7db8 ["CALLIND", null, ["register:0:8"]]
- 00ba7d74 bytes 00013fd6
+ 00ba7db8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bd9b0232e7d8b60c9585428aa649133"></a>

### [`00ba7df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7df4.md) → [`00ba7e38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7e38.md) _ZNSt6__ndk16locale8__globalEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1880.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be18d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 74.07% / 新版 74.07%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba7e74",
      "incomplete_value": false,
      "site": "00ba7e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7e30",
      "incomplete_value": false,
      "site": "00ba7e34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "definition_site": "00ba7e8c",
      "incomplete_value": false,
      "site": "00ba7e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7e48",
      "incomplete_value": false,
      "site": "00ba7e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "definition_site": "00ba7e98",
      "incomplete_value": false,
      "site": "00ba7e9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7e54",
      "incomplete_value": false,
      "site": "00ba7e58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "00ba7e50",
      "READ",
      [
        "storage",
        "010a2ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba7e5c",
      "DATA",
      [
        "storage",
        "010a2aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ba7e74",
      "PARAM",
      [
        "storage",
        "010a2ab0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ba7e50",
      "READ",
      [
        "storage",
        "010a2af0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba7e5c",
      "DATA",
      [
        "storage",
        "010a2ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ba7e74",
      "PARAM",
      [
        "storage",
        "010a2af0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7df4.md#insn-00ba7e08) · [`00ba7e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7df4.md#insn-00ba7e34) · [`00ba7e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7df4.md#insn-00ba7e4c)
- 新版 `00ba7e4c`（命令位置の公開資料なし） · `00ba7e78`（命令位置の公開資料なし） · `00ba7e90`（命令位置の公開資料なし）

~~~diff
- 00ba7e08 ["COPY", "tmp:0:8", ["const:ab0:8"]]
- 00ba7e08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ba7e08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ba7e08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ba7e4c ["COPY", "tmp:0:8", ["const:af0:8"]]
+ 00ba7e4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ba7e4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ba7e4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ba7e08 bytes 08c12a91
+ 00ba7e4c bytes 08c12b91
- 00ba7e34 ["INT_ADD", "register:40f0:8", ["const:ba7e34:8", "const:4:8"]]
- 00ba7e34 ["CALL", null, ["callee:00bdb000:8"]]
+ 00ba7e78 ["INT_ADD", "register:40f0:8", ["const:ba7e78:8", "const:4:8"]]
+ 00ba7e78 ["CALL", null, ["callee:00bdb000:8"]]
- 00ba7e34 bytes 5fcc0094
+ 00ba7e78 bytes 62cc0094
- 00ba7e4c ["INT_ADD", "register:40f0:8", ["const:ba7e4c:8", "const:4:8"]]
- 00ba7e4c ["CALL", null, ["callee:00bdd980:8"]]
+ 00ba7e90 ["INT_ADD", "register:40f0:8", ["const:ba7e90:8", "const:4:8"]]
+ 00ba7e90 ["CALL", null, ["callee:00bdd980:8"]]
- 00ba7e4c bytes b9d60094
+ 00ba7e90 bytes bcd60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c102ea3805a79702a9fa526fe298761f"></a>

### [`00ba7e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7e78.md) → [`00ba7ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7ebc.md) _ZNSt6__ndk16localeC1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdd900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd900.md) · 呼出先 5件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) [`00be1880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1880.md)
- 新版 呼出元 1件 [`00bdd950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd950.md) · 呼出先 5件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) [`00be18d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be18d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 69.44% / 新版 69.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba7f1c",
      "incomplete_value": false,
      "site": "00ba7f20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7ed8",
      "incomplete_value": false,
      "site": "00ba7edc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "definition_site": "00ba7f34",
      "incomplete_value": false,
      "site": "00ba7f38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7ef0",
      "incomplete_value": false,
      "site": "00ba7ef4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "definition_site": "00ba7f40",
      "incomplete_value": false,
      "site": "00ba7f44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:af0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba7efc",
      "incomplete_value": false,
      "site": "00ba7f00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ab0:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ba7ed8",
      "READ",
      [
        "storage",
        "010a2ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba7eec",
      "READ",
      [
        "storage",
        "010a2aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ba7f1c",
      "PARAM",
      [
        "storage",
        "010a2ab0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ba7ed8",
      "READ",
      [
        "storage",
        "010a2af0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba7eec",
      "READ",
      [
        "storage",
        "010a2ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ba7f1c",
      "PARAM",
      [
        "storage",
        "010a2af0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7e78.md#insn-00ba7edc) · [`00ba7ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7e78.md#insn-00ba7ef4) · [`00ba7f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7e78.md#insn-00ba7f00)
- 新版 `00ba7f20`（命令位置の公開資料なし） · `00ba7f38`（命令位置の公開資料なし） · `00ba7f44`（命令位置の公開資料なし）

~~~diff
- 00ba7edc ["INT_ADD", "register:40f0:8", ["const:ba7edc:8", "const:4:8"]]
- 00ba7edc ["CALL", null, ["callee:00bdb000:8"]]
+ 00ba7f20 ["INT_ADD", "register:40f0:8", ["const:ba7f20:8", "const:4:8"]]
+ 00ba7f20 ["CALL", null, ["callee:00bdb000:8"]]
- 00ba7edc bytes 35cc0094
+ 00ba7f20 bytes 38cc0094
- 00ba7ef4 ["INT_ADD", "register:40f0:8", ["const:ba7ef4:8", "const:4:8"]]
- 00ba7ef4 ["CALL", null, ["callee:00bdd980:8"]]
+ 00ba7f38 ["INT_ADD", "register:40f0:8", ["const:ba7f38:8", "const:4:8"]]
+ 00ba7f38 ["CALL", null, ["callee:00bdd980:8"]]
- 00ba7ef4 bytes 8fd60094
+ 00ba7f38 bytes 92d60094
- 00ba7f00 ["INT_ADD", "register:40f0:8", ["const:ba7f00:8", "const:4:8"]]
- 00ba7f00 ["CALL", null, ["callee:00bdb020:8"]]
+ 00ba7f44 ["INT_ADD", "register:40f0:8", ["const:ba7f44:8", "const:4:8"]]
+ 00ba7f44 ["CALL", null, ["callee:00bdb020:8"]]
- 00ba7f00 bytes 34cc0094
+ 00ba7f44 bytes 37cc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f8d7b8cc874b95a07a1e241c37494d4"></a>

### [`00ba7f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7f20.md) → [`00ba7f64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7f64.md) _ZNSt6__ndk16localeC1ERKS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 1件 [`00bdd930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd930.md) · 呼出先 1件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md)
- 新版 呼出元 1件 [`00bdd980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd980.md) · 呼出先 1件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba7f74",
      "incomplete_value": true,
      "site": "00ba7f7c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00ba7f30",
      "incomplete_value": true,
      "site": "00ba7f38",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ba7f38"
      ],
      [
        "FALL_THROUGH",
        "00ba7f7c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ba7f74",
      "incomplete_value": true,
      "site": "00ba7f84",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00ba7f30",
      "incomplete_value": true,
      "site": "00ba7f40",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00ba7f38"
      ],
      [
        "FALL_THROUGH",
        "00ba7f7c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ba7f74",
      "incomplete_value": true,
      "site": "00ba7f84",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00ba7f30",
      "incomplete_value": true,
      "site": "00ba7f40",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ba7f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7f20.md#insn-00ba7f2c) · [`00ba7f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7f20.md#insn-00ba7f50)
- 新版 `00ba7f70`（命令位置の公開資料なし） · `00ba7f94`（命令位置の公開資料なし）

~~~diff
- 00ba7f2c ["COPY", "tmp:0:8", ["const:960:8"]]
- 00ba7f2c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00ba7f2c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00ba7f2c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00ba7f70 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00ba7f70 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00ba7f70 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00ba7f70 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00ba7f2c bytes 29812591
+ 00ba7f70 bytes 29812691
- 00ba7f50 ["INT_ADD", "register:40f0:8", ["const:ba7f50:8", "const:4:8"]]
- 00ba7f50 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba7f94 ["INT_ADD", "register:40f0:8", ["const:ba7f94:8", "const:4:8"]]
+ 00ba7f94 ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba7f50 bytes b4bb0094
+ 00ba7f94 bytes b3bb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c5da09f681a39d1ab701b9a8a0e0ad4"></a>

### [`00ba7fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7fc0.md) → [`00ba8004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8004.md) _ZNSt6__ndk16localeaSERKS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `unresolved` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be1290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1290.md) · 呼出先 2件 [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md)
- 新版 呼出元 1件 [`00be12e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be12e0.md) · 呼出先 2件 [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba802c",
      "incomplete_value": true,
      "site": "00ba8030",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00ba7fe8",
      "incomplete_value": true,
      "site": "00ba7fec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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


#### 変更候補の命令位置

- 旧版 [`00ba7fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7fc0.md#insn-00ba7fdc) · [`00ba7ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7fc0.md#insn-00ba7ff8) · [`00ba8010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7fc0.md#insn-00ba8010)
- 新版 `00ba8020`（命令位置の公開資料なし） · `00ba803c`（命令位置の公開資料なし） · `00ba8054`（命令位置の公開資料なし）

~~~diff
- 00ba7fdc ["COPY", "tmp:0:8", ["const:960:8"]]
- 00ba7fdc ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00ba7fdc ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00ba7fdc ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00ba8020 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00ba8020 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00ba8020 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00ba8020 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00ba7fdc bytes d6822591
+ 00ba8020 bytes d6822691
- 00ba7ff8 ["INT_ADD", "register:40f0:8", ["const:ba7ff8:8", "const:4:8"]]
- 00ba7ff8 ["CALL", null, ["callee:00bd6e60:8"]]
+ 00ba803c ["INT_ADD", "register:40f0:8", ["const:ba803c:8", "const:4:8"]]
+ 00ba803c ["CALL", null, ["callee:00bd6e60:8"]]
- 00ba7ff8 bytes 8abb0094
+ 00ba803c bytes 89bb0094
- 00ba8010 ["INT_ADD", "register:40f0:8", ["const:ba8010:8", "const:4:8"]]
- 00ba8010 ["CALL", null, ["callee:00bd6e90:8"]]
+ 00ba8054 ["INT_ADD", "register:40f0:8", ["const:ba8054:8", "const:4:8"]]
+ 00ba8054 ["CALL", null, ["callee:00bd6e90:8"]]
- 00ba8010 bytes 90bb0094
+ 00ba8054 bytes 8fbb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5859733924d017d249386364324b3eaa"></a>

### [`00ba8048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8048.md) → [`00ba808c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba808c.md) _ZNSt6__ndk16localeC1EPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00ba25d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba2/00ba25d8.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00ba261c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba2/00ba261c.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba8188",
      "incomplete_value": false,
      "site": "00ba818c",
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
            "const:2ef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba8144",
      "incomplete_value": false,
      "site": "00ba8148",
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
            "const:264:8"
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
      "00ba8188",
      "PARAM",
      [
        "storage",
        "002a5264",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ba8188",
      "PARAM",
      [
        "storage",
        "002a52ef",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8048.md#insn-00ba8148) · [`00ba8074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8048.md#insn-00ba8074) · [`00ba8080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8048.md#insn-00ba8080)
- 新版 `00ba818c`（命令位置の公開資料なし） · `00ba80b8`（命令位置の公開資料なし） · `00ba80c4`（命令位置の公開資料なし）

~~~diff
- 00ba8148 ["INT_ADD", "register:40f0:8", ["const:ba8148:8", "const:4:8"]]
- 00ba8148 ["CALL", null, ["callee:00be0fb0:8"]]
+ 00ba818c ["INT_ADD", "register:40f0:8", ["const:ba818c:8", "const:4:8"]]
+ 00ba818c ["CALL", null, ["callee:00be0fb0:8"]]
- 00ba8148 bytes 86e30094
+ 00ba818c bytes 89e30094
- 00ba8074 ["INT_ADD", "register:40f0:8", ["const:ba8074:8", "const:4:8"]]
- 00ba8074 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ba80b8 ["INT_ADD", "register:40f0:8", ["const:ba80b8:8", "const:4:8"]]
+ 00ba80b8 ["CALL", null, ["callee:00bdb040:8"]]
- 00ba8074 bytes dfcb0094
+ 00ba80b8 bytes e2cb0094
- 00ba8080 ["INT_ADD", "register:40f0:8", ["const:ba8080:8", "const:4:8"]]
- 00ba8080 ["CALL", null, ["callee:00bdb190:8"]]
+ 00ba80c4 ["INT_ADD", "register:40f0:8", ["const:ba80c4:8", "const:4:8"]]
+ 00ba80c4 ["CALL", null, ["callee:00bdb190:8"]]
- 00ba8080 bytes 30cc0094
+ 00ba80c4 bytes 33cc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10a4580bcc7f2b3ba0117c026974ca8a"></a>

### [`00ba81ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba81ec.md) → [`00ba8230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8230.md) _ZNSt6__ndk16localeC2ERKS0_PKci

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00418c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418c24.md) [`00ba4a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba4/00ba4a74.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00418c24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418c24.md) [`00ba4ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba4/00ba4ab8.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.63% / 新版 98.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba8344",
      "incomplete_value": false,
      "site": "00ba8348",
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
            "const:2ef:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba8300",
      "incomplete_value": false,
      "site": "00ba8304",
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
            "const:264:8"
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
      "00ba8344",
      "PARAM",
      [
        "storage",
        "002a5264",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ba8344",
      "PARAM",
      [
        "storage",
        "002a52ef",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba81ec.md#insn-00ba8304) · [`00ba8224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba81ec.md#insn-00ba8224) · [`00ba8234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba81ec.md#insn-00ba8234)
- 新版 `00ba8348`（命令位置の公開資料なし） · `00ba8268`（命令位置の公開資料なし） · `00ba8278`（命令位置の公開資料なし）

~~~diff
- 00ba8304 ["INT_ADD", "register:40f0:8", ["const:ba8304:8", "const:4:8"]]
- 00ba8304 ["CALL", null, ["callee:00be0fb0:8"]]
+ 00ba8348 ["INT_ADD", "register:40f0:8", ["const:ba8348:8", "const:4:8"]]
+ 00ba8348 ["CALL", null, ["callee:00be0fb0:8"]]
- 00ba8304 bytes 17e30094
+ 00ba8348 bytes 1ae30094
- 00ba8224 ["INT_ADD", "register:40f0:8", ["const:ba8224:8", "const:4:8"]]
- 00ba8224 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ba8268 ["INT_ADD", "register:40f0:8", ["const:ba8268:8", "const:4:8"]]
+ 00ba8268 ["CALL", null, ["callee:00bdb040:8"]]
- 00ba8224 bytes 73cb0094
+ 00ba8268 bytes 76cb0094
- 00ba8234 ["INT_ADD", "register:40f0:8", ["const:ba8234:8", "const:4:8"]]
- 00ba8234 ["CALL", null, ["callee:00bdb190:8"]]
+ 00ba8278 ["INT_ADD", "register:40f0:8", ["const:ba8278:8", "const:4:8"]]
+ 00ba8278 ["CALL", null, ["callee:00bdb190:8"]]
- 00ba8234 bytes c3cb0094
+ 00ba8278 bytes c6cb0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74ee00b9b520398485724d413f16a24a"></a>

### [`00ba845c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba845c.md) → [`00ba84a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba84a0.md) _ZNSt6__ndk16locale14__install_ctorERKS0_PNS0_5facetEl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `equal`

- 旧版 呼出元 0件  · 呼出先 3件 [`00ba7a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7a20.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00ba7a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba7/00ba7a64.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 branch_value, constant, operands_and_dependencies

命令の説明率　旧版 90.91% / 新版 90.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba84f8",
      "incomplete_value": true,
      "site": "00ba8500",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00ba84b4",
      "incomplete_value": true,
      "site": "00ba84bc",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
  }
]
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba845c.md#insn-00ba8488) · [`00ba849c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba845c.md#insn-00ba849c) · [`00ba84b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba845c.md#insn-00ba84b0)
- 新版 `00ba84cc`（命令位置の公開資料なし） · `00ba84e0`（命令位置の公開資料なし） · `00ba84f4`（命令位置の公開資料なし）

~~~diff
- 00ba8488 ["INT_ADD", "register:40f0:8", ["const:ba8488:8", "const:4:8"]]
- 00ba8488 ["CALL", null, ["callee:00bdb040:8"]]
+ 00ba84cc ["INT_ADD", "register:40f0:8", ["const:ba84cc:8", "const:4:8"]]
+ 00ba84cc ["CALL", null, ["callee:00bdb040:8"]]
- 00ba8488 bytes daca0094
+ 00ba84cc bytes ddca0094
- 00ba849c ["INT_ADD", "register:40f0:8", ["const:ba849c:8", "const:4:8"]]
- 00ba849c ["CALL", null, ["callee:00ba7a64:8"]]
+ 00ba84e0 ["INT_ADD", "register:40f0:8", ["const:ba84e0:8", "const:4:8"]]
+ 00ba84e0 ["CALL", null, ["callee:00ba7a64:8"]]
- 00ba849c bytes 61fdff97
+ 00ba84e0 bytes 61fdff97
- 00ba84b0 ["COPY", "tmp:0:8", ["const:960:8"]]
- 00ba84b0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ba84b0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ba84b0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ba84f4 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00ba84f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ba84f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ba84f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ba84b0 bytes 08812591
+ 00ba84f4 bytes 08812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a338eafbe2d5bc82c8c4b30768b858d0"></a>

### [`00ba84f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba84f4.md) → [`00ba8538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8538.md) _ZNSt6__ndk16locale6globalERKS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00418/00418fe0.md) [`00bd6e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e20.md) [`00bd6e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd6/00bd6e50.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00418fe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00418/00418fe0.md) [`00bd6e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e60.md) [`00bd6e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd6/00bd6e90.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 88.39% / 新版 88.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba85d4",
      "incomplete_value": true,
      "site": "00ba85d4",
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
            "const:ae8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba8590",
      "incomplete_value": true,
      "site": "00ba8590",
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
            "const:aa8:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ba8588",
      "incomplete_value": true,
      "site": "00ba858c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00ba8544",
      "incomplete_value": true,
      "site": "00ba8548",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00ba85a4",
      "incomplete_value": true,
      "site": "00ba85a8",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:40b8:8"
              ]
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
      "definition_site": "00ba8560",
      "incomplete_value": true,
      "site": "00ba8564",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
              [
                "live",
                "register:40b8:8"
              ]
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ba8560",
      "READ",
      [
        "storage",
        "010a2ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba8570",
      "PARAM",
      [
        "storage",
        "010a2aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ba85a0",
      "READ",
      [
        "storage",
        "010a2aa8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ba8560",
      "READ",
      [
        "storage",
        "010a2af0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba8570",
      "PARAM",
      [
        "storage",
        "010a2ae8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ba85a0",
      "READ",
      [
        "storage",
        "010a2ae8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba84f4.md#insn-00ba8534) · [`00ba8590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba84f4.md#insn-00ba8590) · [`00ba8688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba84f4.md#insn-00ba8688)
- 新版 `00ba8578`（命令位置の公開資料なし） · `00ba85d4`（命令位置の公開資料なし） · `00ba86cc`（命令位置の公開資料なし）

~~~diff
- 00ba8534 ["INT_ADD", "register:40f0:8", ["const:ba8534:8", "const:4:8"]]
- 00ba8534 ["CALL", null, ["callee:00bdd980:8"]]
+ 00ba8578 ["INT_ADD", "register:40f0:8", ["const:ba8578:8", "const:4:8"]]
+ 00ba8578 ["CALL", null, ["callee:00bdd980:8"]]
- 00ba8534 bytes ffd40094
+ 00ba8578 bytes 02d50094
- 00ba8590 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:aa8:8"]]
- 00ba8590 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00ba85d4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:ae8:8"]]
+ 00ba85d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00ba8590 bytes c85605f9
+ 00ba85d4 bytes c87605f9
- 00ba8688 ["INT_ADD", "register:40f0:8", ["const:ba8688:8", "const:4:8"]]
- 00ba8688 ["CALL", null, ["callee:00bdb000:8"]]
+ 00ba86cc ["INT_ADD", "register:40f0:8", ["const:ba86cc:8", "const:4:8"]]
+ 00ba86cc ["CALL", null, ["callee:00bdb000:8"]]
- 00ba8688 bytes 4aca0094
+ 00ba86cc bytes 4dca0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d6ae5feab4ef1dc4c656f8fb8da9d70"></a>

### [`00ba89a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba89a8.md) → [`00ba89ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba89ec.md) _ZNSt6__ndk114collate_bynameIcEC1EPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba8a18",
      "incomplete_value": true,
      "site": "00ba8a18",
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
      "definition_site": "00ba89d4",
      "incomplete_value": true,
      "site": "00ba89d4",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba8a54",
      "incomplete_value": false,
      "site": "00ba8a64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:a1f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba8a10",
      "incomplete_value": false,
      "site": "00ba8a20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:a21:8"
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
      "00ba8a0c",
      "READ",
      [
        "storage",
        "00c1bf38",
        null,
        "pointer"
      ]
    ],
    [
      "00ba8a18",
      "DATA",
      [
        "storage",
        "00c138f0",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00ba8a54",
      "PARAM",
      [
        "storage",
        "0029aa21",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ba8a0c",
      "READ",
      [
        "storage",
        "00c1bf88",
        null,
        "pointer"
      ]
    ],
    [
      "00ba8a18",
      "DATA",
      [
        "storage",
        "00c13940",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00ba8a54",
      "PARAM",
      [
        "storage",
        "0029aa1f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba89a8.md#insn-00ba8a20) · [`00ba89c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba89a8.md#insn-00ba89c8) · [`00ba89e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba89a8.md#insn-00ba89e0)
- 新版 `00ba8a64`（命令位置の公開資料なし） · `00ba8a0c`（命令位置の公開資料なし） · `00ba8a24`（命令位置の公開資料なし）

~~~diff
- 00ba8a20 ["INT_ADD", "register:40f0:8", ["const:ba8a20:8", "const:4:8"]]
- 00ba8a20 ["CALL", null, ["callee:00ba8ac4:8"]]
+ 00ba8a64 ["INT_ADD", "register:40f0:8", ["const:ba8a64:8", "const:4:8"]]
+ 00ba8a64 ["CALL", null, ["callee:00ba8ac4:8"]]
- 00ba8a20 bytes 18000094
+ 00ba8a64 bytes 18000094
- 00ba89c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f38:8"]]
- 00ba89c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba8a0c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f88:8"]]
+ 00ba8a0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba89c8 bytes 089d47f9
+ 00ba8a0c bytes 08c547f9
- 00ba89e0 ["INT_ADD", "register:40f0:8", ["const:ba89e0:8", "const:4:8"]]
- 00ba89e0 ["CALL", null, ["callee:00be1570:8"]]
+ 00ba8a24 ["INT_ADD", "register:40f0:8", ["const:ba8a24:8", "const:4:8"]]
+ 00ba8a24 ["CALL", null, ["callee:00be1570:8"]]
- 00ba89e0 bytes d0e20094
+ 00ba8a24 bytes d3e20094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31c632af06e573bdab5b0e101d1d095b"></a>

### [`00ba8ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8ae4.md) → [`00ba8b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8b28.md) _ZNSt6__ndk114collate_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be17e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be17e0.md) · 呼出先 6件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)
- 新版 呼出元 1件 [`00be1830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1830.md) · 呼出先 6件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba8b54",
      "incomplete_value": true,
      "site": "00ba8b54",
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
      "definition_site": "00ba8b10",
      "incomplete_value": true,
      "site": "00ba8b10",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ba8b94",
      "incomplete_value": false,
      "site": "00ba8ba4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:a1f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba8b50",
      "incomplete_value": false,
      "site": "00ba8b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29a000:8"
          ],
          [
            "leaf",
            "const:a21:8"
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
      "00ba8b48",
      "READ",
      [
        "storage",
        "00c1bf38",
        null,
        "pointer"
      ]
    ],
    [
      "00ba8b54",
      "DATA",
      [
        "storage",
        "00c138f0",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00ba8b94",
      "PARAM",
      [
        "storage",
        "0029aa21",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ba8b48",
      "READ",
      [
        "storage",
        "00c1bf88",
        null,
        "pointer"
      ]
    ],
    [
      "00ba8b54",
      "DATA",
      [
        "storage",
        "00c13940",
        null,
        "undefined1[64]"
      ]
    ],
    [
      "00ba8b94",
      "PARAM",
      [
        "storage",
        "0029aa1f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8ae4.md#insn-00ba8b60) · [`00ba8ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8ae4.md#insn-00ba8ba4) · [`00ba8b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8ae4.md#insn-00ba8b04)
- 新版 `00ba8ba4`（命令位置の公開資料なし） · `00ba8be8`（命令位置の公開資料なし） · `00ba8b48`（命令位置の公開資料なし）

~~~diff
- 00ba8b60 ["INT_ADD", "register:40f0:8", ["const:ba8b60:8", "const:4:8"]]
- 00ba8b60 ["CALL", null, ["callee:00bdb260:8"]]
+ 00ba8ba4 ["INT_ADD", "register:40f0:8", ["const:ba8ba4:8", "const:4:8"]]
+ 00ba8ba4 ["CALL", null, ["callee:00bdb260:8"]]
- 00ba8b60 bytes acc90094
+ 00ba8ba4 bytes afc90094
- 00ba8ba4 ["INT_ADD", "register:40f0:8", ["const:ba8ba4:8", "const:4:8"]]
- 00ba8ba4 ["CALL", null, ["callee:00bd70ec:8"]]
+ 00ba8be8 ["INT_ADD", "register:40f0:8", ["const:ba8be8:8", "const:4:8"]]
+ 00ba8be8 ["CALL", null, ["callee:00bd70ec:8"]]
- 00ba8ba4 bytes 42b90094
+ 00ba8be8 bytes 41b90094
- 00ba8b04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f38:8"]]
- 00ba8b04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba8b48 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f88:8"]]
+ 00ba8b48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba8b04 bytes 089d47f9
+ 00ba8b48 bytes 08c547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb38e3c0cdd608857135e5425da7efbe"></a>

### [`00ba8ba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8ba8.md) → [`00ba8bec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8bec.md) _ZNSt6__ndk114collate_bynameIcED1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be18f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18f0.md) · 呼出先 2件 [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)
- 新版 呼出元 1件 [`00be1940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1940.md) · 呼出先 2件 [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba8c0c",
      "incomplete_value": true,
      "site": "00ba8c10",
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
      "definition_site": "00ba8bc8",
      "incomplete_value": true,
      "site": "00ba8bcc",
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
      "00ba8c04",
      "READ",
      [
        "storage",
        "00c1bf38",
        null,
        "pointer"
      ]
    ],
    [
      "00ba8c10",
      "DATA",
      [
        "storage",
        "00c138f0",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00ba8c04",
      "READ",
      [
        "storage",
        "00c1bf88",
        null,
        "pointer"
      ]
    ],
    [
      "00ba8c10",
      "DATA",
      [
        "storage",
        "00c13940",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba8bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8ba8.md#insn-00ba8bc0) · [`00ba8bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8ba8.md#insn-00ba8bd0)
- 新版 `00ba8c04`（命令位置の公開資料なし） · `00ba8c14`（命令位置の公開資料なし）

~~~diff
- 00ba8bc0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f38:8"]]
- 00ba8bc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba8c04 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f88:8"]]
+ 00ba8c04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba8bc0 bytes 089d47f9
+ 00ba8c04 bytes 08c547f9
- 00ba8bd0 ["INT_ADD", "register:40f0:8", ["const:ba8bd0:8", "const:4:8"]]
- 00ba8bd0 ["CALL", null, ["callee:00be1930:8"]]
+ 00ba8c14 ["INT_ADD", "register:40f0:8", ["const:ba8c14:8", "const:4:8"]]
+ 00ba8c14 ["CALL", null, ["callee:00be1930:8"]]
- 00ba8bd0 bytes 44e30094
+ 00ba8c14 bytes 47e30094
~~~


<a id="compare-1ab39cd714bfd0fafb3659c5d56b632f"></a>

### [`00ba8fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8fec.md) → [`00ba9030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9030.md) _ZNSt6__ndk114collate_bynameIwEC1EPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 0件  · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba905c",
      "incomplete_value": true,
      "site": "00ba905c",
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
      "definition_site": "00ba9018",
      "incomplete_value": true,
      "site": "00ba9018",
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
      "00ba9050",
      "READ",
      [
        "storage",
        "00c1bf40",
        null,
        "pointer"
      ]
    ],
    [
      "00ba905c",
      "DATA",
      [
        "storage",
        "00c13930",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00ba9050",
      "READ",
      [
        "storage",
        "00c1bf90",
        null,
        "pointer"
      ]
    ],
    [
      "00ba905c",
      "DATA",
      [
        "storage",
        "00c13980",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba900c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8fec.md#insn-00ba900c) · [`00ba9024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8fec.md#insn-00ba9024) · [`00ba904c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8fec.md#insn-00ba904c)
- 新版 `00ba9050`（命令位置の公開資料なし） · `00ba9068`（命令位置の公開資料なし） · `00ba9090`（命令位置の公開資料なし）

~~~diff
- 00ba900c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 00ba900c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba9050 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
+ 00ba9050 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba900c bytes 08a147f9
+ 00ba9050 bytes 08c947f9
- 00ba9024 ["INT_ADD", "register:40f0:8", ["const:ba9024:8", "const:4:8"]]
- 00ba9024 ["CALL", null, ["callee:00be1570:8"]]
+ 00ba9068 ["INT_ADD", "register:40f0:8", ["const:ba9068:8", "const:4:8"]]
+ 00ba9068 ["CALL", null, ["callee:00be1570:8"]]
- 00ba9024 bytes 3fe10094
+ 00ba9068 bytes 42e10094
- 00ba904c ["INT_ADD", "register:40f0:8", ["const:ba904c:8", "const:4:8"]]
- 00ba904c ["CALL", null, ["callee:0041b298:8"]]
+ 00ba9090 ["INT_ADD", "register:40f0:8", ["const:ba9090:8", "const:4:8"]]
+ 00ba9090 ["CALL", null, ["callee:0041b298:8"]]
- 00ba904c bytes 93c8e197
+ 00ba9090 bytes 82c8e197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac7f9332b09b07f60c76017d45aef2cf"></a>

### [`00ba90c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba90c4.md) → [`00ba9108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9108.md) _ZNSt6__ndk114collate_bynameIwEC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be17f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be17f0.md) · 呼出先 6件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)
- 新版 呼出元 1件 [`00be1840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1840.md) · 呼出先 6件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba9134",
      "incomplete_value": true,
      "site": "00ba9134",
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
      "definition_site": "00ba90f0",
      "incomplete_value": true,
      "site": "00ba90f0",
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
      "00ba9128",
      "READ",
      [
        "storage",
        "00c1bf40",
        null,
        "pointer"
      ]
    ],
    [
      "00ba9134",
      "DATA",
      [
        "storage",
        "00c13930",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00ba9128",
      "READ",
      [
        "storage",
        "00c1bf90",
        null,
        "pointer"
      ]
    ],
    [
      "00ba9134",
      "DATA",
      [
        "storage",
        "00c13980",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba90e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba90c4.md#insn-00ba90e4) · [`00ba910c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba90c4.md#insn-00ba910c) · [`00ba9140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba90c4.md#insn-00ba9140)
- 新版 `00ba9128`（命令位置の公開資料なし） · `00ba9150`（命令位置の公開資料なし） · `00ba9184`（命令位置の公開資料なし）

~~~diff
- 00ba90e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 00ba90e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba9128 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
+ 00ba9128 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba90e4 bytes 08a147f9
+ 00ba9128 bytes 08c947f9
- 00ba910c ["INT_ADD", "register:40f0:8", ["const:ba910c:8", "const:4:8"]]
- 00ba910c ["CALL", null, ["callee:00be1570:8"]]
+ 00ba9150 ["INT_ADD", "register:40f0:8", ["const:ba9150:8", "const:4:8"]]
+ 00ba9150 ["CALL", null, ["callee:00be1570:8"]]
- 00ba910c bytes 05e10094
+ 00ba9150 bytes 08e10094
- 00ba9140 ["INT_ADD", "register:40f0:8", ["const:ba9140:8", "const:4:8"]]
- 00ba9140 ["CALL", null, ["callee:00bdb260:8"]]
+ 00ba9184 ["INT_ADD", "register:40f0:8", ["const:ba9184:8", "const:4:8"]]
+ 00ba9184 ["CALL", null, ["callee:00bdb260:8"]]
- 00ba9140 bytes 34c80094
+ 00ba9184 bytes 37c80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-499d0fcacd22deca7ed4562ac532ad56"></a>

### [`00ba9188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9188.md) → [`00ba91cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba91cc.md) _ZNSt6__ndk114collate_bynameIwED1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1920.md) · 呼出先 2件 [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md)
- 新版 呼出元 1件 [`00be1970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1970.md) · 呼出先 2件 [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba91ec",
      "incomplete_value": true,
      "site": "00ba91f0",
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
      "definition_site": "00ba91a8",
      "incomplete_value": true,
      "site": "00ba91ac",
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
      "00ba91e4",
      "READ",
      [
        "storage",
        "00c1bf40",
        null,
        "pointer"
      ]
    ],
    [
      "00ba91f0",
      "DATA",
      [
        "storage",
        "00c13930",
        null,
        "undefined1[64]"
      ]
    ]
  ],
  "added": [
    [
      "00ba91e4",
      "READ",
      [
        "storage",
        "00c1bf90",
        null,
        "pointer"
      ]
    ],
    [
      "00ba91f0",
      "DATA",
      [
        "storage",
        "00c13980",
        null,
        "undefined1[64]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba91a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9188.md#insn-00ba91a0) · [`00ba91b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9188.md#insn-00ba91b0)
- 新版 `00ba91e4`（命令位置の公開資料なし） · `00ba91f4`（命令位置の公開資料なし）

~~~diff
- 00ba91a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f40:8"]]
- 00ba91a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba91e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f90:8"]]
+ 00ba91e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba91a0 bytes 08a147f9
+ 00ba91e4 bytes 08c947f9
- 00ba91b0 ["INT_ADD", "register:40f0:8", ["const:ba91b0:8", "const:4:8"]]
- 00ba91b0 ["CALL", null, ["callee:00be1930:8"]]
+ 00ba91f4 ["INT_ADD", "register:40f0:8", ["const:ba91f4:8", "const:4:8"]]
+ 00ba91f4 ["CALL", null, ["callee:00be1930:8"]]
- 00ba91b0 bytes cce10094
+ 00ba91f4 bytes cfe10094
~~~


<a id="compare-e21a386c79d2077317609da90b8b620e"></a>

### [`00ba9788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9788.md) → [`00ba97cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba97cc.md) _ZNKSt6__ndk15ctypeIwE10do_toupperEw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md) [`00be1960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1960.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md) [`00be19b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 78.38% / 新版 78.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba984c",
      "incomplete_value": true,
      "site": "00ba984c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9808",
      "incomplete_value": true,
      "site": "00ba9808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "definition_site": "00ba97fc",
      "incomplete_value": true,
      "site": "00ba9804",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba97b8",
      "incomplete_value": true,
      "site": "00ba97c0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
              ]
            ]
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
      "definition_site": "00ba982c",
      "incomplete_value": false,
      "site": "00ba9830",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba97e8",
      "incomplete_value": false,
      "site": "00ba97ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "00ba97f4",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba97fc",
      "READ",
      [
        "storage",
        "010a2950",
        null,
        "undefined8"
      ]
    ],
    [
      "00ba982c",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ba97f4",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba97fc",
      "READ",
      [
        "storage",
        "010a2990",
        null,
        "undefined8"
      ]
    ],
    [
      "00ba982c",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba97a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9788.md#insn-00ba97a8) · [`00ba97c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9788.md#insn-00ba97c0) · [`00ba97ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9788.md#insn-00ba97ec)
- 新版 `00ba97ec`（命令位置の公開資料なし） · `00ba9804`（命令位置の公開資料なし） · `00ba9830`（命令位置の公開資料なし）

~~~diff
- 00ba97a8 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00ba97a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ba97a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ba97a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ba97ec ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00ba97ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ba97ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ba97ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ba97a8 bytes 08612591
+ 00ba97ec bytes 08612691
- 00ba97c0 ["INT_ADD", "register:40f0:8", ["const:ba97c0:8", "const:4:8"]]
- 00ba97c0 ["CALL", null, ["callee:00be19b0:8"]]
+ 00ba9804 ["INT_ADD", "register:40f0:8", ["const:ba9804:8", "const:4:8"]]
+ 00ba9804 ["CALL", null, ["callee:00be19b0:8"]]
- 00ba97c0 bytes 68e00094
+ 00ba9804 bytes 6be00094
- 00ba97ec ["INT_ADD", "register:40f0:8", ["const:ba97ec:8", "const:4:8"]]
- 00ba97ec ["CALL", null, ["callee:00bdb000:8"]]
+ 00ba9830 ["INT_ADD", "register:40f0:8", ["const:ba9830:8", "const:4:8"]]
+ 00ba9830 ["CALL", null, ["callee:00bdb000:8"]]
- 00ba97ec bytes f1c50094
+ 00ba9830 bytes f4c50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4ec8e6fe654a81e38c4647697f419752"></a>

### [`00ba9834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9834.md) → [`00ba9878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9878.md) _ZNKSt6__ndk15ctypeIwE10do_toupperEPwPKw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba9904",
      "incomplete_value": true,
      "site": "00ba9904",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba98c0",
      "incomplete_value": true,
      "site": "00ba98c0",
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
            "const:950:8"
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
      "00ba98dc",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba98e4",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba98f0",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba98dc",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba98e4",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba98f0",
      "PARAM",
      [
        "storage",
        "002a570e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba98c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9834.md#insn-00ba98c0) · [`00ba9860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9834.md#insn-00ba9860) · [`00ba98a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9834.md#insn-00ba98a4)
- 新版 `00ba9904`（命令位置の公開資料なし） · `00ba98a4`（命令位置の公開資料なし） · `00ba98e8`（命令位置の公開資料なし）

~~~diff
- 00ba98c0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:950:8"]]
- 00ba98c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ba9904 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:990:8"]]
+ 00ba9904 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ba98c0 bytes c0aa04f9
+ 00ba9904 bytes c0ca04f9
- 00ba9860 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00ba9860 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00ba9860 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00ba9860 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00ba98a4 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00ba98a4 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00ba98a4 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00ba98a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00ba9860 bytes b5622591
+ 00ba98a4 bytes b5622691
- 00ba98a4 ["INT_ADD", "register:40f0:8", ["const:ba98a4:8", "const:4:8"]]
- 00ba98a4 ["CALL", null, ["callee:00bdb000:8"]]
+ 00ba98e8 ["INT_ADD", "register:40f0:8", ["const:ba98e8:8", "const:4:8"]]
+ 00ba98e8 ["CALL", null, ["callee:00bdb000:8"]]
- 00ba98a4 bytes c3c50094
+ 00ba98e8 bytes c6c50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84b1efa542edc78325b6dda0d6fe11ff"></a>

### [`00ba9908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9908.md) → [`00ba994c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba994c.md) _ZNKSt6__ndk15ctypeIwE10do_tolowerEw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba99c4",
      "incomplete_value": false,
      "site": "00ba99c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9980",
      "incomplete_value": false,
      "site": "00ba9980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "definition_site": "00ba99a0",
      "incomplete_value": false,
      "site": "00ba99a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba995c",
      "incomplete_value": false,
      "site": "00ba9960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "definition_site": "00ba99b0",
      "incomplete_value": false,
      "site": "00ba99bc",
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
            "const:70e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba996c",
      "incomplete_value": false,
      "site": "00ba9978",
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
            "const:683:8"
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
      "00ba9970",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba99a0",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba99b0",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba9970",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba99a0",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba99b0",
      "PARAM",
      [
        "storage",
        "002a570e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9908.md#insn-00ba9960) · [`00ba9978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9908.md#insn-00ba9978) · [`00ba9980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9908.md#insn-00ba9980)
- 新版 `00ba99a4`（命令位置の公開資料なし） · `00ba99bc`（命令位置の公開資料なし） · `00ba99c4`（命令位置の公開資料なし）

~~~diff
- 00ba9960 ["INT_ADD", "register:40f0:8", ["const:ba9960:8", "const:4:8"]]
- 00ba9960 ["CALL", null, ["callee:00bdb000:8"]]
+ 00ba99a4 ["INT_ADD", "register:40f0:8", ["const:ba99a4:8", "const:4:8"]]
+ 00ba99a4 ["CALL", null, ["callee:00bdb000:8"]]
- 00ba9960 bytes 94c50094
+ 00ba99a4 bytes 97c50094
- 00ba9978 ["INT_ADD", "register:40f0:8", ["const:ba9978:8", "const:4:8"]]
- 00ba9978 ["CALL", null, ["callee:00be1570:8"]]
+ 00ba99bc ["INT_ADD", "register:40f0:8", ["const:ba99bc:8", "const:4:8"]]
+ 00ba99bc ["CALL", null, ["callee:00be1570:8"]]
- 00ba9978 bytes eade0094
+ 00ba99bc bytes edde0094
- 00ba9980 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
- 00ba9980 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ba99c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:990:8"]]
+ 00ba99c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ba9980 bytes 00a904f9
+ 00ba99c4 bytes 00c904f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d41b1cd58c09f6ac844a0621b292046"></a>

### [`00ba99ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba99ac.md) → [`00ba99f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba99f0.md) _ZNKSt6__ndk15ctypeIwE10do_tolowerEPwPKw

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba9a7c",
      "incomplete_value": true,
      "site": "00ba9a7c",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9a38",
      "incomplete_value": true,
      "site": "00ba9a38",
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
            "const:950:8"
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
      "00ba9a54",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9a5c",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9a68",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba9a54",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9a5c",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9a68",
      "PARAM",
      [
        "storage",
        "002a570e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba99ac.md#insn-00ba9a38) · [`00ba99d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba99ac.md#insn-00ba99d8) · [`00ba9a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba99ac.md#insn-00ba9a1c)
- 新版 `00ba9a7c`（命令位置の公開資料なし） · `00ba9a1c`（命令位置の公開資料なし） · `00ba9a60`（命令位置の公開資料なし）

~~~diff
- 00ba9a38 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:950:8"]]
- 00ba9a38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ba9a7c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:990:8"]]
+ 00ba9a7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ba9a38 bytes c0aa04f9
+ 00ba9a7c bytes c0ca04f9
- 00ba99d8 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00ba99d8 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00ba99d8 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00ba99d8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00ba9a1c ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00ba9a1c ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00ba9a1c ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00ba9a1c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00ba99d8 bytes b5622591
+ 00ba9a1c bytes b5622691
- 00ba9a1c ["INT_ADD", "register:40f0:8", ["const:ba9a1c:8", "const:4:8"]]
- 00ba9a1c ["CALL", null, ["callee:00bdb000:8"]]
+ 00ba9a60 ["INT_ADD", "register:40f0:8", ["const:ba9a60:8", "const:4:8"]]
+ 00ba9a60 ["CALL", null, ["callee:00bdb000:8"]]
- 00ba9a1c bytes 65c50094
+ 00ba9a60 bytes 68c50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd1761016e662d707a485f4874fbbd06"></a>

### [`00ba9d54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9d54.md) → [`00ba9d98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9d98.md) _ZNSt6__ndk15ctypeIcEC1EPKmbm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be17a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be17a0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be17f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be17f0.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ba9db0",
      "incomplete_value": true,
      "site": "00ba9db4",
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
      "definition_site": "00ba9d6c",
      "incomplete_value": true,
      "site": "00ba9d70",
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
      "00ba9da4",
      "READ",
      [
        "storage",
        "00c1bf48",
        null,
        "pointer"
      ]
    ],
    [
      "00ba9db4",
      "DATA",
      [
        "storage",
        "00c13970",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00ba9da4",
      "READ",
      [
        "storage",
        "00c1bf98",
        null,
        "pointer"
      ]
    ],
    [
      "00ba9db4",
      "DATA",
      [
        "storage",
        "00c139c0",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9d54.md#insn-00ba9d60)
- 新版 `00ba9da4`（命令位置の公開資料なし）

~~~diff
- 00ba9d60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
- 00ba9d60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ba9da4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f98:8"]]
+ 00ba9da4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ba9d60 bytes 08a547f9
+ 00ba9da4 bytes 08cd47f9
~~~


<a id="compare-9cd577608447d3a0fd035ac243e98959"></a>

### [`00ba9e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9e0c.md) → [`00ba9e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9e50.md) _ZNKSt6__ndk15ctypeIcE10do_toupperEc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba9ec8",
      "incomplete_value": false,
      "site": "00ba9ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9e84",
      "incomplete_value": false,
      "site": "00ba9e84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "definition_site": "00ba9ea4",
      "incomplete_value": false,
      "site": "00ba9ea8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9e60",
      "incomplete_value": false,
      "site": "00ba9e64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "definition_site": "00ba9eb4",
      "incomplete_value": false,
      "site": "00ba9ec0",
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
            "const:70e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9e70",
      "incomplete_value": false,
      "site": "00ba9e7c",
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
            "const:683:8"
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
      "00ba9e70",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9ea4",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9eb4",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba9e70",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9ea4",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9eb4",
      "PARAM",
      [
        "storage",
        "002a570e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9e0c.md#insn-00ba9e64) · [`00ba9e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9e0c.md#insn-00ba9e7c) · [`00ba9e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9e0c.md#insn-00ba9e84)
- 新版 `00ba9ea8`（命令位置の公開資料なし） · `00ba9ec0`（命令位置の公開資料なし） · `00ba9ec8`（命令位置の公開資料なし）

~~~diff
- 00ba9e64 ["INT_ADD", "register:40f0:8", ["const:ba9e64:8", "const:4:8"]]
- 00ba9e64 ["CALL", null, ["callee:00bdb000:8"]]
+ 00ba9ea8 ["INT_ADD", "register:40f0:8", ["const:ba9ea8:8", "const:4:8"]]
+ 00ba9ea8 ["CALL", null, ["callee:00bdb000:8"]]
- 00ba9e64 bytes 53c40094
+ 00ba9ea8 bytes 56c40094
- 00ba9e7c ["INT_ADD", "register:40f0:8", ["const:ba9e7c:8", "const:4:8"]]
- 00ba9e7c ["CALL", null, ["callee:00be1570:8"]]
+ 00ba9ec0 ["INT_ADD", "register:40f0:8", ["const:ba9ec0:8", "const:4:8"]]
+ 00ba9ec0 ["CALL", null, ["callee:00be1570:8"]]
- 00ba9e7c bytes a9dd0094
+ 00ba9ec0 bytes acdd0094
- 00ba9e84 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
- 00ba9e84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ba9ec8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:990:8"]]
+ 00ba9ec8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ba9e84 bytes 00a904f9
+ 00ba9ec8 bytes 00c904f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7caa3957ed2b4e84bc32d5b03c2f2085"></a>

### [`00ba9eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9eb0.md) → [`00ba9ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9ef4.md) _ZNKSt6__ndk15ctypeIcE10do_toupperEPcPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ba9f80",
      "incomplete_value": true,
      "site": "00ba9f80",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9f3c",
      "incomplete_value": true,
      "site": "00ba9f3c",
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
            "const:950:8"
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
      "00ba9f58",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9f60",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9f6c",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba9f58",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9f60",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00ba9f6c",
      "PARAM",
      [
        "storage",
        "002a570e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9eb0.md#insn-00ba9f3c) · [`00ba9edc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9eb0.md#insn-00ba9edc) · [`00ba9f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9eb0.md#insn-00ba9f20)
- 新版 `00ba9f80`（命令位置の公開資料なし） · `00ba9f20`（命令位置の公開資料なし） · `00ba9f64`（命令位置の公開資料なし）

~~~diff
- 00ba9f3c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:950:8"]]
- 00ba9f3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ba9f80 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:990:8"]]
+ 00ba9f80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ba9f3c bytes c0aa04f9
+ 00ba9f80 bytes c0ca04f9
- 00ba9edc ["COPY", "tmp:0:8", ["const:958:8"]]
- 00ba9edc ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00ba9edc ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00ba9edc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00ba9f20 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00ba9f20 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00ba9f20 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00ba9f20 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00ba9edc bytes b5622591
+ 00ba9f20 bytes b5622691
- 00ba9f20 ["INT_ADD", "register:40f0:8", ["const:ba9f20:8", "const:4:8"]]
- 00ba9f20 ["CALL", null, ["callee:00bdb000:8"]]
+ 00ba9f64 ["INT_ADD", "register:40f0:8", ["const:ba9f64:8", "const:4:8"]]
+ 00ba9f64 ["CALL", null, ["callee:00bdb000:8"]]
- 00ba9f20 bytes 24c40094
+ 00ba9f64 bytes 27c40094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edc8eafe632214589ec6333152821b2c"></a>

### [`00ba9f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9f84.md) → [`00ba9fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba9/00ba9fc8.md) _ZNKSt6__ndk15ctypeIcE10do_tolowerEc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00baa040",
      "incomplete_value": false,
      "site": "00baa040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9ffc",
      "incomplete_value": false,
      "site": "00ba9ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "definition_site": "00baa01c",
      "incomplete_value": false,
      "site": "00baa020",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:998:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9fd8",
      "incomplete_value": false,
      "site": "00ba9fdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:958:8"
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
      "definition_site": "00baa02c",
      "incomplete_value": false,
      "site": "00baa038",
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
            "const:70e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ba9fe8",
      "incomplete_value": false,
      "site": "00ba9ff4",
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
            "const:683:8"
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
      "00ba9fe8",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00baa01c",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00baa02c",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ba9fe8",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00baa01c",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00baa02c",
      "PARAM",
      [
        "storage",
        "002a570e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ba9fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9f84.md#insn-00ba9fdc) · [`00ba9ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9f84.md#insn-00ba9ff4) · [`00ba9ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba9/00ba9f84.md#insn-00ba9ffc)
- 新版 `00baa020`（命令位置の公開資料なし） · `00baa038`（命令位置の公開資料なし） · `00baa040`（命令位置の公開資料なし）

~~~diff
- 00ba9fdc ["INT_ADD", "register:40f0:8", ["const:ba9fdc:8", "const:4:8"]]
- 00ba9fdc ["CALL", null, ["callee:00bdb000:8"]]
+ 00baa020 ["INT_ADD", "register:40f0:8", ["const:baa020:8", "const:4:8"]]
+ 00baa020 ["CALL", null, ["callee:00bdb000:8"]]
- 00ba9fdc bytes f5c30094
+ 00baa020 bytes f8c30094
- 00ba9ff4 ["INT_ADD", "register:40f0:8", ["const:ba9ff4:8", "const:4:8"]]
- 00ba9ff4 ["CALL", null, ["callee:00be1570:8"]]
+ 00baa038 ["INT_ADD", "register:40f0:8", ["const:baa038:8", "const:4:8"]]
+ 00baa038 ["CALL", null, ["callee:00be1570:8"]]
- 00ba9ff4 bytes 4bdd0094
+ 00baa038 bytes 4edd0094
- 00ba9ffc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:950:8"]]
- 00ba9ffc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00baa040 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:990:8"]]
+ 00baa040 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ba9ffc bytes 00a904f9
+ 00baa040 bytes 00c904f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-382081ae9a5a185ec3c7d3071487d1f4"></a>

### [`00baa028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa028.md) → [`00baa06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa06c.md) _ZNKSt6__ndk15ctypeIcE10do_tolowerEPcPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00baa0f8",
      "incomplete_value": true,
      "site": "00baa0f8",
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
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baa0b4",
      "incomplete_value": true,
      "site": "00baa0b4",
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
            "const:950:8"
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
      "00baa0d0",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00baa0d8",
      "PARAM",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ],
    [
      "00baa0e4",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00baa0d0",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00baa0d8",
      "PARAM",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ],
    [
      "00baa0e4",
      "PARAM",
      [
        "storage",
        "002a570e",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baa0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa028.md#insn-00baa0b4) · [`00baa054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa028.md#insn-00baa054) · [`00baa098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa028.md#insn-00baa098)
- 新版 `00baa0f8`（命令位置の公開資料なし） · `00baa098`（命令位置の公開資料なし） · `00baa0dc`（命令位置の公開資料なし）

~~~diff
- 00baa0b4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:950:8"]]
- 00baa0b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00baa0f8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:990:8"]]
+ 00baa0f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00baa0b4 bytes c0aa04f9
+ 00baa0f8 bytes c0ca04f9
- 00baa054 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00baa054 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
- 00baa054 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
- 00baa054 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
+ 00baa098 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00baa098 ["INT_CARRY", "register:105:1", ["register:40a8:8", "tmp:0:8"]]
+ 00baa098 ["INT_SCARRY", "register:106:1", ["register:40a8:8", "tmp:0:8"]]
+ 00baa098 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "tmp:0:8"]]
- 00baa054 bytes b5622591
+ 00baa098 bytes b5622691
- 00baa098 ["INT_ADD", "register:40f0:8", ["const:baa098:8", "const:4:8"]]
- 00baa098 ["CALL", null, ["callee:00bdb000:8"]]
+ 00baa0dc ["INT_ADD", "register:40f0:8", ["const:baa0dc:8", "const:4:8"]]
+ 00baa0dc ["CALL", null, ["callee:00bdb000:8"]]
- 00baa098 bytes c6c30094
+ 00baa0dc bytes c9c30094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bbdef3373cad6037198957b4ed0c28e0"></a>

### [`00baa2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa2e4.md) → [`00baa328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa328.md) _ZNSt6__ndk112ctype_bynameIcEC1EPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1990.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)
- 新版 呼出元 1件 [`00be19e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19e0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.73% / 新版 92.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00baa35c",
      "incomplete_value": true,
      "site": "00baa364",
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
      "definition_site": "00baa318",
      "incomplete_value": true,
      "site": "00baa320",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00baa3a0",
      "incomplete_value": false,
      "site": "00baa3b0",
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
            "const:173:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baa35c",
      "incomplete_value": false,
      "site": "00baa36c",
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
            "const:e8:8"
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
      "00baa348",
      "READ",
      [
        "storage",
        "00c1bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00baa364",
      "DATA",
      [
        "storage",
        "00c139d8",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00baa3a0",
      "PARAM",
      [
        "storage",
        "002a40e8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00baa348",
      "READ",
      [
        "storage",
        "00c1bfa0",
        null,
        "pointer"
      ]
    ],
    [
      "00baa364",
      "DATA",
      [
        "storage",
        "00c13a28",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00baa3a0",
      "PARAM",
      [
        "storage",
        "002a4173",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baa36c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa2e4.md#insn-00baa36c) · [`00baa304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa2e4.md#insn-00baa304) · [`00baa32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa2e4.md#insn-00baa32c)
- 新版 `00baa3b0`（命令位置の公開資料なし） · `00baa348`（命令位置の公開資料なし） · `00baa370`（命令位置の公開資料なし）

~~~diff
- 00baa36c ["INT_ADD", "register:40f0:8", ["const:baa36c:8", "const:4:8"]]
- 00baa36c ["CALL", null, ["callee:00ba8ac4:8"]]
+ 00baa3b0 ["INT_ADD", "register:40f0:8", ["const:baa3b0:8", "const:4:8"]]
+ 00baa3b0 ["CALL", null, ["callee:00ba8ac4:8"]]
- 00baa36c bytes c5f9ff97
+ 00baa3b0 bytes c5f9ff97
- 00baa304 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f50:8"]]
- 00baa304 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baa348 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fa0:8"]]
+ 00baa348 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00baa304 bytes 29a947f9
+ 00baa348 bytes 29d147f9
- 00baa32c ["INT_ADD", "register:40f0:8", ["const:baa32c:8", "const:4:8"]]
- 00baa32c ["CALL", null, ["callee:00be1570:8"]]
+ 00baa370 ["INT_ADD", "register:40f0:8", ["const:baa370:8", "const:4:8"]]
+ 00baa370 ["CALL", null, ["callee:00be1570:8"]]
- 00baa32c bytes 7ddc0094
+ 00baa370 bytes 80dc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a11d2ee0188c78f42e130e67a98b144"></a>

### [`00baa3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa3cc.md) → [`00baa410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa410.md) _ZNSt6__ndk112ctype_bynameIcEC1ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00be1800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1800.md) [`00be19a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19a0.md) · 呼出先 6件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)
- 新版 呼出元 2件 [`00be1850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1850.md) [`00be19f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19f0.md) · 呼出先 6件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00baa44c",
      "incomplete_value": true,
      "site": "00baa44c",
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
      "definition_site": "00baa408",
      "incomplete_value": true,
      "site": "00baa408",
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
      "definition_site": "00baa48c",
      "incomplete_value": false,
      "site": "00baa49c",
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
            "const:173:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baa448",
      "incomplete_value": false,
      "site": "00baa458",
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
            "const:e8:8"
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
      "00baa43c",
      "READ",
      [
        "storage",
        "00c1bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00baa44c",
      "DATA",
      [
        "storage",
        "00c139d8",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00baa48c",
      "PARAM",
      [
        "storage",
        "002a40e8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00baa43c",
      "READ",
      [
        "storage",
        "00c1bfa0",
        null,
        "pointer"
      ]
    ],
    [
      "00baa44c",
      "DATA",
      [
        "storage",
        "00c13a28",
        null,
        "undefined1[104]"
      ]
    ],
    [
      "00baa48c",
      "PARAM",
      [
        "storage",
        "002a4173",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baa458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa3cc.md#insn-00baa458) · [`00baa49c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa3cc.md#insn-00baa49c) · [`00baa3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa3cc.md#insn-00baa3f8)
- 新版 `00baa49c`（命令位置の公開資料なし） · `00baa4e0`（命令位置の公開資料なし） · `00baa43c`（命令位置の公開資料なし）

~~~diff
- 00baa458 ["INT_ADD", "register:40f0:8", ["const:baa458:8", "const:4:8"]]
- 00baa458 ["CALL", null, ["callee:00bdb260:8"]]
+ 00baa49c ["INT_ADD", "register:40f0:8", ["const:baa49c:8", "const:4:8"]]
+ 00baa49c ["CALL", null, ["callee:00bdb260:8"]]
- 00baa458 bytes 6ec30094
+ 00baa49c bytes 71c30094
- 00baa49c ["INT_ADD", "register:40f0:8", ["const:baa49c:8", "const:4:8"]]
- 00baa49c ["CALL", null, ["callee:00bd70ec:8"]]
+ 00baa4e0 ["INT_ADD", "register:40f0:8", ["const:baa4e0:8", "const:4:8"]]
+ 00baa4e0 ["CALL", null, ["callee:00bd70ec:8"]]
- 00baa49c bytes 04b30094
+ 00baa4e0 bytes 03b30094
- 00baa3f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f50:8"]]
- 00baa3f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baa43c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa0:8"]]
+ 00baa43c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00baa3f8 bytes 08a947f9
+ 00baa43c bytes 08d147f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-55f5791d5f7a42a5ed0e3d4a30e5e361"></a>

### [`00baa85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa85c.md) → [`00baa8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa8a0.md) _ZNSt6__ndk112ctype_bynameIwEC2EPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be19c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19c0.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)
- 新版 呼出元 1件 [`00be1a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a10.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00baa8cc",
      "incomplete_value": true,
      "site": "00baa8cc",
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
      "definition_site": "00baa888",
      "incomplete_value": true,
      "site": "00baa888",
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
      "00baa8c0",
      "READ",
      [
        "storage",
        "00c1bf58",
        null,
        "pointer"
      ]
    ],
    [
      "00baa8cc",
      "DATA",
      [
        "storage",
        "00c13a40",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00baa8c0",
      "READ",
      [
        "storage",
        "00c1bfa8",
        null,
        "pointer"
      ]
    ],
    [
      "00baa8cc",
      "DATA",
      [
        "storage",
        "00c13a90",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baa87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa85c.md#insn-00baa87c) · [`00baa894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa85c.md#insn-00baa894) · [`00baa8bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa85c.md#insn-00baa8bc)
- 新版 `00baa8c0`（命令位置の公開資料なし） · `00baa8d8`（命令位置の公開資料なし） · `00baa900`（命令位置の公開資料なし）

~~~diff
- 00baa87c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f58:8"]]
- 00baa87c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baa8c0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa8:8"]]
+ 00baa8c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00baa87c bytes 08ad47f9
+ 00baa8c0 bytes 08d547f9
- 00baa894 ["INT_ADD", "register:40f0:8", ["const:baa894:8", "const:4:8"]]
- 00baa894 ["CALL", null, ["callee:00be1570:8"]]
+ 00baa8d8 ["INT_ADD", "register:40f0:8", ["const:baa8d8:8", "const:4:8"]]
+ 00baa8d8 ["CALL", null, ["callee:00be1570:8"]]
- 00baa894 bytes 23db0094
+ 00baa8d8 bytes 26db0094
- 00baa8bc ["INT_ADD", "register:40f0:8", ["const:baa8bc:8", "const:4:8"]]
- 00baa8bc ["CALL", null, ["callee:0041b298:8"]]
+ 00baa900 ["INT_ADD", "register:40f0:8", ["const:baa900:8", "const:4:8"]]
+ 00baa900 ["CALL", null, ["callee:0041b298:8"]]
- 00baa8bc bytes 77c2e197
+ 00baa900 bytes 66c2e197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98bad9c7ff21abf89a44376035467089"></a>

### [`00baa934`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa934.md) → [`00baa978`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baa/00baa978.md) _ZNSt6__ndk112ctype_bynameIwEC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00be1810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1810.md) [`00be19e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be19e0.md) · 呼出先 6件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)
- 新版 呼出元 2件 [`00be1860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1860.md) [`00be1a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1a30.md) · 呼出先 6件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00baa9a4",
      "incomplete_value": true,
      "site": "00baa9a4",
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
      "definition_site": "00baa960",
      "incomplete_value": true,
      "site": "00baa960",
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
      "00baa998",
      "READ",
      [
        "storage",
        "00c1bf58",
        null,
        "pointer"
      ]
    ],
    [
      "00baa9a4",
      "DATA",
      [
        "storage",
        "00c13a40",
        null,
        "undefined1[136]"
      ]
    ]
  ],
  "added": [
    [
      "00baa998",
      "READ",
      [
        "storage",
        "00c1bfa8",
        null,
        "pointer"
      ]
    ],
    [
      "00baa9a4",
      "DATA",
      [
        "storage",
        "00c13a90",
        null,
        "undefined1[136]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baa954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa934.md#insn-00baa954) · [`00baa97c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa934.md#insn-00baa97c) · [`00baa9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baa/00baa934.md#insn-00baa9b0)
- 新版 `00baa998`（命令位置の公開資料なし） · `00baa9c0`（命令位置の公開資料なし） · `00baa9f4`（命令位置の公開資料なし）

~~~diff
- 00baa954 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f58:8"]]
- 00baa954 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baa998 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fa8:8"]]
+ 00baa998 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00baa954 bytes 08ad47f9
+ 00baa998 bytes 08d547f9
- 00baa97c ["INT_ADD", "register:40f0:8", ["const:baa97c:8", "const:4:8"]]
- 00baa97c ["CALL", null, ["callee:00be1570:8"]]
+ 00baa9c0 ["INT_ADD", "register:40f0:8", ["const:baa9c0:8", "const:4:8"]]
+ 00baa9c0 ["CALL", null, ["callee:00be1570:8"]]
- 00baa97c bytes e9da0094
+ 00baa9c0 bytes ecda0094
- 00baa9b0 ["INT_ADD", "register:40f0:8", ["const:baa9b0:8", "const:4:8"]]
- 00baa9b0 ["CALL", null, ["callee:00bdb260:8"]]
+ 00baa9f4 ["INT_ADD", "register:40f0:8", ["const:baa9f4:8", "const:4:8"]]
+ 00baa9f4 ["CALL", null, ["callee:00bdb260:8"]]
- 00baa9b0 bytes 18c20094
+ 00baa9f4 bytes 1bc20094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0cde60b17a4c4f2453160f17fcdd806"></a>

### [`00bab34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab34c.md) → [`00bab390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab390.md) _ZNSt6__ndk17codecvtIwc9mbstate_tEC1Em

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00bdd9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9d0.md) [`00be17b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be17b0.md) · 呼出先 3件 [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md) [`00be1520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1520.md)
- 新版 呼出元 2件 [`00bdda20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda20.md) [`00be1800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1800.md) · 呼出先 3件 [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md) [`00be1570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1570.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 62.86% / 新版 62.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bab3b8",
      "incomplete_value": true,
      "site": "00bab3b8",
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
      "definition_site": "00bab374",
      "incomplete_value": true,
      "site": "00bab374",
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
      "definition_site": "00bab3cc",
      "incomplete_value": true,
      "site": "00bab3d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:990:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bab388",
      "incomplete_value": true,
      "site": "00bab38c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:950:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00bab408",
      "incomplete_value": true,
      "site": "00bab408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bab3c4",
      "incomplete_value": true,
      "site": "00bab3c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:950:8"
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
      "00bab3ac",
      "READ",
      [
        "storage",
        "00c1bf60",
        null,
        "pointer"
      ]
    ],
    [
      "00bab3b8",
      "DATA",
      [
        "storage",
        "00c13ac8",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00bab3c4",
      "READ",
      [
        "storage",
        "010a2958",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bab3ac",
      "READ",
      [
        "storage",
        "00c1bfb0",
        null,
        "pointer"
      ]
    ],
    [
      "00bab3b8",
      "DATA",
      [
        "storage",
        "00c13b18",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00bab3c4",
      "READ",
      [
        "storage",
        "010a2998",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bab37c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab34c.md#insn-00bab37c) · [`00bab3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab34c.md#insn-00bab3a8) · [`00bab3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab34c.md#insn-00bab3c0)
- 新版 `00bab3c0`（命令位置の公開資料なし） · `00bab3ec`（命令位置の公開資料なし） · `00bab404`（命令位置の公開資料なし）

~~~diff
- 00bab37c ["COPY", "tmp:0:8", ["const:958:8"]]
- 00bab37c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bab37c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bab37c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bab3c0 ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00bab3c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bab3c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bab3c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bab37c bytes 08612591
+ 00bab3c0 bytes 08612691
- 00bab3a8 ["INT_ADD", "register:40f0:8", ["const:bab3a8:8", "const:4:8"]]
- 00bab3a8 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bab3ec ["INT_ADD", "register:40f0:8", ["const:bab3ec:8", "const:4:8"]]
+ 00bab3ec ["CALL", null, ["callee:00bdb000:8"]]
- 00bab3a8 bytes 02bf0094
+ 00bab3ec bytes 05bf0094
- 00bab3c0 ["INT_ADD", "register:40f0:8", ["const:bab3c0:8", "const:4:8"]]
- 00bab3c0 ["CALL", null, ["callee:00be1570:8"]]
+ 00bab404 ["INT_ADD", "register:40f0:8", ["const:bab404:8", "const:4:8"]]
+ 00bab404 ["CALL", null, ["callee:00be1570:8"]]
- 00bab3c0 bytes 58d80094
+ 00bab404 bytes 5bd80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0985be0179a7401ae3809f5bd8841e6f"></a>

### [`00bab3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab3f8.md) → [`00bab43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bab/00bab43c.md) _ZNSt6__ndk17codecvtIwc9mbstate_tEC2EPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1820.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md)
- 新版 呼出元 1件 [`00be1870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1870.md) · 呼出先 7件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.16% / 新版 92.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bab468",
      "incomplete_value": true,
      "site": "00bab468",
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
      "definition_site": "00bab424",
      "incomplete_value": true,
      "site": "00bab424",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bab4a4",
      "incomplete_value": false,
      "site": "00bab4b4",
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
            "const:265:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bab460",
      "incomplete_value": false,
      "site": "00bab470",
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
            "const:267:8"
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
      "00bab45c",
      "READ",
      [
        "storage",
        "00c1bf60",
        null,
        "pointer"
      ]
    ],
    [
      "00bab468",
      "DATA",
      [
        "storage",
        "00c13ac8",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00bab4a4",
      "PARAM",
      [
        "storage",
        "0029c267",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bab45c",
      "READ",
      [
        "storage",
        "00c1bfb0",
        null,
        "pointer"
      ]
    ],
    [
      "00bab468",
      "DATA",
      [
        "storage",
        "00c13b18",
        null,
        "undefined1[96]"
      ]
    ],
    [
      "00bab4a4",
      "PARAM",
      [
        "storage",
        "0029c265",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bab470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab3f8.md#insn-00bab470) · [`00bab418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab3f8.md#insn-00bab418) · [`00bab430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00bab3f8.md#insn-00bab430)
- 新版 `00bab4b4`（命令位置の公開資料なし） · `00bab45c`（命令位置の公開資料なし） · `00bab474`（命令位置の公開資料なし）

~~~diff
- 00bab470 ["INT_ADD", "register:40f0:8", ["const:bab470:8", "const:4:8"]]
- 00bab470 ["CALL", null, ["callee:00ba8ac4:8"]]
+ 00bab4b4 ["INT_ADD", "register:40f0:8", ["const:bab4b4:8", "const:4:8"]]
+ 00bab4b4 ["CALL", null, ["callee:00ba8ac4:8"]]
- 00bab470 bytes 84f5ff97
+ 00bab4b4 bytes 84f5ff97
- 00bab418 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f60:8"]]
- 00bab418 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00bab45c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fb0:8"]]
+ 00bab45c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00bab418 bytes 08b147f9
+ 00bab45c bytes 08d947f9
- 00bab430 ["INT_ADD", "register:40f0:8", ["const:bab430:8", "const:4:8"]]
- 00bab430 ["CALL", null, ["callee:00be1570:8"]]
+ 00bab474 ["INT_ADD", "register:40f0:8", ["const:bab474:8", "const:4:8"]]
+ 00bab474 ["CALL", null, ["callee:00be1570:8"]]
- 00bab430 bytes 3cd80094
+ 00bab474 bytes 3fd80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3101185221a776be419fa4e7c59febb"></a>

### [`00baefb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baefb8.md) → [`00baeffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bae/00baeffc.md) _ZNSt6__ndk18numpunctIcEC2Em

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be17c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be17c0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be1810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1810.md) · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.73% / 新版 72.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00baf020",
      "incomplete_value": true,
      "site": "00baf020",
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
      "definition_site": "00baefdc",
      "incomplete_value": true,
      "site": "00baefdc",
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
      "00baf008",
      "READ",
      [
        "storage",
        "00c1bf68",
        null,
        "pointer"
      ]
    ],
    [
      "00baf020",
      "DATA",
      [
        "storage",
        "00c13b28",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00baf008",
      "READ",
      [
        "storage",
        "00c1bfb8",
        null,
        "pointer"
      ]
    ],
    [
      "00baf020",
      "DATA",
      [
        "storage",
        "00c13b78",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baefc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baefb8.md#insn-00baefc4)
- 新版 `00baf008`（命令位置の公開資料なし）

~~~diff
- 00baefc4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f68:8"]]
- 00baefc4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baf008 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fb8:8"]]
+ 00baf008 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00baefc4 bytes 29b547f9
+ 00baf008 bytes 29dd47f9
~~~


<a id="compare-a34e262436695063f9535ac47354a5b8"></a>

### [`00baefe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baefe4.md) → [`00baf028`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf028.md) _ZNSt6__ndk18numpunctIwEC2Em

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be17d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be17d0.md) · 呼出先 0件 
- 新版 呼出元 1件 [`00be1820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1820.md) · 呼出先 0件 

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
      "definition_site": "00baf050",
      "incomplete_value": true,
      "site": "00baf050",
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
      "definition_site": "00baf00c",
      "incomplete_value": true,
      "site": "00baf00c",
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
      "00baf038",
      "READ",
      [
        "storage",
        "00c1bf70",
        null,
        "pointer"
      ]
    ],
    [
      "00baf050",
      "DATA",
      [
        "storage",
        "00c13b78",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00baf038",
      "READ",
      [
        "storage",
        "00c1bfc0",
        null,
        "pointer"
      ]
    ],
    [
      "00baf050",
      "DATA",
      [
        "storage",
        "00c13bc8",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baeff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baefe4.md#insn-00baeff4)
- 新版 `00baf038`（命令位置の公開資料なし）

~~~diff
- 00baeff4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f70:8"]]
- 00baeff4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baf038 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:fc0:8"]]
+ 00baf038 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00baeff4 bytes 29b947f9
+ 00baf038 bytes 29e147f9
~~~


<a id="compare-52b30f67ec818da431242947452cd3d1"></a>

### [`00baf314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf314.md) → [`00baf358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf358.md) _ZNSt6__ndk115numpunct_bynameIcEC1EPKcm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00be1c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c20.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00be1c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c70.md)

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
      "definition_site": "00baf38c",
      "incomplete_value": true,
      "site": "00baf38c",
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
      "definition_site": "00baf348",
      "incomplete_value": true,
      "site": "00baf348",
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
      "00baf380",
      "READ",
      [
        "storage",
        "00c1bf78",
        null,
        "pointer"
      ]
    ],
    [
      "00baf38c",
      "DATA",
      [
        "storage",
        "00c13bc8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00baf380",
      "READ",
      [
        "storage",
        "00c1bfc8",
        null,
        "pointer"
      ]
    ],
    [
      "00baf38c",
      "DATA",
      [
        "storage",
        "00c13c18",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf314.md#insn-00baf33c) · [`00baf34c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf314.md#insn-00baf34c)
- 新版 `00baf380`（命令位置の公開資料なし） · `00baf390`（命令位置の公開資料なし）

~~~diff
- 00baf33c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f78:8"]]
- 00baf33c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baf380 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc8:8"]]
+ 00baf380 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00baf33c bytes 08bd47f9
+ 00baf380 bytes 08e547f9
- 00baf34c ["INT_ADD", "register:40f0:8", ["const:baf34c:8", "const:4:8"]]
- 00baf34c ["CALL", null, ["callee:00be1c70:8"]]
+ 00baf390 ["INT_ADD", "register:40f0:8", ["const:baf390:8", "const:4:8"]]
+ 00baf390 ["CALL", null, ["callee:00be1c70:8"]]
- 00baf34c bytes 35ca0094
+ 00baf390 bytes 38ca0094
~~~


<a id="compare-3ffa1009177ccaee8e04fe331eb7a5ae"></a>

### [`00baf374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf374.md) → [`00baf3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf3b8.md) _ZNSt6__ndk115numpunct_bynameIcE6__initEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c20.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00be1c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c70.md) · 呼出先 13件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00b75128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75128.md) [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.67% / 新版 98.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00baf3e0",
      "incomplete_value": false,
      "site": "00baf3e8",
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
            "const:70e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baf39c",
      "incomplete_value": false,
      "site": "00baf3a4",
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
            "const:683:8"
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
      "00baf3e0",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ],
    [
      "00baf5e4",
      "PARAM",
      [
        "storage",
        "00299a27",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00baf3e0",
      "PARAM",
      [
        "storage",
        "002a570e",
        null,
        null
      ]
    ],
    [
      "00baf5e4",
      "PARAM",
      [
        "storage",
        "0029999a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf374.md#insn-00baf3a4) · [`00baf39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf374.md#insn-00baf39c) · [`00baf3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf374.md#insn-00baf3b8)
- 新版 `00baf3e8`（命令位置の公開資料なし） · `00baf3e0`（命令位置の公開資料なし） · `00baf3fc`（命令位置の公開資料なし）

~~~diff
- 00baf3a4 ["INT_ADD", "register:40f0:8", ["const:baf3a4:8", "const:4:8"]]
- 00baf3a4 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00baf3e8 ["INT_ADD", "register:40f0:8", ["const:baf3e8:8", "const:4:8"]]
+ 00baf3e8 ["CALL", null, ["callee:00bde9d0:8"]]
- 00baf3a4 bytes 77bd0094
+ 00baf3e8 bytes 7abd0094
- 00baf39c ["COPY", "tmp:0:8", ["const:683:8"]]
- 00baf39c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00baf39c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00baf39c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00baf3e0 ["COPY", "tmp:0:8", ["const:70e:8"]]
+ 00baf3e0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00baf3e0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00baf3e0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00baf39c bytes 210c1a91
+ 00baf3e0 bytes 21381c91
- 00baf3b8 ["INT_ADD", "register:40f0:8", ["const:baf3b8:8", "const:4:8"]]
- 00baf3b8 ["CALL", null, ["callee:00be1570:8"]]
+ 00baf3fc ["INT_ADD", "register:40f0:8", ["const:baf3fc:8", "const:4:8"]]
+ 00baf3fc ["CALL", null, ["callee:00be1570:8"]]
- 00baf3b8 bytes 5ac80094
+ 00baf3fc bytes 5dc80094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6f8753df4f6c4c8f231bad910de0a59"></a>

### [`00baf648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf648.md) → [`00baf68c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf68c.md) _ZNSt6__ndk115numpunct_bynameIcEC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1830.md) · 呼出先 1件 [`00be1c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c20.md)
- 新版 呼出元 1件 [`00be1880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1880.md) · 呼出先 1件 [`00be1c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1c70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.96% / 新版 86.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00baf6c0",
      "incomplete_value": true,
      "site": "00baf6c0",
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
      "definition_site": "00baf67c",
      "incomplete_value": true,
      "site": "00baf67c",
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
      "00baf6b4",
      "READ",
      [
        "storage",
        "00c1bf78",
        null,
        "pointer"
      ]
    ],
    [
      "00baf6c0",
      "DATA",
      [
        "storage",
        "00c13bc8",
        null,
        "undefined1[80]"
      ]
    ]
  ],
  "added": [
    [
      "00baf6b4",
      "READ",
      [
        "storage",
        "00c1bfc8",
        null,
        "pointer"
      ]
    ],
    [
      "00baf6c0",
      "DATA",
      [
        "storage",
        "00c13c18",
        null,
        "undefined1[80]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf648.md#insn-00baf670) · [`00baf690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf648.md#insn-00baf690)
- 新版 `00baf6b4`（命令位置の公開資料なし） · `00baf6d4`（命令位置の公開資料なし）

~~~diff
- 00baf670 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f78:8"]]
- 00baf670 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00baf6b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:fc8:8"]]
+ 00baf6b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00baf670 bytes 08bd47f9
+ 00baf6b4 bytes 08e547f9
- 00baf690 ["INT_ADD", "register:40f0:8", ["const:baf690:8", "const:4:8"]]
- 00baf690 ["CALL", null, ["callee:00be1c70:8"]]
+ 00baf6d4 ["INT_ADD", "register:40f0:8", ["const:baf6d4:8", "const:4:8"]]
+ 00baf6d4 ["CALL", null, ["callee:00be1c70:8"]]
- 00baf690 bytes 64c90094
+ 00baf6d4 bytes 67c90094
~~~


<a id="compare-9be5e8f465defd5a204feeca334a734f"></a>

### [`00baf770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf770.md) → [`00baf7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf7b4.md) _ZNSt6__ndk115numpunct_bynameIwE6__initEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c50.md) · 呼出先 14件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00b750e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b750e4.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00baf6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf6e4.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)
- 新版 呼出元 1件 [`00be1ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1ca0.md) · 呼出先 14件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00b75128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75128.md) [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md) [`00baf728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf728.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.31% / 新版 98.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00baf928",
      "incomplete_value": false,
      "site": "00baf938",
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
            "const:12a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00baf8e4",
      "incomplete_value": false,
      "site": "00baf8f4",
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
            "const:9f:8"
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
      "00baf7dc",
      "PARAM",
      [
        "storage",
        "002a5683",
        null,
        null
      ]
    ],
    [
      "00baf928",
      "PARAM",
      [
        "storage",
        "002a109f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00baf7dc",
      "PARAM",
      [
        "storage",
        "002a570e",
        null,
        null
      ]
    ],
    [
      "00baf928",
      "PARAM",
      [
        "storage",
        "002a112a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00baf8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf770.md#insn-00baf8f4) · [`00baf798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf770.md#insn-00baf798) · [`00baf7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf770.md#insn-00baf7a0)
- 新版 `00baf938`（命令位置の公開資料なし） · `00baf7dc`（命令位置の公開資料なし） · `00baf7e4`（命令位置の公開資料なし）

~~~diff
- 00baf8f4 ["INT_ADD", "register:40f0:8", ["const:baf8f4:8", "const:4:8"]]
- 00baf8f4 ["CALL", null, ["callee:00ba8ac4:8"]]
+ 00baf938 ["INT_ADD", "register:40f0:8", ["const:baf938:8", "const:4:8"]]
+ 00baf938 ["CALL", null, ["callee:00ba8ac4:8"]]
- 00baf8f4 bytes 63e4ff97
+ 00baf938 bytes 63e4ff97
- 00baf798 ["COPY", "tmp:0:8", ["const:683:8"]]
- 00baf798 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00baf798 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00baf798 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00baf7dc ["COPY", "tmp:0:8", ["const:70e:8"]]
+ 00baf7dc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00baf7dc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00baf7dc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00baf798 bytes 210c1a91
+ 00baf7dc bytes 21381c91
- 00baf7a0 ["INT_ADD", "register:40f0:8", ["const:baf7a0:8", "const:4:8"]]
- 00baf7a0 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00baf7e4 ["INT_ADD", "register:40f0:8", ["const:baf7e4:8", "const:4:8"]]
+ 00baf7e4 ["CALL", null, ["callee:00bde9d0:8"]]
- 00baf7a0 bytes 78bc0094
+ 00baf7e4 bytes 7bbc0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab7cf24a33bec817e1fd2f1e4b4c39ee"></a>

### [`00bafbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafbbc.md) → [`00bafc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00bafc00.md) _ZNKSt6__ndk120__time_get_c_storageIcE7__weeksEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bafc28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafc28.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bafc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00bafc6c.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 62.96% / 新版 62.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bafc5c",
      "incomplete_value": false,
      "site": "00bafc5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bafc18",
      "incomplete_value": false,
      "site": "00bafc18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b60:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bafc4c",
      "incomplete_value": false,
      "site": "00bafc5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bafc08",
      "incomplete_value": false,
      "site": "00bafc18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "definition_site": "00bafc34",
      "incomplete_value": false,
      "site": "00bafc38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bafbf0",
      "incomplete_value": false,
      "site": "00bafbf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "00bafc14",
      "READ",
      [
        "storage",
        "010a2b68",
        null,
        "undefined1"
      ]
    ],
    [
      "00bafc20",
      "READ",
      [
        "storage",
        "010a2b60",
        null,
        "undefined8"
      ]
    ],
    [
      "00bafc20",
      "DATA",
      [
        "storage",
        "010a2c60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bafc14",
      "READ",
      [
        "storage",
        "010a2ba8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bafc20",
      "READ",
      [
        "storage",
        "010a2ba0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bafc20",
      "DATA",
      [
        "storage",
        "010a2ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bafbf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafbbc.md#insn-00bafbf4) · [`00bafc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafbbc.md#insn-00bafc18)
- 新版 `00bafc38`（命令位置の公開資料なし） · `00bafc5c`（命令位置の公開資料なし） · `00bafc18`（命令位置の公開資料なし）

~~~diff
- 00bafbf4 ["INT_ADD", "register:40f0:8", ["const:bafbf4:8", "const:4:8"]]
- 00bafbf4 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bafc38 ["INT_ADD", "register:40f0:8", ["const:bafc38:8", "const:4:8"]]
+ 00bafc38 ["CALL", null, ["callee:00bdb000:8"]]
- 00bafbf4 bytes efac0094
+ 00bafc38 bytes f2ac0094
- 00bafc18 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b60:8"]]
- 00bafc18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00bafc5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ba0:8"]]
+ 00bafc5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bafc18 bytes 09b105f9
+ 00bafc5c bytes 09d105f9
+ 00bafc18 ["COPY", "register:4040:8", ["const:10a2000:8"]]
+ 00bafc18 bytes 882700f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c69cca3e558ee268634d045f2df800c8"></a>

### [`00bafc28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafc28.md) → [`00bafc6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00bafc6c.md) FUN_00bafc6c

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bafbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafbbc.md) · 呼出先 4件 [`00bb8cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8cec.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00bafc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00bafc00.md) · 呼出先 4件 [`00bb8d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb8/00bb8d30.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 70.37% / 新版 70.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 26件, `store_value` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bafca0",
      "incomplete_value": false,
      "site": "00bafca0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bafc5c",
      "incomplete_value": false,
      "site": "00bafc5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bafcb8",
      "incomplete_value": false,
      "site": "00bafcb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bafc74",
      "incomplete_value": false,
      "site": "00bafc74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c68:8"
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
      "definition_site": "00bafcec",
      "incomplete_value": false,
      "site": "00bafcec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bafca8",
      "incomplete_value": false,
      "site": "00bafca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c78:8"
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
      "00bafc80",
      "READ",
      [
        "storage",
        "010a2db0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bafc8c",
      "READ",
      [
        "storage",
        "010a2c60",
        null,
        "undefined1"
      ]
    ],
    [
      "00bafca0",
      "WRITE",
      [
        "storage",
        "010a2c60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bafc80",
      "READ",
      [
        "storage",
        "010a2df0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bafc8c",
      "READ",
      [
        "storage",
        "010a2ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bafca0",
      "WRITE",
      [
        "storage",
        "010a2ca0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bafca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafc28.md#insn-00bafca0) · [`00bafcec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafc28.md#insn-00bafcec) · [`00bafd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00bafc28.md#insn-00bafd30)
- 新版 `00bafce4`（命令位置の公開資料なし） · `00bafd30`（命令位置の公開資料なし） · `00bafd74`（命令位置の公開資料なし）

~~~diff
- 00bafca0 ["COPY", "tmp:0:8", ["const:c78:8"]]
- 00bafca0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bafca0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bafca0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bafce4 ["COPY", "tmp:0:8", ["const:cb8:8"]]
+ 00bafce4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bafce4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bafce4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bafca0 bytes 08e13191
+ 00bafce4 bytes 08e13291
- 00bafcec ["COPY", "tmp:0:8", ["const:c90:8"]]
- 00bafcec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bafcec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bafcec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bafd30 ["COPY", "tmp:0:8", ["const:cd0:8"]]
+ 00bafd30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bafd30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bafd30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bafcec bytes 08413291
+ 00bafd30 bytes 08413391
- 00bafd30 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ca8:8"]]
- 00bafd30 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00bafd30 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00bafd74 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ce8:8"]]
+ 00bafd74 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00bafd74 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00bafd30 bytes 28a17239
+ 00bafd74 bytes 28a17339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d6fbc419963f57f05cb0df91bb3444f"></a>

### [`00bb0060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0060.md) → [`00bb00a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb00a4.md) _ZNKSt6__ndk120__time_get_c_storageIwE7__weeksEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb00e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb00e0.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb0124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0124.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb0100",
      "incomplete_value": true,
      "site": "00bb0100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb00bc",
      "incomplete_value": true,
      "site": "00bb00bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b70:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb00f4",
      "incomplete_value": false,
      "site": "00bb0100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb00b0",
      "incomplete_value": false,
      "site": "00bb00bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:db8:8"
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
      "definition_site": "00bb00e0",
      "incomplete_value": false,
      "site": "00bb00e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb009c",
      "incomplete_value": false,
      "site": "00bb00a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b78:8"
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
      "00bb00c0",
      "READ",
      [
        "storage",
        "010a2b78",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb00c8",
      "READ",
      [
        "storage",
        "010a2b70",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb00c8",
      "DATA",
      [
        "storage",
        "010a2db8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb00c0",
      "READ",
      [
        "storage",
        "010a2bb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb00c8",
      "READ",
      [
        "storage",
        "010a2bb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb00c8",
      "DATA",
      [
        "storage",
        "010a2df8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb00a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0060.md#insn-00bb00a0) · [`00bb00a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0060.md#insn-00bb00a8) · [`00bb00bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0060.md#insn-00bb00bc)
- 新版 `00bb00e4`（命令位置の公開資料なし） · `00bb00ec`（命令位置の公開資料なし） · `00bb0100`（命令位置の公開資料なし）

~~~diff
- 00bb00a0 ["INT_ADD", "register:40f0:8", ["const:bb00a0:8", "const:4:8"]]
- 00bb00a0 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb00e4 ["INT_ADD", "register:40f0:8", ["const:bb00e4:8", "const:4:8"]]
+ 00bb00e4 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb00a0 bytes c4ab0094
+ 00bb00e4 bytes c7ab0094
- 00bb00a8 ["INT_ADD", "register:40f0:8", ["const:bb00a8:8", "const:4:8"]]
- 00bb00a8 ["CALL", null, ["ram:bb00e0:8"]]
+ 00bb00ec ["INT_ADD", "register:40f0:8", ["const:bb00ec:8", "const:4:8"]]
+ 00bb00ec ["CALL", null, ["ram:bb0124:8"]]
- 00bb00a8 bytes 0e000094
+ 00bb00ec bytes 0e000094
- 00bb00bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b70:8"]]
- 00bb00bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bb0100 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bb0:8"]]
+ 00bb0100 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb00bc bytes 68ba05f9
+ 00bb0100 bytes 68da05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f6154d19b1b6929f047e8b6c8a94118"></a>

### [`00bb03b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb03b4.md) → [`00bb03f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb03f8.md) _ZNKSt6__ndk120__time_get_c_storageIcE8__monthsEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb0420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0420.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb0464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0464.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb0454",
      "incomplete_value": false,
      "site": "00bb0454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb0410",
      "incomplete_value": false,
      "site": "00bb0410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b80:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb0444",
      "incomplete_value": false,
      "site": "00bb0454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb0400",
      "incomplete_value": false,
      "site": "00bb0410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:f10:8"
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
      "definition_site": "00bb042c",
      "incomplete_value": false,
      "site": "00bb0430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb03e8",
      "incomplete_value": false,
      "site": "00bb03ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b88:8"
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
      "00bb040c",
      "READ",
      [
        "storage",
        "010a2b88",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0418",
      "READ",
      [
        "storage",
        "010a2b80",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb0418",
      "DATA",
      [
        "storage",
        "010a2f10",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb040c",
      "READ",
      [
        "storage",
        "010a2bc8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0418",
      "READ",
      [
        "storage",
        "010a2bc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb0418",
      "DATA",
      [
        "storage",
        "010a2f50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb03ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb03b4.md#insn-00bb03ec) · [`00bb0410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb03b4.md#insn-00bb0410)
- 新版 `00bb0430`（命令位置の公開資料なし） · `00bb0454`（命令位置の公開資料なし） · `00bb0410`（命令位置の公開資料なし）

~~~diff
- 00bb03ec ["INT_ADD", "register:40f0:8", ["const:bb03ec:8", "const:4:8"]]
- 00bb03ec ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb0430 ["INT_ADD", "register:40f0:8", ["const:bb0430:8", "const:4:8"]]
+ 00bb0430 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb03ec bytes f1aa0094
+ 00bb0430 bytes f4aa0094
- 00bb0410 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b80:8"]]
- 00bb0410 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00bb0454 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bc0:8"]]
+ 00bb0454 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bb0410 bytes 09c105f9
+ 00bb0454 bytes 09e105f9
+ 00bb0410 ["COPY", "register:4040:8", ["const:10a2000:8"]]
+ 00bb0410 bytes 882700d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9846faf707c1ec52c6243f629012ab77"></a>

### [`00bb0420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0420.md) → [`00bb0464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0464.md) FUN_00bb0464

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bb03b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb03b4.md) · 呼出先 4件 [`00bb8fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb8/00bb8fcc.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00bb03f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb03f8.md) · 呼出先 4件 [`00bb9010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb9010.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 70.48% / 新版 70.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 48件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb0498",
      "incomplete_value": false,
      "site": "00bb0498",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb0454",
      "incomplete_value": false,
      "site": "00bb0454",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:f10:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb04b0",
      "incomplete_value": false,
      "site": "00bb04b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb046c",
      "incomplete_value": false,
      "site": "00bb046c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:f18:8"
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
      "definition_site": "00bb04e8",
      "incomplete_value": false,
      "site": "00bb04e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:f68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb04a4",
      "incomplete_value": false,
      "site": "00bb04a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:f28:8"
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
      "00bb0478",
      "READ",
      [
        "storage",
        "010a3150",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0484",
      "READ",
      [
        "storage",
        "010a2f10",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0498",
      "WRITE",
      [
        "storage",
        "010a2f10",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb0478",
      "READ",
      [
        "storage",
        "010a3190",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0484",
      "READ",
      [
        "storage",
        "010a2f50",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0498",
      "WRITE",
      [
        "storage",
        "010a2f50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb0460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0420.md#insn-00bb0460) · [`00bb04b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0420.md#insn-00bb04b0) · [`00bb04e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0420.md#insn-00bb04e8)
- 新版 `00bb04a4`（命令位置の公開資料なし） · `00bb04f4`（命令位置の公開資料なし） · `00bb052c`（命令位置の公開資料なし）

~~~diff
- 00bb0460 ["COPY", "tmp:0:8", ["const:f18:8"]]
- 00bb0460 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bb0460 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bb0460 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bb04a4 ["COPY", "tmp:0:8", ["const:f58:8"]]
+ 00bb04a4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb04a4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb04a4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bb0460 bytes 29613c91
+ 00bb04a4 bytes 29613d91
- 00bb04b0 ["COPY", "tmp:0:8", ["const:f30:8"]]
- 00bb04b0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bb04b0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bb04b0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bb04f4 ["COPY", "tmp:0:8", ["const:f70:8"]]
+ 00bb04f4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb04f4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb04f4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bb04b0 bytes 29c13c91
+ 00bb04f4 bytes 29c13d91
- 00bb04e8 ["COPY", "tmp:0:8", ["const:f40:8"]]
- 00bb04e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb04e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb04e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb052c ["COPY", "tmp:0:8", ["const:f80:8"]]
+ 00bb052c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb052c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb052c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb04e8 bytes 08013d91
+ 00bb052c bytes 08013e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-363076c19d56afeef40e7a9b94ce00bd"></a>

### [`00bb0af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0af4.md) → [`00bb0b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0b38.md) _ZNKSt6__ndk120__time_get_c_storageIwE8__monthsEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb0b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0b74.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb0bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb0/00bb0bb8.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call, call_argument_candidate, call_target, constant, operands_and_dependencies, operation_sequence, store_destination, store_value

命令の説明率　旧版 65.38% / 新版 65.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `call_target` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb0b94",
      "incomplete_value": true,
      "site": "00bb0b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb0b50",
      "incomplete_value": true,
      "site": "00bb0b50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b90:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb0b88",
      "incomplete_value": false,
      "site": "00bb0b94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:198:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb0b44",
      "incomplete_value": false,
      "site": "00bb0b50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:158:8"
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
      "definition_site": "00bb0b74",
      "incomplete_value": false,
      "site": "00bb0b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb0b30",
      "incomplete_value": false,
      "site": "00bb0b34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:b98:8"
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
      "00bb0b54",
      "READ",
      [
        "storage",
        "010a2b98",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0b5c",
      "READ",
      [
        "storage",
        "010a2b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb0b5c",
      "DATA",
      [
        "storage",
        "010a3158",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb0b54",
      "READ",
      [
        "storage",
        "010a2bd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb0b5c",
      "READ",
      [
        "storage",
        "010a2bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb0b5c",
      "DATA",
      [
        "storage",
        "010a3198",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb0b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0af4.md#insn-00bb0b34) · [`00bb0b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0af4.md#insn-00bb0b3c) · [`00bb0b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb0/00bb0af4.md#insn-00bb0b50)
- 新版 `00bb0b78`（命令位置の公開資料なし） · `00bb0b80`（命令位置の公開資料なし） · `00bb0b94`（命令位置の公開資料なし）

~~~diff
- 00bb0b34 ["INT_ADD", "register:40f0:8", ["const:bb0b34:8", "const:4:8"]]
- 00bb0b34 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb0b78 ["INT_ADD", "register:40f0:8", ["const:bb0b78:8", "const:4:8"]]
+ 00bb0b78 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb0b34 bytes 1fa90094
+ 00bb0b78 bytes 22a90094
- 00bb0b3c ["INT_ADD", "register:40f0:8", ["const:bb0b3c:8", "const:4:8"]]
- 00bb0b3c ["CALL", null, ["ram:bb0b74:8"]]
+ 00bb0b80 ["INT_ADD", "register:40f0:8", ["const:bb0b80:8", "const:4:8"]]
+ 00bb0b80 ["CALL", null, ["ram:bb0bb8:8"]]
- 00bb0b3c bytes 0e000094
+ 00bb0b80 bytes 0e000094
- 00bb0b50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b90:8"]]
- 00bb0b50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
+ 00bb0b94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bd0:8"]]
+ 00bb0b94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00bb0b50 bytes 68ca05f9
+ 00bb0b94 bytes 68ea05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd2f15e88d341f12d196da831c6595af"></a>

### [`00bb109c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb109c.md) → [`00bb10e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb10e0.md) _ZNKSt6__ndk120__time_get_c_storageIcE7__am_pmEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb1108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1108.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb114c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb114c.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb113c",
      "incomplete_value": false,
      "site": "00bb113c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:be0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb10f8",
      "incomplete_value": false,
      "site": "00bb10f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ba0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb112c",
      "incomplete_value": false,
      "site": "00bb113c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb10e8",
      "incomplete_value": false,
      "site": "00bb10f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
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
      "definition_site": "00bb1114",
      "incomplete_value": false,
      "site": "00bb1118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:be8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb10d0",
      "incomplete_value": false,
      "site": "00bb10d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
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
      "00bb10f4",
      "READ",
      [
        "storage",
        "010a2ba8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1100",
      "READ",
      [
        "storage",
        "010a2ba0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb1100",
      "DATA",
      [
        "storage",
        "010a33a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb10f4",
      "READ",
      [
        "storage",
        "010a2be8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1100",
      "READ",
      [
        "storage",
        "010a2be0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb1100",
      "DATA",
      [
        "storage",
        "010a33e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb10d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb109c.md#insn-00bb10d4) · [`00bb10f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb109c.md#insn-00bb10f8)
- 新版 `00bb1118`（命令位置の公開資料なし） · `00bb113c`（命令位置の公開資料なし） · `00bb10f8`（命令位置の公開資料なし）

~~~diff
- 00bb10d4 ["INT_ADD", "register:40f0:8", ["const:bb10d4:8", "const:4:8"]]
- 00bb10d4 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb1118 ["INT_ADD", "register:40f0:8", ["const:bb1118:8", "const:4:8"]]
+ 00bb1118 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb10d4 bytes b7a70094
+ 00bb1118 bytes baa70094
- 00bb10f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ba0:8"]]
- 00bb10f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00bb113c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:be0:8"]]
+ 00bb113c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bb10f8 bytes 09d105f9
+ 00bb113c bytes 09f105f9
+ 00bb10f8 ["COPY", "register:4040:8", ["const:10a2000:8"]]
+ 00bb10f8 bytes 882700b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24bc30455150d0112cc7d0aca03244c9"></a>

### [`00bb1108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1108.md) → [`00bb114c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb114c.md) FUN_00bb114c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bb109c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb109c.md) · 呼出先 4件 [`00bb906c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb906c.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00bb10e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb10e0.md) · 呼出先 4件 [`00bb90b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb90b0.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb1180",
      "incomplete_value": false,
      "site": "00bb1180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb113c",
      "incomplete_value": false,
      "site": "00bb113c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3a0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb1198",
      "incomplete_value": false,
      "site": "00bb1198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1154",
      "incomplete_value": false,
      "site": "00bb1154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3a8:8"
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
      "definition_site": "00bb11c0",
      "incomplete_value": false,
      "site": "00bb11c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb117c",
      "incomplete_value": false,
      "site": "00bb117c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3b8:8"
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
      "00bb1160",
      "READ",
      [
        "storage",
        "010a33d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb116c",
      "READ",
      [
        "storage",
        "010a33a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1180",
      "WRITE",
      [
        "storage",
        "010a33a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb1160",
      "READ",
      [
        "storage",
        "010a3410",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb116c",
      "READ",
      [
        "storage",
        "010a33e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1180",
      "WRITE",
      [
        "storage",
        "010a33e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb1174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1108.md#insn-00bb1174) · [`00bb11b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1108.md#insn-00bb11b8) · [`00bb11c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1108.md#insn-00bb11c0)
- 新版 `00bb11b8`（命令位置の公開資料なし） · `00bb11fc`（命令位置の公開資料なし）

~~~diff
- 00bb1174 ["COPY", "tmp:0:8", ["const:3b8:8"]]
- 00bb1174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb1174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb1174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb11b8 ["COPY", "tmp:0:8", ["const:3f8:8"]]
+ 00bb11b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb11b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb11b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb1174 bytes 08e10e91
+ 00bb11b8 bytes 08e10f91
- 00bb11b8 ["INT_ADD", "register:40f0:8", ["const:bb11b8:8", "const:4:8"]]
- 00bb11b8 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb11fc ["INT_ADD", "register:40f0:8", ["const:bb11fc:8", "const:4:8"]]
+ 00bb11fc ["CALL", null, ["callee:00bdb000:8"]]
- 00bb11b8 bytes 7ea70094
+ 00bb11fc bytes 81a70094
- 00bb11c0 ["COPY", "register:4000:8", ["const:bb9000:8"]]
- 00bb11c0 bytes 40000090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-27dd4618ec95976dff99e2d32718dd67"></a>

### [`00bb11e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb11e8.md) → [`00bb122c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb122c.md) _ZNKSt6__ndk120__time_get_c_storageIwE7__am_pmEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bb1254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1254.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bb1298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb1298.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate, store_destination, store_value

命令の説明率　旧版 70.37% / 新版 70.37%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_destination` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb1288",
      "incomplete_value": false,
      "site": "00bb1288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1244",
      "incomplete_value": false,
      "site": "00bb1244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb1278",
      "incomplete_value": true,
      "site": "00bb1288",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1234",
      "incomplete_value": true,
      "site": "00bb1244",
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
            "const:3d8:8"
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
      "definition_site": "00bb1260",
      "incomplete_value": false,
      "site": "00bb1264",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb121c",
      "incomplete_value": false,
      "site": "00bb1220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bb8:8"
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
      "00bb1240",
      "READ",
      [
        "storage",
        "010a2bb8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb124c",
      "READ",
      [
        "storage",
        "010a2bb0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb124c",
      "DATA",
      [
        "storage",
        "010a33d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb1240",
      "READ",
      [
        "storage",
        "010a2bf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb124c",
      "READ",
      [
        "storage",
        "010a2bf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00bb124c",
      "DATA",
      [
        "storage",
        "010a3418",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb1220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb11e8.md#insn-00bb1220) · [`00bb1244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb11e8.md#insn-00bb1244)
- 新版 `00bb1264`（命令位置の公開資料なし） · `00bb1288`（命令位置の公開資料なし） · `00bb1244`（命令位置の公開資料なし）

~~~diff
- 00bb1220 ["INT_ADD", "register:40f0:8", ["const:bb1220:8", "const:4:8"]]
- 00bb1220 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb1264 ["INT_ADD", "register:40f0:8", ["const:bb1264:8", "const:4:8"]]
+ 00bb1264 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb1220 bytes 64a70094
+ 00bb1264 bytes 67a70094
- 00bb1244 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bb0:8"]]
- 00bb1244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
+ 00bb1288 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:bf0:8"]]
+ 00bb1288 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:8"]]
- 00bb1244 bytes 09d905f9
+ 00bb1288 bytes 09f905f9
+ 00bb1244 ["COPY", "register:4040:8", ["const:10a2000:8"]]
+ 00bb1244 bytes 882700b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3e6cc4fc7a9e9a72c2b3b1577084dd4"></a>

### [`00bb1254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1254.md) → [`00bb1298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb1298.md) FUN_00bb1298

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bb11e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb11e8.md) · 呼出先 4件 [`00bb90b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb9/00bb90b8.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00bb122c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb122c.md) · 呼出先 4件 [`00bb90fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb9/00bb90fc.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 75.44% / 新版 75.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb12cc",
      "incomplete_value": false,
      "site": "00bb12cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1288",
      "incomplete_value": false,
      "site": "00bb1288",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3d8:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00bb12e4",
      "incomplete_value": false,
      "site": "00bb12e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb12a0",
      "incomplete_value": false,
      "site": "00bb12a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "definition_site": "00bb1310",
      "incomplete_value": false,
      "site": "00bb1310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:430:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb12cc",
      "incomplete_value": false,
      "site": "00bb12cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a3000:8"
          ],
          [
            "leaf",
            "const:3f0:8"
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
      "00bb12ac",
      "READ",
      [
        "storage",
        "010a3408",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb12b8",
      "READ",
      [
        "storage",
        "010a33d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb12cc",
      "WRITE",
      [
        "storage",
        "010a33d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb12ac",
      "READ",
      [
        "storage",
        "010a3448",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb12b8",
      "READ",
      [
        "storage",
        "010a3418",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb12cc",
      "WRITE",
      [
        "storage",
        "010a3418",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb12c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1254.md#insn-00bb12c4) · [`00bb1308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1254.md#insn-00bb1308) · [`00bb1310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1254.md#insn-00bb1310)
- 新版 `00bb1308`（命令位置の公開資料なし） · `00bb134c`（命令位置の公開資料なし）

~~~diff
- 00bb12c4 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 00bb12c4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00bb12c4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00bb12c4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00bb1308 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 00bb1308 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb1308 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00bb1308 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00bb12c4 bytes 29c10f91
+ 00bb1308 bytes 29c11091
- 00bb1308 ["INT_ADD", "register:40f0:8", ["const:bb1308:8", "const:4:8"]]
- 00bb1308 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb134c ["INT_ADD", "register:40f0:8", ["const:bb134c:8", "const:4:8"]]
+ 00bb134c ["CALL", null, ["callee:00bdb000:8"]]
- 00bb1308 bytes 2aa70094
+ 00bb134c bytes 2da70094
- 00bb1310 ["COPY", "register:4000:8", ["const:bb9000:8"]]
- 00bb1310 bytes 40000090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab2484fb9ed5f0493d7aad412555d92f"></a>

### [`00bb1338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1338.md) → [`00bb137c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb137c.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__xEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb13b0",
      "incomplete_value": false,
      "site": "00bb13b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb136c",
      "incomplete_value": false,
      "site": "00bb1370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bc0:8"
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
      "definition_site": "00bb13d0",
      "incomplete_value": false,
      "site": "00bb13d4",
      "value": [
        "leaf",
        "const:be5fd0:8"
      ]
    },
    "old": {
      "definition_site": "00bb138c",
      "incomplete_value": false,
      "site": "00bb1390",
      "value": [
        "leaf",
        "const:be5f80:8"
      ]
    },
    "ordinal": 1,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb13dc",
      "incomplete_value": true,
      "site": "00bb13e0",
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
            "const:c00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1398",
      "incomplete_value": true,
      "site": "00bb139c",
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
            "const:bc0:8"
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
      "00bb1390",
      "READ",
      [
        "storage",
        "010a2bc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb139c",
      "DATA",
      [
        "storage",
        "00c248e0",
        null,
        null
      ]
    ],
    [
      "00bb13b0",
      "PARAM",
      [
        "storage",
        "010a2bc0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb1390",
      "READ",
      [
        "storage",
        "010a2c00",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb139c",
      "DATA",
      [
        "storage",
        "00c24930",
        null,
        null
      ]
    ],
    [
      "00bb13b0",
      "PARAM",
      [
        "storage",
        "010a2c00",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb1358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1338.md#insn-00bb1358) · [`00bb1370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1338.md#insn-00bb1370) · [`00bb1390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1338.md#insn-00bb1390)
- 新版 `00bb139c`（命令位置の公開資料なし） · `00bb13b4`（命令位置の公開資料なし） · `00bb13d4`（命令位置の公開資料なし）

~~~diff
- 00bb1358 ["COPY", "register:4000:8", ["const:c248e0:8"]]
+ 00bb139c ["COPY", "register:4000:8", ["const:c24930:8"]]
- 00bb1358 bytes 40ac3910
+ 00bb139c bytes a0ac3910
- 00bb1370 ["INT_ADD", "register:40f0:8", ["const:bb1370:8", "const:4:8"]]
- 00bb1370 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb13b4 ["INT_ADD", "register:40f0:8", ["const:bb13b4:8", "const:4:8"]]
+ 00bb13b4 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb1370 bytes 10a70094
+ 00bb13b4 bytes 13a70094
- 00bb1390 ["INT_ADD", "register:40f0:8", ["const:bb1390:8", "const:4:8"]]
- 00bb1390 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00bb13d4 ["INT_ADD", "register:40f0:8", ["const:bb13d4:8", "const:4:8"]]
+ 00bb13d4 ["CALL", null, ["callee:00bdafe0:8"]]
- 00bb1390 bytes 00a70094
+ 00bb13d4 bytes 03a70094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b74304252f05680a175a6920fbb1aeca"></a>

### [`00bb13a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb13a4.md) → [`00bb13e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb13e8.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__xEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b75e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75e74.md) [`00baf1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf1e0.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b75eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75eb8.md) [`00baf224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf224.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb1424",
      "incomplete_value": false,
      "site": "00bb1428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb13e0",
      "incomplete_value": false,
      "site": "00bb13e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:be0:8"
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
      "definition_site": "00bb1450",
      "incomplete_value": true,
      "site": "00bb145c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb140c",
      "incomplete_value": true,
      "site": "00bb1418",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c30:8"
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
      "definition_site": "00bb144c",
      "incomplete_value": false,
      "site": "00bb145c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1408",
      "incomplete_value": false,
      "site": "00bb1418",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bc8:8"
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
      "00bb1400",
      "READ",
      [
        "storage",
        "010a2be0",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb140c",
      "DATA",
      [
        "storage",
        "010a2bc8",
        null,
        null
      ]
    ],
    [
      "00bb1424",
      "PARAM",
      [
        "storage",
        "010a2be0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb1400",
      "READ",
      [
        "storage",
        "010a2c20",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb140c",
      "DATA",
      [
        "storage",
        "010a2c08",
        null,
        null
      ]
    ],
    [
      "00bb1424",
      "PARAM",
      [
        "storage",
        "010a2c20",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb13e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb13a4.md#insn-00bb13e0) · [`00bb13e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb13a4.md#insn-00bb13e4) · [`00bb1418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb13a4.md#insn-00bb1418)
- 新版 `00bb1424`（命令位置の公開資料なし） · `00bb1428`（命令位置の公開資料なし） · `00bb145c`（命令位置の公開資料なし）

~~~diff
- 00bb13e0 ["COPY", "tmp:0:8", ["const:be0:8"]]
- 00bb13e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb13e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb13e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb1424 ["COPY", "tmp:0:8", ["const:c20:8"]]
+ 00bb1424 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb1424 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb1424 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb13e0 bytes 00802f91
+ 00bb1424 bytes 00803091
- 00bb13e4 ["INT_ADD", "register:40f0:8", ["const:bb13e4:8", "const:4:8"]]
- 00bb13e4 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb1428 ["INT_ADD", "register:40f0:8", ["const:bb1428:8", "const:4:8"]]
+ 00bb1428 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb13e4 bytes f3a60094
+ 00bb1428 bytes f6a60094
- 00bb1418 ["INT_ADD", "register:40f0:8", ["const:bb1418:8", "const:4:8"]]
- 00bb1418 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00bb145c ["INT_ADD", "register:40f0:8", ["const:bb145c:8", "const:4:8"]]
+ 00bb145c ["CALL", null, ["callee:00bdafe0:8"]]
- 00bb1418 bytes dea60094
+ 00bb145c bytes e1a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a6fd6f434f124b6c80873346c5c9a40"></a>

### [`00bb1444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1444.md) → [`00bb1488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb1488.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__XEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb14d4",
      "incomplete_value": true,
      "site": "00bb14e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1490",
      "incomplete_value": true,
      "site": "00bb149c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
              ]
            ]
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
      "definition_site": "00bb14d0",
      "incomplete_value": false,
      "site": "00bb14e0",
      "value": [
        "leaf",
        "const:c24948:8"
      ]
    },
    "old": {
      "definition_site": "00bb148c",
      "incomplete_value": false,
      "site": "00bb149c",
      "value": [
        "leaf",
        "const:c248f8:8"
      ]
    },
    "ordinal": 1,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb14dc",
      "incomplete_value": false,
      "site": "00bb14e0",
      "value": [
        "leaf",
        "const:be5fd0:8"
      ]
    },
    "old": {
      "definition_site": "00bb1498",
      "incomplete_value": false,
      "site": "00bb149c",
      "value": [
        "leaf",
        "const:be5f80:8"
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
      "00bb149c",
      "READ",
      [
        "storage",
        "010a2be8",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb14a8",
      "DATA",
      [
        "storage",
        "00c248f8",
        null,
        null
      ]
    ],
    [
      "00bb14bc",
      "PARAM",
      [
        "storage",
        "010a2be8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb149c",
      "READ",
      [
        "storage",
        "010a2c28",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb14a8",
      "DATA",
      [
        "storage",
        "00c24948",
        null,
        null
      ]
    ],
    [
      "00bb14bc",
      "PARAM",
      [
        "storage",
        "010a2c28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb1464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1444.md#insn-00bb1464) · [`00bb149c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1444.md#insn-00bb149c) · [`00bb14a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1444.md#insn-00bb14a8)
- 新版 `00bb14a8`（命令位置の公開資料なし） · `00bb14e0`（命令位置の公開資料なし） · `00bb14ec`（命令位置の公開資料なし）

~~~diff
- 00bb1464 ["COPY", "register:4000:8", ["const:c248f8:8"]]
+ 00bb14a8 ["COPY", "register:4000:8", ["const:c24948:8"]]
- 00bb1464 bytes a0a43910
+ 00bb14a8 bytes 00a53910
- 00bb149c ["INT_ADD", "register:40f0:8", ["const:bb149c:8", "const:4:8"]]
- 00bb149c ["CALL", null, ["callee:00bdafe0:8"]]
+ 00bb14e0 ["INT_ADD", "register:40f0:8", ["const:bb14e0:8", "const:4:8"]]
+ 00bb14e0 ["CALL", null, ["callee:00bdafe0:8"]]
- 00bb149c bytes bda60094
+ 00bb14e0 bytes c0a60094
- 00bb14a8 ["INT_ADD", "register:40f0:8", ["const:bb14a8:8", "const:4:8"]]
- 00bb14a8 ["CALL", null, ["callee:00bdb020:8"]]
+ 00bb14ec ["INT_ADD", "register:40f0:8", ["const:bb14ec:8", "const:4:8"]]
+ 00bb14ec ["CALL", null, ["callee:00bdb020:8"]]
- 00bb14a8 bytes caa60094
+ 00bb14ec bytes cda60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d4902dd39266e14fa02e398b75df215"></a>

### [`00bb14b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb14b0.md) → [`00bb14f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb14f4.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__XEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b75e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75e74.md) [`00baf1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf1e0.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b75eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75eb8.md) [`00baf224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf224.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 73.53% / 新版 73.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb1530",
      "incomplete_value": false,
      "site": "00bb1534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb14ec",
      "incomplete_value": false,
      "site": "00bb14f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c08:8"
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
      "definition_site": "00bb1540",
      "incomplete_value": false,
      "site": "00bb154c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb14fc",
      "incomplete_value": false,
      "site": "00bb1508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
      "definition_site": "00bb155c",
      "incomplete_value": true,
      "site": "00bb1568",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1518",
      "incomplete_value": true,
      "site": "00bb1524",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:c30:8"
              ]
            ]
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
      "00bb150c",
      "READ",
      [
        "storage",
        "010a2c08",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1518",
      "DATA",
      [
        "storage",
        "010a2bf0",
        null,
        null
      ]
    ],
    [
      "00bb1530",
      "PARAM",
      [
        "storage",
        "010a2c08",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb150c",
      "READ",
      [
        "storage",
        "010a2c48",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1518",
      "DATA",
      [
        "storage",
        "010a2c30",
        null,
        null
      ]
    ],
    [
      "00bb1530",
      "PARAM",
      [
        "storage",
        "010a2c48",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb14c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb14b0.md#insn-00bb14c4) · [`00bb14ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb14b0.md#insn-00bb14ec) · [`00bb14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb14b0.md#insn-00bb14f0)
- 新版 `00bb1508`（命令位置の公開資料なし） · `00bb1530`（命令位置の公開資料なし） · `00bb1534`（命令位置の公開資料なし）

~~~diff
- 00bb14c4 ["COPY", "tmp:0:8", ["const:c08:8"]]
- 00bb14c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb14c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb14c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb1508 ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 00bb1508 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb1508 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb1508 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb14c4 bytes 08213091
+ 00bb1508 bytes 08213191
- 00bb14ec ["COPY", "tmp:0:8", ["const:c08:8"]]
- 00bb14ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb14ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb14ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb1530 ["COPY", "tmp:0:8", ["const:c48:8"]]
+ 00bb1530 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb1530 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb1530 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb14ec bytes 00203091
+ 00bb1530 bytes 00203191
- 00bb14f0 ["INT_ADD", "register:40f0:8", ["const:bb14f0:8", "const:4:8"]]
- 00bb14f0 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb1534 ["INT_ADD", "register:40f0:8", ["const:bb1534:8", "const:4:8"]]
+ 00bb1534 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb14f0 bytes b0a60094
+ 00bb1534 bytes b3a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-419bea33a3f0297e535cb3d76d369b35"></a>

### [`00bb1550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1550.md) → [`00bb1594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb1594.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__cEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 85.19% / 新版 85.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb15c8",
      "incomplete_value": false,
      "site": "00bb15cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1584",
      "incomplete_value": false,
      "site": "00bb1588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "definition_site": "00bb15e0",
      "incomplete_value": true,
      "site": "00bb15ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb159c",
      "incomplete_value": true,
      "site": "00bb15a8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:db8:8"
              ]
            ]
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
      "definition_site": "00bb15e8",
      "incomplete_value": false,
      "site": "00bb15ec",
      "value": [
        "leaf",
        "const:be5fd0:8"
      ]
    },
    "old": {
      "definition_site": "00bb15a4",
      "incomplete_value": false,
      "site": "00bb15a8",
      "value": [
        "leaf",
        "const:be5f80:8"
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
      "00bb15a8",
      "READ",
      [
        "storage",
        "010a2c10",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb15b4",
      "DATA",
      [
        "storage",
        "00c24910",
        null,
        "string"
      ]
    ],
    [
      "00bb15c8",
      "PARAM",
      [
        "storage",
        "010a2c10",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb15a8",
      "READ",
      [
        "storage",
        "010a2c50",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb15b4",
      "DATA",
      [
        "storage",
        "00c24960",
        null,
        "string"
      ]
    ],
    [
      "00bb15c8",
      "PARAM",
      [
        "storage",
        "010a2c50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb1570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1550.md#insn-00bb1570) · [`00bb1588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1550.md#insn-00bb1588) · [`00bb15a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1550.md#insn-00bb15a8)
- 新版 `00bb15b4`（命令位置の公開資料なし） · `00bb15cc`（命令位置の公開資料なし） · `00bb15ec`（命令位置の公開資料なし）

~~~diff
- 00bb1570 ["COPY", "register:4000:8", ["const:c24910:8"]]
+ 00bb15b4 ["COPY", "register:4000:8", ["const:c24960:8"]]
- 00bb1570 bytes 009d3910
+ 00bb15b4 bytes 609d3910
- 00bb1588 ["INT_ADD", "register:40f0:8", ["const:bb1588:8", "const:4:8"]]
- 00bb1588 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb15cc ["INT_ADD", "register:40f0:8", ["const:bb15cc:8", "const:4:8"]]
+ 00bb15cc ["CALL", null, ["callee:00bdb000:8"]]
- 00bb1588 bytes 8aa60094
+ 00bb15cc bytes 8da60094
- 00bb15a8 ["INT_ADD", "register:40f0:8", ["const:bb15a8:8", "const:4:8"]]
- 00bb15a8 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00bb15ec ["INT_ADD", "register:40f0:8", ["const:bb15ec:8", "const:4:8"]]
+ 00bb15ec ["CALL", null, ["callee:00bdafe0:8"]]
- 00bb15a8 bytes 7aa60094
+ 00bb15ec bytes 7da60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfc1719d2e15762da4106b187da4b7f1"></a>

### [`00bb15bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb15bc.md) → [`00bb1600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb1600.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__cEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b75e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75e74.md) [`00baf1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf1e0.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b75eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75eb8.md) [`00baf224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf224.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 73.53% / 新版 73.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb163c",
      "incomplete_value": false,
      "site": "00bb1640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb15f8",
      "incomplete_value": false,
      "site": "00bb15fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c30:8"
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
      "definition_site": "00bb164c",
      "incomplete_value": false,
      "site": "00bb1658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1608",
      "incomplete_value": false,
      "site": "00bb1614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c18:8"
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
      "definition_site": "00bb1668",
      "incomplete_value": true,
      "site": "00bb1674",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1624",
      "incomplete_value": true,
      "site": "00bb1630",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
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
      "00bb1618",
      "READ",
      [
        "storage",
        "010a2c30",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1624",
      "DATA",
      [
        "storage",
        "010a2c18",
        null,
        null
      ]
    ],
    [
      "00bb163c",
      "PARAM",
      [
        "storage",
        "010a2c30",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb1618",
      "READ",
      [
        "storage",
        "010a2c70",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1624",
      "DATA",
      [
        "storage",
        "010a2c58",
        null,
        null
      ]
    ],
    [
      "00bb163c",
      "PARAM",
      [
        "storage",
        "010a2c70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb15d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb15bc.md#insn-00bb15d0) · [`00bb15f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb15bc.md#insn-00bb15f8) · [`00bb15fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb15bc.md#insn-00bb15fc)
- 新版 `00bb1614`（命令位置の公開資料なし） · `00bb163c`（命令位置の公開資料なし） · `00bb1640`（命令位置の公開資料なし）

~~~diff
- 00bb15d0 ["COPY", "tmp:0:8", ["const:c30:8"]]
- 00bb15d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb15d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb15d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb1614 ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 00bb1614 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb1614 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb1614 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb15d0 bytes 08c13091
+ 00bb1614 bytes 08c13191
- 00bb15f8 ["COPY", "tmp:0:8", ["const:c30:8"]]
- 00bb15f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb15f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb15f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb163c ["COPY", "tmp:0:8", ["const:c70:8"]]
+ 00bb163c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb163c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb163c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb15f8 bytes 00c03091
+ 00bb163c bytes 00c03191
- 00bb15fc ["INT_ADD", "register:40f0:8", ["const:bb15fc:8", "const:4:8"]]
- 00bb15fc ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb1640 ["INT_ADD", "register:40f0:8", ["const:bb1640:8", "const:4:8"]]
+ 00bb1640 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb15fc bytes 6da60094
+ 00bb1640 bytes 70a60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-057e956ba9df5f7d56a8151acf5d90dc"></a>

### [`00bb165c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb165c.md) → [`00bb16a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb16a0.md) _ZNKSt6__ndk120__time_get_c_storageIcE3__rEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b55618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55618.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b5565c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b5565c.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 2件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb16d4",
      "incomplete_value": false,
      "site": "00bb16d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1690",
      "incomplete_value": false,
      "site": "00bb1694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "definition_site": "00bb16ec",
      "incomplete_value": true,
      "site": "00bb16f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb16a8",
      "incomplete_value": true,
      "site": "00bb16b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db8:8"
              ]
            ]
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
      "definition_site": "00bb16e8",
      "incomplete_value": false,
      "site": "00bb16f8",
      "value": [
        "leaf",
        "const:c24978:8"
      ]
    },
    "old": {
      "definition_site": "00bb16a4",
      "incomplete_value": false,
      "site": "00bb16b4",
      "value": [
        "leaf",
        "const:c24928:8"
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
      "00bb16b4",
      "READ",
      [
        "storage",
        "010a2c38",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb16c0",
      "DATA",
      [
        "storage",
        "00c24928",
        null,
        null
      ]
    ],
    [
      "00bb16d4",
      "PARAM",
      [
        "storage",
        "010a2c38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb16b4",
      "READ",
      [
        "storage",
        "010a2c78",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb16c0",
      "DATA",
      [
        "storage",
        "00c24978",
        null,
        null
      ]
    ],
    [
      "00bb16d4",
      "PARAM",
      [
        "storage",
        "010a2c78",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb167c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb165c.md#insn-00bb167c) · [`00bb1694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb165c.md#insn-00bb1694) · [`00bb16b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb165c.md#insn-00bb16b4)
- 新版 `00bb16c0`（命令位置の公開資料なし） · `00bb16d8`（命令位置の公開資料なし） · `00bb16f8`（命令位置の公開資料なし）

~~~diff
- 00bb167c ["COPY", "register:4000:8", ["const:c24928:8"]]
+ 00bb16c0 ["COPY", "register:4000:8", ["const:c24978:8"]]
- 00bb167c bytes 60953910
+ 00bb16c0 bytes c0953910
- 00bb1694 ["INT_ADD", "register:40f0:8", ["const:bb1694:8", "const:4:8"]]
- 00bb1694 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb16d8 ["INT_ADD", "register:40f0:8", ["const:bb16d8:8", "const:4:8"]]
+ 00bb16d8 ["CALL", null, ["callee:00bdb000:8"]]
- 00bb1694 bytes 47a60094
+ 00bb16d8 bytes 4aa60094
- 00bb16b4 ["INT_ADD", "register:40f0:8", ["const:bb16b4:8", "const:4:8"]]
- 00bb16b4 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00bb16f8 ["INT_ADD", "register:40f0:8", ["const:bb16f8:8", "const:4:8"]]
+ 00bb16f8 ["CALL", null, ["callee:00bdafe0:8"]]
- 00bb16b4 bytes 37a60094
+ 00bb16f8 bytes 3aa60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18b8368b79d27f364e2d1481b63337fb"></a>

### [`00bb16c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb16c8.md) → [`00bb170c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb170c.md) _ZNKSt6__ndk120__time_get_c_storageIwE3__rEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b75e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b75/00b75e74.md) [`00baf1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00baf/00baf1e0.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b75eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b75/00b75eb8.md) [`00baf224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00baf224.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, return_value_candidate

命令の説明率　旧版 73.53% / 新版 73.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `return_value_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb1748",
      "incomplete_value": false,
      "site": "00bb174c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1704",
      "incomplete_value": false,
      "site": "00bb1708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "definition_site": "00bb1758",
      "incomplete_value": false,
      "site": "00bb1764",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1714",
      "incomplete_value": false,
      "site": "00bb1720",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a2000:8"
          ],
          [
            "leaf",
            "const:c40:8"
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
      "definition_site": "00bb1774",
      "incomplete_value": true,
      "site": "00bb1780",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb1730",
      "incomplete_value": true,
      "site": "00bb173c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
              ]
            ]
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
      "00bb1724",
      "READ",
      [
        "storage",
        "010a2c58",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1730",
      "DATA",
      [
        "storage",
        "010a2c40",
        null,
        null
      ]
    ],
    [
      "00bb1748",
      "PARAM",
      [
        "storage",
        "010a2c58",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00bb1724",
      "READ",
      [
        "storage",
        "010a2c98",
        null,
        "undefined1"
      ]
    ],
    [
      "00bb1730",
      "DATA",
      [
        "storage",
        "010a2c80",
        null,
        null
      ]
    ],
    [
      "00bb1748",
      "PARAM",
      [
        "storage",
        "010a2c98",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb16dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb16c8.md#insn-00bb16dc) · [`00bb1704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb16c8.md#insn-00bb1704) · [`00bb1708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb16c8.md#insn-00bb1708)
- 新版 `00bb1720`（命令位置の公開資料なし） · `00bb1748`（命令位置の公開資料なし） · `00bb174c`（命令位置の公開資料なし）

~~~diff
- 00bb16dc ["COPY", "tmp:0:8", ["const:c58:8"]]
- 00bb16dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00bb16dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00bb16dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00bb1720 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 00bb1720 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb1720 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00bb1720 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00bb16dc bytes 08613191
+ 00bb1720 bytes 08613291
- 00bb1704 ["COPY", "tmp:0:8", ["const:c58:8"]]
- 00bb1704 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00bb1704 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00bb1704 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00bb1748 ["COPY", "tmp:0:8", ["const:c98:8"]]
+ 00bb1748 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb1748 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00bb1748 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00bb1704 bytes 00603191
+ 00bb1748 bytes 00603291
- 00bb1708 ["INT_ADD", "register:40f0:8", ["const:bb1708:8", "const:4:8"]]
- 00bb1708 ["CALL", null, ["callee:00bdb000:8"]]
+ 00bb174c ["INT_ADD", "register:40f0:8", ["const:bb174c:8", "const:4:8"]]
+ 00bb174c ["CALL", null, ["callee:00bdb000:8"]]
- 00bb1708 bytes 2aa60094
+ 00bb174c bytes 2da60094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6336637db28a7c6fd9b970c366d7729"></a>

### [`00bb1768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1768.md) → [`00bb17ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb1/00bb17ac.md) _ZNSt6__ndk110__time_getC1EPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1c70.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041b/0041b298.md) [`00ba8a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8a80.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md)
- 新版 呼出元 1件 [`00be1cc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1cc0.md) · 呼出先 6件 [`0041b298`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041b/0041b298.md) [`00ba8ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ba8/00ba8ac4.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.87% / 新版 97.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb1800",
      "incomplete_value": false,
      "site": "00bb1810",
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
            "const:4a1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb17bc",
      "incomplete_value": false,
      "site": "00bb17cc",
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
            "const:407:8"
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
      "00bb1800",
      "PARAM",
      [
        "storage",
        "002a6407",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00bb1800",
      "PARAM",
      [
        "storage",
        "002a64a1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb17cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1768.md#insn-00bb17cc) · [`00bb178c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1768.md#insn-00bb178c) · [`00bb17b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb1/00bb1768.md#insn-00bb17b4)
- 新版 `00bb1810`（命令位置の公開資料なし） · `00bb17d0`（命令位置の公開資料なし） · `00bb17f8`（命令位置の公開資料なし）

~~~diff
- 00bb17cc ["INT_ADD", "register:40f0:8", ["const:bb17cc:8", "const:4:8"]]
- 00bb17cc ["CALL", null, ["callee:00ba8ac4:8"]]
+ 00bb1810 ["INT_ADD", "register:40f0:8", ["const:bb1810:8", "const:4:8"]]
+ 00bb1810 ["CALL", null, ["callee:00ba8ac4:8"]]
- 00bb17cc bytes addcff97
+ 00bb1810 bytes addcff97
- 00bb178c ["INT_ADD", "register:40f0:8", ["const:bb178c:8", "const:4:8"]]
- 00bb178c ["CALL", null, ["callee:00be1570:8"]]
+ 00bb17d0 ["INT_ADD", "register:40f0:8", ["const:bb17d0:8", "const:4:8"]]
+ 00bb17d0 ["CALL", null, ["callee:00be1570:8"]]
- 00bb178c bytes 65bf0094
+ 00bb17d0 bytes 68bf0094
- 00bb17b4 ["INT_ADD", "register:40f0:8", ["const:bb17b4:8", "const:4:8"]]
- 00bb17b4 ["CALL", null, ["callee:0041b298:8"]]
+ 00bb17f8 ["INT_ADD", "register:40f0:8", ["const:bb17f8:8", "const:4:8"]]
+ 00bb17f8 ["CALL", null, ["callee:0041b298:8"]]
- 00bb17b4 bytes b9a6e197
+ 00bb17f8 bytes a8a6e197
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef80d117124b2f0b33dc9e495bc45503"></a>

### [`00bb3e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3e34.md) → [`00bb3e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb3/00bb3e78.md) _ZNSt6__ndk118__time_get_storageIwE4initERKNS_5ctypeIwEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be1cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1cd0.md) · 呼出先 8件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdda00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda00.md) [`00be0f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0f60.md) [`00be1530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1530.md)
- 新版 呼出元 1件 [`00be1d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1d20.md) · 呼出先 8件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdda50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdda50.md) [`00be0fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0fb0.md) [`00be1580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1580.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb3f00",
      "incomplete_value": false,
      "site": "00bb3f08",
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
            "const:100:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb3ebc",
      "incomplete_value": false,
      "site": "00bb3ec4",
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
            "const:75:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb4060",
      "incomplete_value": false,
      "site": "00bb4064",
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
            "const:2b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb401c",
      "incomplete_value": false,
      "site": "00bb4020",
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
            "const:2b9:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00bb41e8",
      "incomplete_value": false,
      "site": "00bb41f0",
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
            "const:2f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb41a4",
      "incomplete_value": false,
      "site": "00bb41ac",
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
            "const:269:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00bb3f00",
      "PARAM",
      [
        "storage",
        "002a2075",
        null,
        null
      ]
    ],
    [
      "00bb4060",
      "PARAM",
      [
        "storage",
        "0029c2b9",
        null,
        null
      ]
    ],
    [
      "00bb41e8",
      "PARAM",
      [
        "storage",
        "0029f269",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00bb3f00",
      "PARAM",
      [
        "storage",
        "002a2100",
        null,
        null
      ]
    ],
    [
      "00bb4060",
      "PARAM",
      [
        "storage",
        "0029c2b7",
        null,
        null
      ]
    ],
    [
      "00bb41e8",
      "PARAM",
      [
        "storage",
        "0029f2f4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb3ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3e34.md#insn-00bb3ec4) · [`00bb4020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3e34.md#insn-00bb4020) · [`00bb41ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb3/00bb3e34.md#insn-00bb41ac)
- 新版 `00bb3f08`（命令位置の公開資料なし） · `00bb4064`（命令位置の公開資料なし） · `00bb41f0`（命令位置の公開資料なし）

~~~diff
- 00bb3ec4 ["INT_ADD", "register:40f0:8", ["const:bb3ec4:8", "const:4:8"]]
- 00bb3ec4 ["CALL", null, ["callee:00be1670:8"]]
+ 00bb3f08 ["INT_ADD", "register:40f0:8", ["const:bb3f08:8", "const:4:8"]]
+ 00bb3f08 ["CALL", null, ["callee:00be1670:8"]]
- 00bb3ec4 bytes d7b50094
+ 00bb3f08 bytes dab50094
- 00bb4020 ["INT_ADD", "register:40f0:8", ["const:bb4020:8", "const:4:8"]]
- 00bb4020 ["CALL", null, ["callee:00be1670:8"]]
+ 00bb4064 ["INT_ADD", "register:40f0:8", ["const:bb4064:8", "const:4:8"]]
+ 00bb4064 ["CALL", null, ["callee:00be1670:8"]]
- 00bb4020 bytes 80b50094
+ 00bb4064 bytes 83b50094
- 00bb41ac ["INT_ADD", "register:40f0:8", ["const:bb41ac:8", "const:4:8"]]
- 00bb41ac ["CALL", null, ["callee:00be1670:8"]]
+ 00bb41f0 ["INT_ADD", "register:40f0:8", ["const:bb41f0:8", "const:4:8"]]
+ 00bb41f0 ["CALL", null, ["callee:00be1670:8"]]
- 00bb41ac bytes 1db50094
+ 00bb41f0 bytes 20b50094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d157256fcf2da0bd7a30c1f9fd19cf1b"></a>

### [`00bb48ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb48ac.md) → [`00bb48f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bb4/00bb48f0.md) _ZNSt6__ndk118__time_get_storageIcEC1EPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md) [`00bdb460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb460.md) [`00bdef40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef40.md) [`00be18e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be18e0.md) [`00be1990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be1/00be1990.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md) [`00bdb4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb4b0.md) [`00bdef90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef90.md) [`00be1930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be1930.md) [`00be19e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be1/00be19e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.65% / 新版 95.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00bb4938",
      "incomplete_value": false,
      "site": "00bb493c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
          ],
          [
            "leaf",
            "const:ef8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00bb48f4",
      "incomplete_value": false,
      "site": "00bb48f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c15000:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00bb4958",
      "incomplete_value": true,
      "site": "00bb495c",
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
      "definition_site": "00bb4914",
      "incomplete_value": true,
      "site": "00bb4918",
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
      "definition_site": "00bb4970",
      "incomplete_value": true,
      "site": "00bb4974",
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
      "definition_site": "00bb492c",
      "incomplete_value": true,
      "site": "00bb4930",
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
      "00bb493c",
      "DATA",
      [
        "storage",
        "00c15ea8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb4950",
      "READ",
      [
        "storage",
        "00c1bf50",
        null,
        "pointer"
      ]
    ],
    [
      "00bb495c",
      "DATA",
      [
        "storage",
        "00c139d8",
        null,
        "undefined1[104]"
      ]
    ]
  ],
  "added": [
    [
      "00bb493c",
      "DATA",
      [
        "storage",
        "00c15ef8",
        null,
        "undefined *"
      ]
    ],
    [
      "00bb4950",
      "READ",
      [
        "storage",
        "00c1bfa0",
        null,
        "pointer"
      ]
    ],
    [
      "00bb495c",
      "DATA",
      [
        "storage",
        "00c13a28",
        null,
        "undefined1[104]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00bb48ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb48ac.md#insn-00bb48ec) · [`00bb48cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb48ac.md#insn-00bb48cc) · [`00bb48dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb4/00bb48ac.md#insn-00bb48dc)
- 新版 `00bb4930`（命令位置の公開資料なし） · `00bb4910`（命令位置の公開資料なし） · `00bb4920`（命令位置の公開資料なし）

~~~diff
- 00bb48ec ["INT_ADD", "register:40f0:8", ["const:bb48ec:8", "const:4:8"]]
- 00bb48ec ["CALL", null, ["callee:00be19e0:8"]]
+ 00bb4930 ["INT_ADD", "register:40f0:8", ["const:bb4930:8", "const:4:8"]]
+ 00bb4930 ["CALL", null, ["callee:00be19e0:8"]]
- 00bb48ec bytes 29b40094
+ 00bb4930 bytes 2cb40094
- 00bb48cc ["INT_ADD", "register:40f0:8", ["const:bb48cc:8", "const:4:8"]]
- 00bb48cc ["CALL", null, ["callee:00be1cc0:8"]]
+ 00bb4910 ["INT_ADD", "register:40f0:8", ["const:bb4910:8", "const:4:8"]]
+ 00bb4910 ["CALL", null, ["callee:00be1cc0:8"]]
- 00bb48cc bytes e9b40094
+ 00bb4910 bytes ecb40094
- 00bb48dc ["INT_ADD", "register:40f0:8", ["const:bb48dc:8", "const:4:8"]]
- 00bb48dc ["CALL", null, ["callee:00bdb240:8"]]
+ 00bb4920 ["INT_ADD", "register:40f0:8", ["const:bb4920:8", "const:4:8"]]
+ 00bb4920 ["CALL", null, ["callee:00bdb240:8"]]
- 00bb48dc bytes 459a0094
+ 00bb4920 bytes 489a0094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

