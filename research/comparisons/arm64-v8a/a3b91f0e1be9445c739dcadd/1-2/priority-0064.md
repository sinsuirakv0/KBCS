# v15.7.3 → v15.7.4 · 最優先の変更候補 (64)

[一覧の目次](README.md)

<a id="compare-b7d577a9b44a4bb6242b30dca28ad3f0"></a>

### [`00aea998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea998.md) → [`00aea9dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea9dc.md) _ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aeaa0c",
      "incomplete_value": true,
      "site": "00aeaa0c",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea9c8",
      "incomplete_value": true,
      "site": "00aea9c8",
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
            "const:7e8:8"
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
      "definition_site": "00aea9f0",
      "incomplete_value": true,
      "site": "00aea9f0",
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
      "definition_site": "00aea9ac",
      "incomplete_value": true,
      "site": "00aea9ac",
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
      "definition_site": "00aea9f8",
      "incomplete_value": false,
      "site": "00aeaa04",
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
            "const:654:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aea9b4",
      "incomplete_value": false,
      "site": "00aea9c0",
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
            "const:6e1:8"
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
      "00aea9ec",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea9f8",
      "PARAM",
      [
        "storage",
        "002996e1",
        null,
        "string"
      ]
    ],
    [
      "00aeaa0c",
      "WRITE",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aea9ec",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "00aea9f8",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ],
    [
      "00aeaa0c",
      "WRITE",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aea9c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea998.md#insn-00aea9c0) · [`00aea9c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea998.md#insn-00aea9c8) · [`00aea9a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea998.md#insn-00aea9a8)
- 新版 [`00aeaa04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea9dc.md#insn-00aeaa04) · [`00aeaa0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea9dc.md#insn-00aeaa0c) · [`00aea9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aea9dc.md#insn-00aea9ec)

~~~diff
- 00aea9c0 ["INT_ADD", "register:40f0:8", ["const:aea9c0:8", "const:4:8"]]
- 00aea9c0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeaa04 ["INT_ADD", "register:40f0:8", ["const:aeaa04:8", "const:4:8"]]
+ 00aeaa04 ["CALL", null, ["callee:00bde090:8"]]
- 00aea9c0 bytes a0cd0394
+ 00aeaa04 bytes a3cd0394
- 00aea9c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
- 00aea9c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeaa0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
+ 00aeaa0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aea9c8 bytes 60f603f9
+ 00aeaa0c bytes 601604f9
- 00aea9a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
- 00aea9a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aea9ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
+ 00aea9ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aea9a8 bytes 68f643f9
+ 00aea9ec bytes 681644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b369bc3b780d59169bdcd4a4ba9f4a34"></a>

### [`00aea9e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea9e8.md) → [`00aeaa2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaa2c.md) _ZN8firebase4util11float_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeaab4",
      "incomplete_value": true,
      "site": "00aeaab4",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaa70",
      "incomplete_value": true,
      "site": "00aeaa70",
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
            "const:7f0:8"
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
      "definition_site": "00aeaa60",
      "incomplete_value": true,
      "site": "00aeaa6c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:828:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaa1c",
      "incomplete_value": true,
      "site": "00aeaa28",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e8:8"
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
      "00aeaa40",
      "READ",
      [
        "storage",
        "010a07f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeaa60",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeaab4",
      "WRITE",
      [
        "storage",
        "010a07f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeaa40",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeaa60",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeaab4",
      "WRITE",
      [
        "storage",
        "010a0830",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaa28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea9e8.md#insn-00aeaa28) · [`00aeaa70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea9e8.md#insn-00aeaa70) · [`00aea9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aea9e8.md#insn-00aea9fc)
- 新版 [`00aeaa6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaa2c.md#insn-00aeaa6c) · [`00aeaab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaa2c.md#insn-00aeaab4) · [`00aeaa40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaa2c.md#insn-00aeaa40)

~~~diff
- 00aeaa28 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeaa28 ["INT_ADD", "register:40f0:8", ["const:aeaa28:8", "const:4:8"]]
- 00aeaa28 ["CALLIND", null, ["register:0:8"]]
+ 00aeaa6c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aeaa6c ["INT_ADD", "register:40f0:8", ["const:aeaa6c:8", "const:4:8"]]
+ 00aeaa6c ["CALLIND", null, ["register:0:8"]]
- 00aeaa28 bytes 00013fd6
+ 00aeaa6c bytes 00013fd6
- 00aeaa70 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aeaa70 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7f0:8"]]
- 00aeaa70 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aeaab4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aeaab4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:830:8"]]
+ 00aeaab4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aeaa70 bytes a0c21f39
+ 00aeaab4 bytes a0c22039
- 00aea9fc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7f0:8"]]
- 00aea9fc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aea9fc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aeaa40 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:830:8"]]
+ 00aeaa40 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aeaa40 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aea9fc bytes a8c25f39
+ 00aeaa40 bytes a8c26039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-431845c8432e70b62db6d4ea3d8d1f3e"></a>

### [`00aeaa84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaa84.md) → [`00aeaac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaac8.md) _ZN8firebase4util11float_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00aeab04",
      "incomplete_value": true,
      "site": "00aeab04",
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
            "const:830:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaac0",
      "incomplete_value": true,
      "site": "00aeaac0",
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
            "const:7f0:8"
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
      "definition_site": "00aeab54",
      "incomplete_value": true,
      "site": "00aeab54",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeab10",
      "incomplete_value": true,
      "site": "00aeab10",
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
            "const:7e8:8"
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
      "definition_site": "00aeaae0",
      "incomplete_value": true,
      "site": "00aeaae0",
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
      "definition_site": "00aeaa9c",
      "incomplete_value": true,
      "site": "00aeaa9c",
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
      "00aeaadc",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeaae8",
      "READ",
      [
        "storage",
        "010a07f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeab04",
      "WRITE",
      [
        "storage",
        "010a07f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeaadc",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeaae8",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeab04",
      "WRITE",
      [
        "storage",
        "010a0830",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaa84.md#insn-00aeaac0) · [`00aeab0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaa84.md#insn-00aeab0c) · [`00aeab10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaa84.md#insn-00aeab10)
- 新版 [`00aeab04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaac8.md#insn-00aeab04) · [`00aeab50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaac8.md#insn-00aeab50) · [`00aeab54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaac8.md#insn-00aeab54)

~~~diff
- 00aeaac0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeaac0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeaac0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7f0:8"]]
- 00aeaac0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aeab04 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aeab04 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aeab04 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:830:8"]]
+ 00aeab04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeaac0 bytes bfc21f39
+ 00aeab04 bytes bfc22039
- 00aeab0c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeab0c ["INT_ADD", "register:40f0:8", ["const:aeab0c:8", "const:4:8"]]
- 00aeab0c ["CALLIND", null, ["register:0:8"]]
+ 00aeab50 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aeab50 ["INT_ADD", "register:40f0:8", ["const:aeab50:8", "const:4:8"]]
+ 00aeab50 ["CALLIND", null, ["register:0:8"]]
- 00aeab0c bytes 00013fd6
+ 00aeab50 bytes 00013fd6
- 00aeab10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e8:8"]]
- 00aeab10 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aeab10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aeab54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
+ 00aeab54 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aeab54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aeab10 bytes 9ff603f9
+ 00aeab54 bytes 9f1604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d71bf02916fdcb4fe93afd473c06aca0"></a>

### [`00aeab24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeab24.md) → [`00aeab68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeab68.md) _ZN8firebase4util11float_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aeaba8",
      "incomplete_value": true,
      "site": "00aeaba8",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeab64",
      "incomplete_value": true,
      "site": "00aeab64",
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
            "const:7e8:8"
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
      "definition_site": "00aeab84",
      "incomplete_value": true,
      "site": "00aeab84",
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
      "definition_site": "00aeab40",
      "incomplete_value": true,
      "site": "00aeab40",
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
      "definition_site": "00aeab8c",
      "incomplete_value": false,
      "site": "00aeaba0",
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
            "const:654:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeab48",
      "incomplete_value": false,
      "site": "00aeab5c",
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
            "const:6e1:8"
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
      "00aeab7c",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeab8c",
      "PARAM",
      [
        "storage",
        "002996e1",
        null,
        "string"
      ]
    ],
    [
      "00aeaba8",
      "WRITE",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeab7c",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeab8c",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ],
    [
      "00aeaba8",
      "WRITE",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeab5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeab24.md#insn-00aeab5c) · [`00aeab64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeab24.md#insn-00aeab64) · [`00aeab38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeab24.md#insn-00aeab38)
- 新版 [`00aeaba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeab68.md#insn-00aeaba0) · [`00aeaba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeab68.md#insn-00aeaba8) · [`00aeab7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeab68.md#insn-00aeab7c)

~~~diff
- 00aeab5c ["INT_ADD", "register:40f0:8", ["const:aeab5c:8", "const:4:8"]]
- 00aeab5c ["CALL", null, ["callee:00bde090:8"]]
+ 00aeaba0 ["INT_ADD", "register:40f0:8", ["const:aeaba0:8", "const:4:8"]]
+ 00aeaba0 ["CALL", null, ["callee:00bde090:8"]]
- 00aeab5c bytes 39cd0394
+ 00aeaba0 bytes 3ccd0394
- 00aeab64 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e8:8"]]
- 00aeab64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeaba8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
+ 00aeaba8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeab64 bytes 80f603f9
+ 00aeaba8 bytes 801604f9
- 00aeab38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e8:8"]]
- 00aeab38 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeab7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
+ 00aeab7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeab38 bytes 81f643f9
+ 00aeab7c bytes 811644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ced74339ad7f596cfafeffbdaa8d306d"></a>

### [`00aeab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeab94.md) → [`00aeabd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeabd8.md) _ZN8firebase4util11float_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00aeabf4",
      "incomplete_value": false,
      "site": "00aeabf8",
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
      "definition_site": "00aeabb0",
      "incomplete_value": false,
      "site": "00aeabb4",
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
      "definition_site": "00aeac04",
      "incomplete_value": true,
      "site": "00aeac10",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeabc0",
      "incomplete_value": true,
      "site": "00aeabcc",
      "value": [
        "LOAD",
        "8",
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
      "00aeabf4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aeac04",
      "DATA",
      [
        "storage",
        "010a07f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeabf4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aeac04",
      "DATA",
      [
        "storage",
        "010a0838",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeabb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeab94.md#insn-00aeabb4) · [`00aeabb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeab94.md#insn-00aeabb0) · [`00aeabbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeab94.md#insn-00aeabbc)
- 新版 [`00aeabf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeabd8.md#insn-00aeabf8) · [`00aeabf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeabd8.md#insn-00aeabf4) · [`00aeac00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeabd8.md#insn-00aeac00)

~~~diff
- 00aeabb4 ["INT_ADD", "register:40f0:8", ["const:aeabb4:8", "const:4:8"]]
- 00aeabb4 ["CALL", null, ["callee:00bde180:8"]]
+ 00aeabf8 ["INT_ADD", "register:40f0:8", ["const:aeabf8:8", "const:4:8"]]
+ 00aeabf8 ["CALL", null, ["callee:00bde180:8"]]
- 00aeabb4 bytes 5fcd0394
+ 00aeabf8 bytes 62cd0394
- 00aeabb0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aeabb0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeabb0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeabb0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeabf4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aeabf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeabf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeabf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeabb0 bytes 00501791
+ 00aeabf4 bytes 001c1591
- 00aeabbc ["COPY", "tmp:0:8", ["const:7f8:8"]]
- 00aeabbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeabbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeabbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeac00 ["COPY", "tmp:0:8", ["const:838:8"]]
+ 00aeac00 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeac00 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeac00 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeabbc bytes 08e11f91
+ 00aeac00 bytes 08e12091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5cca57145c89ec5d20848c4424e1400"></a>

### [`00aeabd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeabd0.md) → [`00aeac14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac14.md) _ZN8firebase4util11float_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aeac54",
      "incomplete_value": true,
      "site": "00aeac54",
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
            "const:828:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeac10",
      "incomplete_value": true,
      "site": "00aeac10",
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
            "const:7e8:8"
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
      "definition_site": "00aeac30",
      "incomplete_value": true,
      "site": "00aeac30",
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
      "definition_site": "00aeabec",
      "incomplete_value": true,
      "site": "00aeabec",
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
      "definition_site": "00aeac38",
      "incomplete_value": false,
      "site": "00aeac4c",
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
            "const:654:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeabf4",
      "incomplete_value": false,
      "site": "00aeac08",
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
            "const:6e1:8"
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
      "00aeac28",
      "READ",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeac38",
      "PARAM",
      [
        "storage",
        "002996e1",
        null,
        "string"
      ]
    ],
    [
      "00aeac54",
      "WRITE",
      [
        "storage",
        "010a07e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeac28",
      "READ",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeac38",
      "PARAM",
      [
        "storage",
        "00299654",
        null,
        "string"
      ]
    ],
    [
      "00aeac54",
      "WRITE",
      [
        "storage",
        "010a0828",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeac08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeabd0.md#insn-00aeac08) · [`00aeac10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeabd0.md#insn-00aeac10) · [`00aeabe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeabd0.md#insn-00aeabe4)
- 新版 [`00aeac4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac14.md#insn-00aeac4c) · [`00aeac54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac14.md#insn-00aeac54) · [`00aeac28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac14.md#insn-00aeac28)

~~~diff
- 00aeac08 ["INT_ADD", "register:40f0:8", ["const:aeac08:8", "const:4:8"]]
- 00aeac08 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeac4c ["INT_ADD", "register:40f0:8", ["const:aeac4c:8", "const:4:8"]]
+ 00aeac4c ["CALL", null, ["callee:00bde090:8"]]
- 00aeac08 bytes 0ecd0394
+ 00aeac4c bytes 11cd0394
- 00aeac10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e8:8"]]
- 00aeac10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeac54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
+ 00aeac54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeac10 bytes 80f603f9
+ 00aeac54 bytes 801604f9
- 00aeabe4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e8:8"]]
- 00aeabe4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeac28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
+ 00aeac28 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeabe4 bytes 81f643f9
+ 00aeac28 bytes 811644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb6f212e592039a5ab2c74341d7d964d"></a>

### [`00aeac40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeac40.md) → [`00aeac84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac84.md) _ZN8firebase4util11float_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aeaca0",
      "incomplete_value": false,
      "site": "00aeaca4",
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
      "definition_site": "00aeac5c",
      "incomplete_value": false,
      "site": "00aeac60",
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
      "definition_site": "00aeacb0",
      "incomplete_value": true,
      "site": "00aeacbc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeac6c",
      "incomplete_value": true,
      "site": "00aeac78",
      "value": [
        "LOAD",
        "8",
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
      "00aeaca0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aeacb0",
      "DATA",
      [
        "storage",
        "010a0808",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeaca0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aeacb0",
      "DATA",
      [
        "storage",
        "010a0848",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeac60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeac40.md#insn-00aeac60) · [`00aeac5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeac40.md#insn-00aeac5c) · [`00aeac68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeac40.md#insn-00aeac68)
- 新版 [`00aeaca4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac84.md#insn-00aeaca4) · [`00aeaca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac84.md#insn-00aeaca0) · [`00aeacac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeac84.md#insn-00aeacac)

~~~diff
- 00aeac60 ["INT_ADD", "register:40f0:8", ["const:aeac60:8", "const:4:8"]]
- 00aeac60 ["CALL", null, ["callee:00bde180:8"]]
+ 00aeaca4 ["INT_ADD", "register:40f0:8", ["const:aeaca4:8", "const:4:8"]]
+ 00aeaca4 ["CALL", null, ["callee:00bde180:8"]]
- 00aeac60 bytes 34cd0394
+ 00aeaca4 bytes 37cd0394
- 00aeac5c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aeac5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeac5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeac5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeaca0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aeaca0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeaca0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeaca0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeac5c bytes 00fc1991
+ 00aeaca0 bytes 00c81791
- 00aeac68 ["COPY", "tmp:0:8", ["const:808:8"]]
- 00aeac68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeac68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeac68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeacac ["COPY", "tmp:0:8", ["const:848:8"]]
+ 00aeacac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeacac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeacac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeac68 bytes 08212091
+ 00aeacac bytes 08212191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b92b0169bbc66d218e74754acb25e88"></a>

### [`00aeac7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeac7c.md) → [`00aeacc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeacc0.md) _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

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
      "definition_site": "00aeacec",
      "incomplete_value": true,
      "site": "00aeacec",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaca8",
      "incomplete_value": true,
      "site": "00aeaca8",
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
            "const:810:8"
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
      "definition_site": "00aeacd4",
      "incomplete_value": true,
      "site": "00aeacd4",
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
      "definition_site": "00aeac90",
      "incomplete_value": true,
      "site": "00aeac90",
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
      "definition_site": "00aeace0",
      "incomplete_value": false,
      "site": "00aeace4",
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
            "const:bd5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeac9c",
      "incomplete_value": false,
      "site": "00aeaca0",
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
            "const:c62:8"
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
      "00aeacd0",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeace0",
      "PARAM",
      [
        "storage",
        "00296c62",
        null,
        "string"
      ]
    ],
    [
      "00aeacec",
      "WRITE",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeacd0",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeace0",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00aeacec",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaca0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeac7c.md#insn-00aeaca0) · [`00aeaca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeac7c.md#insn-00aeaca8) · [`00aeac8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeac7c.md#insn-00aeac8c)
- 新版 [`00aeace4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeacc0.md#insn-00aeace4) · [`00aeacec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeacc0.md#insn-00aeacec) · [`00aeacd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeacc0.md#insn-00aeacd0)

~~~diff
- 00aeaca0 ["INT_ADD", "register:40f0:8", ["const:aeaca0:8", "const:4:8"]]
- 00aeaca0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeace4 ["INT_ADD", "register:40f0:8", ["const:aeace4:8", "const:4:8"]]
+ 00aeace4 ["CALL", null, ["callee:00bde090:8"]]
- 00aeaca0 bytes e8cc0394
+ 00aeace4 bytes ebcc0394
- 00aeaca8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00aeaca8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeacec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00aeacec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeaca8 bytes 600a04f9
+ 00aeacec bytes 602a04f9
- 00aeac8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00aeac8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeacd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00aeacd0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeac8c bytes 680a44f9
+ 00aeacd0 bytes 682a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-986753b0c1736eda803b3e836e9fbe88"></a>

### [`00aeacbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeacbc.md) → [`00aead00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead00.md) _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aead2c",
      "incomplete_value": true,
      "site": "00aead2c",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeace8",
      "incomplete_value": true,
      "site": "00aeace8",
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
            "const:810:8"
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
      "definition_site": "00aead14",
      "incomplete_value": true,
      "site": "00aead14",
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
      "definition_site": "00aeacd0",
      "incomplete_value": true,
      "site": "00aeacd0",
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
      "definition_site": "00aead1c",
      "incomplete_value": false,
      "site": "00aead24",
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
            "const:bd5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeacd8",
      "incomplete_value": false,
      "site": "00aeace0",
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
            "const:c62:8"
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
      "00aead10",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aead1c",
      "PARAM",
      [
        "storage",
        "00296c62",
        null,
        "string"
      ]
    ],
    [
      "00aead2c",
      "WRITE",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aead10",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aead1c",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00aead2c",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeace0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeacbc.md#insn-00aeace0) · [`00aeace8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeacbc.md#insn-00aeace8) · [`00aeaccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeacbc.md#insn-00aeaccc)
- 新版 [`00aead24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead00.md#insn-00aead24) · [`00aead2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead00.md#insn-00aead2c) · [`00aead10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead00.md#insn-00aead10)

~~~diff
- 00aeace0 ["INT_ADD", "register:40f0:8", ["const:aeace0:8", "const:4:8"]]
- 00aeace0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aead24 ["INT_ADD", "register:40f0:8", ["const:aead24:8", "const:4:8"]]
+ 00aead24 ["CALL", null, ["callee:00bde090:8"]]
- 00aeace0 bytes d8cc0394
+ 00aead24 bytes dbcc0394
- 00aeace8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00aeace8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aead2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00aead2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeace8 bytes 600a04f9
+ 00aead2c bytes 602a04f9
- 00aeaccc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00aeaccc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aead10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00aead10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeaccc bytes 680a44f9
+ 00aead10 bytes 682a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c2a4e77845eee3b6c1a8a3acabe00a9"></a>

### [`00aeacfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeacfc.md) → [`00aead40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead40.md) _ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00aead70",
      "incomplete_value": true,
      "site": "00aead70",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aead2c",
      "incomplete_value": true,
      "site": "00aead2c",
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
            "const:810:8"
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
      "definition_site": "00aead54",
      "incomplete_value": true,
      "site": "00aead54",
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
      "definition_site": "00aead10",
      "incomplete_value": true,
      "site": "00aead10",
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
      "definition_site": "00aead60",
      "incomplete_value": false,
      "site": "00aead68",
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
            "const:bd5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aead1c",
      "incomplete_value": false,
      "site": "00aead24",
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
            "const:c62:8"
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
      "00aead50",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aead60",
      "PARAM",
      [
        "storage",
        "00296c62",
        null,
        "string"
      ]
    ],
    [
      "00aead70",
      "WRITE",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aead50",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aead60",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00aead70",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aead24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeacfc.md#insn-00aead24) · [`00aead2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeacfc.md#insn-00aead2c) · [`00aead0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeacfc.md#insn-00aead0c)
- 新版 [`00aead68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead40.md#insn-00aead68) · [`00aead70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead40.md#insn-00aead70) · [`00aead50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead40.md#insn-00aead50)

~~~diff
- 00aead24 ["INT_ADD", "register:40f0:8", ["const:aead24:8", "const:4:8"]]
- 00aead24 ["CALL", null, ["callee:00bde090:8"]]
+ 00aead68 ["INT_ADD", "register:40f0:8", ["const:aead68:8", "const:4:8"]]
+ 00aead68 ["CALL", null, ["callee:00bde090:8"]]
- 00aead24 bytes c7cc0394
+ 00aead68 bytes cacc0394
- 00aead2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00aead2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aead70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00aead70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aead2c bytes 600a04f9
+ 00aead70 bytes 602a04f9
- 00aead0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00aead0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aead50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00aead50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aead0c bytes 680a44f9
+ 00aead50 bytes 682a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-995a2be8cf64d72f3ae2f5ccaf876e43"></a>

### [`00aead40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aead40.md) → [`00aead84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead84.md) _ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aeadb4",
      "incomplete_value": true,
      "site": "00aeadb4",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aead70",
      "incomplete_value": true,
      "site": "00aead70",
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
            "const:810:8"
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
      "definition_site": "00aead98",
      "incomplete_value": true,
      "site": "00aead98",
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
      "definition_site": "00aead54",
      "incomplete_value": true,
      "site": "00aead54",
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
      "definition_site": "00aeada0",
      "incomplete_value": false,
      "site": "00aeadac",
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
            "const:bd5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aead5c",
      "incomplete_value": false,
      "site": "00aead68",
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
            "const:c62:8"
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
      "00aead94",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeada0",
      "PARAM",
      [
        "storage",
        "00296c62",
        null,
        "string"
      ]
    ],
    [
      "00aeadb4",
      "WRITE",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aead94",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeada0",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00aeadb4",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aead68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aead40.md#insn-00aead68) · [`00aead70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aead40.md#insn-00aead70) · [`00aead50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aead40.md#insn-00aead50)
- 新版 [`00aeadac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead84.md#insn-00aeadac) · [`00aeadb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead84.md#insn-00aeadb4) · [`00aead94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aead84.md#insn-00aead94)

~~~diff
- 00aead68 ["INT_ADD", "register:40f0:8", ["const:aead68:8", "const:4:8"]]
- 00aead68 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeadac ["INT_ADD", "register:40f0:8", ["const:aeadac:8", "const:4:8"]]
+ 00aeadac ["CALL", null, ["callee:00bde090:8"]]
- 00aead68 bytes b6cc0394
+ 00aeadac bytes b9cc0394
- 00aead70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00aead70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeadb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00aeadb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aead70 bytes 600a04f9
+ 00aeadb4 bytes 602a04f9
- 00aead50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
- 00aead50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aead94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
+ 00aead94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aead50 bytes 680a44f9
+ 00aead94 bytes 682a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a889ab6a2bbc6b3ae2e898a4d06e64c7"></a>

### [`00aead90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aead90.md) → [`00aeadd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeadd4.md) _ZN8firebase4util8hash_map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeae5c",
      "incomplete_value": true,
      "site": "00aeae5c",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeae18",
      "incomplete_value": true,
      "site": "00aeae18",
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
            "const:818:8"
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
      "00aeade8",
      "READ",
      [
        "storage",
        "010a0818",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeae08",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeae5c",
      "WRITE",
      [
        "storage",
        "010a0818",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeade8",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeae08",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeae5c",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeae18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aead90.md#insn-00aeae18) · [`00aeada4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aead90.md#insn-00aeada4) · [`00aeadc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aead90.md#insn-00aeadc4)
- 新版 [`00aeae5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeadd4.md#insn-00aeae5c) · [`00aeade8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeadd4.md#insn-00aeade8) · [`00aeae08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeadd4.md#insn-00aeae08)

~~~diff
- 00aeae18 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aeae18 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:818:8"]]
- 00aeae18 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aeae5c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aeae5c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:858:8"]]
+ 00aeae5c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aeae18 bytes a0622039
+ 00aeae5c bytes a0622139
- 00aeada4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:818:8"]]
- 00aeada4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aeada4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aeade8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:858:8"]]
+ 00aeade8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aeade8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aeada4 bytes a8626039
+ 00aeade8 bytes a8626139
- 00aeadc4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:810:8"]]
- 00aeadc4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeae08 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:850:8"]]
+ 00aeae08 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeadc4 bytes 210944f9
+ 00aeae08 bytes 212944f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-908949e0a082d4f046829cb02034c5ec"></a>

### [`00aeae2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeae2c.md) → [`00aeae70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeae70.md) _ZN8firebase4util8hash_map12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00aeaeac",
      "incomplete_value": true,
      "site": "00aeaeac",
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
            "const:858:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeae68",
      "incomplete_value": true,
      "site": "00aeae68",
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
            "const:818:8"
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
      "definition_site": "00aeaefc",
      "incomplete_value": true,
      "site": "00aeaefc",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaeb8",
      "incomplete_value": true,
      "site": "00aeaeb8",
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
            "const:810:8"
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
      "definition_site": "00aeae88",
      "incomplete_value": true,
      "site": "00aeae88",
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
      "definition_site": "00aeae44",
      "incomplete_value": true,
      "site": "00aeae44",
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
      "00aeae84",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeae90",
      "READ",
      [
        "storage",
        "010a0818",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeaeac",
      "WRITE",
      [
        "storage",
        "010a0818",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeae84",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeae90",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeaeac",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeae68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeae2c.md#insn-00aeae68) · [`00aeaeb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeae2c.md#insn-00aeaeb4) · [`00aeaeb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeae2c.md#insn-00aeaeb8)
- 新版 [`00aeaeac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeae70.md#insn-00aeaeac) · [`00aeaef8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeae70.md#insn-00aeaef8) · [`00aeaefc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeae70.md#insn-00aeaefc)

~~~diff
- 00aeae68 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeae68 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeae68 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:818:8"]]
- 00aeae68 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aeaeac ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aeaeac ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aeaeac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:858:8"]]
+ 00aeaeac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeae68 bytes bf622039
+ 00aeaeac bytes bf622139
- 00aeaeb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeaeb4 ["INT_ADD", "register:40f0:8", ["const:aeaeb4:8", "const:4:8"]]
- 00aeaeb4 ["CALLIND", null, ["register:0:8"]]
+ 00aeaef8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aeaef8 ["INT_ADD", "register:40f0:8", ["const:aeaef8:8", "const:4:8"]]
+ 00aeaef8 ["CALLIND", null, ["register:0:8"]]
- 00aeaeb4 bytes 00013fd6
+ 00aeaef8 bytes 00013fd6
- 00aeaeb8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
- 00aeaeb8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aeaeb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aeaefc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00aeaefc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aeaefc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aeaeb8 bytes 9f0a04f9
+ 00aeaefc bytes 9f2a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d7a26a71f0d0f57f55856597b5a6e2e"></a>

### [`00aeaecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaecc.md) → [`00aeaf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf10.md) _ZN8firebase4util8hash_map14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aeaf50",
      "incomplete_value": true,
      "site": "00aeaf50",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaf0c",
      "incomplete_value": true,
      "site": "00aeaf0c",
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
            "const:810:8"
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
      "definition_site": "00aeaf2c",
      "incomplete_value": true,
      "site": "00aeaf2c",
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
      "definition_site": "00aeaee8",
      "incomplete_value": true,
      "site": "00aeaee8",
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
      "definition_site": "00aeaf34",
      "incomplete_value": false,
      "site": "00aeaf48",
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
            "const:bd5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaef0",
      "incomplete_value": false,
      "site": "00aeaf04",
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
            "const:c62:8"
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
      "00aeaf24",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeaf34",
      "PARAM",
      [
        "storage",
        "00296c62",
        null,
        "string"
      ]
    ],
    [
      "00aeaf50",
      "WRITE",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeaf24",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeaf34",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00aeaf50",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaf04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaecc.md#insn-00aeaf04) · [`00aeaf0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaecc.md#insn-00aeaf0c) · [`00aeaee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaecc.md#insn-00aeaee0)
- 新版 [`00aeaf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf10.md#insn-00aeaf48) · [`00aeaf50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf10.md#insn-00aeaf50) · [`00aeaf24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf10.md#insn-00aeaf24)

~~~diff
- 00aeaf04 ["INT_ADD", "register:40f0:8", ["const:aeaf04:8", "const:4:8"]]
- 00aeaf04 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeaf48 ["INT_ADD", "register:40f0:8", ["const:aeaf48:8", "const:4:8"]]
+ 00aeaf48 ["CALL", null, ["callee:00bde090:8"]]
- 00aeaf04 bytes 4fcc0394
+ 00aeaf48 bytes 52cc0394
- 00aeaf0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
- 00aeaf0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeaf50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00aeaf50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeaf0c bytes 800a04f9
+ 00aeaf50 bytes 802a04f9
- 00aeaee0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
- 00aeaee0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeaf24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00aeaf24 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeaee0 bytes 810a44f9
+ 00aeaf24 bytes 812a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ead54c341c91ac8dba6545c3094b3f8"></a>

### [`00aeaf3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaf3c.md) → [`00aeaf80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf80.md) _ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0e0.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde130.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00aeaf9c",
      "incomplete_value": false,
      "site": "00aeafa0",
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
      "definition_site": "00aeaf58",
      "incomplete_value": false,
      "site": "00aeaf5c",
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
      "definition_site": "00aeafac",
      "incomplete_value": true,
      "site": "00aeafb8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeaf68",
      "incomplete_value": true,
      "site": "00aeaf74",
      "value": [
        "LOAD",
        "8",
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
      "00aeaf9c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aeafac",
      "DATA",
      [
        "storage",
        "010a0820",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeaf9c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aeafac",
      "DATA",
      [
        "storage",
        "010a0860",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeaf5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaf3c.md#insn-00aeaf5c) · [`00aeaf58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaf3c.md#insn-00aeaf58) · [`00aeaf64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaf3c.md#insn-00aeaf64)
- 新版 [`00aeafa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf80.md#insn-00aeafa0) · [`00aeaf9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf80.md#insn-00aeaf9c) · [`00aeafa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf80.md#insn-00aeafa8)

~~~diff
- 00aeaf5c ["INT_ADD", "register:40f0:8", ["const:aeaf5c:8", "const:4:8"]]
- 00aeaf5c ["CALL", null, ["callee:00bde180:8"]]
+ 00aeafa0 ["INT_ADD", "register:40f0:8", ["const:aeafa0:8", "const:4:8"]]
+ 00aeafa0 ["CALL", null, ["callee:00bde180:8"]]
- 00aeaf5c bytes 75cc0394
+ 00aeafa0 bytes 78cc0394
- 00aeaf58 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aeaf58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeaf58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeaf58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeaf9c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aeaf9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeaf9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeaf9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeaf58 bytes 00501791
+ 00aeaf9c bytes 001c1591
- 00aeaf64 ["COPY", "tmp:0:8", ["const:820:8"]]
- 00aeaf64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeaf64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeaf64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeafa8 ["COPY", "tmp:0:8", ["const:860:8"]]
+ 00aeafa8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeafa8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeafa8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeaf64 bytes 08812091
+ 00aeafa8 bytes 08812191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c11bfd5ba25245bb5eae11e451e1798"></a>

### [`00aeaf78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaf78.md) → [`00aeafbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeafbc.md) _ZN8firebase4util8hash_map13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aeaffc",
      "incomplete_value": true,
      "site": "00aeaffc",
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
            "const:850:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeafb8",
      "incomplete_value": true,
      "site": "00aeafb8",
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
            "const:810:8"
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
      "definition_site": "00aeafd8",
      "incomplete_value": true,
      "site": "00aeafd8",
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
      "definition_site": "00aeaf94",
      "incomplete_value": true,
      "site": "00aeaf94",
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
      "definition_site": "00aeafe0",
      "incomplete_value": false,
      "site": "00aeaff4",
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
            "const:bd5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeaf9c",
      "incomplete_value": false,
      "site": "00aeafb0",
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
            "const:c62:8"
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
      "00aeafd0",
      "READ",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeafe0",
      "PARAM",
      [
        "storage",
        "00296c62",
        null,
        "string"
      ]
    ],
    [
      "00aeaffc",
      "WRITE",
      [
        "storage",
        "010a0810",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeafd0",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeafe0",
      "PARAM",
      [
        "storage",
        "00296bd5",
        null,
        "string"
      ]
    ],
    [
      "00aeaffc",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeafb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaf78.md#insn-00aeafb0) · [`00aeafb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaf78.md#insn-00aeafb8) · [`00aeaf8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaf78.md#insn-00aeaf8c)
- 新版 [`00aeaff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeafbc.md#insn-00aeaff4) · [`00aeaffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeafbc.md#insn-00aeaffc) · [`00aeafd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeafbc.md#insn-00aeafd0)

~~~diff
- 00aeafb0 ["INT_ADD", "register:40f0:8", ["const:aeafb0:8", "const:4:8"]]
- 00aeafb0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeaff4 ["INT_ADD", "register:40f0:8", ["const:aeaff4:8", "const:4:8"]]
+ 00aeaff4 ["CALL", null, ["callee:00bde090:8"]]
- 00aeafb0 bytes 24cc0394
+ 00aeaff4 bytes 27cc0394
- 00aeafb8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
- 00aeafb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeaffc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00aeaffc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeafb8 bytes 800a04f9
+ 00aeaffc bytes 802a04f9
- 00aeaf8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
- 00aeaf8c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeafd0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
+ 00aeafd0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeaf8c bytes 810a44f9
+ 00aeafd0 bytes 812a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e052fb969759d5f309a73047e29c13f"></a>

### [`00aeafe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeafe8.md) → [`00aeb02c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb02c.md) _ZN8firebase4util8hash_map10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aeb048",
      "incomplete_value": false,
      "site": "00aeb04c",
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
      "definition_site": "00aeb004",
      "incomplete_value": false,
      "site": "00aeb008",
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
      "definition_site": "00aeb058",
      "incomplete_value": true,
      "site": "00aeb064",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeb014",
      "incomplete_value": true,
      "site": "00aeb020",
      "value": [
        "LOAD",
        "8",
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
      "00aeb048",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aeb058",
      "DATA",
      [
        "storage",
        "010a0828",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeb048",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aeb058",
      "DATA",
      [
        "storage",
        "010a0868",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeafe8.md#insn-00aeb008) · [`00aeb004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeafe8.md#insn-00aeb004) · [`00aeb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeafe8.md#insn-00aeb010)
- 新版 [`00aeb04c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb02c.md#insn-00aeb04c) · [`00aeb048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb02c.md#insn-00aeb048) · [`00aeb054`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb02c.md#insn-00aeb054)

~~~diff
- 00aeb008 ["INT_ADD", "register:40f0:8", ["const:aeb008:8", "const:4:8"]]
- 00aeb008 ["CALL", null, ["callee:00bde180:8"]]
+ 00aeb04c ["INT_ADD", "register:40f0:8", ["const:aeb04c:8", "const:4:8"]]
+ 00aeb04c ["CALL", null, ["callee:00bde180:8"]]
- 00aeb008 bytes 4acc0394
+ 00aeb04c bytes 4dcc0394
- 00aeb004 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aeb004 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb004 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb004 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeb048 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aeb048 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb048 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb048 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeb004 bytes 00fc1991
+ 00aeb048 bytes 00c81791
- 00aeb010 ["COPY", "tmp:0:8", ["const:828:8"]]
- 00aeb010 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeb010 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeb010 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeb054 ["COPY", "tmp:0:8", ["const:868:8"]]
+ 00aeb054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeb010 bytes 08a12091
+ 00aeb054 bytes 08a12191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4fd573726c1847a358a821b782a74f8"></a>

### [`00aeb024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb024.md) → [`00aeb068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb068.md) _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00aeb094",
      "incomplete_value": true,
      "site": "00aeb094",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb050",
      "incomplete_value": true,
      "site": "00aeb050",
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
            "const:830:8"
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
      "definition_site": "00aeb07c",
      "incomplete_value": true,
      "site": "00aeb07c",
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
      "definition_site": "00aeb038",
      "incomplete_value": true,
      "site": "00aeb038",
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
      "definition_site": "00aeb088",
      "incomplete_value": false,
      "site": "00aeb08c",
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
            "const:612:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb044",
      "incomplete_value": false,
      "site": "00aeb048",
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
            "const:69f:8"
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
      "00aeb078",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb088",
      "PARAM",
      [
        "storage",
        "0029869f",
        null,
        "string"
      ]
    ],
    [
      "00aeb094",
      "WRITE",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb078",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb088",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00aeb094",
      "WRITE",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb024.md#insn-00aeb048) · [`00aeb050`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb024.md#insn-00aeb050) · [`00aeb034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb024.md#insn-00aeb034)
- 新版 [`00aeb08c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb068.md#insn-00aeb08c) · [`00aeb094`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb068.md#insn-00aeb094) · [`00aeb078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb068.md#insn-00aeb078)

~~~diff
- 00aeb048 ["INT_ADD", "register:40f0:8", ["const:aeb048:8", "const:4:8"]]
- 00aeb048 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb08c ["INT_ADD", "register:40f0:8", ["const:aeb08c:8", "const:4:8"]]
+ 00aeb08c ["CALL", null, ["callee:00bde090:8"]]
- 00aeb048 bytes fecb0394
+ 00aeb08c bytes 01cc0394
- 00aeb050 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00aeb050 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb094 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00aeb094 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb050 bytes 601a04f9
+ 00aeb094 bytes 603a04f9
- 00aeb034 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00aeb034 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb078 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00aeb078 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb034 bytes 681a44f9
+ 00aeb078 bytes 683a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef6243927241521d8f39f34ee5e2bea0"></a>

### [`00aeb064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb064.md) → [`00aeb0a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0a8.md) _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00aeb0d4",
      "incomplete_value": true,
      "site": "00aeb0d4",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb090",
      "incomplete_value": true,
      "site": "00aeb090",
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
            "const:830:8"
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
      "definition_site": "00aeb0bc",
      "incomplete_value": true,
      "site": "00aeb0bc",
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
      "definition_site": "00aeb078",
      "incomplete_value": true,
      "site": "00aeb078",
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
      "definition_site": "00aeb0c4",
      "incomplete_value": false,
      "site": "00aeb0cc",
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
            "const:612:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb080",
      "incomplete_value": false,
      "site": "00aeb088",
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
            "const:69f:8"
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
      "00aeb0b8",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb0c4",
      "PARAM",
      [
        "storage",
        "0029869f",
        null,
        "string"
      ]
    ],
    [
      "00aeb0d4",
      "WRITE",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb0b8",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb0c4",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00aeb0d4",
      "WRITE",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb064.md#insn-00aeb088) · [`00aeb090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb064.md#insn-00aeb090) · [`00aeb074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb064.md#insn-00aeb074)
- 新版 [`00aeb0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0a8.md#insn-00aeb0cc) · [`00aeb0d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0a8.md#insn-00aeb0d4) · [`00aeb0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0a8.md#insn-00aeb0b8)

~~~diff
- 00aeb088 ["INT_ADD", "register:40f0:8", ["const:aeb088:8", "const:4:8"]]
- 00aeb088 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb0cc ["INT_ADD", "register:40f0:8", ["const:aeb0cc:8", "const:4:8"]]
+ 00aeb0cc ["CALL", null, ["callee:00bde090:8"]]
- 00aeb088 bytes eecb0394
+ 00aeb0cc bytes f1cb0394
- 00aeb090 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00aeb090 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb0d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00aeb0d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb090 bytes 601a04f9
+ 00aeb0d4 bytes 603a04f9
- 00aeb074 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00aeb074 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb0b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00aeb0b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb074 bytes 681a44f9
+ 00aeb0b8 bytes 683a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c0f177a550c1a6577b41ce99a3d30fcc"></a>

### [`00aeb0a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb0a4.md) → [`00aeb0e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0e8.md) _ZN8firebase4util13integer_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00aeb118",
      "incomplete_value": true,
      "site": "00aeb118",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb0d4",
      "incomplete_value": true,
      "site": "00aeb0d4",
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
            "const:830:8"
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
      "definition_site": "00aeb0fc",
      "incomplete_value": true,
      "site": "00aeb0fc",
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
      "definition_site": "00aeb0b8",
      "incomplete_value": true,
      "site": "00aeb0b8",
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
      "definition_site": "00aeb108",
      "incomplete_value": false,
      "site": "00aeb110",
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
            "const:612:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb0c4",
      "incomplete_value": false,
      "site": "00aeb0cc",
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
            "const:69f:8"
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
      "00aeb0f8",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb108",
      "PARAM",
      [
        "storage",
        "0029869f",
        null,
        "string"
      ]
    ],
    [
      "00aeb118",
      "WRITE",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb0f8",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb108",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00aeb118",
      "WRITE",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb0a4.md#insn-00aeb0cc) · [`00aeb0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb0a4.md#insn-00aeb0d4) · [`00aeb0b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb0a4.md#insn-00aeb0b4)
- 新版 [`00aeb110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0e8.md#insn-00aeb110) · [`00aeb118`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0e8.md#insn-00aeb118) · [`00aeb0f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb0e8.md#insn-00aeb0f8)

~~~diff
- 00aeb0cc ["INT_ADD", "register:40f0:8", ["const:aeb0cc:8", "const:4:8"]]
- 00aeb0cc ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb110 ["INT_ADD", "register:40f0:8", ["const:aeb110:8", "const:4:8"]]
+ 00aeb110 ["CALL", null, ["callee:00bde090:8"]]
- 00aeb0cc bytes ddcb0394
+ 00aeb110 bytes e0cb0394
- 00aeb0d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00aeb0d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00aeb118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb0d4 bytes 601a04f9
+ 00aeb118 bytes 603a04f9
- 00aeb0b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00aeb0b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb0f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00aeb0f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb0b4 bytes 681a44f9
+ 00aeb0f8 bytes 683a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-131cbf60c22b7566cf66e4873d03c998"></a>

### [`00aeb0e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb0e8.md) → [`00aeb12c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb12c.md) _ZN8firebase4util13integer_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aeb15c",
      "incomplete_value": true,
      "site": "00aeb15c",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb118",
      "incomplete_value": true,
      "site": "00aeb118",
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
            "const:830:8"
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
      "definition_site": "00aeb140",
      "incomplete_value": true,
      "site": "00aeb140",
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
      "definition_site": "00aeb0fc",
      "incomplete_value": true,
      "site": "00aeb0fc",
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
      "definition_site": "00aeb148",
      "incomplete_value": false,
      "site": "00aeb154",
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
            "const:612:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb104",
      "incomplete_value": false,
      "site": "00aeb110",
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
            "const:69f:8"
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
      "00aeb13c",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb148",
      "PARAM",
      [
        "storage",
        "0029869f",
        null,
        "string"
      ]
    ],
    [
      "00aeb15c",
      "WRITE",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb13c",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb148",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00aeb15c",
      "WRITE",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb0e8.md#insn-00aeb110) · [`00aeb118`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb0e8.md#insn-00aeb118) · [`00aeb0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb0e8.md#insn-00aeb0f8)
- 新版 [`00aeb154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb12c.md#insn-00aeb154) · [`00aeb15c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb12c.md#insn-00aeb15c) · [`00aeb13c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb12c.md#insn-00aeb13c)

~~~diff
- 00aeb110 ["INT_ADD", "register:40f0:8", ["const:aeb110:8", "const:4:8"]]
- 00aeb110 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb154 ["INT_ADD", "register:40f0:8", ["const:aeb154:8", "const:4:8"]]
+ 00aeb154 ["CALL", null, ["callee:00bde090:8"]]
- 00aeb110 bytes cccb0394
+ 00aeb154 bytes cfcb0394
- 00aeb118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00aeb118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb15c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00aeb15c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb118 bytes 601a04f9
+ 00aeb15c bytes 603a04f9
- 00aeb0f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:830:8"]]
- 00aeb0f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb13c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:870:8"]]
+ 00aeb13c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb0f8 bytes 681a44f9
+ 00aeb13c bytes 683a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b17bf51dcc932dd4ad906faf23bf5c33"></a>

### [`00aeb138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb138.md) → [`00aeb17c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb17c.md) _ZN8firebase4util13integer_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeb204",
      "incomplete_value": true,
      "site": "00aeb204",
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
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb1c0",
      "incomplete_value": true,
      "site": "00aeb1c0",
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
            "const:838:8"
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
      "definition_site": "00aeb1b0",
      "incomplete_value": true,
      "site": "00aeb1bc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:870:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb16c",
      "incomplete_value": true,
      "site": "00aeb178",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:830:8"
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
      "00aeb190",
      "READ",
      [
        "storage",
        "010a0838",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb1b0",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb204",
      "WRITE",
      [
        "storage",
        "010a0838",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeb190",
      "READ",
      [
        "storage",
        "010a0878",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb1b0",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb204",
      "WRITE",
      [
        "storage",
        "010a0878",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb138.md#insn-00aeb178) · [`00aeb1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb138.md#insn-00aeb1c0) · [`00aeb14c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb138.md#insn-00aeb14c)
- 新版 [`00aeb1bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb17c.md#insn-00aeb1bc) · [`00aeb204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb17c.md#insn-00aeb204) · [`00aeb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb17c.md#insn-00aeb190)

~~~diff
- 00aeb178 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeb178 ["INT_ADD", "register:40f0:8", ["const:aeb178:8", "const:4:8"]]
- 00aeb178 ["CALLIND", null, ["register:0:8"]]
+ 00aeb1bc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aeb1bc ["INT_ADD", "register:40f0:8", ["const:aeb1bc:8", "const:4:8"]]
+ 00aeb1bc ["CALLIND", null, ["register:0:8"]]
- 00aeb178 bytes 00013fd6
+ 00aeb1bc bytes 00013fd6
- 00aeb1c0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aeb1c0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:838:8"]]
- 00aeb1c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aeb204 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aeb204 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:878:8"]]
+ 00aeb204 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aeb1c0 bytes a0e22039
+ 00aeb204 bytes a0e22139
- 00aeb14c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:838:8"]]
- 00aeb14c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aeb14c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aeb190 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:878:8"]]
+ 00aeb190 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb190 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aeb14c bytes a8e26039
+ 00aeb190 bytes a8e26139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86ea27a8b13e967013b158f3ed4eb7b8"></a>

### [`00aeb1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb1d4.md) → [`00aeb218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb218.md) _ZN8firebase4util13integer_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00aeb254",
      "incomplete_value": true,
      "site": "00aeb254",
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
            "const:878:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb210",
      "incomplete_value": true,
      "site": "00aeb210",
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
            "const:838:8"
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
      "definition_site": "00aeb2a4",
      "incomplete_value": true,
      "site": "00aeb2a4",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb260",
      "incomplete_value": true,
      "site": "00aeb260",
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
            "const:830:8"
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
      "definition_site": "00aeb230",
      "incomplete_value": true,
      "site": "00aeb230",
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
      "definition_site": "00aeb1ec",
      "incomplete_value": true,
      "site": "00aeb1ec",
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
      "00aeb22c",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb238",
      "READ",
      [
        "storage",
        "010a0838",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb254",
      "WRITE",
      [
        "storage",
        "010a0838",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeb22c",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb238",
      "READ",
      [
        "storage",
        "010a0878",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb254",
      "WRITE",
      [
        "storage",
        "010a0878",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb1d4.md#insn-00aeb210) · [`00aeb260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb1d4.md#insn-00aeb260) · [`00aeb1e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb1d4.md#insn-00aeb1e8)
- 新版 [`00aeb254`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb218.md#insn-00aeb254) · [`00aeb2a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb218.md#insn-00aeb2a4) · [`00aeb22c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb218.md#insn-00aeb22c)

~~~diff
- 00aeb210 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeb210 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeb210 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:838:8"]]
- 00aeb210 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aeb254 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aeb254 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aeb254 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:878:8"]]
+ 00aeb254 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeb210 bytes bfe22039
+ 00aeb254 bytes bfe22139
- 00aeb260 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00aeb260 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aeb260 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aeb2a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
+ 00aeb2a4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aeb2a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aeb260 bytes 9f1a04f9
+ 00aeb2a4 bytes 9f3a04f9
- 00aeb1e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00aeb1e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb22c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
+ 00aeb22c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb1e8 bytes 811a44f9
+ 00aeb22c bytes 813a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8a8d03ee57210b1dcaf713524e4a5b8"></a>

### [`00aeb274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb274.md) → [`00aeb2b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb2b8.md) _ZN8firebase4util13integer_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aeb2f8",
      "incomplete_value": true,
      "site": "00aeb2f8",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb2b4",
      "incomplete_value": true,
      "site": "00aeb2b4",
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
            "const:830:8"
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
      "definition_site": "00aeb2d4",
      "incomplete_value": true,
      "site": "00aeb2d4",
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
      "definition_site": "00aeb290",
      "incomplete_value": true,
      "site": "00aeb290",
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
        "00aeb290"
      ],
      [
        "FALL_THROUGH",
        "00aeb2d4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aeb2d4",
      "incomplete_value": true,
      "site": "00aeb2f8",
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
      "definition_site": "00aeb290",
      "incomplete_value": true,
      "site": "00aeb2b4",
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
      "00aeb2cc",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb2dc",
      "PARAM",
      [
        "storage",
        "0029869f",
        null,
        "string"
      ]
    ],
    [
      "00aeb2f8",
      "WRITE",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb2cc",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb2dc",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00aeb2f8",
      "WRITE",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb2b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb274.md#insn-00aeb2b4) · [`00aeb288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb274.md#insn-00aeb288) · [`00aeb298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb274.md#insn-00aeb298)
- 新版 [`00aeb2f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb2b8.md#insn-00aeb2f8) · [`00aeb2cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb2b8.md#insn-00aeb2cc) · [`00aeb2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb2b8.md#insn-00aeb2dc)

~~~diff
- 00aeb2b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00aeb2b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb2f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
+ 00aeb2f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb2b4 bytes 801a04f9
+ 00aeb2f8 bytes 803a04f9
- 00aeb288 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00aeb288 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb2cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
+ 00aeb2cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb288 bytes 811a44f9
+ 00aeb2cc bytes 813a44f9
- 00aeb298 ["COPY", "tmp:0:8", ["const:69f:8"]]
- 00aeb298 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00aeb298 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00aeb298 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00aeb2dc ["COPY", "tmp:0:8", ["const:612:8"]]
+ 00aeb2dc ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00aeb2dc ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00aeb2dc ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00aeb298 bytes 637c1a91
+ 00aeb2dc bytes 63481891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9346a5346b65fb12403a625692e16548"></a>

### [`00aeb2e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb2e4.md) → [`00aeb328`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb328.md) _ZN8firebase4util13integer_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00aeb344",
      "incomplete_value": false,
      "site": "00aeb348",
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
      "definition_site": "00aeb300",
      "incomplete_value": false,
      "site": "00aeb304",
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
      "definition_site": "00aeb354",
      "incomplete_value": true,
      "site": "00aeb360",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeb310",
      "incomplete_value": true,
      "site": "00aeb31c",
      "value": [
        "LOAD",
        "8",
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
      "00aeb344",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aeb354",
      "DATA",
      [
        "storage",
        "010a0840",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeb344",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aeb354",
      "DATA",
      [
        "storage",
        "010a0880",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb2e4.md#insn-00aeb304) · [`00aeb300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb2e4.md#insn-00aeb300) · [`00aeb30c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb2e4.md#insn-00aeb30c)
- 新版 [`00aeb348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb328.md#insn-00aeb348) · [`00aeb344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb328.md#insn-00aeb344) · [`00aeb350`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb328.md#insn-00aeb350)

~~~diff
- 00aeb304 ["INT_ADD", "register:40f0:8", ["const:aeb304:8", "const:4:8"]]
- 00aeb304 ["CALL", null, ["callee:00bde180:8"]]
+ 00aeb348 ["INT_ADD", "register:40f0:8", ["const:aeb348:8", "const:4:8"]]
+ 00aeb348 ["CALL", null, ["callee:00bde180:8"]]
- 00aeb304 bytes 8bcb0394
+ 00aeb348 bytes 8ecb0394
- 00aeb300 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aeb300 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb300 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb300 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeb344 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aeb344 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb344 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb344 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeb300 bytes 00501791
+ 00aeb344 bytes 001c1591
- 00aeb30c ["COPY", "tmp:0:8", ["const:840:8"]]
- 00aeb30c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeb30c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeb30c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeb350 ["COPY", "tmp:0:8", ["const:880:8"]]
+ 00aeb350 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb350 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb350 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeb30c bytes 08012191
+ 00aeb350 bytes 08012291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6eb3f0e1c5bde9aaa343dd7c220686d6"></a>

### [`00aeb320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb320.md) → [`00aeb364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb364.md) _ZN8firebase4util13integer_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aeb3a4",
      "incomplete_value": true,
      "site": "00aeb3a4",
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
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb360",
      "incomplete_value": true,
      "site": "00aeb360",
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
            "const:830:8"
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
      "definition_site": "00aeb380",
      "incomplete_value": true,
      "site": "00aeb380",
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
      "definition_site": "00aeb33c",
      "incomplete_value": true,
      "site": "00aeb33c",
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
      "definition_site": "00aeb388",
      "incomplete_value": false,
      "site": "00aeb39c",
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
            "const:612:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb344",
      "incomplete_value": false,
      "site": "00aeb358",
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
            "const:69f:8"
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
      "00aeb378",
      "READ",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb388",
      "PARAM",
      [
        "storage",
        "0029869f",
        null,
        "string"
      ]
    ],
    [
      "00aeb3a4",
      "WRITE",
      [
        "storage",
        "010a0830",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb378",
      "READ",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb388",
      "PARAM",
      [
        "storage",
        "00298612",
        null,
        "string"
      ]
    ],
    [
      "00aeb3a4",
      "WRITE",
      [
        "storage",
        "010a0870",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb320.md#insn-00aeb358) · [`00aeb360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb320.md#insn-00aeb360) · [`00aeb334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb320.md#insn-00aeb334)
- 新版 [`00aeb39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb364.md#insn-00aeb39c) · [`00aeb3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb364.md#insn-00aeb3a4) · [`00aeb378`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb364.md#insn-00aeb378)

~~~diff
- 00aeb358 ["INT_ADD", "register:40f0:8", ["const:aeb358:8", "const:4:8"]]
- 00aeb358 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb39c ["INT_ADD", "register:40f0:8", ["const:aeb39c:8", "const:4:8"]]
+ 00aeb39c ["CALL", null, ["callee:00bde090:8"]]
- 00aeb358 bytes 3acb0394
+ 00aeb39c bytes 3dcb0394
- 00aeb360 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00aeb360 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb3a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
+ 00aeb3a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb360 bytes 801a04f9
+ 00aeb3a4 bytes 803a04f9
- 00aeb334 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:830:8"]]
- 00aeb334 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb378 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:870:8"]]
+ 00aeb378 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb334 bytes 811a44f9
+ 00aeb378 bytes 813a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3efdbbad017bc5c045eae9b9994f6b4a"></a>

### [`00aeb390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb390.md) → [`00aeb3d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb3d4.md) _ZN8firebase4util13integer_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aeb3f0",
      "incomplete_value": false,
      "site": "00aeb3f4",
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
      "definition_site": "00aeb3ac",
      "incomplete_value": false,
      "site": "00aeb3b0",
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
      "definition_site": "00aeb400",
      "incomplete_value": true,
      "site": "00aeb40c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeb3bc",
      "incomplete_value": true,
      "site": "00aeb3c8",
      "value": [
        "LOAD",
        "8",
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
      "00aeb3f0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aeb400",
      "DATA",
      [
        "storage",
        "010a0850",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeb3f0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aeb400",
      "DATA",
      [
        "storage",
        "010a0890",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb3b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb390.md#insn-00aeb3b0) · [`00aeb3ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb390.md#insn-00aeb3ac) · [`00aeb3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb390.md#insn-00aeb3b8)
- 新版 [`00aeb3f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb3d4.md#insn-00aeb3f4) · [`00aeb3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb3d4.md#insn-00aeb3f0) · [`00aeb3fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb3d4.md#insn-00aeb3fc)

~~~diff
- 00aeb3b0 ["INT_ADD", "register:40f0:8", ["const:aeb3b0:8", "const:4:8"]]
- 00aeb3b0 ["CALL", null, ["callee:00bde180:8"]]
+ 00aeb3f4 ["INT_ADD", "register:40f0:8", ["const:aeb3f4:8", "const:4:8"]]
+ 00aeb3f4 ["CALL", null, ["callee:00bde180:8"]]
- 00aeb3b0 bytes 60cb0394
+ 00aeb3f4 bytes 63cb0394
- 00aeb3ac ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aeb3ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb3ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb3ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeb3f0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aeb3f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb3f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb3f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeb3ac bytes 00fc1991
+ 00aeb3f0 bytes 00c81791
- 00aeb3b8 ["COPY", "tmp:0:8", ["const:850:8"]]
- 00aeb3b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeb3b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeb3b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeb3fc ["COPY", "tmp:0:8", ["const:890:8"]]
+ 00aeb3fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb3fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb3fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeb3b8 bytes 08412191
+ 00aeb3fc bytes 08412291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d92e264944b8dac2374d09e1e5e62187"></a>

### [`00aeb3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb3cc.md) → [`00aeb410`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb410.md) _ZN8firebase4util6intent19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
      "definition_site": "00aeb43c",
      "incomplete_value": true,
      "site": "00aeb43c",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb3f8",
      "incomplete_value": true,
      "site": "00aeb3f8",
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
            "const:858:8"
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
      "definition_site": "00aeb424",
      "incomplete_value": true,
      "site": "00aeb424",
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
      "definition_site": "00aeb3e0",
      "incomplete_value": true,
      "site": "00aeb3e0",
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
      "definition_site": "00aeb430",
      "incomplete_value": false,
      "site": "00aeb434",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb3ec",
      "incomplete_value": false,
      "site": "00aeb3f0",
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
            "const:289:8"
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
      "00aeb420",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb430",
      "PARAM",
      [
        "storage",
        "00293289",
        null,
        "string"
      ]
    ],
    [
      "00aeb43c",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb420",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb430",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00aeb43c",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb3cc.md#insn-00aeb3f0) · [`00aeb3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb3cc.md#insn-00aeb3f8) · [`00aeb3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb3cc.md#insn-00aeb3dc)
- 新版 [`00aeb434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb410.md#insn-00aeb434) · [`00aeb43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb410.md#insn-00aeb43c) · [`00aeb420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb410.md#insn-00aeb420)

~~~diff
- 00aeb3f0 ["INT_ADD", "register:40f0:8", ["const:aeb3f0:8", "const:4:8"]]
- 00aeb3f0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb434 ["INT_ADD", "register:40f0:8", ["const:aeb434:8", "const:4:8"]]
+ 00aeb434 ["CALL", null, ["callee:00bde090:8"]]
- 00aeb3f0 bytes 14cb0394
+ 00aeb434 bytes 17cb0394
- 00aeb3f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
- 00aeb3f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb43c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
+ 00aeb43c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb3f8 bytes 602e04f9
+ 00aeb43c bytes 604e04f9
- 00aeb3dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
- 00aeb3dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb420 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
+ 00aeb420 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb3dc bytes 682e44f9
+ 00aeb420 bytes 684e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-895ffca32209e951f799d4564223346b"></a>

### [`00aeb40c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb40c.md) → [`00aeb450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb450.md) _ZN8firebase4util6intent19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aeb47c",
      "incomplete_value": true,
      "site": "00aeb47c",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb438",
      "incomplete_value": true,
      "site": "00aeb438",
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
            "const:858:8"
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
      "definition_site": "00aeb464",
      "incomplete_value": true,
      "site": "00aeb464",
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
      "definition_site": "00aeb420",
      "incomplete_value": true,
      "site": "00aeb420",
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
      "definition_site": "00aeb46c",
      "incomplete_value": false,
      "site": "00aeb474",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb428",
      "incomplete_value": false,
      "site": "00aeb430",
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
            "const:289:8"
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
      "00aeb460",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb46c",
      "PARAM",
      [
        "storage",
        "00293289",
        null,
        "string"
      ]
    ],
    [
      "00aeb47c",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb460",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb46c",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00aeb47c",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb40c.md#insn-00aeb430) · [`00aeb438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb40c.md#insn-00aeb438) · [`00aeb41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb40c.md#insn-00aeb41c)
- 新版 [`00aeb474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb450.md#insn-00aeb474) · [`00aeb47c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb450.md#insn-00aeb47c) · [`00aeb460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb450.md#insn-00aeb460)

~~~diff
- 00aeb430 ["INT_ADD", "register:40f0:8", ["const:aeb430:8", "const:4:8"]]
- 00aeb430 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb474 ["INT_ADD", "register:40f0:8", ["const:aeb474:8", "const:4:8"]]
+ 00aeb474 ["CALL", null, ["callee:00bde090:8"]]
- 00aeb430 bytes 04cb0394
+ 00aeb474 bytes 07cb0394
- 00aeb438 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
- 00aeb438 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb47c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
+ 00aeb47c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb438 bytes 602e04f9
+ 00aeb47c bytes 604e04f9
- 00aeb41c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
- 00aeb41c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb460 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
+ 00aeb460 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb41c bytes 682e44f9
+ 00aeb460 bytes 684e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c89e89adf28396fdccb276d7e2aee6c6"></a>

### [`00aeb44c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb44c.md) → [`00aeb490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb490.md) _ZN8firebase4util6intent10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00aeb4c0",
      "incomplete_value": true,
      "site": "00aeb4c0",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb47c",
      "incomplete_value": true,
      "site": "00aeb47c",
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
            "const:858:8"
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
      "definition_site": "00aeb4a4",
      "incomplete_value": true,
      "site": "00aeb4a4",
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
      "definition_site": "00aeb460",
      "incomplete_value": true,
      "site": "00aeb460",
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
      "definition_site": "00aeb4b0",
      "incomplete_value": false,
      "site": "00aeb4b8",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb46c",
      "incomplete_value": false,
      "site": "00aeb474",
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
            "const:289:8"
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
      "00aeb4a0",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb4b0",
      "PARAM",
      [
        "storage",
        "00293289",
        null,
        "string"
      ]
    ],
    [
      "00aeb4c0",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb4a0",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb4b0",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00aeb4c0",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb474`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb44c.md#insn-00aeb474) · [`00aeb47c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb44c.md#insn-00aeb47c) · [`00aeb45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb44c.md#insn-00aeb45c)
- 新版 [`00aeb4b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb490.md#insn-00aeb4b8) · [`00aeb4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb490.md#insn-00aeb4c0) · [`00aeb4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb490.md#insn-00aeb4a0)

~~~diff
- 00aeb474 ["INT_ADD", "register:40f0:8", ["const:aeb474:8", "const:4:8"]]
- 00aeb474 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb4b8 ["INT_ADD", "register:40f0:8", ["const:aeb4b8:8", "const:4:8"]]
+ 00aeb4b8 ["CALL", null, ["callee:00bde090:8"]]
- 00aeb474 bytes f3ca0394
+ 00aeb4b8 bytes f6ca0394
- 00aeb47c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
- 00aeb47c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb4c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
+ 00aeb4c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb47c bytes 602e04f9
+ 00aeb4c0 bytes 604e04f9
- 00aeb45c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
- 00aeb45c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb4a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
+ 00aeb4a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb45c bytes 682e44f9
+ 00aeb4a0 bytes 684e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c23e34615cff9cad715e0d1d97d3b7f5"></a>

### [`00aeb490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb490.md) → [`00aeb4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb4d4.md) _ZN8firebase4util6intent10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aeb504",
      "incomplete_value": true,
      "site": "00aeb504",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb4c0",
      "incomplete_value": true,
      "site": "00aeb4c0",
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
            "const:858:8"
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
      "definition_site": "00aeb4e8",
      "incomplete_value": true,
      "site": "00aeb4e8",
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
      "definition_site": "00aeb4a4",
      "incomplete_value": true,
      "site": "00aeb4a4",
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
      "definition_site": "00aeb4f0",
      "incomplete_value": false,
      "site": "00aeb4fc",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb4ac",
      "incomplete_value": false,
      "site": "00aeb4b8",
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
            "const:289:8"
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
      "00aeb4e4",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb4f0",
      "PARAM",
      [
        "storage",
        "00293289",
        null,
        "string"
      ]
    ],
    [
      "00aeb504",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb4e4",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb4f0",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00aeb504",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb490.md#insn-00aeb4b8) · [`00aeb4c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb490.md#insn-00aeb4c0) · [`00aeb4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb490.md#insn-00aeb4a0)
- 新版 [`00aeb4fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb4d4.md#insn-00aeb4fc) · [`00aeb504`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb4d4.md#insn-00aeb504) · [`00aeb4e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb4d4.md#insn-00aeb4e4)

~~~diff
- 00aeb4b8 ["INT_ADD", "register:40f0:8", ["const:aeb4b8:8", "const:4:8"]]
- 00aeb4b8 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb4fc ["INT_ADD", "register:40f0:8", ["const:aeb4fc:8", "const:4:8"]]
+ 00aeb4fc ["CALL", null, ["callee:00bde090:8"]]
- 00aeb4b8 bytes e2ca0394
+ 00aeb4fc bytes e5ca0394
- 00aeb4c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
- 00aeb4c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb504 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
+ 00aeb504 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb4c0 bytes 602e04f9
+ 00aeb504 bytes 604e04f9
- 00aeb4a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:858:8"]]
- 00aeb4a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb4e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
+ 00aeb4e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb4a0 bytes 682e44f9
+ 00aeb4e4 bytes 684e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-115caf40d5082e50204c7473c050eb89"></a>

### [`00aeb4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb4e0.md) → [`00aeb524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb524.md) _ZN8firebase4util6intent15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeb5ac",
      "incomplete_value": true,
      "site": "00aeb5ac",
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
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb568",
      "incomplete_value": true,
      "site": "00aeb568",
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
            "const:860:8"
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
      "definition_site": "00aeb558",
      "incomplete_value": true,
      "site": "00aeb564",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:898:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb514",
      "incomplete_value": true,
      "site": "00aeb520",
      "value": [
        "LOAD",
        "8",
        [
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
                "register:4048:8"
              ],
              [
                "leaf",
                "const:858:8"
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
      "00aeb538",
      "READ",
      [
        "storage",
        "010a0860",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb558",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb5ac",
      "WRITE",
      [
        "storage",
        "010a0860",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeb538",
      "READ",
      [
        "storage",
        "010a08a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb558",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb5ac",
      "WRITE",
      [
        "storage",
        "010a08a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb4e0.md#insn-00aeb520) · [`00aeb568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb4e0.md#insn-00aeb568) · [`00aeb4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb4e0.md#insn-00aeb4f4)
- 新版 [`00aeb564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb524.md#insn-00aeb564) · [`00aeb5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb524.md#insn-00aeb5ac) · [`00aeb538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb524.md#insn-00aeb538)

~~~diff
- 00aeb520 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeb520 ["INT_ADD", "register:40f0:8", ["const:aeb520:8", "const:4:8"]]
- 00aeb520 ["CALLIND", null, ["register:0:8"]]
+ 00aeb564 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aeb564 ["INT_ADD", "register:40f0:8", ["const:aeb564:8", "const:4:8"]]
+ 00aeb564 ["CALLIND", null, ["register:0:8"]]
- 00aeb520 bytes 00013fd6
+ 00aeb564 bytes 00013fd6
- 00aeb568 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aeb568 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:860:8"]]
- 00aeb568 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aeb5ac ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aeb5ac ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8a0:8"]]
+ 00aeb5ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aeb568 bytes a0822139
+ 00aeb5ac bytes a0822239
- 00aeb4f4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:860:8"]]
- 00aeb4f4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aeb4f4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aeb538 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8a0:8"]]
+ 00aeb538 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb538 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aeb4f4 bytes a8826139
+ 00aeb538 bytes a8826239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-267978775e614360b8674e45fe238539"></a>

### [`00aeb57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb57c.md) → [`00aeb5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb5c0.md) _ZN8firebase4util6intent12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00aeb5fc",
      "incomplete_value": true,
      "site": "00aeb5fc",
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
            "const:8a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb5b8",
      "incomplete_value": true,
      "site": "00aeb5b8",
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
            "const:860:8"
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
      "definition_site": "00aeb64c",
      "incomplete_value": true,
      "site": "00aeb64c",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb608",
      "incomplete_value": true,
      "site": "00aeb608",
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
            "const:858:8"
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
      "definition_site": "00aeb5d8",
      "incomplete_value": true,
      "site": "00aeb5d8",
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
      "definition_site": "00aeb594",
      "incomplete_value": true,
      "site": "00aeb594",
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
      "00aeb5d4",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb5e0",
      "READ",
      [
        "storage",
        "010a0860",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb5fc",
      "WRITE",
      [
        "storage",
        "010a0860",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeb5d4",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb5e0",
      "READ",
      [
        "storage",
        "010a08a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb5fc",
      "WRITE",
      [
        "storage",
        "010a08a0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb5b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb57c.md#insn-00aeb5b8) · [`00aeb604`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb57c.md#insn-00aeb604) · [`00aeb608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb57c.md#insn-00aeb608)
- 新版 [`00aeb5fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb5c0.md#insn-00aeb5fc) · [`00aeb648`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb5c0.md#insn-00aeb648) · [`00aeb64c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb5c0.md#insn-00aeb64c)

~~~diff
- 00aeb5b8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeb5b8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeb5b8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:860:8"]]
- 00aeb5b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aeb5fc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aeb5fc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aeb5fc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8a0:8"]]
+ 00aeb5fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeb5b8 bytes bf822139
+ 00aeb5fc bytes bf822239
- 00aeb604 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeb604 ["INT_ADD", "register:40f0:8", ["const:aeb604:8", "const:4:8"]]
- 00aeb604 ["CALLIND", null, ["register:0:8"]]
+ 00aeb648 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aeb648 ["INT_ADD", "register:40f0:8", ["const:aeb648:8", "const:4:8"]]
+ 00aeb648 ["CALLIND", null, ["register:0:8"]]
- 00aeb604 bytes 00013fd6
+ 00aeb648 bytes 00013fd6
- 00aeb608 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:858:8"]]
- 00aeb608 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aeb608 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aeb64c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
+ 00aeb64c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aeb64c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aeb608 bytes 9f2e04f9
+ 00aeb64c bytes 9f4e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e75589db1e2f912caa9248f1b649c6af"></a>

### [`00aeb61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb61c.md) → [`00aeb660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb660.md) _ZN8firebase4util6intent14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aeb6a0",
      "incomplete_value": true,
      "site": "00aeb6a0",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb65c",
      "incomplete_value": true,
      "site": "00aeb65c",
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
            "const:858:8"
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
      "definition_site": "00aeb67c",
      "incomplete_value": true,
      "site": "00aeb67c",
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
      "definition_site": "00aeb638",
      "incomplete_value": true,
      "site": "00aeb638",
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
      "definition_site": "00aeb684",
      "incomplete_value": false,
      "site": "00aeb698",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb640",
      "incomplete_value": false,
      "site": "00aeb654",
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
            "const:289:8"
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
      "00aeb674",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb684",
      "PARAM",
      [
        "storage",
        "00293289",
        null,
        "string"
      ]
    ],
    [
      "00aeb6a0",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb674",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb684",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00aeb6a0",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb61c.md#insn-00aeb654) · [`00aeb65c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb61c.md#insn-00aeb65c) · [`00aeb630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb61c.md#insn-00aeb630)
- 新版 [`00aeb698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb660.md#insn-00aeb698) · [`00aeb6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb660.md#insn-00aeb6a0) · [`00aeb674`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb660.md#insn-00aeb674)

~~~diff
- 00aeb654 ["INT_ADD", "register:40f0:8", ["const:aeb654:8", "const:4:8"]]
- 00aeb654 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb698 ["INT_ADD", "register:40f0:8", ["const:aeb698:8", "const:4:8"]]
+ 00aeb698 ["CALL", null, ["callee:00bde090:8"]]
- 00aeb654 bytes 7bca0394
+ 00aeb698 bytes 7eca0394
- 00aeb65c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:858:8"]]
- 00aeb65c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb6a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
+ 00aeb6a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb65c bytes 802e04f9
+ 00aeb6a0 bytes 804e04f9
- 00aeb630 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:858:8"]]
- 00aeb630 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb674 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
+ 00aeb674 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb630 bytes 812e44f9
+ 00aeb674 bytes 814e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06a0d430903f5ac02dba204fdd2edfb9"></a>

### [`00aeb68c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb68c.md) → [`00aeb6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb6d0.md) _ZN8firebase4util6intent11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde660.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6b0.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00aeb6ec",
      "incomplete_value": false,
      "site": "00aeb6f0",
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
      "definition_site": "00aeb6a8",
      "incomplete_value": false,
      "site": "00aeb6ac",
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
      "definition_site": "00aeb6fc",
      "incomplete_value": true,
      "site": "00aeb708",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeb6b8",
      "incomplete_value": true,
      "site": "00aeb6c4",
      "value": [
        "LOAD",
        "8",
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
      "00aeb6ec",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aeb6fc",
      "DATA",
      [
        "storage",
        "010a0868",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeb6ec",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aeb6fc",
      "DATA",
      [
        "storage",
        "010a08a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb68c.md#insn-00aeb6ac) · [`00aeb6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb68c.md#insn-00aeb6a8) · [`00aeb6b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb68c.md#insn-00aeb6b4)
- 新版 [`00aeb6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb6d0.md#insn-00aeb6f0) · [`00aeb6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb6d0.md#insn-00aeb6ec) · [`00aeb6f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb6d0.md#insn-00aeb6f8)

~~~diff
- 00aeb6ac ["INT_ADD", "register:40f0:8", ["const:aeb6ac:8", "const:4:8"]]
- 00aeb6ac ["CALL", null, ["callee:00bde180:8"]]
+ 00aeb6f0 ["INT_ADD", "register:40f0:8", ["const:aeb6f0:8", "const:4:8"]]
+ 00aeb6f0 ["CALL", null, ["callee:00bde180:8"]]
- 00aeb6ac bytes a1ca0394
+ 00aeb6f0 bytes a4ca0394
- 00aeb6a8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aeb6a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb6a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb6a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeb6ec ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aeb6ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb6ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb6ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeb6a8 bytes 00501791
+ 00aeb6ec bytes 001c1591
- 00aeb6b4 ["COPY", "tmp:0:8", ["const:868:8"]]
- 00aeb6b4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeb6b4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeb6b4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeb6f8 ["COPY", "tmp:0:8", ["const:8a8:8"]]
+ 00aeb6f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb6f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb6f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeb6b4 bytes 08a12191
+ 00aeb6f8 bytes 08a12291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-447f3af93f9ed06f2cd1956e6de3ef94"></a>

### [`00aeb6c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb6c8.md) → [`00aeb70c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb70c.md) _ZN8firebase4util6intent13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aeb74c",
      "incomplete_value": true,
      "site": "00aeb74c",
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
            "const:898:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb708",
      "incomplete_value": true,
      "site": "00aeb708",
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
            "const:858:8"
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
      "definition_site": "00aeb728",
      "incomplete_value": true,
      "site": "00aeb728",
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
      "definition_site": "00aeb6e4",
      "incomplete_value": true,
      "site": "00aeb6e4",
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
      "definition_site": "00aeb730",
      "incomplete_value": false,
      "site": "00aeb744",
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
            "const:1fc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb6ec",
      "incomplete_value": false,
      "site": "00aeb700",
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
            "const:289:8"
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
      "00aeb720",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb730",
      "PARAM",
      [
        "storage",
        "00293289",
        null,
        "string"
      ]
    ],
    [
      "00aeb74c",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb720",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb730",
      "PARAM",
      [
        "storage",
        "002931fc",
        null,
        "string"
      ]
    ],
    [
      "00aeb74c",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb6c8.md#insn-00aeb700) · [`00aeb708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb6c8.md#insn-00aeb708) · [`00aeb6dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb6c8.md#insn-00aeb6dc)
- 新版 [`00aeb744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb70c.md#insn-00aeb744) · [`00aeb74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb70c.md#insn-00aeb74c) · [`00aeb720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb70c.md#insn-00aeb720)

~~~diff
- 00aeb700 ["INT_ADD", "register:40f0:8", ["const:aeb700:8", "const:4:8"]]
- 00aeb700 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb744 ["INT_ADD", "register:40f0:8", ["const:aeb744:8", "const:4:8"]]
+ 00aeb744 ["CALL", null, ["callee:00bde090:8"]]
- 00aeb700 bytes 50ca0394
+ 00aeb744 bytes 53ca0394
- 00aeb708 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:858:8"]]
- 00aeb708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb74c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
+ 00aeb74c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb708 bytes 802e04f9
+ 00aeb74c bytes 804e04f9
- 00aeb6dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:858:8"]]
- 00aeb6dc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb720 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
+ 00aeb720 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb6dc bytes 812e44f9
+ 00aeb720 bytes 814e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76010edc06a93e98f76a9b4820f9425e"></a>

### [`00aeb738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb738.md) → [`00aeb77c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb77c.md) _ZN8firebase4util6intent10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aeb798",
      "incomplete_value": false,
      "site": "00aeb79c",
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
      "definition_site": "00aeb754",
      "incomplete_value": false,
      "site": "00aeb758",
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
      "definition_site": "00aeb7a8",
      "incomplete_value": true,
      "site": "00aeb7b4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeb764",
      "incomplete_value": true,
      "site": "00aeb770",
      "value": [
        "LOAD",
        "8",
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
      "00aeb798",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aeb7a8",
      "DATA",
      [
        "storage",
        "010a0890",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeb798",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aeb7a8",
      "DATA",
      [
        "storage",
        "010a08d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb738.md#insn-00aeb758) · [`00aeb754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb738.md#insn-00aeb754) · [`00aeb760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb738.md#insn-00aeb760)
- 新版 [`00aeb79c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb77c.md#insn-00aeb79c) · [`00aeb798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb77c.md#insn-00aeb798) · [`00aeb7a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb77c.md#insn-00aeb7a4)

~~~diff
- 00aeb758 ["INT_ADD", "register:40f0:8", ["const:aeb758:8", "const:4:8"]]
- 00aeb758 ["CALL", null, ["callee:00bde180:8"]]
+ 00aeb79c ["INT_ADD", "register:40f0:8", ["const:aeb79c:8", "const:4:8"]]
+ 00aeb79c ["CALL", null, ["callee:00bde180:8"]]
- 00aeb758 bytes 76ca0394
+ 00aeb79c bytes 79ca0394
- 00aeb754 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aeb754 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb754 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeb754 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeb798 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aeb798 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb798 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeb798 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeb754 bytes 00fc1991
+ 00aeb798 bytes 00c81791
- 00aeb760 ["COPY", "tmp:0:8", ["const:890:8"]]
- 00aeb760 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeb760 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeb760 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aeb7a4 ["COPY", "tmp:0:8", ["const:8d0:8"]]
+ 00aeb7a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb7a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aeb7a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeb760 bytes 08412291
+ 00aeb7a4 bytes 08412391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b4b58f25e279c883463f24442c0cae4"></a>

### [`00aeb774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb774.md) → [`00aeb7b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb7b8.md) _ZN8firebase4util8iterable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 93.75% / 新版 93.75%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeb7e4",
      "incomplete_value": true,
      "site": "00aeb7e4",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb7a0",
      "incomplete_value": true,
      "site": "00aeb7a0",
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
            "const:898:8"
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
      "00aeb7c8",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb7e4",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb7c8",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb7e4",
      "WRITE",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb774.md#insn-00aeb7a0) · [`00aeb784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb774.md#insn-00aeb784) · [`00aeb798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb774.md#insn-00aeb798)
- 新版 [`00aeb7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb7b8.md#insn-00aeb7e4) · [`00aeb7c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb7b8.md#insn-00aeb7c8) · [`00aeb7dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb7b8.md#insn-00aeb7dc)

~~~diff
- 00aeb7a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
- 00aeb7a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb7e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
+ 00aeb7e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb7a0 bytes 604e04f9
+ 00aeb7e4 bytes 606e04f9
- 00aeb784 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
- 00aeb784 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb7c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
+ 00aeb7c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb784 bytes 684e44f9
+ 00aeb7c8 bytes 686e44f9
- 00aeb798 ["INT_ADD", "register:40f0:8", ["const:aeb798:8", "const:4:8"]]
- 00aeb798 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb7dc ["INT_ADD", "register:40f0:8", ["const:aeb7dc:8", "const:4:8"]]
+ 00aeb7dc ["CALL", null, ["callee:00bde090:8"]]
- 00aeb798 bytes 2aca0394
+ 00aeb7dc bytes 2dca0394
~~~


<a id="compare-232c2bf472369a219875308f21b2d1cf"></a>

### [`00aeb7b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb7b4.md) → [`00aeb7f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb7f8.md) _ZN8firebase4util8iterable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aeb824",
      "incomplete_value": true,
      "site": "00aeb824",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb7e0",
      "incomplete_value": true,
      "site": "00aeb7e0",
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
            "const:898:8"
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
      "definition_site": "00aeb80c",
      "incomplete_value": true,
      "site": "00aeb80c",
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
      "definition_site": "00aeb7c8",
      "incomplete_value": true,
      "site": "00aeb7c8",
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
        "00aeb7c8"
      ],
      [
        "FALL_THROUGH",
        "00aeb80c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aeb80c",
      "incomplete_value": true,
      "site": "00aeb824",
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
      "definition_site": "00aeb7c8",
      "incomplete_value": true,
      "site": "00aeb7e0",
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
      "00aeb808",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb824",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb808",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb824",
      "WRITE",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb7e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb7b4.md#insn-00aeb7e0) · [`00aeb7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb7b4.md#insn-00aeb7c4) · [`00aeb7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb7b4.md#insn-00aeb7d8)
- 新版 [`00aeb824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb7f8.md#insn-00aeb824) · [`00aeb808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb7f8.md#insn-00aeb808) · [`00aeb81c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb7f8.md#insn-00aeb81c)

~~~diff
- 00aeb7e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
- 00aeb7e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb824 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
+ 00aeb824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb7e0 bytes 604e04f9
+ 00aeb824 bytes 606e04f9
- 00aeb7c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
- 00aeb7c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb808 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
+ 00aeb808 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb7c4 bytes 684e44f9
+ 00aeb808 bytes 686e44f9
- 00aeb7d8 ["INT_ADD", "register:40f0:8", ["const:aeb7d8:8", "const:4:8"]]
- 00aeb7d8 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb81c ["INT_ADD", "register:40f0:8", ["const:aeb81c:8", "const:4:8"]]
+ 00aeb81c ["CALL", null, ["callee:00bde090:8"]]
- 00aeb7d8 bytes 1aca0394
+ 00aeb81c bytes 1dca0394
~~~


<a id="compare-f9a399f913c7cbb4c78258ea79385cb8"></a>

### [`00aeb7f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb7f4.md) → [`00aeb838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb838.md) _ZN8firebase4util8iterable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00aeb868",
      "incomplete_value": true,
      "site": "00aeb868",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb824",
      "incomplete_value": true,
      "site": "00aeb824",
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
            "const:898:8"
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
      "definition_site": "00aeb84c",
      "incomplete_value": true,
      "site": "00aeb84c",
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
      "definition_site": "00aeb808",
      "incomplete_value": true,
      "site": "00aeb808",
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
        "00aeb808"
      ],
      [
        "FALL_THROUGH",
        "00aeb84c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aeb84c",
      "incomplete_value": true,
      "site": "00aeb868",
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
      "definition_site": "00aeb808",
      "incomplete_value": true,
      "site": "00aeb824",
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
      "00aeb848",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb868",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb848",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb868",
      "WRITE",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb7f4.md#insn-00aeb824) · [`00aeb804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb7f4.md#insn-00aeb804) · [`00aeb81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb7f4.md#insn-00aeb81c)
- 新版 [`00aeb868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb838.md#insn-00aeb868) · [`00aeb848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb838.md#insn-00aeb848) · [`00aeb860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb838.md#insn-00aeb860)

~~~diff
- 00aeb824 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
- 00aeb824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
+ 00aeb868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb824 bytes 604e04f9
+ 00aeb868 bytes 606e04f9
- 00aeb804 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
- 00aeb804 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb848 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
+ 00aeb848 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb804 bytes 684e44f9
+ 00aeb848 bytes 686e44f9
- 00aeb81c ["INT_ADD", "register:40f0:8", ["const:aeb81c:8", "const:4:8"]]
- 00aeb81c ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb860 ["INT_ADD", "register:40f0:8", ["const:aeb860:8", "const:4:8"]]
+ 00aeb860 ["CALL", null, ["callee:00bde090:8"]]
- 00aeb81c bytes 09ca0394
+ 00aeb860 bytes 0cca0394
~~~


<a id="compare-cb25c8179b6ba302f70820ba798a58c4"></a>

### [`00aeb838`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb838.md) → [`00aeb87c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb87c.md) _ZN8firebase4util8iterable10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aeb8ac",
      "incomplete_value": true,
      "site": "00aeb8ac",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb868",
      "incomplete_value": true,
      "site": "00aeb868",
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
            "const:898:8"
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
      "definition_site": "00aeb890",
      "incomplete_value": true,
      "site": "00aeb890",
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
      "definition_site": "00aeb84c",
      "incomplete_value": true,
      "site": "00aeb84c",
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
        "00aeb84c"
      ],
      [
        "FALL_THROUGH",
        "00aeb890"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aeb890",
      "incomplete_value": true,
      "site": "00aeb8ac",
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
      "definition_site": "00aeb84c",
      "incomplete_value": true,
      "site": "00aeb868",
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
      "00aeb88c",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb8ac",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeb88c",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb8ac",
      "WRITE",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb838.md#insn-00aeb868) · [`00aeb848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb838.md#insn-00aeb848) · [`00aeb860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb838.md#insn-00aeb860)
- 新版 [`00aeb8ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb87c.md#insn-00aeb8ac) · [`00aeb88c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb87c.md#insn-00aeb88c) · [`00aeb8a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb87c.md#insn-00aeb8a4)

~~~diff
- 00aeb868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
- 00aeb868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeb8ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
+ 00aeb8ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeb868 bytes 604e04f9
+ 00aeb8ac bytes 606e04f9
- 00aeb848 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:898:8"]]
- 00aeb848 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb88c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8d8:8"]]
+ 00aeb88c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb848 bytes 684e44f9
+ 00aeb88c bytes 686e44f9
- 00aeb860 ["INT_ADD", "register:40f0:8", ["const:aeb860:8", "const:4:8"]]
- 00aeb860 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeb8a4 ["INT_ADD", "register:40f0:8", ["const:aeb8a4:8", "const:4:8"]]
+ 00aeb8a4 ["CALL", null, ["callee:00bde090:8"]]
- 00aeb860 bytes f8c90394
+ 00aeb8a4 bytes fbc90394
~~~


<a id="compare-352670b78f185ba8fcc1129b79b64cd5"></a>

### [`00aeb888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb888.md) → [`00aeb8cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb8cc.md) _ZN8firebase4util8iterable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aeb954",
      "incomplete_value": true,
      "site": "00aeb954",
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
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb910",
      "incomplete_value": true,
      "site": "00aeb910",
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
            "const:8a0:8"
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
      "00aeb8e0",
      "READ",
      [
        "storage",
        "010a08a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb900",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb954",
      "WRITE",
      [
        "storage",
        "010a08a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeb8e0",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb900",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb954",
      "WRITE",
      [
        "storage",
        "010a08e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb888.md#insn-00aeb910) · [`00aeb89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb888.md#insn-00aeb89c) · [`00aeb8bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb888.md#insn-00aeb8bc)
- 新版 [`00aeb954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb8cc.md#insn-00aeb954) · [`00aeb8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb8cc.md#insn-00aeb8e0) · [`00aeb900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb8cc.md#insn-00aeb900)

~~~diff
- 00aeb910 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aeb910 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8a0:8"]]
- 00aeb910 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aeb954 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aeb954 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8e0:8"]]
+ 00aeb954 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aeb910 bytes a0822239
+ 00aeb954 bytes a0822339
- 00aeb89c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8a0:8"]]
- 00aeb89c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aeb89c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aeb8e0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8e0:8"]]
+ 00aeb8e0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb8e0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aeb89c bytes a8826239
+ 00aeb8e0 bytes a8826339
- 00aeb8bc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:898:8"]]
- 00aeb8bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeb900 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:8d8:8"]]
+ 00aeb900 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb8bc bytes 214d44f9
+ 00aeb900 bytes 216d44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f42d450c62b6413f1fe37d99913a2765"></a>

### [`00aeb924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb924.md) → [`00aeb968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb968.md) _ZN8firebase4util8iterable12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00aeb9a4",
      "incomplete_value": true,
      "site": "00aeb9a4",
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
            "const:8e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb960",
      "incomplete_value": true,
      "site": "00aeb960",
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
            "const:8a0:8"
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
      "definition_site": "00aeb9f4",
      "incomplete_value": true,
      "site": "00aeb9f4",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeb9b0",
      "incomplete_value": true,
      "site": "00aeb9b0",
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
            "const:898:8"
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
      "definition_site": "00aeb980",
      "incomplete_value": true,
      "site": "00aeb980",
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
      "definition_site": "00aeb93c",
      "incomplete_value": true,
      "site": "00aeb93c",
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
      "00aeb97c",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb988",
      "READ",
      [
        "storage",
        "010a08a0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb9a4",
      "WRITE",
      [
        "storage",
        "010a08a0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeb97c",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeb988",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeb9a4",
      "WRITE",
      [
        "storage",
        "010a08e0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeb960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb924.md#insn-00aeb960) · [`00aeb9ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb924.md#insn-00aeb9ac) · [`00aeb9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb924.md#insn-00aeb9b0)
- 新版 [`00aeb9a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb968.md#insn-00aeb9a4) · [`00aeb9f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb968.md#insn-00aeb9f0) · [`00aeb9f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb968.md#insn-00aeb9f4)

~~~diff
- 00aeb960 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aeb960 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aeb960 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8a0:8"]]
- 00aeb960 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aeb9a4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aeb9a4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aeb9a4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8e0:8"]]
+ 00aeb9a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aeb960 bytes bf822239
+ 00aeb9a4 bytes bf822339
- 00aeb9ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeb9ac ["INT_ADD", "register:40f0:8", ["const:aeb9ac:8", "const:4:8"]]
- 00aeb9ac ["CALLIND", null, ["register:0:8"]]
+ 00aeb9f0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aeb9f0 ["INT_ADD", "register:40f0:8", ["const:aeb9f0:8", "const:4:8"]]
+ 00aeb9f0 ["CALLIND", null, ["register:0:8"]]
- 00aeb9ac bytes 00013fd6
+ 00aeb9f0 bytes 00013fd6
- 00aeb9b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
- 00aeb9b0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aeb9b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aeb9f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d8:8"]]
+ 00aeb9f4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aeb9f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aeb9b0 bytes 9f4e04f9
+ 00aeb9f4 bytes 9f6e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-30cf26d3137b716ee30e38c17bcf0928"></a>

### [`00aeb9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb9c4.md) → [`00aeba08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba08.md) _ZN8firebase4util8iterable14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aeba48",
      "incomplete_value": true,
      "site": "00aeba48",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeba04",
      "incomplete_value": true,
      "site": "00aeba04",
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
            "const:898:8"
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
      "definition_site": "00aeba24",
      "incomplete_value": true,
      "site": "00aeba24",
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
      "definition_site": "00aeb9e0",
      "incomplete_value": true,
      "site": "00aeb9e0",
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
        "00aeb9e0"
      ],
      [
        "FALL_THROUGH",
        "00aeba24"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aeba24",
      "incomplete_value": true,
      "site": "00aeba48",
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
      "definition_site": "00aeb9e0",
      "incomplete_value": true,
      "site": "00aeba04",
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
      "00aeba1c",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeba48",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeba5c",
      "PARAM",
      [
        "storage",
        "00c10428",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00aeba1c",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeba48",
      "WRITE",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeba5c",
      "PARAM",
      [
        "storage",
        "00c10478",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeba04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb9c4.md#insn-00aeba04) · [`00aeb9d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb9c4.md#insn-00aeb9d8) · [`00aeb9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeb9c4.md#insn-00aeb9fc)
- 新版 [`00aeba48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba08.md#insn-00aeba48) · [`00aeba1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba08.md#insn-00aeba1c) · [`00aeba40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba08.md#insn-00aeba40)

~~~diff
- 00aeba04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
- 00aeba04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeba48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d8:8"]]
+ 00aeba48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeba04 bytes 804e04f9
+ 00aeba48 bytes 806e04f9
- 00aeb9d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
- 00aeb9d8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeba1c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d8:8"]]
+ 00aeba1c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeb9d8 bytes 814e44f9
+ 00aeba1c bytes 816e44f9
- 00aeb9fc ["INT_ADD", "register:40f0:8", ["const:aeb9fc:8", "const:4:8"]]
- 00aeb9fc ["CALL", null, ["callee:00bde090:8"]]
+ 00aeba40 ["INT_ADD", "register:40f0:8", ["const:aeba40:8", "const:4:8"]]
+ 00aeba40 ["CALL", null, ["callee:00bde090:8"]]
- 00aeb9fc bytes 91c90394
+ 00aeba40 bytes 94c90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85beba93b3e4874206f068f69aff507f"></a>

### [`00aeba34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeba34.md) → [`00aeba78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba78.md) _ZN8firebase4util8iterable11GetMethodIdENS1_6MethodE

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
      "definition_site": "00aeba94",
      "incomplete_value": false,
      "site": "00aeba98",
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
      "definition_site": "00aeba50",
      "incomplete_value": false,
      "site": "00aeba54",
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
      "definition_site": "00aebaa4",
      "incomplete_value": true,
      "site": "00aebab0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aeba60",
      "incomplete_value": true,
      "site": "00aeba6c",
      "value": [
        "LOAD",
        "8",
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
      "00aeba94",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aebaa4",
      "DATA",
      [
        "storage",
        "010a08a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeba94",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aebaa4",
      "DATA",
      [
        "storage",
        "010a08e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeba54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeba34.md#insn-00aeba54) · [`00aeba50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeba34.md#insn-00aeba50) · [`00aeba5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeba34.md#insn-00aeba5c)
- 新版 [`00aeba98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba78.md#insn-00aeba98) · [`00aeba94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba78.md#insn-00aeba94) · [`00aebaa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeba78.md#insn-00aebaa0)

~~~diff
- 00aeba54 ["INT_ADD", "register:40f0:8", ["const:aeba54:8", "const:4:8"]]
- 00aeba54 ["CALL", null, ["callee:00bde180:8"]]
+ 00aeba98 ["INT_ADD", "register:40f0:8", ["const:aeba98:8", "const:4:8"]]
+ 00aeba98 ["CALL", null, ["callee:00bde180:8"]]
- 00aeba54 bytes b7c90394
+ 00aeba98 bytes bac90394
- 00aeba50 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aeba50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeba50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeba50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeba94 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aeba94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeba94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeba94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeba50 bytes 00501791
+ 00aeba94 bytes 001c1591
- 00aeba5c ["COPY", "tmp:0:8", ["const:8a8:8"]]
- 00aeba5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeba5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeba5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aebaa0 ["COPY", "tmp:0:8", ["const:8e8:8"]]
+ 00aebaa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aebaa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aebaa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeba5c bytes 08a12291
+ 00aebaa0 bytes 08a12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dc02455b01c58dc61c13b794109c685"></a>

### [`00aeba70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeba70.md) → [`00aebab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebab4.md) _ZN8firebase4util8iterable13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aebaf4",
      "incomplete_value": true,
      "site": "00aebaf4",
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
            "const:8d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebab0",
      "incomplete_value": true,
      "site": "00aebab0",
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
            "const:898:8"
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
      "definition_site": "00aebad0",
      "incomplete_value": true,
      "site": "00aebad0",
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
      "definition_site": "00aeba8c",
      "incomplete_value": true,
      "site": "00aeba8c",
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
        "00aeba8c"
      ],
      [
        "FALL_THROUGH",
        "00aebad0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aebad0",
      "incomplete_value": true,
      "site": "00aebaf4",
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
      "definition_site": "00aeba8c",
      "incomplete_value": true,
      "site": "00aebab0",
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
      "00aebac8",
      "READ",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebaf4",
      "WRITE",
      [
        "storage",
        "010a0898",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebb0c",
      "PARAM",
      [
        "storage",
        "010a08b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aebac8",
      "READ",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebaf4",
      "WRITE",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebb0c",
      "PARAM",
      [
        "storage",
        "010a08f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeba70.md#insn-00aebab0) · [`00aeba84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeba70.md#insn-00aeba84) · [`00aebaa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeba70.md#insn-00aebaa8)
- 新版 [`00aebaf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebab4.md#insn-00aebaf4) · [`00aebac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebab4.md#insn-00aebac8) · [`00aebaec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebab4.md#insn-00aebaec)

~~~diff
- 00aebab0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
- 00aebab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebaf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d8:8"]]
+ 00aebaf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebab0 bytes 804e04f9
+ 00aebaf4 bytes 806e04f9
- 00aeba84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:898:8"]]
- 00aeba84 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebac8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8d8:8"]]
+ 00aebac8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeba84 bytes 814e44f9
+ 00aebac8 bytes 816e44f9
- 00aebaa8 ["INT_ADD", "register:40f0:8", ["const:aebaa8:8", "const:4:8"]]
- 00aebaa8 ["CALL", null, ["callee:00bde090:8"]]
+ 00aebaec ["INT_ADD", "register:40f0:8", ["const:aebaec:8", "const:4:8"]]
+ 00aebaec ["CALL", null, ["callee:00bde090:8"]]
- 00aebaa8 bytes 66c90394
+ 00aebaec bytes 69c90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6bf185a5825308876958feb58796e87d"></a>

### [`00aebae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebae0.md) → [`00aebb24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb24.md) _ZN8firebase4util8iterable10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aebb40",
      "incomplete_value": false,
      "site": "00aebb44",
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
      "definition_site": "00aebafc",
      "incomplete_value": false,
      "site": "00aebb00",
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
      "definition_site": "00aebb50",
      "incomplete_value": true,
      "site": "00aebb5c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aebb0c",
      "incomplete_value": true,
      "site": "00aebb18",
      "value": [
        "LOAD",
        "8",
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
      "00aebb40",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aebb50",
      "DATA",
      [
        "storage",
        "010a08b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aebb40",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aebb50",
      "DATA",
      [
        "storage",
        "010a08f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebb00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebae0.md#insn-00aebb00) · [`00aebafc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebae0.md#insn-00aebafc) · [`00aebb08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebae0.md#insn-00aebb08)
- 新版 [`00aebb44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb24.md#insn-00aebb44) · [`00aebb40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb24.md#insn-00aebb40) · [`00aebb4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb24.md#insn-00aebb4c)

~~~diff
- 00aebb00 ["INT_ADD", "register:40f0:8", ["const:aebb00:8", "const:4:8"]]
- 00aebb00 ["CALL", null, ["callee:00bde180:8"]]
+ 00aebb44 ["INT_ADD", "register:40f0:8", ["const:aebb44:8", "const:4:8"]]
+ 00aebb44 ["CALL", null, ["callee:00bde180:8"]]
- 00aebb00 bytes 8cc90394
+ 00aebb44 bytes 8fc90394
- 00aebafc ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aebafc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aebafc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aebafc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aebb40 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aebb40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aebb40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aebb40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aebafc bytes 00fc1991
+ 00aebb40 bytes 00c81791
- 00aebb08 ["COPY", "tmp:0:8", ["const:8b0:8"]]
- 00aebb08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aebb08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aebb08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aebb4c ["COPY", "tmp:0:8", ["const:8f0:8"]]
+ 00aebb4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aebb4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aebb4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aebb08 bytes 08c12291
+ 00aebb4c bytes 08c12391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fdceb5d7bdadd731c7774430ee60418d"></a>

### [`00aebb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb1c.md) → [`00aebb60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb60.md) _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

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
      "definition_site": "00aebb8c",
      "incomplete_value": true,
      "site": "00aebb8c",
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
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebb48",
      "incomplete_value": true,
      "site": "00aebb48",
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
            "const:8b8:8"
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
      "definition_site": "00aebb74",
      "incomplete_value": true,
      "site": "00aebb74",
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
      "definition_site": "00aebb30",
      "incomplete_value": true,
      "site": "00aebb30",
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
      "definition_site": "00aebb80",
      "incomplete_value": false,
      "site": "00aebb84",
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
            "const:4da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebb3c",
      "incomplete_value": false,
      "site": "00aebb40",
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
            "const:567:8"
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
      "00aebb70",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebb80",
      "PARAM",
      [
        "storage",
        "00297567",
        null,
        "string"
      ]
    ],
    [
      "00aebb8c",
      "WRITE",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebb70",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebb80",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ],
    [
      "00aebb8c",
      "WRITE",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebb40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb1c.md#insn-00aebb40) · [`00aebb48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb1c.md#insn-00aebb48) · [`00aebb2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb1c.md#insn-00aebb2c)
- 新版 [`00aebb84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb60.md#insn-00aebb84) · [`00aebb8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb60.md#insn-00aebb8c) · [`00aebb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebb60.md#insn-00aebb70)

~~~diff
- 00aebb40 ["INT_ADD", "register:40f0:8", ["const:aebb40:8", "const:4:8"]]
- 00aebb40 ["CALL", null, ["callee:00bde090:8"]]
+ 00aebb84 ["INT_ADD", "register:40f0:8", ["const:aebb84:8", "const:4:8"]]
+ 00aebb84 ["CALL", null, ["callee:00bde090:8"]]
- 00aebb40 bytes 40c90394
+ 00aebb84 bytes 43c90394
- 00aebb48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00aebb48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebb8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00aebb8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebb48 bytes 605e04f9
+ 00aebb8c bytes 607e04f9
- 00aebb2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00aebb2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebb70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00aebb70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aebb2c bytes 685e44f9
+ 00aebb70 bytes 687e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e9dce1394f1f23555a981b5886c81af7"></a>

### [`00aebb5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb5c.md) → [`00aebba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebba0.md) _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aebbcc",
      "incomplete_value": true,
      "site": "00aebbcc",
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
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebb88",
      "incomplete_value": true,
      "site": "00aebb88",
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
            "const:8b8:8"
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
      "definition_site": "00aebbb4",
      "incomplete_value": true,
      "site": "00aebbb4",
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
      "definition_site": "00aebb70",
      "incomplete_value": true,
      "site": "00aebb70",
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
      "definition_site": "00aebbbc",
      "incomplete_value": false,
      "site": "00aebbc4",
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
            "const:4da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebb78",
      "incomplete_value": false,
      "site": "00aebb80",
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
            "const:567:8"
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
      "00aebbb0",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebbbc",
      "PARAM",
      [
        "storage",
        "00297567",
        null,
        "string"
      ]
    ],
    [
      "00aebbcc",
      "WRITE",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebbb0",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebbbc",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ],
    [
      "00aebbcc",
      "WRITE",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebb80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb5c.md#insn-00aebb80) · [`00aebb88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb5c.md#insn-00aebb88) · [`00aebb6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb5c.md#insn-00aebb6c)
- 新版 [`00aebbc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebba0.md#insn-00aebbc4) · [`00aebbcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebba0.md#insn-00aebbcc) · [`00aebbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebba0.md#insn-00aebbb0)

~~~diff
- 00aebb80 ["INT_ADD", "register:40f0:8", ["const:aebb80:8", "const:4:8"]]
- 00aebb80 ["CALL", null, ["callee:00bde090:8"]]
+ 00aebbc4 ["INT_ADD", "register:40f0:8", ["const:aebbc4:8", "const:4:8"]]
+ 00aebbc4 ["CALL", null, ["callee:00bde090:8"]]
- 00aebb80 bytes 30c90394
+ 00aebbc4 bytes 33c90394
- 00aebb88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00aebb88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebbcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00aebbcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebb88 bytes 605e04f9
+ 00aebbcc bytes 607e04f9
- 00aebb6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00aebb6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebbb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00aebbb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aebb6c bytes 685e44f9
+ 00aebbb0 bytes 687e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b70fd148556fff08870f85f15566141"></a>

### [`00aebb9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb9c.md) → [`00aebbe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebbe0.md) _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00aebc10",
      "incomplete_value": true,
      "site": "00aebc10",
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
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebbcc",
      "incomplete_value": true,
      "site": "00aebbcc",
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
            "const:8b8:8"
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
      "definition_site": "00aebbf4",
      "incomplete_value": true,
      "site": "00aebbf4",
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
      "definition_site": "00aebbb0",
      "incomplete_value": true,
      "site": "00aebbb0",
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
        "00aebbb0"
      ],
      [
        "FALL_THROUGH",
        "00aebbf4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aebbf4",
      "incomplete_value": true,
      "site": "00aebc10",
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
      "definition_site": "00aebbb0",
      "incomplete_value": true,
      "site": "00aebbcc",
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
      "00aebbf0",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebc00",
      "PARAM",
      [
        "storage",
        "00297567",
        null,
        "string"
      ]
    ],
    [
      "00aebc10",
      "WRITE",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebbf0",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebc00",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ],
    [
      "00aebc10",
      "WRITE",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebbcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb9c.md#insn-00aebbcc) · [`00aebbac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb9c.md#insn-00aebbac) · [`00aebbbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebb9c.md#insn-00aebbbc)
- 新版 [`00aebc10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebbe0.md#insn-00aebc10) · [`00aebbf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebbe0.md#insn-00aebbf0) · [`00aebc00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebbe0.md#insn-00aebc00)

~~~diff
- 00aebbcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00aebbcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebc10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00aebc10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebbcc bytes 605e04f9
+ 00aebc10 bytes 607e04f9
- 00aebbac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00aebbac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebbf0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00aebbf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aebbac bytes 685e44f9
+ 00aebbf0 bytes 687e44f9
- 00aebbbc ["COPY", "tmp:0:8", ["const:567:8"]]
- 00aebbbc ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00aebbbc ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00aebbbc ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00aebc00 ["COPY", "tmp:0:8", ["const:4da:8"]]
+ 00aebc00 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00aebc00 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00aebc00 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00aebbbc bytes 639c1591
+ 00aebc00 bytes 63681391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05def5ba071b17bf693f56e08a36851f"></a>

### [`00aebbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebbe0.md) → [`00aebc24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc24.md) _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aebc54",
      "incomplete_value": true,
      "site": "00aebc54",
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
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebc10",
      "incomplete_value": true,
      "site": "00aebc10",
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
            "const:8b8:8"
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
      "definition_site": "00aebc38",
      "incomplete_value": true,
      "site": "00aebc38",
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
      "definition_site": "00aebbf4",
      "incomplete_value": true,
      "site": "00aebbf4",
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
      "definition_site": "00aebc40",
      "incomplete_value": false,
      "site": "00aebc4c",
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
            "const:4da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebbfc",
      "incomplete_value": false,
      "site": "00aebc08",
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
            "const:567:8"
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
      "00aebc34",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebc40",
      "PARAM",
      [
        "storage",
        "00297567",
        null,
        "string"
      ]
    ],
    [
      "00aebc54",
      "WRITE",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebc34",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebc40",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ],
    [
      "00aebc54",
      "WRITE",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebc08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebbe0.md#insn-00aebc08) · [`00aebc10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebbe0.md#insn-00aebc10) · [`00aebbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebbe0.md#insn-00aebbf0)
- 新版 [`00aebc4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc24.md#insn-00aebc4c) · [`00aebc54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc24.md#insn-00aebc54) · [`00aebc34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc24.md#insn-00aebc34)

~~~diff
- 00aebc08 ["INT_ADD", "register:40f0:8", ["const:aebc08:8", "const:4:8"]]
- 00aebc08 ["CALL", null, ["callee:00bde090:8"]]
+ 00aebc4c ["INT_ADD", "register:40f0:8", ["const:aebc4c:8", "const:4:8"]]
+ 00aebc4c ["CALL", null, ["callee:00bde090:8"]]
- 00aebc08 bytes 0ec90394
+ 00aebc4c bytes 11c90394
- 00aebc10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00aebc10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebc54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00aebc54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebc10 bytes 605e04f9
+ 00aebc54 bytes 607e04f9
- 00aebbf0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8b8:8"]]
- 00aebbf0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebc34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f8:8"]]
+ 00aebc34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aebbf0 bytes 685e44f9
+ 00aebc34 bytes 687e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bc7456e2312d25a59b262dfa228ee6d"></a>

### [`00aebc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebc30.md) → [`00aebc74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc74.md) _ZN8firebase4util8iterator15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aebcfc",
      "incomplete_value": true,
      "site": "00aebcfc",
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
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebcb8",
      "incomplete_value": true,
      "site": "00aebcb8",
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
            "const:8c0:8"
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
      "definition_site": "00aebca8",
      "incomplete_value": true,
      "site": "00aebcb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebc64",
      "incomplete_value": true,
      "site": "00aebc70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
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
      "00aebc88",
      "READ",
      [
        "storage",
        "010a08c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aebca8",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebcfc",
      "WRITE",
      [
        "storage",
        "010a08c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aebc88",
      "READ",
      [
        "storage",
        "010a0900",
        null,
        "undefined1"
      ]
    ],
    [
      "00aebca8",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebcfc",
      "WRITE",
      [
        "storage",
        "010a0900",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebc30.md#insn-00aebc70) · [`00aebcb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebc30.md#insn-00aebcb8) · [`00aebc44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebc30.md#insn-00aebc44)
- 新版 [`00aebcb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc74.md#insn-00aebcb4) · [`00aebcfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc74.md#insn-00aebcfc) · [`00aebc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebc74.md#insn-00aebc88)

~~~diff
- 00aebc70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aebc70 ["INT_ADD", "register:40f0:8", ["const:aebc70:8", "const:4:8"]]
- 00aebc70 ["CALLIND", null, ["register:0:8"]]
+ 00aebcb4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aebcb4 ["INT_ADD", "register:40f0:8", ["const:aebcb4:8", "const:4:8"]]
+ 00aebcb4 ["CALLIND", null, ["register:0:8"]]
- 00aebc70 bytes 00013fd6
+ 00aebcb4 bytes 00013fd6
- 00aebcb8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aebcb8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8c0:8"]]
- 00aebcb8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aebcfc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aebcfc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:900:8"]]
+ 00aebcfc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aebcb8 bytes a0022339
+ 00aebcfc bytes a0022439
- 00aebc44 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8c0:8"]]
- 00aebc44 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aebc44 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aebc88 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:900:8"]]
+ 00aebc88 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aebc88 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aebc44 bytes a8026339
+ 00aebc88 bytes a8026439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a59c996bbb302876fc38ae21d636b7b0"></a>

### [`00aebccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebccc.md) → [`00aebd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebd10.md) _ZN8firebase4util8iterator12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00aebd4c",
      "incomplete_value": true,
      "site": "00aebd4c",
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
            "const:900:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebd08",
      "incomplete_value": true,
      "site": "00aebd08",
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
            "const:8c0:8"
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
      "definition_site": "00aebd9c",
      "incomplete_value": true,
      "site": "00aebd9c",
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
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebd58",
      "incomplete_value": true,
      "site": "00aebd58",
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
            "const:8b8:8"
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
      "definition_site": "00aebd28",
      "incomplete_value": true,
      "site": "00aebd28",
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
      "definition_site": "00aebce4",
      "incomplete_value": true,
      "site": "00aebce4",
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
      "00aebd24",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebd30",
      "READ",
      [
        "storage",
        "010a08c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aebd4c",
      "WRITE",
      [
        "storage",
        "010a08c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aebd24",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebd30",
      "READ",
      [
        "storage",
        "010a0900",
        null,
        "undefined1"
      ]
    ],
    [
      "00aebd4c",
      "WRITE",
      [
        "storage",
        "010a0900",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebd08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebccc.md#insn-00aebd08) · [`00aebd54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebccc.md#insn-00aebd54) · [`00aebd58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebccc.md#insn-00aebd58)
- 新版 [`00aebd4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebd10.md#insn-00aebd4c) · [`00aebd98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebd10.md#insn-00aebd98) · [`00aebd9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebd10.md#insn-00aebd9c)

~~~diff
- 00aebd08 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aebd08 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aebd08 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8c0:8"]]
- 00aebd08 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aebd4c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aebd4c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aebd4c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:900:8"]]
+ 00aebd4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aebd08 bytes bf022339
+ 00aebd4c bytes bf022439
- 00aebd54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aebd54 ["INT_ADD", "register:40f0:8", ["const:aebd54:8", "const:4:8"]]
- 00aebd54 ["CALLIND", null, ["register:0:8"]]
+ 00aebd98 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aebd98 ["INT_ADD", "register:40f0:8", ["const:aebd98:8", "const:4:8"]]
+ 00aebd98 ["CALLIND", null, ["register:0:8"]]
- 00aebd54 bytes 00013fd6
+ 00aebd98 bytes 00013fd6
- 00aebd58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
- 00aebd58 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aebd58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aebd9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
+ 00aebd9c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aebd9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aebd58 bytes 9f5e04f9
+ 00aebd9c bytes 9f7e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72c609ae4c6259c464a072b538e40051"></a>

### [`00aebd6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebd6c.md) → [`00aebdb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebdb0.md) _ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aebdf0",
      "incomplete_value": true,
      "site": "00aebdf0",
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
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebdac",
      "incomplete_value": true,
      "site": "00aebdac",
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
            "const:8b8:8"
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
      "definition_site": "00aebdcc",
      "incomplete_value": true,
      "site": "00aebdcc",
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
      "definition_site": "00aebd88",
      "incomplete_value": true,
      "site": "00aebd88",
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
      "definition_site": "00aebdd4",
      "incomplete_value": false,
      "site": "00aebde8",
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
            "const:4da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebd90",
      "incomplete_value": false,
      "site": "00aebda4",
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
            "const:567:8"
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
      "00aebdc4",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebdd4",
      "PARAM",
      [
        "storage",
        "00297567",
        null,
        "string"
      ]
    ],
    [
      "00aebdf0",
      "WRITE",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebdc4",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebdd4",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ],
    [
      "00aebdf0",
      "WRITE",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebd6c.md#insn-00aebda4) · [`00aebdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebd6c.md#insn-00aebdac) · [`00aebd80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebd6c.md#insn-00aebd80)
- 新版 [`00aebde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebdb0.md#insn-00aebde8) · [`00aebdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebdb0.md#insn-00aebdf0) · [`00aebdc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebdb0.md#insn-00aebdc4)

~~~diff
- 00aebda4 ["INT_ADD", "register:40f0:8", ["const:aebda4:8", "const:4:8"]]
- 00aebda4 ["CALL", null, ["callee:00bde090:8"]]
+ 00aebde8 ["INT_ADD", "register:40f0:8", ["const:aebde8:8", "const:4:8"]]
+ 00aebde8 ["CALL", null, ["callee:00bde090:8"]]
- 00aebda4 bytes a7c80394
+ 00aebde8 bytes aac80394
- 00aebdac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
- 00aebdac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebdf0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
+ 00aebdf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebdac bytes 805e04f9
+ 00aebdf0 bytes 807e04f9
- 00aebd80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
- 00aebd80 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebdc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
+ 00aebdc4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aebd80 bytes 815e44f9
+ 00aebdc4 bytes 817e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d805e4aecc6831e495590eac3a50327a"></a>

### [`00aebddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebddc.md) → [`00aebe20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe20.md) _ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde690.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde6e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6e0.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00aebe3c",
      "incomplete_value": false,
      "site": "00aebe40",
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
      "definition_site": "00aebdf8",
      "incomplete_value": false,
      "site": "00aebdfc",
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
      "definition_site": "00aebe4c",
      "incomplete_value": true,
      "site": "00aebe58",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aebe08",
      "incomplete_value": true,
      "site": "00aebe14",
      "value": [
        "LOAD",
        "8",
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
      "00aebe3c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aebe4c",
      "DATA",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebe3c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aebe4c",
      "DATA",
      [
        "storage",
        "010a0908",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebddc.md#insn-00aebdfc) · [`00aebdf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebddc.md#insn-00aebdf8) · [`00aebe04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebddc.md#insn-00aebe04)
- 新版 [`00aebe40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe20.md#insn-00aebe40) · [`00aebe3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe20.md#insn-00aebe3c) · [`00aebe48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe20.md#insn-00aebe48)

~~~diff
- 00aebdfc ["INT_ADD", "register:40f0:8", ["const:aebdfc:8", "const:4:8"]]
- 00aebdfc ["CALL", null, ["callee:00bde180:8"]]
+ 00aebe40 ["INT_ADD", "register:40f0:8", ["const:aebe40:8", "const:4:8"]]
+ 00aebe40 ["CALL", null, ["callee:00bde180:8"]]
- 00aebdfc bytes cdc80394
+ 00aebe40 bytes d0c80394
- 00aebdf8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aebdf8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aebdf8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aebdf8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aebe3c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aebe3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aebe3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aebe3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aebdf8 bytes 00501791
+ 00aebe3c bytes 001c1591
- 00aebe04 ["COPY", "tmp:0:8", ["const:8c8:8"]]
- 00aebe04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aebe04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aebe04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aebe48 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 00aebe48 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aebe48 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aebe48 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aebe04 bytes 08212391
+ 00aebe48 bytes 08212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b7d5b009c35a924507201f2c19ae12db"></a>

### [`00aebe18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebe18.md) → [`00aebe5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe5c.md) _ZN8firebase4util8iterator13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aebe9c",
      "incomplete_value": true,
      "site": "00aebe9c",
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
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebe58",
      "incomplete_value": true,
      "site": "00aebe58",
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
            "const:8b8:8"
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
      "definition_site": "00aebe78",
      "incomplete_value": true,
      "site": "00aebe78",
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
      "definition_site": "00aebe34",
      "incomplete_value": true,
      "site": "00aebe34",
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
      "definition_site": "00aebe80",
      "incomplete_value": false,
      "site": "00aebe94",
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
            "const:4da:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebe3c",
      "incomplete_value": false,
      "site": "00aebe50",
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
            "const:567:8"
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
      "00aebe70",
      "READ",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebe80",
      "PARAM",
      [
        "storage",
        "00297567",
        null,
        "string"
      ]
    ],
    [
      "00aebe9c",
      "WRITE",
      [
        "storage",
        "010a08b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebe70",
      "READ",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebe80",
      "PARAM",
      [
        "storage",
        "002974da",
        null,
        "string"
      ]
    ],
    [
      "00aebe9c",
      "WRITE",
      [
        "storage",
        "010a08f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebe50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebe18.md#insn-00aebe50) · [`00aebe58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebe18.md#insn-00aebe58) · [`00aebe2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebe18.md#insn-00aebe2c)
- 新版 [`00aebe94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe5c.md#insn-00aebe94) · [`00aebe9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe5c.md#insn-00aebe9c) · [`00aebe70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebe5c.md#insn-00aebe70)

~~~diff
- 00aebe50 ["INT_ADD", "register:40f0:8", ["const:aebe50:8", "const:4:8"]]
- 00aebe50 ["CALL", null, ["callee:00bde090:8"]]
+ 00aebe94 ["INT_ADD", "register:40f0:8", ["const:aebe94:8", "const:4:8"]]
+ 00aebe94 ["CALL", null, ["callee:00bde090:8"]]
- 00aebe50 bytes 7cc80394
+ 00aebe94 bytes 7fc80394
- 00aebe58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
- 00aebe58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebe9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
+ 00aebe9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebe58 bytes 805e04f9
+ 00aebe9c bytes 807e04f9
- 00aebe2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8b8:8"]]
- 00aebe2c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebe70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f8:8"]]
+ 00aebe70 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aebe2c bytes 815e44f9
+ 00aebe70 bytes 817e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3149bd5520212d7f6b1c652d79cc1b2"></a>

### [`00aebe88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebe88.md) → [`00aebecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebecc.md) _ZN8firebase4util8iterator10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aebee8",
      "incomplete_value": false,
      "site": "00aebeec",
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
      "definition_site": "00aebea4",
      "incomplete_value": false,
      "site": "00aebea8",
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
      "definition_site": "00aebef8",
      "incomplete_value": true,
      "site": "00aebf04",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aebeb4",
      "incomplete_value": true,
      "site": "00aebec0",
      "value": [
        "LOAD",
        "8",
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
      "00aebee8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aebef8",
      "DATA",
      [
        "storage",
        "010a08d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aebee8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aebef8",
      "DATA",
      [
        "storage",
        "010a0918",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebe88.md#insn-00aebea8) · [`00aebea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebe88.md#insn-00aebea4) · [`00aebeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebe88.md#insn-00aebeb0)
- 新版 [`00aebeec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebecc.md#insn-00aebeec) · [`00aebee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebecc.md#insn-00aebee8) · [`00aebef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebecc.md#insn-00aebef4)

~~~diff
- 00aebea8 ["INT_ADD", "register:40f0:8", ["const:aebea8:8", "const:4:8"]]
- 00aebea8 ["CALL", null, ["callee:00bde180:8"]]
+ 00aebeec ["INT_ADD", "register:40f0:8", ["const:aebeec:8", "const:4:8"]]
+ 00aebeec ["CALL", null, ["callee:00bde180:8"]]
- 00aebea8 bytes a2c80394
+ 00aebeec bytes a5c80394
- 00aebea4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aebea4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aebea4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aebea4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aebee8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aebee8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aebee8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aebee8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aebea4 bytes 00fc1991
+ 00aebee8 bytes 00c81791
- 00aebeb0 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 00aebeb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aebeb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aebeb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aebef4 ["COPY", "tmp:0:8", ["const:918:8"]]
+ 00aebef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aebef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aebef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aebeb0 bytes 08612391
+ 00aebef4 bytes 08612491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-221095e702f65960a28f760f4a04bdd0"></a>

### [`00aebec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebec4.md) → [`00aebf08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf08.md) _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

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
      "definition_site": "00aebf34",
      "incomplete_value": true,
      "site": "00aebf34",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebef0",
      "incomplete_value": true,
      "site": "00aebef0",
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
            "const:8e0:8"
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
      "definition_site": "00aebf1c",
      "incomplete_value": true,
      "site": "00aebf1c",
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
      "definition_site": "00aebed8",
      "incomplete_value": true,
      "site": "00aebed8",
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
        "00aebed8"
      ],
      [
        "FALL_THROUGH",
        "00aebf1c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aebf1c",
      "incomplete_value": true,
      "site": "00aebf34",
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
      "definition_site": "00aebed8",
      "incomplete_value": true,
      "site": "00aebef0",
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
      "00aebf18",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebf34",
      "WRITE",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebf18",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebf34",
      "WRITE",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebec4.md#insn-00aebef0) · [`00aebed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebec4.md#insn-00aebed4) · [`00aebee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebec4.md#insn-00aebee8)
- 新版 [`00aebf34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf08.md#insn-00aebf34) · [`00aebf18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf08.md#insn-00aebf18) · [`00aebf2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf08.md#insn-00aebf2c)

~~~diff
- 00aebef0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e0:8"]]
- 00aebef0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebf34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00aebf34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebef0 bytes 607204f9
+ 00aebf34 bytes 609204f9
- 00aebed4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e0:8"]]
- 00aebed4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebf18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00aebf18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aebed4 bytes 687244f9
+ 00aebf18 bytes 689244f9
- 00aebee8 ["INT_ADD", "register:40f0:8", ["const:aebee8:8", "const:4:8"]]
- 00aebee8 ["CALL", null, ["callee:00bde090:8"]]
+ 00aebf2c ["INT_ADD", "register:40f0:8", ["const:aebf2c:8", "const:4:8"]]
+ 00aebf2c ["CALL", null, ["callee:00bde090:8"]]
- 00aebee8 bytes 56c80394
+ 00aebf2c bytes 59c80394
~~~


<a id="compare-c7df34a9ea70a75d2a770ce9a979f34f"></a>

### [`00aebf04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf04.md) → [`00aebf48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf48.md) _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aebf74",
      "incomplete_value": true,
      "site": "00aebf74",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebf30",
      "incomplete_value": true,
      "site": "00aebf30",
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
            "const:8e0:8"
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
      "definition_site": "00aebf5c",
      "incomplete_value": true,
      "site": "00aebf5c",
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
      "definition_site": "00aebf18",
      "incomplete_value": true,
      "site": "00aebf18",
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
        "00aebf18"
      ],
      [
        "FALL_THROUGH",
        "00aebf5c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aebf5c",
      "incomplete_value": true,
      "site": "00aebf74",
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
      "definition_site": "00aebf18",
      "incomplete_value": true,
      "site": "00aebf30",
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
      "00aebf58",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebf74",
      "WRITE",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebf58",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebf74",
      "WRITE",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebf30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf04.md#insn-00aebf30) · [`00aebf14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf04.md#insn-00aebf14) · [`00aebf28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf04.md#insn-00aebf28)
- 新版 [`00aebf74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf48.md#insn-00aebf74) · [`00aebf58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf48.md#insn-00aebf58) · [`00aebf6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf48.md#insn-00aebf6c)

~~~diff
- 00aebf30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e0:8"]]
- 00aebf30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebf74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00aebf74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebf30 bytes 607204f9
+ 00aebf74 bytes 609204f9
- 00aebf14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e0:8"]]
- 00aebf14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebf58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00aebf58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aebf14 bytes 687244f9
+ 00aebf58 bytes 689244f9
- 00aebf28 ["INT_ADD", "register:40f0:8", ["const:aebf28:8", "const:4:8"]]
- 00aebf28 ["CALL", null, ["callee:00bde090:8"]]
+ 00aebf6c ["INT_ADD", "register:40f0:8", ["const:aebf6c:8", "const:4:8"]]
+ 00aebf6c ["CALL", null, ["callee:00bde090:8"]]
- 00aebf28 bytes 46c80394
+ 00aebf6c bytes 49c80394
~~~


<a id="compare-5d044bc640624ed2fb6c43a4d086968b"></a>

### [`00aebf44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf44.md) → [`00aebf88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf88.md) _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00aebfb8",
      "incomplete_value": true,
      "site": "00aebfb8",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebf74",
      "incomplete_value": true,
      "site": "00aebf74",
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
            "const:8e0:8"
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
      "definition_site": "00aebf9c",
      "incomplete_value": true,
      "site": "00aebf9c",
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
      "definition_site": "00aebf58",
      "incomplete_value": true,
      "site": "00aebf58",
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
        "00aebf58"
      ],
      [
        "FALL_THROUGH",
        "00aebf9c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aebf9c",
      "incomplete_value": true,
      "site": "00aebfb8",
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
      "definition_site": "00aebf58",
      "incomplete_value": true,
      "site": "00aebf74",
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
      "00aebf98",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebfb8",
      "WRITE",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebf98",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebfb8",
      "WRITE",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebf74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf44.md#insn-00aebf74) · [`00aebf54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf44.md#insn-00aebf54) · [`00aebf6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf44.md#insn-00aebf6c)
- 新版 [`00aebfb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf88.md#insn-00aebfb8) · [`00aebf98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf88.md#insn-00aebf98) · [`00aebfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebf88.md#insn-00aebfb0)

~~~diff
- 00aebf74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e0:8"]]
- 00aebf74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebfb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00aebfb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebf74 bytes 607204f9
+ 00aebfb8 bytes 609204f9
- 00aebf54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e0:8"]]
- 00aebf54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebf98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00aebf98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aebf54 bytes 687244f9
+ 00aebf98 bytes 689244f9
- 00aebf6c ["INT_ADD", "register:40f0:8", ["const:aebf6c:8", "const:4:8"]]
- 00aebf6c ["CALL", null, ["callee:00bde090:8"]]
+ 00aebfb0 ["INT_ADD", "register:40f0:8", ["const:aebfb0:8", "const:4:8"]]
+ 00aebfb0 ["CALL", null, ["callee:00bde090:8"]]
- 00aebf6c bytes 35c80394
+ 00aebfb0 bytes 38c80394
~~~


<a id="compare-4a34635b7048c75cc5dbbb6e820d82dd"></a>

### [`00aebf88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf88.md) → [`00aebfcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebfcc.md) _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aebffc",
      "incomplete_value": true,
      "site": "00aebffc",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aebfb8",
      "incomplete_value": true,
      "site": "00aebfb8",
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
            "const:8e0:8"
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
      "definition_site": "00aebfe0",
      "incomplete_value": true,
      "site": "00aebfe0",
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
      "definition_site": "00aebf9c",
      "incomplete_value": true,
      "site": "00aebf9c",
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
        "00aebf9c"
      ],
      [
        "FALL_THROUGH",
        "00aebfe0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aebfe0",
      "incomplete_value": true,
      "site": "00aebffc",
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
      "definition_site": "00aebf9c",
      "incomplete_value": true,
      "site": "00aebfb8",
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
      "00aebfdc",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebffc",
      "WRITE",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aebfdc",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00aebffc",
      "WRITE",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aebfb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf88.md#insn-00aebfb8) · [`00aebf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf88.md#insn-00aebf98) · [`00aebfb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebf88.md#insn-00aebfb0)
- 新版 [`00aebffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebfcc.md#insn-00aebffc) · [`00aebfdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebfcc.md#insn-00aebfdc) · [`00aebff4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aebfcc.md#insn-00aebff4)

~~~diff
- 00aebfb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e0:8"]]
- 00aebfb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aebffc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00aebffc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aebfb8 bytes 607204f9
+ 00aebffc bytes 609204f9
- 00aebf98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e0:8"]]
- 00aebf98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aebfdc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00aebfdc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aebf98 bytes 687244f9
+ 00aebfdc bytes 689244f9
- 00aebfb0 ["INT_ADD", "register:40f0:8", ["const:aebfb0:8", "const:4:8"]]
- 00aebfb0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aebff4 ["INT_ADD", "register:40f0:8", ["const:aebff4:8", "const:4:8"]]
+ 00aebff4 ["CALL", null, ["callee:00bde090:8"]]
- 00aebfb0 bytes 24c80394
+ 00aebff4 bytes 27c80394
~~~


<a id="compare-73c39ebf0181c1cc6440a534a27d79f9"></a>

### [`00aebfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebfd8.md) → [`00aec01c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec01c.md) _ZN8firebase4util4list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec0a4",
      "incomplete_value": true,
      "site": "00aec0a4",
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
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec060",
      "incomplete_value": true,
      "site": "00aec060",
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
            "const:8e8:8"
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
      "definition_site": "00aec050",
      "incomplete_value": true,
      "site": "00aec05c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec00c",
      "incomplete_value": true,
      "site": "00aec018",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e0:8"
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
      "00aec030",
      "READ",
      [
        "storage",
        "010a08e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec050",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec0a4",
      "WRITE",
      [
        "storage",
        "010a08e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aec030",
      "READ",
      [
        "storage",
        "010a0928",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec050",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec0a4",
      "WRITE",
      [
        "storage",
        "010a0928",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebfd8.md#insn-00aec018) · [`00aec060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebfd8.md#insn-00aec060) · [`00aebfec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebfd8.md#insn-00aebfec)
- 新版 [`00aec05c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec01c.md#insn-00aec05c) · [`00aec0a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec01c.md#insn-00aec0a4) · [`00aec030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec01c.md#insn-00aec030)

~~~diff
- 00aec018 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec018 ["INT_ADD", "register:40f0:8", ["const:aec018:8", "const:4:8"]]
- 00aec018 ["CALLIND", null, ["register:0:8"]]
+ 00aec05c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aec05c ["INT_ADD", "register:40f0:8", ["const:aec05c:8", "const:4:8"]]
+ 00aec05c ["CALLIND", null, ["register:0:8"]]
- 00aec018 bytes 00013fd6
+ 00aec05c bytes 00013fd6
- 00aec060 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aec060 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8e8:8"]]
- 00aec060 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aec0a4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aec0a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:928:8"]]
+ 00aec0a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aec060 bytes a0a22339
+ 00aec0a4 bytes a0a22439
- 00aebfec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8e8:8"]]
- 00aebfec ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aebfec ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aec030 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:928:8"]]
+ 00aec030 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aec030 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aebfec bytes a8a26339
+ 00aec030 bytes a8a26439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5b4dcb1910253c41cc6929a6f5228c8"></a>

### [`00aec074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec074.md) → [`00aec0b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec0b8.md) _ZN8firebase4util4list12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00aec0f4",
      "incomplete_value": true,
      "site": "00aec0f4",
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
            "const:928:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec0b0",
      "incomplete_value": true,
      "site": "00aec0b0",
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
            "const:8e8:8"
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
      "definition_site": "00aec144",
      "incomplete_value": true,
      "site": "00aec144",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec100",
      "incomplete_value": true,
      "site": "00aec100",
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
            "const:8e0:8"
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
      "definition_site": "00aec0d0",
      "incomplete_value": true,
      "site": "00aec0d0",
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
      "definition_site": "00aec08c",
      "incomplete_value": true,
      "site": "00aec08c",
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
      "00aec0cc",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec0d8",
      "READ",
      [
        "storage",
        "010a08e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec0f4",
      "WRITE",
      [
        "storage",
        "010a08e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aec0cc",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec0d8",
      "READ",
      [
        "storage",
        "010a0928",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec0f4",
      "WRITE",
      [
        "storage",
        "010a0928",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec074.md#insn-00aec0b0) · [`00aec0fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec074.md#insn-00aec0fc) · [`00aec100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec074.md#insn-00aec100)
- 新版 [`00aec0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec0b8.md#insn-00aec0f4) · [`00aec140`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec0b8.md#insn-00aec140) · [`00aec144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec0b8.md#insn-00aec144)

~~~diff
- 00aec0b0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aec0b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aec0b0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8e8:8"]]
- 00aec0b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aec0f4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aec0f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aec0f4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:928:8"]]
+ 00aec0f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aec0b0 bytes bfa22339
+ 00aec0f4 bytes bfa22439
- 00aec0fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec0fc ["INT_ADD", "register:40f0:8", ["const:aec0fc:8", "const:4:8"]]
- 00aec0fc ["CALLIND", null, ["register:0:8"]]
+ 00aec140 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aec140 ["INT_ADD", "register:40f0:8", ["const:aec140:8", "const:4:8"]]
+ 00aec140 ["CALLIND", null, ["register:0:8"]]
- 00aec0fc bytes 00013fd6
+ 00aec140 bytes 00013fd6
- 00aec100 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e0:8"]]
- 00aec100 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aec100 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aec144 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00aec144 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aec144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aec100 bytes 9f7204f9
+ 00aec144 bytes 9f9204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5940e9e464cd63d1c28577f105671864"></a>

### [`00aec114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec114.md) → [`00aec158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec158.md) _ZN8firebase4util4list14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aec198",
      "incomplete_value": true,
      "site": "00aec198",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec154",
      "incomplete_value": true,
      "site": "00aec154",
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
            "const:8e0:8"
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
      "00aec16c",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec198",
      "WRITE",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec1ac",
      "PARAM",
      [
        "storage",
        "00c10470",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00aec16c",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec198",
      "WRITE",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec1ac",
      "PARAM",
      [
        "storage",
        "00c104c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec114.md#insn-00aec154) · [`00aec128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec114.md#insn-00aec128) · [`00aec14c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec114.md#insn-00aec14c)
- 新版 [`00aec198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec158.md#insn-00aec198) · [`00aec16c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec158.md#insn-00aec16c) · [`00aec190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec158.md#insn-00aec190)

~~~diff
- 00aec154 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e0:8"]]
- 00aec154 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec198 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00aec198 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec154 bytes 807204f9
+ 00aec198 bytes 809204f9
- 00aec128 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e0:8"]]
- 00aec128 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec16c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00aec16c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec128 bytes 817244f9
+ 00aec16c bytes 819244f9
- 00aec14c ["INT_ADD", "register:40f0:8", ["const:aec14c:8", "const:4:8"]]
- 00aec14c ["CALL", null, ["callee:00bde090:8"]]
+ 00aec190 ["INT_ADD", "register:40f0:8", ["const:aec190:8", "const:4:8"]]
+ 00aec190 ["CALL", null, ["callee:00bde090:8"]]
- 00aec14c bytes bdc70394
+ 00aec190 bytes c0c70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bad83f6f2a9f3e926de77955ae83b760"></a>

### [`00aec184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec184.md) → [`00aec1c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec1c8.md) _ZN8firebase4util4list11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde650.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde6a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6a0.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00aec1e4",
      "incomplete_value": false,
      "site": "00aec1e8",
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
      "definition_site": "00aec1a0",
      "incomplete_value": false,
      "site": "00aec1a4",
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
      "definition_site": "00aec1f4",
      "incomplete_value": true,
      "site": "00aec200",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec1b0",
      "incomplete_value": true,
      "site": "00aec1bc",
      "value": [
        "LOAD",
        "8",
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
      "00aec1e4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aec1f4",
      "DATA",
      [
        "storage",
        "010a08f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec1e4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aec1f4",
      "DATA",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec1a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec184.md#insn-00aec1a4) · [`00aec1a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec184.md#insn-00aec1a0) · [`00aec1ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec184.md#insn-00aec1ac)
- 新版 [`00aec1e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec1c8.md#insn-00aec1e8) · [`00aec1e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec1c8.md#insn-00aec1e4) · [`00aec1f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec1c8.md#insn-00aec1f0)

~~~diff
- 00aec1a4 ["INT_ADD", "register:40f0:8", ["const:aec1a4:8", "const:4:8"]]
- 00aec1a4 ["CALL", null, ["callee:00bde180:8"]]
+ 00aec1e8 ["INT_ADD", "register:40f0:8", ["const:aec1e8:8", "const:4:8"]]
+ 00aec1e8 ["CALL", null, ["callee:00bde180:8"]]
- 00aec1a4 bytes e3c70394
+ 00aec1e8 bytes e6c70394
- 00aec1a0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aec1a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec1a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec1a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aec1e4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aec1e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec1e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec1e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec1a0 bytes 00501791
+ 00aec1e4 bytes 001c1591
- 00aec1ac ["COPY", "tmp:0:8", ["const:8f0:8"]]
- 00aec1ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aec1ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aec1ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aec1f0 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 00aec1f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec1f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec1f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aec1ac bytes 08c12391
+ 00aec1f0 bytes 08c12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2e7ed05e8e63b276dc055fceb3af0fc"></a>

### [`00aec1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec1c0.md) → [`00aec204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec204.md) _ZN8firebase4util4list13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aec244",
      "incomplete_value": true,
      "site": "00aec244",
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
            "const:920:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec200",
      "incomplete_value": true,
      "site": "00aec200",
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
            "const:8e0:8"
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
      "definition_site": "00aec220",
      "incomplete_value": true,
      "site": "00aec220",
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
      "definition_site": "00aec1dc",
      "incomplete_value": true,
      "site": "00aec1dc",
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
        "00aec1dc"
      ],
      [
        "FALL_THROUGH",
        "00aec220"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00aec220",
      "incomplete_value": true,
      "site": "00aec244",
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
      "definition_site": "00aec1dc",
      "incomplete_value": true,
      "site": "00aec200",
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
      "00aec218",
      "READ",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec244",
      "WRITE",
      [
        "storage",
        "010a08e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec25c",
      "PARAM",
      [
        "storage",
        "010a0908",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aec218",
      "READ",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec244",
      "WRITE",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec25c",
      "PARAM",
      [
        "storage",
        "010a0948",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec1c0.md#insn-00aec200) · [`00aec1d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec1c0.md#insn-00aec1d4) · [`00aec1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec1c0.md#insn-00aec1f8)
- 新版 [`00aec244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec204.md#insn-00aec244) · [`00aec218`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec204.md#insn-00aec218) · [`00aec23c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec204.md#insn-00aec23c)

~~~diff
- 00aec200 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e0:8"]]
- 00aec200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec244 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00aec244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec200 bytes 807204f9
+ 00aec244 bytes 809204f9
- 00aec1d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e0:8"]]
- 00aec1d4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec218 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00aec218 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec1d4 bytes 817244f9
+ 00aec218 bytes 819244f9
- 00aec1f8 ["INT_ADD", "register:40f0:8", ["const:aec1f8:8", "const:4:8"]]
- 00aec1f8 ["CALL", null, ["callee:00bde090:8"]]
+ 00aec23c ["INT_ADD", "register:40f0:8", ["const:aec23c:8", "const:4:8"]]
+ 00aec23c ["CALL", null, ["callee:00bde090:8"]]
- 00aec1f8 bytes 92c70394
+ 00aec23c bytes 95c70394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7601e4c4a57c3566ce0dcf0d3550a27"></a>

### [`00aec230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec230.md) → [`00aec274`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec274.md) _ZN8firebase4util4list10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aec290",
      "incomplete_value": false,
      "site": "00aec294",
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
      "definition_site": "00aec24c",
      "incomplete_value": false,
      "site": "00aec250",
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
      "definition_site": "00aec2a0",
      "incomplete_value": true,
      "site": "00aec2ac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec25c",
      "incomplete_value": true,
      "site": "00aec268",
      "value": [
        "LOAD",
        "8",
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
      "00aec290",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aec2a0",
      "DATA",
      [
        "storage",
        "010a0908",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aec290",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aec2a0",
      "DATA",
      [
        "storage",
        "010a0948",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec230.md#insn-00aec250) · [`00aec24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec230.md#insn-00aec24c) · [`00aec258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec230.md#insn-00aec258)
- 新版 [`00aec294`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec274.md#insn-00aec294) · [`00aec290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec274.md#insn-00aec290) · [`00aec29c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec274.md#insn-00aec29c)

~~~diff
- 00aec250 ["INT_ADD", "register:40f0:8", ["const:aec250:8", "const:4:8"]]
- 00aec250 ["CALL", null, ["callee:00bde180:8"]]
+ 00aec294 ["INT_ADD", "register:40f0:8", ["const:aec294:8", "const:4:8"]]
+ 00aec294 ["CALL", null, ["callee:00bde180:8"]]
- 00aec250 bytes b8c70394
+ 00aec294 bytes bbc70394
- 00aec24c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aec24c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec24c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec24c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aec290 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aec290 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec290 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec290 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec24c bytes 00fc1991
+ 00aec290 bytes 00c81791
- 00aec258 ["COPY", "tmp:0:8", ["const:908:8"]]
- 00aec258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aec258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aec258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aec29c ["COPY", "tmp:0:8", ["const:948:8"]]
+ 00aec29c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec29c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec29c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aec258 bytes 08212491
+ 00aec29c bytes 08212591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38e4585bcdf3842b516ab86ff7541278"></a>

### [`00aec26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec26c.md) → [`00aec2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2b0.md) _ZN8firebase4util10long_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00aec2dc",
      "incomplete_value": true,
      "site": "00aec2dc",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec298",
      "incomplete_value": true,
      "site": "00aec298",
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
            "const:910:8"
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
      "definition_site": "00aec2c4",
      "incomplete_value": true,
      "site": "00aec2c4",
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
      "definition_site": "00aec280",
      "incomplete_value": true,
      "site": "00aec280",
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
      "definition_site": "00aec2d0",
      "incomplete_value": false,
      "site": "00aec2d4",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec28c",
      "incomplete_value": false,
      "site": "00aec290",
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
            "const:d56:8"
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
      "00aec2c0",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec2d0",
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      "00aec2dc",
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec2c0",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec2d0",
      "PARAM",
      [
        "storage",
        "002a7df0",
        null,
        "string"
      ]
    ],
    [
      "00aec2dc",
      "WRITE",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec26c.md#insn-00aec290) · [`00aec298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec26c.md#insn-00aec298) · [`00aec27c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec26c.md#insn-00aec27c)
- 新版 [`00aec2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2b0.md#insn-00aec2d4) · [`00aec2dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2b0.md#insn-00aec2dc) · [`00aec2c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2b0.md#insn-00aec2c0)

~~~diff
- 00aec290 ["INT_ADD", "register:40f0:8", ["const:aec290:8", "const:4:8"]]
- 00aec290 ["CALL", null, ["callee:00bde090:8"]]
+ 00aec2d4 ["INT_ADD", "register:40f0:8", ["const:aec2d4:8", "const:4:8"]]
+ 00aec2d4 ["CALL", null, ["callee:00bde090:8"]]
- 00aec290 bytes 6cc70394
+ 00aec2d4 bytes 6fc70394
- 00aec298 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aec298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec2dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:950:8"]]
+ 00aec2dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec298 bytes 608a04f9
+ 00aec2dc bytes 60aa04f9
- 00aec27c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aec27c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec2c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:950:8"]]
+ 00aec2c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec27c bytes 688a44f9
+ 00aec2c0 bytes 68aa44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5f89b09a3719943846c184fdacdce76"></a>

### [`00aec2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ac.md) → [`00aec2f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2f0.md) _ZN8firebase4util10long_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aec31c",
      "incomplete_value": true,
      "site": "00aec31c",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec2d8",
      "incomplete_value": true,
      "site": "00aec2d8",
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
            "const:910:8"
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
      "definition_site": "00aec304",
      "incomplete_value": true,
      "site": "00aec304",
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
      "definition_site": "00aec2c0",
      "incomplete_value": true,
      "site": "00aec2c0",
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
      "definition_site": "00aec30c",
      "incomplete_value": false,
      "site": "00aec314",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec2c8",
      "incomplete_value": false,
      "site": "00aec2d0",
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
            "const:d56:8"
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
      "00aec300",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec30c",
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      "00aec31c",
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec300",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec30c",
      "PARAM",
      [
        "storage",
        "002a7df0",
        null,
        "string"
      ]
    ],
    [
      "00aec31c",
      "WRITE",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ac.md#insn-00aec2d0) · [`00aec2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ac.md#insn-00aec2d8) · [`00aec2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ac.md#insn-00aec2bc)
- 新版 [`00aec314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2f0.md#insn-00aec314) · [`00aec31c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2f0.md#insn-00aec31c) · [`00aec300`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec2f0.md#insn-00aec300)

~~~diff
- 00aec2d0 ["INT_ADD", "register:40f0:8", ["const:aec2d0:8", "const:4:8"]]
- 00aec2d0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aec314 ["INT_ADD", "register:40f0:8", ["const:aec314:8", "const:4:8"]]
+ 00aec314 ["CALL", null, ["callee:00bde090:8"]]
- 00aec2d0 bytes 5cc70394
+ 00aec314 bytes 5fc70394
- 00aec2d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aec2d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec31c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:950:8"]]
+ 00aec31c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec2d8 bytes 608a04f9
+ 00aec31c bytes 60aa04f9
- 00aec2bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aec2bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec300 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:950:8"]]
+ 00aec300 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec2bc bytes 688a44f9
+ 00aec300 bytes 68aa44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b84e1d130a5ba882ccf7dc9bf85a9cb2"></a>

### [`00aec2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ec.md) → [`00aec330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec330.md) _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00aec360",
      "incomplete_value": true,
      "site": "00aec360",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec31c",
      "incomplete_value": true,
      "site": "00aec31c",
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
            "const:910:8"
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
      "definition_site": "00aec344",
      "incomplete_value": true,
      "site": "00aec344",
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
      "definition_site": "00aec300",
      "incomplete_value": true,
      "site": "00aec300",
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
      "definition_site": "00aec350",
      "incomplete_value": false,
      "site": "00aec358",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec30c",
      "incomplete_value": false,
      "site": "00aec314",
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
            "const:d56:8"
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
      "00aec340",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec350",
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      "00aec360",
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec340",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec350",
      "PARAM",
      [
        "storage",
        "002a7df0",
        null,
        "string"
      ]
    ],
    [
      "00aec360",
      "WRITE",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ec.md#insn-00aec314) · [`00aec31c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ec.md#insn-00aec31c) · [`00aec2fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ec.md#insn-00aec2fc)
- 新版 [`00aec358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec330.md#insn-00aec358) · [`00aec360`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec330.md#insn-00aec360) · [`00aec340`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec330.md#insn-00aec340)

~~~diff
- 00aec314 ["INT_ADD", "register:40f0:8", ["const:aec314:8", "const:4:8"]]
- 00aec314 ["CALL", null, ["callee:00bde090:8"]]
+ 00aec358 ["INT_ADD", "register:40f0:8", ["const:aec358:8", "const:4:8"]]
+ 00aec358 ["CALL", null, ["callee:00bde090:8"]]
- 00aec314 bytes 4bc70394
+ 00aec358 bytes 4ec70394
- 00aec31c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aec31c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec360 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:950:8"]]
+ 00aec360 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec31c bytes 608a04f9
+ 00aec360 bytes 60aa04f9
- 00aec2fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aec2fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec340 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:950:8"]]
+ 00aec340 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec2fc bytes 688a44f9
+ 00aec340 bytes 68aa44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b838bc2e9ef73e07213da66b96636c0"></a>

### [`00aec330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec330.md) → [`00aec374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec374.md) _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aec3a4",
      "incomplete_value": true,
      "site": "00aec3a4",
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
            "const:950:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec360",
      "incomplete_value": true,
      "site": "00aec360",
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
            "const:910:8"
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
      "definition_site": "00aec388",
      "incomplete_value": true,
      "site": "00aec388",
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
      "definition_site": "00aec344",
      "incomplete_value": true,
      "site": "00aec344",
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
      "definition_site": "00aec390",
      "incomplete_value": false,
      "site": "00aec39c",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec34c",
      "incomplete_value": false,
      "site": "00aec358",
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
            "const:d56:8"
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
      "00aec384",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec390",
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      "00aec3a4",
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec384",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec390",
      "PARAM",
      [
        "storage",
        "002a7df0",
        null,
        "string"
      ]
    ],
    [
      "00aec3a4",
      "WRITE",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec330.md#insn-00aec358) · [`00aec360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec330.md#insn-00aec360) · [`00aec340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec330.md#insn-00aec340)
- 新版 [`00aec39c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec374.md#insn-00aec39c) · [`00aec3a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec374.md#insn-00aec3a4) · [`00aec384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec374.md#insn-00aec384)

~~~diff
- 00aec358 ["INT_ADD", "register:40f0:8", ["const:aec358:8", "const:4:8"]]
- 00aec358 ["CALL", null, ["callee:00bde090:8"]]
+ 00aec39c ["INT_ADD", "register:40f0:8", ["const:aec39c:8", "const:4:8"]]
+ 00aec39c ["CALL", null, ["callee:00bde090:8"]]
- 00aec358 bytes 3ac70394
+ 00aec39c bytes 3dc70394
- 00aec360 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aec360 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec3a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:950:8"]]
+ 00aec3a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec360 bytes 608a04f9
+ 00aec3a4 bytes 60aa04f9
- 00aec340 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aec340 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec384 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:950:8"]]
+ 00aec384 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec340 bytes 688a44f9
+ 00aec384 bytes 68aa44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc66bbb68a8be57c90ef920d8767e4fe"></a>

### [`00aec380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec380.md) → [`00aec3c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec3c4.md) _ZN8firebase4util10long_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec44c",
      "incomplete_value": true,
      "site": "00aec44c",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec408",
      "incomplete_value": true,
      "site": "00aec408",
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
            "const:918:8"
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
      "definition_site": "00aec3f8",
      "incomplete_value": true,
      "site": "00aec404",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:950:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec3b4",
      "incomplete_value": true,
      "site": "00aec3c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:910:8"
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
      "00aec3d8",
      "READ",
      [
        "storage",
        "010a0918",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec3f8",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec44c",
      "WRITE",
      [
        "storage",
        "010a0918",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aec3d8",
      "READ",
      [
        "storage",
        "010a0958",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec3f8",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec44c",
      "WRITE",
      [
        "storage",
        "010a0958",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec380.md#insn-00aec3c0) · [`00aec408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec380.md#insn-00aec408) · [`00aec394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec380.md#insn-00aec394)
- 新版 [`00aec404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec3c4.md#insn-00aec404) · [`00aec44c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec3c4.md#insn-00aec44c) · [`00aec3d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec3c4.md#insn-00aec3d8)

~~~diff
- 00aec3c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec3c0 ["INT_ADD", "register:40f0:8", ["const:aec3c0:8", "const:4:8"]]
- 00aec3c0 ["CALLIND", null, ["register:0:8"]]
+ 00aec404 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aec404 ["INT_ADD", "register:40f0:8", ["const:aec404:8", "const:4:8"]]
+ 00aec404 ["CALLIND", null, ["register:0:8"]]
- 00aec3c0 bytes 00013fd6
+ 00aec404 bytes 00013fd6
- 00aec408 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aec408 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:918:8"]]
- 00aec408 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aec44c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aec44c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:958:8"]]
+ 00aec44c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aec408 bytes a0622439
+ 00aec44c bytes a0622539
- 00aec394 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:918:8"]]
- 00aec394 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aec394 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aec3d8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:958:8"]]
+ 00aec3d8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aec3d8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aec394 bytes a8626439
+ 00aec3d8 bytes a8626539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-915584bab44b8e3e35fa77d4ad84a40c"></a>

### [`00aec41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec41c.md) → [`00aec460`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec460.md) _ZN8firebase4util10long_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00aec49c",
      "incomplete_value": true,
      "site": "00aec49c",
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
            "const:958:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec458",
      "incomplete_value": true,
      "site": "00aec458",
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
            "const:918:8"
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
      "definition_site": "00aec4ec",
      "incomplete_value": true,
      "site": "00aec4ec",
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
    "old": {
      "definition_site": "00aec4a8",
      "incomplete_value": true,
      "site": "00aec4a8",
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
            "const:910:8"
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
      "definition_site": "00aec478",
      "incomplete_value": true,
      "site": "00aec478",
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
      "definition_site": "00aec434",
      "incomplete_value": true,
      "site": "00aec434",
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
      "00aec474",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec480",
      "READ",
      [
        "storage",
        "010a0918",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec49c",
      "WRITE",
      [
        "storage",
        "010a0918",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aec474",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec480",
      "READ",
      [
        "storage",
        "010a0958",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec49c",
      "WRITE",
      [
        "storage",
        "010a0958",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec41c.md#insn-00aec458) · [`00aec4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec41c.md#insn-00aec4a4) · [`00aec4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec41c.md#insn-00aec4a8)
- 新版 [`00aec49c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec460.md#insn-00aec49c) · [`00aec4e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec460.md#insn-00aec4e8) · [`00aec4ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec460.md#insn-00aec4ec)

~~~diff
- 00aec458 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aec458 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aec458 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:918:8"]]
- 00aec458 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aec49c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aec49c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aec49c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:958:8"]]
+ 00aec49c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aec458 bytes bf622439
+ 00aec49c bytes bf622539
- 00aec4a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec4a4 ["INT_ADD", "register:40f0:8", ["const:aec4a4:8", "const:4:8"]]
- 00aec4a4 ["CALLIND", null, ["register:0:8"]]
+ 00aec4e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aec4e8 ["INT_ADD", "register:40f0:8", ["const:aec4e8:8", "const:4:8"]]
+ 00aec4e8 ["CALLIND", null, ["register:0:8"]]
- 00aec4a4 bytes 00013fd6
+ 00aec4e8 bytes 00013fd6
- 00aec4a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00aec4a8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aec4a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aec4ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:950:8"]]
+ 00aec4ec ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aec4ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aec4a8 bytes 9f8a04f9
+ 00aec4ec bytes 9faa04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c94191c7f0358356ddead34d0110cc90"></a>

### [`00aec4bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec4bc.md) → [`00aec500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec500.md) _ZN8firebase4util10long_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aec540",
      "incomplete_value": true,
      "site": "00aec540",
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
    "old": {
      "definition_site": "00aec4fc",
      "incomplete_value": true,
      "site": "00aec4fc",
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
            "const:910:8"
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
      "definition_site": "00aec51c",
      "incomplete_value": true,
      "site": "00aec51c",
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
      "definition_site": "00aec4d8",
      "incomplete_value": true,
      "site": "00aec4d8",
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
      "definition_site": "00aec524",
      "incomplete_value": false,
      "site": "00aec538",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec4e0",
      "incomplete_value": false,
      "site": "00aec4f4",
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
            "const:d56:8"
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
      "00aec514",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec524",
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      "00aec540",
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec514",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec524",
      "PARAM",
      [
        "storage",
        "002a7df0",
        null,
        "string"
      ]
    ],
    [
      "00aec540",
      "WRITE",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec4bc.md#insn-00aec4f4) · [`00aec4fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec4bc.md#insn-00aec4fc) · [`00aec4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec4bc.md#insn-00aec4d0)
- 新版 [`00aec538`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec500.md#insn-00aec538) · [`00aec540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec500.md#insn-00aec540) · [`00aec514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec500.md#insn-00aec514)

~~~diff
- 00aec4f4 ["INT_ADD", "register:40f0:8", ["const:aec4f4:8", "const:4:8"]]
- 00aec4f4 ["CALL", null, ["callee:00bde090:8"]]
+ 00aec538 ["INT_ADD", "register:40f0:8", ["const:aec538:8", "const:4:8"]]
+ 00aec538 ["CALL", null, ["callee:00bde090:8"]]
- 00aec4f4 bytes d3c60394
+ 00aec538 bytes d6c60394
- 00aec4fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00aec4fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec540 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:950:8"]]
+ 00aec540 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec4fc bytes 808a04f9
+ 00aec540 bytes 80aa04f9
- 00aec4d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00aec4d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec514 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:950:8"]]
+ 00aec514 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec4d0 bytes 818a44f9
+ 00aec514 bytes 81aa44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fda76991267abdf63dde3e72990712de"></a>

### [`00aec52c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec52c.md) → [`00aec570`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec570.md) _ZN8firebase4util10long_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde3a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde3a0.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde3f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3f0.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00aec58c",
      "incomplete_value": false,
      "site": "00aec590",
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
      "definition_site": "00aec548",
      "incomplete_value": false,
      "site": "00aec54c",
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
      "definition_site": "00aec59c",
      "incomplete_value": true,
      "site": "00aec5a8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec558",
      "incomplete_value": true,
      "site": "00aec564",
      "value": [
        "LOAD",
        "8",
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
      "00aec58c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aec59c",
      "DATA",
      [
        "storage",
        "010a0920",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec58c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aec59c",
      "DATA",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec54c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec52c.md#insn-00aec54c) · [`00aec548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec52c.md#insn-00aec548) · [`00aec554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec52c.md#insn-00aec554)
- 新版 [`00aec590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec570.md#insn-00aec590) · [`00aec58c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec570.md#insn-00aec58c) · [`00aec598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec570.md#insn-00aec598)

~~~diff
- 00aec54c ["INT_ADD", "register:40f0:8", ["const:aec54c:8", "const:4:8"]]
- 00aec54c ["CALL", null, ["callee:00bde180:8"]]
+ 00aec590 ["INT_ADD", "register:40f0:8", ["const:aec590:8", "const:4:8"]]
+ 00aec590 ["CALL", null, ["callee:00bde180:8"]]
- 00aec54c bytes f9c60394
+ 00aec590 bytes fcc60394
- 00aec548 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aec548 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec548 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec548 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aec58c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aec58c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec58c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec58c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec548 bytes 00501791
+ 00aec58c bytes 001c1591
- 00aec554 ["COPY", "tmp:0:8", ["const:920:8"]]
- 00aec554 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aec554 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aec554 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aec598 ["COPY", "tmp:0:8", ["const:960:8"]]
+ 00aec598 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec598 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec598 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aec554 bytes 08812491
+ 00aec598 bytes 08812591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c518fc102bf129b68775aa9d852f41f"></a>

### [`00aec568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec568.md) → [`00aec5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec5ac.md) _ZN8firebase4util10long_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aec5ec",
      "incomplete_value": true,
      "site": "00aec5ec",
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
    "old": {
      "definition_site": "00aec5a8",
      "incomplete_value": true,
      "site": "00aec5a8",
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
            "const:910:8"
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
      "definition_site": "00aec5c8",
      "incomplete_value": true,
      "site": "00aec5c8",
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
      "definition_site": "00aec584",
      "incomplete_value": true,
      "site": "00aec584",
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
      "definition_site": "00aec5d0",
      "incomplete_value": false,
      "site": "00aec5e4",
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
            "const:df0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec58c",
      "incomplete_value": false,
      "site": "00aec5a0",
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
            "const:d56:8"
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
      "00aec5c0",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec5d0",
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      "00aec5ec",
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec5c0",
      "READ",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec5d0",
      "PARAM",
      [
        "storage",
        "002a7df0",
        null,
        "string"
      ]
    ],
    [
      "00aec5ec",
      "WRITE",
      [
        "storage",
        "010a0950",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec568.md#insn-00aec5a0) · [`00aec5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec568.md#insn-00aec5a8) · [`00aec57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec568.md#insn-00aec57c)
- 新版 [`00aec5e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec5ac.md#insn-00aec5e4) · [`00aec5ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec5ac.md#insn-00aec5ec) · [`00aec5c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec5ac.md#insn-00aec5c0)

~~~diff
- 00aec5a0 ["INT_ADD", "register:40f0:8", ["const:aec5a0:8", "const:4:8"]]
- 00aec5a0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aec5e4 ["INT_ADD", "register:40f0:8", ["const:aec5e4:8", "const:4:8"]]
+ 00aec5e4 ["CALL", null, ["callee:00bde090:8"]]
- 00aec5a0 bytes a8c60394
+ 00aec5e4 bytes abc60394
- 00aec5a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00aec5a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec5ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:950:8"]]
+ 00aec5ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec5a8 bytes 808a04f9
+ 00aec5ec bytes 80aa04f9
- 00aec57c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00aec57c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec5c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:950:8"]]
+ 00aec5c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec57c bytes 818a44f9
+ 00aec5c0 bytes 81aa44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a94f3699f1eb509e9f1413cde0af4bb7"></a>

### [`00aec5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec5d8.md) → [`00aec61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec61c.md) _ZN8firebase4util10long_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aec638",
      "incomplete_value": false,
      "site": "00aec63c",
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
      "definition_site": "00aec5f4",
      "incomplete_value": false,
      "site": "00aec5f8",
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
      "definition_site": "00aec648",
      "incomplete_value": true,
      "site": "00aec654",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec604",
      "incomplete_value": true,
      "site": "00aec610",
      "value": [
        "LOAD",
        "8",
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
      "00aec638",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aec648",
      "DATA",
      [
        "storage",
        "010a0930",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aec638",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aec648",
      "DATA",
      [
        "storage",
        "010a0970",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec5f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec5d8.md#insn-00aec5f8) · [`00aec5f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec5d8.md#insn-00aec5f4) · [`00aec600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec5d8.md#insn-00aec600)
- 新版 [`00aec63c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec61c.md#insn-00aec63c) · [`00aec638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec61c.md#insn-00aec638) · [`00aec644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec61c.md#insn-00aec644)

~~~diff
- 00aec5f8 ["INT_ADD", "register:40f0:8", ["const:aec5f8:8", "const:4:8"]]
- 00aec5f8 ["CALL", null, ["callee:00bde180:8"]]
+ 00aec63c ["INT_ADD", "register:40f0:8", ["const:aec63c:8", "const:4:8"]]
+ 00aec63c ["CALL", null, ["callee:00bde180:8"]]
- 00aec5f8 bytes cec60394
+ 00aec63c bytes d1c60394
- 00aec5f4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aec5f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec5f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec5f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aec638 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aec638 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec638 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec638 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec5f4 bytes 00fc1991
+ 00aec638 bytes 00c81791
- 00aec600 ["COPY", "tmp:0:8", ["const:930:8"]]
- 00aec600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aec600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aec600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aec644 ["COPY", "tmp:0:8", ["const:970:8"]]
+ 00aec644 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec644 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec644 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aec600 bytes 08c12491
+ 00aec644 bytes 08c12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53be60c925647680150874a199b5cc51"></a>

### [`00aec614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec614.md) → [`00aec658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec658.md) _ZN8firebase4util3map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
      "definition_site": "00aec684",
      "incomplete_value": true,
      "site": "00aec684",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec640",
      "incomplete_value": true,
      "site": "00aec640",
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
            "const:938:8"
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
      "definition_site": "00aec66c",
      "incomplete_value": true,
      "site": "00aec66c",
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
      "definition_site": "00aec628",
      "incomplete_value": true,
      "site": "00aec628",
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
      "definition_site": "00aec678",
      "incomplete_value": false,
      "site": "00aec67c",
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
            "const:f85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec634",
      "incomplete_value": false,
      "site": "00aec638",
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
            "const:efa:8"
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
      "00aec668",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec678",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ],
    [
      "00aec684",
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec668",
      "READ",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec678",
      "PARAM",
      [
        "storage",
        "002a0f85",
        null,
        "string"
      ]
    ],
    [
      "00aec684",
      "WRITE",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec614.md#insn-00aec638) · [`00aec640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec614.md#insn-00aec640) · [`00aec624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec614.md#insn-00aec624)
- 新版 [`00aec67c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec658.md#insn-00aec67c) · [`00aec684`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec658.md#insn-00aec684) · [`00aec668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec658.md#insn-00aec668)

~~~diff
- 00aec638 ["INT_ADD", "register:40f0:8", ["const:aec638:8", "const:4:8"]]
- 00aec638 ["CALL", null, ["callee:00bde090:8"]]
+ 00aec67c ["INT_ADD", "register:40f0:8", ["const:aec67c:8", "const:4:8"]]
+ 00aec67c ["CALL", null, ["callee:00bde090:8"]]
- 00aec638 bytes 82c60394
+ 00aec67c bytes 85c60394
- 00aec640 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
- 00aec640 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec684 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:978:8"]]
+ 00aec684 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec640 bytes 609e04f9
+ 00aec684 bytes 60be04f9
- 00aec624 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
- 00aec624 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec668 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:978:8"]]
+ 00aec668 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec624 bytes 689e44f9
+ 00aec668 bytes 68be44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b0a0dd2a1a890405a976820f3a139dc"></a>

### [`00aec654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec654.md) → [`00aec698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec698.md) _ZN8firebase4util3map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aec6c4",
      "incomplete_value": true,
      "site": "00aec6c4",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec680",
      "incomplete_value": true,
      "site": "00aec680",
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
            "const:938:8"
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
      "definition_site": "00aec6ac",
      "incomplete_value": true,
      "site": "00aec6ac",
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
      "definition_site": "00aec668",
      "incomplete_value": true,
      "site": "00aec668",
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
      "definition_site": "00aec6b4",
      "incomplete_value": false,
      "site": "00aec6bc",
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
            "const:f85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec670",
      "incomplete_value": false,
      "site": "00aec678",
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
            "const:efa:8"
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
      "00aec6a8",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec6b4",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ],
    [
      "00aec6c4",
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec6a8",
      "READ",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec6b4",
      "PARAM",
      [
        "storage",
        "002a0f85",
        null,
        "string"
      ]
    ],
    [
      "00aec6c4",
      "WRITE",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec654.md#insn-00aec678) · [`00aec680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec654.md#insn-00aec680) · [`00aec664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec654.md#insn-00aec664)
- 新版 [`00aec6bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec698.md#insn-00aec6bc) · [`00aec6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec698.md#insn-00aec6c4) · [`00aec6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec698.md#insn-00aec6a8)

~~~diff
- 00aec678 ["INT_ADD", "register:40f0:8", ["const:aec678:8", "const:4:8"]]
- 00aec678 ["CALL", null, ["callee:00bde090:8"]]
+ 00aec6bc ["INT_ADD", "register:40f0:8", ["const:aec6bc:8", "const:4:8"]]
+ 00aec6bc ["CALL", null, ["callee:00bde090:8"]]
- 00aec678 bytes 72c60394
+ 00aec6bc bytes 75c60394
- 00aec680 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
- 00aec680 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec6c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:978:8"]]
+ 00aec6c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec680 bytes 609e04f9
+ 00aec6c4 bytes 60be04f9
- 00aec664 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
- 00aec664 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec6a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:978:8"]]
+ 00aec6a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec664 bytes 689e44f9
+ 00aec6a8 bytes 68be44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-562931f512245f0ed93140b1f03b4933"></a>

### [`00aec694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec694.md) → [`00aec6d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec6d8.md) _ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 76.47% / 新版 76.47%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec708",
      "incomplete_value": true,
      "site": "00aec708",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec6c4",
      "incomplete_value": true,
      "site": "00aec6c4",
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
            "const:938:8"
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
      "definition_site": "00aec6ec",
      "incomplete_value": true,
      "site": "00aec6ec",
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
      "definition_site": "00aec6a8",
      "incomplete_value": true,
      "site": "00aec6a8",
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
      "definition_site": "00aec6f8",
      "incomplete_value": false,
      "site": "00aec700",
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
            "const:f85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec6b4",
      "incomplete_value": false,
      "site": "00aec6bc",
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
            "const:efa:8"
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
      "00aec6e8",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec6f8",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ],
    [
      "00aec708",
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec6e8",
      "READ",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec6f8",
      "PARAM",
      [
        "storage",
        "002a0f85",
        null,
        "string"
      ]
    ],
    [
      "00aec708",
      "WRITE",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec6bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec694.md#insn-00aec6bc) · [`00aec6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec694.md#insn-00aec6c4) · [`00aec6a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec694.md#insn-00aec6a4)
- 新版 [`00aec700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec6d8.md#insn-00aec700) · [`00aec708`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec6d8.md#insn-00aec708) · [`00aec6e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec6d8.md#insn-00aec6e8)

~~~diff
- 00aec6bc ["INT_ADD", "register:40f0:8", ["const:aec6bc:8", "const:4:8"]]
- 00aec6bc ["CALL", null, ["callee:00bde090:8"]]
+ 00aec700 ["INT_ADD", "register:40f0:8", ["const:aec700:8", "const:4:8"]]
+ 00aec700 ["CALL", null, ["callee:00bde090:8"]]
- 00aec6bc bytes 61c60394
+ 00aec700 bytes 64c60394
- 00aec6c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
- 00aec6c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec708 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:978:8"]]
+ 00aec708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec6c4 bytes 609e04f9
+ 00aec708 bytes 60be04f9
- 00aec6a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
- 00aec6a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec6e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:978:8"]]
+ 00aec6e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec6a4 bytes 689e44f9
+ 00aec6e8 bytes 68be44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-725fd428a4e9bcdaeee154f09642f714"></a>

### [`00aec6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec6d8.md) → [`00aec71c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec71c.md) _ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aec74c",
      "incomplete_value": true,
      "site": "00aec74c",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec708",
      "incomplete_value": true,
      "site": "00aec708",
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
            "const:938:8"
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
      "definition_site": "00aec730",
      "incomplete_value": true,
      "site": "00aec730",
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
      "definition_site": "00aec6ec",
      "incomplete_value": true,
      "site": "00aec6ec",
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
      "definition_site": "00aec738",
      "incomplete_value": false,
      "site": "00aec744",
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
            "const:f85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec6f4",
      "incomplete_value": false,
      "site": "00aec700",
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
            "const:efa:8"
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
      "00aec72c",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec738",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ],
    [
      "00aec74c",
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec72c",
      "READ",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec738",
      "PARAM",
      [
        "storage",
        "002a0f85",
        null,
        "string"
      ]
    ],
    [
      "00aec74c",
      "WRITE",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec6d8.md#insn-00aec700) · [`00aec708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec6d8.md#insn-00aec708) · [`00aec6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec6d8.md#insn-00aec6e8)
- 新版 [`00aec744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec71c.md#insn-00aec744) · [`00aec74c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec71c.md#insn-00aec74c) · [`00aec72c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec71c.md#insn-00aec72c)

~~~diff
- 00aec700 ["INT_ADD", "register:40f0:8", ["const:aec700:8", "const:4:8"]]
- 00aec700 ["CALL", null, ["callee:00bde090:8"]]
+ 00aec744 ["INT_ADD", "register:40f0:8", ["const:aec744:8", "const:4:8"]]
+ 00aec744 ["CALL", null, ["callee:00bde090:8"]]
- 00aec700 bytes 50c60394
+ 00aec744 bytes 53c60394
- 00aec708 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
- 00aec708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec74c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:978:8"]]
+ 00aec74c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec708 bytes 609e04f9
+ 00aec74c bytes 60be04f9
- 00aec6e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
- 00aec6e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec72c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:978:8"]]
+ 00aec72c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec6e8 bytes 689e44f9
+ 00aec72c bytes 68be44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-236d141215632241ad830e1679699c70"></a>

### [`00aec728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec728.md) → [`00aec76c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec76c.md) _ZN8firebase4util3map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aec7f4",
      "incomplete_value": true,
      "site": "00aec7f4",
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
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec7b0",
      "incomplete_value": true,
      "site": "00aec7b0",
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
            "const:940:8"
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
      "definition_site": "00aec7a0",
      "incomplete_value": true,
      "site": "00aec7ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:978:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec75c",
      "incomplete_value": true,
      "site": "00aec768",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:938:8"
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
      "00aec780",
      "READ",
      [
        "storage",
        "010a0940",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec7a0",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec7f4",
      "WRITE",
      [
        "storage",
        "010a0940",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aec780",
      "READ",
      [
        "storage",
        "010a0980",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec7a0",
      "READ",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec7f4",
      "WRITE",
      [
        "storage",
        "010a0980",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec728.md#insn-00aec768) · [`00aec7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec728.md#insn-00aec7b0) · [`00aec73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec728.md#insn-00aec73c)
- 新版 [`00aec7ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec76c.md#insn-00aec7ac) · [`00aec7f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec76c.md#insn-00aec7f4) · [`00aec780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec76c.md#insn-00aec780)

~~~diff
- 00aec768 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec768 ["INT_ADD", "register:40f0:8", ["const:aec768:8", "const:4:8"]]
- 00aec768 ["CALLIND", null, ["register:0:8"]]
+ 00aec7ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aec7ac ["INT_ADD", "register:40f0:8", ["const:aec7ac:8", "const:4:8"]]
+ 00aec7ac ["CALLIND", null, ["register:0:8"]]
- 00aec768 bytes 00013fd6
+ 00aec7ac bytes 00013fd6
- 00aec7b0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aec7b0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:940:8"]]
- 00aec7b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aec7f4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aec7f4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:980:8"]]
+ 00aec7f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aec7b0 bytes a0022539
+ 00aec7f4 bytes a0022639
- 00aec73c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:940:8"]]
- 00aec73c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aec73c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aec780 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:980:8"]]
+ 00aec780 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aec780 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aec73c bytes a8026539
+ 00aec780 bytes a8026639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4a73cd9ce56dd7469ef8949452e212b3"></a>

### [`00aec7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec7c4.md) → [`00aec808`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec808.md) _ZN8firebase4util3map12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00aec844",
      "incomplete_value": true,
      "site": "00aec844",
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
            "const:980:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec800",
      "incomplete_value": true,
      "site": "00aec800",
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
            "const:940:8"
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
      "definition_site": "00aec894",
      "incomplete_value": true,
      "site": "00aec894",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec850",
      "incomplete_value": true,
      "site": "00aec850",
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
            "const:938:8"
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
      "definition_site": "00aec820",
      "incomplete_value": true,
      "site": "00aec820",
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
      "definition_site": "00aec7dc",
      "incomplete_value": true,
      "site": "00aec7dc",
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
      "00aec81c",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec828",
      "READ",
      [
        "storage",
        "010a0940",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec844",
      "WRITE",
      [
        "storage",
        "010a0940",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aec81c",
      "READ",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec828",
      "READ",
      [
        "storage",
        "010a0980",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec844",
      "WRITE",
      [
        "storage",
        "010a0980",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec7c4.md#insn-00aec800) · [`00aec84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec7c4.md#insn-00aec84c) · [`00aec850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec7c4.md#insn-00aec850)
- 新版 [`00aec844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec808.md#insn-00aec844) · [`00aec890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec808.md#insn-00aec890) · [`00aec894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec808.md#insn-00aec894)

~~~diff
- 00aec800 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aec800 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aec800 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:940:8"]]
- 00aec800 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aec844 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aec844 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aec844 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:980:8"]]
+ 00aec844 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aec800 bytes bf022539
+ 00aec844 bytes bf022639
- 00aec84c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec84c ["INT_ADD", "register:40f0:8", ["const:aec84c:8", "const:4:8"]]
- 00aec84c ["CALLIND", null, ["register:0:8"]]
+ 00aec890 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aec890 ["INT_ADD", "register:40f0:8", ["const:aec890:8", "const:4:8"]]
+ 00aec890 ["CALLIND", null, ["register:0:8"]]
- 00aec84c bytes 00013fd6
+ 00aec890 bytes 00013fd6
- 00aec850 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:938:8"]]
- 00aec850 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aec850 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aec894 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:978:8"]]
+ 00aec894 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aec894 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aec850 bytes 9f9e04f9
+ 00aec894 bytes 9fbe04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76aa65657bc60e3a7efbeb29e1384435"></a>

### [`00aec864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec864.md) → [`00aec8a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec8a8.md) _ZN8firebase4util3map14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aec8e8",
      "incomplete_value": true,
      "site": "00aec8e8",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec8a4",
      "incomplete_value": true,
      "site": "00aec8a4",
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
            "const:938:8"
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
      "definition_site": "00aec8c4",
      "incomplete_value": true,
      "site": "00aec8c4",
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
      "definition_site": "00aec880",
      "incomplete_value": true,
      "site": "00aec880",
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
      "definition_site": "00aec8cc",
      "incomplete_value": false,
      "site": "00aec8e0",
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
            "const:f85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec888",
      "incomplete_value": false,
      "site": "00aec89c",
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
            "const:efa:8"
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
      "00aec8bc",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec8cc",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ],
    [
      "00aec8e8",
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec8bc",
      "READ",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec8cc",
      "PARAM",
      [
        "storage",
        "002a0f85",
        null,
        "string"
      ]
    ],
    [
      "00aec8e8",
      "WRITE",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec864.md#insn-00aec89c) · [`00aec8a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec864.md#insn-00aec8a4) · [`00aec878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec864.md#insn-00aec878)
- 新版 [`00aec8e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec8a8.md#insn-00aec8e0) · [`00aec8e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec8a8.md#insn-00aec8e8) · [`00aec8bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec8a8.md#insn-00aec8bc)

~~~diff
- 00aec89c ["INT_ADD", "register:40f0:8", ["const:aec89c:8", "const:4:8"]]
- 00aec89c ["CALL", null, ["callee:00bde090:8"]]
+ 00aec8e0 ["INT_ADD", "register:40f0:8", ["const:aec8e0:8", "const:4:8"]]
+ 00aec8e0 ["CALL", null, ["callee:00bde090:8"]]
- 00aec89c bytes e9c50394
+ 00aec8e0 bytes ecc50394
- 00aec8a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:938:8"]]
- 00aec8a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec8e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:978:8"]]
+ 00aec8e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec8a4 bytes 809e04f9
+ 00aec8e8 bytes 80be04f9
- 00aec878 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:938:8"]]
- 00aec878 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec8bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:978:8"]]
+ 00aec8bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec878 bytes 819e44f9
+ 00aec8bc bytes 81be44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2b13ca8283b5e26f3b2f3a1abab8947"></a>

### [`00aec8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec8d4.md) → [`00aec918`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec918.md) _ZN8firebase4util3map11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0b0.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde100`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde100.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00aec934",
      "incomplete_value": false,
      "site": "00aec938",
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
      "definition_site": "00aec8f0",
      "incomplete_value": false,
      "site": "00aec8f4",
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
      "definition_site": "00aec944",
      "incomplete_value": true,
      "site": "00aec950",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec900",
      "incomplete_value": true,
      "site": "00aec90c",
      "value": [
        "LOAD",
        "8",
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
      "00aec934",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aec944",
      "DATA",
      [
        "storage",
        "010a0948",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec934",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aec944",
      "DATA",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec8d4.md#insn-00aec8f4) · [`00aec8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec8d4.md#insn-00aec8f0) · [`00aec8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec8d4.md#insn-00aec8fc)
- 新版 [`00aec938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec918.md#insn-00aec938) · [`00aec934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec918.md#insn-00aec934) · [`00aec940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec918.md#insn-00aec940)

~~~diff
- 00aec8f4 ["INT_ADD", "register:40f0:8", ["const:aec8f4:8", "const:4:8"]]
- 00aec8f4 ["CALL", null, ["callee:00bde180:8"]]
+ 00aec938 ["INT_ADD", "register:40f0:8", ["const:aec938:8", "const:4:8"]]
+ 00aec938 ["CALL", null, ["callee:00bde180:8"]]
- 00aec8f4 bytes 0fc60394
+ 00aec938 bytes 12c60394
- 00aec8f0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aec8f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec8f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec8f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aec934 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aec934 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec934 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec934 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec8f0 bytes 00501791
+ 00aec934 bytes 001c1591
- 00aec8fc ["COPY", "tmp:0:8", ["const:948:8"]]
- 00aec8fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aec8fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aec8fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aec940 ["COPY", "tmp:0:8", ["const:988:8"]]
+ 00aec940 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec940 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec940 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aec8fc bytes 08212591
+ 00aec940 bytes 08212691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4a7a933ddc87dca9c8d5c73d34937b6"></a>

### [`00aec910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec910.md) → [`00aec954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec954.md) _ZN8firebase4util3map13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aec994",
      "incomplete_value": true,
      "site": "00aec994",
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
            "const:978:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec950",
      "incomplete_value": true,
      "site": "00aec950",
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
            "const:938:8"
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
      "definition_site": "00aec978",
      "incomplete_value": false,
      "site": "00aec98c",
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
            "const:f85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec934",
      "incomplete_value": false,
      "site": "00aec948",
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
            "const:efa:8"
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
      "00aec968",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec978",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ],
    [
      "00aec994",
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec968",
      "READ",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec978",
      "PARAM",
      [
        "storage",
        "002a0f85",
        null,
        "string"
      ]
    ],
    [
      "00aec994",
      "WRITE",
      [
        "storage",
        "010a0978",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec910.md#insn-00aec948) · [`00aec950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec910.md#insn-00aec950) · [`00aec924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec910.md#insn-00aec924)
- 新版 [`00aec98c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec954.md#insn-00aec98c) · [`00aec994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec954.md#insn-00aec994) · [`00aec968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec954.md#insn-00aec968)

~~~diff
- 00aec948 ["INT_ADD", "register:40f0:8", ["const:aec948:8", "const:4:8"]]
- 00aec948 ["CALL", null, ["callee:00bde090:8"]]
+ 00aec98c ["INT_ADD", "register:40f0:8", ["const:aec98c:8", "const:4:8"]]
+ 00aec98c ["CALL", null, ["callee:00bde090:8"]]
- 00aec948 bytes bec50394
+ 00aec98c bytes c1c50394
- 00aec950 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:938:8"]]
- 00aec950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec994 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:978:8"]]
+ 00aec994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec950 bytes 809e04f9
+ 00aec994 bytes 80be04f9
- 00aec924 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:938:8"]]
- 00aec924 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec968 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:978:8"]]
+ 00aec968 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec924 bytes 819e44f9
+ 00aec968 bytes 81be44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29c08991b20fe1610abdfe0a1c960855"></a>

### [`00aec980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec980.md) → [`00aec9c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec9c4.md) _ZN8firebase4util3map10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aec9e0",
      "incomplete_value": false,
      "site": "00aec9e4",
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
      "definition_site": "00aec99c",
      "incomplete_value": false,
      "site": "00aec9a0",
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
      "definition_site": "00aec9f0",
      "incomplete_value": true,
      "site": "00aec9fc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aec9ac",
      "incomplete_value": true,
      "site": "00aec9b8",
      "value": [
        "LOAD",
        "8",
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
      "00aec9e0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aec9f0",
      "DATA",
      [
        "storage",
        "010a0960",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aec9e0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aec9f0",
      "DATA",
      [
        "storage",
        "010a09a0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec980.md#insn-00aec9a0) · [`00aec99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec980.md#insn-00aec99c) · [`00aec9a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec980.md#insn-00aec9a8)
- 新版 [`00aec9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec9c4.md#insn-00aec9e4) · [`00aec9e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec9c4.md#insn-00aec9e0) · [`00aec9ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aec9c4.md#insn-00aec9ec)

~~~diff
- 00aec9a0 ["INT_ADD", "register:40f0:8", ["const:aec9a0:8", "const:4:8"]]
- 00aec9a0 ["CALL", null, ["callee:00bde180:8"]]
+ 00aec9e4 ["INT_ADD", "register:40f0:8", ["const:aec9e4:8", "const:4:8"]]
+ 00aec9e4 ["CALL", null, ["callee:00bde180:8"]]
- 00aec9a0 bytes e4c50394
+ 00aec9e4 bytes e7c50394
- 00aec99c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aec99c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec99c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec99c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aec9e0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aec9e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec9e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec9e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec99c bytes 00fc1991
+ 00aec9e0 bytes 00c81791
- 00aec9a8 ["COPY", "tmp:0:8", ["const:960:8"]]
- 00aec9a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aec9a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aec9a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aec9ec ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00aec9ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec9ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec9ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aec9a8 bytes 08812591
+ 00aec9ec bytes 08812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a1b226df1585004cdf6bdb0facc5998"></a>

### [`00aec9bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9bc.md) → [`00aeca00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca00.md) _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

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
      "definition_site": "00aeca2c",
      "incomplete_value": true,
      "site": "00aeca2c",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec9e8",
      "incomplete_value": true,
      "site": "00aec9e8",
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
            "const:968:8"
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
      "definition_site": "00aeca14",
      "incomplete_value": true,
      "site": "00aeca14",
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
      "definition_site": "00aec9d0",
      "incomplete_value": true,
      "site": "00aec9d0",
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
      "definition_site": "00aeca20",
      "incomplete_value": false,
      "site": "00aeca24",
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
            "const:1d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec9dc",
      "incomplete_value": false,
      "site": "00aec9e0",
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
            "const:260:8"
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
      "00aeca10",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeca20",
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ],
    [
      "00aeca2c",
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeca10",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeca20",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      "00aeca2c",
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9bc.md#insn-00aec9e0) · [`00aec9e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9bc.md#insn-00aec9e8) · [`00aec9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9bc.md#insn-00aec9cc)
- 新版 [`00aeca24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca00.md#insn-00aeca24) · [`00aeca2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca00.md#insn-00aeca2c) · [`00aeca10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca00.md#insn-00aeca10)

~~~diff
- 00aec9e0 ["INT_ADD", "register:40f0:8", ["const:aec9e0:8", "const:4:8"]]
- 00aec9e0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeca24 ["INT_ADD", "register:40f0:8", ["const:aeca24:8", "const:4:8"]]
+ 00aeca24 ["CALL", null, ["callee:00bde090:8"]]
- 00aec9e0 bytes 98c50394
+ 00aeca24 bytes 9bc50394
- 00aec9e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00aec9e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeca2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aeca2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec9e8 bytes 60b604f9
+ 00aeca2c bytes 60d604f9
- 00aec9cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00aec9cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeca10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aeca10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec9cc bytes 68b644f9
+ 00aeca10 bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8ba3efc9e5eb230bc875c940b916140"></a>

### [`00aec9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9fc.md) → [`00aeca40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca40.md) _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

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
      "definition_site": "00aeca6c",
      "incomplete_value": true,
      "site": "00aeca6c",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeca28",
      "incomplete_value": true,
      "site": "00aeca28",
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
            "const:968:8"
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
      "definition_site": "00aeca54",
      "incomplete_value": true,
      "site": "00aeca54",
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
      "definition_site": "00aeca10",
      "incomplete_value": true,
      "site": "00aeca10",
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
      "definition_site": "00aeca5c",
      "incomplete_value": false,
      "site": "00aeca64",
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
            "const:1d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeca18",
      "incomplete_value": false,
      "site": "00aeca20",
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
            "const:260:8"
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
      "00aeca50",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeca5c",
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ],
    [
      "00aeca6c",
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeca50",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeca5c",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      "00aeca6c",
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeca20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9fc.md#insn-00aeca20) · [`00aeca28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9fc.md#insn-00aeca28) · [`00aeca0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9fc.md#insn-00aeca0c)
- 新版 [`00aeca64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca40.md#insn-00aeca64) · [`00aeca6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca40.md#insn-00aeca6c) · [`00aeca50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca40.md#insn-00aeca50)

~~~diff
- 00aeca20 ["INT_ADD", "register:40f0:8", ["const:aeca20:8", "const:4:8"]]
- 00aeca20 ["CALL", null, ["callee:00bde090:8"]]
+ 00aeca64 ["INT_ADD", "register:40f0:8", ["const:aeca64:8", "const:4:8"]]
+ 00aeca64 ["CALL", null, ["callee:00bde090:8"]]
- 00aeca20 bytes 88c50394
+ 00aeca64 bytes 8bc50394
- 00aeca28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00aeca28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeca6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aeca6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeca28 bytes 60b604f9
+ 00aeca6c bytes 60d604f9
- 00aeca0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00aeca0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeca50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aeca50 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeca0c bytes 68b644f9
+ 00aeca50 bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b64c2970ab820b71fc3a9c8ec523dae9"></a>

### [`00aeca3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca3c.md) → [`00aeca80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca80.md) _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00aecab0",
      "incomplete_value": true,
      "site": "00aecab0",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeca6c",
      "incomplete_value": true,
      "site": "00aeca6c",
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
            "const:968:8"
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
      "definition_site": "00aeca94",
      "incomplete_value": true,
      "site": "00aeca94",
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
      "definition_site": "00aeca50",
      "incomplete_value": true,
      "site": "00aeca50",
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
      "definition_site": "00aecaa0",
      "incomplete_value": true,
      "site": "00aecaa8",
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
            "const:1d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeca5c",
      "incomplete_value": true,
      "site": "00aeca64",
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
            "const:260:8"
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
      "00aeca90",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecaa0",
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ],
    [
      "00aecab0",
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeca90",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecaa0",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      "00aecab0",
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeca64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca3c.md#insn-00aeca64) · [`00aeca6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca3c.md#insn-00aeca6c) · [`00aeca4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca3c.md#insn-00aeca4c)
- 新版 [`00aecaa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca80.md#insn-00aecaa8) · [`00aecab0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca80.md#insn-00aecab0) · [`00aeca90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeca80.md#insn-00aeca90)

~~~diff
- 00aeca64 ["INT_ADD", "register:40f0:8", ["const:aeca64:8", "const:4:8"]]
- 00aeca64 ["CALL", null, ["callee:00bde090:8"]]
+ 00aecaa8 ["INT_ADD", "register:40f0:8", ["const:aecaa8:8", "const:4:8"]]
+ 00aecaa8 ["CALL", null, ["callee:00bde090:8"]]
- 00aeca64 bytes 77c50394
+ 00aecaa8 bytes 7ac50394
- 00aeca6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00aeca6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aecab0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aecab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeca6c bytes 60b604f9
+ 00aecab0 bytes 60d604f9
- 00aeca4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00aeca4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeca90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aeca90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeca4c bytes 68b644f9
+ 00aeca90 bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f0cbe5f240c435377777e35df328692"></a>

### [`00aeca80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca80.md) → [`00aecac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecac4.md) _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aecaf4",
      "incomplete_value": true,
      "site": "00aecaf4",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecab0",
      "incomplete_value": true,
      "site": "00aecab0",
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
            "const:968:8"
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
      "definition_site": "00aecad8",
      "incomplete_value": true,
      "site": "00aecad8",
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
      "definition_site": "00aeca94",
      "incomplete_value": true,
      "site": "00aeca94",
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
      "definition_site": "00aecae0",
      "incomplete_value": false,
      "site": "00aecaec",
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
            "const:1d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeca9c",
      "incomplete_value": false,
      "site": "00aecaa8",
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
            "const:260:8"
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
      "00aecad4",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecae0",
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ],
    [
      "00aecaf4",
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aecad4",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecae0",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      "00aecaf4",
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecaa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca80.md#insn-00aecaa8) · [`00aecab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca80.md#insn-00aecab0) · [`00aeca90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca80.md#insn-00aeca90)
- 新版 [`00aecaec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecac4.md#insn-00aecaec) · [`00aecaf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecac4.md#insn-00aecaf4) · [`00aecad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecac4.md#insn-00aecad4)

~~~diff
- 00aecaa8 ["INT_ADD", "register:40f0:8", ["const:aecaa8:8", "const:4:8"]]
- 00aecaa8 ["CALL", null, ["callee:00bde090:8"]]
+ 00aecaec ["INT_ADD", "register:40f0:8", ["const:aecaec:8", "const:4:8"]]
+ 00aecaec ["CALL", null, ["callee:00bde090:8"]]
- 00aecaa8 bytes 66c50394
+ 00aecaec bytes 69c50394
- 00aecab0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00aecab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aecaf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aecaf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecab0 bytes 60b604f9
+ 00aecaf4 bytes 60d604f9
- 00aeca90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
- 00aeca90 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aecad4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aecad4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeca90 bytes 68b644f9
+ 00aecad4 bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-285d8f0a51d8557ad369cb840569bf4d"></a>

### [`00aecad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecad0.md) → [`00aecb14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecb14.md) _ZN8firebase4util22parcel_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aecb9c",
      "incomplete_value": true,
      "site": "00aecb9c",
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
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecb58",
      "incomplete_value": true,
      "site": "00aecb58",
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
            "const:970:8"
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
      "definition_site": "00aecb48",
      "incomplete_value": true,
      "site": "00aecb54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecb04",
      "incomplete_value": true,
      "site": "00aecb10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:968:8"
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
      "00aecb28",
      "READ",
      [
        "storage",
        "010a0970",
        null,
        "undefined1"
      ]
    ],
    [
      "00aecb48",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecb9c",
      "WRITE",
      [
        "storage",
        "010a0970",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aecb28",
      "READ",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aecb48",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecb9c",
      "WRITE",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecb10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecad0.md#insn-00aecb10) · [`00aecb58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecad0.md#insn-00aecb58) · [`00aecae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecad0.md#insn-00aecae4)
- 新版 [`00aecb54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecb14.md#insn-00aecb54) · [`00aecb9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecb14.md#insn-00aecb9c) · [`00aecb28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecb14.md#insn-00aecb28)

~~~diff
- 00aecb10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aecb10 ["INT_ADD", "register:40f0:8", ["const:aecb10:8", "const:4:8"]]
- 00aecb10 ["CALLIND", null, ["register:0:8"]]
+ 00aecb54 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aecb54 ["INT_ADD", "register:40f0:8", ["const:aecb54:8", "const:4:8"]]
+ 00aecb54 ["CALLIND", null, ["register:0:8"]]
- 00aecb10 bytes 00013fd6
+ 00aecb54 bytes 00013fd6
- 00aecb58 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aecb58 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:970:8"]]
- 00aecb58 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aecb9c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aecb9c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9b0:8"]]
+ 00aecb9c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aecb58 bytes a0c22539
+ 00aecb9c bytes a0c22639
- 00aecae4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:970:8"]]
- 00aecae4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aecae4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aecb28 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b0:8"]]
+ 00aecb28 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aecb28 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aecae4 bytes a8c26539
+ 00aecb28 bytes a8c26639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39153b1612947b4d10444c2287c1458c"></a>

### [`00aecb6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecb6c.md) → [`00aecbb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecbb0.md) _ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

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
      "definition_site": "00aecbec",
      "incomplete_value": true,
      "site": "00aecbec",
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
            "const:9b0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecba8",
      "incomplete_value": true,
      "site": "00aecba8",
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
            "const:970:8"
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
      "definition_site": "00aecc3c",
      "incomplete_value": true,
      "site": "00aecc3c",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecbf8",
      "incomplete_value": true,
      "site": "00aecbf8",
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
            "const:968:8"
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
      "definition_site": "00aecbc8",
      "incomplete_value": true,
      "site": "00aecbc8",
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
      "definition_site": "00aecb84",
      "incomplete_value": true,
      "site": "00aecb84",
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
      "00aecbc4",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecbd0",
      "READ",
      [
        "storage",
        "010a0970",
        null,
        "undefined1"
      ]
    ],
    [
      "00aecbec",
      "WRITE",
      [
        "storage",
        "010a0970",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aecbc4",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecbd0",
      "READ",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aecbec",
      "WRITE",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecb6c.md#insn-00aecba8) · [`00aecbf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecb6c.md#insn-00aecbf4) · [`00aecbf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecb6c.md#insn-00aecbf8)
- 新版 [`00aecbec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecbb0.md#insn-00aecbec) · [`00aecc38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecbb0.md#insn-00aecc38) · [`00aecc3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecbb0.md#insn-00aecc3c)

~~~diff
- 00aecba8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aecba8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aecba8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:970:8"]]
- 00aecba8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aecbec ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aecbec ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aecbec ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9b0:8"]]
+ 00aecbec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aecba8 bytes bfc22539
+ 00aecbec bytes bfc22639
- 00aecbf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aecbf4 ["INT_ADD", "register:40f0:8", ["const:aecbf4:8", "const:4:8"]]
- 00aecbf4 ["CALLIND", null, ["register:0:8"]]
+ 00aecc38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aecc38 ["INT_ADD", "register:40f0:8", ["const:aecc38:8", "const:4:8"]]
+ 00aecc38 ["CALLIND", null, ["register:0:8"]]
- 00aecbf4 bytes 00013fd6
+ 00aecc38 bytes 00013fd6
- 00aecbf8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
- 00aecbf8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aecbf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aecc3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00aecc3c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aecc3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aecbf8 bytes 9fb604f9
+ 00aecc3c bytes 9fd604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4eb9c499f24c393f8a2fa6d0ba2f8959"></a>

### [`00aecc0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc0c.md) → [`00aecc50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecc50.md) _ZN8firebase4util22parcel_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aecc90",
      "incomplete_value": true,
      "site": "00aecc90",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecc4c",
      "incomplete_value": true,
      "site": "00aecc4c",
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
            "const:968:8"
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
      "definition_site": "00aecc6c",
      "incomplete_value": true,
      "site": "00aecc6c",
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
      "definition_site": "00aecc28",
      "incomplete_value": true,
      "site": "00aecc28",
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
      "definition_site": "00aecc74",
      "incomplete_value": false,
      "site": "00aecc88",
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
            "const:1d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecc30",
      "incomplete_value": false,
      "site": "00aecc44",
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
            "const:260:8"
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
      "00aecc64",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecc74",
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ],
    [
      "00aecc90",
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aecc64",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecc74",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      "00aecc90",
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecc44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc0c.md#insn-00aecc44) · [`00aecc4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc0c.md#insn-00aecc4c) · [`00aecc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc0c.md#insn-00aecc20)
- 新版 [`00aecc88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecc50.md#insn-00aecc88) · [`00aecc90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecc50.md#insn-00aecc90) · [`00aecc64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecc50.md#insn-00aecc64)

~~~diff
- 00aecc44 ["INT_ADD", "register:40f0:8", ["const:aecc44:8", "const:4:8"]]
- 00aecc44 ["CALL", null, ["callee:00bde090:8"]]
+ 00aecc88 ["INT_ADD", "register:40f0:8", ["const:aecc88:8", "const:4:8"]]
+ 00aecc88 ["CALL", null, ["callee:00bde090:8"]]
- 00aecc44 bytes ffc40394
+ 00aecc88 bytes 02c50394
- 00aecc4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
- 00aecc4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aecc90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00aecc90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecc4c bytes 80b604f9
+ 00aecc90 bytes 80d604f9
- 00aecc20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
- 00aecc20 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aecc64 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00aecc64 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aecc20 bytes 81b644f9
+ 00aecc64 bytes 81d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-44b2fa4e078aba0e2970ee8054cb4908"></a>

### [`00aecc7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc7c.md) → [`00aeccc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccc0.md) _ZN8firebase4util22parcel_file_descriptor11GetMethodIdENS1_6MethodE

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
      "definition_site": "00aeccdc",
      "incomplete_value": false,
      "site": "00aecce0",
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
      "definition_site": "00aecc98",
      "incomplete_value": false,
      "site": "00aecc9c",
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
      "definition_site": "00aeccec",
      "incomplete_value": true,
      "site": "00aeccf8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aecca8",
      "incomplete_value": true,
      "site": "00aeccb4",
      "value": [
        "LOAD",
        "8",
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
      "00aeccdc",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aeccec",
      "DATA",
      [
        "storage",
        "010a0978",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aeccdc",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aeccec",
      "DATA",
      [
        "storage",
        "010a09b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecc9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc7c.md#insn-00aecc9c) · [`00aecc98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc7c.md#insn-00aecc98) · [`00aecca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc7c.md#insn-00aecca4)
- 新版 [`00aecce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccc0.md#insn-00aecce0) · [`00aeccdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccc0.md#insn-00aeccdc) · [`00aecce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccc0.md#insn-00aecce8)

~~~diff
- 00aecc9c ["INT_ADD", "register:40f0:8", ["const:aecc9c:8", "const:4:8"]]
- 00aecc9c ["CALL", null, ["callee:00bde180:8"]]
+ 00aecce0 ["INT_ADD", "register:40f0:8", ["const:aecce0:8", "const:4:8"]]
+ 00aecce0 ["CALL", null, ["callee:00bde180:8"]]
- 00aecc9c bytes 25c50394
+ 00aecce0 bytes 28c50394
- 00aecc98 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00aecc98 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aecc98 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aecc98 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aeccdc ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00aeccdc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeccdc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aeccdc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aecc98 bytes 00501791
+ 00aeccdc bytes 001c1591
- 00aecca4 ["COPY", "tmp:0:8", ["const:978:8"]]
- 00aecca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aecca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aecca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aecce8 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 00aecce8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aecce8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aecce8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aecca4 bytes 08e12591
+ 00aecce8 bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4b0006e55cc754d206928f2d76083132"></a>

### [`00aeccb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeccb8.md) → [`00aeccfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccfc.md) _ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aecd3c",
      "incomplete_value": true,
      "site": "00aecd3c",
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
            "const:9a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeccf8",
      "incomplete_value": true,
      "site": "00aeccf8",
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
            "const:968:8"
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
      "definition_site": "00aecd18",
      "incomplete_value": true,
      "site": "00aecd18",
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
      "definition_site": "00aeccd4",
      "incomplete_value": true,
      "site": "00aeccd4",
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
      "definition_site": "00aecd20",
      "incomplete_value": false,
      "site": "00aecd34",
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
            "const:1d3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeccdc",
      "incomplete_value": false,
      "site": "00aeccf0",
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
            "const:260:8"
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
      "00aecd10",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecd20",
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ],
    [
      "00aecd3c",
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aecd10",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecd20",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      "00aecd3c",
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeccf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeccb8.md#insn-00aeccf0) · [`00aeccf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeccb8.md#insn-00aeccf8) · [`00aecccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeccb8.md#insn-00aecccc)
- 新版 [`00aecd34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccfc.md#insn-00aecd34) · [`00aecd3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccfc.md#insn-00aecd3c) · [`00aecd10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aeccfc.md#insn-00aecd10)

~~~diff
- 00aeccf0 ["INT_ADD", "register:40f0:8", ["const:aeccf0:8", "const:4:8"]]
- 00aeccf0 ["CALL", null, ["callee:00bde090:8"]]
+ 00aecd34 ["INT_ADD", "register:40f0:8", ["const:aecd34:8", "const:4:8"]]
+ 00aecd34 ["CALL", null, ["callee:00bde090:8"]]
- 00aeccf0 bytes d4c40394
+ 00aecd34 bytes d7c40394
- 00aeccf8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
- 00aeccf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aecd3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00aecd3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeccf8 bytes 80b604f9
+ 00aecd3c bytes 80d604f9
- 00aecccc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
- 00aecccc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aecd10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00aecd10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aecccc bytes 81b644f9
+ 00aecd10 bytes 81d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-97f2e9f3eacf6fee222ea96bec4e45a4"></a>

### [`00aecd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecd28.md) → [`00aecd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecd6c.md) _ZN8firebase4util22parcel_file_descriptor10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aecd88",
      "incomplete_value": false,
      "site": "00aecd8c",
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
      "definition_site": "00aecd44",
      "incomplete_value": false,
      "site": "00aecd48",
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
      "definition_site": "00aecd98",
      "incomplete_value": true,
      "site": "00aecda4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00aecd54",
      "incomplete_value": true,
      "site": "00aecd60",
      "value": [
        "LOAD",
        "8",
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
      "00aecd88",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aecd98",
      "DATA",
      [
        "storage",
        "010a0980",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aecd88",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aecd98",
      "DATA",
      [
        "storage",
        "010a09c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecd48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecd28.md#insn-00aecd48) · [`00aecd44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecd28.md#insn-00aecd44) · [`00aecd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecd28.md#insn-00aecd50)
- 新版 [`00aecd8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecd6c.md#insn-00aecd8c) · [`00aecd88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecd6c.md#insn-00aecd88) · [`00aecd94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecd6c.md#insn-00aecd94)

~~~diff
- 00aecd48 ["INT_ADD", "register:40f0:8", ["const:aecd48:8", "const:4:8"]]
- 00aecd48 ["CALL", null, ["callee:00bde180:8"]]
+ 00aecd8c ["INT_ADD", "register:40f0:8", ["const:aecd8c:8", "const:4:8"]]
+ 00aecd8c ["CALL", null, ["callee:00bde180:8"]]
- 00aecd48 bytes fac40394
+ 00aecd8c bytes fdc40394
- 00aecd44 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00aecd44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aecd44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aecd44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aecd88 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00aecd88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aecd88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aecd88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aecd44 bytes 00fc1991
+ 00aecd88 bytes 00c81791
- 00aecd50 ["COPY", "tmp:0:8", ["const:980:8"]]
- 00aecd50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aecd50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aecd50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aecd94 ["COPY", "tmp:0:8", ["const:9c0:8"]]
+ 00aecd94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aecd94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aecd94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aecd50 bytes 08012691
+ 00aecd94 bytes 08012791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0e1944ac641538c36a43643a57757dd"></a>

### [`00aecd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecd64.md) → [`00aecda8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecda8.md) _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
      "definition_site": "00aecdd4",
      "incomplete_value": true,
      "site": "00aecdd4",
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
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecd90",
      "incomplete_value": true,
      "site": "00aecd90",
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
            "const:988:8"
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
      "definition_site": "00aecdbc",
      "incomplete_value": true,
      "site": "00aecdbc",
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
      "definition_site": "00aecd78",
      "incomplete_value": true,
      "site": "00aecd78",
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
      "definition_site": "00aecdc8",
      "incomplete_value": false,
      "site": "00aecdcc",
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
            "const:4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecd84",
      "incomplete_value": false,
      "site": "00aecd88",
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
            "const:fbf:8"
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
      "00aecdb8",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecdc8",
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      "00aecdd4",
      "WRITE",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aecdb8",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecdc8",
      "PARAM",
      [
        "storage",
        "002a004a",
        null,
        "string"
      ]
    ],
    [
      "00aecdd4",
      "WRITE",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecd88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecd64.md#insn-00aecd88) · [`00aecd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecd64.md#insn-00aecd90) · [`00aecd74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecd64.md#insn-00aecd74)
- 新版 [`00aecdcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecda8.md#insn-00aecdcc) · [`00aecdd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecda8.md#insn-00aecdd4) · [`00aecdb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecda8.md#insn-00aecdb8)

~~~diff
- 00aecd88 ["INT_ADD", "register:40f0:8", ["const:aecd88:8", "const:4:8"]]
- 00aecd88 ["CALL", null, ["callee:00bde090:8"]]
+ 00aecdcc ["INT_ADD", "register:40f0:8", ["const:aecdcc:8", "const:4:8"]]
+ 00aecdcc ["CALL", null, ["callee:00bde090:8"]]
- 00aecd88 bytes aec40394
+ 00aecdcc bytes b1c40394
- 00aecd90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aecd90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aecdd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00aecdd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecd90 bytes 60c604f9
+ 00aecdd4 bytes 60e604f9
- 00aecd74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aecd74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aecdb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00aecdb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aecd74 bytes 68c644f9
+ 00aecdb8 bytes 68e644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9f82740132710c783a397248e82626a"></a>

### [`00aecda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecda4.md) → [`00aecde8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecde8.md) _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aece14",
      "incomplete_value": true,
      "site": "00aece14",
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
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecdd0",
      "incomplete_value": true,
      "site": "00aecdd0",
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
            "const:988:8"
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
      "definition_site": "00aecdfc",
      "incomplete_value": true,
      "site": "00aecdfc",
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
      "definition_site": "00aecdb8",
      "incomplete_value": true,
      "site": "00aecdb8",
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
      "definition_site": "00aece04",
      "incomplete_value": false,
      "site": "00aece0c",
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
            "const:4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecdc0",
      "incomplete_value": false,
      "site": "00aecdc8",
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
            "const:fbf:8"
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
      "00aecdf8",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aece04",
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      "00aece14",
      "WRITE",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aecdf8",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aece04",
      "PARAM",
      [
        "storage",
        "002a004a",
        null,
        "string"
      ]
    ],
    [
      "00aece14",
      "WRITE",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecda4.md#insn-00aecdc8) · [`00aecdd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecda4.md#insn-00aecdd0) · [`00aecdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecda4.md#insn-00aecdb4)
- 新版 [`00aece0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecde8.md#insn-00aece0c) · [`00aece14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecde8.md#insn-00aece14) · [`00aecdf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aecde8.md#insn-00aecdf8)

~~~diff
- 00aecdc8 ["INT_ADD", "register:40f0:8", ["const:aecdc8:8", "const:4:8"]]
- 00aecdc8 ["CALL", null, ["callee:00bde090:8"]]
+ 00aece0c ["INT_ADD", "register:40f0:8", ["const:aece0c:8", "const:4:8"]]
+ 00aece0c ["CALL", null, ["callee:00bde090:8"]]
- 00aecdc8 bytes 9ec40394
+ 00aece0c bytes a1c40394
- 00aecdd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aecdd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aece14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00aece14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecdd0 bytes 60c604f9
+ 00aece14 bytes 60e604f9
- 00aecdb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aecdb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aecdf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00aecdf8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aecdb4 bytes 68c644f9
+ 00aecdf8 bytes 68e644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf9d7cd9508017201a0667d8b1b7382a"></a>

### [`00aecde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecde4.md) → [`00aece28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece28.md) _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00aece58",
      "incomplete_value": true,
      "site": "00aece58",
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
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aece14",
      "incomplete_value": true,
      "site": "00aece14",
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
            "const:988:8"
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
      "definition_site": "00aece3c",
      "incomplete_value": true,
      "site": "00aece3c",
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
      "definition_site": "00aecdf8",
      "incomplete_value": true,
      "site": "00aecdf8",
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
      "definition_site": "00aece48",
      "incomplete_value": false,
      "site": "00aece50",
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
            "const:4a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aece04",
      "incomplete_value": false,
      "site": "00aece0c",
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
            "const:fbf:8"
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
      "00aece38",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aece48",
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      "00aece58",
      "WRITE",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aece38",
      "READ",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aece48",
      "PARAM",
      [
        "storage",
        "002a004a",
        null,
        "string"
      ]
    ],
    [
      "00aece58",
      "WRITE",
      [
        "storage",
        "010a09c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aece0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecde4.md#insn-00aece0c) · [`00aece14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecde4.md#insn-00aece14) · [`00aecdf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecde4.md#insn-00aecdf4)
- 新版 [`00aece50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece28.md#insn-00aece50) · [`00aece58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece28.md#insn-00aece58) · [`00aece38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aec/00aece28.md#insn-00aece38)

~~~diff
- 00aece0c ["INT_ADD", "register:40f0:8", ["const:aece0c:8", "const:4:8"]]
- 00aece0c ["CALL", null, ["callee:00bde090:8"]]
+ 00aece50 ["INT_ADD", "register:40f0:8", ["const:aece50:8", "const:4:8"]]
+ 00aece50 ["CALL", null, ["callee:00bde090:8"]]
- 00aece0c bytes 8dc40394
+ 00aece50 bytes 90c40394
- 00aece14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aece14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aece58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00aece58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aece14 bytes 60c604f9
+ 00aece58 bytes 60e604f9
- 00aecdf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aecdf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aece38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00aece38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aecdf4 bytes 68c644f9
+ 00aece38 bytes 68e644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

