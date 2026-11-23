# v15.7.3 → v15.7.4 · 最優先の変更候補 (61)

[一覧の目次](README.md)

<a id="compare-d2cf1b6c8f0fdec0c658a30edb764e4f"></a>

### [`00ae0834`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0834.md) → [`00ae0878`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0878.md) _ZN8firebase9analytics9analytics13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae08b8",
      "incomplete_value": true,
      "site": "00ae08b8",
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
            "const:70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0874",
      "incomplete_value": true,
      "site": "00ae0874",
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
            "const:30:8"
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
      "definition_site": "00ae0894",
      "incomplete_value": true,
      "site": "00ae0894",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0850",
      "incomplete_value": true,
      "site": "00ae0850",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae089c",
      "incomplete_value": false,
      "site": "00ae08b0",
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
            "const:432:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0858",
      "incomplete_value": false,
      "site": "00ae086c",
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
            "const:4bf:8"
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
      "00ae088c",
      "READ",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae089c",
      "PARAM",
      [
        "storage",
        "002974bf",
        null,
        "string"
      ]
    ],
    [
      "00ae08b8",
      "WRITE",
      [
        "storage",
        "010a0030",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae088c",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae089c",
      "PARAM",
      [
        "storage",
        "00297432",
        null,
        "string"
      ]
    ],
    [
      "00ae08b8",
      "WRITE",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae086c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0834.md#insn-00ae086c) · [`00ae0874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0834.md#insn-00ae0874) · [`00ae0848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0834.md#insn-00ae0848)
- 新版 [`00ae08b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0878.md#insn-00ae08b0) · [`00ae08b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0878.md#insn-00ae08b8) · [`00ae088c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0878.md#insn-00ae088c)

~~~diff
- 00ae086c ["INT_ADD", "register:40f0:8", ["const:ae086c:8", "const:4:8"]]
- 00ae086c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae08b0 ["INT_ADD", "register:40f0:8", ["const:ae08b0:8", "const:4:8"]]
+ 00ae08b0 ["CALL", null, ["callee:00bde090:8"]]
- 00ae086c bytes f5f50394
+ 00ae08b0 bytes f8f50394
- 00ae0874 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:30:8"]]
- 00ae0874 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae08b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:70:8"]]
+ 00ae08b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0874 bytes 801a00f9
+ 00ae08b8 bytes 803a00f9
- 00ae0848 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:30:8"]]
- 00ae0848 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae088c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:70:8"]]
+ 00ae088c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0848 bytes 811a40f9
+ 00ae088c bytes 813a40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4be032655d4e3de7c999ff80c5c66d17"></a>

### [`00ae08a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae08a4.md) → [`00ae08e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae08e8.md) _ZN8firebase9analytics9analytics10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae0904",
      "incomplete_value": false,
      "site": "00ae0908",
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
      "definition_site": "00ae08c0",
      "incomplete_value": false,
      "site": "00ae08c4",
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
      "definition_site": "00ae0914",
      "incomplete_value": true,
      "site": "00ae0920",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae08d0",
      "incomplete_value": true,
      "site": "00ae08dc",
      "value": [
        "LOAD",
        "8",
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
      "00ae0904",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae0914",
      "DATA",
      [
        "storage",
        "010a0098",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae0904",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae0914",
      "DATA",
      [
        "storage",
        "010a00d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae08c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae08a4.md#insn-00ae08c4) · [`00ae08c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae08a4.md#insn-00ae08c0) · [`00ae08cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae08a4.md#insn-00ae08cc)
- 新版 [`00ae0908`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae08e8.md#insn-00ae0908) · [`00ae0904`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae08e8.md#insn-00ae0904) · [`00ae0910`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae08e8.md#insn-00ae0910)

~~~diff
- 00ae08c4 ["INT_ADD", "register:40f0:8", ["const:ae08c4:8", "const:4:8"]]
- 00ae08c4 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae0908 ["INT_ADD", "register:40f0:8", ["const:ae0908:8", "const:4:8"]]
+ 00ae0908 ["CALL", null, ["callee:00bde180:8"]]
- 00ae08c4 bytes 1bf60394
+ 00ae0908 bytes 1ef60394
- 00ae08c0 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae08c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae08c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae08c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae0904 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae0904 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae0904 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae0904 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae08c0 bytes 00fc1991
+ 00ae0904 bytes 00c81791
- 00ae08cc ["COPY", "tmp:0:8", ["const:98:8"]]
- 00ae08cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae08cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae08cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae0910 ["COPY", "tmp:0:8", ["const:d8:8"]]
+ 00ae0910 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae0910 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae0910 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae08cc bytes 08610291
+ 00ae0910 bytes 08610391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c186f4f218ad1db07a731d6b1c8b9316"></a>

### [`00ae08e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae08e0.md) → [`00ae0924`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0924.md) _ZN8firebase9analytics22analytics_consent_type19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

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
      "definition_site": "00ae0950",
      "incomplete_value": true,
      "site": "00ae0950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae090c",
      "incomplete_value": true,
      "site": "00ae090c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a0:8"
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
      "definition_site": "00ae0938",
      "incomplete_value": true,
      "site": "00ae0938",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae08f4",
      "incomplete_value": true,
      "site": "00ae08f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae0944",
      "incomplete_value": false,
      "site": "00ae0948",
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
            "const:e49:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0900",
      "incomplete_value": false,
      "site": "00ae0904",
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
            "const:dbe:8"
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
      "00ae0934",
      "READ",
      [
        "storage",
        "010a00a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0944",
      "PARAM",
      [
        "storage",
        "002a1dbe",
        null,
        "string"
      ]
    ],
    [
      "00ae0950",
      "WRITE",
      [
        "storage",
        "010a00a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae0934",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0944",
      "PARAM",
      [
        "storage",
        "002a1e49",
        null,
        "string"
      ]
    ],
    [
      "00ae0950",
      "WRITE",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae08e0.md#insn-00ae0904) · [`00ae090c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae08e0.md#insn-00ae090c) · [`00ae08f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae08e0.md#insn-00ae08f0)
- 新版 [`00ae0948`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0924.md#insn-00ae0948) · [`00ae0950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0924.md#insn-00ae0950) · [`00ae0934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0924.md#insn-00ae0934)

~~~diff
- 00ae0904 ["INT_ADD", "register:40f0:8", ["const:ae0904:8", "const:4:8"]]
- 00ae0904 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae0948 ["INT_ADD", "register:40f0:8", ["const:ae0948:8", "const:4:8"]]
+ 00ae0948 ["CALL", null, ["callee:00bde090:8"]]
- 00ae0904 bytes cff50394
+ 00ae0948 bytes d2f50394
- 00ae090c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a0:8"]]
- 00ae090c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae0950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e0:8"]]
+ 00ae0950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae090c bytes 605200f9
+ 00ae0950 bytes 607200f9
- 00ae08f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a0:8"]]
- 00ae08f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0934 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e0:8"]]
+ 00ae0934 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae08f0 bytes 685240f9
+ 00ae0934 bytes 687240f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8aef2d8c5f53afd34246eb146bdac719"></a>

### [`00ae0920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0920.md) → [`00ae0964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0964.md) _ZN8firebase9analytics22analytics_consent_type19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

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
      "definition_site": "00ae0990",
      "incomplete_value": true,
      "site": "00ae0990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae094c",
      "incomplete_value": true,
      "site": "00ae094c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a0:8"
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
      "definition_site": "00ae0978",
      "incomplete_value": true,
      "site": "00ae0978",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0934",
      "incomplete_value": true,
      "site": "00ae0934",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae0980",
      "incomplete_value": false,
      "site": "00ae0988",
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
            "const:e49:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae093c",
      "incomplete_value": false,
      "site": "00ae0944",
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
            "const:dbe:8"
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
      "00ae0974",
      "READ",
      [
        "storage",
        "010a00a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0980",
      "PARAM",
      [
        "storage",
        "002a1dbe",
        null,
        "string"
      ]
    ],
    [
      "00ae0990",
      "WRITE",
      [
        "storage",
        "010a00a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae0974",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0980",
      "PARAM",
      [
        "storage",
        "002a1e49",
        null,
        "string"
      ]
    ],
    [
      "00ae0990",
      "WRITE",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0920.md#insn-00ae0944) · [`00ae094c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0920.md#insn-00ae094c) · [`00ae0930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0920.md#insn-00ae0930)
- 新版 [`00ae0988`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0964.md#insn-00ae0988) · [`00ae0990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0964.md#insn-00ae0990) · [`00ae0974`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0964.md#insn-00ae0974)

~~~diff
- 00ae0944 ["INT_ADD", "register:40f0:8", ["const:ae0944:8", "const:4:8"]]
- 00ae0944 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae0988 ["INT_ADD", "register:40f0:8", ["const:ae0988:8", "const:4:8"]]
+ 00ae0988 ["CALL", null, ["callee:00bde090:8"]]
- 00ae0944 bytes bff50394
+ 00ae0988 bytes c2f50394
- 00ae094c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a0:8"]]
- 00ae094c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae0990 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e0:8"]]
+ 00ae0990 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae094c bytes 605200f9
+ 00ae0990 bytes 607200f9
- 00ae0930 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a0:8"]]
- 00ae0930 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0974 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e0:8"]]
+ 00ae0974 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0930 bytes 685240f9
+ 00ae0974 bytes 687240f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bb1f7ddd5dc58d63b9e0f6dba788849"></a>

### [`00ae0960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0960.md) → [`00ae09a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09a4.md) _ZN8firebase9analytics22analytics_consent_type10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00ae09d4",
      "incomplete_value": true,
      "site": "00ae09d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0990",
      "incomplete_value": true,
      "site": "00ae0990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a0:8"
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
      "definition_site": "00ae09b8",
      "incomplete_value": true,
      "site": "00ae09b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0974",
      "incomplete_value": true,
      "site": "00ae0974",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae09c4",
      "incomplete_value": false,
      "site": "00ae09cc",
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
            "const:e49:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0980",
      "incomplete_value": false,
      "site": "00ae0988",
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
            "const:dbe:8"
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
      "00ae09b4",
      "READ",
      [
        "storage",
        "010a00a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae09c4",
      "PARAM",
      [
        "storage",
        "002a1dbe",
        null,
        "string"
      ]
    ],
    [
      "00ae09d4",
      "WRITE",
      [
        "storage",
        "010a00a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae09b4",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae09c4",
      "PARAM",
      [
        "storage",
        "002a1e49",
        null,
        "string"
      ]
    ],
    [
      "00ae09d4",
      "WRITE",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0960.md#insn-00ae0988) · [`00ae0990`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0960.md#insn-00ae0990) · [`00ae0970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0960.md#insn-00ae0970)
- 新版 [`00ae09cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09a4.md#insn-00ae09cc) · [`00ae09d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09a4.md#insn-00ae09d4) · [`00ae09b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09a4.md#insn-00ae09b4)

~~~diff
- 00ae0988 ["INT_ADD", "register:40f0:8", ["const:ae0988:8", "const:4:8"]]
- 00ae0988 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae09cc ["INT_ADD", "register:40f0:8", ["const:ae09cc:8", "const:4:8"]]
+ 00ae09cc ["CALL", null, ["callee:00bde090:8"]]
- 00ae0988 bytes aef50394
+ 00ae09cc bytes b1f50394
- 00ae0990 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a0:8"]]
- 00ae0990 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae09d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e0:8"]]
+ 00ae09d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0990 bytes 605200f9
+ 00ae09d4 bytes 607200f9
- 00ae0970 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a0:8"]]
- 00ae0970 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae09b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e0:8"]]
+ 00ae09b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0970 bytes 685240f9
+ 00ae09b4 bytes 687240f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54107b75c92e20e525cc6d79b94300fb"></a>

### [`00ae09a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae09a4.md) → [`00ae09e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09e8.md) _ZN8firebase9analytics22analytics_consent_type10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae0a18",
      "incomplete_value": true,
      "site": "00ae0a18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae09d4",
      "incomplete_value": true,
      "site": "00ae09d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a0:8"
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
      "definition_site": "00ae09fc",
      "incomplete_value": true,
      "site": "00ae09fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae09b8",
      "incomplete_value": true,
      "site": "00ae09b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae0a04",
      "incomplete_value": false,
      "site": "00ae0a10",
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
            "const:e49:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae09c0",
      "incomplete_value": false,
      "site": "00ae09cc",
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
            "const:dbe:8"
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
      "00ae09f8",
      "READ",
      [
        "storage",
        "010a00a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0a04",
      "PARAM",
      [
        "storage",
        "002a1dbe",
        null,
        "string"
      ]
    ],
    [
      "00ae0a18",
      "WRITE",
      [
        "storage",
        "010a00a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae09f8",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0a04",
      "PARAM",
      [
        "storage",
        "002a1e49",
        null,
        "string"
      ]
    ],
    [
      "00ae0a18",
      "WRITE",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae09cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae09a4.md#insn-00ae09cc) · [`00ae09d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae09a4.md#insn-00ae09d4) · [`00ae09b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae09a4.md#insn-00ae09b4)
- 新版 [`00ae0a10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09e8.md#insn-00ae0a10) · [`00ae0a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09e8.md#insn-00ae0a18) · [`00ae09f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae09e8.md#insn-00ae09f8)

~~~diff
- 00ae09cc ["INT_ADD", "register:40f0:8", ["const:ae09cc:8", "const:4:8"]]
- 00ae09cc ["CALL", null, ["callee:00bde090:8"]]
+ 00ae0a10 ["INT_ADD", "register:40f0:8", ["const:ae0a10:8", "const:4:8"]]
+ 00ae0a10 ["CALL", null, ["callee:00bde090:8"]]
- 00ae09cc bytes 9df50394
+ 00ae0a10 bytes a0f50394
- 00ae09d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a0:8"]]
- 00ae09d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae0a18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e0:8"]]
+ 00ae0a18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae09d4 bytes 605200f9
+ 00ae0a18 bytes 607200f9
- 00ae09b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a0:8"]]
- 00ae09b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae09f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:e0:8"]]
+ 00ae09f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae09b4 bytes 685240f9
+ 00ae09f8 bytes 687240f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96e1051d9d1223f5cfe97c6f3f53aa36"></a>

### [`00ae09f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae09f4.md) → [`00ae0a38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0a38.md) _ZN8firebase9analytics22analytics_consent_type15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae0a90",
      "incomplete_value": true,
      "site": "00ae0a90",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0a4c",
      "incomplete_value": true,
      "site": "00ae0a4c",
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
            "const:a8:8"
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
      "definition_site": "00ae0a6c",
      "incomplete_value": true,
      "site": "00ae0a78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0a28",
      "incomplete_value": true,
      "site": "00ae0a34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a0:8"
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
      "00ae0a4c",
      "READ",
      [
        "storage",
        "010a00a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae0a6c",
      "READ",
      [
        "storage",
        "010a00a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0a90",
      "WRITE",
      [
        "storage",
        "010a00a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae0a4c",
      "READ",
      [
        "storage",
        "010a00e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae0a6c",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0a90",
      "WRITE",
      [
        "storage",
        "010a00e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae09f4.md#insn-00ae0a08) · [`00ae0a34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae09f4.md#insn-00ae0a34) · [`00ae0a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae09f4.md#insn-00ae0a4c)
- 新版 [`00ae0a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0a38.md#insn-00ae0a4c) · [`00ae0a78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0a38.md#insn-00ae0a78) · [`00ae0a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0a38.md#insn-00ae0a90)

~~~diff
- 00ae0a08 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a8:8"]]
- 00ae0a08 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae0a08 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae0a4c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e8:8"]]
+ 00ae0a4c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0a4c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae0a08 bytes a8a24239
+ 00ae0a4c bytes a8a24339
- 00ae0a34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae0a34 ["INT_ADD", "register:40f0:8", ["const:ae0a34:8", "const:4:8"]]
- 00ae0a34 ["CALLIND", null, ["register:0:8"]]
+ 00ae0a78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae0a78 ["INT_ADD", "register:40f0:8", ["const:ae0a78:8", "const:4:8"]]
+ 00ae0a78 ["CALLIND", null, ["register:0:8"]]
- 00ae0a34 bytes 00013fd6
+ 00ae0a78 bytes 00013fd6
- 00ae0a4c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae0a4c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a8:8"]]
- 00ae0a4c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae0a90 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae0a90 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e8:8"]]
+ 00ae0a90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae0a4c bytes a0a20239
+ 00ae0a90 bytes a0a20339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f703ed43ac5b11d5a4bda3431112980"></a>

### [`00ae0a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0a60.md) → [`00ae0aa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0aa4.md) _ZN8firebase9analytics22analytics_consent_type12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae0ae0",
      "incomplete_value": true,
      "site": "00ae0ae0",
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
            "const:e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0a9c",
      "incomplete_value": true,
      "site": "00ae0a9c",
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
            "const:a8:8"
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
      "definition_site": "00ae0b00",
      "incomplete_value": true,
      "site": "00ae0b00",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0abc",
      "incomplete_value": true,
      "site": "00ae0abc",
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
            "const:a0:8"
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
      "definition_site": "00ae0abc",
      "incomplete_value": true,
      "site": "00ae0abc",
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
      "definition_site": "00ae0a78",
      "incomplete_value": true,
      "site": "00ae0a78",
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
      "00ae0ab8",
      "READ",
      [
        "storage",
        "010a00a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0ac4",
      "READ",
      [
        "storage",
        "010a00a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae0ae0",
      "WRITE",
      [
        "storage",
        "010a00a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae0ab8",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0ac4",
      "READ",
      [
        "storage",
        "010a00e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae0ae0",
      "WRITE",
      [
        "storage",
        "010a00e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0a74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0a60.md#insn-00ae0a74) · [`00ae0a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0a60.md#insn-00ae0a9c) · [`00ae0ab8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0a60.md#insn-00ae0ab8)
- 新版 [`00ae0ab8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0aa4.md#insn-00ae0ab8) · [`00ae0ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0aa4.md#insn-00ae0ae0) · [`00ae0afc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0aa4.md#insn-00ae0afc)

~~~diff
- 00ae0a74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a0:8"]]
- 00ae0a74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0ab8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e0:8"]]
+ 00ae0ab8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0a74 bytes 815240f9
+ 00ae0ab8 bytes 817240f9
- 00ae0a9c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae0a9c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae0a9c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a8:8"]]
- 00ae0a9c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae0ae0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae0ae0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae0ae0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e8:8"]]
+ 00ae0ae0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae0a9c bytes bfa20239
+ 00ae0ae0 bytes bfa20339
- 00ae0ab8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae0ab8 ["INT_ADD", "register:40f0:8", ["const:ae0ab8:8", "const:4:8"]]
- 00ae0ab8 ["CALLIND", null, ["register:0:8"]]
+ 00ae0afc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae0afc ["INT_ADD", "register:40f0:8", ["const:ae0afc:8", "const:4:8"]]
+ 00ae0afc ["CALLIND", null, ["register:0:8"]]
- 00ae0ab8 bytes 00013fd6
+ 00ae0afc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c531321995e177874668cb9fbb1fafe"></a>

### [`00ae0ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0ad0.md) → [`00ae0b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b14.md) _ZN8firebase9analytics22analytics_consent_type14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
      "definition_site": "00ae0b54",
      "incomplete_value": true,
      "site": "00ae0b54",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0b10",
      "incomplete_value": true,
      "site": "00ae0b10",
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
            "const:a0:8"
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
      "definition_site": "00ae0b30",
      "incomplete_value": true,
      "site": "00ae0b30",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0aec",
      "incomplete_value": true,
      "site": "00ae0aec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae0b38",
      "incomplete_value": false,
      "site": "00ae0b4c",
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
            "const:e49:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0af4",
      "incomplete_value": false,
      "site": "00ae0b08",
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
            "const:dbe:8"
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
      "00ae0b28",
      "READ",
      [
        "storage",
        "010a00a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0b38",
      "PARAM",
      [
        "storage",
        "002a1dbe",
        null,
        "string"
      ]
    ],
    [
      "00ae0b54",
      "WRITE",
      [
        "storage",
        "010a00a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae0b28",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0b38",
      "PARAM",
      [
        "storage",
        "002a1e49",
        null,
        "string"
      ]
    ],
    [
      "00ae0b54",
      "WRITE",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0ad0.md#insn-00ae0b08) · [`00ae0b10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0ad0.md#insn-00ae0b10) · [`00ae0ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0ad0.md#insn-00ae0ae4)
- 新版 [`00ae0b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b14.md#insn-00ae0b4c) · [`00ae0b54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b14.md#insn-00ae0b54) · [`00ae0b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b14.md#insn-00ae0b28)

~~~diff
- 00ae0b08 ["INT_ADD", "register:40f0:8", ["const:ae0b08:8", "const:4:8"]]
- 00ae0b08 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae0b4c ["INT_ADD", "register:40f0:8", ["const:ae0b4c:8", "const:4:8"]]
+ 00ae0b4c ["CALL", null, ["callee:00bde090:8"]]
- 00ae0b08 bytes 4ef50394
+ 00ae0b4c bytes 51f50394
- 00ae0b10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a0:8"]]
- 00ae0b10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae0b54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e0:8"]]
+ 00ae0b54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0b10 bytes 805200f9
+ 00ae0b54 bytes 807200f9
- 00ae0ae4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a0:8"]]
- 00ae0ae4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0b28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e0:8"]]
+ 00ae0b28 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0ae4 bytes 815240f9
+ 00ae0b28 bytes 817240f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-187cabd3673a2ff4feae98b7955d447f"></a>

### [`00ae0b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0b40.md) → [`00ae0b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b84.md) _ZN8firebase9analytics22analytics_consent_type11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae0ba0",
      "incomplete_value": false,
      "site": "00ae0ba4",
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
      "definition_site": "00ae0b5c",
      "incomplete_value": false,
      "site": "00ae0b60",
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
      "definition_site": "00ae0bb0",
      "incomplete_value": true,
      "site": "00ae0bbc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae0b6c",
      "incomplete_value": true,
      "site": "00ae0b78",
      "value": [
        "LOAD",
        "8",
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
      "00ae0ba0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae0bb0",
      "DATA",
      [
        "storage",
        "010a00b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae0ba0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae0bb0",
      "DATA",
      [
        "storage",
        "010a00f0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0b40.md#insn-00ae0b60) · [`00ae0b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0b40.md#insn-00ae0b5c) · [`00ae0b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0b40.md#insn-00ae0b68)
- 新版 [`00ae0ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b84.md#insn-00ae0ba4) · [`00ae0ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b84.md#insn-00ae0ba0) · [`00ae0bac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0b84.md#insn-00ae0bac)

~~~diff
- 00ae0b60 ["INT_ADD", "register:40f0:8", ["const:ae0b60:8", "const:4:8"]]
- 00ae0b60 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae0ba4 ["INT_ADD", "register:40f0:8", ["const:ae0ba4:8", "const:4:8"]]
+ 00ae0ba4 ["CALL", null, ["callee:00bde180:8"]]
- 00ae0b60 bytes 74f50394
+ 00ae0ba4 bytes 77f50394
- 00ae0b5c ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae0b5c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0b5c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0b5c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae0ba0 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae0ba0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae0ba0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae0ba0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae0b5c bytes 00501791
+ 00ae0ba0 bytes 001c1591
- 00ae0b68 ["COPY", "tmp:0:8", ["const:b0:8"]]
- 00ae0b68 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae0b68 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae0b68 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae0bac ["COPY", "tmp:0:8", ["const:f0:8"]]
+ 00ae0bac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae0bac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae0bac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae0b68 bytes 08c10291
+ 00ae0bac bytes 08c10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69a847580de7db1867beaee02a102d89"></a>

### [`00ae0b7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0b7c.md) → [`00ae0bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0bc0.md) _ZN8firebase9analytics22analytics_consent_type13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00ae0c00",
      "incomplete_value": true,
      "site": "00ae0c00",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0bbc",
      "incomplete_value": true,
      "site": "00ae0bbc",
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
            "const:a0:8"
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
      "definition_site": "00ae0bdc",
      "incomplete_value": true,
      "site": "00ae0bdc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0b98",
      "incomplete_value": true,
      "site": "00ae0b98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae0be4",
      "incomplete_value": false,
      "site": "00ae0bf8",
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
            "const:e49:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0ba0",
      "incomplete_value": false,
      "site": "00ae0bb4",
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
            "const:dbe:8"
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
      "00ae0bd4",
      "READ",
      [
        "storage",
        "010a00a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0be4",
      "PARAM",
      [
        "storage",
        "002a1dbe",
        null,
        "string"
      ]
    ],
    [
      "00ae0c00",
      "WRITE",
      [
        "storage",
        "010a00a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae0bd4",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0be4",
      "PARAM",
      [
        "storage",
        "002a1e49",
        null,
        "string"
      ]
    ],
    [
      "00ae0c00",
      "WRITE",
      [
        "storage",
        "010a00e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0b7c.md#insn-00ae0bb4) · [`00ae0bbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0b7c.md#insn-00ae0bbc) · [`00ae0b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0b7c.md#insn-00ae0b90)
- 新版 [`00ae0bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0bc0.md#insn-00ae0bf8) · [`00ae0c00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0bc0.md#insn-00ae0c00) · [`00ae0bd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0bc0.md#insn-00ae0bd4)

~~~diff
- 00ae0bb4 ["INT_ADD", "register:40f0:8", ["const:ae0bb4:8", "const:4:8"]]
- 00ae0bb4 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae0bf8 ["INT_ADD", "register:40f0:8", ["const:ae0bf8:8", "const:4:8"]]
+ 00ae0bf8 ["CALL", null, ["callee:00bde090:8"]]
- 00ae0bb4 bytes 23f50394
+ 00ae0bf8 bytes 26f50394
- 00ae0bbc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a0:8"]]
- 00ae0bbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae0c00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e0:8"]]
+ 00ae0c00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0bbc bytes 805200f9
+ 00ae0c00 bytes 807200f9
- 00ae0b90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a0:8"]]
- 00ae0b90 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0bd4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:e0:8"]]
+ 00ae0bd4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0b90 bytes 815240f9
+ 00ae0bd4 bytes 817240f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-54528382e4b630cde8b36109b01d4129"></a>

### [`00ae0bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0bec.md) → [`00ae0c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c30.md) _ZN8firebase9analytics22analytics_consent_type10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae0c4c",
      "incomplete_value": false,
      "site": "00ae0c50",
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
      "definition_site": "00ae0c08",
      "incomplete_value": false,
      "site": "00ae0c0c",
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
      "definition_site": "00ae0c5c",
      "incomplete_value": true,
      "site": "00ae0c68",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae0c18",
      "incomplete_value": true,
      "site": "00ae0c24",
      "value": [
        "LOAD",
        "8",
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
      "00ae0c4c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae0c5c",
      "DATA",
      [
        "storage",
        "010a00b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae0c4c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae0c5c",
      "DATA",
      [
        "storage",
        "010a00f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0bec.md#insn-00ae0c0c) · [`00ae0c08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0bec.md#insn-00ae0c08) · [`00ae0c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0bec.md#insn-00ae0c14)
- 新版 [`00ae0c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c30.md#insn-00ae0c50) · [`00ae0c4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c30.md#insn-00ae0c4c) · [`00ae0c58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c30.md#insn-00ae0c58)

~~~diff
- 00ae0c0c ["INT_ADD", "register:40f0:8", ["const:ae0c0c:8", "const:4:8"]]
- 00ae0c0c ["CALL", null, ["callee:00bde180:8"]]
+ 00ae0c50 ["INT_ADD", "register:40f0:8", ["const:ae0c50:8", "const:4:8"]]
+ 00ae0c50 ["CALL", null, ["callee:00bde180:8"]]
- 00ae0c0c bytes 49f50394
+ 00ae0c50 bytes 4cf50394
- 00ae0c08 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae0c08 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0c08 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0c08 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae0c4c ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae0c4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae0c4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae0c4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae0c08 bytes 00fc1991
+ 00ae0c4c bytes 00c81791
- 00ae0c14 ["COPY", "tmp:0:8", ["const:b8:8"]]
- 00ae0c14 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae0c14 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae0c14 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae0c58 ["COPY", "tmp:0:8", ["const:f8:8"]]
+ 00ae0c58 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae0c58 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae0c58 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae0c14 bytes 08e10291
+ 00ae0c58 bytes 08e10391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b2c85984efbbdf0742dd70d3b215e31"></a>

### [`00ae0c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0c28.md) → [`00ae0c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c6c.md) _ZN8firebase9analytics24analytics_consent_status19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

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
      "definition_site": "00ae0c98",
      "incomplete_value": true,
      "site": "00ae0c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0c54",
      "incomplete_value": true,
      "site": "00ae0c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "definition_site": "00ae0c80",
      "incomplete_value": true,
      "site": "00ae0c80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0c3c",
      "incomplete_value": true,
      "site": "00ae0c3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae0c8c",
      "incomplete_value": false,
      "site": "00ae0c90",
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
            "const:d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0c48",
      "incomplete_value": false,
      "site": "00ae0c4c",
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
            "const:166:8"
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
      "00ae0c7c",
      "READ",
      [
        "storage",
        "010a00d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0c8c",
      "PARAM",
      [
        "storage",
        "00294166",
        null,
        "string"
      ]
    ],
    [
      "00ae0c98",
      "WRITE",
      [
        "storage",
        "010a00d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae0c7c",
      "READ",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0c8c",
      "PARAM",
      [
        "storage",
        "002940d9",
        null,
        "string"
      ]
    ],
    [
      "00ae0c98",
      "WRITE",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0c28.md#insn-00ae0c4c) · [`00ae0c54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0c28.md#insn-00ae0c54) · [`00ae0c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0c28.md#insn-00ae0c38)
- 新版 [`00ae0c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c6c.md#insn-00ae0c90) · [`00ae0c98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c6c.md#insn-00ae0c98) · [`00ae0c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0c6c.md#insn-00ae0c7c)

~~~diff
- 00ae0c4c ["INT_ADD", "register:40f0:8", ["const:ae0c4c:8", "const:4:8"]]
- 00ae0c4c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae0c90 ["INT_ADD", "register:40f0:8", ["const:ae0c90:8", "const:4:8"]]
+ 00ae0c90 ["CALL", null, ["callee:00bde090:8"]]
- 00ae0c4c bytes fdf40394
+ 00ae0c90 bytes 00f50394
- 00ae0c54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d8:8"]]
- 00ae0c54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae0c98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:118:8"]]
+ 00ae0c98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0c54 bytes 606e00f9
+ 00ae0c98 bytes 608e00f9
- 00ae0c38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d8:8"]]
- 00ae0c38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0c7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:118:8"]]
+ 00ae0c7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0c38 bytes 686e40f9
+ 00ae0c7c bytes 688e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3197af0c4e479a83a7041043928d007"></a>

### [`00ae0c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0c68.md) → [`00ae0cac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cac.md) _ZN8firebase9analytics24analytics_consent_status19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_

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
      "definition_site": "00ae0cd8",
      "incomplete_value": true,
      "site": "00ae0cd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0c94",
      "incomplete_value": true,
      "site": "00ae0c94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "definition_site": "00ae0cc0",
      "incomplete_value": true,
      "site": "00ae0cc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0c7c",
      "incomplete_value": true,
      "site": "00ae0c7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae0cc8",
      "incomplete_value": false,
      "site": "00ae0cd0",
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
            "const:d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0c84",
      "incomplete_value": false,
      "site": "00ae0c8c",
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
            "const:166:8"
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
      "00ae0cbc",
      "READ",
      [
        "storage",
        "010a00d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0cc8",
      "PARAM",
      [
        "storage",
        "00294166",
        null,
        "string"
      ]
    ],
    [
      "00ae0cd8",
      "WRITE",
      [
        "storage",
        "010a00d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae0cbc",
      "READ",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0cc8",
      "PARAM",
      [
        "storage",
        "002940d9",
        null,
        "string"
      ]
    ],
    [
      "00ae0cd8",
      "WRITE",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0c68.md#insn-00ae0c8c) · [`00ae0c94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0c68.md#insn-00ae0c94) · [`00ae0c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0c68.md#insn-00ae0c78)
- 新版 [`00ae0cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cac.md#insn-00ae0cd0) · [`00ae0cd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cac.md#insn-00ae0cd8) · [`00ae0cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cac.md#insn-00ae0cbc)

~~~diff
- 00ae0c8c ["INT_ADD", "register:40f0:8", ["const:ae0c8c:8", "const:4:8"]]
- 00ae0c8c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae0cd0 ["INT_ADD", "register:40f0:8", ["const:ae0cd0:8", "const:4:8"]]
+ 00ae0cd0 ["CALL", null, ["callee:00bde090:8"]]
- 00ae0c8c bytes edf40394
+ 00ae0cd0 bytes f0f40394
- 00ae0c94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d8:8"]]
- 00ae0c94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae0cd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:118:8"]]
+ 00ae0cd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0c94 bytes 606e00f9
+ 00ae0cd8 bytes 608e00f9
- 00ae0c78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d8:8"]]
- 00ae0c78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0cbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:118:8"]]
+ 00ae0cbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0c78 bytes 686e40f9
+ 00ae0cbc bytes 688e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ba36b734401f5425970577f5c17d67f"></a>

### [`00ae0ca8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0ca8.md) → [`00ae0cec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cec.md) _ZN8firebase9analytics24analytics_consent_status10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00ae0d1c",
      "incomplete_value": true,
      "site": "00ae0d1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0cd8",
      "incomplete_value": true,
      "site": "00ae0cd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "definition_site": "00ae0d00",
      "incomplete_value": true,
      "site": "00ae0d00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0cbc",
      "incomplete_value": true,
      "site": "00ae0cbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae0d0c",
      "incomplete_value": false,
      "site": "00ae0d14",
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
            "const:d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0cc8",
      "incomplete_value": false,
      "site": "00ae0cd0",
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
            "const:166:8"
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
      "00ae0cfc",
      "READ",
      [
        "storage",
        "010a00d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0d0c",
      "PARAM",
      [
        "storage",
        "00294166",
        null,
        "string"
      ]
    ],
    [
      "00ae0d1c",
      "WRITE",
      [
        "storage",
        "010a00d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae0cfc",
      "READ",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0d0c",
      "PARAM",
      [
        "storage",
        "002940d9",
        null,
        "string"
      ]
    ],
    [
      "00ae0d1c",
      "WRITE",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0ca8.md#insn-00ae0cd0) · [`00ae0cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0ca8.md#insn-00ae0cd8) · [`00ae0cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0ca8.md#insn-00ae0cb8)
- 新版 [`00ae0d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cec.md#insn-00ae0d14) · [`00ae0d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cec.md#insn-00ae0d1c) · [`00ae0cfc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0cec.md#insn-00ae0cfc)

~~~diff
- 00ae0cd0 ["INT_ADD", "register:40f0:8", ["const:ae0cd0:8", "const:4:8"]]
- 00ae0cd0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae0d14 ["INT_ADD", "register:40f0:8", ["const:ae0d14:8", "const:4:8"]]
+ 00ae0d14 ["CALL", null, ["callee:00bde090:8"]]
- 00ae0cd0 bytes dcf40394
+ 00ae0d14 bytes dff40394
- 00ae0cd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d8:8"]]
- 00ae0cd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae0d1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:118:8"]]
+ 00ae0d1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0cd8 bytes 606e00f9
+ 00ae0d1c bytes 608e00f9
- 00ae0cb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d8:8"]]
- 00ae0cb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0cfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:118:8"]]
+ 00ae0cfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0cb8 bytes 686e40f9
+ 00ae0cfc bytes 688e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-335d3b9d0cbd0a50b236a6d5705e3827"></a>

### [`00ae0cec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0cec.md) → [`00ae0d30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0d30.md) _ZN8firebase9analytics24analytics_consent_status10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae0d60",
      "incomplete_value": true,
      "site": "00ae0d60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0d1c",
      "incomplete_value": true,
      "site": "00ae0d1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d8:8"
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
      "definition_site": "00ae0d44",
      "incomplete_value": true,
      "site": "00ae0d44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0d00",
      "incomplete_value": true,
      "site": "00ae0d00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae0d4c",
      "incomplete_value": false,
      "site": "00ae0d58",
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
            "const:d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0d08",
      "incomplete_value": false,
      "site": "00ae0d14",
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
            "const:166:8"
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
      "00ae0d40",
      "READ",
      [
        "storage",
        "010a00d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0d4c",
      "PARAM",
      [
        "storage",
        "00294166",
        null,
        "string"
      ]
    ],
    [
      "00ae0d60",
      "WRITE",
      [
        "storage",
        "010a00d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae0d40",
      "READ",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0d4c",
      "PARAM",
      [
        "storage",
        "002940d9",
        null,
        "string"
      ]
    ],
    [
      "00ae0d60",
      "WRITE",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0cec.md#insn-00ae0d14) · [`00ae0d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0cec.md#insn-00ae0d1c) · [`00ae0cfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0cec.md#insn-00ae0cfc)
- 新版 [`00ae0d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0d30.md#insn-00ae0d58) · [`00ae0d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0d30.md#insn-00ae0d60) · [`00ae0d40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0d30.md#insn-00ae0d40)

~~~diff
- 00ae0d14 ["INT_ADD", "register:40f0:8", ["const:ae0d14:8", "const:4:8"]]
- 00ae0d14 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae0d58 ["INT_ADD", "register:40f0:8", ["const:ae0d58:8", "const:4:8"]]
+ 00ae0d58 ["CALL", null, ["callee:00bde090:8"]]
- 00ae0d14 bytes cbf40394
+ 00ae0d58 bytes cef40394
- 00ae0d1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d8:8"]]
- 00ae0d1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae0d60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:118:8"]]
+ 00ae0d60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0d1c bytes 606e00f9
+ 00ae0d60 bytes 608e00f9
- 00ae0cfc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d8:8"]]
- 00ae0cfc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0d40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:118:8"]]
+ 00ae0d40 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0cfc bytes 686e40f9
+ 00ae0d40 bytes 688e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd8b26bd009383494da4e24a63b2c49d"></a>

### [`00ae0d3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0d3c.md) → [`00ae0d80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0d80.md) _ZN8firebase9analytics24analytics_consent_status15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae0dd8",
      "incomplete_value": true,
      "site": "00ae0dd8",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0d94",
      "incomplete_value": true,
      "site": "00ae0d94",
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
            "const:e0:8"
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
      "definition_site": "00ae0db4",
      "incomplete_value": true,
      "site": "00ae0dc0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:118:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0d70",
      "incomplete_value": true,
      "site": "00ae0d7c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d8:8"
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
      "00ae0d94",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae0db4",
      "READ",
      [
        "storage",
        "010a00d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0dd8",
      "WRITE",
      [
        "storage",
        "010a00e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae0d94",
      "READ",
      [
        "storage",
        "010a0120",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae0db4",
      "READ",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0dd8",
      "WRITE",
      [
        "storage",
        "010a0120",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0d50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0d3c.md#insn-00ae0d50) · [`00ae0d7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0d3c.md#insn-00ae0d7c) · [`00ae0d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0d3c.md#insn-00ae0d94)
- 新版 [`00ae0d94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0d80.md#insn-00ae0d94) · [`00ae0dc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0d80.md#insn-00ae0dc0) · [`00ae0dd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0d80.md#insn-00ae0dd8)

~~~diff
- 00ae0d50 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:e0:8"]]
- 00ae0d50 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae0d50 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae0d94 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:120:8"]]
+ 00ae0d94 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0d94 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae0d50 bytes a8824339
+ 00ae0d94 bytes a8824439
- 00ae0d7c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae0d7c ["INT_ADD", "register:40f0:8", ["const:ae0d7c:8", "const:4:8"]]
- 00ae0d7c ["CALLIND", null, ["register:0:8"]]
+ 00ae0dc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae0dc0 ["INT_ADD", "register:40f0:8", ["const:ae0dc0:8", "const:4:8"]]
+ 00ae0dc0 ["CALLIND", null, ["register:0:8"]]
- 00ae0d7c bytes 00013fd6
+ 00ae0dc0 bytes 00013fd6
- 00ae0d94 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae0d94 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:e0:8"]]
- 00ae0d94 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae0dd8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae0dd8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:120:8"]]
+ 00ae0dd8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae0d94 bytes a0820339
+ 00ae0dd8 bytes a0820439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fdc47a70d203fc7d3dddd10ed00c665"></a>

### [`00ae0da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0da8.md) → [`00ae0dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0dec.md) _ZN8firebase9analytics24analytics_consent_status12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae0e28",
      "incomplete_value": true,
      "site": "00ae0e28",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0de4",
      "incomplete_value": true,
      "site": "00ae0de4",
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
            "const:e0:8"
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
      "definition_site": "00ae0e48",
      "incomplete_value": true,
      "site": "00ae0e48",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0e04",
      "incomplete_value": true,
      "site": "00ae0e04",
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
            "const:d8:8"
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
      "definition_site": "00ae0e04",
      "incomplete_value": true,
      "site": "00ae0e04",
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
      "definition_site": "00ae0dc0",
      "incomplete_value": true,
      "site": "00ae0dc0",
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
      "00ae0e00",
      "READ",
      [
        "storage",
        "010a00d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0e0c",
      "READ",
      [
        "storage",
        "010a00e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae0e28",
      "WRITE",
      [
        "storage",
        "010a00e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae0e00",
      "READ",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0e0c",
      "READ",
      [
        "storage",
        "010a0120",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae0e28",
      "WRITE",
      [
        "storage",
        "010a0120",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0da8.md#insn-00ae0dbc) · [`00ae0de4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0da8.md#insn-00ae0de4) · [`00ae0e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0da8.md#insn-00ae0e00)
- 新版 [`00ae0e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0dec.md#insn-00ae0e00) · [`00ae0e28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0dec.md#insn-00ae0e28) · [`00ae0e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0dec.md#insn-00ae0e44)

~~~diff
- 00ae0dbc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d8:8"]]
- 00ae0dbc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0e00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:118:8"]]
+ 00ae0e00 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0dbc bytes 816e40f9
+ 00ae0e00 bytes 818e40f9
- 00ae0de4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae0de4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae0de4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:e0:8"]]
- 00ae0de4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae0e28 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae0e28 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae0e28 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:120:8"]]
+ 00ae0e28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae0de4 bytes bf820339
+ 00ae0e28 bytes bf820439
- 00ae0e00 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae0e00 ["INT_ADD", "register:40f0:8", ["const:ae0e00:8", "const:4:8"]]
- 00ae0e00 ["CALLIND", null, ["register:0:8"]]
+ 00ae0e44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae0e44 ["INT_ADD", "register:40f0:8", ["const:ae0e44:8", "const:4:8"]]
+ 00ae0e44 ["CALLIND", null, ["register:0:8"]]
- 00ae0e00 bytes 00013fd6
+ 00ae0e44 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68124e09cf17063cf545fcbb27318f46"></a>

### [`00ae0e18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0e18.md) → [`00ae0e5c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0e5c.md) _ZN8firebase9analytics24analytics_consent_status14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
      "definition_site": "00ae0e9c",
      "incomplete_value": true,
      "site": "00ae0e9c",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0e58",
      "incomplete_value": true,
      "site": "00ae0e58",
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
            "const:d8:8"
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
      "definition_site": "00ae0e78",
      "incomplete_value": true,
      "site": "00ae0e78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0e34",
      "incomplete_value": true,
      "site": "00ae0e34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae0e80",
      "incomplete_value": false,
      "site": "00ae0e94",
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
            "const:d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0e3c",
      "incomplete_value": false,
      "site": "00ae0e50",
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
            "const:166:8"
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
      "00ae0e70",
      "READ",
      [
        "storage",
        "010a00d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0e80",
      "PARAM",
      [
        "storage",
        "00294166",
        null,
        "string"
      ]
    ],
    [
      "00ae0e9c",
      "WRITE",
      [
        "storage",
        "010a00d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae0e70",
      "READ",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0e80",
      "PARAM",
      [
        "storage",
        "002940d9",
        null,
        "string"
      ]
    ],
    [
      "00ae0e9c",
      "WRITE",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0e50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0e18.md#insn-00ae0e50) · [`00ae0e58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0e18.md#insn-00ae0e58) · [`00ae0e2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0e18.md#insn-00ae0e2c)
- 新版 [`00ae0e94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0e5c.md#insn-00ae0e94) · [`00ae0e9c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0e5c.md#insn-00ae0e9c) · [`00ae0e70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0e5c.md#insn-00ae0e70)

~~~diff
- 00ae0e50 ["INT_ADD", "register:40f0:8", ["const:ae0e50:8", "const:4:8"]]
- 00ae0e50 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae0e94 ["INT_ADD", "register:40f0:8", ["const:ae0e94:8", "const:4:8"]]
+ 00ae0e94 ["CALL", null, ["callee:00bde090:8"]]
- 00ae0e50 bytes 7cf40394
+ 00ae0e94 bytes 7ff40394
- 00ae0e58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d8:8"]]
- 00ae0e58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae0e9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:118:8"]]
+ 00ae0e9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0e58 bytes 806e00f9
+ 00ae0e9c bytes 808e00f9
- 00ae0e2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d8:8"]]
- 00ae0e2c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0e70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:118:8"]]
+ 00ae0e70 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0e2c bytes 816e40f9
+ 00ae0e70 bytes 818e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56cb7817a796969402693b107c2b0997"></a>

### [`00ae0e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0e88.md) → [`00ae0ecc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0ecc.md) _ZN8firebase9analytics24analytics_consent_status11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae0ee8",
      "incomplete_value": false,
      "site": "00ae0eec",
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
      "definition_site": "00ae0ea4",
      "incomplete_value": false,
      "site": "00ae0ea8",
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
      "definition_site": "00ae0ef8",
      "incomplete_value": true,
      "site": "00ae0f04",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae0eb4",
      "incomplete_value": true,
      "site": "00ae0ec0",
      "value": [
        "LOAD",
        "8",
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
      "00ae0ee8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae0ef8",
      "DATA",
      [
        "storage",
        "010a00e8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae0ee8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae0ef8",
      "DATA",
      [
        "storage",
        "010a0128",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0e88.md#insn-00ae0ea8) · [`00ae0ea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0e88.md#insn-00ae0ea4) · [`00ae0eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0e88.md#insn-00ae0eb0)
- 新版 [`00ae0eec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0ecc.md#insn-00ae0eec) · [`00ae0ee8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0ecc.md#insn-00ae0ee8) · [`00ae0ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0ecc.md#insn-00ae0ef4)

~~~diff
- 00ae0ea8 ["INT_ADD", "register:40f0:8", ["const:ae0ea8:8", "const:4:8"]]
- 00ae0ea8 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae0eec ["INT_ADD", "register:40f0:8", ["const:ae0eec:8", "const:4:8"]]
+ 00ae0eec ["CALL", null, ["callee:00bde180:8"]]
- 00ae0ea8 bytes a2f40394
+ 00ae0eec bytes a5f40394
- 00ae0ea4 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae0ea4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0ea4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0ea4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae0ee8 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae0ee8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae0ee8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae0ee8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae0ea4 bytes 00501791
+ 00ae0ee8 bytes 001c1591
- 00ae0eb0 ["COPY", "tmp:0:8", ["const:e8:8"]]
- 00ae0eb0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae0eb0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae0eb0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae0ef4 ["COPY", "tmp:0:8", ["const:128:8"]]
+ 00ae0ef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae0ef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae0ef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae0eb0 bytes 08a10391
+ 00ae0ef4 bytes 08a10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfcf01e111e76eef8fd309c06b29e676"></a>

### [`00ae0ec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0ec4.md) → [`00ae0f08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f08.md) _ZN8firebase9analytics24analytics_consent_status13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md)

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
      "definition_site": "00ae0f48",
      "incomplete_value": true,
      "site": "00ae0f48",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0f04",
      "incomplete_value": true,
      "site": "00ae0f04",
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
            "const:d8:8"
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
      "definition_site": "00ae0f24",
      "incomplete_value": true,
      "site": "00ae0f24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0ee0",
      "incomplete_value": true,
      "site": "00ae0ee0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae0f2c",
      "incomplete_value": false,
      "site": "00ae0f40",
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
            "const:d9:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae0ee8",
      "incomplete_value": false,
      "site": "00ae0efc",
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
            "const:166:8"
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
      "00ae0f1c",
      "READ",
      [
        "storage",
        "010a00d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0f2c",
      "PARAM",
      [
        "storage",
        "00294166",
        null,
        "string"
      ]
    ],
    [
      "00ae0f48",
      "WRITE",
      [
        "storage",
        "010a00d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae0f1c",
      "READ",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0f2c",
      "PARAM",
      [
        "storage",
        "002940d9",
        null,
        "string"
      ]
    ],
    [
      "00ae0f48",
      "WRITE",
      [
        "storage",
        "010a0118",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0efc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0ec4.md#insn-00ae0efc) · [`00ae0f04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0ec4.md#insn-00ae0f04) · [`00ae0ed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0ec4.md#insn-00ae0ed8)
- 新版 [`00ae0f40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f08.md#insn-00ae0f40) · [`00ae0f48`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f08.md#insn-00ae0f48) · [`00ae0f1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f08.md#insn-00ae0f1c)

~~~diff
- 00ae0efc ["INT_ADD", "register:40f0:8", ["const:ae0efc:8", "const:4:8"]]
- 00ae0efc ["CALL", null, ["callee:00bde090:8"]]
+ 00ae0f40 ["INT_ADD", "register:40f0:8", ["const:ae0f40:8", "const:4:8"]]
+ 00ae0f40 ["CALL", null, ["callee:00bde090:8"]]
- 00ae0efc bytes 51f40394
+ 00ae0f40 bytes 54f40394
- 00ae0f04 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d8:8"]]
- 00ae0f04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae0f48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:118:8"]]
+ 00ae0f48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae0f04 bytes 806e00f9
+ 00ae0f48 bytes 808e00f9
- 00ae0ed8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d8:8"]]
- 00ae0ed8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae0f1c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:118:8"]]
+ 00ae0f1c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0ed8 bytes 816e40f9
+ 00ae0f1c bytes 818e40f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d8355d110fbbf5380f7bc41b57510f9"></a>

### [`00ae0f34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0f34.md) → [`00ae0f78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f78.md) _ZN8firebase9analytics24analytics_consent_status10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae0f94",
      "incomplete_value": false,
      "site": "00ae0f98",
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
      "definition_site": "00ae0f50",
      "incomplete_value": false,
      "site": "00ae0f54",
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
      "definition_site": "00ae0fa4",
      "incomplete_value": true,
      "site": "00ae0fb0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae0f60",
      "incomplete_value": true,
      "site": "00ae0f6c",
      "value": [
        "LOAD",
        "8",
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
      "00ae0f94",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae0fa4",
      "DATA",
      [
        "storage",
        "010a00f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae0f94",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae0fa4",
      "DATA",
      [
        "storage",
        "010a0130",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0f34.md#insn-00ae0f54) · [`00ae0f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0f34.md#insn-00ae0f50) · [`00ae0f5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0f34.md#insn-00ae0f5c)
- 新版 [`00ae0f98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f78.md#insn-00ae0f98) · [`00ae0f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f78.md#insn-00ae0f94) · [`00ae0fa0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0f78.md#insn-00ae0fa0)

~~~diff
- 00ae0f54 ["INT_ADD", "register:40f0:8", ["const:ae0f54:8", "const:4:8"]]
- 00ae0f54 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae0f98 ["INT_ADD", "register:40f0:8", ["const:ae0f98:8", "const:4:8"]]
+ 00ae0f98 ["CALL", null, ["callee:00bde180:8"]]
- 00ae0f54 bytes 77f40394
+ 00ae0f98 bytes 7af40394
- 00ae0f50 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae0f50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0f50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae0f50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae0f94 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae0f94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae0f94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae0f94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae0f50 bytes 00fc1991
+ 00ae0f94 bytes 00c81791
- 00ae0f5c ["COPY", "tmp:0:8", ["const:f0:8"]]
- 00ae0f5c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae0f5c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae0f5c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae0fa0 ["COPY", "tmp:0:8", ["const:130:8"]]
+ 00ae0fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae0fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae0fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae0f5c bytes 08c10391
+ 00ae0fa0 bytes 08c10491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-01e0b8c8ca97d835108bc54052564e93"></a>

### [`00ae0f70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0f70.md) → [`00ae0fb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0fb4.md) _ZN8firebase9analytics10InitializeERKNS_3AppE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddac0.md) · 呼出先 13件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bdde10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde10.md) [`00bdde40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde40.md) [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00bddfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfd0.md)
- 新版 呼出元 1件 [`00bddb10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb10.md) · 呼出先 13件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bdde60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde60.md) [`00bdde90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde90.md) [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00bde020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde020.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 78.84% / 新版 78.84%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 5件, `call_argument_candidate` 17件, `store_condition` 2件, `store_destination` 9件

アドレスに依存する影響 `branch_value` 2件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae1070",
      "incomplete_value": true,
      "site": "00ae1070",
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
    "old": {
      "definition_site": "00ae102c",
      "incomplete_value": true,
      "site": "00ae102c",
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
            "const:30:8"
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
      "definition_site": "00ae10c8",
      "incomplete_value": true,
      "site": "00ae10c8",
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
            "const:e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae1084",
      "incomplete_value": true,
      "site": "00ae1084",
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
            "const:a0:8"
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
      "definition_site": "00ae1120",
      "incomplete_value": true,
      "site": "00ae1120",
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
            "const:118:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae10dc",
      "incomplete_value": true,
      "site": "00ae10dc",
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
            "const:d8:8"
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
      "00ae0fd0",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0fdc",
      "READ",
      [
        "storage",
        "00c1b858",
        null,
        "pointer"
      ]
    ],
    [
      "00ae0fec",
      "READ",
      [
        "storage",
        "00c246f8",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ae0fd0",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae0fdc",
      "READ",
      [
        "storage",
        "00c1b8a8",
        null,
        "pointer"
      ]
    ],
    [
      "00ae0fec",
      "READ",
      [
        "storage",
        "00c24748",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae0fcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0f70.md#insn-00ae0fcc) · [`00ae0fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0f70.md#insn-00ae0fd4) · [`00ae1024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae0/00ae0f70.md#insn-00ae1024)
- 新版 [`00ae1010`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0fb4.md#insn-00ae1010) · [`00ae1018`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0fb4.md#insn-00ae1018) · [`00ae1068`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae0/00ae0fb4.md#insn-00ae1068)

~~~diff
- 00ae0fcc ["INT_ADD", "register:40f0:8", ["const:ae0fcc:8", "const:4:8"]]
- 00ae0fcc ["CALL", null, ["callee:00bde160:8"]]
+ 00ae1010 ["INT_ADD", "register:40f0:8", ["const:ae1010:8", "const:4:8"]]
+ 00ae1010 ["CALL", null, ["callee:00bde160:8"]]
- 00ae0fcc bytes 51f40394
+ 00ae1010 bytes 54f40394
- 00ae0fd4 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:108:8"]]
- 00ae0fd4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae1018 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:148:8"]]
+ 00ae1018 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae0fd4 bytes c88640f9
+ 00ae1018 bytes c8a640f9
- 00ae1024 ["INT_ADD", "register:40f0:8", ["const:ae1024:8", "const:4:8"]]
- 00ae1024 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae1068 ["INT_ADD", "register:40f0:8", ["const:ae1068:8", "const:4:8"]]
+ 00ae1068 ["CALL", null, ["callee:00bde090:8"]]
- 00ae1024 bytes 07f40394
+ 00ae1068 bytes 0af40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9f266690233b2e7a4eba90eef072ca11"></a>

### [`00ae1314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1314.md) → [`00ae1358`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1358.md) _ZN8firebase9analytics9TerminateEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddaa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddaa0.md) · 呼出先 7件 [`00bdde20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde20.md) [`00bdde50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde50.md) [`00bddf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf10.md) [`00bde030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde030.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 1件 [`00bddaf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddaf0.md) · 呼出先 7件 [`00bdde70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde70.md) [`00bddea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddea0.md) [`00bddf60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf60.md) [`00bde080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde080.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.23% / 新版 87.23%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 8件

アドレスに依存する影響 `branch_value` 4件, `call_argument_candidate` 1件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00ae1394",
      "incomplete_value": true,
      "site": "00ae1394",
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
            "const:140:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae1350",
      "incomplete_value": true,
      "site": "00ae1350",
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
            "const:100:8"
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
      "definition_site": "00ae13b8",
      "incomplete_value": true,
      "site": "00ae13b8",
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
            "const:148:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae1374",
      "incomplete_value": true,
      "site": "00ae1374",
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
            "const:108:8"
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
      "definition_site": "00ae13dc",
      "incomplete_value": true,
      "site": "00ae13dc",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae1398",
      "incomplete_value": true,
      "site": "00ae1398",
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
            "const:e0:8"
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
      "00ae136c",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae137c",
      "READ",
      [
        "storage",
        "00c1b858",
        null,
        "pointer"
      ]
    ],
    [
      "00ae1384",
      "READ",
      [
        "storage",
        "00c246f8",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ae136c",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae137c",
      "READ",
      [
        "storage",
        "00c1b8a8",
        null,
        "pointer"
      ]
    ],
    [
      "00ae1384",
      "READ",
      [
        "storage",
        "00c24748",
        "_ZN8firebase9analytics8internal20kAnalyticsModuleNameE",
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae1330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1314.md#insn-00ae1330) · [`00ae1350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1314.md#insn-00ae1350) · [`00ae1368`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae1314.md#insn-00ae1368)
- 新版 [`00ae1374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1358.md#insn-00ae1374) · [`00ae1394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1358.md#insn-00ae1394) · [`00ae13ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1358.md#insn-00ae13ac)

~~~diff
- 00ae1330 ["INT_ADD", "register:40f0:8", ["const:ae1330:8", "const:4:8"]]
- 00ae1330 ["CALL", null, ["callee:00bde200:8"]]
+ 00ae1374 ["INT_ADD", "register:40f0:8", ["const:ae1374:8", "const:4:8"]]
+ 00ae1374 ["CALL", null, ["callee:00bde200:8"]]
- 00ae1330 bytes a0f30394
+ 00ae1374 bytes a3f30394
- 00ae1350 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:100:8"]]
- 00ae1350 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae1350 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae1394 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:140:8"]]
+ 00ae1394 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae1394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae1350 bytes 9f8200f9
+ 00ae1394 bytes 9fa200f9
- 00ae1368 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae1368 ["INT_ADD", "register:40f0:8", ["const:ae1368:8", "const:4:8"]]
- 00ae1368 ["CALLIND", null, ["register:0:8"]]
+ 00ae13ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae13ac ["INT_ADD", "register:40f0:8", ["const:ae13ac:8", "const:4:8"]]
+ 00ae13ac ["CALLIND", null, ["register:0:8"]]
- 00ae1368 bytes 00013fd6
+ 00ae13ac bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3dfeab458f2c79086c6ed8b452aa127e"></a>

### [`00ae148c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae148c.md) → [`00ae14d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae14d0.md) _ZN8firebase9analytics29SetAnalyticsCollectionEnabledEb

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.00% / 新版 88.00%

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
      "definition_site": "00ae14e4",
      "incomplete_value": true,
      "site": "00ae14e4",
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
      "definition_site": "00ae14a0",
      "incomplete_value": true,
      "site": "00ae14a0",
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
      "definition_site": "00ae14fc",
      "incomplete_value": true,
      "site": "00ae150c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:148:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae14b8",
      "incomplete_value": true,
      "site": "00ae14c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:108:8"
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
      "definition_site": "00ae1500",
      "incomplete_value": true,
      "site": "00ae150c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:80:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae14bc",
      "incomplete_value": true,
      "site": "00ae14c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:40:8"
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
      "00ae14e0",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae14fc",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae1500",
      "READ",
      [
        "storage",
        "010a0040",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae14e0",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae14fc",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae1500",
      "READ",
      [
        "storage",
        "010a0080",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae14c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae148c.md#insn-00ae14c8) · [`00ae14e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae148c.md#insn-00ae14e4) · [`00ae149c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae148c.md#insn-00ae149c)
- 新版 [`00ae150c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae14d0.md#insn-00ae150c) · [`00ae1528`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae14d0.md#insn-00ae1528) · [`00ae14e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae14d0.md#insn-00ae14e0)

~~~diff
- 00ae14c8 ["INT_ADD", "register:40f0:8", ["const:ae14c8:8", "const:4:8"]]
- 00ae14c8 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae150c ["INT_ADD", "register:40f0:8", ["const:ae150c:8", "const:4:8"]]
+ 00ae150c ["CALL", null, ["callee:00551e14:8"]]
- 00ae14c8 bytes 53c2e997
+ 00ae150c bytes 42c2e997
- 00ae14e4 ["COPY", "tmp:0:8", ["const:16d:8"]]
- 00ae14e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae14e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae14e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae1528 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 00ae1528 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae1528 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae1528 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae14e4 bytes 00b40591
+ 00ae1528 bytes 00800391
- 00ae149c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
- 00ae149c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae14e0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
+ 00ae14e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae149c bytes 088140f9
+ 00ae14e0 bytes 08a140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-679ab93c0e40992e2a851def2f06ca68"></a>

### [`00ae14f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae14f0.md) → [`00ae1534`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1534.md) _ZN8firebase9analytics10SetConsentERKNSt6__ndk13mapINS0_11ConsentTypeENS0_13ConsentStatusENS1_4lessIS3_EENS1_9allocatorINS1_4pairIKS3_S4_EEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde010.md)
- 新版 呼出元 0件  · 呼出先 12件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.67% / 新版 92.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae1558",
      "incomplete_value": true,
      "site": "00ae1558",
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
      "definition_site": "00ae1514",
      "incomplete_value": true,
      "site": "00ae1514",
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
      "definition_site": "00ae1614",
      "incomplete_value": true,
      "site": "00ae1624",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae15d0",
      "incomplete_value": true,
      "site": "00ae15e0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a0:8"
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
      "definition_site": "00ae1618",
      "incomplete_value": true,
      "site": "00ae1624",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:100:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae15d4",
      "incomplete_value": true,
      "site": "00ae15e0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c0:8"
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
      "00ae1554",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae15d8",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ],
    [
      "00ae1600",
      "DATA",
      [
        "storage",
        "002f59e9",
        "switchD_00ae15c4::switchdataD_002f59e9",
        "byte"
      ]
    ]
  ],
  "added": [
    [
      "00ae1554",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae15d8",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ],
    [
      "00ae1600",
      "DATA",
      [
        "storage",
        "002f59e9",
        "switchD_00ae1608::switchdataD_002f59e9",
        "byte"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae1558`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae14f0.md#insn-00ae1558) · [`00ae15e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae14f0.md#insn-00ae15e0) · [`00ae15f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae1/00ae14f0.md#insn-00ae15f8)
- 新版 [`00ae159c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1534.md#insn-00ae159c) · [`00ae1624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1534.md#insn-00ae1624) · [`00ae163c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae1/00ae1534.md#insn-00ae163c)

~~~diff
- 00ae1558 ["INT_ADD", "register:40f0:8", ["const:ae1558:8", "const:4:8"]]
- 00ae1558 ["CALL", null, ["callee:00bde100:8"]]
+ 00ae159c ["INT_ADD", "register:40f0:8", ["const:ae159c:8", "const:4:8"]]
+ 00ae159c ["CALL", null, ["callee:00bde100:8"]]
- 00ae1558 bytes d6f20394
+ 00ae159c bytes d9f20394
- 00ae15e0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae15e0 ["INT_ADD", "register:40f0:8", ["const:ae15e0:8", "const:4:8"]]
- 00ae15e0 ["CALLIND", null, ["register:0:8"]]
+ 00ae1624 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae1624 ["INT_ADD", "register:40f0:8", ["const:ae1624:8", "const:4:8"]]
+ 00ae1624 ["CALLIND", null, ["register:0:8"]]
- 00ae15e0 bytes 00013fd6
+ 00ae1624 bytes 00013fd6
- 00ae15f8 ["INT_ADD", "register:40f0:8", ["const:ae15f8:8", "const:4:8"]]
- 00ae15f8 ["CALL", null, ["callee:00bde060:8"]]
+ 00ae163c ["INT_ADD", "register:40f0:8", ["const:ae163c:8", "const:4:8"]]
+ 00ae163c ["CALL", null, ["callee:00bde060:8"]]
- 00ae15f8 bytes 86f20394
+ 00ae163c bytes 89f20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ba409e3ae3263d08ad9b426af4b9c35"></a>

### [`00ae210c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae210c.md) → [`00ae2150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2150.md) _ZN8firebase9analytics8LogEventEPKcS2_S2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.88% / 新版 95.88%

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
      "definition_site": "00ae216c",
      "incomplete_value": true,
      "site": "00ae216c",
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
      "definition_site": "00ae2128",
      "incomplete_value": true,
      "site": "00ae2128",
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
      "definition_site": "00ae2274",
      "incomplete_value": false,
      "site": "00ae227c",
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
            "const:db:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2230",
      "incomplete_value": false,
      "site": "00ae2238",
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
            "const:41:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 1
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae2168",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2248",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae224c",
      "READ",
      [
        "storage",
        "010a0050",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae2168",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2248",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae224c",
      "READ",
      [
        "storage",
        "010a0090",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2238`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae210c.md#insn-00ae2238) · [`00ae2124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae210c.md#insn-00ae2124) · [`00ae213c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae210c.md#insn-00ae213c)
- 新版 [`00ae227c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2150.md#insn-00ae227c) · [`00ae2168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2150.md#insn-00ae2168) · [`00ae2180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2150.md#insn-00ae2180)

~~~diff
- 00ae2238 ["INT_ADD", "register:40f0:8", ["const:ae2238:8", "const:4:8"]]
- 00ae2238 ["CALL", null, ["callee:00bdde40:8"]]
+ 00ae227c ["INT_ADD", "register:40f0:8", ["const:ae227c:8", "const:4:8"]]
+ 00ae227c ["CALL", null, ["callee:00bdde40:8"]]
- 00ae2238 bytes eeee0394
+ 00ae227c bytes f1ee0394
- 00ae2124 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
- 00ae2124 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae2168 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
+ 00ae2168 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae2124 bytes 088140f9
+ 00ae2168 bytes 08a140f9
- 00ae213c ["INT_ADD", "register:40f0:8", ["const:ae213c:8", "const:4:8"]]
- 00ae213c ["CALL", null, ["callee:00bde200:8"]]
+ 00ae2180 ["INT_ADD", "register:40f0:8", ["const:ae2180:8", "const:4:8"]]
+ 00ae2180 ["CALL", null, ["callee:00bde200:8"]]
- 00ae213c bytes 1df00394
+ 00ae2180 bytes 20f00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbf982edf0d0f93c5d35dd7d3ec13a57"></a>

### [`00ae2290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2290.md) → [`00ae22d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae22d4.md) _ZN8firebase9analytics8LogEventEPKcS2_d

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae22f0",
      "incomplete_value": true,
      "site": "00ae22f0",
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
      "definition_site": "00ae22ac",
      "incomplete_value": true,
      "site": "00ae22ac",
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
      "definition_site": "00ae23a0",
      "incomplete_value": true,
      "site": "00ae23b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:148:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae235c",
      "incomplete_value": true,
      "site": "00ae2374",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:108:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae23a4",
      "incomplete_value": true,
      "site": "00ae23b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2360",
      "incomplete_value": true,
      "site": "00ae2374",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50:8"
              ]
            ]
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
      "00ae22ec",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae23a0",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae23a4",
      "READ",
      [
        "storage",
        "010a0050",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae22ec",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae23a0",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae23a4",
      "READ",
      [
        "storage",
        "010a0090",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2374`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2290.md#insn-00ae2374) · [`00ae2390`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2290.md#insn-00ae2390) · [`00ae22a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2290.md#insn-00ae22a8)
- 新版 [`00ae23b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae22d4.md#insn-00ae23b8) · [`00ae23d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae22d4.md#insn-00ae23d4) · [`00ae22ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae22d4.md#insn-00ae22ec)

~~~diff
- 00ae2374 ["INT_ADD", "register:40f0:8", ["const:ae2374:8", "const:4:8"]]
- 00ae2374 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae23b8 ["INT_ADD", "register:40f0:8", ["const:ae23b8:8", "const:4:8"]]
+ 00ae23b8 ["CALL", null, ["callee:00551e14:8"]]
- 00ae2374 bytes a8bee997
+ 00ae23b8 bytes 97bee997
- 00ae2390 ["INT_ADD", "register:40f0:8", ["const:ae2390:8", "const:4:8"]]
- 00ae2390 ["CALL", null, ["callee:00bdde40:8"]]
+ 00ae23d4 ["INT_ADD", "register:40f0:8", ["const:ae23d4:8", "const:4:8"]]
+ 00ae23d4 ["CALL", null, ["callee:00bdde40:8"]]
- 00ae2390 bytes 98ee0394
+ 00ae23d4 bytes 9bee0394
- 00ae22a8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
- 00ae22a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae22ec ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
+ 00ae22ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae22a8 bytes 088140f9
+ 00ae22ec bytes 08a140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ef4fe8d7c229c8fb053a4b42b2196e7"></a>

### [`00ae23e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae23e8.md) → [`00ae242c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae242c.md) _ZN8firebase9analytics8LogEventEPKcS2_l

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde190`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde190.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)
- 新版 呼出元 1件 [`00bde1e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde1e0.md) · 呼出先 8件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae2448",
      "incomplete_value": true,
      "site": "00ae2448",
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
      "definition_site": "00ae2404",
      "incomplete_value": true,
      "site": "00ae2404",
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
      "definition_site": "00ae24f8",
      "incomplete_value": true,
      "site": "00ae2510",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:148:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae24b4",
      "incomplete_value": true,
      "site": "00ae24cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:108:8"
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae24fc",
      "incomplete_value": true,
      "site": "00ae2510",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:90:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae24b8",
      "incomplete_value": true,
      "site": "00ae24cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:50:8"
              ]
            ]
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
      "00ae2444",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae24f8",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae24fc",
      "READ",
      [
        "storage",
        "010a0050",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae2444",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae24f8",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae24fc",
      "READ",
      [
        "storage",
        "010a0090",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae24cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae23e8.md#insn-00ae24cc) · [`00ae24e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae23e8.md#insn-00ae24e8) · [`00ae2400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae23e8.md#insn-00ae2400)
- 新版 [`00ae2510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae242c.md#insn-00ae2510) · [`00ae252c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae242c.md#insn-00ae252c) · [`00ae2444`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae242c.md#insn-00ae2444)

~~~diff
- 00ae24cc ["INT_ADD", "register:40f0:8", ["const:ae24cc:8", "const:4:8"]]
- 00ae24cc ["CALL", null, ["callee:00551e14:8"]]
+ 00ae2510 ["INT_ADD", "register:40f0:8", ["const:ae2510:8", "const:4:8"]]
+ 00ae2510 ["CALL", null, ["callee:00551e14:8"]]
- 00ae24cc bytes 52bee997
+ 00ae2510 bytes 41bee997
- 00ae24e8 ["INT_ADD", "register:40f0:8", ["const:ae24e8:8", "const:4:8"]]
- 00ae24e8 ["CALL", null, ["callee:00bdde40:8"]]
+ 00ae252c ["INT_ADD", "register:40f0:8", ["const:ae252c:8", "const:4:8"]]
+ 00ae252c ["CALL", null, ["callee:00bdde40:8"]]
- 00ae24e8 bytes 42ee0394
+ 00ae252c bytes 45ee0394
- 00ae2400 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
- 00ae2400 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae2444 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
+ 00ae2444 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae2400 bytes 088140f9
+ 00ae2444 bytes 08a140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16e58e4eb23af832346996e44189a4f5"></a>

### [`00ae26dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae26dc.md) → [`00ae2720`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2720.md) _ZN8firebase9analytics25SetDefaultEventParametersEPKNS0_9ParameterEm

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde170.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0c0.md)
- 新版 呼出元 1件 [`00bde1c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde1c0.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde110`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde110.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 91.96% / 新版 91.96%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae2740",
      "incomplete_value": true,
      "site": "00ae2740",
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
      "definition_site": "00ae26fc",
      "incomplete_value": true,
      "site": "00ae26fc",
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
      "definition_site": "00ae2860",
      "incomplete_value": false,
      "site": "00ae2864",
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
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae281c",
      "incomplete_value": false,
      "site": "00ae2820",
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
            "const:cc5:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae288c",
      "incomplete_value": true,
      "site": "00ae289c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:148:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2848",
      "incomplete_value": true,
      "site": "00ae2858",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:108:8"
              ]
            ]
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
      "00ae273c",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae27e4",
      "PARAM",
      [
        "storage",
        "002a8b70",
        null,
        "string"
      ]
    ],
    [
      "00ae2808",
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
      "00ae273c",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae27e4",
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      "00ae2808",
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

- 旧版 [`00ae27dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae26dc.md#insn-00ae27dc) · [`00ae2820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae26dc.md#insn-00ae2820) · [`00ae2858`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae26dc.md#insn-00ae2858)
- 新版 [`00ae2820`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2720.md#insn-00ae2820) · [`00ae2864`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2720.md#insn-00ae2864) · [`00ae289c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2720.md#insn-00ae289c)

~~~diff
- 00ae27dc ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:90:8"]]
- 00ae27dc ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae2820 ["INT_ADD", "tmp:0:8", ["register:4048:8", "const:d0:8"]]
+ 00ae2820 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae27dc bytes 224940f9
+ 00ae2820 bytes 226940f9
- 00ae2820 ["INT_ADD", "register:40f0:8", ["const:ae2820:8", "const:4:8"]]
- 00ae2820 ["CALL", null, ["callee:00bdde40:8"]]
+ 00ae2864 ["INT_ADD", "register:40f0:8", ["const:ae2864:8", "const:4:8"]]
+ 00ae2864 ["CALL", null, ["callee:00bdde40:8"]]
- 00ae2820 bytes 74ed0394
+ 00ae2864 bytes 77ed0394
- 00ae2858 ["INT_ADD", "register:40f0:8", ["const:ae2858:8", "const:4:8"]]
- 00ae2858 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae289c ["INT_ADD", "register:40f0:8", ["const:ae289c:8", "const:4:8"]]
+ 00ae289c ["CALL", null, ["callee:00551e14:8"]]
- 00ae2858 bytes 6fbde997
+ 00ae289c bytes 5ebde997
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b4341e32a4146dc8eaacb220b41f3c7"></a>

### [`00ae2920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2920.md) → [`00ae2964`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2964.md) _ZN8firebase9analytics15SetUserPropertyEPKcS2_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 5件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 5件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 93.85% / 新版 93.85%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae2980",
      "incomplete_value": true,
      "site": "00ae2980",
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
      "definition_site": "00ae293c",
      "incomplete_value": true,
      "site": "00ae293c",
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
      "definition_site": "00ae29f4",
      "incomplete_value": true,
      "site": "00ae2a08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:148:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae29b0",
      "incomplete_value": true,
      "site": "00ae29c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:108:8"
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
      "definition_site": "00ae29f8",
      "incomplete_value": true,
      "site": "00ae2a08",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae29b4",
      "incomplete_value": true,
      "site": "00ae29c4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:58:8"
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
      "00ae297c",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae29dc",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ],
    [
      "00ae29f4",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae297c",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae29dc",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ],
    [
      "00ae29f4",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae29c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2920.md#insn-00ae29c4) · [`00ae29e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2920.md#insn-00ae29e4) · [`00ae2938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2920.md#insn-00ae2938)
- 新版 [`00ae2a08`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2964.md#insn-00ae2a08) · [`00ae2a28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2964.md#insn-00ae2a28) · [`00ae297c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2964.md#insn-00ae297c)

~~~diff
- 00ae29c4 ["INT_ADD", "register:40f0:8", ["const:ae29c4:8", "const:4:8"]]
- 00ae29c4 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae2a08 ["INT_ADD", "register:40f0:8", ["const:ae2a08:8", "const:4:8"]]
+ 00ae2a08 ["CALL", null, ["callee:00551e14:8"]]
- 00ae29c4 bytes 14bde997
+ 00ae2a08 bytes 03bde997
- 00ae29e4 ["INT_ADD", "register:40f0:8", ["const:ae29e4:8", "const:4:8"]]
- 00ae29e4 ["CALL", null, ["callee:00bdde40:8"]]
+ 00ae2a28 ["INT_ADD", "register:40f0:8", ["const:ae2a28:8", "const:4:8"]]
+ 00ae2a28 ["CALL", null, ["callee:00bdde40:8"]]
- 00ae29e4 bytes 03ed0394
+ 00ae2a28 bytes 06ed0394
- 00ae2938 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
- 00ae2938 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae297c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
+ 00ae297c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae2938 bytes 088140f9
+ 00ae297c bytes 08a140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa080593954a4d891e67e4d4eb7842e1"></a>

### [`00ae2a24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2a24.md) → [`00ae2a68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2a68.md) _ZN8firebase9analytics9SetUserIdEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddae0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddae0.md) · 呼出先 5件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 1件 [`00bddb30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb30.md) · 呼出先 5件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 92.45% / 新版 92.45%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae2a80",
      "incomplete_value": true,
      "site": "00ae2a80",
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
      "definition_site": "00ae2a3c",
      "incomplete_value": true,
      "site": "00ae2a3c",
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
      "definition_site": "00ae2ad8",
      "incomplete_value": true,
      "site": "00ae2ae8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:148:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2a94",
      "incomplete_value": true,
      "site": "00ae2aa4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:108:8"
              ]
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
      "definition_site": "00ae2adc",
      "incomplete_value": true,
      "site": "00ae2ae8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2a98",
      "incomplete_value": true,
      "site": "00ae2aa4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:60:8"
              ]
            ]
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
      "00ae2a7c",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2ac0",
      "PARAM",
      [
        "storage",
        "0029316d",
        null,
        "string"
      ]
    ],
    [
      "00ae2ad8",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae2a7c",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2ac0",
      "PARAM",
      [
        "storage",
        "002930e0",
        null,
        "string"
      ]
    ],
    [
      "00ae2ad8",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2a7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2a24.md#insn-00ae2a7c) · [`00ae2aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2a24.md#insn-00ae2aa4) · [`00ae2ac0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2a24.md#insn-00ae2ac0)
- 新版 [`00ae2ac0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2a68.md#insn-00ae2ac0) · [`00ae2ae8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2a68.md#insn-00ae2ae8) · [`00ae2b04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2a68.md#insn-00ae2b04)

~~~diff
- 00ae2a7c ["COPY", "tmp:0:8", ["const:16d:8"]]
- 00ae2a7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae2a7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae2a7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae2ac0 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 00ae2ac0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae2ac0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae2ac0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae2a7c bytes 00b40591
+ 00ae2ac0 bytes 00800391
- 00ae2aa4 ["INT_ADD", "register:40f0:8", ["const:ae2aa4:8", "const:4:8"]]
- 00ae2aa4 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae2ae8 ["INT_ADD", "register:40f0:8", ["const:ae2ae8:8", "const:4:8"]]
+ 00ae2ae8 ["CALL", null, ["callee:00551e14:8"]]
- 00ae2aa4 bytes dcbce997
+ 00ae2ae8 bytes cbbce997
- 00ae2ac0 ["INT_ADD", "register:40f0:8", ["const:ae2ac0:8", "const:4:8"]]
- 00ae2ac0 ["CALL", null, ["callee:00bdde40:8"]]
+ 00ae2b04 ["INT_ADD", "register:40f0:8", ["const:ae2b04:8", "const:4:8"]]
+ 00ae2b04 ["CALL", null, ["callee:00bdde40:8"]]
- 00ae2ac0 bytes ccec0394
+ 00ae2b04 bytes cfec0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8546b4e7470d9212848bac3fbcd38228"></a>

### [`00ae2af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2af8.md) → [`00ae2b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2b3c.md) _ZN8firebase9analytics25SetSessionTimeoutDurationEl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bddad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddad0.md) · 呼出先 4件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 1件 [`00bddb20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb20.md) · 呼出先 4件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.00% / 新版 88.00%

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
      "definition_site": "00ae2b50",
      "incomplete_value": true,
      "site": "00ae2b50",
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
      "definition_site": "00ae2b0c",
      "incomplete_value": true,
      "site": "00ae2b0c",
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
      "definition_site": "00ae2b68",
      "incomplete_value": true,
      "site": "00ae2b78",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:148:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2b24",
      "incomplete_value": true,
      "site": "00ae2b34",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:108:8"
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
      "definition_site": "00ae2b6c",
      "incomplete_value": true,
      "site": "00ae2b78",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2b28",
      "incomplete_value": true,
      "site": "00ae2b34",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:68:8"
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
      "00ae2b4c",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2b68",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2b6c",
      "READ",
      [
        "storage",
        "010a0068",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae2b4c",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2b68",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2b6c",
      "READ",
      [
        "storage",
        "010a00a8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2b34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2af8.md#insn-00ae2b34) · [`00ae2b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2af8.md#insn-00ae2b50) · [`00ae2b08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2af8.md#insn-00ae2b08)
- 新版 [`00ae2b78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2b3c.md#insn-00ae2b78) · [`00ae2b94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2b3c.md#insn-00ae2b94) · [`00ae2b4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2b3c.md#insn-00ae2b4c)

~~~diff
- 00ae2b34 ["INT_ADD", "register:40f0:8", ["const:ae2b34:8", "const:4:8"]]
- 00ae2b34 ["CALL", null, ["callee:00551e14:8"]]
+ 00ae2b78 ["INT_ADD", "register:40f0:8", ["const:ae2b78:8", "const:4:8"]]
+ 00ae2b78 ["CALL", null, ["callee:00551e14:8"]]
- 00ae2b34 bytes b8bce997
+ 00ae2b78 bytes a7bce997
- 00ae2b50 ["COPY", "tmp:0:8", ["const:16d:8"]]
- 00ae2b50 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae2b50 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae2b50 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae2b94 ["COPY", "tmp:0:8", ["const:e0:8"]]
+ 00ae2b94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae2b94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae2b94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae2b50 bytes 00b40591
+ 00ae2b94 bytes 00800391
- 00ae2b08 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
- 00ae2b08 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae2b4c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
+ 00ae2b4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae2b08 bytes 088140f9
+ 00ae2b4c bytes 08a140f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b0a58eeb17b63d072be06fd7ee6f5bda"></a>

### [`00ae2b5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2b5c.md) → [`00ae2ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2ba0.md) _ZN8firebase9analytics18ResetAnalyticsDataEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 4件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 86.36% / 新版 86.36%

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
      "definition_site": "00ae2bb4",
      "incomplete_value": true,
      "site": "00ae2bb4",
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
      "definition_site": "00ae2b70",
      "incomplete_value": true,
      "site": "00ae2b70",
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
      "definition_site": "00ae2bc4",
      "incomplete_value": true,
      "site": "00ae2bd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:148:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2b80",
      "incomplete_value": true,
      "site": "00ae2b8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:108:8"
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
      "definition_site": "00ae2bc8",
      "incomplete_value": true,
      "site": "00ae2bd0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2b84",
      "incomplete_value": true,
      "site": "00ae2b8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:70:8"
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
      "00ae2bb0",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2bc4",
      "READ",
      [
        "storage",
        "010a0108",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2bc8",
      "READ",
      [
        "storage",
        "010a0070",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae2bb0",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2bc4",
      "READ",
      [
        "storage",
        "010a0148",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2bc8",
      "READ",
      [
        "storage",
        "010a00b0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2b8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2b5c.md#insn-00ae2b8c) · [`00ae2b6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2b5c.md#insn-00ae2b6c) · [`00ae2b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2b5c.md#insn-00ae2b74)
- 新版 [`00ae2bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2ba0.md#insn-00ae2bd0) · [`00ae2bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2ba0.md#insn-00ae2bb0) · [`00ae2bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2ba0.md#insn-00ae2bb8)

~~~diff
- 00ae2b8c ["INT_ADD", "register:40f0:8", ["const:ae2b8c:8", "const:4:8"]]
- 00ae2b8c ["CALL", null, ["callee:00551e14:8"]]
+ 00ae2bd0 ["INT_ADD", "register:40f0:8", ["const:ae2bd0:8", "const:4:8"]]
+ 00ae2bd0 ["CALL", null, ["callee:00551e14:8"]]
- 00ae2b8c bytes a2bce997
+ 00ae2bd0 bytes 91bce997
- 00ae2b6c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:100:8"]]
- 00ae2b6c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae2bb0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:140:8"]]
+ 00ae2bb0 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae2b6c bytes 008140f9
+ 00ae2bb0 bytes 00a140f9
- 00ae2b74 ["INT_ADD", "register:40f0:8", ["const:ae2b74:8", "const:4:8"]]
- 00ae2b74 ["CALL", null, ["callee:00bde200:8"]]
+ 00ae2bb8 ["INT_ADD", "register:40f0:8", ["const:ae2bb8:8", "const:4:8"]]
+ 00ae2bb8 ["CALL", null, ["callee:00bde200:8"]]
- 00ae2b74 bytes 8fed0394
+ 00ae2bb8 bytes 92ed0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a2a10df5ecd917b68782d3c3a5ef99a"></a>

### [`00ae2bc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2bc8.md) → [`00ae2c0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2c0c.md) _ZN8firebase9analytics22GetAnalyticsInstanceIdEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 17件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00ae3330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3330.md) [`00ae3dc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3dc8.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 17件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00ae3374`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3374.md) [`00ae3e0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e0c.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 95.76% / 新版 95.76%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae2c3c",
      "incomplete_value": true,
      "site": "00ae2c3c",
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
      "definition_site": "00ae2bf8",
      "incomplete_value": true,
      "site": "00ae2bf8",
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
      "definition_site": "00ae2c64",
      "incomplete_value": true,
      "site": "00ae2c78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae2c20",
      "incomplete_value": true,
      "site": "00ae2c34",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:868:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae2d64",
      "incomplete_value": false,
      "site": "00ae2d70",
      "value": [
        "leaf",
        "const:ae3374:8"
      ]
    },
    "old": {
      "definition_site": "00ae2d20",
      "incomplete_value": false,
      "site": "00ae2d2c",
      "value": [
        "leaf",
        "const:ae3330:8"
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
      "00ae2c38",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2c64",
      "READ",
      [
        "storage",
        "00c1b868",
        null,
        "pointer"
      ]
    ],
    [
      "00ae2c64",
      "PARAM",
      [
        "storage",
        "00ae3dc8",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae2c38",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2c64",
      "READ",
      [
        "storage",
        "00c1b8b8",
        null,
        "pointer"
      ]
    ],
    [
      "00ae2c64",
      "PARAM",
      [
        "storage",
        "00ae3e0c",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEEEvPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2c34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2bc8.md#insn-00ae2c34) · [`00ae2d2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2bc8.md#insn-00ae2d2c) · [`00ae2d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2bc8.md#insn-00ae2d70)
- 新版 [`00ae2c78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2c0c.md#insn-00ae2c78) · [`00ae2d70`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2c0c.md#insn-00ae2d70) · [`00ae2db4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2c0c.md#insn-00ae2db4)

~~~diff
- 00ae2c34 ["INT_ADD", "register:40f0:8", ["const:ae2c34:8", "const:4:8"]]
- 00ae2c34 ["CALL", null, ["callee:00bddfc0:8"]]
+ 00ae2c78 ["INT_ADD", "register:40f0:8", ["const:ae2c78:8", "const:4:8"]]
+ 00ae2c78 ["CALL", null, ["callee:00bddfc0:8"]]
- 00ae2c34 bytes cfec0394
+ 00ae2c78 bytes d2ec0394
- 00ae2d2c ["INT_ADD", "register:40f0:8", ["const:ae2d2c:8", "const:4:8"]]
- 00ae2d2c ["CALL", null, ["callee:00bde0c0:8"]]
+ 00ae2d70 ["INT_ADD", "register:40f0:8", ["const:ae2d70:8", "const:4:8"]]
+ 00ae2d70 ["CALL", null, ["callee:00bde0c0:8"]]
- 00ae2d2c bytes d1ec0394
+ 00ae2d70 bytes d4ec0394
- 00ae2d70 ["INT_ADD", "register:40f0:8", ["const:ae2d70:8", "const:4:8"]]
- 00ae2d70 ["CALL", null, ["callee:00bddc40:8"]]
+ 00ae2db4 ["INT_ADD", "register:40f0:8", ["const:ae2db4:8", "const:4:8"]]
+ 00ae2db4 ["CALL", null, ["callee:00bddc40:8"]]
- 00ae2d70 bytes a0eb0394
+ 00ae2db4 bytes a3eb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-81ac3e07d678dcbd0117bb53486754cd"></a>

### [`00ae2e1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2e1c.md) → [`00ae2e60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2e60.md) _ZN8firebase9analytics32GetAnalyticsInstanceIdLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde180.md) · 呼出先 8件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bdde00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde00.md)
- 新版 呼出元 1件 [`00bde1d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde1d0.md) · 呼出先 8件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bdde50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde50.md)

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
      "definition_site": "00ae2e7c",
      "incomplete_value": true,
      "site": "00ae2e7c",
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
      "definition_site": "00ae2e38",
      "incomplete_value": true,
      "site": "00ae2e38",
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
      "definition_site": "00ae2ed0",
      "incomplete_value": false,
      "site": "00ae2ed4",
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
      "definition_site": "00ae2e8c",
      "incomplete_value": false,
      "site": "00ae2e90",
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
        "00ae2e38"
      ],
      [
        "FALL_THROUGH",
        "00ae2e7c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae2e7c",
      "incomplete_value": true,
      "site": "00ae2eb0",
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
      "definition_site": "00ae2e38",
      "incomplete_value": true,
      "site": "00ae2e6c",
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
      "00ae2e74",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2ed0",
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
      "00ae2e74",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae2ed0",
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

- 旧版 [`00ae2e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2e1c.md#insn-00ae2e4c) · [`00ae2e90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2e1c.md#insn-00ae2e90) · [`00ae2eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2e1c.md#insn-00ae2eb0)
- 新版 [`00ae2e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2e60.md#insn-00ae2e90) · [`00ae2ed4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2e60.md#insn-00ae2ed4) · [`00ae2ef4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2e60.md#insn-00ae2ef4)

~~~diff
- 00ae2e4c ["INT_ADD", "register:40f0:8", ["const:ae2e4c:8", "const:4:8"]]
- 00ae2e4c ["CALL", null, ["callee:00bddc20:8"]]
+ 00ae2e90 ["INT_ADD", "register:40f0:8", ["const:ae2e90:8", "const:4:8"]]
+ 00ae2e90 ["CALL", null, ["callee:00bddc20:8"]]
- 00ae2e4c bytes 61eb0394
+ 00ae2e90 bytes 64eb0394
- 00ae2e90 ["INT_ADD", "register:40f0:8", ["const:ae2e90:8", "const:4:8"]]
- 00ae2e90 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae2ed4 ["INT_ADD", "register:40f0:8", ["const:ae2ed4:8", "const:4:8"]]
+ 00ae2ed4 ["CALL", null, ["callee:00bde180:8"]]
- 00ae2e90 bytes a8ec0394
+ 00ae2ed4 bytes abec0394
- 00ae2eb0 ["INT_ADD", "register:40f0:8", ["const:ae2eb0:8", "const:4:8"]]
- 00ae2eb0 ["CALL", null, ["callee:00bddd80:8"]]
+ 00ae2ef4 ["INT_ADD", "register:40f0:8", ["const:ae2ef4:8", "const:4:8"]]
+ 00ae2ef4 ["CALL", null, ["callee:00bddd80:8"]]
- 00ae2eb0 bytes a0eb0394
+ 00ae2ef4 bytes a3eb0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-88cbb2e15b3670efec36f3e7cd4aaf13"></a>

### [`00ae2f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2f90.md) → [`00ae2fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2fd4.md) _ZN8firebase9analytics12GetSessionIdEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 19件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00ae3a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3a08.md) [`00ae3e00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3e00.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)
- 新版 呼出元 0件  · 呼出先 19件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00ae3a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3a4c.md) [`00ae3e44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e44.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 92.04% / 新版 92.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae3004",
      "incomplete_value": true,
      "site": "00ae3004",
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
      "definition_site": "00ae2fc0",
      "incomplete_value": true,
      "site": "00ae2fc0",
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
      "definition_site": "00ae3048",
      "incomplete_value": true,
      "site": "00ae304c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:140:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae3004",
      "incomplete_value": true,
      "site": "00ae3008",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:100:8"
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
      "definition_site": "00ae3058",
      "incomplete_value": true,
      "site": "00ae3064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:148:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae3014",
      "incomplete_value": true,
      "site": "00ae3020",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:108:8"
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
      "00ae3000",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae301c",
      "READ",
      [
        "storage",
        "00c1b870",
        null,
        "pointer"
      ]
    ],
    [
      "00ae301c",
      "PARAM",
      [
        "storage",
        "00ae3e00",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIlEEvPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae3000",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae301c",
      "READ",
      [
        "storage",
        "00c1b8c0",
        null,
        "pointer"
      ]
    ],
    [
      "00ae301c",
      "PARAM",
      [
        "storage",
        "00ae3e44",
        "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIlEEvPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae2fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2f90.md#insn-00ae2fc4) · [`00ae3004`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2f90.md#insn-00ae3004) · [`00ae3008`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2f90.md#insn-00ae3008)
- 新版 [`00ae3008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2fd4.md#insn-00ae3008) · [`00ae3048`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2fd4.md#insn-00ae3048) · [`00ae304c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2fd4.md#insn-00ae304c)

~~~diff
- 00ae2fc4 ["INT_ADD", "register:40f0:8", ["const:ae2fc4:8", "const:4:8"]]
- 00ae2fc4 ["CALL", null, ["callee:00bdde50:8"]]
+ 00ae3008 ["INT_ADD", "register:40f0:8", ["const:ae3008:8", "const:4:8"]]
+ 00ae3008 ["CALL", null, ["callee:00bdde50:8"]]
- 00ae2fc4 bytes 8feb0394
+ 00ae3008 bytes 92eb0394
- 00ae3004 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:100:8"]]
- 00ae3004 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae3048 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:140:8"]]
+ 00ae3048 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae3004 bytes a08240f9
+ 00ae3048 bytes a0a240f9
- 00ae3008 ["INT_ADD", "register:40f0:8", ["const:ae3008:8", "const:4:8"]]
- 00ae3008 ["CALL", null, ["callee:00bde200:8"]]
+ 00ae304c ["INT_ADD", "register:40f0:8", ["const:ae304c:8", "const:4:8"]]
+ 00ae304c ["CALL", null, ["callee:00bde200:8"]]
- 00ae3008 bytes 6aec0394
+ 00ae304c bytes 6dec0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bbb0c6d295ba1c7f7c9cc3a551ca0db"></a>

### [`00ae3258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3258.md) → [`00ae329c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae329c.md) _ZN8firebase9analytics22GetSessionIdLastResultEv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 8件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bdde00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde00.md)
- 新版 呼出元 0件  · 呼出先 8件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bdde50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde50.md)

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
      "definition_site": "00ae32b8",
      "incomplete_value": true,
      "site": "00ae32b8",
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
      "definition_site": "00ae3274",
      "incomplete_value": true,
      "site": "00ae3274",
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
      "definition_site": "00ae330c",
      "incomplete_value": false,
      "site": "00ae3310",
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
      "definition_site": "00ae32c8",
      "incomplete_value": false,
      "site": "00ae32cc",
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
        "00ae3274"
      ],
      [
        "FALL_THROUGH",
        "00ae32b8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae32b8",
      "incomplete_value": true,
      "site": "00ae32ec",
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
      "definition_site": "00ae3274",
      "incomplete_value": true,
      "site": "00ae32a8",
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
      "00ae32b0",
      "READ",
      [
        "storage",
        "010a0100",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae330c",
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
      "00ae32b0",
      "READ",
      [
        "storage",
        "010a0140",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae330c",
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

- 旧版 [`00ae3288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3258.md#insn-00ae3288) · [`00ae32cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3258.md#insn-00ae32cc) · [`00ae32ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3258.md#insn-00ae32ec)
- 新版 [`00ae32cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae329c.md#insn-00ae32cc) · [`00ae3310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae329c.md#insn-00ae3310) · [`00ae3330`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae329c.md#insn-00ae3330)

~~~diff
- 00ae3288 ["INT_ADD", "register:40f0:8", ["const:ae3288:8", "const:4:8"]]
- 00ae3288 ["CALL", null, ["callee:00bddc20:8"]]
+ 00ae32cc ["INT_ADD", "register:40f0:8", ["const:ae32cc:8", "const:4:8"]]
+ 00ae32cc ["CALL", null, ["callee:00bddc20:8"]]
- 00ae3288 bytes 52ea0394
+ 00ae32cc bytes 55ea0394
- 00ae32cc ["INT_ADD", "register:40f0:8", ["const:ae32cc:8", "const:4:8"]]
- 00ae32cc ["CALL", null, ["callee:00bde180:8"]]
+ 00ae3310 ["INT_ADD", "register:40f0:8", ["const:ae3310:8", "const:4:8"]]
+ 00ae3310 ["CALL", null, ["callee:00bde180:8"]]
- 00ae32cc bytes 99eb0394
+ 00ae3310 bytes 9ceb0394
- 00ae32ec ["INT_ADD", "register:40f0:8", ["const:ae32ec:8", "const:4:8"]]
- 00ae32ec ["CALL", null, ["callee:00bddd80:8"]]
+ 00ae3330 ["INT_ADD", "register:40f0:8", ["const:ae3330:8", "const:4:8"]]
+ 00ae3330 ["CALL", null, ["callee:00bddd80:8"]]
- 00ae32ec bytes 91ea0394
+ 00ae3330 bytes 94ea0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aead43a7a33967bcaca7438401a041f7"></a>

### [`00ae3554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3554.md) → [`00ae3598`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3598.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS0_26Complet

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddeb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddeb0.md) · 呼出先 11件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00bddf00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf00.md) · 呼出先 11件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

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
      "definition_site": "00ae3604",
      "incomplete_value": false,
      "site": "00ae3608",
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
      "definition_site": "00ae35c0",
      "incomplete_value": false,
      "site": "00ae35c4",
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
      "00ae3604",
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
      "00ae3604",
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

- 旧版 [`00ae35c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3554.md#insn-00ae35c4) · [`00ae3608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3554.md#insn-00ae3608) · [`00ae3588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3554.md#insn-00ae3588)
- 新版 [`00ae3608`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3598.md#insn-00ae3608) · [`00ae364c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3598.md#insn-00ae364c) · [`00ae35cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3598.md#insn-00ae35cc)

~~~diff
- 00ae35c4 ["INT_ADD", "register:40f0:8", ["const:ae35c4:8", "const:4:8"]]
- 00ae35c4 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae3608 ["INT_ADD", "register:40f0:8", ["const:ae3608:8", "const:4:8"]]
+ 00ae3608 ["CALL", null, ["callee:00bde180:8"]]
- 00ae35c4 bytes dbea0394
+ 00ae3608 bytes deea0394
- 00ae3608 ["INT_ADD", "register:40f0:8", ["const:ae3608:8", "const:4:8"]]
- 00ae3608 ["CALL", null, ["callee:00bde230:8"]]
+ 00ae364c ["INT_ADD", "register:40f0:8", ["const:ae364c:8", "const:4:8"]]
+ 00ae364c ["CALL", null, ["callee:00bde230:8"]]
- 00ae3608 bytes f6ea0394
+ 00ae364c bytes f9ea0394
- 00ae3588 ["INT_ADD", "register:40f0:8", ["const:ae3588:8", "const:4:8"]]
- 00ae3588 ["CALL", null, ["callee:00bddc20:8"]]
+ 00ae35cc ["INT_ADD", "register:40f0:8", ["const:ae35cc:8", "const:4:8"]]
+ 00ae35cc ["CALL", null, ["callee:00bddc20:8"]]
- 00ae3588 bytes 92e90394
+ 00ae35cc bytes 95e90394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-832fae536e6a422c32e49b8cb922aa6b"></a>

### [`00ae3a08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3a08.md) → [`00ae3a4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3a4c.md) FUN_00ae3a4c

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00ae2f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae2/00ae2f90.md) · 呼出先 9件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbf0.md) [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bdde00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdde00.md)
- 新版 呼出元 1件 [`00ae2fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae2/00ae2fd4.md) · 呼出先 9件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc40.md) [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bdde50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 95.35% / 新版 95.35%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae3ad4",
      "incomplete_value": false,
      "site": "00ae3adc",
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
            "const:6d7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae3a90",
      "incomplete_value": false,
      "site": "00ae3a98",
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
            "const:6d9:8"
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
      "definition_site": "00ae3b08",
      "incomplete_value": false,
      "site": "00ae3b1c",
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
      "definition_site": "00ae3ac4",
      "incomplete_value": false,
      "site": "00ae3ad8",
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
    "ordinal": 6,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae3ab4",
      "PARAM",
      [
        "storage",
        "00292365",
        null,
        "string"
      ]
    ],
    [
      "00ae3ad4",
      "PARAM",
      [
        "storage",
        "0029a6d9",
        null,
        "string"
      ]
    ],
    [
      "00ae3b08",
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
      "00ae3ab4",
      "PARAM",
      [
        "storage",
        "002922d8",
        null,
        "string"
      ]
    ],
    [
      "00ae3ad4",
      "PARAM",
      [
        "storage",
        "0029a6d7",
        null,
        "string"
      ]
    ],
    [
      "00ae3b08",
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

- 旧版 [`00ae3a98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3a08.md#insn-00ae3a98) · [`00ae3ad8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3a08.md#insn-00ae3ad8) · [`00ae3a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3a08.md#insn-00ae3a44)
- 新版 [`00ae3adc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3a4c.md#insn-00ae3adc) · [`00ae3b1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3a4c.md#insn-00ae3b1c) · [`00ae3a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3a4c.md#insn-00ae3a88)

~~~diff
- 00ae3a98 ["INT_ADD", "register:40f0:8", ["const:ae3a98:8", "const:4:8"]]
- 00ae3a98 ["CALL", null, ["callee:00bdde40:8"]]
+ 00ae3adc ["INT_ADD", "register:40f0:8", ["const:ae3adc:8", "const:4:8"]]
+ 00ae3adc ["CALL", null, ["callee:00bdde40:8"]]
- 00ae3a98 bytes d6e80394
+ 00ae3adc bytes d9e80394
- 00ae3ad8 ["INT_ADD", "register:40f0:8", ["const:ae3ad8:8", "const:4:8"]]
- 00ae3ad8 ["CALL", null, ["callee:00bddf30:8"]]
+ 00ae3b1c ["INT_ADD", "register:40f0:8", ["const:ae3b1c:8", "const:4:8"]]
+ 00ae3b1c ["CALL", null, ["callee:00bddf30:8"]]
- 00ae3ad8 bytes 02e90394
+ 00ae3b1c bytes 05e90394
- 00ae3a44 ["INT_ADD", "register:40f0:8", ["const:ae3a44:8", "const:4:8"]]
- 00ae3a44 ["CALL", null, ["callee:00bdde50:8"]]
+ 00ae3a88 ["INT_ADD", "register:40f0:8", ["const:ae3a88:8", "const:4:8"]]
+ 00ae3a88 ["CALL", null, ["callee:00bdde50:8"]]
- 00ae3a44 bytes efe80394
+ 00ae3a88 bytes f2e80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7c76ada33621ba59499ef0a97fd92e1"></a>

### [`00ae3b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3b80.md) → [`00ae3bc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3bc4.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalImZNS0_26CompleteWithResultInternalImEEvRKNS_12FutureHandleEiPKcRKT_EUlPmE_EEvS5_i

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddee0.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00bddf30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf30.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

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
      "definition_site": "00ae3c30",
      "incomplete_value": false,
      "site": "00ae3c34",
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
      "definition_site": "00ae3bec",
      "incomplete_value": false,
      "site": "00ae3bf0",
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
      "00ae3c30",
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
      "00ae3c30",
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

- 旧版 [`00ae3bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3b80.md#insn-00ae3bf0) · [`00ae3bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3b80.md#insn-00ae3bb4) · [`00ae3bc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3b80.md#insn-00ae3bc0)
- 新版 [`00ae3c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3bc4.md#insn-00ae3c34) · [`00ae3bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3bc4.md#insn-00ae3bf8) · [`00ae3c04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3bc4.md#insn-00ae3c04)

~~~diff
- 00ae3bf0 ["INT_ADD", "register:40f0:8", ["const:ae3bf0:8", "const:4:8"]]
- 00ae3bf0 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae3c34 ["INT_ADD", "register:40f0:8", ["const:ae3c34:8", "const:4:8"]]
+ 00ae3c34 ["CALL", null, ["callee:00bde180:8"]]
- 00ae3bf0 bytes 50e90394
+ 00ae3c34 bytes 53e90394
- 00ae3bb4 ["INT_ADD", "register:40f0:8", ["const:ae3bb4:8", "const:4:8"]]
- 00ae3bb4 ["CALL", null, ["callee:00bddc20:8"]]
+ 00ae3bf8 ["INT_ADD", "register:40f0:8", ["const:ae3bf8:8", "const:4:8"]]
+ 00ae3bf8 ["CALL", null, ["callee:00bddc20:8"]]
- 00ae3bb4 bytes 07e80394
+ 00ae3bf8 bytes 0ae80394
- 00ae3bc0 ["INT_ADD", "register:40f0:8", ["const:ae3bc0:8", "const:4:8"]]
- 00ae3bc0 ["CALL", null, ["callee:00bde000:8"]]
+ 00ae3c04 ["INT_ADD", "register:40f0:8", ["const:ae3c04:8", "const:4:8"]]
+ 00ae3c04 ["CALL", null, ["callee:00bde000:8"]]
- 00ae3bc0 bytes fce80394
+ 00ae3c04 bytes ffe80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d6508f995267ecc89fb2c1cfddff800f"></a>

### [`00ae3ca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3ca4.md) → [`00ae3ce8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3ce8.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIiZNS0_26CompleteWithResultInternalIiEEvRKNS_12FutureHandleEiPKcRKT_EUlPiE_EEvS5_i

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddec0.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00bddf10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf10.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

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
      "definition_site": "00ae3d54",
      "incomplete_value": false,
      "site": "00ae3d58",
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
      "definition_site": "00ae3d10",
      "incomplete_value": false,
      "site": "00ae3d14",
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
      "00ae3d54",
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
      "00ae3d54",
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

- 旧版 [`00ae3d14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3ca4.md#insn-00ae3d14) · [`00ae3cd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3ca4.md#insn-00ae3cd8) · [`00ae3ce4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3ca4.md#insn-00ae3ce4)
- 新版 [`00ae3d58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3ce8.md#insn-00ae3d58) · [`00ae3d1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3ce8.md#insn-00ae3d1c) · [`00ae3d28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3ce8.md#insn-00ae3d28)

~~~diff
- 00ae3d14 ["INT_ADD", "register:40f0:8", ["const:ae3d14:8", "const:4:8"]]
- 00ae3d14 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae3d58 ["INT_ADD", "register:40f0:8", ["const:ae3d58:8", "const:4:8"]]
+ 00ae3d58 ["CALL", null, ["callee:00bde180:8"]]
- 00ae3d14 bytes 07e90394
+ 00ae3d58 bytes 0ae90394
- 00ae3cd8 ["INT_ADD", "register:40f0:8", ["const:ae3cd8:8", "const:4:8"]]
- 00ae3cd8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00ae3d1c ["INT_ADD", "register:40f0:8", ["const:ae3d1c:8", "const:4:8"]]
+ 00ae3d1c ["CALL", null, ["callee:00bddc20:8"]]
- 00ae3cd8 bytes bee70394
+ 00ae3d1c bytes c1e70394
- 00ae3ce4 ["INT_ADD", "register:40f0:8", ["const:ae3ce4:8", "const:4:8"]]
- 00ae3ce4 ["CALL", null, ["callee:00bde000:8"]]
+ 00ae3d28 ["INT_ADD", "register:40f0:8", ["const:ae3d28:8", "const:4:8"]]
+ 00ae3d28 ["CALL", null, ["callee:00bde000:8"]]
- 00ae3ce4 bytes b3e80394
+ 00ae3d28 bytes b6e80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-feacd45076b665e8a46e4531afa1074b"></a>

### [`00ae3e0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3e0c.md) → [`00ae3e50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e50.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIlZNS0_26CompleteWithResultInternalIlEEvRKNS_12FutureHandleEiPKcRKT_EUlPlE_EEvS5_i

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bdded0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdded0.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00bddf20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf20.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

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
      "definition_site": "00ae3ebc",
      "incomplete_value": false,
      "site": "00ae3ec0",
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
      "definition_site": "00ae3e78",
      "incomplete_value": false,
      "site": "00ae3e7c",
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
      "00ae3ebc",
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
      "00ae3ebc",
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

- 旧版 [`00ae3e7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3e0c.md#insn-00ae3e7c) · [`00ae3e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3e0c.md#insn-00ae3e40) · [`00ae3e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3e0c.md#insn-00ae3e4c)
- 新版 [`00ae3ec0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e50.md#insn-00ae3ec0) · [`00ae3e84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e50.md#insn-00ae3e84) · [`00ae3e90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3e50.md#insn-00ae3e90)

~~~diff
- 00ae3e7c ["INT_ADD", "register:40f0:8", ["const:ae3e7c:8", "const:4:8"]]
- 00ae3e7c ["CALL", null, ["callee:00bde180:8"]]
+ 00ae3ec0 ["INT_ADD", "register:40f0:8", ["const:ae3ec0:8", "const:4:8"]]
+ 00ae3ec0 ["CALL", null, ["callee:00bde180:8"]]
- 00ae3e7c bytes ade80394
+ 00ae3ec0 bytes b0e80394
- 00ae3e40 ["INT_ADD", "register:40f0:8", ["const:ae3e40:8", "const:4:8"]]
- 00ae3e40 ["CALL", null, ["callee:00bddc20:8"]]
+ 00ae3e84 ["INT_ADD", "register:40f0:8", ["const:ae3e84:8", "const:4:8"]]
+ 00ae3e84 ["CALL", null, ["callee:00bddc20:8"]]
- 00ae3e40 bytes 64e70394
+ 00ae3e84 bytes 67e70394
- 00ae3e4c ["INT_ADD", "register:40f0:8", ["const:ae3e4c:8", "const:4:8"]]
- 00ae3e4c ["CALL", null, ["callee:00bde000:8"]]
+ 00ae3e90 ["INT_ADD", "register:40f0:8", ["const:ae3e90:8", "const:4:8"]]
+ 00ae3e90 ["CALL", null, ["callee:00bde000:8"]]
- 00ae3e4c bytes 59e80394
+ 00ae3e90 bytes 5ce80394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbad57f4c502845ffb1b06adc2865bba"></a>

### [`00ae3f60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f60.md) → [`00ae3fa4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3fa4.md) _ZN8firebase23LogMessageWithCallbackVENS_8LogLevelEPKcSt9__va_list

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde250.md) · 呼出先 8件 [`00ae3f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f30.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md)
- 新版 呼出元 1件 [`00bde2a0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2a0.md) · 呼出先 8件 [`00ae3f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3f74.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition

命令の説明率　旧版 88.52% / 新版 88.52%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_condition` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00ae3fe0",
      "incomplete_value": true,
      "site": "00ae3fe0",
      "value": [
        "INT_NOTEQUAL",
        "1",
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
      "definition_site": "00ae3f9c",
      "incomplete_value": true,
      "site": "00ae3f9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
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
      "definition_site": "00ae4030",
      "incomplete_value": false,
      "site": "00ae403c",
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
            "const:161:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae3fec",
      "incomplete_value": false,
      "site": "00ae3ff8",
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
            "const:121:8"
          ]
        ]
      ]
    },
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "guard": [
      [
        "FALL_THROUGH",
        "00ae3f9c"
      ],
      [
        "FALL_THROUGH",
        "00ae3fe0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae3fe0",
      "incomplete_value": true,
      "site": "00ae3ff8",
      "value": [
        "INT_NOTEQUAL",
        "1",
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
      "definition_site": "00ae3f9c",
      "incomplete_value": true,
      "site": "00ae3fb4",
      "value": [
        "INT_NOTEQUAL",
        "1",
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
      "00ae3fd4",
      "READ",
      [
        "storage",
        "00c1b888",
        null,
        "pointer"
      ]
    ],
    [
      "00ae3fdc",
      "READ",
      [
        "storage",
        "010a0118",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ],
    [
      "00ae3ff8",
      "WRITE",
      [
        "storage",
        "010a0118",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae3fd4",
      "READ",
      [
        "storage",
        "00c1b8d8",
        null,
        "pointer"
      ]
    ],
    [
      "00ae3fdc",
      "READ",
      [
        "storage",
        "010a0158",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ],
    [
      "00ae3ff8",
      "WRITE",
      [
        "storage",
        "010a0158",
        "_ZN8firebase11g_log_mutexE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae3fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f60.md#insn-00ae3fe0) · [`00ae3ff8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f60.md#insn-00ae3ff8) · [`00ae3f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f60.md#insn-00ae3f90)
- 新版 [`00ae4024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3fa4.md#insn-00ae4024) · [`00ae403c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3fa4.md#insn-00ae403c) · [`00ae3fd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3fa4.md#insn-00ae3fd4)

~~~diff
- 00ae3fe0 ["COPY", "tmp:0:8", ["const:121:8"]]
- 00ae3fe0 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00ae3fe0 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00ae3fe0 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00ae4024 ["COPY", "tmp:0:8", ["const:161:8"]]
+ 00ae4024 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00ae4024 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00ae4024 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00ae3fe0 bytes d6860491
+ 00ae4024 bytes d6860591
- 00ae3ff8 ["INT_ADD", "register:40f0:8", ["const:ae3ff8:8", "const:4:8"]]
- 00ae3ff8 ["CALL", null, ["callee:00bde2d0:8"]]
+ 00ae403c ["INT_ADD", "register:40f0:8", ["const:ae403c:8", "const:4:8"]]
+ 00ae403c ["CALL", null, ["callee:00bde2d0:8"]]
- 00ae3ff8 bytes a2e80394
+ 00ae403c bytes a5e80394
- 00ae3f90 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:888:8"]]
- 00ae3f90 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae3fd4 ["INT_ADD", "tmp:0:8", ["register:40c0:8", "const:8d8:8"]]
+ 00ae3fd4 ["LOAD", "register:40c0:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae3f90 bytes 184744f9
+ 00ae3fd4 bytes 186f44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-182c89ebbce43cc89585e8eec56154d6"></a>

### [`00ae4488`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4488.md) → [`00ae44cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae44cc.md) _ZN8firebase14LogGetCallbackEPPv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00ae3f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f30.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00ae3f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3f74.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, return_value_candidate, store_value

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `return_value_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00ae44f4",
      "incomplete_value": true,
      "site": "00ae44f8",
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
      "definition_site": "00ae44b0",
      "incomplete_value": true,
      "site": "00ae44b4",
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
    "ordinal": 3,
    "slot": 2
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae44e4",
      "incomplete_value": false,
      "site": "00ae44e8",
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
            "const:d5d:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae44a0",
      "incomplete_value": false,
      "site": "00ae44a4",
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
            "const:d5f:8"
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
      "definition_site": "00ae4508",
      "incomplete_value": true,
      "site": "00ae4510",
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
      "definition_site": "00ae44c4",
      "incomplete_value": true,
      "site": "00ae44cc",
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
    "slot": 0
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00ae44e4",
      "PARAM",
      [
        "storage",
        "0029bd5f",
        null,
        "string"
      ]
    ],
    [
      "00ae44f0",
      "READ",
      [
        "storage",
        "00c1b898",
        null,
        "pointer"
      ]
    ],
    [
      "00ae44f4",
      "READ",
      [
        "storage",
        "010a0110",
        "_ZN8firebase19g_log_callback_dataE",
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae44e4",
      "PARAM",
      [
        "storage",
        "0029bd5d",
        null,
        "string"
      ]
    ],
    [
      "00ae44f0",
      "READ",
      [
        "storage",
        "00c1b8e8",
        null,
        "pointer"
      ]
    ],
    [
      "00ae44f4",
      "READ",
      [
        "storage",
        "010a0150",
        "_ZN8firebase19g_log_callback_dataE",
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae44a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4488.md#insn-00ae44a4) · [`00ae44a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4488.md#insn-00ae44a0) · [`00ae44ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4488.md#insn-00ae44ac)
- 新版 [`00ae44e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae44cc.md#insn-00ae44e8) · [`00ae44e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae44cc.md#insn-00ae44e4) · [`00ae44f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae44cc.md#insn-00ae44f0)

~~~diff
- 00ae44a4 ["INT_ADD", "register:40f0:8", ["const:ae44a4:8", "const:4:8"]]
- 00ae44a4 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae44e8 ["INT_ADD", "register:40f0:8", ["const:ae44e8:8", "const:4:8"]]
+ 00ae44e8 ["CALL", null, ["callee:00bde180:8"]]
- 00ae44a4 bytes 23e70394
+ 00ae44e8 bytes 26e70394
- 00ae44a0 ["COPY", "tmp:0:8", ["const:d5f:8"]]
- 00ae44a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae44a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae44a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae44e4 ["COPY", "tmp:0:8", ["const:d5d:8"]]
+ 00ae44e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae44e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae44e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae44a0 bytes 007c3591
+ 00ae44e4 bytes 00743591
- 00ae44ac ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:898:8"]]
- 00ae44ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae44f0 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:8e8:8"]]
+ 00ae44f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae44ac bytes 084d44f9
+ 00ae44f0 bytes 087544f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d1f4f1244b13cc361122efaaa0a7418"></a>

### [`00ae44d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae44d0.md) → [`00ae4514`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4514.md) FUN_00ae4514

採用 · 移動量 `+0x44` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00ae3f30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae3/00ae3f30.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde210.md)
- 新版 呼出元 1件 [`00ae3f74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae3/00ae3f74.md) · 呼出先 2件 [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bde260`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde260.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.44% / 新版 97.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae457c",
      "incomplete_value": false,
      "site": "00ae4588",
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
            "const:d98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4538",
      "incomplete_value": false,
      "site": "00ae4544",
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
            "const:d0d:8"
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
      "00ae457c",
      "PARAM",
      [
        "storage",
        "0029dd0d",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae457c",
      "PARAM",
      [
        "storage",
        "0029dd98",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae44d0.md#insn-00ae4544) · [`00ae4538`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae44d0.md#insn-00ae4538) · [`00ae4568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae44d0.md#insn-00ae4568)
- 新版 [`00ae4588`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4514.md#insn-00ae4588) · [`00ae457c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4514.md#insn-00ae457c) · [`00ae45ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4514.md#insn-00ae45ac)

~~~diff
- 00ae4544 ["INT_ADD", "register:40f0:8", ["const:ae4544:8", "const:4:8"]]
- 00ae4544 ["CALL", null, ["callee:00bde260:8"]]
+ 00ae4588 ["INT_ADD", "register:40f0:8", ["const:ae4588:8", "const:4:8"]]
+ 00ae4588 ["CALL", null, ["callee:00bde260:8"]]
- 00ae4544 bytes 33e70394
+ 00ae4588 bytes 36e70394
- 00ae4538 ["COPY", "tmp:0:8", ["const:d0d:8"]]
- 00ae4538 ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
- 00ae4538 ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
- 00ae4538 ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
+ 00ae457c ["COPY", "tmp:0:8", ["const:d98:8"]]
+ 00ae457c ["INT_CARRY", "register:105:1", ["register:4008:8", "tmp:0:8"]]
+ 00ae457c ["INT_SCARRY", "register:106:1", ["register:4008:8", "tmp:0:8"]]
+ 00ae457c ["INT_ADD", "tmp:1:8", ["register:4008:8", "tmp:0:8"]]
- 00ae4538 bytes 21343491
+ 00ae457c bytes 21603691
- 00ae4568 ["INT_ADD", "register:40f0:8", ["const:ae4568:8", "const:4:8"]]
- 00ae4568 ["CALL", null, ["callee:00bdb090:8"]]
+ 00ae45ac ["INT_ADD", "register:40f0:8", ["const:ae45ac:8", "const:4:8"]]
+ 00ae45ac ["CALL", null, ["callee:00bdb090:8"]]
- 00ae4568 bytes b6da0394
+ 00ae45ac bytes b9da0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce4754a6f72eac69a6951ed7f9aa3add"></a>

### [`00ae4708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4708.md) → [`00ae474c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae474c.md) _ZN8firebase4util12class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

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
      "definition_site": "00ae4778",
      "incomplete_value": true,
      "site": "00ae4778",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4734",
      "incomplete_value": true,
      "site": "00ae4734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "definition_site": "00ae4760",
      "incomplete_value": true,
      "site": "00ae4760",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae471c",
      "incomplete_value": true,
      "site": "00ae471c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae476c",
      "incomplete_value": false,
      "site": "00ae4770",
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
            "const:d6a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4728",
      "incomplete_value": false,
      "site": "00ae472c",
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
            "const:cd0:8"
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
      "00ae475c",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae476c",
      "PARAM",
      [
        "storage",
        "002a7cd0",
        null,
        "string"
      ]
    ],
    [
      "00ae4778",
      "WRITE",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae475c",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae476c",
      "PARAM",
      [
        "storage",
        "002a7d6a",
        null,
        "string"
      ]
    ],
    [
      "00ae4778",
      "WRITE",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae472c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4708.md#insn-00ae472c) · [`00ae4734`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4708.md#insn-00ae4734) · [`00ae4718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4708.md#insn-00ae4718)
- 新版 [`00ae4770`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae474c.md#insn-00ae4770) · [`00ae4778`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae474c.md#insn-00ae4778) · [`00ae475c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae474c.md#insn-00ae475c)

~~~diff
- 00ae472c ["INT_ADD", "register:40f0:8", ["const:ae472c:8", "const:4:8"]]
- 00ae472c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae4770 ["INT_ADD", "register:40f0:8", ["const:ae4770:8", "const:4:8"]]
+ 00ae4770 ["CALL", null, ["callee:00bde090:8"]]
- 00ae472c bytes 45e60394
+ 00ae4770 bytes 48e60394
- 00ae4734 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00ae4734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae4778 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
+ 00ae4778 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae4734 bytes 609601f9
+ 00ae4778 bytes 60b601f9
- 00ae4718 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00ae4718 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae475c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
+ 00ae475c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae4718 bytes 689641f9
+ 00ae475c bytes 68b641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dadf811f81d154431f74e7414c4f443"></a>

### [`00ae4748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4748.md) → [`00ae478c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae478c.md) _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassReq

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) · 呼出先 4件 [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md) [`00bde460`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde460.md) [`00bde6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde6a0.md)
- 新版 呼出元 1件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) · 呼出先 4件 [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md) [`00bde4b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde4b0.md) [`00bde6f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde6f0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.05% / 新版 96.05%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae47ac",
      "incomplete_value": false,
      "site": "00ae47c0",
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
            "const:110:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4768",
      "incomplete_value": false,
      "site": "00ae477c",
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
            "const:76:8"
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
      "definition_site": "00ae47f8",
      "incomplete_value": false,
      "site": "00ae4804",
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
            "const:e94:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae47b4",
      "incomplete_value": false,
      "site": "00ae47c0",
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
            "const:e09:8"
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
      "definition_site": "00ae483c",
      "incomplete_value": false,
      "site": "00ae4848",
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
            "const:609:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae47f8",
      "incomplete_value": false,
      "site": "00ae4804",
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
            "const:696:8"
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
      "00ae47ac",
      "PARAM",
      [
        "storage",
        "002a6076",
        null,
        "string"
      ]
    ],
    [
      "00ae47f8",
      "PARAM",
      [
        "storage",
        "002a1e09",
        null,
        "string"
      ]
    ],
    [
      "00ae483c",
      "PARAM",
      [
        "storage",
        "00299696",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae47ac",
      "PARAM",
      [
        "storage",
        "002a6110",
        null,
        "string"
      ]
    ],
    [
      "00ae47f8",
      "PARAM",
      [
        "storage",
        "002a1e94",
        null,
        "string"
      ]
    ],
    [
      "00ae483c",
      "PARAM",
      [
        "storage",
        "00299609",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae477c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4748.md#insn-00ae477c) · [`00ae47c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4748.md#insn-00ae47c0) · [`00ae4804`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4748.md#insn-00ae4804)
- 新版 [`00ae47c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae478c.md#insn-00ae47c0) · [`00ae4804`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae478c.md#insn-00ae4804) · [`00ae4848`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae478c.md#insn-00ae4848)

~~~diff
- 00ae477c ["INT_ADD", "register:40f0:8", ["const:ae477c:8", "const:4:8"]]
- 00ae477c ["CALL", null, ["callee:00bde2b0:8"]]
+ 00ae47c0 ["INT_ADD", "register:40f0:8", ["const:ae47c0:8", "const:4:8"]]
+ 00ae47c0 ["CALL", null, ["callee:00bde2b0:8"]]
- 00ae477c bytes b9e60394
+ 00ae47c0 bytes bce60394
- 00ae47c0 ["INT_ADD", "register:40f0:8", ["const:ae47c0:8", "const:4:8"]]
- 00ae47c0 ["CALL", null, ["callee:00bde2b0:8"]]
+ 00ae4804 ["INT_ADD", "register:40f0:8", ["const:ae4804:8", "const:4:8"]]
+ 00ae4804 ["CALL", null, ["callee:00bde2b0:8"]]
- 00ae47c0 bytes a8e60394
+ 00ae4804 bytes abe60394
- 00ae4804 ["INT_ADD", "register:40f0:8", ["const:ae4804:8", "const:4:8"]]
- 00ae4804 ["CALL", null, ["callee:00bde2b0:8"]]
+ 00ae4848 ["INT_ADD", "register:40f0:8", ["const:ae4848:8", "const:4:8"]]
+ 00ae4848 ["CALL", null, ["callee:00bde2b0:8"]]
- 00ae4804 bytes 97e60394
+ 00ae4848 bytes 9ae60394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6272cf47ecb7008bf3a97f5bd1177583"></a>

### [`00ae4878`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4878.md) → [`00ae48bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48bc.md) _ZN8firebase4util12class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

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
      "definition_site": "00ae48e8",
      "incomplete_value": true,
      "site": "00ae48e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae48a4",
      "incomplete_value": true,
      "site": "00ae48a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "definition_site": "00ae48d0",
      "incomplete_value": true,
      "site": "00ae48d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae488c",
      "incomplete_value": true,
      "site": "00ae488c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae48d8",
      "incomplete_value": false,
      "site": "00ae48e0",
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
            "const:d6a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4894",
      "incomplete_value": false,
      "site": "00ae489c",
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
            "const:cd0:8"
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
      "00ae48cc",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae48d8",
      "PARAM",
      [
        "storage",
        "002a7cd0",
        null,
        "string"
      ]
    ],
    [
      "00ae48e8",
      "WRITE",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae48cc",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae48d8",
      "PARAM",
      [
        "storage",
        "002a7d6a",
        null,
        "string"
      ]
    ],
    [
      "00ae48e8",
      "WRITE",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae489c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4878.md#insn-00ae489c) · [`00ae48a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4878.md#insn-00ae48a4) · [`00ae4888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4878.md#insn-00ae4888)
- 新版 [`00ae48e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48bc.md#insn-00ae48e0) · [`00ae48e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48bc.md#insn-00ae48e8) · [`00ae48cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48bc.md#insn-00ae48cc)

~~~diff
- 00ae489c ["INT_ADD", "register:40f0:8", ["const:ae489c:8", "const:4:8"]]
- 00ae489c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae48e0 ["INT_ADD", "register:40f0:8", ["const:ae48e0:8", "const:4:8"]]
+ 00ae48e0 ["CALL", null, ["callee:00bde090:8"]]
- 00ae489c bytes e9e50394
+ 00ae48e0 bytes ece50394
- 00ae48a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00ae48a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae48e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
+ 00ae48e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae48a4 bytes 609601f9
+ 00ae48e8 bytes 60b601f9
- 00ae4888 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00ae4888 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae48cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
+ 00ae48cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae4888 bytes 689641f9
+ 00ae48cc bytes 68b641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93d73c89e39a2a7200a54269013fd708"></a>

### [`00ae48b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae48b8.md) → [`00ae48fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48fc.md) _ZN8firebase4util12class_loader10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae492c",
      "incomplete_value": true,
      "site": "00ae492c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae48e8",
      "incomplete_value": true,
      "site": "00ae48e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "definition_site": "00ae4910",
      "incomplete_value": true,
      "site": "00ae4910",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae48cc",
      "incomplete_value": true,
      "site": "00ae48cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae48cc"
      ],
      [
        "FALL_THROUGH",
        "00ae4910"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae4910",
      "incomplete_value": true,
      "site": "00ae492c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae48cc",
      "incomplete_value": true,
      "site": "00ae48e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae490c",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae491c",
      "PARAM",
      [
        "storage",
        "002a7cd0",
        null,
        "string"
      ]
    ],
    [
      "00ae492c",
      "WRITE",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae490c",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae491c",
      "PARAM",
      [
        "storage",
        "002a7d6a",
        null,
        "string"
      ]
    ],
    [
      "00ae492c",
      "WRITE",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae48e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae48b8.md#insn-00ae48e8) · [`00ae48c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae48b8.md#insn-00ae48c8) · [`00ae48d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae48b8.md#insn-00ae48d8)
- 新版 [`00ae492c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48fc.md#insn-00ae492c) · [`00ae490c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48fc.md#insn-00ae490c) · [`00ae491c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae48fc.md#insn-00ae491c)

~~~diff
- 00ae48e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00ae48e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae492c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
+ 00ae492c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae48e8 bytes 609601f9
+ 00ae492c bytes 60b601f9
- 00ae48c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00ae48c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae490c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
+ 00ae490c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae48c8 bytes 689641f9
+ 00ae490c bytes 68b641f9
- 00ae48d8 ["COPY", "tmp:0:8", ["const:cd0:8"]]
- 00ae48d8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00ae48d8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00ae48d8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00ae491c ["COPY", "tmp:0:8", ["const:d6a:8"]]
+ 00ae491c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae491c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00ae491c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00ae48d8 bytes 63403391
+ 00ae491c bytes 63a83591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ca4486ed2ea21648ffcdc5f73e2b00d3"></a>

### [`00ae48fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae48fc.md) → [`00ae4940`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4940.md) _ZN8firebase4util12class_loader10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae4970",
      "incomplete_value": true,
      "site": "00ae4970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae492c",
      "incomplete_value": true,
      "site": "00ae492c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:328:8"
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
      "definition_site": "00ae4954",
      "incomplete_value": true,
      "site": "00ae4954",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4910",
      "incomplete_value": true,
      "site": "00ae4910",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae495c",
      "incomplete_value": false,
      "site": "00ae4968",
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
            "const:d6a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4918",
      "incomplete_value": false,
      "site": "00ae4924",
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
            "const:cd0:8"
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
      "00ae4950",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae495c",
      "PARAM",
      [
        "storage",
        "002a7cd0",
        null,
        "string"
      ]
    ],
    [
      "00ae4970",
      "WRITE",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae4950",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae495c",
      "PARAM",
      [
        "storage",
        "002a7d6a",
        null,
        "string"
      ]
    ],
    [
      "00ae4970",
      "WRITE",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4924`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae48fc.md#insn-00ae4924) · [`00ae492c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae48fc.md#insn-00ae492c) · [`00ae490c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae48fc.md#insn-00ae490c)
- 新版 [`00ae4968`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4940.md#insn-00ae4968) · [`00ae4970`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4940.md#insn-00ae4970) · [`00ae4950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4940.md#insn-00ae4950)

~~~diff
- 00ae4924 ["INT_ADD", "register:40f0:8", ["const:ae4924:8", "const:4:8"]]
- 00ae4924 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae4968 ["INT_ADD", "register:40f0:8", ["const:ae4968:8", "const:4:8"]]
+ 00ae4968 ["CALL", null, ["callee:00bde090:8"]]
- 00ae4924 bytes c7e50394
+ 00ae4968 bytes cae50394
- 00ae492c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00ae492c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae4970 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
+ 00ae4970 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae492c bytes 609601f9
+ 00ae4970 bytes 60b601f9
- 00ae490c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:328:8"]]
- 00ae490c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae4950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:368:8"]]
+ 00ae4950 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae490c bytes 689641f9
+ 00ae4950 bytes 68b641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9754b1146fe9af992b784e79e80063cc"></a>

### [`00ae494c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae494c.md) → [`00ae4990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4990.md) _ZN8firebase4util12class_loader15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae4a18",
      "incomplete_value": true,
      "site": "00ae4a18",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae49d4",
      "incomplete_value": true,
      "site": "00ae49d4",
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
            "const:330:8"
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
      "definition_site": "00ae49c4",
      "incomplete_value": true,
      "site": "00ae49d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:368:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4980",
      "incomplete_value": true,
      "site": "00ae498c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:328:8"
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
      "00ae49a4",
      "READ",
      [
        "storage",
        "010a0330",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae49c4",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4a18",
      "WRITE",
      [
        "storage",
        "010a0330",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae49a4",
      "READ",
      [
        "storage",
        "010a0370",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae49c4",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4a18",
      "WRITE",
      [
        "storage",
        "010a0370",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae498c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae494c.md#insn-00ae498c) · [`00ae49d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae494c.md#insn-00ae49d4) · [`00ae4960`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae494c.md#insn-00ae4960)
- 新版 [`00ae49d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4990.md#insn-00ae49d0) · [`00ae4a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4990.md#insn-00ae4a18) · [`00ae49a4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4990.md#insn-00ae49a4)

~~~diff
- 00ae498c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae498c ["INT_ADD", "register:40f0:8", ["const:ae498c:8", "const:4:8"]]
- 00ae498c ["CALLIND", null, ["register:0:8"]]
+ 00ae49d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae49d0 ["INT_ADD", "register:40f0:8", ["const:ae49d0:8", "const:4:8"]]
+ 00ae49d0 ["CALLIND", null, ["register:0:8"]]
- 00ae498c bytes 00013fd6
+ 00ae49d0 bytes 00013fd6
- 00ae49d4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae49d4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:330:8"]]
- 00ae49d4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae4a18 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae4a18 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:370:8"]]
+ 00ae4a18 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae49d4 bytes a0c20c39
+ 00ae4a18 bytes a0c20d39
- 00ae4960 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:330:8"]]
- 00ae4960 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae4960 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae49a4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:370:8"]]
+ 00ae49a4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae49a4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae4960 bytes a8c24c39
+ 00ae49a4 bytes a8c24d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d44358bab4d21b04d61934f40163e396"></a>

### [`00ae4a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4a44.md) → [`00ae4a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4a88.md) _ZN8firebase4util12class_loader12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae4ac4",
      "incomplete_value": true,
      "site": "00ae4ac4",
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
            "const:370:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4a80",
      "incomplete_value": true,
      "site": "00ae4a80",
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
            "const:330:8"
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
      "definition_site": "00ae4b14",
      "incomplete_value": true,
      "site": "00ae4b14",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4ad0",
      "incomplete_value": true,
      "site": "00ae4ad0",
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
            "const:328:8"
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
      "definition_site": "00ae4aa0",
      "incomplete_value": true,
      "site": "00ae4aa0",
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
      "definition_site": "00ae4a5c",
      "incomplete_value": true,
      "site": "00ae4a5c",
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
      "00ae4a9c",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4aa8",
      "READ",
      [
        "storage",
        "010a0330",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae4ac4",
      "WRITE",
      [
        "storage",
        "010a0330",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae4a9c",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4aa8",
      "READ",
      [
        "storage",
        "010a0370",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae4ac4",
      "WRITE",
      [
        "storage",
        "010a0370",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4a80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4a44.md#insn-00ae4a80) · [`00ae4acc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4a44.md#insn-00ae4acc) · [`00ae4ad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4a44.md#insn-00ae4ad0)
- 新版 [`00ae4ac4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4a88.md#insn-00ae4ac4) · [`00ae4b10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4a88.md#insn-00ae4b10) · [`00ae4b14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4a88.md#insn-00ae4b14)

~~~diff
- 00ae4a80 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae4a80 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae4a80 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:330:8"]]
- 00ae4a80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae4ac4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae4ac4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae4ac4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:370:8"]]
+ 00ae4ac4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae4a80 bytes bfc20c39
+ 00ae4ac4 bytes bfc20d39
- 00ae4acc ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae4acc ["INT_ADD", "register:40f0:8", ["const:ae4acc:8", "const:4:8"]]
- 00ae4acc ["CALLIND", null, ["register:0:8"]]
+ 00ae4b10 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae4b10 ["INT_ADD", "register:40f0:8", ["const:ae4b10:8", "const:4:8"]]
+ 00ae4b10 ["CALLIND", null, ["register:0:8"]]
- 00ae4acc bytes 00013fd6
+ 00ae4b10 bytes 00013fd6
- 00ae4ad0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
- 00ae4ad0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae4ad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae4b14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:368:8"]]
+ 00ae4b14 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae4b14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae4ad0 bytes 9f9601f9
+ 00ae4b14 bytes 9fb601f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5476c2ab85e049fb62d70b64aa9db679"></a>

### [`00ae4ae4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4ae4.md) → [`00ae4b28`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b28.md) _ZN8firebase4util12class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae4b68",
      "incomplete_value": true,
      "site": "00ae4b68",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4b24",
      "incomplete_value": true,
      "site": "00ae4b24",
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
            "const:328:8"
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
      "definition_site": "00ae4b44",
      "incomplete_value": true,
      "site": "00ae4b44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4b00",
      "incomplete_value": true,
      "site": "00ae4b00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae4b4c",
      "incomplete_value": false,
      "site": "00ae4b60",
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
            "const:d6a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4b08",
      "incomplete_value": false,
      "site": "00ae4b1c",
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
            "const:cd0:8"
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
      "00ae4b3c",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4b4c",
      "PARAM",
      [
        "storage",
        "002a7cd0",
        null,
        "string"
      ]
    ],
    [
      "00ae4b68",
      "WRITE",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae4b3c",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4b4c",
      "PARAM",
      [
        "storage",
        "002a7d6a",
        null,
        "string"
      ]
    ],
    [
      "00ae4b68",
      "WRITE",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4b1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4ae4.md#insn-00ae4b1c) · [`00ae4b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4ae4.md#insn-00ae4b24) · [`00ae4af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4ae4.md#insn-00ae4af8)
- 新版 [`00ae4b60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b28.md#insn-00ae4b60) · [`00ae4b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b28.md#insn-00ae4b68) · [`00ae4b3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b28.md#insn-00ae4b3c)

~~~diff
- 00ae4b1c ["INT_ADD", "register:40f0:8", ["const:ae4b1c:8", "const:4:8"]]
- 00ae4b1c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae4b60 ["INT_ADD", "register:40f0:8", ["const:ae4b60:8", "const:4:8"]]
+ 00ae4b60 ["CALL", null, ["callee:00bde090:8"]]
- 00ae4b1c bytes 49e50394
+ 00ae4b60 bytes 4ce50394
- 00ae4b24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
- 00ae4b24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae4b68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:368:8"]]
+ 00ae4b68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae4b24 bytes 809601f9
+ 00ae4b68 bytes 80b601f9
- 00ae4af8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
- 00ae4af8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae4b3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:368:8"]]
+ 00ae4b3c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae4af8 bytes 819641f9
+ 00ae4b3c bytes 81b641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3195384659f0487b7c19199099ce1ed5"></a>

### [`00ae4b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4b54.md) → [`00ae4b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b98.md) _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md) · 呼出先 5件 [`00af15b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af15b0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md)
- 新版 呼出元 1件 [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md) · 呼出先 5件 [`00af15f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af15f4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 93.55% / 新版 93.55%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae4bf0",
      "incomplete_value": false,
      "site": "00ae4bf8",
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
            "const:230:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4bac",
      "incomplete_value": false,
      "site": "00ae4bb4",
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
            "const:2c4:8"
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
      "definition_site": "00ae4d5c",
      "incomplete_value": false,
      "site": "00ae4d60",
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
            "const:d4f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4d18",
      "incomplete_value": false,
      "site": "00ae4d1c",
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
            "const:cc4:8"
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
      "definition_site": "00ae4d6c",
      "incomplete_value": false,
      "site": "00ae4d70",
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
            "const:d9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4d28",
      "incomplete_value": false,
      "site": "00ae4d2c",
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
            "const:d10:8"
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
      "00ae4be8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae4d44"
      ]
    ],
    [
      "00ae4bf0",
      "PARAM",
      [
        "storage",
        "002af2c4",
        null,
        "string"
      ]
    ],
    [
      "00ae4ce4",
      "PARAM",
      [
        "storage",
        "002a0ecf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae4be8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae4d88"
      ]
    ],
    [
      "00ae4bf0",
      "PARAM",
      [
        "storage",
        "002af230",
        null,
        "string"
      ]
    ],
    [
      "00ae4ce4",
      "PARAM",
      [
        "storage",
        "002a0f5a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4bb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4b54.md#insn-00ae4bb4) · [`00ae4d08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4b54.md#insn-00ae4d08) · [`00ae4d1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4b54.md#insn-00ae4d1c)
- 新版 [`00ae4bf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b98.md#insn-00ae4bf8) · [`00ae4d4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b98.md#insn-00ae4d4c) · [`00ae4d60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4b98.md#insn-00ae4d60)

~~~diff
- 00ae4bb4 ["INT_ADD", "register:40f0:8", ["const:ae4bb4:8", "const:4:8"]]
- 00ae4bb4 ["CALL", null, ["callee:00bde2b0:8"]]
+ 00ae4bf8 ["INT_ADD", "register:40f0:8", ["const:ae4bf8:8", "const:4:8"]]
+ 00ae4bf8 ["CALL", null, ["callee:00bde2b0:8"]]
- 00ae4bb4 bytes abe50394
+ 00ae4bf8 bytes aee50394
- 00ae4d08 ["INT_ADD", "register:40f0:8", ["const:ae4d08:8", "const:4:8"]]
- 00ae4d08 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae4d4c ["INT_ADD", "register:40f0:8", ["const:ae4d4c:8", "const:4:8"]]
+ 00ae4d4c ["CALL", null, ["callee:00bde180:8"]]
- 00ae4d08 bytes 0ae50394
+ 00ae4d4c bytes 0de50394
- 00ae4d1c ["INT_ADD", "register:40f0:8", ["const:ae4d1c:8", "const:4:8"]]
- 00ae4d1c ["CALL", null, ["callee:00bde180:8"]]
+ 00ae4d60 ["INT_ADD", "register:40f0:8", ["const:ae4d60:8", "const:4:8"]]
+ 00ae4d60 ["CALL", null, ["callee:00bde180:8"]]
- 00ae4d1c bytes 05e50394
+ 00ae4d60 bytes 08e50394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7d39c6bca89a45a18092a28ac992c1d6"></a>

### [`00ae4dc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4dc0.md) → [`00ae4e04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e04.md) _ZN8firebase4util12class_loader11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae4e20",
      "incomplete_value": false,
      "site": "00ae4e24",
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
      "definition_site": "00ae4ddc",
      "incomplete_value": false,
      "site": "00ae4de0",
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
      "definition_site": "00ae4e30",
      "incomplete_value": true,
      "site": "00ae4e3c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae4dec",
      "incomplete_value": true,
      "site": "00ae4df8",
      "value": [
        "LOAD",
        "8",
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
      "00ae4e20",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae4e30",
      "DATA",
      [
        "storage",
        "010a0338",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae4e20",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae4e30",
      "DATA",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4dc0.md#insn-00ae4de0) · [`00ae4ddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4dc0.md#insn-00ae4ddc) · [`00ae4de8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4dc0.md#insn-00ae4de8)
- 新版 [`00ae4e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e04.md#insn-00ae4e24) · [`00ae4e20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e04.md#insn-00ae4e20) · [`00ae4e2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e04.md#insn-00ae4e2c)

~~~diff
- 00ae4de0 ["INT_ADD", "register:40f0:8", ["const:ae4de0:8", "const:4:8"]]
- 00ae4de0 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae4e24 ["INT_ADD", "register:40f0:8", ["const:ae4e24:8", "const:4:8"]]
+ 00ae4e24 ["CALL", null, ["callee:00bde180:8"]]
- 00ae4de0 bytes d4e40394
+ 00ae4e24 bytes d7e40394
- 00ae4ddc ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae4ddc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae4ddc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae4ddc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae4e20 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae4e20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae4e20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae4e20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae4ddc bytes 00501791
+ 00ae4e20 bytes 001c1591
- 00ae4de8 ["COPY", "tmp:0:8", ["const:338:8"]]
- 00ae4de8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae4de8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae4de8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae4e2c ["COPY", "tmp:0:8", ["const:378:8"]]
+ 00ae4e2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae4e2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae4e2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae4de8 bytes 08e10c91
+ 00ae4e2c bytes 08e10d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dba8ad65b0cacad512f0f6ac87ea54b"></a>

### [`00ae4dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4dfc.md) → [`00ae4e40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e40.md) _ZN8firebase4util12class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae4e80",
      "incomplete_value": true,
      "site": "00ae4e80",
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
            "const:368:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4e3c",
      "incomplete_value": true,
      "site": "00ae4e3c",
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
            "const:328:8"
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
      "definition_site": "00ae4e5c",
      "incomplete_value": true,
      "site": "00ae4e5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4e18",
      "incomplete_value": true,
      "site": "00ae4e18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae4e64",
      "incomplete_value": false,
      "site": "00ae4e78",
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
            "const:d6a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4e20",
      "incomplete_value": false,
      "site": "00ae4e34",
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
            "const:cd0:8"
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
      "00ae4e54",
      "READ",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4e64",
      "PARAM",
      [
        "storage",
        "002a7cd0",
        null,
        "string"
      ]
    ],
    [
      "00ae4e80",
      "WRITE",
      [
        "storage",
        "010a0328",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae4e54",
      "READ",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae4e64",
      "PARAM",
      [
        "storage",
        "002a7d6a",
        null,
        "string"
      ]
    ],
    [
      "00ae4e80",
      "WRITE",
      [
        "storage",
        "010a0368",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4dfc.md#insn-00ae4e34) · [`00ae4e3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4dfc.md#insn-00ae4e3c) · [`00ae4e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4dfc.md#insn-00ae4e10)
- 新版 [`00ae4e78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e40.md#insn-00ae4e78) · [`00ae4e80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e40.md#insn-00ae4e80) · [`00ae4e54`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4e40.md#insn-00ae4e54)

~~~diff
- 00ae4e34 ["INT_ADD", "register:40f0:8", ["const:ae4e34:8", "const:4:8"]]
- 00ae4e34 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae4e78 ["INT_ADD", "register:40f0:8", ["const:ae4e78:8", "const:4:8"]]
+ 00ae4e78 ["CALL", null, ["callee:00bde090:8"]]
- 00ae4e34 bytes 83e40394
+ 00ae4e78 bytes 86e40394
- 00ae4e3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
- 00ae4e3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae4e80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:368:8"]]
+ 00ae4e80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae4e3c bytes 809601f9
+ 00ae4e80 bytes 80b601f9
- 00ae4e10 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:328:8"]]
- 00ae4e10 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae4e54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:368:8"]]
+ 00ae4e54 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae4e10 bytes 819641f9
+ 00ae4e54 bytes 81b641f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-925ca8d26afccb25c3ad2f09a8a3229f"></a>

### [`00ae4e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4e6c.md) → [`00ae4eb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4eb0.md) _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) · 呼出先 5件 [`00af15b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af15b0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md)
- 新版 呼出元 1件 [`00bde070`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde070.md) · 呼出先 5件 [`00af15f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af1/00af15f4.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdde40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde40.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde2b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde2b0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, operation_sequence

命令の説明率　旧版 92.26% / 新版 92.26%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae4f08",
      "incomplete_value": false,
      "site": "00ae4f10",
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
            "const:f4:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae4ec4",
      "incomplete_value": false,
      "site": "00ae4ecc",
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
            "const:5a:8"
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
      "definition_site": "00ae504c",
      "incomplete_value": false,
      "site": "00ae5050",
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
            "const:716:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5008",
      "incomplete_value": false,
      "site": "00ae500c",
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
            "const:718:8"
          ]
        ]
      ]
    },
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00ae5074",
      "incomplete_value": false,
      "site": "00ae5078",
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
            "const:d62:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5030",
      "incomplete_value": false,
      "site": "00ae5034",
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
            "const:cd7:8"
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
      "00ae4f00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00ae505c"
      ]
    ],
    [
      "00ae4f08",
      "PARAM",
      [
        "storage",
        "002a605a",
        null,
        "string"
      ]
    ],
    [
      "00ae4ffc",
      "PARAM",
      [
        "storage",
        "002a0ecf",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00ae4f00",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00ae50a0"
      ]
    ],
    [
      "00ae4f08",
      "PARAM",
      [
        "storage",
        "002a60f4",
        null,
        "string"
      ]
    ],
    [
      "00ae4ffc",
      "PARAM",
      [
        "storage",
        "002a0f5a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae4ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4e6c.md#insn-00ae4ecc) · [`00ae4fc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4e6c.md#insn-00ae4fc8) · [`00ae500c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4e6c.md#insn-00ae500c)
- 新版 [`00ae4f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4eb0.md#insn-00ae4f10) · [`00ae500c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4eb0.md#insn-00ae500c) · [`00ae5050`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae4/00ae4eb0.md#insn-00ae5050)

~~~diff
- 00ae4ecc ["INT_ADD", "register:40f0:8", ["const:ae4ecc:8", "const:4:8"]]
- 00ae4ecc ["CALL", null, ["callee:00bde2b0:8"]]
+ 00ae4f10 ["INT_ADD", "register:40f0:8", ["const:ae4f10:8", "const:4:8"]]
+ 00ae4f10 ["CALL", null, ["callee:00bde2b0:8"]]
- 00ae4ecc bytes e5e40394
+ 00ae4f10 bytes e8e40394
- 00ae4fc8 ["INT_ADD", "register:40f0:8", ["const:ae4fc8:8", "const:4:8"]]
- 00ae4fc8 ["CALL", null, ["callee:00af15f4:8"]]
+ 00ae500c ["INT_ADD", "register:40f0:8", ["const:ae500c:8", "const:4:8"]]
+ 00ae500c ["CALL", null, ["callee:00af15f4:8"]]
- 00ae4fc8 bytes 7a310094
+ 00ae500c bytes 7a310094
- 00ae500c ["INT_ADD", "register:40f0:8", ["const:ae500c:8", "const:4:8"]]
- 00ae500c ["CALL", null, ["callee:00bdde40:8"]]
+ 00ae5050 ["INT_ADD", "register:40f0:8", ["const:ae5050:8", "const:4:8"]]
+ 00ae5050 ["CALL", null, ["callee:00bdde40:8"]]
- 00ae500c bytes 79e30394
+ 00ae5050 bytes 7ce30394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b36e4888670092da49e90a697635b7d8"></a>

### [`00ae50d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae50d8.md) → [`00ae511c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae511c.md) _ZN8firebase4util12class_loader10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae5138",
      "incomplete_value": false,
      "site": "00ae513c",
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
      "definition_site": "00ae50f4",
      "incomplete_value": false,
      "site": "00ae50f8",
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
      "definition_site": "00ae5148",
      "incomplete_value": true,
      "site": "00ae5154",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae5104",
      "incomplete_value": true,
      "site": "00ae5110",
      "value": [
        "LOAD",
        "8",
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
      "00ae5138",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae5148",
      "DATA",
      [
        "storage",
        "010a0348",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae5138",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae5148",
      "DATA",
      [
        "storage",
        "010a0388",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae50f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae50d8.md#insn-00ae50f8) · [`00ae50f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae50d8.md#insn-00ae50f4) · [`00ae5100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae50d8.md#insn-00ae5100)
- 新版 [`00ae513c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae511c.md#insn-00ae513c) · [`00ae5138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae511c.md#insn-00ae5138) · [`00ae5144`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae511c.md#insn-00ae5144)

~~~diff
- 00ae50f8 ["INT_ADD", "register:40f0:8", ["const:ae50f8:8", "const:4:8"]]
- 00ae50f8 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae513c ["INT_ADD", "register:40f0:8", ["const:ae513c:8", "const:4:8"]]
+ 00ae513c ["CALL", null, ["callee:00bde180:8"]]
- 00ae50f8 bytes 0ee40394
+ 00ae513c bytes 11e40394
- 00ae50f4 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae50f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae50f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae50f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae5138 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae5138 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5138 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5138 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae50f4 bytes 00fc1991
+ 00ae5138 bytes 00c81791
- 00ae5100 ["COPY", "tmp:0:8", ["const:348:8"]]
- 00ae5100 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5100 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5100 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae5144 ["COPY", "tmp:0:8", ["const:388:8"]]
+ 00ae5144 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5144 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5144 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae5100 bytes 08210d91
+ 00ae5144 bytes 08210e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fb78f635cf8edb21b8966956309c82b"></a>

### [`00ae5114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5114.md) → [`00ae5158`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5158.md) _ZN8firebase4util17jniresultcallback19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00ae5184",
      "incomplete_value": true,
      "site": "00ae5184",
      "value": [
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
      "definition_site": "00ae5140",
      "incomplete_value": true,
      "site": "00ae5140",
      "value": [
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
      "definition_site": "00ae516c",
      "incomplete_value": true,
      "site": "00ae516c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5128",
      "incomplete_value": true,
      "site": "00ae5128",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae5178",
      "incomplete_value": false,
      "site": "00ae517c",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5134",
      "incomplete_value": false,
      "site": "00ae5138",
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
            "const:f35:8"
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
      "00ae5168",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5178",
      "PARAM",
      [
        "storage",
        "0029ff35",
        null,
        "string"
      ]
    ],
    [
      "00ae5184",
      "WRITE",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5168",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5178",
      "PARAM",
      [
        "storage",
        "0029ffc0",
        null,
        "string"
      ]
    ],
    [
      "00ae5184",
      "WRITE",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5114.md#insn-00ae5138) · [`00ae5140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5114.md#insn-00ae5140) · [`00ae5124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5114.md#insn-00ae5124)
- 新版 [`00ae517c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5158.md#insn-00ae517c) · [`00ae5184`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5158.md#insn-00ae5184) · [`00ae5168`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5158.md#insn-00ae5168)

~~~diff
- 00ae5138 ["INT_ADD", "register:40f0:8", ["const:ae5138:8", "const:4:8"]]
- 00ae5138 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae517c ["INT_ADD", "register:40f0:8", ["const:ae517c:8", "const:4:8"]]
+ 00ae517c ["CALL", null, ["callee:00bde090:8"]]
- 00ae5138 bytes c2e30394
+ 00ae517c bytes c5e30394
- 00ae5140 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00ae5140 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5184 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00ae5184 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5140 bytes 60aa01f9
+ 00ae5184 bytes 60ca01f9
- 00ae5124 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00ae5124 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5168 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00ae5168 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5124 bytes 68aa41f9
+ 00ae5168 bytes 68ca41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0af0b633315f6de323c99cc417fd44ea"></a>

### [`00ae5154`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5154.md) → [`00ae5198`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5198.md) _ZN8firebase4util17jniresultcallback19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00ae51c4",
      "incomplete_value": true,
      "site": "00ae51c4",
      "value": [
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
      "definition_site": "00ae5180",
      "incomplete_value": true,
      "site": "00ae5180",
      "value": [
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
      "definition_site": "00ae51ac",
      "incomplete_value": true,
      "site": "00ae51ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5168",
      "incomplete_value": true,
      "site": "00ae5168",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae51b4",
      "incomplete_value": false,
      "site": "00ae51bc",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5170",
      "incomplete_value": false,
      "site": "00ae5178",
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
            "const:f35:8"
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
      "00ae51a8",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae51b4",
      "PARAM",
      [
        "storage",
        "0029ff35",
        null,
        "string"
      ]
    ],
    [
      "00ae51c4",
      "WRITE",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae51a8",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae51b4",
      "PARAM",
      [
        "storage",
        "0029ffc0",
        null,
        "string"
      ]
    ],
    [
      "00ae51c4",
      "WRITE",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5154.md#insn-00ae5178) · [`00ae5180`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5154.md#insn-00ae5180) · [`00ae5164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5154.md#insn-00ae5164)
- 新版 [`00ae51bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5198.md#insn-00ae51bc) · [`00ae51c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5198.md#insn-00ae51c4) · [`00ae51a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5198.md#insn-00ae51a8)

~~~diff
- 00ae5178 ["INT_ADD", "register:40f0:8", ["const:ae5178:8", "const:4:8"]]
- 00ae5178 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae51bc ["INT_ADD", "register:40f0:8", ["const:ae51bc:8", "const:4:8"]]
+ 00ae51bc ["CALL", null, ["callee:00bde090:8"]]
- 00ae5178 bytes b2e30394
+ 00ae51bc bytes b5e30394
- 00ae5180 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00ae5180 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae51c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00ae51c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5180 bytes 60aa01f9
+ 00ae51c4 bytes 60ca01f9
- 00ae5164 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00ae5164 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae51a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00ae51a8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5164 bytes 68aa41f9
+ 00ae51a8 bytes 68ca41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9b824b6e76cf83079d2a3a9eb340853"></a>

### [`00ae5194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5194.md) → [`00ae51d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae51d8.md) _ZN8firebase4util17jniresultcallback10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae5208",
      "incomplete_value": true,
      "site": "00ae5208",
      "value": [
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
      "definition_site": "00ae51c4",
      "incomplete_value": true,
      "site": "00ae51c4",
      "value": [
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
      "definition_site": "00ae51ec",
      "incomplete_value": true,
      "site": "00ae51ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae51a8",
      "incomplete_value": true,
      "site": "00ae51a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae51f8",
      "incomplete_value": false,
      "site": "00ae5200",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae51b4",
      "incomplete_value": false,
      "site": "00ae51bc",
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
            "const:f35:8"
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
      "00ae51e8",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae51f8",
      "PARAM",
      [
        "storage",
        "0029ff35",
        null,
        "string"
      ]
    ],
    [
      "00ae5208",
      "WRITE",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae51e8",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae51f8",
      "PARAM",
      [
        "storage",
        "0029ffc0",
        null,
        "string"
      ]
    ],
    [
      "00ae5208",
      "WRITE",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae51bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5194.md#insn-00ae51bc) · [`00ae51c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5194.md#insn-00ae51c4) · [`00ae51a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5194.md#insn-00ae51a4)
- 新版 [`00ae5200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae51d8.md#insn-00ae5200) · [`00ae5208`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae51d8.md#insn-00ae5208) · [`00ae51e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae51d8.md#insn-00ae51e8)

~~~diff
- 00ae51bc ["INT_ADD", "register:40f0:8", ["const:ae51bc:8", "const:4:8"]]
- 00ae51bc ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5200 ["INT_ADD", "register:40f0:8", ["const:ae5200:8", "const:4:8"]]
+ 00ae5200 ["CALL", null, ["callee:00bde090:8"]]
- 00ae51bc bytes a1e30394
+ 00ae5200 bytes a4e30394
- 00ae51c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00ae51c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5208 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00ae5208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae51c4 bytes 60aa01f9
+ 00ae5208 bytes 60ca01f9
- 00ae51a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00ae51a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae51e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00ae51e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae51a4 bytes 68aa41f9
+ 00ae51e8 bytes 68ca41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b5d09fa316347addbd03afcdef5086f3"></a>

### [`00ae51d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae51d8.md) → [`00ae521c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae521c.md) _ZN8firebase4util17jniresultcallback10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae524c",
      "incomplete_value": true,
      "site": "00ae524c",
      "value": [
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
      "definition_site": "00ae5208",
      "incomplete_value": true,
      "site": "00ae5208",
      "value": [
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
      "definition_site": "00ae5230",
      "incomplete_value": true,
      "site": "00ae5230",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae51ec",
      "incomplete_value": true,
      "site": "00ae51ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae5238",
      "incomplete_value": false,
      "site": "00ae5244",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae51f4",
      "incomplete_value": false,
      "site": "00ae5200",
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
            "const:f35:8"
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
      "00ae522c",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5238",
      "PARAM",
      [
        "storage",
        "0029ff35",
        null,
        "string"
      ]
    ],
    [
      "00ae524c",
      "WRITE",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae522c",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5238",
      "PARAM",
      [
        "storage",
        "0029ffc0",
        null,
        "string"
      ]
    ],
    [
      "00ae524c",
      "WRITE",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae51d8.md#insn-00ae5200) · [`00ae5208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae51d8.md#insn-00ae5208) · [`00ae51e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae51d8.md#insn-00ae51e8)
- 新版 [`00ae5244`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae521c.md#insn-00ae5244) · [`00ae524c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae521c.md#insn-00ae524c) · [`00ae522c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae521c.md#insn-00ae522c)

~~~diff
- 00ae5200 ["INT_ADD", "register:40f0:8", ["const:ae5200:8", "const:4:8"]]
- 00ae5200 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5244 ["INT_ADD", "register:40f0:8", ["const:ae5244:8", "const:4:8"]]
+ 00ae5244 ["CALL", null, ["callee:00bde090:8"]]
- 00ae5200 bytes 90e30394
+ 00ae5244 bytes 93e30394
- 00ae5208 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00ae5208 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae524c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00ae524c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5208 bytes 60aa01f9
+ 00ae524c bytes 60ca01f9
- 00ae51e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:350:8"]]
- 00ae51e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae522c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:390:8"]]
+ 00ae522c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae51e8 bytes 68aa41f9
+ 00ae522c bytes 68ca41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d21bad1dae1f43873e6739081e07df9e"></a>

### [`00ae5228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5228.md) → [`00ae526c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae526c.md) _ZN8firebase4util17jniresultcallback15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae52f4",
      "incomplete_value": true,
      "site": "00ae52f4",
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
      "definition_site": "00ae52b0",
      "incomplete_value": true,
      "site": "00ae52b0",
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
      "definition_site": "00ae52a0",
      "incomplete_value": true,
      "site": "00ae52ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:390:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae525c",
      "incomplete_value": true,
      "site": "00ae5268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00ae5280",
      "READ",
      [
        "storage",
        "010a0358",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae52a0",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae52f4",
      "WRITE",
      [
        "storage",
        "010a0358",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae5280",
      "READ",
      [
        "storage",
        "010a0398",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae52a0",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae52f4",
      "WRITE",
      [
        "storage",
        "010a0398",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5268`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5228.md#insn-00ae5268) · [`00ae52b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5228.md#insn-00ae52b0) · [`00ae523c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5228.md#insn-00ae523c)
- 新版 [`00ae52ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae526c.md#insn-00ae52ac) · [`00ae52f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae526c.md#insn-00ae52f4) · [`00ae5280`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae526c.md#insn-00ae5280)

~~~diff
- 00ae5268 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae5268 ["INT_ADD", "register:40f0:8", ["const:ae5268:8", "const:4:8"]]
- 00ae5268 ["CALLIND", null, ["register:0:8"]]
+ 00ae52ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae52ac ["INT_ADD", "register:40f0:8", ["const:ae52ac:8", "const:4:8"]]
+ 00ae52ac ["CALLIND", null, ["register:0:8"]]
- 00ae5268 bytes 00013fd6
+ 00ae52ac bytes 00013fd6
- 00ae52b0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae52b0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:358:8"]]
- 00ae52b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae52f4 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae52f4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:398:8"]]
+ 00ae52f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae52b0 bytes a0620d39
+ 00ae52f4 bytes a0620e39
- 00ae523c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:358:8"]]
- 00ae523c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae523c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae5280 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:398:8"]]
+ 00ae5280 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5280 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae523c bytes a8624d39
+ 00ae5280 bytes a8624e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a3386757144317d6d04aeabf792025c"></a>

### [`00ae52c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae52c4.md) → [`00ae5308`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5308.md) _ZN8firebase4util17jniresultcallback12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae5344",
      "incomplete_value": true,
      "site": "00ae5344",
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
      "definition_site": "00ae5300",
      "incomplete_value": true,
      "site": "00ae5300",
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
      "definition_site": "00ae5394",
      "incomplete_value": true,
      "site": "00ae5394",
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
      "definition_site": "00ae5350",
      "incomplete_value": true,
      "site": "00ae5350",
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
      "definition_site": "00ae5320",
      "incomplete_value": true,
      "site": "00ae5320",
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
      "definition_site": "00ae52dc",
      "incomplete_value": true,
      "site": "00ae52dc",
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
      "00ae531c",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5328",
      "READ",
      [
        "storage",
        "010a0358",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae5344",
      "WRITE",
      [
        "storage",
        "010a0358",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae531c",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5328",
      "READ",
      [
        "storage",
        "010a0398",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae5344",
      "WRITE",
      [
        "storage",
        "010a0398",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5300`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae52c4.md#insn-00ae5300) · [`00ae534c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae52c4.md#insn-00ae534c) · [`00ae5350`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae52c4.md#insn-00ae5350)
- 新版 [`00ae5344`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5308.md#insn-00ae5344) · [`00ae5390`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5308.md#insn-00ae5390) · [`00ae5394`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5308.md#insn-00ae5394)

~~~diff
- 00ae5300 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae5300 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae5300 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:358:8"]]
- 00ae5300 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae5344 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae5344 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae5344 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:398:8"]]
+ 00ae5344 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae5300 bytes bf620d39
+ 00ae5344 bytes bf620e39
- 00ae534c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae534c ["INT_ADD", "register:40f0:8", ["const:ae534c:8", "const:4:8"]]
- 00ae534c ["CALLIND", null, ["register:0:8"]]
+ 00ae5390 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae5390 ["INT_ADD", "register:40f0:8", ["const:ae5390:8", "const:4:8"]]
+ 00ae5390 ["CALLIND", null, ["register:0:8"]]
- 00ae534c bytes 00013fd6
+ 00ae5390 bytes 00013fd6
- 00ae5350 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00ae5350 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae5350 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae5394 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
+ 00ae5394 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae5394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae5350 bytes 9faa01f9
+ 00ae5394 bytes 9fca01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-648494e261beb2b7189bace3841b6661"></a>

### [`00ae5364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5364.md) → [`00ae53a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae53a8.md) _ZN8firebase4util17jniresultcallback14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae53e8",
      "incomplete_value": true,
      "site": "00ae53e8",
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
      "definition_site": "00ae53a4",
      "incomplete_value": true,
      "site": "00ae53a4",
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
      "definition_site": "00ae53c4",
      "incomplete_value": true,
      "site": "00ae53c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5380",
      "incomplete_value": true,
      "site": "00ae5380",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae53cc",
      "incomplete_value": false,
      "site": "00ae53e0",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5388",
      "incomplete_value": false,
      "site": "00ae539c",
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
            "const:f35:8"
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
      "00ae53bc",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae53cc",
      "PARAM",
      [
        "storage",
        "0029ff35",
        null,
        "string"
      ]
    ],
    [
      "00ae53e8",
      "WRITE",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae53bc",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae53cc",
      "PARAM",
      [
        "storage",
        "0029ffc0",
        null,
        "string"
      ]
    ],
    [
      "00ae53e8",
      "WRITE",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae539c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5364.md#insn-00ae539c) · [`00ae53a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5364.md#insn-00ae53a4) · [`00ae5378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5364.md#insn-00ae5378)
- 新版 [`00ae53e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae53a8.md#insn-00ae53e0) · [`00ae53e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae53a8.md#insn-00ae53e8) · [`00ae53bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae53a8.md#insn-00ae53bc)

~~~diff
- 00ae539c ["INT_ADD", "register:40f0:8", ["const:ae539c:8", "const:4:8"]]
- 00ae539c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae53e0 ["INT_ADD", "register:40f0:8", ["const:ae53e0:8", "const:4:8"]]
+ 00ae53e0 ["CALL", null, ["callee:00bde090:8"]]
- 00ae539c bytes 29e30394
+ 00ae53e0 bytes 2ce30394
- 00ae53a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00ae53a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae53e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
+ 00ae53e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae53a4 bytes 80aa01f9
+ 00ae53e8 bytes 80ca01f9
- 00ae5378 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00ae5378 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae53bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
+ 00ae53bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5378 bytes 81aa41f9
+ 00ae53bc bytes 81ca41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e866311fbb8e18989410b5c3a12a7f3"></a>

### [`00ae53d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae53d4.md) → [`00ae5418`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5418.md) _ZN8firebase4util17jniresultcallback11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae5434",
      "incomplete_value": false,
      "site": "00ae5438",
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
      "definition_site": "00ae53f0",
      "incomplete_value": false,
      "site": "00ae53f4",
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
      "00ae5434",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae5444",
      "DATA",
      [
        "storage",
        "010a0360",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5434",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae5444",
      "DATA",
      [
        "storage",
        "010a03a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae53f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae53d4.md#insn-00ae53f4) · [`00ae53f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae53d4.md#insn-00ae53f0) · [`00ae53fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae53d4.md#insn-00ae53fc)
- 新版 [`00ae5438`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5418.md#insn-00ae5438) · [`00ae5434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5418.md#insn-00ae5434) · [`00ae5440`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5418.md#insn-00ae5440)

~~~diff
- 00ae53f4 ["INT_ADD", "register:40f0:8", ["const:ae53f4:8", "const:4:8"]]
- 00ae53f4 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae5438 ["INT_ADD", "register:40f0:8", ["const:ae5438:8", "const:4:8"]]
+ 00ae5438 ["CALL", null, ["callee:00bde180:8"]]
- 00ae53f4 bytes 4fe30394
+ 00ae5438 bytes 52e30394
- 00ae53f0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae53f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae53f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae53f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae5434 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae5434 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5434 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5434 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae53f0 bytes 00501791
+ 00ae5434 bytes 001c1591
- 00ae53fc ["COPY", "tmp:0:8", ["const:360:8"]]
- 00ae53fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae53fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae53fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae5440 ["COPY", "tmp:0:8", ["const:3a0:8"]]
+ 00ae5440 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5440 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5440 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae53fc bytes 08810d91
+ 00ae5440 bytes 08810e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46de856473c701513b859e6d1f921db7"></a>

### [`00ae5410`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5410.md) → [`00ae5454`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5454.md) _ZN8firebase4util17jniresultcallback13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae5494",
      "incomplete_value": true,
      "site": "00ae5494",
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
      "definition_site": "00ae5450",
      "incomplete_value": true,
      "site": "00ae5450",
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
      "definition_site": "00ae5470",
      "incomplete_value": true,
      "site": "00ae5470",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae542c",
      "incomplete_value": true,
      "site": "00ae542c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae5478",
      "incomplete_value": false,
      "site": "00ae548c",
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
            "const:fc0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5434",
      "incomplete_value": false,
      "site": "00ae5448",
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
            "const:f35:8"
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
      "00ae5468",
      "READ",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5478",
      "PARAM",
      [
        "storage",
        "0029ff35",
        null,
        "string"
      ]
    ],
    [
      "00ae5494",
      "WRITE",
      [
        "storage",
        "010a0350",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5468",
      "READ",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5478",
      "PARAM",
      [
        "storage",
        "0029ffc0",
        null,
        "string"
      ]
    ],
    [
      "00ae5494",
      "WRITE",
      [
        "storage",
        "010a0390",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5410.md#insn-00ae5448) · [`00ae5450`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5410.md#insn-00ae5450) · [`00ae5424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5410.md#insn-00ae5424)
- 新版 [`00ae548c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5454.md#insn-00ae548c) · [`00ae5494`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5454.md#insn-00ae5494) · [`00ae5468`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5454.md#insn-00ae5468)

~~~diff
- 00ae5448 ["INT_ADD", "register:40f0:8", ["const:ae5448:8", "const:4:8"]]
- 00ae5448 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae548c ["INT_ADD", "register:40f0:8", ["const:ae548c:8", "const:4:8"]]
+ 00ae548c ["CALL", null, ["callee:00bde090:8"]]
- 00ae5448 bytes fee20394
+ 00ae548c bytes 01e30394
- 00ae5450 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00ae5450 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5494 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
+ 00ae5494 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5450 bytes 80aa01f9
+ 00ae5494 bytes 80ca01f9
- 00ae5424 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:350:8"]]
- 00ae5424 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5468 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:390:8"]]
+ 00ae5468 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5424 bytes 81aa41f9
+ 00ae5468 bytes 81ca41f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e043e35900e60b94eedbb3d4e5de9a9"></a>

### [`00ae5480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5480.md) → [`00ae54c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae54c4.md) _ZN8firebase4util17jniresultcallback10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae54e0",
      "incomplete_value": false,
      "site": "00ae54e4",
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
      "definition_site": "00ae549c",
      "incomplete_value": false,
      "site": "00ae54a0",
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
      "definition_site": "00ae54f0",
      "incomplete_value": true,
      "site": "00ae54fc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae54ac",
      "incomplete_value": true,
      "site": "00ae54b8",
      "value": [
        "LOAD",
        "8",
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
      "00ae54e0",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae54f0",
      "DATA",
      [
        "storage",
        "010a0370",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae54e0",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae54f0",
      "DATA",
      [
        "storage",
        "010a03b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae54a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5480.md#insn-00ae54a0) · [`00ae549c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5480.md#insn-00ae549c) · [`00ae54a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5480.md#insn-00ae54a8)
- 新版 [`00ae54e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae54c4.md#insn-00ae54e4) · [`00ae54e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae54c4.md#insn-00ae54e0) · [`00ae54ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae54c4.md#insn-00ae54ec)

~~~diff
- 00ae54a0 ["INT_ADD", "register:40f0:8", ["const:ae54a0:8", "const:4:8"]]
- 00ae54a0 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae54e4 ["INT_ADD", "register:40f0:8", ["const:ae54e4:8", "const:4:8"]]
+ 00ae54e4 ["CALL", null, ["callee:00bde180:8"]]
- 00ae54a0 bytes 24e30394
+ 00ae54e4 bytes 27e30394
- 00ae549c ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae549c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae549c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae549c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae54e0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae54e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae54e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae54e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae549c bytes 00fc1991
+ 00ae54e0 bytes 00c81791
- 00ae54a8 ["COPY", "tmp:0:8", ["const:370:8"]]
- 00ae54a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae54a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae54a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae54ec ["COPY", "tmp:0:8", ["const:3b0:8"]]
+ 00ae54ec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae54ec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae54ec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae54a8 bytes 08c10d91
+ 00ae54ec bytes 08c10e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3a48a4e78c0585a8fbca4c4e0de96716"></a>

### [`00ae54bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae54bc.md) → [`00ae5500`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5500.md) _ZN8firebase4util26cppthreaddispatchercontext19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

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
      "definition_site": "00ae552c",
      "incomplete_value": true,
      "site": "00ae552c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae54e8",
      "incomplete_value": true,
      "site": "00ae54e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "definition_site": "00ae5514",
      "incomplete_value": true,
      "site": "00ae5514",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae54d0",
      "incomplete_value": true,
      "site": "00ae54d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae54d0"
      ],
      [
        "FALL_THROUGH",
        "00ae5514"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae5514",
      "incomplete_value": true,
      "site": "00ae552c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae54d0",
      "incomplete_value": true,
      "site": "00ae54e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae5510",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae552c",
      "WRITE",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5510",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae552c",
      "WRITE",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae54e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae54bc.md#insn-00ae54e8) · [`00ae54cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae54bc.md#insn-00ae54cc) · [`00ae54e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae54bc.md#insn-00ae54e0)
- 新版 [`00ae552c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5500.md#insn-00ae552c) · [`00ae5510`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5500.md#insn-00ae5510) · [`00ae5524`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5500.md#insn-00ae5524)

~~~diff
- 00ae54e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:378:8"]]
- 00ae54e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae552c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b8:8"]]
+ 00ae552c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae54e8 bytes 60be01f9
+ 00ae552c bytes 60de01f9
- 00ae54cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:378:8"]]
- 00ae54cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5510 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b8:8"]]
+ 00ae5510 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae54cc bytes 68be41f9
+ 00ae5510 bytes 68de41f9
- 00ae54e0 ["INT_ADD", "register:40f0:8", ["const:ae54e0:8", "const:4:8"]]
- 00ae54e0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5524 ["INT_ADD", "register:40f0:8", ["const:ae5524:8", "const:4:8"]]
+ 00ae5524 ["CALL", null, ["callee:00bde090:8"]]
- 00ae54e0 bytes d8e20394
+ 00ae5524 bytes dbe20394
~~~


<a id="compare-73640d502b0d47325743d4040846f22f"></a>

### [`00ae54fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae54fc.md) → [`00ae5540`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5540.md) _ZN8firebase4util26cppthreaddispatchercontext19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9al

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
      "definition_site": "00ae556c",
      "incomplete_value": true,
      "site": "00ae556c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5528",
      "incomplete_value": true,
      "site": "00ae5528",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "definition_site": "00ae5554",
      "incomplete_value": true,
      "site": "00ae5554",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5510",
      "incomplete_value": true,
      "site": "00ae5510",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae5510"
      ],
      [
        "FALL_THROUGH",
        "00ae5554"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae5554",
      "incomplete_value": true,
      "site": "00ae556c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5510",
      "incomplete_value": true,
      "site": "00ae5528",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae5550",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae556c",
      "WRITE",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5550",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae556c",
      "WRITE",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5528`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae54fc.md#insn-00ae5528) · [`00ae550c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae54fc.md#insn-00ae550c) · [`00ae5520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae54fc.md#insn-00ae5520)
- 新版 [`00ae556c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5540.md#insn-00ae556c) · [`00ae5550`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5540.md#insn-00ae5550) · [`00ae5564`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5540.md#insn-00ae5564)

~~~diff
- 00ae5528 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:378:8"]]
- 00ae5528 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae556c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b8:8"]]
+ 00ae556c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5528 bytes 60be01f9
+ 00ae556c bytes 60de01f9
- 00ae550c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:378:8"]]
- 00ae550c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5550 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b8:8"]]
+ 00ae5550 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae550c bytes 68be41f9
+ 00ae5550 bytes 68de41f9
- 00ae5520 ["INT_ADD", "register:40f0:8", ["const:ae5520:8", "const:4:8"]]
- 00ae5520 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5564 ["INT_ADD", "register:40f0:8", ["const:ae5564:8", "const:4:8"]]
+ 00ae5564 ["CALL", null, ["callee:00bde090:8"]]
- 00ae5520 bytes c8e20394
+ 00ae5564 bytes cbe20394
~~~


<a id="compare-d72decaa2517f12f9b1b126fb7782e6d"></a>

### [`00ae553c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae553c.md) → [`00ae5580`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5580.md) _ZN8firebase4util26cppthreaddispatchercontext10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae55b0",
      "incomplete_value": true,
      "site": "00ae55b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae556c",
      "incomplete_value": true,
      "site": "00ae556c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "definition_site": "00ae5594",
      "incomplete_value": true,
      "site": "00ae5594",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5550",
      "incomplete_value": true,
      "site": "00ae5550",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae5550"
      ],
      [
        "FALL_THROUGH",
        "00ae5594"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae5594",
      "incomplete_value": true,
      "site": "00ae55b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5550",
      "incomplete_value": true,
      "site": "00ae556c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae5590",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae55b0",
      "WRITE",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5590",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae55b0",
      "WRITE",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae556c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae553c.md#insn-00ae556c) · [`00ae554c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae553c.md#insn-00ae554c) · [`00ae5564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae553c.md#insn-00ae5564)
- 新版 [`00ae55b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5580.md#insn-00ae55b0) · [`00ae5590`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5580.md#insn-00ae5590) · [`00ae55a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5580.md#insn-00ae55a8)

~~~diff
- 00ae556c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:378:8"]]
- 00ae556c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae55b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b8:8"]]
+ 00ae55b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae556c bytes 60be01f9
+ 00ae55b0 bytes 60de01f9
- 00ae554c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:378:8"]]
- 00ae554c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5590 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b8:8"]]
+ 00ae5590 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae554c bytes 68be41f9
+ 00ae5590 bytes 68de41f9
- 00ae5564 ["INT_ADD", "register:40f0:8", ["const:ae5564:8", "const:4:8"]]
- 00ae5564 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae55a8 ["INT_ADD", "register:40f0:8", ["const:ae55a8:8", "const:4:8"]]
+ 00ae55a8 ["CALL", null, ["callee:00bde090:8"]]
- 00ae5564 bytes b7e20394
+ 00ae55a8 bytes bae20394
~~~


<a id="compare-84d2d67fcd21f493ca56ab60f21e8da3"></a>

### [`00ae5580`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5580.md) → [`00ae55c4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae55c4.md) _ZN8firebase4util26cppthreaddispatchercontext10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae55f4",
      "incomplete_value": true,
      "site": "00ae55f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae55b0",
      "incomplete_value": true,
      "site": "00ae55b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:378:8"
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
      "definition_site": "00ae55d8",
      "incomplete_value": true,
      "site": "00ae55d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5594",
      "incomplete_value": true,
      "site": "00ae5594",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae5594"
      ],
      [
        "FALL_THROUGH",
        "00ae55d8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae55d8",
      "incomplete_value": true,
      "site": "00ae55f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5594",
      "incomplete_value": true,
      "site": "00ae55b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae55d4",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae55f4",
      "WRITE",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae55d4",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae55f4",
      "WRITE",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae55b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5580.md#insn-00ae55b0) · [`00ae5590`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5580.md#insn-00ae5590) · [`00ae55a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5580.md#insn-00ae55a8)
- 新版 [`00ae55f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae55c4.md#insn-00ae55f4) · [`00ae55d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae55c4.md#insn-00ae55d4) · [`00ae55ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae55c4.md#insn-00ae55ec)

~~~diff
- 00ae55b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:378:8"]]
- 00ae55b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae55f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b8:8"]]
+ 00ae55f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae55b0 bytes 60be01f9
+ 00ae55f4 bytes 60de01f9
- 00ae5590 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:378:8"]]
- 00ae5590 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae55d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b8:8"]]
+ 00ae55d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5590 bytes 68be41f9
+ 00ae55d4 bytes 68de41f9
- 00ae55a8 ["INT_ADD", "register:40f0:8", ["const:ae55a8:8", "const:4:8"]]
- 00ae55a8 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae55ec ["INT_ADD", "register:40f0:8", ["const:ae55ec:8", "const:4:8"]]
+ 00ae55ec ["CALL", null, ["callee:00bde090:8"]]
- 00ae55a8 bytes a6e20394
+ 00ae55ec bytes a9e20394
~~~


<a id="compare-76c5b1053f10674497fe9d05940db67a"></a>

### [`00ae55d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae55d0.md) → [`00ae5614`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5614.md) _ZN8firebase4util26cppthreaddispatchercontext15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae569c",
      "incomplete_value": true,
      "site": "00ae569c",
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
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5658",
      "incomplete_value": true,
      "site": "00ae5658",
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
            "const:380:8"
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
      "definition_site": "00ae5648",
      "incomplete_value": true,
      "site": "00ae5654",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5604",
      "incomplete_value": true,
      "site": "00ae5610",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:378:8"
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
      "00ae5628",
      "READ",
      [
        "storage",
        "010a0380",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae5648",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae569c",
      "WRITE",
      [
        "storage",
        "010a0380",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae5628",
      "READ",
      [
        "storage",
        "010a03c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae5648",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae569c",
      "WRITE",
      [
        "storage",
        "010a03c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae55d0.md#insn-00ae5610) · [`00ae5658`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae55d0.md#insn-00ae5658) · [`00ae55e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae55d0.md#insn-00ae55e4)
- 新版 [`00ae5654`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5614.md#insn-00ae5654) · [`00ae569c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5614.md#insn-00ae569c) · [`00ae5628`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5614.md#insn-00ae5628)

~~~diff
- 00ae5610 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae5610 ["INT_ADD", "register:40f0:8", ["const:ae5610:8", "const:4:8"]]
- 00ae5610 ["CALLIND", null, ["register:0:8"]]
+ 00ae5654 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae5654 ["INT_ADD", "register:40f0:8", ["const:ae5654:8", "const:4:8"]]
+ 00ae5654 ["CALLIND", null, ["register:0:8"]]
- 00ae5610 bytes 00013fd6
+ 00ae5654 bytes 00013fd6
- 00ae5658 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae5658 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:380:8"]]
- 00ae5658 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae569c ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae569c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3c0:8"]]
+ 00ae569c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae5658 bytes a0020e39
+ 00ae569c bytes a0020f39
- 00ae55e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:380:8"]]
- 00ae55e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae55e4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae5628 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3c0:8"]]
+ 00ae5628 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5628 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae55e4 bytes a8024e39
+ 00ae5628 bytes a8024f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-184601ecf997c5e1facd88cbdb959468"></a>

### [`00ae566c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae566c.md) → [`00ae56b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae56b0.md) _ZN8firebase4util26cppthreaddispatchercontext12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae56ec",
      "incomplete_value": true,
      "site": "00ae56ec",
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
            "const:3c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae56a8",
      "incomplete_value": true,
      "site": "00ae56a8",
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
            "const:380:8"
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
      "definition_site": "00ae573c",
      "incomplete_value": true,
      "site": "00ae573c",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae56f8",
      "incomplete_value": true,
      "site": "00ae56f8",
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
            "const:378:8"
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
      "definition_site": "00ae56c8",
      "incomplete_value": true,
      "site": "00ae56c8",
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
      "definition_site": "00ae5684",
      "incomplete_value": true,
      "site": "00ae5684",
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
      "00ae56c4",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae56d0",
      "READ",
      [
        "storage",
        "010a0380",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae56ec",
      "WRITE",
      [
        "storage",
        "010a0380",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae56c4",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae56d0",
      "READ",
      [
        "storage",
        "010a03c0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae56ec",
      "WRITE",
      [
        "storage",
        "010a03c0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae56a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae566c.md#insn-00ae56a8) · [`00ae56f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae566c.md#insn-00ae56f4) · [`00ae56f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae566c.md#insn-00ae56f8)
- 新版 [`00ae56ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae56b0.md#insn-00ae56ec) · [`00ae5738`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae56b0.md#insn-00ae5738) · [`00ae573c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae56b0.md#insn-00ae573c)

~~~diff
- 00ae56a8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae56a8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae56a8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:380:8"]]
- 00ae56a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae56ec ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae56ec ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae56ec ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3c0:8"]]
+ 00ae56ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae56a8 bytes bf020e39
+ 00ae56ec bytes bf020f39
- 00ae56f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae56f4 ["INT_ADD", "register:40f0:8", ["const:ae56f4:8", "const:4:8"]]
- 00ae56f4 ["CALLIND", null, ["register:0:8"]]
+ 00ae5738 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae5738 ["INT_ADD", "register:40f0:8", ["const:ae5738:8", "const:4:8"]]
+ 00ae5738 ["CALLIND", null, ["register:0:8"]]
- 00ae56f4 bytes 00013fd6
+ 00ae5738 bytes 00013fd6
- 00ae56f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:378:8"]]
- 00ae56f8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae56f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae573c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b8:8"]]
+ 00ae573c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae573c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae56f8 bytes 9fbe01f9
+ 00ae573c bytes 9fde01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c212145a4a79643c1dff47362b6d910d"></a>

### [`00ae570c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae570c.md) → [`00ae5750`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5750.md) _ZN8firebase4util26cppthreaddispatchercontext14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae5790",
      "incomplete_value": true,
      "site": "00ae5790",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae574c",
      "incomplete_value": true,
      "site": "00ae574c",
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
            "const:378:8"
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
      "definition_site": "00ae576c",
      "incomplete_value": true,
      "site": "00ae576c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5728",
      "incomplete_value": true,
      "site": "00ae5728",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae5728"
      ],
      [
        "FALL_THROUGH",
        "00ae576c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae576c",
      "incomplete_value": true,
      "site": "00ae5790",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5728",
      "incomplete_value": true,
      "site": "00ae574c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae5764",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5790",
      "WRITE",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae57a4",
      "PARAM",
      [
        "storage",
        "00c0fc60",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ae5764",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5790",
      "WRITE",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae57a4",
      "PARAM",
      [
        "storage",
        "00c0fcb0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae574c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae570c.md#insn-00ae574c) · [`00ae5720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae570c.md#insn-00ae5720) · [`00ae5744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae570c.md#insn-00ae5744)
- 新版 [`00ae5790`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5750.md#insn-00ae5790) · [`00ae5764`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5750.md#insn-00ae5764) · [`00ae5788`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5750.md#insn-00ae5788)

~~~diff
- 00ae574c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:378:8"]]
- 00ae574c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5790 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b8:8"]]
+ 00ae5790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae574c bytes 80be01f9
+ 00ae5790 bytes 80de01f9
- 00ae5720 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:378:8"]]
- 00ae5720 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5764 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b8:8"]]
+ 00ae5764 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5720 bytes 81be41f9
+ 00ae5764 bytes 81de41f9
- 00ae5744 ["INT_ADD", "register:40f0:8", ["const:ae5744:8", "const:4:8"]]
- 00ae5744 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5788 ["INT_ADD", "register:40f0:8", ["const:ae5788:8", "const:4:8"]]
+ 00ae5788 ["CALL", null, ["callee:00bde090:8"]]
- 00ae5744 bytes 3fe20394
+ 00ae5788 bytes 42e20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-546a5af067485be28426708ae3525343"></a>

### [`00ae577c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae577c.md) → [`00ae57c0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae57c0.md) _ZN8firebase4util26cppthreaddispatchercontext11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae57dc",
      "incomplete_value": false,
      "site": "00ae57e0",
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
      "definition_site": "00ae5798",
      "incomplete_value": false,
      "site": "00ae579c",
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
      "definition_site": "00ae57ec",
      "incomplete_value": true,
      "site": "00ae57f8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae57a8",
      "incomplete_value": true,
      "site": "00ae57b4",
      "value": [
        "LOAD",
        "8",
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
      "00ae57dc",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae57ec",
      "DATA",
      [
        "storage",
        "010a0388",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae57dc",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae57ec",
      "DATA",
      [
        "storage",
        "010a03c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae579c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae577c.md#insn-00ae579c) · [`00ae5798`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae577c.md#insn-00ae5798) · [`00ae57a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae577c.md#insn-00ae57a4)
- 新版 [`00ae57e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae57c0.md#insn-00ae57e0) · [`00ae57dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae57c0.md#insn-00ae57dc) · [`00ae57e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae57c0.md#insn-00ae57e8)

~~~diff
- 00ae579c ["INT_ADD", "register:40f0:8", ["const:ae579c:8", "const:4:8"]]
- 00ae579c ["CALL", null, ["callee:00bde180:8"]]
+ 00ae57e0 ["INT_ADD", "register:40f0:8", ["const:ae57e0:8", "const:4:8"]]
+ 00ae57e0 ["CALL", null, ["callee:00bde180:8"]]
- 00ae579c bytes 65e20394
+ 00ae57e0 bytes 68e20394
- 00ae5798 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae5798 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae5798 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae5798 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae57dc ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae57dc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae57dc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae57dc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae5798 bytes 00501791
+ 00ae57dc bytes 001c1591
- 00ae57a4 ["COPY", "tmp:0:8", ["const:388:8"]]
- 00ae57a4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae57a4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae57a4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae57e8 ["COPY", "tmp:0:8", ["const:3c8:8"]]
+ 00ae57e8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae57e8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae57e8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae57a4 bytes 08210e91
+ 00ae57e8 bytes 08210f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61c34e86ac67c23ab29eb418e02c6479"></a>

### [`00ae57b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae57b8.md) → [`00ae57fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae57fc.md) _ZN8firebase4util26cppthreaddispatchercontext13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae583c",
      "incomplete_value": true,
      "site": "00ae583c",
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
            "const:3b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae57f8",
      "incomplete_value": true,
      "site": "00ae57f8",
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
            "const:378:8"
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
      "definition_site": "00ae5818",
      "incomplete_value": true,
      "site": "00ae5818",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae57d4",
      "incomplete_value": true,
      "site": "00ae57d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae57d4"
      ],
      [
        "FALL_THROUGH",
        "00ae5818"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae5818",
      "incomplete_value": true,
      "site": "00ae583c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae57d4",
      "incomplete_value": true,
      "site": "00ae57f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae5810",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae583c",
      "WRITE",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5854",
      "PARAM",
      [
        "storage",
        "010a03a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae5810",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae583c",
      "WRITE",
      [
        "storage",
        "010a03b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5854",
      "PARAM",
      [
        "storage",
        "010a03e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae57f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae57b8.md#insn-00ae57f8) · [`00ae57cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae57b8.md#insn-00ae57cc) · [`00ae57f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae57b8.md#insn-00ae57f0)
- 新版 [`00ae583c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae57fc.md#insn-00ae583c) · [`00ae5810`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae57fc.md#insn-00ae5810) · [`00ae5834`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae57fc.md#insn-00ae5834)

~~~diff
- 00ae57f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:378:8"]]
- 00ae57f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae583c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b8:8"]]
+ 00ae583c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae57f8 bytes 80be01f9
+ 00ae583c bytes 80de01f9
- 00ae57cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:378:8"]]
- 00ae57cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5810 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b8:8"]]
+ 00ae5810 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae57cc bytes 81be41f9
+ 00ae5810 bytes 81de41f9
- 00ae57f0 ["INT_ADD", "register:40f0:8", ["const:ae57f0:8", "const:4:8"]]
- 00ae57f0 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5834 ["INT_ADD", "register:40f0:8", ["const:ae5834:8", "const:4:8"]]
+ 00ae5834 ["CALL", null, ["callee:00bde090:8"]]
- 00ae57f0 bytes 14e20394
+ 00ae5834 bytes 17e20394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0796c8865c6044dfc66d8ea552692bbf"></a>

### [`00ae5828`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5828.md) → [`00ae586c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae586c.md) _ZN8firebase4util26cppthreaddispatchercontext10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae5888",
      "incomplete_value": false,
      "site": "00ae588c",
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
      "definition_site": "00ae5844",
      "incomplete_value": false,
      "site": "00ae5848",
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
      "definition_site": "00ae5898",
      "incomplete_value": true,
      "site": "00ae58a4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae5854",
      "incomplete_value": true,
      "site": "00ae5860",
      "value": [
        "LOAD",
        "8",
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
      "00ae5888",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae5898",
      "DATA",
      [
        "storage",
        "010a03a8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae5888",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae5898",
      "DATA",
      [
        "storage",
        "010a03e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5828.md#insn-00ae5848) · [`00ae5844`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5828.md#insn-00ae5844) · [`00ae5850`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5828.md#insn-00ae5850)
- 新版 [`00ae588c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae586c.md#insn-00ae588c) · [`00ae5888`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae586c.md#insn-00ae5888) · [`00ae5894`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae586c.md#insn-00ae5894)

~~~diff
- 00ae5848 ["INT_ADD", "register:40f0:8", ["const:ae5848:8", "const:4:8"]]
- 00ae5848 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae588c ["INT_ADD", "register:40f0:8", ["const:ae588c:8", "const:4:8"]]
+ 00ae588c ["CALL", null, ["callee:00bde180:8"]]
- 00ae5848 bytes 3ae20394
+ 00ae588c bytes 3de20394
- 00ae5844 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae5844 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae5844 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae5844 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae5888 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae5888 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5888 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5888 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae5844 bytes 00fc1991
+ 00ae5888 bytes 00c81791
- 00ae5850 ["COPY", "tmp:0:8", ["const:3a8:8"]]
- 00ae5850 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5850 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5850 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae5894 ["COPY", "tmp:0:8", ["const:3e8:8"]]
+ 00ae5894 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5894 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5894 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae5850 bytes 08a10e91
+ 00ae5894 bytes 08a10f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8b08d1716e10202e750e240c368fdda"></a>

### [`00ae5864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5864.md) → [`00ae58a8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae58a8.md) _ZN8firebase4util19cppthreaddispatcher19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocator

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
      "definition_site": "00ae58d4",
      "incomplete_value": true,
      "site": "00ae58d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5890",
      "incomplete_value": true,
      "site": "00ae5890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "definition_site": "00ae58bc",
      "incomplete_value": true,
      "site": "00ae58bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5878",
      "incomplete_value": true,
      "site": "00ae5878",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae5878"
      ],
      [
        "FALL_THROUGH",
        "00ae58bc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae58bc",
      "incomplete_value": true,
      "site": "00ae58d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5878",
      "incomplete_value": true,
      "site": "00ae5890",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae58b8",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae58d4",
      "WRITE",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae58b8",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae58d4",
      "WRITE",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5890`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5864.md#insn-00ae5890) · [`00ae5874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5864.md#insn-00ae5874) · [`00ae5888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5864.md#insn-00ae5888)
- 新版 [`00ae58d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae58a8.md#insn-00ae58d4) · [`00ae58b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae58a8.md#insn-00ae58b8) · [`00ae58cc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae58a8.md#insn-00ae58cc)

~~~diff
- 00ae5890 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
- 00ae5890 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae58d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00ae58d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5890 bytes 60da01f9
+ 00ae58d4 bytes 60fa01f9
- 00ae5874 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
- 00ae5874 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae58b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00ae58b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5874 bytes 68da41f9
+ 00ae58b8 bytes 68fa41f9
- 00ae5888 ["INT_ADD", "register:40f0:8", ["const:ae5888:8", "const:4:8"]]
- 00ae5888 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae58cc ["INT_ADD", "register:40f0:8", ["const:ae58cc:8", "const:4:8"]]
+ 00ae58cc ["CALL", null, ["callee:00bde090:8"]]
- 00ae5888 bytes eee10394
+ 00ae58cc bytes f1e10394
~~~


<a id="compare-95b9c5cd24d9e457b34c90d6ea271c4b"></a>

### [`00ae58a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58a4.md) → [`00ae58e8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae58e8.md) _ZN8firebase4util19cppthreaddispatcher19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocator

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
      "definition_site": "00ae5914",
      "incomplete_value": true,
      "site": "00ae5914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae58d0",
      "incomplete_value": true,
      "site": "00ae58d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "definition_site": "00ae58fc",
      "incomplete_value": true,
      "site": "00ae58fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae58b8",
      "incomplete_value": true,
      "site": "00ae58b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae58b8"
      ],
      [
        "FALL_THROUGH",
        "00ae58fc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae58fc",
      "incomplete_value": true,
      "site": "00ae5914",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae58b8",
      "incomplete_value": true,
      "site": "00ae58d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae58f8",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5914",
      "WRITE",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae58f8",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5914",
      "WRITE",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae58d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58a4.md#insn-00ae58d0) · [`00ae58b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58a4.md#insn-00ae58b4) · [`00ae58c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58a4.md#insn-00ae58c8)
- 新版 [`00ae5914`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae58e8.md#insn-00ae5914) · [`00ae58f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae58e8.md#insn-00ae58f8) · [`00ae590c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae58e8.md#insn-00ae590c)

~~~diff
- 00ae58d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
- 00ae58d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5914 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00ae5914 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae58d0 bytes 60da01f9
+ 00ae5914 bytes 60fa01f9
- 00ae58b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
- 00ae58b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae58f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00ae58f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae58b4 bytes 68da41f9
+ 00ae58f8 bytes 68fa41f9
- 00ae58c8 ["INT_ADD", "register:40f0:8", ["const:ae58c8:8", "const:4:8"]]
- 00ae58c8 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae590c ["INT_ADD", "register:40f0:8", ["const:ae590c:8", "const:4:8"]]
+ 00ae590c ["CALL", null, ["callee:00bde090:8"]]
- 00ae58c8 bytes dee10394
+ 00ae590c bytes e1e10394
~~~


<a id="compare-1d274d85d20d4547e842d2979af4a07a"></a>

### [`00ae58e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58e4.md) → [`00ae5928`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5928.md) _ZN8firebase4util19cppthreaddispatcher10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae5958",
      "incomplete_value": true,
      "site": "00ae5958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5914",
      "incomplete_value": true,
      "site": "00ae5914",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "definition_site": "00ae593c",
      "incomplete_value": true,
      "site": "00ae593c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae58f8",
      "incomplete_value": true,
      "site": "00ae58f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae58f8"
      ],
      [
        "FALL_THROUGH",
        "00ae593c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae593c",
      "incomplete_value": true,
      "site": "00ae5958",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae58f8",
      "incomplete_value": true,
      "site": "00ae5914",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae5938",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5958",
      "WRITE",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5938",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5958",
      "WRITE",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58e4.md#insn-00ae5914) · [`00ae58f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58e4.md#insn-00ae58f4) · [`00ae590c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae58e4.md#insn-00ae590c)
- 新版 [`00ae5958`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5928.md#insn-00ae5958) · [`00ae5938`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5928.md#insn-00ae5938) · [`00ae5950`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5928.md#insn-00ae5950)

~~~diff
- 00ae5914 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
- 00ae5914 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5958 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00ae5958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5914 bytes 60da01f9
+ 00ae5958 bytes 60fa01f9
- 00ae58f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
- 00ae58f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5938 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00ae5938 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae58f4 bytes 68da41f9
+ 00ae5938 bytes 68fa41f9
- 00ae590c ["INT_ADD", "register:40f0:8", ["const:ae590c:8", "const:4:8"]]
- 00ae590c ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5950 ["INT_ADD", "register:40f0:8", ["const:ae5950:8", "const:4:8"]]
+ 00ae5950 ["CALL", null, ["callee:00bde090:8"]]
- 00ae590c bytes cde10394
+ 00ae5950 bytes d0e10394
~~~


<a id="compare-81133109197d3f5dcd68637dc92fa778"></a>

### [`00ae5928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5928.md) → [`00ae596c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae596c.md) _ZN8firebase4util19cppthreaddispatcher10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae599c",
      "incomplete_value": true,
      "site": "00ae599c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5958",
      "incomplete_value": true,
      "site": "00ae5958",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3b0:8"
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
      "definition_site": "00ae5980",
      "incomplete_value": true,
      "site": "00ae5980",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae593c",
      "incomplete_value": true,
      "site": "00ae593c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae593c"
      ],
      [
        "FALL_THROUGH",
        "00ae5980"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae5980",
      "incomplete_value": true,
      "site": "00ae599c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae593c",
      "incomplete_value": true,
      "site": "00ae5958",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae597c",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae599c",
      "WRITE",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae597c",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae599c",
      "WRITE",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5958`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5928.md#insn-00ae5958) · [`00ae5938`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5928.md#insn-00ae5938) · [`00ae5950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5928.md#insn-00ae5950)
- 新版 [`00ae599c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae596c.md#insn-00ae599c) · [`00ae597c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae596c.md#insn-00ae597c) · [`00ae5994`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae596c.md#insn-00ae5994)

~~~diff
- 00ae5958 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
- 00ae5958 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae599c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00ae599c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5958 bytes 60da01f9
+ 00ae599c bytes 60fa01f9
- 00ae5938 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3b0:8"]]
- 00ae5938 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae597c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f0:8"]]
+ 00ae597c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5938 bytes 68da41f9
+ 00ae597c bytes 68fa41f9
- 00ae5950 ["INT_ADD", "register:40f0:8", ["const:ae5950:8", "const:4:8"]]
- 00ae5950 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5994 ["INT_ADD", "register:40f0:8", ["const:ae5994:8", "const:4:8"]]
+ 00ae5994 ["CALL", null, ["callee:00bde090:8"]]
- 00ae5950 bytes bce10394
+ 00ae5994 bytes bfe10394
~~~


<a id="compare-be353647ac12a19df30ad77ca9c265f6"></a>

### [`00ae5978`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5978.md) → [`00ae59bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae59bc.md) _ZN8firebase4util19cppthreaddispatcher15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae5a44",
      "incomplete_value": true,
      "site": "00ae5a44",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5a00",
      "incomplete_value": true,
      "site": "00ae5a00",
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
            "const:3b8:8"
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
      "definition_site": "00ae59f0",
      "incomplete_value": true,
      "site": "00ae59fc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae59ac",
      "incomplete_value": true,
      "site": "00ae59b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3b0:8"
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
      "00ae59d0",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae59f0",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5a44",
      "WRITE",
      [
        "storage",
        "010a03b8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae59d0",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae59f0",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5a44",
      "WRITE",
      [
        "storage",
        "010a03f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae59b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5978.md#insn-00ae59b8) · [`00ae5a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5978.md#insn-00ae5a00) · [`00ae598c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5978.md#insn-00ae598c)
- 新版 [`00ae59fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae59bc.md#insn-00ae59fc) · [`00ae5a44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae59bc.md#insn-00ae5a44) · [`00ae59d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae59bc.md#insn-00ae59d0)

~~~diff
- 00ae59b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae59b8 ["INT_ADD", "register:40f0:8", ["const:ae59b8:8", "const:4:8"]]
- 00ae59b8 ["CALLIND", null, ["register:0:8"]]
+ 00ae59fc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae59fc ["INT_ADD", "register:40f0:8", ["const:ae59fc:8", "const:4:8"]]
+ 00ae59fc ["CALLIND", null, ["register:0:8"]]
- 00ae59b8 bytes 00013fd6
+ 00ae59fc bytes 00013fd6
- 00ae5a00 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae5a00 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3b8:8"]]
- 00ae5a00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae5a44 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae5a44 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3f8:8"]]
+ 00ae5a44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae5a00 bytes a0e20e39
+ 00ae5a44 bytes a0e20f39
- 00ae598c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3b8:8"]]
- 00ae598c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae598c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae59d0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3f8:8"]]
+ 00ae59d0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae59d0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae598c bytes a8e24e39
+ 00ae59d0 bytes a8e24f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f13e4fc421360653d3ce15abd71f0bb3"></a>

### [`00ae5a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5a14.md) → [`00ae5a58`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5a58.md) _ZN8firebase4util19cppthreaddispatcher12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae5a94",
      "incomplete_value": true,
      "site": "00ae5a94",
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
            "const:3f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5a50",
      "incomplete_value": true,
      "site": "00ae5a50",
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
            "const:3b8:8"
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
      "definition_site": "00ae5ae4",
      "incomplete_value": true,
      "site": "00ae5ae4",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5aa0",
      "incomplete_value": true,
      "site": "00ae5aa0",
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
            "const:3b0:8"
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
      "definition_site": "00ae5a70",
      "incomplete_value": true,
      "site": "00ae5a70",
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
      "definition_site": "00ae5a2c",
      "incomplete_value": true,
      "site": "00ae5a2c",
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
      "00ae5a6c",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5a78",
      "READ",
      [
        "storage",
        "010a03b8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae5a94",
      "WRITE",
      [
        "storage",
        "010a03b8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae5a6c",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5a78",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae5a94",
      "WRITE",
      [
        "storage",
        "010a03f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5a50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5a14.md#insn-00ae5a50) · [`00ae5a9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5a14.md#insn-00ae5a9c) · [`00ae5aa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5a14.md#insn-00ae5aa0)
- 新版 [`00ae5a94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5a58.md#insn-00ae5a94) · [`00ae5ae0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5a58.md#insn-00ae5ae0) · [`00ae5ae4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5a58.md#insn-00ae5ae4)

~~~diff
- 00ae5a50 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae5a50 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae5a50 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3b8:8"]]
- 00ae5a50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae5a94 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae5a94 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae5a94 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3f8:8"]]
+ 00ae5a94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae5a50 bytes bfe20e39
+ 00ae5a94 bytes bfe20f39
- 00ae5a9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae5a9c ["INT_ADD", "register:40f0:8", ["const:ae5a9c:8", "const:4:8"]]
- 00ae5a9c ["CALLIND", null, ["register:0:8"]]
+ 00ae5ae0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae5ae0 ["INT_ADD", "register:40f0:8", ["const:ae5ae0:8", "const:4:8"]]
+ 00ae5ae0 ["CALLIND", null, ["register:0:8"]]
- 00ae5a9c bytes 00013fd6
+ 00ae5ae0 bytes 00013fd6
- 00ae5aa0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b0:8"]]
- 00ae5aa0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae5aa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae5ae4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f0:8"]]
+ 00ae5ae4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae5ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae5aa0 bytes 9fda01f9
+ 00ae5ae4 bytes 9ffa01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6f8d2ca635578995ec003e4ab44b810"></a>

### [`00ae5ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ab4.md) → [`00ae5af8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5af8.md) _ZN8firebase4util19cppthreaddispatcher14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae5b38",
      "incomplete_value": true,
      "site": "00ae5b38",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5af4",
      "incomplete_value": true,
      "site": "00ae5af4",
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
            "const:3b0:8"
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
      "definition_site": "00ae5b14",
      "incomplete_value": true,
      "site": "00ae5b14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5ad0",
      "incomplete_value": true,
      "site": "00ae5ad0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae5ad0"
      ],
      [
        "FALL_THROUGH",
        "00ae5b14"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae5b14",
      "incomplete_value": true,
      "site": "00ae5b38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5ad0",
      "incomplete_value": true,
      "site": "00ae5af4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae5b0c",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5b38",
      "WRITE",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5b4c",
      "PARAM",
      [
        "storage",
        "00c0fcc0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ae5b0c",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5b38",
      "WRITE",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5b4c",
      "PARAM",
      [
        "storage",
        "00c0fd10",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5af4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ab4.md#insn-00ae5af4) · [`00ae5ac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ab4.md#insn-00ae5ac8) · [`00ae5aec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ab4.md#insn-00ae5aec)
- 新版 [`00ae5b38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5af8.md#insn-00ae5b38) · [`00ae5b0c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5af8.md#insn-00ae5b0c) · [`00ae5b30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5af8.md#insn-00ae5b30)

~~~diff
- 00ae5af4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b0:8"]]
- 00ae5af4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5b38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f0:8"]]
+ 00ae5b38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5af4 bytes 80da01f9
+ 00ae5b38 bytes 80fa01f9
- 00ae5ac8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b0:8"]]
- 00ae5ac8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5b0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f0:8"]]
+ 00ae5b0c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5ac8 bytes 81da41f9
+ 00ae5b0c bytes 81fa41f9
- 00ae5aec ["INT_ADD", "register:40f0:8", ["const:ae5aec:8", "const:4:8"]]
- 00ae5aec ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5b30 ["INT_ADD", "register:40f0:8", ["const:ae5b30:8", "const:4:8"]]
+ 00ae5b30 ["CALL", null, ["callee:00bde090:8"]]
- 00ae5aec bytes 55e10394
+ 00ae5b30 bytes 58e10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-797ea6b3232a0fc1ff0fcaf27f69cbb7"></a>

### [`00ae5b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b24.md) → [`00ae5b68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5b68.md) _ZN8firebase4util19cppthreaddispatcher11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae5b84",
      "incomplete_value": false,
      "site": "00ae5b88",
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
      "definition_site": "00ae5b40",
      "incomplete_value": false,
      "site": "00ae5b44",
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
      "definition_site": "00ae5b94",
      "incomplete_value": true,
      "site": "00ae5ba0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae5b50",
      "incomplete_value": true,
      "site": "00ae5b5c",
      "value": [
        "LOAD",
        "8",
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
      "00ae5b84",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae5b94",
      "DATA",
      [
        "storage",
        "010a03c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5b84",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae5b94",
      "DATA",
      [
        "storage",
        "010a0400",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5b44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b24.md#insn-00ae5b44) · [`00ae5b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b24.md#insn-00ae5b40) · [`00ae5b4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b24.md#insn-00ae5b4c)
- 新版 [`00ae5b88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5b68.md#insn-00ae5b88) · [`00ae5b84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5b68.md#insn-00ae5b84) · [`00ae5b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5b68.md#insn-00ae5b90)

~~~diff
- 00ae5b44 ["INT_ADD", "register:40f0:8", ["const:ae5b44:8", "const:4:8"]]
- 00ae5b44 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae5b88 ["INT_ADD", "register:40f0:8", ["const:ae5b88:8", "const:4:8"]]
+ 00ae5b88 ["CALL", null, ["callee:00bde180:8"]]
- 00ae5b44 bytes 7be10394
+ 00ae5b88 bytes 7ee10394
- 00ae5b40 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae5b40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae5b40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae5b40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae5b84 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae5b84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5b84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5b84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae5b40 bytes 00501791
+ 00ae5b84 bytes 001c1591
- 00ae5b4c ["COPY", "tmp:0:8", ["const:3c0:8"]]
- 00ae5b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae5b90 ["COPY", "tmp:0:8", ["const:400:8"]]
+ 00ae5b90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5b90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5b90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae5b4c bytes 08010f91
+ 00ae5b90 bytes 08011091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-40b923765b025f444c9610309acc9f41"></a>

### [`00ae5b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b60.md) → [`00ae5ba4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ba4.md) _ZN8firebase4util19cppthreaddispatcher13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae5be4",
      "incomplete_value": true,
      "site": "00ae5be4",
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
            "const:3f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5ba0",
      "incomplete_value": true,
      "site": "00ae5ba0",
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
            "const:3b0:8"
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
      "definition_site": "00ae5bc0",
      "incomplete_value": true,
      "site": "00ae5bc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5b7c",
      "incomplete_value": true,
      "site": "00ae5b7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae5b7c"
      ],
      [
        "FALL_THROUGH",
        "00ae5bc0"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae5bc0",
      "incomplete_value": true,
      "site": "00ae5be4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5b7c",
      "incomplete_value": true,
      "site": "00ae5ba0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae5bb8",
      "READ",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5be4",
      "WRITE",
      [
        "storage",
        "010a03b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5bfc",
      "PARAM",
      [
        "storage",
        "010a03d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae5bb8",
      "READ",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5be4",
      "WRITE",
      [
        "storage",
        "010a03f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5bfc",
      "PARAM",
      [
        "storage",
        "010a0410",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b60.md#insn-00ae5ba0) · [`00ae5b74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b60.md#insn-00ae5b74) · [`00ae5b98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5b60.md#insn-00ae5b98)
- 新版 [`00ae5be4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ba4.md#insn-00ae5be4) · [`00ae5bb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ba4.md#insn-00ae5bb8) · [`00ae5bdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ba4.md#insn-00ae5bdc)

~~~diff
- 00ae5ba0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b0:8"]]
- 00ae5ba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5be4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f0:8"]]
+ 00ae5be4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5ba0 bytes 80da01f9
+ 00ae5be4 bytes 80fa01f9
- 00ae5b74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3b0:8"]]
- 00ae5b74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5bb8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3f0:8"]]
+ 00ae5bb8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5b74 bytes 81da41f9
+ 00ae5bb8 bytes 81fa41f9
- 00ae5b98 ["INT_ADD", "register:40f0:8", ["const:ae5b98:8", "const:4:8"]]
- 00ae5b98 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5bdc ["INT_ADD", "register:40f0:8", ["const:ae5bdc:8", "const:4:8"]]
+ 00ae5bdc ["CALL", null, ["callee:00bde090:8"]]
- 00ae5b98 bytes 2ae10394
+ 00ae5bdc bytes 2de10394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f01bb5c77429d45c17951514235ee852"></a>

### [`00ae5bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5bd0.md) → [`00ae5c14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c14.md) _ZN8firebase4util19cppthreaddispatcher10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae5c30",
      "incomplete_value": false,
      "site": "00ae5c34",
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
      "definition_site": "00ae5bec",
      "incomplete_value": false,
      "site": "00ae5bf0",
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
      "00ae5c30",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae5c40",
      "DATA",
      [
        "storage",
        "010a03d0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae5c30",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae5c40",
      "DATA",
      [
        "storage",
        "010a0410",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5bd0.md#insn-00ae5bf0) · [`00ae5bec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5bd0.md#insn-00ae5bec) · [`00ae5bf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5bd0.md#insn-00ae5bf8)
- 新版 [`00ae5c34`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c14.md#insn-00ae5c34) · [`00ae5c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c14.md#insn-00ae5c30) · [`00ae5c3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c14.md#insn-00ae5c3c)

~~~diff
- 00ae5bf0 ["INT_ADD", "register:40f0:8", ["const:ae5bf0:8", "const:4:8"]]
- 00ae5bf0 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae5c34 ["INT_ADD", "register:40f0:8", ["const:ae5c34:8", "const:4:8"]]
+ 00ae5c34 ["CALL", null, ["callee:00bde180:8"]]
- 00ae5bf0 bytes 50e10394
+ 00ae5c34 bytes 53e10394
- 00ae5bec ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae5bec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae5bec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae5bec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae5c30 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae5c30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5c30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5c30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae5bec bytes 00fc1991
+ 00ae5c30 bytes 00c81791
- 00ae5bf8 ["COPY", "tmp:0:8", ["const:3d0:8"]]
- 00ae5bf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5bf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5bf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae5c3c ["COPY", "tmp:0:8", ["const:410:8"]]
+ 00ae5c3c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5c3c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5c3c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae5bf8 bytes 08410f91
+ 00ae5c3c bytes 08411091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08ba605db9b49a10bb03425a96e656f2"></a>

### [`00ae5c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c0c.md) → [`00ae5c50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c50.md) _ZN8firebase4util3log19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
      "definition_site": "00ae5c7c",
      "incomplete_value": true,
      "site": "00ae5c7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5c38",
      "incomplete_value": true,
      "site": "00ae5c38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "definition_site": "00ae5c64",
      "incomplete_value": true,
      "site": "00ae5c64",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5c20",
      "incomplete_value": true,
      "site": "00ae5c20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae5c20"
      ],
      [
        "FALL_THROUGH",
        "00ae5c64"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae5c64",
      "incomplete_value": true,
      "site": "00ae5c7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5c20",
      "incomplete_value": true,
      "site": "00ae5c38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae5c60",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5c7c",
      "WRITE",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5c60",
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5c7c",
      "WRITE",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5c38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c0c.md#insn-00ae5c38) · [`00ae5c1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c0c.md#insn-00ae5c1c) · [`00ae5c30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c0c.md#insn-00ae5c30)
- 新版 [`00ae5c7c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c50.md#insn-00ae5c7c) · [`00ae5c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c50.md#insn-00ae5c60) · [`00ae5c74`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c50.md#insn-00ae5c74)

~~~diff
- 00ae5c38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
- 00ae5c38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5c7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00ae5c7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5c38 bytes 60ee01f9
+ 00ae5c7c bytes 600e02f9
- 00ae5c1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
- 00ae5c1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5c60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00ae5c60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5c1c bytes 68ee41f9
+ 00ae5c60 bytes 680e42f9
- 00ae5c30 ["INT_ADD", "register:40f0:8", ["const:ae5c30:8", "const:4:8"]]
- 00ae5c30 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5c74 ["INT_ADD", "register:40f0:8", ["const:ae5c74:8", "const:4:8"]]
+ 00ae5c74 ["CALL", null, ["callee:00bde090:8"]]
- 00ae5c30 bytes 04e10394
+ 00ae5c74 bytes 07e10394
~~~


<a id="compare-22bbfec165fb9bd0c0b66fe2231124b2"></a>

### [`00ae5c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c4c.md) → [`00ae5c90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c90.md) _ZN8firebase4util3log19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00ae5cbc",
      "incomplete_value": true,
      "site": "00ae5cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5c78",
      "incomplete_value": true,
      "site": "00ae5c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "definition_site": "00ae5ca4",
      "incomplete_value": true,
      "site": "00ae5ca4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5c60",
      "incomplete_value": true,
      "site": "00ae5c60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae5c60"
      ],
      [
        "FALL_THROUGH",
        "00ae5ca4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae5ca4",
      "incomplete_value": true,
      "site": "00ae5cbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5c60",
      "incomplete_value": true,
      "site": "00ae5c78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae5ca0",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5cbc",
      "WRITE",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5ca0",
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5cbc",
      "WRITE",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5c78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c4c.md#insn-00ae5c78) · [`00ae5c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c4c.md#insn-00ae5c5c) · [`00ae5c70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c4c.md#insn-00ae5c70)
- 新版 [`00ae5cbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c90.md#insn-00ae5cbc) · [`00ae5ca0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c90.md#insn-00ae5ca0) · [`00ae5cb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5c90.md#insn-00ae5cb4)

~~~diff
- 00ae5c78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
- 00ae5c78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5cbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00ae5cbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5c78 bytes 60ee01f9
+ 00ae5cbc bytes 600e02f9
- 00ae5c5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
- 00ae5c5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5ca0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00ae5ca0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5c5c bytes 68ee41f9
+ 00ae5ca0 bytes 680e42f9
- 00ae5c70 ["INT_ADD", "register:40f0:8", ["const:ae5c70:8", "const:4:8"]]
- 00ae5c70 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5cb4 ["INT_ADD", "register:40f0:8", ["const:ae5cb4:8", "const:4:8"]]
+ 00ae5cb4 ["CALL", null, ["callee:00bde090:8"]]
- 00ae5c70 bytes f4e00394
+ 00ae5cb4 bytes f7e00394
~~~


<a id="compare-633cd31997308065aa9ae774f7732e6b"></a>

### [`00ae5c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c8c.md) → [`00ae5cd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5cd0.md) _ZN8firebase4util3log10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00ae5d00",
      "incomplete_value": true,
      "site": "00ae5d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5cbc",
      "incomplete_value": true,
      "site": "00ae5cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "definition_site": "00ae5ce4",
      "incomplete_value": true,
      "site": "00ae5ce4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5ca0",
      "incomplete_value": true,
      "site": "00ae5ca0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae5ca0"
      ],
      [
        "FALL_THROUGH",
        "00ae5ce4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae5ce4",
      "incomplete_value": true,
      "site": "00ae5d00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5ca0",
      "incomplete_value": true,
      "site": "00ae5cbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae5ce0",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5d00",
      "WRITE",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5ce0",
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5d00",
      "WRITE",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5cbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c8c.md#insn-00ae5cbc) · [`00ae5c9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c8c.md#insn-00ae5c9c) · [`00ae5cb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5c8c.md#insn-00ae5cb4)
- 新版 [`00ae5d00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5cd0.md#insn-00ae5d00) · [`00ae5ce0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5cd0.md#insn-00ae5ce0) · [`00ae5cf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5cd0.md#insn-00ae5cf8)

~~~diff
- 00ae5cbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
- 00ae5cbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5d00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00ae5d00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5cbc bytes 60ee01f9
+ 00ae5d00 bytes 600e02f9
- 00ae5c9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
- 00ae5c9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5ce0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00ae5ce0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5c9c bytes 68ee41f9
+ 00ae5ce0 bytes 680e42f9
- 00ae5cb4 ["INT_ADD", "register:40f0:8", ["const:ae5cb4:8", "const:4:8"]]
- 00ae5cb4 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5cf8 ["INT_ADD", "register:40f0:8", ["const:ae5cf8:8", "const:4:8"]]
+ 00ae5cf8 ["CALL", null, ["callee:00bde090:8"]]
- 00ae5cb4 bytes e3e00394
+ 00ae5cf8 bytes e6e00394
~~~


<a id="compare-2a186247c062ef328253bc7bd8d0bbec"></a>

### [`00ae5cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5cd0.md) → [`00ae5d14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5d14.md) _ZN8firebase4util3log10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae5d44",
      "incomplete_value": true,
      "site": "00ae5d44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5d00",
      "incomplete_value": true,
      "site": "00ae5d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:3d8:8"
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
      "definition_site": "00ae5d28",
      "incomplete_value": true,
      "site": "00ae5d28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5ce4",
      "incomplete_value": true,
      "site": "00ae5ce4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae5ce4"
      ],
      [
        "FALL_THROUGH",
        "00ae5d28"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae5d28",
      "incomplete_value": true,
      "site": "00ae5d44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5ce4",
      "incomplete_value": true,
      "site": "00ae5d00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae5d24",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5d44",
      "WRITE",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5d24",
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5d44",
      "WRITE",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5d00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5cd0.md#insn-00ae5d00) · [`00ae5ce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5cd0.md#insn-00ae5ce0) · [`00ae5cf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5cd0.md#insn-00ae5cf8)
- 新版 [`00ae5d44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5d14.md#insn-00ae5d44) · [`00ae5d24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5d14.md#insn-00ae5d24) · [`00ae5d3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5d14.md#insn-00ae5d3c)

~~~diff
- 00ae5d00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
- 00ae5d00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5d44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00ae5d44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5d00 bytes 60ee01f9
+ 00ae5d44 bytes 600e02f9
- 00ae5ce0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3d8:8"]]
- 00ae5ce0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5d24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:418:8"]]
+ 00ae5d24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5ce0 bytes 68ee41f9
+ 00ae5d24 bytes 680e42f9
- 00ae5cf8 ["INT_ADD", "register:40f0:8", ["const:ae5cf8:8", "const:4:8"]]
- 00ae5cf8 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5d3c ["INT_ADD", "register:40f0:8", ["const:ae5d3c:8", "const:4:8"]]
+ 00ae5d3c ["CALL", null, ["callee:00bde090:8"]]
- 00ae5cf8 bytes d2e00394
+ 00ae5d3c bytes d5e00394
~~~


<a id="compare-0f38b514125d49fa61a82654503b8307"></a>

### [`00ae5d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5d20.md) → [`00ae5d64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5d64.md) _ZN8firebase4util3log15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00ae5dec",
      "incomplete_value": true,
      "site": "00ae5dec",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5da8",
      "incomplete_value": true,
      "site": "00ae5da8",
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
            "const:3e0:8"
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
      "definition_site": "00ae5d98",
      "incomplete_value": true,
      "site": "00ae5da4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:418:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5d54",
      "incomplete_value": true,
      "site": "00ae5d60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3d8:8"
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
      "00ae5d78",
      "READ",
      [
        "storage",
        "010a03e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae5d98",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5dec",
      "WRITE",
      [
        "storage",
        "010a03e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae5d78",
      "READ",
      [
        "storage",
        "010a0420",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae5d98",
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5dec",
      "WRITE",
      [
        "storage",
        "010a0420",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5d20.md#insn-00ae5d60) · [`00ae5da8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5d20.md#insn-00ae5da8) · [`00ae5d34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5d20.md#insn-00ae5d34)
- 新版 [`00ae5da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5d64.md#insn-00ae5da4) · [`00ae5dec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5d64.md#insn-00ae5dec) · [`00ae5d78`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5d64.md#insn-00ae5d78)

~~~diff
- 00ae5d60 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae5d60 ["INT_ADD", "register:40f0:8", ["const:ae5d60:8", "const:4:8"]]
- 00ae5d60 ["CALLIND", null, ["register:0:8"]]
+ 00ae5da4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae5da4 ["INT_ADD", "register:40f0:8", ["const:ae5da4:8", "const:4:8"]]
+ 00ae5da4 ["CALLIND", null, ["register:0:8"]]
- 00ae5d60 bytes 00013fd6
+ 00ae5da4 bytes 00013fd6
- 00ae5da8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00ae5da8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3e0:8"]]
- 00ae5da8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00ae5dec ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00ae5dec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:420:8"]]
+ 00ae5dec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00ae5da8 bytes a0820f39
+ 00ae5dec bytes a0821039
- 00ae5d34 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3e0:8"]]
- 00ae5d34 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00ae5d34 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00ae5d78 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:420:8"]]
+ 00ae5d78 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5d78 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00ae5d34 bytes a8824f39
+ 00ae5d78 bytes a8825039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1cb96fcdcb1e027857aeff328eb7fd81"></a>

### [`00ae5dbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5dbc.md) → [`00ae5e00`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5e00.md) _ZN8firebase4util3log12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00ae5e3c",
      "incomplete_value": true,
      "site": "00ae5e3c",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5df8",
      "incomplete_value": true,
      "site": "00ae5df8",
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
            "const:3e0:8"
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
      "definition_site": "00ae5e8c",
      "incomplete_value": true,
      "site": "00ae5e8c",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5e48",
      "incomplete_value": true,
      "site": "00ae5e48",
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
            "const:3d8:8"
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
      "definition_site": "00ae5e18",
      "incomplete_value": true,
      "site": "00ae5e18",
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
      "definition_site": "00ae5dd4",
      "incomplete_value": true,
      "site": "00ae5dd4",
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
      "00ae5e14",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5e20",
      "READ",
      [
        "storage",
        "010a03e0",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae5e3c",
      "WRITE",
      [
        "storage",
        "010a03e0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00ae5e14",
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5e20",
      "READ",
      [
        "storage",
        "010a0420",
        null,
        "undefined1"
      ]
    ],
    [
      "00ae5e3c",
      "WRITE",
      [
        "storage",
        "010a0420",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5df8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5dbc.md#insn-00ae5df8) · [`00ae5e44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5dbc.md#insn-00ae5e44) · [`00ae5e48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5dbc.md#insn-00ae5e48)
- 新版 [`00ae5e3c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5e00.md#insn-00ae5e3c) · [`00ae5e88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5e00.md#insn-00ae5e88) · [`00ae5e8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5e00.md#insn-00ae5e8c)

~~~diff
- 00ae5df8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00ae5df8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00ae5df8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3e0:8"]]
- 00ae5df8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00ae5e3c ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00ae5e3c ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00ae5e3c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:420:8"]]
+ 00ae5e3c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00ae5df8 bytes bf820f39
+ 00ae5e3c bytes bf821039
- 00ae5e44 ["COPY", "register:0:8", ["register:4040:8"]]
- 00ae5e44 ["INT_ADD", "register:40f0:8", ["const:ae5e44:8", "const:4:8"]]
- 00ae5e44 ["CALLIND", null, ["register:0:8"]]
+ 00ae5e88 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00ae5e88 ["INT_ADD", "register:40f0:8", ["const:ae5e88:8", "const:4:8"]]
+ 00ae5e88 ["CALLIND", null, ["register:0:8"]]
- 00ae5e44 bytes 00013fd6
+ 00ae5e88 bytes 00013fd6
- 00ae5e48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d8:8"]]
- 00ae5e48 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00ae5e48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00ae5e8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
+ 00ae5e8c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00ae5e8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00ae5e48 bytes 9fee01f9
+ 00ae5e8c bytes 9f0e02f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4daf9d5fa3358f8957b7244918361614"></a>

### [`00ae5e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5e5c.md) → [`00ae5ea0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ea0.md) _ZN8firebase4util3log14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae5ee0",
      "incomplete_value": true,
      "site": "00ae5ee0",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5e9c",
      "incomplete_value": true,
      "site": "00ae5e9c",
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
            "const:3d8:8"
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
      "definition_site": "00ae5ebc",
      "incomplete_value": true,
      "site": "00ae5ebc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5e78",
      "incomplete_value": true,
      "site": "00ae5e78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae5e78"
      ],
      [
        "FALL_THROUGH",
        "00ae5ebc"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae5ebc",
      "incomplete_value": true,
      "site": "00ae5ee0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5e78",
      "incomplete_value": true,
      "site": "00ae5e9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae5eb4",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5ee0",
      "WRITE",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5ef4",
      "PARAM",
      [
        "storage",
        "00c0fcf0",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00ae5eb4",
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5ee0",
      "WRITE",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5ef4",
      "PARAM",
      [
        "storage",
        "00c0fd40",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5e9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5e5c.md#insn-00ae5e9c) · [`00ae5e70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5e5c.md#insn-00ae5e70) · [`00ae5e94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5e5c.md#insn-00ae5e94)
- 新版 [`00ae5ee0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ea0.md#insn-00ae5ee0) · [`00ae5eb4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ea0.md#insn-00ae5eb4) · [`00ae5ed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ea0.md#insn-00ae5ed8)

~~~diff
- 00ae5e9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d8:8"]]
- 00ae5e9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5ee0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
+ 00ae5ee0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5e9c bytes 80ee01f9
+ 00ae5ee0 bytes 800e02f9
- 00ae5e70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d8:8"]]
- 00ae5e70 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5eb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
+ 00ae5eb4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5e70 bytes 81ee41f9
+ 00ae5eb4 bytes 810e42f9
- 00ae5e94 ["INT_ADD", "register:40f0:8", ["const:ae5e94:8", "const:4:8"]]
- 00ae5e94 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5ed8 ["INT_ADD", "register:40f0:8", ["const:ae5ed8:8", "const:4:8"]]
+ 00ae5ed8 ["CALL", null, ["callee:00bde090:8"]]
- 00ae5e94 bytes 6be00394
+ 00ae5ed8 bytes 6ee00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d58a2b1f6cb0168ce6fb036f4e944b81"></a>

### [`00ae5ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ecc.md) → [`00ae5f10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f10.md) _ZN8firebase4util3log11GetMethodIdENS1_6MethodE

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
      "definition_site": "00ae5f3c",
      "incomplete_value": true,
      "site": "00ae5f48",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae5ef8",
      "incomplete_value": true,
      "site": "00ae5f04",
      "value": [
        "LOAD",
        "8",
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
      "00ae5f2c",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00ae5f3c",
      "DATA",
      [
        "storage",
        "010a03e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00ae5f2c",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00ae5f3c",
      "DATA",
      [
        "storage",
        "010a0428",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5ee8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ecc.md#insn-00ae5ee8) · [`00ae5eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ecc.md#insn-00ae5eec) · [`00ae5ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5ecc.md#insn-00ae5ef4)
- 新版 [`00ae5f2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f10.md#insn-00ae5f2c) · [`00ae5f30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f10.md#insn-00ae5f30) · [`00ae5f38`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f10.md#insn-00ae5f38)

~~~diff
- 00ae5ee8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00ae5ee8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae5ee8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae5ee8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae5f2c ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00ae5f2c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5f2c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5f2c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae5ee8 bytes 00501791
+ 00ae5f2c bytes 001c1591
- 00ae5eec ["INT_ADD", "register:40f0:8", ["const:ae5eec:8", "const:4:8"]]
- 00ae5eec ["CALL", null, ["callee:00bde180:8"]]
+ 00ae5f30 ["INT_ADD", "register:40f0:8", ["const:ae5f30:8", "const:4:8"]]
+ 00ae5f30 ["CALL", null, ["callee:00bde180:8"]]
- 00ae5eec bytes 91e00394
+ 00ae5f30 bytes 94e00394
- 00ae5ef4 ["COPY", "tmp:0:8", ["const:3e8:8"]]
- 00ae5ef4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5ef4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5ef4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae5f38 ["COPY", "tmp:0:8", ["const:428:8"]]
+ 00ae5f38 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5f38 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5f38 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae5ef4 bytes 08a10f91
+ 00ae5f38 bytes 08a11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fe063aedf62625863b28b6a842a13d7"></a>

### [`00ae5f08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5f08.md) → [`00ae5f4c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f4c.md) _ZN8firebase4util3log13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00ae5f8c",
      "incomplete_value": true,
      "site": "00ae5f8c",
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
            "const:418:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5f48",
      "incomplete_value": true,
      "site": "00ae5f48",
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
            "const:3d8:8"
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
      "definition_site": "00ae5f68",
      "incomplete_value": true,
      "site": "00ae5f68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5f24",
      "incomplete_value": true,
      "site": "00ae5f24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00ae5f24"
      ],
      [
        "FALL_THROUGH",
        "00ae5f68"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00ae5f68",
      "incomplete_value": true,
      "site": "00ae5f8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5f24",
      "incomplete_value": true,
      "site": "00ae5f48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00ae5f60",
      "READ",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5f8c",
      "WRITE",
      [
        "storage",
        "010a03d8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5fa4",
      "PARAM",
      [
        "storage",
        "010a03f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae5f60",
      "READ",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5f8c",
      "WRITE",
      [
        "storage",
        "010a0418",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae5fa4",
      "PARAM",
      [
        "storage",
        "010a0430",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5f48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5f08.md#insn-00ae5f48) · [`00ae5f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5f08.md#insn-00ae5f1c) · [`00ae5f40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5f08.md#insn-00ae5f40)
- 新版 [`00ae5f8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f4c.md#insn-00ae5f8c) · [`00ae5f60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f4c.md#insn-00ae5f60) · [`00ae5f84`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5f4c.md#insn-00ae5f84)

~~~diff
- 00ae5f48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d8:8"]]
- 00ae5f48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae5f8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
+ 00ae5f8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5f48 bytes 80ee01f9
+ 00ae5f8c bytes 800e02f9
- 00ae5f1c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3d8:8"]]
- 00ae5f1c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae5f60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:418:8"]]
+ 00ae5f60 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5f1c bytes 81ee41f9
+ 00ae5f60 bytes 810e42f9
- 00ae5f40 ["INT_ADD", "register:40f0:8", ["const:ae5f40:8", "const:4:8"]]
- 00ae5f40 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae5f84 ["INT_ADD", "register:40f0:8", ["const:ae5f84:8", "const:4:8"]]
+ 00ae5f84 ["CALL", null, ["callee:00bde090:8"]]
- 00ae5f40 bytes 40e00394
+ 00ae5f84 bytes 43e00394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac50bc191cf3ee74c731726dd67f03a6"></a>

### [`00ae5f78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5f78.md) → [`00ae5fbc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5fbc.md) _ZN8firebase4util3log10GetFieldIdENS1_5FieldE

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
      "definition_site": "00ae5fd8",
      "incomplete_value": false,
      "site": "00ae5fdc",
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
      "definition_site": "00ae5f94",
      "incomplete_value": false,
      "site": "00ae5f98",
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
      "definition_site": "00ae5fe8",
      "incomplete_value": true,
      "site": "00ae5ff4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00ae5fa4",
      "incomplete_value": true,
      "site": "00ae5fb0",
      "value": [
        "LOAD",
        "8",
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
      "00ae5fd8",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00ae5fe8",
      "DATA",
      [
        "storage",
        "010a03f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00ae5fd8",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00ae5fe8",
      "DATA",
      [
        "storage",
        "010a0430",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00ae5f98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5f78.md#insn-00ae5f98) · [`00ae5f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5f78.md#insn-00ae5f94) · [`00ae5fa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5f78.md#insn-00ae5fa0)
- 新版 [`00ae5fdc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5fbc.md#insn-00ae5fdc) · [`00ae5fd8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5fbc.md#insn-00ae5fd8) · [`00ae5fe4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5fbc.md#insn-00ae5fe4)

~~~diff
- 00ae5f98 ["INT_ADD", "register:40f0:8", ["const:ae5f98:8", "const:4:8"]]
- 00ae5f98 ["CALL", null, ["callee:00bde180:8"]]
+ 00ae5fdc ["INT_ADD", "register:40f0:8", ["const:ae5fdc:8", "const:4:8"]]
+ 00ae5fdc ["CALL", null, ["callee:00bde180:8"]]
- 00ae5f98 bytes 66e00394
+ 00ae5fdc bytes 69e00394
- 00ae5f94 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00ae5f94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00ae5f94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00ae5f94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00ae5fd8 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00ae5fd8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5fd8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00ae5fd8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00ae5f94 bytes 00fc1991
+ 00ae5fd8 bytes 00c81791
- 00ae5fa0 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 00ae5fa0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5fa0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00ae5fa0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00ae5fe4 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 00ae5fe4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5fe4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00ae5fe4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00ae5fa0 bytes 08c10f91
+ 00ae5fe4 bytes 08c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e88287884ce6365d7e82f477d25352e9"></a>

### [`00ae5fb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5fb4.md) → [`00ae5ff8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ff8.md) _ZN8firebase4util10uribuilder19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00ae6024",
      "incomplete_value": true,
      "site": "00ae6024",
      "value": [
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
      "definition_site": "00ae5fe0",
      "incomplete_value": true,
      "site": "00ae5fe0",
      "value": [
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
      "definition_site": "00ae600c",
      "incomplete_value": true,
      "site": "00ae600c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00ae5fc8",
      "incomplete_value": true,
      "site": "00ae5fc8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00ae6018",
      "incomplete_value": false,
      "site": "00ae601c",
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
      "definition_site": "00ae5fd4",
      "incomplete_value": false,
      "site": "00ae5fd8",
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
      "00ae6008",
      "READ",
      [
        "storage",
        "010a03f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6018",
      "PARAM",
      [
        "storage",
        "0029ee1f",
        null,
        "string"
      ]
    ],
    [
      "00ae6024",
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
      "00ae6008",
      "READ",
      [
        "storage",
        "010a0438",
        null,
        "undefined8"
      ]
    ],
    [
      "00ae6018",
      "PARAM",
      [
        "storage",
        "0029eeaa",
        null,
        "string"
      ]
    ],
    [
      "00ae6024",
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

- 旧版 [`00ae5fd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5fb4.md#insn-00ae5fd8) · [`00ae5fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5fb4.md#insn-00ae5fe0) · [`00ae5fc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae5/00ae5fb4.md#insn-00ae5fc4)
- 新版 [`00ae601c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ff8.md#insn-00ae601c) · [`00ae6024`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ff8.md#insn-00ae6024) · [`00ae6008`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae5/00ae5ff8.md#insn-00ae6008)

~~~diff
- 00ae5fd8 ["INT_ADD", "register:40f0:8", ["const:ae5fd8:8", "const:4:8"]]
- 00ae5fd8 ["CALL", null, ["callee:00bde090:8"]]
+ 00ae601c ["INT_ADD", "register:40f0:8", ["const:ae601c:8", "const:4:8"]]
+ 00ae601c ["CALL", null, ["callee:00bde090:8"]]
- 00ae5fd8 bytes 1ae00394
+ 00ae601c bytes 1de00394
- 00ae5fe0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f8:8"]]
- 00ae5fe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00ae6024 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00ae6024 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00ae5fe0 bytes 60fe01f9
+ 00ae6024 bytes 601e02f9
- 00ae5fc4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3f8:8"]]
- 00ae5fc4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00ae6008 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:438:8"]]
+ 00ae6008 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00ae5fc4 bytes 68fe41f9
+ 00ae6008 bytes 681e42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

