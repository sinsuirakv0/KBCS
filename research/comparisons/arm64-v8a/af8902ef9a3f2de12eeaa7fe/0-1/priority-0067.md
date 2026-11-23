# v15.7.3 → v15.7.4 · 最優先の変更候補 (67)

[一覧の目次](README.md)

<a id="compare-db8f48e98fbdce04e0887a668872c3ef"></a>

### [`00b0a968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a968.md) → [`00b0a9ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a9ac.md) _ZN8firebase10AppOptions28PopulateRequiredWithDefaultsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdea40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdea40.md) · 呼出先 5件 [`0084795c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00847/0084795c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md) [`00bdefc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdefc0.md)
- 新版 呼出元 1件 [`00bdea90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdea90.md) · 呼出先 5件 [`0084795c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00847/0084795c.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md) [`00bdf010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf010.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.60% / 新版 98.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0aaa8",
      "incomplete_value": false,
      "site": "00b0aaac",
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
            "const:739:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0aa64",
      "incomplete_value": false,
      "site": "00b0aa68",
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
            "const:7c6:8"
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
      "definition_site": "00b0abb4",
      "incomplete_value": false,
      "site": "00b0abb8",
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
            "const:348:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0ab70",
      "incomplete_value": false,
      "site": "00b0ab74",
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
            "const:3d5:8"
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
      "00b0aaa8",
      "PARAM",
      [
        "storage",
        "002997c6",
        null,
        "string"
      ]
    ],
    [
      "00b0abb4",
      "PARAM",
      [
        "storage",
        "002953d5",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0aaa8",
      "PARAM",
      [
        "storage",
        "00299739",
        null,
        "string"
      ]
    ],
    [
      "00b0abb4",
      "PARAM",
      [
        "storage",
        "00295348",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0aa68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a968.md#insn-00b0aa68) · [`00b0ab74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a968.md#insn-00b0ab74) · [`00b0aa44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0a/00b0a968.md#insn-00b0aa44)
- 新版 [`00b0aaac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a9ac.md#insn-00b0aaac) · [`00b0abb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a9ac.md#insn-00b0abb8) · [`00b0aa88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0a/00b0a9ac.md#insn-00b0aa88)

~~~diff
- 00b0aa68 ["INT_ADD", "register:40f0:8", ["const:b0aa68:8", "const:4:8"]]
- 00b0aa68 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b0aaac ["INT_ADD", "register:40f0:8", ["const:b0aaac:8", "const:4:8"]]
+ 00b0aaac ["CALL", null, ["callee:00bdde40:8"]]
- 00b0aa68 bytes e24c0394
+ 00b0aaac bytes e54c0394
- 00b0ab74 ["INT_ADD", "register:40f0:8", ["const:b0ab74:8", "const:4:8"]]
- 00b0ab74 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b0abb8 ["INT_ADD", "register:40f0:8", ["const:b0abb8:8", "const:4:8"]]
+ 00b0abb8 ["CALL", null, ["callee:00bdde40:8"]]
- 00b0ab74 bytes 9f4c0394
+ 00b0abb8 bytes a24c0394
- 00b0aa44 ["INT_ADD", "register:40f0:8", ["const:b0aa44:8", "const:4:8"]]
- 00b0aa44 ["CALL", null, ["callee:00bdf010:8"]]
+ 00b0aa88 ["INT_ADD", "register:40f0:8", ["const:b0aa88:8", "const:4:8"]]
+ 00b0aa88 ["CALL", null, ["callee:00bdf010:8"]]
- 00b0aa44 bytes 5f510394
+ 00b0aa88 bytes 62510394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e32a4dd302d7e0df8f91ec852a06651c"></a>

### [`00b0d740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d740.md) → [`00b0d784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d784.md) _ZN20google_play_services10InitializeEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdee00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee00.md) · 呼出先 17件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md)
- 新版 呼出元 1件 [`00bdee50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee50.md) · 呼出先 17件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 84.56% / 新版 84.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 5件, `call_argument_candidate` 10件, `store_condition` 5件, `store_destination` 11件

アドレスに依存する影響 `branch_value` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b0d7c4",
      "incomplete_value": false,
      "site": "00b0d7c4",
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
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0d780",
      "incomplete_value": false,
      "site": "00b0d780",
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
            "const:e90:8"
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
      "definition_site": "00b0d814",
      "incomplete_value": true,
      "site": "00b0d814",
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
            "const:ed8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0d7d0",
      "incomplete_value": true,
      "site": "00b0d7d0",
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
            "const:e98:8"
          ]
        ]
      ]
    },
    "ordinal": 15,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b0d95c",
      "incomplete_value": true,
      "site": "00b0d95c",
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
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0d918",
      "incomplete_value": true,
      "site": "00b0d918",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0d7b8",
      "READ",
      [
        "storage",
        "010a0e90",
        null,
        "undefined4"
      ]
    ],
    [
      "00b0d7bc",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0d7c4",
      "WRITE",
      [
        "storage",
        "010a0e90",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b0d7b8",
      "READ",
      [
        "storage",
        "010a0ed0",
        null,
        "undefined4"
      ]
    ],
    [
      "00b0d7bc",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0d7c4",
      "WRITE",
      [
        "storage",
        "010a0ed0",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0d780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d740.md#insn-00b0d780) · [`00b0d7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d740.md#insn-00b0d7d0) · [`00b0d7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0d740.md#insn-00b0d7e8)
- 新版 [`00b0d7c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d784.md#insn-00b0d7c4) · [`00b0d814`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d784.md#insn-00b0d814) · [`00b0d82c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0d784.md#insn-00b0d82c)

~~~diff
- 00b0d780 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:e90:8"]]
- 00b0d780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b0d7c4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:ed0:8"]]
+ 00b0d7c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b0d780 bytes 08930eb9
+ 00b0d7c4 bytes 08d30eb9
- 00b0d7d0 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:e98:8"]]
- 00b0d7d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
+ 00b0d814 ["INT_ADD", "tmp:0:8", ["register:40c8:8", "const:ed8:8"]]
+ 00b0d814 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a8:8"]]
- 00b0d7d0 bytes 354f07f9
+ 00b0d814 bytes 356f07f9
- 00b0d7e8 ["INT_ADD", "register:40f0:8", ["const:b0d7e8:8", "const:4:8"]]
- 00b0d7e8 ["CALL", null, ["callee:00bde6f0:8"]]
+ 00b0d82c ["INT_ADD", "register:40f0:8", ["const:b0d82c:8", "const:4:8"]]
+ 00b0d82c ["CALL", null, ["callee:00bde6f0:8"]]
- 00b0d7e8 bytes ae430394
+ 00b0d82c bytes b1430394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e816caf6bf38a70717712f57191923e"></a>

### [`00b0db4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0db4c.md) → [`00b0db90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0db90.md) _ZN20google_play_services9TerminateEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdee20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee20.md) · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddda0.md) [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 1件 [`00bdee70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee70.md) · 呼出先 7件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bdddf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddf0.md) [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 82.19% / 新版 82.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 4件, `store_destination` 5件

アドレスに依存する影響 `branch_value` 2件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b0dbb0",
      "incomplete_value": true,
      "site": "00b0dbb0",
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
            "const:ed0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0db6c",
      "incomplete_value": true,
      "site": "00b0db6c",
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
            "const:e90:8"
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
      "definition_site": "00b0dc14",
      "incomplete_value": true,
      "site": "00b0dc14",
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
            "const:ef0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dbd0",
      "incomplete_value": true,
      "site": "00b0dbd0",
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
            "const:eb0:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b0dc3c",
      "incomplete_value": true,
      "site": "00b0dc3c",
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
            "const:f10:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dbf8",
      "incomplete_value": true,
      "site": "00b0dbf8",
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
            "const:ed0:8"
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
      "00b0dba4",
      "READ",
      [
        "storage",
        "010a0e90",
        null,
        "undefined4"
      ]
    ],
    [
      "00b0dbb0",
      "WRITE",
      [
        "storage",
        "010a0e90",
        null,
        "undefined4"
      ]
    ],
    [
      "00b0dbbc",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b0dba4",
      "READ",
      [
        "storage",
        "010a0ed0",
        null,
        "undefined4"
      ]
    ],
    [
      "00b0dbb0",
      "WRITE",
      [
        "storage",
        "010a0ed0",
        null,
        "undefined4"
      ]
    ],
    [
      "00b0dbbc",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0db6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0db4c.md#insn-00b0db6c) · [`00b0db94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0db4c.md#insn-00b0db94) · [`00b0db9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0db4c.md#insn-00b0db9c)
- 新版 [`00b0dbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0db90.md#insn-00b0dbb0) · [`00b0dbd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0db90.md#insn-00b0dbd8) · [`00b0dbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0db90.md#insn-00b0dbe0)

~~~diff
- 00b0db6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e90:8"]]
- 00b0db6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
+ 00b0dbb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ed0:8"]]
+ 00b0dbb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4048:4"]]
- 00b0db6c bytes 09910eb9
+ 00b0dbb0 bytes 09d10eb9
- 00b0db94 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ec0:8"]]
- 00b0db94 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b0dbd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:f00:8"]]
+ 00b0dbd8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b0db94 bytes 026147f9
+ 00b0dbd8 bytes 028147f9
- 00b0db9c ["INT_ADD", "register:40f0:8", ["const:b0db9c:8", "const:4:8"]]
- 00b0db9c ["CALL", null, ["callee:00bde3c0:8"]]
+ 00b0dbe0 ["INT_ADD", "register:40f0:8", ["const:b0dbe0:8", "const:4:8"]]
+ 00b0dbe0 ["CALL", null, ["callee:00bde3c0:8"]]
- 00b0db9c bytes f5410394
+ 00b0dbe0 bytes f8410394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f699cc7022e6ce596510bbf1c93e4c7"></a>

### [`00b0dc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0dc70.md) → [`00b0dcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0dcb4.md) _ZN20google_play_services17CheckAvailabilityEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdf020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf020.md) · 呼出先 4件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bdee00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee00.md)
- 新版 呼出元 1件 [`00bdf070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf070.md) · 呼出先 4件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bdee50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee50.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 89.16% / 新版 89.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b0dde8",
      "incomplete_value": true,
      "site": "00b0dde8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:141:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dda4",
      "incomplete_value": true,
      "site": "00b0dda4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:141:8"
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
      "definition_site": "00b0ddec",
      "incomplete_value": true,
      "site": "00b0ddec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:144:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dda8",
      "incomplete_value": true,
      "site": "00b0dda8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:144:8"
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
      "definition_site": "00b0dcd4",
      "incomplete_value": true,
      "site": "00b0dcd4",
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
      "definition_site": "00b0dc90",
      "incomplete_value": true,
      "site": "00b0dc90",
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
      "00b0dcc8",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0dcdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b0dcc0"
      ]
    ],
    [
      "00b0dcf8",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b0dcc8",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0dcdc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b0dd04"
      ]
    ],
    [
      "00b0dcf8",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0dcd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0dc70.md#insn-00b0dcd4) · [`00b0dd08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0dc70.md#insn-00b0dd08)
- 新版 [`00b0dd18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0dcb4.md#insn-00b0dd18) · [`00b0dd4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0dcb4.md#insn-00b0dd4c) · [`00b0dd08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0dcb4.md#insn-00b0dd08)

~~~diff
- 00b0dcd4 ["INT_ADD", "register:40f0:8", ["const:b0dcd4:8", "const:4:8"]]
- 00b0dcd4 ["CALL", null, ["callee:00bddd40:8"]]
+ 00b0dd18 ["INT_ADD", "register:40f0:8", ["const:b0dd18:8", "const:4:8"]]
+ 00b0dd18 ["CALL", null, ["callee:00bddd40:8"]]
- 00b0dcd4 bytes 07400394
+ 00b0dd18 bytes 0a400394
- 00b0dd08 ["INT_ADD", "register:40f0:8", ["const:b0dd08:8", "const:4:8"]]
- 00b0dd08 ["CALL", null, ["callee:005533e0:8"]]
+ 00b0dd4c ["INT_ADD", "register:40f0:8", ["const:b0dd4c:8", "const:4:8"]]
+ 00b0dd4c ["CALL", null, ["callee:005533e0:8"]]
- 00b0dd08 bytes b615e997
+ 00b0dd4c bytes a515e997
+ 00b0dd08 ["COPY", "register:4048:8", ["const:10a0000:8"]]
+ 00b0dd08 bytes 892c00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ff4e646e69f6966f4e3b41284aed0b9"></a>

### [`00b0ddbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0ddbc.md) → [`00b0de00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0de00.md) _ZN20google_play_services17CallMakeAvailableEPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00b0df30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0df30.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf30.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 1件 [`00b0df74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0df74.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf80.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0de38",
      "incomplete_value": true,
      "site": "00b0de48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ef8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0ddf4",
      "incomplete_value": true,
      "site": "00b0de04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:eb8:8"
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
      "definition_site": "00b0de3c",
      "incomplete_value": true,
      "site": "00b0de48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:f08:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0ddf8",
      "incomplete_value": true,
      "site": "00b0de04",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ec8:8"
              ]
            ]
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
      "definition_site": "00b0de7c",
      "incomplete_value": true,
      "site": "00b0de80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0de38",
      "incomplete_value": true,
      "site": "00b0de3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:130:8"
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
      "00b0de38",
      "READ",
      [
        "storage",
        "010a0eb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0de3c",
      "READ",
      [
        "storage",
        "010a0ec8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0de74",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b0de38",
      "READ",
      [
        "storage",
        "010a0ef8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0de3c",
      "READ",
      [
        "storage",
        "010a0f08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0de74",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0ddf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0ddbc.md#insn-00b0ddf8) · [`00b0de04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0ddbc.md#insn-00b0de04) · [`00b0de3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0ddbc.md#insn-00b0de3c)
- 新版 [`00b0de3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0de00.md#insn-00b0de3c) · [`00b0de48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0de00.md#insn-00b0de48) · [`00b0de80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0de00.md#insn-00b0de80)

~~~diff
- 00b0ddf8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ec8:8"]]
- 00b0ddf8 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b0de3c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f08:8"]]
+ 00b0de3c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b0ddf8 bytes 226547f9
+ 00b0de3c bytes 228547f9
- 00b0de04 ["INT_ADD", "register:40f0:8", ["const:b0de04:8", "const:4:8"]]
- 00b0de04 ["CALL", null, ["callee:00bdf090:8"]]
+ 00b0de48 ["INT_ADD", "register:40f0:8", ["const:b0de48:8", "const:4:8"]]
+ 00b0de48 ["CALL", null, ["callee:00bdf090:8"]]
- 00b0de04 bytes 8f440394
+ 00b0de48 bytes 92440394
- 00b0de3c ["INT_ADD", "register:40f0:8", ["const:b0de3c:8", "const:4:8"]]
- 00b0de3c ["CALL", null, ["callee:00bddf80:8"]]
+ 00b0de80 ["INT_ADD", "register:40f0:8", ["const:b0de80:8", "const:4:8"]]
+ 00b0de80 ["CALL", null, ["callee:00bddf80:8"]]
- 00b0de3c bytes 3d400394
+ 00b0de80 bytes 40400394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5558b79827b5384c838d1052d6d96ff"></a>

### [`00b0df30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0df30.md) → [`00b0df74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0df74.md) _ZN20google_play_services13MakeAvailableEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdee10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdee10.md) · 呼出先 14件 [`00b0ddbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0ddbc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md)
- 新版 呼出元 1件 [`00bdee60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee60.md) · 呼出先 14件 [`00b0de00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0de00.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.16% / 新版 94.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b0dfb0",
      "incomplete_value": true,
      "site": "00b0dfb0",
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
      "definition_site": "00b0df6c",
      "incomplete_value": true,
      "site": "00b0df6c",
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
      "definition_site": "00b0e060",
      "incomplete_value": true,
      "site": "00b0e060",
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
      "definition_site": "00b0e01c",
      "incomplete_value": true,
      "site": "00b0e01c",
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
      "definition_site": "00b0dffc",
      "incomplete_value": true,
      "site": "00b0e010",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ed8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0dfb8",
      "incomplete_value": true,
      "site": "00b0dfcc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e98:8"
              ]
            ]
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
      "00b0dfa8",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0dfc8",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0dffc",
      "READ",
      [
        "storage",
        "010a0e98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b0dfa8",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0dfc8",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b0dffc",
      "READ",
      [
        "storage",
        "010a0ed8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0dfb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0df30.md#insn-00b0dfb0) · [`00b0dfcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0df30.md#insn-00b0dfcc) · [`00b0dfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0df30.md#insn-00b0dfd8)
- 新版 [`00b0dff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0df74.md#insn-00b0dff4) · [`00b0e010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0df74.md#insn-00b0e010) · [`00b0e01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0d/00b0df74.md#insn-00b0e01c)

~~~diff
- 00b0dfb0 ["INT_ADD", "register:40f0:8", ["const:b0dfb0:8", "const:4:8"]]
- 00b0dfb0 ["CALL", null, ["callee:00bddc40:8"]]
+ 00b0dff4 ["INT_ADD", "register:40f0:8", ["const:b0dff4:8", "const:4:8"]]
+ 00b0dff4 ["CALL", null, ["callee:00bddc40:8"]]
- 00b0dfb0 bytes 103f0394
+ 00b0dff4 bytes 133f0394
- 00b0dfcc ["INT_ADD", "register:40f0:8", ["const:b0dfcc:8", "const:4:8"]]
- 00b0dfcc ["CALL", null, ["callee:00bddfc0:8"]]
+ 00b0e010 ["INT_ADD", "register:40f0:8", ["const:b0e010:8", "const:4:8"]]
+ 00b0e010 ["CALL", null, ["callee:00bddfc0:8"]]
- 00b0dfcc bytes e93f0394
+ 00b0e010 bytes ec3f0394
- 00b0dfd8 ["INT_ADD", "register:40f0:8", ["const:b0dfd8:8", "const:4:8"]]
- 00b0dfd8 ["CALL", null, ["callee:00bddf80:8"]]
+ 00b0e01c ["INT_ADD", "register:40f0:8", ["const:b0e01c:8", "const:4:8"]]
+ 00b0e01c ["CALL", null, ["callee:00bddf80:8"]]
- 00b0dfd8 bytes d63f0394
+ 00b0e01c bytes d93f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-391a6796c676f51b8e83ddf70034bc0c"></a>

### [`00b0e844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e844.md) → [`00b0e888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e888.md) _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf980.md) · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdf150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf150.md)
- 新版 呼出元 1件 [`00bdf9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9d0.md) · 呼出先 7件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdf1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.77% / 新版 98.77%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0e8d8",
      "incomplete_value": false,
      "site": "00b0e8e4",
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
      "definition_site": "00b0e894",
      "incomplete_value": false,
      "site": "00b0e8a0",
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
    "ordinal": 0,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0e980",
      "incomplete_value": false,
      "site": "00b0e98c",
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
            "const:3cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0e93c",
      "incomplete_value": false,
      "site": "00b0e948",
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
            "const:342:8"
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
      "00b0e8d8",
      "PARAM",
      [
        "storage",
        "002a42a8",
        null,
        null
      ]
    ],
    [
      "00b0e980",
      "PARAM",
      [
        "storage",
        "002a0342",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b0e8d8",
      "PARAM",
      [
        "storage",
        "002a4333",
        null,
        null
      ]
    ],
    [
      "00b0e980",
      "PARAM",
      [
        "storage",
        "002a03cd",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0e8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e844.md#insn-00b0e8a0) · [`00b0e948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e844.md#insn-00b0e948) · [`00b0e894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0e844.md#insn-00b0e894)
- 新版 [`00b0e8e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e888.md#insn-00b0e8e4) · [`00b0e98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e888.md#insn-00b0e98c) · [`00b0e8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0e888.md#insn-00b0e8d8)

~~~diff
- 00b0e8a0 ["INT_ADD", "register:40f0:8", ["const:b0e8a0:8", "const:4:8"]]
- 00b0e8a0 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b0e8e4 ["INT_ADD", "register:40f0:8", ["const:b0e8e4:8", "const:4:8"]]
+ 00b0e8e4 ["CALL", null, ["callee:00bdb130:8"]]
- 00b0e8a0 bytes 10320394
+ 00b0e8e4 bytes 13320394
- 00b0e948 ["INT_ADD", "register:40f0:8", ["const:b0e948:8", "const:4:8"]]
- 00b0e948 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b0e98c ["INT_ADD", "register:40f0:8", ["const:b0e98c:8", "const:4:8"]]
+ 00b0e98c ["CALL", null, ["callee:00bdb130:8"]]
- 00b0e948 bytes e6310394
+ 00b0e98c bytes e9310394
- 00b0e894 ["COPY", "tmp:0:8", ["const:2a8:8"]]
- 00b0e894 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b0e894 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b0e894 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b0e8d8 ["COPY", "tmp:0:8", ["const:333:8"]]
+ 00b0e8d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b0e8d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b0e8d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b0e894 bytes 21a00a91
+ 00b0e8d8 bytes 21cc0c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-992fcc8e49bbd88ff4fc66253681b1e6"></a>

### [`00b0ead0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ead0.md) → [`00b0eb14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0eb14.md) _ZN11flatbuffers11NumToStringIiEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf150.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb310.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 1件 [`00bdf1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1a0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb360.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.21% / 新版 91.21%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0eb70",
      "incomplete_value": true,
      "site": "00b0eb84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b0eb2c",
      "incomplete_value": true,
      "site": "00b0eb40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b0eb68",
      "incomplete_value": true,
      "site": "00b0eb88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b0eb24",
      "incomplete_value": true,
      "site": "00b0eb44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0ebf8",
      "incomplete_value": true,
      "site": "00b0ec04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b0ebb4",
      "incomplete_value": true,
      "site": "00b0ebc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0eb48",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "00b0eb4c",
      "READ",
      [
        "storage",
        "00c1b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b0eb84",
      "DATA",
      [
        "storage",
        "00c110f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b0eb48",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "00b0eb4c",
      "READ",
      [
        "storage",
        "00c1ba48",
        null,
        "pointer"
      ]
    ],
    [
      "00b0eb84",
      "DATA",
      [
        "storage",
        "00c11140",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0ec04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ead0.md#insn-00b0ec04) · [`00b0eb04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ead0.md#insn-00b0eb04) · [`00b0eb08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ead0.md#insn-00b0eb08)
- 新版 [`00b0ec48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0eb14.md#insn-00b0ec48) · [`00b0eb48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0eb14.md#insn-00b0eb48) · [`00b0eb4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0eb14.md#insn-00b0eb4c)

~~~diff
- 00b0ec04 ["INT_ADD", "register:40f0:8", ["const:b0ec04:8", "const:4:8"]]
- 00b0ec04 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b0ec48 ["INT_ADD", "register:40f0:8", ["const:b0ec48:8", "const:4:8"]]
+ 00b0ec48 ["CALL", null, ["callee:00be01e0:8"]]
- 00b0ec04 bytes 63450394
+ 00b0ec48 bytes 66450394
- 00b0eb04 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:dd8:8"]]
- 00b0eb04 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b0eb48 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:e28:8"]]
+ 00b0eb48 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b0eb04 bytes 5aef46f9
+ 00b0eb48 bytes 5a1747f9
- 00b0eb08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9f8:8"]]
- 00b0eb08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b0eb4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a48:8"]]
+ 00b0eb4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b0eb08 bytes 08fd44f9
+ 00b0eb4c bytes 082545f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e542386f2862fe750bb3d4b49018fa87"></a>

### [`00b0ef78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ef78.md) → [`00b0efbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0efbc.md) _ZN11flatbuffers6Parser12RecurseErrorEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf7a0.md) · 呼出先 7件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)
- 新版 呼出元 1件 [`00bdf7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf7f0.md) · 呼出先 7件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)

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
      "definition_site": "00b0eff4",
      "incomplete_value": false,
      "site": "00b0f004",
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
            "const:e4c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0efb0",
      "incomplete_value": false,
      "site": "00b0efc0",
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
            "const:dc1:8"
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
      "definition_site": "00b0f014",
      "incomplete_value": false,
      "site": "00b0f030",
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
            "const:74a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0efd0",
      "incomplete_value": false,
      "site": "00b0efec",
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
            "const:7d7:8"
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
      "00b0eff4",
      "PARAM",
      [
        "storage",
        "002a3dc1",
        null,
        "string"
      ]
    ],
    [
      "00b0f014",
      "PARAM",
      [
        "storage",
        "002987d7",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0eff4",
      "PARAM",
      [
        "storage",
        "002a3e4c",
        null,
        "string"
      ]
    ],
    [
      "00b0f014",
      "PARAM",
      [
        "storage",
        "0029874a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0efa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ef78.md#insn-00b0efa8) · [`00b0efc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ef78.md#insn-00b0efc0) · [`00b0efec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0e/00b0ef78.md#insn-00b0efec)
- 新版 [`00b0efec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0efbc.md#insn-00b0efec) · [`00b0f004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0efbc.md#insn-00b0f004) · [`00b0f030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0efbc.md#insn-00b0f030)

~~~diff
- 00b0efa8 ["INT_ADD", "register:40f0:8", ["const:b0efa8:8", "const:4:8"]]
- 00b0efa8 ["CALL", null, ["callee:00bdf1a0:8"]]
+ 00b0efec ["INT_ADD", "register:40f0:8", ["const:b0efec:8", "const:4:8"]]
+ 00b0efec ["CALL", null, ["callee:00bdf1a0:8"]]
- 00b0efa8 bytes 6a400394
+ 00b0efec bytes 6d400394
- 00b0efc0 ["INT_ADD", "register:40f0:8", ["const:b0efc0:8", "const:4:8"]]
- 00b0efc0 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b0f004 ["INT_ADD", "register:40f0:8", ["const:b0f004:8", "const:4:8"]]
+ 00b0f004 ["CALL", null, ["callee:00bdc180:8"]]
- 00b0efc0 bytes 5c340394
+ 00b0f004 bytes 5f340394
- 00b0efec ["INT_ADD", "register:40f0:8", ["const:b0efec:8", "const:4:8"]]
- 00b0efec ["CALL", null, ["callee:00bdb130:8"]]
+ 00b0f030 ["INT_ADD", "register:40f0:8", ["const:b0f030:8", "const:4:8"]]
+ 00b0f030 ["CALL", null, ["callee:00bdb130:8"]]
- 00b0efec bytes 3d300394
+ 00b0f030 bytes 40300394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfd38a986477db132c5b6cf3835b6114"></a>

### [`00b0f418`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f418.md) → [`00b0f45c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f45c.md) _ZN11flatbuffers6Parser11ParseHexNumEiPm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf740.md) · 呼出先 11件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)
- 新版 呼出元 1件 [`00bdf790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf790.md) · 呼出先 11件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.45% / 新版 99.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b0f508",
      "incomplete_value": false,
      "site": "00b0f524",
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
            "const:2cb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0f4c4",
      "incomplete_value": false,
      "site": "00b0f4e0",
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
            "const:358:8"
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
      "00b0f508",
      "PARAM",
      [
        "storage",
        "00293358",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0f508",
      "PARAM",
      [
        "storage",
        "002932cb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0f49c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f418.md#insn-00b0f49c) · [`00b0f4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f418.md#insn-00b0f4e0) · [`00b0f4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f418.md#insn-00b0f4b4)
- 新版 [`00b0f4e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f45c.md#insn-00b0f4e0) · [`00b0f524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f45c.md#insn-00b0f524) · [`00b0f4f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f45c.md#insn-00b0f4f8)

~~~diff
- 00b0f49c ["INT_ADD", "register:40f0:8", ["const:b0f49c:8", "const:4:8"]]
- 00b0f49c ["CALL", null, ["callee:00bdf1a0:8"]]
+ 00b0f4e0 ["INT_ADD", "register:40f0:8", ["const:b0f4e0:8", "const:4:8"]]
+ 00b0f4e0 ["CALL", null, ["callee:00bdf1a0:8"]]
- 00b0f49c bytes 2d3f0394
+ 00b0f4e0 bytes 303f0394
- 00b0f4e0 ["INT_ADD", "register:40f0:8", ["const:b0f4e0:8", "const:4:8"]]
- 00b0f4e0 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b0f524 ["INT_ADD", "register:40f0:8", ["const:b0f524:8", "const:4:8"]]
+ 00b0f524 ["CALL", null, ["callee:00bdb130:8"]]
- 00b0f4e0 bytes 002f0394
+ 00b0f524 bytes 032f0394
- 00b0f4b4 ["INT_ADD", "register:40f0:8", ["const:b0f4b4:8", "const:4:8"]]
- 00b0f4b4 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b0f4f8 ["INT_ADD", "register:40f0:8", ["const:b0f4f8:8", "const:4:8"]]
+ 00b0f4f8 ["CALL", null, ["callee:00bdc180:8"]]
- 00b0f4b4 bytes 1f330394
+ 00b0f4f8 bytes 22330394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09121cb551e7a988fe3a286c6bc4903d"></a>

### [`00b0f6f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f6f4.md) → [`00b0f738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f738.md) _ZN11flatbuffers6Parser17SkipByteOrderMarkEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8c0.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdf980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf980.md)
- 新版 呼出元 1件 [`00bdf910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf910.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdf9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9d0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 92.75% / 新版 92.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0f7b8",
      "incomplete_value": true,
      "site": "00b0f7cc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b0f774",
      "incomplete_value": true,
      "site": "00b0f788",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 11,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b0f7bc",
      "incomplete_value": true,
      "site": "00b0f7d0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f4c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b0f778",
      "incomplete_value": true,
      "site": "00b0f78c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ec1:8"
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
      "00b0f7b8",
      "READ",
      [
        "storage",
        "002a1ece",
        null,
        "string"
      ]
    ],
    [
      "00b0f7bc",
      "READ",
      [
        "storage",
        "002a1ec1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0f7b8",
      "READ",
      [
        "storage",
        "002a1f59",
        null,
        "string"
      ]
    ],
    [
      "00b0f7bc",
      "READ",
      [
        "storage",
        "002a1f4c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0f768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f6f4.md#insn-00b0f768) · [`00b0f770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f6f4.md#insn-00b0f770) · [`00b0f7a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f6f4.md#insn-00b0f7a8)
- 新版 [`00b0f7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f738.md#insn-00b0f7ac) · [`00b0f7b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f738.md#insn-00b0f7b4) · [`00b0f7ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f738.md#insn-00b0f7ec)

~~~diff
- 00b0f768 ["INT_ADD", "register:40f0:8", ["const:b0f768:8", "const:4:8"]]
- 00b0f768 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b0f7ac ["INT_ADD", "register:40f0:8", ["const:b0f7ac:8", "const:4:8"]]
+ 00b0f7ac ["CALL", null, ["callee:00bdb040:8"]]
- 00b0f768 bytes 222e0394
+ 00b0f7ac bytes 252e0394
- 00b0f770 ["COPY", "tmp:0:8", ["const:ec1:8"]]
- 00b0f770 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b0f770 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b0f770 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b0f7b4 ["COPY", "tmp:0:8", ["const:f4c:8"]]
+ 00b0f7b4 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0f7b4 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b0f7b4 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b0f770 bytes 29053b91
+ 00b0f7b4 bytes 29313d91
- 00b0f7a8 ["INT_ADD", "register:40f0:8", ["const:b0f7a8:8", "const:4:8"]]
- 00b0f7a8 ["CALL", null, ["callee:00bdb260:8"]]
+ 00b0f7ec ["INT_ADD", "register:40f0:8", ["const:b0f7ec:8", "const:4:8"]]
+ 00b0f7ec ["CALL", null, ["callee:00bdb260:8"]]
- 00b0f7a8 bytes 9a2e0394
+ 00b0f7ec bytes 9d2e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2173b9c412245d7c0aaba61951302aa"></a>

### [`00b0f808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f808.md) → [`00b0f84c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f84c.md) _ZN11flatbuffers6Parser4NextEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf920.md) · 呼出先 13件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)
- 新版 呼出元 1件 [`00bdf970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf970.md) · 呼出先 13件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.47% / 新版 97.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_value` 16件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b10900",
      "incomplete_value": true,
      "site": "00b10918",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b108bc",
      "incomplete_value": true,
      "site": "00b108d4",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 147,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b10908",
      "incomplete_value": true,
      "site": "00b10918",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b108c4",
      "incomplete_value": true,
      "site": "00b108d4",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 148,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b10900",
      "incomplete_value": true,
      "site": "00b1091c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:3c1:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b108bc",
      "incomplete_value": true,
      "site": "00b108d8",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:455:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 149,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b0f934",
      "DATA",
      [
        "storage",
        "002f82fe",
        "switchD_00b0f8f8::switchdataD_002f82fe",
        "ushort"
      ]
    ],
    [
      "00b0fb58",
      "READ",
      [
        "storage",
        "00297639",
        null,
        "string"
      ]
    ],
    [
      "00b0fb58",
      "READ",
      [
        "storage",
        "002a3e11",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b0f934",
      "DATA",
      [
        "storage",
        "002f82fe",
        "switchD_00b0f93c::switchdataD_002f82fe",
        "ushort"
      ]
    ],
    [
      "00b0fb58",
      "READ",
      [
        "storage",
        "002975ac",
        null,
        "string"
      ]
    ],
    [
      "00b0fb58",
      "READ",
      [
        "storage",
        "002a3e9c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b0fd34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f808.md#insn-00b0fd34) · [`00b10634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f808.md#insn-00b10634) · [`00b10678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0f/00b0f808.md#insn-00b10678)
- 新版 [`00b0fd78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f84c.md#insn-00b0fd78) · [`00b10678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f84c.md#insn-00b10678) · [`00b106bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0f/00b0f84c.md#insn-00b106bc)

~~~diff
- 00b0fd34 ["INT_ADD", "register:40f0:8", ["const:b0fd34:8", "const:4:8"]]
- 00b0fd34 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b0fd78 ["INT_ADD", "register:40f0:8", ["const:b0fd78:8", "const:4:8"]]
+ 00b0fd78 ["CALL", null, ["callee:00bdc180:8"]]
- 00b0fd34 bytes ff300394
+ 00b0fd78 bytes 02310394
- 00b10634 ["INT_ADD", "register:40f0:8", ["const:b10634:8", "const:4:8"]]
- 00b10634 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b10678 ["INT_ADD", "register:40f0:8", ["const:b10678:8", "const:4:8"]]
+ 00b10678 ["CALL", null, ["callee:00bdb060:8"]]
- 00b10634 bytes 772a0394
+ 00b10678 bytes 7a2a0394
- 00b10678 ["INT_ADD", "register:40f0:8", ["const:b10678:8", "const:4:8"]]
- 00b10678 ["CALL", null, ["callee:00bdb260:8"]]
+ 00b106bc ["INT_ADD", "register:40f0:8", ["const:b106bc:8", "const:4:8"]]
+ 00b106bc ["CALL", null, ["callee:00bdb260:8"]]
- 00b10678 bytes e62a0394
+ 00b106bc bytes e92a0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd73ccc6db046a5f96311d09746c65b2"></a>

### [`00b10e68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10e68.md) → [`00b10eac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10eac.md) _ZN11flatbuffers6Parser6ExpectEi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf960.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdf9b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9b0.md) · 呼出先 12件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.16% / 新版 99.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b10fb8",
      "incomplete_value": false,
      "site": "00b10fc8",
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
            "const:3f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b10f74",
      "incomplete_value": false,
      "site": "00b10f84",
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
            "const:488:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b10f40",
      "DATA",
      [
        "storage",
        "00c10680",
        null,
        "pointer"
      ]
    ],
    [
      "00b10fb8",
      "PARAM",
      [
        "storage",
        "002af488",
        null,
        "string"
      ]
    ],
    [
      "00b11098",
      "DATA",
      [
        "storage",
        "00c10e80",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b10f40",
      "DATA",
      [
        "storage",
        "00c106d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b10fb8",
      "PARAM",
      [
        "storage",
        "002af3f4",
        null,
        "string"
      ]
    ],
    [
      "00b11098",
      "DATA",
      [
        "storage",
        "00c10ed0",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b10f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10e68.md#insn-00b10f84) · [`00b10eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10e68.md#insn-00b10eac) · [`00b10ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b10/00b10e68.md#insn-00b10ed4)
- 新版 [`00b10fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10eac.md#insn-00b10fc8) · [`00b10ef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10eac.md#insn-00b10ef0) · [`00b10f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b10/00b10eac.md#insn-00b10f18)

~~~diff
- 00b10f84 ["INT_ADD", "register:40f0:8", ["const:b10f84:8", "const:4:8"]]
- 00b10f84 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b10fc8 ["INT_ADD", "register:40f0:8", ["const:b10fc8:8", "const:4:8"]]
+ 00b10fc8 ["CALL", null, ["callee:00bdc180:8"]]
- 00b10f84 bytes 6b2c0394
+ 00b10fc8 bytes 6e2c0394
- 00b10eac ["INT_ADD", "register:40f0:8", ["const:b10eac:8", "const:4:8"]]
- 00b10eac ["CALL", null, ["callee:00bdf970:8"]]
+ 00b10ef0 ["INT_ADD", "register:40f0:8", ["const:b10ef0:8", "const:4:8"]]
+ 00b10ef0 ["CALL", null, ["callee:00bdf970:8"]]
- 00b10eac bytes 9d3a0394
+ 00b10ef0 bytes a03a0394
- 00b10ed4 ["COPY", "tmp:0:8", ["const:e80:8"]]
- 00b10ed4 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
- 00b10ed4 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
- 00b10ed4 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
+ 00b10f18 ["COPY", "tmp:0:8", ["const:ed0:8"]]
+ 00b10f18 ["INT_CARRY", "register:105:1", ["register:40d0:8", "tmp:0:8"]]
+ 00b10f18 ["INT_SCARRY", "register:106:1", ["register:40d0:8", "tmp:0:8"]]
+ 00b10f18 ["INT_ADD", "tmp:1:8", ["register:40d0:8", "tmp:0:8"]]
- 00b10ed4 bytes 5a033a91
+ 00b10f18 bytes 5a433b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44b0dadbf3e2ff76c06f4c473344c5a5"></a>

### [`00b11684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11684.md) → [`00b116c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b116c8.md) _ZN11flatbuffers6Parser18LookupCreateStructERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEbb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf8d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8d0.md) · 呼出先 16件 [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 1件 [`00bdf920`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf920.md) · 呼出先 16件 [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.69% / 新版 99.69%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b11980",
      "incomplete_value": false,
      "site": "00b11988",
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
            "const:3cd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1193c",
      "incomplete_value": false,
      "site": "00b11944",
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
            "const:342:8"
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
      "00b11980",
      "PARAM",
      [
        "storage",
        "002a0342",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b11980",
      "PARAM",
      [
        "storage",
        "002a03cd",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b11944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11684.md#insn-00b11944) · [`00b116cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11684.md#insn-00b116cc) · [`00b116dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11684.md#insn-00b116dc)
- 新版 [`00b11988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b116c8.md#insn-00b11988) · [`00b11710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b116c8.md#insn-00b11710) · [`00b11720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b116c8.md#insn-00b11720)

~~~diff
- 00b11944 ["INT_ADD", "register:40f0:8", ["const:b11944:8", "const:4:8"]]
- 00b11944 ["CALL", null, ["callee:00afaa08:8"]]
+ 00b11988 ["INT_ADD", "register:40f0:8", ["const:b11988:8", "const:4:8"]]
+ 00b11988 ["CALL", null, ["callee:00afaa08:8"]]
- 00b11944 bytes 20a4ff97
+ 00b11988 bytes 20a4ff97
- 00b116cc ["INT_ADD", "register:40f0:8", ["const:b116cc:8", "const:4:8"]]
- 00b116cc ["CALL", null, ["callee:00bdfc70:8"]]
+ 00b11710 ["INT_ADD", "register:40f0:8", ["const:b11710:8", "const:4:8"]]
+ 00b11710 ["CALL", null, ["callee:00bdfc70:8"]]
- 00b116cc bytes 55390394
+ 00b11710 bytes 58390394
- 00b116dc ["INT_ADD", "register:40f0:8", ["const:b116dc:8", "const:4:8"]]
- 00b116dc ["CALL", null, ["callee:00bdfcd0:8"]]
+ 00b11720 ["INT_ADD", "register:40f0:8", ["const:b11720:8", "const:4:8"]]
+ 00b11720 ["CALL", null, ["callee:00bdfcd0:8"]]
- 00b116dc bytes 69390394
+ 00b11720 bytes 6c390394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9a368b1b142bcc9373bb5bee0e1eba7"></a>

### [`00b11b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11b94.md) → [`00b11bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11bd8.md) _ZN11flatbuffers6Parser9ParseTypeERNS_4TypeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b11b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11b94.md) [`00bdf9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf9e0.md) · 呼出先 12件 [`00b11b94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11b94.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 2件 [`00b11bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11bd8.md) [`00bdfa30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa30.md) · 呼出先 12件 [`00b11bd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11bd8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.68% / 新版 93.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b11dc4",
      "incomplete_value": true,
      "site": "00b11dc4",
      "value": [
        "LOAD",
        "8",
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
                "const:2f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b11d80",
      "incomplete_value": true,
      "site": "00b11d80",
      "value": [
        "LOAD",
        "8",
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
                "const:2f:8"
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
      "definition_site": "00b11db0",
      "incomplete_value": true,
      "site": "00b11dc8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b11d6c",
      "incomplete_value": true,
      "site": "00b11d84",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b11db0",
      "incomplete_value": true,
      "site": "00b11dc8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b11d6c",
      "incomplete_value": true,
      "site": "00b11d84",
      "value": [
        "LOAD",
        "16",
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
      "00b11c50",
      "DATA",
      [
        "storage",
        "002f84a8",
        "switchD_00b11c14::switchdataD_002f84a8",
        "byte"
      ]
    ],
    [
      "00b11c68",
      "PARAM",
      [
        "storage",
        "002a0f33",
        null,
        null
      ]
    ],
    [
      "00b11cd4",
      "READ",
      [
        "storage",
        "002a1ef3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b11c50",
      "DATA",
      [
        "storage",
        "002f84a8",
        "switchD_00b11c58::switchdataD_002f84a8",
        "byte"
      ]
    ],
    [
      "00b11c68",
      "PARAM",
      [
        "storage",
        "002a0fbe",
        null,
        null
      ]
    ],
    [
      "00b11cd4",
      "READ",
      [
        "storage",
        "002a1f7e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b11c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11b94.md#insn-00b11c08) · [`00b11c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11b94.md#insn-00b11c24) · [`00b11c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b11/00b11b94.md#insn-00b11c30)
- 新版 [`00b11c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11bd8.md#insn-00b11c4c) · [`00b11c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11bd8.md#insn-00b11c68) · [`00b11c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b11/00b11bd8.md#insn-00b11c74)

~~~diff
- 00b11c08 ["COPY", "register:4050:8", ["const:b11c18:8"]]
+ 00b11c4c ["COPY", "register:4050:8", ["const:b11c5c:8"]]
- 00b11c08 bytes 8a000010
+ 00b11c4c bytes 8a000010
- 00b11c24 ["COPY", "tmp:0:8", ["const:f33:8"]]
- 00b11c24 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b11c24 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b11c24 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b11c68 ["COPY", "tmp:0:8", ["const:fbe:8"]]
+ 00b11c68 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b11c68 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b11c68 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b11c24 bytes 21cc3c91
+ 00b11c68 bytes 21f83e91
- 00b11c30 ["INT_ADD", "register:40f0:8", ["const:b11c30:8", "const:4:8"]]
- 00b11c30 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b11c74 ["INT_ADD", "register:40f0:8", ["const:b11c74:8", "const:4:8"]]
+ 00b11c74 ["CALL", null, ["callee:00bdb200:8"]]
- 00b11c30 bytes 60250394
+ 00b11c74 bytes 63250394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-269c4b5589ca1d10a475d277f9588742"></a>

### [`00b12300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b12300.md) → [`00b12344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12344.md) _ZN11flatbuffers6Parser8AddFieldERNS_9StructDefERKNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEERKNS_4TypeEPPNS_8FieldD

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf990.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)
- 新版 呼出元 1件 [`00bdf9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9e0.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.38% / 新版 99.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b123c4",
      "incomplete_value": false,
      "site": "00b123e8",
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
            "const:4cc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b12380",
      "incomplete_value": false,
      "site": "00b123a4",
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
            "const:432:8"
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
      "00b123c4",
      "PARAM",
      [
        "storage",
        "002a7432",
        null,
        null
      ]
    ],
    [
      "00b124c8",
      "READ",
      [
        "storage",
        "00c1b9d8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b123c4",
      "PARAM",
      [
        "storage",
        "002a74cc",
        null,
        null
      ]
    ],
    [
      "00b124c8",
      "READ",
      [
        "storage",
        "00c1ba28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b123a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b12300.md#insn-00b123a4) · [`00b12348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b12300.md#insn-00b12348) · [`00b12380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b12300.md#insn-00b12380)
- 新版 [`00b123e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12344.md#insn-00b123e8) · [`00b1238c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12344.md#insn-00b1238c) · [`00b123c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12344.md#insn-00b123c4)

~~~diff
- 00b123a4 ["INT_ADD", "register:40f0:8", ["const:b123a4:8", "const:4:8"]]
- 00b123a4 ["CALL", null, ["callee:00bde740:8"]]
+ 00b123e8 ["INT_ADD", "register:40f0:8", ["const:b123e8:8", "const:4:8"]]
+ 00b123e8 ["CALL", null, ["callee:00bde740:8"]]
- 00b123a4 bytes d3300394
+ 00b123e8 bytes d6300394
- 00b12348 ["INT_ADD", "register:40f0:8", ["const:b12348:8", "const:4:8"]]
- 00b12348 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b1238c ["INT_ADD", "register:40f0:8", ["const:b1238c:8", "const:4:8"]]
+ 00b1238c ["CALL", null, ["callee:00bdb040:8"]]
- 00b12348 bytes 2a230394
+ 00b1238c bytes 2d230394
- 00b12380 ["COPY", "tmp:0:8", ["const:432:8"]]
- 00b12380 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b12380 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b12380 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b123c4 ["COPY", "tmp:0:8", ["const:4cc:8"]]
+ 00b123c4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b123c4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b123c4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b12380 bytes 21c81091
+ 00b123c4 bytes 21301391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23bf3522a0eab7409643c329a46258a4"></a>

### [`00b127dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b127dc.md) → [`00b12820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12820.md) _ZN11flatbuffers6Parser10ParseFieldERNS_9StructDefE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf700.md) · 呼出先 26件 [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 1件 [`00bdf750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf750.md) · 呼出先 26件 [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 93.79% / 新版 93.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 10件, `store_value` 38件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b12914",
      "incomplete_value": true,
      "site": "00b1292c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b128d0",
      "incomplete_value": true,
      "site": "00b128e8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 25,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1291c",
      "incomplete_value": true,
      "site": "00b1292c",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b128d8",
      "incomplete_value": true,
      "site": "00b128e8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 26,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b12914",
      "incomplete_value": true,
      "site": "00b12930",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5c3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b128d0",
      "incomplete_value": true,
      "site": "00b128ec",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:650:8"
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
      "00b12914",
      "READ",
      [
        "storage",
        "00297650",
        null,
        "string"
      ]
    ],
    [
      "00b12914",
      "READ",
      [
        "storage",
        "00297660",
        null,
        "string"
      ]
    ],
    [
      "00b1291c",
      "READ",
      [
        "storage",
        "00297670",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b12914",
      "READ",
      [
        "storage",
        "002975c3",
        null,
        "string"
      ]
    ],
    [
      "00b12914",
      "READ",
      [
        "storage",
        "002975d3",
        null,
        "string"
      ]
    ],
    [
      "00b1291c",
      "READ",
      [
        "storage",
        "002975e3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b12fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b127dc.md#insn-00b12fe0) · [`00b132c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b127dc.md#insn-00b132c8) · [`00b132d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b12/00b127dc.md#insn-00b132d8)
- 新版 [`00b13024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12820.md#insn-00b13024) · [`00b1330c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12820.md#insn-00b1330c) · [`00b1331c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b12/00b12820.md#insn-00b1331c)

~~~diff
- 00b12fe0 ["INT_ADD", "register:40f0:8", ["const:b12fe0:8", "const:4:8"]]
- 00b12fe0 ["CALL", null, ["callee:00bdf820:8"]]
+ 00b13024 ["INT_ADD", "register:40f0:8", ["const:b13024:8", "const:4:8"]]
+ 00b13024 ["CALL", null, ["callee:00bdf820:8"]]
- 00b12fe0 bytes fc310394
+ 00b13024 bytes ff310394
- 00b132c8 ["INT_ADD", "register:40f0:8", ["const:b132c8:8", "const:4:8"]]
- 00b132c8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b1330c ["INT_ADD", "register:40f0:8", ["const:b1330c:8", "const:4:8"]]
+ 00b1330c ["CALL", null, ["callee:00bdb060:8"]]
- 00b132c8 bytes 521f0394
+ 00b1330c bytes 551f0394
- 00b132d8 ["INT_ADD", "register:40f0:8", ["const:b132d8:8", "const:4:8"]]
- 00b132d8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b1331c ["INT_ADD", "register:40f0:8", ["const:b1331c:8", "const:4:8"]]
+ 00b1331c ["CALL", null, ["callee:00bdb060:8"]]
- 00b132d8 bytes 4e1f0394
+ 00b1331c bytes 511f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6c9b4a645d148a363ec051bcb6c5cde"></a>

### [`00b13df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b13/00b13df8.md) → [`00b13e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e3c.md) _ZN11flatbuffers6Parser16ParseSingleValueEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_5ValueEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdf8a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8a0.md) · 呼出先 34件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdf8f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf8f0.md) · 呼出先 34件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.65% / 新版 97.65%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 7件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b14088",
      "incomplete_value": true,
      "site": "00b14098",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b14044",
      "incomplete_value": true,
      "site": "00b14054",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 22,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1409c",
      "incomplete_value": true,
      "site": "00b140a0",
      "value": [
        "LOAD",
        "16",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b14058",
      "incomplete_value": true,
      "site": "00b1405c",
      "value": [
        "LOAD",
        "16",
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
                "const:40:8"
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
      "definition_site": "00b1409c",
      "incomplete_value": true,
      "site": "00b140a0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b14058",
      "incomplete_value": true,
      "site": "00b1405c",
      "value": [
        "LOAD",
        "16",
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
      "00b14088",
      "READ",
      [
        "storage",
        "002af50a",
        null,
        "string"
      ]
    ],
    [
      "00b14088",
      "READ",
      [
        "storage",
        "002af51a",
        null,
        "string"
      ]
    ],
    [
      "00b14090",
      "READ",
      [
        "storage",
        "002af549",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b14088",
      "READ",
      [
        "storage",
        "002af476",
        null,
        "string"
      ]
    ],
    [
      "00b14088",
      "READ",
      [
        "storage",
        "002af486",
        null,
        "string"
      ]
    ],
    [
      "00b14090",
      "READ",
      [
        "storage",
        "002af4b5",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b14030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b13/00b13df8.md#insn-00b14030) · [`00b14084`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b13/00b13df8.md#insn-00b14084) · [`00b140c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b13/00b13df8.md#insn-00b140c0)
- 新版 [`00b14074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e3c.md#insn-00b14074) · [`00b140c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e3c.md#insn-00b140c8) · [`00b14104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b13/00b13e3c.md#insn-00b14104)

~~~diff
- 00b14030 ["INT_ADD", "register:40f0:8", ["const:b14030:8", "const:4:8"]]
- 00b14030 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b14074 ["INT_ADD", "register:40f0:8", ["const:b14074:8", "const:4:8"]]
+ 00b14074 ["CALL", null, ["callee:00bdb040:8"]]
- 00b14030 bytes f01b0394
+ 00b14074 bytes f31b0394
- 00b14084 ["INT_ADD", "register:40f0:8", ["const:b14084:8", "const:4:8"]]
- 00b14084 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b140c8 ["INT_ADD", "register:40f0:8", ["const:b140c8:8", "const:4:8"]]
+ 00b140c8 ["CALL", null, ["callee:00bdb190:8"]]
- 00b14084 bytes 2f1c0394
+ 00b140c8 bytes 321c0394
- 00b140c0 ["INT_ADD", "register:40f0:8", ["const:b140c0:8", "const:4:8"]]
- 00b140c0 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b14104 ["INT_ADD", "register:40f0:8", ["const:b14104:8", "const:4:8"]]
+ 00b14104 ["CALL", null, ["callee:00bdb130:8"]]
- 00b140c0 bytes 081c0394
+ 00b14104 bytes 0b1c0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-20d7a56e34f8d248e48171d83e193ad9"></a>

### [`00b14fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b14/00b14fc8.md) → [`00b1500c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b1500c.md) _ZN11flatbuffers6Parser13ParseMetaDataEPNS_11SymbolTableINS_5ValueEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf7d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf7d0.md) · 呼出先 13件 [`00613fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00613/00613fbc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdf820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf820.md) · 呼出先 13件 [`00613fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00613/00613fbc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.06% / 新版 99.06%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b15174",
      "incomplete_value": false,
      "site": "00b15184",
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
            "const:4cc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b15130",
      "incomplete_value": false,
      "site": "00b15140",
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
            "const:432:8"
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
      "definition_site": "00b152a0",
      "incomplete_value": true,
      "site": "00b152a4",
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
            "const:39b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1525c",
      "incomplete_value": true,
      "site": "00b15260",
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
            "const:428:8"
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
      "00b15174",
      "PARAM",
      [
        "storage",
        "002a7432",
        null,
        null
      ]
    ],
    [
      "00b152a0",
      "PARAM",
      [
        "storage",
        "00295428",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b15174",
      "PARAM",
      [
        "storage",
        "002a74cc",
        null,
        null
      ]
    ],
    [
      "00b152a0",
      "PARAM",
      [
        "storage",
        "0029539b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b15140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b14/00b14fc8.md#insn-00b15140) · [`00b1521c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b14/00b14fc8.md#insn-00b1521c) · [`00b15260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b14/00b14fc8.md#insn-00b15260)
- 新版 [`00b15184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b1500c.md#insn-00b15184) · [`00b15260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b1500c.md#insn-00b15260) · [`00b152a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b1500c.md#insn-00b152a4)

~~~diff
- 00b15140 ["INT_ADD", "register:40f0:8", ["const:b15140:8", "const:4:8"]]
- 00b15140 ["CALL", null, ["callee:00bde740:8"]]
+ 00b15184 ["INT_ADD", "register:40f0:8", ["const:b15184:8", "const:4:8"]]
+ 00b15184 ["CALL", null, ["callee:00bde740:8"]]
- 00b15140 bytes 6c250394
+ 00b15184 bytes 6f250394
- 00b1521c ["INT_ADD", "register:40f0:8", ["const:b1521c:8", "const:4:8"]]
- 00b1521c ["CALL", null, ["callee:00bdb060:8"]]
+ 00b15260 ["INT_ADD", "register:40f0:8", ["const:b15260:8", "const:4:8"]]
+ 00b15260 ["CALL", null, ["callee:00bdb060:8"]]
- 00b1521c bytes 7d170394
+ 00b15260 bytes 80170394
- 00b15260 ["INT_ADD", "register:40f0:8", ["const:b15260:8", "const:4:8"]]
- 00b15260 ["CALL", null, ["callee:00bdb260:8"]]
+ 00b152a4 ["INT_ADD", "register:40f0:8", ["const:b152a4:8", "const:4:8"]]
+ 00b152a4 ["CALL", null, ["callee:00bdb260:8"]]
- 00b15260 bytes ec170394
+ 00b152a4 bytes ef170394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cdc687f8cb9f13c27d995c4c2dd01273"></a>

### [`00b1567c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1567c.md) → [`00b156c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b156c0.md) _ZN11flatbuffers11NumToStringIjEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf160.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb310.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 1件 [`00bdf1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1b0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb360.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.91% / 新版 87.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1571c",
      "incomplete_value": true,
      "site": "00b15730",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b156d8",
      "incomplete_value": true,
      "site": "00b156ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b15714",
      "incomplete_value": true,
      "site": "00b15734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b156d0",
      "incomplete_value": true,
      "site": "00b156f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b157a4",
      "incomplete_value": true,
      "site": "00b157b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b15760",
      "incomplete_value": true,
      "site": "00b1576c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b156f4",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "00b156f8",
      "READ",
      [
        "storage",
        "00c1b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b15730",
      "DATA",
      [
        "storage",
        "00c110f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b156f4",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "00b156f8",
      "READ",
      [
        "storage",
        "00c1ba48",
        null,
        "pointer"
      ]
    ],
    [
      "00b15730",
      "DATA",
      [
        "storage",
        "00c11140",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b157b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1567c.md#insn-00b157b0) · [`00b156b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1567c.md#insn-00b156b0) · [`00b156b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1567c.md#insn-00b156b4)
- 新版 [`00b157f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b156c0.md#insn-00b157f4) · [`00b156f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b156c0.md#insn-00b156f4) · [`00b156f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b156c0.md#insn-00b156f8)

~~~diff
- 00b157b0 ["INT_ADD", "register:40f0:8", ["const:b157b0:8", "const:4:8"]]
- 00b157b0 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b157f4 ["INT_ADD", "register:40f0:8", ["const:b157f4:8", "const:4:8"]]
+ 00b157f4 ["CALL", null, ["callee:00be01e0:8"]]
- 00b157b0 bytes 782a0394
+ 00b157f4 bytes 7b2a0394
- 00b156b0 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:dd8:8"]]
- 00b156b0 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b156f4 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:e28:8"]]
+ 00b156f4 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b156b0 bytes 5aef46f9
+ 00b156f4 bytes 5a1747f9
- 00b156b4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9f8:8"]]
- 00b156b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b156f8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a48:8"]]
+ 00b156f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b156b4 bytes 08fd44f9
+ 00b156f8 bytes 082545f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63ca7c788f0dfc07071ab2501136823a"></a>

### [`00b1582c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1582c.md) → [`00b15870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b15870.md) _ZN11flatbuffers6Parser13ParseAnyValueERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefEjb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b1582c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1582c.md) [`00bdf7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf7b0.md) · 呼出先 28件 [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00b1582c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1582c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 2件 [`00b15870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b15870.md) [`00bdf800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf800.md) · 呼出先 28件 [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) [`00b15870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b15870.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.73% / 新版 99.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b15ba8",
      "incomplete_value": false,
      "site": "00b15bb4",
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
            "const:81f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b15b64",
      "incomplete_value": false,
      "site": "00b15b70",
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
            "const:821:8"
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
      "00b158c8",
      "DATA",
      [
        "storage",
        "002f84c6",
        "switchD_00b15898::switchdataD_002f84c6",
        "byte"
      ]
    ],
    [
      "00b15ba8",
      "PARAM",
      [
        "storage",
        "0029a821",
        null,
        "string"
      ]
    ],
    [
      "00b15fb0",
      "PARAM",
      [
        "storage",
        "002a1f07",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b158c8",
      "DATA",
      [
        "storage",
        "002f84c6",
        "switchD_00b158dc::switchdataD_002f84c6",
        "byte"
      ]
    ],
    [
      "00b15ba8",
      "PARAM",
      [
        "storage",
        "0029a81f",
        null,
        "string"
      ]
    ],
    [
      "00b15fb0",
      "PARAM",
      [
        "storage",
        "002a1f92",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b15b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1582c.md#insn-00b15b70) · [`00b15880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1582c.md#insn-00b15880) · [`00b158c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b15/00b1582c.md#insn-00b158c8)
- 新版 [`00b15bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b15870.md#insn-00b15bb4) · [`00b158c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b15870.md#insn-00b158c4) · [`00b1590c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b15/00b15870.md#insn-00b1590c)

~~~diff
- 00b15b70 ["INT_ADD", "register:40f0:8", ["const:b15b70:8", "const:4:8"]]
- 00b15b70 ["CALL", null, ["callee:00afaa08:8"]]
+ 00b15bb4 ["INT_ADD", "register:40f0:8", ["const:b15bb4:8", "const:4:8"]]
+ 00b15bb4 ["CALL", null, ["callee:00afaa08:8"]]
- 00b15b70 bytes 9593ff97
+ 00b15bb4 bytes 9593ff97
- 00b15880 ["COPY", "register:4050:8", ["const:b1589c:8"]]
+ 00b158c4 ["COPY", "register:4050:8", ["const:b158e0:8"]]
- 00b15880 bytes ea000010
+ 00b158c4 bytes ea000010
- 00b158c8 ["INT_ADD", "register:40f0:8", ["const:b158c8:8", "const:4:8"]]
- 00b158c8 ["CALL", null, ["callee:00bdfc90:8"]]
+ 00b1590c ["INT_ADD", "register:40f0:8", ["const:b1590c:8", "const:4:8"]]
+ 00b1590c ["CALL", null, ["callee:00bdfc90:8"]]
- 00b158c8 bytes de280394
+ 00b1590c bytes e1280394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1d85c6d99e2be742519b7deab45b9d7"></a>

### [`00b163f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b163f0.md) → [`00b16434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16434.md) _ZN11flatbuffers4atotIjEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf690.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdf6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf6e0.md) · 呼出先 12件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.19% / 新版 98.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b165b4",
      "incomplete_value": false,
      "site": "00b165c8",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b16570",
      "incomplete_value": false,
      "site": "00b16584",
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
            "const:20f:8"
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
      "definition_site": "00b165d8",
      "incomplete_value": false,
      "site": "00b165f8",
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
            "const:41f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b16594",
      "incomplete_value": false,
      "site": "00b165b4",
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
            "const:394:8"
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
      "definition_site": "00b166c0",
      "incomplete_value": false,
      "site": "00b166d4",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1667c",
      "incomplete_value": false,
      "site": "00b16690",
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
            "const:20f:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b165b4",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b165d8",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b166c0",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b165b4",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ],
    [
      "00b165d8",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b166c0",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b16570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b163f0.md#insn-00b16570) · [`00b16584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b163f0.md#insn-00b16584) · [`00b165b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b163f0.md#insn-00b165b4)
- 新版 [`00b165b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16434.md#insn-00b165b4) · [`00b165c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16434.md#insn-00b165c8) · [`00b165f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16434.md#insn-00b165f8)

~~~diff
- 00b16570 ["COPY", "tmp:0:8", ["const:20f:8"]]
- 00b16570 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b16570 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b16570 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b165b4 ["COPY", "tmp:0:8", ["const:2a9:8"]]
+ 00b165b4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b165b4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b165b4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b16570 bytes 423c0891
+ 00b165b4 bytes 42a40a91
- 00b16584 ["INT_ADD", "register:40f0:8", ["const:b16584:8", "const:4:8"]]
- 00b16584 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b165c8 ["INT_ADD", "register:40f0:8", ["const:b165c8:8", "const:4:8"]]
+ 00b165c8 ["CALL", null, ["callee:00bdc180:8"]]
- 00b16584 bytes eb160394
+ 00b165c8 bytes ee160394
- 00b165b4 ["INT_ADD", "register:40f0:8", ["const:b165b4:8", "const:4:8"]]
- 00b165b4 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b165f8 ["INT_ADD", "register:40f0:8", ["const:b165f8:8", "const:4:8"]]
+ 00b165f8 ["CALL", null, ["callee:00bdb130:8"]]
- 00b165b4 bytes cb120394
+ 00b165f8 bytes ce120394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-425b4ee5c8a96542bcdd40017cbc3ab5"></a>

### [`00b16c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16c88.md) → [`00b16ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16ccc.md) _ZN11flatbuffers4atotIhEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf670.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdf6c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf6c0.md) · 呼出先 12件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.19% / 新版 98.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b16e4c",
      "incomplete_value": false,
      "site": "00b16e60",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b16e08",
      "incomplete_value": false,
      "site": "00b16e1c",
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
            "const:20f:8"
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
      "definition_site": "00b16e70",
      "incomplete_value": false,
      "site": "00b16e90",
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
            "const:41f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b16e2c",
      "incomplete_value": false,
      "site": "00b16e4c",
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
            "const:394:8"
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
      "definition_site": "00b16f58",
      "incomplete_value": false,
      "site": "00b16f6c",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b16f14",
      "incomplete_value": false,
      "site": "00b16f28",
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
            "const:20f:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b16e4c",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b16e70",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b16f58",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b16e4c",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ],
    [
      "00b16e70",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b16f58",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b16e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16c88.md#insn-00b16e08) · [`00b16e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16c88.md#insn-00b16e1c) · [`00b16e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b16/00b16c88.md#insn-00b16e4c)
- 新版 [`00b16e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16ccc.md#insn-00b16e4c) · [`00b16e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16ccc.md#insn-00b16e60) · [`00b16e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b16/00b16ccc.md#insn-00b16e90)

~~~diff
- 00b16e08 ["COPY", "tmp:0:8", ["const:20f:8"]]
- 00b16e08 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b16e08 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b16e08 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b16e4c ["COPY", "tmp:0:8", ["const:2a9:8"]]
+ 00b16e4c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b16e4c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b16e4c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b16e08 bytes 423c0891
+ 00b16e4c bytes 42a40a91
- 00b16e1c ["INT_ADD", "register:40f0:8", ["const:b16e1c:8", "const:4:8"]]
- 00b16e1c ["CALL", null, ["callee:00bdc180:8"]]
+ 00b16e60 ["INT_ADD", "register:40f0:8", ["const:b16e60:8", "const:4:8"]]
+ 00b16e60 ["CALL", null, ["callee:00bdc180:8"]]
- 00b16e1c bytes c5140394
+ 00b16e60 bytes c8140394
- 00b16e4c ["INT_ADD", "register:40f0:8", ["const:b16e4c:8", "const:4:8"]]
- 00b16e4c ["CALL", null, ["callee:00bdb130:8"]]
+ 00b16e90 ["INT_ADD", "register:40f0:8", ["const:b16e90:8", "const:4:8"]]
+ 00b16e90 ["CALL", null, ["callee:00bdb130:8"]]
- 00b16e4c bytes a5100394
+ 00b16e90 bytes a8100394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9b057c7e7e9a77a27e48f69433cefaa"></a>

### [`00b1711c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md) → [`00b17160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17160.md) _ZN11flatbuffers6Parser10ParseTableERKNS_9StructDefEPNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEEPj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf710.md) · 呼出先 37件 [`00b3fc88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3f/00b3fc88.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 1件 [`00bdf760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf760.md) · 呼出先 37件 [`00b3fccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3f/00b3fccc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.66% / 新版 99.66%

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
      "definition_site": "00b17908",
      "incomplete_value": true,
      "site": "00b17908",
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
      "definition_site": "00b178c4",
      "incomplete_value": true,
      "site": "00b178c4",
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
    "ordinal": 69,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b17684",
      "incomplete_value": false,
      "site": "00b1768c",
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
            "const:753:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b17640",
      "incomplete_value": false,
      "site": "00b17648",
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
            "const:7e0:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b17694",
      "incomplete_value": false,
      "site": "00b176a0",
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
            "const:21c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b17650",
      "incomplete_value": false,
      "site": "00b1765c",
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
            "const:2a9:8"
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
      "00b172f0",
      "READ",
      [
        "storage",
        "0029987d",
        null,
        "string"
      ]
    ],
    [
      "00b172f0",
      "READ",
      [
        "storage",
        "0029988d",
        null,
        "string"
      ]
    ],
    [
      "00b172f4",
      "READ",
      [
        "storage",
        "0029989c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b172f0",
      "READ",
      [
        "storage",
        "002997f0",
        null,
        "string"
      ]
    ],
    [
      "00b172f0",
      "READ",
      [
        "storage",
        "00299800",
        null,
        "string"
      ]
    ],
    [
      "00b172f4",
      "READ",
      [
        "storage",
        "0029980f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b17648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md#insn-00b17648) · [`00b1765c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md#insn-00b1765c) · [`00b17908`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b17/00b1711c.md#insn-00b17908)
- 新版 [`00b1768c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17160.md#insn-00b1768c) · [`00b176a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17160.md#insn-00b176a0) · [`00b1794c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b17/00b17160.md#insn-00b1794c)

~~~diff
- 00b17648 ["INT_ADD", "register:40f0:8", ["const:b17648:8", "const:4:8"]]
- 00b17648 ["CALL", null, ["callee:00bdb260:8"]]
+ 00b1768c ["INT_ADD", "register:40f0:8", ["const:b1768c:8", "const:4:8"]]
+ 00b1768c ["CALL", null, ["callee:00bdb260:8"]]
- 00b17648 bytes f20e0394
+ 00b1768c bytes f50e0394
- 00b1765c ["INT_ADD", "register:40f0:8", ["const:b1765c:8", "const:4:8"]]
- 00b1765c ["CALL", null, ["callee:00bdb130:8"]]
+ 00b176a0 ["INT_ADD", "register:40f0:8", ["const:b176a0:8", "const:4:8"]]
+ 00b176a0 ["CALL", null, ["callee:00bdb130:8"]]
- 00b1765c bytes a10e0394
+ 00b176a0 bytes a40e0394
- 00b17908 ["INT_ADD", "register:40f0:8", ["const:b17908:8", "const:4:8"]]
- 00b17908 ["CALL", null, ["callee:00bdf390:8"]]
+ 00b1794c ["INT_ADD", "register:40f0:8", ["const:b1794c:8", "const:4:8"]]
+ 00b1794c ["CALL", null, ["callee:00bdf390:8"]]
- 00b17908 bytes 8e1e0394
+ 00b1794c bytes 911e0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b4c744d8c2152df85d409743a2d133b"></a>

### [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) → [`00b18d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md) _ZN11flatbuffers6Parser11ParseVectorERKNS_4TypeEPjPNS_8FieldDefEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf760.md) · 呼出先 32件 [`00b1cd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md) [`00b1ce44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md) [`00b40b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40b10.md) [`00bdafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafb0.md) [`00bdafd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdafd0.md)
- 新版 呼出元 1件 [`00bdf7b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf7b0.md) · 呼出先 32件 [`00b1cd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cd54.md) [`00b1ce88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1ce88.md) [`00b40b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40b54.md) [`00bdb000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb000.md) [`00bdb020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 97.62% / 新版 97.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 2件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b18de0",
      "incomplete_value": true,
      "site": "00b18de0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b18d9c",
      "incomplete_value": true,
      "site": "00b18d9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 31,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b1956c",
      "incomplete_value": false,
      "site": "00b1956c",
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
            "const:f14:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b19528",
      "incomplete_value": false,
      "site": "00b19528",
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
            "const:ed4:8"
          ]
        ]
      ]
    },
    "ordinal": 70,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b19598",
      "incomplete_value": false,
      "site": "00b19598",
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
    "old": {
      "definition_site": "00b19554",
      "incomplete_value": false,
      "site": "00b19554",
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
            "const:ee0:8"
          ]
        ]
      ]
    },
    "ordinal": 71,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b18db4",
      "READ",
      [
        "storage",
        "002af449",
        null,
        "string"
      ]
    ],
    [
      "00b18f14",
      "READ",
      [
        "storage",
        "00c1b9d8",
        null,
        "pointer"
      ]
    ],
    [
      "00b190bc",
      "DATA",
      [
        "storage",
        "002f84e3",
        "switchD_00b19080::switchdataD_002f84e3",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00b18db4",
      "READ",
      [
        "storage",
        "002af3b5",
        null,
        "string"
      ]
    ],
    [
      "00b18f14",
      "READ",
      [
        "storage",
        "00c1ba28",
        null,
        "pointer"
      ]
    ],
    [
      "00b190bc",
      "DATA",
      [
        "storage",
        "002f84e3",
        "switchD_00b190c4::switchdataD_002f84e3",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b19510`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md#insn-00b19510) · [`00b19528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md#insn-00b19528) · [`00b1952c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md#insn-00b1952c)
- 新版 [`00b19554`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md#insn-00b19554) · [`00b1956c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md#insn-00b1956c) · [`00b19570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md#insn-00b19570)

~~~diff
- 00b19510 ["INT_ADD", "register:40f0:8", ["const:b19510:8", "const:4:8"]]
- 00b19510 ["CALL", null, ["callee:00bdb000:8"]]
+ 00b19554 ["INT_ADD", "register:40f0:8", ["const:b19554:8", "const:4:8"]]
+ 00b19554 ["CALL", null, ["callee:00bdb000:8"]]
- 00b19510 bytes a8060394
+ 00b19554 bytes ab060394
- 00b19528 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:ed4:8"]]
- 00b19528 ["COPY", "tmp:1:4", ["register:4040:4"]]
- 00b19528 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
+ 00b1956c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:f14:8"]]
+ 00b1956c ["COPY", "tmp:1:4", ["register:4040:4"]]
+ 00b1956c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:2"]]
- 00b19528 bytes 28a91d79
+ 00b1956c bytes 28291e79
- 00b1952c ["INT_ADD", "register:40f0:8", ["const:b1952c:8", "const:4:8"]]
- 00b1952c ["CALL", null, ["callee:00bdb020:8"]]
+ 00b19570 ["INT_ADD", "register:40f0:8", ["const:b19570:8", "const:4:8"]]
+ 00b19570 ["CALL", null, ["callee:00bdb020:8"]]
- 00b1952c bytes a9060394
+ 00b19570 bytes ac060394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2107defc0b24c84a8473ff22d0db0ad"></a>

### [`00b19c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19c18.md) → [`00b19c5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b19c5c.md) _ZN11flatbuffers6Parser9ParseHashERNS_5ValueEPNS_8FieldDefE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdf9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf9c0.md) · 呼出先 11件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde980.md) [`00bdf150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf150.md) [`00bdf160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf160.md)
- 新版 呼出元 1件 [`00bdfa10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa10.md) · 呼出先 11件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde9d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde9d0.md) [`00bdf1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1a0.md) [`00bdf1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 8件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b19da8",
      "incomplete_value": false,
      "site": "00b19db0",
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
            "const:16e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b19d64",
      "incomplete_value": false,
      "site": "00b19d6c",
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
            "const:e3:8"
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
      "definition_site": "00b19ddc",
      "incomplete_value": false,
      "site": "00b19de4",
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
            "const:165:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b19d98",
      "incomplete_value": false,
      "site": "00b19da0",
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
            "const:da:8"
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
      "definition_site": "00b19e10",
      "incomplete_value": false,
      "site": "00b19e18",
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
            "const:165:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b19dcc",
      "incomplete_value": false,
      "site": "00b19dd4",
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
            "const:da:8"
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
      "00b19cf8",
      "DATA",
      [
        "storage",
        "002f8507",
        "switchD_00b19cbc::switchdataD_002f8507",
        "byte"
      ]
    ],
    [
      "00b19da8",
      "PARAM",
      [
        "storage",
        "002a00e3",
        null,
        "string"
      ]
    ],
    [
      "00b19ddc",
      "PARAM",
      [
        "storage",
        "002a00da",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b19cf8",
      "DATA",
      [
        "storage",
        "002f8507",
        "switchD_00b19d00::switchdataD_002f8507",
        "byte"
      ]
    ],
    [
      "00b19da8",
      "PARAM",
      [
        "storage",
        "002a016e",
        null,
        "string"
      ]
    ],
    [
      "00b19ddc",
      "PARAM",
      [
        "storage",
        "002a0165",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b19d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19c18.md#insn-00b19d6c) · [`00b19da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19c18.md#insn-00b19da0) · [`00b19dd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b19/00b19c18.md#insn-00b19dd4)
- 新版 [`00b19db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b19c5c.md#insn-00b19db0) · [`00b19de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b19c5c.md#insn-00b19de4) · [`00b19e18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b19/00b19c5c.md#insn-00b19e18)

~~~diff
- 00b19d6c ["INT_ADD", "register:40f0:8", ["const:b19d6c:8", "const:4:8"]]
- 00b19d6c ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b19db0 ["INT_ADD", "register:40f0:8", ["const:b19db0:8", "const:4:8"]]
+ 00b19db0 ["CALL", null, ["callee:00bde9d0:8"]]
- 00b19d6c bytes 05130394
+ 00b19db0 bytes 08130394
- 00b19da0 ["INT_ADD", "register:40f0:8", ["const:b19da0:8", "const:4:8"]]
- 00b19da0 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b19de4 ["INT_ADD", "register:40f0:8", ["const:b19de4:8", "const:4:8"]]
+ 00b19de4 ["CALL", null, ["callee:00bde9d0:8"]]
- 00b19da0 bytes f8120394
+ 00b19de4 bytes fb120394
- 00b19dd4 ["INT_ADD", "register:40f0:8", ["const:b19dd4:8", "const:4:8"]]
- 00b19dd4 ["CALL", null, ["callee:00bde9d0:8"]]
+ 00b19e18 ["INT_ADD", "register:40f0:8", ["const:b19e18:8", "const:4:8"]]
+ 00b19e18 ["CALL", null, ["callee:00bde9d0:8"]]
- 00b19dd4 bytes eb120394
+ 00b19e18 bytes ee120394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b4bfef5f49791d0cc1d8c122a5b7bc0"></a>

### [`00b1a2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a2f8.md) → [`00b1a33c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1a33c.md) _ZN11flatbuffers4atotIaEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf640.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdf690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf690.md) · 呼出先 12件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.22% / 新版 98.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1a4c0",
      "incomplete_value": false,
      "site": "00b1a4d4",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1a47c",
      "incomplete_value": false,
      "site": "00b1a490",
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
            "const:20f:8"
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
      "definition_site": "00b1a4e4",
      "incomplete_value": false,
      "site": "00b1a504",
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
            "const:41f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1a4a0",
      "incomplete_value": false,
      "site": "00b1a4c0",
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
            "const:394:8"
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
      "definition_site": "00b1a5cc",
      "incomplete_value": false,
      "site": "00b1a5e0",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1a588",
      "incomplete_value": false,
      "site": "00b1a59c",
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
            "const:20f:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1a4c0",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b1a4e4",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b1a5cc",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1a4c0",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ],
    [
      "00b1a4e4",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b1a5cc",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1a47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a2f8.md#insn-00b1a47c) · [`00b1a490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a2f8.md#insn-00b1a490) · [`00b1a4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a2f8.md#insn-00b1a4c0)
- 新版 [`00b1a4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1a33c.md#insn-00b1a4c0) · [`00b1a4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1a33c.md#insn-00b1a4d4) · [`00b1a504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1a33c.md#insn-00b1a504)

~~~diff
- 00b1a47c ["COPY", "tmp:0:8", ["const:20f:8"]]
- 00b1a47c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b1a47c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b1a47c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b1a4c0 ["COPY", "tmp:0:8", ["const:2a9:8"]]
+ 00b1a4c0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1a4c0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1a4c0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b1a47c bytes 423c0891
+ 00b1a4c0 bytes 42a40a91
- 00b1a490 ["INT_ADD", "register:40f0:8", ["const:b1a490:8", "const:4:8"]]
- 00b1a490 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b1a4d4 ["INT_ADD", "register:40f0:8", ["const:b1a4d4:8", "const:4:8"]]
+ 00b1a4d4 ["CALL", null, ["callee:00bdc180:8"]]
- 00b1a490 bytes 28070394
+ 00b1a4d4 bytes 2b070394
- 00b1a4c0 ["INT_ADD", "register:40f0:8", ["const:b1a4c0:8", "const:4:8"]]
- 00b1a4c0 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b1a504 ["INT_ADD", "register:40f0:8", ["const:b1a504:8", "const:4:8"]]
+ 00b1a504 ["CALL", null, ["callee:00bdb130:8"]]
- 00b1a4c0 bytes 08030394
+ 00b1a504 bytes 0b030394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-152baac5c96324fc2594eb18bac334f0"></a>

### [`00b1a838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a838.md) → [`00b1a87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1a87c.md) _ZN11flatbuffers4atotIsEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf6c0.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdf710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf710.md) · 呼出先 12件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.22% / 新版 98.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1aa00",
      "incomplete_value": false,
      "site": "00b1aa14",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1a9bc",
      "incomplete_value": false,
      "site": "00b1a9d0",
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
            "const:20f:8"
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
      "definition_site": "00b1aa24",
      "incomplete_value": false,
      "site": "00b1aa44",
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
            "const:41f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1a9e0",
      "incomplete_value": false,
      "site": "00b1aa00",
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
            "const:394:8"
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
      "definition_site": "00b1ab0c",
      "incomplete_value": false,
      "site": "00b1ab20",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1aac8",
      "incomplete_value": false,
      "site": "00b1aadc",
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
            "const:20f:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1aa00",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b1aa24",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b1ab0c",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1aa00",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ],
    [
      "00b1aa24",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b1ab0c",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1a9bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a838.md#insn-00b1a9bc) · [`00b1a9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a838.md#insn-00b1a9d0) · [`00b1aa00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1a838.md#insn-00b1aa00)
- 新版 [`00b1aa00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1a87c.md#insn-00b1aa00) · [`00b1aa14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1a87c.md#insn-00b1aa14) · [`00b1aa44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1a87c.md#insn-00b1aa44)

~~~diff
- 00b1a9bc ["COPY", "tmp:0:8", ["const:20f:8"]]
- 00b1a9bc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b1a9bc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b1a9bc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b1aa00 ["COPY", "tmp:0:8", ["const:2a9:8"]]
+ 00b1aa00 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1aa00 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1aa00 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b1a9bc bytes 423c0891
+ 00b1aa00 bytes 42a40a91
- 00b1a9d0 ["INT_ADD", "register:40f0:8", ["const:b1a9d0:8", "const:4:8"]]
- 00b1a9d0 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b1aa14 ["INT_ADD", "register:40f0:8", ["const:b1aa14:8", "const:4:8"]]
+ 00b1aa14 ["CALL", null, ["callee:00bdc180:8"]]
- 00b1a9d0 bytes d8050394
+ 00b1aa14 bytes db050394
- 00b1aa00 ["INT_ADD", "register:40f0:8", ["const:b1aa00:8", "const:4:8"]]
- 00b1aa00 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b1aa44 ["INT_ADD", "register:40f0:8", ["const:b1aa44:8", "const:4:8"]]
+ 00b1aa44 ["CALL", null, ["callee:00bdb130:8"]]
- 00b1aa00 bytes b8010394
+ 00b1aa44 bytes bb010394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9649fd35b6015413e7b7d8f618c8e5a8"></a>

### [`00b1ac9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1ac9c.md) → [`00b1ace0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1ace0.md) _ZN11flatbuffers4atotItEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf6d0.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdf720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf720.md) · 呼出先 12件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.19% / 新版 98.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1ae60",
      "incomplete_value": true,
      "site": "00b1ae74",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1ae1c",
      "incomplete_value": true,
      "site": "00b1ae30",
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
            "const:20f:8"
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
      "definition_site": "00b1ae84",
      "incomplete_value": false,
      "site": "00b1aea4",
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
            "const:41f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1ae40",
      "incomplete_value": false,
      "site": "00b1ae60",
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
            "const:394:8"
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
      "definition_site": "00b1af6c",
      "incomplete_value": false,
      "site": "00b1af80",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1af28",
      "incomplete_value": false,
      "site": "00b1af3c",
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
            "const:20f:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1ae60",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b1ae84",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b1af6c",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1ae60",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ],
    [
      "00b1ae84",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b1af6c",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1ae1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1ac9c.md#insn-00b1ae1c) · [`00b1ae30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1ac9c.md#insn-00b1ae30) · [`00b1ae60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1a/00b1ac9c.md#insn-00b1ae60)
- 新版 [`00b1ae60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1ace0.md#insn-00b1ae60) · [`00b1ae74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1ace0.md#insn-00b1ae74) · [`00b1aea4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1a/00b1ace0.md#insn-00b1aea4)

~~~diff
- 00b1ae1c ["COPY", "tmp:0:8", ["const:20f:8"]]
- 00b1ae1c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b1ae1c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b1ae1c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b1ae60 ["COPY", "tmp:0:8", ["const:2a9:8"]]
+ 00b1ae60 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1ae60 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1ae60 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b1ae1c bytes 423c0891
+ 00b1ae60 bytes 42a40a91
- 00b1ae30 ["INT_ADD", "register:40f0:8", ["const:b1ae30:8", "const:4:8"]]
- 00b1ae30 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b1ae74 ["INT_ADD", "register:40f0:8", ["const:b1ae74:8", "const:4:8"]]
+ 00b1ae74 ["CALL", null, ["callee:00bdc180:8"]]
- 00b1ae30 bytes c0040394
+ 00b1ae74 bytes c3040394
- 00b1ae60 ["INT_ADD", "register:40f0:8", ["const:b1ae60:8", "const:4:8"]]
- 00b1ae60 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b1aea4 ["INT_ADD", "register:40f0:8", ["const:b1aea4:8", "const:4:8"]]
+ 00b1aea4 ["CALL", null, ["callee:00bdb130:8"]]
- 00b1ae60 bytes a0000394
+ 00b1aea4 bytes a3000394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cd6b92fc4a8a02802441c35cf9cbbf59"></a>

### [`00b1b220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b220.md) → [`00b1b264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1b264.md) _ZN11flatbuffers4atotIiEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf680.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdf6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf6d0.md) · 呼出先 12件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.22% / 新版 98.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1b3e8",
      "incomplete_value": false,
      "site": "00b1b3fc",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1b3a4",
      "incomplete_value": false,
      "site": "00b1b3b8",
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
            "const:20f:8"
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
      "definition_site": "00b1b40c",
      "incomplete_value": false,
      "site": "00b1b42c",
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
            "const:41f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1b3c8",
      "incomplete_value": false,
      "site": "00b1b3e8",
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
            "const:394:8"
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
      "definition_site": "00b1b4f4",
      "incomplete_value": false,
      "site": "00b1b508",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1b4b0",
      "incomplete_value": false,
      "site": "00b1b4c4",
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
            "const:20f:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1b3e8",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b1b40c",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b1b4f4",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1b3e8",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ],
    [
      "00b1b40c",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b1b4f4",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1b3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b220.md#insn-00b1b3a4) · [`00b1b3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b220.md#insn-00b1b3b8) · [`00b1b3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b220.md#insn-00b1b3e8)
- 新版 [`00b1b3e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1b264.md#insn-00b1b3e8) · [`00b1b3fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1b264.md#insn-00b1b3fc) · [`00b1b42c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1b264.md#insn-00b1b42c)

~~~diff
- 00b1b3a4 ["COPY", "tmp:0:8", ["const:20f:8"]]
- 00b1b3a4 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b1b3a4 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b1b3a4 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b1b3e8 ["COPY", "tmp:0:8", ["const:2a9:8"]]
+ 00b1b3e8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1b3e8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1b3e8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b1b3a4 bytes 423c0891
+ 00b1b3e8 bytes 42a40a91
- 00b1b3b8 ["INT_ADD", "register:40f0:8", ["const:b1b3b8:8", "const:4:8"]]
- 00b1b3b8 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b1b3fc ["INT_ADD", "register:40f0:8", ["const:b1b3fc:8", "const:4:8"]]
+ 00b1b3fc ["CALL", null, ["callee:00bdc180:8"]]
- 00b1b3b8 bytes 5e030394
+ 00b1b3fc bytes 61030394
- 00b1b3e8 ["INT_ADD", "register:40f0:8", ["const:b1b3e8:8", "const:4:8"]]
- 00b1b3e8 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b1b42c ["INT_ADD", "register:40f0:8", ["const:b1b42c:8", "const:4:8"]]
+ 00b1b42c ["CALL", null, ["callee:00bdb130:8"]]
- 00b1b3e8 bytes 3eff0294
+ 00b1b42c bytes 41ff0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04fd540e13c476d01bb899c713b0812c"></a>

### [`00b1b85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b85c.md) → [`00b1b8a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1b8a0.md) _ZN11flatbuffers4atotIlEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf6a0.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdf6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf6f0.md) · 呼出先 12件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.98% / 新版 97.98%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1bb98",
      "incomplete_value": false,
      "site": "00b1bbb8",
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
            "const:41f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1bb54",
      "incomplete_value": false,
      "site": "00b1bb74",
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
            "const:394:8"
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
      "00b1b9ac",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b1b9d0",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b1ba00",
      "PARAM",
      [
        "storage",
        "00292492",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1b9ac",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ],
    [
      "00b1b9d0",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b1ba00",
      "PARAM",
      [
        "storage",
        "00292405",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1bb30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b85c.md#insn-00b1bb30) · [`00b1bb74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b85c.md#insn-00b1bb74) · [`00b1b8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1b85c.md#insn-00b1b8a4)
- 新版 [`00b1bb74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1b8a0.md#insn-00b1bb74) · [`00b1bbb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1b8a0.md#insn-00b1bbb8) · [`00b1b8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1b8a0.md#insn-00b1b8e8)

~~~diff
- 00b1bb30 ["COPY", "tmp:0:8", ["const:20f:8"]]
- 00b1bb30 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b1bb30 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b1bb30 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b1bb74 ["COPY", "tmp:0:8", ["const:2a9:8"]]
+ 00b1bb74 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1bb74 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1bb74 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b1bb30 bytes 423c0891
+ 00b1bb74 bytes 42a40a91
- 00b1bb74 ["INT_ADD", "register:40f0:8", ["const:b1bb74:8", "const:4:8"]]
- 00b1bb74 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b1bbb8 ["INT_ADD", "register:40f0:8", ["const:b1bbb8:8", "const:4:8"]]
+ 00b1bbb8 ["CALL", null, ["callee:00bdb130:8"]]
- 00b1bb74 bytes 5bfd0294
+ 00b1bbb8 bytes 5efd0294
- 00b1b8a4 ["INT_ADD", "register:40f0:8", ["const:b1b8a4:8", "const:4:8"]]
- 00b1b8a4 ["CALL", null, ["callee:00bdf5e0:8"]]
+ 00b1b8e8 ["INT_ADD", "register:40f0:8", ["const:b1b8e8:8", "const:4:8"]]
+ 00b1b8e8 ["CALL", null, ["callee:00bdf5e0:8"]]
- 00b1b8a4 bytes 3b0f0394
+ 00b1b8e8 bytes 3e0f0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8adbaccd43630b9e5044dce670a50961"></a>

### [`00b1bd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bd28.md) → [`00b1bd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1bd6c.md) _ZN11flatbuffers4atotImEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf6b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf6b0.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdf700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf700.md) · 呼出先 12件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.13% / 新版 98.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1be8c",
      "incomplete_value": false,
      "site": "00b1bea0",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1be48",
      "incomplete_value": false,
      "site": "00b1be5c",
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
            "const:20f:8"
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
      "definition_site": "00b1beb0",
      "incomplete_value": false,
      "site": "00b1bed0",
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
            "const:41f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1be6c",
      "incomplete_value": false,
      "site": "00b1be8c",
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
            "const:394:8"
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
      "definition_site": "00b1bee0",
      "incomplete_value": false,
      "site": "00b1befc",
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
            "const:405:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1be9c",
      "incomplete_value": false,
      "site": "00b1beb8",
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
            "const:492:8"
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
      "00b1be8c",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b1beb0",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b1bee0",
      "PARAM",
      [
        "storage",
        "00292492",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1be8c",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ],
    [
      "00b1beb0",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b1bee0",
      "PARAM",
      [
        "storage",
        "00292405",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1be48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bd28.md#insn-00b1be48) · [`00b1be5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bd28.md#insn-00b1be5c) · [`00b1be8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1b/00b1bd28.md#insn-00b1be8c)
- 新版 [`00b1be8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1bd6c.md#insn-00b1be8c) · [`00b1bea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1bd6c.md#insn-00b1bea0) · [`00b1bed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1b/00b1bd6c.md#insn-00b1bed0)

~~~diff
- 00b1be48 ["COPY", "tmp:0:8", ["const:20f:8"]]
- 00b1be48 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b1be48 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b1be48 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b1be8c ["COPY", "tmp:0:8", ["const:2a9:8"]]
+ 00b1be8c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1be8c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1be8c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b1be48 bytes 423c0891
+ 00b1be8c bytes 42a40a91
- 00b1be5c ["INT_ADD", "register:40f0:8", ["const:b1be5c:8", "const:4:8"]]
- 00b1be5c ["CALL", null, ["callee:00bdc180:8"]]
+ 00b1bea0 ["INT_ADD", "register:40f0:8", ["const:b1bea0:8", "const:4:8"]]
+ 00b1bea0 ["CALL", null, ["callee:00bdc180:8"]]
- 00b1be5c bytes b5000394
+ 00b1bea0 bytes b8000394
- 00b1be8c ["INT_ADD", "register:40f0:8", ["const:b1be8c:8", "const:4:8"]]
- 00b1be8c ["CALL", null, ["callee:00bdb130:8"]]
+ 00b1bed0 ["INT_ADD", "register:40f0:8", ["const:b1bed0:8", "const:4:8"]]
+ 00b1bed0 ["CALL", null, ["callee:00bdb130:8"]]
- 00b1be8c bytes 95fc0294
+ 00b1bed0 bytes 98fc0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca1d9ac15df327af874edbefdb726e8b"></a>

### [`00b1c244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c244.md) → [`00b1c288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c288.md) _ZN11flatbuffers4atotIfEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf660.md) · 呼出先 11件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdf6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf6b0.md) · 呼出先 11件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.36% / 新版 98.36%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1c35c",
      "incomplete_value": false,
      "site": "00b1c370",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1c318",
      "incomplete_value": false,
      "site": "00b1c32c",
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
            "const:20f:8"
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
      "definition_site": "00b1c380",
      "incomplete_value": false,
      "site": "00b1c3a0",
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
            "const:41f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1c33c",
      "incomplete_value": false,
      "site": "00b1c35c",
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
            "const:394:8"
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
      "00b1c35c",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b1c380",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b1c35c",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ],
    [
      "00b1c380",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1c318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c244.md#insn-00b1c318) · [`00b1c32c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c244.md#insn-00b1c32c) · [`00b1c35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c244.md#insn-00b1c35c)
- 新版 [`00b1c35c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c288.md#insn-00b1c35c) · [`00b1c370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c288.md#insn-00b1c370) · [`00b1c3a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c288.md#insn-00b1c3a0)

~~~diff
- 00b1c318 ["COPY", "tmp:0:8", ["const:20f:8"]]
- 00b1c318 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b1c318 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b1c318 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b1c35c ["COPY", "tmp:0:8", ["const:2a9:8"]]
+ 00b1c35c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1c35c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1c35c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b1c318 bytes 423c0891
+ 00b1c35c bytes 42a40a91
- 00b1c32c ["INT_ADD", "register:40f0:8", ["const:b1c32c:8", "const:4:8"]]
- 00b1c32c ["CALL", null, ["callee:00bdc180:8"]]
+ 00b1c370 ["INT_ADD", "register:40f0:8", ["const:b1c370:8", "const:4:8"]]
+ 00b1c370 ["CALL", null, ["callee:00bdc180:8"]]
- 00b1c32c bytes 81ff0294
+ 00b1c370 bytes 84ff0294
- 00b1c35c ["INT_ADD", "register:40f0:8", ["const:b1c35c:8", "const:4:8"]]
- 00b1c35c ["CALL", null, ["callee:00bdb130:8"]]
+ 00b1c3a0 ["INT_ADD", "register:40f0:8", ["const:b1c3a0:8", "const:4:8"]]
+ 00b1c3a0 ["CALL", null, ["callee:00bdb130:8"]]
- 00b1c35c bytes 61fb0294
+ 00b1c3a0 bytes 64fb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a46fd4f89242f86273a1e872655bd84"></a>

### [`00b1c518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c518.md) → [`00b1c55c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c55c.md) _ZN11flatbuffers4atotIdEENS_12CheckedErrorEPKcRNS_6ParserEPT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf650.md) · 呼出先 11件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdf6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf6a0.md) · 呼出先 11件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.35% / 新版 98.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1c62c",
      "incomplete_value": false,
      "site": "00b1c640",
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
            "const:2a9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1c5e8",
      "incomplete_value": false,
      "site": "00b1c5fc",
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
            "const:20f:8"
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
      "definition_site": "00b1c650",
      "incomplete_value": false,
      "site": "00b1c670",
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
            "const:41f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1c60c",
      "incomplete_value": false,
      "site": "00b1c62c",
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
            "const:394:8"
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
      "00b1c62c",
      "PARAM",
      [
        "storage",
        "002a620f",
        null,
        "string"
      ]
    ],
    [
      "00b1c650",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b1c62c",
      "PARAM",
      [
        "storage",
        "002a62a9",
        null,
        "string"
      ]
    ],
    [
      "00b1c650",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1c5e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c518.md#insn-00b1c5e8) · [`00b1c5fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c518.md#insn-00b1c5fc) · [`00b1c62c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1c518.md#insn-00b1c62c)
- 新版 [`00b1c62c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c55c.md#insn-00b1c62c) · [`00b1c640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c55c.md#insn-00b1c640) · [`00b1c670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1c55c.md#insn-00b1c670)

~~~diff
- 00b1c5e8 ["COPY", "tmp:0:8", ["const:20f:8"]]
- 00b1c5e8 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b1c5e8 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b1c5e8 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b1c62c ["COPY", "tmp:0:8", ["const:2a9:8"]]
+ 00b1c62c ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1c62c ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b1c62c ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b1c5e8 bytes 423c0891
+ 00b1c62c bytes 42a40a91
- 00b1c5fc ["INT_ADD", "register:40f0:8", ["const:b1c5fc:8", "const:4:8"]]
- 00b1c5fc ["CALL", null, ["callee:00bdc180:8"]]
+ 00b1c640 ["INT_ADD", "register:40f0:8", ["const:b1c640:8", "const:4:8"]]
+ 00b1c640 ["CALL", null, ["callee:00bdc180:8"]]
- 00b1c5fc bytes cdfe0294
+ 00b1c640 bytes d0fe0294
- 00b1c62c ["INT_ADD", "register:40f0:8", ["const:b1c62c:8", "const:4:8"]]
- 00b1c62c ["CALL", null, ["callee:00bdb130:8"]]
+ 00b1c670 ["INT_ADD", "register:40f0:8", ["const:b1c670:8", "const:4:8"]]
+ 00b1c670 ["CALL", null, ["callee:00bdb130:8"]]
- 00b1c62c bytes adfa0294
+ 00b1c670 bytes b0fa0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42a173dcc87894a631fbe6d549668475"></a>

### [`00b1cd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md) → [`00b1cd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cd54.md) FUN_00b1cd54

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b1cd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md) · 呼出先 2件 [`00b1cd10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md) [`00b40f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40f58.md)
- 新版 呼出元 2件 [`00b18d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md) [`00b1cd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cd54.md) · 呼出先 2件 [`00b1cd54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cd54.md) [`00b40f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40f9c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.81% / 新版 94.81%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1cde4",
      "incomplete_value": true,
      "site": "00b1cdec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "INT_ZEXT",
            "8",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1cda0",
      "incomplete_value": true,
      "site": "00b1cda8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40b0:8"
          ],
          [
            "INT_ZEXT",
            "8",
            [
              "LOAD"
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
      "definition_site": "00b1cde8",
      "incomplete_value": true,
      "site": "00b1cdec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "INT_ZEXT",
            "8",
            [
              "LOAD"
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1cda4",
      "incomplete_value": true,
      "site": "00b1cda8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40d8:8"
          ],
          [
            "INT_ZEXT",
            "8",
            [
              "LOAD"
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
      "definition_site": "00b1cde0",
      "incomplete_value": true,
      "site": "00b1cdec",
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
      "definition_site": "00b1cd9c",
      "incomplete_value": true,
      "site": "00b1cda8",
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
      "00b1cddc",
      "READ",
      [
        "storage",
        "010a0ed4",
        null,
        "undefined2"
      ]
    ],
    [
      "00b1cde0",
      "READ",
      [
        "storage",
        "010a0ee0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b1cddc",
      "READ",
      [
        "storage",
        "010a0f14",
        null,
        "undefined2"
      ]
    ],
    [
      "00b1cde0",
      "READ",
      [
        "storage",
        "010a0f20",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1cd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md#insn-00b1cd64) · [`00b1cda8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md#insn-00b1cda8) · [`00b1cd98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cd10.md#insn-00b1cd98)
- 新版 [`00b1cda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cd54.md#insn-00b1cda8) · [`00b1cdec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cd54.md#insn-00b1cdec) · [`00b1cddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cd54.md#insn-00b1cddc)

~~~diff
- 00b1cd64 ["INT_ADD", "register:40f0:8", ["const:b1cd64:8", "const:4:8"]]
- 00b1cd64 ["CALL", null, ["local:b0:8"]]
+ 00b1cda8 ["INT_ADD", "register:40f0:8", ["const:b1cda8:8", "const:4:8"]]
+ 00b1cda8 ["CALL", null, ["local:b0:8"]]
- 00b1cd64 bytes ebffff97
+ 00b1cda8 bytes ebffff97
- 00b1cda8 ["INT_ADD", "register:40f0:8", ["const:b1cda8:8", "const:4:8"]]
- 00b1cda8 ["CALL", null, ["callee:00b40f9c:8"]]
+ 00b1cdec ["INT_ADD", "register:40f0:8", ["const:b1cdec:8", "const:4:8"]]
+ 00b1cdec ["CALL", null, ["callee:00b40f9c:8"]]
- 00b1cda8 bytes 6c900094
+ 00b1cdec bytes 6c900094
- 00b1cd98 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:ed4:8"]]
- 00b1cd98 ["LOAD", "tmp:1:2", ["const:1b1:8", "tmp:0:8"]]
- 00b1cd98 ["INT_ZEXT", "register:4040:8", ["tmp:1:2"]]
+ 00b1cddc ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:f14:8"]]
+ 00b1cddc ["LOAD", "tmp:1:2", ["const:1b1:8", "tmp:0:8"]]
+ 00b1cddc ["INT_ZEXT", "register:4040:8", ["tmp:1:2"]]
- 00b1cd98 bytes 08ab5d79
+ 00b1cddc bytes 082b5e79
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22cdbd06490bc8680c5cdf6b252e2c50"></a>

### [`00b1ce44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md) → [`00b1ce88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1ce88.md) FUN_00b1ce88

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b18cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b18/00b18cd8.md) [`00b1ce44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md) · 呼出先 2件 [`00b1ce44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md) [`00b40f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b40/00b40f58.md)
- 新版 呼出元 2件 [`00b18d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b18/00b18d1c.md) [`00b1ce88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1ce88.md) · 呼出先 2件 [`00b1ce88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1ce88.md) [`00b40f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b40/00b40f9c.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.73% / 新版 97.73%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1cf8c",
      "incomplete_value": true,
      "site": "00b1cf90",
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
      "definition_site": "00b1cf48",
      "incomplete_value": true,
      "site": "00b1cf4c",
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
      "00b1cf14",
      "READ",
      [
        "storage",
        "010a0ed4",
        null,
        "undefined2"
      ]
    ],
    [
      "00b1cf8c",
      "READ",
      [
        "storage",
        "010a0ee0",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b1cf14",
      "READ",
      [
        "storage",
        "010a0f14",
        null,
        "undefined2"
      ]
    ],
    [
      "00b1cf8c",
      "READ",
      [
        "storage",
        "010a0f20",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1cf4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md#insn-00b1cf4c) · [`00b1ceb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md#insn-00b1ceb0) · [`00b1ced0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1ce44.md#insn-00b1ced0)
- 新版 [`00b1cf90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1ce88.md#insn-00b1cf90) · [`00b1cef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1ce88.md#insn-00b1cef4) · [`00b1cf14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1ce88.md#insn-00b1cf14)

~~~diff
- 00b1cf4c ["INT_ADD", "register:40f0:8", ["const:b1cf4c:8", "const:4:8"]]
- 00b1cf4c ["CALL", null, ["callee:00b40f9c:8"]]
+ 00b1cf90 ["INT_ADD", "register:40f0:8", ["const:b1cf90:8", "const:4:8"]]
+ 00b1cf90 ["CALL", null, ["callee:00b40f9c:8"]]
- 00b1cf4c bytes 03900094
+ 00b1cf90 bytes 03900094
- 00b1ceb0 ["INT_ADD", "register:40f0:8", ["const:b1ceb0:8", "const:4:8"]]
- 00b1ceb0 ["CALL", null, ["local:b0:8"]]
+ 00b1cef4 ["INT_ADD", "register:40f0:8", ["const:b1cef4:8", "const:4:8"]]
+ 00b1cef4 ["CALL", null, ["local:b0:8"]]
- 00b1ceb0 bytes e5ffff97
+ 00b1cef4 bytes e5ffff97
- 00b1ced0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:ed4:8"]]
- 00b1ced0 ["LOAD", "tmp:1:2", ["const:1b1:8", "tmp:0:8"]]
- 00b1ced0 ["INT_ZEXT", "register:40c8:8", ["tmp:1:2"]]
+ 00b1cf14 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f14:8"]]
+ 00b1cf14 ["LOAD", "tmp:1:2", ["const:1b1:8", "tmp:0:8"]]
+ 00b1cf14 ["INT_ZEXT", "register:40c8:8", ["tmp:1:2"]]
- 00b1ced0 bytes b9aa5d79
+ 00b1cf14 bytes b92a5e79
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bf02431f646bed145a41a29b42ee43f"></a>

### [`00b1cfa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cfa4.md) → [`00b1cfe8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cfe8.md) _ZN11flatbuffers6Parser21ParseNestedFlatbufferERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf900`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf900.md) · 呼出先 21件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)
- 新版 呼出元 1件 [`00bdf950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf950.md) · 呼出先 21件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1d184",
      "incomplete_value": true,
      "site": "00b1d184",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b1d140",
      "incomplete_value": true,
      "site": "00b1d140",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 32,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1d178",
      "incomplete_value": true,
      "site": "00b1d1a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b1d134",
      "incomplete_value": true,
      "site": "00b1d160",
      "value": [
        "LOAD",
        "8",
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
      "00b1d174",
      "READ",
      [
        "storage",
        "002987b2",
        null,
        "string"
      ]
    ],
    [
      "00b1d178",
      "READ",
      [
        "storage",
        "002987b9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1d174",
      "READ",
      [
        "storage",
        "00298725",
        null,
        "string"
      ]
    ],
    [
      "00b1d178",
      "READ",
      [
        "storage",
        "0029872c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1d004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cfa4.md#insn-00b1d004) · [`00b1d028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cfa4.md#insn-00b1d028) · [`00b1d088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1c/00b1cfa4.md#insn-00b1d088)
- 新版 [`00b1d048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cfe8.md#insn-00b1d048) · [`00b1d06c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cfe8.md#insn-00b1d06c) · [`00b1d0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1c/00b1cfe8.md#insn-00b1d0cc)

~~~diff
- 00b1d004 ["INT_ADD", "register:40f0:8", ["const:b1d004:8", "const:4:8"]]
- 00b1d004 ["CALL", null, ["callee:00bdf800:8"]]
+ 00b1d048 ["INT_ADD", "register:40f0:8", ["const:b1d048:8", "const:4:8"]]
+ 00b1d048 ["CALL", null, ["callee:00bdf800:8"]]
- 00b1d004 bytes eb090394
+ 00b1d048 bytes ee090394
- 00b1d028 ["INT_ADD", "register:40f0:8", ["const:b1d028:8", "const:4:8"]]
- 00b1d028 ["CALL", null, ["callee:00bdf900:8"]]
+ 00b1d06c ["INT_ADD", "register:40f0:8", ["const:b1d06c:8", "const:4:8"]]
+ 00b1d06c ["CALL", null, ["callee:00bdf900:8"]]
- 00b1d028 bytes 220a0394
+ 00b1d06c bytes 250a0394
- 00b1d088 ["INT_ADD", "register:40f0:8", ["const:b1d088:8", "const:4:8"]]
- 00b1d088 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b1d0cc ["INT_ADD", "register:40f0:8", ["const:b1d0cc:8", "const:4:8"]]
+ 00b1d0cc ["CALL", null, ["callee:00bdb040:8"]]
- 00b1d088 bytes daf70294
+ 00b1d0cc bytes ddf70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2013f59b916cd0bb2536ec6a225c2b3d"></a>

### [`00b1d810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d810.md) → [`00b1d854`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d854.md) _ZN11flatbuffers6Parser19ParseEnumFromStringERKNS_4TypeEPNSt6__ndk112basic_stringIcNS4_11char_traitsIcEENS4_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf8e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf8e0.md) · 呼出先 12件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)
- 新版 呼出元 1件 [`00bdf930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf930.md) · 呼出先 12件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb180.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.25% / 新版 97.25%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1dad4",
      "incomplete_value": true,
      "site": "00b1dae4",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ed3:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1da90",
      "incomplete_value": true,
      "site": "00b1daa0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e48:8"
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
      "definition_site": "00b1dad4",
      "incomplete_value": true,
      "site": "00b1dae4",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b1da90",
      "incomplete_value": true,
      "site": "00b1daa0",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 23,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1dad8",
      "incomplete_value": true,
      "site": "00b1dae8",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b1da94",
      "incomplete_value": true,
      "site": "00b1daa4",
      "value": [
        "LOAD",
        "16",
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
      "00b1d9d4",
      "PARAM",
      [
        "storage",
        "0029de95",
        null,
        "string"
      ]
    ],
    [
      "00b1dad4",
      "READ",
      [
        "storage",
        "002a2e48",
        null,
        "string"
      ]
    ],
    [
      "00b1dad4",
      "READ",
      [
        "storage",
        "002a2e58",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1d9d4",
      "PARAM",
      [
        "storage",
        "0029df20",
        null,
        "string"
      ]
    ],
    [
      "00b1dad4",
      "READ",
      [
        "storage",
        "002a2ed3",
        null,
        "string"
      ]
    ],
    [
      "00b1dad4",
      "READ",
      [
        "storage",
        "002a2ee3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1d994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d810.md#insn-00b1d994) · [`00b1dbd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d810.md#insn-00b1dbd4) · [`00b1d8b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1d810.md#insn-00b1d8b4)
- 新版 [`00b1d9d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d854.md#insn-00b1d9d8) · [`00b1dc18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d854.md#insn-00b1dc18) · [`00b1d8f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1d854.md#insn-00b1d8f8)

~~~diff
- 00b1d994 ["INT_ADD", "register:40f0:8", ["const:b1d994:8", "const:4:8"]]
- 00b1d994 ["CALL", null, ["callee:00bdb260:8"]]
+ 00b1d9d8 ["INT_ADD", "register:40f0:8", ["const:b1d9d8:8", "const:4:8"]]
+ 00b1d9d8 ["CALL", null, ["callee:00bdb260:8"]]
- 00b1d994 bytes 1ff60294
+ 00b1d9d8 bytes 22f60294
- 00b1dbd4 ["INT_ADD", "register:40f0:8", ["const:b1dbd4:8", "const:4:8"]]
- 00b1dbd4 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b1dc18 ["INT_ADD", "register:40f0:8", ["const:b1dc18:8", "const:4:8"]]
+ 00b1dc18 ["CALL", null, ["callee:00bdb060:8"]]
- 00b1dbd4 bytes 0ff50294
+ 00b1dc18 bytes 12f50294
- 00b1d8b4 ["INT_ADD", "register:40f0:8", ["const:b1d8b4:8", "const:4:8"]]
- 00b1d8b4 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b1d8f8 ["INT_ADD", "register:40f0:8", ["const:b1d8f8:8", "const:4:8"]]
+ 00b1d8f8 ["CALL", null, ["callee:00bdb060:8"]]
- 00b1d8b4 bytes d7f50294
+ 00b1d8f8 bytes daf50294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-17304a80d3b3230acf6f0afcb050ccfe"></a>

### [`00b1dd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1dd2c.md) → [`00b1dd70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1dd70.md) _ZN11flatbuffers11NumToStringImEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf180.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb310.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb360.md)
- 新版 呼出元 1件 [`00bdf1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1d0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb360.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 91.11% / 新版 91.11%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1ddc8",
      "incomplete_value": true,
      "site": "00b1dddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b1dd84",
      "incomplete_value": true,
      "site": "00b1dd98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b1ddc0",
      "incomplete_value": true,
      "site": "00b1dde0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b1dd7c",
      "incomplete_value": true,
      "site": "00b1dd9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b1dda0",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "00b1dda4",
      "READ",
      [
        "storage",
        "00c1b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b1dddc",
      "DATA",
      [
        "storage",
        "00c110f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b1dda0",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "00b1dda4",
      "READ",
      [
        "storage",
        "00c1ba48",
        null,
        "pointer"
      ]
    ],
    [
      "00b1dddc",
      "DATA",
      [
        "storage",
        "00c11140",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1dd5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1dd2c.md#insn-00b1dd5c) · [`00b1dd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1dd2c.md#insn-00b1dd60) · [`00b1dda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1dd2c.md#insn-00b1dda4)
- 新版 [`00b1dda0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1dd70.md#insn-00b1dda0) · [`00b1dda4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1dd70.md#insn-00b1dda4) · [`00b1dde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1dd70.md#insn-00b1dde8)

~~~diff
- 00b1dd5c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:dd8:8"]]
- 00b1dd5c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b1dda0 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:e28:8"]]
+ 00b1dda0 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b1dd5c bytes 5aef46f9
+ 00b1dda0 bytes 5a1747f9
- 00b1dd60 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9f8:8"]]
- 00b1dd60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b1dda4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a48:8"]]
+ 00b1dda4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b1dd60 bytes 08fd44f9
+ 00b1dda4 bytes 082545f9
- 00b1dda4 ["INT_ADD", "register:40f0:8", ["const:b1dda4:8", "const:4:8"]]
- 00b1dda4 ["CALL", null, ["callee:00bdb390:8"]]
+ 00b1dde8 ["INT_ADD", "register:40f0:8", ["const:b1dde8:8", "const:4:8"]]
+ 00b1dde8 ["CALL", null, ["callee:00bdb390:8"]]
- 00b1dda4 bytes 67f50294
+ 00b1dde8 bytes 6af50294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-239a85f592d706f0838b88bceba01333"></a>

### [`00b1de94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1de94.md) → [`00b1ded8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1ded8.md) _ZN11flatbuffers11NumToStringIsEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf190.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb310.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 1件 [`00bdf1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1e0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb360.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 87.91% / 新版 87.91%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1df34",
      "incomplete_value": true,
      "site": "00b1df48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b1def0",
      "incomplete_value": true,
      "site": "00b1df04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b1df2c",
      "incomplete_value": true,
      "site": "00b1df4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b1dee8",
      "incomplete_value": true,
      "site": "00b1df08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 16,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1dfbc",
      "incomplete_value": true,
      "site": "00b1dfc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b1df78",
      "incomplete_value": true,
      "site": "00b1df84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b1df0c",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "00b1df10",
      "READ",
      [
        "storage",
        "00c1b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b1df48",
      "DATA",
      [
        "storage",
        "00c110f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b1df0c",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "00b1df10",
      "READ",
      [
        "storage",
        "00c1ba48",
        null,
        "pointer"
      ]
    ],
    [
      "00b1df48",
      "DATA",
      [
        "storage",
        "00c11140",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1dfc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1de94.md#insn-00b1dfc8) · [`00b1dec8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1de94.md#insn-00b1dec8) · [`00b1decc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1d/00b1de94.md#insn-00b1decc)
- 新版 [`00b1e00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1ded8.md#insn-00b1e00c) · [`00b1df0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1ded8.md#insn-00b1df0c) · [`00b1df10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1d/00b1ded8.md#insn-00b1df10)

~~~diff
- 00b1dfc8 ["INT_ADD", "register:40f0:8", ["const:b1dfc8:8", "const:4:8"]]
- 00b1dfc8 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b1e00c ["INT_ADD", "register:40f0:8", ["const:b1e00c:8", "const:4:8"]]
+ 00b1e00c ["CALL", null, ["callee:00be01e0:8"]]
- 00b1dfc8 bytes 72080394
+ 00b1e00c bytes 75080394
- 00b1dec8 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:dd8:8"]]
- 00b1dec8 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b1df0c ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:e28:8"]]
+ 00b1df0c ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b1dec8 bytes 5aef46f9
+ 00b1df0c bytes 5a1747f9
- 00b1decc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9f8:8"]]
- 00b1decc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b1df10 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a48:8"]]
+ 00b1df10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b1decc bytes 08fd44f9
+ 00b1df10 bytes 082545f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93678abda497e1cd21578dd45a2a770b"></a>

### [`00b1e16c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e16c.md) → [`00b1e1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e1b0.md) _ZN11flatbuffers6Parser10TokenErrorEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf720.md) · 呼出先 10件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdf770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf770.md) · 呼出先 10件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.10% / 新版 97.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1e27c",
      "incomplete_value": true,
      "site": "00b1e280",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b1e238",
      "incomplete_value": true,
      "site": "00b1e23c",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 1,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1e320",
      "incomplete_value": false,
      "site": "00b1e330",
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
            "const:dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1e2dc",
      "incomplete_value": false,
      "site": "00b1e2ec",
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
            "const:51:8"
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
      "00b1e270",
      "DATA",
      [
        "storage",
        "00c10e80",
        null,
        "undefined *"
      ]
    ],
    [
      "00b1e320",
      "PARAM",
      [
        "storage",
        "002a0051",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1e270",
      "DATA",
      [
        "storage",
        "00c10ed0",
        null,
        "undefined *"
      ]
    ],
    [
      "00b1e320",
      "PARAM",
      [
        "storage",
        "002a00dc",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1e23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e16c.md#insn-00b1e23c) · [`00b1e2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e16c.md#insn-00b1e2ec) · [`00b1e1e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e16c.md#insn-00b1e1e8)
- 新版 [`00b1e280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e1b0.md#insn-00b1e280) · [`00b1e330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e1b0.md#insn-00b1e330) · [`00b1e22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e1b0.md#insn-00b1e22c)

~~~diff
- 00b1e23c ["INT_ADD", "register:40f0:8", ["const:b1e23c:8", "const:4:8"]]
- 00b1e23c ["CALL", null, ["callee:00bdb190:8"]]
+ 00b1e280 ["INT_ADD", "register:40f0:8", ["const:b1e280:8", "const:4:8"]]
+ 00b1e280 ["CALL", null, ["callee:00bdb190:8"]]
- 00b1e23c bytes c1f30294
+ 00b1e280 bytes c4f30294
- 00b1e2ec ["INT_ADD", "register:40f0:8", ["const:b1e2ec:8", "const:4:8"]]
- 00b1e2ec ["CALL", null, ["callee:00bdc180:8"]]
+ 00b1e330 ["INT_ADD", "register:40f0:8", ["const:b1e330:8", "const:4:8"]]
+ 00b1e330 ["CALL", null, ["callee:00bdc180:8"]]
- 00b1e2ec bytes 91f70294
+ 00b1e330 bytes 94f70294
- 00b1e1e8 ["INT_ADD", "register:40f0:8", ["const:b1e1e8:8", "const:4:8"]]
- 00b1e1e8 ["CALL", null, ["callee:00bdefc0:8"]]
+ 00b1e22c ["INT_ADD", "register:40f0:8", ["const:b1e22c:8", "const:4:8"]]
+ 00b1e22c ["CALL", null, ["callee:00bdefc0:8"]]
- 00b1e1e8 bytes 62030394
+ 00b1e22c bytes 65030394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86ca5496eaecb4845d785de6c0bc11ce"></a>

### [`00b1e394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e394.md) → [`00b1e3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e3d8.md) _ZN11flatbuffers6Parser13ParseFunctionEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEERNS_5ValueE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf7c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf7c0.md) · 呼出先 23件 [`00afa9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afa/00afa9c4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 1件 [`00bdf810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf810.md) · 呼出先 23件 [`00afaa08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afa/00afaa08.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 96.97% / 新版 96.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 7件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1ea28",
      "incomplete_value": true,
      "site": "00b1ea48",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b1e9e4",
      "incomplete_value": true,
      "site": "00b1ea04",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 82,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1ea30",
      "incomplete_value": true,
      "site": "00b1ea4c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ff:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1e9ec",
      "incomplete_value": true,
      "site": "00b1ea08",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:74:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 83,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1e50c",
      "incomplete_value": false,
      "site": "00b1e518",
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
            "const:fc2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1e4c8",
      "incomplete_value": false,
      "site": "00b1e4d4",
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
            "const:f37:8"
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
      "00b1e50c",
      "PARAM",
      [
        "storage",
        "002a0f37",
        null,
        "string"
      ]
    ],
    [
      "00b1e520",
      "PARAM",
      [
        "storage",
        "0029de8e",
        null,
        "string"
      ]
    ],
    [
      "00b1e53c",
      "PARAM",
      [
        "storage",
        "0029770b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1e50c",
      "PARAM",
      [
        "storage",
        "002a0fc2",
        null,
        "string"
      ]
    ],
    [
      "00b1e520",
      "PARAM",
      [
        "storage",
        "0029df19",
        null,
        "string"
      ]
    ],
    [
      "00b1e53c",
      "PARAM",
      [
        "storage",
        "0029767e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1e4d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e394.md#insn-00b1e4d4) · [`00b1e544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e394.md#insn-00b1e544) · [`00b1e680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1e394.md#insn-00b1e680)
- 新版 [`00b1e518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e3d8.md#insn-00b1e518) · [`00b1e588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e3d8.md#insn-00b1e588) · [`00b1e6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1e3d8.md#insn-00b1e6c4)

~~~diff
- 00b1e4d4 ["INT_ADD", "register:40f0:8", ["const:b1e4d4:8", "const:4:8"]]
- 00b1e4d4 ["CALL", null, ["callee:00afaa08:8"]]
+ 00b1e518 ["INT_ADD", "register:40f0:8", ["const:b1e518:8", "const:4:8"]]
+ 00b1e518 ["CALL", null, ["callee:00afaa08:8"]]
- 00b1e4d4 bytes 3c71ff97
+ 00b1e518 bytes 3c71ff97
- 00b1e544 ["INT_ADD", "register:40f0:8", ["const:b1e544:8", "const:4:8"]]
- 00b1e544 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b1e588 ["INT_ADD", "register:40f0:8", ["const:b1e588:8", "const:4:8"]]
+ 00b1e588 ["CALL", null, ["callee:00bdb190:8"]]
- 00b1e544 bytes fff20294
+ 00b1e588 bytes 02f30294
- 00b1e680 ["INT_ADD", "register:40f0:8", ["const:b1e680:8", "const:4:8"]]
- 00b1e680 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b1e6c4 ["INT_ADD", "register:40f0:8", ["const:b1e6c4:8", "const:4:8"]]
+ 00b1e6c4 ["CALL", null, ["callee:00bdb130:8"]]
- 00b1e680 bytes 98f20294
+ 00b1e6c4 bytes 9bf20294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1070cd0f23ae683bf70869c335c94397"></a>

### [`00b1ed64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1ed64.md) → [`00b1eda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1eda8.md) _ZN11flatbuffers6Parser13TryTypedValueEPKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEibRNS_5ValueENS_8BaseTypeEPb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bdf7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf7f0.md) · 呼出先 11件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 1件 [`00bdf840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf840.md) · 呼出先 11件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 97.16% / 新版 97.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b1ee60",
      "incomplete_value": true,
      "site": "00b1ee70",
      "value": [
        "LOAD",
        "16",
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
                "const:a:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1ee1c",
      "incomplete_value": true,
      "site": "00b1ee2c",
      "value": [
        "LOAD",
        "16",
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
                "const:a:8"
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
      "definition_site": "00b1ee64",
      "incomplete_value": true,
      "site": "00b1ee74",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ee0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b1ee20",
      "incomplete_value": true,
      "site": "00b1ee30",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:e55:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b1ee7c",
      "incomplete_value": true,
      "site": "00b1ee84",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b1ee38",
      "incomplete_value": true,
      "site": "00b1ee40",
      "value": [
        "LOAD",
        "8",
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
      "00b1ee50",
      "READ",
      [
        "storage",
        "00c1b9d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b1ee60",
      "READ",
      [
        "storage",
        "002a3e5f",
        null,
        "string"
      ]
    ],
    [
      "00b1ee64",
      "READ",
      [
        "storage",
        "002a3e55",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1ee50",
      "READ",
      [
        "storage",
        "00c1ba20",
        null,
        "pointer"
      ]
    ],
    [
      "00b1ee60",
      "READ",
      [
        "storage",
        "002a3eea",
        null,
        "string"
      ]
    ],
    [
      "00b1ee64",
      "READ",
      [
        "storage",
        "002a3ee0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b1edec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1ed64.md#insn-00b1edec) · [`00b1ee40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1ed64.md#insn-00b1ee40) · [`00b1ee7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1e/00b1ed64.md#insn-00b1ee7c)
- 新版 [`00b1ee30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1eda8.md#insn-00b1ee30) · [`00b1ee84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1eda8.md#insn-00b1ee84) · [`00b1eec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1e/00b1eda8.md#insn-00b1eec0)

~~~diff
- 00b1edec ["INT_ADD", "register:40f0:8", ["const:b1edec:8", "const:4:8"]]
- 00b1edec ["CALL", null, ["callee:00bde230:8"]]
+ 00b1ee30 ["INT_ADD", "register:40f0:8", ["const:b1ee30:8", "const:4:8"]]
+ 00b1ee30 ["CALL", null, ["callee:00bde230:8"]]
- 00b1edec bytes fdfc0294
+ 00b1ee30 bytes 00fd0294
- 00b1ee40 ["INT_ADD", "register:40f0:8", ["const:b1ee40:8", "const:4:8"]]
- 00b1ee40 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b1ee84 ["INT_ADD", "register:40f0:8", ["const:b1ee84:8", "const:4:8"]]
+ 00b1ee84 ["CALL", null, ["callee:00bdb190:8"]]
- 00b1ee40 bytes c0f00294
+ 00b1ee84 bytes c3f00294
- 00b1ee7c ["INT_ADD", "register:40f0:8", ["const:b1ee7c:8", "const:4:8"]]
- 00b1ee7c ["CALL", null, ["callee:00bdb130:8"]]
+ 00b1eec0 ["INT_ADD", "register:40f0:8", ["const:b1eec0:8", "const:4:8"]]
+ 00b1eec0 ["CALL", null, ["callee:00bdb130:8"]]
- 00b1ee7c bytes 99f00294
+ 00b1eec0 bytes 9cf00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68b7ca9d3611a51f6283965fe9eb94ce"></a>

### [`00b1f800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f800.md) → [`00b1f844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f844.md) _ZN11flatbuffers6Parser9ParseEnumEbPPNS_7EnumDefE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf9b0.md) · 呼出先 28件 [`00b417ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b41/00b417ec.md) [`00b421e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b42/00b421e0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00bdfa00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa00.md) · 呼出先 28件 [`00b41830`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b41830.md) [`00b42224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b42/00b42224.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.47% / 新版 97.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 12件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b203e8",
      "incomplete_value": true,
      "site": "00b203fc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b203a4",
      "incomplete_value": true,
      "site": "00b203b8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 141,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b203e8",
      "incomplete_value": true,
      "site": "00b203fc",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b203a4",
      "incomplete_value": true,
      "site": "00b203b8",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 142,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b203f4",
      "incomplete_value": true,
      "site": "00b20404",
      "value": [
        "LOAD",
        "16",
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
                "const:40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b203b0",
      "incomplete_value": true,
      "site": "00b203c0",
      "value": [
        "LOAD",
        "16",
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
                "const:40:8"
              ]
            ]
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
      "00b1fa88",
      "READ",
      [
        "storage",
        "002987c2",
        null,
        "string"
      ]
    ],
    [
      "00b1fcec",
      "PARAM",
      [
        "storage",
        "002a2e79",
        null,
        "string"
      ]
    ],
    [
      "00b202bc",
      "READ",
      [
        "storage",
        "002a61d0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b1fa88",
      "READ",
      [
        "storage",
        "00298735",
        null,
        "string"
      ]
    ],
    [
      "00b1fcec",
      "PARAM",
      [
        "storage",
        "002a2f04",
        null,
        "string"
      ]
    ],
    [
      "00b202bc",
      "READ",
      [
        "storage",
        "002a626a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b203fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f800.md#insn-00b203fc) · [`00b206b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f800.md#insn-00b206b0) · [`00b1f880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b1f/00b1f800.md#insn-00b1f880)
- 新版 [`00b20440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f844.md#insn-00b20440) · [`00b206f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f844.md#insn-00b206f4) · [`00b1f8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b1f/00b1f844.md#insn-00b1f8c4)

~~~diff
- 00b203fc ["INT_ADD", "register:40f0:8", ["const:b203fc:8", "const:4:8"]]
- 00b203fc ["CALL", null, ["callee:00bdb060:8"]]
+ 00b20440 ["INT_ADD", "register:40f0:8", ["const:b20440:8", "const:4:8"]]
+ 00b20440 ["CALL", null, ["callee:00bdb060:8"]]
- 00b203fc bytes 05eb0294
+ 00b20440 bytes 08eb0294
- 00b206b0 ["INT_ADD", "register:40f0:8", ["const:b206b0:8", "const:4:8"]]
- 00b206b0 ["CALL", null, ["callee:00bdfc90:8"]]
+ 00b206f4 ["INT_ADD", "register:40f0:8", ["const:b206f4:8", "const:4:8"]]
+ 00b206f4 ["CALL", null, ["callee:00bdfc90:8"]]
- 00b206b0 bytes 64fd0294
+ 00b206f4 bytes 67fd0294
- 00b1f880 ["INT_ADD", "register:40f0:8", ["const:b1f880:8", "const:4:8"]]
- 00b1f880 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b1f8c4 ["INT_ADD", "register:40f0:8", ["const:b1f8c4:8", "const:4:8"]]
+ 00b1f8c4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b1f880 bytes dced0294
+ 00b1f8c4 bytes dfed0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b21f6781816bc2848aa9e144b658bb05"></a>

### [`00b208ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b208ac.md) → [`00b208f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b208f0.md) _ZN11flatbuffers6Parser9StartEnumERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEbPPNS_7EnumDefE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf9f0.md) · 呼出先 9件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)
- 新版 呼出元 1件 [`00bdfa40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa40.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.24% / 新版 99.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b20a54",
      "incomplete_value": false,
      "site": "00b20a60",
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
            "const:7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b20a10",
      "incomplete_value": false,
      "site": "00b20a1c",
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
            "const:f7c:8"
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
      "00b20a54",
      "PARAM",
      [
        "storage",
        "0029cf7c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b20a54",
      "PARAM",
      [
        "storage",
        "0029d007",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b20a1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b208ac.md#insn-00b20a1c) · [`00b208ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b208ac.md#insn-00b208ec) · [`00b20974`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b208ac.md#insn-00b20974)
- 新版 [`00b20a60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b208f0.md#insn-00b20a60) · [`00b20930`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b208f0.md#insn-00b20930) · [`00b209b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b208f0.md#insn-00b209b8)

~~~diff
- 00b20a1c ["INT_ADD", "register:40f0:8", ["const:b20a1c:8", "const:4:8"]]
- 00b20a1c ["CALL", null, ["callee:00bdb260:8"]]
+ 00b20a60 ["INT_ADD", "register:40f0:8", ["const:b20a60:8", "const:4:8"]]
+ 00b20a60 ["CALL", null, ["callee:00bdb260:8"]]
- 00b20a1c bytes fde90294
+ 00b20a60 bytes 00ea0294
- 00b208ec ["INT_ADD", "register:40f0:8", ["const:b208ec:8", "const:4:8"]]
- 00b208ec ["CALL", null, ["callee:00bdb040:8"]]
+ 00b20930 ["INT_ADD", "register:40f0:8", ["const:b20930:8", "const:4:8"]]
+ 00b20930 ["CALL", null, ["callee:00bdb040:8"]]
- 00b208ec bytes c1e90294
+ 00b20930 bytes c4e90294
- 00b20974 ["INT_ADD", "register:40f0:8", ["const:b20974:8", "const:4:8"]]
- 00b20974 ["CALL", null, ["callee:00bde230:8"]]
+ 00b209b8 ["INT_ADD", "register:40f0:8", ["const:b209b8:8", "const:4:8"]]
+ 00b209b8 ["CALL", null, ["callee:00bde230:8"]]
- 00b20974 bytes 1bf60294
+ 00b209b8 bytes 1ef60294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8830bd8d3c747d155bd256e0191e262"></a>

### [`00b20bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20bb4.md) → [`00b20bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b20bf8.md) _ZN11flatbuffers14EnumValBuilder21AssignEnumeratorValueERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf330.md) · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)
- 新版 呼出元 1件 [`00bdf380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf380.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.80% / 新版 98.80%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b20cdc",
      "incomplete_value": false,
      "site": "00b20ce8",
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
            "const:527:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b20c98",
      "incomplete_value": false,
      "site": "00b20ca4",
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
            "const:5bb:8"
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
      "definition_site": "00b20cf0",
      "incomplete_value": false,
      "site": "00b20d00",
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
            "const:41f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b20cac",
      "incomplete_value": false,
      "site": "00b20cbc",
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
            "const:394:8"
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
      "00b20cdc",
      "PARAM",
      [
        "storage",
        "002af5bb",
        null,
        "string"
      ]
    ],
    [
      "00b20cf0",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b20cdc",
      "PARAM",
      [
        "storage",
        "002af527",
        null,
        "string"
      ]
    ],
    [
      "00b20cf0",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b20ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20bb4.md#insn-00b20ca4) · [`00b20cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20bb4.md#insn-00b20cbc) · [`00b20ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b20/00b20bb4.md#insn-00b20ce8)
- 新版 [`00b20ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b20bf8.md#insn-00b20ce8) · [`00b20d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b20bf8.md#insn-00b20d00) · [`00b20d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b20/00b20bf8.md#insn-00b20d2c)

~~~diff
- 00b20ca4 ["INT_ADD", "register:40f0:8", ["const:b20ca4:8", "const:4:8"]]
- 00b20ca4 ["CALL", null, ["callee:00bdb260:8"]]
+ 00b20ce8 ["INT_ADD", "register:40f0:8", ["const:b20ce8:8", "const:4:8"]]
+ 00b20ce8 ["CALL", null, ["callee:00bdb260:8"]]
- 00b20ca4 bytes 5be90294
+ 00b20ce8 bytes 5ee90294
- 00b20cbc ["INT_ADD", "register:40f0:8", ["const:b20cbc:8", "const:4:8"]]
- 00b20cbc ["CALL", null, ["callee:00bdb130:8"]]
+ 00b20d00 ["INT_ADD", "register:40f0:8", ["const:b20d00:8", "const:4:8"]]
+ 00b20d00 ["CALL", null, ["callee:00bdb130:8"]]
- 00b20cbc bytes 09e90294
+ 00b20d00 bytes 0ce90294
- 00b20ce8 ["INT_ADD", "register:40f0:8", ["const:b20ce8:8", "const:4:8"]]
- 00b20ce8 ["CALL", null, ["callee:00bdb260:8"]]
+ 00b20d2c ["INT_ADD", "register:40f0:8", ["const:b20d2c:8", "const:4:8"]]
+ 00b20d2c ["CALL", null, ["callee:00bdb260:8"]]
- 00b20ce8 bytes 4ae90294
+ 00b20d2c bytes 4de90294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c11727395aab914f8213acd6575851c3"></a>

### [`00b211c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b211c0.md) → [`00b21204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b21/00b21204.md) _ZN11flatbuffers6Parser10CheckClashERNSt6__ndk16vectorIPNS_8FieldDefENS1_9allocatorIS4_EEEEPNS_9StructDefEPKcNS_8BaseTypeE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf6e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf6e0.md) · 呼出先 10件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)
- 新版 呼出元 1件 [`00bdf730`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf730.md) · 呼出先 10件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.44% / 新版 99.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b213d0",
      "incomplete_value": false,
      "site": "00b213dc",
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
            "const:4e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2138c",
      "incomplete_value": false,
      "site": "00b21398",
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
            "const:576:8"
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
      "00b213d0",
      "PARAM",
      [
        "storage",
        "002af576",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b213d0",
      "PARAM",
      [
        "storage",
        "002af4e2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b21398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b211c0.md#insn-00b21398) · [`00b21208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b211c0.md#insn-00b21208) · [`00b21274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b211c0.md#insn-00b21274)
- 新版 [`00b213dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b21/00b21204.md#insn-00b213dc) · [`00b2124c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b21/00b21204.md#insn-00b2124c) · [`00b212b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b21/00b21204.md#insn-00b212b8)

~~~diff
- 00b21398 ["INT_ADD", "register:40f0:8", ["const:b21398:8", "const:4:8"]]
- 00b21398 ["CALL", null, ["callee:00bdb260:8"]]
+ 00b213dc ["INT_ADD", "register:40f0:8", ["const:b213dc:8", "const:4:8"]]
+ 00b213dc ["CALL", null, ["callee:00bdb260:8"]]
- 00b21398 bytes 9ee70294
+ 00b213dc bytes a1e70294
- 00b21208 ["INT_ADD", "register:40f0:8", ["const:b21208:8", "const:4:8"]]
- 00b21208 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b2124c ["INT_ADD", "register:40f0:8", ["const:b2124c:8", "const:4:8"]]
+ 00b2124c ["CALL", null, ["callee:00bdb190:8"]]
- 00b21208 bytes cee70294
+ 00b2124c bytes d1e70294
- 00b21274 ["INT_ADD", "register:40f0:8", ["const:b21274:8", "const:4:8"]]
- 00b21274 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b212b8 ["INT_ADD", "register:40f0:8", ["const:b212b8:8", "const:4:8"]]
+ 00b212b8 ["CALL", null, ["callee:00bdb190:8"]]
- 00b21274 bytes b3e70294
+ 00b212b8 bytes b6e70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-058a8dc3b186a0d34c6e416c4eeda158"></a>

### [`00b2186c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b2186c.md) → [`00b218b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b21/00b218b0.md) _ZN11flatbuffers6Parser9ParseDeclEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf9a0.md) · 呼出先 25件 [`00b222dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b222dc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 1件 [`00bdf9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9f0.md) · 呼出先 25件 [`00b22320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22320.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 95.51% / 新版 95.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `store_value` 10件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b219d4",
      "incomplete_value": true,
      "site": "00b21a04",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fa8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b21990",
      "incomplete_value": true,
      "site": "00b219c0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:f1d:8"
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
      "definition_site": "00b21c00",
      "incomplete_value": true,
      "site": "00b21c00",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b21bbc",
      "incomplete_value": true,
      "site": "00b21bbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 38,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b21c04",
      "incomplete_value": true,
      "site": "00b21c04",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b21bc0",
      "incomplete_value": true,
      "site": "00b21bc0",
      "value": [
        "LOAD",
        "8",
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
      "00b219b8",
      "PARAM",
      [
        "storage",
        "002a6202",
        null,
        "string"
      ]
    ],
    [
      "00b219d4",
      "READ",
      [
        "storage",
        "002a1f1d",
        null,
        "string"
      ]
    ],
    [
      "00b21be0",
      "READ",
      [
        "storage",
        "002a002c",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b219b8",
      "PARAM",
      [
        "storage",
        "002a629c",
        null,
        "string"
      ]
    ],
    [
      "00b219d4",
      "READ",
      [
        "storage",
        "002a1fa8",
        null,
        "string"
      ]
    ],
    [
      "00b21be0",
      "READ",
      [
        "storage",
        "002a00b7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b21c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b2186c.md#insn-00b21c04) · [`00b21fac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b2186c.md#insn-00b21fac) · [`00b21ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b21/00b2186c.md#insn-00b21ff0)
- 新版 [`00b21c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b21/00b218b0.md#insn-00b21c48) · [`00b21ff0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b21/00b218b0.md#insn-00b21ff0) · [`00b22034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b21/00b218b0.md#insn-00b22034)

~~~diff
- 00b21c04 ["INT_ADD", "register:40f0:8", ["const:b21c04:8", "const:4:8"]]
- 00b21c04 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b21c48 ["INT_ADD", "register:40f0:8", ["const:b21c48:8", "const:4:8"]]
+ 00b21c48 ["CALL", null, ["callee:00bdb060:8"]]
- 00b21c04 bytes 03e50294
+ 00b21c48 bytes 06e50294
- 00b21fac ["INT_ADD", "register:40f0:8", ["const:b21fac:8", "const:4:8"]]
- 00b21fac ["CALL", null, ["callee:00bdf730:8"]]
+ 00b21ff0 ["INT_ADD", "register:40f0:8", ["const:b21ff0:8", "const:4:8"]]
+ 00b21ff0 ["CALL", null, ["callee:00bdf730:8"]]
- 00b21fac bytes cdf50294
+ 00b21ff0 bytes d0f50294
- 00b21ff0 ["COPY", "tmp:0:8", ["const:115:8"]]
- 00b21ff0 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b21ff0 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b21ff0 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b22034 ["COPY", "tmp:0:8", ["const:1af:8"]]
+ 00b22034 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b22034 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b22034 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b21ff0 bytes 63540491
+ 00b22034 bytes 63bc0691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eeaffa6c0ed248a0646344ca36e1833b"></a>

### [`00b22414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22414.md) → [`00b22458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22458.md) _ZN11flatbuffers6Parser12ParseServiceEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf790.md) · 呼出先 17件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)
- 新版 呼出元 1件 [`00bdf7e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf7e0.md) · 呼出先 17件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.63% / 新版 99.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2277c",
      "incomplete_value": false,
      "site": "00b22788",
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
            "const:65:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b22738",
      "incomplete_value": false,
      "site": "00b22744",
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
            "const:fda:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b22be0",
      "incomplete_value": false,
      "site": "00b22be4",
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
            "const:1b7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b22b9c",
      "incomplete_value": false,
      "site": "00b22ba0",
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
            "const:11d:8"
          ]
        ]
      ]
    },
    "ordinal": 45,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b2277c",
      "PARAM",
      [
        "storage",
        "0029efda",
        null,
        "string"
      ]
    ],
    [
      "00b22be0",
      "PARAM",
      [
        "storage",
        "002a711d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2277c",
      "PARAM",
      [
        "storage",
        "0029f065",
        null,
        "string"
      ]
    ],
    [
      "00b22be0",
      "PARAM",
      [
        "storage",
        "002a71b7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b22744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22414.md#insn-00b22744) · [`00b22ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22414.md#insn-00b22ba0) · [`00b2247c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b22/00b22414.md#insn-00b2247c)
- 新版 [`00b22788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22458.md#insn-00b22788) · [`00b22be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22458.md#insn-00b22be4) · [`00b224c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b22/00b22458.md#insn-00b224c0)

~~~diff
- 00b22744 ["INT_ADD", "register:40f0:8", ["const:b22744:8", "const:4:8"]]
- 00b22744 ["CALL", null, ["callee:00bdb260:8"]]
+ 00b22788 ["INT_ADD", "register:40f0:8", ["const:b22788:8", "const:4:8"]]
+ 00b22788 ["CALL", null, ["callee:00bdb260:8"]]
- 00b22744 bytes b3e20294
+ 00b22788 bytes b6e20294
- 00b22ba0 ["INT_ADD", "register:40f0:8", ["const:b22ba0:8", "const:4:8"]]
- 00b22ba0 ["CALL", null, ["callee:00bdb260:8"]]
+ 00b22be4 ["INT_ADD", "register:40f0:8", ["const:b22be4:8", "const:4:8"]]
+ 00b22be4 ["CALL", null, ["callee:00bdb260:8"]]
- 00b22ba0 bytes 9ce10294
+ 00b22be4 bytes 9fe10294
- 00b2247c ["INT_ADD", "register:40f0:8", ["const:b2247c:8", "const:4:8"]]
- 00b2247c ["CALL", null, ["callee:00bdb040:8"]]
+ 00b224c0 ["INT_ADD", "register:40f0:8", ["const:b224c0:8", "const:4:8"]]
+ 00b224c0 ["CALL", null, ["callee:00bdb040:8"]]
- 00b2247c bytes dde20294
+ 00b224c0 bytes e0e20294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-11b76cdd73129990770dfe26b8412c16"></a>

### [`00b234f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b234f8.md) → [`00b2353c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b2353c.md) _ZN11flatbuffers6Parser14ParseProtoDeclEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf810.md) · 呼出先 25件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdf860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf860.md) · 呼出先 25件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.51% / 新版 98.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b23878",
      "incomplete_value": true,
      "site": "00b2387c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b23834",
      "incomplete_value": true,
      "site": "00b23838",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b23a38",
      "incomplete_value": false,
      "site": "00b23a48",
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
            "const:fcd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b239f4",
      "incomplete_value": false,
      "site": "00b23a04",
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
            "const:f42:8"
          ]
        ]
      ]
    },
    "ordinal": 23,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b235b0",
      "PARAM",
      [
        "storage",
        "002a1f32",
        null,
        "string"
      ]
    ],
    [
      "00b235d0",
      "PARAM",
      [
        "storage",
        "002a2e96",
        null,
        "string"
      ]
    ],
    [
      "00b236e8",
      "PARAM",
      [
        "storage",
        "002a00cd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b235b0",
      "PARAM",
      [
        "storage",
        "002a1fbd",
        null,
        "string"
      ]
    ],
    [
      "00b235d0",
      "PARAM",
      [
        "storage",
        "002a2f21",
        null,
        "string"
      ]
    ],
    [
      "00b236e8",
      "PARAM",
      [
        "storage",
        "002a0158",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b23838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b234f8.md#insn-00b23838) · [`00b23a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b234f8.md#insn-00b23a04) · [`00b2356c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b234f8.md#insn-00b2356c)
- 新版 [`00b2387c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b2353c.md#insn-00b2387c) · [`00b23a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b2353c.md#insn-00b23a48) · [`00b235b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b2353c.md#insn-00b235b0)

~~~diff
- 00b23838 ["INT_ADD", "register:40f0:8", ["const:b23838:8", "const:4:8"]]
- 00b23838 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b2387c ["INT_ADD", "register:40f0:8", ["const:b2387c:8", "const:4:8"]]
+ 00b2387c ["CALL", null, ["callee:00bdb190:8"]]
- 00b23838 bytes 42de0294
+ 00b2387c bytes 45de0294
- 00b23a04 ["INT_ADD", "register:40f0:8", ["const:b23a04:8", "const:4:8"]]
- 00b23a04 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b23a48 ["INT_ADD", "register:40f0:8", ["const:b23a48:8", "const:4:8"]]
+ 00b23a48 ["CALL", null, ["callee:00bdc180:8"]]
- 00b23a04 bytes cbe10294
+ 00b23a48 bytes cee10294
- 00b2356c ["COPY", "tmp:0:8", ["const:f32:8"]]
- 00b2356c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b2356c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b2356c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b235b0 ["COPY", "tmp:0:8", ["const:fbd:8"]]
+ 00b235b0 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b235b0 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b235b0 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b2356c bytes 21c83c91
+ 00b235b0 bytes 21f43e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-748358698afe60822dbfb9872d840dec"></a>

### [`00b23f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b23f78.md) → [`00b23fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b23fbc.md) _ZN11flatbuffers6Parser16ParseProtoFieldsEPNS_9StructDefEbb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b23f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b23f78.md) [`00bdf880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf880.md) · 呼出先 30件 [`00b23f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b23f78.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md)
- 新版 呼出元 2件 [`00b23fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b23fbc.md) [`00bdf8d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf8d0.md) · 呼出先 30件 [`00b23fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b23fbc.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.94% / 新版 98.94%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b242c4",
      "incomplete_value": true,
      "site": "00b242c8",
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
            "const:f21:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b24280",
      "incomplete_value": true,
      "site": "00b24284",
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
            "const:e96:8"
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
      "definition_site": "00b242e8",
      "incomplete_value": true,
      "site": "00b242ec",
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
            "const:158:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b242a4",
      "incomplete_value": true,
      "site": "00b242a8",
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
            "const:cd:8"
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
      "definition_site": "00b24308",
      "incomplete_value": true,
      "site": "00b2430c",
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
            "const:f04:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b242c4",
      "incomplete_value": true,
      "site": "00b242c8",
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
            "const:e79:8"
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
      "00b241a0",
      "DATA",
      [
        "storage",
        "002f850d",
        "switchD_00b24164::switchdataD_002f850d",
        "byte"
      ]
    ],
    [
      "00b242c4",
      "PARAM",
      [
        "storage",
        "002a2e96",
        null,
        "string"
      ]
    ],
    [
      "00b242e8",
      "PARAM",
      [
        "storage",
        "002a00cd",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b241a0",
      "DATA",
      [
        "storage",
        "002f850d",
        "switchD_00b241a8::switchdataD_002f850d",
        "byte"
      ]
    ],
    [
      "00b242c4",
      "PARAM",
      [
        "storage",
        "002a2f21",
        null,
        "string"
      ]
    ],
    [
      "00b242e8",
      "PARAM",
      [
        "storage",
        "002a0158",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b24284`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b23f78.md#insn-00b24284) · [`00b242a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b23f78.md#insn-00b242a8) · [`00b242c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b23/00b23f78.md#insn-00b242c8)
- 新版 [`00b242c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b23fbc.md#insn-00b242c8) · [`00b242ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b23fbc.md#insn-00b242ec) · [`00b2430c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b23/00b23fbc.md#insn-00b2430c)

~~~diff
- 00b24284 ["INT_ADD", "register:40f0:8", ["const:b24284:8", "const:4:8"]]
- 00b24284 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b242c8 ["INT_ADD", "register:40f0:8", ["const:b242c8:8", "const:4:8"]]
+ 00b242c8 ["CALL", null, ["callee:00bdb200:8"]]
- 00b24284 bytes cbdb0294
+ 00b242c8 bytes cedb0294
- 00b242a8 ["INT_ADD", "register:40f0:8", ["const:b242a8:8", "const:4:8"]]
- 00b242a8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b242ec ["INT_ADD", "register:40f0:8", ["const:b242ec:8", "const:4:8"]]
+ 00b242ec ["CALL", null, ["callee:00bdb200:8"]]
- 00b242a8 bytes c2db0294
+ 00b242ec bytes c5db0294
- 00b242c8 ["INT_ADD", "register:40f0:8", ["const:b242c8:8", "const:4:8"]]
- 00b242c8 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b2430c ["INT_ADD", "register:40f0:8", ["const:b2430c:8", "const:4:8"]]
+ 00b2430c ["CALL", null, ["callee:00bdb200:8"]]
- 00b242c8 bytes badb0294
+ 00b2430c bytes bddb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3a47f680b9073c8f672b24182b20cfc"></a>

### [`00b255a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b255a0.md) → [`00b255e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b255e4.md) _ZN11flatbuffers14EnumValBuilder16AcceptEnumeratorERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf320.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdf1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf1f0.md) [`00bdf310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf310.md)
- 新版 呼出元 1件 [`00bdf370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf370.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdf240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf240.md) [`00bdf360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf360.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.44% / 新版 98.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2565c",
      "incomplete_value": false,
      "site": "00b25668",
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
            "const:82d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b25618",
      "incomplete_value": false,
      "site": "00b25624",
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
            "const:82f:8"
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
      "00b2565c",
      "PARAM",
      [
        "storage",
        "0029a82f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2565c",
      "PARAM",
      [
        "storage",
        "0029a82d",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b25624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b255a0.md#insn-00b25624) · [`00b255e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b255a0.md#insn-00b255e4) · [`00b25604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b25/00b255a0.md#insn-00b25604)
- 新版 [`00b25668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b255e4.md#insn-00b25668) · [`00b25628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b255e4.md#insn-00b25628) · [`00b25648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b25/00b255e4.md#insn-00b25648)

~~~diff
- 00b25624 ["INT_ADD", "register:40f0:8", ["const:b25624:8", "const:4:8"]]
- 00b25624 ["CALL", null, ["callee:00bdb260:8"]]
+ 00b25668 ["INT_ADD", "register:40f0:8", ["const:b25668:8", "const:4:8"]]
+ 00b25668 ["CALL", null, ["callee:00bdb260:8"]]
- 00b25624 bytes fbd60294
+ 00b25668 bytes fed60294
- 00b255e4 ["INT_ADD", "register:40f0:8", ["const:b255e4:8", "const:4:8"]]
- 00b255e4 ["CALL", null, ["callee:00bdf360:8"]]
+ 00b25628 ["INT_ADD", "register:40f0:8", ["const:b25628:8", "const:4:8"]]
+ 00b25628 ["CALL", null, ["callee:00bdf360:8"]]
- 00b255e4 bytes 4be70294
+ 00b25628 bytes 4ee70294
- 00b25604 ["INT_ADD", "register:40f0:8", ["const:b25604:8", "const:4:8"]]
- 00b25604 ["CALL", null, ["callee:00bdf240:8"]]
+ 00b25648 ["INT_ADD", "register:40f0:8", ["const:b25648:8", "const:4:8"]]
+ 00b25648 ["CALL", null, ["callee:00bdf240:8"]]
- 00b25604 bytes fbe60294
+ 00b25648 bytes fee60294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4833f1feef0064f3ee8cd1afaad3c993"></a>

### [`00b26118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b26118.md) → [`00b2615c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b2615c.md) _ZN11flatbuffers6Parser14StartParseFileEPKcS2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf830.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bde1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1e0.md)
- 新版 呼出元 1件 [`00bdf880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf880.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bde230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde230.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.62% / 新版 94.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2622c",
      "incomplete_value": true,
      "site": "00b2625c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:513:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b261e8",
      "incomplete_value": true,
      "site": "00b26218",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:5a0:8"
              ]
            ]
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
      "00b26198",
      "PARAM",
      [
        "storage",
        "00296866",
        null,
        "undefined1"
      ]
    ],
    [
      "00b2622c",
      "READ",
      [
        "storage",
        "002965a0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b26198",
      "PARAM",
      [
        "storage",
        "002967d9",
        null,
        "undefined1"
      ]
    ],
    [
      "00b2622c",
      "READ",
      [
        "storage",
        "00296513",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b26140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b26118.md#insn-00b26140) · [`00b26160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b26118.md#insn-00b26160) · [`00b26170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b26118.md#insn-00b26170)
- 新版 [`00b26184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b2615c.md#insn-00b26184) · [`00b261a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b2615c.md#insn-00b261a4) · [`00b261b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b2615c.md#insn-00b261b4)

~~~diff
- 00b26140 ["COPY", "tmp:0:8", ["const:866:8"]]
- 00b26140 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
- 00b26140 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
- 00b26140 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
+ 00b26184 ["COPY", "tmp:0:8", ["const:7d9:8"]]
+ 00b26184 ["INT_CARRY", "register:105:1", ["register:4048:8", "tmp:0:8"]]
+ 00b26184 ["INT_SCARRY", "register:106:1", ["register:4048:8", "tmp:0:8"]]
+ 00b26184 ["INT_ADD", "tmp:1:8", ["register:4048:8", "tmp:0:8"]]
- 00b26140 bytes 29992191
+ 00b26184 bytes 29651f91
- 00b26160 ["INT_ADD", "register:40f0:8", ["const:b26160:8", "const:4:8"]]
- 00b26160 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b261a4 ["INT_ADD", "register:40f0:8", ["const:b261a4:8", "const:4:8"]]
+ 00b261a4 ["CALL", null, ["callee:00bdb190:8"]]
- 00b26160 bytes f8d30294
+ 00b261a4 bytes fbd30294
- 00b26170 ["INT_ADD", "register:40f0:8", ["const:b26170:8", "const:4:8"]]
- 00b26170 ["CALL", null, ["callee:00bde230:8"]]
+ 00b261b4 ["INT_ADD", "register:40f0:8", ["const:b261b4:8", "const:4:8"]]
+ 00b261b4 ["CALL", null, ["callee:00bde230:8"]]
- 00b26170 bytes 1ce00294
+ 00b261b4 bytes 1fe00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1ab2119b41aee9117bffae3a02e7678"></a>

### [`00b2640c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b2640c.md) → [`00b26450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b26450.md) _ZN11flatbuffers6Parser9ParseRootEPKcPS2_S2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf9d0.md) · 呼出先 15件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0a0.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md)
- 新版 呼出元 1件 [`00bdfa20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfa20.md) · 呼出先 15件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb0f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb0f0.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.86% / 新版 98.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2682c",
      "incomplete_value": false,
      "site": "00b26834",
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
            "const:4e9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b267e8",
      "incomplete_value": false,
      "site": "00b267f0",
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
            "const:57d:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b26874",
      "incomplete_value": false,
      "site": "00b26880",
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
            "const:7b9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b26830",
      "incomplete_value": false,
      "site": "00b2683c",
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
            "const:846:8"
          ]
        ]
      ]
    },
    "ordinal": 20,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2693c",
      "incomplete_value": false,
      "site": "00b2694c",
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
            "const:fd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b268f8",
      "incomplete_value": false,
      "site": "00b26908",
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
            "const:f4d:8"
          ]
        ]
      ]
    },
    "ordinal": 29,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b2682c",
      "PARAM",
      [
        "storage",
        "002af57d",
        null,
        "string"
      ]
    ],
    [
      "00b26874",
      "PARAM",
      [
        "storage",
        "00298846",
        null,
        "string"
      ]
    ],
    [
      "00b2693c",
      "PARAM",
      [
        "storage",
        "0029df4d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2682c",
      "PARAM",
      [
        "storage",
        "002af4e9",
        null,
        "string"
      ]
    ],
    [
      "00b26874",
      "PARAM",
      [
        "storage",
        "002987b9",
        null,
        "string"
      ]
    ],
    [
      "00b2693c",
      "PARAM",
      [
        "storage",
        "0029dfd8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b267f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b2640c.md#insn-00b267f0) · [`00b2683c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b2640c.md#insn-00b2683c) · [`00b26880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b2640c.md#insn-00b26880)
- 新版 [`00b26834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b26450.md#insn-00b26834) · [`00b26880`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b26450.md#insn-00b26880) · [`00b268c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b26450.md#insn-00b268c4)

~~~diff
- 00b267f0 ["INT_ADD", "register:40f0:8", ["const:b267f0:8", "const:4:8"]]
- 00b267f0 ["CALL", null, ["callee:00bdb260:8"]]
+ 00b26834 ["INT_ADD", "register:40f0:8", ["const:b26834:8", "const:4:8"]]
+ 00b26834 ["CALL", null, ["callee:00bdb260:8"]]
- 00b267f0 bytes 88d20294
+ 00b26834 bytes 8bd20294
- 00b2683c ["INT_ADD", "register:40f0:8", ["const:b2683c:8", "const:4:8"]]
- 00b2683c ["CALL", null, ["callee:00bdb260:8"]]
+ 00b26880 ["INT_ADD", "register:40f0:8", ["const:b26880:8", "const:4:8"]]
+ 00b26880 ["CALL", null, ["callee:00bdb260:8"]]
- 00b2683c bytes 75d20294
+ 00b26880 bytes 78d20294
- 00b26880 ["INT_ADD", "register:40f0:8", ["const:b26880:8", "const:4:8"]]
- 00b26880 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b268c4 ["INT_ADD", "register:40f0:8", ["const:b268c4:8", "const:4:8"]]
+ 00b268c4 ["CALL", null, ["callee:00bdb130:8"]]
- 00b26880 bytes 18d20294
+ 00b268c4 bytes 1bd20294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb540ee4502b52bde2df95f4b2fe2248"></a>

### [`00b26ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b26ae4.md) → [`00b26b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b26b28.md) _ZN11flatbuffers6Parser7DoParseEPKcPS2_S2_S2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b26ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b26ae4.md) [`00bdf970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf970.md) · 呼出先 41件 [`0044a6d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a6d0.md) [`0044a7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0044a/0044a7d4.md) [`0051d9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0051d/0051d9f8.md) [`0052773c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00527/0052773c.md) [`00541408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00541/00541408.md)
- 新版 呼出元 2件 [`00b26b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b26b28.md) [`00bdf9c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf9c0.md) · 呼出先 41件 [`0044a6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a6d0.md) [`0044a7d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0044a/0044a7d4.md) [`0051d9f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0051d/0051d9f8.md) [`0052773c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00527/0052773c.md) [`00541408`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00541/00541408.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.35% / 新版 98.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 13件, `store_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b28334",
      "incomplete_value": true,
      "site": "00b28344",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:41:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b282f0",
      "incomplete_value": true,
      "site": "00b28300",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:fb6:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 277,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b28334",
      "incomplete_value": true,
      "site": "00b28344",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b282f0",
      "incomplete_value": true,
      "site": "00b28300",
      "value": [
        "LOAD",
        "16",
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
    "ordinal": 278,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b28338",
      "incomplete_value": true,
      "site": "00b28348",
      "value": [
        "LOAD",
        "16",
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
                "const:1f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b282f4",
      "incomplete_value": true,
      "site": "00b28304",
      "value": [
        "LOAD",
        "16",
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
                "const:1f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 279,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b26f00",
      "DATA",
      [
        "storage",
        "00c24768",
        null,
        "pointer"
      ]
    ],
    [
      "00b270d4",
      "PARAM",
      [
        "storage",
        "002a2e79",
        null,
        "string"
      ]
    ],
    [
      "00b270ec",
      "PARAM",
      [
        "storage",
        "002a6208",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b26f00",
      "DATA",
      [
        "storage",
        "00c247b8",
        null,
        "pointer"
      ]
    ],
    [
      "00b270d4",
      "PARAM",
      [
        "storage",
        "002a2f04",
        null,
        "string"
      ]
    ],
    [
      "00b270ec",
      "PARAM",
      [
        "storage",
        "002a62a2",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b27094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b26ae4.md#insn-00b27094) · [`00b270ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b26ae4.md#insn-00b270ac) · [`00b270d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b26/00b26ae4.md#insn-00b270d8)
- 新版 [`00b270d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b26b28.md#insn-00b270d8) · [`00b270f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b26b28.md#insn-00b270f0) · [`00b2711c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b26/00b26b28.md#insn-00b2711c)

~~~diff
- 00b27094 ["INT_ADD", "register:40f0:8", ["const:b27094:8", "const:4:8"]]
- 00b27094 ["CALL", null, ["callee:00bdb200:8"]]
+ 00b270d8 ["INT_ADD", "register:40f0:8", ["const:b270d8:8", "const:4:8"]]
+ 00b270d8 ["CALL", null, ["callee:00bdb200:8"]]
- 00b27094 bytes 47d00294
+ 00b270d8 bytes 4ad00294
- 00b270ac ["INT_ADD", "register:40f0:8", ["const:b270ac:8", "const:4:8"]]
- 00b270ac ["CALL", null, ["callee:00bdb200:8"]]
+ 00b270f0 ["INT_ADD", "register:40f0:8", ["const:b270f0:8", "const:4:8"]]
+ 00b270f0 ["CALL", null, ["callee:00bdb200:8"]]
- 00b270ac bytes 41d00294
+ 00b270f0 bytes 44d00294
- 00b270d8 ["COPY", "tmp:0:8", ["const:f32:8"]]
- 00b270d8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b270d8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b270d8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b2711c ["COPY", "tmp:0:8", ["const:fbd:8"]]
+ 00b2711c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b2711c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b2711c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b270d8 bytes 21c83c91
+ 00b2711c bytes 21f43e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcddac8c8d284a85df4f6971a8cac0ad"></a>

### [`00b28904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28904.md) → [`00b28948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b28948.md) _ZN11flatbuffers6Parser9SerializeEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 27件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 0件  · 呼出先 27件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.75% / 新版 99.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b28f3c",
      "incomplete_value": false,
      "site": "00b28f44",
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
            "const:44c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b28ef8",
      "incomplete_value": false,
      "site": "00b28f00",
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
            "const:4d9:8"
          ]
        ]
      ]
    },
    "ordinal": 36,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b28cd8",
      "READ",
      [
        "storage",
        "00c1ba18",
        null,
        "pointer"
      ]
    ],
    [
      "00b28cf8",
      "PARAM",
      [
        "storage",
        "010a0ef3",
        "_ZZN11flatbuffers4dataINS_6OffsetIN10reflection6ObjectEEENSt6__ndk19allocatorIS4_EEEEPT_RNS5_6vectorIS8_T0_EEE1t",
        "undefined1"
      ]
    ],
    [
      "00b28d48",
      "READ",
      [
        "storage",
        "00c1ba08",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b28cd8",
      "READ",
      [
        "storage",
        "00c1ba68",
        null,
        "pointer"
      ]
    ],
    [
      "00b28cf8",
      "PARAM",
      [
        "storage",
        "010a0f33",
        "_ZZN11flatbuffers4dataINS_6OffsetIN10reflection6ObjectEEENSt6__ndk19allocatorIS4_EEEEPT_RNS5_6vectorIS8_T0_EEE1t",
        "undefined1"
      ]
    ],
    [
      "00b28d48",
      "READ",
      [
        "storage",
        "00c1ba58",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b28ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28904.md#insn-00b28ebc) · [`00b28f00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28904.md#insn-00b28f00) · [`00b28994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28904.md#insn-00b28994)
- 新版 [`00b28f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b28948.md#insn-00b28f00) · [`00b28f44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b28948.md#insn-00b28f44) · [`00b289d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b28948.md#insn-00b289d8)

~~~diff
- 00b28ebc ["INT_ADD", "register:40f0:8", ["const:b28ebc:8", "const:4:8"]]
- 00b28ebc ["CALL", null, ["callee:00bdf540:8"]]
+ 00b28f00 ["INT_ADD", "register:40f0:8", ["const:b28f00:8", "const:4:8"]]
+ 00b28f00 ["CALL", null, ["callee:00bdf540:8"]]
- 00b28ebc bytes 8dd90294
+ 00b28f00 bytes 90d90294
- 00b28f00 ["INT_ADD", "register:40f0:8", ["const:b28f00:8", "const:4:8"]]
- 00b28f00 ["CALL", null, ["callee:00bdf500:8"]]
+ 00b28f44 ["INT_ADD", "register:40f0:8", ["const:b28f44:8", "const:4:8"]]
+ 00b28f44 ["CALL", null, ["callee:00bdf500:8"]]
- 00b28f00 bytes 6cd90294
+ 00b28f44 bytes 6fd90294
- 00b28994 ["INT_ADD", "register:40f0:8", ["const:b28994:8", "const:4:8"]]
- 00b28994 ["CALL", null, ["callee:00bdeb60:8"]]
+ 00b289d8 ["INT_ADD", "register:40f0:8", ["const:b289d8:8", "const:4:8"]]
+ 00b289d8 ["CALL", null, ["callee:00bdeb60:8"]]
- 00b28994 bytes 5fd80294
+ 00b289d8 bytes 62d80294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b42e88a92b3fbba6f9081136e6920a1c"></a>

### [`00b28f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28f64.md) → [`00b28fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b28fa8.md) _ZN11flatbuffers13AssignIndicesINS_9StructDefEEEvRKNSt6__ndk16vectorIPT_NS2_9allocatorIS5_EEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf240`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf240.md) · 呼出先 7件 [`00b448cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b44/00b448cc.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdf290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf290.md) · 呼出先 7件 [`00b44910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b44/00b44910.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.33% / 新版 97.33%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2901c",
      "incomplete_value": true,
      "site": "00b2902c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b28fd8",
      "incomplete_value": true,
      "site": "00b28fe8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:9e8:8"
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
      "00b2901c",
      "READ",
      [
        "storage",
        "00c1b9e8",
        null,
        "pointer"
      ]
    ],
    [
      "00b2902c",
      "DATA",
      [
        "storage",
        "00b448cc",
        "_ZN11flatbuffers11compareNameINS_9StructDefEEEbPKT_S4_",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b2901c",
      "READ",
      [
        "storage",
        "00c1ba38",
        null,
        "pointer"
      ]
    ],
    [
      "00b2902c",
      "DATA",
      [
        "storage",
        "00b44910",
        "_ZN11flatbuffers11compareNameINS_9StructDefEEEbPKT_S4_",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b28fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28f64.md#insn-00b28fa0) · [`00b28fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28f64.md#insn-00b28fbc) · [`00b28fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b28/00b28f64.md#insn-00b28fd8)
- 新版 [`00b28fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b28fa8.md#insn-00b28fe4) · [`00b29000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b28fa8.md#insn-00b29000) · [`00b2901c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b28/00b28fa8.md#insn-00b2901c)

~~~diff
- 00b28fa0 ["INT_ADD", "register:40f0:8", ["const:b28fa0:8", "const:4:8"]]
- 00b28fa0 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b28fe4 ["INT_ADD", "register:40f0:8", ["const:b28fe4:8", "const:4:8"]]
+ 00b28fe4 ["CALL", null, ["callee:00bdb040:8"]]
- 00b28fa0 bytes 14c80294
+ 00b28fe4 bytes 17c80294
- 00b28fbc ["INT_ADD", "register:40f0:8", ["const:b28fbc:8", "const:4:8"]]
- 00b28fbc ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b29000 ["INT_ADD", "register:40f0:8", ["const:b29000:8", "const:4:8"]]
+ 00b29000 ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b28fbc bytes 69c80294
+ 00b29000 bytes 6cc80294
- 00b28fd8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9e8:8"]]
- 00b28fd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b2901c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a38:8"]]
+ 00b2901c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b28fd8 bytes 08f544f9
+ 00b2901c bytes 081d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09880e35a9b434139737536f61fb11cc"></a>

### [`00b2a248`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2a248.md) → [`00b2a28c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2a28c.md) _ZN11flatbuffers9StructDef11DeserializeERNS_6ParserEPKN10reflection6ObjectE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdfa90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa90.md) · 呼出先 14件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdb1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1f0.md)
- 新版 呼出元 1件 [`00bdfae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfae0.md) · 呼出先 14件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bdb240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb240.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.08% / 新版 98.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2a454",
      "incomplete_value": true,
      "site": "00b2a454",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b7:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2a410",
      "incomplete_value": true,
      "site": "00b2a410",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c:8"
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
    "kind": "store_value",
    "new": {
      "definition_site": "00b2a458",
      "incomplete_value": true,
      "site": "00b2a458",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b2a414",
      "incomplete_value": true,
      "site": "00b2a414",
      "value": [
        "LOAD",
        "8",
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
    "ordinal": 37,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2a610",
      "incomplete_value": false,
      "site": "00b2a618",
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
            "const:4cc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2a5cc",
      "incomplete_value": false,
      "site": "00b2a5d4",
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
            "const:432:8"
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
      "00b2a434",
      "READ",
      [
        "storage",
        "002a002c",
        null,
        "string"
      ]
    ],
    [
      "00b2a438",
      "READ",
      [
        "storage",
        "002a0032",
        null,
        "string"
      ]
    ],
    [
      "00b2a610",
      "PARAM",
      [
        "storage",
        "002a7432",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b2a434",
      "READ",
      [
        "storage",
        "002a00b7",
        null,
        "string"
      ]
    ],
    [
      "00b2a438",
      "READ",
      [
        "storage",
        "002a00bd",
        null,
        "string"
      ]
    ],
    [
      "00b2a610",
      "PARAM",
      [
        "storage",
        "002a74cc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2a5d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2a248.md#insn-00b2a5d4) · [`00b2a2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2a248.md#insn-00b2a2bc) · [`00b2a300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2a248.md#insn-00b2a300)
- 新版 [`00b2a618`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2a28c.md#insn-00b2a618) · [`00b2a300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2a28c.md#insn-00b2a300) · [`00b2a344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2a28c.md#insn-00b2a344)

~~~diff
- 00b2a5d4 ["INT_ADD", "register:40f0:8", ["const:b2a5d4:8", "const:4:8"]]
- 00b2a5d4 ["CALL", null, ["callee:00bde740:8"]]
+ 00b2a618 ["INT_ADD", "register:40f0:8", ["const:b2a618:8", "const:4:8"]]
+ 00b2a618 ["CALL", null, ["callee:00bde740:8"]]
- 00b2a5d4 bytes 47d00294
+ 00b2a618 bytes 4ad00294
- 00b2a2bc ["INT_ADD", "register:40f0:8", ["const:b2a2bc:8", "const:4:8"]]
- 00b2a2bc ["CALL", null, ["callee:00bdf150:8"]]
+ 00b2a300 ["INT_ADD", "register:40f0:8", ["const:b2a300:8", "const:4:8"]]
+ 00b2a300 ["CALL", null, ["callee:00bdf150:8"]]
- 00b2a2bc bytes 91d30294
+ 00b2a300 bytes 94d30294
- 00b2a300 ["INT_ADD", "register:40f0:8", ["const:b2a300:8", "const:4:8"]]
- 00b2a300 ["CALL", null, ["callee:00bdf2b0:8"]]
+ 00b2a344 ["INT_ADD", "register:40f0:8", ["const:b2a344:8", "const:4:8"]]
+ 00b2a344 ["CALL", null, ["callee:00bdf2b0:8"]]
- 00b2a300 bytes d8d30294
+ 00b2a344 bytes dbd30294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5840cb3822e76c82eae34b4875efaa44"></a>

### [`00b2a72c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2a72c.md) → [`00b2a770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2a770.md) _ZN11flatbuffers10Definition21DeserializeAttributesERNS_6ParserEPKNS_6VectorINS_6OffsetIN10reflection8KeyValueEEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf100.md) · 呼出先 8件 [`00613984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00613/00613984.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)
- 新版 呼出元 1件 [`00bdf150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf150.md) · 呼出先 8件 [`00613984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00613/00613984.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.59% / 新版 99.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2a818",
      "incomplete_value": false,
      "site": "00b2a81c",
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
            "const:4cc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2a7d4",
      "incomplete_value": false,
      "site": "00b2a7d8",
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
            "const:432:8"
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
      "00b2a818",
      "PARAM",
      [
        "storage",
        "002a7432",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b2a818",
      "PARAM",
      [
        "storage",
        "002a74cc",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2a7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2a72c.md#insn-00b2a7d8) · [`00b2a7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2a72c.md#insn-00b2a7b4) · [`00b2a7d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2a72c.md#insn-00b2a7d4)
- 新版 [`00b2a81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2a770.md#insn-00b2a81c) · [`00b2a7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2a770.md#insn-00b2a7f8) · [`00b2a818`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2a770.md#insn-00b2a818)

~~~diff
- 00b2a7d8 ["INT_ADD", "register:40f0:8", ["const:b2a7d8:8", "const:4:8"]]
- 00b2a7d8 ["CALL", null, ["callee:00bde740:8"]]
+ 00b2a81c ["INT_ADD", "register:40f0:8", ["const:b2a81c:8", "const:4:8"]]
+ 00b2a81c ["CALL", null, ["callee:00bde740:8"]]
- 00b2a7d8 bytes c6cf0294
+ 00b2a81c bytes c9cf0294
- 00b2a7b4 ["INT_ADD", "register:40f0:8", ["const:b2a7b4:8", "const:4:8"]]
- 00b2a7b4 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b2a7f8 ["INT_ADD", "register:40f0:8", ["const:b2a7f8:8", "const:4:8"]]
+ 00b2a7f8 ["CALL", null, ["callee:00bdb040:8"]]
- 00b2a7b4 bytes 0fc20294
+ 00b2a7f8 bytes 12c20294
- 00b2a7d4 ["COPY", "tmp:0:8", ["const:432:8"]]
- 00b2a7d4 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b2a7d4 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b2a7d4 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b2a818 ["COPY", "tmp:0:8", ["const:4cc:8"]]
+ 00b2a818 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b2a818 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b2a818 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b2a7d4 bytes 21c81091
+ 00b2a818 bytes 21301391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e7a9f9d63995fcbb6a4f3fe2927aa82"></a>

### [`00b2ab04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2ab04.md) → [`00b2ab48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2ab48.md) _ZN11flatbuffers8FieldDef11DeserializeERNS_6ParserEPKN10reflection5FieldE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdfa50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfa50.md) · 呼出先 13件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bde270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde270.md)
- 新版 呼出元 1件 [`00bdfaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfaa0.md) · 呼出先 13件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bde2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.13% / 新版 99.13%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2aefc",
      "incomplete_value": true,
      "site": "00b2aefc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:73f:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2aeb8",
      "incomplete_value": true,
      "site": "00b2aeb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7cc:8"
              ]
            ]
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
      "00b2aed0",
      "READ",
      [
        "storage",
        "002987cc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2aed0",
      "READ",
      [
        "storage",
        "0029873f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2ab88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2ab04.md#insn-00b2ab88) · [`00b2aba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2ab04.md#insn-00b2aba8) · [`00b2abd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2a/00b2ab04.md#insn-00b2abd8)
- 新版 [`00b2abcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2ab48.md#insn-00b2abcc) · [`00b2abec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2ab48.md#insn-00b2abec) · [`00b2ac1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2a/00b2ab48.md#insn-00b2ac1c)

~~~diff
- 00b2ab88 ["INT_ADD", "register:40f0:8", ["const:b2ab88:8", "const:4:8"]]
- 00b2ab88 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b2abcc ["INT_ADD", "register:40f0:8", ["const:b2abcc:8", "const:4:8"]]
+ 00b2abcc ["CALL", null, ["callee:00bdb040:8"]]
- 00b2ab88 bytes 1ac10294
+ 00b2abcc bytes 1dc10294
- 00b2aba8 ["INT_ADD", "register:40f0:8", ["const:b2aba8:8", "const:4:8"]]
- 00b2aba8 ["CALL", null, ["callee:00bdb1b0:8"]]
+ 00b2abec ["INT_ADD", "register:40f0:8", ["const:b2abec:8", "const:4:8"]]
+ 00b2abec ["CALL", null, ["callee:00bdb1b0:8"]]
- 00b2aba8 bytes 6ec10294
+ 00b2abec bytes 71c10294
- 00b2abd8 ["INT_ADD", "register:40f0:8", ["const:b2abd8:8", "const:4:8"]]
- 00b2abd8 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b2ac1c ["INT_ADD", "register:40f0:8", ["const:b2ac1c:8", "const:4:8"]]
+ 00b2ac1c ["CALL", null, ["callee:00bdb060:8"]]
- 00b2abd8 bytes 0ec10294
+ 00b2ac1c bytes 11c10294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb92f6e7deab52016a21813d64ed9118"></a>

### [`00b2b410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b410.md) → [`00b2b454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2b454.md) _ZN11flatbuffers13FloatToStringIdEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEET_i

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf250.md) · 呼出先 9件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb310.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb370.md)
- 新版 呼出元 1件 [`00bdf2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2a0.md) · 呼出先 9件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb360.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb3c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb3c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 94.63% / 新版 94.63%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2b4b8",
      "incomplete_value": true,
      "site": "00b2b4cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b2b474",
      "incomplete_value": true,
      "site": "00b2b488",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b2b4b0",
      "incomplete_value": true,
      "site": "00b2b4d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b2b46c",
      "incomplete_value": true,
      "site": "00b2b48c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b2b540",
      "incomplete_value": true,
      "site": "00b2b54c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b2b4fc",
      "incomplete_value": true,
      "site": "00b2b508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 28,
    "slot": 2
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b2b488",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "00b2b48c",
      "READ",
      [
        "storage",
        "00c1b9f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b2b4cc",
      "DATA",
      [
        "storage",
        "00c110f0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b2b488",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "00b2b48c",
      "READ",
      [
        "storage",
        "00c1ba48",
        null,
        "pointer"
      ]
    ],
    [
      "00b2b4cc",
      "DATA",
      [
        "storage",
        "00c11140",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2b444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b410.md#insn-00b2b444) · [`00b2b448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b410.md#insn-00b2b448) · [`00b2b494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2b/00b2b410.md#insn-00b2b494)
- 新版 [`00b2b488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2b454.md#insn-00b2b488) · [`00b2b48c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2b454.md#insn-00b2b48c) · [`00b2b4d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2b/00b2b454.md#insn-00b2b4d8)

~~~diff
- 00b2b444 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:dd8:8"]]
- 00b2b444 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b2b488 ["INT_ADD", "tmp:0:8", ["register:40d0:8", "const:e28:8"]]
+ 00b2b488 ["LOAD", "register:40d0:8", ["const:1b1:8", "tmp:0:8"]]
- 00b2b444 bytes 5aef46f9
+ 00b2b488 bytes 5a1747f9
- 00b2b448 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:9f8:8"]]
- 00b2b448 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b2b48c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a48:8"]]
+ 00b2b48c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b2b448 bytes 08fd44f9
+ 00b2b48c bytes 082545f9
- 00b2b494 ["INT_ADD", "register:40f0:8", ["const:b2b494:8", "const:4:8"]]
- 00b2b494 ["CALL", null, ["callee:00bdb390:8"]]
+ 00b2b4d8 ["INT_ADD", "register:40f0:8", ["const:b2b4d8:8", "const:4:8"]]
+ 00b2b4d8 ["CALL", null, ["callee:00bdb390:8"]]
- 00b2b494 bytes abbf0294
+ 00b2b4d8 bytes aebf0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1536e156283f4c626c048f802bb56e57"></a>

### [`00b2c7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c7c4.md) → [`00b2c808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c808.md) _ZN11flatbuffers6Parser11DeserializeEPKhm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 5件 [`00b2c8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c8b8.md) [`00b2c95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c95c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdf730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf730.md) [`00be01e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01e0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00b2c8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c8fc.md) [`00b2c9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c9a0.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdf780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf780.md) [`00be0230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0230.md)

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
      "definition_site": "00b2c84c",
      "incomplete_value": false,
      "site": "00b2c864",
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
            "const:44c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2c808",
      "incomplete_value": false,
      "site": "00b2c820",
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
            "const:4d9:8"
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
      "definition_site": "00b2c874",
      "incomplete_value": false,
      "site": "00b2c87c",
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
            "const:44c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2c830",
      "incomplete_value": false,
      "site": "00b2c838",
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
            "const:4d9:8"
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
      "00b2c84c",
      "PARAM",
      [
        "storage",
        "002954d9",
        null,
        null
      ]
    ],
    [
      "00b2c874",
      "PARAM",
      [
        "storage",
        "002954d9",
        null,
        null
      ]
    ],
    [
      "00b2c888",
      "READ",
      [
        "storage",
        "00c1b9c8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b2c84c",
      "PARAM",
      [
        "storage",
        "0029544c",
        null,
        null
      ]
    ],
    [
      "00b2c874",
      "PARAM",
      [
        "storage",
        "0029544c",
        null,
        null
      ]
    ],
    [
      "00b2c888",
      "READ",
      [
        "storage",
        "00c1ba18",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2c820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c7c4.md#insn-00b2c820) · [`00b2c838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c7c4.md#insn-00b2c838) · [`00b2c87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c7c4.md#insn-00b2c87c)
- 新版 [`00b2c864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c808.md#insn-00b2c864) · [`00b2c87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c808.md#insn-00b2c87c) · [`00b2c8c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c808.md#insn-00b2c8c0)

~~~diff
- 00b2c820 ["INT_ADD", "register:40f0:8", ["const:b2c820:8", "const:4:8"]]
- 00b2c820 ["CALL", null, ["callee:00be0230:8"]]
+ 00b2c864 ["INT_ADD", "register:40f0:8", ["const:b2c864:8", "const:4:8"]]
+ 00b2c864 ["CALL", null, ["callee:00be0230:8"]]
- 00b2c820 bytes 70ce0294
+ 00b2c864 bytes 73ce0294
- 00b2c838 ["INT_ADD", "register:40f0:8", ["const:b2c838:8", "const:4:8"]]
- 00b2c838 ["CALL", null, ["callee:00be0230:8"]]
+ 00b2c87c ["INT_ADD", "register:40f0:8", ["const:b2c87c:8", "const:4:8"]]
+ 00b2c87c ["CALL", null, ["callee:00be0230:8"]]
- 00b2c838 bytes 6ace0294
+ 00b2c87c bytes 6dce0294
- 00b2c87c ["INT_ADD", "register:40f0:8", ["const:b2c87c:8", "const:4:8"]]
- 00b2c87c ["CALL", null, ["callee:00bdf780:8"]]
+ 00b2c8c0 ["INT_ADD", "register:40f0:8", ["const:b2c8c0:8", "const:4:8"]]
+ 00b2c8c0 ["CALL", null, ["callee:00bdf780:8"]]
- 00b2c87c bytes adcb0294
+ 00b2c8c0 bytes b0cb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51b2c732e35aa17e887f93640478c5e5"></a>

### [`00b2c8b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c8b8.md) → [`00b2c8fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c8fc.md) _ZN10reflection30VerifySizePrefixedSchemaBufferERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2c7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c7c4.md) · 呼出先 2件 [`00bdfb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb60.md) [`00be01e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01e0.md)
- 新版 呼出元 1件 [`00b2c808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c808.md) · 呼出先 2件 [`00bdfbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfbb0.md) [`00be0230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0230.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.56% / 新版 97.56%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2c940",
      "incomplete_value": false,
      "site": "00b2c948",
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
            "const:44c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2c8fc",
      "incomplete_value": false,
      "site": "00b2c904",
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
            "const:4d9:8"
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
      "00b2c940",
      "PARAM",
      [
        "storage",
        "002954d9",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b2c940",
      "PARAM",
      [
        "storage",
        "0029544c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2c904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c8b8.md#insn-00b2c904) · [`00b2c8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c8b8.md#insn-00b2c8fc)
- 新版 [`00b2c948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c8fc.md#insn-00b2c948) · [`00b2c940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c8fc.md#insn-00b2c940)

~~~diff
- 00b2c904 ["INT_ADD", "register:40f0:8", ["const:b2c904:8", "const:4:8"]]
- 00b2c904 ["CALL", null, ["callee:00be0230:8"]]
+ 00b2c948 ["INT_ADD", "register:40f0:8", ["const:b2c948:8", "const:4:8"]]
+ 00b2c948 ["CALL", null, ["callee:00be0230:8"]]
- 00b2c904 bytes 37ce0294
+ 00b2c948 bytes 3ace0294
- 00b2c8fc ["COPY", "tmp:0:8", ["const:4d9:8"]]
- 00b2c8fc ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b2c8fc ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b2c8fc ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b2c940 ["COPY", "tmp:0:8", ["const:44c:8"]]
+ 00b2c940 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b2c940 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b2c940 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b2c8fc bytes 21641391
+ 00b2c940 bytes 21301191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-290aab0cba14802d1748abf5882606ff"></a>

### [`00b2c95c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c95c.md) → [`00b2c9a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c9a0.md) _ZN10reflection18VerifySchemaBufferERN11flatbuffers8VerifierE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b2c7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c7c4.md) · 呼出先 2件 [`00bdfb60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfb60.md) [`00be01e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be01e0.md)
- 新版 呼出元 1件 [`00b2c808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c808.md) · 呼出先 2件 [`00bdfbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdfbb0.md) [`00be0230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0230.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.88% / 新版 96.88%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2c9c8",
      "incomplete_value": false,
      "site": "00b2c9d4",
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
            "const:44c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2c984",
      "incomplete_value": false,
      "site": "00b2c990",
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
            "const:4d9:8"
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
      "00b2c9c8",
      "PARAM",
      [
        "storage",
        "002954d9",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b2c9c8",
      "PARAM",
      [
        "storage",
        "0029544c",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2c990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c95c.md#insn-00b2c990) · [`00b2c984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2c/00b2c95c.md#insn-00b2c984)
- 新版 [`00b2c9d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c9a0.md#insn-00b2c9d4) · [`00b2c9c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2c/00b2c9a0.md#insn-00b2c9c8)

~~~diff
- 00b2c990 ["INT_ADD", "register:40f0:8", ["const:b2c990:8", "const:4:8"]]
- 00b2c990 ["CALL", null, ["callee:00be0230:8"]]
+ 00b2c9d4 ["INT_ADD", "register:40f0:8", ["const:b2c9d4:8", "const:4:8"]]
+ 00b2c9d4 ["CALL", null, ["callee:00be0230:8"]]
- 00b2c990 bytes 14ce0294
+ 00b2c9d4 bytes 17ce0294
- 00b2c984 ["COPY", "tmp:0:8", ["const:4d9:8"]]
- 00b2c984 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00b2c984 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00b2c984 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00b2c9c8 ["COPY", "tmp:0:8", ["const:44c:8"]]
+ 00b2c9c8 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00b2c9c8 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00b2c9c8 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00b2c984 bytes 21641391
+ 00b2c9c8 bytes 21301191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd63afbcbae8617b789e1b23bcfbe037"></a>

### [`00b2dc2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2d/00b2dc2c.md) → [`00b2dc70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2d/00b2dc70.md) _ZN11flatbuffers6Parser9ConformToERKS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 11件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bde6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6f0.md)
- 新版 呼出元 0件  · 呼出先 11件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb200.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bde740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde740.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.51% / 新版 97.51%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2dff4",
      "incomplete_value": false,
      "site": "00b2dff8",
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
      "definition_site": "00b2dfb0",
      "incomplete_value": false,
      "site": "00b2dfb4",
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
      "00b2de70",
      "PARAM",
      [
        "storage",
        "0029eff3",
        null,
        "string"
      ]
    ],
    [
      "00b2de90",
      "PARAM",
      [
        "storage",
        "002965b4",
        null,
        "string"
      ]
    ],
    [
      "00b2dec0",
      "PARAM",
      [
        "storage",
        "002933ed",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2de70",
      "PARAM",
      [
        "storage",
        "0029f07e",
        null,
        "string"
      ]
    ],
    [
      "00b2de90",
      "PARAM",
      [
        "storage",
        "00296527",
        null,
        "string"
      ]
    ],
    [
      "00b2dec0",
      "PARAM",
      [
        "storage",
        "00293360",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2dfb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2d/00b2dc2c.md#insn-00b2dfb4) · [`00b2dc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2d/00b2dc2c.md#insn-00b2dc94) · [`00b2dca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2d/00b2dc2c.md#insn-00b2dca0)
- 新版 [`00b2dff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2d/00b2dc70.md#insn-00b2dff8) · [`00b2dcd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2d/00b2dc70.md#insn-00b2dcd8) · [`00b2dce4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2d/00b2dc70.md#insn-00b2dce4)

~~~diff
- 00b2dfb4 ["INT_ADD", "register:40f0:8", ["const:b2dfb4:8", "const:4:8"]]
- 00b2dfb4 ["CALL", null, ["callee:00bde740:8"]]
+ 00b2dff8 ["INT_ADD", "register:40f0:8", ["const:b2dff8:8", "const:4:8"]]
+ 00b2dff8 ["CALL", null, ["callee:00bde740:8"]]
- 00b2dfb4 bytes cfc10294
+ 00b2dff8 bytes d2c10294
- 00b2dc94 ["INT_ADD", "register:40f0:8", ["const:b2dc94:8", "const:4:8"]]
- 00b2dc94 ["CALL", null, ["callee:00bdfc70:8"]]
+ 00b2dcd8 ["INT_ADD", "register:40f0:8", ["const:b2dcd8:8", "const:4:8"]]
+ 00b2dcd8 ["CALL", null, ["callee:00bdfc70:8"]]
- 00b2dc94 bytes e3c70294
+ 00b2dcd8 bytes e6c70294
- 00b2dca0 ["INT_ADD", "register:40f0:8", ["const:b2dca0:8", "const:4:8"]]
- 00b2dca0 ["CALL", null, ["callee:00bdfcd0:8"]]
+ 00b2dce4 ["INT_ADD", "register:40f0:8", ["const:b2dce4:8", "const:4:8"]]
+ 00b2dce4 ["CALL", null, ["callee:00bdfcd0:8"]]
- 00b2dca0 bytes f8c70294
+ 00b2dce4 bytes fbc70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e94e4eea6a3d1c97e8467334adc5637a"></a>

### [`00b2ef70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ef70.md) → [`00b2efb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2efb4.md) _ZN11flatbuffers14EnumValBuilder13ValidateValueEPlb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf310.md) · 呼出先 15件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdf270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf270.md)
- 新版 呼出元 1件 [`00bdf360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf360.md) · 呼出先 15件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdf2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2c0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.09% / 新版 97.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b2f088",
      "incomplete_value": true,
      "site": "00b2f0a0",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:177:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2f044",
      "incomplete_value": true,
      "site": "00b2f05c",
      "value": [
        "LOAD",
        "16",
        [
          [
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
                "const:ec:8"
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
      "definition_site": "00b2f088",
      "incomplete_value": true,
      "site": "00b2f0a0",
      "value": [
        "LOAD",
        "16",
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
      "definition_site": "00b2f044",
      "incomplete_value": true,
      "site": "00b2f05c",
      "value": [
        "LOAD",
        "16",
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
      "00b2eff8",
      "DATA",
      [
        "storage",
        "002f8524",
        "switchD_00b2efbc::switchdataD_002f8524",
        "byte"
      ]
    ],
    [
      "00b2f088",
      "READ",
      [
        "storage",
        "002a00ec",
        null,
        "string"
      ]
    ],
    [
      "00b2f088",
      "READ",
      [
        "storage",
        "002a00fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2eff8",
      "DATA",
      [
        "storage",
        "002f8524",
        "switchD_00b2f000::switchdataD_002f8524",
        "byte"
      ]
    ],
    [
      "00b2f088",
      "READ",
      [
        "storage",
        "002a0177",
        null,
        "string"
      ]
    ],
    [
      "00b2f088",
      "READ",
      [
        "storage",
        "002a0187",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2f018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ef70.md#insn-00b2f018) · [`00b2efb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ef70.md#insn-00b2efb0) · [`00b2efc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2ef70.md#insn-00b2efc8)
- 新版 [`00b2f05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2efb4.md#insn-00b2f05c) · [`00b2eff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2efb4.md#insn-00b2eff4) · [`00b2f00c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2e/00b2efb4.md#insn-00b2f00c)

~~~diff
- 00b2f018 ["INT_ADD", "register:40f0:8", ["const:b2f018:8", "const:4:8"]]
- 00b2f018 ["CALL", null, ["callee:00bdf300:8"]]
+ 00b2f05c ["INT_ADD", "register:40f0:8", ["const:b2f05c:8", "const:4:8"]]
+ 00b2f05c ["CALL", null, ["callee:00bdf300:8"]]
- 00b2f018 bytes a6c00294
+ 00b2f05c bytes a9c00294
- 00b2efb0 ["COPY", "register:4050:8", ["const:b2efc0:8"]]
+ 00b2eff4 ["COPY", "register:4050:8", ["const:b2f004:8"]]
- 00b2efb0 bytes 8a000010
+ 00b2eff4 bytes 8a000010
- 00b2efc8 ["INT_ADD", "register:40f0:8", ["const:b2efc8:8", "const:4:8"]]
- 00b2efc8 ["CALL", null, ["callee:00bdf2d0:8"]]
+ 00b2f00c ["INT_ADD", "register:40f0:8", ["const:b2f00c:8", "const:4:8"]]
+ 00b2f00c ["CALL", null, ["callee:00bdf2d0:8"]]
- 00b2efc8 bytes aec00294
+ 00b2f00c bytes b1c00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29b3a15ddd7f7eba3bf49e7929ca401f"></a>

### [`00b2f10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f10c.md) → [`00b2f150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f150.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE1EhEENS_12CheckedErrorEPli

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf280.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)
- 新版 呼出元 1件 [`00bdf2d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2d0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.16% / 新版 97.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2f1a8",
      "incomplete_value": false,
      "site": "00b2f1b8",
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
            "const:527:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2f164",
      "incomplete_value": false,
      "site": "00b2f174",
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
            "const:5bb:8"
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
      "definition_site": "00b2f208",
      "incomplete_value": false,
      "site": "00b2f224",
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
            "const:f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2f1c4",
      "incomplete_value": false,
      "site": "00b2f1e0",
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
            "const:66:8"
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
      "00b2f1a8",
      "PARAM",
      [
        "storage",
        "002af5bb",
        null,
        "string"
      ]
    ],
    [
      "00b2f1dc",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b2f208",
      "PARAM",
      [
        "storage",
        "002a5066",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2f1a8",
      "PARAM",
      [
        "storage",
        "002af527",
        null,
        "string"
      ]
    ],
    [
      "00b2f1dc",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b2f208",
      "PARAM",
      [
        "storage",
        "002a50f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2f174`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f10c.md#insn-00b2f174) · [`00b2f1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f10c.md#insn-00b2f1e0) · [`00b2f15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f10c.md#insn-00b2f15c)
- 新版 [`00b2f1b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f150.md#insn-00b2f1b8) · [`00b2f224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f150.md#insn-00b2f224) · [`00b2f1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f150.md#insn-00b2f1a0)

~~~diff
- 00b2f174 ["INT_ADD", "register:40f0:8", ["const:b2f174:8", "const:4:8"]]
- 00b2f174 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b2f1b8 ["INT_ADD", "register:40f0:8", ["const:b2f1b8:8", "const:4:8"]]
+ 00b2f1b8 ["CALL", null, ["callee:00bdc180:8"]]
- 00b2f174 bytes efb30294
+ 00b2f1b8 bytes f2b30294
- 00b2f1e0 ["INT_ADD", "register:40f0:8", ["const:b2f1e0:8", "const:4:8"]]
- 00b2f1e0 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b2f224 ["INT_ADD", "register:40f0:8", ["const:b2f224:8", "const:4:8"]]
+ 00b2f224 ["CALL", null, ["callee:00bdb130:8"]]
- 00b2f1e0 bytes c0af0294
+ 00b2f224 bytes c3af0294
- 00b2f15c ["INT_ADD", "register:40f0:8", ["const:b2f15c:8", "const:4:8"]]
- 00b2f15c ["CALL", null, ["callee:00bdf1c0:8"]]
+ 00b2f1a0 ["INT_ADD", "register:40f0:8", ["const:b2f1a0:8", "const:4:8"]]
+ 00b2f1a0 ["CALL", null, ["callee:00bdf1c0:8"]]
- 00b2f15c bytes 05c00294
+ 00b2f1a0 bytes 08c00294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7b9025dbd873ada7f6df640d1e015dc"></a>

### [`00b2f340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f340.md) → [`00b2f384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f384.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE2EhEENS_12CheckedErrorEPli

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf290.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)
- 新版 呼出元 1件 [`00bdf2e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2e0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.16% / 新版 97.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2f43c",
      "incomplete_value": false,
      "site": "00b2f458",
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
            "const:f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2f3f8",
      "incomplete_value": false,
      "site": "00b2f414",
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
            "const:66:8"
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
      "00b2f3dc",
      "PARAM",
      [
        "storage",
        "002af5bb",
        null,
        "string"
      ]
    ],
    [
      "00b2f410",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b2f43c",
      "PARAM",
      [
        "storage",
        "002a5066",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2f3dc",
      "PARAM",
      [
        "storage",
        "002af527",
        null,
        "string"
      ]
    ],
    [
      "00b2f410",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b2f43c",
      "PARAM",
      [
        "storage",
        "002a50f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2f414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f340.md#insn-00b2f414) · [`00b2f390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f340.md#insn-00b2f390) · [`00b2f398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f340.md#insn-00b2f398)
- 新版 [`00b2f458`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f384.md#insn-00b2f458) · [`00b2f3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f384.md#insn-00b2f3d4) · [`00b2f3dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f384.md#insn-00b2f3dc)

~~~diff
- 00b2f414 ["INT_ADD", "register:40f0:8", ["const:b2f414:8", "const:4:8"]]
- 00b2f414 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b2f458 ["INT_ADD", "register:40f0:8", ["const:b2f458:8", "const:4:8"]]
+ 00b2f458 ["CALL", null, ["callee:00bdb130:8"]]
- 00b2f414 bytes 33af0294
+ 00b2f458 bytes 36af0294
- 00b2f390 ["INT_ADD", "register:40f0:8", ["const:b2f390:8", "const:4:8"]]
- 00b2f390 ["CALL", null, ["callee:00bdf1c0:8"]]
+ 00b2f3d4 ["INT_ADD", "register:40f0:8", ["const:b2f3d4:8", "const:4:8"]]
+ 00b2f3d4 ["CALL", null, ["callee:00bdf1c0:8"]]
- 00b2f390 bytes 78bf0294
+ 00b2f3d4 bytes 7bbf0294
- 00b2f398 ["COPY", "tmp:0:8", ["const:5bb:8"]]
- 00b2f398 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b2f398 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b2f398 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b2f3dc ["COPY", "tmp:0:8", ["const:527:8"]]
+ 00b2f3dc ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b2f3dc ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b2f3dc ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b2f398 bytes 42ec1691
+ 00b2f3dc bytes 429c1491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6b575211ff2128088436e816722d428"></a>

### [`00b2f574`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f574.md) → [`00b2f5b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f5b8.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE3EaEENS_12CheckedErrorEPli

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf2a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf2a0.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)
- 新版 呼出元 1件 [`00bdf2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2f0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.18% / 新版 97.18%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2f614",
      "incomplete_value": false,
      "site": "00b2f624",
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
            "const:527:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2f5d0",
      "incomplete_value": false,
      "site": "00b2f5e0",
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
            "const:5bb:8"
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
      "definition_site": "00b2f674",
      "incomplete_value": false,
      "site": "00b2f690",
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
            "const:f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2f630",
      "incomplete_value": false,
      "site": "00b2f64c",
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
            "const:66:8"
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
      "00b2f614",
      "PARAM",
      [
        "storage",
        "002af5bb",
        null,
        "string"
      ]
    ],
    [
      "00b2f648",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b2f674",
      "PARAM",
      [
        "storage",
        "002a5066",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2f614",
      "PARAM",
      [
        "storage",
        "002af527",
        null,
        "string"
      ]
    ],
    [
      "00b2f648",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b2f674",
      "PARAM",
      [
        "storage",
        "002a50f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2f5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f574.md#insn-00b2f5e0) · [`00b2f64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f574.md#insn-00b2f64c) · [`00b2f5c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f574.md#insn-00b2f5c8)
- 新版 [`00b2f624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f5b8.md#insn-00b2f624) · [`00b2f690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f5b8.md#insn-00b2f690) · [`00b2f60c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f5b8.md#insn-00b2f60c)

~~~diff
- 00b2f5e0 ["INT_ADD", "register:40f0:8", ["const:b2f5e0:8", "const:4:8"]]
- 00b2f5e0 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b2f624 ["INT_ADD", "register:40f0:8", ["const:b2f624:8", "const:4:8"]]
+ 00b2f624 ["CALL", null, ["callee:00bdc180:8"]]
- 00b2f5e0 bytes d4b20294
+ 00b2f624 bytes d7b20294
- 00b2f64c ["INT_ADD", "register:40f0:8", ["const:b2f64c:8", "const:4:8"]]
- 00b2f64c ["CALL", null, ["callee:00bdb130:8"]]
+ 00b2f690 ["INT_ADD", "register:40f0:8", ["const:b2f690:8", "const:4:8"]]
+ 00b2f690 ["CALL", null, ["callee:00bdb130:8"]]
- 00b2f64c bytes a5ae0294
+ 00b2f690 bytes a8ae0294
- 00b2f5c8 ["INT_ADD", "register:40f0:8", ["const:b2f5c8:8", "const:4:8"]]
- 00b2f5c8 ["CALL", null, ["callee:00bdf1c0:8"]]
+ 00b2f60c ["INT_ADD", "register:40f0:8", ["const:b2f60c:8", "const:4:8"]]
+ 00b2f60c ["CALL", null, ["callee:00bdf1c0:8"]]
- 00b2f5c8 bytes eabe0294
+ 00b2f60c bytes edbe0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b0ef15b9f10b40898299b1604bff09c"></a>

### [`00b2f7ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f7ac.md) → [`00b2f7f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f7f0.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE4EhEENS_12CheckedErrorEPli

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf2b0.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)
- 新版 呼出元 1件 [`00bdf300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf300.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.16% / 新版 97.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2f848",
      "incomplete_value": false,
      "site": "00b2f858",
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
            "const:527:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2f804",
      "incomplete_value": false,
      "site": "00b2f814",
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
            "const:5bb:8"
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
      "definition_site": "00b2f8a8",
      "incomplete_value": false,
      "site": "00b2f8c4",
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
            "const:f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2f864",
      "incomplete_value": false,
      "site": "00b2f880",
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
            "const:66:8"
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
      "00b2f848",
      "PARAM",
      [
        "storage",
        "002af5bb",
        null,
        "string"
      ]
    ],
    [
      "00b2f87c",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b2f8a8",
      "PARAM",
      [
        "storage",
        "002a5066",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2f848",
      "PARAM",
      [
        "storage",
        "002af527",
        null,
        "string"
      ]
    ],
    [
      "00b2f87c",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b2f8a8",
      "PARAM",
      [
        "storage",
        "002a50f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2f814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f7ac.md#insn-00b2f814) · [`00b2f880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f7ac.md#insn-00b2f880) · [`00b2f7fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2f7ac.md#insn-00b2f7fc)
- 新版 [`00b2f858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f7f0.md#insn-00b2f858) · [`00b2f8c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f7f0.md#insn-00b2f8c4) · [`00b2f840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2f7f0.md#insn-00b2f840)

~~~diff
- 00b2f814 ["INT_ADD", "register:40f0:8", ["const:b2f814:8", "const:4:8"]]
- 00b2f814 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b2f858 ["INT_ADD", "register:40f0:8", ["const:b2f858:8", "const:4:8"]]
+ 00b2f858 ["CALL", null, ["callee:00bdc180:8"]]
- 00b2f814 bytes 47b20294
+ 00b2f858 bytes 4ab20294
- 00b2f880 ["INT_ADD", "register:40f0:8", ["const:b2f880:8", "const:4:8"]]
- 00b2f880 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b2f8c4 ["INT_ADD", "register:40f0:8", ["const:b2f8c4:8", "const:4:8"]]
+ 00b2f8c4 ["CALL", null, ["callee:00bdb130:8"]]
- 00b2f880 bytes 18ae0294
+ 00b2f8c4 bytes 1bae0294
- 00b2f7fc ["INT_ADD", "register:40f0:8", ["const:b2f7fc:8", "const:4:8"]]
- 00b2f7fc ["CALL", null, ["callee:00bdf1c0:8"]]
+ 00b2f840 ["INT_ADD", "register:40f0:8", ["const:b2f840:8", "const:4:8"]]
+ 00b2f840 ["CALL", null, ["callee:00bdf1c0:8"]]
- 00b2f7fc bytes 5dbe0294
+ 00b2f840 bytes 60be0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51b45a3bde45b25853501643114c9592"></a>

### [`00b2fc18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2fc18.md) → [`00b2fc5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2fc5c.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE6EtEENS_12CheckedErrorEPli

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf2d0.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)
- 新版 呼出元 1件 [`00bdf320`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf320.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.16% / 新版 97.16%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2fcb4",
      "incomplete_value": false,
      "site": "00b2fcc4",
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
            "const:527:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2fc70",
      "incomplete_value": false,
      "site": "00b2fc80",
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
            "const:5bb:8"
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
      "definition_site": "00b2fd14",
      "incomplete_value": false,
      "site": "00b2fd30",
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
            "const:f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2fcd0",
      "incomplete_value": false,
      "site": "00b2fcec",
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
            "const:66:8"
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
      "00b2fcb4",
      "PARAM",
      [
        "storage",
        "002af5bb",
        null,
        "string"
      ]
    ],
    [
      "00b2fce8",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b2fd14",
      "PARAM",
      [
        "storage",
        "002a5066",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2fcb4",
      "PARAM",
      [
        "storage",
        "002af527",
        null,
        "string"
      ]
    ],
    [
      "00b2fce8",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b2fd14",
      "PARAM",
      [
        "storage",
        "002a50f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2fc80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2fc18.md#insn-00b2fc80) · [`00b2fcec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2fc18.md#insn-00b2fcec) · [`00b2fc68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2fc18.md#insn-00b2fc68)
- 新版 [`00b2fcc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2fc5c.md#insn-00b2fcc4) · [`00b2fd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2fc5c.md#insn-00b2fd30) · [`00b2fcac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2fc5c.md#insn-00b2fcac)

~~~diff
- 00b2fc80 ["INT_ADD", "register:40f0:8", ["const:b2fc80:8", "const:4:8"]]
- 00b2fc80 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b2fcc4 ["INT_ADD", "register:40f0:8", ["const:b2fcc4:8", "const:4:8"]]
+ 00b2fcc4 ["CALL", null, ["callee:00bdc180:8"]]
- 00b2fc80 bytes 2cb10294
+ 00b2fcc4 bytes 2fb10294
- 00b2fcec ["INT_ADD", "register:40f0:8", ["const:b2fcec:8", "const:4:8"]]
- 00b2fcec ["CALL", null, ["callee:00bdb130:8"]]
+ 00b2fd30 ["INT_ADD", "register:40f0:8", ["const:b2fd30:8", "const:4:8"]]
+ 00b2fd30 ["CALL", null, ["callee:00bdb130:8"]]
- 00b2fcec bytes fdac0294
+ 00b2fd30 bytes 00ad0294
- 00b2fc68 ["INT_ADD", "register:40f0:8", ["const:b2fc68:8", "const:4:8"]]
- 00b2fc68 ["CALL", null, ["callee:00bdf1c0:8"]]
+ 00b2fcac ["INT_ADD", "register:40f0:8", ["const:b2fcac:8", "const:4:8"]]
+ 00b2fcac ["CALL", null, ["callee:00bdf1c0:8"]]
- 00b2fc68 bytes 42bd0294
+ 00b2fcac bytes 45bd0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c77a8e4ee8b2310f63937b42a6a4cbd"></a>

### [`00b2fe4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2fe4c.md) → [`00b2fe90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2fe90.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE7EiEENS_12CheckedErrorEPli

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf2e0.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)
- 新版 呼出元 1件 [`00bdf330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf330.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.20% / 新版 97.20%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b2fef0",
      "incomplete_value": false,
      "site": "00b2ff00",
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
            "const:527:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b2feac",
      "incomplete_value": false,
      "site": "00b2febc",
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
            "const:5bb:8"
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
      "00b2fef0",
      "PARAM",
      [
        "storage",
        "002af5bb",
        null,
        "string"
      ]
    ],
    [
      "00b2ff24",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b2ff50",
      "PARAM",
      [
        "storage",
        "002a5066",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b2fef0",
      "PARAM",
      [
        "storage",
        "002af527",
        null,
        "string"
      ]
    ],
    [
      "00b2ff24",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b2ff50",
      "PARAM",
      [
        "storage",
        "002a50f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b2febc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2fe4c.md#insn-00b2febc) · [`00b2fea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2fe4c.md#insn-00b2fea4) · [`00b2feac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2f/00b2fe4c.md#insn-00b2feac)
- 新版 [`00b2ff00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2fe90.md#insn-00b2ff00) · [`00b2fee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2fe90.md#insn-00b2fee8) · [`00b2fef0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b2f/00b2fe90.md#insn-00b2fef0)

~~~diff
- 00b2febc ["INT_ADD", "register:40f0:8", ["const:b2febc:8", "const:4:8"]]
- 00b2febc ["CALL", null, ["callee:00bdc180:8"]]
+ 00b2ff00 ["INT_ADD", "register:40f0:8", ["const:b2ff00:8", "const:4:8"]]
+ 00b2ff00 ["CALL", null, ["callee:00bdc180:8"]]
- 00b2febc bytes 9db00294
+ 00b2ff00 bytes a0b00294
- 00b2fea4 ["INT_ADD", "register:40f0:8", ["const:b2fea4:8", "const:4:8"]]
- 00b2fea4 ["CALL", null, ["callee:00bdf1c0:8"]]
+ 00b2fee8 ["INT_ADD", "register:40f0:8", ["const:b2fee8:8", "const:4:8"]]
+ 00b2fee8 ["CALL", null, ["callee:00bdf1c0:8"]]
- 00b2fea4 bytes b3bc0294
+ 00b2fee8 bytes b6bc0294
- 00b2feac ["COPY", "tmp:0:8", ["const:5bb:8"]]
- 00b2feac ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b2feac ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b2feac ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b2fef0 ["COPY", "tmp:0:8", ["const:527:8"]]
+ 00b2fef0 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b2fef0 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b2fef0 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b2feac bytes 42ec1691
+ 00b2fef0 bytes 429c1491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ed300a8e8a09d7694894060f113e29e"></a>

### [`00b302bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b302bc.md) → [`00b30300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30300.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE9ElEENS_12CheckedErrorEPli

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf300.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)
- 新版 呼出元 1件 [`00bdf350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf350.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)

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
      "definition_site": "00b30354",
      "incomplete_value": false,
      "site": "00b30364",
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
            "const:527:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b30310",
      "incomplete_value": false,
      "site": "00b30320",
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
            "const:5bb:8"
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
      "00b30354",
      "PARAM",
      [
        "storage",
        "002af5bb",
        null,
        "string"
      ]
    ],
    [
      "00b30388",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b303b4",
      "PARAM",
      [
        "storage",
        "002a5066",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b30354",
      "PARAM",
      [
        "storage",
        "002af527",
        null,
        "string"
      ]
    ],
    [
      "00b30388",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b303b4",
      "PARAM",
      [
        "storage",
        "002a50f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b30320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b302bc.md#insn-00b30320) · [`00b30308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b302bc.md#insn-00b30308) · [`00b30310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b302bc.md#insn-00b30310)
- 新版 [`00b30364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30300.md#insn-00b30364) · [`00b3034c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30300.md#insn-00b3034c) · [`00b30354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30300.md#insn-00b30354)

~~~diff
- 00b30320 ["INT_ADD", "register:40f0:8", ["const:b30320:8", "const:4:8"]]
- 00b30320 ["CALL", null, ["callee:00bdc180:8"]]
+ 00b30364 ["INT_ADD", "register:40f0:8", ["const:b30364:8", "const:4:8"]]
+ 00b30364 ["CALL", null, ["callee:00bdc180:8"]]
- 00b30320 bytes 84af0294
+ 00b30364 bytes 87af0294
- 00b30308 ["INT_ADD", "register:40f0:8", ["const:b30308:8", "const:4:8"]]
- 00b30308 ["CALL", null, ["callee:00bdf1c0:8"]]
+ 00b3034c ["INT_ADD", "register:40f0:8", ["const:b3034c:8", "const:4:8"]]
+ 00b3034c ["CALL", null, ["callee:00bdf1c0:8"]]
- 00b30308 bytes 9abb0294
+ 00b3034c bytes 9dbb0294
- 00b30310 ["COPY", "tmp:0:8", ["const:5bb:8"]]
- 00b30310 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
- 00b30310 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
- 00b30310 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
+ 00b30354 ["COPY", "tmp:0:8", ["const:527:8"]]
+ 00b30354 ["INT_CARRY", "register:105:1", ["register:4010:8", "tmp:0:8"]]
+ 00b30354 ["INT_SCARRY", "register:106:1", ["register:4010:8", "tmp:0:8"]]
+ 00b30354 ["INT_ADD", "tmp:1:8", ["register:4010:8", "tmp:0:8"]]
- 00b30310 bytes 42ec1691
+ 00b30354 bytes 429c1491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-203f953150ead6e74589c99b211125dd"></a>

### [`00b304ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b304ec.md) → [`00b30530`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30530.md) _ZN11flatbuffers14EnumValBuilder12ValidateImplILNS_8BaseTypeE10EmEENS_12CheckedErrorEPli

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf270`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf270.md) · 呼出先 8件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb210.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md)
- 新版 呼出元 1件 [`00bdf2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf2c0.md) · 呼出先 8件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdb260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb260.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b30580",
      "incomplete_value": false,
      "site": "00b30590",
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
            "const:527:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b3053c",
      "incomplete_value": false,
      "site": "00b3054c",
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
            "const:5bb:8"
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
      "definition_site": "00b305e0",
      "incomplete_value": false,
      "site": "00b305fc",
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
            "const:f1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b3059c",
      "incomplete_value": false,
      "site": "00b305b8",
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
            "const:66:8"
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
      "00b30580",
      "PARAM",
      [
        "storage",
        "002af5bb",
        null,
        "string"
      ]
    ],
    [
      "00b305b4",
      "PARAM",
      [
        "storage",
        "002a5394",
        null,
        null
      ]
    ],
    [
      "00b305e0",
      "PARAM",
      [
        "storage",
        "002a5066",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b30580",
      "PARAM",
      [
        "storage",
        "002af527",
        null,
        "string"
      ]
    ],
    [
      "00b305b4",
      "PARAM",
      [
        "storage",
        "002a541f",
        null,
        null
      ]
    ],
    [
      "00b305e0",
      "PARAM",
      [
        "storage",
        "002a50f1",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3054c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b304ec.md#insn-00b3054c) · [`00b305b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b304ec.md#insn-00b305b8) · [`00b30534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b304ec.md#insn-00b30534)
- 新版 [`00b30590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30530.md#insn-00b30590) · [`00b305fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30530.md#insn-00b305fc) · [`00b30578`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30530.md#insn-00b30578)

~~~diff
- 00b3054c ["INT_ADD", "register:40f0:8", ["const:b3054c:8", "const:4:8"]]
- 00b3054c ["CALL", null, ["callee:00bdc180:8"]]
+ 00b30590 ["INT_ADD", "register:40f0:8", ["const:b30590:8", "const:4:8"]]
+ 00b30590 ["CALL", null, ["callee:00bdc180:8"]]
- 00b3054c bytes f9ae0294
+ 00b30590 bytes fcae0294
- 00b305b8 ["INT_ADD", "register:40f0:8", ["const:b305b8:8", "const:4:8"]]
- 00b305b8 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b305fc ["INT_ADD", "register:40f0:8", ["const:b305fc:8", "const:4:8"]]
+ 00b305fc ["CALL", null, ["callee:00bdb130:8"]]
- 00b305b8 bytes caaa0294
+ 00b305fc bytes cdaa0294
- 00b30534 ["INT_ADD", "register:40f0:8", ["const:b30534:8", "const:4:8"]]
- 00b30534 ["CALL", null, ["callee:00bdf1d0:8"]]
+ 00b30578 ["INT_ADD", "register:40f0:8", ["const:b30578:8", "const:4:8"]]
+ 00b30578 ["CALL", null, ["callee:00bdf1d0:8"]]
- 00b30534 bytes 13bb0294
+ 00b30578 bytes 16bb0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6999694c22b2834147f661a8b0c5292"></a>

### [`00b30718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30718.md) → [`00b3075c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b3075c.md) _ZN11flatbuffers20TypeToIntervalStringIhEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf5c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5c0.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md) [`00bdf150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf150.md)
- 新版 呼出元 1件 [`00bdf610`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf610.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md) [`00bdf1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b30790",
      "incomplete_value": false,
      "site": "00b307a0",
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
      "definition_site": "00b3074c",
      "incomplete_value": false,
      "site": "00b3075c",
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
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b307b0",
      "incomplete_value": false,
      "site": "00b307cc",
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
            "const:19b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b3076c",
      "incomplete_value": false,
      "site": "00b30788",
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
            "const:110:8"
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
      "definition_site": "00b30828",
      "incomplete_value": false,
      "site": "00b30844",
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
      "definition_site": "00b307e4",
      "incomplete_value": false,
      "site": "00b30800",
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
      "00b30790",
      "PARAM",
      [
        "storage",
        "00299b41",
        null,
        null
      ]
    ],
    [
      "00b307b0",
      "PARAM",
      [
        "storage",
        "002a0110",
        null,
        null
      ]
    ],
    [
      "00b30828",
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
      "00b30790",
      "PARAM",
      [
        "storage",
        "00299ab4",
        null,
        null
      ]
    ],
    [
      "00b307b0",
      "PARAM",
      [
        "storage",
        "002a019b",
        null,
        null
      ]
    ],
    [
      "00b30828",
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

- 旧版 [`00b30744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30718.md#insn-00b30744) · [`00b3075c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30718.md#insn-00b3075c) · [`00b30788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30718.md#insn-00b30788)
- 新版 [`00b30788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b3075c.md#insn-00b30788) · [`00b307a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b3075c.md#insn-00b307a0) · [`00b307cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b3075c.md#insn-00b307cc)

~~~diff
- 00b30744 ["INT_ADD", "register:40f0:8", ["const:b30744:8", "const:4:8"]]
- 00b30744 ["CALL", null, ["callee:00bdf1a0:8"]]
+ 00b30788 ["INT_ADD", "register:40f0:8", ["const:b30788:8", "const:4:8"]]
+ 00b30788 ["CALL", null, ["callee:00bdf1a0:8"]]
- 00b30744 bytes 83ba0294
+ 00b30788 bytes 86ba0294
- 00b3075c ["INT_ADD", "register:40f0:8", ["const:b3075c:8", "const:4:8"]]
- 00b3075c ["CALL", null, ["callee:00bdc180:8"]]
+ 00b307a0 ["INT_ADD", "register:40f0:8", ["const:b307a0:8", "const:4:8"]]
+ 00b307a0 ["CALL", null, ["callee:00bdc180:8"]]
- 00b3075c bytes 75ae0294
+ 00b307a0 bytes 78ae0294
- 00b30788 ["INT_ADD", "register:40f0:8", ["const:b30788:8", "const:4:8"]]
- 00b30788 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b307cc ["INT_ADD", "register:40f0:8", ["const:b307cc:8", "const:4:8"]]
+ 00b307cc ["CALL", null, ["callee:00bdb130:8"]]
- 00b30788 bytes 56aa0294
+ 00b307cc bytes 59aa0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-286868ceedd771ab3e2d19d7b9123989"></a>

### [`00b308b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b308b8.md) → [`00b308fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b308fc.md) _ZN11flatbuffers20TypeToIntervalStringIaEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5b0.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md) [`00bdf150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf150.md)
- 新版 呼出元 1件 [`00bdf600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf600.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md) [`00bdf1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b30930",
      "incomplete_value": false,
      "site": "00b30940",
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
      "definition_site": "00b308ec",
      "incomplete_value": false,
      "site": "00b308fc",
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
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b30950",
      "incomplete_value": false,
      "site": "00b3096c",
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
            "const:19b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b3090c",
      "incomplete_value": false,
      "site": "00b30928",
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
            "const:110:8"
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
      "definition_site": "00b309c8",
      "incomplete_value": false,
      "site": "00b309e4",
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
      "definition_site": "00b30984",
      "incomplete_value": false,
      "site": "00b309a0",
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
      "00b30930",
      "PARAM",
      [
        "storage",
        "00299b41",
        null,
        null
      ]
    ],
    [
      "00b30950",
      "PARAM",
      [
        "storage",
        "002a0110",
        null,
        null
      ]
    ],
    [
      "00b309c8",
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
      "00b30930",
      "PARAM",
      [
        "storage",
        "00299ab4",
        null,
        null
      ]
    ],
    [
      "00b30950",
      "PARAM",
      [
        "storage",
        "002a019b",
        null,
        null
      ]
    ],
    [
      "00b309c8",
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

- 旧版 [`00b308e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b308b8.md#insn-00b308e4) · [`00b308fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b308b8.md#insn-00b308fc) · [`00b30928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b308b8.md#insn-00b30928)
- 新版 [`00b30928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b308fc.md#insn-00b30928) · [`00b30940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b308fc.md#insn-00b30940) · [`00b3096c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b308fc.md#insn-00b3096c)

~~~diff
- 00b308e4 ["INT_ADD", "register:40f0:8", ["const:b308e4:8", "const:4:8"]]
- 00b308e4 ["CALL", null, ["callee:00bdf1a0:8"]]
+ 00b30928 ["INT_ADD", "register:40f0:8", ["const:b30928:8", "const:4:8"]]
+ 00b30928 ["CALL", null, ["callee:00bdf1a0:8"]]
- 00b308e4 bytes 1bba0294
+ 00b30928 bytes 1eba0294
- 00b308fc ["INT_ADD", "register:40f0:8", ["const:b308fc:8", "const:4:8"]]
- 00b308fc ["CALL", null, ["callee:00bdc180:8"]]
+ 00b30940 ["INT_ADD", "register:40f0:8", ["const:b30940:8", "const:4:8"]]
+ 00b30940 ["CALL", null, ["callee:00bdc180:8"]]
- 00b308fc bytes 0dae0294
+ 00b30940 bytes 10ae0294
- 00b30928 ["INT_ADD", "register:40f0:8", ["const:b30928:8", "const:4:8"]]
- 00b30928 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b3096c ["INT_ADD", "register:40f0:8", ["const:b3096c:8", "const:4:8"]]
+ 00b3096c ["CALL", null, ["callee:00bdb130:8"]]
- 00b30928 bytes eea90294
+ 00b3096c bytes f1a90294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25860f8cf4e60802cafb9d34753259c2"></a>

### [`00b30a58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30a58.md) → [`00b30a9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30a9c.md) _ZN11flatbuffers20TypeToIntervalStringIsEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf610.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md) [`00bdf190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf190.md)
- 新版 呼出元 1件 [`00bdf660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf660.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md) [`00bdf1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b30ad0",
      "incomplete_value": false,
      "site": "00b30ae0",
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
      "definition_site": "00b30a8c",
      "incomplete_value": false,
      "site": "00b30a9c",
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
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b30af0",
      "incomplete_value": false,
      "site": "00b30b0c",
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
            "const:19b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b30aac",
      "incomplete_value": false,
      "site": "00b30ac8",
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
            "const:110:8"
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
      "definition_site": "00b30b68",
      "incomplete_value": false,
      "site": "00b30b84",
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
      "definition_site": "00b30b24",
      "incomplete_value": false,
      "site": "00b30b40",
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
      "00b30ad0",
      "PARAM",
      [
        "storage",
        "00299b41",
        null,
        null
      ]
    ],
    [
      "00b30af0",
      "PARAM",
      [
        "storage",
        "002a0110",
        null,
        null
      ]
    ],
    [
      "00b30b68",
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
      "00b30ad0",
      "PARAM",
      [
        "storage",
        "00299ab4",
        null,
        null
      ]
    ],
    [
      "00b30af0",
      "PARAM",
      [
        "storage",
        "002a019b",
        null,
        null
      ]
    ],
    [
      "00b30b68",
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

- 旧版 [`00b30a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30a58.md#insn-00b30a84) · [`00b30a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30a58.md#insn-00b30a9c) · [`00b30ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30a58.md#insn-00b30ac8)
- 新版 [`00b30ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30a9c.md#insn-00b30ac8) · [`00b30ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30a9c.md#insn-00b30ae0) · [`00b30b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30a9c.md#insn-00b30b0c)

~~~diff
- 00b30a84 ["INT_ADD", "register:40f0:8", ["const:b30a84:8", "const:4:8"]]
- 00b30a84 ["CALL", null, ["callee:00bdf1e0:8"]]
+ 00b30ac8 ["INT_ADD", "register:40f0:8", ["const:b30ac8:8", "const:4:8"]]
+ 00b30ac8 ["CALL", null, ["callee:00bdf1e0:8"]]
- 00b30a84 bytes c3b90294
+ 00b30ac8 bytes c6b90294
- 00b30a9c ["INT_ADD", "register:40f0:8", ["const:b30a9c:8", "const:4:8"]]
- 00b30a9c ["CALL", null, ["callee:00bdc180:8"]]
+ 00b30ae0 ["INT_ADD", "register:40f0:8", ["const:b30ae0:8", "const:4:8"]]
+ 00b30ae0 ["CALL", null, ["callee:00bdc180:8"]]
- 00b30a9c bytes a5ad0294
+ 00b30ae0 bytes a8ad0294
- 00b30ac8 ["INT_ADD", "register:40f0:8", ["const:b30ac8:8", "const:4:8"]]
- 00b30ac8 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b30b0c ["INT_ADD", "register:40f0:8", ["const:b30b0c:8", "const:4:8"]]
+ 00b30b0c ["CALL", null, ["callee:00bdb130:8"]]
- 00b30ac8 bytes 86a90294
+ 00b30b0c bytes 89a90294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1785a0a9af3a067ddfae6f58646ac9b"></a>

### [`00b30bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30bf8.md) → [`00b30c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30c3c.md) _ZN11flatbuffers20TypeToIntervalStringItEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf620.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md) [`00bdf1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf1a0.md)
- 新版 呼出元 1件 [`00bdf670`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf670.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md) [`00bdf1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b30c70",
      "incomplete_value": false,
      "site": "00b30c80",
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
      "definition_site": "00b30c2c",
      "incomplete_value": false,
      "site": "00b30c3c",
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
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b30c90",
      "incomplete_value": false,
      "site": "00b30cac",
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
            "const:19b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b30c4c",
      "incomplete_value": false,
      "site": "00b30c68",
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
            "const:110:8"
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
      "definition_site": "00b30d08",
      "incomplete_value": false,
      "site": "00b30d24",
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
      "definition_site": "00b30cc4",
      "incomplete_value": false,
      "site": "00b30ce0",
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
      "00b30c70",
      "PARAM",
      [
        "storage",
        "00299b41",
        null,
        null
      ]
    ],
    [
      "00b30c90",
      "PARAM",
      [
        "storage",
        "002a0110",
        null,
        null
      ]
    ],
    [
      "00b30d08",
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
      "00b30c70",
      "PARAM",
      [
        "storage",
        "00299ab4",
        null,
        null
      ]
    ],
    [
      "00b30c90",
      "PARAM",
      [
        "storage",
        "002a019b",
        null,
        null
      ]
    ],
    [
      "00b30d08",
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

- 旧版 [`00b30c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30bf8.md#insn-00b30c24) · [`00b30c3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30bf8.md#insn-00b30c3c) · [`00b30c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30bf8.md#insn-00b30c68)
- 新版 [`00b30c68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30c3c.md#insn-00b30c68) · [`00b30c80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30c3c.md#insn-00b30c80) · [`00b30cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30c3c.md#insn-00b30cac)

~~~diff
- 00b30c24 ["INT_ADD", "register:40f0:8", ["const:b30c24:8", "const:4:8"]]
- 00b30c24 ["CALL", null, ["callee:00bdf1f0:8"]]
+ 00b30c68 ["INT_ADD", "register:40f0:8", ["const:b30c68:8", "const:4:8"]]
+ 00b30c68 ["CALL", null, ["callee:00bdf1f0:8"]]
- 00b30c24 bytes 5fb90294
+ 00b30c68 bytes 62b90294
- 00b30c3c ["INT_ADD", "register:40f0:8", ["const:b30c3c:8", "const:4:8"]]
- 00b30c3c ["CALL", null, ["callee:00bdc180:8"]]
+ 00b30c80 ["INT_ADD", "register:40f0:8", ["const:b30c80:8", "const:4:8"]]
+ 00b30c80 ["CALL", null, ["callee:00bdc180:8"]]
- 00b30c3c bytes 3dad0294
+ 00b30c80 bytes 40ad0294
- 00b30c68 ["INT_ADD", "register:40f0:8", ["const:b30c68:8", "const:4:8"]]
- 00b30c68 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b30cac ["INT_ADD", "register:40f0:8", ["const:b30cac:8", "const:4:8"]]
+ 00b30cac ["CALL", null, ["callee:00bdb130:8"]]
- 00b30c68 bytes 1ea90294
+ 00b30cac bytes 21a90294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffbd7bdef200b5f2a6c5d185df7ac1b2"></a>

### [`00b30d98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30d98.md) → [`00b30ddc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30ddc.md) _ZN11flatbuffers20TypeToIntervalStringIiEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf5d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5d0.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md) [`00bdf150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf150.md)
- 新版 呼出元 1件 [`00bdf620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf620.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md) [`00bdf1a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1a0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b30e10",
      "incomplete_value": false,
      "site": "00b30e20",
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
      "definition_site": "00b30dcc",
      "incomplete_value": false,
      "site": "00b30ddc",
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
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b30e30",
      "incomplete_value": false,
      "site": "00b30e4c",
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
            "const:19b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b30dec",
      "incomplete_value": false,
      "site": "00b30e08",
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
            "const:110:8"
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
      "definition_site": "00b30ea8",
      "incomplete_value": false,
      "site": "00b30ec4",
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
      "definition_site": "00b30e64",
      "incomplete_value": false,
      "site": "00b30e80",
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
      "00b30e10",
      "PARAM",
      [
        "storage",
        "00299b41",
        null,
        null
      ]
    ],
    [
      "00b30e30",
      "PARAM",
      [
        "storage",
        "002a0110",
        null,
        null
      ]
    ],
    [
      "00b30ea8",
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
      "00b30e10",
      "PARAM",
      [
        "storage",
        "00299ab4",
        null,
        null
      ]
    ],
    [
      "00b30e30",
      "PARAM",
      [
        "storage",
        "002a019b",
        null,
        null
      ]
    ],
    [
      "00b30ea8",
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

- 旧版 [`00b30dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30d98.md#insn-00b30dc4) · [`00b30ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30d98.md#insn-00b30ddc) · [`00b30e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30d98.md#insn-00b30e08)
- 新版 [`00b30e08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30ddc.md#insn-00b30e08) · [`00b30e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30ddc.md#insn-00b30e20) · [`00b30e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30ddc.md#insn-00b30e4c)

~~~diff
- 00b30dc4 ["INT_ADD", "register:40f0:8", ["const:b30dc4:8", "const:4:8"]]
- 00b30dc4 ["CALL", null, ["callee:00bdf1a0:8"]]
+ 00b30e08 ["INT_ADD", "register:40f0:8", ["const:b30e08:8", "const:4:8"]]
+ 00b30e08 ["CALL", null, ["callee:00bdf1a0:8"]]
- 00b30dc4 bytes e3b80294
+ 00b30e08 bytes e6b80294
- 00b30ddc ["INT_ADD", "register:40f0:8", ["const:b30ddc:8", "const:4:8"]]
- 00b30ddc ["CALL", null, ["callee:00bdc180:8"]]
+ 00b30e20 ["INT_ADD", "register:40f0:8", ["const:b30e20:8", "const:4:8"]]
+ 00b30e20 ["CALL", null, ["callee:00bdc180:8"]]
- 00b30ddc bytes d5ac0294
+ 00b30e20 bytes d8ac0294
- 00b30e08 ["INT_ADD", "register:40f0:8", ["const:b30e08:8", "const:4:8"]]
- 00b30e08 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b30e4c ["INT_ADD", "register:40f0:8", ["const:b30e4c:8", "const:4:8"]]
+ 00b30e4c ["CALL", null, ["callee:00bdb130:8"]]
- 00b30e08 bytes b6a80294
+ 00b30e4c bytes b9a80294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e4104bbb3e00749e932dec632831d67"></a>

### [`00b30f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30f38.md) → [`00b30f7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30f7c.md) _ZN11flatbuffers20TypeToIntervalStringIjEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf5e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5e0.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md) [`00bdf160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf160.md)
- 新版 呼出元 1件 [`00bdf630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf630.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md) [`00bdf1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b30fb0",
      "incomplete_value": false,
      "site": "00b30fc0",
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
      "definition_site": "00b30f6c",
      "incomplete_value": false,
      "site": "00b30f7c",
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
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b30fd0",
      "incomplete_value": false,
      "site": "00b30fec",
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
            "const:19b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b30f8c",
      "incomplete_value": false,
      "site": "00b30fa8",
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
            "const:110:8"
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
      "definition_site": "00b31048",
      "incomplete_value": false,
      "site": "00b31064",
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
      "definition_site": "00b31004",
      "incomplete_value": false,
      "site": "00b31020",
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
      "00b30fb0",
      "PARAM",
      [
        "storage",
        "00299b41",
        null,
        null
      ]
    ],
    [
      "00b30fd0",
      "PARAM",
      [
        "storage",
        "002a0110",
        null,
        null
      ]
    ],
    [
      "00b31048",
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
      "00b30fb0",
      "PARAM",
      [
        "storage",
        "00299ab4",
        null,
        null
      ]
    ],
    [
      "00b30fd0",
      "PARAM",
      [
        "storage",
        "002a019b",
        null,
        null
      ]
    ],
    [
      "00b31048",
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

- 旧版 [`00b30f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30f38.md#insn-00b30f64) · [`00b30f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30f38.md#insn-00b30f7c) · [`00b30fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b30/00b30f38.md#insn-00b30fa8)
- 新版 [`00b30fa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30f7c.md#insn-00b30fa8) · [`00b30fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30f7c.md#insn-00b30fc0) · [`00b30fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b30/00b30f7c.md#insn-00b30fec)

~~~diff
- 00b30f64 ["INT_ADD", "register:40f0:8", ["const:b30f64:8", "const:4:8"]]
- 00b30f64 ["CALL", null, ["callee:00bdf1b0:8"]]
+ 00b30fa8 ["INT_ADD", "register:40f0:8", ["const:b30fa8:8", "const:4:8"]]
+ 00b30fa8 ["CALL", null, ["callee:00bdf1b0:8"]]
- 00b30f64 bytes 7fb80294
+ 00b30fa8 bytes 82b80294
- 00b30f7c ["INT_ADD", "register:40f0:8", ["const:b30f7c:8", "const:4:8"]]
- 00b30f7c ["CALL", null, ["callee:00bdc180:8"]]
+ 00b30fc0 ["INT_ADD", "register:40f0:8", ["const:b30fc0:8", "const:4:8"]]
+ 00b30fc0 ["CALL", null, ["callee:00bdc180:8"]]
- 00b30f7c bytes 6dac0294
+ 00b30fc0 bytes 70ac0294
- 00b30fa8 ["INT_ADD", "register:40f0:8", ["const:b30fa8:8", "const:4:8"]]
- 00b30fa8 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b30fec ["INT_ADD", "register:40f0:8", ["const:b30fec:8", "const:4:8"]]
+ 00b30fec ["CALL", null, ["callee:00bdb130:8"]]
- 00b30fa8 bytes 4ea80294
+ 00b30fec bytes 51a80294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7140a0e6e636b4ab6e4ab4a5d0fd247"></a>

### [`00b310d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b310d8.md) → [`00b3111c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3111c.md) _ZN11flatbuffers20TypeToIntervalStringIlEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf5f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf5f0.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md) [`00bdf170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf170.md)
- 新版 呼出元 1件 [`00bdf640`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf640.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md) [`00bdf1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b31150",
      "incomplete_value": false,
      "site": "00b31160",
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
      "definition_site": "00b3110c",
      "incomplete_value": false,
      "site": "00b3111c",
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
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b31170",
      "incomplete_value": false,
      "site": "00b3118c",
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
            "const:19b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b3112c",
      "incomplete_value": false,
      "site": "00b31148",
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
            "const:110:8"
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
      "definition_site": "00b311e8",
      "incomplete_value": false,
      "site": "00b31204",
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
      "definition_site": "00b311a4",
      "incomplete_value": false,
      "site": "00b311c0",
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
      "00b31150",
      "PARAM",
      [
        "storage",
        "00299b41",
        null,
        null
      ]
    ],
    [
      "00b31170",
      "PARAM",
      [
        "storage",
        "002a0110",
        null,
        null
      ]
    ],
    [
      "00b311e8",
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
      "00b31150",
      "PARAM",
      [
        "storage",
        "00299ab4",
        null,
        null
      ]
    ],
    [
      "00b31170",
      "PARAM",
      [
        "storage",
        "002a019b",
        null,
        null
      ]
    ],
    [
      "00b311e8",
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

- 旧版 [`00b31104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b310d8.md#insn-00b31104) · [`00b3111c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b310d8.md#insn-00b3111c) · [`00b31148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b310d8.md#insn-00b31148)
- 新版 [`00b31148`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3111c.md#insn-00b31148) · [`00b31160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3111c.md#insn-00b31160) · [`00b3118c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3111c.md#insn-00b3118c)

~~~diff
- 00b31104 ["INT_ADD", "register:40f0:8", ["const:b31104:8", "const:4:8"]]
- 00b31104 ["CALL", null, ["callee:00bdf1c0:8"]]
+ 00b31148 ["INT_ADD", "register:40f0:8", ["const:b31148:8", "const:4:8"]]
+ 00b31148 ["CALL", null, ["callee:00bdf1c0:8"]]
- 00b31104 bytes 1bb80294
+ 00b31148 bytes 1eb80294
- 00b3111c ["INT_ADD", "register:40f0:8", ["const:b3111c:8", "const:4:8"]]
- 00b3111c ["CALL", null, ["callee:00bdc180:8"]]
+ 00b31160 ["INT_ADD", "register:40f0:8", ["const:b31160:8", "const:4:8"]]
+ 00b31160 ["CALL", null, ["callee:00bdc180:8"]]
- 00b3111c bytes 05ac0294
+ 00b31160 bytes 08ac0294
- 00b31148 ["INT_ADD", "register:40f0:8", ["const:b31148:8", "const:4:8"]]
- 00b31148 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b3118c ["INT_ADD", "register:40f0:8", ["const:b3118c:8", "const:4:8"]]
+ 00b3118c ["CALL", null, ["callee:00bdb130:8"]]
- 00b31148 bytes e6a70294
+ 00b3118c bytes e9a70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2af008067ef2168b545b8afd84bef170"></a>

### [`00b31278`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31278.md) → [`00b312bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b312bc.md) _ZN11flatbuffers20TypeToIntervalStringImEENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bdf600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf600.md) · 呼出先 5件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb0e0.md) [`00bdc130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdc130.md) [`00bdf180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdf180.md)
- 新版 呼出元 1件 [`00bdf650`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf650.md) · 呼出先 5件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb130.md) [`00bdc180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdc180.md) [`00bdf1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf1d0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.12% / 新版 97.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b312f0",
      "incomplete_value": false,
      "site": "00b31300",
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
      "definition_site": "00b312ac",
      "incomplete_value": false,
      "site": "00b312bc",
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
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b31310",
      "incomplete_value": false,
      "site": "00b3132c",
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
            "const:19b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b312cc",
      "incomplete_value": false,
      "site": "00b312e8",
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
            "const:110:8"
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
      "00b312f0",
      "PARAM",
      [
        "storage",
        "00299b41",
        null,
        null
      ]
    ],
    [
      "00b31310",
      "PARAM",
      [
        "storage",
        "002a0110",
        null,
        null
      ]
    ],
    [
      "00b31388",
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
      "00b312f0",
      "PARAM",
      [
        "storage",
        "00299ab4",
        null,
        null
      ]
    ],
    [
      "00b31310",
      "PARAM",
      [
        "storage",
        "002a019b",
        null,
        null
      ]
    ],
    [
      "00b31388",
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

- 旧版 [`00b312a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31278.md#insn-00b312a4) · [`00b312bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31278.md#insn-00b312bc) · [`00b312e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31278.md#insn-00b312e8)
- 新版 [`00b312e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b312bc.md#insn-00b312e8) · [`00b31300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b312bc.md#insn-00b31300) · [`00b3132c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b312bc.md#insn-00b3132c)

~~~diff
- 00b312a4 ["INT_ADD", "register:40f0:8", ["const:b312a4:8", "const:4:8"]]
- 00b312a4 ["CALL", null, ["callee:00bdf1d0:8"]]
+ 00b312e8 ["INT_ADD", "register:40f0:8", ["const:b312e8:8", "const:4:8"]]
+ 00b312e8 ["CALL", null, ["callee:00bdf1d0:8"]]
- 00b312a4 bytes b7b70294
+ 00b312e8 bytes bab70294
- 00b312bc ["INT_ADD", "register:40f0:8", ["const:b312bc:8", "const:4:8"]]
- 00b312bc ["CALL", null, ["callee:00bdc180:8"]]
+ 00b31300 ["INT_ADD", "register:40f0:8", ["const:b31300:8", "const:4:8"]]
+ 00b31300 ["CALL", null, ["callee:00bdc180:8"]]
- 00b312bc bytes 9dab0294
+ 00b31300 bytes a0ab0294
- 00b312e8 ["INT_ADD", "register:40f0:8", ["const:b312e8:8", "const:4:8"]]
- 00b312e8 ["CALL", null, ["callee:00bdb130:8"]]
+ 00b3132c ["INT_ADD", "register:40f0:8", ["const:b3132c:8", "const:4:8"]]
+ 00b3132c ["CALL", null, ["callee:00bdb130:8"]]
- 00b312e8 bytes 7ea70294
+ 00b3132c bytes 81a70294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f6d5a4b0fdd9b37daaf6bd64573a0aa"></a>

### [`00b3148c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b3148c.md) → [`00b314d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b314d0.md) FUN_00b314d0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 70.97% / 新版 70.97%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b314f4",
      "incomplete_value": true,
      "site": "00b31504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b314b0",
      "incomplete_value": true,
      "site": "00b314c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b314f8",
      "incomplete_value": true,
      "site": "00b31508",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b314b4",
      "incomplete_value": true,
      "site": "00b314c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b3150c",
      "incomplete_value": true,
      "site": "00b3150c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b314c8",
      "incomplete_value": true,
      "site": "00b314c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b314e4",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "00b314e8",
      "READ",
      [
        "storage",
        "00c1ad80",
        null,
        "pointer"
      ]
    ],
    [
      "00b31504",
      "DATA",
      [
        "storage",
        "00c10fb0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b314e4",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "00b314e8",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "00b31504",
      "DATA",
      [
        "storage",
        "00c11000",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b314a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b3148c.md#insn-00b314a4) · [`00b314a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b3148c.md#insn-00b314a0) · [`00b314d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b3148c.md#insn-00b314d4)
- 新版 [`00b314e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b314d0.md#insn-00b314e8) · [`00b314e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b314d0.md#insn-00b314e4) · [`00b31518`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b314d0.md#insn-00b31518)

~~~diff
- 00b314a4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d80:8"]]
- 00b314a4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b314e8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd0:8"]]
+ 00b314e8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b314a4 bytes 29c146f9
+ 00b314e8 bytes 29e946f9
- 00b314a0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
- 00b314a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b314e4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e28:8"]]
+ 00b314e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b314a0 bytes 08ed46f9
+ 00b314e4 bytes 081547f9
- 00b314d4 ["INT_ADD", "register:40f0:8", ["const:b314d4:8", "const:4:8"]]
- 00b314d4 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b31518 ["INT_ADD", "register:40f0:8", ["const:b31518:8", "const:4:8"]]
+ 00b31518 ["CALL", null, ["callee:00bdb060:8"]]
- 00b314d4 bytes cfa60294
+ 00b31518 bytes d2a60294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df91ee6aa06a46c4443b8a72d3b43c67"></a>

### [`00b31508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31508.md) → [`00b3154c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3154c.md) FUN_00b3154c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 90.00% / 新版 90.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b31570",
      "incomplete_value": true,
      "site": "00b31570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b3152c",
      "incomplete_value": true,
      "site": "00b3152c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "00b31574",
      "incomplete_value": true,
      "site": "00b31574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b31530",
      "incomplete_value": true,
      "site": "00b31530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "definition_site": "00b3158c",
      "incomplete_value": true,
      "site": "00b3158c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b31548",
      "incomplete_value": true,
      "site": "00b31548",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b3155c",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "00b31570",
      "DATA",
      [
        "storage",
        "00c10fb0",
        null,
        "pointer"
      ]
    ],
    [
      "00b31574",
      "DATA",
      [
        "storage",
        "00c11000",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b3155c",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "00b31570",
      "DATA",
      [
        "storage",
        "00c11000",
        null,
        "pointer"
      ]
    ],
    [
      "00b31574",
      "DATA",
      [
        "storage",
        "00c11050",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b31518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31508.md#insn-00b31518) · [`00b3153c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31508.md#insn-00b3153c) · [`00b31554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31508.md#insn-00b31554)
- 新版 [`00b3155c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3154c.md#insn-00b3155c) · [`00b31580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3154c.md#insn-00b31580) · [`00b31598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3154c.md#insn-00b31598)

~~~diff
- 00b31518 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:dd8:8"]]
- 00b31518 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b3155c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e28:8"]]
+ 00b3155c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b31518 bytes 08ed46f9
+ 00b3155c bytes 081547f9
- 00b3153c ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d80:8"]]
- 00b3153c ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b31580 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:dd0:8"]]
+ 00b31580 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00b3153c bytes 4ac146f9
+ 00b31580 bytes 4ae946f9
- 00b31554 ["INT_ADD", "register:40f0:8", ["const:b31554:8", "const:4:8"]]
- 00b31554 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b31598 ["INT_ADD", "register:40f0:8", ["const:b31598:8", "const:4:8"]]
+ 00b31598 ["CALL", null, ["callee:00bdb060:8"]]
- 00b31554 bytes afa60294
+ 00b31598 bytes b2a60294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-200517b43fd63e95a08641b0912fd226"></a>

### [`00b31600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31600.md) → [`00b31644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31644.md) FUN_00b31644

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b31664",
      "incomplete_value": true,
      "site": "00b31670",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b31620",
      "incomplete_value": true,
      "site": "00b3162c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "00b31674",
      "incomplete_value": true,
      "site": "00b31674",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b31630",
      "incomplete_value": true,
      "site": "00b31630",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "definition_site": "00b3168c",
      "incomplete_value": true,
      "site": "00b3168c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b31648",
      "incomplete_value": true,
      "site": "00b31648",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b3165c",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "00b31670",
      "DATA",
      [
        "storage",
        "00c10fb0",
        null,
        "pointer"
      ]
    ],
    [
      "00b31674",
      "DATA",
      [
        "storage",
        "00c11000",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b3165c",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "00b31670",
      "DATA",
      [
        "storage",
        "00c11000",
        null,
        "pointer"
      ]
    ],
    [
      "00b31674",
      "DATA",
      [
        "storage",
        "00c11050",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b31618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31600.md#insn-00b31618) · [`00b31634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31600.md#insn-00b31634) · [`00b31640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31600.md#insn-00b31640)
- 新版 [`00b3165c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31644.md#insn-00b3165c) · [`00b31684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b31644.md#insn-00b31684)

~~~diff
- 00b31618 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd8:8"]]
- 00b31618 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b3165c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e28:8"]]
+ 00b3165c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b31618 bytes 29ed46f9
+ 00b3165c bytes 291547f9
- 00b31634 ["COPY", "register:4050:8", ["const:c1a000:8"]]
- 00b31634 bytes 4a0700b0
- 00b31640 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:d80:8"]]
- 00b31640 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b31684 ["INT_ADD", "tmp:0:8", ["register:4050:8", "const:dd0:8"]]
+ 00b31684 ["LOAD", "register:4050:8", ["const:1b1:8", "tmp:0:8"]]
- 00b31640 bytes 4ac146f9
+ 00b31684 bytes 4ae946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d2df8a24fc2b0ffb67e2a4468177225"></a>

### [`00b31680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31680.md) → [`00b316c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b316c4.md) FUN_00b316c4

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_value

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 4件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b316e4",
      "incomplete_value": true,
      "site": "00b316f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b316a0",
      "incomplete_value": true,
      "site": "00b316ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "00b316f4",
      "incomplete_value": true,
      "site": "00b316f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b316b0",
      "incomplete_value": true,
      "site": "00b316b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:68:8"
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
      "definition_site": "00b3170c",
      "incomplete_value": true,
      "site": "00b3170c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b316c8",
      "incomplete_value": true,
      "site": "00b316c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b316dc",
      "READ",
      [
        "storage",
        "00c1add8",
        null,
        "pointer"
      ]
    ],
    [
      "00b316f0",
      "DATA",
      [
        "storage",
        "00c10fb0",
        null,
        "pointer"
      ]
    ],
    [
      "00b316f4",
      "DATA",
      [
        "storage",
        "00c11000",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b316dc",
      "READ",
      [
        "storage",
        "00c1ae28",
        null,
        "pointer"
      ]
    ],
    [
      "00b316f0",
      "DATA",
      [
        "storage",
        "00c11000",
        null,
        "pointer"
      ]
    ],
    [
      "00b316f4",
      "DATA",
      [
        "storage",
        "00c11050",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b316f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31680.md#insn-00b316f4) · [`00b31698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31680.md#insn-00b31698) · [`00b316b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31680.md#insn-00b316b4)
- 新版 [`00b31738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b316c4.md#insn-00b31738) · [`00b316dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b316c4.md#insn-00b316dc)

~~~diff
- 00b316f4 ["INT_ADD", "register:40f0:8", ["const:b316f4:8", "const:4:8"]]
- 00b316f4 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b31738 ["INT_ADD", "register:40f0:8", ["const:b31738:8", "const:4:8"]]
+ 00b31738 ["CALL", null, ["callee:00be01e0:8"]]
- 00b316f4 bytes a7ba0294
+ 00b31738 bytes aaba0294
- 00b31698 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd8:8"]]
- 00b31698 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b316dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e28:8"]]
+ 00b316dc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b31698 bytes 29ed46f9
+ 00b316dc bytes 291547f9
- 00b316b4 ["COPY", "register:4050:8", ["const:c1a000:8"]]
- 00b316b4 bytes 4a0700b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-32f40cd47e25c9d8116678542ffa90a5"></a>

### [`00b31708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31708.md) → [`00b3174c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3174c.md) FUN_00b3174c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

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
      "definition_site": "00b31768",
      "incomplete_value": true,
      "site": "00b3176c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b31724",
      "incomplete_value": true,
      "site": "00b31728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b31788",
      "incomplete_value": true,
      "site": "00b31788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b31744",
      "incomplete_value": true,
      "site": "00b31744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b31760",
      "READ",
      [
        "storage",
        "00c1ad80",
        null,
        "pointer"
      ]
    ],
    [
      "00b3176c",
      "DATA",
      [
        "storage",
        "00c11128",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b31780",
      "READ",
      [
        "storage",
        "00c1ba00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b31760",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "00b3176c",
      "DATA",
      [
        "storage",
        "00c11178",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b31780",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3171c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31708.md#insn-00b3171c) · [`00b31734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31708.md#insn-00b31734) · [`00b3173c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31708.md#insn-00b3173c)
- 新版 [`00b31760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3174c.md#insn-00b31760) · [`00b31778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3174c.md#insn-00b31778) · [`00b31780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3174c.md#insn-00b31780)

~~~diff
- 00b3171c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d80:8"]]
- 00b3171c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b31760 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd0:8"]]
+ 00b31760 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b3171c bytes 29c146f9
+ 00b31760 bytes 29e946f9
- 00b31734 ["INT_ADD", "register:40f0:8", ["const:b31734:8", "const:4:8"]]
- 00b31734 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b31778 ["INT_ADD", "register:40f0:8", ["const:b31778:8", "const:4:8"]]
+ 00b31778 ["CALL", null, ["callee:00bdb060:8"]]
- 00b31734 bytes 37a60294
+ 00b31778 bytes 3aa60294
- 00b3173c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a00:8"]]
- 00b3173c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b31780 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a50:8"]]
+ 00b31780 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b3173c bytes 080145f9
+ 00b31780 bytes 082945f9
~~~


<a id="compare-5d75e428d60184483a19a39b918ae4f3"></a>

### [`00b31758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31758.md) → [`00b3179c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3179c.md) FUN_00b3179c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "00b317b8",
      "incomplete_value": true,
      "site": "00b317bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b31774",
      "incomplete_value": true,
      "site": "00b31778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b317dc",
      "incomplete_value": true,
      "site": "00b317dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b31798",
      "incomplete_value": true,
      "site": "00b31798",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b317b0",
      "READ",
      [
        "storage",
        "00c1ad80",
        null,
        "pointer"
      ]
    ],
    [
      "00b317bc",
      "DATA",
      [
        "storage",
        "00c11128",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b317d0",
      "READ",
      [
        "storage",
        "00c1ba00",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b317b0",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "00b317bc",
      "DATA",
      [
        "storage",
        "00c11178",
        null,
        "undefined1[128]"
      ]
    ],
    [
      "00b317d0",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b3176c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31758.md#insn-00b3176c) · [`00b31784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31758.md#insn-00b31784) · [`00b3178c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b31/00b31758.md#insn-00b3178c)
- 新版 [`00b317b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3179c.md#insn-00b317b0) · [`00b317c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3179c.md#insn-00b317c8) · [`00b317d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b31/00b3179c.md#insn-00b317d0)

~~~diff
- 00b3176c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d80:8"]]
- 00b3176c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b317b0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd0:8"]]
+ 00b317b0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b3176c bytes 29c146f9
+ 00b317b0 bytes 29e946f9
- 00b31784 ["INT_ADD", "register:40f0:8", ["const:b31784:8", "const:4:8"]]
- 00b31784 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b317c8 ["INT_ADD", "register:40f0:8", ["const:b317c8:8", "const:4:8"]]
+ 00b317c8 ["CALL", null, ["callee:00bdb060:8"]]
- 00b31784 bytes 23a60294
+ 00b317c8 bytes 26a60294
- 00b3178c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a00:8"]]
- 00b3178c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b317d0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a50:8"]]
+ 00b317d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b3178c bytes 080145f9
+ 00b317d0 bytes 082945f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-229c4556e9385a6e973d0705906d3569"></a>

### [`00b46598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46598.md) → [`00b465dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b465dc.md) _ZN11flatbuffers13FileExistsRawEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 2件 [`00b46e8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46e8c.md) [`00b46ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46ebc.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb400.md) [`00bdd1f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdd1f0.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 2件 [`00b46ed0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46ed0.md) [`00b46f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46f00.md) · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb450.md) [`00bdd240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdd240.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 97.53% / 新版 97.53%

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
      "definition_site": "00b46654",
      "incomplete_value": true,
      "site": "00b4665c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46610",
      "incomplete_value": true,
      "site": "00b46618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "00b46658",
      "incomplete_value": true,
      "site": "00b46664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b46614",
      "incomplete_value": true,
      "site": "00b46620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b46694",
      "incomplete_value": true,
      "site": "00b4669c",
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
            "const:943:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46650",
      "incomplete_value": true,
      "site": "00b46658",
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
            "const:8a9:8"
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
      "00b46600",
      "READ",
      [
        "storage",
        "00c1ba68",
        null,
        "pointer"
      ]
    ],
    [
      "00b46634",
      "DATA",
      [
        "storage",
        "00c112d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b46638",
      "DATA",
      [
        "storage",
        "00c112a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b46600",
      "READ",
      [
        "storage",
        "00c1bab8",
        null,
        "pointer"
      ]
    ],
    [
      "00b46634",
      "DATA",
      [
        "storage",
        "00c11320",
        null,
        "pointer"
      ]
    ],
    [
      "00b46638",
      "DATA",
      [
        "storage",
        "00c112f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46598.md#insn-00b46658) · [`00b4669c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46598.md#insn-00b4669c) · [`00b465bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46598.md#insn-00b465bc)
- 新版 [`00b4669c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b465dc.md#insn-00b4669c) · [`00b466e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b465dc.md#insn-00b466e0) · [`00b46600`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b465dc.md#insn-00b46600)

~~~diff
- 00b46658 ["INT_ADD", "register:40f0:8", ["const:b46658:8", "const:4:8"]]
- 00b46658 ["CALL", null, ["callee:00bdd240:8"]]
+ 00b4669c ["INT_ADD", "register:40f0:8", ["const:b4669c:8", "const:4:8"]]
+ 00b4669c ["CALL", null, ["callee:00bdd240:8"]]
- 00b46658 bytes e65a0294
+ 00b4669c bytes e95a0294
- 00b4669c ["INT_ADD", "register:40f0:8", ["const:b4669c:8", "const:4:8"]]
- 00b4669c ["CALL", null, ["callee:00be02a0:8"]]
+ 00b466e0 ["INT_ADD", "register:40f0:8", ["const:b466e0:8", "const:4:8"]]
+ 00b466e0 ["CALL", null, ["callee:00be02a0:8"]]
- 00b4669c bytes ed660294
+ 00b466e0 bytes f0660294
- 00b465bc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 00b465bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b46600 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00b46600 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b465bc bytes 083545f9
+ 00b46600 bytes 085d45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1ed73510f26795e2576166f83b045855"></a>

### [`00b46718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46718.md) → [`00b4675c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b4675c.md) _ZN11flatbuffers11LoadFileRawEPKcbPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b46e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46e7c.md) [`00b46e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46e98.md) · 呼出先 17件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb310.md) [`00bdb340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb340.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md)
- 新版 呼出元 2件 [`00b46ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46ec0.md) [`00b46edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46edc.md) · 呼出先 17件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb360.md) [`00bdb390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb390.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 98.83% / 新版 98.83%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

アドレスに依存する影響 `store_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b467f4",
      "incomplete_value": true,
      "site": "00b467fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b467b0",
      "incomplete_value": true,
      "site": "00b467b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "00b467f8",
      "incomplete_value": true,
      "site": "00b46804",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b467b4",
      "incomplete_value": true,
      "site": "00b467c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 18,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b4692c",
      "incomplete_value": true,
      "site": "00b46948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b468e8",
      "incomplete_value": true,
      "site": "00b46904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b467ac",
      "READ",
      [
        "storage",
        "00c1ba68",
        null,
        "pointer"
      ]
    ],
    [
      "00b467d4",
      "DATA",
      [
        "storage",
        "00c112d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b467d8",
      "DATA",
      [
        "storage",
        "00c112a8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b467ac",
      "READ",
      [
        "storage",
        "00c1bab8",
        null,
        "pointer"
      ]
    ],
    [
      "00b467d4",
      "DATA",
      [
        "storage",
        "00c11320",
        null,
        "pointer"
      ]
    ],
    [
      "00b467d8",
      "DATA",
      [
        "storage",
        "00c112f8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46718.md#insn-00b46754) · [`00b46768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46718.md#insn-00b46768) · [`00b46798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46718.md#insn-00b46798)
- 新版 [`00b46798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b4675c.md#insn-00b46798) · [`00b467ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b4675c.md#insn-00b467ac) · [`00b467dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b4675c.md#insn-00b467dc)

~~~diff
- 00b46754 ["INT_ADD", "register:40f0:8", ["const:b46754:8", "const:4:8"]]
- 00b46754 ["CALL", null, ["callee:00bdca10:8"]]
+ 00b46798 ["INT_ADD", "register:40f0:8", ["const:b46798:8", "const:4:8"]]
+ 00b46798 ["CALL", null, ["callee:00bdca10:8"]]
- 00b46754 bytes 9b580294
+ 00b46798 bytes 9e580294
- 00b46768 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a68:8"]]
- 00b46768 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b467ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ab8:8"]]
+ 00b467ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46768 bytes 083545f9
+ 00b467ac bytes 085d45f9
- 00b46798 ["INT_ADD", "register:40f0:8", ["const:b46798:8", "const:4:8"]]
- 00b46798 ["CALL", null, ["callee:00bdb390:8"]]
+ 00b467dc ["INT_ADD", "register:40f0:8", ["const:b467dc:8", "const:4:8"]]
+ 00b467dc ["CALL", null, ["callee:00bdb390:8"]]
- 00b46798 bytes ea520294
+ 00b467dc bytes ed520294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9c82d7e2b83090ba55fa319183af938"></a>

### [`00b46e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46e98.md) → [`00b46edc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46edc.md) _ZN11flatbuffers19SetLoadFileFunctionEPFbPKcbPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b46718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46718.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b4675c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b4675c.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 22.22% / 新版 22.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46ef8",
      "incomplete_value": true,
      "site": "00b46ef8",
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
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46eb4",
      "incomplete_value": true,
      "site": "00b46eb4",
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
            "const:778:8"
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
      "00b46ee4",
      "READ",
      [
        "storage",
        "00c24778",
        null,
        "pointer"
      ]
    ],
    [
      "00b46ee8",
      "READ",
      [
        "storage",
        "00c1ba50",
        null,
        "pointer"
      ]
    ],
    [
      "00b46ef4",
      "DATA",
      [
        "storage",
        "00b46718",
        "_ZN11flatbuffers11LoadFileRawEPKcbPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b46ee4",
      "READ",
      [
        "storage",
        "00c247c8",
        null,
        "pointer"
      ]
    ],
    [
      "00b46ee8",
      "READ",
      [
        "storage",
        "00c1baa0",
        null,
        "pointer"
      ]
    ],
    [
      "00b46ef4",
      "DATA",
      [
        "storage",
        "00b4675c",
        "_ZN11flatbuffers11LoadFileRawEPKcbPNSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEE",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46e98.md#insn-00b46eb4) · [`00b46e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46e98.md#insn-00b46e98) · [`00b46e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46e98.md#insn-00b46e9c)
- 新版 [`00b46ef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46edc.md#insn-00b46ef8)

~~~diff
- 00b46eb4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:778:8"]]
- 00b46eb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00b46ef8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7c8:8"]]
+ 00b46ef8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00b46eb4 bytes 2abd03f9
+ 00b46ef8 bytes 2ae503f9
- 00b46e98 ["COPY", "register:4048:8", ["const:c24000:8"]]
- 00b46e98 bytes e90600d0
- 00b46e9c ["COPY", "register:4050:8", ["const:c1b000:8"]]
- 00b46e9c bytes aa0600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-243917f36b2bb977c6df4ff9965ff8ab"></a>

### [`00b46ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46ebc.md) → [`00b46f00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46f00.md) _ZN11flatbuffers21SetFileExistsFunctionEPFbPKcE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00b46598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46598.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00b465dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b465dc.md)

変更の種類 constant, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 22.22% / 新版 22.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b46f1c",
      "incomplete_value": true,
      "site": "00b46f1c",
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
            "const:7d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46ed8",
      "incomplete_value": true,
      "site": "00b46ed8",
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
            "const:780:8"
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
      "00b46f08",
      "READ",
      [
        "storage",
        "00c24780",
        null,
        "pointer"
      ]
    ],
    [
      "00b46f0c",
      "READ",
      [
        "storage",
        "00c1ba58",
        null,
        "pointer"
      ]
    ],
    [
      "00b46f18",
      "DATA",
      [
        "storage",
        "00b46598",
        "_ZN11flatbuffers13FileExistsRawEPKc",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b46f08",
      "READ",
      [
        "storage",
        "00c247d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b46f0c",
      "READ",
      [
        "storage",
        "00c1baa8",
        null,
        "pointer"
      ]
    ],
    [
      "00b46f18",
      "DATA",
      [
        "storage",
        "00b465dc",
        "_ZN11flatbuffers13FileExistsRawEPKc",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46ebc.md#insn-00b46ed8) · [`00b46ebc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46ebc.md#insn-00b46ebc) · [`00b46ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b46/00b46ebc.md#insn-00b46ec0)
- 新版 [`00b46f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b46/00b46f00.md#insn-00b46f1c)

~~~diff
- 00b46ed8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:780:8"]]
- 00b46ed8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
+ 00b46f1c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:7d0:8"]]
+ 00b46f1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00b46ed8 bytes 2ac103f9
+ 00b46f1c bytes 2ae903f9
- 00b46ebc ["COPY", "register:4048:8", ["const:c24000:8"]]
- 00b46ebc bytes e90600d0
- 00b46ec0 ["COPY", "register:4050:8", ["const:c1b000:8"]]
- 00b46ec0 bytes aa0600b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c378d79432add0a41f6d4079c31b1853"></a>

### [`00b47a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47a74.md) → [`00b47ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47ab8.md) FUN_00b47ab8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md) [`00be0250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0250.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md) [`00be02a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b47ae4",
      "incomplete_value": true,
      "site": "00b47ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47aa0",
      "incomplete_value": true,
      "site": "00b47aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b47ae8",
      "incomplete_value": true,
      "site": "00b47ae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b47aa4",
      "incomplete_value": true,
      "site": "00b47aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b47ad0",
      "READ",
      [
        "storage",
        "00c1b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b47ae4",
      "DATA",
      [
        "storage",
        "00c11258",
        null,
        "pointer"
      ]
    ],
    [
      "00b47ae8",
      "DATA",
      [
        "storage",
        "00c11280",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b47ad0",
      "READ",
      [
        "storage",
        "00c1b240",
        null,
        "pointer"
      ]
    ],
    [
      "00b47ae4",
      "DATA",
      [
        "storage",
        "00c112a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b47ae8",
      "DATA",
      [
        "storage",
        "00c112d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47a74.md#insn-00b47a8c) · [`00b47aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47a74.md#insn-00b47aa8)
- 新版 [`00b47ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47ab8.md#insn-00b47ad0) · [`00b47aec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47ab8.md#insn-00b47aec)

~~~diff
- 00b47a8c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1f0:8"]]
- 00b47a8c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47ad0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:240:8"]]
+ 00b47ad0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47a8c bytes 29f940f9
+ 00b47ad0 bytes 292141f9
- 00b47aa8 ["INT_ADD", "register:40f0:8", ["const:b47aa8:8", "const:4:8"]]
- 00b47aa8 ["CALL", null, ["callee:00be02a0:8"]]
+ 00b47aec ["INT_ADD", "register:40f0:8", ["const:b47aec:8", "const:4:8"]]
+ 00b47aec ["CALL", null, ["callee:00be02a0:8"]]
- 00b47aa8 bytes ea610294
+ 00b47aec bytes ed610294
~~~


<a id="compare-e6d5362120ec5976de2c5c1b55994d56"></a>

### [`00b47b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47b04.md) → [`00b47b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47b48.md) FUN_00b47b48

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md) [`00be0250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0250.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md) [`00be02a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b47b78",
      "incomplete_value": true,
      "site": "00b47b78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47b34",
      "incomplete_value": true,
      "site": "00b47b34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "00b47b7c",
      "incomplete_value": true,
      "site": "00b47b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b47b38",
      "incomplete_value": true,
      "site": "00b47b38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b47b60",
      "READ",
      [
        "storage",
        "00c1b1f0",
        null,
        "pointer"
      ]
    ],
    [
      "00b47b78",
      "DATA",
      [
        "storage",
        "00c11258",
        null,
        "pointer"
      ]
    ],
    [
      "00b47b7c",
      "DATA",
      [
        "storage",
        "00c11280",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b47b60",
      "READ",
      [
        "storage",
        "00c1b240",
        null,
        "pointer"
      ]
    ],
    [
      "00b47b78",
      "DATA",
      [
        "storage",
        "00c112a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b47b7c",
      "DATA",
      [
        "storage",
        "00c112d0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47b04.md#insn-00b47b1c) · [`00b47b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47b04.md#insn-00b47b3c) · [`00b47b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b47/00b47b04.md#insn-00b47b44)
- 新版 [`00b47b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47b48.md#insn-00b47b60) · [`00b47b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47b48.md#insn-00b47b80) · [`00b47b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b47/00b47b48.md#insn-00b47b88)

~~~diff
- 00b47b1c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:1f0:8"]]
- 00b47b1c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47b60 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:240:8"]]
+ 00b47b60 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47b1c bytes 29f940f9
+ 00b47b60 bytes 292141f9
- 00b47b3c ["INT_ADD", "register:40f0:8", ["const:b47b3c:8", "const:4:8"]]
- 00b47b3c ["CALL", null, ["callee:00be02a0:8"]]
+ 00b47b80 ["INT_ADD", "register:40f0:8", ["const:b47b80:8", "const:4:8"]]
+ 00b47b80 ["CALL", null, ["callee:00be02a0:8"]]
- 00b47b3c bytes c5610294
+ 00b47b80 bytes c8610294
- 00b47b44 ["INT_ADD", "register:40f0:8", ["const:b47b44:8", "const:4:8"]]
- 00b47b44 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b47b88 ["INT_ADD", "register:40f0:8", ["const:b47b88:8", "const:4:8"]]
+ 00b47b88 ["CALL", null, ["callee:00be01e0:8"]]
- 00b47b44 bytes 93610294
+ 00b47b88 bytes 96610294
~~~


<a id="compare-2430963a00c5150461e18a2a05d9b3fc"></a>

### [`00b48640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48640.md) → [`00b48684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48684.md) FUN_00b48684

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 77.42% / 新版 77.42%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b486c4",
      "incomplete_value": true,
      "site": "00b486c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b48680",
      "incomplete_value": true,
      "site": "00b48684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b486e4",
      "incomplete_value": true,
      "site": "00b486e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b486a0",
      "incomplete_value": true,
      "site": "00b486a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b4869c",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "00b486b0",
      "DATA",
      [
        "storage",
        "00c113a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b486b4",
      "DATA",
      [
        "storage",
        "00c113d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b4869c",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "00b486b0",
      "DATA",
      [
        "storage",
        "00c113f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b486b4",
      "DATA",
      [
        "storage",
        "00c11420",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48640.md#insn-00b48658) · [`00b4867c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48640.md#insn-00b4867c) · [`00b48690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48640.md#insn-00b48690)
- 新版 [`00b4869c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48684.md#insn-00b4869c) · [`00b486c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48684.md#insn-00b486c0) · [`00b486d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48684.md#insn-00b486d4)

~~~diff
- 00b48658 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e48:8"]]
- 00b48658 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4869c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e98:8"]]
+ 00b4869c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48658 bytes 292547f9
+ 00b4869c bytes 294d47f9
- 00b4867c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d80:8"]]
- 00b4867c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b486c0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd0:8"]]
+ 00b486c0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4867c bytes 29c146f9
+ 00b486c0 bytes 29e946f9
- 00b48690 ["INT_ADD", "register:40f0:8", ["const:b48690:8", "const:4:8"]]
- 00b48690 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b486d4 ["INT_ADD", "register:40f0:8", ["const:b486d4:8", "const:4:8"]]
+ 00b486d4 ["CALL", null, ["callee:00bdb060:8"]]
- 00b48690 bytes 604a0294
+ 00b486d4 bytes 634a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfadcabb883191559fd7d4ce05f71f60"></a>

### [`00b48730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48730.md) → [`00b48774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48774.md) FUN_00b48774

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 75.86% / 新版 75.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b48798",
      "incomplete_value": true,
      "site": "00b487a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b48754",
      "incomplete_value": true,
      "site": "00b4875c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b487c4",
      "incomplete_value": true,
      "site": "00b487c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b48780",
      "incomplete_value": true,
      "site": "00b48784",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b48784",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "00b4878c",
      "READ",
      [
        "storage",
        "00c1ad80",
        null,
        "pointer"
      ]
    ],
    [
      "00b487a0",
      "DATA",
      [
        "storage",
        "00c113d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b48784",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "00b4878c",
      "READ",
      [
        "storage",
        "00c1add0",
        null,
        "pointer"
      ]
    ],
    [
      "00b487a0",
      "DATA",
      [
        "storage",
        "00c11420",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48730.md#insn-00b48740) · [`00b48748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48730.md#insn-00b48748) · [`00b48770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48730.md#insn-00b48770)
- 新版 [`00b48784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48774.md#insn-00b48784) · [`00b4878c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48774.md#insn-00b4878c) · [`00b487b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48774.md#insn-00b487b4)

~~~diff
- 00b48740 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e48:8"]]
- 00b48740 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48784 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:e98:8"]]
+ 00b48784 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48740 bytes 082547f9
+ 00b48784 bytes 084d47f9
- 00b48748 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d80:8"]]
- 00b48748 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4878c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd0:8"]]
+ 00b4878c ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48748 bytes 29c146f9
+ 00b4878c bytes 29e946f9
- 00b48770 ["INT_ADD", "register:40f0:8", ["const:b48770:8", "const:4:8"]]
- 00b48770 ["CALL", null, ["callee:00bdb060:8"]]
+ 00b487b4 ["INT_ADD", "register:40f0:8", ["const:b487b4:8", "const:4:8"]]
+ 00b487b4 ["CALL", null, ["callee:00bdb060:8"]]
- 00b48770 bytes 284a0294
+ 00b487b4 bytes 2b4a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5cdb0b19b76bb05a3524772000481cc"></a>

### [`00b487a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b487a4.md) → [`00b487e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b487e8.md) FUN_00b487e8

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb3f0.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb440.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 78.79% / 新版 78.79%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

アドレスに依存する影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b48808",
      "incomplete_value": true,
      "site": "00b48814",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b487c4",
      "incomplete_value": true,
      "site": "00b487d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "00b48818",
      "incomplete_value": true,
      "site": "00b48818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b487d4",
      "incomplete_value": true,
      "site": "00b487d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
    "ordinal": 5,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b48848",
      "incomplete_value": true,
      "site": "00b4884c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b48804",
      "incomplete_value": true,
      "site": "00b48808",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b48800",
      "READ",
      [
        "storage",
        "00c1ae48",
        null,
        "pointer"
      ]
    ],
    [
      "00b48814",
      "DATA",
      [
        "storage",
        "00c113a8",
        null,
        "pointer"
      ]
    ],
    [
      "00b48818",
      "DATA",
      [
        "storage",
        "00c113d0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b48800",
      "READ",
      [
        "storage",
        "00c1ae98",
        null,
        "pointer"
      ]
    ],
    [
      "00b48814",
      "DATA",
      [
        "storage",
        "00c113f8",
        null,
        "pointer"
      ]
    ],
    [
      "00b48818",
      "DATA",
      [
        "storage",
        "00c11420",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48814`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b487a4.md#insn-00b48814) · [`00b487bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b487a4.md#insn-00b487bc) · [`00b487e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b487a4.md#insn-00b487e0)
- 新版 [`00b48858`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b487e8.md#insn-00b48858) · [`00b48800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b487e8.md#insn-00b48800) · [`00b48824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b487e8.md#insn-00b48824)

~~~diff
- 00b48814 ["INT_ADD", "register:40f0:8", ["const:b48814:8", "const:4:8"]]
- 00b48814 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b48858 ["INT_ADD", "register:40f0:8", ["const:b48858:8", "const:4:8"]]
+ 00b48858 ["CALL", null, ["callee:00be01e0:8"]]
- 00b48814 bytes 5f5e0294
+ 00b48858 bytes 625e0294
- 00b487bc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e48:8"]]
- 00b487bc ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48800 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:e98:8"]]
+ 00b48800 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b487bc bytes 292547f9
+ 00b48800 bytes 294d47f9
- 00b487e0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d80:8"]]
- 00b487e0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48824 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:dd0:8"]]
+ 00b48824 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b487e0 bytes 29c146f9
+ 00b48824 bytes 29e946f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e23b1f8dbc18cfd0ed89d08b28d4520"></a>

### [`00b48828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48828.md) → [`00b4886c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b4886c.md) FUN_00b4886c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md) [`00be0250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0250.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md) [`00be02a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 72.22% / 新版 72.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b48898",
      "incomplete_value": true,
      "site": "00b48898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48854",
      "incomplete_value": true,
      "site": "00b48854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b4889c",
      "incomplete_value": true,
      "site": "00b4889c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b48858",
      "incomplete_value": true,
      "site": "00b48858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b48884",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "00b48898",
      "DATA",
      [
        "storage",
        "00c11460",
        null,
        "pointer"
      ]
    ],
    [
      "00b4889c",
      "DATA",
      [
        "storage",
        "00c11488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b48884",
      "READ",
      [
        "storage",
        "00c1b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b48898",
      "DATA",
      [
        "storage",
        "00c114b0",
        null,
        "pointer"
      ]
    ],
    [
      "00b4889c",
      "DATA",
      [
        "storage",
        "00c114d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48828.md#insn-00b48840) · [`00b4885c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48828.md#insn-00b4885c)
- 新版 [`00b48884`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b4886c.md#insn-00b48884) · [`00b488a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b4886c.md#insn-00b488a0)

~~~diff
- 00b48840 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
- 00b48840 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48884 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d0:8"]]
+ 00b48884 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48840 bytes 294140f9
+ 00b48884 bytes 296940f9
- 00b4885c ["INT_ADD", "register:40f0:8", ["const:b4885c:8", "const:4:8"]]
- 00b4885c ["CALL", null, ["callee:00be02a0:8"]]
+ 00b488a0 ["INT_ADD", "register:40f0:8", ["const:b488a0:8", "const:4:8"]]
+ 00b488a0 ["CALL", null, ["callee:00be02a0:8"]]
- 00b4885c bytes 7d5e0294
+ 00b488a0 bytes 805e0294
~~~


<a id="compare-594c66ecdbfdb6738db41e46ff25a4f5"></a>

### [`00b488b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b488b8.md) → [`00b488fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b488fc.md) FUN_00b488fc

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00be0190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0190.md) [`00be0250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0250.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00be01e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be01e0.md) [`00be02a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be02a0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 76.19% / 新版 76.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b4892c",
      "incomplete_value": true,
      "site": "00b4892c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b488e8",
      "incomplete_value": true,
      "site": "00b488e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:18:8"
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
      "definition_site": "00b48930",
      "incomplete_value": true,
      "site": "00b48930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b488ec",
      "incomplete_value": true,
      "site": "00b488ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b48914",
      "READ",
      [
        "storage",
        "00c1b080",
        null,
        "pointer"
      ]
    ],
    [
      "00b4892c",
      "DATA",
      [
        "storage",
        "00c11460",
        null,
        "pointer"
      ]
    ],
    [
      "00b48930",
      "DATA",
      [
        "storage",
        "00c11488",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b48914",
      "READ",
      [
        "storage",
        "00c1b0d0",
        null,
        "pointer"
      ]
    ],
    [
      "00b4892c",
      "DATA",
      [
        "storage",
        "00c114b0",
        null,
        "pointer"
      ]
    ],
    [
      "00b48930",
      "DATA",
      [
        "storage",
        "00c114d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b488d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b488b8.md#insn-00b488d0) · [`00b488f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b488b8.md#insn-00b488f0) · [`00b488f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b488b8.md#insn-00b488f8)
- 新版 [`00b48914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b488fc.md#insn-00b48914) · [`00b48934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b488fc.md#insn-00b48934) · [`00b4893c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b488fc.md#insn-00b4893c)

~~~diff
- 00b488d0 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:80:8"]]
- 00b488d0 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48914 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d0:8"]]
+ 00b48914 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b488d0 bytes 294140f9
+ 00b48914 bytes 296940f9
- 00b488f0 ["INT_ADD", "register:40f0:8", ["const:b488f0:8", "const:4:8"]]
- 00b488f0 ["CALL", null, ["callee:00be02a0:8"]]
+ 00b48934 ["INT_ADD", "register:40f0:8", ["const:b48934:8", "const:4:8"]]
+ 00b48934 ["CALL", null, ["callee:00be02a0:8"]]
- 00b488f0 bytes 585e0294
+ 00b48934 bytes 5b5e0294
- 00b488f8 ["INT_ADD", "register:40f0:8", ["const:b488f8:8", "const:4:8"]]
- 00b488f8 ["CALL", null, ["callee:00be01e0:8"]]
+ 00b4893c ["INT_ADD", "register:40f0:8", ["const:b4893c:8", "const:4:8"]]
+ 00b4893c ["CALL", null, ["callee:00be01e0:8"]]
- 00b488f8 bytes 265e0294
+ 00b4893c bytes 295e0294
~~~


<a id="compare-5e42445893c331de6af9bd0f1c108902"></a>

### [`00b48c44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c44.md) → [`00b48c88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c88.md) _ZN8firebase9messaging11SetListenerEPNS0_8ListenerE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be02f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be02f0.md) · 呼出先 5件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00be0340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0340.md)
- 新版 呼出元 1件 [`00be0340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0340.md) · 呼出先 5件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00be0390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0390.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 80.70% / 新版 80.70%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48cd0",
      "incomplete_value": true,
      "site": "00b48cd0",
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
      "definition_site": "00b48c8c",
      "incomplete_value": true,
      "site": "00b48c8c",
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
    "ordinal": 9,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48cd4",
      "incomplete_value": true,
      "site": "00b48cd4",
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
            "const:f88:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48c90",
      "incomplete_value": true,
      "site": "00b48c90",
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
            "const:f48:8"
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
      "definition_site": "00b48d14",
      "incomplete_value": true,
      "site": "00b48d14",
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
            "const:f98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48cd0",
      "incomplete_value": true,
      "site": "00b48cd0",
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
            "const:f58:8"
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
      "00b48ca0",
      "PARAM",
      [
        "storage",
        "010a0f20",
        null,
        null
      ]
    ],
    [
      "00b48cb0",
      "READ",
      [
        "storage",
        "010a0f48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48cb4",
      "READ",
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
      "00b48ca0",
      "PARAM",
      [
        "storage",
        "010a0f60",
        null,
        null
      ]
    ],
    [
      "00b48cb0",
      "READ",
      [
        "storage",
        "010a0f88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48cb4",
      "READ",
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

- 旧版 [`00b48c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c44.md#insn-00b48c8c) · [`00b48c90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c44.md#insn-00b48c90) · [`00b48ccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b48/00b48c44.md#insn-00b48ccc)
- 新版 [`00b48cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c88.md#insn-00b48cd0) · [`00b48cd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c88.md#insn-00b48cd4) · [`00b48d10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b48/00b48c88.md#insn-00b48d10)

~~~diff
- 00b48c8c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f50:8"]]
- 00b48c8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48cd0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:f90:8"]]
+ 00b48cd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48c8c bytes a0aa07f9
+ 00b48cd0 bytes a0ca07f9
- 00b48c90 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:f48:8"]]
- 00b48c90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
+ 00b48cd4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:f88:8"]]
+ 00b48cd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:40a0:8"]]
- 00b48c90 bytes d4a607f9
+ 00b48cd4 bytes d4c607f9
- 00b48ccc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48ccc ["INT_ADD", "register:40f0:8", ["const:b48ccc:8", "const:4:8"]]
- 00b48ccc ["CALLIND", null, ["register:0:8"]]
+ 00b48d10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48d10 ["INT_ADD", "register:40f0:8", ["const:b48d10:8", "const:4:8"]]
+ 00b48d10 ["CALLIND", null, ["register:0:8"]]
- 00b48ccc bytes 00013fd6
+ 00b48d10 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

