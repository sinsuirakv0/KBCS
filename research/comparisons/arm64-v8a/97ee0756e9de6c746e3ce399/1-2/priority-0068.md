# v15.7.3 → v15.7.4 · 最優先の変更候補 (68)

[一覧の目次](README.md)

<a id="compare-d5ebe61916b00c9c848e4cbdd05e7751"></a>

### [`00b48d48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48d48.md) → [`00b48d8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48d8c.md) _ZN8firebase9messaging11HasListenerEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be02e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02e0.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00be0330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0330.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48da0",
      "incomplete_value": false,
      "site": "00b48da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48d5c",
      "incomplete_value": false,
      "site": "00b48d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "00b48da0",
      "PARAM",
      [
        "storage",
        "010a0f20",
        null,
        null
      ]
    ],
    [
      "00b48dac",
      "READ",
      [
        "storage",
        "010a0f48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48db0",
      "PARAM",
      [
        "storage",
        "010a0f20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b48da0",
      "PARAM",
      [
        "storage",
        "010a0f60",
        null,
        null
      ]
    ],
    [
      "00b48dac",
      "READ",
      [
        "storage",
        "010a0f88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48db0",
      "PARAM",
      [
        "storage",
        "010a0f60",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48d48.md#insn-00b48d60) · [`00b48d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48d48.md#insn-00b48d58) · [`00b48d68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48d48.md#insn-00b48d68)
- 新版 `00b48da4`（命令位置の公開資料なし） · `00b48d9c`（命令位置の公開資料なし） · `00b48dac`（命令位置の公開資料なし）

~~~diff
- 00b48d60 ["INT_ADD", "register:40f0:8", ["const:b48d60:8", "const:4:8"]]
- 00b48d60 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b48da4 ["INT_ADD", "register:40f0:8", ["const:b48da4:8", "const:4:8"]]
+ 00b48da4 ["CALL", null, ["callee:00bddc20:8"]]
- 00b48d60 bytes 9c530294
+ 00b48da4 bytes 9f530294
- 00b48d58 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00b48d58 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00b48d58 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00b48d58 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00b48d9c ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00b48d9c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00b48d9c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00b48d9c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00b48d58 bytes 73823c91
+ 00b48d9c bytes 73823d91
- 00b48d68 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f48:8"]]
- 00b48d68 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48dac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f88:8"]]
+ 00b48dac ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48d68 bytes 14a547f9
+ 00b48dac bytes 14c547f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba40e0840194e1eb6fd6a6a3ae046cce"></a>

### [`00b48da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48da0.md) → [`00b48de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48de4.md) _ZN8firebase9messaging23NotifyListenerOnMessageERKNS0_7MessageE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be03a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03a0.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00be03f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be03f0.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

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
      "definition_site": "00b48e08",
      "incomplete_value": true,
      "site": "00b48e08",
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
      "definition_site": "00b48dc4",
      "incomplete_value": true,
      "site": "00b48dc4",
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
      "definition_site": "00b48df8",
      "incomplete_value": false,
      "site": "00b48dfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48db4",
      "incomplete_value": false,
      "site": "00b48db8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "definition_site": "00b48e20",
      "incomplete_value": false,
      "site": "00b48e24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:f60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48ddc",
      "incomplete_value": false,
      "site": "00b48de0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:f20:8"
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
      "00b48df8",
      "PARAM",
      [
        "storage",
        "010a0f20",
        null,
        null
      ]
    ],
    [
      "00b48e04",
      "READ",
      [
        "storage",
        "010a0f48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48e20",
      "PARAM",
      [
        "storage",
        "010a0f20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b48df8",
      "PARAM",
      [
        "storage",
        "010a0f60",
        null,
        null
      ]
    ],
    [
      "00b48e04",
      "READ",
      [
        "storage",
        "010a0f88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48e20",
      "PARAM",
      [
        "storage",
        "010a0f60",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48da0.md#insn-00b48db8) · [`00b48de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48da0.md#insn-00b48de0) · [`00b48db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48da0.md#insn-00b48db4)
- 新版 `00b48dfc`（命令位置の公開資料なし） · `00b48e24`（命令位置の公開資料なし） · `00b48df8`（命令位置の公開資料なし）

~~~diff
- 00b48db8 ["INT_ADD", "register:40f0:8", ["const:b48db8:8", "const:4:8"]]
- 00b48db8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b48dfc ["INT_ADD", "register:40f0:8", ["const:b48dfc:8", "const:4:8"]]
+ 00b48dfc ["CALL", null, ["callee:00bddc20:8"]]
- 00b48db8 bytes 86530294
+ 00b48dfc bytes 89530294
- 00b48de0 ["INT_ADD", "register:40f0:8", ["const:b48de0:8", "const:4:8"]]
- 00b48de0 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b48e24 ["INT_ADD", "register:40f0:8", ["const:b48e24:8", "const:4:8"]]
+ 00b48e24 ["CALL", null, ["callee:00bddc30:8"]]
- 00b48de0 bytes 80530294
+ 00b48e24 bytes 83530294
- 00b48db4 ["COPY", "tmp:0:8", ["const:f20:8"]]
- 00b48db4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b48db4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b48db4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b48df8 ["COPY", "tmp:0:8", ["const:f60:8"]]
+ 00b48df8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48df8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48df8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b48db4 bytes 00803c91
+ 00b48df8 bytes 00803d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-829f08c7f06dbf66e5e37774bd709b5c"></a>

### [`00b48e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48e10.md) → [`00b48e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48e54.md) _ZN8firebase9messaging29NotifyListenerOnTokenReceivedEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be03b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03b0.md) · 呼出先 8件 [`0041e0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0041e/0041e0fc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md)
- 新版 呼出元 1件 [`00be0400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0400.md) · 呼出先 8件 [`0041e0fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0041e/0041e0fc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 90.62% / 新版 90.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 4件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48ee4",
      "incomplete_value": true,
      "site": "00b48ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:f90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48ea0",
      "incomplete_value": true,
      "site": "00b48ea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:f50:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48f28",
      "incomplete_value": false,
      "site": "00b48f28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48ee4",
      "incomplete_value": false,
      "site": "00b48ee4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:f58:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48e7c",
      "incomplete_value": true,
      "site": "00b48e7c",
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
      "definition_site": "00b48e38",
      "incomplete_value": true,
      "site": "00b48e38",
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
      "00b48e6c",
      "PARAM",
      [
        "storage",
        "010a0f20",
        null,
        null
      ]
    ],
    [
      "00b48e78",
      "READ",
      [
        "storage",
        "010a0f50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48ee4",
      "WRITE",
      [
        "storage",
        "010a0f50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48e6c",
      "PARAM",
      [
        "storage",
        "010a0f60",
        null,
        null
      ]
    ],
    [
      "00b48e78",
      "READ",
      [
        "storage",
        "010a0f90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48ee4",
      "WRITE",
      [
        "storage",
        "010a0f90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48e10.md#insn-00b48e2c) · [`00b48e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48e10.md#insn-00b48e80) · [`00b48ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48e10.md#insn-00b48ea0)
- 新版 `00b48e70`（命令位置の公開資料なし） · `00b48ec4`（命令位置の公開資料なし） · `00b48ee4`（命令位置の公開資料なし）

~~~diff
- 00b48e2c ["INT_ADD", "register:40f0:8", ["const:b48e2c:8", "const:4:8"]]
- 00b48e2c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b48e70 ["INT_ADD", "register:40f0:8", ["const:b48e70:8", "const:4:8"]]
+ 00b48e70 ["CALL", null, ["callee:00bddc20:8"]]
- 00b48e2c bytes 69530294
+ 00b48e70 bytes 6c530294
- 00b48e80 ["INT_ADD", "register:40f0:8", ["const:b48e80:8", "const:4:8"]]
- 00b48e80 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b48ec4 ["INT_ADD", "register:40f0:8", ["const:b48ec4:8", "const:4:8"]]
+ 00b48ec4 ["CALL", null, ["callee:00bdb200:8"]]
- 00b48e80 bytes cc480294
+ 00b48ec4 bytes cf480294
- 00b48ea0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f50:8"]]
- 00b48ea0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48ee4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f90:8"]]
+ 00b48ee4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48ea0 bytes a0aa07f9
+ 00b48ee4 bytes a0ca07f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63fa233713fc5fadc67ef63ae2f18e08"></a>

### [`00b48fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48fb8.md) → [`00b48ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48ffc.md) _ZN8firebase9messaging16PollableListenerD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0330.md) · 呼出先 4件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md) [`00bddc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc20.md) [`00be0440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0440.md)
- 新版 呼出元 1件 [`00be0380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0380.md) · 呼出先 4件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc50.md) [`00bddc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc70.md) [`00be0490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0490.md)

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
      "definition_site": "00b49020",
      "incomplete_value": true,
      "site": "00b49024",
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
      "definition_site": "00b48fdc",
      "incomplete_value": true,
      "site": "00b48fe0",
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
      "00b49018",
      "READ",
      [
        "storage",
        "00c1ba90",
        null,
        "pointer"
      ]
    ],
    [
      "00b49024",
      "DATA",
      [
        "storage",
        "00c11510",
        null,
        "undefined1[48]"
      ]
    ]
  ],
  "added": [
    [
      "00b49018",
      "READ",
      [
        "storage",
        "00c1bae0",
        null,
        "pointer"
      ]
    ],
    [
      "00b49024",
      "DATA",
      [
        "storage",
        "00c11560",
        null,
        "undefined1[48]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48fb8.md#insn-00b48fd4) · [`00b48ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48fb8.md#insn-00b48ff0) · [`00b49004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48fb8.md#insn-00b49004)
- 新版 `00b49018`（命令位置の公開資料なし） · `00b49034`（命令位置の公開資料なし） · `00b49048`（命令位置の公開資料なし）

~~~diff
- 00b48fd4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a90:8"]]
- 00b48fd4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49018 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ae0:8"]]
+ 00b49018 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48fd4 bytes 084945f9
+ 00b49018 bytes 087145f9
- 00b48ff0 ["INT_ADD", "register:40f0:8", ["const:b48ff0:8", "const:4:8"]]
- 00b48ff0 ["CALL", null, ["callee:00be0490:8"]]
+ 00b49034 ["INT_ADD", "register:40f0:8", ["const:b49034:8", "const:4:8"]]
+ 00b49034 ["CALL", null, ["callee:00be0490:8"]]
- 00b48ff0 bytes 145d0294
+ 00b49034 bytes 175d0294
- 00b49004 ["INT_ADD", "register:40f0:8", ["const:b49004:8", "const:4:8"]]
- 00b49004 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b49048 ["INT_ADD", "register:40f0:8", ["const:b49048:8", "const:4:8"]]
+ 00b49048 ["CALL", null, ["callee:00bdb060:8"]]
- 00b49004 bytes 03480294
+ 00b49048 bytes 06480294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1574b7357213b696bf57dbccabe84da"></a>

### [`00b4a204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md) → [`00b4a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md) _ZNSt6__ndk15dequeIN8firebase9messaging7MessageENS_9allocatorIS3_EEE19__add_back_capacityEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0490.md) · 呼出先 9件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00b4a418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a418.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00be04e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04e0.md) · 呼出先 9件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00b4a45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a45c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.09% / 新版 99.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a3f8",
      "incomplete_value": false,
      "site": "00b4a3fc",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a3b4",
      "incomplete_value": false,
      "site": "00b4a3b8",
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
            "const:87d:8"
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
      "00b4a3f8",
      "PARAM",
      [
        "storage",
        "0029887d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4a3f8",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md#insn-00b4a3b8) · [`00b4a250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md#insn-00b4a250) · [`00b4a2a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md#insn-00b4a2a4)
- 新版 `00b4a3fc`（命令位置の公開資料なし） · `00b4a294`（命令位置の公開資料なし） · `00b4a2e8`（命令位置の公開資料なし）

~~~diff
- 00b4a3b8 ["INT_ADD", "register:40f0:8", ["const:b4a3b8:8", "const:4:8"]]
- 00b4a3b8 ["CALL", null, ["callee:00ae04c0:8"]]
+ 00b4a3fc ["INT_ADD", "register:40f0:8", ["const:b4a3fc:8", "const:4:8"]]
+ 00b4a3fc ["CALL", null, ["callee:00ae04c0:8"]]
- 00b4a3b8 bytes 3158fe97
+ 00b4a3fc bytes 3158fe97
- 00b4a250 ["INT_ADD", "register:40f0:8", ["const:b4a250:8", "const:4:8"]]
- 00b4a250 ["CALL", null, ["callee:00b4a45c:8"]]
+ 00b4a294 ["INT_ADD", "register:40f0:8", ["const:b4a294:8", "const:4:8"]]
+ 00b4a294 ["CALL", null, ["callee:00b4a45c:8"]]
- 00b4a250 bytes 72000094
+ 00b4a294 bytes 72000094
- 00b4a2a4 ["INT_ADD", "register:40f0:8", ["const:b4a2a4:8", "const:4:8"]]
- 00b4a2a4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b4a2e8 ["INT_ADD", "register:40f0:8", ["const:b4a2e8:8", "const:4:8"]]
+ 00b4a2e8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b4a2a4 bytes 53430294
+ 00b4a2e8 bytes 56430294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c6de9ebad7a674e2d7c169cbb4a031b"></a>

### [`00b4a418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a418.md) → [`00b4a45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a45c.md) FUN_00b4a45c

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b4a204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a204.md) · 呼出先 4件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00b4a248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a248.md) · 呼出先 4件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a594",
      "incomplete_value": true,
      "site": "00b4a598",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a550",
      "incomplete_value": true,
      "site": "00b4a554",
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
            "const:87d:8"
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
      "00b4a594",
      "PARAM",
      [
        "storage",
        "0029887d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4a594",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a418.md#insn-00b4a554) · [`00b4a484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a418.md#insn-00b4a484) · [`00b4a4bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a418.md#insn-00b4a4bc)
- 新版 `00b4a598`（命令位置の公開資料なし） · `00b4a4c8`（命令位置の公開資料なし） · `00b4a500`（命令位置の公開資料なし）

~~~diff
- 00b4a554 ["INT_ADD", "register:40f0:8", ["const:b4a554:8", "const:4:8"]]
- 00b4a554 ["CALL", null, ["callee:00ae04c0:8"]]
+ 00b4a598 ["INT_ADD", "register:40f0:8", ["const:b4a598:8", "const:4:8"]]
+ 00b4a598 ["CALL", null, ["callee:00ae04c0:8"]]
- 00b4a554 bytes ca57fe97
+ 00b4a598 bytes ca57fe97
- 00b4a484 ["INT_ADD", "register:40f0:8", ["const:b4a484:8", "const:4:8"]]
- 00b4a484 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b4a4c8 ["INT_ADD", "register:40f0:8", ["const:b4a4c8:8", "const:4:8"]]
+ 00b4a4c8 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b4a484 bytes 07430294
+ 00b4a4c8 bytes 0a430294
- 00b4a4bc ["INT_ADD", "register:40f0:8", ["const:b4a4bc:8", "const:4:8"]]
- 00b4a4bc ["CALL", null, ["callee:00bdb040:8"]]
+ 00b4a500 ["INT_ADD", "register:40f0:8", ["const:b4a500:8", "const:4:8"]]
+ 00b4a500 ["CALL", null, ["callee:00bdb040:8"]]
- 00b4a4bc bytes cd420294
+ 00b4a500 bytes d0420294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dd4cceb5b9470fe1d4cbc26a7779c30"></a>

### [`00b4a558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a558.md) → [`00b4a59c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a59c.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageENS_9allocatorIS4_EEE9push_backEOS4_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0460.md) · 呼出先 4件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00be04b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04b0.md) · 呼出先 4件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a6d4",
      "incomplete_value": true,
      "site": "00b4a6d8",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a690",
      "incomplete_value": true,
      "site": "00b4a694",
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
            "const:87d:8"
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
      "00b4a6d4",
      "PARAM",
      [
        "storage",
        "0029887d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4a6d4",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a558.md#insn-00b4a694) · [`00b4a5c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a558.md#insn-00b4a5c4) · [`00b4a5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a558.md#insn-00b4a5fc)
- 新版 `00b4a6d8`（命令位置の公開資料なし） · `00b4a608`（命令位置の公開資料なし） · `00b4a640`（命令位置の公開資料なし）

~~~diff
- 00b4a694 ["INT_ADD", "register:40f0:8", ["const:b4a694:8", "const:4:8"]]
- 00b4a694 ["CALL", null, ["callee:00ae04c0:8"]]
+ 00b4a6d8 ["INT_ADD", "register:40f0:8", ["const:b4a6d8:8", "const:4:8"]]
+ 00b4a6d8 ["CALL", null, ["callee:00ae04c0:8"]]
- 00b4a694 bytes 7a57fe97
+ 00b4a6d8 bytes 7a57fe97
- 00b4a5c4 ["INT_ADD", "register:40f0:8", ["const:b4a5c4:8", "const:4:8"]]
- 00b4a5c4 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b4a608 ["INT_ADD", "register:40f0:8", ["const:b4a608:8", "const:4:8"]]
+ 00b4a608 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b4a5c4 bytes b7420294
+ 00b4a608 bytes ba420294
- 00b4a5fc ["INT_ADD", "register:40f0:8", ["const:b4a5fc:8", "const:4:8"]]
- 00b4a5fc ["CALL", null, ["callee:00bdb040:8"]]
+ 00b4a640 ["INT_ADD", "register:40f0:8", ["const:b4a640:8", "const:4:8"]]
+ 00b4a640 ["CALL", null, ["callee:00bdb040:8"]]
- 00b4a5fc bytes 7d420294
+ 00b4a640 bytes 80420294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d3638e05b1c0540ed8c6add376ec5ae"></a>

### [`00b4a698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a698.md) → [`00b4a6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a6dc.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageENS_9allocatorIS4_EEE10push_frontEOS4_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0450.md) · 呼出先 4件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00be04a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04a0.md) · 呼出先 4件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a814",
      "incomplete_value": false,
      "site": "00b4a818",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a7d0",
      "incomplete_value": false,
      "site": "00b4a7d4",
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
            "const:87d:8"
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
      "00b4a814",
      "PARAM",
      [
        "storage",
        "0029887d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4a814",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a698.md#insn-00b4a7d4) · [`00b4a708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a698.md#insn-00b4a708) · [`00b4a740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a698.md#insn-00b4a740)
- 新版 `00b4a818`（命令位置の公開資料なし） · `00b4a74c`（命令位置の公開資料なし） · `00b4a784`（命令位置の公開資料なし）

~~~diff
- 00b4a7d4 ["INT_ADD", "register:40f0:8", ["const:b4a7d4:8", "const:4:8"]]
- 00b4a7d4 ["CALL", null, ["callee:00ae04c0:8"]]
+ 00b4a818 ["INT_ADD", "register:40f0:8", ["const:b4a818:8", "const:4:8"]]
+ 00b4a818 ["CALL", null, ["callee:00ae04c0:8"]]
- 00b4a7d4 bytes 2a57fe97
+ 00b4a818 bytes 2a57fe97
- 00b4a708 ["INT_ADD", "register:40f0:8", ["const:b4a708:8", "const:4:8"]]
- 00b4a708 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b4a74c ["INT_ADD", "register:40f0:8", ["const:b4a74c:8", "const:4:8"]]
+ 00b4a74c ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b4a708 bytes 66420294
+ 00b4a74c bytes 69420294
- 00b4a740 ["INT_ADD", "register:40f0:8", ["const:b4a740:8", "const:4:8"]]
- 00b4a740 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b4a784 ["INT_ADD", "register:40f0:8", ["const:b4a784:8", "const:4:8"]]
+ 00b4a784 ["CALL", null, ["callee:00bdb040:8"]]
- 00b4a740 bytes 2c420294
+ 00b4a784 bytes 2f420294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-793bb063deeecc5b7768fba9ea88303b"></a>

### [`00b4a7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a7d8.md) → [`00b4a81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a81c.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageERNS_9allocatorIS4_EEE9push_backEOS4_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0480.md) · 呼出先 4件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00be04d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04d0.md) · 呼出先 4件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a954",
      "incomplete_value": false,
      "site": "00b4a958",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a910",
      "incomplete_value": false,
      "site": "00b4a914",
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
            "const:87d:8"
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
      "00b4a954",
      "PARAM",
      [
        "storage",
        "0029887d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4a954",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a7d8.md#insn-00b4a914) · [`00b4a844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a7d8.md#insn-00b4a844) · [`00b4a87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a7d8.md#insn-00b4a87c)
- 新版 `00b4a958`（命令位置の公開資料なし） · `00b4a888`（命令位置の公開資料なし） · `00b4a8c0`（命令位置の公開資料なし）

~~~diff
- 00b4a914 ["INT_ADD", "register:40f0:8", ["const:b4a914:8", "const:4:8"]]
- 00b4a914 ["CALL", null, ["callee:00ae04c0:8"]]
+ 00b4a958 ["INT_ADD", "register:40f0:8", ["const:b4a958:8", "const:4:8"]]
+ 00b4a958 ["CALL", null, ["callee:00ae04c0:8"]]
- 00b4a914 bytes da56fe97
+ 00b4a958 bytes da56fe97
- 00b4a844 ["INT_ADD", "register:40f0:8", ["const:b4a844:8", "const:4:8"]]
- 00b4a844 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b4a888 ["INT_ADD", "register:40f0:8", ["const:b4a888:8", "const:4:8"]]
+ 00b4a888 ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b4a844 bytes 17420294
+ 00b4a888 bytes 1a420294
- 00b4a87c ["INT_ADD", "register:40f0:8", ["const:b4a87c:8", "const:4:8"]]
- 00b4a87c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b4a8c0 ["INT_ADD", "register:40f0:8", ["const:b4a8c0:8", "const:4:8"]]
+ 00b4a8c0 ["CALL", null, ["callee:00bdb040:8"]]
- 00b4a87c bytes dd410294
+ 00b4a8c0 bytes e0410294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05ec22bb8275d60b6325340386ea5431"></a>

### [`00b4a918`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a918.md) → [`00b4a95c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4a95c.md) _ZNSt6__ndk114__split_bufferIPN8firebase9messaging7MessageERNS_9allocatorIS4_EEE10push_frontERKS4_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0470.md) · 呼出先 4件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md)
- 新版 呼出元 1件 [`00be04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be04c0.md) · 呼出先 4件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.75% / 新版 98.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4aa94",
      "incomplete_value": false,
      "site": "00b4aa98",
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
            "const:7f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aa50",
      "incomplete_value": false,
      "site": "00b4aa54",
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
            "const:87d:8"
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
      "00b4aa94",
      "PARAM",
      [
        "storage",
        "0029887d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4aa94",
      "PARAM",
      [
        "storage",
        "002987f0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aa54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a918.md#insn-00b4aa54) · [`00b4a988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a918.md#insn-00b4a988) · [`00b4a9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4a918.md#insn-00b4a9c0)
- 新版 `00b4aa98`（命令位置の公開資料なし） · `00b4a9cc`（命令位置の公開資料なし） · `00b4aa04`（命令位置の公開資料なし）

~~~diff
- 00b4aa54 ["INT_ADD", "register:40f0:8", ["const:b4aa54:8", "const:4:8"]]
- 00b4aa54 ["CALL", null, ["callee:00ae04c0:8"]]
+ 00b4aa98 ["INT_ADD", "register:40f0:8", ["const:b4aa98:8", "const:4:8"]]
+ 00b4aa98 ["CALL", null, ["callee:00ae04c0:8"]]
- 00b4aa54 bytes 8a56fe97
+ 00b4aa98 bytes 8a56fe97
- 00b4a988 ["INT_ADD", "register:40f0:8", ["const:b4a988:8", "const:4:8"]]
- 00b4a988 ["CALL", null, ["callee:00bdb0f0:8"]]
+ 00b4a9cc ["INT_ADD", "register:40f0:8", ["const:b4a9cc:8", "const:4:8"]]
+ 00b4a9cc ["CALL", null, ["callee:00bdb0f0:8"]]
- 00b4a988 bytes c6410294
+ 00b4a9cc bytes c9410294
- 00b4a9c0 ["INT_ADD", "register:40f0:8", ["const:b4a9c0:8", "const:4:8"]]
- 00b4a9c0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b4aa04 ["INT_ADD", "register:40f0:8", ["const:b4aa04:8", "const:4:8"]]
+ 00b4aa04 ["CALL", null, ["callee:00bdb040:8"]]
- 00b4a9c0 bytes 8c410294
+ 00b4aa04 bytes 8f410294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04b045167d0c1144bf09d3246cbda770"></a>

### [`00b4aa58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aa58.md) → [`00b4aa9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4aa9c.md) _INIT_276

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 6件 [`00b0544c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0544c.md) [`00b48b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48b50.md) [`00b48b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48b90.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bddd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd10.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00b05490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05490.md) [`00b48b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48b94.md) [`00b48bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48bd4.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bddd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd60.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 4件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4aac8",
      "incomplete_value": true,
      "site": "00b4aac8",
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
            "const:f40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aa84",
      "incomplete_value": true,
      "site": "00b4aa84",
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
            "const:f00:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4aac8",
      "incomplete_value": true,
      "site": "00b4aac8",
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:f40:8"
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
      "definition_site": "00b4aa84",
      "incomplete_value": true,
      "site": "00b4aa84",
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
                "register:4000:8"
              ],
              [
                "leaf",
                "const:f00:8"
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b4aac8",
      "incomplete_value": true,
      "site": "00b4aac8",
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
            "const:b94:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aa84",
      "incomplete_value": true,
      "site": "00b4aa84",
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
            "const:b50:8"
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
      "00b4aab8",
      "PARAM",
      [
        "storage",
        "010a0f00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aac8",
      "WRITE",
      [
        "storage",
        "010a0f00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aac8",
      "WRITE",
      [
        "storage",
        "010a0f08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aab8",
      "PARAM",
      [
        "storage",
        "010a0f40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aac8",
      "WRITE",
      [
        "storage",
        "010a0f40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aac8",
      "WRITE",
      [
        "storage",
        "010a0f48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aa90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aa58.md#insn-00b4aa90) · [`00b4aaa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aa58.md#insn-00b4aaa4) · [`00b4aa74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aa58.md#insn-00b4aa74)
- 新版 `00b4aad4`（命令位置の公開資料なし） · `00b4aae8`（命令位置の公開資料なし） · `00b4aab8`（命令位置の公開資料なし）

~~~diff
- 00b4aa90 ["INT_ADD", "register:40f0:8", ["const:b4aa90:8", "const:4:8"]]
- 00b4aa90 ["CALL", null, ["callee:00bddd60:8"]]
+ 00b4aad4 ["INT_ADD", "register:40f0:8", ["const:b4aad4:8", "const:4:8"]]
+ 00b4aad4 ["CALL", null, ["callee:00bddd60:8"]]
- 00b4aa90 bytes a04c0294
+ 00b4aad4 bytes a34c0294
- 00b4aaa4 ["INT_ADD", "register:40f0:8", ["const:b4aaa4:8", "const:4:8"]]
- 00b4aaa4 ["CALL", null, ["callee:00bdde20:8"]]
+ 00b4aae8 ["INT_ADD", "register:40f0:8", ["const:b4aae8:8", "const:4:8"]]
+ 00b4aae8 ["CALL", null, ["callee:00bdde20:8"]]
- 00b4aaa4 bytes cb4c0294
+ 00b4aae8 bytes ce4c0294
- 00b4aa74 ["COPY", "tmp:0:8", ["const:f00:8"]]
- 00b4aa74 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4aa74 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4aa74 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4aab8 ["COPY", "tmp:0:8", ["const:f40:8"]]
+ 00b4aab8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4aab8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4aab8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4aa74 bytes 00003c91
+ 00b4aab8 bytes 00003d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcf493090af2396e81792c7beb87588a"></a>

### [`00b4aad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aad0.md) → [`00b4ab14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ab14.md) _ZN8firebase9messaging18firebase_messaging19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 81.25% / 新版 81.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4ab40",
      "incomplete_value": true,
      "site": "00b4ab40",
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
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aafc",
      "incomplete_value": true,
      "site": "00b4aafc",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4ab28",
      "incomplete_value": true,
      "site": "00b4ab28",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4aae4",
      "incomplete_value": true,
      "site": "00b4aae4",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b4aae4"
      ],
      [
        "FALL_THROUGH",
        "00b4ab28"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b4ab28",
      "incomplete_value": true,
      "site": "00b4ab40",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4aae4",
      "incomplete_value": true,
      "site": "00b4aafc",
      "value": [
        "INT_NOTEQUAL",
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
      "00b4ab24",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab40",
      "WRITE",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ab24",
      "READ",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab40",
      "WRITE",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aad0.md#insn-00b4aafc) · [`00b4aae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aad0.md#insn-00b4aae0) · [`00b4aaf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aad0.md#insn-00b4aaf4)
- 新版 `00b4ab40`（命令位置の公開資料なし） · `00b4ab24`（命令位置の公開資料なし） · `00b4ab38`（命令位置の公開資料なし）

~~~diff
- 00b4aafc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fb8:8"]]
- 00b4aafc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ab40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ff8:8"]]
+ 00b4ab40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4aafc bytes 60de07f9
+ 00b4ab40 bytes 60fe07f9
- 00b4aae0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fb8:8"]]
- 00b4aae0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ab24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ff8:8"]]
+ 00b4ab24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4aae0 bytes 68de47f9
+ 00b4ab24 bytes 68fe47f9
- 00b4aaf4 ["INT_ADD", "register:40f0:8", ["const:b4aaf4:8", "const:4:8"]]
- 00b4aaf4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b4ab38 ["INT_ADD", "register:40f0:8", ["const:b4ab38:8", "const:4:8"]]
+ 00b4ab38 ["CALL", null, ["callee:00bde090:8"]]
- 00b4aaf4 bytes 534d0294
+ 00b4ab38 bytes 564d0294
~~~


<a id="compare-6d4201b44fde8eadbf933ab9e541f068"></a>

### [`00b4ab10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab10.md) → [`00b4ab54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ab54.md) _ZN8firebase9messaging18firebase_messaging19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4ab80",
      "incomplete_value": true,
      "site": "00b4ab80",
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
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ab3c",
      "incomplete_value": true,
      "site": "00b4ab3c",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4ab68",
      "incomplete_value": true,
      "site": "00b4ab68",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4ab24",
      "incomplete_value": true,
      "site": "00b4ab24",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b4ab24"
      ],
      [
        "FALL_THROUGH",
        "00b4ab68"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b4ab68",
      "incomplete_value": true,
      "site": "00b4ab80",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4ab24",
      "incomplete_value": true,
      "site": "00b4ab3c",
      "value": [
        "INT_NOTEQUAL",
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
      "00b4ab64",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab80",
      "WRITE",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ab64",
      "READ",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab80",
      "WRITE",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ab3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab10.md#insn-00b4ab3c) · [`00b4ab20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab10.md#insn-00b4ab20) · [`00b4ab34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab10.md#insn-00b4ab34)
- 新版 `00b4ab80`（命令位置の公開資料なし） · `00b4ab64`（命令位置の公開資料なし） · `00b4ab78`（命令位置の公開資料なし）

~~~diff
- 00b4ab3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fb8:8"]]
- 00b4ab3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ab80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ff8:8"]]
+ 00b4ab80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ab3c bytes 60de07f9
+ 00b4ab80 bytes 60fe07f9
- 00b4ab20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fb8:8"]]
- 00b4ab20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ab64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ff8:8"]]
+ 00b4ab64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ab20 bytes 68de47f9
+ 00b4ab64 bytes 68fe47f9
- 00b4ab34 ["INT_ADD", "register:40f0:8", ["const:b4ab34:8", "const:4:8"]]
- 00b4ab34 ["CALL", null, ["callee:00bde090:8"]]
+ 00b4ab78 ["INT_ADD", "register:40f0:8", ["const:b4ab78:8", "const:4:8"]]
+ 00b4ab78 ["CALL", null, ["callee:00bde090:8"]]
- 00b4ab34 bytes 434d0294
+ 00b4ab78 bytes 464d0294
~~~


<a id="compare-ff69b4f0a235800dcb51fbfd45bc461e"></a>

### [`00b4ab50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab50.md) → [`00b4ab94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ab94.md) _ZN8firebase9messaging18firebase_messaging10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4abc4",
      "incomplete_value": true,
      "site": "00b4abc4",
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
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ab80",
      "incomplete_value": true,
      "site": "00b4ab80",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4aba8",
      "incomplete_value": true,
      "site": "00b4aba8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4ab64",
      "incomplete_value": true,
      "site": "00b4ab64",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b4ab64"
      ],
      [
        "FALL_THROUGH",
        "00b4aba8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b4aba8",
      "incomplete_value": true,
      "site": "00b4abc4",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4ab64",
      "incomplete_value": true,
      "site": "00b4ab80",
      "value": [
        "INT_NOTEQUAL",
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
      "00b4aba4",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4abc4",
      "WRITE",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aba4",
      "READ",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4abc4",
      "WRITE",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ab80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab50.md#insn-00b4ab80) · [`00b4ab60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab50.md#insn-00b4ab60) · [`00b4ab78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab50.md#insn-00b4ab78)
- 新版 `00b4abc4`（命令位置の公開資料なし） · `00b4aba4`（命令位置の公開資料なし） · `00b4abbc`（命令位置の公開資料なし）

~~~diff
- 00b4ab80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fb8:8"]]
- 00b4ab80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4abc4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ff8:8"]]
+ 00b4abc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ab80 bytes 60de07f9
+ 00b4abc4 bytes 60fe07f9
- 00b4ab60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fb8:8"]]
- 00b4ab60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4aba4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ff8:8"]]
+ 00b4aba4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ab60 bytes 68de47f9
+ 00b4aba4 bytes 68fe47f9
- 00b4ab78 ["INT_ADD", "register:40f0:8", ["const:b4ab78:8", "const:4:8"]]
- 00b4ab78 ["CALL", null, ["callee:00bde090:8"]]
+ 00b4abbc ["INT_ADD", "register:40f0:8", ["const:b4abbc:8", "const:4:8"]]
+ 00b4abbc ["CALL", null, ["callee:00bde090:8"]]
- 00b4ab78 bytes 324d0294
+ 00b4abbc bytes 354d0294
~~~


<a id="compare-da2d702dc1bfa54f9878aa690feea5ea"></a>

### [`00b4ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab94.md) → [`00b4abd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4abd8.md) _ZN8firebase9messaging18firebase_messaging10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4ac08",
      "incomplete_value": true,
      "site": "00b4ac08",
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
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4abc4",
      "incomplete_value": true,
      "site": "00b4abc4",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4abec",
      "incomplete_value": true,
      "site": "00b4abec",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4aba8",
      "incomplete_value": true,
      "site": "00b4aba8",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b4aba8"
      ],
      [
        "FALL_THROUGH",
        "00b4abec"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b4abec",
      "incomplete_value": true,
      "site": "00b4ac08",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4aba8",
      "incomplete_value": true,
      "site": "00b4abc4",
      "value": [
        "INT_NOTEQUAL",
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
      "00b4abe8",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac08",
      "WRITE",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4abe8",
      "READ",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac08",
      "WRITE",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4abc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab94.md#insn-00b4abc4) · [`00b4aba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab94.md#insn-00b4aba4) · [`00b4abbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ab94.md#insn-00b4abbc)
- 新版 `00b4ac08`（命令位置の公開資料なし） · `00b4abe8`（命令位置の公開資料なし） · `00b4ac00`（命令位置の公開資料なし）

~~~diff
- 00b4abc4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fb8:8"]]
- 00b4abc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ac08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ff8:8"]]
+ 00b4ac08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4abc4 bytes 60de07f9
+ 00b4ac08 bytes 60fe07f9
- 00b4aba4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:fb8:8"]]
- 00b4aba4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4abe8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ff8:8"]]
+ 00b4abe8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4aba4 bytes 68de47f9
+ 00b4abe8 bytes 68fe47f9
- 00b4abbc ["INT_ADD", "register:40f0:8", ["const:b4abbc:8", "const:4:8"]]
- 00b4abbc ["CALL", null, ["callee:00bde090:8"]]
+ 00b4ac00 ["INT_ADD", "register:40f0:8", ["const:b4ac00:8", "const:4:8"]]
+ 00b4ac00 ["CALL", null, ["callee:00bde090:8"]]
- 00b4abbc bytes 214d0294
+ 00b4ac00 bytes 244d0294
~~~


<a id="compare-0e609423ae134c00c063b5a0fea67c44"></a>

### [`00b4abe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4abe4.md) → [`00b4ac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ac28.md) _ZN8firebase9messaging18firebase_messaging15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4ac80",
      "incomplete_value": true,
      "site": "00b4ac80",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": {
      "definition_site": "00b4ac3c",
      "incomplete_value": true,
      "site": "00b4ac3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:fc0:8"
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
      "00b4ac3c",
      "READ",
      [
        "storage",
        "010a0fc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ac5c",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac80",
      "WRITE",
      [
        "storage",
        "010a0fc0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4ac3c",
      "READ",
      [
        "storage",
        "010a1000",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ac5c",
      "READ",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac80",
      "WRITE",
      [
        "storage",
        "010a1000",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4abf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4abe4.md#insn-00b4abf8) · [`00b4ac3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4abe4.md#insn-00b4ac3c) · [`00b4abf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4abe4.md#insn-00b4abf4)
- 新版 `00b4ac3c`（命令位置の公開資料なし） · `00b4ac80`（命令位置の公開資料なし） · `00b4ac38`（命令位置の公開資料なし）

~~~diff
- 00b4abf8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:fc0:8"]]
- 00b4abf8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4abf8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4ac3c ["COPY", "tmp:0:8", ["register:40a8:8"]]
+ 00b4ac3c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ac3c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4abf8 bytes a8027f39
+ 00b4ac3c bytes a8024039
- 00b4ac3c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4ac3c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:fc0:8"]]
- 00b4ac3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4ac80 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4ac80 ["COPY", "tmp:1:8", ["register:40a8:8"]]
+ 00b4ac80 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4ac3c bytes a0023f39
+ 00b4ac80 bytes a0020039
- 00b4abf4 ["COPY", "register:40a8:8", ["const:10a0000:8"]]
+ 00b4ac38 ["COPY", "register:40a8:8", ["const:10a1000:8"]]
- 00b4abf4 bytes b52a00d0
+ 00b4ac38 bytes b52a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c789094f444165a553dc8d766a1ffad"></a>

### [`00b4ac50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ac50.md) → [`00b4ac94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ac94.md) _ZN8firebase9messaging18firebase_messaging12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4acd0",
      "incomplete_value": true,
      "site": "00b4acd0",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": {
      "definition_site": "00b4ac8c",
      "incomplete_value": true,
      "site": "00b4ac8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4acf0",
      "incomplete_value": true,
      "site": "00b4acf0",
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
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4acac",
      "incomplete_value": true,
      "site": "00b4acac",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4acac",
      "incomplete_value": true,
      "site": "00b4acac",
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
      "definition_site": "00b4ac68",
      "incomplete_value": true,
      "site": "00b4ac68",
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
      "00b4aca8",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4acb4",
      "READ",
      [
        "storage",
        "010a0fc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4acd0",
      "WRITE",
      [
        "storage",
        "010a0fc0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4aca8",
      "READ",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4acb4",
      "READ",
      [
        "storage",
        "010a1000",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4acd0",
      "WRITE",
      [
        "storage",
        "010a1000",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ac8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ac50.md#insn-00b4ac8c) · [`00b4acac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ac50.md#insn-00b4acac) · [`00b4ac64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ac50.md#insn-00b4ac64)
- 新版 `00b4acd0`（命令位置の公開資料なし） · `00b4acf0`（命令位置の公開資料なし） · `00b4aca8`（命令位置の公開資料なし）

~~~diff
- 00b4ac8c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4ac8c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4ac8c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:fc0:8"]]
- 00b4ac8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4acd0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4acd0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4acd0 ["COPY", "tmp:2:8", ["register:40a8:8"]]
+ 00b4acd0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4ac8c bytes bf023f39
+ 00b4acd0 bytes bf020039
- 00b4acac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:fb8:8"]]
- 00b4acac ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4acac ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4acf0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ff8:8"]]
+ 00b4acf0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4acf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4acac bytes 9fde07f9
+ 00b4acf0 bytes 9ffe07f9
- 00b4ac64 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:fb8:8"]]
- 00b4ac64 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4aca8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ff8:8"]]
+ 00b4aca8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ac64 bytes 81de47f9
+ 00b4aca8 bytes 81fe47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2a4c28eeea12a8ad8d2ae928e8a6550"></a>

### [`00b4acc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4acc0.md) → [`00b4ad04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ad04.md) _ZN8firebase9messaging18firebase_messaging14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4ad44",
      "incomplete_value": true,
      "site": "00b4ad44",
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
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ad00",
      "incomplete_value": true,
      "site": "00b4ad00",
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
            "const:fb8:8"
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
      "00b4ad18",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad44",
      "WRITE",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad58",
      "PARAM",
      [
        "storage",
        "00c11588",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b4ad18",
      "READ",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad44",
      "WRITE",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad58",
      "PARAM",
      [
        "storage",
        "00c115d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ad00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4acc0.md#insn-00b4ad00) · [`00b4acd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4acc0.md#insn-00b4acd4) · [`00b4acf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4acc0.md#insn-00b4acf8)
- 新版 `00b4ad44`（命令位置の公開資料なし） · `00b4ad18`（命令位置の公開資料なし） · `00b4ad3c`（命令位置の公開資料なし）

~~~diff
- 00b4ad00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:fb8:8"]]
- 00b4ad00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ad44 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ff8:8"]]
+ 00b4ad44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ad00 bytes 80de07f9
+ 00b4ad44 bytes 80fe07f9
- 00b4acd4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:fb8:8"]]
- 00b4acd4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ad18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ff8:8"]]
+ 00b4ad18 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4acd4 bytes 81de47f9
+ 00b4ad18 bytes 81fe47f9
- 00b4acf8 ["INT_ADD", "register:40f0:8", ["const:b4acf8:8", "const:4:8"]]
- 00b4acf8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b4ad3c ["INT_ADD", "register:40f0:8", ["const:b4ad3c:8", "const:4:8"]]
+ 00b4ad3c ["CALL", null, ["callee:00bde090:8"]]
- 00b4acf8 bytes d24c0294
+ 00b4ad3c bytes d54c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d57eb2feefe1bf9cab81f86c24cdb58"></a>

### [`00b4ad30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ad30.md) → [`00b4ad74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ad74.md) _ZN8firebase9messaging18firebase_messaging11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ad90",
      "incomplete_value": false,
      "site": "00b4ad94",
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
            "const:547:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ad4c",
      "incomplete_value": false,
      "site": "00b4ad50",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4ada0",
      "incomplete_value": true,
      "site": "00b4adac",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ad5c",
      "incomplete_value": true,
      "site": "00b4ad68",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b4ad90",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b4ada0",
      "DATA",
      [
        "storage",
        "010a0fc8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ad90",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4ada0",
      "DATA",
      [
        "storage",
        "010a1008",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ad50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ad30.md#insn-00b4ad50) · [`00b4ad4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ad30.md#insn-00b4ad4c) · [`00b4ad54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ad30.md#insn-00b4ad54)
- 新版 `00b4ad94`（命令位置の公開資料なし） · `00b4ad90`（命令位置の公開資料なし） · `00b4ad98`（命令位置の公開資料なし）

~~~diff
- 00b4ad50 ["INT_ADD", "register:40f0:8", ["const:b4ad50:8", "const:4:8"]]
- 00b4ad50 ["CALL", null, ["callee:00bde180:8"]]
+ 00b4ad94 ["INT_ADD", "register:40f0:8", ["const:b4ad94:8", "const:4:8"]]
+ 00b4ad94 ["CALL", null, ["callee:00bde180:8"]]
- 00b4ad50 bytes f84c0294
+ 00b4ad94 bytes fb4c0294
- 00b4ad4c ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b4ad4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ad4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ad4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ad90 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b4ad90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ad90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ad90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4ad4c bytes 00501791
+ 00b4ad90 bytes 001c1591
- 00b4ad54 ["COPY", "register:4040:8", ["const:10a0000:8"]]
+ 00b4ad98 ["COPY", "register:4040:8", ["const:10a1000:8"]]
- 00b4ad54 bytes a82a00d0
+ 00b4ad98 bytes a82a00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-750cc03f9b5404883b09f73419120973"></a>

### [`00b4ad6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ad6c.md) → [`00b4adb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4adb0.md) _ZN8firebase9messaging18firebase_messaging13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4adf0",
      "incomplete_value": true,
      "site": "00b4adf0",
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
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4adac",
      "incomplete_value": true,
      "site": "00b4adac",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4adcc",
      "incomplete_value": true,
      "site": "00b4adcc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4ad88",
      "incomplete_value": true,
      "site": "00b4ad88",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b4ad88"
      ],
      [
        "FALL_THROUGH",
        "00b4adcc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b4adcc",
      "incomplete_value": true,
      "site": "00b4adf0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4ad88",
      "incomplete_value": true,
      "site": "00b4adac",
      "value": [
        "INT_NOTEQUAL",
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
      "00b4adc4",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4adf0",
      "WRITE",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae08",
      "PARAM",
      [
        "storage",
        "010a1010",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4adc4",
      "READ",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4adf0",
      "WRITE",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae08",
      "PARAM",
      [
        "storage",
        "010a1050",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4adac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ad6c.md#insn-00b4adac) · [`00b4ad80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ad6c.md#insn-00b4ad80) · [`00b4ada4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ad6c.md#insn-00b4ada4)
- 新版 `00b4adf0`（命令位置の公開資料なし） · `00b4adc4`（命令位置の公開資料なし） · `00b4ade8`（命令位置の公開資料なし）

~~~diff
- 00b4adac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:fb8:8"]]
- 00b4adac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4adf0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ff8:8"]]
+ 00b4adf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4adac bytes 80de07f9
+ 00b4adf0 bytes 80fe07f9
- 00b4ad80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:fb8:8"]]
- 00b4ad80 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4adc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ff8:8"]]
+ 00b4adc4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ad80 bytes 81de47f9
+ 00b4adc4 bytes 81fe47f9
- 00b4ada4 ["INT_ADD", "register:40f0:8", ["const:b4ada4:8", "const:4:8"]]
- 00b4ada4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b4ade8 ["INT_ADD", "register:40f0:8", ["const:b4ade8:8", "const:4:8"]]
+ 00b4ade8 ["CALL", null, ["callee:00bde090:8"]]
- 00b4ada4 bytes a74c0294
+ 00b4ade8 bytes aa4c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f8f9ad8efa625690b7cda9fcda42bc9"></a>

### [`00b4addc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4addc.md) → [`00b4ae20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ae20.md) _ZN8firebase9messaging18firebase_messaging10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00b4ae3c",
      "incomplete_value": true,
      "site": "00b4ae40",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4adf8",
      "incomplete_value": true,
      "site": "00b4adfc",
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
            "const:67f:8"
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
      "00b4ae3c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b4ae4c",
      "DATA",
      [
        "storage",
        "010a1010",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4ae3c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4ae4c",
      "DATA",
      [
        "storage",
        "010a1050",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4adfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4addc.md#insn-00b4adfc) · [`00b4adf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4addc.md#insn-00b4adf8) · [`00b4ae04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4addc.md#insn-00b4ae04)
- 新版 `00b4ae40`（命令位置の公開資料なし） · `00b4ae3c`（命令位置の公開資料なし） · `00b4ae48`（命令位置の公開資料なし）

~~~diff
- 00b4adfc ["INT_ADD", "register:40f0:8", ["const:b4adfc:8", "const:4:8"]]
- 00b4adfc ["CALL", null, ["callee:00bde180:8"]]
+ 00b4ae40 ["INT_ADD", "register:40f0:8", ["const:b4ae40:8", "const:4:8"]]
+ 00b4ae40 ["CALL", null, ["callee:00bde180:8"]]
- 00b4adfc bytes cd4c0294
+ 00b4ae40 bytes d04c0294
- 00b4adf8 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b4adf8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4adf8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4adf8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ae3c ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b4ae3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ae3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ae3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4adf8 bytes 00fc1991
+ 00b4ae3c bytes 00c81791
- 00b4ae04 ["COPY", "tmp:0:8", ["const:10:8"]]
- 00b4ae04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4ae04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4ae04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4ae48 ["COPY", "tmp:0:8", ["const:50:8"]]
+ 00b4ae48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4ae48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4ae48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4ae04 bytes 08410091
+ 00b4ae48 bytes 08410191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1355d461b950ae05426d8edb13449e92"></a>

### [`00b4ae18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae18.md) → [`00b4ae5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ae5c.md) _ZN8firebase9messaging27registration_intent_service19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4ae88",
      "incomplete_value": true,
      "site": "00b4ae88",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ae44",
      "incomplete_value": true,
      "site": "00b4ae44",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4ae70",
      "incomplete_value": true,
      "site": "00b4ae70",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4ae2c",
      "incomplete_value": true,
      "site": "00b4ae2c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4ae7c",
      "incomplete_value": false,
      "site": "00b4ae80",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ae38",
      "incomplete_value": false,
      "site": "00b4ae3c",
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
            "const:e06:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ae6c",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae7c",
      "PARAM",
      [
        "storage",
        "002a8e06",
        null,
        "string"
      ]
    ],
    [
      "00b4ae88",
      "WRITE",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ae6c",
      "READ",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae7c",
      "PARAM",
      [
        "storage",
        "002a8ea0",
        null,
        "string"
      ]
    ],
    [
      "00b4ae88",
      "WRITE",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ae3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae18.md#insn-00b4ae3c) · [`00b4ae44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae18.md#insn-00b4ae44) · [`00b4ae28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae18.md#insn-00b4ae28)
- 新版 `00b4ae80`（命令位置の公開資料なし） · `00b4ae88`（命令位置の公開資料なし） · `00b4ae6c`（命令位置の公開資料なし）

~~~diff
- 00b4ae3c ["INT_ADD", "register:40f0:8", ["const:b4ae3c:8", "const:4:8"]]
- 00b4ae3c ["CALL", null, ["callee:00bde090:8"]]
+ 00b4ae80 ["INT_ADD", "register:40f0:8", ["const:b4ae80:8", "const:4:8"]]
+ 00b4ae80 ["CALL", null, ["callee:00bde090:8"]]
- 00b4ae3c bytes 814c0294
+ 00b4ae80 bytes 844c0294
- 00b4ae44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
- 00b4ae44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ae88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:58:8"]]
+ 00b4ae88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ae44 bytes 600e00f9
+ 00b4ae88 bytes 602e00f9
- 00b4ae28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
- 00b4ae28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ae6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:58:8"]]
+ 00b4ae6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ae28 bytes 680e40f9
+ 00b4ae6c bytes 682e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e47ae10275f7b6d3201787a15920629"></a>

### [`00b4ae58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae58.md) → [`00b4ae9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4ae9c.md) _ZN8firebase9messaging27registration_intent_service19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4aec8",
      "incomplete_value": true,
      "site": "00b4aec8",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ae84",
      "incomplete_value": true,
      "site": "00b4ae84",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4aeb0",
      "incomplete_value": true,
      "site": "00b4aeb0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4ae6c",
      "incomplete_value": true,
      "site": "00b4ae6c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4aeb8",
      "incomplete_value": false,
      "site": "00b4aec0",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ae74",
      "incomplete_value": false,
      "site": "00b4ae7c",
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
            "const:e06:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4aeac",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aeb8",
      "PARAM",
      [
        "storage",
        "002a8e06",
        null,
        "string"
      ]
    ],
    [
      "00b4aec8",
      "WRITE",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aeac",
      "READ",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aeb8",
      "PARAM",
      [
        "storage",
        "002a8ea0",
        null,
        "string"
      ]
    ],
    [
      "00b4aec8",
      "WRITE",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ae7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae58.md#insn-00b4ae7c) · [`00b4ae84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae58.md#insn-00b4ae84) · [`00b4ae68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae58.md#insn-00b4ae68)
- 新版 `00b4aec0`（命令位置の公開資料なし） · `00b4aec8`（命令位置の公開資料なし） · `00b4aeac`（命令位置の公開資料なし）

~~~diff
- 00b4ae7c ["INT_ADD", "register:40f0:8", ["const:b4ae7c:8", "const:4:8"]]
- 00b4ae7c ["CALL", null, ["callee:00bde090:8"]]
+ 00b4aec0 ["INT_ADD", "register:40f0:8", ["const:b4aec0:8", "const:4:8"]]
+ 00b4aec0 ["CALL", null, ["callee:00bde090:8"]]
- 00b4ae7c bytes 714c0294
+ 00b4aec0 bytes 744c0294
- 00b4ae84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
- 00b4ae84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4aec8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:58:8"]]
+ 00b4aec8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ae84 bytes 600e00f9
+ 00b4aec8 bytes 602e00f9
- 00b4ae68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
- 00b4ae68 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4aeac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:58:8"]]
+ 00b4aeac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ae68 bytes 680e40f9
+ 00b4aeac bytes 682e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8fc8de37841f6b4b34928ac17c57a22"></a>

### [`00b4ae98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae98.md) → [`00b4aedc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4aedc.md) _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4af0c",
      "incomplete_value": true,
      "site": "00b4af0c",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aec8",
      "incomplete_value": true,
      "site": "00b4aec8",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4aef0",
      "incomplete_value": true,
      "site": "00b4aef0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4aeac",
      "incomplete_value": true,
      "site": "00b4aeac",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4aefc",
      "incomplete_value": true,
      "site": "00b4af04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aeb8",
      "incomplete_value": true,
      "site": "00b4aec0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:e06:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4aeec",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aefc",
      "PARAM",
      [
        "storage",
        "002a8e06",
        null,
        "string"
      ]
    ],
    [
      "00b4af0c",
      "WRITE",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4aeec",
      "READ",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aefc",
      "PARAM",
      [
        "storage",
        "002a8ea0",
        null,
        "string"
      ]
    ],
    [
      "00b4af0c",
      "WRITE",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae98.md#insn-00b4aec0) · [`00b4aec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae98.md#insn-00b4aec8) · [`00b4aea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4ae98.md#insn-00b4aea8)
- 新版 `00b4af04`（命令位置の公開資料なし） · `00b4af0c`（命令位置の公開資料なし） · `00b4aeec`（命令位置の公開資料なし）

~~~diff
- 00b4aec0 ["INT_ADD", "register:40f0:8", ["const:b4aec0:8", "const:4:8"]]
- 00b4aec0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b4af04 ["INT_ADD", "register:40f0:8", ["const:b4af04:8", "const:4:8"]]
+ 00b4af04 ["CALL", null, ["callee:00bde090:8"]]
- 00b4aec0 bytes 604c0294
+ 00b4af04 bytes 634c0294
- 00b4aec8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
- 00b4aec8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4af0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:58:8"]]
+ 00b4af0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4aec8 bytes 600e00f9
+ 00b4af0c bytes 602e00f9
- 00b4aea8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
- 00b4aea8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4aeec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:58:8"]]
+ 00b4aeec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4aea8 bytes 680e40f9
+ 00b4aeec bytes 682e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a27eb4d450cad2f10090bc90b4df768d"></a>

### [`00b4aedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aedc.md) → [`00b4af20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4af20.md) _ZN8firebase9messaging27registration_intent_service10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4af50",
      "incomplete_value": true,
      "site": "00b4af50",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4af0c",
      "incomplete_value": true,
      "site": "00b4af0c",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4af34",
      "incomplete_value": true,
      "site": "00b4af34",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4aef0",
      "incomplete_value": true,
      "site": "00b4aef0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4af3c",
      "incomplete_value": false,
      "site": "00b4af48",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aef8",
      "incomplete_value": false,
      "site": "00b4af04",
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
            "const:e06:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4af30",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4af3c",
      "PARAM",
      [
        "storage",
        "002a8e06",
        null,
        "string"
      ]
    ],
    [
      "00b4af50",
      "WRITE",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4af30",
      "READ",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4af3c",
      "PARAM",
      [
        "storage",
        "002a8ea0",
        null,
        "string"
      ]
    ],
    [
      "00b4af50",
      "WRITE",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4af04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aedc.md#insn-00b4af04) · [`00b4af0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aedc.md#insn-00b4af0c) · [`00b4aeec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4aedc.md#insn-00b4aeec)
- 新版 `00b4af48`（命令位置の公開資料なし） · `00b4af50`（命令位置の公開資料なし） · `00b4af30`（命令位置の公開資料なし）

~~~diff
- 00b4af04 ["INT_ADD", "register:40f0:8", ["const:b4af04:8", "const:4:8"]]
- 00b4af04 ["CALL", null, ["callee:00bde090:8"]]
+ 00b4af48 ["INT_ADD", "register:40f0:8", ["const:b4af48:8", "const:4:8"]]
+ 00b4af48 ["CALL", null, ["callee:00bde090:8"]]
- 00b4af04 bytes 4f4c0294
+ 00b4af48 bytes 524c0294
- 00b4af0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
- 00b4af0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4af50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:58:8"]]
+ 00b4af50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4af0c bytes 600e00f9
+ 00b4af50 bytes 602e00f9
- 00b4aeec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:18:8"]]
- 00b4aeec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4af30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:58:8"]]
+ 00b4af30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4aeec bytes 680e40f9
+ 00b4af30 bytes 682e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25948045d04b80b7edd9b9bef273cce1"></a>

### [`00b4af2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af2c.md) → [`00b4af70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4af70.md) _ZN8firebase9messaging27registration_intent_service15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4afc8",
      "incomplete_value": true,
      "site": "00b4afc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4af84",
      "incomplete_value": true,
      "site": "00b4af84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4afa4",
      "incomplete_value": true,
      "site": "00b4afb0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
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
      "definition_site": "00b4af60",
      "incomplete_value": true,
      "site": "00b4af6c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
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
      "00b4af84",
      "READ",
      [
        "storage",
        "010a1020",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4afa4",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4afc8",
      "WRITE",
      [
        "storage",
        "010a1020",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4af84",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4afa4",
      "READ",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4afc8",
      "WRITE",
      [
        "storage",
        "010a1060",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4af40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af2c.md#insn-00b4af40) · [`00b4af6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af2c.md#insn-00b4af6c) · [`00b4af84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af2c.md#insn-00b4af84)
- 新版 `00b4af84`（命令位置の公開資料なし） · `00b4afb0`（命令位置の公開資料なし） · `00b4afc8`（命令位置の公開資料なし）

~~~diff
- 00b4af40 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:20:8"]]
- 00b4af40 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4af40 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4af84 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:60:8"]]
+ 00b4af84 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4af84 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4af40 bytes a8824039
+ 00b4af84 bytes a8824139
- 00b4af6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4af6c ["INT_ADD", "register:40f0:8", ["const:b4af6c:8", "const:4:8"]]
- 00b4af6c ["CALLIND", null, ["register:0:8"]]
+ 00b4afb0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4afb0 ["INT_ADD", "register:40f0:8", ["const:b4afb0:8", "const:4:8"]]
+ 00b4afb0 ["CALLIND", null, ["register:0:8"]]
- 00b4af6c bytes 00013fd6
+ 00b4afb0 bytes 00013fd6
- 00b4af84 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4af84 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:20:8"]]
- 00b4af84 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4afc8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4afc8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:60:8"]]
+ 00b4afc8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4af84 bytes a0820039
+ 00b4afc8 bytes a0820139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc30a8625b63d55fec868b5605b828d3"></a>

### [`00b4af98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af98.md) → [`00b4afdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4a/00b4afdc.md) _ZN8firebase9messaging27registration_intent_service12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b018",
      "incomplete_value": true,
      "site": "00b4b018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4afd4",
      "incomplete_value": true,
      "site": "00b4afd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:20:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b038",
      "incomplete_value": true,
      "site": "00b4b038",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aff4",
      "incomplete_value": true,
      "site": "00b4aff4",
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
            "const:18:8"
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
      "definition_site": "00b4b028",
      "incomplete_value": true,
      "site": "00b4b034",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4afe4",
      "incomplete_value": true,
      "site": "00b4aff0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:18:8"
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
      "00b4aff0",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4affc",
      "READ",
      [
        "storage",
        "010a1020",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b018",
      "WRITE",
      [
        "storage",
        "010a1020",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4aff0",
      "READ",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4affc",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b018",
      "WRITE",
      [
        "storage",
        "010a1060",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4afac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af98.md#insn-00b4afac) · [`00b4afd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af98.md#insn-00b4afd4) · [`00b4aff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4a/00b4af98.md#insn-00b4aff0)
- 新版 `00b4aff0`（命令位置の公開資料なし） · `00b4b018`（命令位置の公開資料なし） · `00b4b034`（命令位置の公開資料なし）

~~~diff
- 00b4afac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:18:8"]]
- 00b4afac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4aff0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:58:8"]]
+ 00b4aff0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4afac bytes 810e40f9
+ 00b4aff0 bytes 812e40f9
- 00b4afd4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4afd4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4afd4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:20:8"]]
- 00b4afd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4b018 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4b018 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4b018 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:60:8"]]
+ 00b4b018 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4afd4 bytes bf820039
+ 00b4b018 bytes bf820139
- 00b4aff0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4aff0 ["INT_ADD", "register:40f0:8", ["const:b4aff0:8", "const:4:8"]]
- 00b4aff0 ["CALLIND", null, ["register:0:8"]]
+ 00b4b034 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b034 ["INT_ADD", "register:40f0:8", ["const:b4b034:8", "const:4:8"]]
+ 00b4b034 ["CALLIND", null, ["register:0:8"]]
- 00b4aff0 bytes 00013fd6
+ 00b4b034 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f7d793fdd385a2c3bdea60996c1724a"></a>

### [`00b4b008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b008.md) → [`00b4b04c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b04c.md) _ZN8firebase9messaging27registration_intent_service14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b08c",
      "incomplete_value": true,
      "site": "00b4b08c",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b048",
      "incomplete_value": true,
      "site": "00b4b048",
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
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b068",
      "incomplete_value": true,
      "site": "00b4b068",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4b024",
      "incomplete_value": true,
      "site": "00b4b024",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b4b024"
      ],
      [
        "FALL_THROUGH",
        "00b4b068"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b4b068",
      "incomplete_value": true,
      "site": "00b4b08c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4b024",
      "incomplete_value": true,
      "site": "00b4b048",
      "value": [
        "INT_NOTEQUAL",
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
      "00b4b060",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b070",
      "PARAM",
      [
        "storage",
        "002a8e06",
        null,
        "string"
      ]
    ],
    [
      "00b4b08c",
      "WRITE",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b060",
      "READ",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b070",
      "PARAM",
      [
        "storage",
        "002a8ea0",
        null,
        "string"
      ]
    ],
    [
      "00b4b08c",
      "WRITE",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b008.md#insn-00b4b048) · [`00b4b01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b008.md#insn-00b4b01c) · [`00b4b02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b008.md#insn-00b4b02c)
- 新版 `00b4b08c`（命令位置の公開資料なし） · `00b4b060`（命令位置の公開資料なし） · `00b4b070`（命令位置の公開資料なし）

~~~diff
- 00b4b048 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:18:8"]]
- 00b4b048 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b08c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:58:8"]]
+ 00b4b08c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b048 bytes 800e00f9
+ 00b4b08c bytes 802e00f9
- 00b4b01c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:18:8"]]
- 00b4b01c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b060 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:58:8"]]
+ 00b4b060 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b01c bytes 810e40f9
+ 00b4b060 bytes 812e40f9
- 00b4b02c ["COPY", "tmp:0:8", ["const:e06:8"]]
- 00b4b02c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b4b02c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b4b02c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b4b070 ["COPY", "tmp:0:8", ["const:ea0:8"]]
+ 00b4b070 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b4b070 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b4b070 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b4b02c bytes 63183891
+ 00b4b070 bytes 63803a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d143c53932058a2241b283663b623ae4"></a>

### [`00b4b078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b078.md) → [`00b4b0bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b0bc.md) _ZN8firebase9messaging27registration_intent_service11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b0d8",
      "incomplete_value": false,
      "site": "00b4b0dc",
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
            "const:547:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b094",
      "incomplete_value": false,
      "site": "00b4b098",
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
            "const:5d4:8"
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
      "00b4b0d8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b4b0e8",
      "DATA",
      [
        "storage",
        "010a1028",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b0d8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4b0e8",
      "DATA",
      [
        "storage",
        "010a1068",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b078.md#insn-00b4b098) · [`00b4b094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b078.md#insn-00b4b094) · [`00b4b0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b078.md#insn-00b4b0a0)
- 新版 `00b4b0dc`（命令位置の公開資料なし） · `00b4b0d8`（命令位置の公開資料なし） · `00b4b0e4`（命令位置の公開資料なし）

~~~diff
- 00b4b098 ["INT_ADD", "register:40f0:8", ["const:b4b098:8", "const:4:8"]]
- 00b4b098 ["CALL", null, ["callee:00bde180:8"]]
+ 00b4b0dc ["INT_ADD", "register:40f0:8", ["const:b4b0dc:8", "const:4:8"]]
+ 00b4b0dc ["CALL", null, ["callee:00bde180:8"]]
- 00b4b098 bytes 264c0294
+ 00b4b0dc bytes 294c0294
- 00b4b094 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b4b094 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b094 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b094 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b0d8 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b4b0d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b0d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b0d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b094 bytes 00501791
+ 00b4b0d8 bytes 001c1591
- 00b4b0a0 ["COPY", "tmp:0:8", ["const:28:8"]]
- 00b4b0a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b0a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b0a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4b0e4 ["COPY", "tmp:0:8", ["const:68:8"]]
+ 00b4b0e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b0e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b0e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4b0a0 bytes 08a10091
+ 00b4b0e4 bytes 08a10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eba24d9d36b2f8d89248416c9a5c154"></a>

### [`00b4b0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b0b4.md) → [`00b4b0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b0f8.md) _ZN8firebase9messaging27registration_intent_service13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b138",
      "incomplete_value": true,
      "site": "00b4b138",
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
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b0f4",
      "incomplete_value": true,
      "site": "00b4b0f4",
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
            "const:18:8"
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
      "definition_site": "00b4b11c",
      "incomplete_value": false,
      "site": "00b4b130",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b0d8",
      "incomplete_value": false,
      "site": "00b4b0ec",
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
            "const:e06:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b10c",
      "READ",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b11c",
      "PARAM",
      [
        "storage",
        "002a8e06",
        null,
        "string"
      ]
    ],
    [
      "00b4b138",
      "WRITE",
      [
        "storage",
        "010a1018",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b10c",
      "READ",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b11c",
      "PARAM",
      [
        "storage",
        "002a8ea0",
        null,
        "string"
      ]
    ],
    [
      "00b4b138",
      "WRITE",
      [
        "storage",
        "010a1058",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b0b4.md#insn-00b4b0ec) · [`00b4b0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b0b4.md#insn-00b4b0f4) · [`00b4b0c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b0b4.md#insn-00b4b0c8)
- 新版 `00b4b130`（命令位置の公開資料なし） · `00b4b138`（命令位置の公開資料なし） · `00b4b10c`（命令位置の公開資料なし）

~~~diff
- 00b4b0ec ["INT_ADD", "register:40f0:8", ["const:b4b0ec:8", "const:4:8"]]
- 00b4b0ec ["CALL", null, ["callee:00bde090:8"]]
+ 00b4b130 ["INT_ADD", "register:40f0:8", ["const:b4b130:8", "const:4:8"]]
+ 00b4b130 ["CALL", null, ["callee:00bde090:8"]]
- 00b4b0ec bytes d54b0294
+ 00b4b130 bytes d84b0294
- 00b4b0f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:18:8"]]
- 00b4b0f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b138 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:58:8"]]
+ 00b4b138 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b0f4 bytes 800e00f9
+ 00b4b138 bytes 802e00f9
- 00b4b0c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:18:8"]]
- 00b4b0c8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b10c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:58:8"]]
+ 00b4b10c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b0c8 bytes 810e40f9
+ 00b4b10c bytes 812e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1cbc1515e69402ed12f873220e26c1d"></a>

### [`00b4b124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b124.md) → [`00b4b168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b168.md) _ZN8firebase9messaging27registration_intent_service10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4b194",
      "incomplete_value": true,
      "site": "00b4b1a0",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b150",
      "incomplete_value": true,
      "site": "00b4b15c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b4b184",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b4b194",
      "DATA",
      [
        "storage",
        "010a1030",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b184",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4b194",
      "DATA",
      [
        "storage",
        "010a1070",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b124.md#insn-00b4b140) · [`00b4b144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b124.md#insn-00b4b144) · [`00b4b14c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b124.md#insn-00b4b14c)
- 新版 `00b4b184`（命令位置の公開資料なし） · `00b4b188`（命令位置の公開資料なし） · `00b4b190`（命令位置の公開資料なし）

~~~diff
- 00b4b140 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b4b140 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b140 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b140 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b184 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b4b184 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b184 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b184 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b140 bytes 00fc1991
+ 00b4b184 bytes 00c81791
- 00b4b144 ["INT_ADD", "register:40f0:8", ["const:b4b144:8", "const:4:8"]]
- 00b4b144 ["CALL", null, ["callee:00bde180:8"]]
+ 00b4b188 ["INT_ADD", "register:40f0:8", ["const:b4b188:8", "const:4:8"]]
+ 00b4b188 ["CALL", null, ["callee:00bde180:8"]]
- 00b4b144 bytes fb4b0294
+ 00b4b188 bytes fe4b0294
- 00b4b14c ["COPY", "tmp:0:8", ["const:30:8"]]
- 00b4b14c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b14c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b14c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4b190 ["COPY", "tmp:0:8", ["const:70:8"]]
+ 00b4b190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4b14c bytes 08c10091
+ 00b4b190 bytes 08c10191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee74588367a79b0a8b3b7a41aab379ce"></a>

### [`00b4b160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b160.md) → [`00b4b1a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b1a4.md) _ZN8firebase9messaging26illegal_argument_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b1d0",
      "incomplete_value": true,
      "site": "00b4b1d0",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b18c",
      "incomplete_value": true,
      "site": "00b4b18c",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b1b8",
      "incomplete_value": true,
      "site": "00b4b1b8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4b174",
      "incomplete_value": true,
      "site": "00b4b174",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4b1c4",
      "incomplete_value": true,
      "site": "00b4b1c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:455:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b180",
      "incomplete_value": true,
      "site": "00b4b184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4018:8"
          ],
          [
            "leaf",
            "const:4e2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b1b4",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b1c4",
      "PARAM",
      [
        "storage",
        "002954e2",
        null,
        "string"
      ]
    ],
    [
      "00b4b1d0",
      "WRITE",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b1b4",
      "READ",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b1c4",
      "PARAM",
      [
        "storage",
        "00295455",
        null,
        "string"
      ]
    ],
    [
      "00b4b1d0",
      "WRITE",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b160.md#insn-00b4b184) · [`00b4b18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b160.md#insn-00b4b18c) · [`00b4b170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b160.md#insn-00b4b170)
- 新版 `00b4b1c8`（命令位置の公開資料なし） · `00b4b1d0`（命令位置の公開資料なし） · `00b4b1b4`（命令位置の公開資料なし）

~~~diff
- 00b4b184 ["INT_ADD", "register:40f0:8", ["const:b4b184:8", "const:4:8"]]
- 00b4b184 ["CALL", null, ["callee:00bde090:8"]]
+ 00b4b1c8 ["INT_ADD", "register:40f0:8", ["const:b4b1c8:8", "const:4:8"]]
+ 00b4b1c8 ["CALL", null, ["callee:00bde090:8"]]
- 00b4b184 bytes af4b0294
+ 00b4b1c8 bytes b24b0294
- 00b4b18c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
- 00b4b18c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b1d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
+ 00b4b1d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b18c bytes 601e00f9
+ 00b4b1d0 bytes 603e00f9
- 00b4b170 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
- 00b4b170 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b1b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
+ 00b4b1b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b170 bytes 681e40f9
+ 00b4b1b4 bytes 683e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7558a1781317450eda31f56dc29d4385"></a>

### [`00b4b1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b1a0.md) → [`00b4b1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b1e4.md) _ZN8firebase9messaging26illegal_argument_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b210",
      "incomplete_value": true,
      "site": "00b4b210",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b1cc",
      "incomplete_value": true,
      "site": "00b4b1cc",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b1f8",
      "incomplete_value": true,
      "site": "00b4b1f8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4b1b4",
      "incomplete_value": true,
      "site": "00b4b1b4",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b4b1b4"
      ],
      [
        "FALL_THROUGH",
        "00b4b1f8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b4b1f8",
      "incomplete_value": true,
      "site": "00b4b210",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4b1b4",
      "incomplete_value": true,
      "site": "00b4b1cc",
      "value": [
        "INT_NOTEQUAL",
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
      "00b4b1f4",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b200",
      "PARAM",
      [
        "storage",
        "002954e2",
        null,
        "string"
      ]
    ],
    [
      "00b4b210",
      "WRITE",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b1f4",
      "READ",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b200",
      "PARAM",
      [
        "storage",
        "00295455",
        null,
        "string"
      ]
    ],
    [
      "00b4b210",
      "WRITE",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b1cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b1a0.md#insn-00b4b1cc) · [`00b4b1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b1a0.md#insn-00b4b1b0) · [`00b4b1bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b1a0.md#insn-00b4b1bc)
- 新版 `00b4b210`（命令位置の公開資料なし） · `00b4b1f4`（命令位置の公開資料なし） · `00b4b200`（命令位置の公開資料なし）

~~~diff
- 00b4b1cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
- 00b4b1cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b210 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
+ 00b4b210 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b1cc bytes 601e00f9
+ 00b4b210 bytes 603e00f9
- 00b4b1b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
- 00b4b1b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b1f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
+ 00b4b1f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b1b0 bytes 681e40f9
+ 00b4b1f4 bytes 683e40f9
- 00b4b1bc ["COPY", "tmp:0:8", ["const:4e2:8"]]
- 00b4b1bc ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b4b1bc ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b4b1bc ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b4b200 ["COPY", "tmp:0:8", ["const:455:8"]]
+ 00b4b200 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b4b200 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b4b200 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b4b1bc bytes 63881391
+ 00b4b200 bytes 63541191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6ce2b5add68af4f4ba09fdde5c66d3f"></a>

### [`00b4b1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b1e0.md) → [`00b4b224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b224.md) _ZN8firebase9messaging26illegal_argument_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b254",
      "incomplete_value": true,
      "site": "00b4b254",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b210",
      "incomplete_value": true,
      "site": "00b4b210",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b238",
      "incomplete_value": true,
      "site": "00b4b238",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4b1f4",
      "incomplete_value": true,
      "site": "00b4b1f4",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4b244",
      "incomplete_value": false,
      "site": "00b4b24c",
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
            "const:455:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b200",
      "incomplete_value": false,
      "site": "00b4b208",
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
            "const:4e2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b234",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b244",
      "PARAM",
      [
        "storage",
        "002954e2",
        null,
        "string"
      ]
    ],
    [
      "00b4b254",
      "WRITE",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b234",
      "READ",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b244",
      "PARAM",
      [
        "storage",
        "00295455",
        null,
        "string"
      ]
    ],
    [
      "00b4b254",
      "WRITE",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b1e0.md#insn-00b4b208) · [`00b4b210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b1e0.md#insn-00b4b210) · [`00b4b1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b1e0.md#insn-00b4b1f0)
- 新版 `00b4b24c`（命令位置の公開資料なし） · `00b4b254`（命令位置の公開資料なし） · `00b4b234`（命令位置の公開資料なし）

~~~diff
- 00b4b208 ["INT_ADD", "register:40f0:8", ["const:b4b208:8", "const:4:8"]]
- 00b4b208 ["CALL", null, ["callee:00bde090:8"]]
+ 00b4b24c ["INT_ADD", "register:40f0:8", ["const:b4b24c:8", "const:4:8"]]
+ 00b4b24c ["CALL", null, ["callee:00bde090:8"]]
- 00b4b208 bytes 8e4b0294
+ 00b4b24c bytes 914b0294
- 00b4b210 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
- 00b4b210 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b254 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
+ 00b4b254 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b210 bytes 601e00f9
+ 00b4b254 bytes 603e00f9
- 00b4b1f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
- 00b4b1f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b234 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
+ 00b4b234 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b1f0 bytes 681e40f9
+ 00b4b234 bytes 683e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dac656bf20cc29fb50d327192bd2804"></a>

### [`00b4b224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b224.md) → [`00b4b268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b268.md) _ZN8firebase9messaging26illegal_argument_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b298",
      "incomplete_value": true,
      "site": "00b4b298",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b254",
      "incomplete_value": true,
      "site": "00b4b254",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b27c",
      "incomplete_value": true,
      "site": "00b4b27c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4b238",
      "incomplete_value": true,
      "site": "00b4b238",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4b284",
      "incomplete_value": false,
      "site": "00b4b290",
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
            "const:455:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b240",
      "incomplete_value": false,
      "site": "00b4b24c",
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
            "const:4e2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b278",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b284",
      "PARAM",
      [
        "storage",
        "002954e2",
        null,
        "string"
      ]
    ],
    [
      "00b4b298",
      "WRITE",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b278",
      "READ",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b284",
      "PARAM",
      [
        "storage",
        "00295455",
        null,
        "string"
      ]
    ],
    [
      "00b4b298",
      "WRITE",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b224.md#insn-00b4b24c) · [`00b4b254`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b224.md#insn-00b4b254) · [`00b4b234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b224.md#insn-00b4b234)
- 新版 `00b4b290`（命令位置の公開資料なし） · `00b4b298`（命令位置の公開資料なし） · `00b4b278`（命令位置の公開資料なし）

~~~diff
- 00b4b24c ["INT_ADD", "register:40f0:8", ["const:b4b24c:8", "const:4:8"]]
- 00b4b24c ["CALL", null, ["callee:00bde090:8"]]
+ 00b4b290 ["INT_ADD", "register:40f0:8", ["const:b4b290:8", "const:4:8"]]
+ 00b4b290 ["CALL", null, ["callee:00bde090:8"]]
- 00b4b24c bytes 7d4b0294
+ 00b4b290 bytes 804b0294
- 00b4b254 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
- 00b4b254 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b298 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
+ 00b4b298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b254 bytes 601e00f9
+ 00b4b298 bytes 603e00f9
- 00b4b234 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:38:8"]]
- 00b4b234 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b278 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:78:8"]]
+ 00b4b278 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b234 bytes 681e40f9
+ 00b4b278 bytes 683e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83286296c7faa28e2081c2da16eaf9b7"></a>

### [`00b4b274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b274.md) → [`00b4b2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b2b8.md) _ZN8firebase9messaging26illegal_argument_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b310",
      "incomplete_value": true,
      "site": "00b4b310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b2cc",
      "incomplete_value": true,
      "site": "00b4b2cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b2ec",
      "incomplete_value": true,
      "site": "00b4b2f8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b2a8",
      "incomplete_value": true,
      "site": "00b4b2b4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
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
      "00b4b2cc",
      "READ",
      [
        "storage",
        "010a1040",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b2ec",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b310",
      "WRITE",
      [
        "storage",
        "010a1040",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b2cc",
      "READ",
      [
        "storage",
        "010a1080",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b2ec",
      "READ",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b310",
      "WRITE",
      [
        "storage",
        "010a1080",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b274.md#insn-00b4b288) · [`00b4b2b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b274.md#insn-00b4b2b4) · [`00b4b2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b274.md#insn-00b4b2cc)
- 新版 `00b4b2cc`（命令位置の公開資料なし） · `00b4b2f8`（命令位置の公開資料なし） · `00b4b310`（命令位置の公開資料なし）

~~~diff
- 00b4b288 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:40:8"]]
- 00b4b288 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4b288 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4b2cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:80:8"]]
+ 00b4b2cc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b2cc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4b288 bytes a8024139
+ 00b4b2cc bytes a8024239
- 00b4b2b4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b2b4 ["INT_ADD", "register:40f0:8", ["const:b4b2b4:8", "const:4:8"]]
- 00b4b2b4 ["CALLIND", null, ["register:0:8"]]
+ 00b4b2f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b2f8 ["INT_ADD", "register:40f0:8", ["const:b4b2f8:8", "const:4:8"]]
+ 00b4b2f8 ["CALLIND", null, ["register:0:8"]]
- 00b4b2b4 bytes 00013fd6
+ 00b4b2f8 bytes 00013fd6
- 00b4b2cc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4b2cc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:40:8"]]
- 00b4b2cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4b310 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4b310 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:80:8"]]
+ 00b4b310 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4b2cc bytes a0020139
+ 00b4b310 bytes a0020239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c1f73ccc12481e3054db241fbf0aff6"></a>

### [`00b4b2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b2e0.md) → [`00b4b324`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b324.md) _ZN8firebase9messaging26illegal_argument_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b360",
      "incomplete_value": true,
      "site": "00b4b360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b31c",
      "incomplete_value": true,
      "site": "00b4b31c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:40:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b380",
      "incomplete_value": true,
      "site": "00b4b380",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b33c",
      "incomplete_value": true,
      "site": "00b4b33c",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b33c",
      "incomplete_value": true,
      "site": "00b4b33c",
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
      "definition_site": "00b4b2f8",
      "incomplete_value": true,
      "site": "00b4b2f8",
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
      "00b4b338",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b344",
      "READ",
      [
        "storage",
        "010a1040",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b360",
      "WRITE",
      [
        "storage",
        "010a1040",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b338",
      "READ",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b344",
      "READ",
      [
        "storage",
        "010a1080",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b360",
      "WRITE",
      [
        "storage",
        "010a1080",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b31c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b2e0.md#insn-00b4b31c) · [`00b4b33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b2e0.md#insn-00b4b33c) · [`00b4b2f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b2e0.md#insn-00b4b2f4)
- 新版 `00b4b360`（命令位置の公開資料なし） · `00b4b380`（命令位置の公開資料なし） · `00b4b338`（命令位置の公開資料なし）

~~~diff
- 00b4b31c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4b31c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4b31c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:40:8"]]
- 00b4b31c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4b360 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4b360 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4b360 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:80:8"]]
+ 00b4b360 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4b31c bytes bf020139
+ 00b4b360 bytes bf020239
- 00b4b33c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:38:8"]]
- 00b4b33c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4b33c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4b380 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
+ 00b4b380 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4b380 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4b33c bytes 9f1e00f9
+ 00b4b380 bytes 9f3e00f9
- 00b4b2f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:38:8"]]
- 00b4b2f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b338 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
+ 00b4b338 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b2f4 bytes 811e40f9
+ 00b4b338 bytes 813e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f4e6bec93a42acb4b167602d7fa78f4"></a>

### [`00b4b350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b350.md) → [`00b4b394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b394.md) _ZN8firebase9messaging26illegal_argument_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b3d4",
      "incomplete_value": true,
      "site": "00b4b3d4",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b390",
      "incomplete_value": true,
      "site": "00b4b390",
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
            "const:38:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b3b0",
      "incomplete_value": true,
      "site": "00b4b3b0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4b36c",
      "incomplete_value": true,
      "site": "00b4b36c",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b4b36c"
      ],
      [
        "FALL_THROUGH",
        "00b4b3b0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b4b3b0",
      "incomplete_value": true,
      "site": "00b4b3d4",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4b36c",
      "incomplete_value": true,
      "site": "00b4b390",
      "value": [
        "INT_NOTEQUAL",
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
      "00b4b3a8",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b3b8",
      "PARAM",
      [
        "storage",
        "002954e2",
        null,
        "string"
      ]
    ],
    [
      "00b4b3d4",
      "WRITE",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b3a8",
      "READ",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b3b8",
      "PARAM",
      [
        "storage",
        "00295455",
        null,
        "string"
      ]
    ],
    [
      "00b4b3d4",
      "WRITE",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b350.md#insn-00b4b390) · [`00b4b364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b350.md#insn-00b4b364) · [`00b4b374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b350.md#insn-00b4b374)
- 新版 `00b4b3d4`（命令位置の公開資料なし） · `00b4b3a8`（命令位置の公開資料なし） · `00b4b3b8`（命令位置の公開資料なし）

~~~diff
- 00b4b390 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:38:8"]]
- 00b4b390 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b3d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
+ 00b4b3d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b390 bytes 801e00f9
+ 00b4b3d4 bytes 803e00f9
- 00b4b364 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:38:8"]]
- 00b4b364 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b3a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
+ 00b4b3a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b364 bytes 811e40f9
+ 00b4b3a8 bytes 813e40f9
- 00b4b374 ["COPY", "tmp:0:8", ["const:4e2:8"]]
- 00b4b374 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b4b374 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b4b374 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b4b3b8 ["COPY", "tmp:0:8", ["const:455:8"]]
+ 00b4b3b8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b4b3b8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b4b3b8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b4b374 bytes 63881391
+ 00b4b3b8 bytes 63541191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97fc5413fddbdc4cfeb59668d89d22fd"></a>

### [`00b4b3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b3c0.md) → [`00b4b404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b404.md) _ZN8firebase9messaging26illegal_argument_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b420",
      "incomplete_value": false,
      "site": "00b4b424",
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
            "const:547:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b3dc",
      "incomplete_value": false,
      "site": "00b4b3e0",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4b430",
      "incomplete_value": true,
      "site": "00b4b43c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b3ec",
      "incomplete_value": true,
      "site": "00b4b3f8",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b4b420",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b4b430",
      "DATA",
      [
        "storage",
        "010a1048",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b420",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b4b430",
      "DATA",
      [
        "storage",
        "010a1088",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b3e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b3c0.md#insn-00b4b3e0) · [`00b4b3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b3c0.md#insn-00b4b3dc) · [`00b4b3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b3c0.md#insn-00b4b3e8)
- 新版 `00b4b424`（命令位置の公開資料なし） · `00b4b420`（命令位置の公開資料なし） · `00b4b42c`（命令位置の公開資料なし）

~~~diff
- 00b4b3e0 ["INT_ADD", "register:40f0:8", ["const:b4b3e0:8", "const:4:8"]]
- 00b4b3e0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b4b424 ["INT_ADD", "register:40f0:8", ["const:b4b424:8", "const:4:8"]]
+ 00b4b424 ["CALL", null, ["callee:00bde180:8"]]
- 00b4b3e0 bytes 544b0294
+ 00b4b424 bytes 574b0294
- 00b4b3dc ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b4b3dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b3dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b3dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b420 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b4b420 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b420 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b420 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b3dc bytes 00501791
+ 00b4b420 bytes 001c1591
- 00b4b3e8 ["COPY", "tmp:0:8", ["const:48:8"]]
- 00b4b3e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b3e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b3e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4b42c ["COPY", "tmp:0:8", ["const:88:8"]]
+ 00b4b42c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b42c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b42c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4b3e8 bytes 08210191
+ 00b4b42c bytes 08210291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-add937e64818230c670ef74555894fb0"></a>

### [`00b4b3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b3fc.md) → [`00b4b440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b440.md) _ZN8firebase9messaging26illegal_argument_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b480",
      "incomplete_value": true,
      "site": "00b4b480",
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
            "const:78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b43c",
      "incomplete_value": true,
      "site": "00b4b43c",
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
            "const:38:8"
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
      "00b4b454",
      "READ",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b464",
      "PARAM",
      [
        "storage",
        "002954e2",
        null,
        "string"
      ]
    ],
    [
      "00b4b480",
      "WRITE",
      [
        "storage",
        "010a1038",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b454",
      "READ",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b464",
      "PARAM",
      [
        "storage",
        "00295455",
        null,
        "string"
      ]
    ],
    [
      "00b4b480",
      "WRITE",
      [
        "storage",
        "010a1078",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b3fc.md#insn-00b4b43c) · [`00b4b410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b3fc.md#insn-00b4b410) · [`00b4b420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b3fc.md#insn-00b4b420)
- 新版 `00b4b480`（命令位置の公開資料なし） · `00b4b454`（命令位置の公開資料なし） · `00b4b464`（命令位置の公開資料なし）

~~~diff
- 00b4b43c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:38:8"]]
- 00b4b43c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b480 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
+ 00b4b480 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b43c bytes 801e00f9
+ 00b4b480 bytes 803e00f9
- 00b4b410 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:38:8"]]
- 00b4b410 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b454 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:78:8"]]
+ 00b4b454 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b410 bytes 811e40f9
+ 00b4b454 bytes 813e40f9
- 00b4b420 ["COPY", "tmp:0:8", ["const:4e2:8"]]
- 00b4b420 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b4b420 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b4b420 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b4b464 ["COPY", "tmp:0:8", ["const:455:8"]]
+ 00b4b464 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b4b464 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b4b464 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b4b420 bytes 63881391
+ 00b4b464 bytes 63541191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d09f62809c4b3cf03a50d6f97cfc6d3f"></a>

### [`00b4b46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b46c.md) → [`00b4b4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b4b0.md) _ZN8firebase9messaging26illegal_argument_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b4cc",
      "incomplete_value": false,
      "site": "00b4b4d0",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b488",
      "incomplete_value": false,
      "site": "00b4b48c",
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
            "const:67f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4b4dc",
      "incomplete_value": true,
      "site": "00b4b4e8",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b498",
      "incomplete_value": true,
      "site": "00b4b4a4",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b4b4cc",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b4b4dc",
      "DATA",
      [
        "storage",
        "010a1050",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b4cc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b4b4dc",
      "DATA",
      [
        "storage",
        "010a1090",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b46c.md#insn-00b4b48c) · [`00b4b488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b46c.md#insn-00b4b488) · [`00b4b494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b46c.md#insn-00b4b494)
- 新版 `00b4b4d0`（命令位置の公開資料なし） · `00b4b4cc`（命令位置の公開資料なし） · `00b4b4d8`（命令位置の公開資料なし）

~~~diff
- 00b4b48c ["INT_ADD", "register:40f0:8", ["const:b4b48c:8", "const:4:8"]]
- 00b4b48c ["CALL", null, ["callee:00bde180:8"]]
+ 00b4b4d0 ["INT_ADD", "register:40f0:8", ["const:b4b4d0:8", "const:4:8"]]
+ 00b4b4d0 ["CALL", null, ["callee:00bde180:8"]]
- 00b4b48c bytes 294b0294
+ 00b4b4d0 bytes 2c4b0294
- 00b4b488 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b4b488 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b488 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b488 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b4cc ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b4b4cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b4cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b4cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b488 bytes 00fc1991
+ 00b4b4cc bytes 00c81791
- 00b4b494 ["COPY", "tmp:0:8", ["const:50:8"]]
- 00b4b494 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b494 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b4b494 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b4b4d8 ["COPY", "tmp:0:8", ["const:90:8"]]
+ 00b4b4d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b4d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b4b4d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b4b494 bytes 08410191
+ 00b4b4d8 bytes 08410291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d77deee09ea372f9f1e710577af20862"></a>

### [`00b4b59c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b59c.md) → [`00b4b5e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b5e0.md) _ZN8firebase9messaging17NotifyListenerSetEPNS0_8ListenerE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0340.md) · 呼出先 6件 [`00bdc930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc930.md) [`00bdd160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd160.md) [`00bdd1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1f0.md) [`00bdd3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd3c0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00be0390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0390.md) · 呼出先 6件 [`00bdc980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc980.md) [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md) [`00bdd240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd240.md) [`00bdd410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd410.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b5f8",
      "incomplete_value": true,
      "site": "00b4b5f8",
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
      "definition_site": "00b4b5b4",
      "incomplete_value": true,
      "site": "00b4b5b4",
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
      "definition_site": "00b4b670",
      "incomplete_value": true,
      "site": "00b4b670",
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
      "definition_site": "00b4b62c",
      "incomplete_value": true,
      "site": "00b4b62c",
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b644",
      "incomplete_value": false,
      "site": "00b4b648",
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
            "const:95a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b600",
      "incomplete_value": false,
      "site": "00b4b604",
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
            "const:9e7:8"
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
      "00b4b5f4",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b600",
      "READ",
      [
        "storage",
        "010a1090",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b624",
      "READ",
      [
        "storage",
        "010a1068",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b5f4",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b600",
      "READ",
      [
        "storage",
        "010a10d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b624",
      "READ",
      [
        "storage",
        "010a10a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b59c.md#insn-00b4b604) · [`00b4b5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b59c.md#insn-00b4b5b0) · [`00b4b5bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b59c.md#insn-00b4b5bc)
- 新版 `00b4b648`（命令位置の公開資料なし） · `00b4b5f4`（命令位置の公開資料なし） · `00b4b600`（命令位置の公開資料なし）

~~~diff
- 00b4b604 ["INT_ADD", "register:40f0:8", ["const:b4b604:8", "const:4:8"]]
- 00b4b604 ["CALL", null, ["callee:00bdd240:8"]]
+ 00b4b648 ["INT_ADD", "register:40f0:8", ["const:b4b648:8", "const:4:8"]]
+ 00b4b648 ["CALL", null, ["callee:00bdd240:8"]]
- 00b4b604 bytes fb460294
+ 00b4b648 bytes fe460294
- 00b4b5b0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:60:8"]]
- 00b4b5b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b5f4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a0:8"]]
+ 00b4b5f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b5b0 bytes 083140f9
+ 00b4b5f4 bytes 085140f9
- 00b4b5bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:90:8"]]
- 00b4b5bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b600 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d0:8"]]
+ 00b4b600 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b5bc bytes 084940f9
+ 00b4b600 bytes 086940f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a7a7b40fef239a41565a427a7fd1e8a"></a>

### [`00b4b688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b688.md) → [`00b4b6cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b6cc.md) _ZN8firebase9messaging17RequestPermissionEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00bddf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf70.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00bddfc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfc0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.25% / 新版 98.25%

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
      "definition_site": "00b4b6f8",
      "incomplete_value": true,
      "site": "00b4b6f8",
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
      "definition_site": "00b4b6b4",
      "incomplete_value": true,
      "site": "00b4b6b4",
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
      "definition_site": "00b4b778",
      "incomplete_value": false,
      "site": "00b4b77c",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b734",
      "incomplete_value": false,
      "site": "00b4b738",
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
            "const:16d:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b6f4",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b778",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4b6f4",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b778",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b688.md#insn-00b4b738) · [`00b4b6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b688.md#insn-00b4b6b0) · [`00b4b6b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b688.md#insn-00b4b6b8)
- 新版 `00b4b77c`（命令位置の公開資料なし） · `00b4b6f4`（命令位置の公開資料なし） · `00b4b6fc`（命令位置の公開資料なし）

~~~diff
- 00b4b738 ["INT_ADD", "register:40f0:8", ["const:b4b738:8", "const:4:8"]]
- 00b4b738 ["CALL", null, ["callee:00bde180:8"]]
+ 00b4b77c ["INT_ADD", "register:40f0:8", ["const:b4b77c:8", "const:4:8"]]
+ 00b4b77c ["CALL", null, ["callee:00bde180:8"]]
- 00b4b738 bytes 7e4a0294
+ 00b4b77c bytes 814a0294
- 00b4b6b0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:60:8"]]
- 00b4b6b0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4b6f4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a0:8"]]
+ 00b4b6f4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4b6b0 bytes 293140f9
+ 00b4b6f4 bytes 295140f9
- 00b4b6b8 ["INT_ADD", "register:40f0:8", ["const:b4b6b8:8", "const:4:8"]]
- 00b4b6b8 ["CALL", null, ["callee:00be0300:8"]]
+ 00b4b6fc ["INT_ADD", "register:40f0:8", ["const:b4b6fc:8", "const:4:8"]]
+ 00b4b6fc ["CALL", null, ["callee:00be0300:8"]]
- 00b4b6b8 bytes fe520294
+ 00b4b6fc bytes 01530294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10f4eaae7fb5b0fa054013ae7bb8b061"></a>

### [`00b4b7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b7b0.md) → [`00b4b7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b7f4.md) _ZN8firebase9messaging27RequestPermissionLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0580.md) · 呼出先 8件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md)
- 新版 呼出元 1件 [`00be05d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be05d0.md) · 呼出先 8件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b810",
      "incomplete_value": true,
      "site": "00b4b810",
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
      "definition_site": "00b4b7cc",
      "incomplete_value": true,
      "site": "00b4b7cc",
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
      "definition_site": "00b4b864",
      "incomplete_value": false,
      "site": "00b4b868",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b820",
      "incomplete_value": false,
      "site": "00b4b824",
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
            "const:16d:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00b4b7cc"
      ],
      [
        "FALL_THROUGH",
        "00b4b810"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b4b810",
      "incomplete_value": true,
      "site": "00b4b844",
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
      "definition_site": "00b4b7cc",
      "incomplete_value": true,
      "site": "00b4b800",
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
      "00b4b808",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b864",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4b808",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b864",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b7b0.md#insn-00b4b7e0) · [`00b4b824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b7b0.md#insn-00b4b824) · [`00b4b844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b7b0.md#insn-00b4b844)
- 新版 `00b4b824`（命令位置の公開資料なし） · `00b4b868`（命令位置の公開資料なし） · `00b4b888`（命令位置の公開資料なし）

~~~diff
- 00b4b7e0 ["INT_ADD", "register:40f0:8", ["const:b4b7e0:8", "const:4:8"]]
- 00b4b7e0 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b4b824 ["INT_ADD", "register:40f0:8", ["const:b4b824:8", "const:4:8"]]
+ 00b4b824 ["CALL", null, ["callee:00bddc20:8"]]
- 00b4b7e0 bytes fc480294
+ 00b4b824 bytes ff480294
- 00b4b824 ["INT_ADD", "register:40f0:8", ["const:b4b824:8", "const:4:8"]]
- 00b4b824 ["CALL", null, ["callee:00bde180:8"]]
+ 00b4b868 ["INT_ADD", "register:40f0:8", ["const:b4b868:8", "const:4:8"]]
+ 00b4b868 ["CALL", null, ["callee:00bde180:8"]]
- 00b4b824 bytes 434a0294
+ 00b4b868 bytes 464a0294
- 00b4b844 ["INT_ADD", "register:40f0:8", ["const:b4b844:8", "const:4:8"]]
- 00b4b844 ["CALL", null, ["callee:00bddd80:8"]]
+ 00b4b888 ["INT_ADD", "register:40f0:8", ["const:b4b888:8", "const:4:8"]]
+ 00b4b888 ["CALL", null, ["callee:00bddd80:8"]]
- 00b4b844 bytes 3b490294
+ 00b4b888 bytes 3e490294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1932294a5cf3915f82630cbce6a9adf6"></a>

### [`00b4b884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b884.md) → [`00b4b8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b8c8.md) _ZN8firebase9messaging15ProcessMessagesEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0570.md) · 呼出先 39件 [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00b4e898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e898.md) [`00b4e89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e89c.md)
- 新版 呼出元 1件 [`00be05c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be05c0.md) · 呼出先 39件 [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00b4e8dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e8dc.md) [`00b4e8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e8e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 98.27% / 新版 98.27%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件, `store_value` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4b954",
      "incomplete_value": true,
      "site": "00b4b954",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b910",
      "incomplete_value": true,
      "site": "00b4b910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:88:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b4c348",
      "incomplete_value": false,
      "site": "00b4c348",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b4e000:8"
          ],
          [
            "leaf",
            "const:8dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c304",
      "incomplete_value": false,
      "site": "00b4c304",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b4e000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "ordinal": 111,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4b908",
      "incomplete_value": true,
      "site": "00b4b908",
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
      "definition_site": "00b4b8c4",
      "incomplete_value": true,
      "site": "00b4b8c4",
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
      "00b4b8f4",
      "PARAM",
      [
        "storage",
        "010a0f68",
        null,
        null
      ]
    ],
    [
      "00b4b904",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b920",
      "PARAM",
      [
        "storage",
        "010a0f68",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b8f4",
      "PARAM",
      [
        "storage",
        "010a0fa8",
        null,
        null
      ]
    ],
    [
      "00b4b904",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b920",
      "PARAM",
      [
        "storage",
        "010a0fa8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b884.md#insn-00b4b8b8) · [`00b4b8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b884.md#insn-00b4b8e0) · [`00b4b8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b884.md#insn-00b4b8fc)
- 新版 `00b4b8fc`（命令位置の公開資料なし） · `00b4b924`（命令位置の公開資料なし） · `00b4b940`（命令位置の公開資料なし）

~~~diff
- 00b4b8b8 ["INT_ADD", "register:40f0:8", ["const:b4b8b8:8", "const:4:8"]]
- 00b4b8b8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b4b8fc ["INT_ADD", "register:40f0:8", ["const:b4b8fc:8", "const:4:8"]]
+ 00b4b8fc ["CALL", null, ["callee:00bddc20:8"]]
- 00b4b8b8 bytes c6480294
+ 00b4b8fc bytes c9480294
- 00b4b8e0 ["INT_ADD", "register:40f0:8", ["const:b4b8e0:8", "const:4:8"]]
- 00b4b8e0 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b4b924 ["INT_ADD", "register:40f0:8", ["const:b4b924:8", "const:4:8"]]
+ 00b4b924 ["CALL", null, ["callee:00bddc30:8"]]
- 00b4b8e0 bytes c0480294
+ 00b4b924 bytes c3480294
- 00b4b8fc ["INT_ADD", "register:40f0:8", ["const:b4b8fc:8", "const:4:8"]]
- 00b4b8fc ["CALL", null, ["callee:00be0330:8"]]
+ 00b4b940 ["INT_ADD", "register:40f0:8", ["const:b4b940:8", "const:4:8"]]
+ 00b4b940 ["CALL", null, ["callee:00be0330:8"]]
- 00b4b8fc bytes 79520294
+ 00b4b940 bytes 7c520294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca84e4696ab638e8b23baf5a61056a3d"></a>

### [`00b4c480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c480.md) → [`00b4c4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4c4c4.md) _ZN8firebase9messaging10InitializeERKNS_3AppEPNS0_8ListenerERKNS0_16MessagingOptionsE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0560.md) · 呼出先 33件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00b4c9a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c9a8.md) [`00b4ca64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ca64.md)
- 新版 呼出元 1件 [`00be05b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be05b0.md) · 呼出先 33件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) [`00b4c9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4c9ec.md) [`00b4caa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4caa8.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 85.05% / 新版 85.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 20件, `store_condition` 1件, `store_destination` 15件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4c598",
      "incomplete_value": true,
      "site": "00b4c598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c554",
      "incomplete_value": true,
      "site": "00b4c554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:fb8:8"
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4c5f0",
      "incomplete_value": true,
      "site": "00b4c5f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c5ac",
      "incomplete_value": true,
      "site": "00b4c5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4c62c",
      "incomplete_value": true,
      "site": "00b4c62c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c5e8",
      "incomplete_value": true,
      "site": "00b4c5e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b8:8"
          ],
          [
            "leaf",
            "const:60:8"
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
      "00b4c514",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c520",
      "PARAM",
      [
        "storage",
        "002942c2",
        null,
        "string"
      ]
    ],
    [
      "00b4c570",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c514",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c520",
      "PARAM",
      [
        "storage",
        "00294235",
        null,
        "string"
      ]
    ],
    [
      "00b4c570",
      "READ",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c480.md#insn-00b4c4e0) · [`00b4c554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c480.md#insn-00b4c554) · [`00b4c568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c480.md#insn-00b4c568)
- 新版 `00b4c524`（命令位置の公開資料なし） · `00b4c598`（命令位置の公開資料なし） · `00b4c5ac`（命令位置の公開資料なし）

~~~diff
- 00b4c4e0 ["INT_ADD", "register:40f0:8", ["const:b4c4e0:8", "const:4:8"]]
- 00b4c4e0 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b4c524 ["INT_ADD", "register:40f0:8", ["const:b4c524:8", "const:4:8"]]
+ 00b4c524 ["CALL", null, ["callee:00bdde40:8"]]
- 00b4c4e0 bytes 44460294
+ 00b4c524 bytes 47460294
- 00b4c554 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:fb8:8"]]
- 00b4c554 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c598 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:ff8:8"]]
+ 00b4c598 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c554 bytes 00df07f9
+ 00b4c598 bytes 00ff07f9
- 00b4c568 ["COPY", "tmp:0:8", ["const:fc8:8"]]
- 00b4c568 ["INT_CARRY", "register:105:1", ["register:4020:8", "tmp:0:8"]]
- 00b4c568 ["INT_SCARRY", "register:106:1", ["register:4020:8", "tmp:0:8"]]
- 00b4c568 ["INT_ADD", "tmp:1:8", ["register:4020:8", "tmp:0:8"]]
+ 00b4c5ac ["COPY", "tmp:0:8", ["const:8:8"]]
+ 00b4c5ac ["INT_CARRY", "register:105:1", ["register:4020:8", "tmp:0:8"]]
+ 00b4c5ac ["INT_SCARRY", "register:106:1", ["register:4020:8", "tmp:0:8"]]
+ 00b4c5ac ["INT_ADD", "tmp:1:8", ["register:4020:8", "tmp:0:8"]]
- 00b4c568 bytes 84203f91
+ 00b4c5ac bytes 84200091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-480816ec7e5d5ab281b5b1702ff85cce"></a>

### [`00b4c9a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c9a8.md) → [`00b4c9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4c9ec.md) FUN_00b4c9ec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b4c480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c480.md) [`00b4ce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ce90.md) · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 2件 [`00b4c4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4c4c4.md) [`00b4ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4ced4.md) · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 82.98% / 新版 82.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4ca28",
      "incomplete_value": true,
      "site": "00b4ca28",
      "value": [
        "live",
        "register:40a8:8"
      ]
    },
    "old": {
      "definition_site": "00b4c9e4",
      "incomplete_value": true,
      "site": "00b4c9e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:fc0:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4ca48",
      "incomplete_value": true,
      "site": "00b4ca48",
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
            "const:ff8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ca04",
      "incomplete_value": true,
      "site": "00b4ca04",
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
            "const:fb8:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4ca74",
      "incomplete_value": true,
      "site": "00b4ca74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ca30",
      "incomplete_value": true,
      "site": "00b4ca30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:20:8"
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
      "00b4ca00",
      "READ",
      [
        "storage",
        "010a0fb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ca10",
      "READ",
      [
        "storage",
        "010a0fc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ca28",
      "WRITE",
      [
        "storage",
        "010a0fc0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4ca00",
      "READ",
      [
        "storage",
        "010a0ff8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ca10",
      "READ",
      [
        "storage",
        "010a1000",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4ca28",
      "WRITE",
      [
        "storage",
        "010a1000",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c9a8.md#insn-00b4c9cc) · [`00b4c9e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c9a8.md#insn-00b4c9e4) · [`00b4c9ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c9a8.md#insn-00b4c9ec)
- 新版 `00b4ca10`（命令位置の公開資料なし） · `00b4ca28`（命令位置の公開資料なし） · `00b4ca30`（命令位置の公開資料なし）

~~~diff
- 00b4c9cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:fc0:8"]]
- 00b4c9cc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4c9cc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4ca10 ["COPY", "tmp:0:8", ["register:40a8:8"]]
+ 00b4ca10 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4ca10 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4c9cc bytes a8027f39
+ 00b4ca10 bytes a8024039
- 00b4c9e4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4c9e4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4c9e4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:fc0:8"]]
- 00b4c9e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4ca28 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4ca28 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4ca28 ["COPY", "tmp:2:8", ["register:40a8:8"]]
+ 00b4ca28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4c9e4 bytes bf023f39
+ 00b4ca28 bytes bf020039
- 00b4c9ec ["INT_ADD", "register:40f0:8", ["const:b4c9ec:8", "const:4:8"]]
- 00b4c9ec ["CALL", null, ["callee:00bde0e0:8"]]
+ 00b4ca30 ["INT_ADD", "register:40f0:8", ["const:b4ca30:8", "const:4:8"]]
+ 00b4ca30 ["CALL", null, ["callee:00bde0e0:8"]]
- 00b4c9ec bytes a9450294
+ 00b4ca30 bytes ac450294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23b5e2c4e6df31bdb55fa7083b466471"></a>

### [`00b4ca64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ca64.md) → [`00b4caa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4caa8.md) FUN_00b4caa8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b4c480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c480.md) · 呼出先 11件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb220.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00b4c4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4c4c4.md) · 呼出先 11件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb270.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.55% / 新版 93.55%

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
      "definition_site": "00b4cae8",
      "incomplete_value": true,
      "site": "00b4cae8",
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
      "definition_site": "00b4caa4",
      "incomplete_value": true,
      "site": "00b4caa4",
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
      "definition_site": "00b4cad4",
      "incomplete_value": false,
      "site": "00b4cadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ca90",
      "incomplete_value": false,
      "site": "00b4ca98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "definition_site": "00b4cb00",
      "incomplete_value": false,
      "site": "00b4cb04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:fa8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cabc",
      "incomplete_value": false,
      "site": "00b4cac0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:f68:8"
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
      "00b4cad4",
      "PARAM",
      [
        "storage",
        "010a0f68",
        null,
        null
      ]
    ],
    [
      "00b4cae4",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cb00",
      "PARAM",
      [
        "storage",
        "010a0f68",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4cad4",
      "PARAM",
      [
        "storage",
        "010a0fa8",
        null,
        null
      ]
    ],
    [
      "00b4cae4",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cb00",
      "PARAM",
      [
        "storage",
        "010a0fa8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ca98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ca64.md#insn-00b4ca98) · [`00b4cac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ca64.md#insn-00b4cac0) · [`00b4cb04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ca64.md#insn-00b4cb04)
- 新版 `00b4cadc`（命令位置の公開資料なし） · `00b4cb04`（命令位置の公開資料なし） · `00b4cb48`（命令位置の公開資料なし）

~~~diff
- 00b4ca98 ["INT_ADD", "register:40f0:8", ["const:b4ca98:8", "const:4:8"]]
- 00b4ca98 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b4cadc ["INT_ADD", "register:40f0:8", ["const:b4cadc:8", "const:4:8"]]
+ 00b4cadc ["CALL", null, ["callee:00bddc20:8"]]
- 00b4ca98 bytes 4e440294
+ 00b4cadc bytes 51440294
- 00b4cac0 ["INT_ADD", "register:40f0:8", ["const:b4cac0:8", "const:4:8"]]
- 00b4cac0 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b4cb04 ["INT_ADD", "register:40f0:8", ["const:b4cb04:8", "const:4:8"]]
+ 00b4cb04 ["CALL", null, ["callee:00bddc30:8"]]
- 00b4cac0 bytes 48440294
+ 00b4cb04 bytes 4b440294
- 00b4cb04 ["INT_ADD", "register:40f0:8", ["const:b4cb04:8", "const:4:8"]]
- 00b4cb04 ["CALL", null, ["callee:00be0610:8"]]
+ 00b4cb48 ["INT_ADD", "register:40f0:8", ["const:b4cb48:8", "const:4:8"]]
+ 00b4cb48 ["CALL", null, ["callee:00be0610:8"]]
- 00b4cb04 bytes af4e0294
+ 00b4cb48 bytes b24e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d9ca49d86fff82a032b3d991eaae185"></a>

### [`00b4cbfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cbfc.md) → [`00b4cc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4cc40.md) _ZN8firebase9messaging33SetTokenRegistrationOnInitEnabledEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bddc40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc40.md) · 呼出先 6件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00b4cda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cda8.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bddc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc90.md) · 呼出先 6件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00b4cdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4cdec.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition, store_destination

命令の説明率　旧版 71.25% / 新版 71.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 7件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4cd3c",
      "incomplete_value": false,
      "site": "00b4cd3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ccf8",
      "incomplete_value": false,
      "site": "00b4ccf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:100:8"
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
      "definition_site": "00b4cc60",
      "incomplete_value": true,
      "site": "00b4cc60",
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
      "definition_site": "00b4cc1c",
      "incomplete_value": true,
      "site": "00b4cc1c",
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
      "definition_site": "00b4cc74",
      "incomplete_value": true,
      "site": "00b4cc74",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4cc30",
      "incomplete_value": true,
      "site": "00b4cc30",
      "value": [
        "INT_NOTEQUAL",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4cc58",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc6c",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc7c",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4cc58",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc6c",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc7c",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cbfc.md#insn-00b4cc3c) · [`00b4cc44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cbfc.md#insn-00b4cc44) · [`00b4cc48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cbfc.md#insn-00b4cc48)
- 新版 `00b4cc80`（命令位置の公開資料なし） · `00b4cc88`（命令位置の公開資料なし） · `00b4cc8c`（命令位置の公開資料なし）

~~~diff
- 00b4cc3c ["INT_ADD", "register:40f0:8", ["const:b4cc3c:8", "const:4:8"]]
- 00b4cc3c ["CALL", null, ["callee:00bdde40:8"]]
+ 00b4cc80 ["INT_ADD", "register:40f0:8", ["const:b4cc80:8", "const:4:8"]]
+ 00b4cc80 ["CALL", null, ["callee:00bdde40:8"]]
- 00b4cc3c bytes 6d440294
+ 00b4cc80 bytes 70440294
- 00b4cc44 ["COPY", "tmp:0:8", ["const:116:8"]]
- 00b4cc44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cc44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cc44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4cc88 ["COPY", "tmp:0:8", ["const:1a1:8"]]
+ 00b4cc88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cc88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cc88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4cc44 bytes 00580491
+ 00b4cc88 bytes 00840691
- 00b4cc48 ["INT_ADD", "register:40f0:8", ["const:b4cc48:8", "const:4:8"]]
- 00b4cc48 ["CALL", null, ["callee:00bde180:8"]]
+ 00b4cc8c ["INT_ADD", "register:40f0:8", ["const:b4cc8c:8", "const:4:8"]]
+ 00b4cc8c ["CALL", null, ["callee:00bde180:8"]]
- 00b4cc48 bytes 3a450294
+ 00b4cc8c bytes 3d450294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c47edcd05f13eda777b425ff661b1bf"></a>

### [`00b4cd3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cd3c.md) → [`00b4cd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4cd80.md) _ZN8firebase9messaging32IsTokenRegistrationOnInitEnabledEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4cd94",
      "incomplete_value": true,
      "site": "00b4cd94",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4cd50",
      "incomplete_value": true,
      "site": "00b4cd50",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b4cdb4",
      "incomplete_value": true,
      "site": "00b4cdb4",
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
      "definition_site": "00b4cd70",
      "incomplete_value": true,
      "site": "00b4cd70",
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
      "definition_site": "00b4cd9c",
      "incomplete_value": true,
      "site": "00b4cda0",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cd58",
      "incomplete_value": true,
      "site": "00b4cd5c",
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
            "const:16d:8"
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
      "00b4cd90",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cd9c",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ],
    [
      "00b4cda8",
      "PARAM",
      [
        "storage",
        "002a0116",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4cd90",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cd9c",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ],
    [
      "00b4cda8",
      "PARAM",
      [
        "storage",
        "002a01a1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cd5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cd3c.md#insn-00b4cd5c) · [`00b4cd68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cd3c.md#insn-00b4cd68) · [`00b4cd88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cd3c.md#insn-00b4cd88)
- 新版 `00b4cda0`（命令位置の公開資料なし） · `00b4cdac`（命令位置の公開資料なし） · `00b4cdcc`（命令位置の公開資料なし）

~~~diff
- 00b4cd5c ["INT_ADD", "register:40f0:8", ["const:b4cd5c:8", "const:4:8"]]
- 00b4cd5c ["CALL", null, ["callee:00bdde40:8"]]
+ 00b4cda0 ["INT_ADD", "register:40f0:8", ["const:b4cda0:8", "const:4:8"]]
+ 00b4cda0 ["CALL", null, ["callee:00bdde40:8"]]
- 00b4cd5c bytes 25440294
+ 00b4cda0 bytes 28440294
- 00b4cd68 ["INT_ADD", "register:40f0:8", ["const:b4cd68:8", "const:4:8"]]
- 00b4cd68 ["CALL", null, ["callee:00bde180:8"]]
+ 00b4cdac ["INT_ADD", "register:40f0:8", ["const:b4cdac:8", "const:4:8"]]
+ 00b4cdac ["CALL", null, ["callee:00bde180:8"]]
- 00b4cd68 bytes f2440294
+ 00b4cdac bytes f5440294
- 00b4cd88 ["INT_ADD", "register:40f0:8", ["const:b4cd88:8", "const:4:8"]]
- 00b4cd88 ["CALL", null, ["callee:00474b70:8"]]
+ 00b4cdcc ["INT_ADD", "register:40f0:8", ["const:b4cdcc:8", "const:4:8"]]
+ 00b4cdcc ["CALL", null, ["callee:00474b70:8"]]
- 00b4cd88 bytes 7a9fe497
+ 00b4cdcc bytes 699fe497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9001914785fb4b8f110ad0b928c59d8f"></a>

### [`00b4cda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cda8.md) → [`00b4cdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4cdec.md) FUN_00b4cdec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b4c480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c480.md) [`00b4cbfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cbfc.md) · 呼出先 8件 [`00848b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00848/00848b34.md) [`00b4ea4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ea4c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 2件 [`00b4c4c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4c4c4.md) [`00b4cc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4cc40.md) · 呼出先 8件 [`00848b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00848/00848b34.md) [`00b4ea90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ea90.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.62% / 新版 93.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4ce10",
      "incomplete_value": true,
      "site": "00b4ce10",
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
      "definition_site": "00b4cdcc",
      "incomplete_value": true,
      "site": "00b4cdcc",
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
      "definition_site": "00b4ce40",
      "incomplete_value": false,
      "site": "00b4ce54",
      "value": [
        "leaf",
        "const:b4ea90:8"
      ]
    },
    "old": {
      "definition_site": "00b4cdfc",
      "incomplete_value": false,
      "site": "00b4ce10",
      "value": [
        "leaf",
        "const:b4ea4c:8"
      ]
    },
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ce70",
      "incomplete_value": false,
      "site": "00b4ce74",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ce2c",
      "incomplete_value": false,
      "site": "00b4ce30",
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
            "const:16d:8"
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
      "00b4ce0c",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ce40",
      "PARAM",
      [
        "storage",
        "00b4ea4c",
        null,
        null
      ]
    ],
    [
      "00b4ce70",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4ce0c",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ce40",
      "PARAM",
      [
        "storage",
        "00b4ea90",
        null,
        null
      ]
    ],
    [
      "00b4ce70",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ce10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cda8.md#insn-00b4ce10) · [`00b4ce30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cda8.md#insn-00b4ce30) · [`00b4ce3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cda8.md#insn-00b4ce3c)
- 新版 `00b4ce54`（命令位置の公開資料なし） · `00b4ce74`（命令位置の公開資料なし） · `00b4ce80`（命令位置の公開資料なし）

~~~diff
- 00b4ce10 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b4ce10 ["INT_ADD", "register:40f0:8", ["const:b4ce10:8", "const:4:8"]]
- 00b4ce10 ["CALLIND", null, ["register:0:8"]]
+ 00b4ce54 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b4ce54 ["INT_ADD", "register:40f0:8", ["const:b4ce54:8", "const:4:8"]]
+ 00b4ce54 ["CALLIND", null, ["register:0:8"]]
- 00b4ce10 bytes 20013fd6
+ 00b4ce54 bytes 20013fd6
- 00b4ce30 ["INT_ADD", "register:40f0:8", ["const:b4ce30:8", "const:4:8"]]
- 00b4ce30 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b4ce74 ["INT_ADD", "register:40f0:8", ["const:b4ce74:8", "const:4:8"]]
+ 00b4ce74 ["CALL", null, ["callee:00bdde40:8"]]
- 00b4ce30 bytes f0430294
+ 00b4ce74 bytes f3430294
- 00b4ce3c ["INT_ADD", "register:40f0:8", ["const:b4ce3c:8", "const:4:8"]]
- 00b4ce3c ["CALL", null, ["callee:00bde180:8"]]
+ 00b4ce80 ["INT_ADD", "register:40f0:8", ["const:b4ce80:8", "const:4:8"]]
+ 00b4ce80 ["CALL", null, ["callee:00bde180:8"]]
- 00b4ce3c bytes bd440294
+ 00b4ce80 bytes c0440294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcdf3efe24dd4657bed57c8f5a112fd2"></a>

### [`00b4ce90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ce90.md) → [`00b4ced4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4ced4.md) _ZN8firebase9messaging9TerminateEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0420.md) · 呼出先 23件 [`00b4c9a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4c9a8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdc930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc930.md) [`00bdd160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd160.md) [`00bdd1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1f0.md)
- 新版 呼出元 1件 [`00be0470`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0470.md) · 呼出先 23件 [`00b4c9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4c9ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdc980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc980.md) [`00bdd1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd1b0.md) [`00bdd240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd240.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 86.50% / 新版 86.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 3件, `call_argument_candidate` 8件, `store_destination` 9件

アドレスに依存する影響 `branch_value` 3件, `call_argument_candidate` 2件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4cf24",
      "incomplete_value": true,
      "site": "00b4cf24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cee0",
      "incomplete_value": true,
      "site": "00b4cee0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:60:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4d040",
      "incomplete_value": true,
      "site": "00b4d040",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cffc",
      "incomplete_value": true,
      "site": "00b4cffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:70:8"
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4d060",
      "incomplete_value": true,
      "site": "00b4d060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d01c",
      "incomplete_value": true,
      "site": "00b4d01c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c0:8"
          ],
          [
            "leaf",
            "const:58:8"
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
      "00b4cef0",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cefc",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cf1c",
      "PARAM",
      [
        "storage",
        "010a0f68",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4cef0",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cefc",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cf1c",
      "PARAM",
      [
        "storage",
        "010a0fa8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ce90.md#insn-00b4cebc) · [`00b4cedc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ce90.md#insn-00b4cedc) · [`00b4cee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4ce90.md#insn-00b4cee0)
- 新版 `00b4cf00`（命令位置の公開資料なし） · `00b4cf20`（命令位置の公開資料なし） · `00b4cf24`（命令位置の公開資料なし）

~~~diff
- 00b4cebc ["INT_ADD", "register:40f0:8", ["const:b4cebc:8", "const:4:8"]]
- 00b4cebc ["CALL", null, ["callee:00bde200:8"]]
+ 00b4cf00 ["INT_ADD", "register:40f0:8", ["const:b4cf00:8", "const:4:8"]]
+ 00b4cf00 ["CALL", null, ["callee:00bde200:8"]]
- 00b4cebc bytes bd440294
+ 00b4cf00 bytes c0440294
- 00b4cedc ["INT_ADD", "register:40f0:8", ["const:b4cedc:8", "const:4:8"]]
- 00b4cedc ["CALL", null, ["callee:00bddc20:8"]]
+ 00b4cf20 ["INT_ADD", "register:40f0:8", ["const:b4cf20:8", "const:4:8"]]
+ 00b4cf20 ["CALL", null, ["callee:00bddc20:8"]]
- 00b4cedc bytes 3d430294
+ 00b4cf20 bytes 40430294
- 00b4cee0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:60:8"]]
- 00b4cee0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4cee0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4cf24 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a0:8"]]
+ 00b4cf24 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4cf24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4cee0 bytes bf3200f9
+ 00b4cf24 bytes bf5200f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eca5e701cf4b5a656286500fa7c4df50"></a>

### [`00b4d204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d204.md) → [`00b4d248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4d248.md) _ZN8firebase9messaging9SubscribeEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 18件 [`00b4d4d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d4d4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00b4d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4d518.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.83% / 新版 97.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d27c",
      "incomplete_value": true,
      "site": "00b4d27c",
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
      "definition_site": "00b4d238",
      "incomplete_value": true,
      "site": "00b4d238",
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
      "definition_site": "00b4d368",
      "incomplete_value": true,
      "site": "00b4d368",
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
      "definition_site": "00b4d324",
      "incomplete_value": true,
      "site": "00b4d324",
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d28c",
      "incomplete_value": true,
      "site": "00b4d290",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d248",
      "incomplete_value": true,
      "site": "00b4d24c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:70:8"
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
      "00b4d278",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d284",
      "READ",
      [
        "storage",
        "010a1070",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d2c8",
      "READ",
      [
        "storage",
        "010a1108",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d278",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d284",
      "READ",
      [
        "storage",
        "010a10b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d2c8",
      "READ",
      [
        "storage",
        "010a1148",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d204.md#insn-00b4d24c) · [`00b4d27c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d204.md#insn-00b4d27c) · [`00b4d284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d204.md#insn-00b4d284)
- 新版 `00b4d290`（命令位置の公開資料なし） · `00b4d2c0`（命令位置の公開資料なし） · `00b4d2c8`（命令位置の公開資料なし）

~~~diff
- 00b4d24c ["INT_ADD", "register:40f0:8", ["const:b4d24c:8", "const:4:8"]]
- 00b4d24c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b4d290 ["INT_ADD", "register:40f0:8", ["const:b4d290:8", "const:4:8"]]
+ 00b4d290 ["CALL", null, ["callee:00bddc20:8"]]
- 00b4d24c bytes 61420294
+ 00b4d290 bytes 64420294
- 00b4d27c ["INT_ADD", "register:40f0:8", ["const:b4d27c:8", "const:4:8"]]
- 00b4d27c ["CALL", null, ["callee:00bddc40:8"]]
+ 00b4d2c0 ["INT_ADD", "register:40f0:8", ["const:b4d2c0:8", "const:4:8"]]
+ 00b4d2c0 ["CALL", null, ["callee:00bddc40:8"]]
- 00b4d27c bytes 5d420294
+ 00b4d2c0 bytes 60420294
- 00b4d284 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:108:8"]]
- 00b4d284 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4d284 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4d2c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 00b4d2c8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d2c8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4d284 bytes 08214439
+ 00b4d2c8 bytes 08214539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06d919794622b21853cb575c07c40845"></a>

### [`00b4d4d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d4d4.md) → [`00b4d518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4d518.md) FUN_00b4d518

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b4d204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d204.md) [`00b4e904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e904.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b4eb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4eb14.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00b4d248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4d248.md) [`00b4e948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e948.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b4eb58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4eb58.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.40% / 新版 96.40%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d558",
      "incomplete_value": true,
      "site": "00b4d55c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d514",
      "incomplete_value": true,
      "site": "00b4d518",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:60:8"
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
      "definition_site": "00b4d57c",
      "incomplete_value": true,
      "site": "00b4d590",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d538",
      "incomplete_value": true,
      "site": "00b4d54c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:98:8"
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
      "definition_site": "00b4d580",
      "incomplete_value": true,
      "site": "00b4d590",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
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
      "definition_site": "00b4d53c",
      "incomplete_value": true,
      "site": "00b4d54c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:fd8:8"
              ]
            ]
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
      "00b4d544",
      "PARAM",
      [
        "storage",
        "0029dfbc",
        null,
        "string"
      ]
    ],
    [
      "00b4d558",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d57c",
      "READ",
      [
        "storage",
        "010a1098",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d544",
      "PARAM",
      [
        "storage",
        "0029e047",
        null,
        "string"
      ]
    ],
    [
      "00b4d558",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d57c",
      "READ",
      [
        "storage",
        "010a10d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d4d4.md#insn-00b4d518) · [`00b4d54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d4d4.md#insn-00b4d54c) · [`00b4d4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d4d4.md#insn-00b4d4f8)
- 新版 `00b4d55c`（命令位置の公開資料なし） · `00b4d590`（命令位置の公開資料なし） · `00b4d53c`（命令位置の公開資料なし）

~~~diff
- 00b4d518 ["INT_ADD", "register:40f0:8", ["const:b4d518:8", "const:4:8"]]
- 00b4d518 ["CALL", null, ["callee:00bde200:8"]]
+ 00b4d55c ["INT_ADD", "register:40f0:8", ["const:b4d55c:8", "const:4:8"]]
+ 00b4d55c ["CALL", null, ["callee:00bde200:8"]]
- 00b4d518 bytes 26430294
+ 00b4d55c bytes 29430294
- 00b4d54c ["INT_ADD", "register:40f0:8", ["const:b4d54c:8", "const:4:8"]]
- 00b4d54c ["CALL", null, ["callee:0047495c:8"]]
+ 00b4d590 ["INT_ADD", "register:40f0:8", ["const:b4d590:8", "const:4:8"]]
+ 00b4d590 ["CALL", null, ["callee:0047495c:8"]]
- 00b4d54c bytes 049de497
+ 00b4d590 bytes f39ce497
- 00b4d4f8 ["COPY", "register:4000:8", ["const:29d000:8"]]
+ 00b4d53c ["COPY", "register:4000:8", ["const:29e000:8"]]
- 00b4d4f8 bytes 80baff90
+ 00b4d53c bytes 80baffb0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6647c808b9dbc09c81e8d815d22fad5d"></a>

### [`00b4d6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d6d0.md) → [`00b4d714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4d714.md) _ZN8firebase9messaging19SubscribeLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d784",
      "incomplete_value": false,
      "site": "00b4d788",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d740",
      "incomplete_value": false,
      "site": "00b4d744",
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
            "const:16d:8"
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
      "00b4d728",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d784",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4d728",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d784",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d6d0.md#insn-00b4d700) · [`00b4d744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d6d0.md#insn-00b4d744) · [`00b4d6e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d6d0.md#insn-00b4d6e4)
- 新版 `00b4d744`（命令位置の公開資料なし） · `00b4d788`（命令位置の公開資料なし） · `00b4d728`（命令位置の公開資料なし）

~~~diff
- 00b4d700 ["INT_ADD", "register:40f0:8", ["const:b4d700:8", "const:4:8"]]
- 00b4d700 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b4d744 ["INT_ADD", "register:40f0:8", ["const:b4d744:8", "const:4:8"]]
+ 00b4d744 ["CALL", null, ["callee:00bddc20:8"]]
- 00b4d700 bytes 34410294
+ 00b4d744 bytes 37410294
- 00b4d744 ["INT_ADD", "register:40f0:8", ["const:b4d744:8", "const:4:8"]]
- 00b4d744 ["CALL", null, ["callee:00bde180:8"]]
+ 00b4d788 ["INT_ADD", "register:40f0:8", ["const:b4d788:8", "const:4:8"]]
+ 00b4d788 ["CALL", null, ["callee:00bde180:8"]]
- 00b4d744 bytes 7b420294
+ 00b4d788 bytes 7e420294
- 00b4d6e4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:60:8"]]
- 00b4d6e4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d728 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a0:8"]]
+ 00b4d728 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4d6e4 bytes 293140f9
+ 00b4d728 bytes 295140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f2a9c865b24651e5ed7352d492ab6c6d"></a>

### [`00b4d7a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d7a8.md) → [`00b4d7ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4d7ec.md) _ZN8firebase9messaging11UnsubscribeEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 18件 [`00b4da78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4da78.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 18件 [`00b4dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4dabc.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.38% / 新版 96.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d820",
      "incomplete_value": true,
      "site": "00b4d820",
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
      "definition_site": "00b4d7dc",
      "incomplete_value": true,
      "site": "00b4d7dc",
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
      "definition_site": "00b4d90c",
      "incomplete_value": true,
      "site": "00b4d90c",
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
      "definition_site": "00b4d8c8",
      "incomplete_value": true,
      "site": "00b4d8c8",
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
    "ordinal": 3,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d88c",
      "incomplete_value": true,
      "site": "00b4d890",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d848",
      "incomplete_value": true,
      "site": "00b4d84c",
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
            "const:16d:8"
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
      "00b4d81c",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d828",
      "READ",
      [
        "storage",
        "010a1070",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d86c",
      "READ",
      [
        "storage",
        "010a1108",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d81c",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d828",
      "READ",
      [
        "storage",
        "010a10b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d86c",
      "READ",
      [
        "storage",
        "010a1148",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d7a8.md#insn-00b4d820) · [`00b4d828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d7a8.md#insn-00b4d828) · [`00b4d84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d7a8.md#insn-00b4d84c)
- 新版 `00b4d864`（命令位置の公開資料なし） · `00b4d86c`（命令位置の公開資料なし） · `00b4d890`（命令位置の公開資料なし）

~~~diff
- 00b4d820 ["INT_ADD", "register:40f0:8", ["const:b4d820:8", "const:4:8"]]
- 00b4d820 ["CALL", null, ["callee:00bddc40:8"]]
+ 00b4d864 ["INT_ADD", "register:40f0:8", ["const:b4d864:8", "const:4:8"]]
+ 00b4d864 ["CALL", null, ["callee:00bddc40:8"]]
- 00b4d820 bytes f4400294
+ 00b4d864 bytes f7400294
- 00b4d828 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:108:8"]]
- 00b4d828 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b4d828 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b4d86c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:148:8"]]
+ 00b4d86c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d86c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b4d828 bytes 08214439
+ 00b4d86c bytes 08214539
- 00b4d84c ["INT_ADD", "register:40f0:8", ["const:b4d84c:8", "const:4:8"]]
- 00b4d84c ["CALL", null, ["callee:00bdde40:8"]]
+ 00b4d890 ["INT_ADD", "register:40f0:8", ["const:b4d890:8", "const:4:8"]]
+ 00b4d890 ["CALL", null, ["callee:00bdde40:8"]]
- 00b4d84c bytes 69410294
+ 00b4d890 bytes 6c410294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-57048c2fc68e4ae2cd83f058ef4925df"></a>

### [`00b4da78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4da78.md) → [`00b4dabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4dabc.md) FUN_00b4dabc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b4d7a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4d7a8.md) [`00b4e904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e904.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b4eb14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4eb14.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00b4d7ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4d7ec.md) [`00b4e948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e948.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b4eb58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4eb58.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.50% / 新版 95.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4dae8",
      "incomplete_value": true,
      "site": "00b4daf4",
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
            "const:55d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4daa4",
      "incomplete_value": true,
      "site": "00b4dab0",
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
            "const:5f1:8"
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
      "definition_site": "00b4dafc",
      "incomplete_value": true,
      "site": "00b4db00",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dab8",
      "incomplete_value": true,
      "site": "00b4dabc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:60:8"
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
      "definition_site": "00b4dc04",
      "incomplete_value": false,
      "site": "00b4dc18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b4e000:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dbc0",
      "incomplete_value": false,
      "site": "00b4dbd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b4e000:8"
          ],
          [
            "leaf",
            "const:b14:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4dae8",
      "PARAM",
      [
        "storage",
        "002af5f1",
        null,
        "string"
      ]
    ],
    [
      "00b4dafc",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db20",
      "READ",
      [
        "storage",
        "010a1098",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dae8",
      "PARAM",
      [
        "storage",
        "002af55d",
        null,
        "string"
      ]
    ],
    [
      "00b4dafc",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db20",
      "READ",
      [
        "storage",
        "010a10d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4da78.md#insn-00b4dab0) · [`00b4dabc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4da78.md#insn-00b4dabc) · [`00b4dbd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4da78.md#insn-00b4dbd4)
- 新版 `00b4daf4`（命令位置の公開資料なし） · `00b4db00`（命令位置の公開資料なし） · `00b4dc18`（命令位置の公開資料なし）

~~~diff
- 00b4dab0 ["INT_ADD", "register:40f0:8", ["const:b4dab0:8", "const:4:8"]]
- 00b4dab0 ["CALL", null, ["callee:00bde2b0:8"]]
+ 00b4daf4 ["INT_ADD", "register:40f0:8", ["const:b4daf4:8", "const:4:8"]]
+ 00b4daf4 ["CALL", null, ["callee:00bde2b0:8"]]
- 00b4dab0 bytes ec410294
+ 00b4daf4 bytes ef410294
- 00b4dabc ["INT_ADD", "register:40f0:8", ["const:b4dabc:8", "const:4:8"]]
- 00b4dabc ["CALL", null, ["callee:00bde200:8"]]
+ 00b4db00 ["INT_ADD", "register:40f0:8", ["const:b4db00:8", "const:4:8"]]
+ 00b4db00 ["CALL", null, ["callee:00bde200:8"]]
- 00b4dabc bytes bd410294
+ 00b4db00 bytes c0410294
- 00b4dbd4 ["INT_ADD", "register:40f0:8", ["const:b4dbd4:8", "const:4:8"]]
- 00b4dbd4 ["CALL", null, ["callee:00bde0c0:8"]]
+ 00b4dc18 ["INT_ADD", "register:40f0:8", ["const:b4dc18:8", "const:4:8"]]
+ 00b4dc18 ["CALL", null, ["callee:00bde0c0:8"]]
- 00b4dbd4 bytes 27410294
+ 00b4dc18 bytes 2a410294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7317654c30d75834df15a98d04fe3cd5"></a>

### [`00b4dc74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4dc74.md) → [`00b4dcb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4dcb8.md) _ZN8firebase9messaging21UnsubscribeLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4dcd4",
      "incomplete_value": true,
      "site": "00b4dcd4",
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
      "definition_site": "00b4dc90",
      "incomplete_value": true,
      "site": "00b4dc90",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b4dc90"
      ],
      [
        "FALL_THROUGH",
        "00b4dcd4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b4dcd4",
      "incomplete_value": true,
      "site": "00b4dd08",
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
      "definition_site": "00b4dc90",
      "incomplete_value": true,
      "site": "00b4dcc4",
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
    "ordinal": 6,
    "slot": 0
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "CONDITIONAL_JUMP",
        "00b4dc90"
      ],
      [
        "CONDITIONAL_JUMP",
        "00b4dcd4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b4dcd4",
      "incomplete_value": true,
      "site": "00b4dd40",
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
      "definition_site": "00b4dc90",
      "incomplete_value": true,
      "site": "00b4dcfc",
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
      "00b4dccc",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dd28",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4dccc",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dd28",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dd08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4dc74.md#insn-00b4dd08) · [`00b4dc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4dc74.md#insn-00b4dc88) · [`00b4dc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4dc74.md#insn-00b4dc94)
- 新版 `00b4dd4c`（命令位置の公開資料なし） · `00b4dccc`（命令位置の公開資料なし） · `00b4dcd8`（命令位置の公開資料なし）

~~~diff
- 00b4dd08 ["INT_ADD", "register:40f0:8", ["const:b4dd08:8", "const:4:8"]]
- 00b4dd08 ["CALL", null, ["callee:00bddd80:8"]]
+ 00b4dd4c ["INT_ADD", "register:40f0:8", ["const:b4dd4c:8", "const:4:8"]]
+ 00b4dd4c ["CALL", null, ["callee:00bddd80:8"]]
- 00b4dd08 bytes 0a400294
+ 00b4dd4c bytes 0d400294
- 00b4dc88 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:60:8"]]
- 00b4dc88 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4dccc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:a0:8"]]
+ 00b4dccc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4dc88 bytes 293140f9
+ 00b4dccc bytes 295140f9
- 00b4dc94 ["INT_ADD", "register:40f0:8", ["const:b4dc94:8", "const:4:8"]]
- 00b4dc94 ["CALL", null, ["callee:00be0300:8"]]
+ 00b4dcd8 ["INT_ADD", "register:40f0:8", ["const:b4dcd8:8", "const:4:8"]]
+ 00b4dcd8 ["CALL", null, ["callee:00be0300:8"]]
- 00b4dc94 bytes 87490294
+ 00b4dcd8 bytes 8a490294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64b257801b26cbc45d1d503fc03a69cc"></a>

### [`00b4dd4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4dd4c.md) → [`00b4dd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4dd90.md) _ZN8firebase9messaging38DeliveryMetricsExportToBigQueryEnabledEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 80.95% / 新版 80.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4dda0",
      "incomplete_value": true,
      "site": "00b4dda0",
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
      "definition_site": "00b4dd5c",
      "incomplete_value": true,
      "site": "00b4dd5c",
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
      "definition_site": "00b4ddb0",
      "incomplete_value": true,
      "site": "00b4ddb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dd6c",
      "incomplete_value": true,
      "site": "00b4dd74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:98:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ddb4",
      "incomplete_value": true,
      "site": "00b4ddb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:30:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4dd70",
      "incomplete_value": true,
      "site": "00b4dd74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a0000:8"
              ],
              [
                "leaf",
                "const:ff0:8"
              ]
            ]
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
      "00b4dd9c",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ddb0",
      "READ",
      [
        "storage",
        "010a1098",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ddb4",
      "READ",
      [
        "storage",
        "010a0ff0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dd9c",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ddb0",
      "READ",
      [
        "storage",
        "010a10d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ddb4",
      "READ",
      [
        "storage",
        "010a1030",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4dd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4dd4c.md#insn-00b4dd74) · [`00b4dd58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4dd4c.md#insn-00b4dd58) · [`00b4dd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4dd4c.md#insn-00b4dd60)
- 新版 `00b4ddb8`（命令位置の公開資料なし） · `00b4dd9c`（命令位置の公開資料なし） · `00b4dda4`（命令位置の公開資料なし）

~~~diff
- 00b4dd74 ["INT_ADD", "register:40f0:8", ["const:b4dd74:8", "const:4:8"]]
- 00b4dd74 ["CALL", null, ["callee:00474b70:8"]]
+ 00b4ddb8 ["INT_ADD", "register:40f0:8", ["const:b4ddb8:8", "const:4:8"]]
+ 00b4ddb8 ["CALL", null, ["callee:00474b70:8"]]
- 00b4dd74 bytes 7f9be497
+ 00b4ddb8 bytes 6e9be497
- 00b4dd58 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:60:8"]]
- 00b4dd58 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4dd9c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a0:8"]]
+ 00b4dd9c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4dd58 bytes 003140f9
+ 00b4dd9c bytes 005140f9
- 00b4dd60 ["INT_ADD", "register:40f0:8", ["const:b4dd60:8", "const:4:8"]]
- 00b4dd60 ["CALL", null, ["callee:00bde200:8"]]
+ 00b4dda4 ["INT_ADD", "register:40f0:8", ["const:b4dda4:8", "const:4:8"]]
+ 00b4dda4 ["CALL", null, ["callee:00bde200:8"]]
- 00b4dd60 bytes 14410294
+ 00b4dda4 bytes 17410294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f01ae824189ed17848c69246ab08692b"></a>

### [`00b4de04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4de04.md) → [`00b4de48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4de48.md) _ZN8firebase9messaging8GetTokenEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0590.md) · 呼出先 22件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00ae3dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3dc8.md) [`00b4e0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e0e0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00be05e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be05e0.md) · 呼出先 22件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00ae3e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e0c.md) [`00b4e124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e124.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 92.65% / 新版 92.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_condition` 4件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4de7c",
      "incomplete_value": true,
      "site": "00b4de7c",
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
      "definition_site": "00b4de38",
      "incomplete_value": true,
      "site": "00b4de38",
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
      "definition_site": "00b4de88",
      "incomplete_value": true,
      "site": "00b4de8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4de44",
      "incomplete_value": true,
      "site": "00b4de48",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:70:8"
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
      "definition_site": "00b4ded8",
      "incomplete_value": true,
      "site": "00b4dedc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4de94",
      "incomplete_value": true,
      "site": "00b4de98",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:60:8"
              ]
            ]
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
      "00b4de78",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de84",
      "READ",
      [
        "storage",
        "010a1070",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4deb0",
      "READ",
      [
        "storage",
        "00c1b868",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b4de78",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de84",
      "READ",
      [
        "storage",
        "010a10b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4deb0",
      "READ",
      [
        "storage",
        "00c1b8b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4de48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4de04.md#insn-00b4de48) · [`00b4de6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4de04.md#insn-00b4de6c) · [`00b4de7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4de04.md#insn-00b4de7c)
- 新版 `00b4de8c`（命令位置の公開資料なし） · `00b4deb0`（命令位置の公開資料なし） · `00b4dec0`（命令位置の公開資料なし）

~~~diff
- 00b4de48 ["INT_ADD", "register:40f0:8", ["const:b4de48:8", "const:4:8"]]
- 00b4de48 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b4de8c ["INT_ADD", "register:40f0:8", ["const:b4de8c:8", "const:4:8"]]
+ 00b4de8c ["CALL", null, ["callee:00bddc20:8"]]
- 00b4de48 bytes 623f0294
+ 00b4de8c bytes 653f0294
- 00b4de6c ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:868:8"]]
- 00b4de6c ["LOAD", "register:4018:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4deb0 ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:8b8:8"]]
+ 00b4deb0 ["LOAD", "register:4018:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4de6c bytes 633444f9
+ 00b4deb0 bytes 635c44f9
- 00b4de7c ["INT_ADD", "register:40f0:8", ["const:b4de7c:8", "const:4:8"]]
- 00b4de7c ["CALL", null, ["callee:00bddfc0:8"]]
+ 00b4dec0 ["INT_ADD", "register:40f0:8", ["const:b4dec0:8", "const:4:8"]]
+ 00b4dec0 ["CALL", null, ["callee:00bddfc0:8"]]
- 00b4de7c bytes 3d400294
+ 00b4dec0 bytes 40400294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07203073429402c1d7b2b35b19e8a2da"></a>

### [`00b4e0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e0e0.md) → [`00b4e124`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e124.md) FUN_00b4e124

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b4de04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4d/00b4de04.md) · 呼出先 15件 [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00b4de48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4de48.md) · 呼出先 15件 [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.62% / 新版 96.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4e158",
      "incomplete_value": true,
      "site": "00b4e170",
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
            "const:7d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e114",
      "incomplete_value": true,
      "site": "00b4e12c",
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
            "const:866:8"
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
      "definition_site": "00b4e1d8",
      "incomplete_value": false,
      "site": "00b4e1dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e194",
      "incomplete_value": false,
      "site": "00b4e198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:f90:8"
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
      "definition_site": "00b4e22c",
      "incomplete_value": false,
      "site": "00b4e230",
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
            "const:f2f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e1e8",
      "incomplete_value": false,
      "site": "00b4e1ec",
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
            "const:f31:8"
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
      "00b4e158",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4e1d8",
      "PARAM",
      [
        "storage",
        "010a0f90",
        null,
        null
      ]
    ],
    [
      "00b4e22c",
      "PARAM",
      [
        "storage",
        "0029bf31",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4e158",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4e1d8",
      "PARAM",
      [
        "storage",
        "010a0fd0",
        null,
        null
      ]
    ],
    [
      "00b4e22c",
      "PARAM",
      [
        "storage",
        "0029bf2f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e12c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e0e0.md#insn-00b4e12c) · [`00b4e170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e0e0.md#insn-00b4e170) · [`00b4e198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e0e0.md#insn-00b4e198)
- 新版 `00b4e170`（命令位置の公開資料なし） · `00b4e1b4`（命令位置の公開資料なし） · `00b4e1dc`（命令位置の公開資料なし）

~~~diff
- 00b4e12c ["INT_ADD", "register:40f0:8", ["const:b4e12c:8", "const:4:8"]]
- 00b4e12c ["CALL", null, ["callee:00bde740:8"]]
+ 00b4e170 ["INT_ADD", "register:40f0:8", ["const:b4e170:8", "const:4:8"]]
+ 00b4e170 ["CALL", null, ["callee:00bde740:8"]]
- 00b4e12c bytes 71410294
+ 00b4e170 bytes 74410294
- 00b4e170 ["INT_ADD", "register:40f0:8", ["const:b4e170:8", "const:4:8"]]
- 00b4e170 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b4e1b4 ["INT_ADD", "register:40f0:8", ["const:b4e1b4:8", "const:4:8"]]
+ 00b4e1b4 ["CALL", null, ["callee:00bdb060:8"]]
- 00b4e170 bytes a8330294
+ 00b4e1b4 bytes ab330294
- 00b4e198 ["INT_ADD", "register:40f0:8", ["const:b4e198:8", "const:4:8"]]
- 00b4e198 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b4e1dc ["INT_ADD", "register:40f0:8", ["const:b4e1dc:8", "const:4:8"]]
+ 00b4e1dc ["CALL", null, ["callee:00bddc20:8"]]
- 00b4e198 bytes 8e3e0294
+ 00b4e1dc bytes 913e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d0a3f22cd0cb7009acf6fee97b0753c"></a>

### [`00b4e368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e368.md) → [`00b4e3ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e3ac.md) _ZN8firebase9messaging18GetTokenLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4e3c8",
      "incomplete_value": true,
      "site": "00b4e3c8",
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
      "definition_site": "00b4e384",
      "incomplete_value": true,
      "site": "00b4e384",
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
      "definition_site": "00b4e41c",
      "incomplete_value": false,
      "site": "00b4e420",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e3d8",
      "incomplete_value": false,
      "site": "00b4e3dc",
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
            "const:16d:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00b4e384"
      ],
      [
        "FALL_THROUGH",
        "00b4e3c8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b4e3c8",
      "incomplete_value": true,
      "site": "00b4e3fc",
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
      "definition_site": "00b4e384",
      "incomplete_value": true,
      "site": "00b4e3b8",
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
      "00b4e3c0",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e41c",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4e3c0",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e41c",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e368.md#insn-00b4e398) · [`00b4e3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e368.md#insn-00b4e3dc) · [`00b4e3fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e368.md#insn-00b4e3fc)
- 新版 `00b4e3dc`（命令位置の公開資料なし） · `00b4e420`（命令位置の公開資料なし） · `00b4e440`（命令位置の公開資料なし）

~~~diff
- 00b4e398 ["INT_ADD", "register:40f0:8", ["const:b4e398:8", "const:4:8"]]
- 00b4e398 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b4e3dc ["INT_ADD", "register:40f0:8", ["const:b4e3dc:8", "const:4:8"]]
+ 00b4e3dc ["CALL", null, ["callee:00bddc20:8"]]
- 00b4e398 bytes 0e3e0294
+ 00b4e3dc bytes 113e0294
- 00b4e3dc ["INT_ADD", "register:40f0:8", ["const:b4e3dc:8", "const:4:8"]]
- 00b4e3dc ["CALL", null, ["callee:00bde180:8"]]
+ 00b4e420 ["INT_ADD", "register:40f0:8", ["const:b4e420:8", "const:4:8"]]
+ 00b4e420 ["CALL", null, ["callee:00bde180:8"]]
- 00b4e3dc bytes 553f0294
+ 00b4e420 bytes 583f0294
- 00b4e3fc ["INT_ADD", "register:40f0:8", ["const:b4e3fc:8", "const:4:8"]]
- 00b4e3fc ["CALL", null, ["callee:00bddd80:8"]]
+ 00b4e440 ["INT_ADD", "register:40f0:8", ["const:b4e440:8", "const:4:8"]]
+ 00b4e440 ["CALL", null, ["callee:00bddd80:8"]]
- 00b4e3fc bytes 4d3e0294
+ 00b4e440 bytes 503e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81a21161f36477cb4c3adda7641d1217"></a>

### [`00b4e440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e440.md) → [`00b4e484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e484.md) _ZN8firebase9messaging11DeleteTokenEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 20件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b4e6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e6a8.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md)
- 新版 呼出元 0件  · 呼出先 20件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b4e6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e6ec.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_condition

命令の説明率　旧版 91.45% / 新版 91.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 5件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4e4b4",
      "incomplete_value": true,
      "site": "00b4e4b4",
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
      "definition_site": "00b4e470",
      "incomplete_value": true,
      "site": "00b4e470",
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
      "definition_site": "00b4e4f8",
      "incomplete_value": true,
      "site": "00b4e4fc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e4b4",
      "incomplete_value": true,
      "site": "00b4e4b8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:60:8"
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
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4e508",
      "incomplete_value": true,
      "site": "00b4e514",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e4c4",
      "incomplete_value": true,
      "site": "00b4e4d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:98:8"
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
      "00b4e4b0",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e4bc",
      "READ",
      [
        "storage",
        "010a1070",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e4f8",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e4b0",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e4bc",
      "READ",
      [
        "storage",
        "010a10b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e4f8",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e440.md#insn-00b4e4b4) · [`00b4e4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e440.md#insn-00b4e4b8) · [`00b4e4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e440.md#insn-00b4e4d0)
- 新版 `00b4e4f8`（命令位置の公開資料なし） · `00b4e4fc`（命令位置の公開資料なし） · `00b4e514`（命令位置の公開資料なし）

~~~diff
- 00b4e4b4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:60:8"]]
- 00b4e4b4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e4f8 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:a0:8"]]
+ 00b4e4f8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4e4b4 bytes c03240f9
+ 00b4e4f8 bytes c05240f9
- 00b4e4b8 ["INT_ADD", "register:40f0:8", ["const:b4e4b8:8", "const:4:8"]]
- 00b4e4b8 ["CALL", null, ["callee:00bde200:8"]]
+ 00b4e4fc ["INT_ADD", "register:40f0:8", ["const:b4e4fc:8", "const:4:8"]]
+ 00b4e4fc ["CALL", null, ["callee:00bde200:8"]]
- 00b4e4b8 bytes 3e3f0294
+ 00b4e4fc bytes 413f0294
- 00b4e4d0 ["INT_ADD", "register:40f0:8", ["const:b4e4d0:8", "const:4:8"]]
- 00b4e4d0 ["CALL", null, ["callee:0047495c:8"]]
+ 00b4e514 ["INT_ADD", "register:40f0:8", ["const:b4e514:8", "const:4:8"]]
+ 00b4e514 ["CALL", null, ["callee:0047495c:8"]]
- 00b4e4d0 bytes 2399e497
+ 00b4e514 bytes 1299e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed705b210fa9fc527f80b8743272bc87"></a>

### [`00b4e6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e6a8.md) → [`00b4e6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e6ec.md) FUN_00b4e6ec

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b4e440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e440.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md)
- 新版 呼出元 1件 [`00b4e484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e484.md) · 呼出先 8件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4e770",
      "incomplete_value": false,
      "site": "00b4e774",
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
            "const:f2f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e72c",
      "incomplete_value": false,
      "site": "00b4e730",
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
            "const:f31:8"
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
      "definition_site": "00b4e794",
      "incomplete_value": false,
      "site": "00b4e798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:fd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e750",
      "incomplete_value": false,
      "site": "00b4e754",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a0000:8"
          ],
          [
            "leaf",
            "const:f90:8"
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
      "00b4e738",
      "PARAM",
      [
        "storage",
        "010a0f90",
        null,
        null
      ]
    ],
    [
      "00b4e770",
      "PARAM",
      [
        "storage",
        "0029bf31",
        null,
        "string"
      ]
    ],
    [
      "00b4e794",
      "PARAM",
      [
        "storage",
        "010a0f90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4e738",
      "PARAM",
      [
        "storage",
        "010a0fd0",
        null,
        null
      ]
    ],
    [
      "00b4e770",
      "PARAM",
      [
        "storage",
        "0029bf2f",
        null,
        "string"
      ]
    ],
    [
      "00b4e794",
      "PARAM",
      [
        "storage",
        "010a0fd0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e6a8.md#insn-00b4e6ec) · [`00b4e730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e6a8.md#insn-00b4e730) · [`00b4e754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e6a8.md#insn-00b4e754)
- 新版 `00b4e730`（命令位置の公開資料なし） · `00b4e774`（命令位置の公開資料なし） · `00b4e798`（命令位置の公開資料なし）

~~~diff
- 00b4e6ec ["INT_ADD", "register:40f0:8", ["const:b4e6ec:8", "const:4:8"]]
- 00b4e6ec ["CALL", null, ["callee:00bddd80:8"]]
+ 00b4e730 ["INT_ADD", "register:40f0:8", ["const:b4e730:8", "const:4:8"]]
+ 00b4e730 ["CALL", null, ["callee:00bddd80:8"]]
- 00b4e6ec bytes 913d0294
+ 00b4e730 bytes 943d0294
- 00b4e730 ["INT_ADD", "register:40f0:8", ["const:b4e730:8", "const:4:8"]]
- 00b4e730 ["CALL", null, ["callee:00bddf60:8"]]
+ 00b4e774 ["INT_ADD", "register:40f0:8", ["const:b4e774:8", "const:4:8"]]
+ 00b4e774 ["CALL", null, ["callee:00bddf60:8"]]
- 00b4e730 bytes f83d0294
+ 00b4e774 bytes fb3d0294
- 00b4e754 ["INT_ADD", "register:40f0:8", ["const:b4e754:8", "const:4:8"]]
- 00b4e754 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b4e798 ["INT_ADD", "register:40f0:8", ["const:b4e798:8", "const:4:8"]]
+ 00b4e798 ["CALL", null, ["callee:00bddc30:8"]]
- 00b4e754 bytes 233d0294
+ 00b4e798 bytes 263d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df91bd3b084829a42780984a29204f52"></a>

### [`00b4e7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e7c0.md) → [`00b4e804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e804.md) _ZN8firebase9messaging21DeleteTokenLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bddea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddea0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bddef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddef0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4e820",
      "incomplete_value": true,
      "site": "00b4e820",
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
      "definition_site": "00b4e7dc",
      "incomplete_value": true,
      "site": "00b4e7dc",
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
      "definition_site": "00b4e874",
      "incomplete_value": true,
      "site": "00b4e878",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e830",
      "incomplete_value": true,
      "site": "00b4e834",
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
            "const:16d:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00b4e7dc"
      ],
      [
        "FALL_THROUGH",
        "00b4e820"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b4e820",
      "incomplete_value": true,
      "site": "00b4e854",
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
      "definition_site": "00b4e7dc",
      "incomplete_value": true,
      "site": "00b4e810",
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
      "00b4e818",
      "READ",
      [
        "storage",
        "010a1060",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e874",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b4e818",
      "READ",
      [
        "storage",
        "010a10a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e874",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e7c0.md#insn-00b4e7f0) · [`00b4e834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e7c0.md#insn-00b4e834) · [`00b4e854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e7c0.md#insn-00b4e854)
- 新版 `00b4e834`（命令位置の公開資料なし） · `00b4e878`（命令位置の公開資料なし） · `00b4e898`（命令位置の公開資料なし）

~~~diff
- 00b4e7f0 ["INT_ADD", "register:40f0:8", ["const:b4e7f0:8", "const:4:8"]]
- 00b4e7f0 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b4e834 ["INT_ADD", "register:40f0:8", ["const:b4e834:8", "const:4:8"]]
+ 00b4e834 ["CALL", null, ["callee:00bddc20:8"]]
- 00b4e7f0 bytes f83c0294
+ 00b4e834 bytes fb3c0294
- 00b4e834 ["INT_ADD", "register:40f0:8", ["const:b4e834:8", "const:4:8"]]
- 00b4e834 ["CALL", null, ["callee:00bde180:8"]]
+ 00b4e878 ["INT_ADD", "register:40f0:8", ["const:b4e878:8", "const:4:8"]]
+ 00b4e878 ["CALL", null, ["callee:00bde180:8"]]
- 00b4e834 bytes 3f3e0294
+ 00b4e878 bytes 423e0294
- 00b4e854 ["INT_ADD", "register:40f0:8", ["const:b4e854:8", "const:4:8"]]
- 00b4e854 ["CALL", null, ["callee:00bddd80:8"]]
+ 00b4e898 ["INT_ADD", "register:40f0:8", ["const:b4e898:8", "const:4:8"]]
+ 00b4e898 ["CALL", null, ["callee:00bddd80:8"]]
- 00b4e854 bytes 373d0294
+ 00b4e898 bytes 3a3d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8d4672efc600e8856ec5a6acd3364fdf"></a>

### [`00b4e89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e89c.md) → [`00b4e8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e8e0.md) FUN_00b4e8e0

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00b4b884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4b/00b4b884.md) · 呼出先 4件 [`00b4e904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e904.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00be03b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03b0.md)
- 新版 呼出元 1件 [`00b4b8c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4b/00b4b8c8.md) · 呼出先 4件 [`00b4e948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e948.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00be0400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0400.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.74% / 新版 94.74%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4e90c",
      "incomplete_value": false,
      "site": "00b4e90c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4e8c8",
      "incomplete_value": false,
      "site": "00b4e8c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "00b4e8f0",
      "READ",
      [
        "storage",
        "010a1070",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e90c",
      "WRITE",
      [
        "storage",
        "010a1108",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4e8f0",
      "READ",
      [
        "storage",
        "010a10b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e90c",
      "WRITE",
      [
        "storage",
        "010a1148",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4e8c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e89c.md#insn-00b4e8c8) · [`00b4e8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e89c.md#insn-00b4e8ac) · [`00b4e8bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e89c.md#insn-00b4e8bc)
- 新版 `00b4e90c`（命令位置の公開資料なし） · `00b4e8f0`（命令位置の公開資料なし） · `00b4e900`（命令位置の公開資料なし）

~~~diff
- 00b4e8c8 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b4e8c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:108:8"]]
- 00b4e8c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4e90c ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00b4e90c ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:148:8"]]
+ 00b4e90c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4e8c8 bytes 09210439
+ 00b4e90c bytes 09210539
- 00b4e8ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:70:8"]]
- 00b4e8ac ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4e8f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b0:8"]]
+ 00b4e8f0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4e8ac bytes 143940f9
+ 00b4e8f0 bytes 145940f9
- 00b4e8bc ["INT_ADD", "register:40f0:8", ["const:b4e8bc:8", "const:4:8"]]
- 00b4e8bc ["CALL", null, ["callee:00bddc20:8"]]
+ 00b4e900 ["INT_ADD", "register:40f0:8", ["const:b4e900:8", "const:4:8"]]
+ 00b4e900 ["CALL", null, ["callee:00bddc20:8"]]
- 00b4e8bc bytes c53c0294
+ 00b4e900 bytes c83c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8919c08bf5b6ee4de9819674c922e871"></a>

### [`00b4ea4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ea4c.md) → [`00b4ea90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ea90.md) FUN_00b4ea90

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b4cda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cda8.md) · 呼出先 4件 [`00b4e904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4e904.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00be03b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be03b0.md)
- 新版 呼出元 1件 [`00b4cdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4c/00b4cdec.md) · 呼出先 4件 [`00b4e948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4e948.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00be0400`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0400.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4eabc",
      "incomplete_value": false,
      "site": "00b4eabc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ea78",
      "incomplete_value": false,
      "site": "00b4ea78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:108:8"
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
      "00b4eaa0",
      "READ",
      [
        "storage",
        "010a1070",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4eabc",
      "WRITE",
      [
        "storage",
        "010a1108",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4eaa0",
      "READ",
      [
        "storage",
        "010a10b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4eabc",
      "WRITE",
      [
        "storage",
        "010a1148",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ea78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ea4c.md#insn-00b4ea78) · [`00b4ea5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ea4c.md#insn-00b4ea5c) · [`00b4ea6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ea4c.md#insn-00b4ea6c)
- 新版 `00b4eabc`（命令位置の公開資料なし） · `00b4eaa0`（命令位置の公開資料なし） · `00b4eab0`（命令位置の公開資料なし）

~~~diff
- 00b4ea78 ["COPY", "tmp:0:4", ["register:4048:4"]]
- 00b4ea78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:108:8"]]
- 00b4ea78 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4eabc ["COPY", "tmp:0:4", ["register:4048:4"]]
+ 00b4eabc ["INT_ADD", "tmp:1:8", ["register:4040:8", "const:148:8"]]
+ 00b4eabc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4ea78 bytes 09210439
+ 00b4eabc bytes 09210539
- 00b4ea5c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:70:8"]]
- 00b4ea5c ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4eaa0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:b0:8"]]
+ 00b4eaa0 ["LOAD", "register:40a0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4ea5c bytes 143940f9
+ 00b4eaa0 bytes 145940f9
- 00b4ea6c ["INT_ADD", "register:40f0:8", ["const:b4ea6c:8", "const:4:8"]]
- 00b4ea6c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b4eab0 ["INT_ADD", "register:40f0:8", ["const:b4eab0:8", "const:4:8"]]
+ 00b4eab0 ["CALL", null, ["callee:00bddc20:8"]]
- 00b4ea6c bytes 593c0294
+ 00b4eab0 bytes 5c3c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9ecabfddaa0a28b110fc9833556e07f"></a>

### [`00b4ee14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ee14.md) → [`00b4ee58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4e/00b4ee58.md) _INIT_277

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b0544c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0544c.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b05490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05490.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 82.76% / 新版 82.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ee90",
      "incomplete_value": true,
      "site": "00b4ee98",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:878:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ee4c",
      "incomplete_value": true,
      "site": "00b4ee54",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:828:8"
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
      "definition_site": "00b4ee94",
      "incomplete_value": false,
      "site": "00b4ee98",
      "value": [
        "leaf",
        "const:be5fd0:8"
      ]
    },
    "old": {
      "definition_site": "00b4ee50",
      "incomplete_value": false,
      "site": "00b4ee54",
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
      "00b4ee74",
      "PARAM",
      [
        "storage",
        "010a0f68",
        null,
        null
      ]
    ],
    [
      "00b4ee80",
      "READ",
      [
        "storage",
        "00c1b828",
        null,
        "pointer"
      ]
    ],
    [
      "00b4ee8c",
      "PARAM",
      [
        "storage",
        "010a0f68",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4ee74",
      "PARAM",
      [
        "storage",
        "010a0fa8",
        null,
        null
      ]
    ],
    [
      "00b4ee80",
      "READ",
      [
        "storage",
        "00c1b878",
        null,
        "pointer"
      ]
    ],
    [
      "00b4ee8c",
      "PARAM",
      [
        "storage",
        "010a0fa8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ee54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ee14.md#insn-00b4ee54) · [`00b4ee28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ee14.md#insn-00b4ee28) · [`00b4ee34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4e/00b4ee14.md#insn-00b4ee34)
- 新版 `00b4ee98`（命令位置の公開資料なし） · `00b4ee6c`（命令位置の公開資料なし） · `00b4ee78`（命令位置の公開資料なし）

~~~diff
- 00b4ee54 ["INT_ADD", "register:40f0:8", ["const:b4ee54:8", "const:4:8"]]
- 00b4ee54 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00b4ee98 ["INT_ADD", "register:40f0:8", ["const:b4ee98:8", "const:4:8"]]
+ 00b4ee98 ["CALL", null, ["callee:00bdafe0:8"]]
- 00b4ee54 bytes 4f300294
+ 00b4ee98 bytes 52300294
- 00b4ee28 ["COPY", "tmp:0:8", ["const:f68:8"]]
- 00b4ee28 ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
- 00b4ee28 ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
- 00b4ee28 ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
+ 00b4ee6c ["COPY", "tmp:0:8", ["const:fa8:8"]]
+ 00b4ee6c ["INT_CARRY", "register:105:1", ["register:4098:8", "tmp:0:8"]]
+ 00b4ee6c ["INT_SCARRY", "register:106:1", ["register:4098:8", "tmp:0:8"]]
+ 00b4ee6c ["INT_ADD", "tmp:1:8", ["register:4098:8", "tmp:0:8"]]
- 00b4ee28 bytes 73a23d91
+ 00b4ee6c bytes 73a23e91
- 00b4ee34 ["INT_ADD", "register:40f0:8", ["const:b4ee34:8", "const:4:8"]]
- 00b4ee34 ["CALL", null, ["callee:00bdde20:8"]]
+ 00b4ee78 ["INT_ADD", "register:40f0:8", ["const:b4ee78:8", "const:4:8"]]
+ 00b4ee78 ["CALL", null, ["callee:00bdde20:8"]]
- 00b4ee34 bytes e73b0294
+ 00b4ee78 bytes ea3b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc71885fa44586d4fea2015742b2641a"></a>

### [`00b52544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52544.md) → [`00b52588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52588.md) _INIT_278

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00b5249c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b5249c.md) [`00b524a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b524a4.md) [`00bddd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd10.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00b524e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b524e0.md) [`00b524e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b524e8.md) [`00bddd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd60.md)

変更の種類 constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 41.67% / 新版 41.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 4件, `store_value` 3件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b525a8",
      "incomplete_value": false,
      "site": "00b525a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:150:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52564",
      "incomplete_value": false,
      "site": "00b52564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:10a1000:8"
          ],
          [
            "leaf",
            "const:110:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b525a8",
      "incomplete_value": false,
      "site": "00b525a8",
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
            "const:86f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52564",
      "incomplete_value": false,
      "site": "00b52564",
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
            "const:8fc:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b525a8",
      "incomplete_value": false,
      "site": "00b525a8",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:150:8"
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
      "definition_site": "00b52564",
      "incomplete_value": false,
      "site": "00b52564",
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
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:110:8"
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
      "00b52598",
      "PARAM",
      [
        "storage",
        "010a1110",
        null,
        "undefined8"
      ]
    ],
    [
      "00b525a8",
      "WRITE",
      [
        "storage",
        "010a1110",
        null,
        "undefined8"
      ]
    ],
    [
      "00b525a8",
      "DATA",
      [
        "storage",
        "002998fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b52598",
      "PARAM",
      [
        "storage",
        "010a1150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b525a8",
      "WRITE",
      [
        "storage",
        "010a1150",
        null,
        "undefined8"
      ]
    ],
    [
      "00b525a8",
      "DATA",
      [
        "storage",
        "0029986f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52544.md#insn-00b52554) · [`00b52558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52544.md#insn-00b52558) · [`00b5255c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52544.md#insn-00b5255c)
- 新版 `00b52598`（命令位置の公開資料なし） · `00b5259c`（命令位置の公開資料なし） · `00b525a0`（命令位置の公開資料なし）

~~~diff
- 00b52554 ["COPY", "tmp:0:8", ["const:110:8"]]
- 00b52554 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b52554 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b52554 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b52598 ["COPY", "tmp:0:8", ["const:150:8"]]
+ 00b52598 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b52598 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b52598 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b52554 bytes 00400491
+ 00b52598 bytes 00400591
- 00b52558 ["COPY", "tmp:0:8", ["const:8fc:8"]]
- 00b52558 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b52558 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b52558 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5259c ["COPY", "tmp:0:8", ["const:86f:8"]]
+ 00b5259c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5259c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5259c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b52558 bytes 08f12391
+ 00b5259c bytes 08bd2191
- 00b5255c ["COPY", "tmp:0:8", ["const:49c:8"]]
- 00b5255c ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b5255c ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b5255c ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b525a0 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 00b525a0 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b525a0 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b525a0 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b5255c bytes 29711291
+ 00b525a0 bytes 29811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26ded146549ff835ef7f1f30b4834a46"></a>

### [`00b5257c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b5257c.md) → [`00b525c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b525c0.md) _ZN8firebase13remote_config12RemoteConfig11GetInstanceEPNS_3AppE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bddc90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc90.md) · 呼出先 11件 [`00b52c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52c84.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd40.md)
- 新版 呼出元 1件 [`00bddce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddce0.md) · 呼出先 11件 [`00b52cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52cc8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd90.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.45% / 新版 98.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b525fc",
      "incomplete_value": true,
      "site": "00b525fc",
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
      "definition_site": "00b525b8",
      "incomplete_value": true,
      "site": "00b525b8",
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
      "definition_site": "00b525e0",
      "incomplete_value": true,
      "site": "00b525e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5259c",
      "incomplete_value": true,
      "site": "00b525a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5265c",
      "incomplete_value": false,
      "site": "00b52660",
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
            "const:ed7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52618",
      "incomplete_value": false,
      "site": "00b5261c",
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
            "const:e4c:8"
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
      "00b525d8",
      "READ",
      [
        "storage",
        "00c1bab0",
        null,
        "pointer"
      ]
    ],
    [
      "00b525e0",
      "PARAM",
      [
        "storage",
        "010a1150",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00b525e8",
      "PARAM",
      [
        "storage",
        "010a1150",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00b525d8",
      "READ",
      [
        "storage",
        "00c1bb00",
        null,
        "pointer"
      ]
    ],
    [
      "00b525e0",
      "PARAM",
      [
        "storage",
        "010a1190",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ],
    [
      "00b525e8",
      "PARAM",
      [
        "storage",
        "010a1190",
        "_ZN8firebase13remote_config10g_rc_mutexE",
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b525a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b5257c.md#insn-00b525a0) · [`00b525fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b5257c.md#insn-00b525fc) · [`00b5261c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b5257c.md#insn-00b5261c)
- 新版 `00b525e4`（命令位置の公開資料なし） · `00b52640`（命令位置の公開資料なし） · `00b52660`（命令位置の公開資料なし）

~~~diff
- 00b525a0 ["INT_ADD", "register:40f0:8", ["const:b525a0:8", "const:4:8"]]
- 00b525a0 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b525e4 ["INT_ADD", "register:40f0:8", ["const:b525e4:8", "const:4:8"]]
+ 00b525e4 ["CALL", null, ["callee:00bddc20:8"]]
- 00b525a0 bytes 8c2d0294
+ 00b525e4 bytes 8f2d0294
- 00b525fc ["INT_ADD", "register:40f0:8", ["const:b525fc:8", "const:4:8"]]
- 00b525fc ["CALL", null, ["callee:00bddc30:8"]]
+ 00b52640 ["INT_ADD", "register:40f0:8", ["const:b52640:8", "const:4:8"]]
+ 00b52640 ["CALL", null, ["callee:00bddc30:8"]]
- 00b525fc bytes 792d0294
+ 00b52640 bytes 7c2d0294
- 00b5261c ["INT_ADD", "register:40f0:8", ["const:b5261c:8", "const:4:8"]]
- 00b5261c ["CALL", null, ["callee:00bde180:8"]]
+ 00b52660 ["INT_ADD", "register:40f0:8", ["const:b52660:8", "const:4:8"]]
+ 00b52660 ["CALL", null, ["callee:00bde180:8"]]
- 00b5261c bytes c52e0294
+ 00b52660 bytes c82e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d492bc53eeeb073de8b8c77c42c13c4"></a>

### [`00b529b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b529b0.md) → [`00b529f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b529f4.md) _ZN8firebase13remote_config12RemoteConfigC1EPNS_3AppE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00be0820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0820.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00be0870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0870.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.24% / 新版 95.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b52a14",
      "incomplete_value": false,
      "site": "00b52a18",
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
            "const:ed7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b529d0",
      "incomplete_value": false,
      "site": "00b529d4",
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
            "const:e4c:8"
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
      "00b52a14",
      "PARAM",
      [
        "storage",
        "002a1e4c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b52a14",
      "PARAM",
      [
        "storage",
        "002a1ed7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b529d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b529b0.md#insn-00b529d4) · [`00b529d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b529b0.md#insn-00b529d0) · [`00b529e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b529b0.md#insn-00b529e0)
- 新版 `00b52a18`（命令位置の公開資料なし） · `00b52a14`（命令位置の公開資料なし） · `00b52a24`（命令位置の公開資料なし）

~~~diff
- 00b529d4 ["INT_ADD", "register:40f0:8", ["const:b529d4:8", "const:4:8"]]
- 00b529d4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b52a18 ["INT_ADD", "register:40f0:8", ["const:b52a18:8", "const:4:8"]]
+ 00b52a18 ["CALL", null, ["callee:00bde180:8"]]
- 00b529d4 bytes d72d0294
+ 00b52a18 bytes da2d0294
- 00b529d0 ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 00b529d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b529d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b529d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b52a14 ["COPY", "tmp:0:8", ["const:ed7:8"]]
+ 00b52a14 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b52a14 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b52a14 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b529d0 bytes 00303991
+ 00b52a14 bytes 005c3b91
- 00b529e0 ["INT_ADD", "register:40f0:8", ["const:b529e0:8", "const:4:8"]]
- 00b529e0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b52a24 ["INT_ADD", "register:40f0:8", ["const:b52a24:8", "const:4:8"]]
+ 00b52a24 ["CALL", null, ["callee:00bdb040:8"]]
- 00b529e0 bytes 84210294
+ 00b52a24 bytes 87210294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1317c584d1240e89dfcd0815d8e2ab80"></a>

### [`00b52c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52c84.md) → [`00b52cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52cc8.md) FUN_00b52cc8

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b5257c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b5257c.md) · 呼出先 2件 [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00be0680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0680.md)
- 新版 呼出元 1件 [`00b525c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b525c0.md) · 呼出先 2件 [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00be06d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be06d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b52ce0",
      "incomplete_value": false,
      "site": "00b52ce8",
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
            "const:f6b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52c9c",
      "incomplete_value": false,
      "site": "00b52ca4",
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
            "const:f6d:8"
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
      "00b52ce0",
      "PARAM",
      [
        "storage",
        "0029bf6d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b52ce0",
      "PARAM",
      [
        "storage",
        "0029bf6b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52c84.md#insn-00b52ca4) · [`00b52c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52c84.md#insn-00b52c9c)
- 新版 `00b52ce8`（命令位置の公開資料なし） · `00b52ce0`（命令位置の公開資料なし）

~~~diff
- 00b52ca4 ["INT_ADD", "register:40f0:8", ["const:b52ca4:8", "const:4:8"]]
- 00b52ca4 ["CALL", null, ["callee:00bddf60:8"]]
+ 00b52ce8 ["INT_ADD", "register:40f0:8", ["const:b52ce8:8", "const:4:8"]]
+ 00b52ce8 ["CALL", null, ["callee:00bddf60:8"]]
- 00b52ca4 bytes 9b2c0294
+ 00b52ce8 bytes 9e2c0294
- 00b52c9c ["COPY", "tmp:0:8", ["const:f6d:8"]]
- 00b52c9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b52c9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b52c9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b52ce0 ["COPY", "tmp:0:8", ["const:f6b:8"]]
+ 00b52ce0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b52ce0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b52ce0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b52c9c bytes 00b43d91
+ 00b52ce0 bytes 00ac3d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ebdbde77d8a5fdd54fdba993b4a2d53"></a>

### [`00b52cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52cf8.md) → [`00b52d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52d3c.md) _INIT_279

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00b0544c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0544c.md) [`00b52574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52574.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00b05490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05490.md) [`00b525b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b525b8.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 88.89% / 新版 88.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 2件, `store_destination` 3件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b52d60",
      "incomplete_value": true,
      "site": "00b52d60",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52d1c",
      "incomplete_value": true,
      "site": "00b52d1c",
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
            "const:8:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b52d6c",
      "incomplete_value": true,
      "site": "00b52d6c",
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
      "definition_site": "00b52d28",
      "incomplete_value": true,
      "site": "00b52d28",
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
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b52d70",
      "incomplete_value": true,
      "site": "00b52d70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52d2c",
      "incomplete_value": true,
      "site": "00b52d2c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ab8:8"
              ]
            ]
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
      "00b52d4c",
      "READ",
      [
        "storage",
        "00c1bab8",
        null,
        "pointer"
      ]
    ],
    [
      "00b52d4c",
      "PARAM",
      [
        "storage",
        "010a1138",
        "_ZN8firebase13remote_config5g_rcsE",
        "undefined8"
      ]
    ],
    [
      "00b52d60",
      "WRITE",
      [
        "storage",
        "010a1140",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52d4c",
      "READ",
      [
        "storage",
        "00c1bb08",
        null,
        "pointer"
      ]
    ],
    [
      "00b52d4c",
      "PARAM",
      [
        "storage",
        "010a1178",
        "_ZN8firebase13remote_config5g_rcsE",
        "undefined8"
      ]
    ],
    [
      "00b52d60",
      "WRITE",
      [
        "storage",
        "010a1180",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52cf8.md#insn-00b52d30) · [`00b52d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52cf8.md#insn-00b52d44) · [`00b52d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52cf8.md#insn-00b52d08)
- 新版 `00b52d74`（命令位置の公開資料なし） · `00b52d88`（命令位置の公開資料なし） · `00b52d4c`（命令位置の公開資料なし）

~~~diff
- 00b52d30 ["INT_ADD", "register:40f0:8", ["const:b52d30:8", "const:4:8"]]
- 00b52d30 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00b52d74 ["INT_ADD", "register:40f0:8", ["const:b52d74:8", "const:4:8"]]
+ 00b52d74 ["CALL", null, ["callee:00bdafe0:8"]]
- 00b52d30 bytes 98200294
+ 00b52d74 bytes 9b200294
- 00b52d44 ["INT_ADD", "register:40f0:8", ["const:b52d44:8", "const:4:8"]]
- 00b52d44 ["CALL", null, ["callee:00bdde20:8"]]
+ 00b52d88 ["INT_ADD", "register:40f0:8", ["const:b52d88:8", "const:4:8"]]
+ 00b52d88 ["CALL", null, ["callee:00bdde20:8"]]
- 00b52d44 bytes 232c0294
+ 00b52d88 bytes 262c0294
- 00b52d08 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:ab8:8"]]
- 00b52d08 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52d4c ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:b08:8"]]
+ 00b52d4c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52d08 bytes 215c45f9
+ 00b52d4c bytes 218445f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7db3f6523583c0894fa12603d10af39"></a>

### [`00b52d64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52d64.md) → [`00b52da8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52da8.md) _ZN8firebase13remote_config8internal6config19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allo

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b52dd4",
      "incomplete_value": true,
      "site": "00b52dd4",
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
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52d90",
      "incomplete_value": true,
      "site": "00b52d90",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b52dbc",
      "incomplete_value": true,
      "site": "00b52dbc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b52d78",
      "incomplete_value": true,
      "site": "00b52d78",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b52dc8",
      "incomplete_value": false,
      "site": "00b52dcc",
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
            "const:a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52d84",
      "incomplete_value": false,
      "site": "00b52d88",
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
            "const:f7f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b52db8",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52dc8",
      "PARAM",
      [
        "storage",
        "002a0f7f",
        null,
        "string"
      ]
    ],
    [
      "00b52dd4",
      "WRITE",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52db8",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52dc8",
      "PARAM",
      [
        "storage",
        "002a100a",
        null,
        "string"
      ]
    ],
    [
      "00b52dd4",
      "WRITE",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52d64.md#insn-00b52d88) · [`00b52d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52d64.md#insn-00b52d90) · [`00b52d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52d64.md#insn-00b52d74)
- 新版 `00b52dcc`（命令位置の公開資料なし） · `00b52dd4`（命令位置の公開資料なし） · `00b52db8`（命令位置の公開資料なし）

~~~diff
- 00b52d88 ["INT_ADD", "register:40f0:8", ["const:b52d88:8", "const:4:8"]]
- 00b52d88 ["CALL", null, ["callee:00bde090:8"]]
+ 00b52dcc ["INT_ADD", "register:40f0:8", ["const:b52dcc:8", "const:4:8"]]
+ 00b52dcc ["CALL", null, ["callee:00bde090:8"]]
- 00b52d88 bytes ae2c0294
+ 00b52dcc bytes b12c0294
- 00b52d90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
- 00b52d90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b52dd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b8:8"]]
+ 00b52dd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52d90 bytes 60be00f9
+ 00b52dd4 bytes 60de00f9
- 00b52d74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
- 00b52d74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52db8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b8:8"]]
+ 00b52db8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52d74 bytes 68be40f9
+ 00b52db8 bytes 68de40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0e7c68a5ad5d819753bd5916eeac4dc"></a>

### [`00b52da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52da4.md) → [`00b52de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52de8.md) _ZN8firebase13remote_config8internal6config19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7_9allo

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b52e14",
      "incomplete_value": true,
      "site": "00b52e14",
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
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52dd0",
      "incomplete_value": true,
      "site": "00b52dd0",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b52dfc",
      "incomplete_value": true,
      "site": "00b52dfc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b52db8",
      "incomplete_value": true,
      "site": "00b52db8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b52e04",
      "incomplete_value": false,
      "site": "00b52e0c",
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
            "const:a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52dc0",
      "incomplete_value": false,
      "site": "00b52dc8",
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
            "const:f7f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b52df8",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52e04",
      "PARAM",
      [
        "storage",
        "002a0f7f",
        null,
        "string"
      ]
    ],
    [
      "00b52e14",
      "WRITE",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52df8",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52e04",
      "PARAM",
      [
        "storage",
        "002a100a",
        null,
        "string"
      ]
    ],
    [
      "00b52e14",
      "WRITE",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52da4.md#insn-00b52dc8) · [`00b52dd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52da4.md#insn-00b52dd0) · [`00b52db4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52da4.md#insn-00b52db4)
- 新版 `00b52e0c`（命令位置の公開資料なし） · `00b52e14`（命令位置の公開資料なし） · `00b52df8`（命令位置の公開資料なし）

~~~diff
- 00b52dc8 ["INT_ADD", "register:40f0:8", ["const:b52dc8:8", "const:4:8"]]
- 00b52dc8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b52e0c ["INT_ADD", "register:40f0:8", ["const:b52e0c:8", "const:4:8"]]
+ 00b52e0c ["CALL", null, ["callee:00bde090:8"]]
- 00b52dc8 bytes 9e2c0294
+ 00b52e0c bytes a12c0294
- 00b52dd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
- 00b52dd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b52e14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b8:8"]]
+ 00b52e14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52dd0 bytes 60be00f9
+ 00b52e14 bytes 60de00f9
- 00b52db4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
- 00b52db4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52df8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b8:8"]]
+ 00b52df8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52db4 bytes 68be40f9
+ 00b52df8 bytes 68de40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a33dc3f22d8c80245a1089aeefe1a10e"></a>

### [`00b52de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52de4.md) → [`00b52e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52e28.md) _ZN8firebase13remote_config8internal6config10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b52e58",
      "incomplete_value": true,
      "site": "00b52e58",
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
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52e14",
      "incomplete_value": true,
      "site": "00b52e14",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b52e3c",
      "incomplete_value": true,
      "site": "00b52e3c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b52df8",
      "incomplete_value": true,
      "site": "00b52df8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b52e48",
      "incomplete_value": false,
      "site": "00b52e50",
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
            "const:a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52e04",
      "incomplete_value": false,
      "site": "00b52e0c",
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
            "const:f7f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b52e38",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52e48",
      "PARAM",
      [
        "storage",
        "002a0f7f",
        null,
        "string"
      ]
    ],
    [
      "00b52e58",
      "WRITE",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52e38",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52e48",
      "PARAM",
      [
        "storage",
        "002a100a",
        null,
        "string"
      ]
    ],
    [
      "00b52e58",
      "WRITE",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52de4.md#insn-00b52e0c) · [`00b52e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52de4.md#insn-00b52e14) · [`00b52df4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52de4.md#insn-00b52df4)
- 新版 `00b52e50`（命令位置の公開資料なし） · `00b52e58`（命令位置の公開資料なし） · `00b52e38`（命令位置の公開資料なし）

~~~diff
- 00b52e0c ["INT_ADD", "register:40f0:8", ["const:b52e0c:8", "const:4:8"]]
- 00b52e0c ["CALL", null, ["callee:00bde090:8"]]
+ 00b52e50 ["INT_ADD", "register:40f0:8", ["const:b52e50:8", "const:4:8"]]
+ 00b52e50 ["CALL", null, ["callee:00bde090:8"]]
- 00b52e0c bytes 8d2c0294
+ 00b52e50 bytes 902c0294
- 00b52e14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
- 00b52e14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b52e58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b8:8"]]
+ 00b52e58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52e14 bytes 60be00f9
+ 00b52e58 bytes 60de00f9
- 00b52df4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
- 00b52df4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52e38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b8:8"]]
+ 00b52e38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52df4 bytes 68be40f9
+ 00b52e38 bytes 68de40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-024775cc1e8a1a33d0af37212d904825"></a>

### [`00b52e28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52e28.md) → [`00b52e6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52e6c.md) _ZN8firebase13remote_config8internal6config10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b52e9c",
      "incomplete_value": true,
      "site": "00b52e9c",
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
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52e58",
      "incomplete_value": true,
      "site": "00b52e58",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b52e80",
      "incomplete_value": true,
      "site": "00b52e80",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b52e3c",
      "incomplete_value": true,
      "site": "00b52e3c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b52e88",
      "incomplete_value": false,
      "site": "00b52e94",
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
            "const:a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52e44",
      "incomplete_value": false,
      "site": "00b52e50",
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
            "const:f7f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b52e7c",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52e88",
      "PARAM",
      [
        "storage",
        "002a0f7f",
        null,
        "string"
      ]
    ],
    [
      "00b52e9c",
      "WRITE",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52e7c",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52e88",
      "PARAM",
      [
        "storage",
        "002a100a",
        null,
        "string"
      ]
    ],
    [
      "00b52e9c",
      "WRITE",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52e28.md#insn-00b52e50) · [`00b52e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52e28.md#insn-00b52e58) · [`00b52e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52e28.md#insn-00b52e38)
- 新版 `00b52e94`（命令位置の公開資料なし） · `00b52e9c`（命令位置の公開資料なし） · `00b52e7c`（命令位置の公開資料なし）

~~~diff
- 00b52e50 ["INT_ADD", "register:40f0:8", ["const:b52e50:8", "const:4:8"]]
- 00b52e50 ["CALL", null, ["callee:00bde090:8"]]
+ 00b52e94 ["INT_ADD", "register:40f0:8", ["const:b52e94:8", "const:4:8"]]
+ 00b52e94 ["CALL", null, ["callee:00bde090:8"]]
- 00b52e50 bytes 7c2c0294
+ 00b52e94 bytes 7f2c0294
- 00b52e58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
- 00b52e58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b52e9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b8:8"]]
+ 00b52e9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52e58 bytes 60be00f9
+ 00b52e9c bytes 60de00f9
- 00b52e38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:178:8"]]
- 00b52e38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52e7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:1b8:8"]]
+ 00b52e7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52e38 bytes 68be40f9
+ 00b52e7c bytes 68de40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a04d74ddda9f77afe7a526016bfa87c"></a>

### [`00b52e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52e78.md) → [`00b52ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52ebc.md) _ZN8firebase13remote_config8internal6config15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b52f14",
      "incomplete_value": true,
      "site": "00b52f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52ed0",
      "incomplete_value": true,
      "site": "00b52ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b52ef0",
      "incomplete_value": true,
      "site": "00b52efc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:1b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52eac",
      "incomplete_value": true,
      "site": "00b52eb8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:178:8"
              ]
            ]
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
      "00b52ed0",
      "READ",
      [
        "storage",
        "010a1180",
        null,
        "undefined1"
      ]
    ],
    [
      "00b52ef0",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52f14",
      "WRITE",
      [
        "storage",
        "010a1180",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b52ed0",
      "READ",
      [
        "storage",
        "010a11c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b52ef0",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52f14",
      "WRITE",
      [
        "storage",
        "010a11c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52e78.md#insn-00b52e8c) · [`00b52eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52e78.md#insn-00b52eb8) · [`00b52ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52e78.md#insn-00b52ed0)
- 新版 `00b52ed0`（命令位置の公開資料なし） · `00b52efc`（命令位置の公開資料なし） · `00b52f14`（命令位置の公開資料なし）

~~~diff
- 00b52e8c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:180:8"]]
- 00b52e8c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b52e8c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b52ed0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:1c0:8"]]
+ 00b52ed0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b52ed0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b52e8c bytes a8024639
+ 00b52ed0 bytes a8024739
- 00b52eb8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b52eb8 ["INT_ADD", "register:40f0:8", ["const:b52eb8:8", "const:4:8"]]
- 00b52eb8 ["CALLIND", null, ["register:0:8"]]
+ 00b52efc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b52efc ["INT_ADD", "register:40f0:8", ["const:b52efc:8", "const:4:8"]]
+ 00b52efc ["CALLIND", null, ["register:0:8"]]
- 00b52eb8 bytes 00013fd6
+ 00b52efc bytes 00013fd6
- 00b52ed0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b52ed0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:180:8"]]
- 00b52ed0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b52f14 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b52f14 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:1c0:8"]]
+ 00b52f14 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b52ed0 bytes a0020639
+ 00b52f14 bytes a0020739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80d9334643dd1226a0d84b1408df65a5"></a>

### [`00b52ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52ee4.md) → [`00b52f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52f28.md) _ZN8firebase13remote_config8internal6config12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b52f64",
      "incomplete_value": true,
      "site": "00b52f64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:1c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52f20",
      "incomplete_value": true,
      "site": "00b52f20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:180:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b52f84",
      "incomplete_value": true,
      "site": "00b52f84",
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
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52f40",
      "incomplete_value": true,
      "site": "00b52f40",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b52f40",
      "incomplete_value": true,
      "site": "00b52f40",
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
      "definition_site": "00b52efc",
      "incomplete_value": true,
      "site": "00b52efc",
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
      "00b52f3c",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52f48",
      "READ",
      [
        "storage",
        "010a1180",
        null,
        "undefined1"
      ]
    ],
    [
      "00b52f64",
      "WRITE",
      [
        "storage",
        "010a1180",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b52f3c",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52f48",
      "READ",
      [
        "storage",
        "010a11c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b52f64",
      "WRITE",
      [
        "storage",
        "010a11c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52ef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52ee4.md#insn-00b52ef8) · [`00b52f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52ee4.md#insn-00b52f20) · [`00b52f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52ee4.md#insn-00b52f3c)
- 新版 `00b52f3c`（命令位置の公開資料なし） · `00b52f64`（命令位置の公開資料なし） · `00b52f80`（命令位置の公開資料なし）

~~~diff
- 00b52ef8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:178:8"]]
- 00b52ef8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52f3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1b8:8"]]
+ 00b52f3c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52ef8 bytes 81be40f9
+ 00b52f3c bytes 81de40f9
- 00b52f20 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b52f20 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b52f20 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:180:8"]]
- 00b52f20 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b52f64 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b52f64 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b52f64 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:1c0:8"]]
+ 00b52f64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b52f20 bytes bf020639
+ 00b52f64 bytes bf020739
- 00b52f3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b52f3c ["INT_ADD", "register:40f0:8", ["const:b52f3c:8", "const:4:8"]]
- 00b52f3c ["CALLIND", null, ["register:0:8"]]
+ 00b52f80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b52f80 ["INT_ADD", "register:40f0:8", ["const:b52f80:8", "const:4:8"]]
+ 00b52f80 ["CALLIND", null, ["register:0:8"]]
- 00b52f3c bytes 00013fd6
+ 00b52f80 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfa38d5518387279dcfabec9dc309574"></a>

### [`00b52f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52f54.md) → [`00b52f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b52/00b52f98.md) _ZN8firebase13remote_config8internal6config14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b52fd8",
      "incomplete_value": true,
      "site": "00b52fd8",
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
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52f94",
      "incomplete_value": true,
      "site": "00b52f94",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b52fb4",
      "incomplete_value": true,
      "site": "00b52fb4",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b52f70",
      "incomplete_value": true,
      "site": "00b52f70",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b52fbc",
      "incomplete_value": false,
      "site": "00b52fd0",
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
            "const:a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52f78",
      "incomplete_value": false,
      "site": "00b52f8c",
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
            "const:f7f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b52fac",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52fbc",
      "PARAM",
      [
        "storage",
        "002a0f7f",
        null,
        "string"
      ]
    ],
    [
      "00b52fd8",
      "WRITE",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b52fac",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b52fbc",
      "PARAM",
      [
        "storage",
        "002a100a",
        null,
        "string"
      ]
    ],
    [
      "00b52fd8",
      "WRITE",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52f8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52f54.md#insn-00b52f8c) · [`00b52f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52f54.md#insn-00b52f94) · [`00b52f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52f54.md#insn-00b52f68)
- 新版 `00b52fd0`（命令位置の公開資料なし） · `00b52fd8`（命令位置の公開資料なし） · `00b52fac`（命令位置の公開資料なし）

~~~diff
- 00b52f8c ["INT_ADD", "register:40f0:8", ["const:b52f8c:8", "const:4:8"]]
- 00b52f8c ["CALL", null, ["callee:00bde090:8"]]
+ 00b52fd0 ["INT_ADD", "register:40f0:8", ["const:b52fd0:8", "const:4:8"]]
+ 00b52fd0 ["CALL", null, ["callee:00bde090:8"]]
- 00b52f8c bytes 2d2c0294
+ 00b52fd0 bytes 302c0294
- 00b52f94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:178:8"]]
- 00b52f94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b52fd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1b8:8"]]
+ 00b52fd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b52f94 bytes 80be00f9
+ 00b52fd8 bytes 80de00f9
- 00b52f68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:178:8"]]
- 00b52f68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b52fac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1b8:8"]]
+ 00b52fac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b52f68 bytes 81be40f9
+ 00b52fac bytes 81de40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a6a45908cb12974d0de8812c3b659fe"></a>

### [`00b52fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52fc4.md) → [`00b53008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53008.md) _ZN8firebase13remote_config8internal6config11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53024",
      "incomplete_value": false,
      "site": "00b53028",
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
            "const:547:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52fe0",
      "incomplete_value": false,
      "site": "00b52fe4",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b53034",
      "incomplete_value": true,
      "site": "00b53040",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b52ff0",
      "incomplete_value": true,
      "site": "00b52ffc",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b53024",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b53034",
      "DATA",
      [
        "storage",
        "010a1188",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53024",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b53034",
      "DATA",
      [
        "storage",
        "010a11c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b52fe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52fc4.md#insn-00b52fe4) · [`00b52fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52fc4.md#insn-00b52fe0) · [`00b52fec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b52/00b52fc4.md#insn-00b52fec)
- 新版 `00b53028`（命令位置の公開資料なし） · `00b53024`（命令位置の公開資料なし） · `00b53030`（命令位置の公開資料なし）

~~~diff
- 00b52fe4 ["INT_ADD", "register:40f0:8", ["const:b52fe4:8", "const:4:8"]]
- 00b52fe4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b53028 ["INT_ADD", "register:40f0:8", ["const:b53028:8", "const:4:8"]]
+ 00b53028 ["CALL", null, ["callee:00bde180:8"]]
- 00b52fe4 bytes 532c0294
+ 00b53028 bytes 562c0294
- 00b52fe0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b52fe0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b52fe0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b52fe0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b53024 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b53024 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53024 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53024 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b52fe0 bytes 00501791
+ 00b53024 bytes 001c1591
- 00b52fec ["COPY", "tmp:0:8", ["const:188:8"]]
- 00b52fec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b52fec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b52fec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b53030 ["COPY", "tmp:0:8", ["const:1c8:8"]]
+ 00b53030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b52fec bytes 08210691
+ 00b53030 bytes 08210791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d7c3afc1ac015c9220720d66992f693"></a>

### [`00b53000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53000.md) → [`00b53044`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53044.md) _ZN8firebase13remote_config8internal6config13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b53084",
      "incomplete_value": true,
      "site": "00b53084",
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
            "const:1b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53040",
      "incomplete_value": true,
      "site": "00b53040",
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
            "const:178:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b53060",
      "incomplete_value": true,
      "site": "00b53060",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b5301c",
      "incomplete_value": true,
      "site": "00b5301c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53068",
      "incomplete_value": false,
      "site": "00b5307c",
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
            "const:a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53024",
      "incomplete_value": false,
      "site": "00b53038",
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
            "const:f7f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b53058",
      "READ",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53068",
      "PARAM",
      [
        "storage",
        "002a0f7f",
        null,
        "string"
      ]
    ],
    [
      "00b53084",
      "WRITE",
      [
        "storage",
        "010a1178",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53058",
      "READ",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53068",
      "PARAM",
      [
        "storage",
        "002a100a",
        null,
        "string"
      ]
    ],
    [
      "00b53084",
      "WRITE",
      [
        "storage",
        "010a11b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53000.md#insn-00b53038) · [`00b53040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53000.md#insn-00b53040) · [`00b53014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53000.md#insn-00b53014)
- 新版 `00b5307c`（命令位置の公開資料なし） · `00b53084`（命令位置の公開資料なし） · `00b53058`（命令位置の公開資料なし）

~~~diff
- 00b53038 ["INT_ADD", "register:40f0:8", ["const:b53038:8", "const:4:8"]]
- 00b53038 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5307c ["INT_ADD", "register:40f0:8", ["const:b5307c:8", "const:4:8"]]
+ 00b5307c ["CALL", null, ["callee:00bde090:8"]]
- 00b53038 bytes 022c0294
+ 00b5307c bytes 052c0294
- 00b53040 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:178:8"]]
- 00b53040 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53084 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1b8:8"]]
+ 00b53084 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53040 bytes 80be00f9
+ 00b53084 bytes 80de00f9
- 00b53014 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:178:8"]]
- 00b53014 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53058 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:1b8:8"]]
+ 00b53058 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53014 bytes 81be40f9
+ 00b53058 bytes 81de40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-be13bced68a69e9f3d6eff0f4feb90fa"></a>

### [`00b53070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53070.md) → [`00b530b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b530b4.md) _ZN8firebase13remote_config8internal6config10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b530d0",
      "incomplete_value": false,
      "site": "00b530d4",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5308c",
      "incomplete_value": false,
      "site": "00b53090",
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
            "const:67f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b530e0",
      "incomplete_value": true,
      "site": "00b530ec",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5309c",
      "incomplete_value": true,
      "site": "00b530a8",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b530d0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b530e0",
      "DATA",
      [
        "storage",
        "010a1210",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b530d0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b530e0",
      "DATA",
      [
        "storage",
        "010a1250",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53070.md#insn-00b53090) · [`00b5308c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53070.md#insn-00b5308c) · [`00b53098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53070.md#insn-00b53098)
- 新版 `00b530d4`（命令位置の公開資料なし） · `00b530d0`（命令位置の公開資料なし） · `00b530dc`（命令位置の公開資料なし）

~~~diff
- 00b53090 ["INT_ADD", "register:40f0:8", ["const:b53090:8", "const:4:8"]]
- 00b53090 ["CALL", null, ["callee:00bde180:8"]]
+ 00b530d4 ["INT_ADD", "register:40f0:8", ["const:b530d4:8", "const:4:8"]]
+ 00b530d4 ["CALL", null, ["callee:00bde180:8"]]
- 00b53090 bytes 282c0294
+ 00b530d4 bytes 2b2c0294
- 00b5308c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b5308c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5308c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5308c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b530d0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b530d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b530d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b530d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5308c bytes 00fc1991
+ 00b530d0 bytes 00c81791
- 00b53098 ["COPY", "tmp:0:8", ["const:210:8"]]
- 00b53098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b53098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b53098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b530dc ["COPY", "tmp:0:8", ["const:250:8"]]
+ 00b530dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b530dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b530dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b53098 bytes 08410891
+ 00b530dc bytes 08410991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db016cf42d5f34bfd20eebbcc30983ca"></a>

### [`00b530ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b530ac.md) → [`00b530f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b530f0.md) _ZN8firebase13remote_config8internal12config_value19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5311c",
      "incomplete_value": true,
      "site": "00b5311c",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b530d8",
      "incomplete_value": true,
      "site": "00b530d8",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b53104",
      "incomplete_value": true,
      "site": "00b53104",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b530c0",
      "incomplete_value": true,
      "site": "00b530c0",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b530c0"
      ],
      [
        "FALL_THROUGH",
        "00b53104"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b53104",
      "incomplete_value": true,
      "site": "00b5311c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b530c0",
      "incomplete_value": true,
      "site": "00b530d8",
      "value": [
        "INT_NOTEQUAL",
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
      "00b53100",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5311c",
      "WRITE",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53100",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5311c",
      "WRITE",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b530d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b530ac.md#insn-00b530d8) · [`00b530bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b530ac.md#insn-00b530bc) · [`00b530d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b530ac.md#insn-00b530d0)
- 新版 `00b5311c`（命令位置の公開資料なし） · `00b53100`（命令位置の公開資料なし） · `00b53114`（命令位置の公開資料なし）

~~~diff
- 00b530d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
- 00b530d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5311c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b5311c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b530d8 bytes 600e01f9
+ 00b5311c bytes 602e01f9
- 00b530bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
- 00b530bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53100 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b53100 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b530bc bytes 680e41f9
+ 00b53100 bytes 682e41f9
- 00b530d0 ["INT_ADD", "register:40f0:8", ["const:b530d0:8", "const:4:8"]]
- 00b530d0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53114 ["INT_ADD", "register:40f0:8", ["const:b53114:8", "const:4:8"]]
+ 00b53114 ["CALL", null, ["callee:00bde090:8"]]
- 00b530d0 bytes dc2b0294
+ 00b53114 bytes df2b0294
~~~


<a id="compare-637fb5fac0cfe77be08ac2473531e6ec"></a>

### [`00b530ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b530ec.md) → [`00b53130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53130.md) _ZN8firebase13remote_config8internal12config_value19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5315c",
      "incomplete_value": true,
      "site": "00b5315c",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53118",
      "incomplete_value": true,
      "site": "00b53118",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b53144",
      "incomplete_value": true,
      "site": "00b53144",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53100",
      "incomplete_value": true,
      "site": "00b53100",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b53100"
      ],
      [
        "FALL_THROUGH",
        "00b53144"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b53144",
      "incomplete_value": true,
      "site": "00b5315c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53100",
      "incomplete_value": true,
      "site": "00b53118",
      "value": [
        "INT_NOTEQUAL",
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
      "00b53140",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5315c",
      "WRITE",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53140",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5315c",
      "WRITE",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b530ec.md#insn-00b53118) · [`00b530fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b530ec.md#insn-00b530fc) · [`00b53110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b530ec.md#insn-00b53110)
- 新版 `00b5315c`（命令位置の公開資料なし） · `00b53140`（命令位置の公開資料なし） · `00b53154`（命令位置の公開資料なし）

~~~diff
- 00b53118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
- 00b53118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5315c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b5315c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53118 bytes 600e01f9
+ 00b5315c bytes 602e01f9
- 00b530fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
- 00b530fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53140 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b53140 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b530fc bytes 680e41f9
+ 00b53140 bytes 682e41f9
- 00b53110 ["INT_ADD", "register:40f0:8", ["const:b53110:8", "const:4:8"]]
- 00b53110 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53154 ["INT_ADD", "register:40f0:8", ["const:b53154:8", "const:4:8"]]
+ 00b53154 ["CALL", null, ["callee:00bde090:8"]]
- 00b53110 bytes cc2b0294
+ 00b53154 bytes cf2b0294
~~~


<a id="compare-bb48de9795cda946503f2660a24e2458"></a>

### [`00b5312c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5312c.md) → [`00b53170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53170.md) _ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b531a0",
      "incomplete_value": true,
      "site": "00b531a0",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5315c",
      "incomplete_value": true,
      "site": "00b5315c",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b53184",
      "incomplete_value": true,
      "site": "00b53184",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53140",
      "incomplete_value": true,
      "site": "00b53140",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b53140"
      ],
      [
        "FALL_THROUGH",
        "00b53184"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b53184",
      "incomplete_value": true,
      "site": "00b531a0",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53140",
      "incomplete_value": true,
      "site": "00b5315c",
      "value": [
        "INT_NOTEQUAL",
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
      "00b53180",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b531a0",
      "WRITE",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53180",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b531a0",
      "WRITE",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5315c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5312c.md#insn-00b5315c) · [`00b5313c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5312c.md#insn-00b5313c) · [`00b53154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5312c.md#insn-00b53154)
- 新版 `00b531a0`（命令位置の公開資料なし） · `00b53180`（命令位置の公開資料なし） · `00b53198`（命令位置の公開資料なし）

~~~diff
- 00b5315c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
- 00b5315c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b531a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b531a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5315c bytes 600e01f9
+ 00b531a0 bytes 602e01f9
- 00b5313c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
- 00b5313c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53180 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b53180 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5313c bytes 680e41f9
+ 00b53180 bytes 682e41f9
- 00b53154 ["INT_ADD", "register:40f0:8", ["const:b53154:8", "const:4:8"]]
- 00b53154 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53198 ["INT_ADD", "register:40f0:8", ["const:b53198:8", "const:4:8"]]
+ 00b53198 ["CALL", null, ["callee:00bde090:8"]]
- 00b53154 bytes bb2b0294
+ 00b53198 bytes be2b0294
~~~


<a id="compare-d0944ea5866ae4935b4aad3ebab19d07"></a>

### [`00b53170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53170.md) → [`00b531b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b531b4.md) _ZN8firebase13remote_config8internal12config_value10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b531e4",
      "incomplete_value": true,
      "site": "00b531e4",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b531a0",
      "incomplete_value": true,
      "site": "00b531a0",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b531c8",
      "incomplete_value": true,
      "site": "00b531c8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53184",
      "incomplete_value": true,
      "site": "00b53184",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b53184"
      ],
      [
        "FALL_THROUGH",
        "00b531c8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b531c8",
      "incomplete_value": true,
      "site": "00b531e4",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53184",
      "incomplete_value": true,
      "site": "00b531a0",
      "value": [
        "INT_NOTEQUAL",
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
      "00b531c4",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b531e4",
      "WRITE",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b531c4",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b531e4",
      "WRITE",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b531a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53170.md#insn-00b531a0) · [`00b53180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53170.md#insn-00b53180) · [`00b53198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53170.md#insn-00b53198)
- 新版 `00b531e4`（命令位置の公開資料なし） · `00b531c4`（命令位置の公開資料なし） · `00b531dc`（命令位置の公開資料なし）

~~~diff
- 00b531a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
- 00b531a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b531e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b531e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b531a0 bytes 600e01f9
+ 00b531e4 bytes 602e01f9
- 00b53180 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:218:8"]]
- 00b53180 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b531c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:258:8"]]
+ 00b531c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53180 bytes 680e41f9
+ 00b531c4 bytes 682e41f9
- 00b53198 ["INT_ADD", "register:40f0:8", ["const:b53198:8", "const:4:8"]]
- 00b53198 ["CALL", null, ["callee:00bde090:8"]]
+ 00b531dc ["INT_ADD", "register:40f0:8", ["const:b531dc:8", "const:4:8"]]
+ 00b531dc ["CALL", null, ["callee:00bde090:8"]]
- 00b53198 bytes aa2b0294
+ 00b531dc bytes ad2b0294
~~~


<a id="compare-2331256c05ccaab9f5896874976b36df"></a>

### [`00b531c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b531c0.md) → [`00b53204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53204.md) _ZN8firebase13remote_config8internal12config_value15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5325c",
      "incomplete_value": true,
      "site": "00b5325c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53218",
      "incomplete_value": true,
      "site": "00b53218",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53238",
      "incomplete_value": true,
      "site": "00b53244",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:258:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b531f4",
      "incomplete_value": true,
      "site": "00b53200",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:218:8"
              ]
            ]
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
      "00b53218",
      "READ",
      [
        "storage",
        "010a1220",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53238",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5325c",
      "WRITE",
      [
        "storage",
        "010a1220",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53218",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53238",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5325c",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b531d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b531c0.md#insn-00b531d4) · [`00b53200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b531c0.md#insn-00b53200) · [`00b53218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b531c0.md#insn-00b53218)
- 新版 `00b53218`（命令位置の公開資料なし） · `00b53244`（命令位置の公開資料なし） · `00b5325c`（命令位置の公開資料なし）

~~~diff
- 00b531d4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:220:8"]]
- 00b531d4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b531d4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b53218 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:260:8"]]
+ 00b53218 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b53218 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b531d4 bytes a8824839
+ 00b53218 bytes a8824939
- 00b53200 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53200 ["INT_ADD", "register:40f0:8", ["const:b53200:8", "const:4:8"]]
- 00b53200 ["CALLIND", null, ["register:0:8"]]
+ 00b53244 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53244 ["INT_ADD", "register:40f0:8", ["const:b53244:8", "const:4:8"]]
+ 00b53244 ["CALLIND", null, ["register:0:8"]]
- 00b53200 bytes 00013fd6
+ 00b53244 bytes 00013fd6
- 00b53218 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b53218 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:220:8"]]
- 00b53218 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b5325c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b5325c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:260:8"]]
+ 00b5325c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b53218 bytes a0820839
+ 00b5325c bytes a0820939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-980fc065f9b51ad6ebb8a1a2e0d08c3a"></a>

### [`00b5322c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5322c.md) → [`00b53270`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53270.md) _ZN8firebase13remote_config8internal12config_value12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b532ac",
      "incomplete_value": true,
      "site": "00b532ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:260:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53268",
      "incomplete_value": true,
      "site": "00b53268",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:220:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b532cc",
      "incomplete_value": true,
      "site": "00b532cc",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53288",
      "incomplete_value": true,
      "site": "00b53288",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b53288",
      "incomplete_value": true,
      "site": "00b53288",
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
      "definition_site": "00b53244",
      "incomplete_value": true,
      "site": "00b53244",
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
      "00b53284",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53290",
      "READ",
      [
        "storage",
        "010a1220",
        null,
        "undefined1"
      ]
    ],
    [
      "00b532ac",
      "WRITE",
      [
        "storage",
        "010a1220",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53284",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53290",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined1"
      ]
    ],
    [
      "00b532ac",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5322c.md#insn-00b53240) · [`00b53268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5322c.md#insn-00b53268) · [`00b53284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5322c.md#insn-00b53284)
- 新版 `00b53284`（命令位置の公開資料なし） · `00b532ac`（命令位置の公開資料なし） · `00b532c8`（命令位置の公開資料なし）

~~~diff
- 00b53240 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:218:8"]]
- 00b53240 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53284 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
+ 00b53284 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53240 bytes 810e41f9
+ 00b53284 bytes 812e41f9
- 00b53268 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b53268 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b53268 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:220:8"]]
- 00b53268 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b532ac ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b532ac ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b532ac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:260:8"]]
+ 00b532ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b53268 bytes bf820839
+ 00b532ac bytes bf820939
- 00b53284 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53284 ["INT_ADD", "register:40f0:8", ["const:b53284:8", "const:4:8"]]
- 00b53284 ["CALLIND", null, ["register:0:8"]]
+ 00b532c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b532c8 ["INT_ADD", "register:40f0:8", ["const:b532c8:8", "const:4:8"]]
+ 00b532c8 ["CALLIND", null, ["register:0:8"]]
- 00b53284 bytes 00013fd6
+ 00b532c8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de114d13079aa79f4c3b7718b81f714a"></a>

### [`00b5329c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5329c.md) → [`00b532e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b532e0.md) _ZN8firebase13remote_config8internal12config_value14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b53320",
      "incomplete_value": true,
      "site": "00b53320",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b532dc",
      "incomplete_value": true,
      "site": "00b532dc",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b532fc",
      "incomplete_value": true,
      "site": "00b532fc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b532b8",
      "incomplete_value": true,
      "site": "00b532b8",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b532b8"
      ],
      [
        "FALL_THROUGH",
        "00b532fc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b532fc",
      "incomplete_value": true,
      "site": "00b53320",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b532b8",
      "incomplete_value": true,
      "site": "00b532dc",
      "value": [
        "INT_NOTEQUAL",
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
      "00b532f4",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53320",
      "WRITE",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53334",
      "PARAM",
      [
        "storage",
        "00c11828",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b532f4",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53320",
      "WRITE",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53334",
      "PARAM",
      [
        "storage",
        "00c11878",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b532dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5329c.md#insn-00b532dc) · [`00b532b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5329c.md#insn-00b532b0) · [`00b532d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5329c.md#insn-00b532d4)
- 新版 `00b53320`（命令位置の公開資料なし） · `00b532f4`（命令位置の公開資料なし） · `00b53318`（命令位置の公開資料なし）

~~~diff
- 00b532dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:218:8"]]
- 00b532dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53320 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
+ 00b53320 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b532dc bytes 800e01f9
+ 00b53320 bytes 802e01f9
- 00b532b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:218:8"]]
- 00b532b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b532f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
+ 00b532f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b532b0 bytes 810e41f9
+ 00b532f4 bytes 812e41f9
- 00b532d4 ["INT_ADD", "register:40f0:8", ["const:b532d4:8", "const:4:8"]]
- 00b532d4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53318 ["INT_ADD", "register:40f0:8", ["const:b53318:8", "const:4:8"]]
+ 00b53318 ["CALL", null, ["callee:00bde090:8"]]
- 00b532d4 bytes 5b2b0294
+ 00b53318 bytes 5e2b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef940a89735e4c8e3525c95a3ff07be5"></a>

### [`00b5330c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5330c.md) → [`00b53350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53350.md) _ZN8firebase13remote_config8internal12config_value11GetMethodIdENS2_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5336c",
      "incomplete_value": false,
      "site": "00b53370",
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
            "const:547:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53328",
      "incomplete_value": false,
      "site": "00b5332c",
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
            "const:5d4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b5337c",
      "incomplete_value": true,
      "site": "00b53388",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53338",
      "incomplete_value": true,
      "site": "00b53344",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b5336c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b5337c",
      "DATA",
      [
        "storage",
        "010a1228",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5336c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b5337c",
      "DATA",
      [
        "storage",
        "010a1268",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5332c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5330c.md#insn-00b5332c) · [`00b53328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5330c.md#insn-00b53328) · [`00b53334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5330c.md#insn-00b53334)
- 新版 `00b53370`（命令位置の公開資料なし） · `00b5336c`（命令位置の公開資料なし） · `00b53378`（命令位置の公開資料なし）

~~~diff
- 00b5332c ["INT_ADD", "register:40f0:8", ["const:b5332c:8", "const:4:8"]]
- 00b5332c ["CALL", null, ["callee:00bde180:8"]]
+ 00b53370 ["INT_ADD", "register:40f0:8", ["const:b53370:8", "const:4:8"]]
+ 00b53370 ["CALL", null, ["callee:00bde180:8"]]
- 00b5332c bytes 812b0294
+ 00b53370 bytes 842b0294
- 00b53328 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b53328 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b53328 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b53328 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5336c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b5336c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5336c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5336c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b53328 bytes 00501791
+ 00b5336c bytes 001c1591
- 00b53334 ["COPY", "tmp:0:8", ["const:228:8"]]
- 00b53334 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b53334 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b53334 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b53378 ["COPY", "tmp:0:8", ["const:268:8"]]
+ 00b53378 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53378 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53378 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b53334 bytes 08a10891
+ 00b53378 bytes 08a10991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23a221fb54f6d2d3359cd89dfa169762"></a>

### [`00b53348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53348.md) → [`00b5338c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b5338c.md) _ZN8firebase13remote_config8internal12config_value13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b533cc",
      "incomplete_value": true,
      "site": "00b533cc",
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
            "const:258:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53388",
      "incomplete_value": true,
      "site": "00b53388",
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
            "const:218:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b533a8",
      "incomplete_value": true,
      "site": "00b533a8",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53364",
      "incomplete_value": true,
      "site": "00b53364",
      "value": [
        "INT_NOTEQUAL",
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
    "guard": [
      [
        "FALL_THROUGH",
        "00b53364"
      ],
      [
        "FALL_THROUGH",
        "00b533a8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b533a8",
      "incomplete_value": true,
      "site": "00b533cc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53364",
      "incomplete_value": true,
      "site": "00b53388",
      "value": [
        "INT_NOTEQUAL",
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
      "00b533a0",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b533cc",
      "WRITE",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b533e4",
      "PARAM",
      [
        "storage",
        "010a1258",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b533a0",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b533cc",
      "WRITE",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b533e4",
      "PARAM",
      [
        "storage",
        "010a1298",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53348.md#insn-00b53388) · [`00b5335c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53348.md#insn-00b5335c) · [`00b53380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53348.md#insn-00b53380)
- 新版 `00b533cc`（命令位置の公開資料なし） · `00b533a0`（命令位置の公開資料なし） · `00b533c4`（命令位置の公開資料なし）

~~~diff
- 00b53388 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:218:8"]]
- 00b53388 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b533cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
+ 00b533cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53388 bytes 800e01f9
+ 00b533cc bytes 802e01f9
- 00b5335c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:218:8"]]
- 00b5335c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b533a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:258:8"]]
+ 00b533a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5335c bytes 810e41f9
+ 00b533a0 bytes 812e41f9
- 00b53380 ["INT_ADD", "register:40f0:8", ["const:b53380:8", "const:4:8"]]
- 00b53380 ["CALL", null, ["callee:00bde090:8"]]
+ 00b533c4 ["INT_ADD", "register:40f0:8", ["const:b533c4:8", "const:4:8"]]
+ 00b533c4 ["CALL", null, ["callee:00bde090:8"]]
- 00b53380 bytes 302b0294
+ 00b533c4 bytes 332b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37ce8730c316b5c979cf6943e55ce785"></a>

### [`00b533b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b533b8.md) → [`00b533fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b533fc.md) _ZN8firebase13remote_config8internal12config_value10GetFieldIdENS2_5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 80.00% / 新版 80.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53418",
      "incomplete_value": false,
      "site": "00b5341c",
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
            "const:5f2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b533d4",
      "incomplete_value": false,
      "site": "00b533d8",
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
            "const:67f:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b53428",
      "incomplete_value": true,
      "site": "00b53434",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b533e4",
      "incomplete_value": true,
      "site": "00b533f0",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b53418",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b53428",
      "DATA",
      [
        "storage",
        "010a1258",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b53418",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b53428",
      "DATA",
      [
        "storage",
        "010a1298",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b533d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b533b8.md#insn-00b533d8) · [`00b533d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b533b8.md#insn-00b533d4) · [`00b533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b533b8.md#insn-00b533e0)
- 新版 `00b5341c`（命令位置の公開資料なし） · `00b53418`（命令位置の公開資料なし） · `00b53424`（命令位置の公開資料なし）

~~~diff
- 00b533d8 ["INT_ADD", "register:40f0:8", ["const:b533d8:8", "const:4:8"]]
- 00b533d8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5341c ["INT_ADD", "register:40f0:8", ["const:b5341c:8", "const:4:8"]]
+ 00b5341c ["CALL", null, ["callee:00bde180:8"]]
- 00b533d8 bytes 562b0294
+ 00b5341c bytes 592b0294
- 00b533d4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b533d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b533d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b533d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b53418 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b53418 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53418 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53418 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b533d4 bytes 00fc1991
+ 00b53418 bytes 00c81791
- 00b533e0 ["COPY", "tmp:0:8", ["const:258:8"]]
- 00b533e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b533e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b533e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b53424 ["COPY", "tmp:0:8", ["const:298:8"]]
+ 00b53424 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53424 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53424 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b533e0 bytes 08610991
+ 00b53424 bytes 08610a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c7c38a39ad84dc449c39b21e148955b"></a>

### [`00b533f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b533f4.md) → [`00b53438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53438.md) _ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b53464",
      "incomplete_value": true,
      "site": "00b53464",
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
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53420",
      "incomplete_value": true,
      "site": "00b53420",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5344c",
      "incomplete_value": true,
      "site": "00b5344c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53408",
      "incomplete_value": true,
      "site": "00b53408",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53458",
      "incomplete_value": false,
      "site": "00b5345c",
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
            "const:6d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53414",
      "incomplete_value": false,
      "site": "00b53418",
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
            "const:75e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b53448",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53458",
      "PARAM",
      [
        "storage",
        "0029775e",
        null,
        "string"
      ]
    ],
    [
      "00b53464",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53448",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53458",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00b53464",
      "WRITE",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b533f4.md#insn-00b53418) · [`00b53420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b533f4.md#insn-00b53420) · [`00b53404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b533f4.md#insn-00b53404)
- 新版 `00b5345c`（命令位置の公開資料なし） · `00b53464`（命令位置の公開資料なし） · `00b53448`（命令位置の公開資料なし）

~~~diff
- 00b53418 ["INT_ADD", "register:40f0:8", ["const:b53418:8", "const:4:8"]]
- 00b53418 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5345c ["INT_ADD", "register:40f0:8", ["const:b5345c:8", "const:4:8"]]
+ 00b5345c ["CALL", null, ["callee:00bde090:8"]]
- 00b53418 bytes 0a2b0294
+ 00b5345c bytes 0d2b0294
- 00b53420 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
- 00b53420 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53464 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a0:8"]]
+ 00b53464 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53420 bytes 603201f9
+ 00b53464 bytes 605201f9
- 00b53404 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
- 00b53404 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53448 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a0:8"]]
+ 00b53448 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53404 bytes 683241f9
+ 00b53448 bytes 685241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17d9ac38d5d89a954169bdfa6810223f"></a>

### [`00b53434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53434.md) → [`00b53478`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53478.md) _ZN8firebase13remote_config8internal11config_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS7

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b534a4",
      "incomplete_value": true,
      "site": "00b534a4",
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
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53460",
      "incomplete_value": true,
      "site": "00b53460",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5348c",
      "incomplete_value": true,
      "site": "00b5348c",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53448",
      "incomplete_value": true,
      "site": "00b53448",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53494",
      "incomplete_value": false,
      "site": "00b5349c",
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
            "const:6d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53450",
      "incomplete_value": false,
      "site": "00b53458",
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
            "const:75e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b53488",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53494",
      "PARAM",
      [
        "storage",
        "0029775e",
        null,
        "string"
      ]
    ],
    [
      "00b534a4",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53488",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53494",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00b534a4",
      "WRITE",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53434.md#insn-00b53458) · [`00b53460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53434.md#insn-00b53460) · [`00b53444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53434.md#insn-00b53444)
- 新版 `00b5349c`（命令位置の公開資料なし） · `00b534a4`（命令位置の公開資料なし） · `00b53488`（命令位置の公開資料なし）

~~~diff
- 00b53458 ["INT_ADD", "register:40f0:8", ["const:b53458:8", "const:4:8"]]
- 00b53458 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5349c ["INT_ADD", "register:40f0:8", ["const:b5349c:8", "const:4:8"]]
+ 00b5349c ["CALL", null, ["callee:00bde090:8"]]
- 00b53458 bytes fa2a0294
+ 00b5349c bytes fd2a0294
- 00b53460 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
- 00b53460 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b534a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a0:8"]]
+ 00b534a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53460 bytes 603201f9
+ 00b534a4 bytes 605201f9
- 00b53444 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
- 00b53444 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53488 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a0:8"]]
+ 00b53488 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53444 bytes 683241f9
+ 00b53488 bytes 685241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-abcbb05c6b2b589c1f2d89dcd2c4d7ee"></a>

### [`00b53474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53474.md) → [`00b534b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b534b8.md) _ZN8firebase13remote_config8internal11config_info10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b534e8",
      "incomplete_value": true,
      "site": "00b534e8",
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
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b534a4",
      "incomplete_value": true,
      "site": "00b534a4",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b534cc",
      "incomplete_value": true,
      "site": "00b534cc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53488",
      "incomplete_value": true,
      "site": "00b53488",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b534d8",
      "incomplete_value": false,
      "site": "00b534e0",
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
            "const:6d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53494",
      "incomplete_value": false,
      "site": "00b5349c",
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
            "const:75e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b534c8",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b534d8",
      "PARAM",
      [
        "storage",
        "0029775e",
        null,
        "string"
      ]
    ],
    [
      "00b534e8",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b534c8",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b534d8",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00b534e8",
      "WRITE",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5349c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53474.md#insn-00b5349c) · [`00b534a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53474.md#insn-00b534a4) · [`00b53484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53474.md#insn-00b53484)
- 新版 `00b534e0`（命令位置の公開資料なし） · `00b534e8`（命令位置の公開資料なし） · `00b534c8`（命令位置の公開資料なし）

~~~diff
- 00b5349c ["INT_ADD", "register:40f0:8", ["const:b5349c:8", "const:4:8"]]
- 00b5349c ["CALL", null, ["callee:00bde090:8"]]
+ 00b534e0 ["INT_ADD", "register:40f0:8", ["const:b534e0:8", "const:4:8"]]
+ 00b534e0 ["CALL", null, ["callee:00bde090:8"]]
- 00b5349c bytes e92a0294
+ 00b534e0 bytes ec2a0294
- 00b534a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
- 00b534a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b534e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a0:8"]]
+ 00b534e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b534a4 bytes 603201f9
+ 00b534e8 bytes 605201f9
- 00b53484 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
- 00b53484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b534c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a0:8"]]
+ 00b534c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53484 bytes 683241f9
+ 00b534c8 bytes 685241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6b1366ee0a1034e5af218351717633b4"></a>

### [`00b534b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b534b8.md) → [`00b534fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b534fc.md) _ZN8firebase13remote_config8internal11config_info10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5352c",
      "incomplete_value": true,
      "site": "00b5352c",
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
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b534e8",
      "incomplete_value": true,
      "site": "00b534e8",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b53510",
      "incomplete_value": true,
      "site": "00b53510",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b534cc",
      "incomplete_value": true,
      "site": "00b534cc",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53518",
      "incomplete_value": false,
      "site": "00b53524",
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
            "const:6d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b534d4",
      "incomplete_value": false,
      "site": "00b534e0",
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
            "const:75e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5350c",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53518",
      "PARAM",
      [
        "storage",
        "0029775e",
        null,
        "string"
      ]
    ],
    [
      "00b5352c",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5350c",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53518",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00b5352c",
      "WRITE",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b534e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b534b8.md#insn-00b534e0) · [`00b534e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b534b8.md#insn-00b534e8) · [`00b534c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b534b8.md#insn-00b534c8)
- 新版 `00b53524`（命令位置の公開資料なし） · `00b5352c`（命令位置の公開資料なし） · `00b5350c`（命令位置の公開資料なし）

~~~diff
- 00b534e0 ["INT_ADD", "register:40f0:8", ["const:b534e0:8", "const:4:8"]]
- 00b534e0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53524 ["INT_ADD", "register:40f0:8", ["const:b53524:8", "const:4:8"]]
+ 00b53524 ["CALL", null, ["callee:00bde090:8"]]
- 00b534e0 bytes d82a0294
+ 00b53524 bytes db2a0294
- 00b534e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
- 00b534e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5352c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a0:8"]]
+ 00b5352c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b534e8 bytes 603201f9
+ 00b5352c bytes 605201f9
- 00b534c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:260:8"]]
- 00b534c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5350c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2a0:8"]]
+ 00b5350c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b534c8 bytes 683241f9
+ 00b5350c bytes 685241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd98488b3f60638b739a198be5c1873a"></a>

### [`00b53508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53508.md) → [`00b5354c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b5354c.md) _ZN8firebase13remote_config8internal11config_info15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b535a4",
      "incomplete_value": true,
      "site": "00b535a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53560",
      "incomplete_value": true,
      "site": "00b53560",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b53580",
      "incomplete_value": true,
      "site": "00b5358c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:2a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5353c",
      "incomplete_value": true,
      "site": "00b53548",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:10a1000:8"
              ],
              [
                "leaf",
                "const:260:8"
              ]
            ]
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
      "00b53560",
      "READ",
      [
        "storage",
        "010a1268",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53580",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b535a4",
      "WRITE",
      [
        "storage",
        "010a1268",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53560",
      "READ",
      [
        "storage",
        "010a12a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53580",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b535a4",
      "WRITE",
      [
        "storage",
        "010a12a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5351c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53508.md#insn-00b5351c) · [`00b53548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53508.md#insn-00b53548) · [`00b53560`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53508.md#insn-00b53560)
- 新版 `00b53560`（命令位置の公開資料なし） · `00b5358c`（命令位置の公開資料なし） · `00b535a4`（命令位置の公開資料なし）

~~~diff
- 00b5351c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:268:8"]]
- 00b5351c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b5351c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b53560 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:2a8:8"]]
+ 00b53560 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b53560 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b5351c bytes a8a24939
+ 00b53560 bytes a8a24a39
- 00b53548 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53548 ["INT_ADD", "register:40f0:8", ["const:b53548:8", "const:4:8"]]
- 00b53548 ["CALLIND", null, ["register:0:8"]]
+ 00b5358c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5358c ["INT_ADD", "register:40f0:8", ["const:b5358c:8", "const:4:8"]]
+ 00b5358c ["CALLIND", null, ["register:0:8"]]
- 00b53548 bytes 00013fd6
+ 00b5358c bytes 00013fd6
- 00b53560 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b53560 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:268:8"]]
- 00b53560 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b535a4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b535a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:2a8:8"]]
+ 00b535a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b53560 bytes a0a20939
+ 00b535a4 bytes a0a20a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8b0844fffa357f65da6a689675fd516"></a>

### [`00b53574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53574.md) → [`00b535b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b535b8.md) _ZN8firebase13remote_config8internal11config_info12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b535f4",
      "incomplete_value": true,
      "site": "00b535f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:2a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b535b0",
      "incomplete_value": true,
      "site": "00b535b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:268:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b53614",
      "incomplete_value": true,
      "site": "00b53614",
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
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b535d0",
      "incomplete_value": true,
      "site": "00b535d0",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b535d0",
      "incomplete_value": true,
      "site": "00b535d0",
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
      "definition_site": "00b5358c",
      "incomplete_value": true,
      "site": "00b5358c",
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
      "00b535cc",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b535d8",
      "READ",
      [
        "storage",
        "010a1268",
        null,
        "undefined1"
      ]
    ],
    [
      "00b535f4",
      "WRITE",
      [
        "storage",
        "010a1268",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b535cc",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b535d8",
      "READ",
      [
        "storage",
        "010a12a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b535f4",
      "WRITE",
      [
        "storage",
        "010a12a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53574.md#insn-00b53588) · [`00b535b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53574.md#insn-00b535b0) · [`00b535cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53574.md#insn-00b535cc)
- 新版 `00b535cc`（命令位置の公開資料なし） · `00b535f4`（命令位置の公開資料なし） · `00b53610`（命令位置の公開資料なし）

~~~diff
- 00b53588 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:260:8"]]
- 00b53588 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b535cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2a0:8"]]
+ 00b535cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53588 bytes 813241f9
+ 00b535cc bytes 815241f9
- 00b535b0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b535b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b535b0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:268:8"]]
- 00b535b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b535f4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b535f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b535f4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2a8:8"]]
+ 00b535f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b535b0 bytes bfa20939
+ 00b535f4 bytes bfa20a39
- 00b535cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b535cc ["INT_ADD", "register:40f0:8", ["const:b535cc:8", "const:4:8"]]
- 00b535cc ["CALLIND", null, ["register:0:8"]]
+ 00b53610 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53610 ["INT_ADD", "register:40f0:8", ["const:b53610:8", "const:4:8"]]
+ 00b53610 ["CALLIND", null, ["register:0:8"]]
- 00b535cc bytes 00013fd6
+ 00b53610 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee70e89f707a3b81f26a94c6d6632bf8"></a>

### [`00b535e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b535e4.md) → [`00b53628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53628.md) _ZN8firebase13remote_config8internal11config_info14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b53668",
      "incomplete_value": true,
      "site": "00b53668",
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
            "const:2a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53624",
      "incomplete_value": true,
      "site": "00b53624",
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
            "const:260:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b53644",
      "incomplete_value": true,
      "site": "00b53644",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b53600",
      "incomplete_value": true,
      "site": "00b53600",
      "value": [
        "INT_NOTEQUAL",
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
      "definition_site": "00b5364c",
      "incomplete_value": false,
      "site": "00b53660",
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
            "const:6d1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53608",
      "incomplete_value": false,
      "site": "00b5361c",
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
            "const:75e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5363c",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5364c",
      "PARAM",
      [
        "storage",
        "0029775e",
        null,
        "string"
      ]
    ],
    [
      "00b53668",
      "WRITE",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5363c",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5364c",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00b53668",
      "WRITE",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5361c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b535e4.md#insn-00b5361c) · [`00b53624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b535e4.md#insn-00b53624) · [`00b535f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b535e4.md#insn-00b535f8)
- 新版 `00b53660`（命令位置の公開資料なし） · `00b53668`（命令位置の公開資料なし） · `00b5363c`（命令位置の公開資料なし）

~~~diff
- 00b5361c ["INT_ADD", "register:40f0:8", ["const:b5361c:8", "const:4:8"]]
- 00b5361c ["CALL", null, ["callee:00bde090:8"]]
+ 00b53660 ["INT_ADD", "register:40f0:8", ["const:b53660:8", "const:4:8"]]
+ 00b53660 ["CALL", null, ["callee:00bde090:8"]]
- 00b5361c bytes 892a0294
+ 00b53660 bytes 8c2a0294
- 00b53624 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:260:8"]]
- 00b53624 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53668 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2a0:8"]]
+ 00b53668 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53624 bytes 803201f9
+ 00b53668 bytes 805201f9
- 00b535f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:260:8"]]
- 00b535f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5363c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2a0:8"]]
+ 00b5363c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b535f8 bytes 813241f9
+ 00b5363c bytes 815241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

