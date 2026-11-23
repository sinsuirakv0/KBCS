# v15.7.3 → v15.7.4 · 最優先の変更候補 (62)

[一覧の目次](README.md)

<a id="compare-dd39c6a628484c4cff8176cae3cb0e9d"></a>

### [`00ae5ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ff4.md) → [`00ae6038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6038.md) _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00ae6064",
      "incomplete_value": true,
      "site": "00ae6064",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6020",
      "incomplete_value": true,
      "site": "00ae6020",
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
            "const:3f8:8"
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
      "definition_site": "00ae604c",
      "incomplete_value": true,
      "site": "00ae604c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6008",
      "incomplete_value": true,
      "site": "00ae6008",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae6054",
      "incomplete_value": false,
      "site": "00ae605c",
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
            "const:eaa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6010",
      "incomplete_value": false,
      "site": "00ae6018",
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
            "const:e1f:8"
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
      "00ae6048",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6054",
      "PARAM",
      [
        "storage",
        "0029ee1f",
        null,
        "string"
      ]
    ],
    [
      "00ae6064",
      "WRITE",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6048",
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6054",
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ],
    [
      "00ae6064",
      "WRITE",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ff4.md#insn-00ae6018) · [`00ae6020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ff4.md#insn-00ae6020) · [`00ae6004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ff4.md#insn-00ae6004)
- 新版 [`00ae605c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6038.md#insn-00ae605c) · [`00ae6064`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6038.md#insn-00ae6064) · [`00ae6048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6038.md#insn-00ae6048)

~~~diff
- 00ae6018 ["INT_ADD", "register:40f0:8", ["const:ae6018:8", "const:4:8"]]
- 00ae6018 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae605c ["INT_ADD", "register:40f0:8", ["const:ae605c:8", "const:4:8"]]
+ 00ae605c ["CALL", null, ["callee:00bde090:8"]]
- 00ae6018 bytes 0ae00394
+ 00ae605c bytes 0de00394
- 00ae6020 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f8:8"]]
- 00ae6020 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6064 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00ae6064 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6020 bytes 60fe01f9
+ 00ae6064 bytes 601e02f9
- 00ae6004 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f8:8"]]
- 00ae6004 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6048 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00ae6048 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6004 bytes 68fe41f9
+ 00ae6048 bytes 681e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7c83eeafb964401b6d1d375fafb39512"></a>

### [`00ae6034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6034.md) → [`00ae6078`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6078.md) _ZN8firebase4util10uribuilder10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae60a8",
      "incomplete_value": true,
      "site": "00ae60a8",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6064",
      "incomplete_value": true,
      "site": "00ae6064",
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
            "const:3f8:8"
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
      "definition_site": "00ae608c",
      "incomplete_value": true,
      "site": "00ae608c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6048",
      "incomplete_value": true,
      "site": "00ae6048",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae6098",
      "incomplete_value": false,
      "site": "00ae60a0",
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
            "const:eaa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6054",
      "incomplete_value": false,
      "site": "00ae605c",
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
            "const:e1f:8"
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
      "00ae6088",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6098",
      "PARAM",
      [
        "storage",
        "0029ee1f",
        null,
        "string"
      ]
    ],
    [
      "00ae60a8",
      "WRITE",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6088",
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6098",
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ],
    [
      "00ae60a8",
      "WRITE",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae605c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6034.md#insn-00ae605c) · [`00ae6064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6034.md#insn-00ae6064) · [`00ae6044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6034.md#insn-00ae6044)
- 新版 [`00ae60a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6078.md#insn-00ae60a0) · [`00ae60a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6078.md#insn-00ae60a8) · [`00ae6088`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6078.md#insn-00ae6088)

~~~diff
- 00ae605c ["INT_ADD", "register:40f0:8", ["const:ae605c:8", "const:4:8"]]
- 00ae605c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae60a0 ["INT_ADD", "register:40f0:8", ["const:ae60a0:8", "const:4:8"]]
+ 00ae60a0 ["CALL", null, ["callee:00bde090:8"]]
- 00ae605c bytes f9df0394
+ 00ae60a0 bytes fcdf0394
- 00ae6064 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f8:8"]]
- 00ae6064 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae60a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00ae60a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6064 bytes 60fe01f9
+ 00ae60a8 bytes 601e02f9
- 00ae6044 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f8:8"]]
- 00ae6044 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6088 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00ae6088 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6044 bytes 68fe41f9
+ 00ae6088 bytes 681e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dfdb23d8dd1c73936fad77d62916f781"></a>

### [`00ae6078`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6078.md) → [`00ae60bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae60bc.md) _ZN8firebase4util10uribuilder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae60ec",
      "incomplete_value": true,
      "site": "00ae60ec",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae60a8",
      "incomplete_value": true,
      "site": "00ae60a8",
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
            "const:3f8:8"
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
      "definition_site": "00ae60d0",
      "incomplete_value": true,
      "site": "00ae60d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae608c",
      "incomplete_value": true,
      "site": "00ae608c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae608c"
      ],
      [
        "FALL_THROUGH",
        "00ae60d0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae60d0",
      "incomplete_value": true,
      "site": "00ae60ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae608c",
      "incomplete_value": true,
      "site": "00ae60a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae60cc",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae60d8",
      "PARAM",
      [
        "storage",
        "0029ee1f",
        null,
        "string"
      ]
    ],
    [
      "00ae60ec",
      "WRITE",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae60cc",
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae60d8",
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ],
    [
      "00ae60ec",
      "WRITE",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae60a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6078.md#insn-00ae60a8) · [`00ae6088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6078.md#insn-00ae6088) · [`00ae6094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6078.md#insn-00ae6094)
- 新版 [`00ae60ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae60bc.md#insn-00ae60ec) · [`00ae60cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae60bc.md#insn-00ae60cc) · [`00ae60d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae60bc.md#insn-00ae60d8)

~~~diff
- 00ae60a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f8:8"]]
- 00ae60a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae60ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00ae60ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae60a8 bytes 60fe01f9
+ 00ae60ec bytes 601e02f9
- 00ae6088 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f8:8"]]
- 00ae6088 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae60cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00ae60cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6088 bytes 68fe41f9
+ 00ae60cc bytes 681e42f9
- 00ae6094 ["COPY", "tmp:0:8", ["const:e1f:8"]]
- 00ae6094 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae6094 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae6094 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae60d8 ["COPY", "tmp:0:8", ["const:eaa:8"]]
+ 00ae60d8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae60d8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae60d8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae6094 bytes 637c3891
+ 00ae60d8 bytes 63a83a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f1864b35a3e9070bd85b5da0dc96c15"></a>

### [`00ae60c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae60c8.md) → [`00ae610c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae610c.md) _ZN8firebase4util10uribuilder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae6194",
      "incomplete_value": true,
      "site": "00ae6194",
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
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6150",
      "incomplete_value": true,
      "site": "00ae6150",
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
            "const:400:8"
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
      "definition_site": "00ae6140",
      "incomplete_value": true,
      "site": "00ae614c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:438:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae60fc",
      "incomplete_value": true,
      "site": "00ae6108",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f8:8"
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
      "00ae6120",
      "READ",
      [
        "storage",
        "010a0400",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6140",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6194",
      "WRITE",
      [
        "storage",
        "010a0400",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae6120",
      "READ",
      [
        "storage",
        "010a0440",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6140",
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6194",
      "WRITE",
      [
        "storage",
        "010a0440",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae60c8.md#insn-00ae6108) · [`00ae6150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae60c8.md#insn-00ae6150) · [`00ae60dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae60c8.md#insn-00ae60dc)
- 新版 [`00ae614c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae610c.md#insn-00ae614c) · [`00ae6194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae610c.md#insn-00ae6194) · [`00ae6120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae610c.md#insn-00ae6120)

~~~diff
- 00ae6108 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6108 ["INT_ADD", "register:40f0:8", ["const:ae6108:8", "const:4:8"]]
- 00ae6108 ["CALLIND", null, ["register:0:8"]]
+ 00ae614c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae614c ["INT_ADD", "register:40f0:8", ["const:ae614c:8", "const:4:8"]]
+ 00ae614c ["CALLIND", null, ["register:0:8"]]
- 00ae6108 bytes 00013fd6
+ 00ae614c bytes 00013fd6
- 00ae6150 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae6150 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:400:8"]]
- 00ae6150 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae6194 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae6194 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:440:8"]]
+ 00ae6194 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae6150 bytes a0021039
+ 00ae6194 bytes a0021139
- 00ae60dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:400:8"]]
- 00ae60dc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae60dc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae6120 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:440:8"]]
+ 00ae6120 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6120 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae60dc bytes a8025039
+ 00ae6120 bytes a8025139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75ecab7143de98076a3f0816907c5abb"></a>

### [`00ae6164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6164.md) → [`00ae61a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae61a8.md) _ZN8firebase4util10uribuilder12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae61e4",
      "incomplete_value": true,
      "site": "00ae61e4",
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
            "const:440:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae61a0",
      "incomplete_value": true,
      "site": "00ae61a0",
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
            "const:400:8"
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
      "definition_site": "00ae6234",
      "incomplete_value": true,
      "site": "00ae6234",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae61f0",
      "incomplete_value": true,
      "site": "00ae61f0",
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
            "const:3f8:8"
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
      "definition_site": "00ae6224",
      "incomplete_value": true,
      "site": "00ae6230",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:438:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae61e0",
      "incomplete_value": true,
      "site": "00ae61ec",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:3f8:8"
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
      "00ae61bc",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae61c8",
      "READ",
      [
        "storage",
        "010a0400",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae61e4",
      "WRITE",
      [
        "storage",
        "010a0400",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae61bc",
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae61c8",
      "READ",
      [
        "storage",
        "010a0440",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae61e4",
      "WRITE",
      [
        "storage",
        "010a0440",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae61a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6164.md#insn-00ae61a0) · [`00ae61ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6164.md#insn-00ae61ec) · [`00ae61f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6164.md#insn-00ae61f0)
- 新版 [`00ae61e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae61a8.md#insn-00ae61e4) · [`00ae6230`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae61a8.md#insn-00ae6230) · [`00ae6234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae61a8.md#insn-00ae6234)

~~~diff
- 00ae61a0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae61a0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae61a0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:400:8"]]
- 00ae61a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae61e4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae61e4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae61e4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:440:8"]]
+ 00ae61e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae61a0 bytes bf021039
+ 00ae61e4 bytes bf021139
- 00ae61ec ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae61ec ["INT_ADD", "register:40f0:8", ["const:ae61ec:8", "const:4:8"]]
- 00ae61ec ["CALLIND", null, ["register:0:8"]]
+ 00ae6230 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae6230 ["INT_ADD", "register:40f0:8", ["const:ae6230:8", "const:4:8"]]
+ 00ae6230 ["CALLIND", null, ["register:0:8"]]
- 00ae61ec bytes 00013fd6
+ 00ae6230 bytes 00013fd6
- 00ae61f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f8:8"]]
- 00ae61f0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae61f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae6234 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
+ 00ae6234 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae6234 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae61f0 bytes 9ffe01f9
+ 00ae6234 bytes 9f1e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad1784fc702cf810c56259f5581ca0ae"></a>

### [`00ae6204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6204.md) → [`00ae6248`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6248.md) _ZN8firebase4util10uribuilder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae6288",
      "incomplete_value": true,
      "site": "00ae6288",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6244",
      "incomplete_value": true,
      "site": "00ae6244",
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
            "const:3f8:8"
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
      "definition_site": "00ae6264",
      "incomplete_value": true,
      "site": "00ae6264",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6220",
      "incomplete_value": true,
      "site": "00ae6220",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae626c",
      "incomplete_value": false,
      "site": "00ae6280",
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
            "const:eaa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6228",
      "incomplete_value": false,
      "site": "00ae623c",
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
            "const:e1f:8"
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
      "00ae625c",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae626c",
      "PARAM",
      [
        "storage",
        "0029ee1f",
        null,
        "string"
      ]
    ],
    [
      "00ae6288",
      "WRITE",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae625c",
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae626c",
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ],
    [
      "00ae6288",
      "WRITE",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae623c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6204.md#insn-00ae623c) · [`00ae6244`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6204.md#insn-00ae6244) · [`00ae6218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6204.md#insn-00ae6218)
- 新版 [`00ae6280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6248.md#insn-00ae6280) · [`00ae6288`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6248.md#insn-00ae6288) · [`00ae625c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6248.md#insn-00ae625c)

~~~diff
- 00ae623c ["INT_ADD", "register:40f0:8", ["const:ae623c:8", "const:4:8"]]
- 00ae623c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6280 ["INT_ADD", "register:40f0:8", ["const:ae6280:8", "const:4:8"]]
+ 00ae6280 ["CALL", null, ["callee:00bde090:8"]]
- 00ae623c bytes 81df0394
+ 00ae6280 bytes 84df0394
- 00ae6244 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f8:8"]]
- 00ae6244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6288 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
+ 00ae6288 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6244 bytes 80fe01f9
+ 00ae6288 bytes 801e02f9
- 00ae6218 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f8:8"]]
- 00ae6218 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae625c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
+ 00ae625c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6218 bytes 81fe41f9
+ 00ae625c bytes 811e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c8d1c81d7207212e1e088995356ee00"></a>

### [`00ae6274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6274.md) → [`00ae62b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae62b8.md) _ZN8firebase4util10uribuilder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae62d4",
      "incomplete_value": false,
      "site": "00ae62d8",
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
      "definition_site": "00ae6290",
      "incomplete_value": false,
      "site": "00ae6294",
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
      "definition_site": "00ae62e4",
      "incomplete_value": true,
      "site": "00ae62f0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae62a0",
      "incomplete_value": true,
      "site": "00ae62ac",
      "value": [
        "LOAD",
        "8",
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
      "00ae62d4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae62e4",
      "DATA",
      [
        "storage",
        "010a0408",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae62d4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae62e4",
      "DATA",
      [
        "storage",
        "010a0448",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6274.md#insn-00ae6294) · [`00ae6290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6274.md#insn-00ae6290) · [`00ae629c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6274.md#insn-00ae629c)
- 新版 [`00ae62d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae62b8.md#insn-00ae62d8) · [`00ae62d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae62b8.md#insn-00ae62d4) · [`00ae62e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae62b8.md#insn-00ae62e0)

~~~diff
- 00ae6294 ["INT_ADD", "register:40f0:8", ["const:ae6294:8", "const:4:8"]]
- 00ae6294 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae62d8 ["INT_ADD", "register:40f0:8", ["const:ae62d8:8", "const:4:8"]]
+ 00ae62d8 ["CALL", null, ["callee:00bde180:8"]]
- 00ae6294 bytes a7df0394
+ 00ae62d8 bytes aadf0394
- 00ae6290 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae6290 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6290 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6290 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae62d4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae62d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae62d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae62d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae6290 bytes 00501791
+ 00ae62d4 bytes 001c1591
- 00ae629c ["COPY", "tmp:0:8", ["const:408:8"]]
- 00ae629c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae629c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae629c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae62e0 ["COPY", "tmp:0:8", ["const:448:8"]]
+ 00ae62e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae62e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae62e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae629c bytes 08211091
+ 00ae62e0 bytes 08211191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a6e30d208bcaec98685c0158dbe3d919"></a>

### [`00ae62b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae62b0.md) → [`00ae62f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae62f4.md) _ZN8firebase4util10uribuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae6334",
      "incomplete_value": true,
      "site": "00ae6334",
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
            "const:438:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae62f0",
      "incomplete_value": true,
      "site": "00ae62f0",
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
            "const:3f8:8"
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
      "definition_site": "00ae6310",
      "incomplete_value": true,
      "site": "00ae6310",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae62cc",
      "incomplete_value": true,
      "site": "00ae62cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae62cc"
      ],
      [
        "FALL_THROUGH",
        "00ae6310"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae6310",
      "incomplete_value": true,
      "site": "00ae6334",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae62cc",
      "incomplete_value": true,
      "site": "00ae62f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae6308",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6318",
      "PARAM",
      [
        "storage",
        "0029ee1f",
        null,
        "string"
      ]
    ],
    [
      "00ae6334",
      "WRITE",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6308",
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6318",
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ],
    [
      "00ae6334",
      "WRITE",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae62f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae62b0.md#insn-00ae62f0) · [`00ae62c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae62b0.md#insn-00ae62c4) · [`00ae62d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae62b0.md#insn-00ae62d4)
- 新版 [`00ae6334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae62f4.md#insn-00ae6334) · [`00ae6308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae62f4.md#insn-00ae6308) · [`00ae6318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae62f4.md#insn-00ae6318)

~~~diff
- 00ae62f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f8:8"]]
- 00ae62f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6334 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
+ 00ae6334 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae62f0 bytes 80fe01f9
+ 00ae6334 bytes 801e02f9
- 00ae62c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f8:8"]]
- 00ae62c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6308 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:438:8"]]
+ 00ae6308 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae62c4 bytes 81fe41f9
+ 00ae6308 bytes 811e42f9
- 00ae62d4 ["COPY", "tmp:0:8", ["const:e1f:8"]]
- 00ae62d4 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae62d4 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae62d4 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae6318 ["COPY", "tmp:0:8", ["const:eaa:8"]]
+ 00ae6318 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae6318 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae6318 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae62d4 bytes 637c3891
+ 00ae6318 bytes 63a83a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14f60118de0bc838a63ed1f2d173aa12"></a>

### [`00ae6320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6320.md) → [`00ae6364`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6364.md) _ZN8firebase4util10uribuilder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae6390",
      "incomplete_value": true,
      "site": "00ae639c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae634c",
      "incomplete_value": true,
      "site": "00ae6358",
      "value": [
        "LOAD",
        "8",
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
      "00ae6380",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae6390",
      "DATA",
      [
        "storage",
        "010a0420",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae6380",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae6390",
      "DATA",
      [
        "storage",
        "010a0460",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae633c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6320.md#insn-00ae633c) · [`00ae6340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6320.md#insn-00ae6340) · [`00ae6348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6320.md#insn-00ae6348)
- 新版 [`00ae6380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6364.md#insn-00ae6380) · [`00ae6384`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6364.md#insn-00ae6384) · [`00ae638c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6364.md#insn-00ae638c)

~~~diff
- 00ae633c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae633c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae633c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae633c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae6380 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae6380 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae6380 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae6380 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae633c bytes 00fc1991
+ 00ae6380 bytes 00c81791
- 00ae6340 ["INT_ADD", "register:40f0:8", ["const:ae6340:8", "const:4:8"]]
- 00ae6340 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae6384 ["INT_ADD", "register:40f0:8", ["const:ae6384:8", "const:4:8"]]
+ 00ae6384 ["CALL", null, ["callee:00bde180:8"]]
- 00ae6340 bytes 7cdf0394
+ 00ae6384 bytes 7fdf0394
- 00ae6348 ["COPY", "tmp:0:8", ["const:420:8"]]
- 00ae6348 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae6348 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae6348 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae638c ["COPY", "tmp:0:8", ["const:460:8"]]
+ 00ae638c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae638c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae638c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae6348 bytes 08811091
+ 00ae638c bytes 08811191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00bb158c9c9e3fb4e6233f6f878767d2"></a>

### [`00ae635c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae635c.md) → [`00ae63a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63a0.md) _ZN8firebase4util3url19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
      "definition_site": "00ae63cc",
      "incomplete_value": true,
      "site": "00ae63cc",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6388",
      "incomplete_value": true,
      "site": "00ae6388",
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
            "const:428:8"
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
      "definition_site": "00ae63b4",
      "incomplete_value": true,
      "site": "00ae63b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6370",
      "incomplete_value": true,
      "site": "00ae6370",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae6370"
      ],
      [
        "FALL_THROUGH",
        "00ae63b4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae63b4",
      "incomplete_value": true,
      "site": "00ae63cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6370",
      "incomplete_value": true,
      "site": "00ae6388",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae63b0",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae63cc",
      "WRITE",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae63b0",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae63cc",
      "WRITE",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae635c.md#insn-00ae6388) · [`00ae636c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae635c.md#insn-00ae636c) · [`00ae6380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae635c.md#insn-00ae6380)
- 新版 [`00ae63cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63a0.md#insn-00ae63cc) · [`00ae63b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63a0.md#insn-00ae63b0) · [`00ae63c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63a0.md#insn-00ae63c4)

~~~diff
- 00ae6388 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:428:8"]]
- 00ae6388 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae63cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
+ 00ae63cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6388 bytes 601602f9
+ 00ae63cc bytes 603602f9
- 00ae636c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:428:8"]]
- 00ae636c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae63b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
+ 00ae63b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae636c bytes 681642f9
+ 00ae63b0 bytes 683642f9
- 00ae6380 ["INT_ADD", "register:40f0:8", ["const:ae6380:8", "const:4:8"]]
- 00ae6380 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae63c4 ["INT_ADD", "register:40f0:8", ["const:ae63c4:8", "const:4:8"]]
+ 00ae63c4 ["CALL", null, ["callee:00bde090:8"]]
- 00ae6380 bytes 30df0394
+ 00ae63c4 bytes 33df0394
~~~


<a id="compare-893b10706e788388cabca4138878c018"></a>

### [`00ae639c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae639c.md) → [`00ae63e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63e0.md) _ZN8firebase4util3url19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00ae640c",
      "incomplete_value": true,
      "site": "00ae640c",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae63c8",
      "incomplete_value": true,
      "site": "00ae63c8",
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
            "const:428:8"
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
      "definition_site": "00ae63f4",
      "incomplete_value": true,
      "site": "00ae63f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae63b0",
      "incomplete_value": true,
      "site": "00ae63b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae63b0"
      ],
      [
        "FALL_THROUGH",
        "00ae63f4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae63f4",
      "incomplete_value": true,
      "site": "00ae640c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae63b0",
      "incomplete_value": true,
      "site": "00ae63c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae63f0",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae640c",
      "WRITE",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae63f0",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae640c",
      "WRITE",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae63c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae639c.md#insn-00ae63c8) · [`00ae63ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae639c.md#insn-00ae63ac) · [`00ae63c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae639c.md#insn-00ae63c0)
- 新版 [`00ae640c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63e0.md#insn-00ae640c) · [`00ae63f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63e0.md#insn-00ae63f0) · [`00ae6404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae63e0.md#insn-00ae6404)

~~~diff
- 00ae63c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:428:8"]]
- 00ae63c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae640c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
+ 00ae640c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae63c8 bytes 601602f9
+ 00ae640c bytes 603602f9
- 00ae63ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:428:8"]]
- 00ae63ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae63f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
+ 00ae63f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae63ac bytes 681642f9
+ 00ae63f0 bytes 683642f9
- 00ae63c0 ["INT_ADD", "register:40f0:8", ["const:ae63c0:8", "const:4:8"]]
- 00ae63c0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6404 ["INT_ADD", "register:40f0:8", ["const:ae6404:8", "const:4:8"]]
+ 00ae6404 ["CALL", null, ["callee:00bde090:8"]]
- 00ae63c0 bytes 20df0394
+ 00ae6404 bytes 23df0394
~~~


<a id="compare-9d19f669724b5be402f066baa4385422"></a>

### [`00ae63dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae63dc.md) → [`00ae6420`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6420.md) _ZN8firebase4util3url10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae6450",
      "incomplete_value": true,
      "site": "00ae6450",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae640c",
      "incomplete_value": true,
      "site": "00ae640c",
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
            "const:428:8"
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
      "definition_site": "00ae6434",
      "incomplete_value": true,
      "site": "00ae6434",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae63f0",
      "incomplete_value": true,
      "site": "00ae63f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae63f0"
      ],
      [
        "FALL_THROUGH",
        "00ae6434"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae6434",
      "incomplete_value": true,
      "site": "00ae6450",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae63f0",
      "incomplete_value": true,
      "site": "00ae640c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae6430",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6450",
      "WRITE",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6430",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6450",
      "WRITE",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae640c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae63dc.md#insn-00ae640c) · [`00ae63ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae63dc.md#insn-00ae63ec) · [`00ae6404`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae63dc.md#insn-00ae6404)
- 新版 [`00ae6450`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6420.md#insn-00ae6450) · [`00ae6430`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6420.md#insn-00ae6430) · [`00ae6448`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6420.md#insn-00ae6448)

~~~diff
- 00ae640c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:428:8"]]
- 00ae640c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6450 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
+ 00ae6450 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae640c bytes 601602f9
+ 00ae6450 bytes 603602f9
- 00ae63ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:428:8"]]
- 00ae63ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6430 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
+ 00ae6430 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae63ec bytes 681642f9
+ 00ae6430 bytes 683642f9
- 00ae6404 ["INT_ADD", "register:40f0:8", ["const:ae6404:8", "const:4:8"]]
- 00ae6404 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6448 ["INT_ADD", "register:40f0:8", ["const:ae6448:8", "const:4:8"]]
+ 00ae6448 ["CALL", null, ["callee:00bde090:8"]]
- 00ae6404 bytes 0fdf0394
+ 00ae6448 bytes 12df0394
~~~


<a id="compare-e9cbf129328aaf41256e6bd14db632d6"></a>

### [`00ae6420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6420.md) → [`00ae6464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6464.md) _ZN8firebase4util3url10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae6494",
      "incomplete_value": true,
      "site": "00ae6494",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6450",
      "incomplete_value": true,
      "site": "00ae6450",
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
            "const:428:8"
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
      "definition_site": "00ae6478",
      "incomplete_value": true,
      "site": "00ae6478",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6434",
      "incomplete_value": true,
      "site": "00ae6434",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae6434"
      ],
      [
        "FALL_THROUGH",
        "00ae6478"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae6478",
      "incomplete_value": true,
      "site": "00ae6494",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6434",
      "incomplete_value": true,
      "site": "00ae6450",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae6474",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6494",
      "WRITE",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6474",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6494",
      "WRITE",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6420.md#insn-00ae6450) · [`00ae6430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6420.md#insn-00ae6430) · [`00ae6448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6420.md#insn-00ae6448)
- 新版 [`00ae6494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6464.md#insn-00ae6494) · [`00ae6474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6464.md#insn-00ae6474) · [`00ae648c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6464.md#insn-00ae648c)

~~~diff
- 00ae6450 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:428:8"]]
- 00ae6450 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6494 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
+ 00ae6494 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6450 bytes 601602f9
+ 00ae6494 bytes 603602f9
- 00ae6430 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:428:8"]]
- 00ae6430 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6474 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:468:8"]]
+ 00ae6474 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6430 bytes 681642f9
+ 00ae6474 bytes 683642f9
- 00ae6448 ["INT_ADD", "register:40f0:8", ["const:ae6448:8", "const:4:8"]]
- 00ae6448 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae648c ["INT_ADD", "register:40f0:8", ["const:ae648c:8", "const:4:8"]]
+ 00ae648c ["CALL", null, ["callee:00bde090:8"]]
- 00ae6448 bytes fede0394
+ 00ae648c bytes 01df0394
~~~


<a id="compare-8c55b1bd71ad7c4d3c4353c53e718d12"></a>

### [`00ae6470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6470.md) → [`00ae64b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae64b4.md) _ZN8firebase4util3url15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae653c",
      "incomplete_value": true,
      "site": "00ae653c",
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
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae64f8",
      "incomplete_value": true,
      "site": "00ae64f8",
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
            "const:430:8"
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
      "definition_site": "00ae64e8",
      "incomplete_value": true,
      "site": "00ae64f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:468:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae64a4",
      "incomplete_value": true,
      "site": "00ae64b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:428:8"
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
      "00ae64c8",
      "READ",
      [
        "storage",
        "010a0430",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae64e8",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae653c",
      "WRITE",
      [
        "storage",
        "010a0430",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae64c8",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae64e8",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae653c",
      "WRITE",
      [
        "storage",
        "010a0470",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae64b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6470.md#insn-00ae64b0) · [`00ae64f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6470.md#insn-00ae64f8) · [`00ae6484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6470.md#insn-00ae6484)
- 新版 [`00ae64f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae64b4.md#insn-00ae64f4) · [`00ae653c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae64b4.md#insn-00ae653c) · [`00ae64c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae64b4.md#insn-00ae64c8)

~~~diff
- 00ae64b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae64b0 ["INT_ADD", "register:40f0:8", ["const:ae64b0:8", "const:4:8"]]
- 00ae64b0 ["CALLIND", null, ["register:0:8"]]
+ 00ae64f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae64f4 ["INT_ADD", "register:40f0:8", ["const:ae64f4:8", "const:4:8"]]
+ 00ae64f4 ["CALLIND", null, ["register:0:8"]]
- 00ae64b0 bytes 00013fd6
+ 00ae64f4 bytes 00013fd6
- 00ae64f8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae64f8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:430:8"]]
- 00ae64f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae653c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae653c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:470:8"]]
+ 00ae653c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae64f8 bytes a0c21039
+ 00ae653c bytes a0c21139
- 00ae6484 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:430:8"]]
- 00ae6484 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae6484 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae64c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:470:8"]]
+ 00ae64c8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae64c8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae6484 bytes a8c25039
+ 00ae64c8 bytes a8c25139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09a1edc6801a198ada49895084ebea5a"></a>

### [`00ae650c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae650c.md) → [`00ae6550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6550.md) _ZN8firebase4util3url12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae658c",
      "incomplete_value": true,
      "site": "00ae658c",
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
            "const:470:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6548",
      "incomplete_value": true,
      "site": "00ae6548",
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
            "const:430:8"
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
      "definition_site": "00ae65dc",
      "incomplete_value": true,
      "site": "00ae65dc",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6598",
      "incomplete_value": true,
      "site": "00ae6598",
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
            "const:428:8"
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
      "definition_site": "00ae65cc",
      "incomplete_value": true,
      "site": "00ae65d8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:468:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6588",
      "incomplete_value": true,
      "site": "00ae6594",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:428:8"
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
      "00ae6564",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6570",
      "READ",
      [
        "storage",
        "010a0430",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae658c",
      "WRITE",
      [
        "storage",
        "010a0430",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae6564",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6570",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae658c",
      "WRITE",
      [
        "storage",
        "010a0470",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae650c.md#insn-00ae6548) · [`00ae6594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae650c.md#insn-00ae6594) · [`00ae6598`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae650c.md#insn-00ae6598)
- 新版 [`00ae658c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6550.md#insn-00ae658c) · [`00ae65d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6550.md#insn-00ae65d8) · [`00ae65dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6550.md#insn-00ae65dc)

~~~diff
- 00ae6548 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae6548 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae6548 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:430:8"]]
- 00ae6548 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae658c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae658c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae658c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:470:8"]]
+ 00ae658c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae6548 bytes bfc21039
+ 00ae658c bytes bfc21139
- 00ae6594 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6594 ["INT_ADD", "register:40f0:8", ["const:ae6594:8", "const:4:8"]]
- 00ae6594 ["CALLIND", null, ["register:0:8"]]
+ 00ae65d8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae65d8 ["INT_ADD", "register:40f0:8", ["const:ae65d8:8", "const:4:8"]]
+ 00ae65d8 ["CALLIND", null, ["register:0:8"]]
- 00ae6594 bytes 00013fd6
+ 00ae65d8 bytes 00013fd6
- 00ae6598 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:428:8"]]
- 00ae6598 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae6598 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae65dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:468:8"]]
+ 00ae65dc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae65dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae6598 bytes 9f1602f9
+ 00ae65dc bytes 9f3602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5df9bc0f4c2d753a52db299456d8e1bf"></a>

### [`00ae65ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae65ac.md) → [`00ae65f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae65f0.md) _ZN8firebase4util3url14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae6630",
      "incomplete_value": true,
      "site": "00ae6630",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae65ec",
      "incomplete_value": true,
      "site": "00ae65ec",
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
            "const:428:8"
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
      "00ae6604",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6630",
      "WRITE",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6644",
      "PARAM",
      [
        "storage",
        "00c0fd50",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ae6604",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6630",
      "WRITE",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6644",
      "PARAM",
      [
        "storage",
        "00c0fda0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae65ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae65ac.md#insn-00ae65ec) · [`00ae65c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae65ac.md#insn-00ae65c0) · [`00ae65e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae65ac.md#insn-00ae65e4)
- 新版 [`00ae6630`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae65f0.md#insn-00ae6630) · [`00ae6604`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae65f0.md#insn-00ae6604) · [`00ae6628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae65f0.md#insn-00ae6628)

~~~diff
- 00ae65ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:428:8"]]
- 00ae65ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6630 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:468:8"]]
+ 00ae6630 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae65ec bytes 801602f9
+ 00ae6630 bytes 803602f9
- 00ae65c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:428:8"]]
- 00ae65c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6604 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:468:8"]]
+ 00ae6604 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae65c0 bytes 811642f9
+ 00ae6604 bytes 813642f9
- 00ae65e4 ["INT_ADD", "register:40f0:8", ["const:ae65e4:8", "const:4:8"]]
- 00ae65e4 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6628 ["INT_ADD", "register:40f0:8", ["const:ae6628:8", "const:4:8"]]
+ 00ae6628 ["CALL", null, ["callee:00bde090:8"]]
- 00ae65e4 bytes 97de0394
+ 00ae6628 bytes 9ade0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52bfa75ad67403dd3f44f65383d080f8"></a>

### [`00ae661c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae661c.md) → [`00ae6660`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6660.md) _ZN8firebase4util3url11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae667c",
      "incomplete_value": false,
      "site": "00ae6680",
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
      "definition_site": "00ae6638",
      "incomplete_value": false,
      "site": "00ae663c",
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
      "definition_site": "00ae668c",
      "incomplete_value": true,
      "site": "00ae6698",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae6648",
      "incomplete_value": true,
      "site": "00ae6654",
      "value": [
        "LOAD",
        "8",
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
      "00ae667c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae668c",
      "DATA",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae667c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae668c",
      "DATA",
      [
        "storage",
        "010a0478",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae663c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae661c.md#insn-00ae663c) · [`00ae6638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae661c.md#insn-00ae6638) · [`00ae6644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae661c.md#insn-00ae6644)
- 新版 [`00ae6680`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6660.md#insn-00ae6680) · [`00ae667c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6660.md#insn-00ae667c) · [`00ae6688`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6660.md#insn-00ae6688)

~~~diff
- 00ae663c ["INT_ADD", "register:40f0:8", ["const:ae663c:8", "const:4:8"]]
- 00ae663c ["CALL", null, ["callee:00bde180:8"]]
+ 00ae6680 ["INT_ADD", "register:40f0:8", ["const:ae6680:8", "const:4:8"]]
+ 00ae6680 ["CALL", null, ["callee:00bde180:8"]]
- 00ae663c bytes bdde0394
+ 00ae6680 bytes c0de0394
- 00ae6638 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae6638 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6638 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6638 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae667c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae667c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae667c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae667c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae6638 bytes 00501791
+ 00ae667c bytes 001c1591
- 00ae6644 ["COPY", "tmp:0:8", ["const:438:8"]]
- 00ae6644 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae6644 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae6644 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae6688 ["COPY", "tmp:0:8", ["const:478:8"]]
+ 00ae6688 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae6688 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae6688 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae6644 bytes 08e11091
+ 00ae6688 bytes 08e11191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93972dad1e168fe87e2228d4040a02bc"></a>

### [`00ae6658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6658.md) → [`00ae669c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae669c.md) _ZN8firebase4util3url13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae66dc",
      "incomplete_value": true,
      "site": "00ae66dc",
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
            "const:468:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6698",
      "incomplete_value": true,
      "site": "00ae6698",
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
            "const:428:8"
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
      "definition_site": "00ae66b8",
      "incomplete_value": true,
      "site": "00ae66b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6674",
      "incomplete_value": true,
      "site": "00ae6674",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae6674"
      ],
      [
        "FALL_THROUGH",
        "00ae66b8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae66b8",
      "incomplete_value": true,
      "site": "00ae66dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6674",
      "incomplete_value": true,
      "site": "00ae6698",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae66b0",
      "READ",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae66dc",
      "WRITE",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae66f4",
      "PARAM",
      [
        "storage",
        "010a0448",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae66b0",
      "READ",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae66dc",
      "WRITE",
      [
        "storage",
        "010a0468",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae66f4",
      "PARAM",
      [
        "storage",
        "010a0488",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6658.md#insn-00ae6698) · [`00ae666c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6658.md#insn-00ae666c) · [`00ae6690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6658.md#insn-00ae6690)
- 新版 [`00ae66dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae669c.md#insn-00ae66dc) · [`00ae66b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae669c.md#insn-00ae66b0) · [`00ae66d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae669c.md#insn-00ae66d4)

~~~diff
- 00ae6698 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:428:8"]]
- 00ae6698 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae66dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:468:8"]]
+ 00ae66dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6698 bytes 801602f9
+ 00ae66dc bytes 803602f9
- 00ae666c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:428:8"]]
- 00ae666c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae66b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:468:8"]]
+ 00ae66b0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae666c bytes 811642f9
+ 00ae66b0 bytes 813642f9
- 00ae6690 ["INT_ADD", "register:40f0:8", ["const:ae6690:8", "const:4:8"]]
- 00ae6690 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae66d4 ["INT_ADD", "register:40f0:8", ["const:ae66d4:8", "const:4:8"]]
+ 00ae66d4 ["CALL", null, ["callee:00bde090:8"]]
- 00ae6690 bytes 6cde0394
+ 00ae66d4 bytes 6fde0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6962822d002fa6c30406875cbeec8b63"></a>

### [`00ae66c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae66c8.md) → [`00ae670c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae670c.md) _ZN8firebase4util3url10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae6728",
      "incomplete_value": false,
      "site": "00ae672c",
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
      "definition_site": "00ae66e4",
      "incomplete_value": false,
      "site": "00ae66e8",
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
      "00ae6728",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae6738",
      "DATA",
      [
        "storage",
        "010a0448",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae6728",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae6738",
      "DATA",
      [
        "storage",
        "010a0488",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae66e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae66c8.md#insn-00ae66e8) · [`00ae66e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae66c8.md#insn-00ae66e4) · [`00ae66f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae66c8.md#insn-00ae66f0)
- 新版 [`00ae672c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae670c.md#insn-00ae672c) · [`00ae6728`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae670c.md#insn-00ae6728) · [`00ae6734`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae670c.md#insn-00ae6734)

~~~diff
- 00ae66e8 ["INT_ADD", "register:40f0:8", ["const:ae66e8:8", "const:4:8"]]
- 00ae66e8 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae672c ["INT_ADD", "register:40f0:8", ["const:ae672c:8", "const:4:8"]]
+ 00ae672c ["CALL", null, ["callee:00bde180:8"]]
- 00ae66e8 bytes 92de0394
+ 00ae672c bytes 95de0394
- 00ae66e4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae66e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae66e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae66e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae6728 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae6728 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae6728 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae6728 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae66e4 bytes 00fc1991
+ 00ae6728 bytes 00c81791
- 00ae66f0 ["COPY", "tmp:0:8", ["const:448:8"]]
- 00ae66f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae66f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae66f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae6734 ["COPY", "tmp:0:8", ["const:488:8"]]
+ 00ae6734 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae6734 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae6734 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae66f0 bytes 08211191
+ 00ae6734 bytes 08211291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96aa300d3661914a1e9b1ca3ae2189ea"></a>

### [`00ae6704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6704.md) → [`00ae6748`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6748.md) _ZN8firebase4util18file_output_stream19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "definition_site": "00ae6774",
      "incomplete_value": true,
      "site": "00ae6774",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6730",
      "incomplete_value": true,
      "site": "00ae6730",
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
            "const:450:8"
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
      "definition_site": "00ae6768",
      "incomplete_value": false,
      "site": "00ae676c",
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
            "const:ff7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6724",
      "incomplete_value": false,
      "site": "00ae6728",
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
            "const:f6c:8"
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
      "00ae6758",
      "READ",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6768",
      "PARAM",
      [
        "storage",
        "0029ff6c",
        null,
        "string"
      ]
    ],
    [
      "00ae6774",
      "WRITE",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6758",
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6768",
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      "00ae6774",
      "WRITE",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6704.md#insn-00ae6728) · [`00ae6730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6704.md#insn-00ae6730) · [`00ae6714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6704.md#insn-00ae6714)
- 新版 [`00ae676c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6748.md#insn-00ae676c) · [`00ae6774`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6748.md#insn-00ae6774) · [`00ae6758`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6748.md#insn-00ae6758)

~~~diff
- 00ae6728 ["INT_ADD", "register:40f0:8", ["const:ae6728:8", "const:4:8"]]
- 00ae6728 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae676c ["INT_ADD", "register:40f0:8", ["const:ae676c:8", "const:4:8"]]
+ 00ae676c ["CALL", null, ["callee:00bde090:8"]]
- 00ae6728 bytes 46de0394
+ 00ae676c bytes 49de0394
- 00ae6730 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:450:8"]]
- 00ae6730 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6774 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
+ 00ae6774 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6730 bytes 602a02f9
+ 00ae6774 bytes 604a02f9
- 00ae6714 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:450:8"]]
- 00ae6714 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6758 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
+ 00ae6758 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6714 bytes 682a42f9
+ 00ae6758 bytes 684a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6c52d9e79d0bad9e9d3037df7805309e"></a>

### [`00ae6744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6744.md) → [`00ae6788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6788.md) _ZN8firebase4util18file_output_stream19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "definition_site": "00ae67b4",
      "incomplete_value": true,
      "site": "00ae67b4",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6770",
      "incomplete_value": true,
      "site": "00ae6770",
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
            "const:450:8"
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
      "definition_site": "00ae679c",
      "incomplete_value": true,
      "site": "00ae679c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6758",
      "incomplete_value": true,
      "site": "00ae6758",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae67a4",
      "incomplete_value": true,
      "site": "00ae67ac",
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
            "const:ff7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6760",
      "incomplete_value": true,
      "site": "00ae6768",
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
            "const:f6c:8"
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
      "00ae6798",
      "READ",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae67a4",
      "PARAM",
      [
        "storage",
        "0029ff6c",
        null,
        "string"
      ]
    ],
    [
      "00ae67b4",
      "WRITE",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6798",
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae67a4",
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      "00ae67b4",
      "WRITE",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6744.md#insn-00ae6768) · [`00ae6770`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6744.md#insn-00ae6770) · [`00ae6754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6744.md#insn-00ae6754)
- 新版 [`00ae67ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6788.md#insn-00ae67ac) · [`00ae67b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6788.md#insn-00ae67b4) · [`00ae6798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6788.md#insn-00ae6798)

~~~diff
- 00ae6768 ["INT_ADD", "register:40f0:8", ["const:ae6768:8", "const:4:8"]]
- 00ae6768 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae67ac ["INT_ADD", "register:40f0:8", ["const:ae67ac:8", "const:4:8"]]
+ 00ae67ac ["CALL", null, ["callee:00bde090:8"]]
- 00ae6768 bytes 36de0394
+ 00ae67ac bytes 39de0394
- 00ae6770 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:450:8"]]
- 00ae6770 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae67b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
+ 00ae67b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6770 bytes 602a02f9
+ 00ae67b4 bytes 604a02f9
- 00ae6754 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:450:8"]]
- 00ae6754 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6798 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
+ 00ae6798 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6754 bytes 682a42f9
+ 00ae6798 bytes 684a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f02027c55dce3701bc49701e6450c87f"></a>

### [`00ae6784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6784.md) → [`00ae67c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae67c8.md) _ZN8firebase4util18file_output_stream10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae67f8",
      "incomplete_value": true,
      "site": "00ae67f8",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae67b4",
      "incomplete_value": true,
      "site": "00ae67b4",
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
            "const:450:8"
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
      "definition_site": "00ae67dc",
      "incomplete_value": true,
      "site": "00ae67dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6798",
      "incomplete_value": true,
      "site": "00ae6798",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae67e8",
      "incomplete_value": false,
      "site": "00ae67f0",
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
            "const:ff7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae67a4",
      "incomplete_value": false,
      "site": "00ae67ac",
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
            "const:f6c:8"
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
      "00ae67d8",
      "READ",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae67e8",
      "PARAM",
      [
        "storage",
        "0029ff6c",
        null,
        "string"
      ]
    ],
    [
      "00ae67f8",
      "WRITE",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae67d8",
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae67e8",
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      "00ae67f8",
      "WRITE",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae67ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6784.md#insn-00ae67ac) · [`00ae67b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6784.md#insn-00ae67b4) · [`00ae6794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6784.md#insn-00ae6794)
- 新版 [`00ae67f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae67c8.md#insn-00ae67f0) · [`00ae67f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae67c8.md#insn-00ae67f8) · [`00ae67d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae67c8.md#insn-00ae67d8)

~~~diff
- 00ae67ac ["INT_ADD", "register:40f0:8", ["const:ae67ac:8", "const:4:8"]]
- 00ae67ac ["CALL", null, ["callee:00bde090:8"]]
+ 00ae67f0 ["INT_ADD", "register:40f0:8", ["const:ae67f0:8", "const:4:8"]]
+ 00ae67f0 ["CALL", null, ["callee:00bde090:8"]]
- 00ae67ac bytes 25de0394
+ 00ae67f0 bytes 28de0394
- 00ae67b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:450:8"]]
- 00ae67b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae67f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
+ 00ae67f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae67b4 bytes 602a02f9
+ 00ae67f8 bytes 604a02f9
- 00ae6794 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:450:8"]]
- 00ae6794 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae67d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
+ 00ae67d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6794 bytes 682a42f9
+ 00ae67d8 bytes 684a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-856c490283cb9c53c1ef43cecebaf560"></a>

### [`00ae67c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae67c8.md) → [`00ae680c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae680c.md) _ZN8firebase4util18file_output_stream10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae683c",
      "incomplete_value": true,
      "site": "00ae683c",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae67f8",
      "incomplete_value": true,
      "site": "00ae67f8",
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
            "const:450:8"
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
      "definition_site": "00ae6820",
      "incomplete_value": true,
      "site": "00ae6820",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae67dc",
      "incomplete_value": true,
      "site": "00ae67dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae6828",
      "incomplete_value": true,
      "site": "00ae6834",
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
            "const:ff7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae67e4",
      "incomplete_value": true,
      "site": "00ae67f0",
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
            "const:f6c:8"
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
      "00ae681c",
      "READ",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6828",
      "PARAM",
      [
        "storage",
        "0029ff6c",
        null,
        "string"
      ]
    ],
    [
      "00ae683c",
      "WRITE",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae681c",
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6828",
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      "00ae683c",
      "WRITE",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae67f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae67c8.md#insn-00ae67f0) · [`00ae67f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae67c8.md#insn-00ae67f8) · [`00ae67d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae67c8.md#insn-00ae67d8)
- 新版 [`00ae6834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae680c.md#insn-00ae6834) · [`00ae683c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae680c.md#insn-00ae683c) · [`00ae681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae680c.md#insn-00ae681c)

~~~diff
- 00ae67f0 ["INT_ADD", "register:40f0:8", ["const:ae67f0:8", "const:4:8"]]
- 00ae67f0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6834 ["INT_ADD", "register:40f0:8", ["const:ae6834:8", "const:4:8"]]
+ 00ae6834 ["CALL", null, ["callee:00bde090:8"]]
- 00ae67f0 bytes 14de0394
+ 00ae6834 bytes 17de0394
- 00ae67f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:450:8"]]
- 00ae67f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae683c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
+ 00ae683c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae67f8 bytes 602a02f9
+ 00ae683c bytes 604a02f9
- 00ae67d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:450:8"]]
- 00ae67d8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae681c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:490:8"]]
+ 00ae681c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae67d8 bytes 682a42f9
+ 00ae681c bytes 684a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f1b3f6100b2e4cc1e4bddfa63396a3a"></a>

### [`00ae6818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6818.md) → [`00ae685c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae685c.md) _ZN8firebase4util18file_output_stream15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae68e4",
      "incomplete_value": true,
      "site": "00ae68e4",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae68a0",
      "incomplete_value": true,
      "site": "00ae68a0",
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
            "const:458:8"
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
      "definition_site": "00ae6890",
      "incomplete_value": true,
      "site": "00ae689c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:490:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae684c",
      "incomplete_value": true,
      "site": "00ae6858",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:450:8"
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
      "00ae6870",
      "READ",
      [
        "storage",
        "010a0458",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6890",
      "READ",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae68e4",
      "WRITE",
      [
        "storage",
        "010a0458",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae6870",
      "READ",
      [
        "storage",
        "010a0498",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6890",
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae68e4",
      "WRITE",
      [
        "storage",
        "010a0498",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6818.md#insn-00ae6858) · [`00ae68a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6818.md#insn-00ae68a0) · [`00ae682c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6818.md#insn-00ae682c)
- 新版 [`00ae689c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae685c.md#insn-00ae689c) · [`00ae68e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae685c.md#insn-00ae68e4) · [`00ae6870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae685c.md#insn-00ae6870)

~~~diff
- 00ae6858 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6858 ["INT_ADD", "register:40f0:8", ["const:ae6858:8", "const:4:8"]]
- 00ae6858 ["CALLIND", null, ["register:0:8"]]
+ 00ae689c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae689c ["INT_ADD", "register:40f0:8", ["const:ae689c:8", "const:4:8"]]
+ 00ae689c ["CALLIND", null, ["register:0:8"]]
- 00ae6858 bytes 00013fd6
+ 00ae689c bytes 00013fd6
- 00ae68a0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae68a0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:458:8"]]
- 00ae68a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae68e4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae68e4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:498:8"]]
+ 00ae68e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae68a0 bytes a0621139
+ 00ae68e4 bytes a0621239
- 00ae682c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:458:8"]]
- 00ae682c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae682c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae6870 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:498:8"]]
+ 00ae6870 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6870 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae682c bytes a8625139
+ 00ae6870 bytes a8625239
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0afea66010a0c0d62541963b0d83459c"></a>

### [`00ae68b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae68b4.md) → [`00ae68f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae68f8.md) _ZN8firebase4util18file_output_stream12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae6934",
      "incomplete_value": true,
      "site": "00ae6934",
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
            "const:498:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae68f0",
      "incomplete_value": true,
      "site": "00ae68f0",
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
            "const:458:8"
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
      "definition_site": "00ae6984",
      "incomplete_value": true,
      "site": "00ae6984",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6940",
      "incomplete_value": true,
      "site": "00ae6940",
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
            "const:450:8"
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
      "definition_site": "00ae6910",
      "incomplete_value": true,
      "site": "00ae6910",
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
      "definition_site": "00ae68cc",
      "incomplete_value": true,
      "site": "00ae68cc",
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
      "00ae690c",
      "READ",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6918",
      "READ",
      [
        "storage",
        "010a0458",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6934",
      "WRITE",
      [
        "storage",
        "010a0458",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae690c",
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6918",
      "READ",
      [
        "storage",
        "010a0498",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6934",
      "WRITE",
      [
        "storage",
        "010a0498",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae68f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae68b4.md#insn-00ae68f0) · [`00ae693c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae68b4.md#insn-00ae693c) · [`00ae6940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae68b4.md#insn-00ae6940)
- 新版 [`00ae6934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae68f8.md#insn-00ae6934) · [`00ae6980`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae68f8.md#insn-00ae6980) · [`00ae6984`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae68f8.md#insn-00ae6984)

~~~diff
- 00ae68f0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae68f0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae68f0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:458:8"]]
- 00ae68f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae6934 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae6934 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae6934 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:498:8"]]
+ 00ae6934 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae68f0 bytes bf621139
+ 00ae6934 bytes bf621239
- 00ae693c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae693c ["INT_ADD", "register:40f0:8", ["const:ae693c:8", "const:4:8"]]
- 00ae693c ["CALLIND", null, ["register:0:8"]]
+ 00ae6980 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae6980 ["INT_ADD", "register:40f0:8", ["const:ae6980:8", "const:4:8"]]
+ 00ae6980 ["CALLIND", null, ["register:0:8"]]
- 00ae693c bytes 00013fd6
+ 00ae6980 bytes 00013fd6
- 00ae6940 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:450:8"]]
- 00ae6940 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae6940 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae6984 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:490:8"]]
+ 00ae6984 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae6984 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae6940 bytes 9f2a02f9
+ 00ae6984 bytes 9f4a02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce43fe84b3969c7683cd4cd403b8dbda"></a>

### [`00ae6954`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6954.md) → [`00ae6998`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6998.md) _ZN8firebase4util18file_output_stream14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae69d8",
      "incomplete_value": true,
      "site": "00ae69d8",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6994",
      "incomplete_value": true,
      "site": "00ae6994",
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
            "const:450:8"
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
      "definition_site": "00ae69b4",
      "incomplete_value": true,
      "site": "00ae69b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6970",
      "incomplete_value": true,
      "site": "00ae6970",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae69bc",
      "incomplete_value": false,
      "site": "00ae69d0",
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
            "const:ff7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6978",
      "incomplete_value": false,
      "site": "00ae698c",
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
            "const:f6c:8"
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
      "00ae69ac",
      "READ",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae69bc",
      "PARAM",
      [
        "storage",
        "0029ff6c",
        null,
        "string"
      ]
    ],
    [
      "00ae69d8",
      "WRITE",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae69ac",
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae69bc",
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      "00ae69d8",
      "WRITE",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae698c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6954.md#insn-00ae698c) · [`00ae6994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6954.md#insn-00ae6994) · [`00ae6968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6954.md#insn-00ae6968)
- 新版 [`00ae69d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6998.md#insn-00ae69d0) · [`00ae69d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6998.md#insn-00ae69d8) · [`00ae69ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6998.md#insn-00ae69ac)

~~~diff
- 00ae698c ["INT_ADD", "register:40f0:8", ["const:ae698c:8", "const:4:8"]]
- 00ae698c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae69d0 ["INT_ADD", "register:40f0:8", ["const:ae69d0:8", "const:4:8"]]
+ 00ae69d0 ["CALL", null, ["callee:00bde090:8"]]
- 00ae698c bytes addd0394
+ 00ae69d0 bytes b0dd0394
- 00ae6994 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:450:8"]]
- 00ae6994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae69d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:490:8"]]
+ 00ae69d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6994 bytes 802a02f9
+ 00ae69d8 bytes 804a02f9
- 00ae6968 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:450:8"]]
- 00ae6968 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae69ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:490:8"]]
+ 00ae69ac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6968 bytes 812a42f9
+ 00ae69ac bytes 814a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a14b1b60109cb77ca0cb8ee74c4c38d"></a>

### [`00ae69c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae69c4.md) → [`00ae6a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6a08.md) _ZN8firebase4util18file_output_stream11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae6a24",
      "incomplete_value": false,
      "site": "00ae6a28",
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
      "definition_site": "00ae69e0",
      "incomplete_value": false,
      "site": "00ae69e4",
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
      "definition_site": "00ae6a34",
      "incomplete_value": true,
      "site": "00ae6a40",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae69f0",
      "incomplete_value": true,
      "site": "00ae69fc",
      "value": [
        "LOAD",
        "8",
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
      "00ae6a24",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae6a34",
      "DATA",
      [
        "storage",
        "010a0460",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6a24",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae6a34",
      "DATA",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae69e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae69c4.md#insn-00ae69e4) · [`00ae69e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae69c4.md#insn-00ae69e0) · [`00ae69ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae69c4.md#insn-00ae69ec)
- 新版 [`00ae6a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6a08.md#insn-00ae6a28) · [`00ae6a24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6a08.md#insn-00ae6a24) · [`00ae6a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6a08.md#insn-00ae6a30)

~~~diff
- 00ae69e4 ["INT_ADD", "register:40f0:8", ["const:ae69e4:8", "const:4:8"]]
- 00ae69e4 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae6a28 ["INT_ADD", "register:40f0:8", ["const:ae6a28:8", "const:4:8"]]
+ 00ae6a28 ["CALL", null, ["callee:00bde180:8"]]
- 00ae69e4 bytes d3dd0394
+ 00ae6a28 bytes d6dd0394
- 00ae69e0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae69e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae69e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae69e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae6a24 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae6a24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae6a24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae6a24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae69e0 bytes 00501791
+ 00ae6a24 bytes 001c1591
- 00ae69ec ["COPY", "tmp:0:8", ["const:460:8"]]
- 00ae69ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae69ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae69ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae6a30 ["COPY", "tmp:0:8", ["const:4a0:8"]]
+ 00ae6a30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae6a30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae6a30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae69ec bytes 08811191
+ 00ae6a30 bytes 08811291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-22ff5e0bb3ca41d4f4a6aceb2654102f"></a>

### [`00ae6a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6a00.md) → [`00ae6a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6a44.md) _ZN8firebase4util18file_output_stream13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae6a84",
      "incomplete_value": true,
      "site": "00ae6a84",
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
            "const:490:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6a40",
      "incomplete_value": true,
      "site": "00ae6a40",
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
            "const:450:8"
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
      "00ae6a58",
      "READ",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6a68",
      "PARAM",
      [
        "storage",
        "0029ff6c",
        null,
        "string"
      ]
    ],
    [
      "00ae6a84",
      "WRITE",
      [
        "storage",
        "010a0450",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6a58",
      "READ",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6a68",
      "PARAM",
      [
        "storage",
        "0029fff7",
        null,
        "string"
      ]
    ],
    [
      "00ae6a84",
      "WRITE",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6a00.md#insn-00ae6a40) · [`00ae6a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6a00.md#insn-00ae6a14) · [`00ae6a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6a00.md#insn-00ae6a24)
- 新版 [`00ae6a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6a44.md#insn-00ae6a84) · [`00ae6a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6a44.md#insn-00ae6a58) · [`00ae6a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6a44.md#insn-00ae6a68)

~~~diff
- 00ae6a40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:450:8"]]
- 00ae6a40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6a84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:490:8"]]
+ 00ae6a84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6a40 bytes 802a02f9
+ 00ae6a84 bytes 804a02f9
- 00ae6a14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:450:8"]]
- 00ae6a14 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6a58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:490:8"]]
+ 00ae6a58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6a14 bytes 812a42f9
+ 00ae6a58 bytes 814a42f9
- 00ae6a24 ["COPY", "tmp:0:8", ["const:f6c:8"]]
- 00ae6a24 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae6a24 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae6a24 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae6a68 ["COPY", "tmp:0:8", ["const:ff7:8"]]
+ 00ae6a68 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae6a68 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae6a68 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae6a24 bytes 63b03d91
+ 00ae6a68 bytes 63dc3f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef3770ecd167fcbc8e2c4446069e0deb"></a>

### [`00ae6a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6a70.md) → [`00ae6ab4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ab4.md) _ZN8firebase4util18file_output_stream10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae6ad0",
      "incomplete_value": false,
      "site": "00ae6ad4",
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
      "definition_site": "00ae6a8c",
      "incomplete_value": false,
      "site": "00ae6a90",
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
      "definition_site": "00ae6ae0",
      "incomplete_value": true,
      "site": "00ae6aec",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae6a9c",
      "incomplete_value": true,
      "site": "00ae6aa8",
      "value": [
        "LOAD",
        "8",
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
      "00ae6ad0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae6ae0",
      "DATA",
      [
        "storage",
        "010a0478",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae6ad0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae6ae0",
      "DATA",
      [
        "storage",
        "010a04b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6a90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6a70.md#insn-00ae6a90) · [`00ae6a8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6a70.md#insn-00ae6a8c) · [`00ae6a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6a70.md#insn-00ae6a98)
- 新版 [`00ae6ad4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ab4.md#insn-00ae6ad4) · [`00ae6ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ab4.md#insn-00ae6ad0) · [`00ae6adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ab4.md#insn-00ae6adc)

~~~diff
- 00ae6a90 ["INT_ADD", "register:40f0:8", ["const:ae6a90:8", "const:4:8"]]
- 00ae6a90 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae6ad4 ["INT_ADD", "register:40f0:8", ["const:ae6ad4:8", "const:4:8"]]
+ 00ae6ad4 ["CALL", null, ["callee:00bde180:8"]]
- 00ae6a90 bytes a8dd0394
+ 00ae6ad4 bytes abdd0394
- 00ae6a8c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae6a8c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6a8c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6a8c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae6ad0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae6ad0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae6ad0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae6ad0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae6a8c bytes 00fc1991
+ 00ae6ad0 bytes 00c81791
- 00ae6a98 ["COPY", "tmp:0:8", ["const:478:8"]]
- 00ae6a98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae6a98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae6a98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae6adc ["COPY", "tmp:0:8", ["const:4b8:8"]]
+ 00ae6adc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae6adc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae6adc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae6a98 bytes 08e11191
+ 00ae6adc bytes 08e11291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b10319fccdfc70846e1546b770b2197"></a>

### [`00ae6aac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6aac.md) → [`00ae6af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6af0.md) _ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

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
      "definition_site": "00ae6b1c",
      "incomplete_value": true,
      "site": "00ae6b1c",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ad8",
      "incomplete_value": true,
      "site": "00ae6ad8",
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
            "const:480:8"
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
      "definition_site": "00ae6b04",
      "incomplete_value": true,
      "site": "00ae6b04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ac0",
      "incomplete_value": true,
      "site": "00ae6ac0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae6b10",
      "incomplete_value": false,
      "site": "00ae6b14",
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
            "const:d9a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6acc",
      "incomplete_value": false,
      "site": "00ae6ad0",
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
            "const:d00:8"
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
      "00ae6b00",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6b10",
      "PARAM",
      [
        "storage",
        "002a7d00",
        null,
        "string"
      ]
    ],
    [
      "00ae6b1c",
      "WRITE",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6b00",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6b10",
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ],
    [
      "00ae6b1c",
      "WRITE",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6aac.md#insn-00ae6ad0) · [`00ae6ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6aac.md#insn-00ae6ad8) · [`00ae6abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6aac.md#insn-00ae6abc)
- 新版 [`00ae6b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6af0.md#insn-00ae6b14) · [`00ae6b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6af0.md#insn-00ae6b1c) · [`00ae6b00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6af0.md#insn-00ae6b00)

~~~diff
- 00ae6ad0 ["INT_ADD", "register:40f0:8", ["const:ae6ad0:8", "const:4:8"]]
- 00ae6ad0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6b14 ["INT_ADD", "register:40f0:8", ["const:ae6b14:8", "const:4:8"]]
+ 00ae6b14 ["CALL", null, ["callee:00bde090:8"]]
- 00ae6ad0 bytes 5cdd0394
+ 00ae6b14 bytes 5fdd0394
- 00ae6ad8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00ae6ad8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6b1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
+ 00ae6b1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6ad8 bytes 604202f9
+ 00ae6b1c bytes 606202f9
- 00ae6abc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00ae6abc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6b00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
+ 00ae6b00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6abc bytes 684242f9
+ 00ae6b00 bytes 686242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc2c4b72ecb50857e79be9d71db5b8a3"></a>

### [`00ae6aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6aec.md) → [`00ae6b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b30.md) _ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

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
      "definition_site": "00ae6b5c",
      "incomplete_value": true,
      "site": "00ae6b5c",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6b18",
      "incomplete_value": true,
      "site": "00ae6b18",
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
            "const:480:8"
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
      "definition_site": "00ae6b44",
      "incomplete_value": true,
      "site": "00ae6b44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6b00",
      "incomplete_value": true,
      "site": "00ae6b00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae6b4c",
      "incomplete_value": false,
      "site": "00ae6b54",
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
            "const:d9a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6b08",
      "incomplete_value": false,
      "site": "00ae6b10",
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
            "const:d00:8"
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
      "00ae6b40",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6b4c",
      "PARAM",
      [
        "storage",
        "002a7d00",
        null,
        "string"
      ]
    ],
    [
      "00ae6b5c",
      "WRITE",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6b40",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6b4c",
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ],
    [
      "00ae6b5c",
      "WRITE",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6aec.md#insn-00ae6b10) · [`00ae6b18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6aec.md#insn-00ae6b18) · [`00ae6afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6aec.md#insn-00ae6afc)
- 新版 [`00ae6b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b30.md#insn-00ae6b54) · [`00ae6b5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b30.md#insn-00ae6b5c) · [`00ae6b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b30.md#insn-00ae6b40)

~~~diff
- 00ae6b10 ["INT_ADD", "register:40f0:8", ["const:ae6b10:8", "const:4:8"]]
- 00ae6b10 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6b54 ["INT_ADD", "register:40f0:8", ["const:ae6b54:8", "const:4:8"]]
+ 00ae6b54 ["CALL", null, ["callee:00bde090:8"]]
- 00ae6b10 bytes 4cdd0394
+ 00ae6b54 bytes 4fdd0394
- 00ae6b18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00ae6b18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6b5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
+ 00ae6b5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6b18 bytes 604202f9
+ 00ae6b5c bytes 606202f9
- 00ae6afc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00ae6afc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6b40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
+ 00ae6b40 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6afc bytes 684242f9
+ 00ae6b40 bytes 686242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d3675243fbe2704fce342f9cf81827d"></a>

### [`00ae6b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6b2c.md) → [`00ae6b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b70.md) _ZN8firebase4util16dex_class_loader10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae6ba0",
      "incomplete_value": true,
      "site": "00ae6ba0",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6b5c",
      "incomplete_value": true,
      "site": "00ae6b5c",
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
            "const:480:8"
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
      "definition_site": "00ae6b84",
      "incomplete_value": true,
      "site": "00ae6b84",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6b40",
      "incomplete_value": true,
      "site": "00ae6b40",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae6b90",
      "incomplete_value": true,
      "site": "00ae6b98",
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
            "const:d9a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6b4c",
      "incomplete_value": true,
      "site": "00ae6b54",
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
            "const:d00:8"
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
      "00ae6b80",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6b90",
      "PARAM",
      [
        "storage",
        "002a7d00",
        null,
        "string"
      ]
    ],
    [
      "00ae6ba0",
      "WRITE",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6b80",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6b90",
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ],
    [
      "00ae6ba0",
      "WRITE",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6b2c.md#insn-00ae6b54) · [`00ae6b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6b2c.md#insn-00ae6b5c) · [`00ae6b3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6b2c.md#insn-00ae6b3c)
- 新版 [`00ae6b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b70.md#insn-00ae6b98) · [`00ae6ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b70.md#insn-00ae6ba0) · [`00ae6b80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6b70.md#insn-00ae6b80)

~~~diff
- 00ae6b54 ["INT_ADD", "register:40f0:8", ["const:ae6b54:8", "const:4:8"]]
- 00ae6b54 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6b98 ["INT_ADD", "register:40f0:8", ["const:ae6b98:8", "const:4:8"]]
+ 00ae6b98 ["CALL", null, ["callee:00bde090:8"]]
- 00ae6b54 bytes 3bdd0394
+ 00ae6b98 bytes 3edd0394
- 00ae6b5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00ae6b5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6ba0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
+ 00ae6ba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6b5c bytes 604202f9
+ 00ae6ba0 bytes 606202f9
- 00ae6b3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00ae6b3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6b80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
+ 00ae6b80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6b3c bytes 684242f9
+ 00ae6b80 bytes 686242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2df9c49a7e52cc1e6e709a85cc2fc04"></a>

### [`00ae6b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6b70.md) → [`00ae6bb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6bb4.md) _ZN8firebase4util16dex_class_loader10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae6be4",
      "incomplete_value": true,
      "site": "00ae6be4",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ba0",
      "incomplete_value": true,
      "site": "00ae6ba0",
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
            "const:480:8"
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
      "definition_site": "00ae6bc8",
      "incomplete_value": true,
      "site": "00ae6bc8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6b84",
      "incomplete_value": true,
      "site": "00ae6b84",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae6bd0",
      "incomplete_value": false,
      "site": "00ae6bdc",
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
            "const:d9a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6b8c",
      "incomplete_value": false,
      "site": "00ae6b98",
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
            "const:d00:8"
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
      "00ae6bc4",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6bd0",
      "PARAM",
      [
        "storage",
        "002a7d00",
        null,
        "string"
      ]
    ],
    [
      "00ae6be4",
      "WRITE",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6bc4",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6bd0",
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ],
    [
      "00ae6be4",
      "WRITE",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6b70.md#insn-00ae6b98) · [`00ae6ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6b70.md#insn-00ae6ba0) · [`00ae6b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6b70.md#insn-00ae6b80)
- 新版 [`00ae6bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6bb4.md#insn-00ae6bdc) · [`00ae6be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6bb4.md#insn-00ae6be4) · [`00ae6bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6bb4.md#insn-00ae6bc4)

~~~diff
- 00ae6b98 ["INT_ADD", "register:40f0:8", ["const:ae6b98:8", "const:4:8"]]
- 00ae6b98 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6bdc ["INT_ADD", "register:40f0:8", ["const:ae6bdc:8", "const:4:8"]]
+ 00ae6bdc ["CALL", null, ["callee:00bde090:8"]]
- 00ae6b98 bytes 2add0394
+ 00ae6bdc bytes 2ddd0394
- 00ae6ba0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00ae6ba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6be4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
+ 00ae6be4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6ba0 bytes 604202f9
+ 00ae6be4 bytes 606202f9
- 00ae6b80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:480:8"]]
- 00ae6b80 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6bc4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c0:8"]]
+ 00ae6bc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6b80 bytes 684242f9
+ 00ae6bc4 bytes 686242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d4ceefd1d499b6af8c1fee047d85120"></a>

### [`00ae6bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6bc0.md) → [`00ae6c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6c04.md) _ZN8firebase4util16dex_class_loader15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae6c8c",
      "incomplete_value": true,
      "site": "00ae6c8c",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6c48",
      "incomplete_value": true,
      "site": "00ae6c48",
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
            "const:488:8"
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
      "00ae6c18",
      "READ",
      [
        "storage",
        "010a0488",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6c38",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6c8c",
      "WRITE",
      [
        "storage",
        "010a0488",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae6c18",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6c38",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6c8c",
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6bc0.md#insn-00ae6c48) · [`00ae6bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6bc0.md#insn-00ae6bd4) · [`00ae6bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6bc0.md#insn-00ae6bf4)
- 新版 [`00ae6c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6c04.md#insn-00ae6c8c) · [`00ae6c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6c04.md#insn-00ae6c18) · [`00ae6c38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6c04.md#insn-00ae6c38)

~~~diff
- 00ae6c48 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae6c48 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:488:8"]]
- 00ae6c48 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae6c8c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae6c8c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4c8:8"]]
+ 00ae6c8c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae6c48 bytes a0221239
+ 00ae6c8c bytes a0221339
- 00ae6bd4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:488:8"]]
- 00ae6bd4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae6bd4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae6c18 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4c8:8"]]
+ 00ae6c18 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6c18 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae6bd4 bytes a8225239
+ 00ae6c18 bytes a8225339
- 00ae6bf4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:480:8"]]
- 00ae6bf4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6c38 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:4c0:8"]]
+ 00ae6c38 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6bf4 bytes 214142f9
+ 00ae6c38 bytes 216142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6361059dd92888f05fcdef16fd5e559f"></a>

### [`00ae6c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6c5c.md) → [`00ae6ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ca0.md) _ZN8firebase4util16dex_class_loader12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae6cdc",
      "incomplete_value": true,
      "site": "00ae6cdc",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6c98",
      "incomplete_value": true,
      "site": "00ae6c98",
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
            "const:488:8"
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
      "definition_site": "00ae6d2c",
      "incomplete_value": true,
      "site": "00ae6d2c",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ce8",
      "incomplete_value": true,
      "site": "00ae6ce8",
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
            "const:480:8"
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
      "definition_site": "00ae6cb8",
      "incomplete_value": true,
      "site": "00ae6cb8",
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
      "definition_site": "00ae6c74",
      "incomplete_value": true,
      "site": "00ae6c74",
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
      "00ae6cb4",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6cc0",
      "READ",
      [
        "storage",
        "010a0488",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6cdc",
      "WRITE",
      [
        "storage",
        "010a0488",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae6cb4",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6cc0",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6cdc",
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6c5c.md#insn-00ae6c98) · [`00ae6ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6c5c.md#insn-00ae6ce4) · [`00ae6ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6c5c.md#insn-00ae6ce8)
- 新版 [`00ae6cdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ca0.md#insn-00ae6cdc) · [`00ae6d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ca0.md#insn-00ae6d28) · [`00ae6d2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ca0.md#insn-00ae6d2c)

~~~diff
- 00ae6c98 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae6c98 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae6c98 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:488:8"]]
- 00ae6c98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae6cdc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae6cdc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae6cdc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4c8:8"]]
+ 00ae6cdc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae6c98 bytes bf221239
+ 00ae6cdc bytes bf221339
- 00ae6ce4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6ce4 ["INT_ADD", "register:40f0:8", ["const:ae6ce4:8", "const:4:8"]]
- 00ae6ce4 ["CALLIND", null, ["register:0:8"]]
+ 00ae6d28 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae6d28 ["INT_ADD", "register:40f0:8", ["const:ae6d28:8", "const:4:8"]]
+ 00ae6d28 ["CALLIND", null, ["register:0:8"]]
- 00ae6ce4 bytes 00013fd6
+ 00ae6d28 bytes 00013fd6
- 00ae6ce8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00ae6ce8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae6ce8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae6d2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
+ 00ae6d2c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae6d2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae6ce8 bytes 9f4202f9
+ 00ae6d2c bytes 9f6202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1ddee5be31ec8e2c1a6fc4f7585e387"></a>

### [`00ae6cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6cfc.md) → [`00ae6d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6d40.md) _ZN8firebase4util16dex_class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae6d80",
      "incomplete_value": true,
      "site": "00ae6d80",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6d3c",
      "incomplete_value": true,
      "site": "00ae6d3c",
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
            "const:480:8"
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
      "definition_site": "00ae6d64",
      "incomplete_value": false,
      "site": "00ae6d78",
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
            "const:d9a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6d20",
      "incomplete_value": false,
      "site": "00ae6d34",
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
            "const:d00:8"
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
      "00ae6d54",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6d64",
      "PARAM",
      [
        "storage",
        "002a7d00",
        null,
        "string"
      ]
    ],
    [
      "00ae6d80",
      "WRITE",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6d54",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6d64",
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ],
    [
      "00ae6d80",
      "WRITE",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6cfc.md#insn-00ae6d34) · [`00ae6d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6cfc.md#insn-00ae6d3c) · [`00ae6d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6cfc.md#insn-00ae6d10)
- 新版 [`00ae6d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6d40.md#insn-00ae6d78) · [`00ae6d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6d40.md#insn-00ae6d80) · [`00ae6d54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6d40.md#insn-00ae6d54)

~~~diff
- 00ae6d34 ["INT_ADD", "register:40f0:8", ["const:ae6d34:8", "const:4:8"]]
- 00ae6d34 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6d78 ["INT_ADD", "register:40f0:8", ["const:ae6d78:8", "const:4:8"]]
+ 00ae6d78 ["CALL", null, ["callee:00bde090:8"]]
- 00ae6d34 bytes c3dc0394
+ 00ae6d78 bytes c6dc0394
- 00ae6d3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00ae6d3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6d80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
+ 00ae6d80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6d3c bytes 804202f9
+ 00ae6d80 bytes 806202f9
- 00ae6d10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00ae6d10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6d54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
+ 00ae6d54 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6d10 bytes 814242f9
+ 00ae6d54 bytes 816242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15ffce82155b48cafc1f6e98243c6dff"></a>

### [`00ae6d6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6d6c.md) → [`00ae6db0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6db0.md) _ZN8firebase4util16dex_class_loader11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae6dcc",
      "incomplete_value": false,
      "site": "00ae6dd0",
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
      "definition_site": "00ae6d88",
      "incomplete_value": false,
      "site": "00ae6d8c",
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
      "definition_site": "00ae6ddc",
      "incomplete_value": true,
      "site": "00ae6de8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae6d98",
      "incomplete_value": true,
      "site": "00ae6da4",
      "value": [
        "LOAD",
        "8",
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
      "00ae6dcc",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae6ddc",
      "DATA",
      [
        "storage",
        "010a0490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6dcc",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae6ddc",
      "DATA",
      [
        "storage",
        "010a04d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6d6c.md#insn-00ae6d8c) · [`00ae6d88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6d6c.md#insn-00ae6d88) · [`00ae6d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6d6c.md#insn-00ae6d94)
- 新版 [`00ae6dd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6db0.md#insn-00ae6dd0) · [`00ae6dcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6db0.md#insn-00ae6dcc) · [`00ae6dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6db0.md#insn-00ae6dd8)

~~~diff
- 00ae6d8c ["INT_ADD", "register:40f0:8", ["const:ae6d8c:8", "const:4:8"]]
- 00ae6d8c ["CALL", null, ["callee:00bde180:8"]]
+ 00ae6dd0 ["INT_ADD", "register:40f0:8", ["const:ae6dd0:8", "const:4:8"]]
+ 00ae6dd0 ["CALL", null, ["callee:00bde180:8"]]
- 00ae6d8c bytes e9dc0394
+ 00ae6dd0 bytes ecdc0394
- 00ae6d88 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae6d88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6d88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6d88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae6dcc ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae6dcc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae6dcc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae6dcc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae6d88 bytes 00501791
+ 00ae6dcc bytes 001c1591
- 00ae6d94 ["COPY", "tmp:0:8", ["const:490:8"]]
- 00ae6d94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae6d94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae6d94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae6dd8 ["COPY", "tmp:0:8", ["const:4d0:8"]]
+ 00ae6dd8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae6dd8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae6dd8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae6d94 bytes 08411291
+ 00ae6dd8 bytes 08411391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f46cc5fce10f77b3ceca10a3a457dd2e"></a>

### [`00ae6da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6da8.md) → [`00ae6dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6dec.md) _ZN8firebase4util16dex_class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae6e2c",
      "incomplete_value": true,
      "site": "00ae6e2c",
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
            "const:4c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6de8",
      "incomplete_value": true,
      "site": "00ae6de8",
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
            "const:480:8"
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
      "definition_site": "00ae6e08",
      "incomplete_value": true,
      "site": "00ae6e08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6dc4",
      "incomplete_value": true,
      "site": "00ae6dc4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae6e10",
      "incomplete_value": false,
      "site": "00ae6e24",
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
            "const:d9a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6dcc",
      "incomplete_value": false,
      "site": "00ae6de0",
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
            "const:d00:8"
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
      "00ae6e00",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6e10",
      "PARAM",
      [
        "storage",
        "002a7d00",
        null,
        "string"
      ]
    ],
    [
      "00ae6e2c",
      "WRITE",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6e00",
      "READ",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6e10",
      "PARAM",
      [
        "storage",
        "002a7d9a",
        null,
        "string"
      ]
    ],
    [
      "00ae6e2c",
      "WRITE",
      [
        "storage",
        "010a04c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6da8.md#insn-00ae6de0) · [`00ae6de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6da8.md#insn-00ae6de8) · [`00ae6dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6da8.md#insn-00ae6dbc)
- 新版 [`00ae6e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6dec.md#insn-00ae6e24) · [`00ae6e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6dec.md#insn-00ae6e2c) · [`00ae6e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6dec.md#insn-00ae6e00)

~~~diff
- 00ae6de0 ["INT_ADD", "register:40f0:8", ["const:ae6de0:8", "const:4:8"]]
- 00ae6de0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6e24 ["INT_ADD", "register:40f0:8", ["const:ae6e24:8", "const:4:8"]]
+ 00ae6e24 ["CALL", null, ["callee:00bde090:8"]]
- 00ae6de0 bytes 98dc0394
+ 00ae6e24 bytes 9bdc0394
- 00ae6de8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00ae6de8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6e2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
+ 00ae6e2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6de8 bytes 804202f9
+ 00ae6e2c bytes 806202f9
- 00ae6dbc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:480:8"]]
- 00ae6dbc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6e00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c0:8"]]
+ 00ae6e00 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6dbc bytes 814242f9
+ 00ae6e00 bytes 816242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-76785c93e4814dd72403ab1993c3f9cb"></a>

### [`00ae6e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e18.md) → [`00ae6e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e5c.md) _ZN8firebase4util16dex_class_loader10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae6e78",
      "incomplete_value": false,
      "site": "00ae6e7c",
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
      "definition_site": "00ae6e34",
      "incomplete_value": false,
      "site": "00ae6e38",
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
      "definition_site": "00ae6e88",
      "incomplete_value": true,
      "site": "00ae6e94",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae6e44",
      "incomplete_value": true,
      "site": "00ae6e50",
      "value": [
        "LOAD",
        "8",
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
      "00ae6e78",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae6e88",
      "DATA",
      [
        "storage",
        "010a04a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae6e78",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae6e88",
      "DATA",
      [
        "storage",
        "010a04e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e18.md#insn-00ae6e38) · [`00ae6e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e18.md#insn-00ae6e34) · [`00ae6e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e18.md#insn-00ae6e40)
- 新版 [`00ae6e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e5c.md#insn-00ae6e7c) · [`00ae6e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e5c.md#insn-00ae6e78) · [`00ae6e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e5c.md#insn-00ae6e84)

~~~diff
- 00ae6e38 ["INT_ADD", "register:40f0:8", ["const:ae6e38:8", "const:4:8"]]
- 00ae6e38 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae6e7c ["INT_ADD", "register:40f0:8", ["const:ae6e7c:8", "const:4:8"]]
+ 00ae6e7c ["CALL", null, ["callee:00bde180:8"]]
- 00ae6e38 bytes bedc0394
+ 00ae6e7c bytes c1dc0394
- 00ae6e34 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae6e34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6e34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae6e34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae6e78 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae6e78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae6e78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae6e78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae6e34 bytes 00fc1991
+ 00ae6e78 bytes 00c81791
- 00ae6e40 ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 00ae6e40 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae6e40 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae6e40 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae6e84 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 00ae6e84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae6e84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae6e84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae6e40 bytes 08811291
+ 00ae6e84 bytes 08811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdc3400b2a20bb42f64b264919c5de8e"></a>

### [`00ae6e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e54.md) → [`00ae6e98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e98.md) _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0

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
      "definition_site": "00ae6ec4",
      "incomplete_value": true,
      "site": "00ae6ec4",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6e80",
      "incomplete_value": true,
      "site": "00ae6e80",
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
            "const:4a8:8"
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
      "definition_site": "00ae6eac",
      "incomplete_value": true,
      "site": "00ae6eac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6e68",
      "incomplete_value": true,
      "site": "00ae6e68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae6eb8",
      "incomplete_value": false,
      "site": "00ae6ebc",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6e74",
      "incomplete_value": false,
      "site": "00ae6e78",
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
            "const:e51:8"
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
      "00ae6ea8",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6eb8",
      "PARAM",
      [
        "storage",
        "002a4e51",
        null,
        "string"
      ]
    ],
    [
      "00ae6ec4",
      "WRITE",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6ea8",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6eb8",
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      "00ae6ec4",
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6e78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e54.md#insn-00ae6e78) · [`00ae6e80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e54.md#insn-00ae6e80) · [`00ae6e64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e54.md#insn-00ae6e64)
- 新版 [`00ae6ebc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e98.md#insn-00ae6ebc) · [`00ae6ec4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e98.md#insn-00ae6ec4) · [`00ae6ea8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6e98.md#insn-00ae6ea8)

~~~diff
- 00ae6e78 ["INT_ADD", "register:40f0:8", ["const:ae6e78:8", "const:4:8"]]
- 00ae6e78 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6ebc ["INT_ADD", "register:40f0:8", ["const:ae6ebc:8", "const:4:8"]]
+ 00ae6ebc ["CALL", null, ["callee:00bde090:8"]]
- 00ae6e78 bytes 72dc0394
+ 00ae6ebc bytes 75dc0394
- 00ae6e80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00ae6e80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6ec4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00ae6ec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6e80 bytes 605602f9
+ 00ae6ec4 bytes 607602f9
- 00ae6e64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00ae6e64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6ea8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00ae6ea8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6e64 bytes 685642f9
+ 00ae6ea8 bytes 687642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ffec1be033e45e22737284ef9ab1387"></a>

### [`00ae6e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e94.md) → [`00ae6ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ed8.md) _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00ae6f04",
      "incomplete_value": true,
      "site": "00ae6f04",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ec0",
      "incomplete_value": true,
      "site": "00ae6ec0",
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
            "const:4a8:8"
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
      "definition_site": "00ae6eec",
      "incomplete_value": true,
      "site": "00ae6eec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ea8",
      "incomplete_value": true,
      "site": "00ae6ea8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae6ef4",
      "incomplete_value": false,
      "site": "00ae6efc",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6eb0",
      "incomplete_value": false,
      "site": "00ae6eb8",
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
            "const:e51:8"
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
      "00ae6ee8",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6ef4",
      "PARAM",
      [
        "storage",
        "002a4e51",
        null,
        "string"
      ]
    ],
    [
      "00ae6f04",
      "WRITE",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6ee8",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6ef4",
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      "00ae6f04",
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e94.md#insn-00ae6eb8) · [`00ae6ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e94.md#insn-00ae6ec0) · [`00ae6ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6e94.md#insn-00ae6ea4)
- 新版 [`00ae6efc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ed8.md#insn-00ae6efc) · [`00ae6f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ed8.md#insn-00ae6f04) · [`00ae6ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6ed8.md#insn-00ae6ee8)

~~~diff
- 00ae6eb8 ["INT_ADD", "register:40f0:8", ["const:ae6eb8:8", "const:4:8"]]
- 00ae6eb8 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6efc ["INT_ADD", "register:40f0:8", ["const:ae6efc:8", "const:4:8"]]
+ 00ae6efc ["CALL", null, ["callee:00bde090:8"]]
- 00ae6eb8 bytes 62dc0394
+ 00ae6efc bytes 65dc0394
- 00ae6ec0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00ae6ec0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6f04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00ae6f04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6ec0 bytes 605602f9
+ 00ae6f04 bytes 607602f9
- 00ae6ea4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00ae6ea4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6ee8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00ae6ee8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6ea4 bytes 685642f9
+ 00ae6ee8 bytes 687642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe37d6a501852822ac81f318c57ce7ce"></a>

### [`00ae6ed4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6ed4.md) → [`00ae6f18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f18.md) _ZN8firebase4util9resources10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae6f48",
      "incomplete_value": true,
      "site": "00ae6f48",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f04",
      "incomplete_value": true,
      "site": "00ae6f04",
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
            "const:4a8:8"
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
      "definition_site": "00ae6f2c",
      "incomplete_value": true,
      "site": "00ae6f2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ee8",
      "incomplete_value": true,
      "site": "00ae6ee8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae6f38",
      "incomplete_value": false,
      "site": "00ae6f40",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ef4",
      "incomplete_value": false,
      "site": "00ae6efc",
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
            "const:e51:8"
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
      "00ae6f28",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6f38",
      "PARAM",
      [
        "storage",
        "002a4e51",
        null,
        "string"
      ]
    ],
    [
      "00ae6f48",
      "WRITE",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6f28",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6f38",
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      "00ae6f48",
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6ed4.md#insn-00ae6efc) · [`00ae6f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6ed4.md#insn-00ae6f04) · [`00ae6ee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6ed4.md#insn-00ae6ee4)
- 新版 [`00ae6f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f18.md#insn-00ae6f40) · [`00ae6f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f18.md#insn-00ae6f48) · [`00ae6f28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f18.md#insn-00ae6f28)

~~~diff
- 00ae6efc ["INT_ADD", "register:40f0:8", ["const:ae6efc:8", "const:4:8"]]
- 00ae6efc ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6f40 ["INT_ADD", "register:40f0:8", ["const:ae6f40:8", "const:4:8"]]
+ 00ae6f40 ["CALL", null, ["callee:00bde090:8"]]
- 00ae6efc bytes 51dc0394
+ 00ae6f40 bytes 54dc0394
- 00ae6f04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00ae6f04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6f48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00ae6f48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6f04 bytes 605602f9
+ 00ae6f48 bytes 607602f9
- 00ae6ee4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00ae6ee4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6f28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00ae6f28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6ee4 bytes 685642f9
+ 00ae6f28 bytes 687642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92ac64b3f867c595079318661654d60c"></a>

### [`00ae6f18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6f18.md) → [`00ae6f5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f5c.md) _ZN8firebase4util9resources10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae6f8c",
      "incomplete_value": true,
      "site": "00ae6f8c",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f48",
      "incomplete_value": true,
      "site": "00ae6f48",
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
            "const:4a8:8"
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
      "definition_site": "00ae6f70",
      "incomplete_value": true,
      "site": "00ae6f70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f2c",
      "incomplete_value": true,
      "site": "00ae6f2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae6f78",
      "incomplete_value": false,
      "site": "00ae6f84",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f34",
      "incomplete_value": false,
      "site": "00ae6f40",
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
            "const:e51:8"
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
      "00ae6f6c",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6f78",
      "PARAM",
      [
        "storage",
        "002a4e51",
        null,
        "string"
      ]
    ],
    [
      "00ae6f8c",
      "WRITE",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae6f6c",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6f78",
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      "00ae6f8c",
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6f18.md#insn-00ae6f40) · [`00ae6f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6f18.md#insn-00ae6f48) · [`00ae6f28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6f18.md#insn-00ae6f28)
- 新版 [`00ae6f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f5c.md#insn-00ae6f84) · [`00ae6f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f5c.md#insn-00ae6f8c) · [`00ae6f6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6f5c.md#insn-00ae6f6c)

~~~diff
- 00ae6f40 ["INT_ADD", "register:40f0:8", ["const:ae6f40:8", "const:4:8"]]
- 00ae6f40 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae6f84 ["INT_ADD", "register:40f0:8", ["const:ae6f84:8", "const:4:8"]]
+ 00ae6f84 ["CALL", null, ["callee:00bde090:8"]]
- 00ae6f40 bytes 40dc0394
+ 00ae6f84 bytes 43dc0394
- 00ae6f48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00ae6f48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6f8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00ae6f8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae6f48 bytes 605602f9
+ 00ae6f8c bytes 607602f9
- 00ae6f28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00ae6f28 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6f6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00ae6f6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae6f28 bytes 685642f9
+ 00ae6f6c bytes 687642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-78002e967516751c48e123a0036a0165"></a>

### [`00ae6f68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6f68.md) → [`00ae6fac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6fac.md) _ZN8firebase4util9resources15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae7034",
      "incomplete_value": true,
      "site": "00ae7034",
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
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6ff0",
      "incomplete_value": true,
      "site": "00ae6ff0",
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
            "const:4b0:8"
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
      "definition_site": "00ae6fe0",
      "incomplete_value": true,
      "site": "00ae6fec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae6f9c",
      "incomplete_value": true,
      "site": "00ae6fa8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a8:8"
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
      "00ae6fc0",
      "READ",
      [
        "storage",
        "010a04b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6fe0",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7034",
      "WRITE",
      [
        "storage",
        "010a04b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae6fc0",
      "READ",
      [
        "storage",
        "010a04f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae6fe0",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7034",
      "WRITE",
      [
        "storage",
        "010a04f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae6fa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6f68.md#insn-00ae6fa8) · [`00ae6ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6f68.md#insn-00ae6ff0) · [`00ae6f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae6/00ae6f68.md#insn-00ae6f7c)
- 新版 [`00ae6fec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6fac.md#insn-00ae6fec) · [`00ae7034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6fac.md#insn-00ae7034) · [`00ae6fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae6/00ae6fac.md#insn-00ae6fc0)

~~~diff
- 00ae6fa8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae6fa8 ["INT_ADD", "register:40f0:8", ["const:ae6fa8:8", "const:4:8"]]
- 00ae6fa8 ["CALLIND", null, ["register:0:8"]]
+ 00ae6fec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae6fec ["INT_ADD", "register:40f0:8", ["const:ae6fec:8", "const:4:8"]]
+ 00ae6fec ["CALLIND", null, ["register:0:8"]]
- 00ae6fa8 bytes 00013fd6
+ 00ae6fec bytes 00013fd6
- 00ae6ff0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae6ff0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4b0:8"]]
- 00ae6ff0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae7034 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae7034 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4f0:8"]]
+ 00ae7034 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae6ff0 bytes a0c21239
+ 00ae7034 bytes a0c21339
- 00ae6f7c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4b0:8"]]
- 00ae6f7c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae6f7c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae6fc0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4f0:8"]]
+ 00ae6fc0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6fc0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae6f7c bytes a8c25239
+ 00ae6fc0 bytes a8c25339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-02bc8e2a68cd790f7a7f3fff62a6ebc2"></a>

### [`00ae7004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7004.md) → [`00ae7048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7048.md) _ZN8firebase4util9resources12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae7084",
      "incomplete_value": true,
      "site": "00ae7084",
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
            "const:4f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7040",
      "incomplete_value": true,
      "site": "00ae7040",
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
            "const:4b0:8"
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
      "definition_site": "00ae70d4",
      "incomplete_value": true,
      "site": "00ae70d4",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7090",
      "incomplete_value": true,
      "site": "00ae7090",
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
            "const:4a8:8"
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
      "definition_site": "00ae7060",
      "incomplete_value": true,
      "site": "00ae7060",
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
      "definition_site": "00ae701c",
      "incomplete_value": true,
      "site": "00ae701c",
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
      "00ae705c",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7068",
      "READ",
      [
        "storage",
        "010a04b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7084",
      "WRITE",
      [
        "storage",
        "010a04b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae705c",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7068",
      "READ",
      [
        "storage",
        "010a04f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7084",
      "WRITE",
      [
        "storage",
        "010a04f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7004.md#insn-00ae7040) · [`00ae7090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7004.md#insn-00ae7090) · [`00ae7018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7004.md#insn-00ae7018)
- 新版 [`00ae7084`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7048.md#insn-00ae7084) · [`00ae70d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7048.md#insn-00ae70d4) · [`00ae705c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7048.md#insn-00ae705c)

~~~diff
- 00ae7040 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae7040 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae7040 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4b0:8"]]
- 00ae7040 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae7084 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae7084 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae7084 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4f0:8"]]
+ 00ae7084 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae7040 bytes bfc21239
+ 00ae7084 bytes bfc21339
- 00ae7090 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00ae7090 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae7090 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae70d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
+ 00ae70d4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae70d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae7090 bytes 9f5602f9
+ 00ae70d4 bytes 9f7602f9
- 00ae7018 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00ae7018 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae705c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
+ 00ae705c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7018 bytes 815642f9
+ 00ae705c bytes 817642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3972f74e454fe07d35152e2d8bfd25d"></a>

### [`00ae70a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae70a4.md) → [`00ae70e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae70e8.md) _ZN8firebase4util9resources14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae7128",
      "incomplete_value": true,
      "site": "00ae7128",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae70e4",
      "incomplete_value": true,
      "site": "00ae70e4",
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
            "const:4a8:8"
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
      "definition_site": "00ae7104",
      "incomplete_value": true,
      "site": "00ae7104",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae70c0",
      "incomplete_value": true,
      "site": "00ae70c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae70c0"
      ],
      [
        "FALL_THROUGH",
        "00ae7104"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7104",
      "incomplete_value": true,
      "site": "00ae7128",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae70c0",
      "incomplete_value": true,
      "site": "00ae70e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae70fc",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae710c",
      "PARAM",
      [
        "storage",
        "002a4e51",
        null,
        "string"
      ]
    ],
    [
      "00ae7128",
      "WRITE",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae70fc",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae710c",
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      "00ae7128",
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae70e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae70a4.md#insn-00ae70e4) · [`00ae70b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae70a4.md#insn-00ae70b8) · [`00ae70c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae70a4.md#insn-00ae70c8)
- 新版 [`00ae7128`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae70e8.md#insn-00ae7128) · [`00ae70fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae70e8.md#insn-00ae70fc) · [`00ae710c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae70e8.md#insn-00ae710c)

~~~diff
- 00ae70e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00ae70e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7128 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
+ 00ae7128 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae70e4 bytes 805602f9
+ 00ae7128 bytes 807602f9
- 00ae70b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00ae70b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae70fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
+ 00ae70fc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae70b8 bytes 815642f9
+ 00ae70fc bytes 817642f9
- 00ae70c8 ["COPY", "tmp:0:8", ["const:e51:8"]]
- 00ae70c8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae70c8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae70c8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae710c ["COPY", "tmp:0:8", ["const:edc:8"]]
+ 00ae710c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae710c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae710c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae70c8 bytes 63443991
+ 00ae710c bytes 63703b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-429eede149f727076ede9b5348e2e00f"></a>

### [`00ae7114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7114.md) → [`00ae7158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7158.md) _ZN8firebase4util9resources11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae7174",
      "incomplete_value": false,
      "site": "00ae7178",
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
      "definition_site": "00ae7130",
      "incomplete_value": false,
      "site": "00ae7134",
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
      "definition_site": "00ae7184",
      "incomplete_value": true,
      "site": "00ae7190",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae7140",
      "incomplete_value": true,
      "site": "00ae714c",
      "value": [
        "LOAD",
        "8",
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
      "00ae7174",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae7184",
      "DATA",
      [
        "storage",
        "010a04b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7174",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae7184",
      "DATA",
      [
        "storage",
        "010a04f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7114.md#insn-00ae7134) · [`00ae7130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7114.md#insn-00ae7130) · [`00ae713c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7114.md#insn-00ae713c)
- 新版 [`00ae7178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7158.md#insn-00ae7178) · [`00ae7174`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7158.md#insn-00ae7174) · [`00ae7180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7158.md#insn-00ae7180)

~~~diff
- 00ae7134 ["INT_ADD", "register:40f0:8", ["const:ae7134:8", "const:4:8"]]
- 00ae7134 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae7178 ["INT_ADD", "register:40f0:8", ["const:ae7178:8", "const:4:8"]]
+ 00ae7178 ["CALL", null, ["callee:00bde180:8"]]
- 00ae7134 bytes ffdb0394
+ 00ae7178 bytes 02dc0394
- 00ae7130 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae7130 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7130 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7130 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae7174 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae7174 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae7174 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae7174 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae7130 bytes 00501791
+ 00ae7174 bytes 001c1591
- 00ae713c ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 00ae713c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae713c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae713c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae7180 ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00ae7180 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae7180 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae7180 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae713c bytes 08e11291
+ 00ae7180 bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0124c384b2cb1910fc9b129972fef777"></a>

### [`00ae7150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7150.md) → [`00ae7194`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7194.md) _ZN8firebase4util9resources13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae71d4",
      "incomplete_value": true,
      "site": "00ae71d4",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7190",
      "incomplete_value": true,
      "site": "00ae7190",
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
            "const:4a8:8"
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
      "definition_site": "00ae71b0",
      "incomplete_value": true,
      "site": "00ae71b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae716c",
      "incomplete_value": true,
      "site": "00ae716c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae71b8",
      "incomplete_value": false,
      "site": "00ae71cc",
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
            "const:edc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7174",
      "incomplete_value": false,
      "site": "00ae7188",
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
            "const:e51:8"
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
      "00ae71a8",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae71b8",
      "PARAM",
      [
        "storage",
        "002a4e51",
        null,
        "string"
      ]
    ],
    [
      "00ae71d4",
      "WRITE",
      [
        "storage",
        "010a04a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae71a8",
      "READ",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae71b8",
      "PARAM",
      [
        "storage",
        "002a4edc",
        null,
        "string"
      ]
    ],
    [
      "00ae71d4",
      "WRITE",
      [
        "storage",
        "010a04e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7150.md#insn-00ae7188) · [`00ae7190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7150.md#insn-00ae7190) · [`00ae7164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7150.md#insn-00ae7164)
- 新版 [`00ae71cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7194.md#insn-00ae71cc) · [`00ae71d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7194.md#insn-00ae71d4) · [`00ae71a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7194.md#insn-00ae71a8)

~~~diff
- 00ae7188 ["INT_ADD", "register:40f0:8", ["const:ae7188:8", "const:4:8"]]
- 00ae7188 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae71cc ["INT_ADD", "register:40f0:8", ["const:ae71cc:8", "const:4:8"]]
+ 00ae71cc ["CALL", null, ["callee:00bde090:8"]]
- 00ae7188 bytes aedb0394
+ 00ae71cc bytes b1db0394
- 00ae7190 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00ae7190 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae71d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
+ 00ae71d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7190 bytes 805602f9
+ 00ae71d4 bytes 807602f9
- 00ae7164 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00ae7164 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae71a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
+ 00ae71a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7164 bytes 815642f9
+ 00ae71a8 bytes 817642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-966bd57456a13f2b249c80eda8399e4f"></a>

### [`00ae71c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae71c0.md) → [`00ae7204`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7204.md) _ZN8firebase4util9resources10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae7220",
      "incomplete_value": false,
      "site": "00ae7224",
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
      "definition_site": "00ae71dc",
      "incomplete_value": false,
      "site": "00ae71e0",
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
      "definition_site": "00ae7230",
      "incomplete_value": true,
      "site": "00ae723c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae71ec",
      "incomplete_value": true,
      "site": "00ae71f8",
      "value": [
        "LOAD",
        "8",
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
      "00ae7220",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae7230",
      "DATA",
      [
        "storage",
        "010a04c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae7220",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae7230",
      "DATA",
      [
        "storage",
        "010a0500",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae71e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae71c0.md#insn-00ae71e0) · [`00ae71dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae71c0.md#insn-00ae71dc) · [`00ae71e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae71c0.md#insn-00ae71e8)
- 新版 [`00ae7224`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7204.md#insn-00ae7224) · [`00ae7220`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7204.md#insn-00ae7220) · [`00ae722c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7204.md#insn-00ae722c)

~~~diff
- 00ae71e0 ["INT_ADD", "register:40f0:8", ["const:ae71e0:8", "const:4:8"]]
- 00ae71e0 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae7224 ["INT_ADD", "register:40f0:8", ["const:ae7224:8", "const:4:8"]]
+ 00ae7224 ["CALL", null, ["callee:00bde180:8"]]
- 00ae71e0 bytes d4db0394
+ 00ae7224 bytes d7db0394
- 00ae71dc ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae71dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae71dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae71dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae7220 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae7220 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae7220 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae7220 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae71dc bytes 00fc1991
+ 00ae7220 bytes 00c81791
- 00ae71e8 ["COPY", "tmp:0:8", ["const:4c0:8"]]
- 00ae71e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae71e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae71e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae722c ["COPY", "tmp:0:8", ["const:500:8"]]
+ 00ae722c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae722c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae722c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae71e8 bytes 08011391
+ 00ae722c bytes 08011491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-639e285738e649c40fd19f3d320c7e20"></a>

### [`00ae71fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae71fc.md) → [`00ae7240`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7240.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

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
      "definition_site": "00ae726c",
      "incomplete_value": true,
      "site": "00ae726c",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7228",
      "incomplete_value": true,
      "site": "00ae7228",
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
            "const:4c8:8"
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
      "definition_site": "00ae7254",
      "incomplete_value": true,
      "site": "00ae7254",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7210",
      "incomplete_value": true,
      "site": "00ae7210",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae7210"
      ],
      [
        "FALL_THROUGH",
        "00ae7254"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7254",
      "incomplete_value": true,
      "site": "00ae726c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7210",
      "incomplete_value": true,
      "site": "00ae7228",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae7250",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae726c",
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7250",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae726c",
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae71fc.md#insn-00ae7228) · [`00ae720c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae71fc.md#insn-00ae720c) · [`00ae7220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae71fc.md#insn-00ae7220)
- 新版 [`00ae726c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7240.md#insn-00ae726c) · [`00ae7250`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7240.md#insn-00ae7250) · [`00ae7264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7240.md#insn-00ae7264)

~~~diff
- 00ae7228 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00ae7228 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae726c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00ae726c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7228 bytes 606602f9
+ 00ae726c bytes 608602f9
- 00ae720c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00ae720c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7250 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00ae7250 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae720c bytes 686642f9
+ 00ae7250 bytes 688642f9
- 00ae7220 ["INT_ADD", "register:40f0:8", ["const:ae7220:8", "const:4:8"]]
- 00ae7220 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae7264 ["INT_ADD", "register:40f0:8", ["const:ae7264:8", "const:4:8"]]
+ 00ae7264 ["CALL", null, ["callee:00bde090:8"]]
- 00ae7220 bytes 88db0394
+ 00ae7264 bytes 8bdb0394
~~~


<a id="compare-72f9f0ebbe395dbe3ad060070d25c06a"></a>

### [`00ae723c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae723c.md) → [`00ae7280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7280.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00ae72ac",
      "incomplete_value": true,
      "site": "00ae72ac",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7268",
      "incomplete_value": true,
      "site": "00ae7268",
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
            "const:4c8:8"
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
      "definition_site": "00ae7294",
      "incomplete_value": true,
      "site": "00ae7294",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7250",
      "incomplete_value": true,
      "site": "00ae7250",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae7250"
      ],
      [
        "FALL_THROUGH",
        "00ae7294"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7294",
      "incomplete_value": true,
      "site": "00ae72ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7250",
      "incomplete_value": true,
      "site": "00ae7268",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae7290",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae72ac",
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7290",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae72ac",
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae723c.md#insn-00ae7268) · [`00ae724c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae723c.md#insn-00ae724c) · [`00ae7260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae723c.md#insn-00ae7260)
- 新版 [`00ae72ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7280.md#insn-00ae72ac) · [`00ae7290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7280.md#insn-00ae7290) · [`00ae72a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7280.md#insn-00ae72a4)

~~~diff
- 00ae7268 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00ae7268 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae72ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00ae72ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7268 bytes 606602f9
+ 00ae72ac bytes 608602f9
- 00ae724c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00ae724c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7290 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00ae7290 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae724c bytes 686642f9
+ 00ae7290 bytes 688642f9
- 00ae7260 ["INT_ADD", "register:40f0:8", ["const:ae7260:8", "const:4:8"]]
- 00ae7260 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae72a4 ["INT_ADD", "register:40f0:8", ["const:ae72a4:8", "const:4:8"]]
+ 00ae72a4 ["CALL", null, ["callee:00bde090:8"]]
- 00ae7260 bytes 78db0394
+ 00ae72a4 bytes 7bdb0394
~~~


<a id="compare-49e26a5d6afd743b2679de64ec0262d6"></a>

### [`00ae727c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae727c.md) → [`00ae72c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae72c0.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae72f0",
      "incomplete_value": true,
      "site": "00ae72f0",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae72ac",
      "incomplete_value": true,
      "site": "00ae72ac",
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
            "const:4c8:8"
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
      "definition_site": "00ae72d4",
      "incomplete_value": true,
      "site": "00ae72d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7290",
      "incomplete_value": true,
      "site": "00ae7290",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae7290"
      ],
      [
        "FALL_THROUGH",
        "00ae72d4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae72d4",
      "incomplete_value": true,
      "site": "00ae72f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7290",
      "incomplete_value": true,
      "site": "00ae72ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae72d0",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae72f0",
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae72d0",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae72f0",
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae72ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae727c.md#insn-00ae72ac) · [`00ae728c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae727c.md#insn-00ae728c) · [`00ae72a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae727c.md#insn-00ae72a4)
- 新版 [`00ae72f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae72c0.md#insn-00ae72f0) · [`00ae72d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae72c0.md#insn-00ae72d0) · [`00ae72e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae72c0.md#insn-00ae72e8)

~~~diff
- 00ae72ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00ae72ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae72f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00ae72f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae72ac bytes 606602f9
+ 00ae72f0 bytes 608602f9
- 00ae728c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00ae728c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae72d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00ae72d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae728c bytes 686642f9
+ 00ae72d0 bytes 688642f9
- 00ae72a4 ["INT_ADD", "register:40f0:8", ["const:ae72a4:8", "const:4:8"]]
- 00ae72a4 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae72e8 ["INT_ADD", "register:40f0:8", ["const:ae72e8:8", "const:4:8"]]
+ 00ae72e8 ["CALL", null, ["callee:00bde090:8"]]
- 00ae72a4 bytes 67db0394
+ 00ae72e8 bytes 6adb0394
~~~


<a id="compare-c42e9e5b6d5c65ff815c3af258d3e0ae"></a>

### [`00ae72c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae72c0.md) → [`00ae7304`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7304.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae7334",
      "incomplete_value": true,
      "site": "00ae7334",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae72f0",
      "incomplete_value": true,
      "site": "00ae72f0",
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
            "const:4c8:8"
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
      "definition_site": "00ae7318",
      "incomplete_value": true,
      "site": "00ae7318",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae72d4",
      "incomplete_value": true,
      "site": "00ae72d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae72d4"
      ],
      [
        "FALL_THROUGH",
        "00ae7318"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7318",
      "incomplete_value": true,
      "site": "00ae7334",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae72d4",
      "incomplete_value": true,
      "site": "00ae72f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae7314",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7334",
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7314",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7334",
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae72f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae72c0.md#insn-00ae72f0) · [`00ae72d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae72c0.md#insn-00ae72d0) · [`00ae72e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae72c0.md#insn-00ae72e8)
- 新版 [`00ae7334`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7304.md#insn-00ae7334) · [`00ae7314`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7304.md#insn-00ae7314) · [`00ae732c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7304.md#insn-00ae732c)

~~~diff
- 00ae72f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00ae72f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7334 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00ae7334 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae72f0 bytes 606602f9
+ 00ae7334 bytes 608602f9
- 00ae72d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
- 00ae72d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7314 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:508:8"]]
+ 00ae7314 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae72d0 bytes 686642f9
+ 00ae7314 bytes 688642f9
- 00ae72e8 ["INT_ADD", "register:40f0:8", ["const:ae72e8:8", "const:4:8"]]
- 00ae72e8 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae732c ["INT_ADD", "register:40f0:8", ["const:ae732c:8", "const:4:8"]]
+ 00ae732c ["CALL", null, ["callee:00bde090:8"]]
- 00ae72e8 bytes 56db0394
+ 00ae732c bytes 59db0394
~~~


<a id="compare-e8f35e3e389a28678f426bc93d532948"></a>

### [`00ae7310`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7310.md) → [`00ae7354`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7354.md) _ZN8firebase4util8activity15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae73dc",
      "incomplete_value": true,
      "site": "00ae73dc",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7398",
      "incomplete_value": true,
      "site": "00ae7398",
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
            "const:4d0:8"
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
      "definition_site": "00ae7388",
      "incomplete_value": true,
      "site": "00ae7394",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:508:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7344",
      "incomplete_value": true,
      "site": "00ae7350",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
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
      "00ae7368",
      "READ",
      [
        "storage",
        "010a04d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7388",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae73dc",
      "WRITE",
      [
        "storage",
        "010a04d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae7368",
      "READ",
      [
        "storage",
        "010a0510",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7388",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae73dc",
      "WRITE",
      [
        "storage",
        "010a0510",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7310.md#insn-00ae7350) · [`00ae7398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7310.md#insn-00ae7398) · [`00ae7324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7310.md#insn-00ae7324)
- 新版 [`00ae7394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7354.md#insn-00ae7394) · [`00ae73dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7354.md#insn-00ae73dc) · [`00ae7368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7354.md#insn-00ae7368)

~~~diff
- 00ae7350 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7350 ["INT_ADD", "register:40f0:8", ["const:ae7350:8", "const:4:8"]]
- 00ae7350 ["CALLIND", null, ["register:0:8"]]
+ 00ae7394 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae7394 ["INT_ADD", "register:40f0:8", ["const:ae7394:8", "const:4:8"]]
+ 00ae7394 ["CALLIND", null, ["register:0:8"]]
- 00ae7350 bytes 00013fd6
+ 00ae7394 bytes 00013fd6
- 00ae7398 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae7398 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4d0:8"]]
- 00ae7398 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae73dc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae73dc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:510:8"]]
+ 00ae73dc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae7398 bytes a0421339
+ 00ae73dc bytes a0421439
- 00ae7324 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4d0:8"]]
- 00ae7324 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae7324 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae7368 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:510:8"]]
+ 00ae7368 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7368 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae7324 bytes a8425339
+ 00ae7368 bytes a8425439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-29d09fb9d05e5b1e9801e28fd5031169"></a>

### [`00ae73ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae73ac.md) → [`00ae73f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae73f0.md) _ZN8firebase4util8activity12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae742c",
      "incomplete_value": true,
      "site": "00ae742c",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae73e8",
      "incomplete_value": true,
      "site": "00ae73e8",
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
            "const:4d0:8"
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
      "definition_site": "00ae747c",
      "incomplete_value": true,
      "site": "00ae747c",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7438",
      "incomplete_value": true,
      "site": "00ae7438",
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
            "const:4c8:8"
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
      "definition_site": "00ae7408",
      "incomplete_value": true,
      "site": "00ae7408",
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
      "definition_site": "00ae73c4",
      "incomplete_value": true,
      "site": "00ae73c4",
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
      "00ae7404",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7410",
      "READ",
      [
        "storage",
        "010a04d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae742c",
      "WRITE",
      [
        "storage",
        "010a04d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae7404",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7410",
      "READ",
      [
        "storage",
        "010a0510",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae742c",
      "WRITE",
      [
        "storage",
        "010a0510",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae73e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae73ac.md#insn-00ae73e8) · [`00ae7438`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae73ac.md#insn-00ae7438) · [`00ae73c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae73ac.md#insn-00ae73c0)
- 新版 [`00ae742c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae73f0.md#insn-00ae742c) · [`00ae747c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae73f0.md#insn-00ae747c) · [`00ae7404`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae73f0.md#insn-00ae7404)

~~~diff
- 00ae73e8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae73e8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae73e8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4d0:8"]]
- 00ae73e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae742c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae742c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae742c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:510:8"]]
+ 00ae742c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae73e8 bytes bf421339
+ 00ae742c bytes bf421439
- 00ae7438 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
- 00ae7438 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae7438 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae747c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
+ 00ae747c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae747c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae7438 bytes 9f6602f9
+ 00ae747c bytes 9f8602f9
- 00ae73c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
- 00ae73c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7404 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
+ 00ae7404 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae73c0 bytes 816642f9
+ 00ae7404 bytes 818642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d25eb7f08376dd70f3d3a2cb3eca053"></a>

### [`00ae744c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae744c.md) → [`00ae7490`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7490.md) _ZN8firebase4util8activity14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae74d0",
      "incomplete_value": true,
      "site": "00ae74d0",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae748c",
      "incomplete_value": true,
      "site": "00ae748c",
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
            "const:4c8:8"
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
      "definition_site": "00ae74ac",
      "incomplete_value": true,
      "site": "00ae74ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7468",
      "incomplete_value": true,
      "site": "00ae7468",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae7468"
      ],
      [
        "FALL_THROUGH",
        "00ae74ac"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae74ac",
      "incomplete_value": true,
      "site": "00ae74d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7468",
      "incomplete_value": true,
      "site": "00ae748c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae74a4",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae74d0",
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae74e4",
      "PARAM",
      [
        "storage",
        "00c0fe10",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ae74a4",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae74d0",
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae74e4",
      "PARAM",
      [
        "storage",
        "00c0fe60",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae748c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae744c.md#insn-00ae748c) · [`00ae7460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae744c.md#insn-00ae7460) · [`00ae7484`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae744c.md#insn-00ae7484)
- 新版 [`00ae74d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7490.md#insn-00ae74d0) · [`00ae74a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7490.md#insn-00ae74a4) · [`00ae74c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7490.md#insn-00ae74c8)

~~~diff
- 00ae748c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
- 00ae748c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae74d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
+ 00ae74d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae748c bytes 806602f9
+ 00ae74d0 bytes 808602f9
- 00ae7460 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
- 00ae7460 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae74a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
+ 00ae74a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7460 bytes 816642f9
+ 00ae74a4 bytes 818642f9
- 00ae7484 ["INT_ADD", "register:40f0:8", ["const:ae7484:8", "const:4:8"]]
- 00ae7484 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae74c8 ["INT_ADD", "register:40f0:8", ["const:ae74c8:8", "const:4:8"]]
+ 00ae74c8 ["CALL", null, ["callee:00bde090:8"]]
- 00ae7484 bytes efda0394
+ 00ae74c8 bytes f2da0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9fadbd908ef0077efc7515783d97ca0"></a>

### [`00ae74bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae74bc.md) → [`00ae7500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7500.md) _ZN8firebase4util8activity11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde680.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde6d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6d0.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00ae751c",
      "incomplete_value": false,
      "site": "00ae7520",
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
      "definition_site": "00ae74d8",
      "incomplete_value": false,
      "site": "00ae74dc",
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
      "definition_site": "00ae752c",
      "incomplete_value": true,
      "site": "00ae7538",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae74e8",
      "incomplete_value": true,
      "site": "00ae74f4",
      "value": [
        "LOAD",
        "8",
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
      "00ae751c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae752c",
      "DATA",
      [
        "storage",
        "010a04d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae751c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae752c",
      "DATA",
      [
        "storage",
        "010a0518",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae74dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae74bc.md#insn-00ae74dc) · [`00ae74d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae74bc.md#insn-00ae74d8) · [`00ae74e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae74bc.md#insn-00ae74e4)
- 新版 [`00ae7520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7500.md#insn-00ae7520) · [`00ae751c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7500.md#insn-00ae751c) · [`00ae7528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7500.md#insn-00ae7528)

~~~diff
- 00ae74dc ["INT_ADD", "register:40f0:8", ["const:ae74dc:8", "const:4:8"]]
- 00ae74dc ["CALL", null, ["callee:00bde180:8"]]
+ 00ae7520 ["INT_ADD", "register:40f0:8", ["const:ae7520:8", "const:4:8"]]
+ 00ae7520 ["CALL", null, ["callee:00bde180:8"]]
- 00ae74dc bytes 15db0394
+ 00ae7520 bytes 18db0394
- 00ae74d8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae74d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae74d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae74d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae751c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae751c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae751c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae751c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae74d8 bytes 00501791
+ 00ae751c bytes 001c1591
- 00ae74e4 ["COPY", "tmp:0:8", ["const:4d8:8"]]
- 00ae74e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae74e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae74e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae7528 ["COPY", "tmp:0:8", ["const:518:8"]]
+ 00ae7528 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae7528 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae7528 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae74e4 bytes 08611391
+ 00ae7528 bytes 08611491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f06815660ac188fe59200f7fdd09e9f"></a>

### [`00ae74f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae74f8.md) → [`00ae753c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae753c.md) _ZN8firebase4util8activity13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae757c",
      "incomplete_value": true,
      "site": "00ae757c",
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
            "const:508:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7538",
      "incomplete_value": true,
      "site": "00ae7538",
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
            "const:4c8:8"
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
      "definition_site": "00ae7558",
      "incomplete_value": true,
      "site": "00ae7558",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7514",
      "incomplete_value": true,
      "site": "00ae7514",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae7514"
      ],
      [
        "FALL_THROUGH",
        "00ae7558"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7558",
      "incomplete_value": true,
      "site": "00ae757c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7514",
      "incomplete_value": true,
      "site": "00ae7538",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae7550",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae757c",
      "WRITE",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7594",
      "PARAM",
      [
        "storage",
        "010a0528",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae7550",
      "READ",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae757c",
      "WRITE",
      [
        "storage",
        "010a0508",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7594",
      "PARAM",
      [
        "storage",
        "010a0568",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae74f8.md#insn-00ae7538) · [`00ae750c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae74f8.md#insn-00ae750c) · [`00ae7530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae74f8.md#insn-00ae7530)
- 新版 [`00ae757c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae753c.md#insn-00ae757c) · [`00ae7550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae753c.md#insn-00ae7550) · [`00ae7574`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae753c.md#insn-00ae7574)

~~~diff
- 00ae7538 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
- 00ae7538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae757c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
+ 00ae757c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7538 bytes 806602f9
+ 00ae757c bytes 808602f9
- 00ae750c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
- 00ae750c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7550 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:508:8"]]
+ 00ae7550 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae750c bytes 816642f9
+ 00ae7550 bytes 818642f9
- 00ae7530 ["INT_ADD", "register:40f0:8", ["const:ae7530:8", "const:4:8"]]
- 00ae7530 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae7574 ["INT_ADD", "register:40f0:8", ["const:ae7574:8", "const:4:8"]]
+ 00ae7574 ["CALL", null, ["callee:00bde090:8"]]
- 00ae7530 bytes c4da0394
+ 00ae7574 bytes c7da0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ab9d4c1367c92495f8a4ca03020030d"></a>

### [`00ae7568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7568.md) → [`00ae75ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75ac.md) _ZN8firebase4util8activity10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae75c8",
      "incomplete_value": false,
      "site": "00ae75cc",
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
      "definition_site": "00ae7584",
      "incomplete_value": false,
      "site": "00ae7588",
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
      "definition_site": "00ae75d8",
      "incomplete_value": true,
      "site": "00ae75e4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae7594",
      "incomplete_value": true,
      "site": "00ae75a0",
      "value": [
        "LOAD",
        "8",
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
      "00ae75c8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae75d8",
      "DATA",
      [
        "storage",
        "010a0528",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae75c8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae75d8",
      "DATA",
      [
        "storage",
        "010a0568",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7568.md#insn-00ae7588) · [`00ae7584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7568.md#insn-00ae7584) · [`00ae7590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7568.md#insn-00ae7590)
- 新版 [`00ae75cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75ac.md#insn-00ae75cc) · [`00ae75c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75ac.md#insn-00ae75c8) · [`00ae75d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75ac.md#insn-00ae75d4)

~~~diff
- 00ae7588 ["INT_ADD", "register:40f0:8", ["const:ae7588:8", "const:4:8"]]
- 00ae7588 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae75cc ["INT_ADD", "register:40f0:8", ["const:ae75cc:8", "const:4:8"]]
+ 00ae75cc ["CALL", null, ["callee:00bde180:8"]]
- 00ae7588 bytes eada0394
+ 00ae75cc bytes edda0394
- 00ae7584 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae7584 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7584 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7584 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae75c8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae75c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae75c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae75c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae7584 bytes 00fc1991
+ 00ae75c8 bytes 00c81791
- 00ae7590 ["COPY", "tmp:0:8", ["const:528:8"]]
- 00ae7590 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae7590 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae7590 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae75d4 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00ae75d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae75d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae75d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae7590 bytes 08a11491
+ 00ae75d4 bytes 08a11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c437404007b97bfbcf33736933e70450"></a>

### [`00ae75a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae75a4.md) → [`00ae75e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75e8.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00ae7614",
      "incomplete_value": true,
      "site": "00ae7614",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae75d0",
      "incomplete_value": true,
      "site": "00ae75d0",
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
            "const:530:8"
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
      "definition_site": "00ae75fc",
      "incomplete_value": true,
      "site": "00ae75fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae75b8",
      "incomplete_value": true,
      "site": "00ae75b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae7608",
      "incomplete_value": false,
      "site": "00ae760c",
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
            "const:497:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae75c4",
      "incomplete_value": false,
      "site": "00ae75c8",
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
            "const:524:8"
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
      "00ae75f8",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7608",
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ],
    [
      "00ae7614",
      "WRITE",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae75f8",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7608",
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      "00ae7614",
      "WRITE",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae75c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae75a4.md#insn-00ae75c8) · [`00ae75d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae75a4.md#insn-00ae75d0) · [`00ae75b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae75a4.md#insn-00ae75b4)
- 新版 [`00ae760c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75e8.md#insn-00ae760c) · [`00ae7614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75e8.md#insn-00ae7614) · [`00ae75f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae75e8.md#insn-00ae75f8)

~~~diff
- 00ae75c8 ["INT_ADD", "register:40f0:8", ["const:ae75c8:8", "const:4:8"]]
- 00ae75c8 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae760c ["INT_ADD", "register:40f0:8", ["const:ae760c:8", "const:4:8"]]
+ 00ae760c ["CALL", null, ["callee:00bde090:8"]]
- 00ae75c8 bytes 9eda0394
+ 00ae760c bytes a1da0394
- 00ae75d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00ae75d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7614 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00ae7614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae75d0 bytes 609a02f9
+ 00ae7614 bytes 60ba02f9
- 00ae75b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00ae75b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae75f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00ae75f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae75b4 bytes 689a42f9
+ 00ae75f8 bytes 68ba42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5b786feceeef21b35d51548d9c90c162"></a>

### [`00ae75e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae75e4.md) → [`00ae7628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7628.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00ae7654",
      "incomplete_value": true,
      "site": "00ae7654",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7610",
      "incomplete_value": true,
      "site": "00ae7610",
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
            "const:530:8"
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
      "definition_site": "00ae763c",
      "incomplete_value": true,
      "site": "00ae763c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae75f8",
      "incomplete_value": true,
      "site": "00ae75f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae7644",
      "incomplete_value": false,
      "site": "00ae764c",
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
            "const:497:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7600",
      "incomplete_value": false,
      "site": "00ae7608",
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
            "const:524:8"
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
      "00ae7638",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7644",
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ],
    [
      "00ae7654",
      "WRITE",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7638",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7644",
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      "00ae7654",
      "WRITE",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae75e4.md#insn-00ae7608) · [`00ae7610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae75e4.md#insn-00ae7610) · [`00ae75f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae75e4.md#insn-00ae75f4)
- 新版 [`00ae764c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7628.md#insn-00ae764c) · [`00ae7654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7628.md#insn-00ae7654) · [`00ae7638`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7628.md#insn-00ae7638)

~~~diff
- 00ae7608 ["INT_ADD", "register:40f0:8", ["const:ae7608:8", "const:4:8"]]
- 00ae7608 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae764c ["INT_ADD", "register:40f0:8", ["const:ae764c:8", "const:4:8"]]
+ 00ae764c ["CALL", null, ["callee:00bde090:8"]]
- 00ae7608 bytes 8eda0394
+ 00ae764c bytes 91da0394
- 00ae7610 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00ae7610 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7654 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00ae7654 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7610 bytes 609a02f9
+ 00ae7654 bytes 60ba02f9
- 00ae75f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00ae75f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7638 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00ae7638 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae75f4 bytes 689a42f9
+ 00ae7638 bytes 68ba42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb1f251dc7a3520551d5bd5472e2c56f"></a>

### [`00ae7624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7624.md) → [`00ae7668`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7668.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae7698",
      "incomplete_value": true,
      "site": "00ae7698",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7654",
      "incomplete_value": true,
      "site": "00ae7654",
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
            "const:530:8"
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
      "definition_site": "00ae767c",
      "incomplete_value": true,
      "site": "00ae767c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7638",
      "incomplete_value": true,
      "site": "00ae7638",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae7688",
      "incomplete_value": true,
      "site": "00ae7690",
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
            "const:497:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7644",
      "incomplete_value": true,
      "site": "00ae764c",
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
            "const:524:8"
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
      "00ae7678",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7688",
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ],
    [
      "00ae7698",
      "WRITE",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7678",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7688",
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      "00ae7698",
      "WRITE",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae764c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7624.md#insn-00ae764c) · [`00ae7654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7624.md#insn-00ae7654) · [`00ae7634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7624.md#insn-00ae7634)
- 新版 [`00ae7690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7668.md#insn-00ae7690) · [`00ae7698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7668.md#insn-00ae7698) · [`00ae7678`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7668.md#insn-00ae7678)

~~~diff
- 00ae764c ["INT_ADD", "register:40f0:8", ["const:ae764c:8", "const:4:8"]]
- 00ae764c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae7690 ["INT_ADD", "register:40f0:8", ["const:ae7690:8", "const:4:8"]]
+ 00ae7690 ["CALL", null, ["callee:00bde090:8"]]
- 00ae764c bytes 7dda0394
+ 00ae7690 bytes 80da0394
- 00ae7654 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00ae7654 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7698 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00ae7698 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7654 bytes 609a02f9
+ 00ae7698 bytes 60ba02f9
- 00ae7634 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00ae7634 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7678 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00ae7678 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7634 bytes 689a42f9
+ 00ae7678 bytes 68ba42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-209996687a3acd430c8fdc8abcbb489a"></a>

### [`00ae7668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7668.md) → [`00ae76ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76ac.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae76dc",
      "incomplete_value": true,
      "site": "00ae76dc",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7698",
      "incomplete_value": true,
      "site": "00ae7698",
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
            "const:530:8"
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
      "definition_site": "00ae76c0",
      "incomplete_value": true,
      "site": "00ae76c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae767c",
      "incomplete_value": true,
      "site": "00ae767c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae76c8",
      "incomplete_value": false,
      "site": "00ae76d4",
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
            "const:497:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7684",
      "incomplete_value": false,
      "site": "00ae7690",
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
            "const:524:8"
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
      "00ae76bc",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae76c8",
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ],
    [
      "00ae76dc",
      "WRITE",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae76bc",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae76c8",
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      "00ae76dc",
      "WRITE",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7668.md#insn-00ae7690) · [`00ae7698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7668.md#insn-00ae7698) · [`00ae7678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7668.md#insn-00ae7678)
- 新版 [`00ae76d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76ac.md#insn-00ae76d4) · [`00ae76dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76ac.md#insn-00ae76dc) · [`00ae76bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76ac.md#insn-00ae76bc)

~~~diff
- 00ae7690 ["INT_ADD", "register:40f0:8", ["const:ae7690:8", "const:4:8"]]
- 00ae7690 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae76d4 ["INT_ADD", "register:40f0:8", ["const:ae76d4:8", "const:4:8"]]
+ 00ae76d4 ["CALL", null, ["callee:00bde090:8"]]
- 00ae7690 bytes 6cda0394
+ 00ae76d4 bytes 6fda0394
- 00ae7698 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00ae7698 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae76dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00ae76dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7698 bytes 609a02f9
+ 00ae76dc bytes 60ba02f9
- 00ae7678 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00ae7678 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae76bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00ae76bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7678 bytes 689a42f9
+ 00ae76bc bytes 68ba42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df7abcab58760cb57e569f2e168861c5"></a>

### [`00ae76b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae76b8.md) → [`00ae76fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76fc.md) _ZN8firebase4util10array_list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae7784",
      "incomplete_value": true,
      "site": "00ae7784",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7740",
      "incomplete_value": true,
      "site": "00ae7740",
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
            "const:538:8"
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
      "definition_site": "00ae7730",
      "incomplete_value": true,
      "site": "00ae773c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae76ec",
      "incomplete_value": true,
      "site": "00ae76f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:530:8"
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
      "00ae7710",
      "READ",
      [
        "storage",
        "010a0538",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7730",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7784",
      "WRITE",
      [
        "storage",
        "010a0538",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae7710",
      "READ",
      [
        "storage",
        "010a0578",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7730",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7784",
      "WRITE",
      [
        "storage",
        "010a0578",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae76f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae76b8.md#insn-00ae76f8) · [`00ae7740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae76b8.md#insn-00ae7740) · [`00ae76cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae76b8.md#insn-00ae76cc)
- 新版 [`00ae773c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76fc.md#insn-00ae773c) · [`00ae7784`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76fc.md#insn-00ae7784) · [`00ae7710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae76fc.md#insn-00ae7710)

~~~diff
- 00ae76f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae76f8 ["INT_ADD", "register:40f0:8", ["const:ae76f8:8", "const:4:8"]]
- 00ae76f8 ["CALLIND", null, ["register:0:8"]]
+ 00ae773c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae773c ["INT_ADD", "register:40f0:8", ["const:ae773c:8", "const:4:8"]]
+ 00ae773c ["CALLIND", null, ["register:0:8"]]
- 00ae76f8 bytes 00013fd6
+ 00ae773c bytes 00013fd6
- 00ae7740 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae7740 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:538:8"]]
- 00ae7740 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae7784 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae7784 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:578:8"]]
+ 00ae7784 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae7740 bytes a0e21439
+ 00ae7784 bytes a0e21539
- 00ae76cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:538:8"]]
- 00ae76cc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae76cc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae7710 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:578:8"]]
+ 00ae7710 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7710 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae76cc bytes a8e25439
+ 00ae7710 bytes a8e25539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b63db96d2356e667d95f9f2b25e576a"></a>

### [`00ae7754`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7754.md) → [`00ae7798`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7798.md) _ZN8firebase4util10array_list12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae77d4",
      "incomplete_value": true,
      "site": "00ae77d4",
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
            "const:578:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7790",
      "incomplete_value": true,
      "site": "00ae7790",
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
            "const:538:8"
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
      "definition_site": "00ae7824",
      "incomplete_value": true,
      "site": "00ae7824",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae77e0",
      "incomplete_value": true,
      "site": "00ae77e0",
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
            "const:530:8"
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
      "definition_site": "00ae77b0",
      "incomplete_value": true,
      "site": "00ae77b0",
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
      "definition_site": "00ae776c",
      "incomplete_value": true,
      "site": "00ae776c",
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
      "00ae77ac",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae77b8",
      "READ",
      [
        "storage",
        "010a0538",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae77d4",
      "WRITE",
      [
        "storage",
        "010a0538",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae77ac",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae77b8",
      "READ",
      [
        "storage",
        "010a0578",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae77d4",
      "WRITE",
      [
        "storage",
        "010a0578",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7754.md#insn-00ae7790) · [`00ae77dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7754.md#insn-00ae77dc) · [`00ae77e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7754.md#insn-00ae77e0)
- 新版 [`00ae77d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7798.md#insn-00ae77d4) · [`00ae7820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7798.md#insn-00ae7820) · [`00ae7824`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7798.md#insn-00ae7824)

~~~diff
- 00ae7790 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae7790 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae7790 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:538:8"]]
- 00ae7790 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae77d4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae77d4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae77d4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:578:8"]]
+ 00ae77d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae7790 bytes bfe21439
+ 00ae77d4 bytes bfe21539
- 00ae77dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae77dc ["INT_ADD", "register:40f0:8", ["const:ae77dc:8", "const:4:8"]]
- 00ae77dc ["CALLIND", null, ["register:0:8"]]
+ 00ae7820 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae7820 ["INT_ADD", "register:40f0:8", ["const:ae7820:8", "const:4:8"]]
+ 00ae7820 ["CALLIND", null, ["register:0:8"]]
- 00ae77dc bytes 00013fd6
+ 00ae7820 bytes 00013fd6
- 00ae77e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00ae77e0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae77e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae7824 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
+ 00ae7824 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae7824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae77e0 bytes 9f9a02f9
+ 00ae7824 bytes 9fba02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-683188f2bb8fc81cefae8f8d2b454124"></a>

### [`00ae77f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae77f4.md) → [`00ae7838`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7838.md) _ZN8firebase4util10array_list14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae7878",
      "incomplete_value": true,
      "site": "00ae7878",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7834",
      "incomplete_value": true,
      "site": "00ae7834",
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
            "const:530:8"
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
      "definition_site": "00ae7854",
      "incomplete_value": true,
      "site": "00ae7854",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7810",
      "incomplete_value": true,
      "site": "00ae7810",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae785c",
      "incomplete_value": false,
      "site": "00ae7870",
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
            "const:497:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7818",
      "incomplete_value": false,
      "site": "00ae782c",
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
            "const:524:8"
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
      "00ae784c",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae785c",
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ],
    [
      "00ae7878",
      "WRITE",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae784c",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae785c",
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      "00ae7878",
      "WRITE",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae782c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae77f4.md#insn-00ae782c) · [`00ae7834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae77f4.md#insn-00ae7834) · [`00ae7808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae77f4.md#insn-00ae7808)
- 新版 [`00ae7870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7838.md#insn-00ae7870) · [`00ae7878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7838.md#insn-00ae7878) · [`00ae784c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7838.md#insn-00ae784c)

~~~diff
- 00ae782c ["INT_ADD", "register:40f0:8", ["const:ae782c:8", "const:4:8"]]
- 00ae782c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae7870 ["INT_ADD", "register:40f0:8", ["const:ae7870:8", "const:4:8"]]
+ 00ae7870 ["CALL", null, ["callee:00bde090:8"]]
- 00ae782c bytes 05da0394
+ 00ae7870 bytes 08da0394
- 00ae7834 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00ae7834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7878 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
+ 00ae7878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7834 bytes 809a02f9
+ 00ae7878 bytes 80ba02f9
- 00ae7808 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00ae7808 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae784c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
+ 00ae784c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7808 bytes 819a42f9
+ 00ae784c bytes 81ba42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f06f58d607c001c1848a1ad1fc434b61"></a>

### [`00ae7864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7864.md) → [`00ae78a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78a8.md) _ZN8firebase4util10array_list11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bddfe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfe0.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde030.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00ae78c4",
      "incomplete_value": false,
      "site": "00ae78c8",
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
      "definition_site": "00ae7880",
      "incomplete_value": false,
      "site": "00ae7884",
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
      "definition_site": "00ae78d4",
      "incomplete_value": true,
      "site": "00ae78e0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae7890",
      "incomplete_value": true,
      "site": "00ae789c",
      "value": [
        "LOAD",
        "8",
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
      "00ae78c4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae78d4",
      "DATA",
      [
        "storage",
        "010a0540",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae78c4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae78d4",
      "DATA",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7884`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7864.md#insn-00ae7884) · [`00ae7880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7864.md#insn-00ae7880) · [`00ae788c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7864.md#insn-00ae788c)
- 新版 [`00ae78c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78a8.md#insn-00ae78c8) · [`00ae78c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78a8.md#insn-00ae78c4) · [`00ae78d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78a8.md#insn-00ae78d0)

~~~diff
- 00ae7884 ["INT_ADD", "register:40f0:8", ["const:ae7884:8", "const:4:8"]]
- 00ae7884 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae78c8 ["INT_ADD", "register:40f0:8", ["const:ae78c8:8", "const:4:8"]]
+ 00ae78c8 ["CALL", null, ["callee:00bde180:8"]]
- 00ae7884 bytes 2bda0394
+ 00ae78c8 bytes 2eda0394
- 00ae7880 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae7880 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7880 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7880 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae78c4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae78c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae78c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae78c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae7880 bytes 00501791
+ 00ae78c4 bytes 001c1591
- 00ae788c ["COPY", "tmp:0:8", ["const:540:8"]]
- 00ae788c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae788c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae788c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae78d0 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00ae78d0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae78d0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae78d0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae788c bytes 08011591
+ 00ae78d0 bytes 08011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5a528470e82edfc6092e323c367c6b39"></a>

### [`00ae78a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae78a0.md) → [`00ae78e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78e4.md) _ZN8firebase4util10array_list13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae7924",
      "incomplete_value": true,
      "site": "00ae7924",
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
            "const:570:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae78e0",
      "incomplete_value": true,
      "site": "00ae78e0",
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
            "const:530:8"
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
      "definition_site": "00ae7900",
      "incomplete_value": true,
      "site": "00ae7900",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae78bc",
      "incomplete_value": true,
      "site": "00ae78bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae7908",
      "incomplete_value": false,
      "site": "00ae791c",
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
            "const:497:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae78c4",
      "incomplete_value": false,
      "site": "00ae78d8",
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
            "const:524:8"
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
      "00ae78f8",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7908",
      "PARAM",
      [
        "storage",
        "00297524",
        null,
        "string"
      ]
    ],
    [
      "00ae7924",
      "WRITE",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae78f8",
      "READ",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7908",
      "PARAM",
      [
        "storage",
        "00297497",
        null,
        "string"
      ]
    ],
    [
      "00ae7924",
      "WRITE",
      [
        "storage",
        "010a0570",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae78d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae78a0.md#insn-00ae78d8) · [`00ae78e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae78a0.md#insn-00ae78e0) · [`00ae78b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae78a0.md#insn-00ae78b4)
- 新版 [`00ae791c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78e4.md#insn-00ae791c) · [`00ae7924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78e4.md#insn-00ae7924) · [`00ae78f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae78e4.md#insn-00ae78f8)

~~~diff
- 00ae78d8 ["INT_ADD", "register:40f0:8", ["const:ae78d8:8", "const:4:8"]]
- 00ae78d8 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae791c ["INT_ADD", "register:40f0:8", ["const:ae791c:8", "const:4:8"]]
+ 00ae791c ["CALL", null, ["callee:00bde090:8"]]
- 00ae78d8 bytes dad90394
+ 00ae791c bytes ddd90394
- 00ae78e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00ae78e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7924 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
+ 00ae7924 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae78e0 bytes 809a02f9
+ 00ae7924 bytes 80ba02f9
- 00ae78b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00ae78b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae78f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
+ 00ae78f8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae78b4 bytes 819a42f9
+ 00ae78f8 bytes 81ba42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9d795a7f9d0175e813eaded7ee54e1e"></a>

### [`00ae7910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7910.md) → [`00ae7954`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7954.md) _ZN8firebase4util10array_list10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae7970",
      "incomplete_value": false,
      "site": "00ae7974",
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
      "definition_site": "00ae792c",
      "incomplete_value": false,
      "site": "00ae7930",
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
      "definition_site": "00ae7980",
      "incomplete_value": true,
      "site": "00ae798c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae793c",
      "incomplete_value": true,
      "site": "00ae7948",
      "value": [
        "LOAD",
        "8",
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
      "00ae7970",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae7980",
      "DATA",
      [
        "storage",
        "010a0558",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae7970",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae7980",
      "DATA",
      [
        "storage",
        "010a0598",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7910.md#insn-00ae7930) · [`00ae792c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7910.md#insn-00ae792c) · [`00ae7938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7910.md#insn-00ae7938)
- 新版 [`00ae7974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7954.md#insn-00ae7974) · [`00ae7970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7954.md#insn-00ae7970) · [`00ae797c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7954.md#insn-00ae797c)

~~~diff
- 00ae7930 ["INT_ADD", "register:40f0:8", ["const:ae7930:8", "const:4:8"]]
- 00ae7930 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae7974 ["INT_ADD", "register:40f0:8", ["const:ae7974:8", "const:4:8"]]
+ 00ae7974 ["CALL", null, ["callee:00bde180:8"]]
- 00ae7930 bytes 00da0394
+ 00ae7974 bytes 03da0394
- 00ae792c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae792c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae792c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae792c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae7970 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae7970 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae7970 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae7970 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae792c bytes 00fc1991
+ 00ae7970 bytes 00c81791
- 00ae7938 ["COPY", "tmp:0:8", ["const:558:8"]]
- 00ae7938 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae7938 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae7938 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae797c ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00ae797c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae797c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae797c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae7938 bytes 08611591
+ 00ae797c bytes 08611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fde755e3dfe5bcb1d29f30041c68abb9"></a>

### [`00ae794c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae794c.md) → [`00ae7990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7990.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00ae79bc",
      "incomplete_value": true,
      "site": "00ae79bc",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7978",
      "incomplete_value": true,
      "site": "00ae7978",
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
            "const:560:8"
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
      "definition_site": "00ae79a4",
      "incomplete_value": true,
      "site": "00ae79a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7960",
      "incomplete_value": true,
      "site": "00ae7960",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae7960"
      ],
      [
        "FALL_THROUGH",
        "00ae79a4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae79a4",
      "incomplete_value": true,
      "site": "00ae79bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7960",
      "incomplete_value": true,
      "site": "00ae7978",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae79a0",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae79bc",
      "WRITE",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae79a0",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae79bc",
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae794c.md#insn-00ae7978) · [`00ae795c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae794c.md#insn-00ae795c) · [`00ae7970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae794c.md#insn-00ae7970)
- 新版 [`00ae79bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7990.md#insn-00ae79bc) · [`00ae79a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7990.md#insn-00ae79a0) · [`00ae79b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7990.md#insn-00ae79b4)

~~~diff
- 00ae7978 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00ae7978 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae79bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00ae79bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7978 bytes 60b202f9
+ 00ae79bc bytes 60d202f9
- 00ae795c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00ae795c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae79a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00ae79a0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae795c bytes 68b242f9
+ 00ae79a0 bytes 68d242f9
- 00ae7970 ["INT_ADD", "register:40f0:8", ["const:ae7970:8", "const:4:8"]]
- 00ae7970 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae79b4 ["INT_ADD", "register:40f0:8", ["const:ae79b4:8", "const:4:8"]]
+ 00ae79b4 ["CALL", null, ["callee:00bde090:8"]]
- 00ae7970 bytes b4d90394
+ 00ae79b4 bytes b7d90394
~~~


<a id="compare-710a4106c40e4a5887a7dcf8dc78edb5"></a>

### [`00ae798c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae798c.md) → [`00ae79d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae79d0.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00ae79fc",
      "incomplete_value": true,
      "site": "00ae79fc",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae79b8",
      "incomplete_value": true,
      "site": "00ae79b8",
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
            "const:560:8"
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
      "definition_site": "00ae79e4",
      "incomplete_value": true,
      "site": "00ae79e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae79a0",
      "incomplete_value": true,
      "site": "00ae79a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae79a0"
      ],
      [
        "FALL_THROUGH",
        "00ae79e4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae79e4",
      "incomplete_value": true,
      "site": "00ae79fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae79a0",
      "incomplete_value": true,
      "site": "00ae79b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae79e0",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae79fc",
      "WRITE",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae79e0",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae79fc",
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae79b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae798c.md#insn-00ae79b8) · [`00ae799c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae798c.md#insn-00ae799c) · [`00ae79b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae798c.md#insn-00ae79b0)
- 新版 [`00ae79fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae79d0.md#insn-00ae79fc) · [`00ae79e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae79d0.md#insn-00ae79e0) · [`00ae79f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae79d0.md#insn-00ae79f4)

~~~diff
- 00ae79b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00ae79b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae79fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00ae79fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae79b8 bytes 60b202f9
+ 00ae79fc bytes 60d202f9
- 00ae799c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00ae799c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae79e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00ae79e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae799c bytes 68b242f9
+ 00ae79e0 bytes 68d242f9
- 00ae79b0 ["INT_ADD", "register:40f0:8", ["const:ae79b0:8", "const:4:8"]]
- 00ae79b0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae79f4 ["INT_ADD", "register:40f0:8", ["const:ae79f4:8", "const:4:8"]]
+ 00ae79f4 ["CALL", null, ["callee:00bde090:8"]]
- 00ae79b0 bytes a4d90394
+ 00ae79f4 bytes a7d90394
~~~


<a id="compare-bb8e66d27604c57d02f82ae0dd2e5b10"></a>

### [`00ae79cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae79cc.md) → [`00ae7a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a10.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae7a40",
      "incomplete_value": true,
      "site": "00ae7a40",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae79fc",
      "incomplete_value": true,
      "site": "00ae79fc",
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
            "const:560:8"
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
      "definition_site": "00ae7a24",
      "incomplete_value": true,
      "site": "00ae7a24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae79e0",
      "incomplete_value": true,
      "site": "00ae79e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae79e0"
      ],
      [
        "FALL_THROUGH",
        "00ae7a24"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7a24",
      "incomplete_value": true,
      "site": "00ae7a40",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae79e0",
      "incomplete_value": true,
      "site": "00ae79fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae7a20",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7a40",
      "WRITE",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7a20",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7a40",
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae79fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae79cc.md#insn-00ae79fc) · [`00ae79dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae79cc.md#insn-00ae79dc) · [`00ae79f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae79cc.md#insn-00ae79f4)
- 新版 [`00ae7a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a10.md#insn-00ae7a40) · [`00ae7a20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a10.md#insn-00ae7a20) · [`00ae7a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a10.md#insn-00ae7a38)

~~~diff
- 00ae79fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00ae79fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7a40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00ae7a40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae79fc bytes 60b202f9
+ 00ae7a40 bytes 60d202f9
- 00ae79dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00ae79dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7a20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00ae7a20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae79dc bytes 68b242f9
+ 00ae7a20 bytes 68d242f9
- 00ae79f4 ["INT_ADD", "register:40f0:8", ["const:ae79f4:8", "const:4:8"]]
- 00ae79f4 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae7a38 ["INT_ADD", "register:40f0:8", ["const:ae7a38:8", "const:4:8"]]
+ 00ae7a38 ["CALL", null, ["callee:00bde090:8"]]
- 00ae79f4 bytes 93d90394
+ 00ae7a38 bytes 96d90394
~~~


<a id="compare-d33212273e082d0822992e116c9053ef"></a>

### [`00ae7a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7a10.md) → [`00ae7a54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a54.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.12% / 新版 94.12%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae7a84",
      "incomplete_value": true,
      "site": "00ae7a84",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7a40",
      "incomplete_value": true,
      "site": "00ae7a40",
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
            "const:560:8"
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
      "00ae7a64",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7a84",
      "WRITE",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7a64",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7a84",
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7a10.md#insn-00ae7a40) · [`00ae7a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7a10.md#insn-00ae7a20) · [`00ae7a38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7a10.md#insn-00ae7a38)
- 新版 [`00ae7a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a54.md#insn-00ae7a84) · [`00ae7a64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a54.md#insn-00ae7a64) · [`00ae7a7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7a54.md#insn-00ae7a7c)

~~~diff
- 00ae7a40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00ae7a40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7a84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00ae7a84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7a40 bytes 60b202f9
+ 00ae7a84 bytes 60d202f9
- 00ae7a20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00ae7a20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7a64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00ae7a64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7a20 bytes 68b242f9
+ 00ae7a64 bytes 68d242f9
- 00ae7a38 ["INT_ADD", "register:40f0:8", ["const:ae7a38:8", "const:4:8"]]
- 00ae7a38 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae7a7c ["INT_ADD", "register:40f0:8", ["const:ae7a7c:8", "const:4:8"]]
+ 00ae7a7c ["CALL", null, ["callee:00bde090:8"]]
- 00ae7a38 bytes 82d90394
+ 00ae7a7c bytes 85d90394
~~~


<a id="compare-dafbc0d4fea8fd2b6ef6607db1626077"></a>

### [`00ae7a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7a60.md) → [`00ae7aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7aa4.md) _ZN8firebase4util21asset_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae7b2c",
      "incomplete_value": true,
      "site": "00ae7b2c",
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
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7ae8",
      "incomplete_value": true,
      "site": "00ae7ae8",
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
            "const:568:8"
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
      "definition_site": "00ae7ad8",
      "incomplete_value": true,
      "site": "00ae7ae4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7a94",
      "incomplete_value": true,
      "site": "00ae7aa0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:560:8"
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
      "00ae7ab8",
      "READ",
      [
        "storage",
        "010a0568",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7ad8",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7b2c",
      "WRITE",
      [
        "storage",
        "010a0568",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae7ab8",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7ad8",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7b2c",
      "WRITE",
      [
        "storage",
        "010a05a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7a60.md#insn-00ae7aa0) · [`00ae7ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7a60.md#insn-00ae7ae8) · [`00ae7a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7a60.md#insn-00ae7a74)
- 新版 [`00ae7ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7aa4.md#insn-00ae7ae4) · [`00ae7b2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7aa4.md#insn-00ae7b2c) · [`00ae7ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7aa4.md#insn-00ae7ab8)

~~~diff
- 00ae7aa0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7aa0 ["INT_ADD", "register:40f0:8", ["const:ae7aa0:8", "const:4:8"]]
- 00ae7aa0 ["CALLIND", null, ["register:0:8"]]
+ 00ae7ae4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae7ae4 ["INT_ADD", "register:40f0:8", ["const:ae7ae4:8", "const:4:8"]]
+ 00ae7ae4 ["CALLIND", null, ["register:0:8"]]
- 00ae7aa0 bytes 00013fd6
+ 00ae7ae4 bytes 00013fd6
- 00ae7ae8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae7ae8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:568:8"]]
- 00ae7ae8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae7b2c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae7b2c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5a8:8"]]
+ 00ae7b2c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae7ae8 bytes a0a21539
+ 00ae7b2c bytes a0a21639
- 00ae7a74 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:568:8"]]
- 00ae7a74 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae7a74 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae7ab8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5a8:8"]]
+ 00ae7ab8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7ab8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae7a74 bytes a8a25539
+ 00ae7ab8 bytes a8a25639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d065bbd33390ddb26a827527fae1da1a"></a>

### [`00ae7afc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7afc.md) → [`00ae7b40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7b40.md) _ZN8firebase4util21asset_file_descriptor12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae7b7c",
      "incomplete_value": true,
      "site": "00ae7b7c",
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
            "const:5a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7b38",
      "incomplete_value": true,
      "site": "00ae7b38",
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
            "const:568:8"
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
      "definition_site": "00ae7bcc",
      "incomplete_value": true,
      "site": "00ae7bcc",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7b88",
      "incomplete_value": true,
      "site": "00ae7b88",
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
            "const:560:8"
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
      "definition_site": "00ae7b58",
      "incomplete_value": true,
      "site": "00ae7b58",
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
      "definition_site": "00ae7b14",
      "incomplete_value": true,
      "site": "00ae7b14",
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
      "00ae7b54",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7b60",
      "READ",
      [
        "storage",
        "010a0568",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7b7c",
      "WRITE",
      [
        "storage",
        "010a0568",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae7b54",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7b60",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7b7c",
      "WRITE",
      [
        "storage",
        "010a05a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7b38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7afc.md#insn-00ae7b38) · [`00ae7b84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7afc.md#insn-00ae7b84) · [`00ae7b88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7afc.md#insn-00ae7b88)
- 新版 [`00ae7b7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7b40.md#insn-00ae7b7c) · [`00ae7bc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7b40.md#insn-00ae7bc8) · [`00ae7bcc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7b40.md#insn-00ae7bcc)

~~~diff
- 00ae7b38 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae7b38 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae7b38 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:568:8"]]
- 00ae7b38 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae7b7c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae7b7c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae7b7c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5a8:8"]]
+ 00ae7b7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae7b38 bytes bfa21539
+ 00ae7b7c bytes bfa21639
- 00ae7b84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7b84 ["INT_ADD", "register:40f0:8", ["const:ae7b84:8", "const:4:8"]]
- 00ae7b84 ["CALLIND", null, ["register:0:8"]]
+ 00ae7bc8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae7bc8 ["INT_ADD", "register:40f0:8", ["const:ae7bc8:8", "const:4:8"]]
+ 00ae7bc8 ["CALLIND", null, ["register:0:8"]]
- 00ae7b84 bytes 00013fd6
+ 00ae7bc8 bytes 00013fd6
- 00ae7b88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00ae7b88 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae7b88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae7bcc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
+ 00ae7bcc ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae7bcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae7b88 bytes 9fb202f9
+ 00ae7bcc bytes 9fd202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0927ada231eba8c3f76691c38dd0f66c"></a>

### [`00ae7b9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7b9c.md) → [`00ae7be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7be0.md) _ZN8firebase4util21asset_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae7c20",
      "incomplete_value": true,
      "site": "00ae7c20",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7bdc",
      "incomplete_value": true,
      "site": "00ae7bdc",
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
            "const:560:8"
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
      "definition_site": "00ae7bfc",
      "incomplete_value": true,
      "site": "00ae7bfc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7bb8",
      "incomplete_value": true,
      "site": "00ae7bb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae7bb8"
      ],
      [
        "FALL_THROUGH",
        "00ae7bfc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7bfc",
      "incomplete_value": true,
      "site": "00ae7c20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7bb8",
      "incomplete_value": true,
      "site": "00ae7bdc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae7bf4",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7c20",
      "WRITE",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7c34",
      "PARAM",
      [
        "storage",
        "00c0ff48",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ae7bf4",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7c20",
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7c34",
      "PARAM",
      [
        "storage",
        "00c0ff98",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7bdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7b9c.md#insn-00ae7bdc) · [`00ae7bb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7b9c.md#insn-00ae7bb0) · [`00ae7bd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7b9c.md#insn-00ae7bd4)
- 新版 [`00ae7c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7be0.md#insn-00ae7c20) · [`00ae7bf4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7be0.md#insn-00ae7bf4) · [`00ae7c18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7be0.md#insn-00ae7c18)

~~~diff
- 00ae7bdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00ae7bdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7c20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
+ 00ae7c20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7bdc bytes 80b202f9
+ 00ae7c20 bytes 80d202f9
- 00ae7bb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00ae7bb0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7bf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
+ 00ae7bf4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7bb0 bytes 81b242f9
+ 00ae7bf4 bytes 81d242f9
- 00ae7bd4 ["INT_ADD", "register:40f0:8", ["const:ae7bd4:8", "const:4:8"]]
- 00ae7bd4 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae7c18 ["INT_ADD", "register:40f0:8", ["const:ae7c18:8", "const:4:8"]]
+ 00ae7c18 ["CALL", null, ["callee:00bde090:8"]]
- 00ae7bd4 bytes 1bd90394
+ 00ae7c18 bytes 1ed90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63b52912084fdcc4e6743352310cf968"></a>

### [`00ae7c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7c0c.md) → [`00ae7c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c50.md) _ZN8firebase4util21asset_file_descriptor11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae7c6c",
      "incomplete_value": false,
      "site": "00ae7c70",
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
      "definition_site": "00ae7c28",
      "incomplete_value": false,
      "site": "00ae7c2c",
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
      "definition_site": "00ae7c7c",
      "incomplete_value": true,
      "site": "00ae7c88",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae7c38",
      "incomplete_value": true,
      "site": "00ae7c44",
      "value": [
        "LOAD",
        "8",
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
      "00ae7c6c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae7c7c",
      "DATA",
      [
        "storage",
        "010a0570",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae7c6c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae7c7c",
      "DATA",
      [
        "storage",
        "010a05b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7c2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7c0c.md#insn-00ae7c2c) · [`00ae7c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7c0c.md#insn-00ae7c28) · [`00ae7c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7c0c.md#insn-00ae7c34)
- 新版 [`00ae7c70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c50.md#insn-00ae7c70) · [`00ae7c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c50.md#insn-00ae7c6c) · [`00ae7c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c50.md#insn-00ae7c78)

~~~diff
- 00ae7c2c ["INT_ADD", "register:40f0:8", ["const:ae7c2c:8", "const:4:8"]]
- 00ae7c2c ["CALL", null, ["callee:00bde180:8"]]
+ 00ae7c70 ["INT_ADD", "register:40f0:8", ["const:ae7c70:8", "const:4:8"]]
+ 00ae7c70 ["CALL", null, ["callee:00bde180:8"]]
- 00ae7c2c bytes 41d90394
+ 00ae7c70 bytes 44d90394
- 00ae7c28 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae7c28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7c28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7c28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae7c6c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae7c6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae7c6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae7c6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae7c28 bytes 00501791
+ 00ae7c6c bytes 001c1591
- 00ae7c34 ["COPY", "tmp:0:8", ["const:570:8"]]
- 00ae7c34 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae7c34 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae7c34 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae7c78 ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 00ae7c78 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae7c78 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae7c78 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae7c34 bytes 08c11591
+ 00ae7c78 bytes 08c11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a3522ca93ccb0f23cc947d267e063892"></a>

### [`00ae7c48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7c48.md) → [`00ae7c8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c8c.md) _ZN8firebase4util21asset_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae7ccc",
      "incomplete_value": true,
      "site": "00ae7ccc",
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
            "const:5a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7c88",
      "incomplete_value": true,
      "site": "00ae7c88",
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
            "const:560:8"
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
      "definition_site": "00ae7ca8",
      "incomplete_value": true,
      "site": "00ae7ca8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7c64",
      "incomplete_value": true,
      "site": "00ae7c64",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae7c64"
      ],
      [
        "FALL_THROUGH",
        "00ae7ca8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7ca8",
      "incomplete_value": true,
      "site": "00ae7ccc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7c64",
      "incomplete_value": true,
      "site": "00ae7c88",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae7ca0",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7ccc",
      "WRITE",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7ce4",
      "PARAM",
      [
        "storage",
        "010a0578",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae7ca0",
      "READ",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7ccc",
      "WRITE",
      [
        "storage",
        "010a05a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7ce4",
      "PARAM",
      [
        "storage",
        "010a05b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7c48.md#insn-00ae7c88) · [`00ae7c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7c48.md#insn-00ae7c5c) · [`00ae7c80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7c48.md#insn-00ae7c80)
- 新版 [`00ae7ccc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c8c.md#insn-00ae7ccc) · [`00ae7ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c8c.md#insn-00ae7ca0) · [`00ae7cc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7c8c.md#insn-00ae7cc4)

~~~diff
- 00ae7c88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00ae7c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7ccc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
+ 00ae7ccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7c88 bytes 80b202f9
+ 00ae7ccc bytes 80d202f9
- 00ae7c5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00ae7c5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7ca0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
+ 00ae7ca0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7c5c bytes 81b242f9
+ 00ae7ca0 bytes 81d242f9
- 00ae7c80 ["INT_ADD", "register:40f0:8", ["const:ae7c80:8", "const:4:8"]]
- 00ae7c80 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae7cc4 ["INT_ADD", "register:40f0:8", ["const:ae7cc4:8", "const:4:8"]]
+ 00ae7cc4 ["CALL", null, ["callee:00bde090:8"]]
- 00ae7c80 bytes f0d80394
+ 00ae7cc4 bytes f3d80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-95e705a4560733bd86fabdb72802e1e5"></a>

### [`00ae7cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7cb8.md) → [`00ae7cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7cfc.md) _ZN8firebase4util21asset_file_descriptor10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae7d18",
      "incomplete_value": false,
      "site": "00ae7d1c",
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
      "definition_site": "00ae7cd4",
      "incomplete_value": false,
      "site": "00ae7cd8",
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
      "definition_site": "00ae7d28",
      "incomplete_value": true,
      "site": "00ae7d34",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae7ce4",
      "incomplete_value": true,
      "site": "00ae7cf0",
      "value": [
        "LOAD",
        "8",
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
      "00ae7d18",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae7d28",
      "DATA",
      [
        "storage",
        "010a0578",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae7d18",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae7d28",
      "DATA",
      [
        "storage",
        "010a05b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7cb8.md#insn-00ae7cd8) · [`00ae7cd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7cb8.md#insn-00ae7cd4) · [`00ae7ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7cb8.md#insn-00ae7ce0)
- 新版 [`00ae7d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7cfc.md#insn-00ae7d1c) · [`00ae7d18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7cfc.md#insn-00ae7d18) · [`00ae7d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7cfc.md#insn-00ae7d24)

~~~diff
- 00ae7cd8 ["INT_ADD", "register:40f0:8", ["const:ae7cd8:8", "const:4:8"]]
- 00ae7cd8 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae7d1c ["INT_ADD", "register:40f0:8", ["const:ae7d1c:8", "const:4:8"]]
+ 00ae7d1c ["CALL", null, ["callee:00bde180:8"]]
- 00ae7cd8 bytes 16d90394
+ 00ae7d1c bytes 19d90394
- 00ae7cd4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae7cd4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7cd4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7cd4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae7d18 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae7d18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae7d18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae7d18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae7cd4 bytes 00fc1991
+ 00ae7d18 bytes 00c81791
- 00ae7ce0 ["COPY", "tmp:0:8", ["const:578:8"]]
- 00ae7ce0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae7ce0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae7ce0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae7d24 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 00ae7d24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae7d24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae7d24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae7ce0 bytes 08e11591
+ 00ae7d24 bytes 08e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-363d15d17e27fbcfbae4cdb2e1a17368"></a>

### [`00ae7cf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7cf4.md) → [`00ae7d38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7d38.md) _ZN8firebase4util13boolean_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00ae7d64",
      "incomplete_value": true,
      "site": "00ae7d64",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7d20",
      "incomplete_value": true,
      "site": "00ae7d20",
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
            "const:580:8"
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
      "definition_site": "00ae7d4c",
      "incomplete_value": true,
      "site": "00ae7d4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7d08",
      "incomplete_value": true,
      "site": "00ae7d08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae7d58",
      "incomplete_value": false,
      "site": "00ae7d5c",
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
            "const:5dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7d14",
      "incomplete_value": false,
      "site": "00ae7d18",
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
            "const:669:8"
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
      "00ae7d48",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7d58",
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ],
    [
      "00ae7d64",
      "WRITE",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7d48",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7d58",
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      "00ae7d64",
      "WRITE",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7d18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7cf4.md#insn-00ae7d18) · [`00ae7d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7cf4.md#insn-00ae7d20) · [`00ae7d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7cf4.md#insn-00ae7d04)
- 新版 [`00ae7d5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7d38.md#insn-00ae7d5c) · [`00ae7d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7d38.md#insn-00ae7d64) · [`00ae7d48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7d38.md#insn-00ae7d48)

~~~diff
- 00ae7d18 ["INT_ADD", "register:40f0:8", ["const:ae7d18:8", "const:4:8"]]
- 00ae7d18 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae7d5c ["INT_ADD", "register:40f0:8", ["const:ae7d5c:8", "const:4:8"]]
+ 00ae7d5c ["CALL", null, ["callee:00bde090:8"]]
- 00ae7d18 bytes cad80394
+ 00ae7d5c bytes cdd80394
- 00ae7d20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00ae7d20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7d64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00ae7d64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7d20 bytes 60c202f9
+ 00ae7d64 bytes 60e202f9
- 00ae7d04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00ae7d04 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7d48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00ae7d48 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7d04 bytes 68c242f9
+ 00ae7d48 bytes 68e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a4a40d3baf2939decefcdab6986dcdb"></a>

### [`00ae7d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7d34.md) → [`00ae7d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7d78.md) _ZN8firebase4util13boolean_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00ae7da4",
      "incomplete_value": true,
      "site": "00ae7da4",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7d60",
      "incomplete_value": true,
      "site": "00ae7d60",
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
            "const:580:8"
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
      "definition_site": "00ae7d8c",
      "incomplete_value": true,
      "site": "00ae7d8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7d48",
      "incomplete_value": true,
      "site": "00ae7d48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae7d94",
      "incomplete_value": true,
      "site": "00ae7d9c",
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
            "const:5dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7d50",
      "incomplete_value": true,
      "site": "00ae7d58",
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
            "const:669:8"
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
      "00ae7d88",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7d94",
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ],
    [
      "00ae7da4",
      "WRITE",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7d88",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7d94",
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      "00ae7da4",
      "WRITE",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7d34.md#insn-00ae7d58) · [`00ae7d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7d34.md#insn-00ae7d60) · [`00ae7d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7d34.md#insn-00ae7d44)
- 新版 [`00ae7d9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7d78.md#insn-00ae7d9c) · [`00ae7da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7d78.md#insn-00ae7da4) · [`00ae7d88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7d78.md#insn-00ae7d88)

~~~diff
- 00ae7d58 ["INT_ADD", "register:40f0:8", ["const:ae7d58:8", "const:4:8"]]
- 00ae7d58 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae7d9c ["INT_ADD", "register:40f0:8", ["const:ae7d9c:8", "const:4:8"]]
+ 00ae7d9c ["CALL", null, ["callee:00bde090:8"]]
- 00ae7d58 bytes bad80394
+ 00ae7d9c bytes bdd80394
- 00ae7d60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00ae7d60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7da4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00ae7da4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7d60 bytes 60c202f9
+ 00ae7da4 bytes 60e202f9
- 00ae7d44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00ae7d44 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7d88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00ae7d88 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7d44 bytes 68c242f9
+ 00ae7d88 bytes 68e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6db5604fb690c1a58c61cb1981e0abcd"></a>

### [`00ae7d74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7d74.md) → [`00ae7db8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7db8.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae7de8",
      "incomplete_value": true,
      "site": "00ae7de8",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7da4",
      "incomplete_value": true,
      "site": "00ae7da4",
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
            "const:580:8"
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
      "definition_site": "00ae7dcc",
      "incomplete_value": true,
      "site": "00ae7dcc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7d88",
      "incomplete_value": true,
      "site": "00ae7d88",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae7d88"
      ],
      [
        "FALL_THROUGH",
        "00ae7dcc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae7dcc",
      "incomplete_value": true,
      "site": "00ae7de8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7d88",
      "incomplete_value": true,
      "site": "00ae7da4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae7dc8",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7dd8",
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ],
    [
      "00ae7de8",
      "WRITE",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7dc8",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7dd8",
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      "00ae7de8",
      "WRITE",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7da4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7d74.md#insn-00ae7da4) · [`00ae7d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7d74.md#insn-00ae7d84) · [`00ae7d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7d74.md#insn-00ae7d94)
- 新版 [`00ae7de8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7db8.md#insn-00ae7de8) · [`00ae7dc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7db8.md#insn-00ae7dc8) · [`00ae7dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7db8.md#insn-00ae7dd8)

~~~diff
- 00ae7da4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00ae7da4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7de8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00ae7de8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7da4 bytes 60c202f9
+ 00ae7de8 bytes 60e202f9
- 00ae7d84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00ae7d84 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7dc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00ae7dc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7d84 bytes 68c242f9
+ 00ae7dc8 bytes 68e242f9
- 00ae7d94 ["COPY", "tmp:0:8", ["const:669:8"]]
- 00ae7d94 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae7d94 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae7d94 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae7dd8 ["COPY", "tmp:0:8", ["const:5dc:8"]]
+ 00ae7dd8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae7dd8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae7dd8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae7d94 bytes 63a41991
+ 00ae7dd8 bytes 63701791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-644580e6fb6b2316cfc8f0e8b002ebf1"></a>

### [`00ae7db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7db8.md) → [`00ae7dfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7dfc.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae7e2c",
      "incomplete_value": true,
      "site": "00ae7e2c",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7de8",
      "incomplete_value": true,
      "site": "00ae7de8",
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
            "const:580:8"
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
      "definition_site": "00ae7e10",
      "incomplete_value": true,
      "site": "00ae7e10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7dcc",
      "incomplete_value": true,
      "site": "00ae7dcc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae7e18",
      "incomplete_value": false,
      "site": "00ae7e24",
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
            "const:5dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7dd4",
      "incomplete_value": false,
      "site": "00ae7de0",
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
            "const:669:8"
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
      "00ae7e0c",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7e18",
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ],
    [
      "00ae7e2c",
      "WRITE",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7e0c",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7e18",
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      "00ae7e2c",
      "WRITE",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7db8.md#insn-00ae7de0) · [`00ae7de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7db8.md#insn-00ae7de8) · [`00ae7dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7db8.md#insn-00ae7dc8)
- 新版 [`00ae7e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7dfc.md#insn-00ae7e24) · [`00ae7e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7dfc.md#insn-00ae7e2c) · [`00ae7e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7dfc.md#insn-00ae7e0c)

~~~diff
- 00ae7de0 ["INT_ADD", "register:40f0:8", ["const:ae7de0:8", "const:4:8"]]
- 00ae7de0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae7e24 ["INT_ADD", "register:40f0:8", ["const:ae7e24:8", "const:4:8"]]
+ 00ae7e24 ["CALL", null, ["callee:00bde090:8"]]
- 00ae7de0 bytes 98d80394
+ 00ae7e24 bytes 9bd80394
- 00ae7de8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00ae7de8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7e2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00ae7e2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7de8 bytes 60c202f9
+ 00ae7e2c bytes 60e202f9
- 00ae7dc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00ae7dc8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7e0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00ae7e0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7dc8 bytes 68c242f9
+ 00ae7e0c bytes 68e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-10ea3aac3a7607f2d19a0753910bb35c"></a>

### [`00ae7e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7e08.md) → [`00ae7e4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7e4c.md) _ZN8firebase4util13boolean_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.31% / 新版 92.31%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae7ed4",
      "incomplete_value": true,
      "site": "00ae7ed4",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7e90",
      "incomplete_value": true,
      "site": "00ae7e90",
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
            "const:588:8"
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
      "00ae7e60",
      "READ",
      [
        "storage",
        "010a0588",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7e80",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7ed4",
      "WRITE",
      [
        "storage",
        "010a0588",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae7e60",
      "READ",
      [
        "storage",
        "010a05c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7e80",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7ed4",
      "WRITE",
      [
        "storage",
        "010a05c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7e08.md#insn-00ae7e90) · [`00ae7e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7e08.md#insn-00ae7e1c) · [`00ae7e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7e08.md#insn-00ae7e3c)
- 新版 [`00ae7ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7e4c.md#insn-00ae7ed4) · [`00ae7e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7e4c.md#insn-00ae7e60) · [`00ae7e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7e4c.md#insn-00ae7e80)

~~~diff
- 00ae7e90 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae7e90 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:588:8"]]
- 00ae7e90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae7ed4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae7ed4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5c8:8"]]
+ 00ae7ed4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae7e90 bytes a0221639
+ 00ae7ed4 bytes a0221739
- 00ae7e1c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:588:8"]]
- 00ae7e1c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae7e1c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae7e60 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5c8:8"]]
+ 00ae7e60 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7e60 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae7e1c bytes a8225639
+ 00ae7e60 bytes a8225739
- 00ae7e3c ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:580:8"]]
- 00ae7e3c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7e80 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:5c0:8"]]
+ 00ae7e80 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7e3c bytes 21c142f9
+ 00ae7e80 bytes 21e142f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cbad8a1bfc32b544e94c9bbf9f51bf4"></a>

### [`00ae7ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7ea4.md) → [`00ae7ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ee8.md) _ZN8firebase4util13boolean_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae7f24",
      "incomplete_value": true,
      "site": "00ae7f24",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7ee0",
      "incomplete_value": true,
      "site": "00ae7ee0",
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
            "const:588:8"
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
      "definition_site": "00ae7f74",
      "incomplete_value": true,
      "site": "00ae7f74",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7f30",
      "incomplete_value": true,
      "site": "00ae7f30",
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
            "const:580:8"
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
      "definition_site": "00ae7f00",
      "incomplete_value": true,
      "site": "00ae7f00",
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
      "definition_site": "00ae7ebc",
      "incomplete_value": true,
      "site": "00ae7ebc",
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
      "00ae7efc",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7f08",
      "READ",
      [
        "storage",
        "010a0588",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7f24",
      "WRITE",
      [
        "storage",
        "010a0588",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae7efc",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7f08",
      "READ",
      [
        "storage",
        "010a05c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae7f24",
      "WRITE",
      [
        "storage",
        "010a05c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7ea4.md#insn-00ae7ee0) · [`00ae7f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7ea4.md#insn-00ae7f2c) · [`00ae7f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7ea4.md#insn-00ae7f30)
- 新版 [`00ae7f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ee8.md#insn-00ae7f24) · [`00ae7f70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ee8.md#insn-00ae7f70) · [`00ae7f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ee8.md#insn-00ae7f74)

~~~diff
- 00ae7ee0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae7ee0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae7ee0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:588:8"]]
- 00ae7ee0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae7f24 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae7f24 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae7f24 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5c8:8"]]
+ 00ae7f24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae7ee0 bytes bf221639
+ 00ae7f24 bytes bf221739
- 00ae7f2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae7f2c ["INT_ADD", "register:40f0:8", ["const:ae7f2c:8", "const:4:8"]]
- 00ae7f2c ["CALLIND", null, ["register:0:8"]]
+ 00ae7f70 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae7f70 ["INT_ADD", "register:40f0:8", ["const:ae7f70:8", "const:4:8"]]
+ 00ae7f70 ["CALLIND", null, ["register:0:8"]]
- 00ae7f2c bytes 00013fd6
+ 00ae7f70 bytes 00013fd6
- 00ae7f30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00ae7f30 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae7f30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae7f74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00ae7f74 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae7f74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae7f30 bytes 9fc202f9
+ 00ae7f74 bytes 9fe202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4875cb2c9fa6da54176439dec621f07"></a>

### [`00ae7f44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7f44.md) → [`00ae7f88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7f88.md) _ZN8firebase4util13boolean_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae7fc8",
      "incomplete_value": true,
      "site": "00ae7fc8",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7f84",
      "incomplete_value": true,
      "site": "00ae7f84",
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
            "const:580:8"
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
      "definition_site": "00ae7fa4",
      "incomplete_value": true,
      "site": "00ae7fa4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7f60",
      "incomplete_value": true,
      "site": "00ae7f60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae7fac",
      "incomplete_value": false,
      "site": "00ae7fc0",
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
            "const:5dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae7f68",
      "incomplete_value": false,
      "site": "00ae7f7c",
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
            "const:669:8"
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
      "00ae7f9c",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7fac",
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ],
    [
      "00ae7fc8",
      "WRITE",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae7f9c",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae7fac",
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      "00ae7fc8",
      "WRITE",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7f7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7f44.md#insn-00ae7f7c) · [`00ae7f84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7f44.md#insn-00ae7f84) · [`00ae7f58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7f44.md#insn-00ae7f58)
- 新版 [`00ae7fc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7f88.md#insn-00ae7fc0) · [`00ae7fc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7f88.md#insn-00ae7fc8) · [`00ae7f9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7f88.md#insn-00ae7f9c)

~~~diff
- 00ae7f7c ["INT_ADD", "register:40f0:8", ["const:ae7f7c:8", "const:4:8"]]
- 00ae7f7c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae7fc0 ["INT_ADD", "register:40f0:8", ["const:ae7fc0:8", "const:4:8"]]
+ 00ae7fc0 ["CALL", null, ["callee:00bde090:8"]]
- 00ae7f7c bytes 31d80394
+ 00ae7fc0 bytes 34d80394
- 00ae7f84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00ae7f84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae7fc8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00ae7fc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae7f84 bytes 80c202f9
+ 00ae7fc8 bytes 80e202f9
- 00ae7f58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00ae7f58 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae7f9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00ae7f9c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae7f58 bytes 81c242f9
+ 00ae7f9c bytes 81e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b3646a5daed19d2eaecb8d6ca2441696"></a>

### [`00ae7fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7fb4.md) → [`00ae7ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ff8.md) _ZN8firebase4util13boolean_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde3f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde3f0.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde440.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00ae8014",
      "incomplete_value": false,
      "site": "00ae8018",
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
      "definition_site": "00ae7fd0",
      "incomplete_value": false,
      "site": "00ae7fd4",
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
      "definition_site": "00ae8024",
      "incomplete_value": true,
      "site": "00ae8030",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae7fe0",
      "incomplete_value": true,
      "site": "00ae7fec",
      "value": [
        "LOAD",
        "8",
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
      "00ae8014",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae8024",
      "DATA",
      [
        "storage",
        "010a0590",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8014",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae8024",
      "DATA",
      [
        "storage",
        "010a05d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae7fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7fb4.md#insn-00ae7fd4) · [`00ae7fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7fb4.md#insn-00ae7fd0) · [`00ae7fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7fb4.md#insn-00ae7fdc)
- 新版 [`00ae8018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ff8.md#insn-00ae8018) · [`00ae8014`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ff8.md#insn-00ae8014) · [`00ae8020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae7/00ae7ff8.md#insn-00ae8020)

~~~diff
- 00ae7fd4 ["INT_ADD", "register:40f0:8", ["const:ae7fd4:8", "const:4:8"]]
- 00ae7fd4 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae8018 ["INT_ADD", "register:40f0:8", ["const:ae8018:8", "const:4:8"]]
+ 00ae8018 ["CALL", null, ["callee:00bde180:8"]]
- 00ae7fd4 bytes 57d80394
+ 00ae8018 bytes 5ad80394
- 00ae7fd0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae7fd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7fd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae7fd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae8014 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae8014 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae8014 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae8014 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae7fd0 bytes 00501791
+ 00ae8014 bytes 001c1591
- 00ae7fdc ["COPY", "tmp:0:8", ["const:590:8"]]
- 00ae7fdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae7fdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae7fdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae8020 ["COPY", "tmp:0:8", ["const:5d0:8"]]
+ 00ae8020 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae8020 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae8020 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae7fdc bytes 08411691
+ 00ae8020 bytes 08411791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-82ec5963bbe146b34a5f221614c7fd8c"></a>

### [`00ae7ff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7ff0.md) → [`00ae8034`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8034.md) _ZN8firebase4util13boolean_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae8074",
      "incomplete_value": true,
      "site": "00ae8074",
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
            "const:5c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8030",
      "incomplete_value": true,
      "site": "00ae8030",
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
            "const:580:8"
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
      "definition_site": "00ae8050",
      "incomplete_value": true,
      "site": "00ae8050",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae800c",
      "incomplete_value": true,
      "site": "00ae800c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae8058",
      "incomplete_value": false,
      "site": "00ae806c",
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
            "const:5dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8014",
      "incomplete_value": false,
      "site": "00ae8028",
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
            "const:669:8"
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
      "00ae8048",
      "READ",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8058",
      "PARAM",
      [
        "storage",
        "00298669",
        null,
        "string"
      ]
    ],
    [
      "00ae8074",
      "WRITE",
      [
        "storage",
        "010a0580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8048",
      "READ",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8058",
      "PARAM",
      [
        "storage",
        "002985dc",
        null,
        "string"
      ]
    ],
    [
      "00ae8074",
      "WRITE",
      [
        "storage",
        "010a05c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8028`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7ff0.md#insn-00ae8028) · [`00ae8030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7ff0.md#insn-00ae8030) · [`00ae8004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae7/00ae7ff0.md#insn-00ae8004)
- 新版 [`00ae806c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8034.md#insn-00ae806c) · [`00ae8074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8034.md#insn-00ae8074) · [`00ae8048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8034.md#insn-00ae8048)

~~~diff
- 00ae8028 ["INT_ADD", "register:40f0:8", ["const:ae8028:8", "const:4:8"]]
- 00ae8028 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae806c ["INT_ADD", "register:40f0:8", ["const:ae806c:8", "const:4:8"]]
+ 00ae806c ["CALL", null, ["callee:00bde090:8"]]
- 00ae8028 bytes 06d80394
+ 00ae806c bytes 09d80394
- 00ae8030 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00ae8030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8074 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00ae8074 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8030 bytes 80c202f9
+ 00ae8074 bytes 80e202f9
- 00ae8004 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00ae8004 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8048 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00ae8048 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8004 bytes 81c242f9
+ 00ae8048 bytes 81e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45a6b73efe7ec009bb2d7a290ddb7d51"></a>

### [`00ae8060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8060.md) → [`00ae80a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae80a4.md) _ZN8firebase4util13boolean_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae80c0",
      "incomplete_value": false,
      "site": "00ae80c4",
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
      "definition_site": "00ae807c",
      "incomplete_value": false,
      "site": "00ae8080",
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
      "definition_site": "00ae80d0",
      "incomplete_value": true,
      "site": "00ae80dc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae808c",
      "incomplete_value": true,
      "site": "00ae8098",
      "value": [
        "LOAD",
        "8",
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
      "00ae80c0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae80d0",
      "DATA",
      [
        "storage",
        "010a05a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae80c0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae80d0",
      "DATA",
      [
        "storage",
        "010a05e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8060.md#insn-00ae8080) · [`00ae807c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8060.md#insn-00ae807c) · [`00ae8088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8060.md#insn-00ae8088)
- 新版 [`00ae80c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae80a4.md#insn-00ae80c4) · [`00ae80c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae80a4.md#insn-00ae80c0) · [`00ae80cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae80a4.md#insn-00ae80cc)

~~~diff
- 00ae8080 ["INT_ADD", "register:40f0:8", ["const:ae8080:8", "const:4:8"]]
- 00ae8080 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae80c4 ["INT_ADD", "register:40f0:8", ["const:ae80c4:8", "const:4:8"]]
+ 00ae80c4 ["CALL", null, ["callee:00bde180:8"]]
- 00ae8080 bytes 2cd80394
+ 00ae80c4 bytes 2fd80394
- 00ae807c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae807c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae807c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae807c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae80c0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae80c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae80c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae80c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae807c bytes 00fc1991
+ 00ae80c0 bytes 00c81791
- 00ae8088 ["COPY", "tmp:0:8", ["const:5a0:8"]]
- 00ae8088 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae8088 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae8088 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae80cc ["COPY", "tmp:0:8", ["const:5e0:8"]]
+ 00ae80cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae80cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae80cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae8088 bytes 08811691
+ 00ae80cc bytes 08811791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28b0b693ae9ae06d861b6247283867b1"></a>

### [`00ae809c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae809c.md) → [`00ae80e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae80e0.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
      "definition_site": "00ae810c",
      "incomplete_value": true,
      "site": "00ae810c",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae80c8",
      "incomplete_value": true,
      "site": "00ae80c8",
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
            "const:5a8:8"
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
      "definition_site": "00ae8100",
      "incomplete_value": false,
      "site": "00ae8104",
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
            "const:c92:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae80bc",
      "incomplete_value": false,
      "site": "00ae80c0",
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
            "const:bf8:8"
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
      "00ae80f0",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8100",
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ],
    [
      "00ae810c",
      "WRITE",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae80f0",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8100",
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ],
    [
      "00ae810c",
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae80c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae809c.md#insn-00ae80c0) · [`00ae80c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae809c.md#insn-00ae80c8) · [`00ae80ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae809c.md#insn-00ae80ac)
- 新版 [`00ae8104`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae80e0.md#insn-00ae8104) · [`00ae810c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae80e0.md#insn-00ae810c) · [`00ae80f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae80e0.md#insn-00ae80f0)

~~~diff
- 00ae80c0 ["INT_ADD", "register:40f0:8", ["const:ae80c0:8", "const:4:8"]]
- 00ae80c0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8104 ["INT_ADD", "register:40f0:8", ["const:ae8104:8", "const:4:8"]]
+ 00ae8104 ["CALL", null, ["callee:00bde090:8"]]
- 00ae80c0 bytes e0d70394
+ 00ae8104 bytes e3d70394
- 00ae80c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00ae80c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae810c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00ae810c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae80c8 bytes 60d602f9
+ 00ae810c bytes 60f602f9
- 00ae80ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00ae80ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae80f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00ae80f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae80ac bytes 68d642f9
+ 00ae80f0 bytes 68f642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-63f577e0cf3e46b99934b4d109165114"></a>

### [`00ae80dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae80dc.md) → [`00ae8120`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8120.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00ae814c",
      "incomplete_value": true,
      "site": "00ae814c",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8108",
      "incomplete_value": true,
      "site": "00ae8108",
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
            "const:5a8:8"
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
      "definition_site": "00ae8134",
      "incomplete_value": true,
      "site": "00ae8134",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae80f0",
      "incomplete_value": true,
      "site": "00ae80f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae813c",
      "incomplete_value": false,
      "site": "00ae8144",
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
            "const:c92:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae80f8",
      "incomplete_value": false,
      "site": "00ae8100",
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
            "const:bf8:8"
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
      "00ae8130",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae813c",
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ],
    [
      "00ae814c",
      "WRITE",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8130",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae813c",
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ],
    [
      "00ae814c",
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae80dc.md#insn-00ae8100) · [`00ae8108`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae80dc.md#insn-00ae8108) · [`00ae80ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae80dc.md#insn-00ae80ec)
- 新版 [`00ae8144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8120.md#insn-00ae8144) · [`00ae814c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8120.md#insn-00ae814c) · [`00ae8130`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8120.md#insn-00ae8130)

~~~diff
- 00ae8100 ["INT_ADD", "register:40f0:8", ["const:ae8100:8", "const:4:8"]]
- 00ae8100 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8144 ["INT_ADD", "register:40f0:8", ["const:ae8144:8", "const:4:8"]]
+ 00ae8144 ["CALL", null, ["callee:00bde090:8"]]
- 00ae8100 bytes d0d70394
+ 00ae8144 bytes d3d70394
- 00ae8108 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00ae8108 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae814c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00ae814c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8108 bytes 60d602f9
+ 00ae814c bytes 60f602f9
- 00ae80ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00ae80ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8130 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00ae8130 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae80ec bytes 68d642f9
+ 00ae8130 bytes 68f642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4a4fd35cbc153818f2ef90d3ff9df13"></a>

### [`00ae811c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae811c.md) → [`00ae8160`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8160.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae8190",
      "incomplete_value": true,
      "site": "00ae8190",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae814c",
      "incomplete_value": true,
      "site": "00ae814c",
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
            "const:5a8:8"
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
      "definition_site": "00ae8174",
      "incomplete_value": true,
      "site": "00ae8174",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8130",
      "incomplete_value": true,
      "site": "00ae8130",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae8180",
      "incomplete_value": false,
      "site": "00ae8188",
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
            "const:c92:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae813c",
      "incomplete_value": false,
      "site": "00ae8144",
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
            "const:bf8:8"
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
      "00ae8170",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8180",
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ],
    [
      "00ae8190",
      "WRITE",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8170",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8180",
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ],
    [
      "00ae8190",
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae811c.md#insn-00ae8144) · [`00ae814c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae811c.md#insn-00ae814c) · [`00ae812c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae811c.md#insn-00ae812c)
- 新版 [`00ae8188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8160.md#insn-00ae8188) · [`00ae8190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8160.md#insn-00ae8190) · [`00ae8170`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8160.md#insn-00ae8170)

~~~diff
- 00ae8144 ["INT_ADD", "register:40f0:8", ["const:ae8144:8", "const:4:8"]]
- 00ae8144 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8188 ["INT_ADD", "register:40f0:8", ["const:ae8188:8", "const:4:8"]]
+ 00ae8188 ["CALL", null, ["callee:00bde090:8"]]
- 00ae8144 bytes bfd70394
+ 00ae8188 bytes c2d70394
- 00ae814c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00ae814c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8190 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00ae8190 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae814c bytes 60d602f9
+ 00ae8190 bytes 60f602f9
- 00ae812c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00ae812c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8170 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00ae8170 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae812c bytes 68d642f9
+ 00ae8170 bytes 68f642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-351bda3932f2bff969752606427d849d"></a>

### [`00ae8160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8160.md) → [`00ae81a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81a4.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae81d4",
      "incomplete_value": true,
      "site": "00ae81d4",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8190",
      "incomplete_value": true,
      "site": "00ae8190",
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
            "const:5a8:8"
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
      "definition_site": "00ae81b8",
      "incomplete_value": true,
      "site": "00ae81b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8174",
      "incomplete_value": true,
      "site": "00ae8174",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
        "00ae8174"
      ],
      [
        "FALL_THROUGH",
        "00ae81b8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae81b8",
      "incomplete_value": true,
      "site": "00ae81d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8174",
      "incomplete_value": true,
      "site": "00ae8190",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae81b4",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae81c0",
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ],
    [
      "00ae81d4",
      "WRITE",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae81b4",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae81c0",
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ],
    [
      "00ae81d4",
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8160.md#insn-00ae8190) · [`00ae8170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8160.md#insn-00ae8170) · [`00ae817c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8160.md#insn-00ae817c)
- 新版 [`00ae81d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81a4.md#insn-00ae81d4) · [`00ae81b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81a4.md#insn-00ae81b4) · [`00ae81c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81a4.md#insn-00ae81c0)

~~~diff
- 00ae8190 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00ae8190 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae81d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00ae81d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8190 bytes 60d602f9
+ 00ae81d4 bytes 60f602f9
- 00ae8170 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a8:8"]]
- 00ae8170 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae81b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5e8:8"]]
+ 00ae81b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8170 bytes 68d642f9
+ 00ae81b4 bytes 68f642f9
- 00ae817c ["COPY", "tmp:0:8", ["const:bf8:8"]]
- 00ae817c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae817c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae817c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae81c0 ["COPY", "tmp:0:8", ["const:c92:8"]]
+ 00ae81c0 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae81c0 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae81c0 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae817c bytes 63e02f91
+ 00ae81c0 bytes 63483291
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ecd633c903755ed215da2760cc6ea40e"></a>

### [`00ae81b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae81b0.md) → [`00ae81f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81f4.md) _ZN8firebase4util6bundle15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae827c",
      "incomplete_value": true,
      "site": "00ae827c",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8238",
      "incomplete_value": true,
      "site": "00ae8238",
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
            "const:5b0:8"
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
      "definition_site": "00ae8228",
      "incomplete_value": true,
      "site": "00ae8234",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae81e4",
      "incomplete_value": true,
      "site": "00ae81f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5a8:8"
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
      "00ae8208",
      "READ",
      [
        "storage",
        "010a05b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae8228",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae827c",
      "WRITE",
      [
        "storage",
        "010a05b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae8208",
      "READ",
      [
        "storage",
        "010a05f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae8228",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae827c",
      "WRITE",
      [
        "storage",
        "010a05f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae81f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae81b0.md#insn-00ae81f0) · [`00ae8238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae81b0.md#insn-00ae8238) · [`00ae81c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae81b0.md#insn-00ae81c4)
- 新版 [`00ae8234`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81f4.md#insn-00ae8234) · [`00ae827c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81f4.md#insn-00ae827c) · [`00ae8208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae81f4.md#insn-00ae8208)

~~~diff
- 00ae81f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae81f0 ["INT_ADD", "register:40f0:8", ["const:ae81f0:8", "const:4:8"]]
- 00ae81f0 ["CALLIND", null, ["register:0:8"]]
+ 00ae8234 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae8234 ["INT_ADD", "register:40f0:8", ["const:ae8234:8", "const:4:8"]]
+ 00ae8234 ["CALLIND", null, ["register:0:8"]]
- 00ae81f0 bytes 00013fd6
+ 00ae8234 bytes 00013fd6
- 00ae8238 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae8238 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5b0:8"]]
- 00ae8238 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae827c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae827c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5f0:8"]]
+ 00ae827c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae8238 bytes a0c21639
+ 00ae827c bytes a0c21739
- 00ae81c4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5b0:8"]]
- 00ae81c4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae81c4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae8208 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5f0:8"]]
+ 00ae8208 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8208 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae81c4 bytes a8c25639
+ 00ae8208 bytes a8c25739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a3d5759802a7a81ec0f4b38f72f84a5"></a>

### [`00ae824c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae824c.md) → [`00ae8290`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8290.md) _ZN8firebase4util6bundle12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae82cc",
      "incomplete_value": true,
      "site": "00ae82cc",
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
            "const:5f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8288",
      "incomplete_value": true,
      "site": "00ae8288",
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
            "const:5b0:8"
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
      "definition_site": "00ae831c",
      "incomplete_value": true,
      "site": "00ae831c",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae82d8",
      "incomplete_value": true,
      "site": "00ae82d8",
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
            "const:5a8:8"
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
      "definition_site": "00ae82a8",
      "incomplete_value": true,
      "site": "00ae82a8",
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
      "definition_site": "00ae8264",
      "incomplete_value": true,
      "site": "00ae8264",
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
      "00ae82a4",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae82b0",
      "READ",
      [
        "storage",
        "010a05b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae82cc",
      "WRITE",
      [
        "storage",
        "010a05b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae82a4",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae82b0",
      "READ",
      [
        "storage",
        "010a05f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae82cc",
      "WRITE",
      [
        "storage",
        "010a05f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae824c.md#insn-00ae8288) · [`00ae82d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae824c.md#insn-00ae82d4) · [`00ae82d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae824c.md#insn-00ae82d8)
- 新版 [`00ae82cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8290.md#insn-00ae82cc) · [`00ae8318`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8290.md#insn-00ae8318) · [`00ae831c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8290.md#insn-00ae831c)

~~~diff
- 00ae8288 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae8288 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae8288 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5b0:8"]]
- 00ae8288 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae82cc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae82cc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae82cc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5f0:8"]]
+ 00ae82cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae8288 bytes bfc21639
+ 00ae82cc bytes bfc21739
- 00ae82d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae82d4 ["INT_ADD", "register:40f0:8", ["const:ae82d4:8", "const:4:8"]]
- 00ae82d4 ["CALLIND", null, ["register:0:8"]]
+ 00ae8318 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae8318 ["INT_ADD", "register:40f0:8", ["const:ae8318:8", "const:4:8"]]
+ 00ae8318 ["CALLIND", null, ["register:0:8"]]
- 00ae82d4 bytes 00013fd6
+ 00ae8318 bytes 00013fd6
- 00ae82d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00ae82d8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae82d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae831c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
+ 00ae831c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae831c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae82d8 bytes 9fd602f9
+ 00ae831c bytes 9ff602f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d615ef580f2d7f47e811fc5bd748dddf"></a>

### [`00ae82ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae82ec.md) → [`00ae8330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8330.md) _ZN8firebase4util6bundle14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae8370",
      "incomplete_value": true,
      "site": "00ae8370",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae832c",
      "incomplete_value": true,
      "site": "00ae832c",
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
            "const:5a8:8"
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
      "definition_site": "00ae834c",
      "incomplete_value": true,
      "site": "00ae834c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8308",
      "incomplete_value": true,
      "site": "00ae8308",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae8354",
      "incomplete_value": false,
      "site": "00ae8368",
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
            "const:c92:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8310",
      "incomplete_value": false,
      "site": "00ae8324",
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
            "const:bf8:8"
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
      "00ae8344",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8354",
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ],
    [
      "00ae8370",
      "WRITE",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8344",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8354",
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ],
    [
      "00ae8370",
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae82ec.md#insn-00ae8324) · [`00ae832c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae82ec.md#insn-00ae832c) · [`00ae8300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae82ec.md#insn-00ae8300)
- 新版 [`00ae8368`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8330.md#insn-00ae8368) · [`00ae8370`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8330.md#insn-00ae8370) · [`00ae8344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8330.md#insn-00ae8344)

~~~diff
- 00ae8324 ["INT_ADD", "register:40f0:8", ["const:ae8324:8", "const:4:8"]]
- 00ae8324 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8368 ["INT_ADD", "register:40f0:8", ["const:ae8368:8", "const:4:8"]]
+ 00ae8368 ["CALL", null, ["callee:00bde090:8"]]
- 00ae8324 bytes 47d70394
+ 00ae8368 bytes 4ad70394
- 00ae832c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00ae832c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae8370 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
+ 00ae8370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae832c bytes 80d602f9
+ 00ae8370 bytes 80f602f9
- 00ae8300 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00ae8300 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8344 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
+ 00ae8344 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8300 bytes 81d642f9
+ 00ae8344 bytes 81f642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1595a8671a677d8d27df54334a3be818"></a>

### [`00ae835c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae835c.md) → [`00ae83a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83a0.md) _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

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
      "definition_site": "00ae83bc",
      "incomplete_value": false,
      "site": "00ae83c0",
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
      "definition_site": "00ae8378",
      "incomplete_value": false,
      "site": "00ae837c",
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
      "00ae83bc",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae83cc",
      "DATA",
      [
        "storage",
        "010a05b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae83bc",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae83cc",
      "DATA",
      [
        "storage",
        "010a05f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae837c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae835c.md#insn-00ae837c) · [`00ae8378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae835c.md#insn-00ae8378) · [`00ae8384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae835c.md#insn-00ae8384)
- 新版 [`00ae83c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83a0.md#insn-00ae83c0) · [`00ae83bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83a0.md#insn-00ae83bc) · [`00ae83c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83a0.md#insn-00ae83c8)

~~~diff
- 00ae837c ["INT_ADD", "register:40f0:8", ["const:ae837c:8", "const:4:8"]]
- 00ae837c ["CALL", null, ["callee:00bde180:8"]]
+ 00ae83c0 ["INT_ADD", "register:40f0:8", ["const:ae83c0:8", "const:4:8"]]
+ 00ae83c0 ["CALL", null, ["callee:00bde180:8"]]
- 00ae837c bytes 6dd70394
+ 00ae83c0 bytes 70d70394
- 00ae8378 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae8378 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae8378 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae8378 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae83bc ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae83bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae83bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae83bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae8378 bytes 00501791
+ 00ae83bc bytes 001c1591
- 00ae8384 ["COPY", "tmp:0:8", ["const:5b8:8"]]
- 00ae8384 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae8384 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae8384 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae83c8 ["COPY", "tmp:0:8", ["const:5f8:8"]]
+ 00ae83c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae83c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae83c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae8384 bytes 08e11691
+ 00ae83c8 bytes 08e11791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5eb247a8d6c2b390b254db34ec109248"></a>

### [`00ae8398`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8398.md) → [`00ae83dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83dc.md) _ZN8firebase4util6bundle13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae841c",
      "incomplete_value": true,
      "site": "00ae841c",
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
            "const:5e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae83d8",
      "incomplete_value": true,
      "site": "00ae83d8",
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
            "const:5a8:8"
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
      "definition_site": "00ae83f8",
      "incomplete_value": true,
      "site": "00ae83f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae83b4",
      "incomplete_value": true,
      "site": "00ae83b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae8400",
      "incomplete_value": false,
      "site": "00ae8414",
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
            "const:c92:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae83bc",
      "incomplete_value": false,
      "site": "00ae83d0",
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
            "const:bf8:8"
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
      "00ae83f0",
      "READ",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8400",
      "PARAM",
      [
        "storage",
        "002a8bf8",
        null,
        "string"
      ]
    ],
    [
      "00ae841c",
      "WRITE",
      [
        "storage",
        "010a05a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae83f0",
      "READ",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae8400",
      "PARAM",
      [
        "storage",
        "002a8c92",
        null,
        "string"
      ]
    ],
    [
      "00ae841c",
      "WRITE",
      [
        "storage",
        "010a05e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae83d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8398.md#insn-00ae83d0) · [`00ae83d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8398.md#insn-00ae83d8) · [`00ae83ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8398.md#insn-00ae83ac)
- 新版 [`00ae8414`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83dc.md#insn-00ae8414) · [`00ae841c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83dc.md#insn-00ae841c) · [`00ae83f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae83dc.md#insn-00ae83f0)

~~~diff
- 00ae83d0 ["INT_ADD", "register:40f0:8", ["const:ae83d0:8", "const:4:8"]]
- 00ae83d0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae8414 ["INT_ADD", "register:40f0:8", ["const:ae8414:8", "const:4:8"]]
+ 00ae8414 ["CALL", null, ["callee:00bde090:8"]]
- 00ae83d0 bytes 1cd70394
+ 00ae8414 bytes 1fd70394
- 00ae83d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00ae83d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae841c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
+ 00ae841c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae83d8 bytes 80d602f9
+ 00ae841c bytes 80f602f9
- 00ae83ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a8:8"]]
- 00ae83ac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae83f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5e8:8"]]
+ 00ae83f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae83ac bytes 81d642f9
+ 00ae83f0 bytes 81f642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-91086d98c2cd9ef28037f051f9e7dd68"></a>

### [`00ae8408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8408.md) → [`00ae844c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae844c.md) _ZN8firebase4util6bundle10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae8468",
      "incomplete_value": false,
      "site": "00ae846c",
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
      "definition_site": "00ae8424",
      "incomplete_value": false,
      "site": "00ae8428",
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
      "definition_site": "00ae8478",
      "incomplete_value": true,
      "site": "00ae8484",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae8434",
      "incomplete_value": true,
      "site": "00ae8440",
      "value": [
        "LOAD",
        "8",
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
      "00ae8468",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae8478",
      "DATA",
      [
        "storage",
        "010a0600",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae8468",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae8478",
      "DATA",
      [
        "storage",
        "010a0640",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8408.md#insn-00ae8428) · [`00ae8424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8408.md#insn-00ae8424) · [`00ae8430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8408.md#insn-00ae8430)
- 新版 [`00ae846c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae844c.md#insn-00ae846c) · [`00ae8468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae844c.md#insn-00ae8468) · [`00ae8474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae844c.md#insn-00ae8474)

~~~diff
- 00ae8428 ["INT_ADD", "register:40f0:8", ["const:ae8428:8", "const:4:8"]]
- 00ae8428 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae846c ["INT_ADD", "register:40f0:8", ["const:ae846c:8", "const:4:8"]]
+ 00ae846c ["CALL", null, ["callee:00bde180:8"]]
- 00ae8428 bytes 42d70394
+ 00ae846c bytes 45d70394
- 00ae8424 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae8424 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae8424 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae8424 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae8468 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae8468 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae8468 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae8468 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae8424 bytes 00fc1991
+ 00ae8468 bytes 00c81791
- 00ae8430 ["COPY", "tmp:0:8", ["const:600:8"]]
- 00ae8430 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae8430 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae8430 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae8474 ["COPY", "tmp:0:8", ["const:640:8"]]
+ 00ae8474 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae8474 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae8474 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae8430 bytes 08011891
+ 00ae8474 bytes 08011991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-109c52a2a4102e8f70ba4ac16186a408"></a>

### [`00ae8444`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8444.md) → [`00ae8488`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8488.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00ae84b4",
      "incomplete_value": true,
      "site": "00ae84b4",
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
            "const:648:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8470",
      "incomplete_value": true,
      "site": "00ae8470",
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
            "const:608:8"
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
      "definition_site": "00ae849c",
      "incomplete_value": true,
      "site": "00ae849c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8458",
      "incomplete_value": true,
      "site": "00ae8458",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "definition_site": "00ae84a8",
      "incomplete_value": false,
      "site": "00ae84ac",
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
            "const:459:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae8464",
      "incomplete_value": false,
      "site": "00ae8468",
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
            "const:4e6:8"
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
      "00ae8498",
      "READ",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae84a8",
      "PARAM",
      [
        "storage",
        "002964e6",
        null,
        "string"
      ]
    ],
    [
      "00ae84b4",
      "WRITE",
      [
        "storage",
        "010a0608",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae8498",
      "READ",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae84a8",
      "PARAM",
      [
        "storage",
        "00296459",
        null,
        "string"
      ]
    ],
    [
      "00ae84b4",
      "WRITE",
      [
        "storage",
        "010a0648",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae8468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8444.md#insn-00ae8468) · [`00ae8470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8444.md#insn-00ae8470) · [`00ae8454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae8/00ae8444.md#insn-00ae8454)
- 新版 [`00ae84ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8488.md#insn-00ae84ac) · [`00ae84b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8488.md#insn-00ae84b4) · [`00ae8498`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8488.md#insn-00ae8498)

~~~diff
- 00ae8468 ["INT_ADD", "register:40f0:8", ["const:ae8468:8", "const:4:8"]]
- 00ae8468 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae84ac ["INT_ADD", "register:40f0:8", ["const:ae84ac:8", "const:4:8"]]
+ 00ae84ac ["CALL", null, ["callee:00bde090:8"]]
- 00ae8468 bytes f6d60394
+ 00ae84ac bytes f9d60394
- 00ae8470 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00ae8470 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae84b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
+ 00ae84b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae8470 bytes 600603f9
+ 00ae84b4 bytes 602603f9
- 00ae8454 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:608:8"]]
- 00ae8454 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae8498 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:648:8"]]
+ 00ae8498 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae8454 bytes 680643f9
+ 00ae8498 bytes 682643f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

