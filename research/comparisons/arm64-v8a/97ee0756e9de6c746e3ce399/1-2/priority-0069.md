# v15.7.3 → v15.7.4 · 最優先の変更候補 (69)

[一覧の目次](README.md)

<a id="compare-51de8550c7081b92018b62b4b2e9c54d"></a>

### [`00b53654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53654.md) → [`00b53698`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53698.md) _ZN8firebase13remote_config8internal11config_info11GetMethodIdENS2_6MethodE

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
      "definition_site": "00b536b4",
      "incomplete_value": false,
      "site": "00b536b8",
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
      "definition_site": "00b53670",
      "incomplete_value": false,
      "site": "00b53674",
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
      "definition_site": "00b536c4",
      "incomplete_value": true,
      "site": "00b536d0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b53680",
      "incomplete_value": true,
      "site": "00b5368c",
      "value": [
        "LOAD",
        "8",
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
      "00b536b4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b536c4",
      "DATA",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b536b4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b536c4",
      "DATA",
      [
        "storage",
        "010a12b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53654.md#insn-00b53674) · [`00b53670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53654.md#insn-00b53670) · [`00b5367c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53654.md#insn-00b5367c)
- 新版 `00b536b8`（命令位置の公開資料なし） · `00b536b4`（命令位置の公開資料なし） · `00b536c0`（命令位置の公開資料なし）

~~~diff
- 00b53674 ["INT_ADD", "register:40f0:8", ["const:b53674:8", "const:4:8"]]
- 00b53674 ["CALL", null, ["callee:00bde180:8"]]
+ 00b536b8 ["INT_ADD", "register:40f0:8", ["const:b536b8:8", "const:4:8"]]
+ 00b536b8 ["CALL", null, ["callee:00bde180:8"]]
- 00b53674 bytes af2a0294
+ 00b536b8 bytes b22a0294
- 00b53670 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b53670 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b53670 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b53670 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b536b4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b536b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b536b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b536b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b53670 bytes 00501791
+ 00b536b4 bytes 001c1591
- 00b5367c ["COPY", "tmp:0:8", ["const:270:8"]]
- 00b5367c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5367c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5367c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b536c0 ["COPY", "tmp:0:8", ["const:2b0:8"]]
+ 00b536c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b536c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b536c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5367c bytes 08c10991
+ 00b536c0 bytes 08c10a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-42b884a2f822013248298d92fdfa83a2"></a>

### [`00b53690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53690.md) → [`00b536d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b536d4.md) _ZN8firebase13remote_config8internal11config_info13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b53714",
      "incomplete_value": true,
      "site": "00b53714",
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
      "definition_site": "00b536d0",
      "incomplete_value": true,
      "site": "00b536d0",
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
      "definition_site": "00b536f0",
      "incomplete_value": true,
      "site": "00b536f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b536ac",
      "incomplete_value": true,
      "site": "00b536ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b536f8",
      "incomplete_value": false,
      "site": "00b5370c",
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
      "definition_site": "00b536b4",
      "incomplete_value": false,
      "site": "00b536c8",
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
      "00b536e8",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b536f8",
      "PARAM",
      [
        "storage",
        "0029775e",
        null,
        "string"
      ]
    ],
    [
      "00b53714",
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
      "00b536e8",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b536f8",
      "PARAM",
      [
        "storage",
        "002976d1",
        null,
        "string"
      ]
    ],
    [
      "00b53714",
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

- 旧版 [`00b536c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53690.md#insn-00b536c8) · [`00b536d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53690.md#insn-00b536d0) · [`00b536a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53690.md#insn-00b536a4)
- 新版 `00b5370c`（命令位置の公開資料なし） · `00b53714`（命令位置の公開資料なし） · `00b536e8`（命令位置の公開資料なし）

~~~diff
- 00b536c8 ["INT_ADD", "register:40f0:8", ["const:b536c8:8", "const:4:8"]]
- 00b536c8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5370c ["INT_ADD", "register:40f0:8", ["const:b5370c:8", "const:4:8"]]
+ 00b5370c ["CALL", null, ["callee:00bde090:8"]]
- 00b536c8 bytes 5e2a0294
+ 00b5370c bytes 612a0294
- 00b536d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:260:8"]]
- 00b536d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53714 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2a0:8"]]
+ 00b53714 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b536d0 bytes 803201f9
+ 00b53714 bytes 805201f9
- 00b536a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:260:8"]]
- 00b536a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b536e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2a0:8"]]
+ 00b536e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b536a4 bytes 813241f9
+ 00b536e8 bytes 815241f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c0164a2d2cc195fb09e5f8c84ab1c28"></a>

### [`00b53700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53700.md) → [`00b53744`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53744.md) _ZN8firebase13remote_config8internal11config_info10GetFieldIdENS2_5FieldE

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
      "definition_site": "00b53760",
      "incomplete_value": false,
      "site": "00b53764",
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
      "definition_site": "00b5371c",
      "incomplete_value": false,
      "site": "00b53720",
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
      "definition_site": "00b53770",
      "incomplete_value": true,
      "site": "00b5377c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5372c",
      "incomplete_value": true,
      "site": "00b53738",
      "value": [
        "LOAD",
        "8",
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
      "00b53760",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b53770",
      "DATA",
      [
        "storage",
        "010a1288",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b53760",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b53770",
      "DATA",
      [
        "storage",
        "010a12c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53700.md#insn-00b53720) · [`00b5371c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53700.md#insn-00b5371c) · [`00b53728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53700.md#insn-00b53728)
- 新版 `00b53764`（命令位置の公開資料なし） · `00b53760`（命令位置の公開資料なし） · `00b5376c`（命令位置の公開資料なし）

~~~diff
- 00b53720 ["INT_ADD", "register:40f0:8", ["const:b53720:8", "const:4:8"]]
- 00b53720 ["CALL", null, ["callee:00bde180:8"]]
+ 00b53764 ["INT_ADD", "register:40f0:8", ["const:b53764:8", "const:4:8"]]
+ 00b53764 ["CALL", null, ["callee:00bde180:8"]]
- 00b53720 bytes 842a0294
+ 00b53764 bytes 872a0294
- 00b5371c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b5371c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5371c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5371c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b53760 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b53760 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53760 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53760 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5371c bytes 00fc1991
+ 00b53760 bytes 00c81791
- 00b53728 ["COPY", "tmp:0:8", ["const:288:8"]]
- 00b53728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b53728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b53728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5376c ["COPY", "tmp:0:8", ["const:2c8:8"]]
+ 00b5376c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5376c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5376c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b53728 bytes 08210a91
+ 00b5376c bytes 08210b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24a4b9c700d213ac36564ab5518ffbe6"></a>

### [`00b5373c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5373c.md) → [`00b53780`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53780.md) _ZN8firebase13remote_config8internal15config_settings19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFile

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
      "definition_site": "00b537ac",
      "incomplete_value": true,
      "site": "00b537ac",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53768",
      "incomplete_value": true,
      "site": "00b53768",
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
            "const:290:8"
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
      "definition_site": "00b53794",
      "incomplete_value": true,
      "site": "00b53794",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53750",
      "incomplete_value": true,
      "site": "00b53750",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b537a0",
      "incomplete_value": false,
      "site": "00b537a4",
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
            "const:f3e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5375c",
      "incomplete_value": false,
      "site": "00b53760",
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
            "const:ea4:8"
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
      "00b53790",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b537a0",
      "PARAM",
      [
        "storage",
        "002a7ea4",
        null,
        "string"
      ]
    ],
    [
      "00b537ac",
      "WRITE",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53790",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b537a0",
      "PARAM",
      [
        "storage",
        "002a7f3e",
        null,
        "string"
      ]
    ],
    [
      "00b537ac",
      "WRITE",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53760`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5373c.md#insn-00b53760) · [`00b53768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5373c.md#insn-00b53768) · [`00b5374c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5373c.md#insn-00b5374c)
- 新版 `00b537a4`（命令位置の公開資料なし） · `00b537ac`（命令位置の公開資料なし） · `00b53790`（命令位置の公開資料なし）

~~~diff
- 00b53760 ["INT_ADD", "register:40f0:8", ["const:b53760:8", "const:4:8"]]
- 00b53760 ["CALL", null, ["callee:00bde090:8"]]
+ 00b537a4 ["INT_ADD", "register:40f0:8", ["const:b537a4:8", "const:4:8"]]
+ 00b537a4 ["CALL", null, ["callee:00bde090:8"]]
- 00b53760 bytes 382a0294
+ 00b537a4 bytes 3b2a0294
- 00b53768 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00b53768 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b537ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2d0:8"]]
+ 00b537ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53768 bytes 604a01f9
+ 00b537ac bytes 606a01f9
- 00b5374c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00b5374c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53790 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2d0:8"]]
+ 00b53790 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5374c bytes 684a41f9
+ 00b53790 bytes 686a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba949af322ea93c0ca9edbee2cea132e"></a>

### [`00b5377c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5377c.md) → [`00b537c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b537c0.md) _ZN8firebase13remote_config8internal15config_settings19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFile

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
      "definition_site": "00b537ec",
      "incomplete_value": true,
      "site": "00b537ec",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b537a8",
      "incomplete_value": true,
      "site": "00b537a8",
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
            "const:290:8"
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
      "definition_site": "00b537d4",
      "incomplete_value": true,
      "site": "00b537d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53790",
      "incomplete_value": true,
      "site": "00b53790",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b537dc",
      "incomplete_value": false,
      "site": "00b537e4",
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
            "const:f3e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53798",
      "incomplete_value": false,
      "site": "00b537a0",
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
            "const:ea4:8"
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
      "00b537d0",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b537dc",
      "PARAM",
      [
        "storage",
        "002a7ea4",
        null,
        "string"
      ]
    ],
    [
      "00b537ec",
      "WRITE",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b537d0",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b537dc",
      "PARAM",
      [
        "storage",
        "002a7f3e",
        null,
        "string"
      ]
    ],
    [
      "00b537ec",
      "WRITE",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b537a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5377c.md#insn-00b537a0) · [`00b537a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5377c.md#insn-00b537a8) · [`00b5378c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5377c.md#insn-00b5378c)
- 新版 `00b537e4`（命令位置の公開資料なし） · `00b537ec`（命令位置の公開資料なし） · `00b537d0`（命令位置の公開資料なし）

~~~diff
- 00b537a0 ["INT_ADD", "register:40f0:8", ["const:b537a0:8", "const:4:8"]]
- 00b537a0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b537e4 ["INT_ADD", "register:40f0:8", ["const:b537e4:8", "const:4:8"]]
+ 00b537e4 ["CALL", null, ["callee:00bde090:8"]]
- 00b537a0 bytes 282a0294
+ 00b537e4 bytes 2b2a0294
- 00b537a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00b537a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b537ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2d0:8"]]
+ 00b537ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b537a8 bytes 604a01f9
+ 00b537ec bytes 606a01f9
- 00b5378c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00b5378c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b537d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2d0:8"]]
+ 00b537d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5378c bytes 684a41f9
+ 00b537d0 bytes 686a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-765c7fa43d5a3e9f77f7ad01e9ebbfaa"></a>

### [`00b537bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b537bc.md) → [`00b53800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53800.md) _ZN8firebase13remote_config8internal15config_settings10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b53830",
      "incomplete_value": true,
      "site": "00b53830",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b537ec",
      "incomplete_value": true,
      "site": "00b537ec",
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
            "const:290:8"
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
      "definition_site": "00b53820",
      "incomplete_value": true,
      "site": "00b53828",
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
            "const:f3e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b537dc",
      "incomplete_value": true,
      "site": "00b537e4",
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
            "const:ea4:8"
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
      "00b53810",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53820",
      "PARAM",
      [
        "storage",
        "002a7ea4",
        null,
        "string"
      ]
    ],
    [
      "00b53830",
      "WRITE",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53810",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53820",
      "PARAM",
      [
        "storage",
        "002a7f3e",
        null,
        "string"
      ]
    ],
    [
      "00b53830",
      "WRITE",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b537e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b537bc.md#insn-00b537e4) · [`00b537ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b537bc.md#insn-00b537ec) · [`00b537cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b537bc.md#insn-00b537cc)
- 新版 `00b53828`（命令位置の公開資料なし） · `00b53830`（命令位置の公開資料なし） · `00b53810`（命令位置の公開資料なし）

~~~diff
- 00b537e4 ["INT_ADD", "register:40f0:8", ["const:b537e4:8", "const:4:8"]]
- 00b537e4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53828 ["INT_ADD", "register:40f0:8", ["const:b53828:8", "const:4:8"]]
+ 00b53828 ["CALL", null, ["callee:00bde090:8"]]
- 00b537e4 bytes 172a0294
+ 00b53828 bytes 1a2a0294
- 00b537ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00b537ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53830 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2d0:8"]]
+ 00b53830 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b537ec bytes 604a01f9
+ 00b53830 bytes 606a01f9
- 00b537cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00b537cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53810 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2d0:8"]]
+ 00b53810 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b537cc bytes 684a41f9
+ 00b53810 bytes 686a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2492b4baa73b6feb2500d577a799600a"></a>

### [`00b53800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53800.md) → [`00b53844`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53844.md) _ZN8firebase13remote_config8internal15config_settings10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b53874",
      "incomplete_value": true,
      "site": "00b53874",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53830",
      "incomplete_value": true,
      "site": "00b53830",
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
            "const:290:8"
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
      "definition_site": "00b53858",
      "incomplete_value": true,
      "site": "00b53858",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53814",
      "incomplete_value": true,
      "site": "00b53814",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b53860",
      "incomplete_value": false,
      "site": "00b5386c",
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
            "const:f3e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5381c",
      "incomplete_value": false,
      "site": "00b53828",
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
            "const:ea4:8"
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
      "00b53854",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53860",
      "PARAM",
      [
        "storage",
        "002a7ea4",
        null,
        "string"
      ]
    ],
    [
      "00b53874",
      "WRITE",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53854",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53860",
      "PARAM",
      [
        "storage",
        "002a7f3e",
        null,
        "string"
      ]
    ],
    [
      "00b53874",
      "WRITE",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53800.md#insn-00b53828) · [`00b53830`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53800.md#insn-00b53830) · [`00b53810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53800.md#insn-00b53810)
- 新版 `00b5386c`（命令位置の公開資料なし） · `00b53874`（命令位置の公開資料なし） · `00b53854`（命令位置の公開資料なし）

~~~diff
- 00b53828 ["INT_ADD", "register:40f0:8", ["const:b53828:8", "const:4:8"]]
- 00b53828 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5386c ["INT_ADD", "register:40f0:8", ["const:b5386c:8", "const:4:8"]]
+ 00b5386c ["CALL", null, ["callee:00bde090:8"]]
- 00b53828 bytes 062a0294
+ 00b5386c bytes 092a0294
- 00b53830 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00b53830 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53874 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2d0:8"]]
+ 00b53874 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53830 bytes 604a01f9
+ 00b53874 bytes 606a01f9
- 00b53810 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:290:8"]]
- 00b53810 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53854 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2d0:8"]]
+ 00b53854 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53810 bytes 684a41f9
+ 00b53854 bytes 686a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-668aecd0db1af2894412aca902a48670"></a>

### [`00b53850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53850.md) → [`00b53894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53894.md) _ZN8firebase13remote_config8internal15config_settings15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b538ec",
      "incomplete_value": true,
      "site": "00b538ec",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b538a8",
      "incomplete_value": true,
      "site": "00b538a8",
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
            "const:298:8"
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
      "definition_site": "00b538c8",
      "incomplete_value": true,
      "site": "00b538d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53884",
      "incomplete_value": true,
      "site": "00b53890",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:290:8"
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
      "00b538a8",
      "READ",
      [
        "storage",
        "010a1298",
        null,
        "undefined1"
      ]
    ],
    [
      "00b538c8",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b538ec",
      "WRITE",
      [
        "storage",
        "010a1298",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b538a8",
      "READ",
      [
        "storage",
        "010a12d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b538c8",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b538ec",
      "WRITE",
      [
        "storage",
        "010a12d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53850.md#insn-00b53864) · [`00b53890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53850.md#insn-00b53890) · [`00b538a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53850.md#insn-00b538a8)
- 新版 `00b538a8`（命令位置の公開資料なし） · `00b538d4`（命令位置の公開資料なし） · `00b538ec`（命令位置の公開資料なし）

~~~diff
- 00b53864 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:298:8"]]
- 00b53864 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b53864 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b538a8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:2d8:8"]]
+ 00b538a8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b538a8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b53864 bytes a8624a39
+ 00b538a8 bytes a8624b39
- 00b53890 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53890 ["INT_ADD", "register:40f0:8", ["const:b53890:8", "const:4:8"]]
- 00b53890 ["CALLIND", null, ["register:0:8"]]
+ 00b538d4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b538d4 ["INT_ADD", "register:40f0:8", ["const:b538d4:8", "const:4:8"]]
+ 00b538d4 ["CALLIND", null, ["register:0:8"]]
- 00b53890 bytes 00013fd6
+ 00b538d4 bytes 00013fd6
- 00b538a8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b538a8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:298:8"]]
- 00b538a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b538ec ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b538ec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:2d8:8"]]
+ 00b538ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b538a8 bytes a0620a39
+ 00b538ec bytes a0620b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-addce8e79ccfc0c08c7e9b0fe79cb9d6"></a>

### [`00b538bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b538bc.md) → [`00b53900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53900.md) _ZN8firebase13remote_config8internal15config_settings12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b5393c",
      "incomplete_value": true,
      "site": "00b5393c",
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
            "const:2d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b538f8",
      "incomplete_value": true,
      "site": "00b538f8",
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
            "const:298:8"
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
      "definition_site": "00b5395c",
      "incomplete_value": true,
      "site": "00b5395c",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53918",
      "incomplete_value": true,
      "site": "00b53918",
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
            "const:290:8"
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
      "definition_site": "00b53918",
      "incomplete_value": true,
      "site": "00b53918",
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
      "definition_site": "00b538d4",
      "incomplete_value": true,
      "site": "00b538d4",
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
      "00b53914",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53920",
      "READ",
      [
        "storage",
        "010a1298",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5393c",
      "WRITE",
      [
        "storage",
        "010a1298",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53914",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53920",
      "READ",
      [
        "storage",
        "010a12d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5393c",
      "WRITE",
      [
        "storage",
        "010a12d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b538d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b538bc.md#insn-00b538d0) · [`00b538f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b538bc.md#insn-00b538f8) · [`00b53914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b538bc.md#insn-00b53914)
- 新版 `00b53914`（命令位置の公開資料なし） · `00b5393c`（命令位置の公開資料なし） · `00b53958`（命令位置の公開資料なし）

~~~diff
- 00b538d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00b538d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53914 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2d0:8"]]
+ 00b53914 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b538d0 bytes 814a41f9
+ 00b53914 bytes 816a41f9
- 00b538f8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b538f8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b538f8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:298:8"]]
- 00b538f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b5393c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b5393c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b5393c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2d8:8"]]
+ 00b5393c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b538f8 bytes bf620a39
+ 00b5393c bytes bf620b39
- 00b53914 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53914 ["INT_ADD", "register:40f0:8", ["const:b53914:8", "const:4:8"]]
- 00b53914 ["CALLIND", null, ["register:0:8"]]
+ 00b53958 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53958 ["INT_ADD", "register:40f0:8", ["const:b53958:8", "const:4:8"]]
+ 00b53958 ["CALLIND", null, ["register:0:8"]]
- 00b53914 bytes 00013fd6
+ 00b53958 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b44ef1d855a91d06af1c8e442270b3bc"></a>

### [`00b5392c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5392c.md) → [`00b53970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53970.md) _ZN8firebase13remote_config8internal15config_settings14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b539b0",
      "incomplete_value": true,
      "site": "00b539b0",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5396c",
      "incomplete_value": true,
      "site": "00b5396c",
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
            "const:290:8"
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
      "definition_site": "00b5398c",
      "incomplete_value": true,
      "site": "00b5398c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53948",
      "incomplete_value": true,
      "site": "00b53948",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b53994",
      "incomplete_value": false,
      "site": "00b539a8",
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
            "const:f3e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53950",
      "incomplete_value": false,
      "site": "00b53964",
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
            "const:ea4:8"
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
      "00b53984",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53994",
      "PARAM",
      [
        "storage",
        "002a7ea4",
        null,
        "string"
      ]
    ],
    [
      "00b539b0",
      "WRITE",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53984",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53994",
      "PARAM",
      [
        "storage",
        "002a7f3e",
        null,
        "string"
      ]
    ],
    [
      "00b539b0",
      "WRITE",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5392c.md#insn-00b53964) · [`00b5396c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5392c.md#insn-00b5396c) · [`00b53940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5392c.md#insn-00b53940)
- 新版 `00b539a8`（命令位置の公開資料なし） · `00b539b0`（命令位置の公開資料なし） · `00b53984`（命令位置の公開資料なし）

~~~diff
- 00b53964 ["INT_ADD", "register:40f0:8", ["const:b53964:8", "const:4:8"]]
- 00b53964 ["CALL", null, ["callee:00bde090:8"]]
+ 00b539a8 ["INT_ADD", "register:40f0:8", ["const:b539a8:8", "const:4:8"]]
+ 00b539a8 ["CALL", null, ["callee:00bde090:8"]]
- 00b53964 bytes b7290294
+ 00b539a8 bytes ba290294
- 00b5396c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00b5396c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b539b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2d0:8"]]
+ 00b539b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5396c bytes 804a01f9
+ 00b539b0 bytes 806a01f9
- 00b53940 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00b53940 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53984 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2d0:8"]]
+ 00b53984 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53940 bytes 814a41f9
+ 00b53984 bytes 816a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9aaf53004bed120e441c3e5d6b7c80c"></a>

### [`00b5399c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5399c.md) → [`00b539e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b539e0.md) _ZN8firebase13remote_config8internal15config_settings11GetMethodIdENS2_6MethodE

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
      "definition_site": "00b539fc",
      "incomplete_value": false,
      "site": "00b53a00",
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
      "definition_site": "00b539b8",
      "incomplete_value": false,
      "site": "00b539bc",
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
      "definition_site": "00b53a0c",
      "incomplete_value": true,
      "site": "00b53a18",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b539c8",
      "incomplete_value": true,
      "site": "00b539d4",
      "value": [
        "LOAD",
        "8",
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
      "00b539fc",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b53a0c",
      "DATA",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b539fc",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b53a0c",
      "DATA",
      [
        "storage",
        "010a12e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b539bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5399c.md#insn-00b539bc) · [`00b539b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5399c.md#insn-00b539b8) · [`00b539c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b5399c.md#insn-00b539c4)
- 新版 `00b53a00`（命令位置の公開資料なし） · `00b539fc`（命令位置の公開資料なし） · `00b53a08`（命令位置の公開資料なし）

~~~diff
- 00b539bc ["INT_ADD", "register:40f0:8", ["const:b539bc:8", "const:4:8"]]
- 00b539bc ["CALL", null, ["callee:00bde180:8"]]
+ 00b53a00 ["INT_ADD", "register:40f0:8", ["const:b53a00:8", "const:4:8"]]
+ 00b53a00 ["CALL", null, ["callee:00bde180:8"]]
- 00b539bc bytes dd290294
+ 00b53a00 bytes e0290294
- 00b539b8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b539b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b539b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b539b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b539fc ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b539fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b539fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b539fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b539b8 bytes 00501791
+ 00b539fc bytes 001c1591
- 00b539c4 ["COPY", "tmp:0:8", ["const:2a0:8"]]
- 00b539c4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b539c4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b539c4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b53a08 ["COPY", "tmp:0:8", ["const:2e0:8"]]
+ 00b53a08 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53a08 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53a08 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b539c4 bytes 08810a91
+ 00b53a08 bytes 08810b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1909ee4f1ef955a1e805f15211d3d8e"></a>

### [`00b539d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b539d8.md) → [`00b53a1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53a1c.md) _ZN8firebase13remote_config8internal15config_settings13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b53a5c",
      "incomplete_value": true,
      "site": "00b53a5c",
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
            "const:2d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53a18",
      "incomplete_value": true,
      "site": "00b53a18",
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
            "const:290:8"
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
      "definition_site": "00b53a38",
      "incomplete_value": true,
      "site": "00b53a38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b539f4",
      "incomplete_value": true,
      "site": "00b539f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b53a40",
      "incomplete_value": false,
      "site": "00b53a54",
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
            "const:f3e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b539fc",
      "incomplete_value": false,
      "site": "00b53a10",
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
            "const:ea4:8"
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
      "00b53a30",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53a40",
      "PARAM",
      [
        "storage",
        "002a7ea4",
        null,
        "string"
      ]
    ],
    [
      "00b53a5c",
      "WRITE",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53a30",
      "READ",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53a40",
      "PARAM",
      [
        "storage",
        "002a7f3e",
        null,
        "string"
      ]
    ],
    [
      "00b53a5c",
      "WRITE",
      [
        "storage",
        "010a12d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53a10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b539d8.md#insn-00b53a10) · [`00b53a18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b539d8.md#insn-00b53a18) · [`00b539ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b539d8.md#insn-00b539ec)
- 新版 `00b53a54`（命令位置の公開資料なし） · `00b53a5c`（命令位置の公開資料なし） · `00b53a30`（命令位置の公開資料なし）

~~~diff
- 00b53a10 ["INT_ADD", "register:40f0:8", ["const:b53a10:8", "const:4:8"]]
- 00b53a10 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53a54 ["INT_ADD", "register:40f0:8", ["const:b53a54:8", "const:4:8"]]
+ 00b53a54 ["CALL", null, ["callee:00bde090:8"]]
- 00b53a10 bytes 8c290294
+ 00b53a54 bytes 8f290294
- 00b53a18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00b53a18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53a5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2d0:8"]]
+ 00b53a5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53a18 bytes 804a01f9
+ 00b53a5c bytes 806a01f9
- 00b539ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:290:8"]]
- 00b539ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53a30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2d0:8"]]
+ 00b53a30 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b539ec bytes 814a41f9
+ 00b53a30 bytes 816a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea4861d28be2473cb92c0a6d2eeecb43"></a>

### [`00b53a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53a48.md) → [`00b53a8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53a8c.md) _ZN8firebase13remote_config8internal15config_settings10GetFieldIdENS2_5FieldE

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
      "definition_site": "00b53aa8",
      "incomplete_value": false,
      "site": "00b53aac",
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
      "definition_site": "00b53a64",
      "incomplete_value": false,
      "site": "00b53a68",
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
      "definition_site": "00b53ab8",
      "incomplete_value": true,
      "site": "00b53ac4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b53a74",
      "incomplete_value": true,
      "site": "00b53a80",
      "value": [
        "LOAD",
        "8",
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
      "00b53aa8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b53ab8",
      "DATA",
      [
        "storage",
        "010a12b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b53aa8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b53ab8",
      "DATA",
      [
        "storage",
        "010a12f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53a48.md#insn-00b53a68) · [`00b53a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53a48.md#insn-00b53a64) · [`00b53a70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53a48.md#insn-00b53a70)
- 新版 `00b53aac`（命令位置の公開資料なし） · `00b53aa8`（命令位置の公開資料なし） · `00b53ab4`（命令位置の公開資料なし）

~~~diff
- 00b53a68 ["INT_ADD", "register:40f0:8", ["const:b53a68:8", "const:4:8"]]
- 00b53a68 ["CALL", null, ["callee:00bde180:8"]]
+ 00b53aac ["INT_ADD", "register:40f0:8", ["const:b53aac:8", "const:4:8"]]
+ 00b53aac ["CALL", null, ["callee:00bde180:8"]]
- 00b53a68 bytes b2290294
+ 00b53aac bytes b5290294
- 00b53a64 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b53a64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b53a64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b53a64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b53aa8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b53aa8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53aa8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53aa8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b53a64 bytes 00fc1991
+ 00b53aa8 bytes 00c81791
- 00b53a70 ["COPY", "tmp:0:8", ["const:2b0:8"]]
- 00b53a70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b53a70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b53a70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b53ab4 ["COPY", "tmp:0:8", ["const:2f0:8"]]
+ 00b53ab4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53ab4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53ab4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b53a70 bytes 08c10a91
+ 00b53ab4 bytes 08c10b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b947c00d5347fdf30494f2a63ca52885"></a>

### [`00b53a84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53a84.md) → [`00b53ac8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53ac8.md) _ZN8firebase13remote_config8internal23config_settings_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embe

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
      "definition_site": "00b53af4",
      "incomplete_value": true,
      "site": "00b53af4",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53ab0",
      "incomplete_value": true,
      "site": "00b53ab0",
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
            "const:2b8:8"
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
      "definition_site": "00b53adc",
      "incomplete_value": true,
      "site": "00b53adc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53a98",
      "incomplete_value": true,
      "site": "00b53a98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b53ae8",
      "incomplete_value": false,
      "site": "00b53aec",
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
            "const:f07:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53aa4",
      "incomplete_value": false,
      "site": "00b53aa8",
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
            "const:e6d:8"
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
      "00b53ad8",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53ae8",
      "PARAM",
      [
        "storage",
        "002a8e6d",
        null,
        "string"
      ]
    ],
    [
      "00b53af4",
      "WRITE",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53ad8",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53ae8",
      "PARAM",
      [
        "storage",
        "002a8f07",
        null,
        "string"
      ]
    ],
    [
      "00b53af4",
      "WRITE",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53aa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53a84.md#insn-00b53aa8) · [`00b53ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53a84.md#insn-00b53ab0) · [`00b53a94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53a84.md#insn-00b53a94)
- 新版 `00b53aec`（命令位置の公開資料なし） · `00b53af4`（命令位置の公開資料なし） · `00b53ad8`（命令位置の公開資料なし）

~~~diff
- 00b53aa8 ["INT_ADD", "register:40f0:8", ["const:b53aa8:8", "const:4:8"]]
- 00b53aa8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53aec ["INT_ADD", "register:40f0:8", ["const:b53aec:8", "const:4:8"]]
+ 00b53aec ["CALL", null, ["callee:00bde090:8"]]
- 00b53aa8 bytes 66290294
+ 00b53aec bytes 69290294
- 00b53ab0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
- 00b53ab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53af4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
+ 00b53af4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53ab0 bytes 605e01f9
+ 00b53af4 bytes 607e01f9
- 00b53a94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
- 00b53a94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53ad8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
+ 00b53ad8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53a94 bytes 685e41f9
+ 00b53ad8 bytes 687e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65d133b7b33f32b4adc99fe4ac397fe8"></a>

### [`00b53ac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ac4.md) → [`00b53b08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b08.md) _ZN8firebase13remote_config8internal23config_settings_builder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embe

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
      "definition_site": "00b53b34",
      "incomplete_value": true,
      "site": "00b53b34",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53af0",
      "incomplete_value": true,
      "site": "00b53af0",
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
            "const:2b8:8"
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
      "definition_site": "00b53b1c",
      "incomplete_value": true,
      "site": "00b53b1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53ad8",
      "incomplete_value": true,
      "site": "00b53ad8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b53b24",
      "incomplete_value": false,
      "site": "00b53b2c",
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
            "const:f07:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53ae0",
      "incomplete_value": false,
      "site": "00b53ae8",
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
            "const:e6d:8"
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
      "00b53b18",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53b24",
      "PARAM",
      [
        "storage",
        "002a8e6d",
        null,
        "string"
      ]
    ],
    [
      "00b53b34",
      "WRITE",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53b18",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53b24",
      "PARAM",
      [
        "storage",
        "002a8f07",
        null,
        "string"
      ]
    ],
    [
      "00b53b34",
      "WRITE",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53ae8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ac4.md#insn-00b53ae8) · [`00b53af0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ac4.md#insn-00b53af0) · [`00b53ad4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ac4.md#insn-00b53ad4)
- 新版 `00b53b2c`（命令位置の公開資料なし） · `00b53b34`（命令位置の公開資料なし） · `00b53b18`（命令位置の公開資料なし）

~~~diff
- 00b53ae8 ["INT_ADD", "register:40f0:8", ["const:b53ae8:8", "const:4:8"]]
- 00b53ae8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53b2c ["INT_ADD", "register:40f0:8", ["const:b53b2c:8", "const:4:8"]]
+ 00b53b2c ["CALL", null, ["callee:00bde090:8"]]
- 00b53ae8 bytes 56290294
+ 00b53b2c bytes 59290294
- 00b53af0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
- 00b53af0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53b34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
+ 00b53b34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53af0 bytes 605e01f9
+ 00b53b34 bytes 607e01f9
- 00b53ad4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
- 00b53ad4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53b18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
+ 00b53b18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53ad4 bytes 685e41f9
+ 00b53b18 bytes 687e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa712d6d688fc8ac28d064363504ba94"></a>

### [`00b53b04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b04.md) → [`00b53b48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b48.md) _ZN8firebase13remote_config8internal23config_settings_builder10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b53b78",
      "incomplete_value": true,
      "site": "00b53b78",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53b34",
      "incomplete_value": true,
      "site": "00b53b34",
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
            "const:2b8:8"
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
      "definition_site": "00b53b5c",
      "incomplete_value": true,
      "site": "00b53b5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53b18",
      "incomplete_value": true,
      "site": "00b53b18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b53b68",
      "incomplete_value": false,
      "site": "00b53b70",
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
            "const:f07:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53b24",
      "incomplete_value": false,
      "site": "00b53b2c",
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
            "const:e6d:8"
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
      "00b53b58",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53b68",
      "PARAM",
      [
        "storage",
        "002a8e6d",
        null,
        "string"
      ]
    ],
    [
      "00b53b78",
      "WRITE",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53b58",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53b68",
      "PARAM",
      [
        "storage",
        "002a8f07",
        null,
        "string"
      ]
    ],
    [
      "00b53b78",
      "WRITE",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53b2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b04.md#insn-00b53b2c) · [`00b53b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b04.md#insn-00b53b34) · [`00b53b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b04.md#insn-00b53b14)
- 新版 `00b53b70`（命令位置の公開資料なし） · `00b53b78`（命令位置の公開資料なし） · `00b53b58`（命令位置の公開資料なし）

~~~diff
- 00b53b2c ["INT_ADD", "register:40f0:8", ["const:b53b2c:8", "const:4:8"]]
- 00b53b2c ["CALL", null, ["callee:00bde090:8"]]
+ 00b53b70 ["INT_ADD", "register:40f0:8", ["const:b53b70:8", "const:4:8"]]
+ 00b53b70 ["CALL", null, ["callee:00bde090:8"]]
- 00b53b2c bytes 45290294
+ 00b53b70 bytes 48290294
- 00b53b34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
- 00b53b34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53b78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
+ 00b53b78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53b34 bytes 605e01f9
+ 00b53b78 bytes 607e01f9
- 00b53b14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
- 00b53b14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53b58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
+ 00b53b58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53b14 bytes 685e41f9
+ 00b53b58 bytes 687e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e81261dcd392ec30ff75ae00c45c6c30"></a>

### [`00b53b48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b48.md) → [`00b53b8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53b8c.md) _ZN8firebase13remote_config8internal23config_settings_builder10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b53bbc",
      "incomplete_value": true,
      "site": "00b53bbc",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53b78",
      "incomplete_value": true,
      "site": "00b53b78",
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
            "const:2b8:8"
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
      "definition_site": "00b53ba0",
      "incomplete_value": true,
      "site": "00b53ba0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53b5c",
      "incomplete_value": true,
      "site": "00b53b5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b53ba8",
      "incomplete_value": false,
      "site": "00b53bb4",
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
            "const:f07:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53b64",
      "incomplete_value": false,
      "site": "00b53b70",
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
            "const:e6d:8"
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
      "00b53b9c",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53ba8",
      "PARAM",
      [
        "storage",
        "002a8e6d",
        null,
        "string"
      ]
    ],
    [
      "00b53bbc",
      "WRITE",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53b9c",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53ba8",
      "PARAM",
      [
        "storage",
        "002a8f07",
        null,
        "string"
      ]
    ],
    [
      "00b53bbc",
      "WRITE",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b48.md#insn-00b53b70) · [`00b53b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b48.md#insn-00b53b78) · [`00b53b58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b48.md#insn-00b53b58)
- 新版 `00b53bb4`（命令位置の公開資料なし） · `00b53bbc`（命令位置の公開資料なし） · `00b53b9c`（命令位置の公開資料なし）

~~~diff
- 00b53b70 ["INT_ADD", "register:40f0:8", ["const:b53b70:8", "const:4:8"]]
- 00b53b70 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53bb4 ["INT_ADD", "register:40f0:8", ["const:b53bb4:8", "const:4:8"]]
+ 00b53bb4 ["CALL", null, ["callee:00bde090:8"]]
- 00b53b70 bytes 34290294
+ 00b53bb4 bytes 37290294
- 00b53b78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
- 00b53b78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53bbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
+ 00b53bbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53b78 bytes 605e01f9
+ 00b53bbc bytes 607e01f9
- 00b53b58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2b8:8"]]
- 00b53b58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53b9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f8:8"]]
+ 00b53b9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53b58 bytes 685e41f9
+ 00b53b9c bytes 687e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5044d4c35677d4200ae0639fff05721"></a>

### [`00b53b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b98.md) → [`00b53bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53bdc.md) _ZN8firebase13remote_config8internal23config_settings_builder15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b53c34",
      "incomplete_value": true,
      "site": "00b53c34",
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
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53bf0",
      "incomplete_value": true,
      "site": "00b53bf0",
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
            "const:2c0:8"
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
      "00b53bf0",
      "READ",
      [
        "storage",
        "010a12c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53c10",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53c34",
      "WRITE",
      [
        "storage",
        "010a12c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53bf0",
      "READ",
      [
        "storage",
        "010a1300",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53c10",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53c34",
      "WRITE",
      [
        "storage",
        "010a1300",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53bac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b98.md#insn-00b53bac) · [`00b53bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b98.md#insn-00b53bf0) · [`00b53bcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53b98.md#insn-00b53bcc)
- 新版 `00b53bf0`（命令位置の公開資料なし） · `00b53c34`（命令位置の公開資料なし） · `00b53c10`（命令位置の公開資料なし）

~~~diff
- 00b53bac ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:2c0:8"]]
- 00b53bac ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b53bac ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b53bf0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:300:8"]]
+ 00b53bf0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b53bf0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b53bac bytes a8024b39
+ 00b53bf0 bytes a8024c39
- 00b53bf0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b53bf0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:2c0:8"]]
- 00b53bf0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b53c34 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b53c34 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:300:8"]]
+ 00b53c34 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b53bf0 bytes a0020b39
+ 00b53c34 bytes a0020c39
- 00b53bcc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2b8:8"]]
- 00b53bcc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53c10 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2f8:8"]]
+ 00b53c10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53bcc bytes 215d41f9
+ 00b53c10 bytes 217d41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fb111de5511d5a24b9ff1d495c69e76"></a>

### [`00b53c04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53c04.md) → [`00b53c48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53c48.md) _ZN8firebase13remote_config8internal23config_settings_builder12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b53c84",
      "incomplete_value": true,
      "site": "00b53c84",
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
            "const:300:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53c40",
      "incomplete_value": true,
      "site": "00b53c40",
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
            "const:2c0:8"
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
      "definition_site": "00b53ca4",
      "incomplete_value": true,
      "site": "00b53ca4",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53c60",
      "incomplete_value": true,
      "site": "00b53c60",
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
            "const:2b8:8"
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
      "definition_site": "00b53c60",
      "incomplete_value": true,
      "site": "00b53c60",
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
      "definition_site": "00b53c1c",
      "incomplete_value": true,
      "site": "00b53c1c",
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
      "00b53c5c",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53c68",
      "READ",
      [
        "storage",
        "010a12c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53c84",
      "WRITE",
      [
        "storage",
        "010a12c0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53c5c",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53c68",
      "READ",
      [
        "storage",
        "010a1300",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53c84",
      "WRITE",
      [
        "storage",
        "010a1300",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53c18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53c04.md#insn-00b53c18) · [`00b53c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53c04.md#insn-00b53c40) · [`00b53c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53c04.md#insn-00b53c5c)
- 新版 `00b53c5c`（命令位置の公開資料なし） · `00b53c84`（命令位置の公開資料なし） · `00b53ca0`（命令位置の公開資料なし）

~~~diff
- 00b53c18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2b8:8"]]
- 00b53c18 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53c5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
+ 00b53c5c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53c18 bytes 815e41f9
+ 00b53c5c bytes 817e41f9
- 00b53c40 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b53c40 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b53c40 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2c0:8"]]
- 00b53c40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b53c84 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b53c84 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b53c84 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:300:8"]]
+ 00b53c84 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b53c40 bytes bf020b39
+ 00b53c84 bytes bf020c39
- 00b53c5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53c5c ["INT_ADD", "register:40f0:8", ["const:b53c5c:8", "const:4:8"]]
- 00b53c5c ["CALLIND", null, ["register:0:8"]]
+ 00b53ca0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53ca0 ["INT_ADD", "register:40f0:8", ["const:b53ca0:8", "const:4:8"]]
+ 00b53ca0 ["CALLIND", null, ["register:0:8"]]
- 00b53c5c bytes 00013fd6
+ 00b53ca0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b35541fad35acbe64eaf3a5ada9fb449"></a>

### [`00b53c74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53c74.md) → [`00b53cb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53cb8.md) _ZN8firebase13remote_config8internal23config_settings_builder14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b53cf8",
      "incomplete_value": true,
      "site": "00b53cf8",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53cb4",
      "incomplete_value": true,
      "site": "00b53cb4",
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
            "const:2b8:8"
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
      "definition_site": "00b53cd4",
      "incomplete_value": true,
      "site": "00b53cd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53c90",
      "incomplete_value": true,
      "site": "00b53c90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b53cdc",
      "incomplete_value": false,
      "site": "00b53cf0",
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
            "const:f07:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53c98",
      "incomplete_value": false,
      "site": "00b53cac",
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
            "const:e6d:8"
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
      "00b53ccc",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53cdc",
      "PARAM",
      [
        "storage",
        "002a8e6d",
        null,
        "string"
      ]
    ],
    [
      "00b53cf8",
      "WRITE",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53ccc",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53cdc",
      "PARAM",
      [
        "storage",
        "002a8f07",
        null,
        "string"
      ]
    ],
    [
      "00b53cf8",
      "WRITE",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53cac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53c74.md#insn-00b53cac) · [`00b53cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53c74.md#insn-00b53cb4) · [`00b53c88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53c74.md#insn-00b53c88)
- 新版 `00b53cf0`（命令位置の公開資料なし） · `00b53cf8`（命令位置の公開資料なし） · `00b53ccc`（命令位置の公開資料なし）

~~~diff
- 00b53cac ["INT_ADD", "register:40f0:8", ["const:b53cac:8", "const:4:8"]]
- 00b53cac ["CALL", null, ["callee:00bde090:8"]]
+ 00b53cf0 ["INT_ADD", "register:40f0:8", ["const:b53cf0:8", "const:4:8"]]
+ 00b53cf0 ["CALL", null, ["callee:00bde090:8"]]
- 00b53cac bytes e5280294
+ 00b53cf0 bytes e8280294
- 00b53cb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2b8:8"]]
- 00b53cb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53cf8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
+ 00b53cf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53cb4 bytes 805e01f9
+ 00b53cf8 bytes 807e01f9
- 00b53c88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2b8:8"]]
- 00b53c88 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53ccc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
+ 00b53ccc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53c88 bytes 815e41f9
+ 00b53ccc bytes 817e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b86c03bf74f4eb00a1b9d0f4ab3d1df"></a>

### [`00b53ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ce4.md) → [`00b53d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53d28.md) _ZN8firebase13remote_config8internal23config_settings_builder11GetMethodIdENS2_6MethodE

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
      "definition_site": "00b53d44",
      "incomplete_value": false,
      "site": "00b53d48",
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
      "definition_site": "00b53d00",
      "incomplete_value": false,
      "site": "00b53d04",
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
      "definition_site": "00b53d54",
      "incomplete_value": true,
      "site": "00b53d60",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b53d10",
      "incomplete_value": true,
      "site": "00b53d1c",
      "value": [
        "LOAD",
        "8",
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
      "00b53d44",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b53d54",
      "DATA",
      [
        "storage",
        "010a12c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53d44",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b53d54",
      "DATA",
      [
        "storage",
        "010a1308",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53d04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ce4.md#insn-00b53d04) · [`00b53d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ce4.md#insn-00b53d00) · [`00b53d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ce4.md#insn-00b53d0c)
- 新版 `00b53d48`（命令位置の公開資料なし） · `00b53d44`（命令位置の公開資料なし） · `00b53d50`（命令位置の公開資料なし）

~~~diff
- 00b53d04 ["INT_ADD", "register:40f0:8", ["const:b53d04:8", "const:4:8"]]
- 00b53d04 ["CALL", null, ["callee:00bde180:8"]]
+ 00b53d48 ["INT_ADD", "register:40f0:8", ["const:b53d48:8", "const:4:8"]]
+ 00b53d48 ["CALL", null, ["callee:00bde180:8"]]
- 00b53d04 bytes 0b290294
+ 00b53d48 bytes 0e290294
- 00b53d00 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b53d00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b53d00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b53d00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b53d44 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b53d44 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53d44 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53d44 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b53d00 bytes 00501791
+ 00b53d44 bytes 001c1591
- 00b53d0c ["COPY", "tmp:0:8", ["const:2c8:8"]]
- 00b53d0c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b53d0c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b53d0c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b53d50 ["COPY", "tmp:0:8", ["const:308:8"]]
+ 00b53d50 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53d50 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53d50 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b53d0c bytes 08210b91
+ 00b53d50 bytes 08210c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b6efbe6b7a04989418f1401dfd6171f"></a>

### [`00b53d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53d20.md) → [`00b53d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53d64.md) _ZN8firebase13remote_config8internal23config_settings_builder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b53da4",
      "incomplete_value": true,
      "site": "00b53da4",
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
            "const:2f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53d60",
      "incomplete_value": true,
      "site": "00b53d60",
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
            "const:2b8:8"
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
      "definition_site": "00b53d80",
      "incomplete_value": true,
      "site": "00b53d80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53d3c",
      "incomplete_value": true,
      "site": "00b53d3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b53d88",
      "incomplete_value": false,
      "site": "00b53d9c",
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
            "const:f07:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53d44",
      "incomplete_value": false,
      "site": "00b53d58",
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
            "const:e6d:8"
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
      "00b53d78",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53d88",
      "PARAM",
      [
        "storage",
        "002a8e6d",
        null,
        "string"
      ]
    ],
    [
      "00b53da4",
      "WRITE",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53d78",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53d88",
      "PARAM",
      [
        "storage",
        "002a8f07",
        null,
        "string"
      ]
    ],
    [
      "00b53da4",
      "WRITE",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53d58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53d20.md#insn-00b53d58) · [`00b53d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53d20.md#insn-00b53d60) · [`00b53d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53d20.md#insn-00b53d34)
- 新版 `00b53d9c`（命令位置の公開資料なし） · `00b53da4`（命令位置の公開資料なし） · `00b53d78`（命令位置の公開資料なし）

~~~diff
- 00b53d58 ["INT_ADD", "register:40f0:8", ["const:b53d58:8", "const:4:8"]]
- 00b53d58 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53d9c ["INT_ADD", "register:40f0:8", ["const:b53d9c:8", "const:4:8"]]
+ 00b53d9c ["CALL", null, ["callee:00bde090:8"]]
- 00b53d58 bytes ba280294
+ 00b53d9c bytes bd280294
- 00b53d60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2b8:8"]]
- 00b53d60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53da4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
+ 00b53da4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53d60 bytes 805e01f9
+ 00b53da4 bytes 807e01f9
- 00b53d34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2b8:8"]]
- 00b53d34 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53d78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f8:8"]]
+ 00b53d78 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53d34 bytes 815e41f9
+ 00b53d78 bytes 817e41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69d7385fd52bdd1c41156982b1334a7e"></a>

### [`00b53d90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53d90.md) → [`00b53dd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53dd4.md) _ZN8firebase13remote_config8internal23config_settings_builder10GetFieldIdENS2_5FieldE

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
      "definition_site": "00b53df0",
      "incomplete_value": true,
      "site": "00b53df4",
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
      "definition_site": "00b53dac",
      "incomplete_value": true,
      "site": "00b53db0",
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
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b53e00",
      "incomplete_value": true,
      "site": "00b53e0c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b53dbc",
      "incomplete_value": true,
      "site": "00b53dc8",
      "value": [
        "LOAD",
        "8",
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
      "00b53df0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b53e00",
      "DATA",
      [
        "storage",
        "010a12e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b53df0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b53e00",
      "DATA",
      [
        "storage",
        "010a1328",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53d90.md#insn-00b53db0) · [`00b53dac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53d90.md#insn-00b53dac) · [`00b53db8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53d90.md#insn-00b53db8)
- 新版 `00b53df4`（命令位置の公開資料なし） · `00b53df0`（命令位置の公開資料なし） · `00b53dfc`（命令位置の公開資料なし）

~~~diff
- 00b53db0 ["INT_ADD", "register:40f0:8", ["const:b53db0:8", "const:4:8"]]
- 00b53db0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b53df4 ["INT_ADD", "register:40f0:8", ["const:b53df4:8", "const:4:8"]]
+ 00b53df4 ["CALL", null, ["callee:00bde180:8"]]
- 00b53db0 bytes e0280294
+ 00b53df4 bytes e3280294
- 00b53dac ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b53dac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b53dac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b53dac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b53df0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b53df0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53df0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b53df0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b53dac bytes 00fc1991
+ 00b53df0 bytes 00c81791
- 00b53db8 ["COPY", "tmp:0:8", ["const:2e8:8"]]
- 00b53db8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b53db8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b53db8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b53dfc ["COPY", "tmp:0:8", ["const:328:8"]]
+ 00b53dfc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53dfc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b53dfc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b53db8 bytes 08a10b91
+ 00b53dfc bytes 08a10c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0c8e08ca7e6e12bcca0a3f4a39ad155"></a>

### [`00b53dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53dcc.md) → [`00b53e10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e10.md) _ZN8firebase13remote_config8internal19throttled_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embedded

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
      "definition_site": "00b53e3c",
      "incomplete_value": true,
      "site": "00b53e3c",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53df8",
      "incomplete_value": true,
      "site": "00b53df8",
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
            "const:2f0:8"
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
      "definition_site": "00b53e24",
      "incomplete_value": true,
      "site": "00b53e24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53de0",
      "incomplete_value": true,
      "site": "00b53de0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b53e30",
      "incomplete_value": false,
      "site": "00b53e34",
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
            "const:f51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53dec",
      "incomplete_value": false,
      "site": "00b53df0",
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
            "const:eb7:8"
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
      "00b53e20",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53e30",
      "PARAM",
      [
        "storage",
        "002a8eb7",
        null,
        "string"
      ]
    ],
    [
      "00b53e3c",
      "WRITE",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53e20",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53e30",
      "PARAM",
      [
        "storage",
        "002a8f51",
        null,
        "string"
      ]
    ],
    [
      "00b53e3c",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53dcc.md#insn-00b53df0) · [`00b53df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53dcc.md#insn-00b53df8) · [`00b53ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53dcc.md#insn-00b53ddc)
- 新版 `00b53e34`（命令位置の公開資料なし） · `00b53e3c`（命令位置の公開資料なし） · `00b53e20`（命令位置の公開資料なし）

~~~diff
- 00b53df0 ["INT_ADD", "register:40f0:8", ["const:b53df0:8", "const:4:8"]]
- 00b53df0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53e34 ["INT_ADD", "register:40f0:8", ["const:b53e34:8", "const:4:8"]]
+ 00b53e34 ["CALL", null, ["callee:00bde090:8"]]
- 00b53df0 bytes 94280294
+ 00b53e34 bytes 97280294
- 00b53df8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00b53df8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53e3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
+ 00b53e3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53df8 bytes 607a01f9
+ 00b53e3c bytes 609a01f9
- 00b53ddc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00b53ddc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53e20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
+ 00b53e20 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53ddc bytes 687a41f9
+ 00b53e20 bytes 689a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0241d33b6ca0693036fa2d708f0d08e1"></a>

### [`00b53e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e0c.md) → [`00b53e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e50.md) _ZN8firebase13remote_config8internal19throttled_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12Embedded

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
      "definition_site": "00b53e7c",
      "incomplete_value": true,
      "site": "00b53e7c",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53e38",
      "incomplete_value": true,
      "site": "00b53e38",
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
            "const:2f0:8"
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
      "definition_site": "00b53e64",
      "incomplete_value": true,
      "site": "00b53e64",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53e20",
      "incomplete_value": true,
      "site": "00b53e20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b53e6c",
      "incomplete_value": false,
      "site": "00b53e74",
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
            "const:f51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53e28",
      "incomplete_value": false,
      "site": "00b53e30",
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
            "const:eb7:8"
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
      "00b53e60",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53e6c",
      "PARAM",
      [
        "storage",
        "002a8eb7",
        null,
        "string"
      ]
    ],
    [
      "00b53e7c",
      "WRITE",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53e60",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53e6c",
      "PARAM",
      [
        "storage",
        "002a8f51",
        null,
        "string"
      ]
    ],
    [
      "00b53e7c",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53e30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e0c.md#insn-00b53e30) · [`00b53e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e0c.md#insn-00b53e38) · [`00b53e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e0c.md#insn-00b53e1c)
- 新版 `00b53e74`（命令位置の公開資料なし） · `00b53e7c`（命令位置の公開資料なし） · `00b53e60`（命令位置の公開資料なし）

~~~diff
- 00b53e30 ["INT_ADD", "register:40f0:8", ["const:b53e30:8", "const:4:8"]]
- 00b53e30 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53e74 ["INT_ADD", "register:40f0:8", ["const:b53e74:8", "const:4:8"]]
+ 00b53e74 ["CALL", null, ["callee:00bde090:8"]]
- 00b53e30 bytes 84280294
+ 00b53e74 bytes 87280294
- 00b53e38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00b53e38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53e7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
+ 00b53e7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53e38 bytes 607a01f9
+ 00b53e7c bytes 609a01f9
- 00b53e1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00b53e1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53e60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
+ 00b53e60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53e1c bytes 687a41f9
+ 00b53e60 bytes 689a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b08057d1d1a9fe6c38d93e09c132b58a"></a>

### [`00b53e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e4c.md) → [`00b53e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53e90.md) _ZN8firebase13remote_config8internal19throttled_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b53ec0",
      "incomplete_value": true,
      "site": "00b53ec0",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53e7c",
      "incomplete_value": true,
      "site": "00b53e7c",
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
            "const:2f0:8"
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
      "definition_site": "00b53ea4",
      "incomplete_value": true,
      "site": "00b53ea4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53e60",
      "incomplete_value": true,
      "site": "00b53e60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b53eb0",
      "incomplete_value": false,
      "site": "00b53eb8",
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
            "const:f51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53e6c",
      "incomplete_value": false,
      "site": "00b53e74",
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
            "const:eb7:8"
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
      "00b53ea0",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53eb0",
      "PARAM",
      [
        "storage",
        "002a8eb7",
        null,
        "string"
      ]
    ],
    [
      "00b53ec0",
      "WRITE",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53ea0",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53eb0",
      "PARAM",
      [
        "storage",
        "002a8f51",
        null,
        "string"
      ]
    ],
    [
      "00b53ec0",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e4c.md#insn-00b53e74) · [`00b53e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e4c.md#insn-00b53e7c) · [`00b53e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e4c.md#insn-00b53e5c)
- 新版 `00b53eb8`（命令位置の公開資料なし） · `00b53ec0`（命令位置の公開資料なし） · `00b53ea0`（命令位置の公開資料なし）

~~~diff
- 00b53e74 ["INT_ADD", "register:40f0:8", ["const:b53e74:8", "const:4:8"]]
- 00b53e74 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53eb8 ["INT_ADD", "register:40f0:8", ["const:b53eb8:8", "const:4:8"]]
+ 00b53eb8 ["CALL", null, ["callee:00bde090:8"]]
- 00b53e74 bytes 73280294
+ 00b53eb8 bytes 76280294
- 00b53e7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00b53e7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53ec0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
+ 00b53ec0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53e7c bytes 607a01f9
+ 00b53ec0 bytes 609a01f9
- 00b53e5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00b53e5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53ea0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
+ 00b53ea0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53e5c bytes 687a41f9
+ 00b53ea0 bytes 689a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ebd5a2110f010b37176216b74b2b915a"></a>

### [`00b53e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e90.md) → [`00b53ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53ed4.md) _ZN8firebase13remote_config8internal19throttled_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b53f04",
      "incomplete_value": true,
      "site": "00b53f04",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53ec0",
      "incomplete_value": true,
      "site": "00b53ec0",
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
            "const:2f0:8"
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
      "definition_site": "00b53ee8",
      "incomplete_value": true,
      "site": "00b53ee8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53ea4",
      "incomplete_value": true,
      "site": "00b53ea4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b53ef0",
      "incomplete_value": false,
      "site": "00b53efc",
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
            "const:f51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53eac",
      "incomplete_value": false,
      "site": "00b53eb8",
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
            "const:eb7:8"
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
      "00b53ee4",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53ef0",
      "PARAM",
      [
        "storage",
        "002a8eb7",
        null,
        "string"
      ]
    ],
    [
      "00b53f04",
      "WRITE",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b53ee4",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53ef0",
      "PARAM",
      [
        "storage",
        "002a8f51",
        null,
        "string"
      ]
    ],
    [
      "00b53f04",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53eb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e90.md#insn-00b53eb8) · [`00b53ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e90.md#insn-00b53ec0) · [`00b53ea0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53e90.md#insn-00b53ea0)
- 新版 `00b53efc`（命令位置の公開資料なし） · `00b53f04`（命令位置の公開資料なし） · `00b53ee4`（命令位置の公開資料なし）

~~~diff
- 00b53eb8 ["INT_ADD", "register:40f0:8", ["const:b53eb8:8", "const:4:8"]]
- 00b53eb8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b53efc ["INT_ADD", "register:40f0:8", ["const:b53efc:8", "const:4:8"]]
+ 00b53efc ["CALL", null, ["callee:00bde090:8"]]
- 00b53eb8 bytes 62280294
+ 00b53efc bytes 65280294
- 00b53ec0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00b53ec0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b53f04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
+ 00b53f04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53ec0 bytes 607a01f9
+ 00b53f04 bytes 609a01f9
- 00b53ea0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:2f0:8"]]
- 00b53ea0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53ee4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
+ 00b53ee4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53ea0 bytes 687a41f9
+ 00b53ee4 bytes 689a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f307db735f3b3eaa8ddc20118f167f9"></a>

### [`00b53ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ee0.md) → [`00b53f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53f24.md) _ZN8firebase13remote_config8internal19throttled_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b53f7c",
      "incomplete_value": true,
      "site": "00b53f7c",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53f38",
      "incomplete_value": true,
      "site": "00b53f38",
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
            "const:2f8:8"
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
      "definition_site": "00b53f58",
      "incomplete_value": true,
      "site": "00b53f64",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:330:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53f14",
      "incomplete_value": true,
      "site": "00b53f20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f0:8"
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
      "00b53f38",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53f58",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53f7c",
      "WRITE",
      [
        "storage",
        "010a12f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53f38",
      "READ",
      [
        "storage",
        "010a1338",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53f58",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53f7c",
      "WRITE",
      [
        "storage",
        "010a1338",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ee0.md#insn-00b53ef4) · [`00b53f20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ee0.md#insn-00b53f20) · [`00b53f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53ee0.md#insn-00b53f38)
- 新版 `00b53f38`（命令位置の公開資料なし） · `00b53f64`（命令位置の公開資料なし） · `00b53f7c`（命令位置の公開資料なし）

~~~diff
- 00b53ef4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:2f8:8"]]
- 00b53ef4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b53ef4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b53f38 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
+ 00b53f38 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b53f38 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b53ef4 bytes a8e24b39
+ 00b53f38 bytes a8e24c39
- 00b53f20 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53f20 ["INT_ADD", "register:40f0:8", ["const:b53f20:8", "const:4:8"]]
- 00b53f20 ["CALLIND", null, ["register:0:8"]]
+ 00b53f64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53f64 ["INT_ADD", "register:40f0:8", ["const:b53f64:8", "const:4:8"]]
+ 00b53f64 ["CALLIND", null, ["register:0:8"]]
- 00b53f20 bytes 00013fd6
+ 00b53f64 bytes 00013fd6
- 00b53f38 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b53f38 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:2f8:8"]]
- 00b53f38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b53f7c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b53f7c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:338:8"]]
+ 00b53f7c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b53f38 bytes a0e20b39
+ 00b53f7c bytes a0e20c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edbc18a7a2e56feef5aa5274f8a4f805"></a>

### [`00b53f4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53f4c.md) → [`00b53f90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b53/00b53f90.md) _ZN8firebase13remote_config8internal19throttled_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b53fcc",
      "incomplete_value": true,
      "site": "00b53fcc",
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
            "const:338:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53f88",
      "incomplete_value": true,
      "site": "00b53f88",
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
            "const:2f8:8"
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
      "definition_site": "00b53fec",
      "incomplete_value": true,
      "site": "00b53fec",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53fa8",
      "incomplete_value": true,
      "site": "00b53fa8",
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
            "const:2f0:8"
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
      "definition_site": "00b53fa8",
      "incomplete_value": true,
      "site": "00b53fa8",
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
      "definition_site": "00b53f64",
      "incomplete_value": true,
      "site": "00b53f64",
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
      "00b53fa4",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53fb0",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53fcc",
      "WRITE",
      [
        "storage",
        "010a12f8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b53fa4",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b53fb0",
      "READ",
      [
        "storage",
        "010a1338",
        null,
        "undefined1"
      ]
    ],
    [
      "00b53fcc",
      "WRITE",
      [
        "storage",
        "010a1338",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53f4c.md#insn-00b53f60) · [`00b53f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53f4c.md#insn-00b53f88) · [`00b53fa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53f4c.md#insn-00b53fa4)
- 新版 `00b53fa4`（命令位置の公開資料なし） · `00b53fcc`（命令位置の公開資料なし） · `00b53fe8`（命令位置の公開資料なし）

~~~diff
- 00b53f60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f0:8"]]
- 00b53f60 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b53fa4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
+ 00b53fa4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53f60 bytes 817a41f9
+ 00b53fa4 bytes 819a41f9
- 00b53f88 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b53f88 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b53f88 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:2f8:8"]]
- 00b53f88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b53fcc ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b53fcc ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b53fcc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:338:8"]]
+ 00b53fcc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b53f88 bytes bfe20b39
+ 00b53fcc bytes bfe20c39
- 00b53fa4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b53fa4 ["INT_ADD", "register:40f0:8", ["const:b53fa4:8", "const:4:8"]]
- 00b53fa4 ["CALLIND", null, ["register:0:8"]]
+ 00b53fe8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b53fe8 ["INT_ADD", "register:40f0:8", ["const:b53fe8:8", "const:4:8"]]
+ 00b53fe8 ["CALLIND", null, ["register:0:8"]]
- 00b53fa4 bytes 00013fd6
+ 00b53fe8 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d48a59b3f0a869fcec4583f4a2442b0e"></a>

### [`00b53fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53fbc.md) → [`00b54000`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54000.md) _ZN8firebase13remote_config8internal19throttled_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b54040",
      "incomplete_value": true,
      "site": "00b54040",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53ffc",
      "incomplete_value": true,
      "site": "00b53ffc",
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
            "const:2f0:8"
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
      "definition_site": "00b5401c",
      "incomplete_value": true,
      "site": "00b5401c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53fd8",
      "incomplete_value": true,
      "site": "00b53fd8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b54024",
      "incomplete_value": false,
      "site": "00b54038",
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
            "const:f51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b53fe0",
      "incomplete_value": false,
      "site": "00b53ff4",
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
            "const:eb7:8"
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
      "00b54014",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54024",
      "PARAM",
      [
        "storage",
        "002a8eb7",
        null,
        "string"
      ]
    ],
    [
      "00b54040",
      "WRITE",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54014",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54024",
      "PARAM",
      [
        "storage",
        "002a8f51",
        null,
        "string"
      ]
    ],
    [
      "00b54040",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b53ff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53fbc.md#insn-00b53ff4) · [`00b53ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53fbc.md#insn-00b53ffc) · [`00b53fd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b53/00b53fbc.md#insn-00b53fd0)
- 新版 `00b54038`（命令位置の公開資料なし） · `00b54040`（命令位置の公開資料なし） · `00b54014`（命令位置の公開資料なし）

~~~diff
- 00b53ff4 ["INT_ADD", "register:40f0:8", ["const:b53ff4:8", "const:4:8"]]
- 00b53ff4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b54038 ["INT_ADD", "register:40f0:8", ["const:b54038:8", "const:4:8"]]
+ 00b54038 ["CALL", null, ["callee:00bde090:8"]]
- 00b53ff4 bytes 13280294
+ 00b54038 bytes 16280294
- 00b53ffc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f0:8"]]
- 00b53ffc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54040 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
+ 00b54040 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b53ffc bytes 807a01f9
+ 00b54040 bytes 809a01f9
- 00b53fd0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f0:8"]]
- 00b53fd0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b54014 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
+ 00b54014 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b53fd0 bytes 817a41f9
+ 00b54014 bytes 819a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a58ba69dd1cfd7f7a4d13c86faa885b2"></a>

### [`00b5402c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5402c.md) → [`00b54070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54070.md) _ZN8firebase13remote_config8internal19throttled_exception11GetMethodIdENS2_6MethodE

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
      "definition_site": "00b5408c",
      "incomplete_value": false,
      "site": "00b54090",
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
      "definition_site": "00b54048",
      "incomplete_value": false,
      "site": "00b5404c",
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
      "00b5408c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b5409c",
      "DATA",
      [
        "storage",
        "010a1300",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5408c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b5409c",
      "DATA",
      [
        "storage",
        "010a1340",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5404c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5402c.md#insn-00b5404c) · [`00b54048`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5402c.md#insn-00b54048) · [`00b54054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5402c.md#insn-00b54054)
- 新版 `00b54090`（命令位置の公開資料なし） · `00b5408c`（命令位置の公開資料なし） · `00b54098`（命令位置の公開資料なし）

~~~diff
- 00b5404c ["INT_ADD", "register:40f0:8", ["const:b5404c:8", "const:4:8"]]
- 00b5404c ["CALL", null, ["callee:00bde180:8"]]
+ 00b54090 ["INT_ADD", "register:40f0:8", ["const:b54090:8", "const:4:8"]]
+ 00b54090 ["CALL", null, ["callee:00bde180:8"]]
- 00b5404c bytes 39280294
+ 00b54090 bytes 3c280294
- 00b54048 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b54048 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b54048 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b54048 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5408c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b5408c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5408c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5408c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b54048 bytes 00501791
+ 00b5408c bytes 001c1591
- 00b54054 ["COPY", "tmp:0:8", ["const:300:8"]]
- 00b54054 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b54054 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b54054 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b54098 ["COPY", "tmp:0:8", ["const:340:8"]]
+ 00b54098 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54098 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54098 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b54054 bytes 08010c91
+ 00b54098 bytes 08010d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-931c147d894b855d2e4b983f4c99494c"></a>

### [`00b54068`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54068.md) → [`00b540ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b540ac.md) _ZN8firebase13remote_config8internal19throttled_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b540ec",
      "incomplete_value": true,
      "site": "00b540ec",
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
            "const:330:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b540a8",
      "incomplete_value": true,
      "site": "00b540a8",
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
            "const:2f0:8"
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
      "definition_site": "00b540c8",
      "incomplete_value": true,
      "site": "00b540c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54084",
      "incomplete_value": true,
      "site": "00b54084",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b540d0",
      "incomplete_value": false,
      "site": "00b540e4",
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
            "const:f51:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5408c",
      "incomplete_value": false,
      "site": "00b540a0",
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
            "const:eb7:8"
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
      "00b540c0",
      "READ",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b540d0",
      "PARAM",
      [
        "storage",
        "002a8eb7",
        null,
        "string"
      ]
    ],
    [
      "00b540ec",
      "WRITE",
      [
        "storage",
        "010a12f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b540c0",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b540d0",
      "PARAM",
      [
        "storage",
        "002a8f51",
        null,
        "string"
      ]
    ],
    [
      "00b540ec",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b540a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54068.md#insn-00b540a0) · [`00b540a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54068.md#insn-00b540a8) · [`00b5407c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54068.md#insn-00b5407c)
- 新版 `00b540e4`（命令位置の公開資料なし） · `00b540ec`（命令位置の公開資料なし） · `00b540c0`（命令位置の公開資料なし）

~~~diff
- 00b540a0 ["INT_ADD", "register:40f0:8", ["const:b540a0:8", "const:4:8"]]
- 00b540a0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b540e4 ["INT_ADD", "register:40f0:8", ["const:b540e4:8", "const:4:8"]]
+ 00b540e4 ["CALL", null, ["callee:00bde090:8"]]
- 00b540a0 bytes e8270294
+ 00b540e4 bytes eb270294
- 00b540a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f0:8"]]
- 00b540a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b540ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
+ 00b540ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b540a8 bytes 807a01f9
+ 00b540ec bytes 809a01f9
- 00b5407c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:2f0:8"]]
- 00b5407c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b540c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
+ 00b540c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5407c bytes 817a41f9
+ 00b540c0 bytes 819a41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-338c30ffa930b31db30ac90919529964"></a>

### [`00b540d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b540d8.md) → [`00b5411c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5411c.md) _ZN8firebase13remote_config8internal19throttled_exception10GetFieldIdENS2_5FieldE

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
      "definition_site": "00b54138",
      "incomplete_value": false,
      "site": "00b5413c",
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
      "definition_site": "00b540f4",
      "incomplete_value": false,
      "site": "00b540f8",
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
      "definition_site": "00b54148",
      "incomplete_value": true,
      "site": "00b54154",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b54104",
      "incomplete_value": true,
      "site": "00b54110",
      "value": [
        "LOAD",
        "8",
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
      "00b54138",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b54148",
      "DATA",
      [
        "storage",
        "010a1308",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54138",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b54148",
      "DATA",
      [
        "storage",
        "010a1348",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b540f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b540d8.md#insn-00b540f8) · [`00b540f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b540d8.md#insn-00b540f4) · [`00b54100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b540d8.md#insn-00b54100)
- 新版 `00b5413c`（命令位置の公開資料なし） · `00b54138`（命令位置の公開資料なし） · `00b54144`（命令位置の公開資料なし）

~~~diff
- 00b540f8 ["INT_ADD", "register:40f0:8", ["const:b540f8:8", "const:4:8"]]
- 00b540f8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5413c ["INT_ADD", "register:40f0:8", ["const:b5413c:8", "const:4:8"]]
+ 00b5413c ["CALL", null, ["callee:00bde180:8"]]
- 00b540f8 bytes 0e280294
+ 00b5413c bytes 11280294
- 00b540f4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b540f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b540f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b540f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b54138 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b54138 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b54138 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b54138 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b540f4 bytes 00fc1991
+ 00b54138 bytes 00c81791
- 00b54100 ["COPY", "tmp:0:8", ["const:308:8"]]
- 00b54100 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b54100 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b54100 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b54144 ["COPY", "tmp:0:8", ["const:348:8"]]
+ 00b54144 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54144 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54144 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b54100 bytes 08210c91
+ 00b54144 bytes 08210d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fd426cdc8b36729f2db1906a5580d10"></a>

### [`00b54114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54114.md) → [`00b54158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54158.md) _ZN8firebase13remote_config8internal26jni_config_update_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12E

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
      "definition_site": "00b54184",
      "incomplete_value": true,
      "site": "00b54184",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54140",
      "incomplete_value": true,
      "site": "00b54140",
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
            "const:310:8"
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
      "definition_site": "00b5416c",
      "incomplete_value": true,
      "site": "00b5416c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54128",
      "incomplete_value": true,
      "site": "00b54128",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b54178",
      "incomplete_value": false,
      "site": "00b5417c",
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
            "const:32d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54134",
      "incomplete_value": false,
      "site": "00b54138",
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
            "const:293:8"
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
      "00b54168",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54178",
      "PARAM",
      [
        "storage",
        "002a6293",
        null,
        "string"
      ]
    ],
    [
      "00b54184",
      "WRITE",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54168",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54178",
      "PARAM",
      [
        "storage",
        "002a632d",
        null,
        "string"
      ]
    ],
    [
      "00b54184",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54114.md#insn-00b54138) · [`00b54140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54114.md#insn-00b54140) · [`00b54124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54114.md#insn-00b54124)
- 新版 `00b5417c`（命令位置の公開資料なし） · `00b54184`（命令位置の公開資料なし） · `00b54168`（命令位置の公開資料なし）

~~~diff
- 00b54138 ["INT_ADD", "register:40f0:8", ["const:b54138:8", "const:4:8"]]
- 00b54138 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5417c ["INT_ADD", "register:40f0:8", ["const:b5417c:8", "const:4:8"]]
+ 00b5417c ["CALL", null, ["callee:00bde090:8"]]
- 00b54138 bytes c2270294
+ 00b5417c bytes c5270294
- 00b54140 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:310:8"]]
- 00b54140 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54184 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00b54184 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54140 bytes 608a01f9
+ 00b54184 bytes 60aa01f9
- 00b54124 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:310:8"]]
- 00b54124 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b54168 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00b54168 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b54124 bytes 688a41f9
+ 00b54168 bytes 68aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98b889c27d8c41ed9675ee36816ac701"></a>

### [`00b54154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54154.md) → [`00b54198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54198.md) _ZN8firebase13remote_config8internal26jni_config_update_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12E

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
      "definition_site": "00b541c4",
      "incomplete_value": true,
      "site": "00b541c4",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54180",
      "incomplete_value": true,
      "site": "00b54180",
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
            "const:310:8"
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
      "definition_site": "00b541ac",
      "incomplete_value": true,
      "site": "00b541ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54168",
      "incomplete_value": true,
      "site": "00b54168",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b541b4",
      "incomplete_value": false,
      "site": "00b541bc",
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
            "const:32d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54170",
      "incomplete_value": false,
      "site": "00b54178",
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
            "const:293:8"
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
      "00b541a8",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b541b4",
      "PARAM",
      [
        "storage",
        "002a6293",
        null,
        "string"
      ]
    ],
    [
      "00b541c4",
      "WRITE",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b541a8",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b541b4",
      "PARAM",
      [
        "storage",
        "002a632d",
        null,
        "string"
      ]
    ],
    [
      "00b541c4",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54154.md#insn-00b54178) · [`00b54180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54154.md#insn-00b54180) · [`00b54164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54154.md#insn-00b54164)
- 新版 `00b541bc`（命令位置の公開資料なし） · `00b541c4`（命令位置の公開資料なし） · `00b541a8`（命令位置の公開資料なし）

~~~diff
- 00b54178 ["INT_ADD", "register:40f0:8", ["const:b54178:8", "const:4:8"]]
- 00b54178 ["CALL", null, ["callee:00bde090:8"]]
+ 00b541bc ["INT_ADD", "register:40f0:8", ["const:b541bc:8", "const:4:8"]]
+ 00b541bc ["CALL", null, ["callee:00bde090:8"]]
- 00b54178 bytes b2270294
+ 00b541bc bytes b5270294
- 00b54180 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:310:8"]]
- 00b54180 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b541c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00b541c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54180 bytes 608a01f9
+ 00b541c4 bytes 60aa01f9
- 00b54164 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:310:8"]]
- 00b54164 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b541a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00b541a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b54164 bytes 688a41f9
+ 00b541a8 bytes 68aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-207dc4992b95ab69cdd232b97055a50b"></a>

### [`00b54194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54194.md) → [`00b541d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b541d8.md) _ZN8firebase13remote_config8internal26jni_config_update_listener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b54208",
      "incomplete_value": true,
      "site": "00b54208",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b541c4",
      "incomplete_value": true,
      "site": "00b541c4",
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
            "const:310:8"
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
      "definition_site": "00b541ec",
      "incomplete_value": true,
      "site": "00b541ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b541a8",
      "incomplete_value": true,
      "site": "00b541a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b541f8",
      "incomplete_value": true,
      "site": "00b54200",
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
            "const:32d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b541b4",
      "incomplete_value": true,
      "site": "00b541bc",
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
            "const:293:8"
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
      "00b541e8",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b541f8",
      "PARAM",
      [
        "storage",
        "002a6293",
        null,
        "string"
      ]
    ],
    [
      "00b54208",
      "WRITE",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b541e8",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b541f8",
      "PARAM",
      [
        "storage",
        "002a632d",
        null,
        "string"
      ]
    ],
    [
      "00b54208",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b541bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54194.md#insn-00b541bc) · [`00b541c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54194.md#insn-00b541c4) · [`00b541a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54194.md#insn-00b541a4)
- 新版 `00b54200`（命令位置の公開資料なし） · `00b54208`（命令位置の公開資料なし） · `00b541e8`（命令位置の公開資料なし）

~~~diff
- 00b541bc ["INT_ADD", "register:40f0:8", ["const:b541bc:8", "const:4:8"]]
- 00b541bc ["CALL", null, ["callee:00bde090:8"]]
+ 00b54200 ["INT_ADD", "register:40f0:8", ["const:b54200:8", "const:4:8"]]
+ 00b54200 ["CALL", null, ["callee:00bde090:8"]]
- 00b541bc bytes a1270294
+ 00b54200 bytes a4270294
- 00b541c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:310:8"]]
- 00b541c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54208 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00b54208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b541c4 bytes 608a01f9
+ 00b54208 bytes 60aa01f9
- 00b541a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:310:8"]]
- 00b541a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b541e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00b541e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b541a4 bytes 688a41f9
+ 00b541e8 bytes 68aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-739e2d7ca5cc6b8677e25c80099d4d71"></a>

### [`00b541d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b541d8.md) → [`00b5421c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5421c.md) _ZN8firebase13remote_config8internal26jni_config_update_listener10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b5424c",
      "incomplete_value": true,
      "site": "00b5424c",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54208",
      "incomplete_value": true,
      "site": "00b54208",
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
            "const:310:8"
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
      "definition_site": "00b54230",
      "incomplete_value": true,
      "site": "00b54230",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b541ec",
      "incomplete_value": true,
      "site": "00b541ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b54238",
      "incomplete_value": false,
      "site": "00b54244",
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
            "const:32d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b541f4",
      "incomplete_value": false,
      "site": "00b54200",
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
            "const:293:8"
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
      "00b5422c",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54238",
      "PARAM",
      [
        "storage",
        "002a6293",
        null,
        "string"
      ]
    ],
    [
      "00b5424c",
      "WRITE",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5422c",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54238",
      "PARAM",
      [
        "storage",
        "002a632d",
        null,
        "string"
      ]
    ],
    [
      "00b5424c",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b541d8.md#insn-00b54200) · [`00b54208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b541d8.md#insn-00b54208) · [`00b541e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b541d8.md#insn-00b541e8)
- 新版 `00b54244`（命令位置の公開資料なし） · `00b5424c`（命令位置の公開資料なし） · `00b5422c`（命令位置の公開資料なし）

~~~diff
- 00b54200 ["INT_ADD", "register:40f0:8", ["const:b54200:8", "const:4:8"]]
- 00b54200 ["CALL", null, ["callee:00bde090:8"]]
+ 00b54244 ["INT_ADD", "register:40f0:8", ["const:b54244:8", "const:4:8"]]
+ 00b54244 ["CALL", null, ["callee:00bde090:8"]]
- 00b54200 bytes 90270294
+ 00b54244 bytes 93270294
- 00b54208 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:310:8"]]
- 00b54208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5424c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00b5424c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54208 bytes 608a01f9
+ 00b5424c bytes 60aa01f9
- 00b541e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:310:8"]]
- 00b541e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5422c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
+ 00b5422c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b541e8 bytes 688a41f9
+ 00b5422c bytes 68aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-559a2f01243a84bffeea2e3508ed5071"></a>

### [`00b54228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54228.md) → [`00b5426c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5426c.md) _ZN8firebase13remote_config8internal26jni_config_update_listener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b542c4",
      "incomplete_value": true,
      "site": "00b542c4",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54280",
      "incomplete_value": true,
      "site": "00b54280",
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
            "const:318:8"
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
      "definition_site": "00b542a0",
      "incomplete_value": true,
      "site": "00b542ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5425c",
      "incomplete_value": true,
      "site": "00b54268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:310:8"
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
      "00b54280",
      "READ",
      [
        "storage",
        "010a1318",
        null,
        "undefined1"
      ]
    ],
    [
      "00b542a0",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b542c4",
      "WRITE",
      [
        "storage",
        "010a1318",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b54280",
      "READ",
      [
        "storage",
        "010a1358",
        null,
        "undefined1"
      ]
    ],
    [
      "00b542a0",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b542c4",
      "WRITE",
      [
        "storage",
        "010a1358",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5423c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54228.md#insn-00b5423c) · [`00b54268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54228.md#insn-00b54268) · [`00b54280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54228.md#insn-00b54280)
- 新版 `00b54280`（命令位置の公開資料なし） · `00b542ac`（命令位置の公開資料なし） · `00b542c4`（命令位置の公開資料なし）

~~~diff
- 00b5423c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:318:8"]]
- 00b5423c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b5423c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b54280 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:358:8"]]
+ 00b54280 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b54280 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b5423c bytes a8624c39
+ 00b54280 bytes a8624d39
- 00b54268 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54268 ["INT_ADD", "register:40f0:8", ["const:b54268:8", "const:4:8"]]
- 00b54268 ["CALLIND", null, ["register:0:8"]]
+ 00b542ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b542ac ["INT_ADD", "register:40f0:8", ["const:b542ac:8", "const:4:8"]]
+ 00b542ac ["CALLIND", null, ["register:0:8"]]
- 00b54268 bytes 00013fd6
+ 00b542ac bytes 00013fd6
- 00b54280 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b54280 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:318:8"]]
- 00b54280 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b542c4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b542c4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:358:8"]]
+ 00b542c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b54280 bytes a0620c39
+ 00b542c4 bytes a0620d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-855a96ea3a1a24953ac0c66baf993c78"></a>

### [`00b54294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54294.md) → [`00b542d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b542d8.md) _ZN8firebase13remote_config8internal26jni_config_update_listener12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 89.29% / 新版 89.29%

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
      "definition_site": "00b54314",
      "incomplete_value": true,
      "site": "00b54314",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b542d0",
      "incomplete_value": true,
      "site": "00b542d0",
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
            "const:318:8"
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
      "definition_site": "00b54334",
      "incomplete_value": true,
      "site": "00b54334",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b542f0",
      "incomplete_value": true,
      "site": "00b542f0",
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
            "const:310:8"
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
      "definition_site": "00b542f0",
      "incomplete_value": true,
      "site": "00b542f0",
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
      "definition_site": "00b542ac",
      "incomplete_value": true,
      "site": "00b542ac",
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
      "00b542ec",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b542f8",
      "READ",
      [
        "storage",
        "010a1318",
        null,
        "undefined1"
      ]
    ],
    [
      "00b54314",
      "WRITE",
      [
        "storage",
        "010a1318",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b542ec",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b542f8",
      "READ",
      [
        "storage",
        "010a1358",
        null,
        "undefined1"
      ]
    ],
    [
      "00b54314",
      "WRITE",
      [
        "storage",
        "010a1358",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b542d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54294.md#insn-00b542d0) · [`00b542f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54294.md#insn-00b542f0) · [`00b542a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54294.md#insn-00b542a8)
- 新版 `00b54314`（命令位置の公開資料なし） · `00b54334`（命令位置の公開資料なし） · `00b542ec`（命令位置の公開資料なし）

~~~diff
- 00b542d0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b542d0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b542d0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:318:8"]]
- 00b542d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b54314 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b54314 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b54314 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:358:8"]]
+ 00b54314 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b542d0 bytes bf620c39
+ 00b54314 bytes bf620d39
- 00b542f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:310:8"]]
- 00b542f0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b542f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b54334 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00b54334 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b54334 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b542f0 bytes 9f8a01f9
+ 00b54334 bytes 9faa01f9
- 00b542a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:310:8"]]
- 00b542a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b542ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00b542ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b542a8 bytes 818a41f9
+ 00b542ec bytes 81aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5971e5c63fc3fb2c7897b81f47ad6f74"></a>

### [`00b54304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54304.md) → [`00b54348`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54348.md) _ZN8firebase13remote_config8internal26jni_config_update_listener14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b54388",
      "incomplete_value": true,
      "site": "00b54388",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54344",
      "incomplete_value": true,
      "site": "00b54344",
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
            "const:310:8"
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
      "definition_site": "00b54364",
      "incomplete_value": true,
      "site": "00b54364",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54320",
      "incomplete_value": true,
      "site": "00b54320",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b5436c",
      "incomplete_value": false,
      "site": "00b54380",
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
            "const:32d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54328",
      "incomplete_value": false,
      "site": "00b5433c",
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
            "const:293:8"
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
      "00b5435c",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5436c",
      "PARAM",
      [
        "storage",
        "002a6293",
        null,
        "string"
      ]
    ],
    [
      "00b54388",
      "WRITE",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5435c",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5436c",
      "PARAM",
      [
        "storage",
        "002a632d",
        null,
        "string"
      ]
    ],
    [
      "00b54388",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5433c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54304.md#insn-00b5433c) · [`00b54344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54304.md#insn-00b54344) · [`00b54318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54304.md#insn-00b54318)
- 新版 `00b54380`（命令位置の公開資料なし） · `00b54388`（命令位置の公開資料なし） · `00b5435c`（命令位置の公開資料なし）

~~~diff
- 00b5433c ["INT_ADD", "register:40f0:8", ["const:b5433c:8", "const:4:8"]]
- 00b5433c ["CALL", null, ["callee:00bde090:8"]]
+ 00b54380 ["INT_ADD", "register:40f0:8", ["const:b54380:8", "const:4:8"]]
+ 00b54380 ["CALL", null, ["callee:00bde090:8"]]
- 00b5433c bytes 41270294
+ 00b54380 bytes 44270294
- 00b54344 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:310:8"]]
- 00b54344 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54388 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00b54388 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54344 bytes 808a01f9
+ 00b54388 bytes 80aa01f9
- 00b54318 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:310:8"]]
- 00b54318 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5435c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00b5435c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b54318 bytes 818a41f9
+ 00b5435c bytes 81aa41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cafc21999c147cf80cc075e7ecc8245a"></a>

### [`00b54374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54374.md) → [`00b543b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b543b8.md) _ZN8firebase13remote_config8internal26jni_config_update_listener11GetMethodIdENS2_6MethodE

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
      "definition_site": "00b543d4",
      "incomplete_value": false,
      "site": "00b543d8",
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
      "definition_site": "00b54390",
      "incomplete_value": false,
      "site": "00b54394",
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
      "definition_site": "00b543e4",
      "incomplete_value": true,
      "site": "00b543f0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b543a0",
      "incomplete_value": true,
      "site": "00b543ac",
      "value": [
        "LOAD",
        "8",
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
      "00b543d4",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b543e4",
      "DATA",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b543d4",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b543e4",
      "DATA",
      [
        "storage",
        "010a1360",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54374.md#insn-00b54394) · [`00b54390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54374.md#insn-00b54390) · [`00b5439c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54374.md#insn-00b5439c)
- 新版 `00b543d8`（命令位置の公開資料なし） · `00b543d4`（命令位置の公開資料なし） · `00b543e0`（命令位置の公開資料なし）

~~~diff
- 00b54394 ["INT_ADD", "register:40f0:8", ["const:b54394:8", "const:4:8"]]
- 00b54394 ["CALL", null, ["callee:00bde180:8"]]
+ 00b543d8 ["INT_ADD", "register:40f0:8", ["const:b543d8:8", "const:4:8"]]
+ 00b543d8 ["CALL", null, ["callee:00bde180:8"]]
- 00b54394 bytes 67270294
+ 00b543d8 bytes 6a270294
- 00b54390 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b54390 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b54390 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b54390 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b543d4 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b543d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b543d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b543d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b54390 bytes 00501791
+ 00b543d4 bytes 001c1591
- 00b5439c ["COPY", "tmp:0:8", ["const:320:8"]]
- 00b5439c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5439c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5439c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b543e0 ["COPY", "tmp:0:8", ["const:360:8"]]
+ 00b543e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b543e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b543e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5439c bytes 08810c91
+ 00b543e0 bytes 08810d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c045581871706d2ed0150a1a41b0c69"></a>

### [`00b543b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b543b0.md) → [`00b543f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b543f4.md) _ZN8firebase13remote_config8internal26jni_config_update_listener13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b54434",
      "incomplete_value": true,
      "site": "00b54434",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b543f0",
      "incomplete_value": true,
      "site": "00b543f0",
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
            "const:310:8"
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
      "definition_site": "00b54410",
      "incomplete_value": true,
      "site": "00b54410",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b543cc",
      "incomplete_value": true,
      "site": "00b543cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
        "00b543cc"
      ],
      [
        "FALL_THROUGH",
        "00b54410"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b54410",
      "incomplete_value": true,
      "site": "00b54434",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b543cc",
      "incomplete_value": true,
      "site": "00b543f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b54408",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54418",
      "PARAM",
      [
        "storage",
        "002a6293",
        null,
        "string"
      ]
    ],
    [
      "00b54434",
      "WRITE",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54408",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54418",
      "PARAM",
      [
        "storage",
        "002a632d",
        null,
        "string"
      ]
    ],
    [
      "00b54434",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b543f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b543b0.md#insn-00b543f0) · [`00b543c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b543b0.md#insn-00b543c4) · [`00b543d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b543b0.md#insn-00b543d4)
- 新版 `00b54434`（命令位置の公開資料なし） · `00b54408`（命令位置の公開資料なし） · `00b54418`（命令位置の公開資料なし）

~~~diff
- 00b543f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:310:8"]]
- 00b543f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54434 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00b54434 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b543f0 bytes 808a01f9
+ 00b54434 bytes 80aa01f9
- 00b543c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:310:8"]]
- 00b543c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b54408 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00b54408 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b543c4 bytes 818a41f9
+ 00b54408 bytes 81aa41f9
- 00b543d4 ["COPY", "tmp:0:8", ["const:293:8"]]
- 00b543d4 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b543d4 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b543d4 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b54418 ["COPY", "tmp:0:8", ["const:32d:8"]]
+ 00b54418 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b54418 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b54418 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b543d4 bytes 634c0a91
+ 00b54418 bytes 63b40c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c4d7bd53bc7a13eb379e2d1924a54de2"></a>

### [`00b54420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54420.md) → [`00b54464`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54464.md) _ZN8firebase13remote_config8internal26jni_config_update_listener10GetFieldIdENS2_5FieldE

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
      "definition_site": "00b54480",
      "incomplete_value": false,
      "site": "00b54484",
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
      "definition_site": "00b5443c",
      "incomplete_value": false,
      "site": "00b54440",
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
      "definition_site": "00b54490",
      "incomplete_value": true,
      "site": "00b5449c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5444c",
      "incomplete_value": true,
      "site": "00b54458",
      "value": [
        "LOAD",
        "8",
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
      "00b54480",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b54490",
      "DATA",
      [
        "storage",
        "010a1328",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54480",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b54490",
      "DATA",
      [
        "storage",
        "010a1368",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54420.md#insn-00b54440) · [`00b5443c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54420.md#insn-00b5443c) · [`00b54448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54420.md#insn-00b54448)
- 新版 `00b54484`（命令位置の公開資料なし） · `00b54480`（命令位置の公開資料なし） · `00b5448c`（命令位置の公開資料なし）

~~~diff
- 00b54440 ["INT_ADD", "register:40f0:8", ["const:b54440:8", "const:4:8"]]
- 00b54440 ["CALL", null, ["callee:00bde180:8"]]
+ 00b54484 ["INT_ADD", "register:40f0:8", ["const:b54484:8", "const:4:8"]]
+ 00b54484 ["CALL", null, ["callee:00bde180:8"]]
- 00b54440 bytes 3c270294
+ 00b54484 bytes 3f270294
- 00b5443c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b5443c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5443c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5443c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b54480 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b54480 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b54480 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b54480 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5443c bytes 00fc1991
+ 00b54480 bytes 00c81791
- 00b54448 ["COPY", "tmp:0:8", ["const:328:8"]]
- 00b54448 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b54448 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b54448 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5448c ["COPY", "tmp:0:8", ["const:368:8"]]
+ 00b5448c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5448c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5448c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b54448 bytes 08a10c91
+ 00b5448c bytes 08a10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cd2a0a38d72604786a1f6f4423ebfb1"></a>

### [`00b5445c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5445c.md) → [`00b544a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b544a0.md) _ZN8firebase13remote_config8internal13config_update19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

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
      "definition_site": "00b544cc",
      "incomplete_value": true,
      "site": "00b544cc",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54488",
      "incomplete_value": true,
      "site": "00b54488",
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
            "const:330:8"
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
      "00b544b0",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b544cc",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b544b0",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "00b544cc",
      "WRITE",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5445c.md#insn-00b54488) · [`00b5446c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5445c.md#insn-00b5446c) · [`00b54480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5445c.md#insn-00b54480)
- 新版 `00b544cc`（命令位置の公開資料なし） · `00b544b0`（命令位置の公開資料なし） · `00b544c4`（命令位置の公開資料なし）

~~~diff
- 00b54488 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
- 00b54488 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b544cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:370:8"]]
+ 00b544cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54488 bytes 609a01f9
+ 00b544cc bytes 60ba01f9
- 00b5446c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
- 00b5446c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b544b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:370:8"]]
+ 00b544b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5446c bytes 689a41f9
+ 00b544b0 bytes 68ba41f9
- 00b54480 ["INT_ADD", "register:40f0:8", ["const:b54480:8", "const:4:8"]]
- 00b54480 ["CALL", null, ["callee:00bde090:8"]]
+ 00b544c4 ["INT_ADD", "register:40f0:8", ["const:b544c4:8", "const:4:8"]]
+ 00b544c4 ["CALL", null, ["callee:00bde090:8"]]
- 00b54480 bytes f0260294
+ 00b544c4 bytes f3260294
~~~


<a id="compare-3729f5fe4277de81a9248569e0fb6ab2"></a>

### [`00b5449c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5449c.md) → [`00b544e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b544e0.md) _ZN8firebase13remote_config8internal13config_update19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileEN

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
      "definition_site": "00b5450c",
      "incomplete_value": true,
      "site": "00b5450c",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b544c8",
      "incomplete_value": true,
      "site": "00b544c8",
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
            "const:330:8"
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
      "definition_site": "00b544f4",
      "incomplete_value": true,
      "site": "00b544f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b544b0",
      "incomplete_value": true,
      "site": "00b544b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
        "00b544b0"
      ],
      [
        "FALL_THROUGH",
        "00b544f4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b544f4",
      "incomplete_value": true,
      "site": "00b5450c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b544b0",
      "incomplete_value": true,
      "site": "00b544c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b544f0",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5450c",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b544f0",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5450c",
      "WRITE",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b544c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5449c.md#insn-00b544c8) · [`00b544ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5449c.md#insn-00b544ac) · [`00b544c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5449c.md#insn-00b544c0)
- 新版 `00b5450c`（命令位置の公開資料なし） · `00b544f0`（命令位置の公開資料なし） · `00b54504`（命令位置の公開資料なし）

~~~diff
- 00b544c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
- 00b544c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5450c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:370:8"]]
+ 00b5450c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b544c8 bytes 609a01f9
+ 00b5450c bytes 60ba01f9
- 00b544ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
- 00b544ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b544f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:370:8"]]
+ 00b544f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b544ac bytes 689a41f9
+ 00b544f0 bytes 68ba41f9
- 00b544c0 ["INT_ADD", "register:40f0:8", ["const:b544c0:8", "const:4:8"]]
- 00b544c0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b54504 ["INT_ADD", "register:40f0:8", ["const:b54504:8", "const:4:8"]]
+ 00b54504 ["CALL", null, ["callee:00bde090:8"]]
- 00b544c0 bytes e0260294
+ 00b54504 bytes e3260294
~~~


<a id="compare-ff4febacd63b0cc437ec9fb725a8bd6f"></a>

### [`00b544dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b544dc.md) → [`00b54520`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54520.md) _ZN8firebase13remote_config8internal13config_update10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b54550",
      "incomplete_value": true,
      "site": "00b54550",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5450c",
      "incomplete_value": true,
      "site": "00b5450c",
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
            "const:330:8"
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
      "definition_site": "00b54534",
      "incomplete_value": true,
      "site": "00b54534",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b544f0",
      "incomplete_value": true,
      "site": "00b544f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
        "00b544f0"
      ],
      [
        "FALL_THROUGH",
        "00b54534"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b54534",
      "incomplete_value": true,
      "site": "00b54550",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b544f0",
      "incomplete_value": true,
      "site": "00b5450c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b54530",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54550",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54530",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54550",
      "WRITE",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5450c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b544dc.md#insn-00b5450c) · [`00b544ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b544dc.md#insn-00b544ec) · [`00b54504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b544dc.md#insn-00b54504)
- 新版 `00b54550`（命令位置の公開資料なし） · `00b54530`（命令位置の公開資料なし） · `00b54548`（命令位置の公開資料なし）

~~~diff
- 00b5450c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
- 00b5450c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54550 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:370:8"]]
+ 00b54550 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5450c bytes 609a01f9
+ 00b54550 bytes 60ba01f9
- 00b544ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
- 00b544ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b54530 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:370:8"]]
+ 00b54530 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b544ec bytes 689a41f9
+ 00b54530 bytes 68ba41f9
- 00b54504 ["INT_ADD", "register:40f0:8", ["const:b54504:8", "const:4:8"]]
- 00b54504 ["CALL", null, ["callee:00bde090:8"]]
+ 00b54548 ["INT_ADD", "register:40f0:8", ["const:b54548:8", "const:4:8"]]
+ 00b54548 ["CALL", null, ["callee:00bde090:8"]]
- 00b54504 bytes cf260294
+ 00b54548 bytes d2260294
~~~


<a id="compare-d0cb6d19b2aec7f827d23dc853e36ed0"></a>

### [`00b54520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54520.md) → [`00b54564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54564.md) _ZN8firebase13remote_config8internal13config_update10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b54594",
      "incomplete_value": true,
      "site": "00b54594",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54550",
      "incomplete_value": true,
      "site": "00b54550",
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
            "const:330:8"
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
      "definition_site": "00b54578",
      "incomplete_value": true,
      "site": "00b54578",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54534",
      "incomplete_value": true,
      "site": "00b54534",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
        "00b54534"
      ],
      [
        "FALL_THROUGH",
        "00b54578"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b54578",
      "incomplete_value": true,
      "site": "00b54594",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54534",
      "incomplete_value": true,
      "site": "00b54550",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b54574",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54594",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54574",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54594",
      "WRITE",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54520.md#insn-00b54550) · [`00b54530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54520.md#insn-00b54530) · [`00b54548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54520.md#insn-00b54548)
- 新版 `00b54594`（命令位置の公開資料なし） · `00b54574`（命令位置の公開資料なし） · `00b5458c`（命令位置の公開資料なし）

~~~diff
- 00b54550 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
- 00b54550 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54594 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:370:8"]]
+ 00b54594 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54550 bytes 609a01f9
+ 00b54594 bytes 60ba01f9
- 00b54530 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:330:8"]]
- 00b54530 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b54574 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:370:8"]]
+ 00b54574 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b54530 bytes 689a41f9
+ 00b54574 bytes 68ba41f9
- 00b54548 ["INT_ADD", "register:40f0:8", ["const:b54548:8", "const:4:8"]]
- 00b54548 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5458c ["INT_ADD", "register:40f0:8", ["const:b5458c:8", "const:4:8"]]
+ 00b5458c ["CALL", null, ["callee:00bde090:8"]]
- 00b54548 bytes be260294
+ 00b5458c bytes c1260294
~~~


<a id="compare-6466e37a57f1eee095e4d52d1d28c952"></a>

### [`00b54570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54570.md) → [`00b545b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b545b4.md) _ZN8firebase13remote_config8internal13config_update15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b5460c",
      "incomplete_value": true,
      "site": "00b5460c",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b545c8",
      "incomplete_value": true,
      "site": "00b545c8",
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
            "const:338:8"
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
      "definition_site": "00b545e8",
      "incomplete_value": true,
      "site": "00b545f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:370:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b545a4",
      "incomplete_value": true,
      "site": "00b545b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:330:8"
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
      "00b545c8",
      "READ",
      [
        "storage",
        "010a1338",
        null,
        "undefined1"
      ]
    ],
    [
      "00b545e8",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5460c",
      "WRITE",
      [
        "storage",
        "010a1338",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b545c8",
      "READ",
      [
        "storage",
        "010a1378",
        null,
        "undefined1"
      ]
    ],
    [
      "00b545e8",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5460c",
      "WRITE",
      [
        "storage",
        "010a1378",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54570.md#insn-00b54584) · [`00b545b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54570.md#insn-00b545b0) · [`00b545c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54570.md#insn-00b545c8)
- 新版 `00b545c8`（命令位置の公開資料なし） · `00b545f4`（命令位置の公開資料なし） · `00b5460c`（命令位置の公開資料なし）

~~~diff
- 00b54584 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:338:8"]]
- 00b54584 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b54584 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b545c8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:378:8"]]
+ 00b545c8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b545c8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b54584 bytes a8e24c39
+ 00b545c8 bytes a8e24d39
- 00b545b0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b545b0 ["INT_ADD", "register:40f0:8", ["const:b545b0:8", "const:4:8"]]
- 00b545b0 ["CALLIND", null, ["register:0:8"]]
+ 00b545f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b545f4 ["INT_ADD", "register:40f0:8", ["const:b545f4:8", "const:4:8"]]
+ 00b545f4 ["CALLIND", null, ["register:0:8"]]
- 00b545b0 bytes 00013fd6
+ 00b545f4 bytes 00013fd6
- 00b545c8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b545c8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:338:8"]]
- 00b545c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b5460c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b5460c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:378:8"]]
+ 00b5460c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b545c8 bytes a0e20c39
+ 00b5460c bytes a0e20d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-534ddbe5be45347118db6559daa77a03"></a>

### [`00b545dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b545dc.md) → [`00b54620`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54620.md) _ZN8firebase13remote_config8internal13config_update12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b5465c",
      "incomplete_value": true,
      "site": "00b5465c",
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
            "const:378:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54618",
      "incomplete_value": true,
      "site": "00b54618",
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
            "const:338:8"
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
      "definition_site": "00b5467c",
      "incomplete_value": true,
      "site": "00b5467c",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54638",
      "incomplete_value": true,
      "site": "00b54638",
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
            "const:330:8"
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
      "definition_site": "00b54638",
      "incomplete_value": true,
      "site": "00b54638",
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
      "definition_site": "00b545f4",
      "incomplete_value": true,
      "site": "00b545f4",
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
      "00b54634",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54640",
      "READ",
      [
        "storage",
        "010a1338",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5465c",
      "WRITE",
      [
        "storage",
        "010a1338",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b54634",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54640",
      "READ",
      [
        "storage",
        "010a1378",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5465c",
      "WRITE",
      [
        "storage",
        "010a1378",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b545f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b545dc.md#insn-00b545f0) · [`00b54618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b545dc.md#insn-00b54618) · [`00b54634`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b545dc.md#insn-00b54634)
- 新版 `00b54634`（命令位置の公開資料なし） · `00b5465c`（命令位置の公開資料なし） · `00b54678`（命令位置の公開資料なし）

~~~diff
- 00b545f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
- 00b545f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b54634 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:370:8"]]
+ 00b54634 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b545f0 bytes 819a41f9
+ 00b54634 bytes 81ba41f9
- 00b54618 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b54618 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b54618 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:338:8"]]
- 00b54618 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b5465c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b5465c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b5465c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:378:8"]]
+ 00b5465c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b54618 bytes bfe20c39
+ 00b5465c bytes bfe20d39
- 00b54634 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b54634 ["INT_ADD", "register:40f0:8", ["const:b54634:8", "const:4:8"]]
- 00b54634 ["CALLIND", null, ["register:0:8"]]
+ 00b54678 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b54678 ["INT_ADD", "register:40f0:8", ["const:b54678:8", "const:4:8"]]
+ 00b54678 ["CALLIND", null, ["register:0:8"]]
- 00b54634 bytes 00013fd6
+ 00b54678 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5dc260a116347565760e0954661881b7"></a>

### [`00b5464c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5464c.md) → [`00b54690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54690.md) _ZN8firebase13remote_config8internal13config_update14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b546d0",
      "incomplete_value": true,
      "site": "00b546d0",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5468c",
      "incomplete_value": true,
      "site": "00b5468c",
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
            "const:330:8"
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
      "definition_site": "00b546ac",
      "incomplete_value": true,
      "site": "00b546ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54668",
      "incomplete_value": true,
      "site": "00b54668",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
        "00b54668"
      ],
      [
        "FALL_THROUGH",
        "00b546ac"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b546ac",
      "incomplete_value": true,
      "site": "00b546d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54668",
      "incomplete_value": true,
      "site": "00b5468c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b546a4",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b546d0",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b546e4",
      "PARAM",
      [
        "storage",
        "00c119c0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b546a4",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "00b546d0",
      "WRITE",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "00b546e4",
      "PARAM",
      [
        "storage",
        "00c11a10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5468c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5464c.md#insn-00b5468c) · [`00b54660`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5464c.md#insn-00b54660) · [`00b54684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b5464c.md#insn-00b54684)
- 新版 `00b546d0`（命令位置の公開資料なし） · `00b546a4`（命令位置の公開資料なし） · `00b546c8`（命令位置の公開資料なし）

~~~diff
- 00b5468c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
- 00b5468c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b546d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:370:8"]]
+ 00b546d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5468c bytes 809a01f9
+ 00b546d0 bytes 80ba01f9
- 00b54660 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
- 00b54660 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b546a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:370:8"]]
+ 00b546a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b54660 bytes 819a41f9
+ 00b546a4 bytes 81ba41f9
- 00b54684 ["INT_ADD", "register:40f0:8", ["const:b54684:8", "const:4:8"]]
- 00b54684 ["CALL", null, ["callee:00bde090:8"]]
+ 00b546c8 ["INT_ADD", "register:40f0:8", ["const:b546c8:8", "const:4:8"]]
+ 00b546c8 ["CALL", null, ["callee:00bde090:8"]]
- 00b54684 bytes 6f260294
+ 00b546c8 bytes 72260294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52499963be100c420b29d36405107189"></a>

### [`00b546bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b546bc.md) → [`00b54700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54700.md) _ZN8firebase13remote_config8internal13config_update11GetMethodIdENS2_6MethodE

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
      "definition_site": "00b5471c",
      "incomplete_value": false,
      "site": "00b54720",
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
      "definition_site": "00b546d8",
      "incomplete_value": false,
      "site": "00b546dc",
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
      "definition_site": "00b5472c",
      "incomplete_value": true,
      "site": "00b54738",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b546e8",
      "incomplete_value": true,
      "site": "00b546f4",
      "value": [
        "LOAD",
        "8",
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
      "00b5471c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b5472c",
      "DATA",
      [
        "storage",
        "010a1340",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5471c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b5472c",
      "DATA",
      [
        "storage",
        "010a1380",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b546dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b546bc.md#insn-00b546dc) · [`00b546d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b546bc.md#insn-00b546d8) · [`00b546e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b546bc.md#insn-00b546e4)
- 新版 `00b54720`（命令位置の公開資料なし） · `00b5471c`（命令位置の公開資料なし） · `00b54728`（命令位置の公開資料なし）

~~~diff
- 00b546dc ["INT_ADD", "register:40f0:8", ["const:b546dc:8", "const:4:8"]]
- 00b546dc ["CALL", null, ["callee:00bde180:8"]]
+ 00b54720 ["INT_ADD", "register:40f0:8", ["const:b54720:8", "const:4:8"]]
+ 00b54720 ["CALL", null, ["callee:00bde180:8"]]
- 00b546dc bytes 95260294
+ 00b54720 bytes 98260294
- 00b546d8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b546d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b546d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b546d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5471c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b5471c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5471c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5471c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b546d8 bytes 00501791
+ 00b5471c bytes 001c1591
- 00b546e4 ["COPY", "tmp:0:8", ["const:340:8"]]
- 00b546e4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b546e4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b546e4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b54728 ["COPY", "tmp:0:8", ["const:380:8"]]
+ 00b54728 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54728 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54728 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b546e4 bytes 08010d91
+ 00b54728 bytes 08010e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c54bf7de31c4a5d20e9c313428fd271e"></a>

### [`00b546f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b546f8.md) → [`00b5473c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b5473c.md) _ZN8firebase13remote_config8internal13config_update13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b5477c",
      "incomplete_value": true,
      "site": "00b5477c",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54738",
      "incomplete_value": true,
      "site": "00b54738",
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
            "const:330:8"
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
      "definition_site": "00b54758",
      "incomplete_value": true,
      "site": "00b54758",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54714",
      "incomplete_value": true,
      "site": "00b54714",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
        "00b54714"
      ],
      [
        "FALL_THROUGH",
        "00b54758"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b54758",
      "incomplete_value": true,
      "site": "00b5477c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54714",
      "incomplete_value": true,
      "site": "00b54738",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b54750",
      "READ",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5477c",
      "WRITE",
      [
        "storage",
        "010a1330",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54794",
      "PARAM",
      [
        "storage",
        "010a1348",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54750",
      "READ",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5477c",
      "WRITE",
      [
        "storage",
        "010a1370",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54794",
      "PARAM",
      [
        "storage",
        "010a1388",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b546f8.md#insn-00b54738) · [`00b5470c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b546f8.md#insn-00b5470c) · [`00b54730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b546f8.md#insn-00b54730)
- 新版 `00b5477c`（命令位置の公開資料なし） · `00b54750`（命令位置の公開資料なし） · `00b54774`（命令位置の公開資料なし）

~~~diff
- 00b54738 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
- 00b54738 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5477c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:370:8"]]
+ 00b5477c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54738 bytes 809a01f9
+ 00b5477c bytes 80ba01f9
- 00b5470c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:330:8"]]
- 00b5470c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b54750 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:370:8"]]
+ 00b54750 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5470c bytes 819a41f9
+ 00b54750 bytes 81ba41f9
- 00b54730 ["INT_ADD", "register:40f0:8", ["const:b54730:8", "const:4:8"]]
- 00b54730 ["CALL", null, ["callee:00bde090:8"]]
+ 00b54774 ["INT_ADD", "register:40f0:8", ["const:b54774:8", "const:4:8"]]
+ 00b54774 ["CALL", null, ["callee:00bde090:8"]]
- 00b54730 bytes 44260294
+ 00b54774 bytes 47260294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d8044008a71b437c96f0d4646fab24de"></a>

### [`00b54768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54768.md) → [`00b547ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b547ac.md) _ZN8firebase13remote_config8internal13config_update10GetFieldIdENS2_5FieldE

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
      "definition_site": "00b547c8",
      "incomplete_value": false,
      "site": "00b547cc",
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
      "definition_site": "00b54784",
      "incomplete_value": false,
      "site": "00b54788",
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
      "definition_site": "00b547d8",
      "incomplete_value": true,
      "site": "00b547e4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b54794",
      "incomplete_value": true,
      "site": "00b547a0",
      "value": [
        "LOAD",
        "8",
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
      "00b547c8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b547d8",
      "DATA",
      [
        "storage",
        "010a1348",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b547c8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b547d8",
      "DATA",
      [
        "storage",
        "010a1388",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54768.md#insn-00b54788) · [`00b54784`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54768.md#insn-00b54784) · [`00b54790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54768.md#insn-00b54790)
- 新版 `00b547cc`（命令位置の公開資料なし） · `00b547c8`（命令位置の公開資料なし） · `00b547d4`（命令位置の公開資料なし）

~~~diff
- 00b54788 ["INT_ADD", "register:40f0:8", ["const:b54788:8", "const:4:8"]]
- 00b54788 ["CALL", null, ["callee:00bde180:8"]]
+ 00b547cc ["INT_ADD", "register:40f0:8", ["const:b547cc:8", "const:4:8"]]
+ 00b547cc ["CALL", null, ["callee:00bde180:8"]]
- 00b54788 bytes 6a260294
+ 00b547cc bytes 6d260294
- 00b54784 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b54784 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b54784 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b54784 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b547c8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b547c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b547c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b547c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b54784 bytes 00fc1991
+ 00b547c8 bytes 00c81791
- 00b54790 ["COPY", "tmp:0:8", ["const:348:8"]]
- 00b54790 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b54790 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b54790 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b547d4 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 00b547d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b547d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b547d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b54790 bytes 08210d91
+ 00b547d4 bytes 08210e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bee183968d900dfcca5fb80d907cac93"></a>

### [`00b547a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b547a4.md) → [`00b547e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b547e8.md) _ZN8firebase13remote_config8internal35config_update_listener_registration19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8in

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
      "definition_site": "00b54814",
      "incomplete_value": true,
      "site": "00b54814",
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
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b547d0",
      "incomplete_value": true,
      "site": "00b547d0",
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
            "const:350:8"
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
      "definition_site": "00b547fc",
      "incomplete_value": true,
      "site": "00b547fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b547b8",
      "incomplete_value": true,
      "site": "00b547b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b54808",
      "incomplete_value": false,
      "site": "00b5480c",
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
            "const:889:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b547c4",
      "incomplete_value": false,
      "site": "00b547c8",
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
            "const:916:8"
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
      "00b547f8",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54808",
      "PARAM",
      [
        "storage",
        "00299916",
        null,
        "string"
      ]
    ],
    [
      "00b54814",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b547f8",
      "READ",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54808",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ],
    [
      "00b54814",
      "WRITE",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b547c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b547a4.md#insn-00b547c8) · [`00b547d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b547a4.md#insn-00b547d0) · [`00b547b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b547a4.md#insn-00b547b4)
- 新版 `00b5480c`（命令位置の公開資料なし） · `00b54814`（命令位置の公開資料なし） · `00b547f8`（命令位置の公開資料なし）

~~~diff
- 00b547c8 ["INT_ADD", "register:40f0:8", ["const:b547c8:8", "const:4:8"]]
- 00b547c8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5480c ["INT_ADD", "register:40f0:8", ["const:b5480c:8", "const:4:8"]]
+ 00b5480c ["CALL", null, ["callee:00bde090:8"]]
- 00b547c8 bytes 1e260294
+ 00b5480c bytes 21260294
- 00b547d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00b547d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54814 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00b54814 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b547d0 bytes 60aa01f9
+ 00b54814 bytes 60ca01f9
- 00b547b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00b547b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b547f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00b547f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b547b4 bytes 68aa41f9
+ 00b547f8 bytes 68ca41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ef70acb00c49c8f0a87dc5736d56ced"></a>

### [`00b547e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b547e4.md) → [`00b54828`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54828.md) _ZN8firebase13remote_config8internal35config_update_listener_registration19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8in

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
      "definition_site": "00b54854",
      "incomplete_value": true,
      "site": "00b54854",
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
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54810",
      "incomplete_value": true,
      "site": "00b54810",
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
            "const:350:8"
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
      "definition_site": "00b5483c",
      "incomplete_value": true,
      "site": "00b5483c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b547f8",
      "incomplete_value": true,
      "site": "00b547f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b54844",
      "incomplete_value": false,
      "site": "00b5484c",
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
            "const:889:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54800",
      "incomplete_value": false,
      "site": "00b54808",
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
            "const:916:8"
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
      "00b54838",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54844",
      "PARAM",
      [
        "storage",
        "00299916",
        null,
        "string"
      ]
    ],
    [
      "00b54854",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54838",
      "READ",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54844",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ],
    [
      "00b54854",
      "WRITE",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b547e4.md#insn-00b54808) · [`00b54810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b547e4.md#insn-00b54810) · [`00b547f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b547e4.md#insn-00b547f4)
- 新版 `00b5484c`（命令位置の公開資料なし） · `00b54854`（命令位置の公開資料なし） · `00b54838`（命令位置の公開資料なし）

~~~diff
- 00b54808 ["INT_ADD", "register:40f0:8", ["const:b54808:8", "const:4:8"]]
- 00b54808 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5484c ["INT_ADD", "register:40f0:8", ["const:b5484c:8", "const:4:8"]]
+ 00b5484c ["CALL", null, ["callee:00bde090:8"]]
- 00b54808 bytes 0e260294
+ 00b5484c bytes 11260294
- 00b54810 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00b54810 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54854 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00b54854 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54810 bytes 60aa01f9
+ 00b54854 bytes 60ca01f9
- 00b547f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00b547f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b54838 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00b54838 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b547f4 bytes 68aa41f9
+ 00b54838 bytes 68ca41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-337c4e3a735013d41cb6ba21b7151f65"></a>

### [`00b54824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54824.md) → [`00b54868`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54868.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b54898",
      "incomplete_value": true,
      "site": "00b54898",
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
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54854",
      "incomplete_value": true,
      "site": "00b54854",
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
            "const:350:8"
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
      "definition_site": "00b5487c",
      "incomplete_value": true,
      "site": "00b5487c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54838",
      "incomplete_value": true,
      "site": "00b54838",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b54888",
      "incomplete_value": false,
      "site": "00b54890",
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
            "const:889:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54844",
      "incomplete_value": false,
      "site": "00b5484c",
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
            "const:916:8"
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
      "00b54878",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54888",
      "PARAM",
      [
        "storage",
        "00299916",
        null,
        "string"
      ]
    ],
    [
      "00b54898",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54878",
      "READ",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54888",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ],
    [
      "00b54898",
      "WRITE",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5484c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54824.md#insn-00b5484c) · [`00b54854`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54824.md#insn-00b54854) · [`00b54834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54824.md#insn-00b54834)
- 新版 `00b54890`（命令位置の公開資料なし） · `00b54898`（命令位置の公開資料なし） · `00b54878`（命令位置の公開資料なし）

~~~diff
- 00b5484c ["INT_ADD", "register:40f0:8", ["const:b5484c:8", "const:4:8"]]
- 00b5484c ["CALL", null, ["callee:00bde090:8"]]
+ 00b54890 ["INT_ADD", "register:40f0:8", ["const:b54890:8", "const:4:8"]]
+ 00b54890 ["CALL", null, ["callee:00bde090:8"]]
- 00b5484c bytes fd250294
+ 00b54890 bytes 00260294
- 00b54854 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00b54854 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54898 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00b54898 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54854 bytes 60aa01f9
+ 00b54898 bytes 60ca01f9
- 00b54834 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00b54834 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b54878 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00b54878 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b54834 bytes 68aa41f9
+ 00b54878 bytes 68ca41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-772a0351ffbd1d4334def87e3423150b"></a>

### [`00b54868`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54868.md) → [`00b548ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b548ac.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b548dc",
      "incomplete_value": true,
      "site": "00b548dc",
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
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54898",
      "incomplete_value": true,
      "site": "00b54898",
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
            "const:350:8"
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
      "definition_site": "00b548c0",
      "incomplete_value": true,
      "site": "00b548c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5487c",
      "incomplete_value": true,
      "site": "00b5487c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b548c8",
      "incomplete_value": false,
      "site": "00b548d4",
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
            "const:889:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54884",
      "incomplete_value": false,
      "site": "00b54890",
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
            "const:916:8"
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
      "00b548bc",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b548c8",
      "PARAM",
      [
        "storage",
        "00299916",
        null,
        "string"
      ]
    ],
    [
      "00b548dc",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b548bc",
      "READ",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ],
    [
      "00b548c8",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ],
    [
      "00b548dc",
      "WRITE",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54868.md#insn-00b54890) · [`00b54898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54868.md#insn-00b54898) · [`00b54878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54868.md#insn-00b54878)
- 新版 `00b548d4`（命令位置の公開資料なし） · `00b548dc`（命令位置の公開資料なし） · `00b548bc`（命令位置の公開資料なし）

~~~diff
- 00b54890 ["INT_ADD", "register:40f0:8", ["const:b54890:8", "const:4:8"]]
- 00b54890 ["CALL", null, ["callee:00bde090:8"]]
+ 00b548d4 ["INT_ADD", "register:40f0:8", ["const:b548d4:8", "const:4:8"]]
+ 00b548d4 ["CALL", null, ["callee:00bde090:8"]]
- 00b54890 bytes ec250294
+ 00b548d4 bytes ef250294
- 00b54898 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00b54898 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b548dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00b548dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54898 bytes 60aa01f9
+ 00b548dc bytes 60ca01f9
- 00b54878 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00b54878 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b548bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00b548bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b54878 bytes 68aa41f9
+ 00b548bc bytes 68ca41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3c6a4660720fb815490ac277ebc4c10"></a>

### [`00b548b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b548b8.md) → [`00b548fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b548fc.md) _ZN8firebase13remote_config8internal35config_update_listener_registration15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b54954",
      "incomplete_value": true,
      "site": "00b54954",
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
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54910",
      "incomplete_value": true,
      "site": "00b54910",
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
            "const:358:8"
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
      "definition_site": "00b54930",
      "incomplete_value": true,
      "site": "00b5493c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:390:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b548ec",
      "incomplete_value": true,
      "site": "00b548f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:350:8"
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
      "00b54910",
      "READ",
      [
        "storage",
        "010a1358",
        null,
        "undefined1"
      ]
    ],
    [
      "00b54930",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54954",
      "WRITE",
      [
        "storage",
        "010a1358",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b54910",
      "READ",
      [
        "storage",
        "010a1398",
        null,
        "undefined1"
      ]
    ],
    [
      "00b54930",
      "READ",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54954",
      "WRITE",
      [
        "storage",
        "010a1398",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b548cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b548b8.md#insn-00b548cc) · [`00b548f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b548b8.md#insn-00b548f8) · [`00b54910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b548b8.md#insn-00b54910)
- 新版 `00b54910`（命令位置の公開資料なし） · `00b5493c`（命令位置の公開資料なし） · `00b54954`（命令位置の公開資料なし）

~~~diff
- 00b548cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:358:8"]]
- 00b548cc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b548cc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b54910 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:398:8"]]
+ 00b54910 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b54910 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b548cc bytes a8624d39
+ 00b54910 bytes a8624e39
- 00b548f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b548f8 ["INT_ADD", "register:40f0:8", ["const:b548f8:8", "const:4:8"]]
- 00b548f8 ["CALLIND", null, ["register:0:8"]]
+ 00b5493c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5493c ["INT_ADD", "register:40f0:8", ["const:b5493c:8", "const:4:8"]]
+ 00b5493c ["CALLIND", null, ["register:0:8"]]
- 00b548f8 bytes 00013fd6
+ 00b5493c bytes 00013fd6
- 00b54910 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b54910 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:358:8"]]
- 00b54910 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b54954 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b54954 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:398:8"]]
+ 00b54954 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b54910 bytes a0620d39
+ 00b54954 bytes a0620e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc5b0f03e017f5f6860ac966899bba26"></a>

### [`00b54924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54924.md) → [`00b54968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54968.md) _ZN8firebase13remote_config8internal35config_update_listener_registration12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b549a4",
      "incomplete_value": true,
      "site": "00b549a4",
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
            "const:398:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54960",
      "incomplete_value": true,
      "site": "00b54960",
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
            "const:358:8"
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
      "definition_site": "00b549c4",
      "incomplete_value": true,
      "site": "00b549c4",
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
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54980",
      "incomplete_value": true,
      "site": "00b54980",
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
            "const:350:8"
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
      "definition_site": "00b54980",
      "incomplete_value": true,
      "site": "00b54980",
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
      "definition_site": "00b5493c",
      "incomplete_value": true,
      "site": "00b5493c",
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
      "00b5497c",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54988",
      "READ",
      [
        "storage",
        "010a1358",
        null,
        "undefined1"
      ]
    ],
    [
      "00b549a4",
      "WRITE",
      [
        "storage",
        "010a1358",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5497c",
      "READ",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54988",
      "READ",
      [
        "storage",
        "010a1398",
        null,
        "undefined1"
      ]
    ],
    [
      "00b549a4",
      "WRITE",
      [
        "storage",
        "010a1398",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54924.md#insn-00b54938) · [`00b54960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54924.md#insn-00b54960) · [`00b5497c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54924.md#insn-00b5497c)
- 新版 `00b5497c`（命令位置の公開資料なし） · `00b549a4`（命令位置の公開資料なし） · `00b549c0`（命令位置の公開資料なし）

~~~diff
- 00b54938 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00b54938 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5497c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
+ 00b5497c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b54938 bytes 81aa41f9
+ 00b5497c bytes 81ca41f9
- 00b54960 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b54960 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b54960 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:358:8"]]
- 00b54960 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b549a4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b549a4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b549a4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:398:8"]]
+ 00b549a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b54960 bytes bf620d39
+ 00b549a4 bytes bf620e39
- 00b5497c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5497c ["INT_ADD", "register:40f0:8", ["const:b5497c:8", "const:4:8"]]
- 00b5497c ["CALLIND", null, ["register:0:8"]]
+ 00b549c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b549c0 ["INT_ADD", "register:40f0:8", ["const:b549c0:8", "const:4:8"]]
+ 00b549c0 ["CALLIND", null, ["register:0:8"]]
- 00b5497c bytes 00013fd6
+ 00b549c0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-446e88d2439e53efb62d4344568670f2"></a>

### [`00b54994`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54994.md) → [`00b549d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b549d8.md) _ZN8firebase13remote_config8internal35config_update_listener_registration14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b54a18",
      "incomplete_value": true,
      "site": "00b54a18",
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
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b549d4",
      "incomplete_value": true,
      "site": "00b549d4",
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
            "const:350:8"
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
      "definition_site": "00b549f4",
      "incomplete_value": true,
      "site": "00b549f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b549b0",
      "incomplete_value": true,
      "site": "00b549b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b549fc",
      "incomplete_value": false,
      "site": "00b54a10",
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
            "const:889:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b549b8",
      "incomplete_value": false,
      "site": "00b549cc",
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
            "const:916:8"
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
      "00b549ec",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b549fc",
      "PARAM",
      [
        "storage",
        "00299916",
        null,
        "string"
      ]
    ],
    [
      "00b54a18",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b549ec",
      "READ",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ],
    [
      "00b549fc",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ],
    [
      "00b54a18",
      "WRITE",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b549cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54994.md#insn-00b549cc) · [`00b549d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54994.md#insn-00b549d4) · [`00b549a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54994.md#insn-00b549a8)
- 新版 `00b54a10`（命令位置の公開資料なし） · `00b54a18`（命令位置の公開資料なし） · `00b549ec`（命令位置の公開資料なし）

~~~diff
- 00b549cc ["INT_ADD", "register:40f0:8", ["const:b549cc:8", "const:4:8"]]
- 00b549cc ["CALL", null, ["callee:00bde090:8"]]
+ 00b54a10 ["INT_ADD", "register:40f0:8", ["const:b54a10:8", "const:4:8"]]
+ 00b54a10 ["CALL", null, ["callee:00bde090:8"]]
- 00b549cc bytes 9d250294
+ 00b54a10 bytes a0250294
- 00b549d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00b549d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54a18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
+ 00b54a18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b549d4 bytes 80aa01f9
+ 00b54a18 bytes 80ca01f9
- 00b549a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00b549a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b549ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
+ 00b549ec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b549a8 bytes 81aa41f9
+ 00b549ec bytes 81ca41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbe366869ed0cfec2de2c7b194bf1df2"></a>

### [`00b54a04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54a04.md) → [`00b54a48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54a48.md) _ZN8firebase13remote_config8internal35config_update_listener_registration11GetMethodIdENS2_6MethodE

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
      "definition_site": "00b54a64",
      "incomplete_value": false,
      "site": "00b54a68",
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
      "definition_site": "00b54a20",
      "incomplete_value": false,
      "site": "00b54a24",
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
      "definition_site": "00b54a74",
      "incomplete_value": true,
      "site": "00b54a80",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b54a30",
      "incomplete_value": true,
      "site": "00b54a3c",
      "value": [
        "LOAD",
        "8",
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
      "00b54a64",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b54a74",
      "DATA",
      [
        "storage",
        "010a1360",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54a64",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b54a74",
      "DATA",
      [
        "storage",
        "010a13a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54a04.md#insn-00b54a24) · [`00b54a20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54a04.md#insn-00b54a20) · [`00b54a2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54a04.md#insn-00b54a2c)
- 新版 `00b54a68`（命令位置の公開資料なし） · `00b54a64`（命令位置の公開資料なし） · `00b54a70`（命令位置の公開資料なし）

~~~diff
- 00b54a24 ["INT_ADD", "register:40f0:8", ["const:b54a24:8", "const:4:8"]]
- 00b54a24 ["CALL", null, ["callee:00bde180:8"]]
+ 00b54a68 ["INT_ADD", "register:40f0:8", ["const:b54a68:8", "const:4:8"]]
+ 00b54a68 ["CALL", null, ["callee:00bde180:8"]]
- 00b54a24 bytes c3250294
+ 00b54a68 bytes c6250294
- 00b54a20 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b54a20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b54a20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b54a20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b54a64 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b54a64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b54a64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b54a64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b54a20 bytes 00501791
+ 00b54a64 bytes 001c1591
- 00b54a2c ["COPY", "tmp:0:8", ["const:360:8"]]
- 00b54a2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b54a2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b54a2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b54a70 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 00b54a70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54a70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54a70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b54a2c bytes 08810d91
+ 00b54a70 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c381cca2692923908897df9e7f9c3bd"></a>

### [`00b54a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54a40.md) → [`00b54a84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54a84.md) _ZN8firebase13remote_config8internal35config_update_listener_registration13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b54ac4",
      "incomplete_value": true,
      "site": "00b54ac4",
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
            "const:390:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54a80",
      "incomplete_value": true,
      "site": "00b54a80",
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
            "const:350:8"
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
      "definition_site": "00b54aa0",
      "incomplete_value": true,
      "site": "00b54aa0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54a5c",
      "incomplete_value": true,
      "site": "00b54a5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "definition_site": "00b54aa8",
      "incomplete_value": false,
      "site": "00b54abc",
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
            "const:889:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54a64",
      "incomplete_value": false,
      "site": "00b54a78",
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
            "const:916:8"
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
      "00b54a98",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54aa8",
      "PARAM",
      [
        "storage",
        "00299916",
        null,
        "string"
      ]
    ],
    [
      "00b54ac4",
      "WRITE",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b54a98",
      "READ",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ],
    [
      "00b54aa8",
      "PARAM",
      [
        "storage",
        "00299889",
        null,
        "string"
      ]
    ],
    [
      "00b54ac4",
      "WRITE",
      [
        "storage",
        "010a1390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54a40.md#insn-00b54a78) · [`00b54a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54a40.md#insn-00b54a80) · [`00b54a54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54a40.md#insn-00b54a54)
- 新版 `00b54abc`（命令位置の公開資料なし） · `00b54ac4`（命令位置の公開資料なし） · `00b54a98`（命令位置の公開資料なし）

~~~diff
- 00b54a78 ["INT_ADD", "register:40f0:8", ["const:b54a78:8", "const:4:8"]]
- 00b54a78 ["CALL", null, ["callee:00bde090:8"]]
+ 00b54abc ["INT_ADD", "register:40f0:8", ["const:b54abc:8", "const:4:8"]]
+ 00b54abc ["CALL", null, ["callee:00bde090:8"]]
- 00b54a78 bytes 72250294
+ 00b54abc bytes 75250294
- 00b54a80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00b54a80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b54ac4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
+ 00b54ac4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b54a80 bytes 80aa01f9
+ 00b54ac4 bytes 80ca01f9
- 00b54a54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00b54a54 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b54a98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
+ 00b54a98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b54a54 bytes 81aa41f9
+ 00b54a98 bytes 81ca41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cb1a35ef5ff5cf4d3287483b351e78d"></a>

### [`00b54ab0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54ab0.md) → [`00b54af4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54af4.md) _ZN8firebase13remote_config8internal35config_update_listener_registration10GetFieldIdENS2_5FieldE

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
      "definition_site": "00b54b10",
      "incomplete_value": false,
      "site": "00b54b14",
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
      "definition_site": "00b54acc",
      "incomplete_value": false,
      "site": "00b54ad0",
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
      "definition_site": "00b54b20",
      "incomplete_value": true,
      "site": "00b54b2c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b54adc",
      "incomplete_value": true,
      "site": "00b54ae8",
      "value": [
        "LOAD",
        "8",
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
      "00b54b10",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b54b20",
      "DATA",
      [
        "storage",
        "010a1368",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54b10",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b54b20",
      "DATA",
      [
        "storage",
        "010a13a8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54ab0.md#insn-00b54ad0) · [`00b54acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54ab0.md#insn-00b54acc) · [`00b54ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54ab0.md#insn-00b54ad8)
- 新版 `00b54b14`（命令位置の公開資料なし） · `00b54b10`（命令位置の公開資料なし） · `00b54b1c`（命令位置の公開資料なし）

~~~diff
- 00b54ad0 ["INT_ADD", "register:40f0:8", ["const:b54ad0:8", "const:4:8"]]
- 00b54ad0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b54b14 ["INT_ADD", "register:40f0:8", ["const:b54b14:8", "const:4:8"]]
+ 00b54b14 ["CALL", null, ["callee:00bde180:8"]]
- 00b54ad0 bytes 98250294
+ 00b54b14 bytes 9b250294
- 00b54acc ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b54acc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b54acc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b54acc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b54b10 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b54b10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b54b10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b54b10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b54acc bytes 00fc1991
+ 00b54b10 bytes 00c81791
- 00b54ad8 ["COPY", "tmp:0:8", ["const:368:8"]]
- 00b54ad8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b54ad8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b54ad8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b54b1c ["COPY", "tmp:0:8", ["const:3a8:8"]]
+ 00b54b1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54b1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b54b1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b54ad8 bytes 08a10d91
+ 00b54b1c bytes 08a10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7cf9e35c9f87cc92c5f82503b87976a5"></a>

### [`00b54af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54af4.md) → [`00b54b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b54/00b54b38.md) _ZN8firebase13remote_config8internal20RemoteConfigInternalC1ERKNS_3AppE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0820.md) · 呼出先 22件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00be0870`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0870.md) · 呼出先 22件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 branch_value, call_argument_candidate, comparison, comparison_count, constant, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, store_value, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 77.78% / 新版 77.78%

CFGの説明率　旧版 74.66% / 新版 74.66%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 32件, `store_destination` 3件, `unresolved_branch_alignment` 8件, `unresolved_call_alignment` 13件, `unresolved_store_alignment` 9件

アドレスに依存する影響 `branch_value` 13件, `call_argument_candidate` 6件, `store_condition` 7件, `store_destination` 14件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b54cc4",
      "incomplete_value": true,
      "site": "00b54cdc",
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
      "definition_site": "00b54c80",
      "incomplete_value": true,
      "site": "00b54c98",
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
    "ordinal": 36,
    "slot": 2
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b54d40",
      "incomplete_value": false,
      "site": "00b54d40",
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
            "const:350:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54cfc",
      "incomplete_value": false,
      "site": "00b54cfc",
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
            "const:310:8"
          ]
        ]
      ]
    },
    "ordinal": 39,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b54dc0",
      "incomplete_value": false,
      "site": "00b54dc0",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b54d7c",
      "incomplete_value": false,
      "site": "00b54d7c",
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
            "const:318:8"
          ]
        ]
      ]
    },
    "ordinal": 40,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b54ba0",
      "READ",
      [
        "storage",
        "00c1baf8",
        null,
        "pointer"
      ]
    ],
    [
      "00b54bc0",
      "DATA",
      [
        "storage",
        "010a1370",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ],
    [
      "00b54bc0",
      "DATA",
      [
        "storage",
        "010a1374",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b54ba0",
      "READ",
      [
        "storage",
        "00c1bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00b54bc0",
      "DATA",
      [
        "storage",
        "010a13b0",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ],
    [
      "00b54bc0",
      "DATA",
      [
        "storage",
        "010a13b4",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b54cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54af4.md#insn-00b54cb8) · [`00b54cdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54af4.md#insn-00b54cdc) · [`00b54cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b54/00b54af4.md#insn-00b54cfc)
- 新版 `00b54cfc`（命令位置の公開資料なし） · `00b54d20`（命令位置の公開資料なし） · `00b54d40`（命令位置の公開資料なし）

~~~diff
- 00b54cb8 ["INT_ADD", "register:40f0:8", ["const:b54cb8:8", "const:4:8"]]
- 00b54cb8 ["CALL", null, ["callee:00be0970:8"]]
+ 00b54cfc ["INT_ADD", "register:40f0:8", ["const:b54cfc:8", "const:4:8"]]
+ 00b54cfc ["CALL", null, ["callee:00be0970:8"]]
- 00b54cb8 bytes 1a2f0294
+ 00b54cfc bytes 1d2f0294
- 00b54cdc ["COPY", "tmp:0:8", ["const:293:8"]]
- 00b54cdc ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b54cdc ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b54cdc ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b54d20 ["COPY", "tmp:0:8", ["const:32d:8"]]
+ 00b54d20 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b54d20 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b54d20 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b54cdc bytes 634c0a91
+ 00b54d20 bytes 63b40c91
- 00b54cfc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:310:8"]]
- 00b54cfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
+ 00b54d40 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
+ 00b54d40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4008:8"]]
- 00b54cfc bytes 018901f9
+ 00b54d40 bytes 01a901f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94cac295df2c90c44ad593ae74992518"></a>

### [`00b55964`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55964.md) → [`00b559a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b559a8.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal7CleanupEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be07b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be07b0.md) · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde100.md)
- 新版 呼出元 1件 [`00be0800`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0800.md) · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde150.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 84.09% / 新版 84.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 2件, `call_argument_candidate` 5件, `store_destination` 18件, `store_value` 2件

アドレスに依存する影響 `branch_value` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b559dc",
      "incomplete_value": true,
      "site": "00b559dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b55998",
      "incomplete_value": true,
      "site": "00b55998",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:af8:8"
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
      "definition_site": "00b559dc",
      "incomplete_value": true,
      "site": "00b559dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b55998",
      "incomplete_value": true,
      "site": "00b55998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:4:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b55a5c",
      "incomplete_value": true,
      "site": "00b55a5c",
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
            "const:358:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b55a18",
      "incomplete_value": true,
      "site": "00b55a18",
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
            "const:318:8"
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
      "00b559c8",
      "READ",
      [
        "storage",
        "00c1baf8",
        null,
        "pointer"
      ]
    ],
    [
      "00b559d8",
      "PARAM",
      [
        "storage",
        "010a1374",
        null,
        null
      ]
    ],
    [
      "00b559dc",
      "DATA",
      [
        "storage",
        "010a1370",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00b559c8",
      "READ",
      [
        "storage",
        "00c1bb48",
        null,
        "pointer"
      ]
    ],
    [
      "00b559d8",
      "PARAM",
      [
        "storage",
        "010a13b4",
        null,
        null
      ]
    ],
    [
      "00b559dc",
      "DATA",
      [
        "storage",
        "010a13b0",
        "_ZN8firebase13remote_config8internal20RemoteConfigInternal12initializer_E",
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5599c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55964.md#insn-00b5599c) · [`00b559f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55964.md#insn-00b559f0) · [`00b55a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55964.md#insn-00b55a00)
- 新版 `00b559e0`（命令位置の公開資料なし） · `00b55a34`（命令位置の公開資料なし） · `00b55a44`（命令位置の公開資料なし）

~~~diff
- 00b5599c ["INT_ADD", "register:40f0:8", ["const:b5599c:8", "const:4:8"]]
- 00b5599c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b559e0 ["INT_ADD", "register:40f0:8", ["const:b559e0:8", "const:4:8"]]
+ 00b559e0 ["CALL", null, ["callee:00bddc20:8"]]
- 00b5599c bytes 8d200294
+ 00b559e0 bytes 90200294
- 00b559f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:310:8"]]
- 00b559f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b55a34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
+ 00b55a34 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b559f0 bytes 818a41f9
+ 00b55a34 bytes 81aa41f9
- 00b55a00 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:318:8"]]
- 00b55a00 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b55a00 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b55a44 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:358:8"]]
+ 00b55a44 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b55a44 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b55a00 bytes c8624c39
+ 00b55a44 bytes c8624d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70b1705959a571f412b0444f6eeeb8de"></a>

### [`00b55e38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55e38.md) → [`00b55e7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55e7c.md) FUN_00b55e7c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00b55d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55d08.md) [`00b59808`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59808.md) · 呼出先 4件 [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`0056c6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c6c4.md) [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 2件 [`00b55d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55d4c.md) [`00b5984c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b5984c.md) · 呼出先 4件 [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`0056c6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c6c4.md) [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.84% / 新版 91.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b55eb4",
      "incomplete_value": true,
      "site": "00b55ec0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b55e70",
      "incomplete_value": true,
      "site": "00b55e7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:270:8"
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
      "definition_site": "00b55f18",
      "incomplete_value": false,
      "site": "00b55f1c",
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
            "const:5dd:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b55ed4",
      "incomplete_value": false,
      "site": "00b55ed8",
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
            "const:671:8"
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
      "00b55e98",
      "READ",
      [
        "storage",
        "010a1260",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55eb4",
      "READ",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55ed4",
      "READ",
      [
        "storage",
        "010a1278",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b55e98",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55eb4",
      "READ",
      [
        "storage",
        "010a12b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b55ed4",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b55e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55e38.md#insn-00b55e7c) · [`00b55ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55e38.md#insn-00b55ed8) · [`00b55e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55e38.md#insn-00b55e54)
- 新版 `00b55ec0`（命令位置の公開資料なし） · `00b55f1c`（命令位置の公開資料なし） · `00b55e98`（命令位置の公開資料なし）

~~~diff
- 00b55e7c ["INT_ADD", "register:40f0:8", ["const:b55e7c:8", "const:4:8"]]
- 00b55e7c ["CALL", null, ["callee:0056c6c4:8"]]
+ 00b55ec0 ["INT_ADD", "register:40f0:8", ["const:b55ec0:8", "const:4:8"]]
+ 00b55ec0 ["CALL", null, ["callee:0056c6c4:8"]]
- 00b55e7c bytes 125ae897
+ 00b55ec0 bytes 015ae897
- 00b55ed8 ["INT_ADD", "register:40f0:8", ["const:b55ed8:8", "const:4:8"]]
- 00b55ed8 ["CALL", null, ["callee:00bddf60:8"]]
+ 00b55f1c ["INT_ADD", "register:40f0:8", ["const:b55f1c:8", "const:4:8"]]
+ 00b55f1c ["CALL", null, ["callee:00bddf60:8"]]
- 00b55ed8 bytes 0e200294
+ 00b55f1c bytes 11200294
- 00b55e54 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:260:8"]]
- 00b55e54 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b55e98 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:2a0:8"]]
+ 00b55e98 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b55e54 bytes 223141f9
+ 00b55e98 bytes 225141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-175fab348315f8c643f2983db227ba85"></a>

### [`00b564b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b564b0.md) → [`00b564f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b564f4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17EnsureInitializedEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0700.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b55d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55d08.md) [`00b5a2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a2a8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00be0750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0750.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b55d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55d4c.md) [`00b5a2ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a2ec.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.19% / 新版 99.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b56538",
      "incomplete_value": true,
      "site": "00b5654c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b564f4",
      "incomplete_value": true,
      "site": "00b56508",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b56574",
      "incomplete_value": true,
      "site": "00b5657c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56530",
      "incomplete_value": true,
      "site": "00b56538",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:190:8"
              ]
            ]
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
      "definition_site": "00b565a0",
      "incomplete_value": false,
      "site": "00b565b4",
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
            "const:2bb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5655c",
      "incomplete_value": false,
      "site": "00b56570",
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
            "const:221:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b56538",
      "READ",
      [
        "storage",
        "00c1bb08",
        null,
        "pointer"
      ]
    ],
    [
      "00b56538",
      "PARAM",
      [
        "storage",
        "00b5a2a8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_13remote_config10ConfigInfoEEEvPv",
        null
      ]
    ],
    [
      "00b56574",
      "READ",
      [
        "storage",
        "010a1190",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b56538",
      "READ",
      [
        "storage",
        "00c1bb58",
        null,
        "pointer"
      ]
    ],
    [
      "00b56538",
      "PARAM",
      [
        "storage",
        "00b5a2ec",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_13remote_config10ConfigInfoEEEvPv",
        null
      ]
    ],
    [
      "00b56574",
      "READ",
      [
        "storage",
        "010a11d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b564f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b564b0.md#insn-00b564f4) · [`00b56508`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b564b0.md#insn-00b56508) · [`00b56538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b564b0.md#insn-00b56538)
- 新版 `00b56538`（命令位置の公開資料なし） · `00b5654c`（命令位置の公開資料なし） · `00b5657c`（命令位置の公開資料なし）

~~~diff
- 00b564f4 ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:b08:8"]]
- 00b564f4 ["LOAD", "register:4018:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b56538 ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:b58:8"]]
+ 00b56538 ["LOAD", "register:4018:8", ["const:1b1:8", "tmp:0:8"]]
- 00b564f4 bytes 638445f9
+ 00b56538 bytes 63ac45f9
- 00b56508 ["INT_ADD", "register:40f0:8", ["const:b56508:8", "const:4:8"]]
- 00b56508 ["CALL", null, ["callee:00bddfc0:8"]]
+ 00b5654c ["INT_ADD", "register:40f0:8", ["const:b5654c:8", "const:4:8"]]
+ 00b5654c ["CALL", null, ["callee:00bddfc0:8"]]
- 00b56508 bytes 9a1e0294
+ 00b5654c bytes 9d1e0294
- 00b56538 ["INT_ADD", "register:40f0:8", ["const:b56538:8", "const:4:8"]]
- 00b56538 ["CALL", null, ["callee:0047495c:8"]]
+ 00b5657c ["INT_ADD", "register:40f0:8", ["const:b5657c:8", "const:4:8"]]
+ 00b5657c ["CALL", null, ["callee:0047495c:8"]]
- 00b56538 bytes 0979e497
+ 00b5657c bytes f878e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65501144d31d237f3507049663fe52a8"></a>

### [`00b567dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b567dc.md) → [`00b56820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56820.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal8ActivateEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be07f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be07f0.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b55efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55efc.md) [`00b5a45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a45c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00be0840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0840.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b55f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55f40.md) [`00b5a4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a4a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.19% / 新版 99.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b56864",
      "incomplete_value": true,
      "site": "00b56878",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56820",
      "incomplete_value": true,
      "site": "00b56834",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b568a0",
      "incomplete_value": true,
      "site": "00b568a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1d8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5685c",
      "incomplete_value": true,
      "site": "00b56864",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:198:8"
              ]
            ]
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
      "definition_site": "00b568cc",
      "incomplete_value": false,
      "site": "00b568e0",
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
            "const:2e3:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56888",
      "incomplete_value": false,
      "site": "00b5689c",
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
            "const:249:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b56864",
      "READ",
      [
        "storage",
        "00c1bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00b56864",
      "PARAM",
      [
        "storage",
        "00b5a45c",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00b568a0",
      "READ",
      [
        "storage",
        "010a1198",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b56864",
      "READ",
      [
        "storage",
        "00c1bb60",
        null,
        "pointer"
      ]
    ],
    [
      "00b56864",
      "PARAM",
      [
        "storage",
        "00b5a4a0",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00b568a0",
      "READ",
      [
        "storage",
        "010a11d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b56820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b567dc.md#insn-00b56820) · [`00b56834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b567dc.md#insn-00b56834) · [`00b56864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b567dc.md#insn-00b56864)
- 新版 `00b56864`（命令位置の公開資料なし） · `00b56878`（命令位置の公開資料なし） · `00b568a8`（命令位置の公開資料なし）

~~~diff
- 00b56820 ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:b10:8"]]
- 00b56820 ["LOAD", "register:4018:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b56864 ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:b60:8"]]
+ 00b56864 ["LOAD", "register:4018:8", ["const:1b1:8", "tmp:0:8"]]
- 00b56820 bytes 638845f9
+ 00b56864 bytes 63b045f9
- 00b56834 ["INT_ADD", "register:40f0:8", ["const:b56834:8", "const:4:8"]]
- 00b56834 ["CALL", null, ["callee:00bddfc0:8"]]
+ 00b56878 ["INT_ADD", "register:40f0:8", ["const:b56878:8", "const:4:8"]]
+ 00b56878 ["CALL", null, ["callee:00bddfc0:8"]]
- 00b56834 bytes cf1d0294
+ 00b56878 bytes d21d0294
- 00b56864 ["INT_ADD", "register:40f0:8", ["const:b56864:8", "const:4:8"]]
- 00b56864 ["CALL", null, ["callee:0047495c:8"]]
+ 00b568a8 ["INT_ADD", "register:40f0:8", ["const:b568a8:8", "const:4:8"]]
+ 00b568a8 ["CALL", null, ["callee:0047495c:8"]]
- 00b56864 bytes 3e78e497
+ 00b568a8 bytes 2d78e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-016dc1b5e8acb689acae4a252f0711e4"></a>

### [`00b56b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56b08.md) → [`00b56b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56b4c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal16FetchAndActivateEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be06f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be06f0.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b55efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b55/00b55efc.md) [`00b5a45c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a45c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00be0740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0740.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b55f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b55/00b55f40.md) [`00b5a4a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a4a0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.19% / 新版 99.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b56b90",
      "incomplete_value": true,
      "site": "00b56ba4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b60:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56b4c",
      "incomplete_value": true,
      "site": "00b56b60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b10:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 1,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b56bcc",
      "incomplete_value": true,
      "site": "00b56bd4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56b88",
      "incomplete_value": true,
      "site": "00b56b90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a0:8"
              ]
            ]
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
      "definition_site": "00b56bf8",
      "incomplete_value": false,
      "site": "00b56c0c",
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
            "const:f43:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56bb4",
      "incomplete_value": false,
      "site": "00b56bc8",
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
            "const:eb8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b56b90",
      "READ",
      [
        "storage",
        "00c1bb10",
        null,
        "pointer"
      ]
    ],
    [
      "00b56b90",
      "PARAM",
      [
        "storage",
        "00b5a45c",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00b56bcc",
      "READ",
      [
        "storage",
        "010a11a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b56b90",
      "READ",
      [
        "storage",
        "00c1bb60",
        null,
        "pointer"
      ]
    ],
    [
      "00b56b90",
      "PARAM",
      [
        "storage",
        "00b5a4a0",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv",
        null
      ]
    ],
    [
      "00b56bcc",
      "READ",
      [
        "storage",
        "010a11e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b56b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56b08.md#insn-00b56b4c) · [`00b56b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56b08.md#insn-00b56b60) · [`00b56b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56b08.md#insn-00b56b90)
- 新版 `00b56b90`（命令位置の公開資料なし） · `00b56ba4`（命令位置の公開資料なし） · `00b56bd4`（命令位置の公開資料なし）

~~~diff
- 00b56b4c ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:b10:8"]]
- 00b56b4c ["LOAD", "register:4018:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b56b90 ["INT_ADD", "tmp:0:8", ["register:4018:8", "const:b60:8"]]
+ 00b56b90 ["LOAD", "register:4018:8", ["const:1b1:8", "tmp:0:8"]]
- 00b56b4c bytes 638845f9
+ 00b56b90 bytes 63b045f9
- 00b56b60 ["INT_ADD", "register:40f0:8", ["const:b56b60:8", "const:4:8"]]
- 00b56b60 ["CALL", null, ["callee:00bddfc0:8"]]
+ 00b56ba4 ["INT_ADD", "register:40f0:8", ["const:b56ba4:8", "const:4:8"]]
+ 00b56ba4 ["CALL", null, ["callee:00bddfc0:8"]]
- 00b56b60 bytes 041d0294
+ 00b56ba4 bytes 071d0294
- 00b56b90 ["INT_ADD", "register:40f0:8", ["const:b56b90:8", "const:4:8"]]
- 00b56b90 ["CALL", null, ["callee:0047495c:8"]]
+ 00b56bd4 ["INT_ADD", "register:40f0:8", ["const:b56bd4:8", "const:4:8"]]
+ 00b56bd4 ["CALL", null, ["callee:0047495c:8"]]
- 00b56b90 bytes 7377e497
+ 00b56bd4 bytes 6277e497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fef69f25ac316e70b013cb8c6cfd142f"></a>

### [`00b56e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56e34.md) → [`00b56e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56e78.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal5FetchEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0790.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b56134`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56134.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00be07e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07e0.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b56178`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56178.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.19% / 新版 99.19%

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
      "definition_site": "00b56f20",
      "incomplete_value": false,
      "site": "00b56f34",
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
            "const:6a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56edc",
      "incomplete_value": false,
      "site": "00b56ef0",
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
            "const:735:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b56ff0",
      "incomplete_value": true,
      "site": "00b57000",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b56fac",
      "incomplete_value": true,
      "site": "00b56fbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ad8:8"
              ]
            ]
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
      "00b56ef0",
      "READ",
      [
        "storage",
        "010a1200",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56f20",
      "PARAM",
      [
        "storage",
        "00297735",
        null,
        "string"
      ]
    ],
    [
      "00b56ff0",
      "READ",
      [
        "storage",
        "00c1bad8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b56ef0",
      "READ",
      [
        "storage",
        "010a1240",
        null,
        "undefined8"
      ]
    ],
    [
      "00b56f20",
      "PARAM",
      [
        "storage",
        "002976a8",
        null,
        "string"
      ]
    ],
    [
      "00b56ff0",
      "READ",
      [
        "storage",
        "00c1bb28",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b56eac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56e34.md#insn-00b56eac) · [`00b56ef0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56e34.md#insn-00b56ef0) · [`00b56fbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b56e34.md#insn-00b56fbc)
- 新版 `00b56ef0`（命令位置の公開資料なし） · `00b56f34`（命令位置の公開資料なし） · `00b57000`（命令位置の公開資料なし）

~~~diff
- 00b56eac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:200:8"]]
- 00b56eac ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b56ef0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:240:8"]]
+ 00b56ef0 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b56eac bytes 020141f9
+ 00b56ef0 bytes 022141f9
- 00b56ef0 ["INT_ADD", "register:40f0:8", ["const:b56ef0:8", "const:4:8"]]
- 00b56ef0 ["CALL", null, ["callee:00bdee00:8"]]
+ 00b56f34 ["INT_ADD", "register:40f0:8", ["const:b56f34:8", "const:4:8"]]
+ 00b56f34 ["CALL", null, ["callee:00bdee00:8"]]
- 00b56ef0 bytes b01f0294
+ 00b56f34 bytes b31f0294
- 00b56fbc ["INT_ADD", "register:40f0:8", ["const:b56fbc:8", "const:4:8"]]
- 00b56fbc ["CALL", null, ["callee:00bde0c0:8"]]
+ 00b57000 ["INT_ADD", "register:40f0:8", ["const:b57000:8", "const:4:8"]]
+ 00b57000 ["CALL", null, ["callee:00bde0c0:8"]]
- 00b56fbc bytes 2d1c0294
+ 00b57000 bytes 301c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd2e22e2902c01c41b27871cbea46902"></a>

### [`00b5715c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b5715c.md) → [`00b571a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b571a0.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEi

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be06c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be06c0.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b561b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b561b4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 1件 [`00be0710`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0710.md) · 呼出先 14件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b561f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b561f8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.19% / 新版 99.19%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b57218",
      "incomplete_value": true,
      "site": "00b57224",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b571d4",
      "incomplete_value": true,
      "site": "00b571e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1a8:8"
              ]
            ]
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
      "definition_site": "00b57248",
      "incomplete_value": false,
      "site": "00b5725c",
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
            "const:5a5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b57204",
      "incomplete_value": false,
      "site": "00b57218",
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
            "const:639:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b57318",
      "incomplete_value": true,
      "site": "00b57328",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b572d4",
      "incomplete_value": true,
      "site": "00b572e4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae8:8"
              ]
            ]
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
      "00b57218",
      "READ",
      [
        "storage",
        "010a11a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b57248",
      "PARAM",
      [
        "storage",
        "002af639",
        null,
        "string"
      ]
    ],
    [
      "00b57318",
      "READ",
      [
        "storage",
        "00c1bae8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b57218",
      "READ",
      [
        "storage",
        "010a11e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b57248",
      "PARAM",
      [
        "storage",
        "002af5a5",
        null,
        "string"
      ]
    ],
    [
      "00b57318",
      "READ",
      [
        "storage",
        "00c1bb38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b571d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b5715c.md#insn-00b571d4) · [`00b571e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b5715c.md#insn-00b571e0) · [`00b57218`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b5715c.md#insn-00b57218)
- 新版 `00b57218`（命令位置の公開資料なし） · `00b57224`（命令位置の公開資料なし） · `00b5725c`（命令位置の公開資料なし）

~~~diff
- 00b571d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1a8:8"]]
- 00b571d4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b57218 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:1e8:8"]]
+ 00b57218 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b571d4 bytes 02d540f9
+ 00b57218 bytes 02f540f9
- 00b571e0 ["INT_ADD", "register:40f0:8", ["const:b571e0:8", "const:4:8"]]
- 00b571e0 ["CALL", null, ["callee:0047495c:8"]]
+ 00b57224 ["INT_ADD", "register:40f0:8", ["const:b57224:8", "const:4:8"]]
+ 00b57224 ["CALL", null, ["callee:0047495c:8"]]
- 00b571e0 bytes df75e497
+ 00b57224 bytes ce75e497
- 00b57218 ["INT_ADD", "register:40f0:8", ["const:b57218:8", "const:4:8"]]
- 00b57218 ["CALL", null, ["callee:00bdee00:8"]]
+ 00b5725c ["INT_ADD", "register:40f0:8", ["const:b5725c:8", "const:4:8"]]
+ 00b5725c ["CALL", null, ["callee:00bdee00:8"]]
- 00b57218 bytes e61e0294
+ 00b5725c bytes e91e0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8746f03507c04bdc31ef52d9d889c6df"></a>

### [`00b573f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b573f4.md) → [`00b57438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57438.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEPKNS0_21ConfigKeyValueVariantEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be06b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be06b0.md) · 呼出先 33件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00b561b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b561b4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00be0700`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0700.md) · 呼出先 33件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00b561f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b561f8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.46% / 新版 99.46%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5770c",
      "incomplete_value": false,
      "site": "00b57710",
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
            "const:98b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b576c8",
      "incomplete_value": false,
      "site": "00b576cc",
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
            "const:a18:8"
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b57818",
      "incomplete_value": true,
      "site": "00b57824",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b577d4",
      "incomplete_value": true,
      "site": "00b577e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 41,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b57920",
      "incomplete_value": true,
      "site": "00b57930",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b578dc",
      "incomplete_value": true,
      "site": "00b578ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 52,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b57530",
      "DATA",
      [
        "storage",
        "002f8b4a",
        "switchD_00b574f4::switchdataD_002f8b4a",
        "byte"
      ]
    ],
    [
      "00b5770c",
      "PARAM",
      [
        "storage",
        "00298a18",
        null,
        "string"
      ]
    ],
    [
      "00b57818",
      "READ",
      [
        "storage",
        "010a11b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b57530",
      "DATA",
      [
        "storage",
        "002f8b4a",
        "switchD_00b57538::switchdataD_002f8b4a",
        "byte"
      ]
    ],
    [
      "00b5770c",
      "PARAM",
      [
        "storage",
        "0029898b",
        null,
        "string"
      ]
    ],
    [
      "00b57818",
      "READ",
      [
        "storage",
        "010a11f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b576cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b573f4.md#insn-00b576cc) · [`00b57710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b573f4.md#insn-00b57710) · [`00b5779c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b573f4.md#insn-00b5779c)
- 新版 `00b57710`（命令位置の公開資料なし） · `00b57754`（命令位置の公開資料なし） · `00b577e0`（命令位置の公開資料なし）

~~~diff
- 00b576cc ["INT_ADD", "register:40f0:8", ["const:b576cc:8", "const:4:8"]]
- 00b576cc ["CALL", null, ["callee:00bdde40:8"]]
+ 00b57710 ["INT_ADD", "register:40f0:8", ["const:b57710:8", "const:4:8"]]
+ 00b57710 ["CALL", null, ["callee:00bdde40:8"]]
- 00b576cc bytes c9190294
+ 00b57710 bytes cc190294
- 00b57710 ["INT_ADD", "register:40f0:8", ["const:b57710:8", "const:4:8"]]
- 00b57710 ["CALL", null, ["callee:00bddcb0:8"]]
+ 00b57754 ["INT_ADD", "register:40f0:8", ["const:b57754:8", "const:4:8"]]
+ 00b57754 ["CALL", null, ["callee:00bddcb0:8"]]
- 00b57710 bytes 54190294
+ 00b57754 bytes 57190294
- 00b5779c ["INT_ADD", "register:40f0:8", ["const:b5779c:8", "const:4:8"]]
- 00b5779c ["CALL", null, ["callee:00bde740:8"]]
+ 00b577e0 ["INT_ADD", "register:40f0:8", ["const:b577e0:8", "const:4:8"]]
+ 00b577e0 ["CALL", null, ["callee:00bde740:8"]]
- 00b5779c bytes d51b0294
+ 00b577e0 bytes d81b0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e48ee426e351c3db875b06d41ecec78d"></a>

### [`00b57b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b57b08.md) → [`00b57b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b57/00b57b4c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEPKNS0_14ConfigKeyValueEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be06a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be06a0.md) · 呼出先 21件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00b561b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b561b4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00be06f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be06f0.md) · 呼出先 21件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00b561f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b561f8.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.60% / 新版 99.60%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b57d40",
      "incomplete_value": true,
      "site": "00b57d4c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b57cfc",
      "incomplete_value": true,
      "site": "00b57d08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 19,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b57d74",
      "incomplete_value": false,
      "site": "00b57d88",
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
            "const:5a5:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b57d30",
      "incomplete_value": false,
      "site": "00b57d44",
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
            "const:639:8"
          ]
        ]
      ]
    },
    "ordinal": 22,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b57e48",
      "incomplete_value": true,
      "site": "00b57e58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b38:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b57e04",
      "incomplete_value": true,
      "site": "00b57e14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ae8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 30,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b57d40",
      "READ",
      [
        "storage",
        "010a11b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b57d74",
      "PARAM",
      [
        "storage",
        "002af639",
        null,
        "string"
      ]
    ],
    [
      "00b57e48",
      "READ",
      [
        "storage",
        "00c1bae8",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b57d40",
      "READ",
      [
        "storage",
        "010a11f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b57d74",
      "PARAM",
      [
        "storage",
        "002af5a5",
        null,
        "string"
      ]
    ],
    [
      "00b57e48",
      "READ",
      [
        "storage",
        "00c1bb38",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b57cc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b57b08.md#insn-00b57cc4) · [`00b57d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b57b08.md#insn-00b57d08) · [`00b57d44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b57/00b57b08.md#insn-00b57d44)
- 新版 `00b57d08`（命令位置の公開資料なし） · `00b57d4c`（命令位置の公開資料なし） · `00b57d88`（命令位置の公開資料なし）

~~~diff
- 00b57cc4 ["INT_ADD", "register:40f0:8", ["const:b57cc4:8", "const:4:8"]]
- 00b57cc4 ["CALL", null, ["callee:00bde740:8"]]
+ 00b57d08 ["INT_ADD", "register:40f0:8", ["const:b57d08:8", "const:4:8"]]
+ 00b57d08 ["CALL", null, ["callee:00bde740:8"]]
- 00b57cc4 bytes 8b1a0294
+ 00b57d08 bytes 8e1a0294
- 00b57d08 ["INT_ADD", "register:40f0:8", ["const:b57d08:8", "const:4:8"]]
- 00b57d08 ["CALL", null, ["callee:0047495c:8"]]
+ 00b57d4c ["INT_ADD", "register:40f0:8", ["const:b57d4c:8", "const:4:8"]]
+ 00b57d4c ["CALL", null, ["callee:0047495c:8"]]
- 00b57d08 bytes 1573e497
+ 00b57d4c bytes 0473e497
- 00b57d44 ["INT_ADD", "register:40f0:8", ["const:b57d44:8", "const:4:8"]]
- 00b57d44 ["CALL", null, ["callee:00bdee00:8"]]
+ 00b57d88 ["INT_ADD", "register:40f0:8", ["const:b57d88:8", "const:4:8"]]
+ 00b57d88 ["CALL", null, ["callee:00bdee00:8"]]
- 00b57d44 bytes 1b1c0294
+ 00b57d88 bytes 1e1c0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aaf94d9d694d189cb2de12149e3385d4"></a>

### [`00b580c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b580c4.md) → [`00b58108`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58108.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17SetConfigSettingsENS0_14ConfigSettingsE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0720.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00b5602c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b56/00b5602c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 1件 [`00be0770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0770.md) · 呼出先 15件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00b56070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b56/00b56070.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.83% / 新版 96.83%

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
      "definition_site": "00b58184",
      "incomplete_value": true,
      "site": "00b58190",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58140",
      "incomplete_value": true,
      "site": "00b5814c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2b8:8"
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
      "definition_site": "00b58188",
      "incomplete_value": true,
      "site": "00b58190",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:308:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58144",
      "incomplete_value": true,
      "site": "00b5814c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c8:8"
              ]
            ]
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
      "definition_site": "00b581fc",
      "incomplete_value": true,
      "site": "00b58208",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:310:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b581b8",
      "incomplete_value": true,
      "site": "00b581c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 9,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b58184",
      "READ",
      [
        "storage",
        "010a12b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58188",
      "READ",
      [
        "storage",
        "010a12c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b581a4",
      "READ",
      [
        "storage",
        "010a12d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b58184",
      "READ",
      [
        "storage",
        "010a12f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58188",
      "READ",
      [
        "storage",
        "010a1308",
        null,
        "undefined8"
      ]
    ],
    [
      "00b581a4",
      "READ",
      [
        "storage",
        "010a1318",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5814c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b580c4.md#insn-00b5814c) · [`00b58180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b580c4.md#insn-00b58180) · [`00b58190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b580c4.md#insn-00b58190)
- 新版 `00b58190`（命令位置の公開資料なし） · `00b581c4`（命令位置の公開資料なし） · `00b581d4`（命令位置の公開資料なし）

~~~diff
- 00b5814c ["INT_ADD", "register:40f0:8", ["const:b5814c:8", "const:4:8"]]
- 00b5814c ["CALL", null, ["callee:0056681c:8"]]
+ 00b58190 ["INT_ADD", "register:40f0:8", ["const:b58190:8", "const:4:8"]]
+ 00b58190 ["CALL", null, ["callee:0056681c:8"]]
- 00b5814c bytes b439e897
+ 00b58190 bytes a339e897
- 00b58180 ["INT_ADD", "register:40f0:8", ["const:b58180:8", "const:4:8"]]
- 00b58180 ["CALL", null, ["callee:0047495c:8"]]
+ 00b581c4 ["INT_ADD", "register:40f0:8", ["const:b581c4:8", "const:4:8"]]
+ 00b581c4 ["CALL", null, ["callee:0047495c:8"]]
- 00b58180 bytes f771e497
+ 00b581c4 bytes e671e497
- 00b58190 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:2e0:8"]]
- 00b58190 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b581d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:320:8"]]
+ 00b581d4 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b58190 bytes 027141f9
+ 00b581d4 bytes 029141f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6ff6eda8c0187e9b1e14ac8cb4a18c37"></a>

### [`00b58518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58518.md) → [`00b5855c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b5855c.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal17GetConfigSettingsEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0710.md) · 呼出先 4件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056c6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c6c4.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 1件 [`00be0760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0760.md) · 呼出先 4件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056c6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c6c4.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.83% / 新版 94.83%

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
      "definition_site": "00b58584",
      "incomplete_value": true,
      "site": "00b5858c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:238:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58540",
      "incomplete_value": true,
      "site": "00b58548",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1f8:8"
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
      "definition_site": "00b585a0",
      "incomplete_value": true,
      "site": "00b585ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5855c",
      "incomplete_value": true,
      "site": "00b58568",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:280:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b585c4",
      "incomplete_value": true,
      "site": "00b585d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:2e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58580",
      "incomplete_value": true,
      "site": "00b5858c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b58584",
      "READ",
      [
        "storage",
        "010a11f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b585a0",
      "READ",
      [
        "storage",
        "010a1280",
        null,
        "undefined8"
      ]
    ],
    [
      "00b585c4",
      "READ",
      [
        "storage",
        "010a12a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b58584",
      "READ",
      [
        "storage",
        "010a1238",
        null,
        "undefined8"
      ]
    ],
    [
      "00b585a0",
      "READ",
      [
        "storage",
        "010a12c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b585c4",
      "READ",
      [
        "storage",
        "010a12e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58548`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58518.md#insn-00b58548) · [`00b58568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58518.md#insn-00b58568) · [`00b5858c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58518.md#insn-00b5858c)
- 新版 `00b5858c`（命令位置の公開資料なし） · `00b585ac`（命令位置の公開資料なし） · `00b585d0`（命令位置の公開資料なし）

~~~diff
- 00b58548 ["INT_ADD", "register:40f0:8", ["const:b58548:8", "const:4:8"]]
- 00b58548 ["CALL", null, ["callee:0047495c:8"]]
+ 00b5858c ["INT_ADD", "register:40f0:8", ["const:b5858c:8", "const:4:8"]]
+ 00b5858c ["CALL", null, ["callee:0047495c:8"]]
- 00b58548 bytes 0571e497
+ 00b5858c bytes f470e497
- 00b58568 ["INT_ADD", "register:40f0:8", ["const:b58568:8", "const:4:8"]]
- 00b58568 ["CALL", null, ["callee:0047495c:8"]]
+ 00b585ac ["INT_ADD", "register:40f0:8", ["const:b585ac:8", "const:4:8"]]
+ 00b585ac ["CALL", null, ["callee:0047495c:8"]]
- 00b58568 bytes fd70e497
+ 00b585ac bytes ec70e497
- 00b5858c ["INT_ADD", "register:40f0:8", ["const:b5858c:8", "const:4:8"]]
- 00b5858c ["CALL", null, ["callee:0056c6c4:8"]]
+ 00b585d0 ["INT_ADD", "register:40f0:8", ["const:b585d0:8", "const:4:8"]]
+ 00b585d0 ["CALL", null, ["callee:0056c6c4:8"]]
- 00b5858c bytes 4e50e897
+ 00b585d0 bytes 3d50e897
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04b4590e1d502b5f33d676ec8739593a"></a>

### [`00b58600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58600.md) → [`00b58644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58644.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal10GetBooleanEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0690.md) · 呼出先 4件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00b586f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b586f4.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 1件 [`00be06e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be06e0.md) · 呼出先 4件 [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`00b58738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58738.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.36% / 新版 98.36%

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
      "definition_site": "00b58688",
      "incomplete_value": true,
      "site": "00b58698",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:288:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58644",
      "incomplete_value": true,
      "site": "00b58654",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:248:8"
              ]
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
      "definition_site": "00b586e4",
      "incomplete_value": false,
      "site": "00b586ec",
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
            "const:871:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b586a0",
      "incomplete_value": false,
      "site": "00b586a8",
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
            "const:873:8"
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
      "00b58688",
      "READ",
      [
        "storage",
        "010a1248",
        null,
        "undefined8"
      ]
    ],
    [
      "00b586e4",
      "PARAM",
      [
        "storage",
        "0029a873",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b58688",
      "READ",
      [
        "storage",
        "010a1288",
        null,
        "undefined8"
      ]
    ],
    [
      "00b586e4",
      "PARAM",
      [
        "storage",
        "0029a871",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58600.md#insn-00b58654) · [`00b586a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58600.md#insn-00b586a8) · [`00b58624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58600.md#insn-00b58624)
- 新版 `00b58698`（命令位置の公開資料なし） · `00b586ec`（命令位置の公開資料なし） · `00b58668`（命令位置の公開資料なし）

~~~diff
- 00b58654 ["INT_ADD", "register:40f0:8", ["const:b58654:8", "const:4:8"]]
- 00b58654 ["CALL", null, ["callee:00474b70:8"]]
+ 00b58698 ["INT_ADD", "register:40f0:8", ["const:b58698:8", "const:4:8"]]
+ 00b58698 ["CALL", null, ["callee:00474b70:8"]]
- 00b58654 bytes 4771e497
+ 00b58698 bytes 3671e497
- 00b586a8 ["INT_ADD", "register:40f0:8", ["const:b586a8:8", "const:4:8"]]
- 00b586a8 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b586ec ["INT_ADD", "register:40f0:8", ["const:b586ec:8", "const:4:8"]]
+ 00b586ec ["CALL", null, ["callee:00bdde40:8"]]
- 00b586a8 bytes d2150294
+ 00b586ec bytes d5150294
- 00b58624 ["INT_ADD", "register:40f0:8", ["const:b58624:8", "const:4:8"]]
- 00b58624 ["CALL", null, ["callee:00bde200:8"]]
+ 00b58668 ["INT_ADD", "register:40f0:8", ["const:b58668:8", "const:4:8"]]
+ 00b58668 ["CALL", null, ["callee:00bde200:8"]]
- 00b58624 bytes e3160294
+ 00b58668 bytes e6160294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7027db434131d8a3c000af02d59e17f0"></a>

### [`00b586f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b586f4.md) → [`00b58738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58738.md) FUN_00b58738

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 5件 [`00b58600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58600.md) [`00b588ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b588ac.md) [`00b589a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b589a0.md) [`00b58aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58aa0.md) [`00b58c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58c10.md) · 呼出先 4件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00553/005533e0.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 5件 [`00b58644`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58644.md) [`00b588f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b588f0.md) [`00b589e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b589e4.md) [`00b58ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58ae4.md) [`00b58c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58c54.md) · 呼出先 4件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`005533e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00553/005533e0.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.18% / 新版 98.18%

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
      "definition_site": "00b58770",
      "incomplete_value": true,
      "site": "00b58784",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:220:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5872c",
      "incomplete_value": true,
      "site": "00b58740",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e0:8"
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
      "definition_site": "00b587e4",
      "incomplete_value": false,
      "site": "00b587ec",
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
            "const:8cb:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b587a0",
      "incomplete_value": false,
      "site": "00b587a8",
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
            "const:958:8"
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
      "definition_site": "00b58838",
      "incomplete_value": true,
      "site": "00b58844",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:290:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b587f4",
      "incomplete_value": true,
      "site": "00b58800",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:250:8"
              ]
            ]
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
      "00b58770",
      "READ",
      [
        "storage",
        "010a11e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b587e4",
      "PARAM",
      [
        "storage",
        "00299958",
        null,
        "string"
      ]
    ],
    [
      "00b58838",
      "READ",
      [
        "storage",
        "010a1250",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b58770",
      "READ",
      [
        "storage",
        "010a1220",
        null,
        "undefined8"
      ]
    ],
    [
      "00b587e4",
      "PARAM",
      [
        "storage",
        "002998cb",
        null,
        "string"
      ]
    ],
    [
      "00b58838",
      "READ",
      [
        "storage",
        "010a1290",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58740`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b586f4.md#insn-00b58740) · [`00b587a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b586f4.md#insn-00b587a8) · [`00b58800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b586f4.md#insn-00b58800)
- 新版 `00b58784`（命令位置の公開資料なし） · `00b587ec`（命令位置の公開資料なし） · `00b58844`（命令位置の公開資料なし）

~~~diff
- 00b58740 ["INT_ADD", "register:40f0:8", ["const:b58740:8", "const:4:8"]]
- 00b58740 ["CALL", null, ["callee:0047495c:8"]]
+ 00b58784 ["INT_ADD", "register:40f0:8", ["const:b58784:8", "const:4:8"]]
+ 00b58784 ["CALL", null, ["callee:0047495c:8"]]
- 00b58740 bytes 8770e497
+ 00b58784 bytes 7670e497
- 00b587a8 ["INT_ADD", "register:40f0:8", ["const:b587a8:8", "const:4:8"]]
- 00b587a8 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b587ec ["INT_ADD", "register:40f0:8", ["const:b587ec:8", "const:4:8"]]
+ 00b587ec ["CALL", null, ["callee:00bdde40:8"]]
- 00b587a8 bytes 92150294
+ 00b587ec bytes 95150294
- 00b58800 ["INT_ADD", "register:40f0:8", ["const:b58800:8", "const:4:8"]]
- 00b58800 ["CALL", null, ["callee:005533e0:8"]]
+ 00b58844 ["INT_ADD", "register:40f0:8", ["const:b58844:8", "const:4:8"]]
+ 00b58844 ["CALL", null, ["callee:005533e0:8"]]
- 00b58800 bytes f8eae797
+ 00b58844 bytes e7eae797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e2e808a2feace6c571355108bec5f0c7"></a>

### [`00b589a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b589a0.md) → [`00b589e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b589e4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal9GetDoubleEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0800`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0800.md) · 呼出先 4件 [`00b586f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b586f4.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bde360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde360.md)
- 新版 呼出元 1件 [`00be0850`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0850.md) · 呼出先 4件 [`00b58738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58738.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bde3b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde3b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.44% / 新版 98.44%

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
      "definition_site": "00b58a28",
      "incomplete_value": true,
      "site": "00b58a38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:270:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b589e4",
      "incomplete_value": true,
      "site": "00b589f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:230:8"
              ]
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
      "definition_site": "00b58a84",
      "incomplete_value": false,
      "site": "00b58a8c",
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
            "const:f19:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58a40",
      "incomplete_value": false,
      "site": "00b58a48",
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
            "const:e8e:8"
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
      "00b58a28",
      "READ",
      [
        "storage",
        "010a1230",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58a84",
      "PARAM",
      [
        "storage",
        "0029de8e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b58a28",
      "READ",
      [
        "storage",
        "010a1270",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58a84",
      "PARAM",
      [
        "storage",
        "0029df19",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b589f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b589a0.md#insn-00b589f4) · [`00b58a48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b589a0.md#insn-00b58a48) · [`00b589c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b589a0.md#insn-00b589c4)
- 新版 `00b58a38`（命令位置の公開資料なし） · `00b58a8c`（命令位置の公開資料なし） · `00b58a08`（命令位置の公開資料なし）

~~~diff
- 00b589f4 ["INT_ADD", "register:40f0:8", ["const:b589f4:8", "const:4:8"]]
- 00b589f4 ["CALL", null, ["callee:00bde3b0:8"]]
+ 00b58a38 ["INT_ADD", "register:40f0:8", ["const:b58a38:8", "const:4:8"]]
+ 00b58a38 ["CALL", null, ["callee:00bde3b0:8"]]
- 00b589f4 bytes 5b160294
+ 00b58a38 bytes 5e160294
- 00b58a48 ["INT_ADD", "register:40f0:8", ["const:b58a48:8", "const:4:8"]]
- 00b58a48 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b58a8c ["INT_ADD", "register:40f0:8", ["const:b58a8c:8", "const:4:8"]]
+ 00b58a8c ["CALL", null, ["callee:00bdde40:8"]]
- 00b58a48 bytes ea140294
+ 00b58a8c bytes ed140294
- 00b589c4 ["INT_ADD", "register:40f0:8", ["const:b589c4:8", "const:4:8"]]
- 00b589c4 ["CALL", null, ["callee:00bde200:8"]]
+ 00b58a08 ["INT_ADD", "register:40f0:8", ["const:b58a08:8", "const:4:8"]]
+ 00b58a08 ["CALL", null, ["callee:00bde200:8"]]
- 00b589c4 bytes fb150294
+ 00b58a08 bytes fe150294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4b5f517fdec21ed05d71e83c178c95e"></a>

### [`00b58aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58aa0.md) → [`00b58ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58ae4.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal9GetStringEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0810`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0810.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b586f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b586f4.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 1件 [`00be0860`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0860.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b58738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58738.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.85% / 新版 98.85%

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
      "definition_site": "00b58b4c",
      "incomplete_value": true,
      "site": "00b58b58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:278:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58b08",
      "incomplete_value": true,
      "site": "00b58b14",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:238:8"
              ]
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
      "definition_site": "00b58bb4",
      "incomplete_value": false,
      "site": "00b58bbc",
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
            "const:67e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58b70",
      "incomplete_value": false,
      "site": "00b58b78",
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
            "const:70b:8"
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
      "00b58b4c",
      "READ",
      [
        "storage",
        "010a1238",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58bb4",
      "PARAM",
      [
        "storage",
        "0029970b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b58b4c",
      "READ",
      [
        "storage",
        "010a1278",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58bb4",
      "PARAM",
      [
        "storage",
        "0029967e",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b58b14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58aa0.md#insn-00b58b14) · [`00b58b78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58aa0.md#insn-00b58b78) · [`00b58ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58aa0.md#insn-00b58ae4)
- 新版 `00b58b58`（命令位置の公開資料なし） · `00b58bbc`（命令位置の公開資料なし） · `00b58b28`（命令位置の公開資料なし）

~~~diff
- 00b58b14 ["INT_ADD", "register:40f0:8", ["const:b58b14:8", "const:4:8"]]
- 00b58b14 ["CALL", null, ["callee:0047495c:8"]]
+ 00b58b58 ["INT_ADD", "register:40f0:8", ["const:b58b58:8", "const:4:8"]]
+ 00b58b58 ["CALL", null, ["callee:0047495c:8"]]
- 00b58b14 bytes 926fe497
+ 00b58b58 bytes 816fe497
- 00b58b78 ["INT_ADD", "register:40f0:8", ["const:b58b78:8", "const:4:8"]]
- 00b58b78 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b58bbc ["INT_ADD", "register:40f0:8", ["const:b58bbc:8", "const:4:8"]]
+ 00b58bbc ["CALL", null, ["callee:00bdde40:8"]]
- 00b58b78 bytes 9e140294
+ 00b58bbc bytes a1140294
- 00b58ae4 ["INT_ADD", "register:40f0:8", ["const:b58ae4:8", "const:4:8"]]
- 00b58ae4 ["CALL", null, ["callee:00bde200:8"]]
+ 00b58b28 ["INT_ADD", "register:40f0:8", ["const:b58b28:8", "const:4:8"]]
+ 00b58b28 ["CALL", null, ["callee:00bde200:8"]]
- 00b58ae4 bytes b3150294
+ 00b58b28 bytes b6150294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8ae8f7b4fc31df3ec3930d7f7323ea65"></a>

### [`00b58c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58c10.md) → [`00b58c54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58c54.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal7GetDataEPKcPNS0_9ValueInfoE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be07c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be07c0.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b586f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b586f4.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 1件 [`00be0810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0810.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b58738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b58/00b58738.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.85% / 新版 98.85%

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
      "definition_site": "00b58cbc",
      "incomplete_value": true,
      "site": "00b58cc8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:280:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b58c78",
      "incomplete_value": true,
      "site": "00b58c84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:240:8"
              ]
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
      "definition_site": "00b58d24",
      "incomplete_value": false,
      "site": "00b58d2c",
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
      "definition_site": "00b58ce0",
      "incomplete_value": false,
      "site": "00b58ce8",
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
      "00b58cbc",
      "READ",
      [
        "storage",
        "010a1240",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58d24",
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
      "00b58cbc",
      "READ",
      [
        "storage",
        "010a1280",
        null,
        "undefined8"
      ]
    ],
    [
      "00b58d24",
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

- 旧版 [`00b58c84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58c10.md#insn-00b58c84) · [`00b58ce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58c10.md#insn-00b58ce8) · [`00b58c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b58/00b58c10.md#insn-00b58c54)
- 新版 `00b58cc8`（命令位置の公開資料なし） · `00b58d2c`（命令位置の公開資料なし） · `00b58c98`（命令位置の公開資料なし）

~~~diff
- 00b58c84 ["INT_ADD", "register:40f0:8", ["const:b58c84:8", "const:4:8"]]
- 00b58c84 ["CALL", null, ["callee:0047495c:8"]]
+ 00b58cc8 ["INT_ADD", "register:40f0:8", ["const:b58cc8:8", "const:4:8"]]
+ 00b58cc8 ["CALL", null, ["callee:0047495c:8"]]
- 00b58c84 bytes 366fe497
+ 00b58cc8 bytes 256fe497
- 00b58ce8 ["INT_ADD", "register:40f0:8", ["const:b58ce8:8", "const:4:8"]]
- 00b58ce8 ["CALL", null, ["callee:00bdde40:8"]]
+ 00b58d2c ["INT_ADD", "register:40f0:8", ["const:b58d2c:8", "const:4:8"]]
+ 00b58d2c ["CALL", null, ["callee:00bdde40:8"]]
- 00b58ce8 bytes 42140294
+ 00b58d2c bytes 45140294
- 00b58c54 ["INT_ADD", "register:40f0:8", ["const:b58c54:8", "const:4:8"]]
- 00b58c54 ["CALL", null, ["callee:00bde200:8"]]
+ 00b58c98 ["INT_ADD", "register:40f0:8", ["const:b58c98:8", "const:4:8"]]
+ 00b58c98 ["CALL", null, ["callee:00bde200:8"]]
- 00b58c54 bytes 57150294
+ 00b58c98 bytes 5a150294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-38ca4857dcd3013824008c5e488088c1"></a>

### [`00b5906c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b5906c.md) → [`00b590b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b590b0.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal6GetAllEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be07a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be07a0.md) · 呼出先 26件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`0056c6c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0056c/0056c6c4.md) [`0084c0cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/0084c/0084c0cc.md) [`00bd70ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd7/00bd70ac.md)
- 新版 呼出元 1件 [`00be07f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07f0.md) · 呼出先 26件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/00474b70.md) [`0056c6c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0056c/0056c6c4.md) [`0084c0cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0084c/0084c0cc.md) [`00bd70ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bd7/00bd70ec.md)

変更の種類 call, call_argument_candidate, call_count, constant, operands_and_dependencies, operation_sequence, unresolved_call_alignment

命令の説明率　旧版 97.09% / 新版 97.09%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 9件, `unresolved_call_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 7件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b59108",
      "incomplete_value": true,
      "site": "00b59110",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:228:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b590c4",
      "incomplete_value": true,
      "site": "00b590cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:1e8:8"
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
      "definition_site": "00b59258",
      "incomplete_value": true,
      "site": "00b59268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b59214",
      "incomplete_value": true,
      "site": "00b59224",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "ordinal": 20,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b59278",
      "incomplete_value": true,
      "site": "00b59284",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:268:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b59234",
      "incomplete_value": true,
      "site": "00b59240",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:228:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 21,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b59108",
      "READ",
      [
        "storage",
        "010a11e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b59258",
      "READ",
      [
        "storage",
        "010a1218",
        null,
        "undefined8"
      ]
    ],
    [
      "00b59278",
      "READ",
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
      "00b59108",
      "READ",
      [
        "storage",
        "010a1228",
        null,
        "undefined8"
      ]
    ],
    [
      "00b59258",
      "READ",
      [
        "storage",
        "010a1258",
        null,
        "undefined8"
      ]
    ],
    [
      "00b59278",
      "READ",
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

- 旧版 [`00b590cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b5906c.md#insn-00b590cc) · [`00b591e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b5906c.md#insn-00b591e0) · [`00b59224`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b5906c.md#insn-00b59224)
- 新版 `00b59110`（命令位置の公開資料なし） · `00b59224`（命令位置の公開資料なし） · `00b59268`（命令位置の公開資料なし）

~~~diff
- 00b590cc ["INT_ADD", "register:40f0:8", ["const:b590cc:8", "const:4:8"]]
- 00b590cc ["CALL", null, ["callee:0047495c:8"]]
+ 00b59110 ["INT_ADD", "register:40f0:8", ["const:b59110:8", "const:4:8"]]
+ 00b59110 ["CALL", null, ["callee:0047495c:8"]]
- 00b590cc bytes 246ee497
+ 00b59110 bytes 136ee497
- 00b591e0 ["INT_ADD", "register:40f0:8", ["const:b591e0:8", "const:4:8"]]
- 00b591e0 ["CALL", null, ["callee:0047495c:8"]]
+ 00b59224 ["INT_ADD", "register:40f0:8", ["const:b59224:8", "const:4:8"]]
+ 00b59224 ["CALL", null, ["callee:0047495c:8"]]
- 00b591e0 bytes df6de497
+ 00b59224 bytes ce6de497
- 00b59224 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b59224 ["INT_ADD", "register:40f0:8", ["const:b59224:8", "const:4:8"]]
- 00b59224 ["CALLIND", null, ["register:0:8"]]
+ 00b59268 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b59268 ["INT_ADD", "register:40f0:8", ["const:b59268:8", "const:4:8"]]
+ 00b59268 ["CALLIND", null, ["register:0:8"]]
- 00b59224 bytes 00013fd6
+ 00b59268 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9052de19d7a8aa7d04c4358330c64efc"></a>

### [`00b59888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59888.md) → [`00b598cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b598cc.md) _ZN8firebase13remote_config8internal20RemoteConfigInternal25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17Remote

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0750.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00b5a02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a02c.md) [`00b5a664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a664.md) [`00b5a668`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a668.md)
- 新版 呼出元 1件 [`00be07a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be07a0.md) · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00b5a070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a070.md) [`00b5a6a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a6a8.md) [`00b5a6ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a6ac.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.14% / 新版 95.14%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b599dc",
      "incomplete_value": true,
      "site": "00b599ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:350:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b59998",
      "incomplete_value": true,
      "site": "00b599a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:310:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b599e0",
      "incomplete_value": true,
      "site": "00b599ec",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:360:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5999c",
      "incomplete_value": true,
      "site": "00b599a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:320:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b59a04",
      "incomplete_value": false,
      "site": "00b59a08",
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
            "const:44b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b599c0",
      "incomplete_value": false,
      "site": "00b599c4",
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
            "const:4d8:8"
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
      "00b599dc",
      "READ",
      [
        "storage",
        "010a1310",
        null,
        "undefined8"
      ]
    ],
    [
      "00b599e0",
      "READ",
      [
        "storage",
        "010a1320",
        null,
        "undefined8"
      ]
    ],
    [
      "00b59a04",
      "PARAM",
      [
        "storage",
        "002924d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b599dc",
      "READ",
      [
        "storage",
        "010a1350",
        null,
        "undefined8"
      ]
    ],
    [
      "00b599e0",
      "READ",
      [
        "storage",
        "010a1360",
        null,
        "undefined8"
      ]
    ],
    [
      "00b59a04",
      "PARAM",
      [
        "storage",
        "0029244b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b59998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59888.md#insn-00b59998) · [`00b599a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59888.md#insn-00b599a8) · [`00b599b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b59/00b59888.md#insn-00b599b4)
- 新版 `00b599dc`（命令位置の公開資料なし） · `00b599ec`（命令位置の公開資料なし） · `00b599f8`（命令位置の公開資料なし）

~~~diff
- 00b59998 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:310:8"]]
- 00b59998 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b599dc ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:350:8"]]
+ 00b599dc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b59998 bytes 018941f9
+ 00b599dc bytes 01a941f9
- 00b599a8 ["INT_ADD", "register:40f0:8", ["const:b599a8:8", "const:4:8"]]
- 00b599a8 ["CALL", null, ["callee:0056681c:8"]]
+ 00b599ec ["INT_ADD", "register:40f0:8", ["const:b599ec:8", "const:4:8"]]
+ 00b599ec ["CALL", null, ["callee:0056681c:8"]]
- 00b599a8 bytes 9d33e897
+ 00b599ec bytes 8c33e897
- 00b599b4 ["INT_ADD", "register:40f0:8", ["const:b599b4:8", "const:4:8"]]
- 00b599b4 ["CALL", null, ["callee:00bde0e0:8"]]
+ 00b599f8 ["INT_ADD", "register:40f0:8", ["const:b599f8:8", "const:4:8"]]
+ 00b599f8 ["CALL", null, ["callee:00bde0e0:8"]]
- 00b599b4 bytes b7110294
+ 00b599f8 bytes ba110294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f8b61d6f49d5ba384f43e0bb67799f6"></a>

### [`00b5a184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a184.md) → [`00b5a1c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a1c8.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIbZNS0_26CompleteWithResultInternalIbEEvRKNS_12FutureHandleEiPKcRKT_EUlPbE_EEvS5_i

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0890.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00be08e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be08e0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

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
      "definition_site": "00b5a234",
      "incomplete_value": false,
      "site": "00b5a238",
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
      "definition_site": "00b5a1f0",
      "incomplete_value": false,
      "site": "00b5a1f4",
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
      "00b5a234",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5a234",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a1f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a184.md#insn-00b5a1f4) · [`00b5a1b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a184.md#insn-00b5a1b8) · [`00b5a1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a184.md#insn-00b5a1c4)
- 新版 `00b5a238`（命令位置の公開資料なし） · `00b5a1fc`（命令位置の公開資料なし） · `00b5a208`（命令位置の公開資料なし）

~~~diff
- 00b5a1f4 ["INT_ADD", "register:40f0:8", ["const:b5a1f4:8", "const:4:8"]]
- 00b5a1f4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5a238 ["INT_ADD", "register:40f0:8", ["const:b5a238:8", "const:4:8"]]
+ 00b5a238 ["CALL", null, ["callee:00bde180:8"]]
- 00b5a1f4 bytes cf0f0294
+ 00b5a238 bytes d20f0294
- 00b5a1b8 ["INT_ADD", "register:40f0:8", ["const:b5a1b8:8", "const:4:8"]]
- 00b5a1b8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5a1fc ["INT_ADD", "register:40f0:8", ["const:b5a1fc:8", "const:4:8"]]
+ 00b5a1fc ["CALL", null, ["callee:00bddc20:8"]]
- 00b5a1b8 bytes 860e0294
+ 00b5a1fc bytes 890e0294
- 00b5a1c4 ["INT_ADD", "register:40f0:8", ["const:b5a1c4:8", "const:4:8"]]
- 00b5a1c4 ["CALL", null, ["callee:00bde000:8"]]
+ 00b5a208 ["INT_ADD", "register:40f0:8", ["const:b5a208:8", "const:4:8"]]
+ 00b5a208 ["CALL", null, ["callee:00bde000:8"]]
- 00b5a1c4 bytes 7b0f0294
+ 00b5a208 bytes 7e0f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-86b140c1676c4c7367120b5d206cbf1e"></a>

### [`00b5a468`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a468.md) → [`00b5a4ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a4ac.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIbEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be08b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be08b0.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00be0900`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0900.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.48% / 新版 98.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5a510",
      "incomplete_value": false,
      "site": "00b5a514",
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
      "definition_site": "00b5a4cc",
      "incomplete_value": false,
      "site": "00b5a4d0",
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
      "00b5a510",
      "PARAM",
      [
        "storage",
        "002974f4",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5a510",
      "PARAM",
      [
        "storage",
        "00297467",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a468.md#insn-00b5a4d0) · [`00b5a514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a468.md#insn-00b5a514) · [`00b5a494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a468.md#insn-00b5a494)
- 新版 `00b5a514`（命令位置の公開資料なし） · `00b5a558`（命令位置の公開資料なし） · `00b5a4d8`（命令位置の公開資料なし）

~~~diff
- 00b5a4d0 ["INT_ADD", "register:40f0:8", ["const:b5a4d0:8", "const:4:8"]]
- 00b5a4d0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5a514 ["INT_ADD", "register:40f0:8", ["const:b5a514:8", "const:4:8"]]
+ 00b5a514 ["CALL", null, ["callee:00bde180:8"]]
- 00b5a4d0 bytes 180f0294
+ 00b5a514 bytes 1b0f0294
- 00b5a514 ["INT_ADD", "register:40f0:8", ["const:b5a514:8", "const:4:8"]]
- 00b5a514 ["CALL", null, ["callee:00bde010:8"]]
+ 00b5a558 ["INT_ADD", "register:40f0:8", ["const:b5a558:8", "const:4:8"]]
+ 00b5a558 ["CALL", null, ["callee:00bde010:8"]]
- 00b5a514 bytes ab0e0294
+ 00b5a558 bytes ae0e0294
- 00b5a494 ["INT_ADD", "register:40f0:8", ["const:b5a494:8", "const:4:8"]]
- 00b5a494 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5a4d8 ["INT_ADD", "register:40f0:8", ["const:b5a4d8:8", "const:4:8"]]
+ 00b5a4d8 ["CALL", null, ["callee:00bddc20:8"]]
- 00b5a494 bytes cf0d0294
+ 00b5a4d8 bytes d20d0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa91f5cea8b85c196d8ed807cc7463dd"></a>

### [`00b5a614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a614.md) → [`00b5a658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a658.md) FUN_00b5a658

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 85.71% / 新版 85.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5a674",
      "incomplete_value": false,
      "site": "00b5a678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c11000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a630",
      "incomplete_value": false,
      "site": "00b5a634",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c11000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "00b5a678",
      "DATA",
      [
        "storage",
        "00c11a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b5a678",
      "DATA",
      [
        "storage",
        "00c11a80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a614.md#insn-00b5a628) · [`00b5a630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a614.md#insn-00b5a630)
- 新版 `00b5a66c`（命令位置の公開資料なし） · `00b5a674`（命令位置の公開資料なし）

~~~diff
- 00b5a628 ["INT_ADD", "register:40f0:8", ["const:b5a628:8", "const:4:8"]]
- 00b5a628 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b5a66c ["INT_ADD", "register:40f0:8", ["const:b5a66c:8", "const:4:8"]]
+ 00b5a66c ["CALL", null, ["callee:00bdb040:8"]]
- 00b5a628 bytes 72020294
+ 00b5a66c bytes 75020294
- 00b5a630 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 00b5a630 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5a630 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5a630 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5a674 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00b5a674 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5a674 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5a674 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5a630 bytes 08c12891
+ 00b5a674 bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d13ec152860c4d146a916735029bb5a"></a>

### [`00b5a64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a64c.md) → [`00b5a690`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a690.md) FUN_00b5a690

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `bounded` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5a694",
      "incomplete_value": false,
      "site": "00b5a698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c11000:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a650",
      "incomplete_value": false,
      "site": "00b5a654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:c11000:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "00b5a698",
      "DATA",
      [
        "storage",
        "00c11a30",
        null,
        "undefined *"
      ]
    ]
  ],
  "added": [
    [
      "00b5a698",
      "DATA",
      [
        "storage",
        "00c11a80",
        null,
        "undefined *"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a64c.md#insn-00b5a650)
- 新版 `00b5a694`（命令位置の公開資料なし）

~~~diff
- 00b5a650 ["COPY", "tmp:0:8", ["const:a30:8"]]
- 00b5a650 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5a650 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5a650 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5a694 ["COPY", "tmp:0:8", ["const:a80:8"]]
+ 00b5a694 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5a694 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5a694 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5a650 bytes 08c12891
+ 00b5a694 bytes 08012a91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab97fc4f0cb7ff350e5dd5a68efe8e45"></a>

### [`00b5a66c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a66c.md) → [`00b5a6b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a6b0.md) FUN_00b5a6b0

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde470.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde4c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde4c0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.30% / 新版 91.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5a6cc",
      "incomplete_value": true,
      "site": "00b5a6d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a688",
      "incomplete_value": true,
      "site": "00b5a690",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:360:8"
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
      "definition_site": "00b5a6e8",
      "incomplete_value": false,
      "site": "00b5a6ec",
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
            "const:44b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5a6a4",
      "incomplete_value": false,
      "site": "00b5a6a8",
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
            "const:4d8:8"
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
      "00b5a6cc",
      "READ",
      [
        "storage",
        "010a1360",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5a6e8",
      "PARAM",
      [
        "storage",
        "002924d8",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5a6cc",
      "READ",
      [
        "storage",
        "010a13a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5a6e8",
      "PARAM",
      [
        "storage",
        "0029244b",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a66c.md#insn-00b5a690) · [`00b5a6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a66c.md#insn-00b5a6a8) · [`00b5a67c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a66c.md#insn-00b5a67c)
- 新版 `00b5a6d4`（命令位置の公開資料なし） · `00b5a6ec`（命令位置の公開資料なし） · `00b5a6c0`（命令位置の公開資料なし）

~~~diff
- 00b5a690 ["INT_ADD", "register:40f0:8", ["const:b5a690:8", "const:4:8"]]
- 00b5a690 ["CALL", null, ["callee:00551e14:8"]]
+ 00b5a6d4 ["INT_ADD", "register:40f0:8", ["const:b5a6d4:8", "const:4:8"]]
+ 00b5a6d4 ["CALL", null, ["callee:00551e14:8"]]
- 00b5a690 bytes e1dde797
+ 00b5a6d4 bytes d0dde797
- 00b5a6a8 ["INT_ADD", "register:40f0:8", ["const:b5a6a8:8", "const:4:8"]]
- 00b5a6a8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5a6ec ["INT_ADD", "register:40f0:8", ["const:b5a6ec:8", "const:4:8"]]
+ 00b5a6ec ["CALL", null, ["callee:00bde180:8"]]
- 00b5a6a8 bytes a20e0294
+ 00b5a6ec bytes a50e0294
- 00b5a67c ["INT_ADD", "register:40f0:8", ["const:b5a67c:8", "const:4:8"]]
- 00b5a67c ["CALL", null, ["callee:00bde4c0:8"]]
+ 00b5a6c0 ["INT_ADD", "register:40f0:8", ["const:b5a6c0:8", "const:4:8"]]
+ 00b5a6c0 ["CALL", null, ["callee:00bde4c0:8"]]
- 00b5a67c bytes 7d0f0294
+ 00b5a6c0 bytes 800f0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c34c253adab07d5e2b76da7e37185b80"></a>

### [`00b5a84c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a84c.md) → [`00b5a890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a890.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationD1Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5a8ac",
      "incomplete_value": true,
      "site": "00b5a8b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b5a868",
      "incomplete_value": true,
      "site": "00b5a86c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b5a8a4",
      "READ",
      [
        "storage",
        "00c1baa8",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a8b0",
      "DATA",
      [
        "storage",
        "00c11ab0",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b5a8a4",
      "READ",
      [
        "storage",
        "00c1baf8",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a8b0",
      "DATA",
      [
        "storage",
        "00c11b00",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a84c.md#insn-00b5a860) · [`00b5a87c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a84c.md#insn-00b5a87c)
- 新版 `00b5a8a4`（命令位置の公開資料なし） · `00b5a8c0`（命令位置の公開資料なし）

~~~diff
- 00b5a860 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:aa8:8"]]
- 00b5a860 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5a8a4 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:af8:8"]]
+ 00b5a8a4 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5a860 bytes 295545f9
+ 00b5a8a4 bytes 297d45f9
- 00b5a87c ["INT_ADD", "register:40f0:8", ["const:b5a87c:8", "const:4:8"]]
- 00b5a87c ["CALL", null, ["callee:00bdddb0:8"]]
+ 00b5a8c0 ["INT_ADD", "register:40f0:8", ["const:b5a8c0:8", "const:4:8"]]
+ 00b5a8c0 ["CALL", null, ["callee:00bdddb0:8"]]
- 00b5a87c bytes 390d0294
+ 00b5a8c0 bytes 3c0d0294
~~~


<a id="compare-25dda003e9f931c8faaf0690bdfdcef8"></a>

### [`00b5a894`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a894.md) → [`00b5a8d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a8d8.md) _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationD0Ev

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bddd60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd60.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdddb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdddb0.md)

変更の種類 constant, operands_and_dependencies, store_value

命令の説明率　旧版 82.35% / 新版 82.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5a8f4",
      "incomplete_value": true,
      "site": "00b5a8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "definition_site": "00b5a8b0",
      "incomplete_value": true,
      "site": "00b5a8b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "LOAD",
            "8",
            [
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
      "00b5a8ec",
      "READ",
      [
        "storage",
        "00c1baa8",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a8f8",
      "DATA",
      [
        "storage",
        "00c11ab0",
        null,
        "undefined1[32]"
      ]
    ]
  ],
  "added": [
    [
      "00b5a8ec",
      "READ",
      [
        "storage",
        "00c1baf8",
        null,
        "pointer"
      ]
    ],
    [
      "00b5a8f8",
      "DATA",
      [
        "storage",
        "00c11b00",
        null,
        "undefined1[32]"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5a8a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a894.md#insn-00b5a8a8) · [`00b5a8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5a894.md#insn-00b5a8c4)
- 新版 `00b5a8ec`（命令位置の公開資料なし） · `00b5a908`（命令位置の公開資料なし）

~~~diff
- 00b5a8a8 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:aa8:8"]]
- 00b5a8a8 ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5a8ec ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:af8:8"]]
+ 00b5a8ec ["LOAD", "register:4048:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5a8a8 bytes 295545f9
+ 00b5a8ec bytes 297d45f9
- 00b5a8c4 ["INT_ADD", "register:40f0:8", ["const:b5a8c4:8", "const:4:8"]]
- 00b5a8c4 ["CALL", null, ["callee:00bdddb0:8"]]
+ 00b5a908 ["INT_ADD", "register:40f0:8", ["const:b5a908:8", "const:4:8"]]
+ 00b5a908 ["CALL", null, ["callee:00bdddb0:8"]]
- 00b5a8c4 bytes 270d0294
+ 00b5a908 bytes 2a0d0294
~~~


<a id="compare-275b109d24bb39d2e18fe53353606924"></a>

### [`00b5ab78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ab78.md) → [`00b5abbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5abbc.md) _ZN8firebase4auth4Auth7GetAuthEPNS_3AppEPNS_10InitResultE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bddb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb20.md) · 呼出先 8件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md)
- 新版 呼出元 1件 [`00bddb70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb70.md) · 呼出先 8件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md) [`00bde760`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde760.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.17% / 新版 99.17%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5ac08",
      "incomplete_value": true,
      "site": "00b5ac08",
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
      "definition_site": "00b5abc4",
      "incomplete_value": true,
      "site": "00b5abc4",
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
      "definition_site": "00b5abe8",
      "incomplete_value": true,
      "site": "00b5abec",
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
      "definition_site": "00b5aba4",
      "incomplete_value": true,
      "site": "00b5aba8",
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
      "definition_site": "00b5acb0",
      "incomplete_value": false,
      "site": "00b5acbc",
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
            "const:84:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ac6c",
      "incomplete_value": false,
      "site": "00b5ac78",
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
            "const:ff9:8"
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
      "00b5abd8",
      "READ",
      [
        "storage",
        "00c1bb20",
        null,
        "pointer"
      ]
    ],
    [
      "00b5abe4",
      "READ",
      [
        "storage",
        "010a13d8",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00b5abf0",
      "READ",
      [
        "storage",
        "010a13d8",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5abd8",
      "READ",
      [
        "storage",
        "00c1bb70",
        null,
        "pointer"
      ]
    ],
    [
      "00b5abe4",
      "READ",
      [
        "storage",
        "010a1418",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ],
    [
      "00b5abf0",
      "READ",
      [
        "storage",
        "010a1418",
        "_ZN8firebase4auth13g_auths_mutexE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5aba8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ab78.md#insn-00b5aba8) · [`00b5ac78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ab78.md#insn-00b5ac78) · [`00b5ab94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ab78.md#insn-00b5ab94)
- 新版 `00b5abec`（命令位置の公開資料なし） · `00b5acbc`（命令位置の公開資料なし） · `00b5abd8`（命令位置の公開資料なし）

~~~diff
- 00b5aba8 ["INT_ADD", "register:40f0:8", ["const:b5aba8:8", "const:4:8"]]
- 00b5aba8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5abec ["INT_ADD", "register:40f0:8", ["const:b5abec:8", "const:4:8"]]
+ 00b5abec ["CALL", null, ["callee:00bddc20:8"]]
- 00b5aba8 bytes 0a0c0294
+ 00b5abec bytes 0d0c0294
- 00b5ac78 ["INT_ADD", "register:40f0:8", ["const:b5ac78:8", "const:4:8"]]
- 00b5ac78 ["CALL", null, ["callee:00bde2b0:8"]]
+ 00b5acbc ["INT_ADD", "register:40f0:8", ["const:b5acbc:8", "const:4:8"]]
+ 00b5acbc ["CALL", null, ["callee:00bde2b0:8"]]
- 00b5ac78 bytes 7a0d0294
+ 00b5acbc bytes 7d0d0294
- 00b5ab94 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:b20:8"]]
- 00b5ab94 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5abd8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:b70:8"]]
+ 00b5abd8 ["LOAD", "register:40a8:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5ab94 bytes b59245f9
+ 00b5abd8 bytes b5ba45f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df8d770395827f80fc305899530fbb2d"></a>

### [`00b5ae24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ae24.md) → [`00b5ae68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5ae68.md) _ZN8firebase4auth4AuthC2EPNS_3AppEPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0a40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a40.md) · 呼出先 10件 [`00b5c440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c440.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddd40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd40.md)
- 新版 呼出元 1件 [`00be0a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a90.md) · 呼出先 10件 [`00b5c484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c484.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddd90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.53% / 新版 98.53%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5aeb8",
      "incomplete_value": false,
      "site": "00b5aebc",
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
            "const:bf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ae74",
      "incomplete_value": false,
      "site": "00b5ae78",
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
            "const:34:8"
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
      "00b5aeb8",
      "PARAM",
      [
        "storage",
        "0029f034",
        null,
        "string"
      ]
    ],
    [
      "00b5af40",
      "PARAM",
      [
        "storage",
        "00b5c440",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5aeb8",
      "PARAM",
      [
        "storage",
        "0029f0bf",
        null,
        "string"
      ]
    ],
    [
      "00b5af40",
      "PARAM",
      [
        "storage",
        "00b5c484",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ae78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ae24.md#insn-00b5ae78) · [`00b5ae58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ae24.md#insn-00b5ae58) · [`00b5ae60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ae24.md#insn-00b5ae60)
- 新版 `00b5aebc`（命令位置の公開資料なし） · `00b5ae9c`（命令位置の公開資料なし） · `00b5aea4`（命令位置の公開資料なし）

~~~diff
- 00b5ae78 ["INT_ADD", "register:40f0:8", ["const:b5ae78:8", "const:4:8"]]
- 00b5ae78 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5aebc ["INT_ADD", "register:40f0:8", ["const:b5aebc:8", "const:4:8"]]
+ 00b5aebc ["CALL", null, ["callee:00bde180:8"]]
- 00b5ae78 bytes ae0c0294
+ 00b5aebc bytes b10c0294
- 00b5ae58 ["INT_ADD", "register:40f0:8", ["const:b5ae58:8", "const:4:8"]]
- 00b5ae58 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b5ae9c ["INT_ADD", "register:40f0:8", ["const:b5ae9c:8", "const:4:8"]]
+ 00b5ae9c ["CALL", null, ["callee:00bdb040:8"]]
- 00b5ae58 bytes 66000294
+ 00b5ae9c bytes 69000294
- 00b5ae60 ["INT_ADD", "register:40f0:8", ["const:b5ae60:8", "const:4:8"]]
- 00b5ae60 ["CALL", null, ["callee:00be0aa0:8"]]
+ 00b5aea4 ["INT_ADD", "register:40f0:8", ["const:b5aea4:8", "const:4:8"]]
+ 00b5aea4 ["CALL", null, ["callee:00be0aa0:8"]]
- 00b5ae60 bytes fc160294
+ 00b5aea4 bytes ff160294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e9876781d80af6e8e370490a63e36a5"></a>

### [`00b5b490`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b490.md) → [`00b5b4d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b4d4.md) _ZN8firebase4auth4Auth3appEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a30.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00be0a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a80.md) · 呼出先 1件 [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5b4f0",
      "incomplete_value": false,
      "site": "00b5b4f4",
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
            "const:7c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b4ac",
      "incomplete_value": false,
      "site": "00b5b4b0",
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
            "const:ff1:8"
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
      "00b5b4f0",
      "PARAM",
      [
        "storage",
        "002a0ff1",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5b4f0",
      "PARAM",
      [
        "storage",
        "002a107c",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b490.md#insn-00b5b4b0) · [`00b5b4a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b490.md#insn-00b5b4a8) · [`00b5b4ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b490.md#insn-00b5b4ac)
- 新版 `00b5b4f4`（命令位置の公開資料なし） · `00b5b4ec`（命令位置の公開資料なし） · `00b5b4f0`（命令位置の公開資料なし）

~~~diff
- 00b5b4b0 ["INT_ADD", "register:40f0:8", ["const:b5b4b0:8", "const:4:8"]]
- 00b5b4b0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5b4f4 ["INT_ADD", "register:40f0:8", ["const:b5b4f4:8", "const:4:8"]]
+ 00b5b4f4 ["CALL", null, ["callee:00bde180:8"]]
- 00b5b4b0 bytes 200b0294
+ 00b5b4f4 bytes 230b0294
- 00b5b4a8 ["COPY", "register:4000:8", ["const:2a0000:8"]]
+ 00b5b4ec ["COPY", "register:4000:8", ["const:2a1000:8"]]
- 00b5b4a8 bytes 20baffb0
+ 00b5b4ec bytes 20baffd0
- 00b5b4ac ["COPY", "tmp:0:8", ["const:ff1:8"]]
- 00b5b4ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5b4ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5b4ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5b4f0 ["COPY", "tmp:0:8", ["const:7c:8"]]
+ 00b5b4f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5b4f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5b4f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5b4ac bytes 00c43f91
+ 00b5b4f0 bytes 00f00191
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a58cb52d9b87db4c3e74fbfe0492744"></a>

### [`00b5b4c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b4c8.md) → [`00b5b50c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b50c.md) _ZN8firebase4auth4Auth20AddAuthStateListenerEPNS0_17AuthStateListenerE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 6件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00be0aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0aa0.md)
- 新版 呼出元 0件  · 呼出先 6件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00be0af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0af0.md)

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
      "definition_site": "00b5b684",
      "incomplete_value": false,
      "site": "00b5b688",
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
            "const:f8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b640",
      "incomplete_value": false,
      "site": "00b5b644",
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
            "const:ef0:8"
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
      "00b5b684",
      "PARAM",
      [
        "storage",
        "002a7ef0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5b684",
      "PARAM",
      [
        "storage",
        "002a7f8a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b644`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b4c8.md#insn-00b5b644) · [`00b5b504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b4c8.md#insn-00b5b504) · [`00b5b588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b4c8.md#insn-00b5b588)
- 新版 `00b5b688`（命令位置の公開資料なし） · `00b5b548`（命令位置の公開資料なし） · `00b5b5cc`（命令位置の公開資料なし）

~~~diff
- 00b5b644 ["INT_ADD", "register:40f0:8", ["const:b5b644:8", "const:4:8"]]
- 00b5b644 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5b688 ["INT_ADD", "register:40f0:8", ["const:b5b688:8", "const:4:8"]]
+ 00b5b688 ["CALL", null, ["callee:00bde180:8"]]
- 00b5b644 bytes bb0a0294
+ 00b5b688 bytes be0a0294
- 00b5b504 ["INT_ADD", "register:40f0:8", ["const:b5b504:8", "const:4:8"]]
- 00b5b504 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5b548 ["INT_ADD", "register:40f0:8", ["const:b5b548:8", "const:4:8"]]
+ 00b5b548 ["CALL", null, ["callee:00bddc20:8"]]
- 00b5b504 bytes b3090294
+ 00b5b548 bytes b6090294
- 00b5b588 ["INT_ADD", "register:40f0:8", ["const:b5b588:8", "const:4:8"]]
- 00b5b588 ["CALL", null, ["callee:00be0af0:8"]]
+ 00b5b5cc ["INT_ADD", "register:40f0:8", ["const:b5b5cc:8", "const:4:8"]]
+ 00b5b5cc ["CALL", null, ["callee:00be0af0:8"]]
- 00b5b588 bytes 46150294
+ 00b5b5cc bytes 49150294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-65d6f0f489a62e44cb428cb4bee41a1a"></a>

### [`00b5b698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b698.md) → [`00b5b6dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b6dc.md) _ZN8firebase4auth4Auth18AddIdTokenListenerEPNS0_15IdTokenListenerE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 7件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00be0990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0990.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00be09e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09e0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 99.10% / 新版 99.10%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5b85c",
      "incomplete_value": false,
      "site": "00b5b860",
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
            "const:f8a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5b818",
      "incomplete_value": false,
      "site": "00b5b81c",
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
            "const:ef0:8"
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
      "00b5b85c",
      "PARAM",
      [
        "storage",
        "002a7ef0",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5b85c",
      "PARAM",
      [
        "storage",
        "002a7f8a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5b81c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b698.md#insn-00b5b81c) · [`00b5b6d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b698.md#insn-00b5b6d4) · [`00b5b758`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5b698.md#insn-00b5b758)
- 新版 `00b5b860`（命令位置の公開資料なし） · `00b5b718`（命令位置の公開資料なし） · `00b5b79c`（命令位置の公開資料なし）

~~~diff
- 00b5b81c ["INT_ADD", "register:40f0:8", ["const:b5b81c:8", "const:4:8"]]
- 00b5b81c ["CALL", null, ["callee:00bde180:8"]]
+ 00b5b860 ["INT_ADD", "register:40f0:8", ["const:b5b860:8", "const:4:8"]]
+ 00b5b860 ["CALL", null, ["callee:00bde180:8"]]
- 00b5b81c bytes 450a0294
+ 00b5b860 bytes 480a0294
- 00b5b6d4 ["INT_ADD", "register:40f0:8", ["const:b5b6d4:8", "const:4:8"]]
- 00b5b6d4 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5b718 ["INT_ADD", "register:40f0:8", ["const:b5b718:8", "const:4:8"]]
+ 00b5b718 ["CALL", null, ["callee:00bddc20:8"]]
- 00b5b6d4 bytes 3f090294
+ 00b5b718 bytes 42090294
- 00b5b758 ["INT_ADD", "register:40f0:8", ["const:b5b758:8", "const:4:8"]]
- 00b5b758 ["CALL", null, ["callee:00be0ad0:8"]]
+ 00b5b79c ["INT_ADD", "register:40f0:8", ["const:b5b79c:8", "const:4:8"]]
+ 00b5b79c ["CALL", null, ["callee:00be0ad0:8"]]
- 00b5b758 bytes ca140294
+ 00b5b79c bytes cd140294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8875ef0737114d021d29ea0c97ed8a7"></a>

### [`00b5be10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5be10.md) → [`00b5be54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5be54.md) _ZN8firebase4auth22NotifyIdTokenListenersEPNS0_8AuthDataE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be09a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09a0.md) · 呼出先 6件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md)
- 新版 呼出元 1件 [`00be09f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09f0.md) · 呼出先 6件 [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.68% / 新版 98.68%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5bea4",
      "incomplete_value": false,
      "site": "00b5bea8",
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
            "const:5d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5be60",
      "incomplete_value": false,
      "site": "00b5be64",
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
            "const:665:8"
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
      "00b5bea4",
      "PARAM",
      [
        "storage",
        "00296665",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5bea4",
      "PARAM",
      [
        "storage",
        "002965d8",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5be64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5be10.md#insn-00b5be64) · [`00b5be3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5be10.md#insn-00b5be3c) · [`00b5be4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5b/00b5be10.md#insn-00b5be4c)
- 新版 `00b5bea8`（命令位置の公開資料なし） · `00b5be80`（命令位置の公開資料なし） · `00b5be90`（命令位置の公開資料なし）

~~~diff
- 00b5be64 ["INT_ADD", "register:40f0:8", ["const:b5be64:8", "const:4:8"]]
- 00b5be64 ["CALL", null, ["callee:00bde2b0:8"]]
+ 00b5bea8 ["INT_ADD", "register:40f0:8", ["const:b5bea8:8", "const:4:8"]]
+ 00b5bea8 ["CALL", null, ["callee:00bde2b0:8"]]
- 00b5be64 bytes ff080294
+ 00b5bea8 bytes 02090294
- 00b5be3c ["INT_ADD", "register:40f0:8", ["const:b5be3c:8", "const:4:8"]]
- 00b5be3c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b5be80 ["INT_ADD", "register:40f0:8", ["const:b5be80:8", "const:4:8"]]
+ 00b5be80 ["CALL", null, ["callee:00bddc20:8"]]
- 00b5be3c bytes 65070294
+ 00b5be80 bytes 68070294
- 00b5be4c ["INT_ADD", "register:40f0:8", ["const:b5be4c:8", "const:4:8"]]
- 00b5be4c ["CALL", null, ["callee:00be0ae0:8"]]
+ 00b5be90 ["INT_ADD", "register:40f0:8", ["const:b5be90:8", "const:4:8"]]
+ 00b5be90 ["CALL", null, ["callee:00be0ae0:8"]]
- 00b5be4c bytes 11130294
+ 00b5be90 bytes 14130294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f39f53a97a179a9413adc777b722f7b"></a>

### [`00b5c440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c440.md) → [`00b5c484`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c484.md) FUN_00b5c484

採用 · 移動量 `+0x44` · 根拠 `code_order_and_references` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00b5ae24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ae24.md) · 呼出先 2件 [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00be09e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09e0.md)
- 新版 呼出元 1件 [`00b5ae68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5ae68.md) · 呼出先 2件 [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00be0a30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c49c",
      "incomplete_value": false,
      "site": "00b5c4a8",
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
            "const:279:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c458",
      "incomplete_value": false,
      "site": "00b5c464",
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
            "const:306:8"
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
      "00b5c49c",
      "PARAM",
      [
        "storage",
        "00294306",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5c49c",
      "PARAM",
      [
        "storage",
        "00294279",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c440.md#insn-00b5c464) · [`00b5c458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c440.md#insn-00b5c458)
- 新版 `00b5c4a8`（命令位置の公開資料なし） · `00b5c49c`（命令位置の公開資料なし）

~~~diff
- 00b5c464 ["INT_ADD", "register:40f0:8", ["const:b5c464:8", "const:4:8"]]
- 00b5c464 ["CALL", null, ["callee:00bddf60:8"]]
+ 00b5c4a8 ["INT_ADD", "register:40f0:8", ["const:b5c4a8:8", "const:4:8"]]
+ 00b5c4a8 ["CALL", null, ["callee:00bddf60:8"]]
- 00b5c464 bytes ab060294
+ 00b5c4a8 bytes ae060294
- 00b5c458 ["COPY", "tmp:0:8", ["const:306:8"]]
- 00b5c458 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c458 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c458 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5c49c ["COPY", "tmp:0:8", ["const:279:8"]]
+ 00b5c49c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5c49c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5c49c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5c458 bytes 00180c91
+ 00b5c49c bytes 00e40991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1600cf4c4bbe70873a8bf462798e4b3e"></a>

### [`00b5c4b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c4b8.md) → [`00b5c4fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c4fc.md) _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0aa0.md) · 呼出先 5件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)
- 新版 呼出元 1件 [`00be0af0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0af0.md) · 呼出先 5件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c564",
      "incomplete_value": false,
      "site": "00b5c568",
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
      "definition_site": "00b5c520",
      "incomplete_value": false,
      "site": "00b5c524",
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
      "00b5c564",
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
      "00b5c564",
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

- 旧版 [`00b5c524`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c4b8.md#insn-00b5c524) · [`00b5c520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c4b8.md#insn-00b5c520) · [`00b5c530`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c4b8.md#insn-00b5c530)
- 新版 `00b5c568`（命令位置の公開資料なし） · `00b5c564`（命令位置の公開資料なし） · `00b5c574`（命令位置の公開資料なし）

~~~diff
- 00b5c524 ["INT_ADD", "register:40f0:8", ["const:b5c524:8", "const:4:8"]]
- 00b5c524 ["CALL", null, ["callee:00ae04c0:8"]]
+ 00b5c568 ["INT_ADD", "register:40f0:8", ["const:b5c568:8", "const:4:8"]]
+ 00b5c568 ["CALL", null, ["callee:00ae04c0:8"]]
- 00b5c524 bytes d60ffe97
+ 00b5c568 bytes d60ffe97
- 00b5c520 ["COPY", "tmp:0:8", ["const:87d:8"]]
- 00b5c520 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c520 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c520 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5c564 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 00b5c564 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5c564 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5c564 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5c520 bytes 00f42191
+ 00b5c564 bytes 00c01f91
- 00b5c530 ["INT_ADD", "register:40f0:8", ["const:b5c530:8", "const:4:8"]]
- 00b5c530 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b5c574 ["INT_ADD", "register:40f0:8", ["const:b5c574:8", "const:4:8"]]
+ 00b5c574 ["CALL", null, ["callee:00bdb040:8"]]
- 00b5c530 bytes b0fa0194
+ 00b5c574 bytes b3fa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1d7b594cf89902ee60a4fa09e4f49351"></a>

### [`00b5c5b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c5b0.md) → [`00b5c5f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c5f4.md) _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ac0.md) · 呼出先 5件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)
- 新版 呼出元 1件 [`00be0b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0b10.md) · 呼出先 5件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c65c",
      "incomplete_value": false,
      "site": "00b5c660",
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
      "definition_site": "00b5c618",
      "incomplete_value": false,
      "site": "00b5c61c",
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
      "00b5c65c",
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
      "00b5c65c",
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

- 旧版 [`00b5c61c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c5b0.md#insn-00b5c61c) · [`00b5c618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c5b0.md#insn-00b5c618) · [`00b5c628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c5b0.md#insn-00b5c628)
- 新版 `00b5c660`（命令位置の公開資料なし） · `00b5c65c`（命令位置の公開資料なし） · `00b5c66c`（命令位置の公開資料なし）

~~~diff
- 00b5c61c ["INT_ADD", "register:40f0:8", ["const:b5c61c:8", "const:4:8"]]
- 00b5c61c ["CALL", null, ["callee:00ae04c0:8"]]
+ 00b5c660 ["INT_ADD", "register:40f0:8", ["const:b5c660:8", "const:4:8"]]
+ 00b5c660 ["CALL", null, ["callee:00ae04c0:8"]]
- 00b5c61c bytes 980ffe97
+ 00b5c660 bytes 980ffe97
- 00b5c618 ["COPY", "tmp:0:8", ["const:87d:8"]]
- 00b5c618 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c618 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c618 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5c65c ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 00b5c65c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5c65c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5c65c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5c618 bytes 00f42191
+ 00b5c65c bytes 00c01f91
- 00b5c628 ["INT_ADD", "register:40f0:8", ["const:b5c628:8", "const:4:8"]]
- 00b5c628 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b5c66c ["INT_ADD", "register:40f0:8", ["const:b5c66c:8", "const:4:8"]]
+ 00b5c66c ["CALL", null, ["callee:00bdb040:8"]]
- 00b5c628 bytes 72fa0194
+ 00b5c66c bytes 75fa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39d357848cccfe053cfb99475ed4c1e7"></a>

### [`00b5c6a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c6a8.md) → [`00b5c6ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c6ec.md) _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a80.md) · 呼出先 5件 [`00ae047c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae047c.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md) [`00bdde60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde60.md)
- 新版 呼出元 1件 [`00be0ad0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ad0.md) · 呼出先 5件 [`00ae04c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae04c0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb1b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb1b0.md) [`00bddeb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddeb0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.39% / 新版 98.39%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5c754",
      "incomplete_value": false,
      "site": "00b5c758",
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
      "definition_site": "00b5c710",
      "incomplete_value": false,
      "site": "00b5c714",
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
      "00b5c754",
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
      "00b5c754",
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

- 旧版 [`00b5c714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c6a8.md#insn-00b5c714) · [`00b5c710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c6a8.md#insn-00b5c710) · [`00b5c720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c6a8.md#insn-00b5c720)
- 新版 `00b5c758`（命令位置の公開資料なし） · `00b5c754`（命令位置の公開資料なし） · `00b5c764`（命令位置の公開資料なし）

~~~diff
- 00b5c714 ["INT_ADD", "register:40f0:8", ["const:b5c714:8", "const:4:8"]]
- 00b5c714 ["CALL", null, ["callee:00ae04c0:8"]]
+ 00b5c758 ["INT_ADD", "register:40f0:8", ["const:b5c758:8", "const:4:8"]]
+ 00b5c758 ["CALL", null, ["callee:00ae04c0:8"]]
- 00b5c714 bytes 5a0ffe97
+ 00b5c758 bytes 5a0ffe97
- 00b5c710 ["COPY", "tmp:0:8", ["const:87d:8"]]
- 00b5c710 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c710 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c710 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5c754 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 00b5c754 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5c754 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5c754 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5c710 bytes 00f42191
+ 00b5c754 bytes 00c01f91
- 00b5c720 ["INT_ADD", "register:40f0:8", ["const:b5c720:8", "const:4:8"]]
- 00b5c720 ["CALL", null, ["callee:00bdb040:8"]]
+ 00b5c764 ["INT_ADD", "register:40f0:8", ["const:b5c764:8", "const:4:8"]]
+ 00b5c764 ["CALL", null, ["callee:00bdb040:8"]]
- 00b5c720 bytes 34fa0194
+ 00b5c764 bytes 37fa0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e0f900abdccb2e2a5a3e6787834c1c3"></a>

### [`00b5c7a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c7a0.md) → [`00b5c7e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c7e4.md) _INIT_281

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 7件 [`00b5ab64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ab64.md) [`00b5ab6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ab6c.md) [`00b5ab70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5a/00b5ab70.md) [`00bdaf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf90.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md)
- 新版 呼出元 0件  · 呼出先 7件 [`00b5aba8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5aba8.md) [`00b5abb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5abb0.md) [`00b5abb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5abb4.md) [`00bdafe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdafe0.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination, store_value

命令の説明率　旧版 78.38% / 新版 78.38%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 4件, `store_value` 2件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_destination` 4件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5c810",
      "incomplete_value": true,
      "site": "00b5c810",
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
            "const:3e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c7cc",
      "incomplete_value": true,
      "site": "00b5c7cc",
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
            "const:3a0:8"
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
      "definition_site": "00b5c810",
      "incomplete_value": true,
      "site": "00b5c810",
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
                "const:3e0:8"
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
      "definition_site": "00b5c7cc",
      "incomplete_value": true,
      "site": "00b5c7cc",
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
                "const:3a0:8"
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "bounded",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5c810",
      "incomplete_value": false,
      "site": "00b5c810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b5a000:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c7cc",
      "incomplete_value": false,
      "site": "00b5c7cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:b5a000:8"
          ],
          [
            "leaf",
            "const:b64:8"
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
      "00b5c800",
      "PARAM",
      [
        "storage",
        "010a13a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5c810",
      "WRITE",
      [
        "storage",
        "010a13a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5c810",
      "WRITE",
      [
        "storage",
        "010a13a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5c800",
      "PARAM",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5c810",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5c810",
      "WRITE",
      [
        "storage",
        "010a13e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c7bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c7a0.md#insn-00b5c7bc) · [`00b5c7d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c7a0.md#insn-00b5c7d8) · [`00b5c804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c7a0.md#insn-00b5c804)
- 新版 `00b5c800`（命令位置の公開資料なし） · `00b5c81c`（命令位置の公開資料なし） · `00b5c848`（命令位置の公開資料なし）

~~~diff
- 00b5c7bc ["COPY", "tmp:0:8", ["const:3a0:8"]]
- 00b5c7bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c7bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5c7bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5c800 ["COPY", "tmp:0:8", ["const:3e0:8"]]
+ 00b5c800 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5c800 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5c800 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5c7bc bytes 00800e91
+ 00b5c800 bytes 00800f91
- 00b5c7d8 ["INT_ADD", "register:40f0:8", ["const:b5c7d8:8", "const:4:8"]]
- 00b5c7d8 ["CALL", null, ["callee:00bddd60:8"]]
+ 00b5c81c ["INT_ADD", "register:40f0:8", ["const:b5c81c:8", "const:4:8"]]
+ 00b5c81c ["CALL", null, ["callee:00bddd60:8"]]
- 00b5c7d8 bytes 4e050294
+ 00b5c81c bytes 51050294
- 00b5c804 ["INT_ADD", "register:40f0:8", ["const:b5c804:8", "const:4:8"]]
- 00b5c804 ["CALL", null, ["callee:00bdafe0:8"]]
+ 00b5c848 ["INT_ADD", "register:40f0:8", ["const:b5c848:8", "const:4:8"]]
+ 00b5c848 ["CALL", null, ["callee:00bdafe0:8"]]
- 00b5c804 bytes e3f90194
+ 00b5c848 bytes e6f90194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

