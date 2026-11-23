# v15.7.3 → v15.7.4 · 最優先の変更候補 (66)

[一覧の目次](README.md)

<a id="compare-7f40c15883366cd06372497138d89b58"></a>

### [`00af92fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af92fc.md) → [`00af9340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9340.md) _ZN8firebase10app_common16IsDefaultAppNameEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde860.md) · 呼出先 1件 [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)
- 新版 呼出元 1件 [`00bde8b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8b0.md) · 呼出先 1件 [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af9350",
      "incomplete_value": false,
      "site": "00af9354",
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
            "const:f51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af930c",
      "incomplete_value": false,
      "site": "00af9310",
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
            "const:ec6:8"
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
      "00af9350",
      "PARAM",
      [
        "storage",
        "002a4ec6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00af9350",
      "PARAM",
      [
        "storage",
        "002a4f51",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af9310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af92fc.md#insn-00af9310) · [`00af930c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af92fc.md#insn-00af930c)
- 新版 [`00af9354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9340.md#insn-00af9354) · [`00af9350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9340.md#insn-00af9350)

~~~diff
- 00af9310 ["INT_ADD", "register:40f0:8", ["const:af9310:8", "const:4:8"]]
- 00af9310 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00af9354 ["INT_ADD", "register:40f0:8", ["const:af9354:8", "const:4:8"]]
+ 00af9354 ["CALL", null, ["callee:00bde9d0:8"]]
- 00af9310 bytes 9c950394
+ 00af9354 bytes 9f950394
- 00af930c ["COPY", "tmp:0:8", ["const:ec6:8"]]
- 00af930c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00af930c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00af930c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00af9350 ["COPY", "tmp:0:8", ["const:f51:8"]]
+ 00af9350 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00af9350 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00af9350 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00af930c bytes 00183b91
+ 00af9350 bytes 00443d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e075f07955e856059a62ee1117424946"></a>

### [`00af9398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9398.md) → [`00af93dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af93dc.md) _ZN8firebase10app_common10GetAllAppsEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde800.md) · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00bde850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde850.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.36% / 新版 96.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00af945c",
      "incomplete_value": true,
      "site": "00af9460",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40b0:8"
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
      "definition_site": "00af9418",
      "incomplete_value": true,
      "site": "00af941c",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40b0:8"
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
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af940c",
      "incomplete_value": true,
      "site": "00af9418",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af93c8",
      "incomplete_value": true,
      "site": "00af93d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00af93fc",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9408",
      "READ",
      [
        "storage",
        "010a0cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9420",
      "READ",
      [
        "storage",
        "010a0cd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af93fc",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9408",
      "READ",
      [
        "storage",
        "010a0d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9420",
      "READ",
      [
        "storage",
        "010a0d18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af93d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9398.md#insn-00af93d4) · [`00af9460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9398.md#insn-00af9460) · [`00af93b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9398.md#insn-00af93b8)
- 新版 [`00af9418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af93dc.md#insn-00af9418) · [`00af94a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af93dc.md#insn-00af94a4) · [`00af93fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af93dc.md#insn-00af93fc)

~~~diff
- 00af93d4 ["INT_ADD", "register:40f0:8", ["const:af93d4:8", "const:4:8"]]
- 00af93d4 ["CALL", null, ["callee:00bddc20:8"]]
+ 00af9418 ["INT_ADD", "register:40f0:8", ["const:af9418:8", "const:4:8"]]
+ 00af9418 ["CALL", null, ["callee:00bddc20:8"]]
- 00af93d4 bytes ff910394
+ 00af9418 bytes 02920394
- 00af9460 ["INT_ADD", "register:40f0:8", ["const:af9460:8", "const:4:8"]]
- 00af9460 ["CALL", null, ["callee:00bde9c0:8"]]
+ 00af94a4 ["INT_ADD", "register:40f0:8", ["const:af94a4:8", "const:4:8"]]
+ 00af94a4 ["CALL", null, ["callee:00bde9c0:8"]]
- 00af9460 bytes 44950394
+ 00af94a4 bytes 47950394
- 00af93b8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cc0:8"]]
- 00af93b8 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af93fc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d00:8"]]
+ 00af93fc ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00af93b8 bytes 336146f9
+ 00af93fc bytes 338146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a0ac710a6b65f1b4d645c0b1a4cec492"></a>

### [`00af9550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9550.md) → [`00af9594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9594.md) _ZN8firebase10app_common9RemoveAppEPNS_3AppE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde890.md) · 呼出先 16件 [`0044a5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a5b8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bde8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8e0.md) · 呼出先 16件 [`0044a5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a5b8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 3件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af96ec",
      "incomplete_value": true,
      "site": "00af96ec",
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
            "const:d10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af96a8",
      "incomplete_value": true,
      "site": "00af96a8",
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
            "const:cd0:8"
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af9758",
      "incomplete_value": true,
      "site": "00af9758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:d18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af9714",
      "incomplete_value": true,
      "site": "00af9714",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00af95dc",
      "incomplete_value": true,
      "site": "00af95dc",
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
      "definition_site": "00af9598",
      "incomplete_value": true,
      "site": "00af9598",
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
      "00af95c8",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af95d8",
      "READ",
      [
        "storage",
        "010a0cd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9688",
      "READ",
      [
        "storage",
        "010a0cd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af95c8",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00af95d8",
      "READ",
      [
        "storage",
        "010a0d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00af9688",
      "READ",
      [
        "storage",
        "010a0d18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af958c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9550.md#insn-00af958c) · [`00af9694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9550.md#insn-00af9694) · [`00af96a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9550.md#insn-00af96a8)
- 新版 [`00af95d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9594.md#insn-00af95d0) · [`00af96d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9594.md#insn-00af96d8) · [`00af96ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af9594.md#insn-00af96ec)

~~~diff
- 00af958c ["INT_ADD", "register:40f0:8", ["const:af958c:8", "const:4:8"]]
- 00af958c ["CALL", null, ["callee:00bddc20:8"]]
+ 00af95d0 ["INT_ADD", "register:40f0:8", ["const:af95d0:8", "const:4:8"]]
+ 00af95d0 ["CALL", null, ["callee:00bddc20:8"]]
- 00af958c bytes 91910394
+ 00af95d0 bytes 94910394
- 00af9694 ["INT_ADD", "register:40f0:8", ["const:af9694:8", "const:4:8"]]
- 00af9694 ["CALL", null, ["callee:00bde9a0:8"]]
+ 00af96d8 ["INT_ADD", "register:40f0:8", ["const:af96d8:8", "const:4:8"]]
+ 00af96d8 ["CALL", null, ["callee:00bde9a0:8"]]
- 00af9694 bytes af940394
+ 00af96d8 bytes b2940394
- 00af96a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
- 00af96a8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00af96a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00af96ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d10:8"]]
+ 00af96ec ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00af96ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00af96a8 bytes 1f6906f9
+ 00af96ec bytes 1f8906f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-979b52b440a60ecf4476de62a6d267c3"></a>

### [`00af9760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9760.md) → [`00af97a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af97a4.md) _ZN8firebase10app_common14DestroyAllAppsEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.71% / 新版 97.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00af97e0",
      "incomplete_value": true,
      "site": "00af97e0",
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
      "definition_site": "00af979c",
      "incomplete_value": true,
      "site": "00af979c",
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
      "definition_site": "00af9810",
      "incomplete_value": true,
      "site": "00af9814",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40d8:8"
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
      "definition_site": "00af97cc",
      "incomplete_value": true,
      "site": "00af97d0",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              [
                "live",
                "register:40d8:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af97d0",
      "incomplete_value": true,
      "site": "00af97d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af978c",
      "incomplete_value": true,
      "site": "00af9790",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00af97c4",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af97cc",
      "READ",
      [
        "storage",
        "010a0cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af97dc",
      "READ",
      [
        "storage",
        "010a0cd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00af97c4",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00af97cc",
      "READ",
      [
        "storage",
        "010a0d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00af97dc",
      "READ",
      [
        "storage",
        "010a0d18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af9790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9760.md#insn-00af9790) · [`00af9780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9760.md#insn-00af9780) · [`00af9788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af9/00af9760.md#insn-00af9788)
- 新版 [`00af97d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af97a4.md#insn-00af97d4) · [`00af97c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af97a4.md#insn-00af97c4) · [`00af97cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af9/00af97a4.md#insn-00af97cc)

~~~diff
- 00af9790 ["INT_ADD", "register:40f0:8", ["const:af9790:8", "const:4:8"]]
- 00af9790 ["CALL", null, ["callee:00bddc20:8"]]
+ 00af97d4 ["INT_ADD", "register:40f0:8", ["const:af97d4:8", "const:4:8"]]
+ 00af97d4 ["CALL", null, ["callee:00bddc20:8"]]
- 00af9790 bytes 10910394
+ 00af97d4 bytes 13910394
- 00af9780 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cc0:8"]]
- 00af9780 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af97c4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d00:8"]]
+ 00af97c4 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00af9780 bytes 336146f9
+ 00af97c4 bytes 338146f9
- 00af9788 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cd0:8"]]
- 00af9788 ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af97cc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d10:8"]]
+ 00af97cc ["LOAD", "register:40b8:8", ["const:1b1:8", "tmp:0:8"]]
- 00af9788 bytes 176946f9
+ 00af97cc bytes 178946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a93a8b1742415bfaaeb4c2a00942f360"></a>

### [`00afa148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa148.md) → [`00afa18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa18c.md) _ZN8firebase10app_common30RegisterLibrariesFromUserAgentEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00afa1d4",
      "incomplete_value": true,
      "site": "00afa1d4",
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
              "LOAD"
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
      "definition_site": "00afa190",
      "incomplete_value": true,
      "site": "00afa190",
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
              "LOAD"
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
      "definition_site": "00afa1c0",
      "incomplete_value": true,
      "site": "00afa1c4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afa17c",
      "incomplete_value": true,
      "site": "00afa180",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:cc0:8"
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
    "guard": [
      [
        "FALL_THROUGH",
        "00afa190"
      ],
      [
        "FALL_THROUGH",
        "00afa1d4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00afa1d4",
      "incomplete_value": true,
      "site": "00afa1e8",
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
              "LOAD"
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
      "definition_site": "00afa190",
      "incomplete_value": true,
      "site": "00afa1a4",
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
              "LOAD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "00afa1bc",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afa1cc",
      "READ",
      [
        "storage",
        "00c1b900",
        null,
        "pointer"
      ]
    ],
    [
      "00afa1d0",
      "READ",
      [
        "storage",
        "010a0cc8",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00afa1bc",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00afa1cc",
      "READ",
      [
        "storage",
        "00c1b950",
        null,
        "pointer"
      ]
    ],
    [
      "00afa1d0",
      "READ",
      [
        "storage",
        "010a0d08",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afa180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa148.md#insn-00afa180) · [`00afa1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa148.md#insn-00afa1d4) · [`00afa178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa148.md#insn-00afa178)
- 新版 [`00afa1c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa18c.md#insn-00afa1c4) · [`00afa218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa18c.md#insn-00afa218) · [`00afa1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa18c.md#insn-00afa1bc)

~~~diff
- 00afa180 ["INT_ADD", "register:40f0:8", ["const:afa180:8", "const:4:8"]]
- 00afa180 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afa1c4 ["INT_ADD", "register:40f0:8", ["const:afa1c4:8", "const:4:8"]]
+ 00afa1c4 ["CALL", null, ["callee:00bddc20:8"]]
- 00afa180 bytes 948e0394
+ 00afa1c4 bytes 978e0394
- 00afa1d4 ["INT_ADD", "register:40f0:8", ["const:afa1d4:8", "const:4:8"]]
- 00afa1d4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00afa218 ["INT_ADD", "register:40f0:8", ["const:afa218:8", "const:4:8"]]
+ 00afa218 ["CALL", null, ["callee:00bdb040:8"]]
- 00afa1d4 bytes 87830394
+ 00afa218 bytes 8a830394
- 00afa178 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 00afa178 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00afa1bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d00:8"]]
+ 00afa1bc ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00afa178 bytes 136146f9
+ 00afa1bc bytes 138146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6702f1599cd8eb7f5d938412554eb0e8"></a>

### [`00afa2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa2a0.md) → [`00afa2e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa2e4.md) _ZN8firebase10app_common16RegisterSdkUsageEPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde870`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde870.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde8e0.md)
- 新版 呼出元 1件 [`00bde8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde8c0.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde930.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 91.18% / 新版 91.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_condition` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00afa314",
      "incomplete_value": true,
      "site": "00afa314",
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
              "LOAD"
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
      "definition_site": "00afa2d0",
      "incomplete_value": true,
      "site": "00afa2d0",
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
              "LOAD"
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
      "definition_site": "00afa300",
      "incomplete_value": true,
      "site": "00afa304",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afa2bc",
      "incomplete_value": true,
      "site": "00afa2c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cc0:8"
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
      "definition_site": "00afa350",
      "incomplete_value": true,
      "site": "00afa35c",
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
            "const:685:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afa30c",
      "incomplete_value": true,
      "site": "00afa318",
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
            "const:712:8"
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
      "00afa2f8",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afa30c",
      "READ",
      [
        "storage",
        "00c1b900",
        null,
        "pointer"
      ]
    ],
    [
      "00afa310",
      "READ",
      [
        "storage",
        "010a0cc8",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00afa2f8",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00afa30c",
      "READ",
      [
        "storage",
        "00c1b950",
        null,
        "pointer"
      ]
    ],
    [
      "00afa310",
      "READ",
      [
        "storage",
        "010a0d08",
        "_ZN8firebase10app_common15LibraryRegistry17library_registry_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afa2b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa2a0.md#insn-00afa2b4) · [`00afa2c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa2a0.md#insn-00afa2c0) · [`00afa30c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa2a0.md#insn-00afa30c)
- 新版 [`00afa2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa2e4.md#insn-00afa2f8) · [`00afa304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa2e4.md#insn-00afa304) · [`00afa350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa2e4.md#insn-00afa350)

~~~diff
- 00afa2b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 00afa2b4 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00afa2f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d00:8"]]
+ 00afa2f8 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00afa2b4 bytes 136146f9
+ 00afa2f8 bytes 138146f9
- 00afa2c0 ["INT_ADD", "register:40f0:8", ["const:afa2c0:8", "const:4:8"]]
- 00afa2c0 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afa304 ["INT_ADD", "register:40f0:8", ["const:afa304:8", "const:4:8"]]
+ 00afa304 ["CALL", null, ["callee:00bddc20:8"]]
- 00afa2c0 bytes 448e0394
+ 00afa304 bytes 478e0394
- 00afa30c ["COPY", "tmp:0:8", ["const:712:8"]]
- 00afa30c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00afa30c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00afa30c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00afa350 ["COPY", "tmp:0:8", ["const:685:8"]]
+ 00afa350 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00afa350 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00afa350 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00afa30c bytes 00481c91
+ 00afa350 bytes 00141a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dd7c3a28279ce40c3904d70194310af"></a>

### [`00afa88c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa88c.md) → [`00afa8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa8d0.md) _ZN8firebase10app_common19FindAppLoggerByNameEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00afa914",
      "incomplete_value": true,
      "site": "00afa914",
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
      "definition_site": "00afa8d0",
      "incomplete_value": true,
      "site": "00afa8d0",
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
      "definition_site": "00afa9b0",
      "incomplete_value": true,
      "site": "00afa9b4",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_ADD",
              [
                "live",
                "register:40a0:8"
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
      "definition_site": "00afa96c",
      "incomplete_value": true,
      "site": "00afa970",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "INT_ADD",
              [
                "live",
                "register:40a0:8"
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
    "ordinal": 5,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afa904",
      "incomplete_value": true,
      "site": "00afa908",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d00:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afa8c0",
      "incomplete_value": true,
      "site": "00afa8c4",
      "value": [
        "LOAD",
        "8",
        [
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
      "00afa900",
      "READ",
      [
        "storage",
        "010a0cc0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afa910",
      "READ",
      [
        "storage",
        "010a0cd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00afa9a8",
      "READ",
      [
        "storage",
        "010a0cd8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00afa900",
      "READ",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ],
    [
      "00afa910",
      "READ",
      [
        "storage",
        "010a0d18",
        null,
        "undefined8"
      ]
    ],
    [
      "00afa9a8",
      "READ",
      [
        "storage",
        "010a0d18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afa8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa88c.md#insn-00afa8c4) · [`00afa91c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa88c.md#insn-00afa91c) · [`00afa8bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa88c.md#insn-00afa8bc)
- 新版 [`00afa908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa8d0.md#insn-00afa908) · [`00afa960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa8d0.md#insn-00afa960) · [`00afa900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afa8d0.md#insn-00afa900)

~~~diff
- 00afa8c4 ["INT_ADD", "register:40f0:8", ["const:afa8c4:8", "const:4:8"]]
- 00afa8c4 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afa908 ["INT_ADD", "register:40f0:8", ["const:afa908:8", "const:4:8"]]
+ 00afa908 ["CALL", null, ["callee:00bddc20:8"]]
- 00afa8c4 bytes c38c0394
+ 00afa908 bytes c68c0394
- 00afa91c ["INT_ADD", "register:40f0:8", ["const:afa91c:8", "const:4:8"]]
- 00afa91c ["CALL", null, ["callee:00bdb040:8"]]
+ 00afa960 ["INT_ADD", "register:40f0:8", ["const:afa960:8", "const:4:8"]]
+ 00afa960 ["CALL", null, ["callee:00bdb040:8"]]
- 00afa91c bytes b5810394
+ 00afa960 bytes b8810394
- 00afa8bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 00afa8bc ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00afa900 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d00:8"]]
+ 00afa900 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00afa8bc bytes 136146f9
+ 00afa900 bytes 138146f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-550f3e6f88b42be37dac9a40a00a7ff5"></a>

### [`00afafcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afafcc.md) → [`00afb010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb010.md) _INIT_271

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00afb01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb01c.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00afb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb060.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00afb054",
      "incomplete_value": false,
      "site": "00afb054",
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
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afb010",
      "incomplete_value": false,
      "site": "00afb010",
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
            "const:cc0:8"
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
      "definition_site": "00afb024",
      "incomplete_value": true,
      "site": "00afb034",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afafe0",
      "incomplete_value": true,
      "site": "00afaff0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8a0:8"
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
      "definition_site": "00afb028",
      "incomplete_value": true,
      "site": "00afb034",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:958:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afafe4",
      "incomplete_value": true,
      "site": "00afaff0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:908:8"
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
      "00afb024",
      "READ",
      [
        "storage",
        "00c1b8a0",
        null,
        "pointer"
      ]
    ],
    [
      "00afb024",
      "PARAM",
      [
        "storage",
        "00afb01c",
        "_ZN8firebase6LoggerD2Ev",
        null
      ]
    ],
    [
      "00afb028",
      "READ",
      [
        "storage",
        "00c1b908",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00afb024",
      "READ",
      [
        "storage",
        "00c1b8f0",
        null,
        "pointer"
      ]
    ],
    [
      "00afb024",
      "PARAM",
      [
        "storage",
        "00afb060",
        "_ZN8firebase6LoggerD2Ev",
        null
      ]
    ],
    [
      "00afb028",
      "READ",
      [
        "storage",
        "00c1b958",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afafcc.md#insn-00afaff0) · [`00afb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afafcc.md#insn-00afb010) · [`00afafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afafcc.md#insn-00afafe0)
- 新版 [`00afb034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb010.md#insn-00afb034) · [`00afb054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb010.md#insn-00afb054) · [`00afb024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb010.md#insn-00afb024)

~~~diff
- 00afaff0 ["INT_ADD", "register:40f0:8", ["const:afaff0:8", "const:4:8"]]
- 00afaff0 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00afb034 ["INT_ADD", "register:40f0:8", ["const:afb034:8", "const:4:8"]]
+ 00afb034 ["CALL", null, ["callee:00bdafe0:8"]]
- 00afaff0 bytes e87f0394
+ 00afb034 bytes eb7f0394
- 00afb010 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:cc0:8"]]
- 00afb010 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00afb054 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d00:8"]]
+ 00afb054 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00afb010 bytes 136106f9
+ 00afb054 bytes 138106f9
- 00afafe0 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8a0:8"]]
- 00afafe0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00afb024 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:8f0:8"]]
+ 00afb024 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00afafe0 bytes 005044f9
+ 00afb024 bytes 007844f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-884daa753055e69261db1ec2f26c2c52"></a>

### [`00afb754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb754.md) → [`00afb798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb798.md) _ZN8firebase8callback10InitializeEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde900.md) · 呼出先 4件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)
- 新版 呼出元 1件 [`00bde950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde950.md) · 呼出先 4件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00afb7f8",
      "incomplete_value": false,
      "site": "00afb7f8",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afb7b4",
      "incomplete_value": false,
      "site": "00afb7b4",
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
            "const:cf0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00afb800",
      "incomplete_value": true,
      "site": "00afb800",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afb7bc",
      "incomplete_value": true,
      "site": "00afb7bc",
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
            "const:ce8:8"
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
      "definition_site": "00afb7b0",
      "incomplete_value": true,
      "site": "00afb7b4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afb76c",
      "incomplete_value": true,
      "site": "00afb770",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
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
      "00afb7ac",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afb7bc",
      "READ",
      [
        "storage",
        "010a0ce8",
        null,
        "undefined4"
      ]
    ],
    [
      "00afb7f0",
      "READ",
      [
        "storage",
        "010a0ce8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00afb7ac",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00afb7bc",
      "READ",
      [
        "storage",
        "010a0d28",
        null,
        "undefined4"
      ]
    ],
    [
      "00afb7f0",
      "READ",
      [
        "storage",
        "010a0d28",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb754.md#insn-00afb770) · [`00afb778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb754.md#insn-00afb778) · [`00afb7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb754.md#insn-00afb7b4)
- 新版 [`00afb7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb798.md#insn-00afb7b4) · [`00afb7bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb798.md#insn-00afb7bc) · [`00afb7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb798.md#insn-00afb7f8)

~~~diff
- 00afb770 ["INT_ADD", "register:40f0:8", ["const:afb770:8", "const:4:8"]]
- 00afb770 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afb7b4 ["INT_ADD", "register:40f0:8", ["const:afb7b4:8", "const:4:8"]]
+ 00afb7b4 ["CALL", null, ["callee:00bddc20:8"]]
- 00afb770 bytes 18890394
+ 00afb7b4 bytes 1b890394
- 00afb778 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ce8:8"]]
- 00afb778 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00afb778 ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
+ 00afb7bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d28:8"]]
+ 00afb7bc ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00afb7bc ["INT_ZEXT", "register:4040:8", ["tmp:1:4"]]
- 00afb778 bytes a8ea4cb9
+ 00afb7bc bytes a82a4db9
- 00afb7b4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:cf0:8"]]
- 00afb7b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00afb7f8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d30:8"]]
+ 00afb7f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00afb7b4 bytes 347906f9
+ 00afb7f8 bytes 349906f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afd0f62ba6377216b1d2ade7c2494f20"></a>

### [`00afb944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb944.md) → [`00afb988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb988.md) FUN_00afb988

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 3件 [`00afb7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb7e8.md) [`00afbd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbd1c.md) [`00afbe48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbe48.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md)
- 新版 呼出元 3件 [`00afb82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb82c.md) [`00afbd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbd60.md) [`00afbe8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbe8c.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.58% / 新版 89.58%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00afb9bc",
      "incomplete_value": true,
      "site": "00afb9bc",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afb978",
      "incomplete_value": true,
      "site": "00afb978",
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
            "const:ce8:8"
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
      "definition_site": "00afb9dc",
      "incomplete_value": true,
      "site": "00afb9dc",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afb998",
      "incomplete_value": true,
      "site": "00afb998",
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
            "const:ce8:8"
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
      "definition_site": "00afb9f0",
      "incomplete_value": false,
      "site": "00afb9f0",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afb9ac",
      "incomplete_value": false,
      "site": "00afb9ac",
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
            "const:cf0:8"
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
      "00afb99c",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afb9b0",
      "READ",
      [
        "storage",
        "010a0ce8",
        null,
        "undefined4"
      ]
    ],
    [
      "00afb9bc",
      "WRITE",
      [
        "storage",
        "010a0ce8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00afb99c",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00afb9b0",
      "READ",
      [
        "storage",
        "010a0d28",
        null,
        "undefined4"
      ]
    ],
    [
      "00afb9bc",
      "WRITE",
      [
        "storage",
        "010a0d28",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afb964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb944.md#insn-00afb964) · [`00afb978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb944.md#insn-00afb978) · [`00afb998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb944.md#insn-00afb998)
- 新版 [`00afb9a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb988.md#insn-00afb9a8) · [`00afb9bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb988.md#insn-00afb9bc) · [`00afb9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb988.md#insn-00afb9dc)

~~~diff
- 00afb964 ["INT_ADD", "register:40f0:8", ["const:afb964:8", "const:4:8"]]
- 00afb964 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afb9a8 ["INT_ADD", "register:40f0:8", ["const:afb9a8:8", "const:4:8"]]
+ 00afb9a8 ["CALL", null, ["callee:00bddc20:8"]]
- 00afb964 bytes 9b880394
+ 00afb9a8 bytes 9e880394
- 00afb978 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ce8:8"]]
- 00afb978 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
+ 00afb9bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d28:8"]]
+ 00afb9bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:4"]]
- 00afb978 bytes a1ea0cb9
+ 00afb9bc bytes a12a0db9
- 00afb998 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ce8:8"]]
- 00afb998 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00afb9dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d28:8"]]
+ 00afb9dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00afb998 bytes a8ea0cb9
+ 00afb9dc bytes a82a0db9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-247ec632a28633d821594d190cd49ac6"></a>

### [`00afba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afba04.md) → [`00afba48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afba48.md) _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdebe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdebe0.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md) [`00bdec00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec00.md)
- 新版 呼出元 1件 [`00bdec30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec30.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md) [`00bdec50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec50.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 84.78% / 新版 84.78%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00afbabc",
      "incomplete_value": true,
      "site": "00afbabc",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afba78",
      "incomplete_value": true,
      "site": "00afba78",
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
            "const:cf0:8"
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
      "definition_site": "00afbac8",
      "incomplete_value": true,
      "site": "00afbac8",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afba84",
      "incomplete_value": true,
      "site": "00afba84",
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
            "const:ce8:8"
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
      "definition_site": "00afba68",
      "incomplete_value": true,
      "site": "00afba6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afba24",
      "incomplete_value": true,
      "site": "00afba28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
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
      "00afba60",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afba70",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afba80",
      "READ",
      [
        "storage",
        "010a0ce8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00afba60",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00afba70",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00afba80",
      "READ",
      [
        "storage",
        "010a0d28",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afba28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afba04.md#insn-00afba28) · [`00afba34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afba04.md#insn-00afba34) · [`00afba78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afba04.md#insn-00afba78)
- 新版 [`00afba6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afba48.md#insn-00afba6c) · [`00afba78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afba48.md#insn-00afba78) · [`00afbabc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afba48.md#insn-00afbabc)

~~~diff
- 00afba28 ["INT_ADD", "register:40f0:8", ["const:afba28:8", "const:4:8"]]
- 00afba28 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afba6c ["INT_ADD", "register:40f0:8", ["const:afba6c:8", "const:4:8"]]
+ 00afba6c ["CALL", null, ["callee:00bddc20:8"]]
- 00afba28 bytes 6a880394
+ 00afba6c bytes 6d880394
- 00afba34 ["INT_ADD", "register:40f0:8", ["const:afba34:8", "const:4:8"]]
- 00afba34 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afba78 ["INT_ADD", "register:40f0:8", ["const:afba78:8", "const:4:8"]]
+ 00afba78 ["CALL", null, ["callee:00bddc20:8"]]
- 00afba34 bytes 67880394
+ 00afba78 bytes 6a880394
- 00afba78 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:cf0:8"]]
- 00afba78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
+ 00afbabc ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:d30:8"]]
+ 00afbabc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 00afba78 bytes f67a06f9
+ 00afbabc bytes f69a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7774e6d2ae3e003cfdd96334e83b1c45"></a>

### [`00afbd1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbd1c.md) → [`00afbd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbd60.md) _ZN8firebase8callback14RemoveCallbackEPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00afb944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb944.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00afb988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb988.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bdde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.33% / 新版 85.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00afbde4",
      "incomplete_value": true,
      "site": "00afbde4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afbda0",
      "incomplete_value": true,
      "site": "00afbda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40c8:8"
          ],
          [
            "leaf",
            "const:cf0:8"
          ]
        ]
      ]
    },
    "ordinal": 12,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00afbdf0",
      "incomplete_value": true,
      "site": "00afbdf0",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afbdac",
      "incomplete_value": true,
      "site": "00afbdac",
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
            "const:ce8:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afbda0",
      "incomplete_value": true,
      "site": "00afbda4",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afbd5c",
      "incomplete_value": true,
      "site": "00afbd60",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ce0:8"
              ]
            ]
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
      "00afbd7c",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afbd90",
      "READ",
      [
        "storage",
        "010a0ce8",
        null,
        "undefined4"
      ]
    ],
    [
      "00afbd9c",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00afbd7c",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00afbd90",
      "READ",
      [
        "storage",
        "010a0d28",
        null,
        "undefined4"
      ]
    ],
    [
      "00afbd9c",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afbd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbd1c.md#insn-00afbd60) · [`00afbda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbd1c.md#insn-00afbda0) · [`00afbdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbd1c.md#insn-00afbdac)
- 新版 [`00afbda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbd60.md#insn-00afbda4) · [`00afbde4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbd60.md#insn-00afbde4) · [`00afbdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbd60.md#insn-00afbdf0)

~~~diff
- 00afbd60 ["INT_ADD", "register:40f0:8", ["const:afbd60:8", "const:4:8"]]
- 00afbd60 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afbda4 ["INT_ADD", "register:40f0:8", ["const:afbda4:8", "const:4:8"]]
+ 00afbda4 ["CALL", null, ["callee:00bddc20:8"]]
- 00afbd60 bytes 9c870394
+ 00afbda4 bytes 9f870394
- 00afbda0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:cf0:8"]]
- 00afbda0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
+ 00afbde4 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:d30:8"]]
+ 00afbde4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40b0:8"]]
- 00afbda0 bytes 367b06f9
+ 00afbde4 bytes 369b06f9
- 00afbdac ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:ce8:8"]]
- 00afbdac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00afbdf0 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:d28:8"]]
+ 00afbdf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00afbdac bytes 08eb0cb9
+ 00afbdf0 bytes 082b0db9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c192aba99d7edffa229430c43dea87b5"></a>

### [`00afbe48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbe48.md) → [`00afbe8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbe8c.md) _ZN8firebase8callback13PollCallbacksEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00afb944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb944.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb780.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00afb988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb988.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb7d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7d0.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 84.75% / 新版 84.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 3件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00afbf08",
      "incomplete_value": true,
      "site": "00afbf08",
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
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afbec4",
      "incomplete_value": true,
      "site": "00afbec4",
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
            "const:cf0:8"
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
      "definition_site": "00afbf14",
      "incomplete_value": true,
      "site": "00afbf14",
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
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afbed0",
      "incomplete_value": true,
      "site": "00afbed0",
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
            "const:ce8:8"
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
      "definition_site": "00afbf30",
      "incomplete_value": false,
      "site": "00afbf30",
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
            "const:d40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afbeec",
      "incomplete_value": false,
      "site": "00afbeec",
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
            "const:d00:8"
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
      "00afbea4",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afbeb4",
      "READ",
      [
        "storage",
        "010a0ce8",
        null,
        "undefined4"
      ]
    ],
    [
      "00afbec0",
      "READ",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00afbea4",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00afbeb4",
      "READ",
      [
        "storage",
        "010a0d28",
        null,
        "undefined4"
      ]
    ],
    [
      "00afbec0",
      "READ",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afbe68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbe48.md#insn-00afbe68) · [`00afbe84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbe48.md#insn-00afbe84) · [`00afbebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbe48.md#insn-00afbebc)
- 新版 [`00afbeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbe8c.md#insn-00afbeac) · [`00afbec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbe8c.md#insn-00afbec8) · [`00afbf00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbe8c.md#insn-00afbf00)

~~~diff
- 00afbe68 ["INT_ADD", "register:40f0:8", ["const:afbe68:8", "const:4:8"]]
- 00afbe68 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afbeac ["INT_ADD", "register:40f0:8", ["const:afbeac:8", "const:4:8"]]
+ 00afbeac ["CALL", null, ["callee:00bddc20:8"]]
- 00afbe68 bytes 5a870394
+ 00afbeac bytes 5d870394
- 00afbe84 ["INT_ADD", "register:40f0:8", ["const:afbe84:8", "const:4:8"]]
- 00afbe84 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afbec8 ["INT_ADD", "register:40f0:8", ["const:afbec8:8", "const:4:8"]]
+ 00afbec8 ["CALL", null, ["callee:00bddc20:8"]]
- 00afbe84 bytes 53870394
+ 00afbec8 bytes 56870394
- 00afbebc ["INT_ADD", "register:40f0:8", ["const:afbebc:8", "const:4:8"]]
- 00afbebc ["CALL", null, ["callee:00bdde20:8"]]
+ 00afbf00 ["INT_ADD", "register:40f0:8", ["const:afbf00:8", "const:4:8"]]
+ 00afbf00 ["CALL", null, ["callee:00bdde20:8"]]
- 00afbebc bytes c5870394
+ 00afbf00 bytes c8870394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6f2def5a81e32f71a457f8452d76997"></a>

### [`00afc06c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc06c.md) → [`00afc0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc0b0.md) _ZN8firebase8callback18CallbackDispatcherD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdec30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec30.md) · 呼出先 6件 [`00bdafe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafe0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md)
- 新版 呼出元 1件 [`00bdec80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdec80.md) · 呼出先 6件 [`00bdb030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb030.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.02% / 新版 99.02%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afc0dc",
      "incomplete_value": false,
      "site": "00afc0e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:e08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afc098",
      "incomplete_value": false,
      "site": "00afc09c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:d7d:8"
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
      "00afc0dc",
      "PARAM",
      [
        "storage",
        "0029dd7d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00afc0dc",
      "PARAM",
      [
        "storage",
        "0029de08",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc06c.md#insn-00afc09c) · [`00afc088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc06c.md#insn-00afc088) · [`00afc098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc06c.md#insn-00afc098)
- 新版 [`00afc0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc0b0.md#insn-00afc0e0) · [`00afc0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc0b0.md#insn-00afc0cc) · [`00afc0dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc0b0.md#insn-00afc0dc)

~~~diff
- 00afc09c ["INT_ADD", "register:40f0:8", ["const:afc09c:8", "const:4:8"]]
- 00afc09c ["CALL", null, ["callee:00bddf60:8"]]
+ 00afc0e0 ["INT_ADD", "register:40f0:8", ["const:afc0e0:8", "const:4:8"]]
+ 00afc0e0 ["CALL", null, ["callee:00bddf60:8"]]
- 00afc09c bytes 9d870394
+ 00afc0e0 bytes a0870394
- 00afc088 ["INT_ADD", "register:40f0:8", ["const:afc088:8", "const:4:8"]]
- 00afc088 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afc0cc ["INT_ADD", "register:40f0:8", ["const:afc0cc:8", "const:4:8"]]
+ 00afc0cc ["CALL", null, ["callee:00bddc20:8"]]
- 00afc088 bytes d2860394
+ 00afc0cc bytes d5860394
- 00afc098 ["COPY", "tmp:0:8", ["const:d7d:8"]]
- 00afc098 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00afc098 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00afc098 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00afc0dc ["COPY", "tmp:0:8", ["const:e08:8"]]
+ 00afc0dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00afc0dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00afc0dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00afc098 bytes 00f43591
+ 00afc0dc bytes 00203891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88a67078d47a0da8a1b19e7cd75b7d8c"></a>

### [`00afc204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc204.md) → [`00afc248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc248.md) _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEED2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.32% / 新版 90.32%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00afc268",
      "incomplete_value": true,
      "site": "00afc26c",
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
      "definition_site": "00afc224",
      "incomplete_value": true,
      "site": "00afc228",
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
      "00afc260",
      "READ",
      [
        "storage",
        "00c1b938",
        null,
        "pointer"
      ]
    ],
    [
      "00afc26c",
      "DATA",
      [
        "storage",
        "00c107a8",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00afc260",
      "READ",
      [
        "storage",
        "00c1b988",
        null,
        "pointer"
      ]
    ],
    [
      "00afc26c",
      "DATA",
      [
        "storage",
        "00c107f8",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc21c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc204.md#insn-00afc21c) · [`00afc230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc204.md#insn-00afc230) · [`00afc240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc204.md#insn-00afc240)
- 新版 [`00afc260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc248.md#insn-00afc260) · [`00afc274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc248.md#insn-00afc274) · [`00afc284`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc248.md#insn-00afc284)

~~~diff
- 00afc21c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:938:8"]]
- 00afc21c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00afc260 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:988:8"]]
+ 00afc260 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00afc21c bytes 089d44f9
+ 00afc260 bytes 08c544f9
- 00afc230 ["INT_ADD", "register:40f0:8", ["const:afc230:8", "const:4:8"]]
- 00afc230 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afc274 ["INT_ADD", "register:40f0:8", ["const:afc274:8", "const:4:8"]]
+ 00afc274 ["CALL", null, ["callee:00bddc20:8"]]
- 00afc230 bytes 68860394
+ 00afc274 bytes 6b860394
- 00afc240 ["INT_ADD", "register:40f0:8", ["const:afc240:8", "const:4:8"]]
- 00afc240 ["CALL", null, ["callee:00bddc30:8"]]
+ 00afc284 ["INT_ADD", "register:40f0:8", ["const:afc284:8", "const:4:8"]]
+ 00afc284 ["CALL", null, ["callee:00bddc30:8"]]
- 00afc240 bytes 68860394
+ 00afc284 bytes 6b860394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2da4207a88fefde9208abd7a11c0b93"></a>

### [`00afc280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc280.md) → [`00afc2c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc2c4.md) _ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEED0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00bdb000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb000.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00bdb050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb050.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

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
      "definition_site": "00afc2e4",
      "incomplete_value": true,
      "site": "00afc2e8",
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
      "definition_site": "00afc2a0",
      "incomplete_value": true,
      "site": "00afc2a4",
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
      "00afc2dc",
      "READ",
      [
        "storage",
        "00c1b938",
        null,
        "pointer"
      ]
    ],
    [
      "00afc2e8",
      "DATA",
      [
        "storage",
        "00c107a8",
        null,
        "undefined1[56]"
      ]
    ]
  ],
  "added": [
    [
      "00afc2dc",
      "READ",
      [
        "storage",
        "00c1b988",
        null,
        "pointer"
      ]
    ],
    [
      "00afc2e8",
      "DATA",
      [
        "storage",
        "00c107f8",
        null,
        "undefined1[56]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc280.md#insn-00afc298) · [`00afc2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc280.md#insn-00afc2ac) · [`00afc2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc280.md#insn-00afc2bc)
- 新版 [`00afc2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc2c4.md#insn-00afc2dc) · [`00afc2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc2c4.md#insn-00afc2f0) · [`00afc300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc2c4.md#insn-00afc300)

~~~diff
- 00afc298 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:938:8"]]
- 00afc298 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00afc2dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:988:8"]]
+ 00afc2dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00afc298 bytes 089d44f9
+ 00afc2dc bytes 08c544f9
- 00afc2ac ["INT_ADD", "register:40f0:8", ["const:afc2ac:8", "const:4:8"]]
- 00afc2ac ["CALL", null, ["callee:00bddc20:8"]]
+ 00afc2f0 ["INT_ADD", "register:40f0:8", ["const:afc2f0:8", "const:4:8"]]
+ 00afc2f0 ["CALL", null, ["callee:00bddc20:8"]]
- 00afc2ac bytes 49860394
+ 00afc2f0 bytes 4c860394
- 00afc2bc ["INT_ADD", "register:40f0:8", ["const:afc2bc:8", "const:4:8"]]
- 00afc2bc ["CALL", null, ["callee:00bddc30:8"]]
+ 00afc300 ["INT_ADD", "register:40f0:8", ["const:afc300:8", "const:4:8"]]
+ 00afc300 ["CALL", null, ["callee:00bddc30:8"]]
- 00afc2bc bytes 49860394
+ 00afc300 bytes 4c860394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef783ac0fbffc6fc7bebcb8cdef7ff3f"></a>

### [`00afc374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc374.md) → [`00afc3b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc3b8.md) _ZN8firebase8callback16BlockingCallbackD2Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdec70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec70.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdecc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdecc0.md)

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
      "definition_site": "00afc3d4",
      "incomplete_value": true,
      "site": "00afc3d8",
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
      "definition_site": "00afc390",
      "incomplete_value": true,
      "site": "00afc394",
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
      "00afc3cc",
      "READ",
      [
        "storage",
        "00c1b930",
        null,
        "pointer"
      ]
    ],
    [
      "00afc3d8",
      "DATA",
      [
        "storage",
        "00c107f8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00afc3cc",
      "READ",
      [
        "storage",
        "00c1b980",
        null,
        "pointer"
      ]
    ],
    [
      "00afc3d8",
      "DATA",
      [
        "storage",
        "00c10848",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc374.md#insn-00afc388) · [`00afc39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc374.md#insn-00afc39c)
- 新版 [`00afc3cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc3b8.md#insn-00afc3cc) · [`00afc3e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc3b8.md#insn-00afc3e0)

~~~diff
- 00afc388 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:930:8"]]
- 00afc388 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00afc3cc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:980:8"]]
+ 00afc3cc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00afc388 bytes 299944f9
+ 00afc3cc bytes 29c144f9
- 00afc39c ["INT_ADD", "register:40f0:8", ["const:afc39c:8", "const:4:8"]]
- 00afc39c ["CALL", null, ["callee:00bdecc0:8"]]
+ 00afc3e0 ["INT_ADD", "register:40f0:8", ["const:afc3e0:8", "const:4:8"]]
+ 00afc3e0 ["CALL", null, ["callee:00bdecc0:8"]]
- 00afc39c bytes 358a0394
+ 00afc3e0 bytes 388a0394
~~~


<a id="compare-62931945d79c25057f545b3ef03b7293"></a>

### [`00afc3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc3c8.md) → [`00afc40c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc40c.md) _ZN8firebase8callback16BlockingCallbackD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdec70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdec70.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdecc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdecc0.md)

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
      "definition_site": "00afc428",
      "incomplete_value": true,
      "site": "00afc42c",
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
      "definition_site": "00afc3e4",
      "incomplete_value": true,
      "site": "00afc3e8",
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
      "00afc420",
      "READ",
      [
        "storage",
        "00c1b930",
        null,
        "pointer"
      ]
    ],
    [
      "00afc42c",
      "DATA",
      [
        "storage",
        "00c107f8",
        null,
        "undefined1[40]"
      ]
    ]
  ],
  "added": [
    [
      "00afc420",
      "READ",
      [
        "storage",
        "00c1b980",
        null,
        "pointer"
      ]
    ],
    [
      "00afc42c",
      "DATA",
      [
        "storage",
        "00c10848",
        null,
        "undefined1[40]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc3c8.md#insn-00afc3dc) · [`00afc3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc3c8.md#insn-00afc3f0) · [`00afc404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc3c8.md#insn-00afc404)
- 新版 [`00afc420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc40c.md#insn-00afc420) · [`00afc434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc40c.md#insn-00afc434) · [`00afc448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc40c.md#insn-00afc448)

~~~diff
- 00afc3dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:930:8"]]
- 00afc3dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00afc420 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:980:8"]]
+ 00afc420 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00afc3dc bytes 299944f9
+ 00afc420 bytes 29c144f9
- 00afc3f0 ["INT_ADD", "register:40f0:8", ["const:afc3f0:8", "const:4:8"]]
- 00afc3f0 ["CALL", null, ["callee:00bdecc0:8"]]
+ 00afc434 ["INT_ADD", "register:40f0:8", ["const:afc434:8", "const:4:8"]]
+ 00afc434 ["CALL", null, ["callee:00bdecc0:8"]]
- 00afc3f0 bytes 208a0394
+ 00afc434 bytes 238a0394
- 00afc404 ["COPY", "register:0:8", ["register:4040:8"]]
- 00afc404 ["INT_ADD", "register:40f0:8", ["const:afc404:8", "const:4:8"]]
- 00afc404 ["CALLIND", null, ["register:0:8"]]
+ 00afc448 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00afc448 ["INT_ADD", "register:40f0:8", ["const:afc448:8", "const:4:8"]]
+ 00afc448 ["CALLIND", null, ["register:0:8"]]
- 00afc404 bytes 00013fd6
+ 00afc448 bytes 00013fd6
~~~


<a id="compare-8929087539bd823286431bbcb69b1a5a"></a>

### [`00afc4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc4f0.md) → [`00afc534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc534.md) _INIT_272

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 86.67% / 新版 86.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00afc560",
      "incomplete_value": false,
      "site": "00afc560",
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
            "const:d20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afc51c",
      "incomplete_value": false,
      "site": "00afc51c",
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
            "const:ce0:8"
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
      "definition_site": "00afc564",
      "incomplete_value": false,
      "site": "00afc564",
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
            "const:d40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afc520",
      "incomplete_value": false,
      "site": "00afc520",
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
            "const:d00:8"
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
      "00afc560",
      "WRITE",
      [
        "storage",
        "010a0ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00afc564",
      "WRITE",
      [
        "storage",
        "010a0d00",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00afc560",
      "WRITE",
      [
        "storage",
        "010a0d20",
        null,
        "undefined8"
      ]
    ],
    [
      "00afc564",
      "WRITE",
      [
        "storage",
        "010a0d40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afc51c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc4f0.md#insn-00afc51c) · [`00afc520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc4f0.md#insn-00afc520) · [`00afc500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afc4f0.md#insn-00afc500)
- 新版 [`00afc560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc534.md#insn-00afc560) · [`00afc564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc534.md#insn-00afc564) · [`00afc544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afc534.md#insn-00afc544)

~~~diff
- 00afc51c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce0:8"]]
- 00afc51c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
+ 00afc560 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d20:8"]]
+ 00afc560 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4098:8"]]
- 00afc51c bytes 137106f9
+ 00afc560 bytes 139106f9
- 00afc520 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d00:8"]]
- 00afc520 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00afc520 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00afc564 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d40:8"]]
+ 00afc564 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00afc564 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00afc520 bytes 3f8106f9
+ 00afc564 bytes 3fa106f9
- 00afc500 ["INT_ADD", "register:40f0:8", ["const:afc500:8", "const:4:8"]]
- 00afc500 ["CALL", null, ["callee:00bdb040:8"]]
+ 00afc544 ["INT_ADD", "register:40f0:8", ["const:afc544:8", "const:4:8"]]
+ 00afc544 ["CALL", null, ["callee:00bdb040:8"]]
- 00afc500 bytes bc7a0394
+ 00afc544 bytes bf7a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd0e67f54852dd7c6263b2519ec7dbfc"></a>

### [`00afcd70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afcd70.md) → [`00afcdb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcdb4.md) _ZN8firebase15CleanupNotifier11FindByOwnerEPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bddd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd40.md) · 呼出先 2件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00bddd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd90.md) · 呼出先 2件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.67% / 新版 91.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00afcde4",
      "incomplete_value": true,
      "site": "00afcde4",
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
              "LOAD"
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
      "definition_site": "00afcda0",
      "incomplete_value": true,
      "site": "00afcda0",
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
              "LOAD"
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
      "definition_site": "00afcdd0",
      "incomplete_value": true,
      "site": "00afcdd4",
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
      "definition_site": "00afcd8c",
      "incomplete_value": true,
      "site": "00afcd90",
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
      "00afcdc4",
      "READ",
      [
        "storage",
        "00c1b948",
        null,
        "pointer"
      ]
    ],
    [
      "00afcdcc",
      "READ",
      [
        "storage",
        "010a0d08",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00afcddc",
      "READ",
      [
        "storage",
        "00c1b940",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00afcdc4",
      "READ",
      [
        "storage",
        "00c1b998",
        null,
        "pointer"
      ]
    ],
    [
      "00afcdcc",
      "READ",
      [
        "storage",
        "010a0d48",
        "_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00afcddc",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afcd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afcd70.md#insn-00afcd90) · [`00afcde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afcd70.md#insn-00afcde4) · [`00afcd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afcd70.md#insn-00afcd80)
- 新版 [`00afcdd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcdb4.md#insn-00afcdd4) · [`00afce28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcdb4.md#insn-00afce28) · [`00afcdc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afc/00afcdb4.md#insn-00afcdc4)

~~~diff
- 00afcd90 ["INT_ADD", "register:40f0:8", ["const:afcd90:8", "const:4:8"]]
- 00afcd90 ["CALL", null, ["callee:00bddc20:8"]]
+ 00afcdd4 ["INT_ADD", "register:40f0:8", ["const:afcdd4:8", "const:4:8"]]
+ 00afcdd4 ["CALL", null, ["callee:00bddc20:8"]]
- 00afcd90 bytes 90830394
+ 00afcdd4 bytes 93830394
- 00afcde4 ["INT_ADD", "register:40f0:8", ["const:afcde4:8", "const:4:8"]]
- 00afcde4 ["CALL", null, ["callee:00bddc30:8"]]
+ 00afce28 ["INT_ADD", "register:40f0:8", ["const:afce28:8", "const:4:8"]]
+ 00afce28 ["CALL", null, ["callee:00bddc30:8"]]
- 00afcde4 bytes 7f830394
+ 00afce28 bytes 82830394
- 00afcd80 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:948:8"]]
- 00afcd80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00afcdc4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:998:8"]]
+ 00afcdc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00afcd80 bytes 08a544f9
+ 00afcdc4 bytes 08cd44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6abf83cdd9e31cbb998be4fb910d4df8"></a>

### [`00afd268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md) → [`00afd2ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md) FUN_00afd2ac

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00afd0c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd0c4.md) [`00afd1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd1f8.md) [`00afdc04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afdc04.md) [`00afddb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afddb4.md) · 呼出先 3件 [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb750.md) [`00bded30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded30.md)
- 新版 呼出元 4件 [`00afd108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd108.md) [`00afd23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd23c.md) [`00afdc48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afdc48.md) [`00afddf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afddf8.md) · 呼出先 3件 [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7a0.md) [`00bded80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.33% / 新版 98.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afd2f0",
      "incomplete_value": false,
      "site": "00afd2fc",
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
      "definition_site": "00afd2ac",
      "incomplete_value": false,
      "site": "00afd2b8",
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
      "00afd2f0",
      "PARAM",
      [
        "storage",
        "002958ca",
        null,
        null
      ]
    ],
    [
      "00afd444",
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
      "00afd2f0",
      "PARAM",
      [
        "storage",
        "0029583d",
        null,
        null
      ]
    ],
    [
      "00afd444",
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

- 旧版 [`00afd2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md#insn-00afd2b8) · [`00afd2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md#insn-00afd2ac) · [`00afd3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd268.md#insn-00afd3b8)
- 新版 [`00afd2fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md#insn-00afd2fc) · [`00afd2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md#insn-00afd2f0) · [`00afd3fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd2ac.md#insn-00afd3fc)

~~~diff
- 00afd2b8 ["INT_ADD", "register:40f0:8", ["const:afd2b8:8", "const:4:8"]]
- 00afd2b8 ["CALL", null, ["callee:00bded80:8"]]
+ 00afd2fc ["INT_ADD", "register:40f0:8", ["const:afd2fc:8", "const:4:8"]]
+ 00afd2fc ["CALL", null, ["callee:00bded80:8"]]
- 00afd2b8 bytes 9e860394
+ 00afd2fc bytes a1860394
- 00afd2ac ["COPY", "tmp:0:8", ["const:8ca:8"]]
- 00afd2ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00afd2ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00afd2ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00afd2f0 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 00afd2f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00afd2f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00afd2f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00afd2ac bytes 00282391
+ 00afd2f0 bytes 00f42091
- 00afd3b8 ["INT_ADD", "register:40f0:8", ["const:afd3b8:8", "const:4:8"]]
- 00afd3b8 ["CALL", null, ["callee:00bdb7a0:8"]]
+ 00afd3fc ["INT_ADD", "register:40f0:8", ["const:afd3fc:8", "const:4:8"]]
+ 00afd3fc ["CALL", null, ["callee:00bdb7a0:8"]]
- 00afd3b8 bytes e6780394
+ 00afd3fc bytes e9780394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a96d8b72ad6758c0bcba701b623c5f4a"></a>

### [`00afd448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd448.md) → [`00afd48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd48c.md) _ZNK8firebase4Path8GetChildERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdece0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdece0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bded30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded30.md)

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
      "definition_site": "00afd4b4",
      "incomplete_value": false,
      "site": "00afd4c0",
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
      "definition_site": "00afd470",
      "incomplete_value": false,
      "site": "00afd47c",
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
      "00afd4b4",
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
      "00afd4b4",
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

- 旧版 [`00afd47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd448.md#insn-00afd47c) · [`00afd4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd448.md#insn-00afd4c0) · [`00afd470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd448.md#insn-00afd470)
- 新版 [`00afd4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd48c.md#insn-00afd4c0) · [`00afd504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd48c.md#insn-00afd504) · [`00afd4b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd48c.md#insn-00afd4b4)

~~~diff
- 00afd47c ["INT_ADD", "register:40f0:8", ["const:afd47c:8", "const:4:8"]]
- 00afd47c ["CALL", null, ["callee:00afaa08:8"]]
+ 00afd4c0 ["INT_ADD", "register:40f0:8", ["const:afd4c0:8", "const:4:8"]]
+ 00afd4c0 ["CALL", null, ["callee:00afaa08:8"]]
- 00afd47c bytes 52f5ff97
+ 00afd4c0 bytes 52f5ff97
- 00afd4c0 ["INT_ADD", "register:40f0:8", ["const:afd4c0:8", "const:4:8"]]
- 00afd4c0 ["CALL", null, ["callee:00bded30:8"]]
+ 00afd504 ["INT_ADD", "register:40f0:8", ["const:afd504:8", "const:4:8"]]
+ 00afd504 ["CALL", null, ["callee:00bded30:8"]]
- 00afd4c0 bytes 08860394
+ 00afd504 bytes 0b860394
- 00afd470 ["COPY", "tmp:0:8", ["const:8ca:8"]]
- 00afd470 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00afd470 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00afd470 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00afd4b4 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 00afd4b4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00afd4b4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00afd4b4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00afd470 bytes 21282391
+ 00afd4b4 bytes 21f42091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ff9cba7d927360ecd5f2e8b14c174b0"></a>

### [`00afd50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd50c.md) → [`00afd550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd550.md) _ZNK8firebase4Path8GetChildERKS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdece0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdece0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bded30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded30.md)

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
      "definition_site": "00afd578",
      "incomplete_value": false,
      "site": "00afd584",
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
      "definition_site": "00afd534",
      "incomplete_value": false,
      "site": "00afd540",
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
      "00afd578",
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
      "00afd578",
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

- 旧版 [`00afd540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd50c.md#insn-00afd540) · [`00afd584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd50c.md#insn-00afd584) · [`00afd534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afd/00afd50c.md#insn-00afd534)
- 新版 [`00afd584`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd550.md#insn-00afd584) · [`00afd5c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd550.md#insn-00afd5c8) · [`00afd578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afd550.md#insn-00afd578)

~~~diff
- 00afd540 ["INT_ADD", "register:40f0:8", ["const:afd540:8", "const:4:8"]]
- 00afd540 ["CALL", null, ["callee:00afaa08:8"]]
+ 00afd584 ["INT_ADD", "register:40f0:8", ["const:afd584:8", "const:4:8"]]
+ 00afd584 ["CALL", null, ["callee:00afaa08:8"]]
- 00afd540 bytes 21f5ff97
+ 00afd584 bytes 21f5ff97
- 00afd584 ["INT_ADD", "register:40f0:8", ["const:afd584:8", "const:4:8"]]
- 00afd584 ["CALL", null, ["callee:00bded30:8"]]
+ 00afd5c8 ["INT_ADD", "register:40f0:8", ["const:afd5c8:8", "const:4:8"]]
+ 00afd5c8 ["CALL", null, ["callee:00bded30:8"]]
- 00afd584 bytes d7850394
+ 00afd5c8 bytes da850394
- 00afd534 ["COPY", "tmp:0:8", ["const:8ca:8"]]
- 00afd534 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00afd534 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00afd534 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00afd578 ["COPY", "tmp:0:8", ["const:83d:8"]]
+ 00afd578 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00afd578 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00afd578 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00afd534 bytes 21282391
+ 00afd578 bytes 21f42091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cded9c459810b0c4a282b075cfc6267"></a>

### [`00afe760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe760.md) → [`00afe7a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe7a4.md) _ZN8firebase17FutureBackingDataD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bded80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded80.md) · 呼出先 10件 [`00b00cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00cbc.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md)
- 新版 呼出元 1件 [`00bdedd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdedd0.md) · 呼出先 10件 [`00b00d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d00.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.76% / 新版 98.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00afe7d8",
      "incomplete_value": false,
      "site": "00afe7dc",
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
            "const:349:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afe794",
      "incomplete_value": false,
      "site": "00afe798",
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
            "const:3dd:8"
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
      "definition_site": "00afe800",
      "incomplete_value": false,
      "site": "00afe804",
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
            "const:eb5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00afe7bc",
      "incomplete_value": false,
      "site": "00afe7c0",
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
            "const:e2a:8"
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
      "00afe7d8",
      "PARAM",
      [
        "storage",
        "002af3dd",
        null,
        "string"
      ]
    ],
    [
      "00afe800",
      "PARAM",
      [
        "storage",
        "002a1e2a",
        null,
        "string"
      ]
    ],
    [
      "00afe838",
      "READ",
      [
        "storage",
        "00c1b958",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00afe7d8",
      "PARAM",
      [
        "storage",
        "002af349",
        null,
        "string"
      ]
    ],
    [
      "00afe800",
      "PARAM",
      [
        "storage",
        "002a1eb5",
        null,
        "string"
      ]
    ],
    [
      "00afe838",
      "READ",
      [
        "storage",
        "00c1b9a8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afe77c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe760.md#insn-00afe77c) · [`00afe798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe760.md#insn-00afe798) · [`00afe7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afe760.md#insn-00afe7c0)
- 新版 [`00afe7c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe7a4.md#insn-00afe7c0) · [`00afe7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe7a4.md#insn-00afe7dc) · [`00afe804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afe7a4.md#insn-00afe804)

~~~diff
- 00afe77c ["INT_ADD", "register:40f0:8", ["const:afe77c:8", "const:4:8"]]
- 00afe77c ["CALL", null, ["callee:00bdedc0:8"]]
+ 00afe7c0 ["INT_ADD", "register:40f0:8", ["const:afe7c0:8", "const:4:8"]]
+ 00afe7c0 ["CALL", null, ["callee:00bdedc0:8"]]
- 00afe77c bytes 7d810394
+ 00afe7c0 bytes 80810394
- 00afe798 ["INT_ADD", "register:40f0:8", ["const:afe798:8", "const:4:8"]]
- 00afe798 ["CALL", null, ["callee:00bde180:8"]]
+ 00afe7dc ["INT_ADD", "register:40f0:8", ["const:afe7dc:8", "const:4:8"]]
+ 00afe7dc ["CALL", null, ["callee:00bde180:8"]]
- 00afe798 bytes 667e0394
+ 00afe7dc bytes 697e0394
- 00afe7c0 ["INT_ADD", "register:40f0:8", ["const:afe7c0:8", "const:4:8"]]
- 00afe7c0 ["CALL", null, ["callee:00bde180:8"]]
+ 00afe804 ["INT_ADD", "register:40f0:8", ["const:afe804:8", "const:4:8"]]
+ 00afe804 ["CALL", null, ["callee:00bde180:8"]]
- 00afe7c0 bytes 5c7e0394
+ 00afe804 bytes 5f7e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-699429eaa48bb1e343105928db6fc3cb"></a>

### [`00afeae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afeae0.md) → [`00afeb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afeb24.md) _ZN8firebase26ReferenceCountedFutureImplD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md) [`00bdedd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedd0.md) · 呼出先 11件 [`00b0129c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0129c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc00.md)
- 新版 呼出元 2件 [`00bdddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md) [`00bdee20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee20.md) · 呼出先 11件 [`00b012e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b012e0.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc50.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00afeb50",
      "incomplete_value": true,
      "site": "00afeb54",
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
      "definition_site": "00afeb0c",
      "incomplete_value": true,
      "site": "00afeb10",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00afeb44",
      "READ",
      [
        "storage",
        "00c1b860",
        null,
        "pointer"
      ]
    ],
    [
      "00afeb54",
      "DATA",
      [
        "storage",
        "00c10850",
        null,
        "undefined1[120]"
      ]
    ]
  ],
  "added": [
    [
      "00afeb44",
      "READ",
      [
        "storage",
        "00c1b8b0",
        null,
        "pointer"
      ]
    ],
    [
      "00afeb54",
      "DATA",
      [
        "storage",
        "00c108a0",
        null,
        "undefined1[120]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00afeb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afeae0.md#insn-00afeb00) · [`00afeb28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afeae0.md#insn-00afeb28) · [`00afeb4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afe/00afeae0.md#insn-00afeb4c)
- 新版 [`00afeb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afeb24.md#insn-00afeb44) · [`00afeb6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afeb24.md#insn-00afeb6c) · [`00afeb90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afe/00afeb24.md#insn-00afeb90)

~~~diff
- 00afeb00 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:860:8"]]
- 00afeb00 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00afeb44 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:8b0:8"]]
+ 00afeb44 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00afeb00 bytes 4a3144f9
+ 00afeb44 bytes 4a5944f9
- 00afeb28 ["INT_ADD", "register:40f0:8", ["const:afeb28:8", "const:4:8"]]
- 00afeb28 ["CALL", null, ["callee:00bddc30:8"]]
+ 00afeb6c ["INT_ADD", "register:40f0:8", ["const:afeb6c:8", "const:4:8"]]
+ 00afeb6c ["CALL", null, ["callee:00bddc30:8"]]
- 00afeb28 bytes 2e7c0394
+ 00afeb6c bytes 317c0394
- 00afeb4c ["INT_ADD", "register:40f0:8", ["const:afeb4c:8", "const:4:8"]]
- 00afeb4c ["CALL", null, ["callee:00bddc20:8"]]
+ 00afeb90 ["INT_ADD", "register:40f0:8", ["const:afeb90:8", "const:4:8"]]
+ 00afeb90 ["CALL", null, ["callee:00bddc20:8"]]
- 00afeb4c bytes 217c0394
+ 00afeb90 bytes 247c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fec49b7bce2cd72c3ad8c6a2b4d0699a"></a>

### [`00b00578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00578.md) → [`00b005bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b005bc.md) _ZN8firebase26ReferenceCountedFutureImpl14SetContextDataERKNS_12FutureHandleEPvPFvS4_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bded90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded90.md) · 呼出先 3件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bdede0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdede0.md) · 呼出先 3件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.92% / 新版 97.92%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0066c",
      "incomplete_value": false,
      "site": "00b00670",
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
            "const:e32:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b00628",
      "incomplete_value": false,
      "site": "00b0062c",
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
            "const:d98:8"
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
      "00b0066c",
      "PARAM",
      [
        "storage",
        "002a7d98",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0066c",
      "PARAM",
      [
        "storage",
        "002a7e32",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0062c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00578.md#insn-00b0062c) · [`00b005a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00578.md#insn-00b005a4) · [`00b005b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00578.md#insn-00b005b0)
- 新版 [`00b00670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b005bc.md#insn-00b00670) · [`00b005e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b005bc.md#insn-00b005e8) · [`00b005f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b005bc.md#insn-00b005f4)

~~~diff
- 00b0062c ["INT_ADD", "register:40f0:8", ["const:b0062c:8", "const:4:8"]]
- 00b0062c ["CALL", null, ["callee:00bde180:8"]]
+ 00b00670 ["INT_ADD", "register:40f0:8", ["const:b00670:8", "const:4:8"]]
+ 00b00670 ["CALL", null, ["callee:00bde180:8"]]
- 00b0062c bytes c1760394
+ 00b00670 bytes c4760394
- 00b005a4 ["INT_ADD", "register:40f0:8", ["const:b005a4:8", "const:4:8"]]
- 00b005a4 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b005e8 ["INT_ADD", "register:40f0:8", ["const:b005e8:8", "const:4:8"]]
+ 00b005e8 ["CALL", null, ["callee:00bddc20:8"]]
- 00b005a4 bytes 8b750394
+ 00b005e8 bytes 8e750394
- 00b005b0 ["INT_ADD", "register:40f0:8", ["const:b005b0:8", "const:4:8"]]
- 00b005b0 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b005f4 ["INT_ADD", "register:40f0:8", ["const:b005f4:8", "const:4:8"]]
+ 00b005f4 ["CALL", null, ["callee:00bddc20:8"]]
- 00b005b0 bytes 88750394
+ 00b005f4 bytes 8b750394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f653691f46865a2178f08d0fa9d6234"></a>

### [`00b00e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e00.md) → [`00b00e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00e44.md) _ZN8firebase12FutureHandleC1EOS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bded50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded50.md) · 呼出先 3件 [`00b00cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00cbc.md) [`00bddd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd50.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)
- 新版 呼出元 1件 [`00bdeda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeda0.md) · 呼出先 3件 [`00b00d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d00.md) [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.83% / 新版 95.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b00e7c",
      "incomplete_value": false,
      "site": "00b00e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b00000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b00e38",
      "incomplete_value": false,
      "site": "00b00e3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b00000:8"
          ],
          [
            "leaf",
            "const:cbc:8"
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
      "00b00e7c",
      "PARAM",
      [
        "storage",
        "00b00cbc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b00e7c",
      "PARAM",
      [
        "storage",
        "00b00d00",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e00.md#insn-00b00e3c) · [`00b00e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e00.md#insn-00b00e38) · [`00b00e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e00.md#insn-00b00e4c)
- 新版 [`00b00e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00e44.md#insn-00b00e80) · [`00b00e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00e44.md#insn-00b00e7c) · [`00b00e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00e44.md#insn-00b00e90)

~~~diff
- 00b00e3c ["INT_ADD", "register:40f0:8", ["const:b00e3c:8", "const:4:8"]]
- 00b00e3c ["CALL", null, ["callee:00bddda0:8"]]
+ 00b00e80 ["INT_ADD", "register:40f0:8", ["const:b00e80:8", "const:4:8"]]
+ 00b00e80 ["CALL", null, ["callee:00bddda0:8"]]
- 00b00e3c bytes c5730394
+ 00b00e80 bytes c8730394
- 00b00e38 ["COPY", "tmp:0:8", ["const:cbc:8"]]
- 00b00e38 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b00e38 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b00e38 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b00e7c ["COPY", "tmp:0:8", ["const:d00:8"]]
+ 00b00e7c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b00e7c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b00e7c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b00e38 bytes 42f03291
+ 00b00e7c bytes 42003491
- 00b00e4c ["INT_ADD", "register:40f0:8", ["const:b00e4c:8", "const:4:8"]]
- 00b00e4c ["CALL", null, ["callee:00bdddb0:8"]]
+ 00b00e90 ["INT_ADD", "register:40f0:8", ["const:b00e90:8", "const:4:8"]]
+ 00b00e90 ["CALL", null, ["callee:00bdddb0:8"]]
- 00b00e4c bytes c5730394
+ 00b00e90 bytes c8730394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-489956c921fc5d23a3e5b6644f0b11ae"></a>

### [`00b00e60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e60.md) → [`00b00ea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00ea4.md) _ZN8firebase12FutureHandleaSEOS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bded60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded60.md) · 呼出先 3件 [`00b00cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00cbc.md) [`00bddd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd50.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)
- 新版 呼出元 1件 [`00bdedb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdedb0.md) · 呼出先 3件 [`00b00d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d00.md) [`00bddda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddda0.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.30% / 新版 97.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b00f08",
      "incomplete_value": false,
      "site": "00b00f10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b00000:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b00ec4",
      "incomplete_value": false,
      "site": "00b00ecc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b00000:8"
          ],
          [
            "leaf",
            "const:cbc:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b00f08",
      "PARAM",
      [
        "storage",
        "00b00cbc",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b00f08",
      "PARAM",
      [
        "storage",
        "00b00d00",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b00ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e60.md#insn-00b00ecc) · [`00b00e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e60.md#insn-00b00e84) · [`00b00e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00e60.md#insn-00b00e98)
- 新版 [`00b00f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00ea4.md#insn-00b00f10) · [`00b00ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00ea4.md#insn-00b00ec8) · [`00b00edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00ea4.md#insn-00b00edc)

~~~diff
- 00b00ecc ["INT_ADD", "register:40f0:8", ["const:b00ecc:8", "const:4:8"]]
- 00b00ecc ["CALL", null, ["callee:00bddda0:8"]]
+ 00b00f10 ["INT_ADD", "register:40f0:8", ["const:b00f10:8", "const:4:8"]]
+ 00b00f10 ["CALL", null, ["callee:00bddda0:8"]]
- 00b00ecc bytes a1730394
+ 00b00f10 bytes a4730394
- 00b00e84 ["INT_ADD", "register:40f0:8", ["const:b00e84:8", "const:4:8"]]
- 00b00e84 ["CALL", null, ["callee:00bdddb0:8"]]
+ 00b00ec8 ["INT_ADD", "register:40f0:8", ["const:b00ec8:8", "const:4:8"]]
+ 00b00ec8 ["CALL", null, ["callee:00bdddb0:8"]]
- 00b00e84 bytes b7730394
+ 00b00ec8 bytes ba730394
- 00b00e98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b00e98 ["INT_ADD", "register:40f0:8", ["const:b00e98:8", "const:4:8"]]
- 00b00e98 ["CALLIND", null, ["register:0:8"]]
+ 00b00edc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b00edc ["INT_ADD", "register:40f0:8", ["const:b00edc:8", "const:4:8"]]
+ 00b00edc ["CALLIND", null, ["register:0:8"]]
- 00b00e98 bytes 00013fd6
+ 00b00edc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd1cf14ce51cd6b283130b7c280e62b6"></a>

### [`00b00f3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00f3c.md) → [`00b00f80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00f80.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdedb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdedb0.md) · 呼出先 8件 [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00bdee00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee00.md) · 呼出先 8件 [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.70% / 新版 96.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b01048",
      "incomplete_value": false,
      "site": "00b0104c",
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
            "const:467:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b01004",
      "incomplete_value": false,
      "site": "00b01008",
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
            "const:4f4:8"
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
      "00b01048",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ],
    [
      "00b01060",
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
      "00b01048",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ],
    [
      "00b01060",
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

- 旧版 [`00b01008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00f3c.md#insn-00b01008) · [`00b0104c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00f3c.md#insn-00b0104c) · [`00b00f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00f3c.md#insn-00b00f68)
- 新版 [`00b0104c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00f80.md#insn-00b0104c) · [`00b01090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00f80.md#insn-00b01090) · [`00b00fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00f80.md#insn-00b00fac)

~~~diff
- 00b01008 ["INT_ADD", "register:40f0:8", ["const:b01008:8", "const:4:8"]]
- 00b01008 ["CALL", null, ["callee:00bde180:8"]]
+ 00b0104c ["INT_ADD", "register:40f0:8", ["const:b0104c:8", "const:4:8"]]
+ 00b0104c ["CALL", null, ["callee:00bde180:8"]]
- 00b01008 bytes 4a740394
+ 00b0104c bytes 4d740394
- 00b0104c ["INT_ADD", "register:40f0:8", ["const:b0104c:8", "const:4:8"]]
- 00b0104c ["CALL", null, ["callee:00bddfd0:8"]]
+ 00b01090 ["INT_ADD", "register:40f0:8", ["const:b01090:8", "const:4:8"]]
+ 00b01090 ["CALL", null, ["callee:00bddfd0:8"]]
- 00b0104c bytes cd730394
+ 00b01090 bytes d0730394
- 00b00f68 ["INT_ADD", "register:40f0:8", ["const:b00f68:8", "const:4:8"]]
- 00b00f68 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b00fac ["INT_ADD", "register:40f0:8", ["const:b00fac:8", "const:4:8"]]
+ 00b00fac ["CALL", null, ["callee:00bddc20:8"]]
- 00b00f68 bytes 1a730394
+ 00b00fac bytes 1d730394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4aab4d58e2bc1ecc552a42cbd44670ec"></a>

### [`00b0132c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0132c.md) → [`00b01370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01370.md) _INIT_274

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00b00cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b00/00b00cc4.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00b00d08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b00/00b00d08.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 62.50% / 新版 62.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b01388",
      "incomplete_value": true,
      "site": "00b01388",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b01344",
      "incomplete_value": true,
      "site": "00b01344",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:958:8"
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b01388",
      "incomplete_value": true,
      "site": "00b01388",
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
      "definition_site": "00b01344",
      "incomplete_value": true,
      "site": "00b01344",
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
      "00b01378",
      "READ",
      [
        "storage",
        "00c1b958",
        null,
        "pointer"
      ]
    ],
    [
      "00b01378",
      "PARAM",
      [
        "storage",
        "010a0d18",
        "_ZN8firebase26ReferenceCountedFutureImpl14kInvalidHandleE",
        "undefined8"
      ]
    ],
    [
      "00b0137c",
      "READ",
      [
        "storage",
        "00c1b950",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b01378",
      "READ",
      [
        "storage",
        "00c1b9a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b01378",
      "PARAM",
      [
        "storage",
        "010a0d58",
        "_ZN8firebase26ReferenceCountedFutureImpl14kInvalidHandleE",
        "undefined8"
      ]
    ],
    [
      "00b0137c",
      "READ",
      [
        "storage",
        "00c1b9a0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b01334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0132c.md#insn-00b01334) · [`00b01338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0132c.md#insn-00b01338) · [`00b01340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0132c.md#insn-00b01340)
- 新版 [`00b01378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01370.md#insn-00b01378) · [`00b0137c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01370.md#insn-00b0137c) · [`00b01384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01370.md#insn-00b01384)

~~~diff
- 00b01334 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:958:8"]]
- 00b01334 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b01378 ["INT_ADD", "tmp:0:8", ["register:4008:8", "const:9a8:8"]]
+ 00b01378 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b01334 bytes 21ac44f9
+ 00b01378 bytes 21d444f9
- 00b01338 ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:950:8"]]
- 00b01338 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b0137c ["INT_ADD", "tmp:0:8", ["register:4000:8", "const:9a0:8"]]
+ 00b0137c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b01338 bytes 00a844f9
+ 00b0137c bytes 00d044f9
- 00b01340 ["COPY", "register:4010:8", ["const:be5f80:8"]]
+ 00b01384 ["COPY", "register:4010:8", ["const:be5fd0:8"]]
- 00b01340 bytes 02627210
+ 00b01384 bytes 62627210
~~~


<a id="compare-c3920f56fa519f31d2899a4297f4a685"></a>

### [`00b013b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b013b0.md) → [`00b013f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b013f4.md) _ZN8firebase17ModuleInitializerD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bdddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md)

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
      "definition_site": "00b01410",
      "incomplete_value": true,
      "site": "00b01414",
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
      "definition_site": "00b013cc",
      "incomplete_value": true,
      "site": "00b013d0",
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
      "00b01408",
      "READ",
      [
        "storage",
        "00c1b988",
        null,
        "pointer"
      ]
    ],
    [
      "00b01414",
      "DATA",
      [
        "storage",
        "00c10968",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b01408",
      "READ",
      [
        "storage",
        "00c1b9d8",
        null,
        "pointer"
      ]
    ],
    [
      "00b01414",
      "DATA",
      [
        "storage",
        "00c109b8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b013c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b013b0.md#insn-00b013c4) · [`00b013e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b013b0.md#insn-00b013e4) · [`00b013ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b013b0.md#insn-00b013ec)
- 新版 [`00b01408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b013f4.md#insn-00b01408) · [`00b01428`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b013f4.md#insn-00b01428) · [`00b01430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b013f4.md#insn-00b01430)

~~~diff
- 00b013c4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:988:8"]]
- 00b013c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b01408 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d8:8"]]
+ 00b01408 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b013c4 bytes 08c544f9
+ 00b01408 bytes 08ed44f9
- 00b013e4 ["INT_ADD", "register:40f0:8", ["const:b013e4:8", "const:4:8"]]
- 00b013e4 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b01428 ["INT_ADD", "register:40f0:8", ["const:b01428:8", "const:4:8"]]
+ 00b01428 ["CALL", null, ["callee:00bdb060:8"]]
- 00b013e4 bytes 0b670394
+ 00b01428 bytes 0e670394
- 00b013ec ["INT_ADD", "register:40f0:8", ["const:b013ec:8", "const:4:8"]]
- 00b013ec ["CALL", null, ["callee:00bddc40:8"]]
+ 00b01430 ["INT_ADD", "register:40f0:8", ["const:b01430:8", "const:4:8"]]
+ 00b01430 ["CALL", null, ["callee:00bddc40:8"]]
- 00b013ec bytes 01720394
+ 00b01430 bytes 04720394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc919d0cc5507178c183e6805514f68c"></a>

### [`00b01410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01410.md) → [`00b01454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01454.md) _ZN8firebase17ModuleInitializerD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bdddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md)

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
      "definition_site": "00b01470",
      "incomplete_value": true,
      "site": "00b01474",
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
      "definition_site": "00b0142c",
      "incomplete_value": true,
      "site": "00b01430",
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
      "00b01468",
      "READ",
      [
        "storage",
        "00c1b988",
        null,
        "pointer"
      ]
    ],
    [
      "00b01474",
      "DATA",
      [
        "storage",
        "00c10968",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b01468",
      "READ",
      [
        "storage",
        "00c1b9d8",
        null,
        "pointer"
      ]
    ],
    [
      "00b01474",
      "DATA",
      [
        "storage",
        "00c109b8",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b01424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01410.md#insn-00b01424) · [`00b01444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01410.md#insn-00b01444) · [`00b0144c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01410.md#insn-00b0144c)
- 新版 [`00b01468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01454.md#insn-00b01468) · [`00b01488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01454.md#insn-00b01488) · [`00b01490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01454.md#insn-00b01490)

~~~diff
- 00b01424 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:988:8"]]
- 00b01424 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b01468 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9d8:8"]]
+ 00b01468 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b01424 bytes 08c544f9
+ 00b01468 bytes 08ed44f9
- 00b01444 ["INT_ADD", "register:40f0:8", ["const:b01444:8", "const:4:8"]]
- 00b01444 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b01488 ["INT_ADD", "register:40f0:8", ["const:b01488:8", "const:4:8"]]
+ 00b01488 ["CALL", null, ["callee:00bdb060:8"]]
- 00b01444 bytes f3660394
+ 00b01488 bytes f6660394
- 00b0144c ["INT_ADD", "register:40f0:8", ["const:b0144c:8", "const:4:8"]]
- 00b0144c ["CALL", null, ["callee:00bddc40:8"]]
+ 00b01490 ["INT_ADD", "register:40f0:8", ["const:b01490:8", "const:4:8"]]
+ 00b01490 ["CALL", null, ["callee:00bddc40:8"]]
- 00b0144c bytes e9710394
+ 00b01490 bytes ec710394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42cc2533b061bbfe4a238eb570bec1e9"></a>

### [`00b01470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01470.md) → [`00b014b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b014b4.md) _ZN8firebase17ModuleInitializer10InitializeEPNS_3AppEPvPFNS_10InitResultES2_S3_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bdee50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee50.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bdeea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeea0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.67% / 新版 97.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b01540",
      "incomplete_value": false,
      "site": "00b01544",
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
      "definition_site": "00b014fc",
      "incomplete_value": false,
      "site": "00b01500",
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
      "00b01540",
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
      "00b01540",
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

- 旧版 [`00b01500`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01470.md#insn-00b01500) · [`00b014cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01470.md#insn-00b014cc) · [`00b014fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01470.md#insn-00b014fc)
- 新版 [`00b01544`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b014b4.md#insn-00b01544) · [`00b01510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b014b4.md#insn-00b01510) · [`00b01540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b014b4.md#insn-00b01540)

~~~diff
- 00b01500 ["INT_ADD", "register:40f0:8", ["const:b01500:8", "const:4:8"]]
- 00b01500 ["CALL", null, ["callee:00bde180:8"]]
+ 00b01544 ["INT_ADD", "register:40f0:8", ["const:b01544:8", "const:4:8"]]
+ 00b01544 ["CALL", null, ["callee:00bde180:8"]]
- 00b01500 bytes 0c730394
+ 00b01544 bytes 0f730394
- 00b014cc ["INT_ADD", "register:40f0:8", ["const:b014cc:8", "const:4:8"]]
- 00b014cc ["CALL", null, ["callee:00bdeea0:8"]]
+ 00b01510 ["INT_ADD", "register:40f0:8", ["const:b01510:8", "const:4:8"]]
+ 00b01510 ["CALL", null, ["callee:00bdeea0:8"]]
- 00b014cc bytes 61760394
+ 00b01510 bytes 64760394
- 00b014fc ["COPY", "tmp:0:8", ["const:e4c:8"]]
- 00b014fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b014fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b014fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b01540 ["COPY", "tmp:0:8", ["const:ed7:8"]]
+ 00b01540 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b01540 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b01540 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b014fc bytes 00303991
+ 00b01540 bytes 005c3b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f2167678bcfc4e793ab90c203a6b133"></a>

### [`00b0151c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0151c.md) → [`00b01560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01560.md) _ZN8firebase17ModuleInitializer10InitializeEPNS_3AppEPvPKPFNS_10InitResultES2_S3_Em

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdee50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee50.md) · 呼出先 14件 [`00b016d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md)
- 新版 呼出元 1件 [`00bdeea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeea0.md) · 呼出先 14件 [`00b01714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01714.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.08% / 新版 99.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b01680",
      "incomplete_value": false,
      "site": "00b01684",
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
      "definition_site": "00b0163c",
      "incomplete_value": false,
      "site": "00b01640",
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
      "00b01680",
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
      "00b01680",
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

- 旧版 [`00b01640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0151c.md#insn-00b01640) · [`00b01684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0151c.md#insn-00b01684) · [`00b01570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0151c.md#insn-00b01570)
- 新版 [`00b01684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01560.md#insn-00b01684) · [`00b016c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01560.md#insn-00b016c8) · [`00b015b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01560.md#insn-00b015b4)

~~~diff
- 00b01640 ["INT_ADD", "register:40f0:8", ["const:b01640:8", "const:4:8"]]
- 00b01640 ["CALL", null, ["callee:00bde180:8"]]
+ 00b01684 ["INT_ADD", "register:40f0:8", ["const:b01684:8", "const:4:8"]]
+ 00b01684 ["CALL", null, ["callee:00bde180:8"]]
- 00b01640 bytes bc720394
+ 00b01684 bytes bf720394
- 00b01684 ["INT_ADD", "register:40f0:8", ["const:b01684:8", "const:4:8"]]
- 00b01684 ["CALL", null, ["callee:00bdde10:8"]]
+ 00b016c8 ["INT_ADD", "register:40f0:8", ["const:b016c8:8", "const:4:8"]]
+ 00b016c8 ["CALL", null, ["callee:00bdde10:8"]]
- 00b01684 bytes cf710394
+ 00b016c8 bytes d2710394
- 00b01570 ["INT_ADD", "register:40f0:8", ["const:b01570:8", "const:4:8"]]
- 00b01570 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b015b4 ["INT_ADD", "register:40f0:8", ["const:b015b4:8", "const:4:8"]]
+ 00b015b4 ["CALL", null, ["callee:00bddf80:8"]]
- 00b01570 bytes 70720394
+ 00b015b4 bytes 73720394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46c930adb7156164286c145d4f2931aa"></a>

### [`00b016d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md) → [`00b01714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01714.md) FUN_00b01714

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b0151c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b0151c.md) [`00b02854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02854.md) · 呼出先 12件 [`00b02854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02854.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md)
- 新版 呼出元 2件 [`00b01560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01560.md) [`00b02898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02898.md) · 呼出先 12件 [`00b02898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02898.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.48% / 新版 97.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b017ec",
      "incomplete_value": false,
      "site": "00b017f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:e40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b017a8",
      "incomplete_value": false,
      "site": "00b017ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:db5:8"
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
      "definition_site": "00b0182c",
      "incomplete_value": false,
      "site": "00b01844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b02000:8"
          ],
          [
            "leaf",
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b017e8",
      "incomplete_value": false,
      "site": "00b01800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b02000:8"
          ],
          [
            "leaf",
            "const:854:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b018cc",
      "incomplete_value": false,
      "site": "00b018e0",
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
            "const:cb8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b01888",
      "incomplete_value": false,
      "site": "00b0189c",
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
            "const:c1e:8"
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b017ec",
      "PARAM",
      [
        "storage",
        "0029ddb5",
        null,
        "string"
      ]
    ],
    [
      "00b0182c",
      "PARAM",
      [
        "storage",
        "00b02854",
        null,
        null
      ]
    ],
    [
      "00b018cc",
      "PARAM",
      [
        "storage",
        "002a8c1e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b017ec",
      "PARAM",
      [
        "storage",
        "0029de40",
        null,
        "string"
      ]
    ],
    [
      "00b0182c",
      "PARAM",
      [
        "storage",
        "00b02898",
        null,
        null
      ]
    ],
    [
      "00b018cc",
      "PARAM",
      [
        "storage",
        "002a8cb8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b017ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md#insn-00b017ac) · [`00b01800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md#insn-00b01800) · [`00b0189c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md#insn-00b0189c)
- 新版 [`00b017f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01714.md#insn-00b017f0) · [`00b01844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01714.md#insn-00b01844) · [`00b018e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01714.md#insn-00b018e0)

~~~diff
- 00b017ac ["INT_ADD", "register:40f0:8", ["const:b017ac:8", "const:4:8"]]
- 00b017ac ["CALL", null, ["callee:00bddf60:8"]]
+ 00b017f0 ["INT_ADD", "register:40f0:8", ["const:b017f0:8", "const:4:8"]]
+ 00b017f0 ["CALL", null, ["callee:00bddf60:8"]]
- 00b017ac bytes d9710394
+ 00b017f0 bytes dc710394
- 00b01800 ["COPY", "register:0:8", ["register:4048:8"]]
- 00b01800 ["INT_ADD", "register:40f0:8", ["const:b01800:8", "const:4:8"]]
- 00b01800 ["CALLIND", null, ["register:0:8"]]
+ 00b01844 ["COPY", "register:0:8", ["register:4048:8"]]
+ 00b01844 ["INT_ADD", "register:40f0:8", ["const:b01844:8", "const:4:8"]]
+ 00b01844 ["CALLIND", null, ["register:0:8"]]
- 00b01800 bytes 20013fd6
+ 00b01844 bytes 20013fd6
- 00b0189c ["INT_ADD", "register:40f0:8", ["const:b0189c:8", "const:4:8"]]
- 00b0189c ["CALL", null, ["callee:00bdee00:8"]]
+ 00b018e0 ["INT_ADD", "register:40f0:8", ["const:b018e0:8", "const:4:8"]]
+ 00b018e0 ["CALL", null, ["callee:00bdee00:8"]]
- 00b0189c bytes 45750394
+ 00b018e0 bytes 48750394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af702c4b8200dc2187507420578d4d52"></a>

### [`00b01d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01d00.md) → [`00b01d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01d44.md) _ZN8firebase11AppCallback16SetEnabledByNameEPKcb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 10件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 0件  · 呼出先 10件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 94.79% / 新版 94.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b01d98",
      "incomplete_value": true,
      "site": "00b01d98",
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
              "LOAD"
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
      "definition_site": "00b01d54",
      "incomplete_value": true,
      "site": "00b01d54",
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
              "LOAD"
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
      "definition_site": "00b01d84",
      "incomplete_value": true,
      "site": "00b01d88",
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
      "definition_site": "00b01d40",
      "incomplete_value": true,
      "site": "00b01d44",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b01e58",
      "incomplete_value": true,
      "site": "00b01e64",
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
            "const:f16:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b01e14",
      "incomplete_value": true,
      "site": "00b01e20",
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
            "const:e8b:8"
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
      "00b01d7c",
      "READ",
      [
        "storage",
        "00c1b970",
        null,
        "pointer"
      ]
    ],
    [
      "00b01d80",
      "READ",
      [
        "storage",
        "010a0d30",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b01d90",
      "READ",
      [
        "storage",
        "00c1b968",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b01d7c",
      "READ",
      [
        "storage",
        "00c1b9c0",
        null,
        "pointer"
      ]
    ],
    [
      "00b01d80",
      "READ",
      [
        "storage",
        "010a0d70",
        "_ZN8firebase11AppCallback16callbacks_mutex_E",
        "undefined8"
      ]
    ],
    [
      "00b01d90",
      "READ",
      [
        "storage",
        "00c1b9b8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b01d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01d00.md#insn-00b01d44) · [`00b01da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01d00.md#insn-00b01da0) · [`00b01e20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01d00.md#insn-00b01e20)
- 新版 [`00b01d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01d44.md#insn-00b01d88) · [`00b01de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01d44.md#insn-00b01de4) · [`00b01e64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01d44.md#insn-00b01e64)

~~~diff
- 00b01d44 ["INT_ADD", "register:40f0:8", ["const:b01d44:8", "const:4:8"]]
- 00b01d44 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b01d88 ["INT_ADD", "register:40f0:8", ["const:b01d88:8", "const:4:8"]]
+ 00b01d88 ["CALL", null, ["callee:00bddc20:8"]]
- 00b01d44 bytes a36f0394
+ 00b01d88 bytes a66f0394
- 00b01da0 ["INT_ADD", "register:40f0:8", ["const:b01da0:8", "const:4:8"]]
- 00b01da0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b01de4 ["INT_ADD", "register:40f0:8", ["const:b01de4:8", "const:4:8"]]
+ 00b01de4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b01da0 bytes 94640394
+ 00b01de4 bytes 97640394
- 00b01e20 ["INT_ADD", "register:40f0:8", ["const:b01e20:8", "const:4:8"]]
- 00b01e20 ["CALL", null, ["callee:00bde2b0:8"]]
+ 00b01e64 ["INT_ADD", "register:40f0:8", ["const:b01e64:8", "const:4:8"]]
+ 00b01e64 ["CALL", null, ["callee:00bde2b0:8"]]
- 00b01e20 bytes 10710394
+ 00b01e64 bytes 13710394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f74050aa42219527f045314d0152da0e"></a>

### [`00b01fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01fa8.md) → [`00b01fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01fec.md) _ZN8firebase11AppCallback11AddCallbackEPS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bddd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd10.md) · 呼出先 11件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bddd60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd60.md) · 呼出先 11件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 96.82% / 新版 96.82%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b02028",
      "incomplete_value": true,
      "site": "00b02028",
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
              "LOAD"
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
      "definition_site": "00b01fe4",
      "incomplete_value": true,
      "site": "00b01fe4",
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
              "LOAD"
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
      "definition_site": "00b020f8",
      "incomplete_value": false,
      "site": "00b020fc",
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
            "const:dc5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b020b4",
      "incomplete_value": false,
      "site": "00b020b8",
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
            "const:d3a:8"
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
      "definition_site": "00b02148",
      "incomplete_value": false,
      "site": "00b0214c",
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
            "const:e0e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b02104",
      "incomplete_value": false,
      "site": "00b02108",
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
            "const:d83:8"
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
      "00b02020",
      "READ",
      [
        "storage",
        "00c1b968",
        null,
        "pointer"
      ]
    ],
    [
      "00b02024",
      "READ",
      [
        "storage",
        "010a0d28",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ],
    [
      "00b02048",
      "WRITE",
      [
        "storage",
        "010a0d28",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b02020",
      "READ",
      [
        "storage",
        "00c1b9b8",
        null,
        "pointer"
      ]
    ],
    [
      "00b02024",
      "READ",
      [
        "storage",
        "010a0d68",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ],
    [
      "00b02048",
      "WRITE",
      [
        "storage",
        "010a0d68",
        "_ZN8firebase11AppCallback10callbacks_E",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01fa8.md#insn-00b02074) · [`00b020b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01fa8.md#insn-00b020b8) · [`00b02108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b01fa8.md#insn-00b02108)
- 新版 [`00b020b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01fec.md#insn-00b020b8) · [`00b020fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01fec.md#insn-00b020fc) · [`00b0214c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01fec.md#insn-00b0214c)

~~~diff
- 00b02074 ["INT_ADD", "register:40f0:8", ["const:b02074:8", "const:4:8"]]
- 00b02074 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b020b8 ["INT_ADD", "register:40f0:8", ["const:b020b8:8", "const:4:8"]]
+ 00b020b8 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b02074 bytes 3b640394
+ 00b020b8 bytes 3e640394
- 00b020b8 ["INT_ADD", "register:40f0:8", ["const:b020b8:8", "const:4:8"]]
- 00b020b8 ["CALL", null, ["callee:00bddf60:8"]]
+ 00b020fc ["INT_ADD", "register:40f0:8", ["const:b020fc:8", "const:4:8"]]
+ 00b020fc ["CALL", null, ["callee:00bddf60:8"]]
- 00b020b8 bytes 966f0394
+ 00b020fc bytes 996f0394
- 00b02108 ["INT_ADD", "register:40f0:8", ["const:b02108:8", "const:4:8"]]
- 00b02108 ["CALL", null, ["callee:00bde2b0:8"]]
+ 00b0214c ["INT_ADD", "register:40f0:8", ["const:b0214c:8", "const:4:8"]]
+ 00b0214c ["CALL", null, ["callee:00bde2b0:8"]]
- 00b02108 bytes 56700394
+ 00b0214c bytes 59700394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b0758c418c7fc48e8a1dc9dbaed9cea"></a>

### [`00b02710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02710.md) → [`00b02754`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02754.md) _ZN8firebase19CreateApiIdentifierEPKcPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdee60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee60.md) · 呼出先 2件 [`00b027b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b027b0.md) [`00bdb750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb750.md)
- 新版 呼出元 1件 [`00bdeeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeeb0.md) · 呼出先 2件 [`00b027f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b027f4.md) [`00bdb7a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb7a0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 97.50% / 新版 97.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b027a0",
      "incomplete_value": false,
      "site": "00b027a0",
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
            "const:d88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0275c",
      "incomplete_value": false,
      "site": "00b0275c",
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
            "const:d48:8"
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
      "00b02770",
      "READ",
      [
        "storage",
        "010a0d48",
        null,
        "undefined4"
      ]
    ],
    [
      "00b027a0",
      "WRITE",
      [
        "storage",
        "010a0d48",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b02770",
      "READ",
      [
        "storage",
        "010a0d88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b027a0",
      "WRITE",
      [
        "storage",
        "010a0d88",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0275c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02710.md#insn-00b0275c) · [`00b0272c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02710.md#insn-00b0272c) · [`00b02760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02710.md#insn-00b02760)
- 新版 [`00b027a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02754.md#insn-00b027a0) · [`00b02770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02754.md#insn-00b02770) · [`00b027a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02754.md#insn-00b027a4)

~~~diff
- 00b0275c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d48:8"]]
- 00b0275c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b027a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d88:8"]]
+ 00b027a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b0275c bytes 09490db9
+ 00b027a0 bytes 09890db9
- 00b0272c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d48:8"]]
- 00b0272c ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
- 00b0272c ["INT_ZEXT", "register:40b0:8", ["tmp:1:4"]]
+ 00b02770 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:d88:8"]]
+ 00b02770 ["LOAD", "tmp:1:4", ["const:1b1:8", "tmp:0:8"]]
+ 00b02770 ["INT_ZEXT", "register:40b0:8", ["tmp:1:4"]]
- 00b0272c bytes 16494db9
+ 00b02770 bytes 16894db9
- 00b02760 ["INT_ADD", "register:40f0:8", ["const:b02760:8", "const:4:8"]]
- 00b02760 ["CALL", null, ["callee:00b027f4:8"]]
+ 00b027a4 ["INT_ADD", "register:40f0:8", ["const:b027a4:8", "const:4:8"]]
+ 00b027a4 ["CALL", null, ["callee:00b027f4:8"]]
- 00b02760 bytes 14000094
+ 00b027a4 bytes 14000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-986b99b94c7cecf41f5b741270552cf2"></a>

### [`00b02854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02854.md) → [`00b02898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02898.md) FUN_00b02898

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b016d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md) · 呼出先 12件 [`00b016d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b01/00b016d0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md)
- 新版 呼出元 1件 [`00b01714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01714.md) · 呼出先 12件 [`00b01714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b01/00b01714.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.53% / 新版 97.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b02928",
      "incomplete_value": false,
      "site": "00b0292c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:e71:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b028e4",
      "incomplete_value": false,
      "site": "00b028e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:de6:8"
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
      "definition_site": "00b0295c",
      "incomplete_value": false,
      "site": "00b02960",
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
            "const:f2c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b02918",
      "incomplete_value": false,
      "site": "00b0291c",
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
            "const:ea1:8"
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
      "00b02928",
      "PARAM",
      [
        "storage",
        "0029dde6",
        null,
        "string"
      ]
    ],
    [
      "00b0295c",
      "PARAM",
      [
        "storage",
        "0029eea1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b02928",
      "PARAM",
      [
        "storage",
        "0029de71",
        null,
        "string"
      ]
    ],
    [
      "00b0295c",
      "PARAM",
      [
        "storage",
        "0029ef2c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b028d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02854.md#insn-00b028d8) · [`00b028e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02854.md#insn-00b028e8) · [`00b0291c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02854.md#insn-00b0291c)
- 新版 [`00b0291c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02898.md#insn-00b0291c) · [`00b0292c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02898.md#insn-00b0292c) · [`00b02960`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02898.md#insn-00b02960)

~~~diff
- 00b028d8 ["INT_ADD", "register:40f0:8", ["const:b028d8:8", "const:4:8"]]
- 00b028d8 ["CALL", null, ["callee:00bddc30:8"]]
+ 00b0291c ["INT_ADD", "register:40f0:8", ["const:b0291c:8", "const:4:8"]]
+ 00b0291c ["CALL", null, ["callee:00bddc30:8"]]
- 00b028d8 bytes c26c0394
+ 00b0291c bytes c56c0394
- 00b028e8 ["INT_ADD", "register:40f0:8", ["const:b028e8:8", "const:4:8"]]
- 00b028e8 ["CALL", null, ["callee:00bde160:8"]]
+ 00b0292c ["INT_ADD", "register:40f0:8", ["const:b0292c:8", "const:4:8"]]
+ 00b0292c ["CALL", null, ["callee:00bde160:8"]]
- 00b028e8 bytes 0a6e0394
+ 00b0292c bytes 0d6e0394
- 00b0291c ["INT_ADD", "register:40f0:8", ["const:b0291c:8", "const:4:8"]]
- 00b0291c ["CALL", null, ["callee:00bdde40:8"]]
+ 00b02960 ["INT_ADD", "register:40f0:8", ["const:b02960:8", "const:4:8"]]
+ 00b02960 ["CALL", null, ["callee:00bdde40:8"]]
- 00b0291c bytes 356d0394
+ 00b02960 bytes 386d0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a7240a18254acbd7aa98184d71b33f0"></a>

### [`00b02e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02e7c.md) → [`00b02ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ec0.md) _ZN8firebase7VariantaSERKS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdda50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdda50.md) · 呼出先 11件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bddaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaa0.md) · 呼出先 11件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 86.60% / 新版 86.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 17件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b02f34",
      "incomplete_value": true,
      "site": "00b02f38",
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
            "const:ea1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b02ef0",
      "incomplete_value": true,
      "site": "00b02ef4",
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
            "const:e16:8"
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
      "definition_site": "00b02f50",
      "incomplete_value": true,
      "site": "00b02f5c",
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
            "const:f54:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b02f0c",
      "incomplete_value": true,
      "site": "00b02f18",
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
            "const:ec9:8"
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
      "definition_site": "00b02fac",
      "incomplete_value": false,
      "site": "00b02fb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:ea1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b02f68",
      "incomplete_value": false,
      "site": "00b02f6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:e16:8"
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
      "00b02f18",
      "DATA",
      [
        "storage",
        "002f6059",
        "switchD_00b02edc::switchdataD_002f6059",
        "byte"
      ]
    ],
    [
      "00b02f34",
      "PARAM",
      [
        "storage",
        "0029de16",
        null,
        "string"
      ]
    ],
    [
      "00b02f44",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b02f18",
      "DATA",
      [
        "storage",
        "002f6059",
        "switchD_00b02f20::switchdataD_002f6059",
        "byte"
      ]
    ],
    [
      "00b02f34",
      "PARAM",
      [
        "storage",
        "0029dea1",
        null,
        "string"
      ]
    ],
    [
      "00b02f44",
      "READ",
      [
        "storage",
        "00c1b9e0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b02ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02e7c.md#insn-00b02ef4) · [`00b02f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02e7c.md#insn-00b02f18) · [`00b02f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b02/00b02e7c.md#insn-00b02f6c)
- 新版 [`00b02f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ec0.md#insn-00b02f38) · [`00b02f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ec0.md#insn-00b02f5c) · [`00b02fb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b02/00b02ec0.md#insn-00b02fb0)

~~~diff
- 00b02ef4 ["INT_ADD", "register:40f0:8", ["const:b02ef4:8", "const:4:8"]]
- 00b02ef4 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b02f38 ["INT_ADD", "register:40f0:8", ["const:b02f38:8", "const:4:8"]]
+ 00b02f38 ["CALL", null, ["callee:00bdde40:8"]]
- 00b02ef4 bytes bf6b0394
+ 00b02f38 bytes c26b0394
- 00b02f18 ["INT_ADD", "register:40f0:8", ["const:b02f18:8", "const:4:8"]]
- 00b02f18 ["CALL", null, ["callee:00bde180:8"]]
+ 00b02f5c ["INT_ADD", "register:40f0:8", ["const:b02f5c:8", "const:4:8"]]
+ 00b02f5c ["CALL", null, ["callee:00bde180:8"]]
- 00b02f18 bytes 866c0394
+ 00b02f5c bytes 896c0394
- 00b02f6c ["INT_ADD", "register:40f0:8", ["const:b02f6c:8", "const:4:8"]]
- 00b02f6c ["CALL", null, ["callee:00bdde40:8"]]
+ 00b02fb0 ["INT_ADD", "register:40f0:8", ["const:b02fb0:8", "const:4:8"]]
+ 00b02fb0 ["CALL", null, ["callee:00bdde40:8"]]
- 00b02f6c bytes a16b0394
+ 00b02fb0 bytes a46b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a57cdf3f35c706312d0a0d973e40aad2"></a>

### [`00b031c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b031c0.md) → [`00b03204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03204.md) _ZN8firebase7Variant5ClearENS0_4TypeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 2件 [`00b031c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b031c0.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) · 呼出先 6件 [`00b031c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b031c0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bdef20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef20.md)
- 新版 呼出元 2件 [`00b03204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03204.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) · 呼出先 6件 [`00b03204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03204.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bdef70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef70.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.86% / 新版 98.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b03460",
      "incomplete_value": false,
      "site": "00b03464",
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
      "definition_site": "00b0341c",
      "incomplete_value": false,
      "site": "00b03420",
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
      "00b0323c",
      "DATA",
      [
        "storage",
        "002f6064",
        "switchD_00b03200::switchdataD_002f6064",
        "byte"
      ]
    ],
    [
      "00b033fc",
      "DATA",
      [
        "storage",
        "002f606f",
        "switchD_00b033c0::switchdataD_002f606f",
        "byte"
      ]
    ],
    [
      "00b03464",
      "DATA",
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
      "00b0323c",
      "DATA",
      [
        "storage",
        "002f6064",
        "switchD_00b03244::switchdataD_002f6064",
        "byte"
      ]
    ],
    [
      "00b033fc",
      "DATA",
      [
        "storage",
        "002f606f",
        "switchD_00b03404::switchdataD_002f606f",
        "byte"
      ]
    ],
    [
      "00b03464",
      "DATA",
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

- 旧版 [`00b031f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b031c0.md#insn-00b031f4) · [`00b0327c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b031c0.md#insn-00b0327c) · [`00b032ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b031c0.md#insn-00b032ac)
- 新版 [`00b03238`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03204.md#insn-00b03238) · [`00b032c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03204.md#insn-00b032c0) · [`00b032f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03204.md#insn-00b032f0)

~~~diff
- 00b031f4 ["COPY", "register:4050:8", ["const:b03204:8"]]
+ 00b03238 ["COPY", "register:4050:8", ["const:b03248:8"]]
- 00b031f4 bytes 8a000010
+ 00b03238 bytes 8a000010
- 00b0327c ["INT_ADD", "register:40f0:8", ["const:b0327c:8", "const:4:8"]]
- 00b0327c ["CALL", null, ["local:b0:8"]]
+ 00b032c0 ["INT_ADD", "register:40f0:8", ["const:b032c0:8", "const:4:8"]]
+ 00b032c0 ["CALL", null, ["local:b0:8"]]
- 00b0327c bytes d1ffff97
+ 00b032c0 bytes d1ffff97
- 00b032ac ["INT_ADD", "register:40f0:8", ["const:b032ac:8", "const:4:8"]]
- 00b032ac ["CALL", null, ["callee:00bdef70:8"]]
+ 00b032f0 ["INT_ADD", "register:40f0:8", ["const:b032f0:8", "const:4:8"]]
+ 00b032f0 ["CALL", null, ["callee:00bdef70:8"]]
- 00b032ac bytes 1d6f0394
+ 00b032f0 bytes 206f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b581c43430a7aa237656b4af4a649b2"></a>

### [`00b0357c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b0357c.md) → [`00b035c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b035c0.md) _ZN8firebase7Variant16set_mutable_blobEPKvm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdeed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeed0.md) · 呼出先 5件 [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bdef50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef50.md)
- 新版 呼出元 1件 [`00bdef20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef20.md) · 呼出先 5件 [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bdefa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefa0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.89% / 新版 91.89%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b03634",
      "incomplete_value": false,
      "site": "00b0363c",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b035f0",
      "incomplete_value": false,
      "site": "00b035f8",
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
            "const:5c5:8"
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
      "definition_site": "00b03638",
      "incomplete_value": true,
      "site": "00b0363c",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b035f4",
      "incomplete_value": true,
      "site": "00b035f8",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b0362c",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ],
    [
      "00b03634",
      "PARAM",
      [
        "storage",
        "002975c5",
        null,
        "string"
      ]
    ],
    [
      "00b03638",
      "DATA",
      [
        "storage",
        "00c10988",
        "_ZN8firebase7Variant10kTypeNamesE",
        "undefined1[96]"
      ]
    ]
  ],
  "added": [
    [
      "00b0362c",
      "READ",
      [
        "storage",
        "00c1b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b03634",
      "PARAM",
      [
        "storage",
        "00297538",
        null,
        "string"
      ]
    ],
    [
      "00b03638",
      "DATA",
      [
        "storage",
        "00c109d8",
        "_ZN8firebase7Variant10kTypeNamesE",
        "undefined1[96]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b035b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b0357c.md#insn-00b035b4) · [`00b035f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b0357c.md#insn-00b035f8) · [`00b0359c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b0357c.md#insn-00b0359c)
- 新版 [`00b035f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b035c0.md#insn-00b035f8) · [`00b0363c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b035c0.md#insn-00b0363c) · [`00b035e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b035c0.md#insn-00b035e0)

~~~diff
- 00b035b4 ["INT_ADD", "register:40f0:8", ["const:b035b4:8", "const:4:8"]]
- 00b035b4 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b035f8 ["INT_ADD", "register:40f0:8", ["const:b035f8:8", "const:4:8"]]
+ 00b035f8 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b035b4 bytes eb5e0394
+ 00b035f8 bytes ee5e0394
- 00b035f8 ["INT_ADD", "register:40f0:8", ["const:b035f8:8", "const:4:8"]]
- 00b035f8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b0363c ["INT_ADD", "register:40f0:8", ["const:b0363c:8", "const:4:8"]]
+ 00b0363c ["CALL", null, ["callee:00bde180:8"]]
- 00b035f8 bytes ce6a0394
+ 00b0363c bytes d16a0394
- 00b0359c ["INT_ADD", "register:40f0:8", ["const:b0359c:8", "const:4:8"]]
- 00b0359c ["CALL", null, ["callee:00bdefa0:8"]]
+ 00b035e0 ["INT_ADD", "register:40f0:8", ["const:b035e0:8", "const:4:8"]]
+ 00b035e0 ["CALL", null, ["callee:00bdefa0:8"]]
- 00b0359c bytes 6d6e0394
+ 00b035e0 bytes 706e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e872ed3b4df46214cc007d5d0192f7b"></a>

### [`00b03610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03610.md) → [`00b03654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03654.md) _ZN8firebase7VariantaSEOS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdd9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd9a0.md) · 呼出先 3件 [`00bdd990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd990.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bdd9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9f0.md) · 呼出先 3件 [`00bdd9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd9e0.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.71% / 新版 95.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b03718",
      "incomplete_value": false,
      "site": "00b03720",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b036d4",
      "incomplete_value": false,
      "site": "00b036dc",
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
            "const:5c5:8"
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
      "definition_site": "00b0371c",
      "incomplete_value": true,
      "site": "00b03720",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b036d8",
      "incomplete_value": true,
      "site": "00b036dc",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
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
      "00b036a8",
      "DATA",
      [
        "storage",
        "002f607a",
        "switchD_00b0366c::switchdataD_002f607a",
        "byte"
      ]
    ],
    [
      "00b03710",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ],
    [
      "00b03718",
      "PARAM",
      [
        "storage",
        "002975c5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b036a8",
      "DATA",
      [
        "storage",
        "002f607a",
        "switchD_00b036b0::switchdataD_002f607a",
        "byte"
      ]
    ],
    [
      "00b03710",
      "READ",
      [
        "storage",
        "00c1b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b03718",
      "PARAM",
      [
        "storage",
        "00297538",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b036dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03610.md#insn-00b036dc) · [`00b03638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03610.md#insn-00b03638) · [`00b03660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03610.md#insn-00b03660)
- 新版 [`00b03720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03654.md#insn-00b03720) · [`00b0367c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03654.md#insn-00b0367c) · [`00b036a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03654.md#insn-00b036a4)

~~~diff
- 00b036dc ["INT_ADD", "register:40f0:8", ["const:b036dc:8", "const:4:8"]]
- 00b036dc ["CALL", null, ["callee:00bde180:8"]]
+ 00b03720 ["INT_ADD", "register:40f0:8", ["const:b03720:8", "const:4:8"]]
+ 00b03720 ["CALL", null, ["callee:00bde180:8"]]
- 00b036dc bytes 956a0394
+ 00b03720 bytes 986a0394
- 00b03638 ["INT_ADD", "register:40f0:8", ["const:b03638:8", "const:4:8"]]
- 00b03638 ["CALL", null, ["callee:00bdd9e0:8"]]
+ 00b0367c ["INT_ADD", "register:40f0:8", ["const:b0367c:8", "const:4:8"]]
+ 00b0367c ["CALL", null, ["callee:00bdd9e0:8"]]
- 00b03638 bytes d6680394
+ 00b0367c bytes d9680394
- 00b03660 ["COPY", "register:4050:8", ["const:b03670:8"]]
+ 00b036a4 ["COPY", "register:4050:8", ["const:b036b4:8"]]
- 00b03660 bytes 8a000010
+ 00b036a4 bytes 8a000010
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2cba3463c4adae67b3aaff37562a4e0"></a>

### [`00b03728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03728.md) → [`00b0376c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b0376c.md) _ZNK8firebase7VarianteqERKS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00b03728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03728.md) [`00bdeef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeef0.md) · 呼出先 5件 [`00b03728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03728.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md)
- 新版 呼出元 2件 [`00b0376c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b0376c.md) [`00bdef40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef40.md) · 呼出先 5件 [`00b0376c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b0376c.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.88% / 新版 90.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b038b8",
      "incomplete_value": false,
      "site": "00b038c0",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b03874",
      "incomplete_value": false,
      "site": "00b0387c",
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
            "const:5c5:8"
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
      "definition_site": "00b03910",
      "incomplete_value": false,
      "site": "00b03914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:ea1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b038cc",
      "incomplete_value": false,
      "site": "00b038d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:e16:8"
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
      "definition_site": "00b0392c",
      "incomplete_value": false,
      "site": "00b03938",
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
            "const:f54:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b038e8",
      "incomplete_value": false,
      "site": "00b038f4",
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
            "const:ec9:8"
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
      "00b03804",
      "DATA",
      [
        "storage",
        "002f6085",
        "switchD_00b037cc::switchdataD_002f6085",
        "byte"
      ]
    ],
    [
      "00b03860",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ],
    [
      "00b03884",
      "PARAM",
      [
        "storage",
        "002975c5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b03804",
      "DATA",
      [
        "storage",
        "002f6085",
        "switchD_00b03810::switchdataD_002f6085",
        "byte"
      ]
    ],
    [
      "00b03860",
      "READ",
      [
        "storage",
        "00c1b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b03884",
      "PARAM",
      [
        "storage",
        "00297538",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0387c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03728.md#insn-00b0387c) · [`00b038d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03728.md#insn-00b038d0) · [`00b038f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03728.md#insn-00b038f4)
- 新版 [`00b038c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b0376c.md#insn-00b038c0) · [`00b03914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b0376c.md#insn-00b03914) · [`00b03938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b0376c.md#insn-00b03938)

~~~diff
- 00b0387c ["INT_ADD", "register:40f0:8", ["const:b0387c:8", "const:4:8"]]
- 00b0387c ["CALL", null, ["callee:00bde180:8"]]
+ 00b038c0 ["INT_ADD", "register:40f0:8", ["const:b038c0:8", "const:4:8"]]
+ 00b038c0 ["CALL", null, ["callee:00bde180:8"]]
- 00b0387c bytes 2d6a0394
+ 00b038c0 bytes 306a0394
- 00b038d0 ["INT_ADD", "register:40f0:8", ["const:b038d0:8", "const:4:8"]]
- 00b038d0 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b03914 ["INT_ADD", "register:40f0:8", ["const:b03914:8", "const:4:8"]]
+ 00b03914 ["CALL", null, ["callee:00bdde40:8"]]
- 00b038d0 bytes 48690394
+ 00b03914 bytes 4b690394
- 00b038f4 ["INT_ADD", "register:40f0:8", ["const:b038f4:8", "const:4:8"]]
- 00b038f4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b03938 ["INT_ADD", "register:40f0:8", ["const:b03938:8", "const:4:8"]]
+ 00b03938 ["CALL", null, ["callee:00bde180:8"]]
- 00b038f4 bytes 0f6a0394
+ 00b03938 bytes 126a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e48ddcce3a94b6bf81430386e7d49ad6"></a>

### [`00b03ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03ca4.md) → [`00b03ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03ce8.md) _ZNK8firebase7VariantltERKS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bde6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6d0.md) · 呼出先 5件 [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md) [`00bdeef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeef0.md)
- 新版 呼出元 1件 [`00bde720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde720.md) · 呼出先 5件 [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md) [`00bdef40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdef40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 30件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b03ee0",
      "incomplete_value": false,
      "site": "00b03ee8",
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
            "const:534:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b03e9c",
      "incomplete_value": false,
      "site": "00b03ea4",
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
            "const:5c1:8"
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
      "definition_site": "00b03f1c",
      "incomplete_value": false,
      "site": "00b03f24",
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
            "const:534:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b03ed8",
      "incomplete_value": false,
      "site": "00b03ee0",
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
            "const:5c1:8"
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
      "definition_site": "00b04034",
      "incomplete_value": false,
      "site": "00b04038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:ea1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b03ff0",
      "incomplete_value": false,
      "site": "00b03ff4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:e16:8"
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
      "00b03d0c",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ],
    [
      "00b03dbc",
      "DATA",
      [
        "storage",
        "002f6092",
        "switchD_00b03d80::switchdataD_002f6092",
        "ushort"
      ]
    ],
    [
      "00b03dd8",
      "PARAM",
      [
        "storage",
        "0029de16",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b03d0c",
      "READ",
      [
        "storage",
        "00c1b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b03dbc",
      "DATA",
      [
        "storage",
        "002f6092",
        "switchD_00b03dc4::switchdataD_002f6092",
        "ushort"
      ]
    ],
    [
      "00b03dd8",
      "PARAM",
      [
        "storage",
        "0029dea1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b03e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03ca4.md#insn-00b03e9c) · [`00b03ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03ca4.md#insn-00b03ea4) · [`00b03ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b03/00b03ca4.md#insn-00b03ee0)
- 新版 [`00b03ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03ce8.md#insn-00b03ee0) · [`00b03ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03ce8.md#insn-00b03ee8) · [`00b03f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b03/00b03ce8.md#insn-00b03f24)

~~~diff
- 00b03e9c ["COPY", "tmp:0:8", ["const:5c1:8"]]
- 00b03e9c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b03e9c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b03e9c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b03ee0 ["COPY", "tmp:0:8", ["const:534:8"]]
+ 00b03ee0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b03ee0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b03ee0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b03e9c bytes 21041791
+ 00b03ee0 bytes 21d01491
- 00b03ea4 ["INT_ADD", "register:40f0:8", ["const:b03ea4:8", "const:4:8"]]
- 00b03ea4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b03ee8 ["INT_ADD", "register:40f0:8", ["const:b03ee8:8", "const:4:8"]]
+ 00b03ee8 ["CALL", null, ["callee:00bde180:8"]]
- 00b03ea4 bytes a3680394
+ 00b03ee8 bytes a6680394
- 00b03ee0 ["INT_ADD", "register:40f0:8", ["const:b03ee0:8", "const:4:8"]]
- 00b03ee0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b03f24 ["INT_ADD", "register:40f0:8", ["const:b03f24:8", "const:4:8"]]
+ 00b03f24 ["CALL", null, ["callee:00bde180:8"]]
- 00b03ee0 bytes 94680394
+ 00b03f24 bytes 97680394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a3f744022da834a8f425632ae330955"></a>

### [`00b04510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04510.md) → [`00b04554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04554.md) _ZNK8firebase7Variant14assert_is_typeENS0_4TypeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bddc60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc60.md) · 呼出先 2件 [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bddcb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddcb0.md) · 呼出先 2件 [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b04580",
      "incomplete_value": false,
      "site": "00b04588",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:ea1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0453c",
      "incomplete_value": false,
      "site": "00b04544",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:e16:8"
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
      "00b04580",
      "PARAM",
      [
        "storage",
        "0029de16",
        null,
        "string"
      ]
    ],
    [
      "00b04594",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ],
    [
      "00b045a0",
      "PARAM",
      [
        "storage",
        "0029eec9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b04580",
      "PARAM",
      [
        "storage",
        "0029dea1",
        null,
        "string"
      ]
    ],
    [
      "00b04594",
      "READ",
      [
        "storage",
        "00c1b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b045a0",
      "PARAM",
      [
        "storage",
        "0029ef54",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b04544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04510.md#insn-00b04544) · [`00b0453c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04510.md#insn-00b0453c) · [`00b04550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04510.md#insn-00b04550)
- 新版 [`00b04588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04554.md#insn-00b04588) · [`00b04580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04554.md#insn-00b04580) · [`00b04594`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04554.md#insn-00b04594)

~~~diff
- 00b04544 ["INT_ADD", "register:40f0:8", ["const:b04544:8", "const:4:8"]]
- 00b04544 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b04588 ["INT_ADD", "register:40f0:8", ["const:b04588:8", "const:4:8"]]
+ 00b04588 ["CALL", null, ["callee:00bdde40:8"]]
- 00b04544 bytes 2b660394
+ 00b04588 bytes 2e660394
- 00b0453c ["COPY", "tmp:0:8", ["const:e16:8"]]
- 00b0453c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b0453c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b0453c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b04580 ["COPY", "tmp:0:8", ["const:ea1:8"]]
+ 00b04580 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b04580 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b04580 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b0453c bytes 00583891
+ 00b04580 bytes 00843a91
- 00b04550 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:990:8"]]
- 00b04550 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b04594 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:9e0:8"]]
+ 00b04594 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b04550 bytes 29c944f9
+ 00b04594 bytes 29f144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-362ef92230414be5b1ff93cadcb78fe8"></a>

### [`00b04570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04570.md) → [`00b045b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b045b4.md) _ZNK8firebase7Variant18assert_is_not_typeENS0_4TypeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 90.48% / 新版 90.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b045dc",
      "incomplete_value": false,
      "site": "00b045e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:ea1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04598",
      "incomplete_value": false,
      "site": "00b045a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:29d000:8"
          ],
          [
            "leaf",
            "const:e16:8"
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
      "00b045dc",
      "PARAM",
      [
        "storage",
        "0029de16",
        null,
        "string"
      ]
    ],
    [
      "00b045ec",
      "READ",
      [
        "storage",
        "00c1b990",
        null,
        "pointer"
      ]
    ],
    [
      "00b045f8",
      "PARAM",
      [
        "storage",
        "0029971b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b045dc",
      "PARAM",
      [
        "storage",
        "0029dea1",
        null,
        "string"
      ]
    ],
    [
      "00b045ec",
      "READ",
      [
        "storage",
        "00c1b9e0",
        null,
        "pointer"
      ]
    ],
    [
      "00b045f8",
      "PARAM",
      [
        "storage",
        "0029968e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b045a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04570.md#insn-00b045a0) · [`00b04598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04570.md#insn-00b04598) · [`00b045a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04570.md#insn-00b045a8)
- 新版 [`00b045e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b045b4.md#insn-00b045e4) · [`00b045dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b045b4.md#insn-00b045dc) · [`00b045ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b045b4.md#insn-00b045ec)

~~~diff
- 00b045a0 ["INT_ADD", "register:40f0:8", ["const:b045a0:8", "const:4:8"]]
- 00b045a0 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b045e4 ["INT_ADD", "register:40f0:8", ["const:b045e4:8", "const:4:8"]]
+ 00b045e4 ["CALL", null, ["callee:00bdde40:8"]]
- 00b045a0 bytes 14660394
+ 00b045e4 bytes 17660394
- 00b04598 ["COPY", "tmp:0:8", ["const:e16:8"]]
- 00b04598 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b04598 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b04598 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b045dc ["COPY", "tmp:0:8", ["const:ea1:8"]]
+ 00b045dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b045dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b045dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b04598 bytes 00583891
+ 00b045dc bytes 00843a91
- 00b045a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:990:8"]]
- 00b045a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b045ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9e0:8"]]
+ 00b045ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b045a8 bytes 08c944f9
+ 00b045ec bytes 08f144f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b29253acaccb6ab02c647ef994bfb7a4"></a>

### [`00b0468c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b0468c.md) → [`00b046d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b046d0.md) _ZNK8firebase7Variant8AsStringEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bddc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc70.md) · 呼出先 10件 [`00b04830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04830.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bddcc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddcc0.md) · 呼出先 10件 [`00b04874`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04874.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.19% / 新版 96.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b04760",
      "incomplete_value": false,
      "site": "00b04768",
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
            "const:e77:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0471c",
      "incomplete_value": false,
      "site": "00b04724",
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
            "const:dec:8"
          ]
        ]
      ]
    },
    "ordinal": 2,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b04794",
      "incomplete_value": false,
      "site": "00b0479c",
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
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04750",
      "incomplete_value": false,
      "site": "00b04758",
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
            "const:74d:8"
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
      "00b04714",
      "DATA",
      [
        "storage",
        "002f60a8",
        "switchD_00b046dc::switchdataD_002f60a8",
        "byte"
      ]
    ],
    [
      "00b04760",
      "PARAM",
      [
        "storage",
        "0029cdec",
        null,
        null
      ]
    ],
    [
      "00b04794",
      "PARAM",
      [
        "storage",
        "0029974d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b04714",
      "DATA",
      [
        "storage",
        "002f60a8",
        "switchD_00b04720::switchdataD_002f60a8",
        "byte"
      ]
    ],
    [
      "00b04760",
      "PARAM",
      [
        "storage",
        "0029ce77",
        null,
        null
      ]
    ],
    [
      "00b04794",
      "PARAM",
      [
        "storage",
        "002996c0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b04724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b0468c.md#insn-00b04724) · [`00b04758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b0468c.md#insn-00b04758) · [`00b04768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b0468c.md#insn-00b04768)
- 新版 [`00b04768`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b046d0.md#insn-00b04768) · [`00b0479c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b046d0.md#insn-00b0479c) · [`00b047ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b046d0.md#insn-00b047ac)

~~~diff
- 00b04724 ["INT_ADD", "register:40f0:8", ["const:b04724:8", "const:4:8"]]
- 00b04724 ["CALL", null, ["callee:00b04874:8"]]
+ 00b04768 ["INT_ADD", "register:40f0:8", ["const:b04768:8", "const:4:8"]]
+ 00b04768 ["CALL", null, ["callee:00b04874:8"]]
- 00b04724 bytes 43000094
+ 00b04768 bytes 43000094
- 00b04758 ["INT_ADD", "register:40f0:8", ["const:b04758:8", "const:4:8"]]
- 00b04758 ["CALL", null, ["callee:00b04874:8"]]
+ 00b0479c ["INT_ADD", "register:40f0:8", ["const:b0479c:8", "const:4:8"]]
+ 00b0479c ["CALL", null, ["callee:00b04874:8"]]
- 00b04758 bytes 36000094
+ 00b0479c bytes 36000094
- 00b04768 ["INT_ADD", "register:40f0:8", ["const:b04768:8", "const:4:8"]]
- 00b04768 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b047ac ["INT_ADD", "register:40f0:8", ["const:b047ac:8", "const:4:8"]]
+ 00b047ac ["CALL", null, ["callee:00bdb190:8"]]
- 00b04768 bytes 765a0394
+ 00b047ac bytes 795a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33798dbd2fb5b32a57bab97dd5009ecd"></a>

### [`00b04d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04d18.md) → [`00b04d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04d5c.md) _ZN8firebase7Variant8TypeNameENS0_4TypeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde120.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde170.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_destination

命令の説明率　旧版 84.00% / 新版 84.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `return_value_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b04d88",
      "incomplete_value": true,
      "site": "00b04d88",
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
            "const:d8c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04d44",
      "incomplete_value": true,
      "site": "00b04d44",
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
            "const:d4c:8"
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
      "definition_site": "00b04da0",
      "incomplete_value": false,
      "site": "00b04da4",
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
            "const:6c6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04d5c",
      "incomplete_value": false,
      "site": "00b04d60",
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
            "const:753:8"
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
      "definition_site": "00b04db4",
      "incomplete_value": true,
      "site": "00b04dbc",
      "value": [
        "LOAD",
        "8",
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
              "INT_LEFT"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b04d70",
      "incomplete_value": true,
      "site": "00b04d78",
      "value": [
        "LOAD",
        "8",
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
      "00b04d6c",
      "READ",
      [
        "storage",
        "010a0d4c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b04d88",
      "WRITE",
      [
        "storage",
        "010a0d4c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b04da0",
      "PARAM",
      [
        "storage",
        "00299753",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b04d6c",
      "READ",
      [
        "storage",
        "010a0d8c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b04d88",
      "WRITE",
      [
        "storage",
        "010a0d8c",
        null,
        "undefined1"
      ]
    ],
    [
      "00b04da0",
      "PARAM",
      [
        "storage",
        "002996c6",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b04d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04d18.md#insn-00b04d44) · [`00b04d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04d18.md#insn-00b04d60) · [`00b04d28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b04/00b04d18.md#insn-00b04d28)
- 新版 [`00b04d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04d5c.md#insn-00b04d88) · [`00b04da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04d5c.md#insn-00b04da4) · [`00b04d6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b04/00b04d5c.md#insn-00b04d6c)

~~~diff
- 00b04d44 ["COPY", "tmp:0:4", ["register:4040:4"]]
- 00b04d44 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:d4c:8"]]
- 00b04d44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b04d88 ["COPY", "tmp:0:4", ["register:4040:4"]]
+ 00b04d88 ["INT_ADD", "tmp:1:8", ["register:4048:8", "const:d8c:8"]]
+ 00b04d88 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b04d44 bytes 28313539
+ 00b04d88 bytes 28313639
- 00b04d60 ["INT_ADD", "register:40f0:8", ["const:b04d60:8", "const:4:8"]]
- 00b04d60 ["CALL", null, ["callee:00bde180:8"]]
+ 00b04da4 ["INT_ADD", "register:40f0:8", ["const:b04da4:8", "const:4:8"]]
+ 00b04da4 ["CALL", null, ["callee:00bde180:8"]]
- 00b04d60 bytes f4640394
+ 00b04da4 bytes f7640394
- 00b04d28 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d4c:8"]]
- 00b04d28 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b04d28 ["INT_ZEXT", "register:4050:8", ["tmp:1:1"]]
+ 00b04d6c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d8c:8"]]
+ 00b04d6c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b04d6c ["INT_ZEXT", "register:4050:8", ["tmp:1:1"]]
- 00b04d28 bytes 2a317539
+ 00b04d6c bytes 2a317639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c2161eccf5525b2ed52e4dbb061d7b0"></a>

### [`00b05390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05390.md) → [`00b053d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b053d4.md) _ZN8firebase5MutexC2ENS0_4ModeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bdddd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddd0.md) · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bdef80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef80.md) [`00bdef90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef90.md) [`00bdefa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdefa0.md)
- 新版 呼出元 2件 [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bdde20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md) · 呼出先 6件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bdefd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefd0.md) [`00bdefe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdefe0.md) [`00bdeff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdeff0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.49% / 新版 91.49%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0540c",
      "incomplete_value": false,
      "site": "00b05410",
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
            "const:e7b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b053c8",
      "incomplete_value": false,
      "site": "00b053cc",
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
            "const:df0:8"
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
      "definition_site": "00b0542c",
      "incomplete_value": false,
      "site": "00b05430",
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
            "const:e7b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b053e8",
      "incomplete_value": false,
      "site": "00b053ec",
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
            "const:df0:8"
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
      "definition_site": "00b05448",
      "incomplete_value": false,
      "site": "00b0544c",
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
            "const:e7b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05404",
      "incomplete_value": false,
      "site": "00b05408",
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
            "const:df0:8"
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
      "00b0540c",
      "PARAM",
      [
        "storage",
        "0029cdf0",
        null,
        "string"
      ]
    ],
    [
      "00b0542c",
      "PARAM",
      [
        "storage",
        "0029cdf0",
        null,
        "string"
      ]
    ],
    [
      "00b05448",
      "PARAM",
      [
        "storage",
        "0029cdf0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0540c",
      "PARAM",
      [
        "storage",
        "0029ce7b",
        null,
        "string"
      ]
    ],
    [
      "00b0542c",
      "PARAM",
      [
        "storage",
        "0029ce7b",
        null,
        "string"
      ]
    ],
    [
      "00b05448",
      "PARAM",
      [
        "storage",
        "0029ce7b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b053cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05390.md#insn-00b053cc) · [`00b053dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05390.md#insn-00b053dc) · [`00b053ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05390.md#insn-00b053ec)
- 新版 [`00b05410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b053d4.md#insn-00b05410) · [`00b05420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b053d4.md#insn-00b05420) · [`00b05430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b053d4.md#insn-00b05430)

~~~diff
- 00b053cc ["INT_ADD", "register:40f0:8", ["const:b053cc:8", "const:4:8"]]
- 00b053cc ["CALL", null, ["callee:00bde180:8"]]
+ 00b05410 ["INT_ADD", "register:40f0:8", ["const:b05410:8", "const:4:8"]]
+ 00b05410 ["CALL", null, ["callee:00bde180:8"]]
- 00b053cc bytes 59630394
+ 00b05410 bytes 5c630394
- 00b053dc ["INT_ADD", "register:40f0:8", ["const:b053dc:8", "const:4:8"]]
- 00b053dc ["CALL", null, ["callee:00bdf000:8"]]
+ 00b05420 ["INT_ADD", "register:40f0:8", ["const:b05420:8", "const:4:8"]]
+ 00b05420 ["CALL", null, ["callee:00bdf000:8"]]
- 00b053dc bytes f5660394
+ 00b05420 bytes f8660394
- 00b053ec ["INT_ADD", "register:40f0:8", ["const:b053ec:8", "const:4:8"]]
- 00b053ec ["CALL", null, ["callee:00bde180:8"]]
+ 00b05430 ["INT_ADD", "register:40f0:8", ["const:b05430:8", "const:4:8"]]
+ 00b05430 ["CALL", null, ["callee:00bde180:8"]]
- 00b053ec bytes 51630394
+ 00b05430 bytes 54630394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3443ba0136d9fa3ac240a406bfa1868"></a>

### [`00b054cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b054cc.md) → [`00b05510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05510.md) _ZN8firebase3app19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEENS_4util16Clas

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
      "definition_site": "00b0553c",
      "incomplete_value": true,
      "site": "00b0553c",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b054f8",
      "incomplete_value": true,
      "site": "00b054f8",
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
            "const:d50:8"
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
      "definition_site": "00b05524",
      "incomplete_value": true,
      "site": "00b05524",
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
      "definition_site": "00b054e0",
      "incomplete_value": true,
      "site": "00b054e0",
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
      "definition_site": "00b05530",
      "incomplete_value": false,
      "site": "00b05534",
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
            "const:1a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b054ec",
      "incomplete_value": false,
      "site": "00b054f0",
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
            "const:10d:8"
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
      "00b05520",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05530",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ],
    [
      "00b0553c",
      "WRITE",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05520",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05530",
      "PARAM",
      [
        "storage",
        "002a61a7",
        null,
        "string"
      ]
    ],
    [
      "00b0553c",
      "WRITE",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b054f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b054cc.md#insn-00b054f0) · [`00b054f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b054cc.md#insn-00b054f8) · [`00b054dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b054cc.md#insn-00b054dc)
- 新版 [`00b05534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05510.md#insn-00b05534) · [`00b0553c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05510.md#insn-00b0553c) · [`00b05520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05510.md#insn-00b05520)

~~~diff
- 00b054f0 ["INT_ADD", "register:40f0:8", ["const:b054f0:8", "const:4:8"]]
- 00b054f0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b05534 ["INT_ADD", "register:40f0:8", ["const:b05534:8", "const:4:8"]]
+ 00b05534 ["CALL", null, ["callee:00bde090:8"]]
- 00b054f0 bytes d4620394
+ 00b05534 bytes d7620394
- 00b054f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d50:8"]]
- 00b054f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b0553c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d90:8"]]
+ 00b0553c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b054f8 bytes 60aa06f9
+ 00b0553c bytes 60ca06f9
- 00b054dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d50:8"]]
- 00b054dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05520 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d90:8"]]
+ 00b05520 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b054dc bytes 68aa46f9
+ 00b05520 bytes 68ca46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8005fdd51744aa1f01462c687cd8eed"></a>

### [`00b0550c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0550c.md) → [`00b05550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05550.md) _ZN8firebase3app19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

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
      "definition_site": "00b0557c",
      "incomplete_value": true,
      "site": "00b0557c",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05538",
      "incomplete_value": true,
      "site": "00b05538",
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
            "const:d50:8"
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
      "definition_site": "00b05564",
      "incomplete_value": true,
      "site": "00b05564",
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
      "definition_site": "00b05520",
      "incomplete_value": true,
      "site": "00b05520",
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
      "definition_site": "00b0556c",
      "incomplete_value": false,
      "site": "00b05574",
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
            "const:1a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05528",
      "incomplete_value": false,
      "site": "00b05530",
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
            "const:10d:8"
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
      "00b05560",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0556c",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ],
    [
      "00b0557c",
      "WRITE",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05560",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0556c",
      "PARAM",
      [
        "storage",
        "002a61a7",
        null,
        "string"
      ]
    ],
    [
      "00b0557c",
      "WRITE",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0550c.md#insn-00b05530) · [`00b05538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0550c.md#insn-00b05538) · [`00b0551c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0550c.md#insn-00b0551c)
- 新版 [`00b05574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05550.md#insn-00b05574) · [`00b0557c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05550.md#insn-00b0557c) · [`00b05560`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05550.md#insn-00b05560)

~~~diff
- 00b05530 ["INT_ADD", "register:40f0:8", ["const:b05530:8", "const:4:8"]]
- 00b05530 ["CALL", null, ["callee:00bde090:8"]]
+ 00b05574 ["INT_ADD", "register:40f0:8", ["const:b05574:8", "const:4:8"]]
+ 00b05574 ["CALL", null, ["callee:00bde090:8"]]
- 00b05530 bytes c4620394
+ 00b05574 bytes c7620394
- 00b05538 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d50:8"]]
- 00b05538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b0557c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d90:8"]]
+ 00b0557c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05538 bytes 60aa06f9
+ 00b0557c bytes 60ca06f9
- 00b0551c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d50:8"]]
- 00b0551c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05560 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d90:8"]]
+ 00b05560 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b0551c bytes 68aa46f9
+ 00b05560 bytes 68ca46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a307b0eaa90883213bb7041d9d928c1d"></a>

### [`00b0554c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0554c.md) → [`00b05590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05590.md) _ZN8firebase3app10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

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
      "definition_site": "00b055c0",
      "incomplete_value": true,
      "site": "00b055c0",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0557c",
      "incomplete_value": true,
      "site": "00b0557c",
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
            "const:d50:8"
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
      "definition_site": "00b055a4",
      "incomplete_value": true,
      "site": "00b055a4",
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
      "definition_site": "00b05560",
      "incomplete_value": true,
      "site": "00b05560",
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
        "00b05560"
      ],
      [
        "FALL_THROUGH",
        "00b055a4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b055a4",
      "incomplete_value": true,
      "site": "00b055c0",
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
      "definition_site": "00b05560",
      "incomplete_value": true,
      "site": "00b0557c",
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
      "00b055a0",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b055b0",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ],
    [
      "00b055c0",
      "WRITE",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b055a0",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b055b0",
      "PARAM",
      [
        "storage",
        "002a61a7",
        null,
        "string"
      ]
    ],
    [
      "00b055c0",
      "WRITE",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0557c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0554c.md#insn-00b0557c) · [`00b0555c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0554c.md#insn-00b0555c) · [`00b0556c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0554c.md#insn-00b0556c)
- 新版 [`00b055c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05590.md#insn-00b055c0) · [`00b055a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05590.md#insn-00b055a0) · [`00b055b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05590.md#insn-00b055b0)

~~~diff
- 00b0557c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d50:8"]]
- 00b0557c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b055c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d90:8"]]
+ 00b055c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b0557c bytes 60aa06f9
+ 00b055c0 bytes 60ca06f9
- 00b0555c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d50:8"]]
- 00b0555c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b055a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d90:8"]]
+ 00b055a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b0555c bytes 68aa46f9
+ 00b055a0 bytes 68ca46f9
- 00b0556c ["COPY", "tmp:0:8", ["const:10d:8"]]
- 00b0556c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b0556c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b0556c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b055b0 ["COPY", "tmp:0:8", ["const:1a7:8"]]
+ 00b055b0 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b055b0 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b055b0 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b0556c bytes 63340491
+ 00b055b0 bytes 639c0691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e84d10c5352064948705a4740cc2624c"></a>

### [`00b05590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05590.md) → [`00b055d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b055d4.md) _ZN8firebase3app10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b05604",
      "incomplete_value": true,
      "site": "00b05604",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b055c0",
      "incomplete_value": true,
      "site": "00b055c0",
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
            "const:d50:8"
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
      "definition_site": "00b055e8",
      "incomplete_value": true,
      "site": "00b055e8",
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
      "definition_site": "00b055a4",
      "incomplete_value": true,
      "site": "00b055a4",
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
      "definition_site": "00b055f0",
      "incomplete_value": false,
      "site": "00b055fc",
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
            "const:1a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b055ac",
      "incomplete_value": false,
      "site": "00b055b8",
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
            "const:10d:8"
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
      "00b055e4",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b055f0",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ],
    [
      "00b05604",
      "WRITE",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b055e4",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b055f0",
      "PARAM",
      [
        "storage",
        "002a61a7",
        null,
        "string"
      ]
    ],
    [
      "00b05604",
      "WRITE",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b055b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05590.md#insn-00b055b8) · [`00b055c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05590.md#insn-00b055c0) · [`00b055a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05590.md#insn-00b055a0)
- 新版 [`00b055fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b055d4.md#insn-00b055fc) · [`00b05604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b055d4.md#insn-00b05604) · [`00b055e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b055d4.md#insn-00b055e4)

~~~diff
- 00b055b8 ["INT_ADD", "register:40f0:8", ["const:b055b8:8", "const:4:8"]]
- 00b055b8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b055fc ["INT_ADD", "register:40f0:8", ["const:b055fc:8", "const:4:8"]]
+ 00b055fc ["CALL", null, ["callee:00bde090:8"]]
- 00b055b8 bytes a2620394
+ 00b055fc bytes a5620394
- 00b055c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d50:8"]]
- 00b055c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05604 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d90:8"]]
+ 00b05604 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b055c0 bytes 60aa06f9
+ 00b05604 bytes 60ca06f9
- 00b055a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d50:8"]]
- 00b055a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b055e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d90:8"]]
+ 00b055e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b055a0 bytes 68aa46f9
+ 00b055e4 bytes 68ca46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a636b49fb1e6b4523604fb34d1f04b8"></a>

### [`00b055e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b055e0.md) → [`00b05624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05624.md) _ZN8firebase3app15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b0567c",
      "incomplete_value": true,
      "site": "00b0567c",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05638",
      "incomplete_value": true,
      "site": "00b05638",
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
            "const:d58:8"
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
      "definition_site": "00b05658",
      "incomplete_value": true,
      "site": "00b05664",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05614",
      "incomplete_value": true,
      "site": "00b05620",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d50:8"
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
      "00b05638",
      "READ",
      [
        "storage",
        "010a0d58",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05658",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0567c",
      "WRITE",
      [
        "storage",
        "010a0d58",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b05638",
      "READ",
      [
        "storage",
        "010a0d98",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05658",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0567c",
      "WRITE",
      [
        "storage",
        "010a0d98",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b055f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b055e0.md#insn-00b055f4) · [`00b05620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b055e0.md#insn-00b05620) · [`00b05638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b055e0.md#insn-00b05638)
- 新版 [`00b05638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05624.md#insn-00b05638) · [`00b05664`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05624.md#insn-00b05664) · [`00b0567c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05624.md#insn-00b0567c)

~~~diff
- 00b055f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d58:8"]]
- 00b055f4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b055f4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b05638 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d98:8"]]
+ 00b05638 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b05638 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b055f4 bytes a8627539
+ 00b05638 bytes a8627639
- 00b05620 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b05620 ["INT_ADD", "register:40f0:8", ["const:b05620:8", "const:4:8"]]
- 00b05620 ["CALLIND", null, ["register:0:8"]]
+ 00b05664 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b05664 ["INT_ADD", "register:40f0:8", ["const:b05664:8", "const:4:8"]]
+ 00b05664 ["CALLIND", null, ["register:0:8"]]
- 00b05620 bytes 00013fd6
+ 00b05664 bytes 00013fd6
- 00b05638 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b05638 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d58:8"]]
- 00b05638 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b0567c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b0567c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d98:8"]]
+ 00b0567c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b05638 bytes a0623539
+ 00b0567c bytes a0623639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9250032b2543adecd54fb70505f79187"></a>

### [`00b0564c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0564c.md) → [`00b05690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05690.md) _ZN8firebase3app12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b056cc",
      "incomplete_value": true,
      "site": "00b056cc",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05688",
      "incomplete_value": true,
      "site": "00b05688",
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
            "const:d58:8"
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
      "definition_site": "00b056ec",
      "incomplete_value": true,
      "site": "00b056ec",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b056a8",
      "incomplete_value": true,
      "site": "00b056a8",
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
            "const:d50:8"
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
      "definition_site": "00b056a8",
      "incomplete_value": true,
      "site": "00b056a8",
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
      "definition_site": "00b05664",
      "incomplete_value": true,
      "site": "00b05664",
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
      "00b056a4",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b056b0",
      "READ",
      [
        "storage",
        "010a0d58",
        null,
        "undefined1"
      ]
    ],
    [
      "00b056cc",
      "WRITE",
      [
        "storage",
        "010a0d58",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b056a4",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b056b0",
      "READ",
      [
        "storage",
        "010a0d98",
        null,
        "undefined1"
      ]
    ],
    [
      "00b056cc",
      "WRITE",
      [
        "storage",
        "010a0d98",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0564c.md#insn-00b05660) · [`00b05688`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0564c.md#insn-00b05688) · [`00b056a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0564c.md#insn-00b056a4)
- 新版 [`00b056a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05690.md#insn-00b056a4) · [`00b056cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05690.md#insn-00b056cc) · [`00b056e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05690.md#insn-00b056e8)

~~~diff
- 00b05660 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d50:8"]]
- 00b05660 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b056a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d90:8"]]
+ 00b056a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05660 bytes 81aa46f9
+ 00b056a4 bytes 81ca46f9
- 00b05688 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b05688 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b05688 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d58:8"]]
- 00b05688 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b056cc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b056cc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b056cc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d98:8"]]
+ 00b056cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b05688 bytes bf623539
+ 00b056cc bytes bf623639
- 00b056a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b056a4 ["INT_ADD", "register:40f0:8", ["const:b056a4:8", "const:4:8"]]
- 00b056a4 ["CALLIND", null, ["register:0:8"]]
+ 00b056e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b056e8 ["INT_ADD", "register:40f0:8", ["const:b056e8:8", "const:4:8"]]
+ 00b056e8 ["CALLIND", null, ["register:0:8"]]
- 00b056a4 bytes 00013fd6
+ 00b056e8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-489657de0b76e7857bdd0b5b345b26a0"></a>

### [`00b056bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b056bc.md) → [`00b05700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05700.md) _ZN8firebase3app14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b05740",
      "incomplete_value": true,
      "site": "00b05740",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b056fc",
      "incomplete_value": true,
      "site": "00b056fc",
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
            "const:d50:8"
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
      "definition_site": "00b0571c",
      "incomplete_value": true,
      "site": "00b0571c",
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
      "definition_site": "00b056d8",
      "incomplete_value": true,
      "site": "00b056d8",
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
      "definition_site": "00b05724",
      "incomplete_value": false,
      "site": "00b05738",
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
            "const:1a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b056e0",
      "incomplete_value": false,
      "site": "00b056f4",
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
            "const:10d:8"
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
      "00b05714",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05724",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ],
    [
      "00b05740",
      "WRITE",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05714",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05724",
      "PARAM",
      [
        "storage",
        "002a61a7",
        null,
        "string"
      ]
    ],
    [
      "00b05740",
      "WRITE",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b056f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b056bc.md#insn-00b056f4) · [`00b056fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b056bc.md#insn-00b056fc) · [`00b056d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b056bc.md#insn-00b056d0)
- 新版 [`00b05738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05700.md#insn-00b05738) · [`00b05740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05700.md#insn-00b05740) · [`00b05714`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05700.md#insn-00b05714)

~~~diff
- 00b056f4 ["INT_ADD", "register:40f0:8", ["const:b056f4:8", "const:4:8"]]
- 00b056f4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b05738 ["INT_ADD", "register:40f0:8", ["const:b05738:8", "const:4:8"]]
+ 00b05738 ["CALL", null, ["callee:00bde090:8"]]
- 00b056f4 bytes 53620394
+ 00b05738 bytes 56620394
- 00b056fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d50:8"]]
- 00b056fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05740 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d90:8"]]
+ 00b05740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b056fc bytes 80aa06f9
+ 00b05740 bytes 80ca06f9
- 00b056d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d50:8"]]
- 00b056d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05714 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d90:8"]]
+ 00b05714 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b056d0 bytes 81aa46f9
+ 00b05714 bytes 81ca46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50473e14161ce20f989ce75eeff75a9f"></a>

### [`00b0572c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0572c.md) → [`00b05770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05770.md) _ZN8firebase3app11GetMethodIdENS0_6MethodE

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
      "definition_site": "00b0578c",
      "incomplete_value": false,
      "site": "00b05790",
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
      "definition_site": "00b05748",
      "incomplete_value": false,
      "site": "00b0574c",
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
      "definition_site": "00b0579c",
      "incomplete_value": true,
      "site": "00b057a8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b05758",
      "incomplete_value": true,
      "site": "00b05764",
      "value": [
        "LOAD",
        "8",
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
      "00b0578c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b0579c",
      "DATA",
      [
        "storage",
        "010a0d60",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b0578c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b0579c",
      "DATA",
      [
        "storage",
        "010a0da0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0574c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0572c.md#insn-00b0574c) · [`00b05748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0572c.md#insn-00b05748) · [`00b05754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b0572c.md#insn-00b05754)
- 新版 [`00b05790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05770.md#insn-00b05790) · [`00b0578c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05770.md#insn-00b0578c) · [`00b05798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05770.md#insn-00b05798)

~~~diff
- 00b0574c ["INT_ADD", "register:40f0:8", ["const:b0574c:8", "const:4:8"]]
- 00b0574c ["CALL", null, ["callee:00bde180:8"]]
+ 00b05790 ["INT_ADD", "register:40f0:8", ["const:b05790:8", "const:4:8"]]
+ 00b05790 ["CALL", null, ["callee:00bde180:8"]]
- 00b0574c bytes 79620394
+ 00b05790 bytes 7c620394
- 00b05748 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b05748 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b05748 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b05748 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b0578c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b0578c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b0578c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b0578c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b05748 bytes 00501791
+ 00b0578c bytes 001c1591
- 00b05754 ["COPY", "tmp:0:8", ["const:d60:8"]]
- 00b05754 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b05754 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b05754 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b05798 ["COPY", "tmp:0:8", ["const:da0:8"]]
+ 00b05798 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05798 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05798 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b05754 bytes 08813591
+ 00b05798 bytes 08813691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e624335457308101879843dfd249e5d"></a>

### [`00b05768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05768.md) → [`00b057ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b057ac.md) _ZN8firebase3app13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b057ec",
      "incomplete_value": true,
      "site": "00b057ec",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b057a8",
      "incomplete_value": true,
      "site": "00b057a8",
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
            "const:d50:8"
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
      "definition_site": "00b057c8",
      "incomplete_value": true,
      "site": "00b057c8",
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
      "definition_site": "00b05784",
      "incomplete_value": true,
      "site": "00b05784",
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
      "definition_site": "00b057d0",
      "incomplete_value": false,
      "site": "00b057e4",
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
            "const:1a7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0578c",
      "incomplete_value": false,
      "site": "00b057a0",
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
            "const:10d:8"
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
      "00b057c0",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b057d0",
      "PARAM",
      [
        "storage",
        "002a610d",
        null,
        "string"
      ]
    ],
    [
      "00b057ec",
      "WRITE",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b057c0",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b057d0",
      "PARAM",
      [
        "storage",
        "002a61a7",
        null,
        "string"
      ]
    ],
    [
      "00b057ec",
      "WRITE",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b057a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05768.md#insn-00b057a0) · [`00b057a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05768.md#insn-00b057a8) · [`00b0577c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05768.md#insn-00b0577c)
- 新版 [`00b057e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b057ac.md#insn-00b057e4) · [`00b057ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b057ac.md#insn-00b057ec) · [`00b057c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b057ac.md#insn-00b057c0)

~~~diff
- 00b057a0 ["INT_ADD", "register:40f0:8", ["const:b057a0:8", "const:4:8"]]
- 00b057a0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b057e4 ["INT_ADD", "register:40f0:8", ["const:b057e4:8", "const:4:8"]]
+ 00b057e4 ["CALL", null, ["callee:00bde090:8"]]
- 00b057a0 bytes 28620394
+ 00b057e4 bytes 2b620394
- 00b057a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d50:8"]]
- 00b057a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b057ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d90:8"]]
+ 00b057ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b057a8 bytes 80aa06f9
+ 00b057ec bytes 80ca06f9
- 00b0577c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d50:8"]]
- 00b0577c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b057c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d90:8"]]
+ 00b057c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b0577c bytes 81aa46f9
+ 00b057c0 bytes 81ca46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0015eb1b02d11e5d96106869fbf4ca95"></a>

### [`00b057d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b057d8.md) → [`00b0581c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0581c.md) _ZN8firebase3app10GetFieldIdENS0_5FieldE

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
      "definition_site": "00b05838",
      "incomplete_value": false,
      "site": "00b0583c",
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
      "definition_site": "00b057f4",
      "incomplete_value": false,
      "site": "00b057f8",
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b05838",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b05848",
      "DATA",
      [
        "storage",
        "010a0da8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b05838",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b05848",
      "DATA",
      [
        "storage",
        "010a0de8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b057f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b057d8.md#insn-00b057f8) · [`00b057f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b057d8.md#insn-00b057f4) · [`00b05800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b057d8.md#insn-00b05800)
- 新版 [`00b0583c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0581c.md#insn-00b0583c) · [`00b05838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0581c.md#insn-00b05838) · [`00b05844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0581c.md#insn-00b05844)

~~~diff
- 00b057f8 ["INT_ADD", "register:40f0:8", ["const:b057f8:8", "const:4:8"]]
- 00b057f8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b0583c ["INT_ADD", "register:40f0:8", ["const:b0583c:8", "const:4:8"]]
+ 00b0583c ["CALL", null, ["callee:00bde180:8"]]
- 00b057f8 bytes 4e620394
+ 00b0583c bytes 51620394
- 00b057f4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b057f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b057f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b057f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b05838 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b05838 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05838 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05838 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b057f4 bytes 00fc1991
+ 00b05838 bytes 00c81791
- 00b05800 ["COPY", "tmp:0:8", ["const:da8:8"]]
- 00b05800 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b05800 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b05800 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b05844 ["COPY", "tmp:0:8", ["const:de8:8"]]
+ 00b05844 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05844 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05844 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b05800 bytes 08a13691
+ 00b05844 bytes 08a13791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d0854e90952f9bbae7cdaa67331c91dc"></a>

### [`00b05814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05814.md) → [`00b05858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05858.md) _ZN8firebase15options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEN

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b05884",
      "incomplete_value": true,
      "site": "00b05884",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05840",
      "incomplete_value": true,
      "site": "00b05840",
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
            "const:db0:8"
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
      "definition_site": "00b05878",
      "incomplete_value": false,
      "site": "00b0587c",
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
            "const:221:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05834",
      "incomplete_value": false,
      "site": "00b05838",
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
            "const:2ae:8"
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
      "00b05868",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05878",
      "PARAM",
      [
        "storage",
        "002932ae",
        null,
        "string"
      ]
    ],
    [
      "00b05884",
      "WRITE",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05868",
      "READ",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05878",
      "PARAM",
      [
        "storage",
        "00293221",
        null,
        "string"
      ]
    ],
    [
      "00b05884",
      "WRITE",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05814.md#insn-00b05838) · [`00b05840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05814.md#insn-00b05840) · [`00b05824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05814.md#insn-00b05824)
- 新版 [`00b0587c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05858.md#insn-00b0587c) · [`00b05884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05858.md#insn-00b05884) · [`00b05868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05858.md#insn-00b05868)

~~~diff
- 00b05838 ["INT_ADD", "register:40f0:8", ["const:b05838:8", "const:4:8"]]
- 00b05838 ["CALL", null, ["callee:00bde090:8"]]
+ 00b0587c ["INT_ADD", "register:40f0:8", ["const:b0587c:8", "const:4:8"]]
+ 00b0587c ["CALL", null, ["callee:00bde090:8"]]
- 00b05838 bytes 02620394
+ 00b0587c bytes 05620394
- 00b05840 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00b05840 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05884 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b05884 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05840 bytes 60da06f9
+ 00b05884 bytes 60fa06f9
- 00b05824 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00b05824 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b05868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05824 bytes 68da46f9
+ 00b05868 bytes 68fa46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e6de42c6bf349322120ca73d2b9f963"></a>

### [`00b05854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05854.md) → [`00b05898`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05898.md) _ZN8firebase15options_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

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
      "definition_site": "00b058c4",
      "incomplete_value": true,
      "site": "00b058c4",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05880",
      "incomplete_value": true,
      "site": "00b05880",
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
            "const:db0:8"
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
      "definition_site": "00b058ac",
      "incomplete_value": true,
      "site": "00b058ac",
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
      "definition_site": "00b05868",
      "incomplete_value": true,
      "site": "00b05868",
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
      "definition_site": "00b058b4",
      "incomplete_value": false,
      "site": "00b058bc",
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
            "const:221:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05870",
      "incomplete_value": false,
      "site": "00b05878",
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
            "const:2ae:8"
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
      "00b058a8",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b058b4",
      "PARAM",
      [
        "storage",
        "002932ae",
        null,
        "string"
      ]
    ],
    [
      "00b058c4",
      "WRITE",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b058a8",
      "READ",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b058b4",
      "PARAM",
      [
        "storage",
        "00293221",
        null,
        "string"
      ]
    ],
    [
      "00b058c4",
      "WRITE",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05854.md#insn-00b05878) · [`00b05880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05854.md#insn-00b05880) · [`00b05864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05854.md#insn-00b05864)
- 新版 [`00b058bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05898.md#insn-00b058bc) · [`00b058c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05898.md#insn-00b058c4) · [`00b058a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05898.md#insn-00b058a8)

~~~diff
- 00b05878 ["INT_ADD", "register:40f0:8", ["const:b05878:8", "const:4:8"]]
- 00b05878 ["CALL", null, ["callee:00bde090:8"]]
+ 00b058bc ["INT_ADD", "register:40f0:8", ["const:b058bc:8", "const:4:8"]]
+ 00b058bc ["CALL", null, ["callee:00bde090:8"]]
- 00b05878 bytes f2610394
+ 00b058bc bytes f5610394
- 00b05880 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00b05880 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b058c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b058c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05880 bytes 60da06f9
+ 00b058c4 bytes 60fa06f9
- 00b05864 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00b05864 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b058a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b058a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05864 bytes 68da46f9
+ 00b058a8 bytes 68fa46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7862049ea19675de2625dfe8428a46d6"></a>

### [`00b05894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05894.md) → [`00b058d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b058d8.md) _ZN8firebase15options_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b05908",
      "incomplete_value": true,
      "site": "00b05908",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b058c4",
      "incomplete_value": true,
      "site": "00b058c4",
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
            "const:db0:8"
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
      "definition_site": "00b058ec",
      "incomplete_value": true,
      "site": "00b058ec",
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
      "definition_site": "00b058a8",
      "incomplete_value": true,
      "site": "00b058a8",
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
      "definition_site": "00b058f8",
      "incomplete_value": false,
      "site": "00b05900",
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
            "const:221:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b058b4",
      "incomplete_value": false,
      "site": "00b058bc",
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
            "const:2ae:8"
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
      "00b058e8",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b058f8",
      "PARAM",
      [
        "storage",
        "002932ae",
        null,
        "string"
      ]
    ],
    [
      "00b05908",
      "WRITE",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b058e8",
      "READ",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b058f8",
      "PARAM",
      [
        "storage",
        "00293221",
        null,
        "string"
      ]
    ],
    [
      "00b05908",
      "WRITE",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b058bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05894.md#insn-00b058bc) · [`00b058c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05894.md#insn-00b058c4) · [`00b058a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05894.md#insn-00b058a4)
- 新版 [`00b05900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b058d8.md#insn-00b05900) · [`00b05908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b058d8.md#insn-00b05908) · [`00b058e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b058d8.md#insn-00b058e8)

~~~diff
- 00b058bc ["INT_ADD", "register:40f0:8", ["const:b058bc:8", "const:4:8"]]
- 00b058bc ["CALL", null, ["callee:00bde090:8"]]
+ 00b05900 ["INT_ADD", "register:40f0:8", ["const:b05900:8", "const:4:8"]]
+ 00b05900 ["CALL", null, ["callee:00bde090:8"]]
- 00b058bc bytes e1610394
+ 00b05900 bytes e4610394
- 00b058c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00b058c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05908 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b05908 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b058c4 bytes 60da06f9
+ 00b05908 bytes 60fa06f9
- 00b058a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00b058a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b058e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b058e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b058a4 bytes 68da46f9
+ 00b058e8 bytes 68fa46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07b445ebbac6ebd391612dbce9b24d25"></a>

### [`00b058d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b058d8.md) → [`00b0591c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0591c.md) _ZN8firebase15options_builder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b0594c",
      "incomplete_value": true,
      "site": "00b0594c",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05908",
      "incomplete_value": true,
      "site": "00b05908",
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
            "const:db0:8"
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
      "definition_site": "00b05930",
      "incomplete_value": true,
      "site": "00b05930",
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
      "definition_site": "00b058ec",
      "incomplete_value": true,
      "site": "00b058ec",
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
      "definition_site": "00b05938",
      "incomplete_value": false,
      "site": "00b05944",
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
            "const:221:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b058f4",
      "incomplete_value": false,
      "site": "00b05900",
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
            "const:2ae:8"
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
      "00b0592c",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05938",
      "PARAM",
      [
        "storage",
        "002932ae",
        null,
        "string"
      ]
    ],
    [
      "00b0594c",
      "WRITE",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b0592c",
      "READ",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05938",
      "PARAM",
      [
        "storage",
        "00293221",
        null,
        "string"
      ]
    ],
    [
      "00b0594c",
      "WRITE",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b058d8.md#insn-00b05900) · [`00b05908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b058d8.md#insn-00b05908) · [`00b058e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b058d8.md#insn-00b058e8)
- 新版 [`00b05944`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0591c.md#insn-00b05944) · [`00b0594c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0591c.md#insn-00b0594c) · [`00b0592c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0591c.md#insn-00b0592c)

~~~diff
- 00b05900 ["INT_ADD", "register:40f0:8", ["const:b05900:8", "const:4:8"]]
- 00b05900 ["CALL", null, ["callee:00bde090:8"]]
+ 00b05944 ["INT_ADD", "register:40f0:8", ["const:b05944:8", "const:4:8"]]
+ 00b05944 ["CALL", null, ["callee:00bde090:8"]]
- 00b05900 bytes d0610394
+ 00b05944 bytes d3610394
- 00b05908 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00b05908 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b0594c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b0594c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05908 bytes 60da06f9
+ 00b0594c bytes 60fa06f9
- 00b058e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:db0:8"]]
- 00b058e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b0592c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:df0:8"]]
+ 00b0592c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b058e8 bytes 68da46f9
+ 00b0592c bytes 68fa46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff01a8a9754c6003e8189667400de868"></a>

### [`00b05928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05928.md) → [`00b0596c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0596c.md) _ZN8firebase15options_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b059c4",
      "incomplete_value": true,
      "site": "00b059c4",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05980",
      "incomplete_value": true,
      "site": "00b05980",
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
            "const:db8:8"
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
      "definition_site": "00b059a0",
      "incomplete_value": true,
      "site": "00b059ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:df0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0595c",
      "incomplete_value": true,
      "site": "00b05968",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db0:8"
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
      "00b05980",
      "READ",
      [
        "storage",
        "010a0db8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b059a0",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b059c4",
      "WRITE",
      [
        "storage",
        "010a0db8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b05980",
      "READ",
      [
        "storage",
        "010a0df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b059a0",
      "READ",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b059c4",
      "WRITE",
      [
        "storage",
        "010a0df8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0593c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05928.md#insn-00b0593c) · [`00b05968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05928.md#insn-00b05968) · [`00b05980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05928.md#insn-00b05980)
- 新版 [`00b05980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0596c.md#insn-00b05980) · [`00b059ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0596c.md#insn-00b059ac) · [`00b059c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b0596c.md#insn-00b059c4)

~~~diff
- 00b0593c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:db8:8"]]
- 00b0593c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b0593c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b05980 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:df8:8"]]
+ 00b05980 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b05980 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b0593c bytes a8e27639
+ 00b05980 bytes a8e27739
- 00b05968 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b05968 ["INT_ADD", "register:40f0:8", ["const:b05968:8", "const:4:8"]]
- 00b05968 ["CALLIND", null, ["register:0:8"]]
+ 00b059ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b059ac ["INT_ADD", "register:40f0:8", ["const:b059ac:8", "const:4:8"]]
+ 00b059ac ["CALLIND", null, ["register:0:8"]]
- 00b05968 bytes 00013fd6
+ 00b059ac bytes 00013fd6
- 00b05980 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b05980 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:db8:8"]]
- 00b05980 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b059c4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b059c4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:df8:8"]]
+ 00b059c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b05980 bytes a0e23639
+ 00b059c4 bytes a0e23739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1750c5b6d1d9d93a1f6e11130d7d03d"></a>

### [`00b05994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05994.md) → [`00b059d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b059d8.md) _ZN8firebase15options_builder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b05a14",
      "incomplete_value": true,
      "site": "00b05a14",
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
            "const:df8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b059d0",
      "incomplete_value": true,
      "site": "00b059d0",
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
            "const:db8:8"
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
      "definition_site": "00b05a34",
      "incomplete_value": true,
      "site": "00b05a34",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b059f0",
      "incomplete_value": true,
      "site": "00b059f0",
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
            "const:db0:8"
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
      "definition_site": "00b059f0",
      "incomplete_value": true,
      "site": "00b059f0",
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
      "definition_site": "00b059ac",
      "incomplete_value": true,
      "site": "00b059ac",
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
      "00b059ec",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b059f8",
      "READ",
      [
        "storage",
        "010a0db8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05a14",
      "WRITE",
      [
        "storage",
        "010a0db8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b059ec",
      "READ",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b059f8",
      "READ",
      [
        "storage",
        "010a0df8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05a14",
      "WRITE",
      [
        "storage",
        "010a0df8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b059a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05994.md#insn-00b059a8) · [`00b059d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05994.md#insn-00b059d0) · [`00b059ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05994.md#insn-00b059ec)
- 新版 [`00b059ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b059d8.md#insn-00b059ec) · [`00b05a14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b059d8.md#insn-00b05a14) · [`00b05a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b059d8.md#insn-00b05a30)

~~~diff
- 00b059a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
- 00b059a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b059ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
+ 00b059ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b059a8 bytes 81da46f9
+ 00b059ec bytes 81fa46f9
- 00b059d0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b059d0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b059d0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:db8:8"]]
- 00b059d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b05a14 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b05a14 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b05a14 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:df8:8"]]
+ 00b05a14 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b059d0 bytes bfe23639
+ 00b05a14 bytes bfe23739
- 00b059ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00b059ec ["INT_ADD", "register:40f0:8", ["const:b059ec:8", "const:4:8"]]
- 00b059ec ["CALLIND", null, ["register:0:8"]]
+ 00b05a30 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b05a30 ["INT_ADD", "register:40f0:8", ["const:b05a30:8", "const:4:8"]]
+ 00b05a30 ["CALLIND", null, ["register:0:8"]]
- 00b059ec bytes 00013fd6
+ 00b05a30 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-385088f4f04dfc028d61c54bac5ba79d"></a>

### [`00b05a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05a04.md) → [`00b05a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05a48.md) _ZN8firebase15options_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b05a88",
      "incomplete_value": true,
      "site": "00b05a88",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05a44",
      "incomplete_value": true,
      "site": "00b05a44",
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
            "const:db0:8"
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
      "definition_site": "00b05a6c",
      "incomplete_value": false,
      "site": "00b05a80",
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
            "const:221:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05a28",
      "incomplete_value": false,
      "site": "00b05a3c",
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
            "const:2ae:8"
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
      "00b05a5c",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05a6c",
      "PARAM",
      [
        "storage",
        "002932ae",
        null,
        "string"
      ]
    ],
    [
      "00b05a88",
      "WRITE",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05a5c",
      "READ",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05a6c",
      "PARAM",
      [
        "storage",
        "00293221",
        null,
        "string"
      ]
    ],
    [
      "00b05a88",
      "WRITE",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05a3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05a04.md#insn-00b05a3c) · [`00b05a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05a04.md#insn-00b05a44) · [`00b05a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05a04.md#insn-00b05a18)
- 新版 [`00b05a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05a48.md#insn-00b05a80) · [`00b05a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05a48.md#insn-00b05a88) · [`00b05a5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05a48.md#insn-00b05a5c)

~~~diff
- 00b05a3c ["INT_ADD", "register:40f0:8", ["const:b05a3c:8", "const:4:8"]]
- 00b05a3c ["CALL", null, ["callee:00bde090:8"]]
+ 00b05a80 ["INT_ADD", "register:40f0:8", ["const:b05a80:8", "const:4:8"]]
+ 00b05a80 ["CALL", null, ["callee:00bde090:8"]]
- 00b05a3c bytes 81610394
+ 00b05a80 bytes 84610394
- 00b05a44 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
- 00b05a44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05a88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
+ 00b05a88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05a44 bytes 80da06f9
+ 00b05a88 bytes 80fa06f9
- 00b05a18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
- 00b05a18 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05a5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
+ 00b05a5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05a18 bytes 81da46f9
+ 00b05a5c bytes 81fa46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15e71a570c20c5dab619b2db7b914960"></a>

### [`00b05a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05a74.md) → [`00b05ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ab8.md) _ZN8firebase15options_builder11GetMethodIdENS0_6MethodE

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
      "definition_site": "00b05ad4",
      "incomplete_value": false,
      "site": "00b05ad8",
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
      "definition_site": "00b05a90",
      "incomplete_value": false,
      "site": "00b05a94",
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
      "definition_site": "00b05ae4",
      "incomplete_value": true,
      "site": "00b05af0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b05aa0",
      "incomplete_value": true,
      "site": "00b05aac",
      "value": [
        "LOAD",
        "8",
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
      "00b05ad4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b05ae4",
      "DATA",
      [
        "storage",
        "010a0dc0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05ad4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b05ae4",
      "DATA",
      [
        "storage",
        "010a0e00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05a74.md#insn-00b05a94) · [`00b05a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05a74.md#insn-00b05a90) · [`00b05a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05a74.md#insn-00b05a9c)
- 新版 [`00b05ad8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ab8.md#insn-00b05ad8) · [`00b05ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ab8.md#insn-00b05ad4) · [`00b05ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ab8.md#insn-00b05ae0)

~~~diff
- 00b05a94 ["INT_ADD", "register:40f0:8", ["const:b05a94:8", "const:4:8"]]
- 00b05a94 ["CALL", null, ["callee:00bde180:8"]]
+ 00b05ad8 ["INT_ADD", "register:40f0:8", ["const:b05ad8:8", "const:4:8"]]
+ 00b05ad8 ["CALL", null, ["callee:00bde180:8"]]
- 00b05a94 bytes a7610394
+ 00b05ad8 bytes aa610394
- 00b05a90 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b05a90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b05a90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b05a90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b05ad4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b05ad4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05ad4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05ad4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b05a90 bytes 00501791
+ 00b05ad4 bytes 001c1591
- 00b05a9c ["COPY", "tmp:0:8", ["const:dc0:8"]]
- 00b05a9c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b05a9c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b05a9c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b05ae0 ["COPY", "tmp:0:8", ["const:e00:8"]]
+ 00b05ae0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05ae0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05ae0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b05a9c bytes 08013791
+ 00b05ae0 bytes 08013891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81116e018a514f98918ef48a8edf584d"></a>

### [`00b05ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ab0.md) → [`00b05af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05af4.md) _ZN8firebase15options_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.57% / 新版 78.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b05b34",
      "incomplete_value": true,
      "site": "00b05b34",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05af0",
      "incomplete_value": true,
      "site": "00b05af0",
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
            "const:db0:8"
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
      "definition_site": "00b05b10",
      "incomplete_value": true,
      "site": "00b05b10",
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
      "definition_site": "00b05acc",
      "incomplete_value": true,
      "site": "00b05acc",
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
        "00b05acc"
      ],
      [
        "FALL_THROUGH",
        "00b05b10"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b05b10",
      "incomplete_value": true,
      "site": "00b05b34",
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
      "definition_site": "00b05acc",
      "incomplete_value": true,
      "site": "00b05af0",
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
      "00b05b08",
      "READ",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05b18",
      "PARAM",
      [
        "storage",
        "002932ae",
        null,
        "string"
      ]
    ],
    [
      "00b05b34",
      "WRITE",
      [
        "storage",
        "010a0db0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05b08",
      "READ",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05b18",
      "PARAM",
      [
        "storage",
        "00293221",
        null,
        "string"
      ]
    ],
    [
      "00b05b34",
      "WRITE",
      [
        "storage",
        "010a0df0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ab0.md#insn-00b05af0) · [`00b05ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ab0.md#insn-00b05ac4) · [`00b05ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ab0.md#insn-00b05ad4)
- 新版 [`00b05b34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05af4.md#insn-00b05b34) · [`00b05b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05af4.md#insn-00b05b08) · [`00b05b18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05af4.md#insn-00b05b18)

~~~diff
- 00b05af0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
- 00b05af0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05b34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
+ 00b05b34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05af0 bytes 80da06f9
+ 00b05b34 bytes 80fa06f9
- 00b05ac4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:db0:8"]]
- 00b05ac4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05b08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:df0:8"]]
+ 00b05b08 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05ac4 bytes 81da46f9
+ 00b05b08 bytes 81fa46f9
- 00b05ad4 ["COPY", "tmp:0:8", ["const:2ae:8"]]
- 00b05ad4 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b05ad4 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b05ad4 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b05b18 ["COPY", "tmp:0:8", ["const:221:8"]]
+ 00b05b18 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b05b18 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b05b18 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b05ad4 bytes 63b80a91
+ 00b05b18 bytes 63840891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-474fa8cf03e3b79a92117cb72d4930c9"></a>

### [`00b05b20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b20.md) → [`00b05b64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05b64.md) _ZN8firebase15options_builder10GetFieldIdENS0_5FieldE

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
      "definition_site": "00b05b80",
      "incomplete_value": false,
      "site": "00b05b84",
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
      "definition_site": "00b05b3c",
      "incomplete_value": false,
      "site": "00b05b40",
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
      "definition_site": "00b05b90",
      "incomplete_value": true,
      "site": "00b05b9c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b05b4c",
      "incomplete_value": true,
      "site": "00b05b58",
      "value": [
        "LOAD",
        "8",
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
      "00b05b80",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b05b90",
      "DATA",
      [
        "storage",
        "010a0e00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b05b80",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b05b90",
      "DATA",
      [
        "storage",
        "010a0e40",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b20.md#insn-00b05b40) · [`00b05b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b20.md#insn-00b05b3c) · [`00b05b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b20.md#insn-00b05b48)
- 新版 [`00b05b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05b64.md#insn-00b05b84) · [`00b05b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05b64.md#insn-00b05b80) · [`00b05b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05b64.md#insn-00b05b8c)

~~~diff
- 00b05b40 ["INT_ADD", "register:40f0:8", ["const:b05b40:8", "const:4:8"]]
- 00b05b40 ["CALL", null, ["callee:00bde180:8"]]
+ 00b05b84 ["INT_ADD", "register:40f0:8", ["const:b05b84:8", "const:4:8"]]
+ 00b05b84 ["CALL", null, ["callee:00bde180:8"]]
- 00b05b40 bytes 7c610394
+ 00b05b84 bytes 7f610394
- 00b05b3c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b05b3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b05b3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b05b3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b05b80 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b05b80 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05b80 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05b80 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b05b3c bytes 00fc1991
+ 00b05b80 bytes 00c81791
- 00b05b48 ["COPY", "tmp:0:8", ["const:e00:8"]]
- 00b05b48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b05b48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b05b48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b05b8c ["COPY", "tmp:0:8", ["const:e40:8"]]
+ 00b05b8c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05b8c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05b8c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b05b48 bytes 08013891
+ 00b05b8c bytes 08013991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-042f5082e8767cfe4da542e54e8e53c5"></a>

### [`00b05b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b5c.md) → [`00b05ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ba0.md) _ZN8firebase7options19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEENS_4util16

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
      "definition_site": "00b05bcc",
      "incomplete_value": true,
      "site": "00b05bcc",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05b88",
      "incomplete_value": true,
      "site": "00b05b88",
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
            "const:e08:8"
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
      "definition_site": "00b05bb4",
      "incomplete_value": true,
      "site": "00b05bb4",
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
      "definition_site": "00b05b70",
      "incomplete_value": true,
      "site": "00b05b70",
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
      "definition_site": "00b05bc0",
      "incomplete_value": false,
      "site": "00b05bc4",
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
            "const:f8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05b7c",
      "incomplete_value": false,
      "site": "00b05b80",
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
            "const:eff:8"
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
      "00b05bb0",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05bc0",
      "PARAM",
      [
        "storage",
        "002a4eff",
        null,
        "string"
      ]
    ],
    [
      "00b05bcc",
      "WRITE",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05bb0",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05bc0",
      "PARAM",
      [
        "storage",
        "002a4f8a",
        null,
        "string"
      ]
    ],
    [
      "00b05bcc",
      "WRITE",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b5c.md#insn-00b05b80) · [`00b05b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b5c.md#insn-00b05b88) · [`00b05b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b5c.md#insn-00b05b6c)
- 新版 [`00b05bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ba0.md#insn-00b05bc4) · [`00b05bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ba0.md#insn-00b05bcc) · [`00b05bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ba0.md#insn-00b05bb0)

~~~diff
- 00b05b80 ["INT_ADD", "register:40f0:8", ["const:b05b80:8", "const:4:8"]]
- 00b05b80 ["CALL", null, ["callee:00bde090:8"]]
+ 00b05bc4 ["INT_ADD", "register:40f0:8", ["const:b05bc4:8", "const:4:8"]]
+ 00b05bc4 ["CALL", null, ["callee:00bde090:8"]]
- 00b05b80 bytes 30610394
+ 00b05bc4 bytes 33610394
- 00b05b88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e08:8"]]
- 00b05b88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05bcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b05bcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05b88 bytes 600607f9
+ 00b05bcc bytes 602607f9
- 00b05b6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e08:8"]]
- 00b05b6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05bb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b05bb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05b6c bytes 680647f9
+ 00b05bb0 bytes 682647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bcff62a313041b5eda697e72fd420584"></a>

### [`00b05b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b9c.md) → [`00b05be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05be0.md) _ZN8firebase7options19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

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
      "definition_site": "00b05c0c",
      "incomplete_value": true,
      "site": "00b05c0c",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05bc8",
      "incomplete_value": true,
      "site": "00b05bc8",
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
            "const:e08:8"
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
      "definition_site": "00b05bf4",
      "incomplete_value": true,
      "site": "00b05bf4",
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
      "definition_site": "00b05bb0",
      "incomplete_value": true,
      "site": "00b05bb0",
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
      "definition_site": "00b05bfc",
      "incomplete_value": false,
      "site": "00b05c04",
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
            "const:f8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05bb8",
      "incomplete_value": false,
      "site": "00b05bc0",
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
            "const:eff:8"
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
      "00b05bf0",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05bfc",
      "PARAM",
      [
        "storage",
        "002a4eff",
        null,
        "string"
      ]
    ],
    [
      "00b05c0c",
      "WRITE",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05bf0",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05bfc",
      "PARAM",
      [
        "storage",
        "002a4f8a",
        null,
        "string"
      ]
    ],
    [
      "00b05c0c",
      "WRITE",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b9c.md#insn-00b05bc0) · [`00b05bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b9c.md#insn-00b05bc8) · [`00b05bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05b9c.md#insn-00b05bac)
- 新版 [`00b05c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05be0.md#insn-00b05c04) · [`00b05c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05be0.md#insn-00b05c0c) · [`00b05bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05be0.md#insn-00b05bf0)

~~~diff
- 00b05bc0 ["INT_ADD", "register:40f0:8", ["const:b05bc0:8", "const:4:8"]]
- 00b05bc0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b05c04 ["INT_ADD", "register:40f0:8", ["const:b05c04:8", "const:4:8"]]
+ 00b05c04 ["CALL", null, ["callee:00bde090:8"]]
- 00b05bc0 bytes 20610394
+ 00b05c04 bytes 23610394
- 00b05bc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e08:8"]]
- 00b05bc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05c0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b05c0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05bc8 bytes 600607f9
+ 00b05c0c bytes 602607f9
- 00b05bac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e08:8"]]
- 00b05bac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05bf0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b05bf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05bac bytes 680647f9
+ 00b05bf0 bytes 682647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-998b8a188080e4480b4caa8803ca373d"></a>

### [`00b05bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05bdc.md) → [`00b05c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c20.md) _ZN8firebase7options10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b05c50",
      "incomplete_value": true,
      "site": "00b05c50",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05c0c",
      "incomplete_value": true,
      "site": "00b05c0c",
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
            "const:e08:8"
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
      "definition_site": "00b05c34",
      "incomplete_value": true,
      "site": "00b05c34",
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
      "definition_site": "00b05bf0",
      "incomplete_value": true,
      "site": "00b05bf0",
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
      "definition_site": "00b05c40",
      "incomplete_value": false,
      "site": "00b05c48",
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
            "const:f8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05bfc",
      "incomplete_value": false,
      "site": "00b05c04",
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
            "const:eff:8"
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
      "00b05c30",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05c40",
      "PARAM",
      [
        "storage",
        "002a4eff",
        null,
        "string"
      ]
    ],
    [
      "00b05c50",
      "WRITE",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05c30",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05c40",
      "PARAM",
      [
        "storage",
        "002a4f8a",
        null,
        "string"
      ]
    ],
    [
      "00b05c50",
      "WRITE",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05bdc.md#insn-00b05c04) · [`00b05c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05bdc.md#insn-00b05c0c) · [`00b05bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05bdc.md#insn-00b05bec)
- 新版 [`00b05c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c20.md#insn-00b05c48) · [`00b05c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c20.md#insn-00b05c50) · [`00b05c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c20.md#insn-00b05c30)

~~~diff
- 00b05c04 ["INT_ADD", "register:40f0:8", ["const:b05c04:8", "const:4:8"]]
- 00b05c04 ["CALL", null, ["callee:00bde090:8"]]
+ 00b05c48 ["INT_ADD", "register:40f0:8", ["const:b05c48:8", "const:4:8"]]
+ 00b05c48 ["CALL", null, ["callee:00bde090:8"]]
- 00b05c04 bytes 0f610394
+ 00b05c48 bytes 12610394
- 00b05c0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e08:8"]]
- 00b05c0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05c50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b05c50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05c0c bytes 600607f9
+ 00b05c50 bytes 602607f9
- 00b05bec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e08:8"]]
- 00b05bec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05c30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b05c30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05bec bytes 680647f9
+ 00b05c30 bytes 682647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e40b1a76a9f6019c4755afb4fae69d94"></a>

### [`00b05c20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05c20.md) → [`00b05c64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c64.md) _ZN8firebase7options10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b05c94",
      "incomplete_value": true,
      "site": "00b05c94",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05c50",
      "incomplete_value": true,
      "site": "00b05c50",
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
            "const:e08:8"
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
      "definition_site": "00b05c78",
      "incomplete_value": true,
      "site": "00b05c78",
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
      "definition_site": "00b05c34",
      "incomplete_value": true,
      "site": "00b05c34",
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
      "definition_site": "00b05c80",
      "incomplete_value": false,
      "site": "00b05c8c",
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
            "const:f8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05c3c",
      "incomplete_value": false,
      "site": "00b05c48",
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
            "const:eff:8"
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
      "00b05c74",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05c80",
      "PARAM",
      [
        "storage",
        "002a4eff",
        null,
        "string"
      ]
    ],
    [
      "00b05c94",
      "WRITE",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05c74",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05c80",
      "PARAM",
      [
        "storage",
        "002a4f8a",
        null,
        "string"
      ]
    ],
    [
      "00b05c94",
      "WRITE",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05c20.md#insn-00b05c48) · [`00b05c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05c20.md#insn-00b05c50) · [`00b05c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05c20.md#insn-00b05c30)
- 新版 [`00b05c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c64.md#insn-00b05c8c) · [`00b05c94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c64.md#insn-00b05c94) · [`00b05c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05c64.md#insn-00b05c74)

~~~diff
- 00b05c48 ["INT_ADD", "register:40f0:8", ["const:b05c48:8", "const:4:8"]]
- 00b05c48 ["CALL", null, ["callee:00bde090:8"]]
+ 00b05c8c ["INT_ADD", "register:40f0:8", ["const:b05c8c:8", "const:4:8"]]
+ 00b05c8c ["CALL", null, ["callee:00bde090:8"]]
- 00b05c48 bytes fe600394
+ 00b05c8c bytes 01610394
- 00b05c50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e08:8"]]
- 00b05c50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05c94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b05c94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05c50 bytes 600607f9
+ 00b05c94 bytes 602607f9
- 00b05c30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e08:8"]]
- 00b05c30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05c74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e48:8"]]
+ 00b05c74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05c30 bytes 680647f9
+ 00b05c74 bytes 682647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5430936a18ab796e90d68ec8ee03df3"></a>

### [`00b05c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05c70.md) → [`00b05cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05cb4.md) _ZN8firebase7options15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b05d0c",
      "incomplete_value": true,
      "site": "00b05d0c",
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
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05cc8",
      "incomplete_value": true,
      "site": "00b05cc8",
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
            "const:e10:8"
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
      "definition_site": "00b05ce8",
      "incomplete_value": true,
      "site": "00b05cf4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05ca4",
      "incomplete_value": true,
      "site": "00b05cb0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
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
      "00b05cc8",
      "READ",
      [
        "storage",
        "010a0e10",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05ce8",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05d0c",
      "WRITE",
      [
        "storage",
        "010a0e10",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b05cc8",
      "READ",
      [
        "storage",
        "010a0e50",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05ce8",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05d0c",
      "WRITE",
      [
        "storage",
        "010a0e50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05c70.md#insn-00b05c84) · [`00b05cb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05c70.md#insn-00b05cb0) · [`00b05cc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05c70.md#insn-00b05cc8)
- 新版 [`00b05cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05cb4.md#insn-00b05cc8) · [`00b05cf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05cb4.md#insn-00b05cf4) · [`00b05d0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05cb4.md#insn-00b05d0c)

~~~diff
- 00b05c84 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e10:8"]]
- 00b05c84 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b05c84 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b05cc8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e50:8"]]
+ 00b05cc8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b05cc8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b05c84 bytes a8427839
+ 00b05cc8 bytes a8427939
- 00b05cb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b05cb0 ["INT_ADD", "register:40f0:8", ["const:b05cb0:8", "const:4:8"]]
- 00b05cb0 ["CALLIND", null, ["register:0:8"]]
+ 00b05cf4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b05cf4 ["INT_ADD", "register:40f0:8", ["const:b05cf4:8", "const:4:8"]]
+ 00b05cf4 ["CALLIND", null, ["register:0:8"]]
- 00b05cb0 bytes 00013fd6
+ 00b05cf4 bytes 00013fd6
- 00b05cc8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b05cc8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e10:8"]]
- 00b05cc8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b05d0c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b05d0c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e50:8"]]
+ 00b05d0c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b05cc8 bytes a0423839
+ 00b05d0c bytes a0423939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-726346477d9489125d9a483dc4895738"></a>

### [`00b05cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05cdc.md) → [`00b05d20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d20.md) _ZN8firebase7options12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b05d5c",
      "incomplete_value": true,
      "site": "00b05d5c",
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
            "const:e50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05d18",
      "incomplete_value": true,
      "site": "00b05d18",
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
            "const:e10:8"
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
      "definition_site": "00b05d7c",
      "incomplete_value": true,
      "site": "00b05d7c",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05d38",
      "incomplete_value": true,
      "site": "00b05d38",
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
            "const:e08:8"
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
      "definition_site": "00b05d38",
      "incomplete_value": true,
      "site": "00b05d38",
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
      "definition_site": "00b05cf4",
      "incomplete_value": true,
      "site": "00b05cf4",
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
      "00b05d34",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05d40",
      "READ",
      [
        "storage",
        "010a0e10",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05d5c",
      "WRITE",
      [
        "storage",
        "010a0e10",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b05d34",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05d40",
      "READ",
      [
        "storage",
        "010a0e50",
        null,
        "undefined1"
      ]
    ],
    [
      "00b05d5c",
      "WRITE",
      [
        "storage",
        "010a0e50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05cdc.md#insn-00b05d18) · [`00b05d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05cdc.md#insn-00b05d38) · [`00b05cf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05cdc.md#insn-00b05cf0)
- 新版 [`00b05d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d20.md#insn-00b05d5c) · [`00b05d7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d20.md#insn-00b05d7c) · [`00b05d34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d20.md#insn-00b05d34)

~~~diff
- 00b05d18 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b05d18 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b05d18 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e10:8"]]
- 00b05d18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b05d5c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b05d5c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b05d5c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e50:8"]]
+ 00b05d5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b05d18 bytes bf423839
+ 00b05d5c bytes bf423939
- 00b05d38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e08:8"]]
- 00b05d38 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b05d38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b05d7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e48:8"]]
+ 00b05d7c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b05d7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b05d38 bytes 9f0607f9
+ 00b05d7c bytes 9f2607f9
- 00b05cf0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e08:8"]]
- 00b05cf0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05d34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e48:8"]]
+ 00b05d34 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05cf0 bytes 810647f9
+ 00b05d34 bytes 812647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ed8589c3bed41b55a29ed8bf9e1d68f"></a>

### [`00b05d4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05d4c.md) → [`00b05d90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d90.md) _ZN8firebase7options14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b05dd0",
      "incomplete_value": true,
      "site": "00b05dd0",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05d8c",
      "incomplete_value": true,
      "site": "00b05d8c",
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
            "const:e08:8"
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
      "definition_site": "00b05dac",
      "incomplete_value": true,
      "site": "00b05dac",
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
      "definition_site": "00b05d68",
      "incomplete_value": true,
      "site": "00b05d68",
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
      "definition_site": "00b05db4",
      "incomplete_value": false,
      "site": "00b05dc8",
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
            "const:f8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05d70",
      "incomplete_value": false,
      "site": "00b05d84",
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
            "const:eff:8"
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
      "00b05da4",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05db4",
      "PARAM",
      [
        "storage",
        "002a4eff",
        null,
        "string"
      ]
    ],
    [
      "00b05dd0",
      "WRITE",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05da4",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05db4",
      "PARAM",
      [
        "storage",
        "002a4f8a",
        null,
        "string"
      ]
    ],
    [
      "00b05dd0",
      "WRITE",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05d4c.md#insn-00b05d84) · [`00b05d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05d4c.md#insn-00b05d8c) · [`00b05d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05d4c.md#insn-00b05d60)
- 新版 [`00b05dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d90.md#insn-00b05dc8) · [`00b05dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d90.md#insn-00b05dd0) · [`00b05da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05d90.md#insn-00b05da4)

~~~diff
- 00b05d84 ["INT_ADD", "register:40f0:8", ["const:b05d84:8", "const:4:8"]]
- 00b05d84 ["CALL", null, ["callee:00bde090:8"]]
+ 00b05dc8 ["INT_ADD", "register:40f0:8", ["const:b05dc8:8", "const:4:8"]]
+ 00b05dc8 ["CALL", null, ["callee:00bde090:8"]]
- 00b05d84 bytes af600394
+ 00b05dc8 bytes b2600394
- 00b05d8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e08:8"]]
- 00b05d8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05dd0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e48:8"]]
+ 00b05dd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05d8c bytes 800607f9
+ 00b05dd0 bytes 802607f9
- 00b05d60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e08:8"]]
- 00b05d60 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05da4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e48:8"]]
+ 00b05da4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05d60 bytes 810647f9
+ 00b05da4 bytes 812647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4fb347d057f351333d4d0cb0da65ec6"></a>

### [`00b05dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05dbc.md) → [`00b05e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e00.md) _ZN8firebase7options11GetMethodIdENS0_6MethodE

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
      "definition_site": "00b05e1c",
      "incomplete_value": false,
      "site": "00b05e20",
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
      "definition_site": "00b05dd8",
      "incomplete_value": false,
      "site": "00b05ddc",
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
      "definition_site": "00b05e2c",
      "incomplete_value": true,
      "site": "00b05e38",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b05de8",
      "incomplete_value": true,
      "site": "00b05df4",
      "value": [
        "LOAD",
        "8",
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
      "00b05e1c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b05e2c",
      "DATA",
      [
        "storage",
        "010a0e18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05e1c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b05e2c",
      "DATA",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05dbc.md#insn-00b05ddc) · [`00b05dd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05dbc.md#insn-00b05dd8) · [`00b05de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05dbc.md#insn-00b05de4)
- 新版 [`00b05e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e00.md#insn-00b05e20) · [`00b05e1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e00.md#insn-00b05e1c) · [`00b05e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e00.md#insn-00b05e28)

~~~diff
- 00b05ddc ["INT_ADD", "register:40f0:8", ["const:b05ddc:8", "const:4:8"]]
- 00b05ddc ["CALL", null, ["callee:00bde180:8"]]
+ 00b05e20 ["INT_ADD", "register:40f0:8", ["const:b05e20:8", "const:4:8"]]
+ 00b05e20 ["CALL", null, ["callee:00bde180:8"]]
- 00b05ddc bytes d5600394
+ 00b05e20 bytes d8600394
- 00b05dd8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b05dd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b05dd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b05dd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b05e1c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b05e1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05e1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05e1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b05dd8 bytes 00501791
+ 00b05e1c bytes 001c1591
- 00b05de4 ["COPY", "tmp:0:8", ["const:e18:8"]]
- 00b05de4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b05de4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b05de4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b05e28 ["COPY", "tmp:0:8", ["const:e58:8"]]
+ 00b05e28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05e28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05e28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b05de4 bytes 08613891
+ 00b05e28 bytes 08613991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d2ae44a6c002a8e427ce7741eb1eced"></a>

### [`00b05df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05df8.md) → [`00b05e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e3c.md) _ZN8firebase7options13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b05e7c",
      "incomplete_value": true,
      "site": "00b05e7c",
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
            "const:e48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05e38",
      "incomplete_value": true,
      "site": "00b05e38",
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
            "const:e08:8"
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
      "definition_site": "00b05e58",
      "incomplete_value": true,
      "site": "00b05e58",
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
      "definition_site": "00b05e14",
      "incomplete_value": true,
      "site": "00b05e14",
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
      "definition_site": "00b05e60",
      "incomplete_value": false,
      "site": "00b05e74",
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
            "const:f8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05e1c",
      "incomplete_value": false,
      "site": "00b05e30",
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
            "const:eff:8"
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
      "00b05e50",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05e60",
      "PARAM",
      [
        "storage",
        "002a4eff",
        null,
        "string"
      ]
    ],
    [
      "00b05e7c",
      "WRITE",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05e50",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05e60",
      "PARAM",
      [
        "storage",
        "002a4f8a",
        null,
        "string"
      ]
    ],
    [
      "00b05e7c",
      "WRITE",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05df8.md#insn-00b05e30) · [`00b05e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05df8.md#insn-00b05e38) · [`00b05e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05df8.md#insn-00b05e0c)
- 新版 [`00b05e74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e3c.md#insn-00b05e74) · [`00b05e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e3c.md#insn-00b05e7c) · [`00b05e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05e3c.md#insn-00b05e50)

~~~diff
- 00b05e30 ["INT_ADD", "register:40f0:8", ["const:b05e30:8", "const:4:8"]]
- 00b05e30 ["CALL", null, ["callee:00bde090:8"]]
+ 00b05e74 ["INT_ADD", "register:40f0:8", ["const:b05e74:8", "const:4:8"]]
+ 00b05e74 ["CALL", null, ["callee:00bde090:8"]]
- 00b05e30 bytes 84600394
+ 00b05e74 bytes 87600394
- 00b05e38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e08:8"]]
- 00b05e38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05e7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e48:8"]]
+ 00b05e7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05e38 bytes 800607f9
+ 00b05e7c bytes 802607f9
- 00b05e0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e08:8"]]
- 00b05e0c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05e50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e48:8"]]
+ 00b05e50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05e0c bytes 810647f9
+ 00b05e50 bytes 812647f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f907d7bb3a2b972d8e18a7e362d19c59"></a>

### [`00b05e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05e68.md) → [`00b05eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05eac.md) _ZN8firebase7options10GetFieldIdENS0_5FieldE

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
      "definition_site": "00b05ec8",
      "incomplete_value": false,
      "site": "00b05ecc",
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
      "definition_site": "00b05e84",
      "incomplete_value": false,
      "site": "00b05e88",
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
      "definition_site": "00b05ed8",
      "incomplete_value": true,
      "site": "00b05ee4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b05e94",
      "incomplete_value": true,
      "site": "00b05ea0",
      "value": [
        "LOAD",
        "8",
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
      "00b05ec8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b05ed8",
      "DATA",
      [
        "storage",
        "010a0e50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b05ec8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b05ed8",
      "DATA",
      [
        "storage",
        "010a0e90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05e68.md#insn-00b05e88) · [`00b05e84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05e68.md#insn-00b05e84) · [`00b05e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05e68.md#insn-00b05e90)
- 新版 [`00b05ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05eac.md#insn-00b05ecc) · [`00b05ec8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05eac.md#insn-00b05ec8) · [`00b05ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05eac.md#insn-00b05ed4)

~~~diff
- 00b05e88 ["INT_ADD", "register:40f0:8", ["const:b05e88:8", "const:4:8"]]
- 00b05e88 ["CALL", null, ["callee:00bde180:8"]]
+ 00b05ecc ["INT_ADD", "register:40f0:8", ["const:b05ecc:8", "const:4:8"]]
+ 00b05ecc ["CALL", null, ["callee:00bde180:8"]]
- 00b05e88 bytes aa600394
+ 00b05ecc bytes ad600394
- 00b05e84 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b05e84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b05e84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b05e84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b05ec8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b05ec8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05ec8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b05ec8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b05e84 bytes 00fc1991
+ 00b05ec8 bytes 00c81791
- 00b05e90 ["COPY", "tmp:0:8", ["const:e50:8"]]
- 00b05e90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b05e90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b05e90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b05ed4 ["COPY", "tmp:0:8", ["const:e90:8"]]
+ 00b05ed4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05ed4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b05ed4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b05e90 bytes 08413991
+ 00b05ed4 bytes 08413a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9af2c9c70048b6d6faf81efae1aa0279"></a>

### [`00b05ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ea4.md) → [`00b05ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ee8.md) _ZN8firebase17version_registrar19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEE

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
      "definition_site": "00b05f14",
      "incomplete_value": true,
      "site": "00b05f14",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05ed0",
      "incomplete_value": true,
      "site": "00b05ed0",
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
            "const:e58:8"
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
      "definition_site": "00b05efc",
      "incomplete_value": true,
      "site": "00b05efc",
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
      "definition_site": "00b05eb8",
      "incomplete_value": true,
      "site": "00b05eb8",
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
      "definition_site": "00b05f08",
      "incomplete_value": false,
      "site": "00b05f0c",
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
            "const:376:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05ec4",
      "incomplete_value": false,
      "site": "00b05ec8",
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
            "const:40a:8"
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
      "00b05ef8",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05f08",
      "PARAM",
      [
        "storage",
        "002af40a",
        null,
        "string"
      ]
    ],
    [
      "00b05f14",
      "WRITE",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05ef8",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05f08",
      "PARAM",
      [
        "storage",
        "002af376",
        null,
        "string"
      ]
    ],
    [
      "00b05f14",
      "WRITE",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05ec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ea4.md#insn-00b05ec8) · [`00b05ed0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ea4.md#insn-00b05ed0) · [`00b05eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ea4.md#insn-00b05eb4)
- 新版 [`00b05f0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ee8.md#insn-00b05f0c) · [`00b05f14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ee8.md#insn-00b05f14) · [`00b05ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ee8.md#insn-00b05ef8)

~~~diff
- 00b05ec8 ["INT_ADD", "register:40f0:8", ["const:b05ec8:8", "const:4:8"]]
- 00b05ec8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b05f0c ["INT_ADD", "register:40f0:8", ["const:b05f0c:8", "const:4:8"]]
+ 00b05f0c ["CALL", null, ["callee:00bde090:8"]]
- 00b05ec8 bytes 5e600394
+ 00b05f0c bytes 61600394
- 00b05ed0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
- 00b05ed0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05f14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e98:8"]]
+ 00b05f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05ed0 bytes 602e07f9
+ 00b05f14 bytes 604e07f9
- 00b05eb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
- 00b05eb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05ef8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e98:8"]]
+ 00b05ef8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05eb4 bytes 682e47f9
+ 00b05ef8 bytes 684e47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc63d2a3c466f220c0bc828fc436d6de"></a>

### [`00b05ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ee4.md) → [`00b05f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f28.md) _ZN8firebase17version_registrar19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEE

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
      "definition_site": "00b05f54",
      "incomplete_value": true,
      "site": "00b05f54",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f10",
      "incomplete_value": true,
      "site": "00b05f10",
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
            "const:e58:8"
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
      "definition_site": "00b05f3c",
      "incomplete_value": true,
      "site": "00b05f3c",
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
      "definition_site": "00b05ef8",
      "incomplete_value": true,
      "site": "00b05ef8",
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
      "definition_site": "00b05f44",
      "incomplete_value": false,
      "site": "00b05f4c",
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
            "const:376:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f00",
      "incomplete_value": false,
      "site": "00b05f08",
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
            "const:40a:8"
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
      "00b05f38",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05f44",
      "PARAM",
      [
        "storage",
        "002af40a",
        null,
        "string"
      ]
    ],
    [
      "00b05f54",
      "WRITE",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05f38",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05f44",
      "PARAM",
      [
        "storage",
        "002af376",
        null,
        "string"
      ]
    ],
    [
      "00b05f54",
      "WRITE",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ee4.md#insn-00b05f08) · [`00b05f10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ee4.md#insn-00b05f10) · [`00b05ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05ee4.md#insn-00b05ef4)
- 新版 [`00b05f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f28.md#insn-00b05f4c) · [`00b05f54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f28.md#insn-00b05f54) · [`00b05f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f28.md#insn-00b05f38)

~~~diff
- 00b05f08 ["INT_ADD", "register:40f0:8", ["const:b05f08:8", "const:4:8"]]
- 00b05f08 ["CALL", null, ["callee:00bde090:8"]]
+ 00b05f4c ["INT_ADD", "register:40f0:8", ["const:b05f4c:8", "const:4:8"]]
+ 00b05f4c ["CALL", null, ["callee:00bde090:8"]]
- 00b05f08 bytes 4e600394
+ 00b05f4c bytes 51600394
- 00b05f10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
- 00b05f10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05f54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e98:8"]]
+ 00b05f54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05f10 bytes 602e07f9
+ 00b05f54 bytes 604e07f9
- 00b05ef4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
- 00b05ef4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05f38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e98:8"]]
+ 00b05f38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05ef4 bytes 682e47f9
+ 00b05f38 bytes 684e47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35146fda2f0a4ad6b727d4809f2a8059"></a>

### [`00b05f24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f24.md) → [`00b05f68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f68.md) _ZN8firebase17version_registrar10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b05f98",
      "incomplete_value": true,
      "site": "00b05f98",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f54",
      "incomplete_value": true,
      "site": "00b05f54",
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
            "const:e58:8"
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
      "definition_site": "00b05f7c",
      "incomplete_value": true,
      "site": "00b05f7c",
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
      "definition_site": "00b05f38",
      "incomplete_value": true,
      "site": "00b05f38",
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
      "definition_site": "00b05f88",
      "incomplete_value": false,
      "site": "00b05f90",
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
            "const:376:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f44",
      "incomplete_value": false,
      "site": "00b05f4c",
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
            "const:40a:8"
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
      "00b05f78",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05f88",
      "PARAM",
      [
        "storage",
        "002af40a",
        null,
        "string"
      ]
    ],
    [
      "00b05f98",
      "WRITE",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05f78",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05f88",
      "PARAM",
      [
        "storage",
        "002af376",
        null,
        "string"
      ]
    ],
    [
      "00b05f98",
      "WRITE",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f24.md#insn-00b05f4c) · [`00b05f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f24.md#insn-00b05f54) · [`00b05f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f24.md#insn-00b05f34)
- 新版 [`00b05f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f68.md#insn-00b05f90) · [`00b05f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f68.md#insn-00b05f98) · [`00b05f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05f68.md#insn-00b05f78)

~~~diff
- 00b05f4c ["INT_ADD", "register:40f0:8", ["const:b05f4c:8", "const:4:8"]]
- 00b05f4c ["CALL", null, ["callee:00bde090:8"]]
+ 00b05f90 ["INT_ADD", "register:40f0:8", ["const:b05f90:8", "const:4:8"]]
+ 00b05f90 ["CALL", null, ["callee:00bde090:8"]]
- 00b05f4c bytes 3d600394
+ 00b05f90 bytes 40600394
- 00b05f54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
- 00b05f54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05f98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e98:8"]]
+ 00b05f98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05f54 bytes 602e07f9
+ 00b05f98 bytes 604e07f9
- 00b05f34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
- 00b05f34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05f78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e98:8"]]
+ 00b05f78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05f34 bytes 682e47f9
+ 00b05f78 bytes 684e47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f83e019398656fa67f82c0a9185e0a1"></a>

### [`00b05f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f68.md) → [`00b05fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05fac.md) _ZN8firebase17version_registrar10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b05fdc",
      "incomplete_value": true,
      "site": "00b05fdc",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f98",
      "incomplete_value": true,
      "site": "00b05f98",
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
            "const:e58:8"
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
      "definition_site": "00b05fc0",
      "incomplete_value": true,
      "site": "00b05fc0",
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
      "definition_site": "00b05f7c",
      "incomplete_value": true,
      "site": "00b05f7c",
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
      "definition_site": "00b05fc8",
      "incomplete_value": false,
      "site": "00b05fd4",
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
            "const:376:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05f84",
      "incomplete_value": false,
      "site": "00b05f90",
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
            "const:40a:8"
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
      "00b05fbc",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05fc8",
      "PARAM",
      [
        "storage",
        "002af40a",
        null,
        "string"
      ]
    ],
    [
      "00b05fdc",
      "WRITE",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b05fbc",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b05fc8",
      "PARAM",
      [
        "storage",
        "002af376",
        null,
        "string"
      ]
    ],
    [
      "00b05fdc",
      "WRITE",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f68.md#insn-00b05f90) · [`00b05f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f68.md#insn-00b05f98) · [`00b05f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05f68.md#insn-00b05f78)
- 新版 [`00b05fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05fac.md#insn-00b05fd4) · [`00b05fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05fac.md#insn-00b05fdc) · [`00b05fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05fac.md#insn-00b05fbc)

~~~diff
- 00b05f90 ["INT_ADD", "register:40f0:8", ["const:b05f90:8", "const:4:8"]]
- 00b05f90 ["CALL", null, ["callee:00bde090:8"]]
+ 00b05fd4 ["INT_ADD", "register:40f0:8", ["const:b05fd4:8", "const:4:8"]]
+ 00b05fd4 ["CALL", null, ["callee:00bde090:8"]]
- 00b05f90 bytes 2c600394
+ 00b05fd4 bytes 2f600394
- 00b05f98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
- 00b05f98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b05fdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e98:8"]]
+ 00b05fdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b05f98 bytes 602e07f9
+ 00b05fdc bytes 604e07f9
- 00b05f78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e58:8"]]
- 00b05f78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b05fbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e98:8"]]
+ 00b05fbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b05f78 bytes 682e47f9
+ 00b05fbc bytes 684e47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd2d81bb8d702ff7d777280ea92e765c"></a>

### [`00b05fb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05fb8.md) → [`00b05ffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ffc.md) _ZN8firebase17version_registrar15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b06054",
      "incomplete_value": true,
      "site": "00b06054",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06010",
      "incomplete_value": true,
      "site": "00b06010",
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
            "const:e60:8"
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
      "definition_site": "00b06030",
      "incomplete_value": true,
      "site": "00b0603c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b05fec",
      "incomplete_value": true,
      "site": "00b05ff8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
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
      "00b06010",
      "READ",
      [
        "storage",
        "010a0e60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b06030",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b06054",
      "WRITE",
      [
        "storage",
        "010a0e60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b06010",
      "READ",
      [
        "storage",
        "010a0ea0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b06030",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b06054",
      "WRITE",
      [
        "storage",
        "010a0ea0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b05fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05fb8.md#insn-00b05fcc) · [`00b05ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05fb8.md#insn-00b05ff8) · [`00b06010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b05/00b05fb8.md#insn-00b06010)
- 新版 [`00b06010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ffc.md#insn-00b06010) · [`00b0603c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ffc.md#insn-00b0603c) · [`00b06054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b05/00b05ffc.md#insn-00b06054)

~~~diff
- 00b05fcc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e60:8"]]
- 00b05fcc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b05fcc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b06010 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ea0:8"]]
+ 00b06010 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b06010 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b05fcc bytes a8827939
+ 00b06010 bytes a8827a39
- 00b05ff8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b05ff8 ["INT_ADD", "register:40f0:8", ["const:b05ff8:8", "const:4:8"]]
- 00b05ff8 ["CALLIND", null, ["register:0:8"]]
+ 00b0603c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b0603c ["INT_ADD", "register:40f0:8", ["const:b0603c:8", "const:4:8"]]
+ 00b0603c ["CALLIND", null, ["register:0:8"]]
- 00b05ff8 bytes 00013fd6
+ 00b0603c bytes 00013fd6
- 00b06010 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b06010 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e60:8"]]
- 00b06010 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b06054 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b06054 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ea0:8"]]
+ 00b06054 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b06010 bytes a0823939
+ 00b06054 bytes a0823a39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e8d60657ebbc9b28ff946f0874dc527"></a>

### [`00b06024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06024.md) → [`00b06068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06068.md) _ZN8firebase17version_registrar12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b060a4",
      "incomplete_value": true,
      "site": "00b060a4",
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
            "const:ea0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06060",
      "incomplete_value": true,
      "site": "00b06060",
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
            "const:e60:8"
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
      "definition_site": "00b060c4",
      "incomplete_value": true,
      "site": "00b060c4",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06080",
      "incomplete_value": true,
      "site": "00b06080",
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
            "const:e58:8"
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
      "definition_site": "00b06080",
      "incomplete_value": true,
      "site": "00b06080",
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
      "definition_site": "00b0603c",
      "incomplete_value": true,
      "site": "00b0603c",
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
      "00b0607c",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b06088",
      "READ",
      [
        "storage",
        "010a0e60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b060a4",
      "WRITE",
      [
        "storage",
        "010a0e60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b0607c",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b06088",
      "READ",
      [
        "storage",
        "010a0ea0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b060a4",
      "WRITE",
      [
        "storage",
        "010a0ea0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06024.md#insn-00b06038) · [`00b06060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06024.md#insn-00b06060) · [`00b0607c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06024.md#insn-00b0607c)
- 新版 [`00b0607c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06068.md#insn-00b0607c) · [`00b060a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06068.md#insn-00b060a4) · [`00b060c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06068.md#insn-00b060c0)

~~~diff
- 00b06038 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e58:8"]]
- 00b06038 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b0607c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e98:8"]]
+ 00b0607c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b06038 bytes 812e47f9
+ 00b0607c bytes 814e47f9
- 00b06060 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b06060 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b06060 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e60:8"]]
- 00b06060 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b060a4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b060a4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b060a4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ea0:8"]]
+ 00b060a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b06060 bytes bf823939
+ 00b060a4 bytes bf823a39
- 00b0607c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b0607c ["INT_ADD", "register:40f0:8", ["const:b0607c:8", "const:4:8"]]
- 00b0607c ["CALLIND", null, ["register:0:8"]]
+ 00b060c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b060c0 ["INT_ADD", "register:40f0:8", ["const:b060c0:8", "const:4:8"]]
+ 00b060c0 ["CALLIND", null, ["register:0:8"]]
- 00b0607c bytes 00013fd6
+ 00b060c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d319c8723e77e1d83c2027e58fbd1bca"></a>

### [`00b06094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06094.md) → [`00b060d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b060d8.md) _ZN8firebase17version_registrar14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b06118",
      "incomplete_value": true,
      "site": "00b06118",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b060d4",
      "incomplete_value": true,
      "site": "00b060d4",
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
            "const:e58:8"
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
      "definition_site": "00b060f4",
      "incomplete_value": true,
      "site": "00b060f4",
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
      "definition_site": "00b060b0",
      "incomplete_value": true,
      "site": "00b060b0",
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
      "definition_site": "00b060fc",
      "incomplete_value": false,
      "site": "00b06110",
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
            "const:376:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b060b8",
      "incomplete_value": false,
      "site": "00b060cc",
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
            "const:40a:8"
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
      "00b060ec",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b060fc",
      "PARAM",
      [
        "storage",
        "002af40a",
        null,
        "string"
      ]
    ],
    [
      "00b06118",
      "WRITE",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b060ec",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b060fc",
      "PARAM",
      [
        "storage",
        "002af376",
        null,
        "string"
      ]
    ],
    [
      "00b06118",
      "WRITE",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b060cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06094.md#insn-00b060cc) · [`00b060d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06094.md#insn-00b060d4) · [`00b060a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06094.md#insn-00b060a8)
- 新版 [`00b06110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b060d8.md#insn-00b06110) · [`00b06118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b060d8.md#insn-00b06118) · [`00b060ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b060d8.md#insn-00b060ec)

~~~diff
- 00b060cc ["INT_ADD", "register:40f0:8", ["const:b060cc:8", "const:4:8"]]
- 00b060cc ["CALL", null, ["callee:00bde090:8"]]
+ 00b06110 ["INT_ADD", "register:40f0:8", ["const:b06110:8", "const:4:8"]]
+ 00b06110 ["CALL", null, ["callee:00bde090:8"]]
- 00b060cc bytes dd5f0394
+ 00b06110 bytes e05f0394
- 00b060d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e58:8"]]
- 00b060d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b06118 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e98:8"]]
+ 00b06118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b060d4 bytes 802e07f9
+ 00b06118 bytes 804e07f9
- 00b060a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e58:8"]]
- 00b060a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b060ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e98:8"]]
+ 00b060ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b060a8 bytes 812e47f9
+ 00b060ec bytes 814e47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-da6b59dd139499c519bc8e5d5df85b96"></a>

### [`00b06104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06104.md) → [`00b06148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06148.md) _ZN8firebase17version_registrar11GetMethodIdENS0_6MethodE

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
      "definition_site": "00b06164",
      "incomplete_value": false,
      "site": "00b06168",
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
      "definition_site": "00b06120",
      "incomplete_value": false,
      "site": "00b06124",
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
      "definition_site": "00b06174",
      "incomplete_value": true,
      "site": "00b06180",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b06130",
      "incomplete_value": true,
      "site": "00b0613c",
      "value": [
        "LOAD",
        "8",
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
      "00b06164",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b06174",
      "DATA",
      [
        "storage",
        "010a0e68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b06164",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b06174",
      "DATA",
      [
        "storage",
        "010a0ea8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06104.md#insn-00b06124) · [`00b06120`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06104.md#insn-00b06120) · [`00b0612c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06104.md#insn-00b0612c)
- 新版 [`00b06168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06148.md#insn-00b06168) · [`00b06164`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06148.md#insn-00b06164) · [`00b06170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06148.md#insn-00b06170)

~~~diff
- 00b06124 ["INT_ADD", "register:40f0:8", ["const:b06124:8", "const:4:8"]]
- 00b06124 ["CALL", null, ["callee:00bde180:8"]]
+ 00b06168 ["INT_ADD", "register:40f0:8", ["const:b06168:8", "const:4:8"]]
+ 00b06168 ["CALL", null, ["callee:00bde180:8"]]
- 00b06124 bytes 03600394
+ 00b06168 bytes 06600394
- 00b06120 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b06120 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b06120 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b06120 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b06164 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b06164 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b06164 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b06164 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b06120 bytes 00501791
+ 00b06164 bytes 001c1591
- 00b0612c ["COPY", "tmp:0:8", ["const:e68:8"]]
- 00b0612c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b0612c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b0612c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b06170 ["COPY", "tmp:0:8", ["const:ea8:8"]]
+ 00b06170 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b06170 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b06170 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b0612c bytes 08a13991
+ 00b06170 bytes 08a13a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8cdbb2a780824071e5bb69d0696cd200"></a>

### [`00b06140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06140.md) → [`00b06184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06184.md) _ZN8firebase17version_registrar13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b061c4",
      "incomplete_value": true,
      "site": "00b061c4",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06180",
      "incomplete_value": true,
      "site": "00b06180",
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
            "const:e58:8"
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
      "definition_site": "00b061a0",
      "incomplete_value": true,
      "site": "00b061a0",
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
      "definition_site": "00b0615c",
      "incomplete_value": true,
      "site": "00b0615c",
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
      "definition_site": "00b061a8",
      "incomplete_value": false,
      "site": "00b061bc",
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
            "const:376:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06164",
      "incomplete_value": false,
      "site": "00b06178",
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
            "const:40a:8"
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
      "00b06198",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b061a8",
      "PARAM",
      [
        "storage",
        "002af40a",
        null,
        "string"
      ]
    ],
    [
      "00b061c4",
      "WRITE",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b06198",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b061a8",
      "PARAM",
      [
        "storage",
        "002af376",
        null,
        "string"
      ]
    ],
    [
      "00b061c4",
      "WRITE",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06140.md#insn-00b06178) · [`00b06180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06140.md#insn-00b06180) · [`00b06154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06140.md#insn-00b06154)
- 新版 [`00b061bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06184.md#insn-00b061bc) · [`00b061c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06184.md#insn-00b061c4) · [`00b06198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06184.md#insn-00b06198)

~~~diff
- 00b06178 ["INT_ADD", "register:40f0:8", ["const:b06178:8", "const:4:8"]]
- 00b06178 ["CALL", null, ["callee:00bde090:8"]]
+ 00b061bc ["INT_ADD", "register:40f0:8", ["const:b061bc:8", "const:4:8"]]
+ 00b061bc ["CALL", null, ["callee:00bde090:8"]]
- 00b06178 bytes b25f0394
+ 00b061bc bytes b55f0394
- 00b06180 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e58:8"]]
- 00b06180 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b061c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e98:8"]]
+ 00b061c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b06180 bytes 802e07f9
+ 00b061c4 bytes 804e07f9
- 00b06154 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e58:8"]]
- 00b06154 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b06198 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e98:8"]]
+ 00b06198 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b06154 bytes 812e47f9
+ 00b06198 bytes 814e47f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3aac5c303bfb93a265b7ede16330e22"></a>

### [`00b061b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061b0.md) → [`00b061f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b061f4.md) _ZN8firebase17version_registrar10GetFieldIdENS0_5FieldE

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
      "definition_site": "00b06210",
      "incomplete_value": false,
      "site": "00b06214",
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
      "definition_site": "00b061cc",
      "incomplete_value": false,
      "site": "00b061d0",
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
      "definition_site": "00b06220",
      "incomplete_value": true,
      "site": "00b0622c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b061dc",
      "incomplete_value": true,
      "site": "00b061e8",
      "value": [
        "LOAD",
        "8",
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
      "00b06210",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b06220",
      "DATA",
      [
        "storage",
        "010a0e80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b06210",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b06220",
      "DATA",
      [
        "storage",
        "010a0ec0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b061d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061b0.md#insn-00b061d0) · [`00b061cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061b0.md#insn-00b061cc) · [`00b061d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061b0.md#insn-00b061d8)
- 新版 [`00b06214`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b061f4.md#insn-00b06214) · [`00b06210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b061f4.md#insn-00b06210) · [`00b0621c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b061f4.md#insn-00b0621c)

~~~diff
- 00b061d0 ["INT_ADD", "register:40f0:8", ["const:b061d0:8", "const:4:8"]]
- 00b061d0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b06214 ["INT_ADD", "register:40f0:8", ["const:b06214:8", "const:4:8"]]
+ 00b06214 ["CALL", null, ["callee:00bde180:8"]]
- 00b061d0 bytes d85f0394
+ 00b06214 bytes db5f0394
- 00b061cc ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b061cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b061cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b061cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b06210 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b06210 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b06210 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b06210 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b061cc bytes 00fc1991
+ 00b06210 bytes 00c81791
- 00b061d8 ["COPY", "tmp:0:8", ["const:e80:8"]]
- 00b061d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b061d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b061d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b0621c ["COPY", "tmp:0:8", ["const:ec0:8"]]
+ 00b0621c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0621c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b0621c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b061d8 bytes 08013a91
+ 00b0621c bytes 08013b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0687bb4528213df786a72a9cc8196a09"></a>

### [`00b061ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061ec.md) → [`00b06230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06230.md) _ZN8firebase10AppOptions11LoadDefaultEPS0_P7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdefc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdefc0.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b06390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md) [`00b06578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06578.md) [`00b06984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 1件 [`00bdf010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf010.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b063d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md) [`00b065bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b065bc.md) [`00b069c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.10% / 新版 98.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b06278",
      "incomplete_value": true,
      "site": "00b06288",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06234",
      "incomplete_value": true,
      "site": "00b06244",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e08:8"
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
      "definition_site": "00b0627c",
      "incomplete_value": true,
      "site": "00b06288",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06238",
      "incomplete_value": true,
      "site": "00b06244",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e18:8"
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
      "00b06278",
      "READ",
      [
        "storage",
        "010a0e08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0627c",
      "READ",
      [
        "storage",
        "010a0e18",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b06278",
      "READ",
      [
        "storage",
        "010a0e48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0627c",
      "READ",
      [
        "storage",
        "010a0e58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061ec.md#insn-00b06244) · [`00b06288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061ec.md#insn-00b06288) · [`00b06224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061ec.md#insn-00b06224)
- 新版 [`00b06288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06230.md#insn-00b06288) · [`00b062cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06230.md#insn-00b062cc) · [`00b06268`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06230.md#insn-00b06268)

~~~diff
- 00b06244 ["INT_ADD", "register:40f0:8", ["const:b06244:8", "const:4:8"]]
- 00b06244 ["CALL", null, ["callee:00bddd40:8"]]
+ 00b06288 ["INT_ADD", "register:40f0:8", ["const:b06288:8", "const:4:8"]]
+ 00b06288 ["CALL", null, ["callee:00bddd40:8"]]
- 00b06244 bytes ab5e0394
+ 00b06288 bytes ae5e0394
- 00b06288 ["INT_ADD", "register:40f0:8", ["const:b06288:8", "const:4:8"]]
- 00b06288 ["CALL", null, ["callee:00bde0e0:8"]]
+ 00b062cc ["INT_ADD", "register:40f0:8", ["const:b062cc:8", "const:4:8"]]
+ 00b062cc ["CALL", null, ["callee:00bde0e0:8"]]
- 00b06288 bytes 825f0394
+ 00b062cc bytes 855f0394
- 00b06224 ["INT_ADD", "register:40f0:8", ["const:b06224:8", "const:4:8"]]
- 00b06224 ["CALL", null, ["callee:00b063d4:8"]]
+ 00b06268 ["INT_ADD", "register:40f0:8", ["const:b06268:8", "const:4:8"]]
+ 00b06268 ["CALL", null, ["callee:00b063d4:8"]]
- 00b06224 bytes 5b000094
+ 00b06268 bytes 5b000094
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c931d72e6718111a915a1bba55ad4850"></a>

### [`00b06390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md) → [`00b063d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md) FUN_00b063d4

採用 · 移動量 `+0x44` · 根拠 `similar_code_order_and_calls` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 4件 [`00b061ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061ec.md) [`00b06be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06be8.md) [`00b06ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md) [`00b0817c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0817c.md) · 呼出先 5件 [`00b06984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md) [`00bddfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfd0.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md) [`00bdee00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee00.md)
- 新版 呼出元 4件 [`00b06230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06230.md) [`00b06c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06c2c.md) [`00b06d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md) [`00b081c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b081c0.md) · 呼出先 5件 [`00b069c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md) [`00bde020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde020.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md) [`00bdee50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 81.97% / 新版 81.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 4件, `store_condition` 4件, `store_destination` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b063f0",
      "incomplete_value": false,
      "site": "00b063f0",
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
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b063ac",
      "incomplete_value": false,
      "site": "00b063ac",
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
            "const:e88:8"
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
      "definition_site": "00b0643c",
      "incomplete_value": true,
      "site": "00b0643c",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b063f8",
      "incomplete_value": true,
      "site": "00b063f8",
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
            "const:d50:8"
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
      "definition_site": "00b06494",
      "incomplete_value": true,
      "site": "00b06494",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06450",
      "incomplete_value": true,
      "site": "00b06450",
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
            "const:db0:8"
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
      "00b063e8",
      "READ",
      [
        "storage",
        "010a0e88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b063f0",
      "WRITE",
      [
        "storage",
        "010a0e88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b06414",
      "READ",
      [
        "storage",
        "010a0d50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b063e8",
      "READ",
      [
        "storage",
        "010a0ec8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b063f0",
      "WRITE",
      [
        "storage",
        "010a0ec8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b06414",
      "READ",
      [
        "storage",
        "010a0d90",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b063ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md#insn-00b063ac) · [`00b063f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md#insn-00b063f0) · [`00b063f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md#insn-00b063f8)
- 新版 [`00b063f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md#insn-00b063f0) · [`00b06434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md#insn-00b06434) · [`00b0643c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md#insn-00b0643c)

~~~diff
- 00b063ac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e88:8"]]
- 00b063ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b063f0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ec8:8"]]
+ 00b063f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b063ac bytes a98a0eb9
+ 00b063f0 bytes a9ca0eb9
- 00b063f0 ["INT_ADD", "register:40f0:8", ["const:b063f0:8", "const:4:8"]]
- 00b063f0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b06434 ["INT_ADD", "register:40f0:8", ["const:b06434:8", "const:4:8"]]
+ 00b06434 ["CALL", null, ["callee:00bde090:8"]]
- 00b063f0 bytes 145f0394
+ 00b06434 bytes 175f0394
- 00b063f8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d50:8"]]
- 00b063f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b0643c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d90:8"]]
+ 00b0643c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b063f8 bytes a0aa06f9
+ 00b0643c bytes a0ca06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a4d61f7b09302911ac1b6ce34d62b6c"></a>

### [`00b06984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md) → [`00b069c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md) FUN_00b069c8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 6件 [`00b061ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b061ec.md) [`00b06390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md) [`00b06b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06b34.md) [`00b06be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06be8.md) [`00b06ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md) · 呼出先 4件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde100.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bdee20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee20.md)
- 新版 呼出元 6件 [`00b06230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06230.md) [`00b063d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md) [`00b06b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06b78.md) [`00b06c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06c2c.md) [`00b06d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md) · 呼出先 4件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde150.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bdee70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee70.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.05% / 新版 85.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 10件

アドレスに依存する影響 `branch_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b069fc",
      "incomplete_value": true,
      "site": "00b069fc",
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
            "const:ec8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b069b8",
      "incomplete_value": true,
      "site": "00b069b8",
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
            "const:e88:8"
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
      "definition_site": "00b06a3c",
      "incomplete_value": true,
      "site": "00b06a3c",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b069f8",
      "incomplete_value": true,
      "site": "00b069f8",
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
            "const:d58:8"
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
      "definition_site": "00b06a5c",
      "incomplete_value": true,
      "site": "00b06a5c",
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
            "const:d90:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06a18",
      "incomplete_value": true,
      "site": "00b06a18",
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
            "const:d50:8"
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
      "00b069dc",
      "READ",
      [
        "storage",
        "010a0e88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b069f4",
      "READ",
      [
        "storage",
        "010a0e88",
        null,
        "undefined4"
      ]
    ],
    [
      "00b069fc",
      "WRITE",
      [
        "storage",
        "010a0e88",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b069dc",
      "READ",
      [
        "storage",
        "010a0ec8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b069f4",
      "READ",
      [
        "storage",
        "010a0ec8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b069fc",
      "WRITE",
      [
        "storage",
        "010a0ec8",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b069b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md#insn-00b069b8) · [`00b069d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md#insn-00b069d4) · [`00b069e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md#insn-00b069e0)
- 新版 [`00b069fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md#insn-00b069fc) · [`00b06a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md#insn-00b06a18) · [`00b06a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md#insn-00b06a24)

~~~diff
- 00b069b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e88:8"]]
- 00b069b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b069fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ec8:8"]]
+ 00b069fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b069b8 bytes 888a0eb9
+ 00b069fc bytes 88ca0eb9
- 00b069d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d50:8"]]
- 00b069d4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b06a18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d90:8"]]
+ 00b06a18 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b069d4 bytes 81aa46f9
+ 00b06a18 bytes 81ca46f9
- 00b069e0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d58:8"]]
- 00b069e0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b069e0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b06a24 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:d98:8"]]
+ 00b06a24 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b06a24 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b069e0 bytes a8627539
+ 00b06a24 bytes a8627639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6dbf58526209640b112925a06c5f36e"></a>

### [`00b06be8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06be8.md) → [`00b06c2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06c2c.md) _ZN8firebase3App6CreateEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bddab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddab0.md) · 呼出先 7件 [`0084795c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/0084795c.md) [`00b06390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md) [`00b06984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06984.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md)
- 新版 呼出元 1件 [`00bddb00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb00.md) · 呼出先 7件 [`0084795c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md) [`00b063d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md) [`00b069c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b069c8.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.21% / 新版 98.21%

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
      "definition_site": "00b06ca8",
      "incomplete_value": true,
      "site": "00b06cac",
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
      "definition_site": "00b06c64",
      "incomplete_value": true,
      "site": "00b06c68",
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
    "ordinal": 2,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b06cc4",
      "incomplete_value": false,
      "site": "00b06cc8",
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
            "const:107:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06c80",
      "incomplete_value": false,
      "site": "00b06c84",
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
            "const:6d:8"
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
      "00b06c98",
      "READ",
      [
        "storage",
        "00c1b928",
        null,
        "pointer"
      ]
    ],
    [
      "00b06ca8",
      "READ",
      [
        "storage",
        "00c10690",
        "_ZN8firebase15kDefaultAppNameE",
        "pointer"
      ]
    ],
    [
      "00b06ca8",
      "PARAM",
      [
        "storage",
        "002a4ec6",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b06c98",
      "READ",
      [
        "storage",
        "00c1b978",
        null,
        "pointer"
      ]
    ],
    [
      "00b06ca8",
      "READ",
      [
        "storage",
        "00c106e0",
        "_ZN8firebase15kDefaultAppNameE",
        "pointer"
      ]
    ],
    [
      "00b06ca8",
      "PARAM",
      [
        "storage",
        "002a4f51",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06be8.md#insn-00b06c68) · [`00b06c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06be8.md#insn-00b06c84) · [`00b06c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06be8.md#insn-00b06c10)
- 新版 [`00b06cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06c2c.md#insn-00b06cac) · [`00b06cc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06c2c.md#insn-00b06cc8) · [`00b06c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06c2c.md#insn-00b06c54)

~~~diff
- 00b06c68 ["INT_ADD", "register:40f0:8", ["const:b06c68:8", "const:4:8"]]
- 00b06c68 ["CALL", null, ["callee:00bdf020:8"]]
+ 00b06cac ["INT_ADD", "register:40f0:8", ["const:b06cac:8", "const:4:8"]]
+ 00b06cac ["CALL", null, ["callee:00bdf020:8"]]
- 00b06c68 bytes da600394
+ 00b06cac bytes dd600394
- 00b06c84 ["INT_ADD", "register:40f0:8", ["const:b06c84:8", "const:4:8"]]
- 00b06c84 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b06cc8 ["INT_ADD", "register:40f0:8", ["const:b06cc8:8", "const:4:8"]]
+ 00b06cc8 ["CALL", null, ["callee:00bdde40:8"]]
- 00b06c84 bytes 5b5c0394
+ 00b06cc8 bytes 5e5c0394
- 00b06c10 ["INT_ADD", "register:40f0:8", ["const:b06c10:8", "const:4:8"]]
- 00b06c10 ["CALL", null, ["callee:00b063d4:8"]]
+ 00b06c54 ["INT_ADD", "register:40f0:8", ["const:b06c54:8", "const:4:8"]]
+ 00b06c54 ["CALL", null, ["callee:00b063d4:8"]]
- 00b06c10 bytes e0fdff97
+ 00b06c54 bytes e0fdff97
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-90d9a7f7579ac16b30cc2bffe1259529"></a>

### [`00b06ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md) → [`00b06d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md) _ZN8firebase3App6CreateERKNS_10AppOptionsEPKcP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdefd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdefd0.md) · 呼出先 28件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`0084795c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/0084795c.md) [`00b06390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06390.md)
- 新版 呼出元 1件 [`00bdf020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf020.md) · 呼出先 28件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`0084795c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md) [`00b063d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b063d4.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.57% / 新版 98.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件

アドレスに依存する影響 `call_argument_candidate` 11件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b06d98",
      "incomplete_value": true,
      "site": "00b06d9c",
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
      "definition_site": "00b06d54",
      "incomplete_value": true,
      "site": "00b06d58",
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
    "ordinal": 2,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b06dcc",
      "incomplete_value": true,
      "site": "00b06dd8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06d88",
      "incomplete_value": true,
      "site": "00b06d94",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d50:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b06dd0",
      "incomplete_value": true,
      "site": "00b06dd8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:db0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b06d8c",
      "incomplete_value": true,
      "site": "00b06d94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d70:8"
              ]
            ]
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
      "00b06d88",
      "READ",
      [
        "storage",
        "00c1b998",
        null,
        "pointer"
      ]
    ],
    [
      "00b06d98",
      "READ",
      [
        "storage",
        "00c24758",
        "_ZN8firebase22kFirebaseVersionStringE",
        "pointer"
      ]
    ],
    [
      "00b06d98",
      "PARAM",
      [
        "storage",
        "0029ef03",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b06d88",
      "READ",
      [
        "storage",
        "00c1b9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b06d98",
      "READ",
      [
        "storage",
        "00c247a8",
        "_ZN8firebase22kFirebaseVersionStringE",
        "pointer"
      ]
    ],
    [
      "00b06d98",
      "PARAM",
      [
        "storage",
        "0029ef8e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b06d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md#insn-00b06d58) · [`00b06d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md#insn-00b06d94) · [`00b06dd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b06/00b06ce0.md#insn-00b06dd4)
- 新版 [`00b06d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md#insn-00b06d9c) · [`00b06dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md#insn-00b06dd8) · [`00b06e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b06/00b06d24.md#insn-00b06e18)

~~~diff
- 00b06d58 ["INT_ADD", "register:40f0:8", ["const:b06d58:8", "const:4:8"]]
- 00b06d58 ["CALL", null, ["callee:00bde2b0:8"]]
+ 00b06d9c ["INT_ADD", "register:40f0:8", ["const:b06d9c:8", "const:4:8"]]
+ 00b06d9c ["CALL", null, ["callee:00bde2b0:8"]]
- 00b06d58 bytes 425d0394
+ 00b06d9c bytes 455d0394
- 00b06d94 ["INT_ADD", "register:40f0:8", ["const:b06d94:8", "const:4:8"]]
- 00b06d94 ["CALL", null, ["callee:00bddd40:8"]]
+ 00b06dd8 ["INT_ADD", "register:40f0:8", ["const:b06dd8:8", "const:4:8"]]
+ 00b06dd8 ["CALL", null, ["callee:00bddd40:8"]]
- 00b06d94 bytes d75b0394
+ 00b06dd8 bytes da5b0394
- 00b06dd4 ["INT_ADD", "register:40f0:8", ["const:b06dd4:8", "const:4:8"]]
- 00b06dd4 ["CALL", null, ["callee:00bddd40:8"]]
+ 00b06e18 ["INT_ADD", "register:40f0:8", ["const:b06e18:8", "const:4:8"]]
+ 00b06e18 ["CALL", null, ["callee:00bddd40:8"]]
- 00b06dd4 bytes c75b0394
+ 00b06e18 bytes ca5b0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cb2b0e3209f20033d6884128205c3df"></a>

### [`00b07f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b07/00b07f84.md) → [`00b07fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b07/00b07fc8.md) _ZN8firebase3App15RegisterLibraryEPKcS2_Pv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde8e0.md) · 呼出先 5件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde850.md)
- 新版 呼出元 1件 [`00bde930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde930.md) · 呼出先 2件 [`00bdae9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdae9c.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 branch_condition_or_target, branch_count, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence

命令の説明率　旧版 14.71% / 新版 62.50%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_count` 1件, `call_count` 10件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b07fd8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b07fb0"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b07fc8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b07fe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b07fb4"
      ]
    ],
    [
      "unmatched:00b07fac",
      "PARAM",
      [
        "storage",
        "002a7dd9",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b07fb0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde180"
      ]
    ]
  ],
  "added": [
    [
      "00b07fe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b07ff8"
      ]
    ],
    [
      "00b07ff0",
      "PARAM",
      [
        "storage",
        "002a7e73",
        null,
        "string"
      ]
    ],
    [
      "00b07ff4",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde180"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b07fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b07/00b07f84.md#insn-00b07fb0) · [`00b07fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b07/00b07f84.md#insn-00b07fc8) · [`00b07fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b07/00b07f84.md#insn-00b07fd4)

~~~diff
- 00b07fb0 ["INT_ADD", "register:40f0:8", ["const:b07fb0:8", "const:4:8"]]
- 00b07fb0 ["CALL", null, ["callee:00bde180:8"]]
- 00b07fb0 bytes 60580394
- 00b07fc8 ["INT_ADD", "register:40f0:8", ["const:b07fc8:8", "const:4:8"]]
- 00b07fc8 ["CALL", null, ["callee:00bddd40:8"]]
- 00b07fc8 bytes 4a570394
- 00b07fd4 ["INT_ADD", "register:40f0:8", ["const:b07fd4:8", "const:4:8"]]
- 00b07fd4 ["CALL", null, ["callee:00bde0e0:8"]]
- 00b07fd4 bytes 2f580394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44c56147c1c465865d23d1d528519e2d"></a>

### [`00b08098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b08098.md) → [`00b080dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b080dc.md) _ZN8firebase3App31SetDataCollectionDefaultEnabledEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4f0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde540.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.55% / 新版 96.55%

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
      "definition_site": "00b080f4",
      "incomplete_value": true,
      "site": "00b080f4",
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
      "definition_site": "00b080b0",
      "incomplete_value": true,
      "site": "00b080b0",
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
      "definition_site": "00b08110",
      "incomplete_value": true,
      "site": "00b08120",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:de0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b080cc",
      "incomplete_value": true,
      "site": "00b080dc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:da0:8"
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
      "00b080f0",
      "READ",
      [
        "storage",
        "010a0da0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b08110",
      "READ",
      [
        "storage",
        "010a0da0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b080f0",
      "READ",
      [
        "storage",
        "010a0de0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b08110",
      "READ",
      [
        "storage",
        "010a0de0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b080dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b08098.md#insn-00b080dc) · [`00b080ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b08098.md#insn-00b080ac) · [`00b080c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b08098.md#insn-00b080c4)
- 新版 [`00b08120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b080dc.md#insn-00b08120) · [`00b080f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b080dc.md#insn-00b080f0) · [`00b08108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b080dc.md#insn-00b08108)

~~~diff
- 00b080dc ["INT_ADD", "register:40f0:8", ["const:b080dc:8", "const:4:8"]]
- 00b080dc ["CALL", null, ["callee:00551e14:8"]]
+ 00b08120 ["INT_ADD", "register:40f0:8", ["const:b08120:8", "const:4:8"]]
+ 00b08120 ["CALL", null, ["callee:00551e14:8"]]
- 00b080dc bytes 4e27e997
+ 00b08120 bytes 3d27e997
- 00b080ac ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:da0:8"]]
- 00b080ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b080f0 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:de0:8"]]
+ 00b080f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b080ac bytes c8d246f9
+ 00b080f0 bytes c8f246f9
- 00b080c4 ["INT_ADD", "register:40f0:8", ["const:b080c4:8", "const:4:8"]]
- 00b080c4 ["CALL", null, ["callee:00bde540:8"]]
+ 00b08108 ["INT_ADD", "register:40f0:8", ["const:b08108:8", "const:4:8"]]
+ 00b08108 ["CALL", null, ["callee:00bde540:8"]]
- 00b080c4 bytes 0b590394
+ 00b08108 bytes 0e590394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-433f9c85155d99447dc1131981bae023"></a>

### [`00b0810c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0810c.md) → [`00b08150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08150.md) _ZNK8firebase3App30IsDataCollectionDefaultEnabledEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde4f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4f0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde540.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.00% / 新版 96.00%

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
      "definition_site": "00b08164",
      "incomplete_value": true,
      "site": "00b08164",
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
      "definition_site": "00b08120",
      "incomplete_value": true,
      "site": "00b08120",
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
      "definition_site": "00b0817c",
      "incomplete_value": true,
      "site": "00b08188",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:dd8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b08138",
      "incomplete_value": true,
      "site": "00b08144",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:d98:8"
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
      "00b08160",
      "READ",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0817c",
      "READ",
      [
        "storage",
        "010a0d98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b08160",
      "READ",
      [
        "storage",
        "010a0dd8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0817c",
      "READ",
      [
        "storage",
        "010a0dd8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b08144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0810c.md#insn-00b08144) · [`00b0811c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0810c.md#insn-00b0811c) · [`00b08130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0810c.md#insn-00b08130)
- 新版 [`00b08188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08150.md#insn-00b08188) · [`00b08160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08150.md#insn-00b08160) · [`00b08174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08150.md#insn-00b08174)

~~~diff
- 00b08144 ["INT_ADD", "register:40f0:8", ["const:b08144:8", "const:4:8"]]
- 00b08144 ["CALL", null, ["callee:00474b70:8"]]
+ 00b08188 ["INT_ADD", "register:40f0:8", ["const:b08188:8", "const:4:8"]]
+ 00b08188 ["CALL", null, ["callee:00474b70:8"]]
- 00b08144 bytes 8bb2e597
+ 00b08188 bytes 7ab2e597
- 00b0811c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d98:8"]]
- 00b0811c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b08160 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:dd8:8"]]
+ 00b08160 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b0811c bytes 88ce46f9
+ 00b08160 bytes 88ee46f9
- 00b08130 ["INT_ADD", "register:40f0:8", ["const:b08130:8", "const:4:8"]]
- 00b08130 ["CALL", null, ["callee:00bde540:8"]]
+ 00b08174 ["INT_ADD", "register:40f0:8", ["const:b08174:8", "const:4:8"]]
+ 00b08174 ["CALL", null, ["callee:00bde540:8"]]
- 00b08130 bytes f0580394
+ 00b08174 bytes f3580394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bd631909e95b87bedcf365983c40aaa"></a>

### [`00b0871c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0871c.md) → [`00b08760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08760.md) _ZN8firebase10AppOptions18LoadFromJsonConfigEPKcPS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 14件 [`0084795c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/0084795c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0084795c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.67% / 新版 96.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 12件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b087dc",
      "incomplete_value": true,
      "site": "00b087dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:725:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b08798",
      "incomplete_value": true,
      "site": "00b08798",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7b2:8"
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
      "definition_site": "00b087ac",
      "incomplete_value": true,
      "site": "00b087e4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b08768",
      "incomplete_value": true,
      "site": "00b087a0",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b088c4",
      "incomplete_value": true,
      "site": "00b088d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b08880",
      "incomplete_value": true,
      "site": "00b08890",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f0:8"
              ]
            ]
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
      "00b087a8",
      "READ",
      [
        "storage",
        "002987b2",
        null,
        "string"
      ]
    ],
    [
      "00b087ac",
      "READ",
      [
        "storage",
        "002987b9",
        null,
        "string"
      ]
    ],
    [
      "00b088c4",
      "READ",
      [
        "storage",
        "00c1b8f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b087a8",
      "READ",
      [
        "storage",
        "00298725",
        null,
        "string"
      ]
    ],
    [
      "00b087ac",
      "READ",
      [
        "storage",
        "0029872c",
        null,
        "string"
      ]
    ],
    [
      "00b088c4",
      "READ",
      [
        "storage",
        "00c1b940",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b08890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0871c.md#insn-00b08890) · [`00b08928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0871c.md#insn-00b08928) · [`00b08948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b08/00b0871c.md#insn-00b08948)
- 新版 [`00b088d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08760.md#insn-00b088d4) · [`00b0896c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08760.md#insn-00b0896c) · [`00b0898c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b08/00b08760.md#insn-00b0898c)

~~~diff
- 00b08890 ["INT_ADD", "register:40f0:8", ["const:b08890:8", "const:4:8"]]
- 00b08890 ["CALL", null, ["callee:00bdf060:8"]]
+ 00b088d4 ["INT_ADD", "register:40f0:8", ["const:b088d4:8", "const:4:8"]]
+ 00b088d4 ["CALL", null, ["callee:00bdf060:8"]]
- 00b08890 bytes e0590394
+ 00b088d4 bytes e3590394
- 00b08928 ["INT_ADD", "register:40f0:8", ["const:b08928:8", "const:4:8"]]
- 00b08928 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b0896c ["INT_ADD", "register:40f0:8", ["const:b0896c:8", "const:4:8"]]
+ 00b0896c ["CALL", null, ["callee:00bdde40:8"]]
- 00b08928 bytes 32550394
+ 00b0896c bytes 35550394
- 00b08948 ["INT_ADD", "register:40f0:8", ["const:b08948:8", "const:4:8"]]
- 00b08948 ["CALL", null, ["callee:00bde180:8"]]
+ 00b0898c ["INT_ADD", "register:40f0:8", ["const:b0898c:8", "const:4:8"]]
+ 00b0898c ["CALL", null, ["callee:00bde180:8"]]
- 00b08948 bytes fa550394
+ 00b0898c bytes fd550394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-139e913b06ca05dbce93bf0892670ec4"></a>

### [`00b09008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b09/00b09008.md) → [`00b0904c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b09/00b0904c.md) _ZN11flatbuffers6ParserC2ERKNS_10IDLOptionsE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdea20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea20.md) · 呼出先 8件 [`00613984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00613/00613984.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 1件 [`00bdea70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea70.md) · 呼出先 8件 [`00613984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00613/00613984.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.71% / 新版 96.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 15件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0924c",
      "incomplete_value": true,
      "site": "00b0924c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:fe3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b09208",
      "incomplete_value": true,
      "site": "00b09208",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 89,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b096c8",
      "incomplete_value": true,
      "site": "00b096c8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
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
    "old": {
      "definition_site": "00b09684",
      "incomplete_value": true,
      "site": "00b09684",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:2af000:8"
              ],
              [
                "leaf",
                "const:449:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 203,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b09790",
      "incomplete_value": true,
      "site": "00b09790",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:735:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0974c",
      "incomplete_value": true,
      "site": "00b0974c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c2:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 223,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b09220",
      "READ",
      [
        "storage",
        "0029ef58",
        null,
        "string"
      ]
    ],
    [
      "00b0969c",
      "READ",
      [
        "storage",
        "002af449",
        null,
        "string"
      ]
    ],
    [
      "00b09768",
      "READ",
      [
        "storage",
        "002987c2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b09220",
      "READ",
      [
        "storage",
        "0029efe3",
        null,
        "string"
      ]
    ],
    [
      "00b0969c",
      "READ",
      [
        "storage",
        "002af3b5",
        null,
        "string"
      ]
    ],
    [
      "00b09768",
      "READ",
      [
        "storage",
        "00298735",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b090d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b09/00b09008.md#insn-00b090d4) · [`00b090f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b09/00b09008.md#insn-00b090f0) · [`00b09174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b09/00b09008.md#insn-00b09174)
- 新版 [`00b09118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b09/00b0904c.md#insn-00b09118) · [`00b09134`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b09/00b0904c.md#insn-00b09134) · [`00b091b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b09/00b0904c.md#insn-00b091b8)

~~~diff
- 00b090d4 ["INT_ADD", "register:40f0:8", ["const:b090d4:8", "const:4:8"]]
- 00b090d4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b09118 ["INT_ADD", "register:40f0:8", ["const:b09118:8", "const:4:8"]]
+ 00b09118 ["CALL", null, ["callee:00bdb040:8"]]
- 00b090d4 bytes c7470394
+ 00b09118 bytes ca470394
- 00b090f0 ["INT_ADD", "register:40f0:8", ["const:b090f0:8", "const:4:8"]]
- 00b090f0 ["CALL", null, ["callee:00bdb240:8"]]
+ 00b09134 ["INT_ADD", "register:40f0:8", ["const:b09134:8", "const:4:8"]]
+ 00b09134 ["CALL", null, ["callee:00bdb240:8"]]
- 00b090f0 bytes 40480394
+ 00b09134 bytes 43480394
- 00b09174 ["INT_ADD", "register:40f0:8", ["const:b09174:8", "const:4:8"]]
- 00b09174 ["CALL", null, ["callee:00bdea00:8"]]
+ 00b091b8 ["INT_ADD", "register:40f0:8", ["const:b091b8:8", "const:4:8"]]
+ 00b091b8 ["CALL", null, ["callee:00bdea00:8"]]
- 00b09174 bytes 0f560394
+ 00b091b8 bytes 12560394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

