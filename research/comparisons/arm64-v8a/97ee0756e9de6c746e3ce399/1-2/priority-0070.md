# v15.7.3 → v15.7.4 · 最優先の変更候補 (70)

[一覧の目次](README.md)

<a id="compare-9f94b7d3aadf8e76c6f652cff3388947"></a>

### [`00b5c9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c9a0.md) → [`00b5c9e4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5c9e4.md) _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4util

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
      "definition_site": "00b5ca10",
      "incomplete_value": true,
      "site": "00b5ca10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c9cc",
      "incomplete_value": true,
      "site": "00b5c9cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
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
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5c9f8",
      "incomplete_value": true,
      "site": "00b5c9f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c9b4",
      "incomplete_value": true,
      "site": "00b5c9b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5ca04",
      "incomplete_value": false,
      "site": "00b5ca08",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c9c0",
      "incomplete_value": false,
      "site": "00b5c9c4",
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
            "const:fd8:8"
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
      "00b5c9f4",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ca04",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b5ca10",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5c9f4",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ca04",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00b5ca10",
      "WRITE",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5c9c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c9a0.md#insn-00b5c9c4) · [`00b5c9cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c9a0.md#insn-00b5c9cc) · [`00b5c9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c9a0.md#insn-00b5c9b0)
- 新版 `00b5ca08`（命令位置の公開資料なし） · `00b5ca10`（命令位置の公開資料なし） · `00b5c9f4`（命令位置の公開資料なし）

~~~diff
- 00b5c9c4 ["INT_ADD", "register:40f0:8", ["const:b5c9c4:8", "const:4:8"]]
- 00b5c9c4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5ca08 ["INT_ADD", "register:40f0:8", ["const:b5ca08:8", "const:4:8"]]
+ 00b5ca08 ["CALL", null, ["callee:00bde090:8"]]
- 00b5c9c4 bytes 9f050294
+ 00b5ca08 bytes a2050294
- 00b5c9cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
- 00b5c9cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5ca10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:420:8"]]
+ 00b5ca10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5c9cc bytes 60f201f9
+ 00b5ca10 bytes 601202f9
- 00b5c9b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
- 00b5c9b0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5c9f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:420:8"]]
+ 00b5c9f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5c9b0 bytes 68f241f9
+ 00b5c9f4 bytes 681242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3345786c8c409fd352f17f37d9be612d"></a>

### [`00b5c9e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c9e0.md) → [`00b5ca24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ca24.md) _ZN8firebase4auth4auth19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b5ca50",
      "incomplete_value": true,
      "site": "00b5ca50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca0c",
      "incomplete_value": true,
      "site": "00b5ca0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
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
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5ca38",
      "incomplete_value": true,
      "site": "00b5ca38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c9f4",
      "incomplete_value": true,
      "site": "00b5c9f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5ca40",
      "incomplete_value": false,
      "site": "00b5ca48",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5c9fc",
      "incomplete_value": false,
      "site": "00b5ca04",
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
            "const:fd8:8"
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
      "00b5ca34",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ca40",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b5ca50",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5ca34",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ca40",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00b5ca50",
      "WRITE",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ca04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c9e0.md#insn-00b5ca04) · [`00b5ca0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c9e0.md#insn-00b5ca0c) · [`00b5c9f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5c9e0.md#insn-00b5c9f0)
- 新版 `00b5ca48`（命令位置の公開資料なし） · `00b5ca50`（命令位置の公開資料なし） · `00b5ca34`（命令位置の公開資料なし）

~~~diff
- 00b5ca04 ["INT_ADD", "register:40f0:8", ["const:b5ca04:8", "const:4:8"]]
- 00b5ca04 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5ca48 ["INT_ADD", "register:40f0:8", ["const:b5ca48:8", "const:4:8"]]
+ 00b5ca48 ["CALL", null, ["callee:00bde090:8"]]
- 00b5ca04 bytes 8f050294
+ 00b5ca48 bytes 92050294
- 00b5ca0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
- 00b5ca0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5ca50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:420:8"]]
+ 00b5ca50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5ca0c bytes 60f201f9
+ 00b5ca50 bytes 601202f9
- 00b5c9f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
- 00b5c9f0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5ca34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:420:8"]]
+ 00b5ca34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5c9f0 bytes 68f241f9
+ 00b5ca34 bytes 681242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf2c99baf719e610f7b7c9ac40541477"></a>

### [`00b5ca20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ca20.md) → [`00b5ca64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ca64.md) _ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b5ca94",
      "incomplete_value": true,
      "site": "00b5ca94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca50",
      "incomplete_value": true,
      "site": "00b5ca50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
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
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5ca78",
      "incomplete_value": true,
      "site": "00b5ca78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca34",
      "incomplete_value": true,
      "site": "00b5ca34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5ca84",
      "incomplete_value": false,
      "site": "00b5ca8c",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca40",
      "incomplete_value": false,
      "site": "00b5ca48",
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
            "const:fd8:8"
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
      "00b5ca74",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ca84",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b5ca94",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5ca74",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ca84",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00b5ca94",
      "WRITE",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ca48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ca20.md#insn-00b5ca48) · [`00b5ca50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ca20.md#insn-00b5ca50) · [`00b5ca30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ca20.md#insn-00b5ca30)
- 新版 `00b5ca8c`（命令位置の公開資料なし） · `00b5ca94`（命令位置の公開資料なし） · `00b5ca74`（命令位置の公開資料なし）

~~~diff
- 00b5ca48 ["INT_ADD", "register:40f0:8", ["const:b5ca48:8", "const:4:8"]]
- 00b5ca48 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5ca8c ["INT_ADD", "register:40f0:8", ["const:b5ca8c:8", "const:4:8"]]
+ 00b5ca8c ["CALL", null, ["callee:00bde090:8"]]
- 00b5ca48 bytes 7e050294
+ 00b5ca8c bytes 81050294
- 00b5ca50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
- 00b5ca50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5ca94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:420:8"]]
+ 00b5ca94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5ca50 bytes 60f201f9
+ 00b5ca94 bytes 601202f9
- 00b5ca30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
- 00b5ca30 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5ca74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:420:8"]]
+ 00b5ca74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5ca30 bytes 68f241f9
+ 00b5ca74 bytes 681242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e280e820d70ed284ed4a9f96ae4f17c"></a>

### [`00b5ca64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ca64.md) → [`00b5caa8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5caa8.md) _ZN8firebase4auth4auth10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b5cad8",
      "incomplete_value": true,
      "site": "00b5cad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca94",
      "incomplete_value": true,
      "site": "00b5ca94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
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
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b5cabc",
      "incomplete_value": true,
      "site": "00b5cabc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca78",
      "incomplete_value": true,
      "site": "00b5ca78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5cac4",
      "incomplete_value": false,
      "site": "00b5cad0",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ca80",
      "incomplete_value": false,
      "site": "00b5ca8c",
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
            "const:fd8:8"
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
      "00b5cab8",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cac4",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b5cad8",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cab8",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cac4",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00b5cad8",
      "WRITE",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ca8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ca64.md#insn-00b5ca8c) · [`00b5ca94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ca64.md#insn-00b5ca94) · [`00b5ca74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ca64.md#insn-00b5ca74)
- 新版 `00b5cad0`（命令位置の公開資料なし） · `00b5cad8`（命令位置の公開資料なし） · `00b5cab8`（命令位置の公開資料なし）

~~~diff
- 00b5ca8c ["INT_ADD", "register:40f0:8", ["const:b5ca8c:8", "const:4:8"]]
- 00b5ca8c ["CALL", null, ["callee:00bde090:8"]]
+ 00b5cad0 ["INT_ADD", "register:40f0:8", ["const:b5cad0:8", "const:4:8"]]
+ 00b5cad0 ["CALL", null, ["callee:00bde090:8"]]
- 00b5ca8c bytes 6d050294
+ 00b5cad0 bytes 70050294
- 00b5ca94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
- 00b5ca94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5cad8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:420:8"]]
+ 00b5cad8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5ca94 bytes 60f201f9
+ 00b5cad8 bytes 601202f9
- 00b5ca74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:3e0:8"]]
- 00b5ca74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cab8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:420:8"]]
+ 00b5cab8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5ca74 bytes 68f241f9
+ 00b5cab8 bytes 681242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa04e3fe2cb45a16ff20ee97b40eef8b"></a>

### [`00b5cab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cab4.md) → [`00b5caf8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5caf8.md) _ZN8firebase4auth4auth15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b5cb50",
      "incomplete_value": true,
      "site": "00b5cb50",
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
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cb0c",
      "incomplete_value": true,
      "site": "00b5cb0c",
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
            "const:3e8:8"
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
      "definition_site": "00b5cb2c",
      "incomplete_value": true,
      "site": "00b5cb38",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:420:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cae8",
      "incomplete_value": true,
      "site": "00b5caf4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e0:8"
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
      "00b5cb0c",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5cb2c",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cb50",
      "WRITE",
      [
        "storage",
        "010a13e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5cb0c",
      "READ",
      [
        "storage",
        "010a1428",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5cb2c",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cb50",
      "WRITE",
      [
        "storage",
        "010a1428",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cac8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cab4.md#insn-00b5cac8) · [`00b5caf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cab4.md#insn-00b5caf4) · [`00b5cb0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cab4.md#insn-00b5cb0c)
- 新版 `00b5cb0c`（命令位置の公開資料なし） · `00b5cb38`（命令位置の公開資料なし） · `00b5cb50`（命令位置の公開資料なし）

~~~diff
- 00b5cac8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3e8:8"]]
- 00b5cac8 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b5cac8 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b5cb0c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:428:8"]]
+ 00b5cb0c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cb0c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b5cac8 bytes a8a24f39
+ 00b5cb0c bytes a8a25039
- 00b5caf4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5caf4 ["INT_ADD", "register:40f0:8", ["const:b5caf4:8", "const:4:8"]]
- 00b5caf4 ["CALLIND", null, ["register:0:8"]]
+ 00b5cb38 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5cb38 ["INT_ADD", "register:40f0:8", ["const:b5cb38:8", "const:4:8"]]
+ 00b5cb38 ["CALLIND", null, ["register:0:8"]]
- 00b5caf4 bytes 00013fd6
+ 00b5cb38 bytes 00013fd6
- 00b5cb0c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b5cb0c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:3e8:8"]]
- 00b5cb0c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b5cb50 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b5cb50 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:428:8"]]
+ 00b5cb50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b5cb0c bytes a0a20f39
+ 00b5cb50 bytes a0a21039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbdf414841cc5f3f7e5bba2abae07c55"></a>

### [`00b5cb20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cb20.md) → [`00b5cb64`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cb64.md) _ZN8firebase4auth4auth12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b5cba0",
      "incomplete_value": true,
      "site": "00b5cba0",
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
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cb5c",
      "incomplete_value": true,
      "site": "00b5cb5c",
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
            "const:3e8:8"
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
      "definition_site": "00b5cbc0",
      "incomplete_value": true,
      "site": "00b5cbc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cb7c",
      "incomplete_value": true,
      "site": "00b5cb7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "definition_site": "00b5cb7c",
      "incomplete_value": true,
      "site": "00b5cb7c",
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
      "definition_site": "00b5cb38",
      "incomplete_value": true,
      "site": "00b5cb38",
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
      "00b5cb78",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cb84",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5cba0",
      "WRITE",
      [
        "storage",
        "010a13e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5cb78",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cb84",
      "READ",
      [
        "storage",
        "010a1428",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5cba0",
      "WRITE",
      [
        "storage",
        "010a1428",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cb34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cb20.md#insn-00b5cb34) · [`00b5cb5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cb20.md#insn-00b5cb5c) · [`00b5cb78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cb20.md#insn-00b5cb78)
- 新版 `00b5cb78`（命令位置の公開資料なし） · `00b5cba0`（命令位置の公開資料なし） · `00b5cbbc`（命令位置の公開資料なし）

~~~diff
- 00b5cb34 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3e0:8"]]
- 00b5cb34 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cb78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:420:8"]]
+ 00b5cb78 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5cb34 bytes 81f241f9
+ 00b5cb78 bytes 811242f9
- 00b5cb5c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5cb5c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5cb5c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3e8:8"]]
- 00b5cb5c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b5cba0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b5cba0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b5cba0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:428:8"]]
+ 00b5cba0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5cb5c bytes bfa20f39
+ 00b5cba0 bytes bfa21039
- 00b5cb78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5cb78 ["INT_ADD", "register:40f0:8", ["const:b5cb78:8", "const:4:8"]]
- 00b5cb78 ["CALLIND", null, ["register:0:8"]]
+ 00b5cbbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5cbbc ["INT_ADD", "register:40f0:8", ["const:b5cbbc:8", "const:4:8"]]
+ 00b5cbbc ["CALLIND", null, ["register:0:8"]]
- 00b5cb78 bytes 00013fd6
+ 00b5cbbc bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d711c21d9bb1d6533d0d4694d4816a40"></a>

### [`00b5cb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cb90.md) → [`00b5cbd4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cbd4.md) _ZN8firebase4auth4auth14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b5cc14",
      "incomplete_value": true,
      "site": "00b5cc14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cbd0",
      "incomplete_value": true,
      "site": "00b5cbd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "definition_site": "00b5cbf0",
      "incomplete_value": true,
      "site": "00b5cbf0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cbac",
      "incomplete_value": true,
      "site": "00b5cbac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5cbf8",
      "incomplete_value": false,
      "site": "00b5cc0c",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cbb4",
      "incomplete_value": false,
      "site": "00b5cbc8",
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
            "const:fd8:8"
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
      "00b5cbe8",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cbf8",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b5cc14",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cbe8",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cbf8",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00b5cc14",
      "WRITE",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cbc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cb90.md#insn-00b5cbc8) · [`00b5cbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cb90.md#insn-00b5cbd0) · [`00b5cba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cb90.md#insn-00b5cba4)
- 新版 `00b5cc0c`（命令位置の公開資料なし） · `00b5cc14`（命令位置の公開資料なし） · `00b5cbe8`（命令位置の公開資料なし）

~~~diff
- 00b5cbc8 ["INT_ADD", "register:40f0:8", ["const:b5cbc8:8", "const:4:8"]]
- 00b5cbc8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5cc0c ["INT_ADD", "register:40f0:8", ["const:b5cc0c:8", "const:4:8"]]
+ 00b5cc0c ["CALL", null, ["callee:00bde090:8"]]
- 00b5cbc8 bytes 1e050294
+ 00b5cc0c bytes 21050294
- 00b5cbd0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3e0:8"]]
- 00b5cbd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5cc14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:420:8"]]
+ 00b5cc14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cbd0 bytes 80f201f9
+ 00b5cc14 bytes 801202f9
- 00b5cba4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3e0:8"]]
- 00b5cba4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cbe8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:420:8"]]
+ 00b5cbe8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5cba4 bytes 81f241f9
+ 00b5cbe8 bytes 811242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1913dfa3ab53468d39a30e9338ed9125"></a>

### [`00b5cc00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cc00.md) → [`00b5cc44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cc44.md) _ZN8firebase4auth4auth11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b5cc60",
      "incomplete_value": false,
      "site": "00b5cc64",
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
      "definition_site": "00b5cc1c",
      "incomplete_value": false,
      "site": "00b5cc20",
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
      "definition_site": "00b5cc70",
      "incomplete_value": true,
      "site": "00b5cc7c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5cc2c",
      "incomplete_value": true,
      "site": "00b5cc38",
      "value": [
        "LOAD",
        "8",
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
      "00b5cc60",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b5cc70",
      "DATA",
      [
        "storage",
        "010a13f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cc60",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b5cc70",
      "DATA",
      [
        "storage",
        "010a1430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cc20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cc00.md#insn-00b5cc20) · [`00b5cc1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cc00.md#insn-00b5cc1c) · [`00b5cc28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cc00.md#insn-00b5cc28)
- 新版 `00b5cc64`（命令位置の公開資料なし） · `00b5cc60`（命令位置の公開資料なし） · `00b5cc6c`（命令位置の公開資料なし）

~~~diff
- 00b5cc20 ["INT_ADD", "register:40f0:8", ["const:b5cc20:8", "const:4:8"]]
- 00b5cc20 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5cc64 ["INT_ADD", "register:40f0:8", ["const:b5cc64:8", "const:4:8"]]
+ 00b5cc64 ["CALL", null, ["callee:00bde180:8"]]
- 00b5cc20 bytes 44050294
+ 00b5cc64 bytes 47050294
- 00b5cc1c ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b5cc1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5cc1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5cc1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5cc60 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b5cc60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5cc60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5cc60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5cc1c bytes 00501791
+ 00b5cc60 bytes 001c1591
- 00b5cc28 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 00b5cc28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5cc28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5cc28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5cc6c ["COPY", "tmp:0:8", ["const:430:8"]]
+ 00b5cc6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5cc6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5cc6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5cc28 bytes 08c10f91
+ 00b5cc6c bytes 08c11091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7718fed392b163a945ae9aca7e215279"></a>

### [`00b5cc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cc3c.md) → [`00b5cc80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cc80.md) _ZN8firebase4auth4auth13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b5ccc0",
      "incomplete_value": true,
      "site": "00b5ccc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cc7c",
      "incomplete_value": true,
      "site": "00b5cc7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "definition_site": "00b5cc9c",
      "incomplete_value": true,
      "site": "00b5cc9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cc58",
      "incomplete_value": true,
      "site": "00b5cc58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5cca4",
      "incomplete_value": false,
      "site": "00b5ccb8",
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
            "const:fd6:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cc60",
      "incomplete_value": false,
      "site": "00b5cc74",
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
            "const:fd8:8"
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
      "00b5cc94",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cca4",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b5ccc0",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cc94",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cca4",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00b5ccc0",
      "WRITE",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cc74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cc3c.md#insn-00b5cc74) · [`00b5cc7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cc3c.md#insn-00b5cc7c) · [`00b5cc50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cc3c.md#insn-00b5cc50)
- 新版 `00b5ccb8`（命令位置の公開資料なし） · `00b5ccc0`（命令位置の公開資料なし） · `00b5cc94`（命令位置の公開資料なし）

~~~diff
- 00b5cc74 ["INT_ADD", "register:40f0:8", ["const:b5cc74:8", "const:4:8"]]
- 00b5cc74 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5ccb8 ["INT_ADD", "register:40f0:8", ["const:b5ccb8:8", "const:4:8"]]
+ 00b5ccb8 ["CALL", null, ["callee:00bde090:8"]]
- 00b5cc74 bytes f3040294
+ 00b5ccb8 bytes f6040294
- 00b5cc7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3e0:8"]]
- 00b5cc7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5ccc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:420:8"]]
+ 00b5ccc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cc7c bytes 80f201f9
+ 00b5ccc0 bytes 801202f9
- 00b5cc50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3e0:8"]]
- 00b5cc50 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cc94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:420:8"]]
+ 00b5cc94 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5cc50 bytes 81f241f9
+ 00b5cc94 bytes 811242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3df9f1dc00c4b61ab2dc9e5e9770a86"></a>

### [`00b5ccac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ccac.md) → [`00b5ccf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ccf0.md) _ZN8firebase4auth4auth10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b5cd0c",
      "incomplete_value": false,
      "site": "00b5cd10",
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
      "definition_site": "00b5ccc8",
      "incomplete_value": false,
      "site": "00b5cccc",
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
      "definition_site": "00b5cd1c",
      "incomplete_value": true,
      "site": "00b5cd28",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5ccd8",
      "incomplete_value": true,
      "site": "00b5cce4",
      "value": [
        "LOAD",
        "8",
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
      "00b5cd0c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b5cd1c",
      "DATA",
      [
        "storage",
        "010a1480",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5cd0c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b5cd1c",
      "DATA",
      [
        "storage",
        "010a14c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cccc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ccac.md#insn-00b5cccc) · [`00b5ccc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ccac.md#insn-00b5ccc8) · [`00b5ccd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ccac.md#insn-00b5ccd4)
- 新版 `00b5cd10`（命令位置の公開資料なし） · `00b5cd0c`（命令位置の公開資料なし） · `00b5cd18`（命令位置の公開資料なし）

~~~diff
- 00b5cccc ["INT_ADD", "register:40f0:8", ["const:b5cccc:8", "const:4:8"]]
- 00b5cccc ["CALL", null, ["callee:00bde180:8"]]
+ 00b5cd10 ["INT_ADD", "register:40f0:8", ["const:b5cd10:8", "const:4:8"]]
+ 00b5cd10 ["CALL", null, ["callee:00bde180:8"]]
- 00b5cccc bytes 19050294
+ 00b5cd10 bytes 1c050294
- 00b5ccc8 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b5ccc8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5ccc8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5ccc8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5cd0c ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b5cd0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5cd0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5cd0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5ccc8 bytes 00fc1991
+ 00b5cd0c bytes 00c81791
- 00b5ccd4 ["COPY", "tmp:0:8", ["const:480:8"]]
- 00b5ccd4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5ccd4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5ccd4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5cd18 ["COPY", "tmp:0:8", ["const:4c0:8"]]
+ 00b5cd18 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5cd18 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5cd18 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5ccd4 bytes 08011291
+ 00b5cd18 bytes 08011391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4b75a817449628bca440e4fef69b780"></a>

### [`00b5cce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cce8.md) → [`00b5cd2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cd2c.md) _ZN8firebase4auth17signinmethodquery19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00b5cd58",
      "incomplete_value": true,
      "site": "00b5cd58",
      "value": [
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
    "old": {
      "definition_site": "00b5cd14",
      "incomplete_value": true,
      "site": "00b5cd14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "definition_site": "00b5cd40",
      "incomplete_value": true,
      "site": "00b5cd40",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ccfc",
      "incomplete_value": true,
      "site": "00b5ccfc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5cd4c",
      "incomplete_value": false,
      "site": "00b5cd50",
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
            "const:40e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cd08",
      "incomplete_value": false,
      "site": "00b5cd0c",
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
            "const:49b:8"
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
      "00b5cd3c",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cd4c",
      "PARAM",
      [
        "storage",
        "0029349b",
        null,
        "string"
      ]
    ],
    [
      "00b5cd58",
      "WRITE",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cd3c",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cd4c",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00b5cd58",
      "WRITE",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cd0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cce8.md#insn-00b5cd0c) · [`00b5cd14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cce8.md#insn-00b5cd14) · [`00b5ccf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cce8.md#insn-00b5ccf8)
- 新版 `00b5cd50`（命令位置の公開資料なし） · `00b5cd58`（命令位置の公開資料なし） · `00b5cd3c`（命令位置の公開資料なし）

~~~diff
- 00b5cd0c ["INT_ADD", "register:40f0:8", ["const:b5cd0c:8", "const:4:8"]]
- 00b5cd0c ["CALL", null, ["callee:00bde090:8"]]
+ 00b5cd50 ["INT_ADD", "register:40f0:8", ["const:b5cd50:8", "const:4:8"]]
+ 00b5cd50 ["CALL", null, ["callee:00bde090:8"]]
- 00b5cd0c bytes cd040294
+ 00b5cd50 bytes d0040294
- 00b5cd14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
- 00b5cd14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5cd58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00b5cd58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cd14 bytes 604602f9
+ 00b5cd58 bytes 606602f9
- 00b5ccf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
- 00b5ccf8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cd3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00b5cd3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5ccf8 bytes 684642f9
+ 00b5cd3c bytes 686642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee6919672653a1b0370f0b1e870c5686"></a>

### [`00b5cd28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cd28.md) → [`00b5cd6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cd6c.md) _ZN8firebase4auth17signinmethodquery19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS

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
      "definition_site": "00b5cd98",
      "incomplete_value": true,
      "site": "00b5cd98",
      "value": [
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
    "old": {
      "definition_site": "00b5cd54",
      "incomplete_value": true,
      "site": "00b5cd54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "definition_site": "00b5cd80",
      "incomplete_value": true,
      "site": "00b5cd80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cd3c",
      "incomplete_value": true,
      "site": "00b5cd3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5cd88",
      "incomplete_value": false,
      "site": "00b5cd90",
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
            "const:40e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cd44",
      "incomplete_value": false,
      "site": "00b5cd4c",
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
            "const:49b:8"
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
      "00b5cd7c",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cd88",
      "PARAM",
      [
        "storage",
        "0029349b",
        null,
        "string"
      ]
    ],
    [
      "00b5cd98",
      "WRITE",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cd7c",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cd88",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00b5cd98",
      "WRITE",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cd4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cd28.md#insn-00b5cd4c) · [`00b5cd54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cd28.md#insn-00b5cd54) · [`00b5cd38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cd28.md#insn-00b5cd38)
- 新版 `00b5cd90`（命令位置の公開資料なし） · `00b5cd98`（命令位置の公開資料なし） · `00b5cd7c`（命令位置の公開資料なし）

~~~diff
- 00b5cd4c ["INT_ADD", "register:40f0:8", ["const:b5cd4c:8", "const:4:8"]]
- 00b5cd4c ["CALL", null, ["callee:00bde090:8"]]
+ 00b5cd90 ["INT_ADD", "register:40f0:8", ["const:b5cd90:8", "const:4:8"]]
+ 00b5cd90 ["CALL", null, ["callee:00bde090:8"]]
- 00b5cd4c bytes bd040294
+ 00b5cd90 bytes c0040294
- 00b5cd54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
- 00b5cd54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5cd98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00b5cd98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cd54 bytes 604602f9
+ 00b5cd98 bytes 606602f9
- 00b5cd38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
- 00b5cd38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cd7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00b5cd7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5cd38 bytes 684642f9
+ 00b5cd7c bytes 686642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49003add0027c9a3c851107cadb78655"></a>

### [`00b5cd68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cd68.md) → [`00b5cdac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cdac.md) _ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b5cddc",
      "incomplete_value": true,
      "site": "00b5cddc",
      "value": [
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
    "old": {
      "definition_site": "00b5cd98",
      "incomplete_value": true,
      "site": "00b5cd98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "definition_site": "00b5cdc0",
      "incomplete_value": true,
      "site": "00b5cdc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cd7c",
      "incomplete_value": true,
      "site": "00b5cd7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5cdcc",
      "incomplete_value": false,
      "site": "00b5cdd4",
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
            "const:40e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cd88",
      "incomplete_value": false,
      "site": "00b5cd90",
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
            "const:49b:8"
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
      "00b5cdbc",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cdcc",
      "PARAM",
      [
        "storage",
        "0029349b",
        null,
        "string"
      ]
    ],
    [
      "00b5cddc",
      "WRITE",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cdbc",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cdcc",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00b5cddc",
      "WRITE",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cd90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cd68.md#insn-00b5cd90) · [`00b5cd98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cd68.md#insn-00b5cd98) · [`00b5cd78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cd68.md#insn-00b5cd78)
- 新版 `00b5cdd4`（命令位置の公開資料なし） · `00b5cddc`（命令位置の公開資料なし） · `00b5cdbc`（命令位置の公開資料なし）

~~~diff
- 00b5cd90 ["INT_ADD", "register:40f0:8", ["const:b5cd90:8", "const:4:8"]]
- 00b5cd90 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5cdd4 ["INT_ADD", "register:40f0:8", ["const:b5cdd4:8", "const:4:8"]]
+ 00b5cdd4 ["CALL", null, ["callee:00bde090:8"]]
- 00b5cd90 bytes ac040294
+ 00b5cdd4 bytes af040294
- 00b5cd98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
- 00b5cd98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5cddc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00b5cddc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cd98 bytes 604602f9
+ 00b5cddc bytes 606602f9
- 00b5cd78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
- 00b5cd78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cdbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00b5cdbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5cd78 bytes 684642f9
+ 00b5cdbc bytes 686642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d115d38e7f933f336b5b0faf40e8af4c"></a>

### [`00b5cdac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cdac.md) → [`00b5cdf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cdf0.md) _ZN8firebase4auth17signinmethodquery10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b5ce20",
      "incomplete_value": true,
      "site": "00b5ce20",
      "value": [
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
    "old": {
      "definition_site": "00b5cddc",
      "incomplete_value": true,
      "site": "00b5cddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "definition_site": "00b5ce04",
      "incomplete_value": true,
      "site": "00b5ce04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cdc0",
      "incomplete_value": true,
      "site": "00b5cdc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5ce0c",
      "incomplete_value": false,
      "site": "00b5ce18",
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
            "const:40e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cdc8",
      "incomplete_value": false,
      "site": "00b5cdd4",
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
            "const:49b:8"
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
      "00b5ce00",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ce0c",
      "PARAM",
      [
        "storage",
        "0029349b",
        null,
        "string"
      ]
    ],
    [
      "00b5ce20",
      "WRITE",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5ce00",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ce0c",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00b5ce20",
      "WRITE",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cdd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cdac.md#insn-00b5cdd4) · [`00b5cddc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cdac.md#insn-00b5cddc) · [`00b5cdbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cdac.md#insn-00b5cdbc)
- 新版 `00b5ce18`（命令位置の公開資料なし） · `00b5ce20`（命令位置の公開資料なし） · `00b5ce00`（命令位置の公開資料なし）

~~~diff
- 00b5cdd4 ["INT_ADD", "register:40f0:8", ["const:b5cdd4:8", "const:4:8"]]
- 00b5cdd4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5ce18 ["INT_ADD", "register:40f0:8", ["const:b5ce18:8", "const:4:8"]]
+ 00b5ce18 ["CALL", null, ["callee:00bde090:8"]]
- 00b5cdd4 bytes 9b040294
+ 00b5ce18 bytes 9e040294
- 00b5cddc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
- 00b5cddc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5ce20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00b5ce20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cddc bytes 604602f9
+ 00b5ce20 bytes 606602f9
- 00b5cdbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:488:8"]]
- 00b5cdbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5ce00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4c8:8"]]
+ 00b5ce00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5cdbc bytes 684642f9
+ 00b5ce00 bytes 686642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d5eca796477c9d3dcfd14779d519df43"></a>

### [`00b5cdfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cdfc.md) → [`00b5ce40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ce40.md) _ZN8firebase4auth17signinmethodquery15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b5ce98",
      "incomplete_value": true,
      "site": "00b5ce98",
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
    "old": {
      "definition_site": "00b5ce54",
      "incomplete_value": true,
      "site": "00b5ce54",
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
            "const:490:8"
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
      "definition_site": "00b5ce74",
      "incomplete_value": true,
      "site": "00b5ce80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5ce30",
      "incomplete_value": true,
      "site": "00b5ce3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:488:8"
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
      "00b5ce54",
      "READ",
      [
        "storage",
        "010a1490",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5ce74",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ce98",
      "WRITE",
      [
        "storage",
        "010a1490",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5ce54",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5ce74",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5ce98",
      "WRITE",
      [
        "storage",
        "010a14d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ce10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cdfc.md#insn-00b5ce10) · [`00b5ce3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cdfc.md#insn-00b5ce3c) · [`00b5ce54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cdfc.md#insn-00b5ce54)
- 新版 `00b5ce54`（命令位置の公開資料なし） · `00b5ce80`（命令位置の公開資料なし） · `00b5ce98`（命令位置の公開資料なし）

~~~diff
- 00b5ce10 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:490:8"]]
- 00b5ce10 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b5ce10 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b5ce54 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4d0:8"]]
+ 00b5ce54 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b5ce54 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b5ce10 bytes a8425239
+ 00b5ce54 bytes a8425339
- 00b5ce3c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5ce3c ["INT_ADD", "register:40f0:8", ["const:b5ce3c:8", "const:4:8"]]
- 00b5ce3c ["CALLIND", null, ["register:0:8"]]
+ 00b5ce80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5ce80 ["INT_ADD", "register:40f0:8", ["const:b5ce80:8", "const:4:8"]]
+ 00b5ce80 ["CALLIND", null, ["register:0:8"]]
- 00b5ce3c bytes 00013fd6
+ 00b5ce80 bytes 00013fd6
- 00b5ce54 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b5ce54 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:490:8"]]
- 00b5ce54 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b5ce98 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b5ce98 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4d0:8"]]
+ 00b5ce98 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b5ce54 bytes a0421239
+ 00b5ce98 bytes a0421339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7195b91c9cff18aa26b46a82d42c5660"></a>

### [`00b5ce68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ce68.md) → [`00b5ceac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5ceac.md) _ZN8firebase4auth17signinmethodquery12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b5cee8",
      "incomplete_value": true,
      "site": "00b5cee8",
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
    "old": {
      "definition_site": "00b5cea4",
      "incomplete_value": true,
      "site": "00b5cea4",
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
            "const:490:8"
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
      "definition_site": "00b5cf08",
      "incomplete_value": true,
      "site": "00b5cf08",
      "value": [
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
    "old": {
      "definition_site": "00b5cec4",
      "incomplete_value": true,
      "site": "00b5cec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "definition_site": "00b5cec4",
      "incomplete_value": true,
      "site": "00b5cec4",
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
      "definition_site": "00b5ce80",
      "incomplete_value": true,
      "site": "00b5ce80",
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
      "00b5cec0",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cecc",
      "READ",
      [
        "storage",
        "010a1490",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5cee8",
      "WRITE",
      [
        "storage",
        "010a1490",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5cec0",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cecc",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5cee8",
      "WRITE",
      [
        "storage",
        "010a14d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5ce7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ce68.md#insn-00b5ce7c) · [`00b5cea4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ce68.md#insn-00b5cea4) · [`00b5cec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ce68.md#insn-00b5cec0)
- 新版 `00b5cec0`（命令位置の公開資料なし） · `00b5cee8`（命令位置の公開資料なし） · `00b5cf04`（命令位置の公開資料なし）

~~~diff
- 00b5ce7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:488:8"]]
- 00b5ce7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cec0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
+ 00b5cec0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5ce7c bytes 814642f9
+ 00b5cec0 bytes 816642f9
- 00b5cea4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5cea4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5cea4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:490:8"]]
- 00b5cea4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b5cee8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b5cee8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b5cee8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4d0:8"]]
+ 00b5cee8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5cea4 bytes bf421239
+ 00b5cee8 bytes bf421339
- 00b5cec0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5cec0 ["INT_ADD", "register:40f0:8", ["const:b5cec0:8", "const:4:8"]]
- 00b5cec0 ["CALLIND", null, ["register:0:8"]]
+ 00b5cf04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5cf04 ["INT_ADD", "register:40f0:8", ["const:b5cf04:8", "const:4:8"]]
+ 00b5cf04 ["CALLIND", null, ["register:0:8"]]
- 00b5cec0 bytes 00013fd6
+ 00b5cf04 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e660f63148819cb3f543f50552f1f11"></a>

### [`00b5ced8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ced8.md) → [`00b5cf1c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cf1c.md) _ZN8firebase4auth17signinmethodquery14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b5cf5c",
      "incomplete_value": true,
      "site": "00b5cf5c",
      "value": [
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
    "old": {
      "definition_site": "00b5cf18",
      "incomplete_value": true,
      "site": "00b5cf18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "definition_site": "00b5cf38",
      "incomplete_value": true,
      "site": "00b5cf38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cef4",
      "incomplete_value": true,
      "site": "00b5cef4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5cf40",
      "incomplete_value": false,
      "site": "00b5cf54",
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
            "const:40e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cefc",
      "incomplete_value": false,
      "site": "00b5cf10",
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
            "const:49b:8"
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
      "00b5cf30",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cf40",
      "PARAM",
      [
        "storage",
        "0029349b",
        null,
        "string"
      ]
    ],
    [
      "00b5cf5c",
      "WRITE",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cf30",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cf40",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00b5cf5c",
      "WRITE",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cf10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ced8.md#insn-00b5cf10) · [`00b5cf18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ced8.md#insn-00b5cf18) · [`00b5ceec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5ced8.md#insn-00b5ceec)
- 新版 `00b5cf54`（命令位置の公開資料なし） · `00b5cf5c`（命令位置の公開資料なし） · `00b5cf30`（命令位置の公開資料なし）

~~~diff
- 00b5cf10 ["INT_ADD", "register:40f0:8", ["const:b5cf10:8", "const:4:8"]]
- 00b5cf10 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5cf54 ["INT_ADD", "register:40f0:8", ["const:b5cf54:8", "const:4:8"]]
+ 00b5cf54 ["CALL", null, ["callee:00bde090:8"]]
- 00b5cf10 bytes 4c040294
+ 00b5cf54 bytes 4f040294
- 00b5cf18 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:488:8"]]
- 00b5cf18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5cf5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
+ 00b5cf5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cf18 bytes 804602f9
+ 00b5cf5c bytes 806602f9
- 00b5ceec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:488:8"]]
- 00b5ceec ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cf30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
+ 00b5cf30 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5ceec bytes 814642f9
+ 00b5cf30 bytes 816642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cde0f98e8138763f6fe300efed72fe02"></a>

### [`00b5cf48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cf48.md) → [`00b5cf8c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cf8c.md) _ZN8firebase4auth17signinmethodquery11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b5cfa8",
      "incomplete_value": false,
      "site": "00b5cfac",
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
      "definition_site": "00b5cf64",
      "incomplete_value": false,
      "site": "00b5cf68",
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
      "definition_site": "00b5cfb8",
      "incomplete_value": true,
      "site": "00b5cfc4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5cf74",
      "incomplete_value": true,
      "site": "00b5cf80",
      "value": [
        "LOAD",
        "8",
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
      "00b5cfa8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b5cfb8",
      "DATA",
      [
        "storage",
        "010a1498",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cfa8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b5cfb8",
      "DATA",
      [
        "storage",
        "010a14d8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cf68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cf48.md#insn-00b5cf68) · [`00b5cf64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cf48.md#insn-00b5cf64) · [`00b5cf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cf48.md#insn-00b5cf70)
- 新版 `00b5cfac`（命令位置の公開資料なし） · `00b5cfa8`（命令位置の公開資料なし） · `00b5cfb4`（命令位置の公開資料なし）

~~~diff
- 00b5cf68 ["INT_ADD", "register:40f0:8", ["const:b5cf68:8", "const:4:8"]]
- 00b5cf68 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5cfac ["INT_ADD", "register:40f0:8", ["const:b5cfac:8", "const:4:8"]]
+ 00b5cfac ["CALL", null, ["callee:00bde180:8"]]
- 00b5cf68 bytes 72040294
+ 00b5cfac bytes 75040294
- 00b5cf64 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b5cf64 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5cf64 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5cf64 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5cfa8 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b5cfa8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5cfa8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5cfa8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5cf64 bytes 00501791
+ 00b5cfa8 bytes 001c1591
- 00b5cf70 ["COPY", "tmp:0:8", ["const:498:8"]]
- 00b5cf70 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5cf70 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5cf70 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5cfb4 ["COPY", "tmp:0:8", ["const:4d8:8"]]
+ 00b5cfb4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5cfb4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5cfb4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5cf70 bytes 08611291
+ 00b5cfb4 bytes 08611391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-344f731eb1262fc016af06b79fc14621"></a>

### [`00b5cf84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cf84.md) → [`00b5cfc8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5c/00b5cfc8.md) _ZN8firebase4auth17signinmethodquery13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b5d008",
      "incomplete_value": true,
      "site": "00b5d008",
      "value": [
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
    "old": {
      "definition_site": "00b5cfc4",
      "incomplete_value": true,
      "site": "00b5cfc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:488:8"
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
      "definition_site": "00b5cfe4",
      "incomplete_value": true,
      "site": "00b5cfe4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cfa0",
      "incomplete_value": true,
      "site": "00b5cfa0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5cfec",
      "incomplete_value": false,
      "site": "00b5d000",
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
            "const:40e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5cfa8",
      "incomplete_value": false,
      "site": "00b5cfbc",
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
            "const:49b:8"
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
      "00b5cfdc",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cfec",
      "PARAM",
      [
        "storage",
        "0029349b",
        null,
        "string"
      ]
    ],
    [
      "00b5d008",
      "WRITE",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5cfdc",
      "READ",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5cfec",
      "PARAM",
      [
        "storage",
        "0029340e",
        null,
        "string"
      ]
    ],
    [
      "00b5d008",
      "WRITE",
      [
        "storage",
        "010a14c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5cfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cf84.md#insn-00b5cfbc) · [`00b5cfc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cf84.md#insn-00b5cfc4) · [`00b5cf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cf84.md#insn-00b5cf98)
- 新版 `00b5d000`（命令位置の公開資料なし） · `00b5d008`（命令位置の公開資料なし） · `00b5cfdc`（命令位置の公開資料なし）

~~~diff
- 00b5cfbc ["INT_ADD", "register:40f0:8", ["const:b5cfbc:8", "const:4:8"]]
- 00b5cfbc ["CALL", null, ["callee:00bde090:8"]]
+ 00b5d000 ["INT_ADD", "register:40f0:8", ["const:b5d000:8", "const:4:8"]]
+ 00b5d000 ["CALL", null, ["callee:00bde090:8"]]
- 00b5cfbc bytes 21040294
+ 00b5d000 bytes 24040294
- 00b5cfc4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:488:8"]]
- 00b5cfc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d008 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
+ 00b5d008 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5cfc4 bytes 804602f9
+ 00b5d008 bytes 806602f9
- 00b5cf98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:488:8"]]
- 00b5cf98 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5cfdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4c8:8"]]
+ 00b5cfdc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5cf98 bytes 814642f9
+ 00b5cfdc bytes 816642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2a3831d702ad86d49e7a41769c117a25"></a>

### [`00b5cff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cff4.md) → [`00b5d038`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d038.md) _ZN8firebase4auth17signinmethodquery10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b5d064",
      "incomplete_value": true,
      "site": "00b5d070",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5d020",
      "incomplete_value": true,
      "site": "00b5d02c",
      "value": [
        "LOAD",
        "8",
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
      "00b5d054",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b5d064",
      "DATA",
      [
        "storage",
        "010a14a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5d054",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b5d064",
      "DATA",
      [
        "storage",
        "010a14e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cff4.md#insn-00b5d010) · [`00b5d014`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cff4.md#insn-00b5d014) · [`00b5d01c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5c/00b5cff4.md#insn-00b5d01c)
- 新版 `00b5d054`（命令位置の公開資料なし） · `00b5d058`（命令位置の公開資料なし） · `00b5d060`（命令位置の公開資料なし）

~~~diff
- 00b5d010 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b5d010 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d010 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d010 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5d054 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b5d054 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d054 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d054 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5d010 bytes 00fc1991
+ 00b5d054 bytes 00c81791
- 00b5d014 ["INT_ADD", "register:40f0:8", ["const:b5d014:8", "const:4:8"]]
- 00b5d014 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5d058 ["INT_ADD", "register:40f0:8", ["const:b5d058:8", "const:4:8"]]
+ 00b5d058 ["CALL", null, ["callee:00bde180:8"]]
- 00b5d014 bytes 47040294
+ 00b5d058 bytes 4a040294
- 00b5d01c ["COPY", "tmp:0:8", ["const:4a0:8"]]
- 00b5d01c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d01c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d01c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5d060 ["COPY", "tmp:0:8", ["const:4e0:8"]]
+ 00b5d060 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d060 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d060 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5d01c bytes 08811291
+ 00b5d060 bytes 08811391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-122bee35ce7c74ae6aab24e7eb43447f"></a>

### [`00b5d030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d030.md) → [`00b5d074`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d074.md) _ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b5d0a0",
      "incomplete_value": true,
      "site": "00b5d0a0",
      "value": [
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
      "definition_site": "00b5d05c",
      "incomplete_value": true,
      "site": "00b5d05c",
      "value": [
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
      "definition_site": "00b5d088",
      "incomplete_value": true,
      "site": "00b5d088",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d044",
      "incomplete_value": true,
      "site": "00b5d044",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5d094",
      "incomplete_value": false,
      "site": "00b5d098",
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
            "const:16c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d050",
      "incomplete_value": false,
      "site": "00b5d054",
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
            "const:e1:8"
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
      "00b5d084",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d094",
      "PARAM",
      [
        "storage",
        "002a50e1",
        null,
        "string"
      ]
    ],
    [
      "00b5d0a0",
      "WRITE",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d084",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d094",
      "PARAM",
      [
        "storage",
        "002a516c",
        null,
        "string"
      ]
    ],
    [
      "00b5d0a0",
      "WRITE",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d030.md#insn-00b5d054) · [`00b5d05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d030.md#insn-00b5d05c) · [`00b5d040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d030.md#insn-00b5d040)
- 新版 `00b5d098`（命令位置の公開資料なし） · `00b5d0a0`（命令位置の公開資料なし） · `00b5d084`（命令位置の公開資料なし）

~~~diff
- 00b5d054 ["INT_ADD", "register:40f0:8", ["const:b5d054:8", "const:4:8"]]
- 00b5d054 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5d098 ["INT_ADD", "register:40f0:8", ["const:b5d098:8", "const:4:8"]]
+ 00b5d098 ["CALL", null, ["callee:00bde090:8"]]
- 00b5d054 bytes fb030294
+ 00b5d098 bytes fe030294
- 00b5d05c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00b5d05c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d0a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00b5d0a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d05c bytes 605602f9
+ 00b5d0a0 bytes 607602f9
- 00b5d040 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00b5d040 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d084 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00b5d084 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d040 bytes 685642f9
+ 00b5d084 bytes 687642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37ffa7a7dc391c1214f826f0f0c76099"></a>

### [`00b5d070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d070.md) → [`00b5d0b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d0b4.md) _ZN8firebase4auth11jnilistener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b5d0e0",
      "incomplete_value": true,
      "site": "00b5d0e0",
      "value": [
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
      "definition_site": "00b5d09c",
      "incomplete_value": true,
      "site": "00b5d09c",
      "value": [
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
      "definition_site": "00b5d0c8",
      "incomplete_value": true,
      "site": "00b5d0c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d084",
      "incomplete_value": true,
      "site": "00b5d084",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5d0d0",
      "incomplete_value": false,
      "site": "00b5d0d8",
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
            "const:16c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d08c",
      "incomplete_value": false,
      "site": "00b5d094",
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
            "const:e1:8"
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
      "00b5d0c4",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d0d0",
      "PARAM",
      [
        "storage",
        "002a50e1",
        null,
        "string"
      ]
    ],
    [
      "00b5d0e0",
      "WRITE",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d0c4",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d0d0",
      "PARAM",
      [
        "storage",
        "002a516c",
        null,
        "string"
      ]
    ],
    [
      "00b5d0e0",
      "WRITE",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d070.md#insn-00b5d094) · [`00b5d09c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d070.md#insn-00b5d09c) · [`00b5d080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d070.md#insn-00b5d080)
- 新版 `00b5d0d8`（命令位置の公開資料なし） · `00b5d0e0`（命令位置の公開資料なし） · `00b5d0c4`（命令位置の公開資料なし）

~~~diff
- 00b5d094 ["INT_ADD", "register:40f0:8", ["const:b5d094:8", "const:4:8"]]
- 00b5d094 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5d0d8 ["INT_ADD", "register:40f0:8", ["const:b5d0d8:8", "const:4:8"]]
+ 00b5d0d8 ["CALL", null, ["callee:00bde090:8"]]
- 00b5d094 bytes eb030294
+ 00b5d0d8 bytes ee030294
- 00b5d09c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00b5d09c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d0e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00b5d0e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d09c bytes 605602f9
+ 00b5d0e0 bytes 607602f9
- 00b5d080 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00b5d080 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d0c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00b5d0c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d080 bytes 685642f9
+ 00b5d0c4 bytes 687642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f1028d83bde9aecc7893fa91d06a8c4b"></a>

### [`00b5d0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d0b0.md) → [`00b5d0f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d0f4.md) _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b5d124",
      "incomplete_value": true,
      "site": "00b5d124",
      "value": [
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
      "definition_site": "00b5d0e0",
      "incomplete_value": true,
      "site": "00b5d0e0",
      "value": [
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
      "definition_site": "00b5d108",
      "incomplete_value": true,
      "site": "00b5d108",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d0c4",
      "incomplete_value": true,
      "site": "00b5d0c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5d114",
      "incomplete_value": false,
      "site": "00b5d11c",
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
            "const:16c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d0d0",
      "incomplete_value": false,
      "site": "00b5d0d8",
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
            "const:e1:8"
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
      "00b5d104",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d114",
      "PARAM",
      [
        "storage",
        "002a50e1",
        null,
        "string"
      ]
    ],
    [
      "00b5d124",
      "WRITE",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d104",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d114",
      "PARAM",
      [
        "storage",
        "002a516c",
        null,
        "string"
      ]
    ],
    [
      "00b5d124",
      "WRITE",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d0d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d0b0.md#insn-00b5d0d8) · [`00b5d0e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d0b0.md#insn-00b5d0e0) · [`00b5d0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d0b0.md#insn-00b5d0c0)
- 新版 `00b5d11c`（命令位置の公開資料なし） · `00b5d124`（命令位置の公開資料なし） · `00b5d104`（命令位置の公開資料なし）

~~~diff
- 00b5d0d8 ["INT_ADD", "register:40f0:8", ["const:b5d0d8:8", "const:4:8"]]
- 00b5d0d8 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5d11c ["INT_ADD", "register:40f0:8", ["const:b5d11c:8", "const:4:8"]]
+ 00b5d11c ["CALL", null, ["callee:00bde090:8"]]
- 00b5d0d8 bytes da030294
+ 00b5d11c bytes dd030294
- 00b5d0e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00b5d0e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d124 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00b5d124 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d0e0 bytes 605602f9
+ 00b5d124 bytes 607602f9
- 00b5d0c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00b5d0c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d104 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00b5d104 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d0c0 bytes 685642f9
+ 00b5d104 bytes 687642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61f2422016b7f745ec9cf5c41e1c3ed9"></a>

### [`00b5d0f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d0f4.md) → [`00b5d138`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d138.md) _ZN8firebase4auth11jnilistener10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b5d168",
      "incomplete_value": true,
      "site": "00b5d168",
      "value": [
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
      "definition_site": "00b5d124",
      "incomplete_value": true,
      "site": "00b5d124",
      "value": [
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
      "definition_site": "00b5d14c",
      "incomplete_value": true,
      "site": "00b5d14c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d108",
      "incomplete_value": true,
      "site": "00b5d108",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5d154",
      "incomplete_value": false,
      "site": "00b5d160",
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
            "const:16c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d110",
      "incomplete_value": false,
      "site": "00b5d11c",
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
            "const:e1:8"
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
      "00b5d148",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d154",
      "PARAM",
      [
        "storage",
        "002a50e1",
        null,
        "string"
      ]
    ],
    [
      "00b5d168",
      "WRITE",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d148",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d154",
      "PARAM",
      [
        "storage",
        "002a516c",
        null,
        "string"
      ]
    ],
    [
      "00b5d168",
      "WRITE",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d0f4.md#insn-00b5d11c) · [`00b5d124`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d0f4.md#insn-00b5d124) · [`00b5d104`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d0f4.md#insn-00b5d104)
- 新版 `00b5d160`（命令位置の公開資料なし） · `00b5d168`（命令位置の公開資料なし） · `00b5d148`（命令位置の公開資料なし）

~~~diff
- 00b5d11c ["INT_ADD", "register:40f0:8", ["const:b5d11c:8", "const:4:8"]]
- 00b5d11c ["CALL", null, ["callee:00bde090:8"]]
+ 00b5d160 ["INT_ADD", "register:40f0:8", ["const:b5d160:8", "const:4:8"]]
+ 00b5d160 ["CALL", null, ["callee:00bde090:8"]]
- 00b5d11c bytes c9030294
+ 00b5d160 bytes cc030294
- 00b5d124 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00b5d124 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d168 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00b5d168 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d124 bytes 605602f9
+ 00b5d168 bytes 607602f9
- 00b5d104 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4a8:8"]]
- 00b5d104 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d148 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4e8:8"]]
+ 00b5d148 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d104 bytes 685642f9
+ 00b5d148 bytes 687642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1747b51adf32294ee3ca70c35f589eeb"></a>

### [`00b5d144`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d144.md) → [`00b5d188`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d188.md) _ZN8firebase4auth11jnilistener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b5d1e0",
      "incomplete_value": true,
      "site": "00b5d1e0",
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
      "definition_site": "00b5d19c",
      "incomplete_value": true,
      "site": "00b5d19c",
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
      "definition_site": "00b5d1bc",
      "incomplete_value": true,
      "site": "00b5d1c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d178",
      "incomplete_value": true,
      "site": "00b5d184",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b5d19c",
      "READ",
      [
        "storage",
        "010a14b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d1bc",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d1e0",
      "WRITE",
      [
        "storage",
        "010a14b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5d19c",
      "READ",
      [
        "storage",
        "010a14f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d1bc",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d1e0",
      "WRITE",
      [
        "storage",
        "010a14f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d144.md#insn-00b5d158) · [`00b5d184`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d144.md#insn-00b5d184) · [`00b5d19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d144.md#insn-00b5d19c)
- 新版 `00b5d19c`（命令位置の公開資料なし） · `00b5d1c8`（命令位置の公開資料なし） · `00b5d1e0`（命令位置の公開資料なし）

~~~diff
- 00b5d158 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4b0:8"]]
- 00b5d158 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b5d158 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b5d19c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4f0:8"]]
+ 00b5d19c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d19c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b5d158 bytes a8c25239
+ 00b5d19c bytes a8c25339
- 00b5d184 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5d184 ["INT_ADD", "register:40f0:8", ["const:b5d184:8", "const:4:8"]]
- 00b5d184 ["CALLIND", null, ["register:0:8"]]
+ 00b5d1c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5d1c8 ["INT_ADD", "register:40f0:8", ["const:b5d1c8:8", "const:4:8"]]
+ 00b5d1c8 ["CALLIND", null, ["register:0:8"]]
- 00b5d184 bytes 00013fd6
+ 00b5d1c8 bytes 00013fd6
- 00b5d19c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b5d19c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4b0:8"]]
- 00b5d19c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b5d1e0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b5d1e0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4f0:8"]]
+ 00b5d1e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b5d19c bytes a0c21239
+ 00b5d1e0 bytes a0c21339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9dd29b576a719fc9bb3bbac5a12c125"></a>

### [`00b5d1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d1b0.md) → [`00b5d1f4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d1f4.md) _ZN8firebase4auth11jnilistener12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b5d230",
      "incomplete_value": true,
      "site": "00b5d230",
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
      "definition_site": "00b5d1ec",
      "incomplete_value": true,
      "site": "00b5d1ec",
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
      "definition_site": "00b5d250",
      "incomplete_value": true,
      "site": "00b5d250",
      "value": [
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
      "definition_site": "00b5d20c",
      "incomplete_value": true,
      "site": "00b5d20c",
      "value": [
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
      "definition_site": "00b5d20c",
      "incomplete_value": true,
      "site": "00b5d20c",
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
      "definition_site": "00b5d1c8",
      "incomplete_value": true,
      "site": "00b5d1c8",
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
      "00b5d208",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d214",
      "READ",
      [
        "storage",
        "010a14b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d230",
      "WRITE",
      [
        "storage",
        "010a14b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5d208",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d214",
      "READ",
      [
        "storage",
        "010a14f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d230",
      "WRITE",
      [
        "storage",
        "010a14f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d1c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d1b0.md#insn-00b5d1c4) · [`00b5d1ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d1b0.md#insn-00b5d1ec) · [`00b5d208`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d1b0.md#insn-00b5d208)
- 新版 `00b5d208`（命令位置の公開資料なし） · `00b5d230`（命令位置の公開資料なし） · `00b5d24c`（命令位置の公開資料なし）

~~~diff
- 00b5d1c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00b5d1c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d208 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
+ 00b5d208 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d1c4 bytes 815642f9
+ 00b5d208 bytes 817642f9
- 00b5d1ec ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5d1ec ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5d1ec ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4b0:8"]]
- 00b5d1ec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b5d230 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b5d230 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b5d230 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4f0:8"]]
+ 00b5d230 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5d1ec bytes bfc21239
+ 00b5d230 bytes bfc21339
- 00b5d208 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5d208 ["INT_ADD", "register:40f0:8", ["const:b5d208:8", "const:4:8"]]
- 00b5d208 ["CALLIND", null, ["register:0:8"]]
+ 00b5d24c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5d24c ["INT_ADD", "register:40f0:8", ["const:b5d24c:8", "const:4:8"]]
+ 00b5d24c ["CALLIND", null, ["register:0:8"]]
- 00b5d208 bytes 00013fd6
+ 00b5d24c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fbf94b2d9b22284c24ca3c701de0082"></a>

### [`00b5d220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d220.md) → [`00b5d264`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d264.md) _ZN8firebase4auth11jnilistener14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b5d2a4",
      "incomplete_value": true,
      "site": "00b5d2a4",
      "value": [
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
      "definition_site": "00b5d260",
      "incomplete_value": true,
      "site": "00b5d260",
      "value": [
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
      "definition_site": "00b5d280",
      "incomplete_value": true,
      "site": "00b5d280",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d23c",
      "incomplete_value": true,
      "site": "00b5d23c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5d288",
      "incomplete_value": false,
      "site": "00b5d29c",
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
            "const:16c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d244",
      "incomplete_value": false,
      "site": "00b5d258",
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
            "const:e1:8"
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
      "00b5d278",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d288",
      "PARAM",
      [
        "storage",
        "002a50e1",
        null,
        "string"
      ]
    ],
    [
      "00b5d2a4",
      "WRITE",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d278",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d288",
      "PARAM",
      [
        "storage",
        "002a516c",
        null,
        "string"
      ]
    ],
    [
      "00b5d2a4",
      "WRITE",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d220.md#insn-00b5d258) · [`00b5d260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d220.md#insn-00b5d260) · [`00b5d234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d220.md#insn-00b5d234)
- 新版 `00b5d29c`（命令位置の公開資料なし） · `00b5d2a4`（命令位置の公開資料なし） · `00b5d278`（命令位置の公開資料なし）

~~~diff
- 00b5d258 ["INT_ADD", "register:40f0:8", ["const:b5d258:8", "const:4:8"]]
- 00b5d258 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5d29c ["INT_ADD", "register:40f0:8", ["const:b5d29c:8", "const:4:8"]]
+ 00b5d29c ["CALL", null, ["callee:00bde090:8"]]
- 00b5d258 bytes 7a030294
+ 00b5d29c bytes 7d030294
- 00b5d260 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00b5d260 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d2a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
+ 00b5d2a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d260 bytes 805602f9
+ 00b5d2a4 bytes 807602f9
- 00b5d234 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00b5d234 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d278 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
+ 00b5d278 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d234 bytes 815642f9
+ 00b5d278 bytes 817642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-110ce665a1c6070586f9305c5d21df9a"></a>

### [`00b5d290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d290.md) → [`00b5d2d4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d2d4.md) _ZN8firebase4auth11jnilistener11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b5d2f0",
      "incomplete_value": false,
      "site": "00b5d2f4",
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
      "definition_site": "00b5d2ac",
      "incomplete_value": false,
      "site": "00b5d2b0",
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
      "definition_site": "00b5d300",
      "incomplete_value": true,
      "site": "00b5d30c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5d2bc",
      "incomplete_value": true,
      "site": "00b5d2c8",
      "value": [
        "LOAD",
        "8",
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
      "00b5d2f0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b5d300",
      "DATA",
      [
        "storage",
        "010a14b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d2f0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b5d300",
      "DATA",
      [
        "storage",
        "010a14f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d2b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d290.md#insn-00b5d2b0) · [`00b5d2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d290.md#insn-00b5d2ac) · [`00b5d2b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d290.md#insn-00b5d2b8)
- 新版 `00b5d2f4`（命令位置の公開資料なし） · `00b5d2f0`（命令位置の公開資料なし） · `00b5d2fc`（命令位置の公開資料なし）

~~~diff
- 00b5d2b0 ["INT_ADD", "register:40f0:8", ["const:b5d2b0:8", "const:4:8"]]
- 00b5d2b0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5d2f4 ["INT_ADD", "register:40f0:8", ["const:b5d2f4:8", "const:4:8"]]
+ 00b5d2f4 ["CALL", null, ["callee:00bde180:8"]]
- 00b5d2b0 bytes a0030294
+ 00b5d2f4 bytes a3030294
- 00b5d2ac ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b5d2ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d2ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d2ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5d2f0 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b5d2f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d2f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d2f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5d2ac bytes 00501791
+ 00b5d2f0 bytes 001c1591
- 00b5d2b8 ["COPY", "tmp:0:8", ["const:4b8:8"]]
- 00b5d2b8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d2b8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d2b8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5d2fc ["COPY", "tmp:0:8", ["const:4f8:8"]]
+ 00b5d2fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d2fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d2fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5d2b8 bytes 08e11291
+ 00b5d2fc bytes 08e11391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-982f31b8e62e9fc4cedc71c094cfc569"></a>

### [`00b5d2cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d2cc.md) → [`00b5d310`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d310.md) _ZN8firebase4auth11jnilistener13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b5d350",
      "incomplete_value": true,
      "site": "00b5d350",
      "value": [
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
      "definition_site": "00b5d30c",
      "incomplete_value": true,
      "site": "00b5d30c",
      "value": [
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
      "definition_site": "00b5d32c",
      "incomplete_value": true,
      "site": "00b5d32c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d2e8",
      "incomplete_value": true,
      "site": "00b5d2e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5d334",
      "incomplete_value": false,
      "site": "00b5d348",
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
            "const:16c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d2f0",
      "incomplete_value": false,
      "site": "00b5d304",
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
            "const:e1:8"
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
      "00b5d324",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d334",
      "PARAM",
      [
        "storage",
        "002a50e1",
        null,
        "string"
      ]
    ],
    [
      "00b5d350",
      "WRITE",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d324",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d334",
      "PARAM",
      [
        "storage",
        "002a516c",
        null,
        "string"
      ]
    ],
    [
      "00b5d350",
      "WRITE",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d304`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d2cc.md#insn-00b5d304) · [`00b5d30c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d2cc.md#insn-00b5d30c) · [`00b5d2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d2cc.md#insn-00b5d2e0)
- 新版 `00b5d348`（命令位置の公開資料なし） · `00b5d350`（命令位置の公開資料なし） · `00b5d324`（命令位置の公開資料なし）

~~~diff
- 00b5d304 ["INT_ADD", "register:40f0:8", ["const:b5d304:8", "const:4:8"]]
- 00b5d304 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5d348 ["INT_ADD", "register:40f0:8", ["const:b5d348:8", "const:4:8"]]
+ 00b5d348 ["CALL", null, ["callee:00bde090:8"]]
- 00b5d304 bytes 4f030294
+ 00b5d348 bytes 52030294
- 00b5d30c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00b5d30c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d350 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
+ 00b5d350 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d30c bytes 805602f9
+ 00b5d350 bytes 807602f9
- 00b5d2e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a8:8"]]
- 00b5d2e0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d324 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4e8:8"]]
+ 00b5d324 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d2e0 bytes 815642f9
+ 00b5d324 bytes 817642f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-49a49d3cf851ab02c583f3ba7ab2337a"></a>

### [`00b5d33c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d33c.md) → [`00b5d380`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d380.md) _ZN8firebase4auth11jnilistener10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b5d39c",
      "incomplete_value": false,
      "site": "00b5d3a0",
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
      "definition_site": "00b5d358",
      "incomplete_value": false,
      "site": "00b5d35c",
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
      "definition_site": "00b5d3ac",
      "incomplete_value": true,
      "site": "00b5d3b8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5d368",
      "incomplete_value": true,
      "site": "00b5d374",
      "value": [
        "LOAD",
        "8",
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
      "00b5d39c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b5d3ac",
      "DATA",
      [
        "storage",
        "010a14c8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5d39c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b5d3ac",
      "DATA",
      [
        "storage",
        "010a1508",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d33c.md#insn-00b5d35c) · [`00b5d358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d33c.md#insn-00b5d358) · [`00b5d364`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d33c.md#insn-00b5d364)
- 新版 `00b5d3a0`（命令位置の公開資料なし） · `00b5d39c`（命令位置の公開資料なし） · `00b5d3a8`（命令位置の公開資料なし）

~~~diff
- 00b5d35c ["INT_ADD", "register:40f0:8", ["const:b5d35c:8", "const:4:8"]]
- 00b5d35c ["CALL", null, ["callee:00bde180:8"]]
+ 00b5d3a0 ["INT_ADD", "register:40f0:8", ["const:b5d3a0:8", "const:4:8"]]
+ 00b5d3a0 ["CALL", null, ["callee:00bde180:8"]]
- 00b5d35c bytes 75030294
+ 00b5d3a0 bytes 78030294
- 00b5d358 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b5d358 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d358 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d358 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5d39c ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b5d39c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d39c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d39c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5d358 bytes 00fc1991
+ 00b5d39c bytes 00c81791
- 00b5d364 ["COPY", "tmp:0:8", ["const:4c8:8"]]
- 00b5d364 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d364 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d364 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5d3a8 ["COPY", "tmp:0:8", ["const:508:8"]]
+ 00b5d3a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d3a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d3a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5d364 bytes 08211391
+ 00b5d3a8 bytes 08211491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7afd36a52ca7e2ff6bdea47cafe95d3e"></a>

### [`00b5d378`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d378.md) → [`00b5d3bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d3bc.md) _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b5d3e8",
      "incomplete_value": true,
      "site": "00b5d3e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d3a4",
      "incomplete_value": true,
      "site": "00b5d3a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "definition_site": "00b5d3d0",
      "incomplete_value": true,
      "site": "00b5d3d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d38c",
      "incomplete_value": true,
      "site": "00b5d38c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5d3dc",
      "incomplete_value": false,
      "site": "00b5d3e0",
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
            "const:8dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d398",
      "incomplete_value": false,
      "site": "00b5d39c",
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
            "const:8de:8"
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
      "00b5d3cc",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d3dc",
      "PARAM",
      [
        "storage",
        "0029a8de",
        null,
        "string"
      ]
    ],
    [
      "00b5d3e8",
      "WRITE",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d3cc",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d3dc",
      "PARAM",
      [
        "storage",
        "0029a8dc",
        null,
        "string"
      ]
    ],
    [
      "00b5d3e8",
      "WRITE",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d378.md#insn-00b5d39c) · [`00b5d3a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d378.md#insn-00b5d3a4) · [`00b5d388`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d378.md#insn-00b5d388)
- 新版 `00b5d3e0`（命令位置の公開資料なし） · `00b5d3e8`（命令位置の公開資料なし） · `00b5d3cc`（命令位置の公開資料なし）

~~~diff
- 00b5d39c ["INT_ADD", "register:40f0:8", ["const:b5d39c:8", "const:4:8"]]
- 00b5d39c ["CALL", null, ["callee:00bde090:8"]]
+ 00b5d3e0 ["INT_ADD", "register:40f0:8", ["const:b5d3e0:8", "const:4:8"]]
+ 00b5d3e0 ["CALL", null, ["callee:00bde090:8"]]
- 00b5d39c bytes 29030294
+ 00b5d3e0 bytes 2c030294
- 00b5d3a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d0:8"]]
- 00b5d3a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d3e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:510:8"]]
+ 00b5d3e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d3a4 bytes 606a02f9
+ 00b5d3e8 bytes 608a02f9
- 00b5d388 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d0:8"]]
- 00b5d388 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d3cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:510:8"]]
+ 00b5d3cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d388 bytes 686a42f9
+ 00b5d3cc bytes 688a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3503c59e60ec42c4745eacd6f227b89f"></a>

### [`00b5d3b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d3b8.md) → [`00b5d3fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d3fc.md) _ZN8firebase4auth21jni_id_token_listener19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b5d428",
      "incomplete_value": true,
      "site": "00b5d428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d3e4",
      "incomplete_value": true,
      "site": "00b5d3e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "definition_site": "00b5d410",
      "incomplete_value": true,
      "site": "00b5d410",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d3cc",
      "incomplete_value": true,
      "site": "00b5d3cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5d418",
      "incomplete_value": false,
      "site": "00b5d420",
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
            "const:8dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d3d4",
      "incomplete_value": false,
      "site": "00b5d3dc",
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
            "const:8de:8"
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
      "00b5d40c",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d418",
      "PARAM",
      [
        "storage",
        "0029a8de",
        null,
        "string"
      ]
    ],
    [
      "00b5d428",
      "WRITE",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d40c",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d418",
      "PARAM",
      [
        "storage",
        "0029a8dc",
        null,
        "string"
      ]
    ],
    [
      "00b5d428",
      "WRITE",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d3dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d3b8.md#insn-00b5d3dc) · [`00b5d3e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d3b8.md#insn-00b5d3e4) · [`00b5d3c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d3b8.md#insn-00b5d3c8)
- 新版 `00b5d420`（命令位置の公開資料なし） · `00b5d428`（命令位置の公開資料なし） · `00b5d40c`（命令位置の公開資料なし）

~~~diff
- 00b5d3dc ["INT_ADD", "register:40f0:8", ["const:b5d3dc:8", "const:4:8"]]
- 00b5d3dc ["CALL", null, ["callee:00bde090:8"]]
+ 00b5d420 ["INT_ADD", "register:40f0:8", ["const:b5d420:8", "const:4:8"]]
+ 00b5d420 ["CALL", null, ["callee:00bde090:8"]]
- 00b5d3dc bytes 19030294
+ 00b5d420 bytes 1c030294
- 00b5d3e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d0:8"]]
- 00b5d3e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d428 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:510:8"]]
+ 00b5d428 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d3e4 bytes 606a02f9
+ 00b5d428 bytes 608a02f9
- 00b5d3c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d0:8"]]
- 00b5d3c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d40c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:510:8"]]
+ 00b5d40c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d3c8 bytes 686a42f9
+ 00b5d40c bytes 688a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-562ad6840d290f2141262cd30fc3fe62"></a>

### [`00b5d3f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d3f8.md) → [`00b5d43c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d43c.md) _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b5d46c",
      "incomplete_value": true,
      "site": "00b5d46c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d428",
      "incomplete_value": true,
      "site": "00b5d428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "definition_site": "00b5d450",
      "incomplete_value": true,
      "site": "00b5d450",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d40c",
      "incomplete_value": true,
      "site": "00b5d40c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5d45c",
      "incomplete_value": false,
      "site": "00b5d464",
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
            "const:8dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d418",
      "incomplete_value": false,
      "site": "00b5d420",
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
            "const:8de:8"
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
      "00b5d44c",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d45c",
      "PARAM",
      [
        "storage",
        "0029a8de",
        null,
        "string"
      ]
    ],
    [
      "00b5d46c",
      "WRITE",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d44c",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d45c",
      "PARAM",
      [
        "storage",
        "0029a8dc",
        null,
        "string"
      ]
    ],
    [
      "00b5d46c",
      "WRITE",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d420`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d3f8.md#insn-00b5d420) · [`00b5d428`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d3f8.md#insn-00b5d428) · [`00b5d408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d3f8.md#insn-00b5d408)
- 新版 `00b5d464`（命令位置の公開資料なし） · `00b5d46c`（命令位置の公開資料なし） · `00b5d44c`（命令位置の公開資料なし）

~~~diff
- 00b5d420 ["INT_ADD", "register:40f0:8", ["const:b5d420:8", "const:4:8"]]
- 00b5d420 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5d464 ["INT_ADD", "register:40f0:8", ["const:b5d464:8", "const:4:8"]]
+ 00b5d464 ["CALL", null, ["callee:00bde090:8"]]
- 00b5d420 bytes 08030294
+ 00b5d464 bytes 0b030294
- 00b5d428 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d0:8"]]
- 00b5d428 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d46c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:510:8"]]
+ 00b5d46c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d428 bytes 606a02f9
+ 00b5d46c bytes 608a02f9
- 00b5d408 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d0:8"]]
- 00b5d408 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d44c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:510:8"]]
+ 00b5d44c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d408 bytes 686a42f9
+ 00b5d44c bytes 688a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2818ee32137717107827436c9804f1d7"></a>

### [`00b5d43c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d43c.md) → [`00b5d480`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d480.md) _ZN8firebase4auth21jni_id_token_listener10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b5d4b0",
      "incomplete_value": true,
      "site": "00b5d4b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d46c",
      "incomplete_value": true,
      "site": "00b5d46c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "definition_site": "00b5d494",
      "incomplete_value": true,
      "site": "00b5d494",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d450",
      "incomplete_value": true,
      "site": "00b5d450",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5d49c",
      "incomplete_value": false,
      "site": "00b5d4a8",
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
            "const:8dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d458",
      "incomplete_value": false,
      "site": "00b5d464",
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
            "const:8de:8"
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
      "00b5d490",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d49c",
      "PARAM",
      [
        "storage",
        "0029a8de",
        null,
        "string"
      ]
    ],
    [
      "00b5d4b0",
      "WRITE",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d490",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d49c",
      "PARAM",
      [
        "storage",
        "0029a8dc",
        null,
        "string"
      ]
    ],
    [
      "00b5d4b0",
      "WRITE",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d464`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d43c.md#insn-00b5d464) · [`00b5d46c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d43c.md#insn-00b5d46c) · [`00b5d44c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d43c.md#insn-00b5d44c)
- 新版 `00b5d4a8`（命令位置の公開資料なし） · `00b5d4b0`（命令位置の公開資料なし） · `00b5d490`（命令位置の公開資料なし）

~~~diff
- 00b5d464 ["INT_ADD", "register:40f0:8", ["const:b5d464:8", "const:4:8"]]
- 00b5d464 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5d4a8 ["INT_ADD", "register:40f0:8", ["const:b5d4a8:8", "const:4:8"]]
+ 00b5d4a8 ["CALL", null, ["callee:00bde090:8"]]
- 00b5d464 bytes f7020294
+ 00b5d4a8 bytes fa020294
- 00b5d46c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d0:8"]]
- 00b5d46c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d4b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:510:8"]]
+ 00b5d4b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d46c bytes 606a02f9
+ 00b5d4b0 bytes 608a02f9
- 00b5d44c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:4d0:8"]]
- 00b5d44c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d490 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:510:8"]]
+ 00b5d490 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d44c bytes 686a42f9
+ 00b5d490 bytes 688a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2ef9f428ce9dd5eaaee0f81eaba5a44d"></a>

### [`00b5d48c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d48c.md) → [`00b5d4d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d4d0.md) _ZN8firebase4auth21jni_id_token_listener15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b5d528",
      "incomplete_value": true,
      "site": "00b5d528",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d4e4",
      "incomplete_value": true,
      "site": "00b5d4e4",
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
            "const:4d8:8"
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
      "definition_site": "00b5d504",
      "incomplete_value": true,
      "site": "00b5d510",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:510:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d4c0",
      "incomplete_value": true,
      "site": "00b5d4cc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4d0:8"
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
      "00b5d4e4",
      "READ",
      [
        "storage",
        "010a14d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d504",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d528",
      "WRITE",
      [
        "storage",
        "010a14d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5d4e4",
      "READ",
      [
        "storage",
        "010a1518",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d504",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d528",
      "WRITE",
      [
        "storage",
        "010a1518",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d48c.md#insn-00b5d4a0) · [`00b5d4cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d48c.md#insn-00b5d4cc) · [`00b5d4e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d48c.md#insn-00b5d4e4)
- 新版 `00b5d4e4`（命令位置の公開資料なし） · `00b5d510`（命令位置の公開資料なし） · `00b5d528`（命令位置の公開資料なし）

~~~diff
- 00b5d4a0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:4d8:8"]]
- 00b5d4a0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b5d4a0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b5d4e4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:518:8"]]
+ 00b5d4e4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d4e4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b5d4a0 bytes a8625339
+ 00b5d4e4 bytes a8625439
- 00b5d4cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5d4cc ["INT_ADD", "register:40f0:8", ["const:b5d4cc:8", "const:4:8"]]
- 00b5d4cc ["CALLIND", null, ["register:0:8"]]
+ 00b5d510 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5d510 ["INT_ADD", "register:40f0:8", ["const:b5d510:8", "const:4:8"]]
+ 00b5d510 ["CALLIND", null, ["register:0:8"]]
- 00b5d4cc bytes 00013fd6
+ 00b5d510 bytes 00013fd6
- 00b5d4e4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b5d4e4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:4d8:8"]]
- 00b5d4e4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b5d528 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b5d528 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:518:8"]]
+ 00b5d528 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b5d4e4 bytes a0621339
+ 00b5d528 bytes a0621439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec095d6e927b56cf03eeb805878340ef"></a>

### [`00b5d4f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d4f8.md) → [`00b5d53c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d53c.md) _ZN8firebase4auth21jni_id_token_listener12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b5d578",
      "incomplete_value": true,
      "site": "00b5d578",
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
            "const:518:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d534",
      "incomplete_value": true,
      "site": "00b5d534",
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
            "const:4d8:8"
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
      "definition_site": "00b5d598",
      "incomplete_value": true,
      "site": "00b5d598",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d554",
      "incomplete_value": true,
      "site": "00b5d554",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "definition_site": "00b5d554",
      "incomplete_value": true,
      "site": "00b5d554",
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
      "definition_site": "00b5d510",
      "incomplete_value": true,
      "site": "00b5d510",
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
      "00b5d550",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d55c",
      "READ",
      [
        "storage",
        "010a14d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d578",
      "WRITE",
      [
        "storage",
        "010a14d8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5d550",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d55c",
      "READ",
      [
        "storage",
        "010a1518",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d578",
      "WRITE",
      [
        "storage",
        "010a1518",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d50c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d4f8.md#insn-00b5d50c) · [`00b5d534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d4f8.md#insn-00b5d534) · [`00b5d550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d4f8.md#insn-00b5d550)
- 新版 `00b5d550`（命令位置の公開資料なし） · `00b5d578`（命令位置の公開資料なし） · `00b5d594`（命令位置の公開資料なし）

~~~diff
- 00b5d50c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4d0:8"]]
- 00b5d50c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d550 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:510:8"]]
+ 00b5d550 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d50c bytes 816a42f9
+ 00b5d550 bytes 818a42f9
- 00b5d534 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5d534 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5d534 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4d8:8"]]
- 00b5d534 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b5d578 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b5d578 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b5d578 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:518:8"]]
+ 00b5d578 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5d534 bytes bf621339
+ 00b5d578 bytes bf621439
- 00b5d550 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5d550 ["INT_ADD", "register:40f0:8", ["const:b5d550:8", "const:4:8"]]
- 00b5d550 ["CALLIND", null, ["register:0:8"]]
+ 00b5d594 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5d594 ["INT_ADD", "register:40f0:8", ["const:b5d594:8", "const:4:8"]]
+ 00b5d594 ["CALLIND", null, ["register:0:8"]]
- 00b5d550 bytes 00013fd6
+ 00b5d594 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab12d4c4bc1375189462ab1bccf39e4f"></a>

### [`00b5d568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d568.md) → [`00b5d5ac`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d5ac.md) _ZN8firebase4auth21jni_id_token_listener14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b5d5ec",
      "incomplete_value": true,
      "site": "00b5d5ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d5a8",
      "incomplete_value": true,
      "site": "00b5d5a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "definition_site": "00b5d5d0",
      "incomplete_value": false,
      "site": "00b5d5e4",
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
            "const:8dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d58c",
      "incomplete_value": false,
      "site": "00b5d5a0",
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
            "const:8de:8"
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
      "00b5d5c0",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d5d0",
      "PARAM",
      [
        "storage",
        "0029a8de",
        null,
        "string"
      ]
    ],
    [
      "00b5d5ec",
      "WRITE",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d5c0",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d5d0",
      "PARAM",
      [
        "storage",
        "0029a8dc",
        null,
        "string"
      ]
    ],
    [
      "00b5d5ec",
      "WRITE",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d568.md#insn-00b5d5a0) · [`00b5d5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d568.md#insn-00b5d5a8) · [`00b5d57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d568.md#insn-00b5d57c)
- 新版 `00b5d5e4`（命令位置の公開資料なし） · `00b5d5ec`（命令位置の公開資料なし） · `00b5d5c0`（命令位置の公開資料なし）

~~~diff
- 00b5d5a0 ["INT_ADD", "register:40f0:8", ["const:b5d5a0:8", "const:4:8"]]
- 00b5d5a0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5d5e4 ["INT_ADD", "register:40f0:8", ["const:b5d5e4:8", "const:4:8"]]
+ 00b5d5e4 ["CALL", null, ["callee:00bde090:8"]]
- 00b5d5a0 bytes a8020294
+ 00b5d5e4 bytes ab020294
- 00b5d5a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4d0:8"]]
- 00b5d5a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d5ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:510:8"]]
+ 00b5d5ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d5a8 bytes 806a02f9
+ 00b5d5ec bytes 808a02f9
- 00b5d57c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4d0:8"]]
- 00b5d57c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d5c0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:510:8"]]
+ 00b5d5c0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d57c bytes 816a42f9
+ 00b5d5c0 bytes 818a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1fdf68675bdf09614b264e7dc49a028f"></a>

### [`00b5d5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d5d8.md) → [`00b5d61c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d61c.md) _ZN8firebase4auth21jni_id_token_listener11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b5d638",
      "incomplete_value": false,
      "site": "00b5d63c",
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
      "definition_site": "00b5d5f4",
      "incomplete_value": false,
      "site": "00b5d5f8",
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
      "definition_site": "00b5d648",
      "incomplete_value": true,
      "site": "00b5d654",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5d604",
      "incomplete_value": true,
      "site": "00b5d610",
      "value": [
        "LOAD",
        "8",
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
      "00b5d638",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b5d648",
      "DATA",
      [
        "storage",
        "010a14e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d638",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b5d648",
      "DATA",
      [
        "storage",
        "010a1520",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d5f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d5d8.md#insn-00b5d5f8) · [`00b5d5f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d5d8.md#insn-00b5d5f4) · [`00b5d600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d5d8.md#insn-00b5d600)
- 新版 `00b5d63c`（命令位置の公開資料なし） · `00b5d638`（命令位置の公開資料なし） · `00b5d644`（命令位置の公開資料なし）

~~~diff
- 00b5d5f8 ["INT_ADD", "register:40f0:8", ["const:b5d5f8:8", "const:4:8"]]
- 00b5d5f8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5d63c ["INT_ADD", "register:40f0:8", ["const:b5d63c:8", "const:4:8"]]
+ 00b5d63c ["CALL", null, ["callee:00bde180:8"]]
- 00b5d5f8 bytes ce020294
+ 00b5d63c bytes d1020294
- 00b5d5f4 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b5d5f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d5f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d5f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5d638 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b5d638 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d638 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d638 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5d5f4 bytes 00501791
+ 00b5d638 bytes 001c1591
- 00b5d600 ["COPY", "tmp:0:8", ["const:4e0:8"]]
- 00b5d600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5d644 ["COPY", "tmp:0:8", ["const:520:8"]]
+ 00b5d644 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d644 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d644 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5d600 bytes 08811391
+ 00b5d644 bytes 08811491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1380899e6796be9c52fde7ff7b9c2e67"></a>

### [`00b5d614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d614.md) → [`00b5d658`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d658.md) _ZN8firebase4auth21jni_id_token_listener13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b5d698",
      "incomplete_value": true,
      "site": "00b5d698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d654",
      "incomplete_value": true,
      "site": "00b5d654",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4d0:8"
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
      "definition_site": "00b5d674",
      "incomplete_value": true,
      "site": "00b5d674",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d630",
      "incomplete_value": true,
      "site": "00b5d630",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b5d67c",
      "incomplete_value": false,
      "site": "00b5d690",
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
            "const:8dc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d638",
      "incomplete_value": false,
      "site": "00b5d64c",
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
            "const:8de:8"
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
      "00b5d66c",
      "READ",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d67c",
      "PARAM",
      [
        "storage",
        "0029a8de",
        null,
        "string"
      ]
    ],
    [
      "00b5d698",
      "WRITE",
      [
        "storage",
        "010a14d0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d66c",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d67c",
      "PARAM",
      [
        "storage",
        "0029a8dc",
        null,
        "string"
      ]
    ],
    [
      "00b5d698",
      "WRITE",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d64c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d614.md#insn-00b5d64c) · [`00b5d654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d614.md#insn-00b5d654) · [`00b5d628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d614.md#insn-00b5d628)
- 新版 `00b5d690`（命令位置の公開資料なし） · `00b5d698`（命令位置の公開資料なし） · `00b5d66c`（命令位置の公開資料なし）

~~~diff
- 00b5d64c ["INT_ADD", "register:40f0:8", ["const:b5d64c:8", "const:4:8"]]
- 00b5d64c ["CALL", null, ["callee:00bde090:8"]]
+ 00b5d690 ["INT_ADD", "register:40f0:8", ["const:b5d690:8", "const:4:8"]]
+ 00b5d690 ["CALL", null, ["callee:00bde090:8"]]
- 00b5d64c bytes 7d020294
+ 00b5d690 bytes 80020294
- 00b5d654 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4d0:8"]]
- 00b5d654 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d698 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:510:8"]]
+ 00b5d698 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d654 bytes 806a02f9
+ 00b5d698 bytes 808a02f9
- 00b5d628 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4d0:8"]]
- 00b5d628 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d66c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:510:8"]]
+ 00b5d66c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d628 bytes 816a42f9
+ 00b5d66c bytes 818a42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a79e7da3aabfe14e97ee00f10569396"></a>

### [`00b5d684`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d684.md) → [`00b5d6c8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d6c8.md) _ZN8firebase4auth21jni_id_token_listener10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b5d6e4",
      "incomplete_value": false,
      "site": "00b5d6e8",
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
      "definition_site": "00b5d6a0",
      "incomplete_value": false,
      "site": "00b5d6a4",
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
      "definition_site": "00b5d6f4",
      "incomplete_value": true,
      "site": "00b5d700",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b5d6b0",
      "incomplete_value": true,
      "site": "00b5d6bc",
      "value": [
        "LOAD",
        "8",
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
      "00b5d6e4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b5d6f4",
      "DATA",
      [
        "storage",
        "010a14f0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5d6e4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b5d6f4",
      "DATA",
      [
        "storage",
        "010a1530",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d6a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d684.md#insn-00b5d6a4) · [`00b5d6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d684.md#insn-00b5d6a0) · [`00b5d6ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d684.md#insn-00b5d6ac)
- 新版 `00b5d6e8`（命令位置の公開資料なし） · `00b5d6e4`（命令位置の公開資料なし） · `00b5d6f0`（命令位置の公開資料なし）

~~~diff
- 00b5d6a4 ["INT_ADD", "register:40f0:8", ["const:b5d6a4:8", "const:4:8"]]
- 00b5d6a4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5d6e8 ["INT_ADD", "register:40f0:8", ["const:b5d6e8:8", "const:4:8"]]
+ 00b5d6e8 ["CALL", null, ["callee:00bde180:8"]]
- 00b5d6a4 bytes a3020294
+ 00b5d6e8 bytes a6020294
- 00b5d6a0 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b5d6a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d6a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5d6a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5d6e4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b5d6e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d6e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5d6e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5d6a0 bytes 00fc1991
+ 00b5d6e4 bytes 00c81791
- 00b5d6ac ["COPY", "tmp:0:8", ["const:4f0:8"]]
- 00b5d6ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d6ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b5d6ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b5d6f0 ["COPY", "tmp:0:8", ["const:530:8"]]
+ 00b5d6f0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d6f0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b5d6f0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b5d6ac bytes 08c11391
+ 00b5d6f0 bytes 08c11491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-073afaa7a3c506cfd9475afb5e637e83"></a>

### [`00b5d6c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d6c0.md) → [`00b5d704`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d704.md) _ZN8firebase4auth18CacheAuthMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0bf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0bf0.md) · 呼出先 3件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 1件 [`00be0c40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c40.md) · 呼出先 3件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 81.43% / 新版 81.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 16件, `store_condition` 1件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 3件, `call_argument_candidate` 1件, `store_condition` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d750",
      "incomplete_value": true,
      "site": "00b5d750",
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
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d70c",
      "incomplete_value": true,
      "site": "00b5d70c",
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
            "const:3e0:8"
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
      "definition_site": "00b5d7a8",
      "incomplete_value": true,
      "site": "00b5d7a8",
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
            "const:4c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d764",
      "incomplete_value": true,
      "site": "00b5d764",
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
            "const:488:8"
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
      "definition_site": "00b5d800",
      "incomplete_value": true,
      "site": "00b5d800",
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
            "const:4e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d7bc",
      "incomplete_value": true,
      "site": "00b5d7bc",
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
            "const:4a8:8"
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
      "00b5d720",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d734",
      "PARAM",
      [
        "storage",
        "0029bfd8",
        null,
        "string"
      ]
    ],
    [
      "00b5d750",
      "WRITE",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5d720",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d734",
      "PARAM",
      [
        "storage",
        "0029bfd6",
        null,
        "string"
      ]
    ],
    [
      "00b5d750",
      "WRITE",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d6c0.md#insn-00b5d704) · [`00b5d70c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d6c0.md#insn-00b5d70c) · [`00b5d720`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d6c0.md#insn-00b5d720)
- 新版 `00b5d748`（命令位置の公開資料なし） · `00b5d750`（命令位置の公開資料なし） · `00b5d764`（命令位置の公開資料なし）

~~~diff
- 00b5d704 ["INT_ADD", "register:40f0:8", ["const:b5d704:8", "const:4:8"]]
- 00b5d704 ["CALL", null, ["callee:00bde090:8"]]
+ 00b5d748 ["INT_ADD", "register:40f0:8", ["const:b5d748:8", "const:4:8"]]
+ 00b5d748 ["CALL", null, ["callee:00bde090:8"]]
- 00b5d704 bytes 4f020294
+ 00b5d748 bytes 52020294
- 00b5d70c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:3e0:8"]]
- 00b5d70c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b5d750 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:420:8"]]
+ 00b5d750 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b5d70c bytes c0f201f9
+ 00b5d750 bytes c01202f9
- 00b5d720 ["COPY", "tmp:0:8", ["const:3f0:8"]]
- 00b5d720 ["INT_CARRY", "register:105:1", ["register:4020:8", "tmp:0:8"]]
- 00b5d720 ["INT_SCARRY", "register:106:1", ["register:4020:8", "tmp:0:8"]]
- 00b5d720 ["INT_ADD", "tmp:1:8", ["register:4020:8", "tmp:0:8"]]
+ 00b5d764 ["COPY", "tmp:0:8", ["const:430:8"]]
+ 00b5d764 ["INT_CARRY", "register:105:1", ["register:4020:8", "tmp:0:8"]]
+ 00b5d764 ["INT_SCARRY", "register:106:1", ["register:4020:8", "tmp:0:8"]]
+ 00b5d764 ["INT_ADD", "tmp:1:8", ["register:4020:8", "tmp:0:8"]]
- 00b5d720 bytes 84c00f91
+ 00b5d764 bytes 84c01091
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a8f26d715b137ebe78940c1ced2ef8c"></a>

### [`00b5d8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d8f0.md) → [`00b5d934`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5d934.md) _ZN8firebase4auth18ReleaseAuthClassesEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0c10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c10.md) · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 1件 [`00be0c60`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c60.md) · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 84.71% / 新版 84.71%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 4件, `store_destination` 8件

アドレスに依存する影響 `branch_value` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5d970",
      "incomplete_value": true,
      "site": "00b5d970",
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
            "const:428:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d92c",
      "incomplete_value": true,
      "site": "00b5d92c",
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
            "const:3e8:8"
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
      "definition_site": "00b5d990",
      "incomplete_value": true,
      "site": "00b5d990",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:420:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5d94c",
      "incomplete_value": true,
      "site": "00b5d94c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:3e0:8"
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
      "definition_site": "00b5d9bc",
      "incomplete_value": true,
      "site": "00b5d9bc",
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
    "old": {
      "definition_site": "00b5d978",
      "incomplete_value": true,
      "site": "00b5d978",
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
            "const:490:8"
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
      "00b5d948",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d958",
      "READ",
      [
        "storage",
        "010a13e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d970",
      "WRITE",
      [
        "storage",
        "010a13e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b5d948",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5d958",
      "READ",
      [
        "storage",
        "010a1428",
        null,
        "undefined1"
      ]
    ],
    [
      "00b5d970",
      "WRITE",
      [
        "storage",
        "010a1428",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5d904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d8f0.md#insn-00b5d904) · [`00b5d914`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d8f0.md#insn-00b5d914) · [`00b5d92c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5d8f0.md#insn-00b5d92c)
- 新版 `00b5d948`（命令位置の公開資料なし） · `00b5d958`（命令位置の公開資料なし） · `00b5d970`（命令位置の公開資料なし）

~~~diff
- 00b5d904 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:3e0:8"]]
- 00b5d904 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d948 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:420:8"]]
+ 00b5d948 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5d904 bytes 81f241f9
+ 00b5d948 bytes 811242f9
- 00b5d914 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:3e8:8"]]
- 00b5d914 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b5d914 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b5d958 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:428:8"]]
+ 00b5d958 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b5d958 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b5d914 bytes a8a24f39
+ 00b5d958 bytes a8a25039
- 00b5d92c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b5d92c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b5d92c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:3e8:8"]]
- 00b5d92c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b5d970 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b5d970 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b5d970 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:428:8"]]
+ 00b5d970 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b5d92c bytes bfa20f39
+ 00b5d970 bytes bfa21039
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e359bb4864ce14e40521e3b2c90b2558"></a>

### [`00b5da44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5da44.md) → [`00b5da88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5da88.md) _ZN8firebase4auth17UpdateCurrentUserEPNS0_8AuthDataE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be0be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0be0.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 1件 [`00be0c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c30.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.50% / 新版 97.50%

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
      "definition_site": "00b5dac0",
      "incomplete_value": true,
      "site": "00b5dac8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:438:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5da7c",
      "incomplete_value": true,
      "site": "00b5da84",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f8:8"
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
      "definition_site": "00b5db00",
      "incomplete_value": false,
      "site": "00b5db08",
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
            "const:fa7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5dabc",
      "incomplete_value": false,
      "site": "00b5dac4",
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
            "const:f0d:8"
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
      "00b5dac0",
      "READ",
      [
        "storage",
        "010a13f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5db00",
      "PARAM",
      [
        "storage",
        "002a7f0d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5dac0",
      "READ",
      [
        "storage",
        "010a1438",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5db00",
      "PARAM",
      [
        "storage",
        "002a7fa7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5da84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5da44.md#insn-00b5da84) · [`00b5dac4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5da44.md#insn-00b5dac4) · [`00b5da60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5da44.md#insn-00b5da60)
- 新版 `00b5dac8`（命令位置の公開資料なし） · `00b5db08`（命令位置の公開資料なし） · `00b5daa4`（命令位置の公開資料なし）

~~~diff
- 00b5da84 ["INT_ADD", "register:40f0:8", ["const:b5da84:8", "const:4:8"]]
- 00b5da84 ["CALL", null, ["callee:0047495c:8"]]
+ 00b5dac8 ["INT_ADD", "register:40f0:8", ["const:b5dac8:8", "const:4:8"]]
+ 00b5dac8 ["CALL", null, ["callee:0047495c:8"]]
- 00b5da84 bytes b65be497
+ 00b5dac8 bytes a55be497
- 00b5dac4 ["INT_ADD", "register:40f0:8", ["const:b5dac4:8", "const:4:8"]]
- 00b5dac4 ["CALL", null, ["callee:00bde2b0:8"]]
+ 00b5db08 ["INT_ADD", "register:40f0:8", ["const:b5db08:8", "const:4:8"]]
+ 00b5db08 ["CALL", null, ["callee:00bde2b0:8"]]
- 00b5dac4 bytes e7010294
+ 00b5db08 bytes ea010294
- 00b5da60 ["INT_ADD", "register:40f0:8", ["const:b5da60:8", "const:4:8"]]
- 00b5da60 ["CALL", null, ["callee:00bde200:8"]]
+ 00b5daa4 ["INT_ADD", "register:40f0:8", ["const:b5daa4:8", "const:4:8"]]
+ 00b5daa4 ["CALL", null, ["callee:00bde200:8"]]
- 00b5da60 bytes d4010294
+ 00b5daa4 bytes d7010294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c45549e2f5287981f8387b136d87731d"></a>

### [`00b5db00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5db00.md) → [`00b5db44`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5db44.md) _ZN8firebase4auth14SetEmulatorJniEPNS0_8AuthDataEPKcj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

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
      "definition_site": "00b5db84",
      "incomplete_value": true,
      "site": "00b5db98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:480:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5db40",
      "incomplete_value": true,
      "site": "00b5db54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:440:8"
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
      "00b5db84",
      "READ",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5db84",
      "READ",
      [
        "storage",
        "010a1480",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5db54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5db00.md#insn-00b5db54) · [`00b5db20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5db00.md#insn-00b5db20) · [`00b5db34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5db00.md#insn-00b5db34)
- 新版 `00b5db98`（命令位置の公開資料なし） · `00b5db64`（命令位置の公開資料なし） · `00b5db78`（命令位置の公開資料なし）

~~~diff
- 00b5db54 ["INT_ADD", "register:40f0:8", ["const:b5db54:8", "const:4:8"]]
- 00b5db54 ["CALL", null, ["callee:00551e14:8"]]
+ 00b5db98 ["INT_ADD", "register:40f0:8", ["const:b5db98:8", "const:4:8"]]
+ 00b5db98 ["CALL", null, ["callee:00551e14:8"]]
- 00b5db54 bytes b0d0e797
+ 00b5db98 bytes 9fd0e797
- 00b5db20 ["INT_ADD", "register:40f0:8", ["const:b5db20:8", "const:4:8"]]
- 00b5db20 ["CALL", null, ["callee:00bde200:8"]]
+ 00b5db64 ["INT_ADD", "register:40f0:8", ["const:b5db64:8", "const:4:8"]]
+ 00b5db64 ["CALL", null, ["callee:00bde200:8"]]
- 00b5db20 bytes a4010294
+ 00b5db64 bytes a7010294
- 00b5db34 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5db34 ["INT_ADD", "register:40f0:8", ["const:b5db34:8", "const:4:8"]]
- 00b5db34 ["CALLIND", null, ["register:0:8"]]
+ 00b5db78 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5db78 ["INT_ADD", "register:40f0:8", ["const:b5db78:8", "const:4:8"]]
+ 00b5db78 ["CALLIND", null, ["register:0:8"]]
- 00b5db34 bytes 00013fd6
+ 00b5db78 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-936c28a883167903defbbaa3871fb072"></a>

### [`00b5db80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5db80.md) → [`00b5dbc4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5dbc4.md) _ZN8firebase4auth13CheckEmulatorEPNS0_8AuthDataE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0bd0.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb1c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1c0.md) [`00bdca00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdca00.md)
- 新版 呼出元 1件 [`00be0c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c20.md) · 呼出先 9件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb210`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb210.md) [`00bdca50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdca50.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.34% / 新版 96.34%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5dc3c",
      "incomplete_value": false,
      "site": "00b5dc40",
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
            "const:92:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5dbf8",
      "incomplete_value": false,
      "site": "00b5dbfc",
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
            "const:7:8"
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
      "definition_site": "00b5dca0",
      "incomplete_value": true,
      "site": "00b5dcb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:480:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5dc5c",
      "incomplete_value": true,
      "site": "00b5dc70",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:440:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 11,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5dcdc",
      "incomplete_value": false,
      "site": "00b5dce0",
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
            "const:a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5dc98",
      "incomplete_value": false,
      "site": "00b5dc9c",
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
            "const:15:8"
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
      "00b5dc3c",
      "PARAM",
      [
        "storage",
        "002a1007",
        null,
        "string"
      ]
    ],
    [
      "00b5dca0",
      "READ",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5dcdc",
      "PARAM",
      [
        "storage",
        "0029d015",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5dc3c",
      "PARAM",
      [
        "storage",
        "002a1092",
        null,
        "string"
      ]
    ],
    [
      "00b5dca0",
      "READ",
      [
        "storage",
        "010a1480",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5dcdc",
      "PARAM",
      [
        "storage",
        "0029d0a0",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5dbfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5db80.md#insn-00b5dbfc) · [`00b5dc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5db80.md#insn-00b5dc70) · [`00b5dc9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5db80.md#insn-00b5dc9c)
- 新版 `00b5dc40`（命令位置の公開資料なし） · `00b5dcb4`（命令位置の公開資料なし） · `00b5dce0`（命令位置の公開資料なし）

~~~diff
- 00b5dbfc ["INT_ADD", "register:40f0:8", ["const:b5dbfc:8", "const:4:8"]]
- 00b5dbfc ["CALL", null, ["callee:00bdca50:8"]]
+ 00b5dc40 ["INT_ADD", "register:40f0:8", ["const:b5dc40:8", "const:4:8"]]
+ 00b5dc40 ["CALL", null, ["callee:00bdca50:8"]]
- 00b5dbfc bytes 81fb0194
+ 00b5dc40 bytes 84fb0194
- 00b5dc70 ["INT_ADD", "register:40f0:8", ["const:b5dc70:8", "const:4:8"]]
- 00b5dc70 ["CALL", null, ["callee:00551e14:8"]]
+ 00b5dcb4 ["INT_ADD", "register:40f0:8", ["const:b5dcb4:8", "const:4:8"]]
+ 00b5dcb4 ["CALL", null, ["callee:00551e14:8"]]
- 00b5dc70 bytes 69d0e797
+ 00b5dcb4 bytes 58d0e797
- 00b5dc9c ["INT_ADD", "register:40f0:8", ["const:b5dc9c:8", "const:4:8"]]
- 00b5dc9c ["CALL", null, ["callee:00bde160:8"]]
+ 00b5dce0 ["INT_ADD", "register:40f0:8", ["const:b5dce0:8", "const:4:8"]]
+ 00b5dce0 ["CALL", null, ["callee:00bde160:8"]]
- 00b5dc9c bytes 1d010294
+ 00b5dce0 bytes 20010294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af576584f6267bd341035aae0950fb3c"></a>

### [`00b5dce8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5dce8.md) → [`00b5dd2c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5dd2c.md) _ZN8firebase4auth18CreatePlatformAuthEPNS_3AppE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0980.md) · 呼出先 21件 [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bddfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfd0.md)
- 新版 呼出元 1件 [`00be09d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be09d0.md) · 呼出先 21件 [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb060`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb060.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bde020`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde020.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 94.62% / 新版 94.62%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5dd70",
      "incomplete_value": true,
      "site": "00b5dd70",
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
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5dd2c",
      "incomplete_value": true,
      "site": "00b5dd2c",
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
            "const:4f8:8"
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
      "definition_site": "00b5dd80",
      "incomplete_value": true,
      "site": "00b5dd94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:420:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5dd3c",
      "incomplete_value": true,
      "site": "00b5dd50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e0:8"
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
      "definition_site": "00b5dd84",
      "incomplete_value": true,
      "site": "00b5dd94",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5dd40",
      "incomplete_value": true,
      "site": "00b5dd50",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f0:8"
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
      "00b5dd5c",
      "READ",
      [
        "storage",
        "010a14f8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5dd70",
      "WRITE",
      [
        "storage",
        "010a14f8",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5dd80",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5dd5c",
      "READ",
      [
        "storage",
        "010a1538",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5dd70",
      "WRITE",
      [
        "storage",
        "010a1538",
        null,
        "undefined4"
      ]
    ],
    [
      "00b5dd80",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5dd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5dce8.md#insn-00b5dd2c) · [`00b5dd50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5dce8.md#insn-00b5dd50) · [`00b5dd6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5dce8.md#insn-00b5dd6c)
- 新版 `00b5dd70`（命令位置の公開資料なし） · `00b5dd94`（命令位置の公開資料なし） · `00b5ddb0`（命令位置の公開資料なし）

~~~diff
- 00b5dd2c ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:4f8:8"]]
- 00b5dd2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00b5dd70 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:538:8"]]
+ 00b5dd70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00b5dd2c bytes e8fa04b9
+ 00b5dd70 bytes e83a05b9
- 00b5dd50 ["INT_ADD", "register:40f0:8", ["const:b5dd50:8", "const:4:8"]]
- 00b5dd50 ["CALL", null, ["callee:00bddd40:8"]]
+ 00b5dd94 ["INT_ADD", "register:40f0:8", ["const:b5dd94:8", "const:4:8"]]
+ 00b5dd94 ["CALL", null, ["callee:00bddd40:8"]]
- 00b5dd50 bytes e8ff0194
+ 00b5dd94 bytes ebff0194
- 00b5dd6c ["INT_ADD", "register:40f0:8", ["const:b5dd6c:8", "const:4:8"]]
- 00b5dd6c ["CALL", null, ["callee:00bde180:8"]]
+ 00b5ddb0 ["INT_ADD", "register:40f0:8", ["const:b5ddb0:8", "const:4:8"]]
+ 00b5ddb0 ["CALL", null, ["callee:00bde180:8"]]
- 00b5dd6c bytes f1000294
+ 00b5ddb0 bytes f4000294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-827af8475c6e86fc4a295ea40c2ddf8b"></a>

### [`00b5df24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5df24.md) → [`00b5df68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5d/00b5df68.md) _ZN8firebase4auth4Auth16InitPlatformAuthEPNS0_8AuthDataE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00be09f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be09f0.md) · 呼出先 6件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00be0bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0bd0.md) [`00be0be0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0be0.md)
- 新版 呼出元 1件 [`00be0a40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a40.md) · 呼出先 6件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00566/0056681c.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00be0c20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c20.md) [`00be0c30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0c30.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 88.00% / 新版 88.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5df8c",
      "incomplete_value": true,
      "site": "00b5df9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5df48",
      "incomplete_value": true,
      "site": "00b5df58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4a8:8"
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
      "definition_site": "00b5df90",
      "incomplete_value": true,
      "site": "00b5df9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4f8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5df4c",
      "incomplete_value": true,
      "site": "00b5df58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
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
      "definition_site": "00b5dfac",
      "incomplete_value": true,
      "site": "00b5dfbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:458:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5df68",
      "incomplete_value": true,
      "site": "00b5df78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:418:8"
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
      "00b5df8c",
      "READ",
      [
        "storage",
        "010a14a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5df90",
      "READ",
      [
        "storage",
        "010a14b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5dfac",
      "READ",
      [
        "storage",
        "010a1418",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5df8c",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5df90",
      "READ",
      [
        "storage",
        "010a14f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5dfac",
      "READ",
      [
        "storage",
        "010a1458",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5df58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5df24.md#insn-00b5df58) · [`00b5df60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5df24.md#insn-00b5df60) · [`00b5df78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5df24.md#insn-00b5df78)
- 新版 `00b5df9c`（命令位置の公開資料なし） · `00b5dfa4`（命令位置の公開資料なし） · `00b5dfbc`（命令位置の公開資料なし）

~~~diff
- 00b5df58 ["INT_ADD", "register:40f0:8", ["const:b5df58:8", "const:4:8"]]
- 00b5df58 ["CALL", null, ["callee:0056681c:8"]]
+ 00b5df9c ["INT_ADD", "register:40f0:8", ["const:b5df9c:8", "const:4:8"]]
+ 00b5df9c ["CALL", null, ["callee:0056681c:8"]]
- 00b5df58 bytes 3122e897
+ 00b5df9c bytes 2022e897
- 00b5df60 ["COPY", "tmp:0:8", ["const:418:8"]]
- 00b5df60 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00b5df60 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00b5df60 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00b5dfa4 ["COPY", "tmp:0:8", ["const:458:8"]]
+ 00b5dfa4 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00b5dfa4 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00b5dfa4 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00b5df60 bytes d6621091
+ 00b5dfa4 bytes d6621191
- 00b5df78 ["INT_ADD", "register:40f0:8", ["const:b5df78:8", "const:4:8"]]
- 00b5df78 ["CALL", null, ["callee:00551e14:8"]]
+ 00b5dfbc ["INT_ADD", "register:40f0:8", ["const:b5dfbc:8", "const:4:8"]]
+ 00b5dfbc ["CALL", null, ["callee:00551e14:8"]]
- 00b5df78 bytes a7cfe797
+ 00b5dfbc bytes 96cfe797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f5685676d55741381f9f487248363ec"></a>

### [`00b5dfec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5dfec.md) → [`00b5e030`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e030.md) _ZN8firebase4auth4Auth19DestroyPlatformAuthEPNS0_8AuthDataE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved`

- 旧版 呼出元 1件 [`00be0a00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a00.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde030.md) [`00bde100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde100.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 1件 [`00be0a50`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a50.md) · 呼出先 10件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde080`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde080.md) [`00bde150`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde150.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 call_argument_candidate, constant, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 91.95% / 新版 91.95%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b5e138",
      "incomplete_value": true,
      "site": "00b5e138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:538:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5e0f4",
      "incomplete_value": true,
      "site": "00b5e0f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:4f8:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5e098",
      "incomplete_value": true,
      "site": "00b5e0a8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:460:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5e054",
      "incomplete_value": true,
      "site": "00b5e064",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:420:8"
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
      "definition_site": "00b5e0b4",
      "incomplete_value": true,
      "site": "00b5e0c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:528:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5e070",
      "incomplete_value": true,
      "site": "00b5e07c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4e8:8"
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
      "00b5e07c",
      "READ",
      [
        "storage",
        "010a14c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5e098",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5e0b4",
      "READ",
      [
        "storage",
        "010a14e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5e07c",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5e098",
      "READ",
      [
        "storage",
        "010a1460",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5e0b4",
      "READ",
      [
        "storage",
        "010a1528",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e038`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5dfec.md#insn-00b5e038) · [`00b5e064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5dfec.md#insn-00b5e064) · [`00b5e07c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5d/00b5dfec.md#insn-00b5e07c)
- 新版 `00b5e07c`（命令位置の公開資料なし） · `00b5e0a8`（命令位置の公開資料なし） · `00b5e0c0`（命令位置の公開資料なし）

~~~diff
- 00b5e038 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:4c0:8"]]
- 00b5e038 ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b5e07c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:500:8"]]
+ 00b5e07c ["LOAD", "register:4010:8", ["const:1b1:8", "tmp:0:8"]]
- 00b5e038 bytes 026142f9
+ 00b5e07c bytes 028142f9
- 00b5e064 ["INT_ADD", "register:40f0:8", ["const:b5e064:8", "const:4:8"]]
- 00b5e064 ["CALL", null, ["callee:00551e14:8"]]
+ 00b5e0a8 ["INT_ADD", "register:40f0:8", ["const:b5e0a8:8", "const:4:8"]]
+ 00b5e0a8 ["CALL", null, ["callee:00551e14:8"]]
- 00b5e064 bytes 6ccfe797
+ 00b5e0a8 bytes 5bcfe797
- 00b5e07c ["INT_ADD", "register:40f0:8", ["const:b5e07c:8", "const:4:8"]]
- 00b5e07c ["CALL", null, ["callee:00551e14:8"]]
+ 00b5e0c0 ["INT_ADD", "register:40f0:8", ["const:b5e0c0:8", "const:4:8"]]
+ 00b5e0c0 ["CALL", null, ["callee:00551e14:8"]]
- 00b5e07c bytes 66cfe797
+ 00b5e0c0 bytes 55cfe797
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f8eba3029c19f43fdea7a5de9805cba"></a>

### [`00b5e148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e148.md) → [`00b5e18c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e18c.md) _ZN8firebase4auth12LogHeartbeatEPNS0_4AuthE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0940.md) · 呼出先 5件 [`00bddcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddcf0.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md) [`00bdeff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeff0.md) [`00be0a30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0a30.md)
- 新版 呼出元 1件 [`00be0990`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0990.md) · 呼出先 5件 [`00bddd40`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd40.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md) [`00bdf040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf040.md) [`00be0a80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0a80.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5e1c4",
      "incomplete_value": true,
      "site": "00b5e1d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:420:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5e180",
      "incomplete_value": true,
      "site": "00b5e194",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3e0:8"
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
      "definition_site": "00b5e1c8",
      "incomplete_value": true,
      "site": "00b5e1d8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:430:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5e184",
      "incomplete_value": true,
      "site": "00b5e194",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:3f0:8"
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
      "00b5e1c4",
      "READ",
      [
        "storage",
        "010a13e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5e1c8",
      "READ",
      [
        "storage",
        "010a13f0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5e1c4",
      "READ",
      [
        "storage",
        "010a1420",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5e1c8",
      "READ",
      [
        "storage",
        "010a1430",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5e194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e148.md#insn-00b5e194) · [`00b5e164`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e148.md#insn-00b5e164) · [`00b5e170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e148.md#insn-00b5e170)
- 新版 `00b5e1d8`（命令位置の公開資料なし） · `00b5e1a8`（命令位置の公開資料なし） · `00b5e1b4`（命令位置の公開資料なし）

~~~diff
- 00b5e194 ["INT_ADD", "register:40f0:8", ["const:b5e194:8", "const:4:8"]]
- 00b5e194 ["CALL", null, ["callee:00bddd40:8"]]
+ 00b5e1d8 ["INT_ADD", "register:40f0:8", ["const:b5e1d8:8", "const:4:8"]]
+ 00b5e1d8 ["CALL", null, ["callee:00bddd40:8"]]
- 00b5e194 bytes d7fe0194
+ 00b5e1d8 bytes dafe0194
- 00b5e164 ["INT_ADD", "register:40f0:8", ["const:b5e164:8", "const:4:8"]]
- 00b5e164 ["CALL", null, ["callee:00bde200:8"]]
+ 00b5e1a8 ["INT_ADD", "register:40f0:8", ["const:b5e1a8:8", "const:4:8"]]
+ 00b5e1a8 ["CALL", null, ["callee:00bde200:8"]]
- 00b5e164 bytes 13000294
+ 00b5e1a8 bytes 16000294
- 00b5e170 ["INT_ADD", "register:40f0:8", ["const:b5e170:8", "const:4:8"]]
- 00b5e170 ["CALL", null, ["callee:00be0a80:8"]]
+ 00b5e1b4 ["INT_ADD", "register:40f0:8", ["const:b5e1b4:8", "const:4:8"]]
+ 00b5e1b4 ["CALL", null, ["callee:00be0a80:8"]]
- 00b5e170 bytes 300a0294
+ 00b5e1b4 bytes 330a0294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aecc9b38d53f25a7b2d7b21c8147cbc6"></a>

### [`00b5f110`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f110.md) → [`00b5f154`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f154.md) _ZN8firebase4auth4Auth18SignInWithProviderEPNS0_21FederatedAuthProviderE

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bddce0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddce0.md) · 呼出先 3件 [`00bddd30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddd30.md) [`00bdddc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddc0.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)
- 新版 呼出元 1件 [`00bddd30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd30.md) · 呼出先 3件 [`00bddd80`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd80.md) [`00bdde10`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde10.md) [`00bde180`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde180.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 96.43% / 新版 96.43%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5f190",
      "incomplete_value": false,
      "site": "00b5f194",
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
            "const:154:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f14c",
      "incomplete_value": false,
      "site": "00b5f150",
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
            "const:c9:8"
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
      "00b5f190",
      "PARAM",
      [
        "storage",
        "002a50c9",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b5f190",
      "PARAM",
      [
        "storage",
        "002a5154",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f110.md#insn-00b5f150) · [`00b5f14c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f110.md#insn-00b5f14c) · [`00b5f15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f110.md#insn-00b5f15c)
- 新版 `00b5f194`（命令位置の公開資料なし） · `00b5f190`（命令位置の公開資料なし） · `00b5f1a0`（命令位置の公開資料なし）

~~~diff
- 00b5f150 ["INT_ADD", "register:40f0:8", ["const:b5f150:8", "const:4:8"]]
- 00b5f150 ["CALL", null, ["callee:00bde180:8"]]
+ 00b5f194 ["INT_ADD", "register:40f0:8", ["const:b5f194:8", "const:4:8"]]
+ 00b5f194 ["CALL", null, ["callee:00bde180:8"]]
- 00b5f150 bytes f8fb0194
+ 00b5f194 bytes fbfb0194
- 00b5f14c ["COPY", "tmp:0:8", ["const:c9:8"]]
- 00b5f14c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b5f14c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b5f14c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b5f190 ["COPY", "tmp:0:8", ["const:154:8"]]
+ 00b5f190 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5f190 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b5f190 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b5f14c bytes 00240391
+ 00b5f190 bytes 00500591
- 00b5f15c ["INT_ADD", "register:40f0:8", ["const:b5f15c:8", "const:4:8"]]
- 00b5f15c ["CALL", null, ["callee:00bdde10:8"]]
+ 00b5f1a0 ["INT_ADD", "register:40f0:8", ["const:b5f1a0:8", "const:4:8"]]
+ 00b5f1a0 ["CALL", null, ["callee:00bdde10:8"]]
- 00b5f15c bytes 19fb0194
+ 00b5f1a0 bytes 1cfb0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-35d337a84acf5e948b7e592e17fd02e3"></a>

### [`00b5f5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f5ac.md) → [`00b5f5f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5f5f0.md) _ZN8firebase4auth4Auth30CreateUserWithEmailAndPasswordEPKcS3_

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 14件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b603d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b603d8.md) [`00b64ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)
- 新版 呼出元 0件  · 呼出先 14件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b6041c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b6041c.md) [`00b64f04`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b64/00b64f04.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies, store_value

命令の説明率　旧版 99.30% / 新版 99.30%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

アドレスに依存する影響 `call_argument_candidate` 1件, `store_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_value",
    "new": {
      "definition_site": "00b5f734",
      "incomplete_value": true,
      "site": "00b5f734",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f6f0",
      "incomplete_value": true,
      "site": "00b5f6f0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ba0:8"
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
      "definition_site": "00b5f6a0",
      "incomplete_value": true,
      "site": "00b5f6b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f65c",
      "incomplete_value": true,
      "site": "00b5f674",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:470:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5f774",
      "incomplete_value": false,
      "site": "00b5f788",
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
            "const:17:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5f730",
      "incomplete_value": false,
      "site": "00b5f744",
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
            "const:19:8"
          ]
        ]
      ]
    },
    "ordinal": 16,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5f6a0",
      "READ",
      [
        "storage",
        "010a1470",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5f730",
      "READ",
      [
        "storage",
        "00c1bba0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5f734",
      "DATA",
      [
        "storage",
        "00b64ec0",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b5f6a0",
      "READ",
      [
        "storage",
        "010a14b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5f730",
      "READ",
      [
        "storage",
        "00c1bbf0",
        null,
        "pointer"
      ]
    ],
    [
      "00b5f734",
      "DATA",
      [
        "storage",
        "00b64f04",
        "_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5f674`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f5ac.md#insn-00b5f674) · [`00b5f744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f5ac.md#insn-00b5f744) · [`00b5f5f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f5ac.md#insn-00b5f5f8)
- 新版 `00b5f6b8`（命令位置の公開資料なし） · `00b5f788`（命令位置の公開資料なし） · `00b5f63c`（命令位置の公開資料なし）

~~~diff
- 00b5f674 ["INT_ADD", "register:40f0:8", ["const:b5f674:8", "const:4:8"]]
- 00b5f674 ["CALL", null, ["callee:0047495c:8"]]
+ 00b5f6b8 ["INT_ADD", "register:40f0:8", ["const:b5f6b8:8", "const:4:8"]]
+ 00b5f6b8 ["CALL", null, ["callee:0047495c:8"]]
- 00b5f674 bytes ba54e497
+ 00b5f6b8 bytes a954e497
- 00b5f744 ["INT_ADD", "register:40f0:8", ["const:b5f744:8", "const:4:8"]]
- 00b5f744 ["CALL", null, ["callee:00be0bc0:8"]]
+ 00b5f788 ["INT_ADD", "register:40f0:8", ["const:b5f788:8", "const:4:8"]]
+ 00b5f788 ["CALL", null, ["callee:00be0bc0:8"]]
- 00b5f744 bytes 0b050294
+ 00b5f788 bytes 0e050294
- 00b5f5f8 ["INT_ADD", "register:40f0:8", ["const:b5f5f8:8", "const:4:8"]]
- 00b5f5f8 ["CALL", null, ["callee:00be0c00:8"]]
+ 00b5f63c ["INT_ADD", "register:40f0:8", ["const:b5f63c:8", "const:4:8"]]
+ 00b5f63c ["CALL", null, ["callee:00be0c00:8"]]
- 00b5f5f8 bytes 6e050294
+ 00b5f63c bytes 71050294
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f7bcb264d933196ee15ad9d90d36fcf"></a>

### [`00b5fb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fb44.md) → [`00b5fb88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fb88.md) _ZN8firebase4auth4Auth22SendPasswordResetEmailEPKc

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00b60b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60b54.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb140`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb140.md)
- 新版 呼出元 0件  · 呼出先 13件 [`0047495c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00474/0047495c.md) [`00b60b98`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60b98.md) [`00bdb040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb040.md) [`00bdb090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb090.md) [`00bdb190`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdb190.md)

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
      "definition_site": "00b5fc28",
      "incomplete_value": true,
      "site": "00b5fc3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:4b8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5fbe4",
      "incomplete_value": true,
      "site": "00b5fbf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:478:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5fcc4",
      "incomplete_value": false,
      "site": "00b5fcd8",
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
            "const:ffa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5fc80",
      "incomplete_value": false,
      "site": "00b5fc94",
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
            "const:f6f:8"
          ]
        ]
      ]
    },
    "ordinal": 14,
    "slot": 4
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5fd00",
      "incomplete_value": true,
      "site": "00b5fd10",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:be8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5fcbc",
      "incomplete_value": true,
      "site": "00b5fccc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:b98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 17,
    "slot": 3
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b5fc28",
      "READ",
      [
        "storage",
        "010a1478",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5fcc4",
      "PARAM",
      [
        "storage",
        "002a2f6f",
        null,
        "string"
      ]
    ],
    [
      "00b5fd00",
      "READ",
      [
        "storage",
        "00c1bb98",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b5fc28",
      "READ",
      [
        "storage",
        "010a14b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b5fcc4",
      "PARAM",
      [
        "storage",
        "002a2ffa",
        null,
        "string"
      ]
    ],
    [
      "00b5fd00",
      "READ",
      [
        "storage",
        "00c1bbe8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5fbb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fb44.md#insn-00b5fbb4) · [`00b5fbf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fb44.md#insn-00b5fbf8) · [`00b5fc3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fb44.md#insn-00b5fc3c)
- 新版 `00b5fbf8`（命令位置の公開資料なし） · `00b5fc3c`（命令位置の公開資料なし） · `00b5fc80`（命令位置の公開資料なし）

~~~diff
- 00b5fbb4 ["INT_ADD", "register:40f0:8", ["const:b5fbb4:8", "const:4:8"]]
- 00b5fbb4 ["CALL", null, ["callee:00bdb190:8"]]
+ 00b5fbf8 ["INT_ADD", "register:40f0:8", ["const:b5fbf8:8", "const:4:8"]]
+ 00b5fbf8 ["CALL", null, ["callee:00bdb190:8"]]
- 00b5fbb4 bytes 63ed0194
+ 00b5fbf8 bytes 66ed0194
- 00b5fbf8 ["INT_ADD", "register:40f0:8", ["const:b5fbf8:8", "const:4:8"]]
- 00b5fbf8 ["CALL", null, ["callee:0047495c:8"]]
+ 00b5fc3c ["INT_ADD", "register:40f0:8", ["const:b5fc3c:8", "const:4:8"]]
+ 00b5fc3c ["CALL", null, ["callee:0047495c:8"]]
- 00b5fbf8 bytes 5953e497
+ 00b5fc3c bytes 4853e497
- 00b5fc3c ["INT_ADD", "register:40f0:8", ["const:b5fc3c:8", "const:4:8"]]
- 00b5fc3c ["CALL", null, ["callee:00bde200:8"]]
+ 00b5fc80 ["INT_ADD", "register:40f0:8", ["const:b5fc80:8", "const:4:8"]]
+ 00b5fc80 ["CALL", null, ["callee:00bde200:8"]]
- 00b5fc3c bytes 5df90194
+ 00b5fc80 bytes 60f90194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-52de9673dc97343b17bdc4f5ca6715cb"></a>

### [`00b5fe94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fe94.md) → [`00b5fed8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fed8.md) _ZN8firebase4auth4Auth11UseEmulatorENSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEj

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md) [`00bde1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde1b0.md)
- 新版 呼出元 0件  · 呼出先 3件 [`00551e14`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00551/00551e14.md) [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md) [`00bde200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde200.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 97.22% / 新版 97.22%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b5ff28",
      "incomplete_value": true,
      "site": "00b5ff3c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:480:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b5fee4",
      "incomplete_value": true,
      "site": "00b5fef8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:440:8"
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
      "00b5ff28",
      "READ",
      [
        "storage",
        "010a1440",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b5ff28",
      "READ",
      [
        "storage",
        "010a1480",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b5fef8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fe94.md#insn-00b5fef8) · [`00b5fec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fe94.md#insn-00b5fec4) · [`00b5fed8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5fe94.md#insn-00b5fed8)
- 新版 `00b5ff3c`（命令位置の公開資料なし） · `00b5ff08`（命令位置の公開資料なし） · `00b5ff1c`（命令位置の公開資料なし）

~~~diff
- 00b5fef8 ["INT_ADD", "register:40f0:8", ["const:b5fef8:8", "const:4:8"]]
- 00b5fef8 ["CALL", null, ["callee:00551e14:8"]]
+ 00b5ff3c ["INT_ADD", "register:40f0:8", ["const:b5ff3c:8", "const:4:8"]]
+ 00b5ff3c ["CALL", null, ["callee:00551e14:8"]]
- 00b5fef8 bytes c7c7e797
+ 00b5ff3c bytes b6c7e797
- 00b5fec4 ["INT_ADD", "register:40f0:8", ["const:b5fec4:8", "const:4:8"]]
- 00b5fec4 ["CALL", null, ["callee:00bde200:8"]]
+ 00b5ff08 ["INT_ADD", "register:40f0:8", ["const:b5ff08:8", "const:4:8"]]
+ 00b5ff08 ["CALL", null, ["callee:00bde200:8"]]
- 00b5fec4 bytes bbf80194
+ 00b5ff08 bytes bef80194
- 00b5fed8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b5fed8 ["INT_ADD", "register:40f0:8", ["const:b5fed8:8", "const:4:8"]]
- 00b5fed8 ["CALLIND", null, ["register:0:8"]]
+ 00b5ff1c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b5ff1c ["INT_ADD", "register:40f0:8", ["const:b5ff1c:8", "const:4:8"]]
+ 00b5ff1c ["CALLIND", null, ["register:0:8"]]
- 00b5fed8 bytes 00013fd6
+ 00b5ff1c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37f0d36c9d28b836894c7080e6b83576"></a>

### [`00b5ffb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5ffb8.md) → [`00b5fffc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5fffc.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4Auth20FetchProvidersResultEEEvRKNS_12FutureHand

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0b80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b80.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00be0bd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bd0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

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
      "definition_site": "00b60060",
      "incomplete_value": false,
      "site": "00b60064",
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
      "definition_site": "00b6001c",
      "incomplete_value": false,
      "site": "00b60020",
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
      "00b60060",
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
      "00b60060",
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

- 旧版 [`00b60020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5ffb8.md#insn-00b60020) · [`00b60064`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5ffb8.md#insn-00b60064) · [`00b5ffe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5ffb8.md#insn-00b5ffe4)
- 新版 `00b60064`（命令位置の公開資料なし） · `00b600a8`（命令位置の公開資料なし） · `00b60028`（命令位置の公開資料なし）

~~~diff
- 00b60020 ["INT_ADD", "register:40f0:8", ["const:b60020:8", "const:4:8"]]
- 00b60020 ["CALL", null, ["callee:00bde180:8"]]
+ 00b60064 ["INT_ADD", "register:40f0:8", ["const:b60064:8", "const:4:8"]]
+ 00b60064 ["CALL", null, ["callee:00bde180:8"]]
- 00b60020 bytes 44f80194
+ 00b60064 bytes 47f80194
- 00b60064 ["INT_ADD", "register:40f0:8", ["const:b60064:8", "const:4:8"]]
- 00b60064 ["CALL", null, ["callee:00bde010:8"]]
+ 00b600a8 ["INT_ADD", "register:40f0:8", ["const:b600a8:8", "const:4:8"]]
+ 00b600a8 ["CALL", null, ["callee:00bde010:8"]]
- 00b60064 bytes d7f70194
+ 00b600a8 bytes daf70194
- 00b5ffe4 ["INT_ADD", "register:40f0:8", ["const:b5ffe4:8", "const:4:8"]]
- 00b5ffe4 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b60028 ["INT_ADD", "register:40f0:8", ["const:b60028:8", "const:4:8"]]
+ 00b60028 ["CALL", null, ["callee:00bddc20:8"]]
- 00b5ffe4 bytes fbf60194
+ 00b60028 bytes fef60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-06ceb78919b76def370d6b8748566f9d"></a>

### [`00b60194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60194.md) → [`00b601d8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b601d8.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4Auth20FetchProvidersResultEZNS2_14FutureCallbackIS4_EEvP7_JNIEnvP8_jobje

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b50.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00be0ba0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0ba0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60244",
      "incomplete_value": false,
      "site": "00b60248",
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
      "definition_site": "00b60200",
      "incomplete_value": false,
      "site": "00b60204",
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
      "00b60244",
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
      "00b60244",
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

- 旧版 [`00b60204`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60194.md#insn-00b60204) · [`00b601c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60194.md#insn-00b601c8) · [`00b601d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60194.md#insn-00b601d4)
- 新版 `00b60248`（命令位置の公開資料なし） · `00b6020c`（命令位置の公開資料なし） · `00b60218`（命令位置の公開資料なし）

~~~diff
- 00b60204 ["INT_ADD", "register:40f0:8", ["const:b60204:8", "const:4:8"]]
- 00b60204 ["CALL", null, ["callee:00bde180:8"]]
+ 00b60248 ["INT_ADD", "register:40f0:8", ["const:b60248:8", "const:4:8"]]
+ 00b60248 ["CALL", null, ["callee:00bde180:8"]]
- 00b60204 bytes cbf70194
+ 00b60248 bytes cef70194
- 00b601c8 ["INT_ADD", "register:40f0:8", ["const:b601c8:8", "const:4:8"]]
- 00b601c8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b6020c ["INT_ADD", "register:40f0:8", ["const:b6020c:8", "const:4:8"]]
+ 00b6020c ["CALL", null, ["callee:00bddc20:8"]]
- 00b601c8 bytes 82f60194
+ 00b6020c bytes 85f60194
- 00b601d4 ["INT_ADD", "register:40f0:8", ["const:b601d4:8", "const:4:8"]]
- 00b601d4 ["CALL", null, ["callee:00bde000:8"]]
+ 00b60218 ["INT_ADD", "register:40f0:8", ["const:b60218:8", "const:4:8"]]
+ 00b60218 ["CALL", null, ["callee:00bde000:8"]]
- 00b601d4 bytes 77f70194
+ 00b60218 bytes 7af70194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cb3a2139e8f90f35aa059cf32c1571a"></a>

### [`00b604ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b604ac.md) → [`00b604f0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b604f0.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12Fut

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0b40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b40.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00be0b90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0b90.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6055c",
      "incomplete_value": false,
      "site": "00b60560",
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
      "definition_site": "00b60518",
      "incomplete_value": false,
      "site": "00b6051c",
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
      "00b6055c",
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
      "00b6055c",
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

- 旧版 [`00b6051c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b604ac.md#insn-00b6051c) · [`00b604e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b604ac.md#insn-00b604e0) · [`00b604ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b604ac.md#insn-00b604ec)
- 新版 `00b60560`（命令位置の公開資料なし） · `00b60524`（命令位置の公開資料なし） · `00b60530`（命令位置の公開資料なし）

~~~diff
- 00b6051c ["INT_ADD", "register:40f0:8", ["const:b6051c:8", "const:4:8"]]
- 00b6051c ["CALL", null, ["callee:00bde180:8"]]
+ 00b60560 ["INT_ADD", "register:40f0:8", ["const:b60560:8", "const:4:8"]]
+ 00b60560 ["CALL", null, ["callee:00bde180:8"]]
- 00b6051c bytes 05f70194
+ 00b60560 bytes 08f70194
- 00b604e0 ["INT_ADD", "register:40f0:8", ["const:b604e0:8", "const:4:8"]]
- 00b604e0 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b60524 ["INT_ADD", "register:40f0:8", ["const:b60524:8", "const:4:8"]]
+ 00b60524 ["CALL", null, ["callee:00bddc20:8"]]
- 00b604e0 bytes bcf50194
+ 00b60524 bytes bff50194
- 00b604ec ["INT_ADD", "register:40f0:8", ["const:b604ec:8", "const:4:8"]]
- 00b604ec ["CALL", null, ["callee:00bde000:8"]]
+ 00b60530 ["INT_ADD", "register:40f0:8", ["const:b60530:8", "const:4:8"]]
+ 00b60530 ["CALL", null, ["callee:00bde000:8"]]
- 00b604ec bytes b1f60194
+ 00b60530 bytes b4f60194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-45a41e799f778585330129a2daeeb024"></a>

### [`00b60698`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60698.md) → [`00b606dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b606dc.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4UserEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b90.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00be0be0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0be0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

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
      "definition_site": "00b60740",
      "incomplete_value": false,
      "site": "00b60744",
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
      "definition_site": "00b606fc",
      "incomplete_value": false,
      "site": "00b60700",
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
      "00b60740",
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
      "00b60740",
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

- 旧版 [`00b60700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60698.md#insn-00b60700) · [`00b60744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60698.md#insn-00b60744) · [`00b606c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60698.md#insn-00b606c4)
- 新版 `00b60744`（命令位置の公開資料なし） · `00b60788`（命令位置の公開資料なし） · `00b60708`（命令位置の公開資料なし）

~~~diff
- 00b60700 ["INT_ADD", "register:40f0:8", ["const:b60700:8", "const:4:8"]]
- 00b60700 ["CALL", null, ["callee:00bde180:8"]]
+ 00b60744 ["INT_ADD", "register:40f0:8", ["const:b60744:8", "const:4:8"]]
+ 00b60744 ["CALL", null, ["callee:00bde180:8"]]
- 00b60700 bytes 8cf60194
+ 00b60744 bytes 8ff60194
- 00b60744 ["INT_ADD", "register:40f0:8", ["const:b60744:8", "const:4:8"]]
- 00b60744 ["CALL", null, ["callee:00bde010:8"]]
+ 00b60788 ["INT_ADD", "register:40f0:8", ["const:b60788:8", "const:4:8"]]
+ 00b60788 ["CALL", null, ["callee:00bde010:8"]]
- 00b60744 bytes 1ff60194
+ 00b60788 bytes 22f60194
- 00b606c4 ["INT_ADD", "register:40f0:8", ["const:b606c4:8", "const:4:8"]]
- 00b606c4 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b60708 ["INT_ADD", "register:40f0:8", ["const:b60708:8", "const:4:8"]]
+ 00b60708 ["CALL", null, ["callee:00bddc20:8"]]
- 00b606c4 bytes 43f50194
+ 00b60708 bytes 46f50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-43ed5b130e0d149ee841fb3c4af50e11"></a>

### [`00b60874`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60874.md) → [`00b608b8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b608b8.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4UserEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResu

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b60.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00be0bb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bb0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60924",
      "incomplete_value": false,
      "site": "00b60928",
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
      "definition_site": "00b608e0",
      "incomplete_value": false,
      "site": "00b608e4",
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
      "00b60924",
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
      "00b60924",
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

- 旧版 [`00b608e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60874.md#insn-00b608e4) · [`00b608a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60874.md#insn-00b608a8) · [`00b608b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60874.md#insn-00b608b4)
- 新版 `00b60928`（命令位置の公開資料なし） · `00b608ec`（命令位置の公開資料なし） · `00b608f8`（命令位置の公開資料なし）

~~~diff
- 00b608e4 ["INT_ADD", "register:40f0:8", ["const:b608e4:8", "const:4:8"]]
- 00b608e4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b60928 ["INT_ADD", "register:40f0:8", ["const:b60928:8", "const:4:8"]]
+ 00b60928 ["CALL", null, ["callee:00bde180:8"]]
- 00b608e4 bytes 13f60194
+ 00b60928 bytes 16f60194
- 00b608a8 ["INT_ADD", "register:40f0:8", ["const:b608a8:8", "const:4:8"]]
- 00b608a8 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b608ec ["INT_ADD", "register:40f0:8", ["const:b608ec:8", "const:4:8"]]
+ 00b608ec ["CALL", null, ["callee:00bddc20:8"]]
- 00b608a8 bytes caf40194
+ 00b608ec bytes cdf40194
- 00b608b4 ["INT_ADD", "register:40f0:8", ["const:b608b4:8", "const:4:8"]]
- 00b608b4 ["CALL", null, ["callee:00bde000:8"]]
+ 00b608f8 ["INT_ADD", "register:40f0:8", ["const:b608f8:8", "const:4:8"]]
+ 00b608f8 ["CALL", null, ["callee:00bde000:8"]]
- 00b608b4 bytes bff50194
+ 00b608f8 bytes c2f50194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b55b810d6a3499a8d4cb4f54d119dff0"></a>

### [`00b60a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60a4c.md) → [`00b60a90`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60a90.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10AuthResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_E

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0b70.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00be0bc0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bc0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

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
      "definition_site": "00b60af4",
      "incomplete_value": false,
      "site": "00b60af8",
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
      "definition_site": "00b60ab0",
      "incomplete_value": false,
      "site": "00b60ab4",
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
      "00b60af4",
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
      "00b60af4",
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

- 旧版 [`00b60ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60a4c.md#insn-00b60ab4) · [`00b60af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60a4c.md#insn-00b60af8) · [`00b60a78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60a4c.md#insn-00b60a78)
- 新版 `00b60af8`（命令位置の公開資料なし） · `00b60b3c`（命令位置の公開資料なし） · `00b60abc`（命令位置の公開資料なし）

~~~diff
- 00b60ab4 ["INT_ADD", "register:40f0:8", ["const:b60ab4:8", "const:4:8"]]
- 00b60ab4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b60af8 ["INT_ADD", "register:40f0:8", ["const:b60af8:8", "const:4:8"]]
+ 00b60af8 ["CALL", null, ["callee:00bde180:8"]]
- 00b60ab4 bytes 9ff50194
+ 00b60af8 bytes a2f50194
- 00b60af8 ["INT_ADD", "register:40f0:8", ["const:b60af8:8", "const:4:8"]]
- 00b60af8 ["CALL", null, ["callee:00bde010:8"]]
+ 00b60b3c ["INT_ADD", "register:40f0:8", ["const:b60b3c:8", "const:4:8"]]
+ 00b60b3c ["CALL", null, ["callee:00bde010:8"]]
- 00b60af8 bytes 32f50194
+ 00b60b3c bytes 35f50194
- 00b60a78 ["INT_ADD", "register:40f0:8", ["const:b60a78:8", "const:4:8"]]
- 00b60a78 ["CALL", null, ["callee:00bddc20:8"]]
+ 00b60abc ["INT_ADD", "register:40f0:8", ["const:b60abc:8", "const:4:8"]]
+ 00b60abc ["CALL", null, ["callee:00bddc20:8"]]
- 00b60a78 bytes 56f40194
+ 00b60abc bytes 59f40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09e31aaa524f1363e30428fbe27fdd26"></a>

### [`00b60c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60c28.md) → [`00b60c6c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60c6c.md) _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS_4auth14FutureCallbackIvEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUl

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00be0ba0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0ba0.md) · 呼出先 10件 [`00bddbd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbd0.md) [`00bddbe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddbe0.md) [`00bddf60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) [`00bddf80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) [`00bddf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md)
- 新版 呼出元 1件 [`00be0bf0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00be0/00be0bf0.md) · 呼出先 10件 [`00bddc20`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc20.md) [`00bddc30`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddc30.md) [`00bddfb0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfb0.md) [`00bddfd0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfd0.md) [`00bddfe0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddfe0.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.72% / 新版 98.72%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b60cd8",
      "incomplete_value": false,
      "site": "00b60cdc",
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
      "definition_site": "00b60c94",
      "incomplete_value": false,
      "site": "00b60c98",
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
      "00b60cd8",
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
      "00b60cd8",
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

- 旧版 [`00b60c98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60c28.md#insn-00b60c98) · [`00b60c5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60c28.md#insn-00b60c5c) · [`00b60c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60c28.md#insn-00b60c68)
- 新版 `00b60cdc`（命令位置の公開資料なし） · `00b60ca0`（命令位置の公開資料なし） · `00b60cac`（命令位置の公開資料なし）

~~~diff
- 00b60c98 ["INT_ADD", "register:40f0:8", ["const:b60c98:8", "const:4:8"]]
- 00b60c98 ["CALL", null, ["callee:00bde180:8"]]
+ 00b60cdc ["INT_ADD", "register:40f0:8", ["const:b60cdc:8", "const:4:8"]]
+ 00b60cdc ["CALL", null, ["callee:00bde180:8"]]
- 00b60c98 bytes 26f50194
+ 00b60cdc bytes 29f50194
- 00b60c5c ["INT_ADD", "register:40f0:8", ["const:b60c5c:8", "const:4:8"]]
- 00b60c5c ["CALL", null, ["callee:00bddc20:8"]]
+ 00b60ca0 ["INT_ADD", "register:40f0:8", ["const:b60ca0:8", "const:4:8"]]
+ 00b60ca0 ["CALL", null, ["callee:00bddc20:8"]]
- 00b60c5c bytes ddf30194
+ 00b60ca0 bytes e0f30194
- 00b60c68 ["INT_ADD", "register:40f0:8", ["const:b60c68:8", "const:4:8"]]
- 00b60c68 ["CALL", null, ["callee:00bde000:8"]]
+ 00b60cac ["INT_ADD", "register:40f0:8", ["const:b60cac:8", "const:4:8"]]
+ 00b60cac ["CALL", null, ["callee:00bde000:8"]]
- 00b60c68 bytes d2f40194
+ 00b60cac bytes d5f40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e00bc79cdce62c3ec4f2c74ff95368a"></a>

### [`00b60d60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60d60.md) → [`00b60da4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60da4.md) _ZN8firebase4auth10authresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00b60dd0",
      "incomplete_value": true,
      "site": "00b60dd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60d8c",
      "incomplete_value": true,
      "site": "00b60d8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "definition_site": "00b60db8",
      "incomplete_value": true,
      "site": "00b60db8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60d74",
      "incomplete_value": true,
      "site": "00b60d74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b60dc4",
      "incomplete_value": false,
      "site": "00b60dc8",
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
            "const:55:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60d80",
      "incomplete_value": false,
      "site": "00b60d84",
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
            "const:fca:8"
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
      "00b60db4",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60dc4",
      "PARAM",
      [
        "storage",
        "002a1fca",
        null,
        "string"
      ]
    ],
    [
      "00b60dd0",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b60db4",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60dc4",
      "PARAM",
      [
        "storage",
        "002a2055",
        null,
        "string"
      ]
    ],
    [
      "00b60dd0",
      "WRITE",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60d84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60d60.md#insn-00b60d84) · [`00b60d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60d60.md#insn-00b60d8c) · [`00b60d70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60d60.md#insn-00b60d70)
- 新版 `00b60dc8`（命令位置の公開資料なし） · `00b60dd0`（命令位置の公開資料なし） · `00b60db4`（命令位置の公開資料なし）

~~~diff
- 00b60d84 ["INT_ADD", "register:40f0:8", ["const:b60d84:8", "const:4:8"]]
- 00b60d84 ["CALL", null, ["callee:00bde090:8"]]
+ 00b60dc8 ["INT_ADD", "register:40f0:8", ["const:b60dc8:8", "const:4:8"]]
+ 00b60dc8 ["CALL", null, ["callee:00bde090:8"]]
- 00b60d84 bytes aff40194
+ 00b60dc8 bytes b2f40194
- 00b60d8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b60d8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b60dd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
+ 00b60dd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60d8c bytes 608202f9
+ 00b60dd0 bytes 60a202f9
- 00b60d70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b60d70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b60db4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
+ 00b60db4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b60d70 bytes 688242f9
+ 00b60db4 bytes 68a242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-64b79ff401506ab45768d1a87548b6bb"></a>

### [`00b60da0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60da0.md) → [`00b60de4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60de4.md) _ZN8firebase4auth10authresult19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b60e10",
      "incomplete_value": true,
      "site": "00b60e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60dcc",
      "incomplete_value": true,
      "site": "00b60dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "definition_site": "00b60df8",
      "incomplete_value": true,
      "site": "00b60df8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60db4",
      "incomplete_value": true,
      "site": "00b60db4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b60e00",
      "incomplete_value": false,
      "site": "00b60e08",
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
            "const:55:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60dbc",
      "incomplete_value": false,
      "site": "00b60dc4",
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
            "const:fca:8"
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
      "00b60df4",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60e00",
      "PARAM",
      [
        "storage",
        "002a1fca",
        null,
        "string"
      ]
    ],
    [
      "00b60e10",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b60df4",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60e00",
      "PARAM",
      [
        "storage",
        "002a2055",
        null,
        "string"
      ]
    ],
    [
      "00b60e10",
      "WRITE",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60dc4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60da0.md#insn-00b60dc4) · [`00b60dcc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60da0.md#insn-00b60dcc) · [`00b60db0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60da0.md#insn-00b60db0)
- 新版 `00b60e08`（命令位置の公開資料なし） · `00b60e10`（命令位置の公開資料なし） · `00b60df4`（命令位置の公開資料なし）

~~~diff
- 00b60dc4 ["INT_ADD", "register:40f0:8", ["const:b60dc4:8", "const:4:8"]]
- 00b60dc4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b60e08 ["INT_ADD", "register:40f0:8", ["const:b60e08:8", "const:4:8"]]
+ 00b60e08 ["CALL", null, ["callee:00bde090:8"]]
- 00b60dc4 bytes 9ff40194
+ 00b60e08 bytes a2f40194
- 00b60dcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b60dcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b60e10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
+ 00b60e10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60dcc bytes 608202f9
+ 00b60e10 bytes 60a202f9
- 00b60db0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b60db0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b60df4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
+ 00b60df4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b60db0 bytes 688242f9
+ 00b60df4 bytes 68a242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50e748222275adfb8810bcb093cc3195"></a>

### [`00b60de0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60de0.md) → [`00b60e24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60e24.md) _ZN8firebase4auth10authresult10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b60e54",
      "incomplete_value": true,
      "site": "00b60e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60e10",
      "incomplete_value": true,
      "site": "00b60e10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "definition_site": "00b60e38",
      "incomplete_value": true,
      "site": "00b60e38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60df4",
      "incomplete_value": true,
      "site": "00b60df4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b60e44",
      "incomplete_value": false,
      "site": "00b60e4c",
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
            "const:55:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60e00",
      "incomplete_value": false,
      "site": "00b60e08",
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
            "const:fca:8"
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
      "00b60e34",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60e44",
      "PARAM",
      [
        "storage",
        "002a1fca",
        null,
        "string"
      ]
    ],
    [
      "00b60e54",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b60e34",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60e44",
      "PARAM",
      [
        "storage",
        "002a2055",
        null,
        "string"
      ]
    ],
    [
      "00b60e54",
      "WRITE",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60e08`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60de0.md#insn-00b60e08) · [`00b60e10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60de0.md#insn-00b60e10) · [`00b60df0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60de0.md#insn-00b60df0)
- 新版 `00b60e4c`（命令位置の公開資料なし） · `00b60e54`（命令位置の公開資料なし） · `00b60e34`（命令位置の公開資料なし）

~~~diff
- 00b60e08 ["INT_ADD", "register:40f0:8", ["const:b60e08:8", "const:4:8"]]
- 00b60e08 ["CALL", null, ["callee:00bde090:8"]]
+ 00b60e4c ["INT_ADD", "register:40f0:8", ["const:b60e4c:8", "const:4:8"]]
+ 00b60e4c ["CALL", null, ["callee:00bde090:8"]]
- 00b60e08 bytes 8ef40194
+ 00b60e4c bytes 91f40194
- 00b60e10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b60e10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b60e54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
+ 00b60e54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60e10 bytes 608202f9
+ 00b60e54 bytes 60a202f9
- 00b60df0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b60df0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b60e34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
+ 00b60e34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b60df0 bytes 688242f9
+ 00b60e34 bytes 68a242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-877a624590b6ebc15912841d48af8042"></a>

### [`00b60e24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60e24.md) → [`00b60e68`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60e68.md) _ZN8firebase4auth10authresult10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b60e98",
      "incomplete_value": true,
      "site": "00b60e98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60e54",
      "incomplete_value": true,
      "site": "00b60e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "definition_site": "00b60e7c",
      "incomplete_value": true,
      "site": "00b60e7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60e38",
      "incomplete_value": true,
      "site": "00b60e38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b60e84",
      "incomplete_value": false,
      "site": "00b60e90",
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
            "const:55:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60e40",
      "incomplete_value": false,
      "site": "00b60e4c",
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
            "const:fca:8"
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
      "00b60e78",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60e84",
      "PARAM",
      [
        "storage",
        "002a1fca",
        null,
        "string"
      ]
    ],
    [
      "00b60e98",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b60e78",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60e84",
      "PARAM",
      [
        "storage",
        "002a2055",
        null,
        "string"
      ]
    ],
    [
      "00b60e98",
      "WRITE",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60e4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60e24.md#insn-00b60e4c) · [`00b60e54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60e24.md#insn-00b60e54) · [`00b60e34`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60e24.md#insn-00b60e34)
- 新版 `00b60e90`（命令位置の公開資料なし） · `00b60e98`（命令位置の公開資料なし） · `00b60e78`（命令位置の公開資料なし）

~~~diff
- 00b60e4c ["INT_ADD", "register:40f0:8", ["const:b60e4c:8", "const:4:8"]]
- 00b60e4c ["CALL", null, ["callee:00bde090:8"]]
+ 00b60e90 ["INT_ADD", "register:40f0:8", ["const:b60e90:8", "const:4:8"]]
+ 00b60e90 ["CALL", null, ["callee:00bde090:8"]]
- 00b60e4c bytes 7df40194
+ 00b60e90 bytes 80f40194
- 00b60e54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b60e54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b60e98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
+ 00b60e98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60e54 bytes 608202f9
+ 00b60e98 bytes 60a202f9
- 00b60e34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:500:8"]]
- 00b60e34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b60e78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:540:8"]]
+ 00b60e78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b60e34 bytes 688242f9
+ 00b60e78 bytes 68a242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6fc4472d53107eef8676f703d9c0551"></a>

### [`00b60e74`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60e74.md) → [`00b60eb8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60eb8.md) _ZN8firebase4auth10authresult15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b60f10",
      "incomplete_value": true,
      "site": "00b60f10",
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
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60ecc",
      "incomplete_value": true,
      "site": "00b60ecc",
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
            "const:508:8"
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
      "definition_site": "00b60eec",
      "incomplete_value": true,
      "site": "00b60ef8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:540:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60ea8",
      "incomplete_value": true,
      "site": "00b60eb4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:500:8"
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
      "00b60ecc",
      "READ",
      [
        "storage",
        "010a1508",
        null,
        "undefined1"
      ]
    ],
    [
      "00b60eec",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60f10",
      "WRITE",
      [
        "storage",
        "010a1508",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b60ecc",
      "READ",
      [
        "storage",
        "010a1548",
        null,
        "undefined1"
      ]
    ],
    [
      "00b60eec",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60f10",
      "WRITE",
      [
        "storage",
        "010a1548",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60e88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60e74.md#insn-00b60e88) · [`00b60eb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60e74.md#insn-00b60eb4) · [`00b60ecc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60e74.md#insn-00b60ecc)
- 新版 `00b60ecc`（命令位置の公開資料なし） · `00b60ef8`（命令位置の公開資料なし） · `00b60f10`（命令位置の公開資料なし）

~~~diff
- 00b60e88 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:508:8"]]
- 00b60e88 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b60e88 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b60ecc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:548:8"]]
+ 00b60ecc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b60ecc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b60e88 bytes a8225439
+ 00b60ecc bytes a8225539
- 00b60eb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60eb4 ["INT_ADD", "register:40f0:8", ["const:b60eb4:8", "const:4:8"]]
- 00b60eb4 ["CALLIND", null, ["register:0:8"]]
+ 00b60ef8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60ef8 ["INT_ADD", "register:40f0:8", ["const:b60ef8:8", "const:4:8"]]
+ 00b60ef8 ["CALLIND", null, ["register:0:8"]]
- 00b60eb4 bytes 00013fd6
+ 00b60ef8 bytes 00013fd6
- 00b60ecc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b60ecc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:508:8"]]
- 00b60ecc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b60f10 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b60f10 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:548:8"]]
+ 00b60f10 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b60ecc bytes a0221439
+ 00b60f10 bytes a0221539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-976d0e0b3fc13520dd688b5e46522dbd"></a>

### [`00b60ee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60ee0.md) → [`00b60f24`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60f24.md) _ZN8firebase4auth10authresult12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b60f60",
      "incomplete_value": true,
      "site": "00b60f60",
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
            "const:548:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60f1c",
      "incomplete_value": true,
      "site": "00b60f1c",
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
            "const:508:8"
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
      "definition_site": "00b60f80",
      "incomplete_value": true,
      "site": "00b60f80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60f3c",
      "incomplete_value": true,
      "site": "00b60f3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "definition_site": "00b60f3c",
      "incomplete_value": true,
      "site": "00b60f3c",
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
      "definition_site": "00b60ef8",
      "incomplete_value": true,
      "site": "00b60ef8",
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
      "00b60f38",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60f44",
      "READ",
      [
        "storage",
        "010a1508",
        null,
        "undefined1"
      ]
    ],
    [
      "00b60f60",
      "WRITE",
      [
        "storage",
        "010a1508",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b60f38",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60f44",
      "READ",
      [
        "storage",
        "010a1548",
        null,
        "undefined1"
      ]
    ],
    [
      "00b60f60",
      "WRITE",
      [
        "storage",
        "010a1548",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60ef4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60ee0.md#insn-00b60ef4) · [`00b60f1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60ee0.md#insn-00b60f1c) · [`00b60f38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60ee0.md#insn-00b60f38)
- 新版 `00b60f38`（命令位置の公開資料なし） · `00b60f60`（命令位置の公開資料なし） · `00b60f7c`（命令位置の公開資料なし）

~~~diff
- 00b60ef4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:500:8"]]
- 00b60ef4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b60f38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:540:8"]]
+ 00b60f38 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b60ef4 bytes 818242f9
+ 00b60f38 bytes 81a242f9
- 00b60f1c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b60f1c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b60f1c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:508:8"]]
- 00b60f1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b60f60 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b60f60 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b60f60 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:548:8"]]
+ 00b60f60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b60f1c bytes bf221439
+ 00b60f60 bytes bf221539
- 00b60f38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b60f38 ["INT_ADD", "register:40f0:8", ["const:b60f38:8", "const:4:8"]]
- 00b60f38 ["CALLIND", null, ["register:0:8"]]
+ 00b60f7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b60f7c ["INT_ADD", "register:40f0:8", ["const:b60f7c:8", "const:4:8"]]
+ 00b60f7c ["CALLIND", null, ["register:0:8"]]
- 00b60f38 bytes 00013fd6
+ 00b60f7c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3aae418b523de695606e14ddfd47419"></a>

### [`00b60f50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60f50.md) → [`00b60f94`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b60f94.md) _ZN8firebase4auth10authresult14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b60fd4",
      "incomplete_value": true,
      "site": "00b60fd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60f90",
      "incomplete_value": true,
      "site": "00b60f90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "definition_site": "00b60fb0",
      "incomplete_value": true,
      "site": "00b60fb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60f6c",
      "incomplete_value": true,
      "site": "00b60f6c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b60fb8",
      "incomplete_value": false,
      "site": "00b60fcc",
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
            "const:55:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b60f74",
      "incomplete_value": false,
      "site": "00b60f88",
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
            "const:fca:8"
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
      "00b60fa8",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60fb8",
      "PARAM",
      [
        "storage",
        "002a1fca",
        null,
        "string"
      ]
    ],
    [
      "00b60fd4",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b60fa8",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00b60fb8",
      "PARAM",
      [
        "storage",
        "002a2055",
        null,
        "string"
      ]
    ],
    [
      "00b60fd4",
      "WRITE",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60f88`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60f50.md#insn-00b60f88) · [`00b60f90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60f50.md#insn-00b60f90) · [`00b60f64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60f50.md#insn-00b60f64)
- 新版 `00b60fcc`（命令位置の公開資料なし） · `00b60fd4`（命令位置の公開資料なし） · `00b60fa8`（命令位置の公開資料なし）

~~~diff
- 00b60f88 ["INT_ADD", "register:40f0:8", ["const:b60f88:8", "const:4:8"]]
- 00b60f88 ["CALL", null, ["callee:00bde090:8"]]
+ 00b60fcc ["INT_ADD", "register:40f0:8", ["const:b60fcc:8", "const:4:8"]]
+ 00b60fcc ["CALL", null, ["callee:00bde090:8"]]
- 00b60f88 bytes 2ef40194
+ 00b60fcc bytes 31f40194
- 00b60f90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:500:8"]]
- 00b60f90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b60fd4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:540:8"]]
+ 00b60fd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b60f90 bytes 808202f9
+ 00b60fd4 bytes 80a202f9
- 00b60f64 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:500:8"]]
- 00b60f64 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b60fa8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:540:8"]]
+ 00b60fa8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b60f64 bytes 818242f9
+ 00b60fa8 bytes 81a242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c025a953e78f6a842f5348d7a933b29d"></a>

### [`00b60fc0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60fc0.md) → [`00b61004`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61004.md) _ZN8firebase4auth10authresult11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b61020",
      "incomplete_value": false,
      "site": "00b61024",
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
      "definition_site": "00b60fdc",
      "incomplete_value": false,
      "site": "00b60fe0",
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
      "definition_site": "00b61030",
      "incomplete_value": true,
      "site": "00b6103c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b60fec",
      "incomplete_value": true,
      "site": "00b60ff8",
      "value": [
        "LOAD",
        "8",
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
      "00b61020",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b61030",
      "DATA",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61020",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b61030",
      "DATA",
      [
        "storage",
        "010a1550",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b60fe0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60fc0.md#insn-00b60fe0) · [`00b60fdc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60fc0.md#insn-00b60fdc) · [`00b60fe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60fc0.md#insn-00b60fe8)
- 新版 `00b61024`（命令位置の公開資料なし） · `00b61020`（命令位置の公開資料なし） · `00b6102c`（命令位置の公開資料なし）

~~~diff
- 00b60fe0 ["INT_ADD", "register:40f0:8", ["const:b60fe0:8", "const:4:8"]]
- 00b60fe0 ["CALL", null, ["callee:00bde180:8"]]
+ 00b61024 ["INT_ADD", "register:40f0:8", ["const:b61024:8", "const:4:8"]]
+ 00b61024 ["CALL", null, ["callee:00bde180:8"]]
- 00b60fe0 bytes 54f40194
+ 00b61024 bytes 57f40194
- 00b60fdc ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b60fdc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b60fdc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b60fdc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b61020 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b61020 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61020 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61020 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b60fdc bytes 00501791
+ 00b61020 bytes 001c1591
- 00b60fe8 ["COPY", "tmp:0:8", ["const:510:8"]]
- 00b60fe8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b60fe8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b60fe8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6102c ["COPY", "tmp:0:8", ["const:550:8"]]
+ 00b6102c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6102c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6102c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b60fe8 bytes 08411491
+ 00b6102c bytes 08411591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c05fb152e381a40f6f8aca1bdaf6517f"></a>

### [`00b60ffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60ffc.md) → [`00b61040`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61040.md) _ZN8firebase4auth10authresult13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b61080",
      "incomplete_value": true,
      "site": "00b61080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:540:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6103c",
      "incomplete_value": true,
      "site": "00b6103c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:500:8"
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
      "definition_site": "00b6105c",
      "incomplete_value": true,
      "site": "00b6105c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61018",
      "incomplete_value": true,
      "site": "00b61018",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61064",
      "incomplete_value": false,
      "site": "00b61078",
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
            "const:55:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61020",
      "incomplete_value": false,
      "site": "00b61034",
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
            "const:fca:8"
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
      "00b61054",
      "READ",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61064",
      "PARAM",
      [
        "storage",
        "002a1fca",
        null,
        "string"
      ]
    ],
    [
      "00b61080",
      "WRITE",
      [
        "storage",
        "010a1500",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61054",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61064",
      "PARAM",
      [
        "storage",
        "002a2055",
        null,
        "string"
      ]
    ],
    [
      "00b61080",
      "WRITE",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61034`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60ffc.md#insn-00b61034) · [`00b6103c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60ffc.md#insn-00b6103c) · [`00b61010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b60/00b60ffc.md#insn-00b61010)
- 新版 `00b61078`（命令位置の公開資料なし） · `00b61080`（命令位置の公開資料なし） · `00b61054`（命令位置の公開資料なし）

~~~diff
- 00b61034 ["INT_ADD", "register:40f0:8", ["const:b61034:8", "const:4:8"]]
- 00b61034 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61078 ["INT_ADD", "register:40f0:8", ["const:b61078:8", "const:4:8"]]
+ 00b61078 ["CALL", null, ["callee:00bde090:8"]]
- 00b61034 bytes 03f40194
+ 00b61078 bytes 06f40194
- 00b6103c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:500:8"]]
- 00b6103c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61080 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:540:8"]]
+ 00b61080 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6103c bytes 808202f9
+ 00b61080 bytes 80a202f9
- 00b61010 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:500:8"]]
- 00b61010 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61054 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:540:8"]]
+ 00b61054 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61010 bytes 818242f9
+ 00b61054 bytes 81a242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ceeb07f3592b1e6e55c68c72ce283373"></a>

### [`00b6106c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6106c.md) → [`00b610b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b610b0.md) _ZN8firebase4auth10authresult10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b610cc",
      "incomplete_value": false,
      "site": "00b610d0",
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
      "definition_site": "00b61088",
      "incomplete_value": false,
      "site": "00b6108c",
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
      "definition_site": "00b610dc",
      "incomplete_value": true,
      "site": "00b610e8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b61098",
      "incomplete_value": true,
      "site": "00b610a4",
      "value": [
        "LOAD",
        "8",
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
      "00b610cc",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b610dc",
      "DATA",
      [
        "storage",
        "010a1528",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b610cc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b610dc",
      "DATA",
      [
        "storage",
        "010a1568",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6108c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6106c.md#insn-00b6108c) · [`00b61088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6106c.md#insn-00b61088) · [`00b61094`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6106c.md#insn-00b61094)
- 新版 `00b610d0`（命令位置の公開資料なし） · `00b610cc`（命令位置の公開資料なし） · `00b610d8`（命令位置の公開資料なし）

~~~diff
- 00b6108c ["INT_ADD", "register:40f0:8", ["const:b6108c:8", "const:4:8"]]
- 00b6108c ["CALL", null, ["callee:00bde180:8"]]
+ 00b610d0 ["INT_ADD", "register:40f0:8", ["const:b610d0:8", "const:4:8"]]
+ 00b610d0 ["CALL", null, ["callee:00bde180:8"]]
- 00b6108c bytes 29f40194
+ 00b610d0 bytes 2cf40194
- 00b61088 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b61088 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b61088 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b61088 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b610cc ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b610cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b610cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b610cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b61088 bytes 00fc1991
+ 00b610cc bytes 00c81791
- 00b61094 ["COPY", "tmp:0:8", ["const:528:8"]]
- 00b61094 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b61094 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b61094 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b610d8 ["COPY", "tmp:0:8", ["const:568:8"]]
+ 00b610d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b610d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b610d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b61094 bytes 08a11491
+ 00b610d8 bytes 08a11591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f6a3be5d0de3613bc5375e182bbfcd1"></a>

### [`00b610a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b610a8.md) → [`00b610ec`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b610ec.md) _ZN8firebase4auth20additional_user_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocato

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
      "definition_site": "00b61118",
      "incomplete_value": true,
      "site": "00b61118",
      "value": [
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
      "definition_site": "00b610d4",
      "incomplete_value": true,
      "site": "00b610d4",
      "value": [
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
      "definition_site": "00b61100",
      "incomplete_value": true,
      "site": "00b61100",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b610bc",
      "incomplete_value": true,
      "site": "00b610bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b6110c",
      "incomplete_value": false,
      "site": "00b61110",
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
            "const:74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b610c8",
      "incomplete_value": false,
      "site": "00b610cc",
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
            "const:76:8"
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
      "00b610fc",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6110c",
      "PARAM",
      [
        "storage",
        "0029c076",
        null,
        "string"
      ]
    ],
    [
      "00b61118",
      "WRITE",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b610fc",
      "READ",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6110c",
      "PARAM",
      [
        "storage",
        "0029c074",
        null,
        "string"
      ]
    ],
    [
      "00b61118",
      "WRITE",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b610cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b610a8.md#insn-00b610cc) · [`00b610d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b610a8.md#insn-00b610d4) · [`00b610b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b610a8.md#insn-00b610b8)
- 新版 `00b61110`（命令位置の公開資料なし） · `00b61118`（命令位置の公開資料なし） · `00b610fc`（命令位置の公開資料なし）

~~~diff
- 00b610cc ["INT_ADD", "register:40f0:8", ["const:b610cc:8", "const:4:8"]]
- 00b610cc ["CALL", null, ["callee:00bde090:8"]]
+ 00b61110 ["INT_ADD", "register:40f0:8", ["const:b61110:8", "const:4:8"]]
+ 00b61110 ["CALL", null, ["callee:00bde090:8"]]
- 00b610cc bytes ddf30194
+ 00b61110 bytes e0f30194
- 00b610d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00b610d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00b61118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b610d4 bytes 609a02f9
+ 00b61118 bytes 60ba02f9
- 00b610b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00b610b8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b610fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00b610fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b610b8 bytes 689a42f9
+ 00b610fc bytes 68ba42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1e47902ed80752097a69a71bfe6bd8b"></a>

### [`00b610e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b610e8.md) → [`00b6112c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6112c.md) _ZN8firebase4auth20additional_user_info19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocato

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
      "definition_site": "00b61158",
      "incomplete_value": true,
      "site": "00b61158",
      "value": [
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
      "definition_site": "00b61114",
      "incomplete_value": true,
      "site": "00b61114",
      "value": [
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
      "definition_site": "00b61140",
      "incomplete_value": true,
      "site": "00b61140",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b610fc",
      "incomplete_value": true,
      "site": "00b610fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61148",
      "incomplete_value": false,
      "site": "00b61150",
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
            "const:74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61104",
      "incomplete_value": false,
      "site": "00b6110c",
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
            "const:76:8"
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
      "00b6113c",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61148",
      "PARAM",
      [
        "storage",
        "0029c076",
        null,
        "string"
      ]
    ],
    [
      "00b61158",
      "WRITE",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6113c",
      "READ",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61148",
      "PARAM",
      [
        "storage",
        "0029c074",
        null,
        "string"
      ]
    ],
    [
      "00b61158",
      "WRITE",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6110c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b610e8.md#insn-00b6110c) · [`00b61114`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b610e8.md#insn-00b61114) · [`00b610f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b610e8.md#insn-00b610f8)
- 新版 `00b61150`（命令位置の公開資料なし） · `00b61158`（命令位置の公開資料なし） · `00b6113c`（命令位置の公開資料なし）

~~~diff
- 00b6110c ["INT_ADD", "register:40f0:8", ["const:b6110c:8", "const:4:8"]]
- 00b6110c ["CALL", null, ["callee:00bde090:8"]]
+ 00b61150 ["INT_ADD", "register:40f0:8", ["const:b61150:8", "const:4:8"]]
+ 00b61150 ["CALL", null, ["callee:00bde090:8"]]
- 00b6110c bytes cdf30194
+ 00b61150 bytes d0f30194
- 00b61114 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00b61114 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61158 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00b61158 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61114 bytes 609a02f9
+ 00b61158 bytes 60ba02f9
- 00b610f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00b610f8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6113c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00b6113c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b610f8 bytes 689a42f9
+ 00b6113c bytes 68ba42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4e0dd7fe7f339a111f9689986a47387"></a>

### [`00b61128`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61128.md) → [`00b6116c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6116c.md) _ZN8firebase4auth20additional_user_info10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b6119c",
      "incomplete_value": true,
      "site": "00b6119c",
      "value": [
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
      "definition_site": "00b61158",
      "incomplete_value": true,
      "site": "00b61158",
      "value": [
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
      "definition_site": "00b61180",
      "incomplete_value": true,
      "site": "00b61180",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6113c",
      "incomplete_value": true,
      "site": "00b6113c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b6118c",
      "incomplete_value": false,
      "site": "00b61194",
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
            "const:74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61148",
      "incomplete_value": false,
      "site": "00b61150",
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
            "const:76:8"
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
      "00b6117c",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6118c",
      "PARAM",
      [
        "storage",
        "0029c076",
        null,
        "string"
      ]
    ],
    [
      "00b6119c",
      "WRITE",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6117c",
      "READ",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6118c",
      "PARAM",
      [
        "storage",
        "0029c074",
        null,
        "string"
      ]
    ],
    [
      "00b6119c",
      "WRITE",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61150`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61128.md#insn-00b61150) · [`00b61158`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61128.md#insn-00b61158) · [`00b61138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61128.md#insn-00b61138)
- 新版 `00b61194`（命令位置の公開資料なし） · `00b6119c`（命令位置の公開資料なし） · `00b6117c`（命令位置の公開資料なし）

~~~diff
- 00b61150 ["INT_ADD", "register:40f0:8", ["const:b61150:8", "const:4:8"]]
- 00b61150 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61194 ["INT_ADD", "register:40f0:8", ["const:b61194:8", "const:4:8"]]
+ 00b61194 ["CALL", null, ["callee:00bde090:8"]]
- 00b61150 bytes bcf30194
+ 00b61194 bytes bff30194
- 00b61158 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00b61158 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6119c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00b6119c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61158 bytes 609a02f9
+ 00b6119c bytes 60ba02f9
- 00b61138 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00b61138 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6117c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00b6117c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61138 bytes 689a42f9
+ 00b6117c bytes 68ba42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8dcabba7ea23f47ca227bd98310749ab"></a>

### [`00b6116c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6116c.md) → [`00b611b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b611b0.md) _ZN8firebase4auth20additional_user_info10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b611e0",
      "incomplete_value": true,
      "site": "00b611e0",
      "value": [
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
      "definition_site": "00b6119c",
      "incomplete_value": true,
      "site": "00b6119c",
      "value": [
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
      "definition_site": "00b611c4",
      "incomplete_value": true,
      "site": "00b611c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61180",
      "incomplete_value": true,
      "site": "00b61180",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b611cc",
      "incomplete_value": false,
      "site": "00b611d8",
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
            "const:74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61188",
      "incomplete_value": false,
      "site": "00b61194",
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
            "const:76:8"
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
      "00b611c0",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b611cc",
      "PARAM",
      [
        "storage",
        "0029c076",
        null,
        "string"
      ]
    ],
    [
      "00b611e0",
      "WRITE",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b611c0",
      "READ",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ],
    [
      "00b611cc",
      "PARAM",
      [
        "storage",
        "0029c074",
        null,
        "string"
      ]
    ],
    [
      "00b611e0",
      "WRITE",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6116c.md#insn-00b61194) · [`00b6119c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6116c.md#insn-00b6119c) · [`00b6117c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6116c.md#insn-00b6117c)
- 新版 `00b611d8`（命令位置の公開資料なし） · `00b611e0`（命令位置の公開資料なし） · `00b611c0`（命令位置の公開資料なし）

~~~diff
- 00b61194 ["INT_ADD", "register:40f0:8", ["const:b61194:8", "const:4:8"]]
- 00b61194 ["CALL", null, ["callee:00bde090:8"]]
+ 00b611d8 ["INT_ADD", "register:40f0:8", ["const:b611d8:8", "const:4:8"]]
+ 00b611d8 ["CALL", null, ["callee:00bde090:8"]]
- 00b61194 bytes abf30194
+ 00b611d8 bytes aef30194
- 00b6119c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00b6119c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b611e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00b611e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6119c bytes 609a02f9
+ 00b611e0 bytes 60ba02f9
- 00b6117c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:530:8"]]
- 00b6117c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b611c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:570:8"]]
+ 00b611c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6117c bytes 689a42f9
+ 00b611c0 bytes 68ba42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6895a543eaa71cf33bd4b48398fe74e"></a>

### [`00b611bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b611bc.md) → [`00b61200`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61200.md) _ZN8firebase4auth20additional_user_info15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b61258",
      "incomplete_value": true,
      "site": "00b61258",
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
      "definition_site": "00b61214",
      "incomplete_value": true,
      "site": "00b61214",
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
      "definition_site": "00b61234",
      "incomplete_value": true,
      "site": "00b61240",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:570:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b611f0",
      "incomplete_value": true,
      "site": "00b611fc",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b61214",
      "READ",
      [
        "storage",
        "010a1538",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61234",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61258",
      "WRITE",
      [
        "storage",
        "010a1538",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b61214",
      "READ",
      [
        "storage",
        "010a1578",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61234",
      "READ",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61258",
      "WRITE",
      [
        "storage",
        "010a1578",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b611d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b611bc.md#insn-00b611d0) · [`00b611fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b611bc.md#insn-00b611fc) · [`00b61214`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b611bc.md#insn-00b61214)
- 新版 `00b61214`（命令位置の公開資料なし） · `00b61240`（命令位置の公開資料なし） · `00b61258`（命令位置の公開資料なし）

~~~diff
- 00b611d0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:538:8"]]
- 00b611d0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b611d0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b61214 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:578:8"]]
+ 00b61214 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b61214 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b611d0 bytes a8e25439
+ 00b61214 bytes a8e25539
- 00b611fc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b611fc ["INT_ADD", "register:40f0:8", ["const:b611fc:8", "const:4:8"]]
- 00b611fc ["CALLIND", null, ["register:0:8"]]
+ 00b61240 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b61240 ["INT_ADD", "register:40f0:8", ["const:b61240:8", "const:4:8"]]
+ 00b61240 ["CALLIND", null, ["register:0:8"]]
- 00b611fc bytes 00013fd6
+ 00b61240 bytes 00013fd6
- 00b61214 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b61214 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:538:8"]]
- 00b61214 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b61258 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b61258 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:578:8"]]
+ 00b61258 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b61214 bytes a0e21439
+ 00b61258 bytes a0e21539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b42a1c9e3ec4f82fc61ad561df398948"></a>

### [`00b61228`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61228.md) → [`00b6126c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6126c.md) _ZN8firebase4auth20additional_user_info12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde0e0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0e0.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.71% / 新版 85.71%

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
      "definition_site": "00b612a8",
      "incomplete_value": true,
      "site": "00b612a8",
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
      "definition_site": "00b61264",
      "incomplete_value": true,
      "site": "00b61264",
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
      "definition_site": "00b612c8",
      "incomplete_value": true,
      "site": "00b612c8",
      "value": [
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
      "definition_site": "00b61284",
      "incomplete_value": true,
      "site": "00b61284",
      "value": [
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
      "definition_site": "00b61284",
      "incomplete_value": true,
      "site": "00b61284",
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
      "definition_site": "00b61240",
      "incomplete_value": true,
      "site": "00b61240",
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
      "00b61280",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6128c",
      "READ",
      [
        "storage",
        "010a1538",
        null,
        "undefined1"
      ]
    ],
    [
      "00b612a8",
      "WRITE",
      [
        "storage",
        "010a1538",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b61280",
      "READ",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6128c",
      "READ",
      [
        "storage",
        "010a1578",
        null,
        "undefined1"
      ]
    ],
    [
      "00b612a8",
      "WRITE",
      [
        "storage",
        "010a1578",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6123c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61228.md#insn-00b6123c) · [`00b61264`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61228.md#insn-00b61264) · [`00b61280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61228.md#insn-00b61280)
- 新版 `00b61280`（命令位置の公開資料なし） · `00b612a8`（命令位置の公開資料なし） · `00b612c4`（命令位置の公開資料なし）

~~~diff
- 00b6123c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00b6123c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61280 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
+ 00b61280 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6123c bytes 819a42f9
+ 00b61280 bytes 81ba42f9
- 00b61264 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b61264 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b61264 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:538:8"]]
- 00b61264 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b612a8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b612a8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b612a8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:578:8"]]
+ 00b612a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b61264 bytes bfe21439
+ 00b612a8 bytes bfe21539
- 00b61280 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61280 ["INT_ADD", "register:40f0:8", ["const:b61280:8", "const:4:8"]]
- 00b61280 ["CALLIND", null, ["register:0:8"]]
+ 00b612c4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b612c4 ["INT_ADD", "register:40f0:8", ["const:b612c4:8", "const:4:8"]]
+ 00b612c4 ["CALLIND", null, ["register:0:8"]]
- 00b61280 bytes 00013fd6
+ 00b612c4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d8291a3567c54f9b3fe72f28f727002"></a>

### [`00b61298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61298.md) → [`00b612dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b612dc.md) _ZN8firebase4auth20additional_user_info14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b6131c",
      "incomplete_value": true,
      "site": "00b6131c",
      "value": [
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
      "definition_site": "00b612d8",
      "incomplete_value": true,
      "site": "00b612d8",
      "value": [
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
      "definition_site": "00b612f8",
      "incomplete_value": true,
      "site": "00b612f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b612b4",
      "incomplete_value": true,
      "site": "00b612b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61300",
      "incomplete_value": false,
      "site": "00b61314",
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
            "const:74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b612bc",
      "incomplete_value": false,
      "site": "00b612d0",
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
            "const:76:8"
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
      "00b612f0",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61300",
      "PARAM",
      [
        "storage",
        "0029c076",
        null,
        "string"
      ]
    ],
    [
      "00b6131c",
      "WRITE",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b612f0",
      "READ",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61300",
      "PARAM",
      [
        "storage",
        "0029c074",
        null,
        "string"
      ]
    ],
    [
      "00b6131c",
      "WRITE",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b612d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61298.md#insn-00b612d0) · [`00b612d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61298.md#insn-00b612d8) · [`00b612ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61298.md#insn-00b612ac)
- 新版 `00b61314`（命令位置の公開資料なし） · `00b6131c`（命令位置の公開資料なし） · `00b612f0`（命令位置の公開資料なし）

~~~diff
- 00b612d0 ["INT_ADD", "register:40f0:8", ["const:b612d0:8", "const:4:8"]]
- 00b612d0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61314 ["INT_ADD", "register:40f0:8", ["const:b61314:8", "const:4:8"]]
+ 00b61314 ["CALL", null, ["callee:00bde090:8"]]
- 00b612d0 bytes 5cf30194
+ 00b61314 bytes 5ff30194
- 00b612d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00b612d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6131c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
+ 00b6131c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b612d8 bytes 809a02f9
+ 00b6131c bytes 80ba02f9
- 00b612ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00b612ac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b612f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
+ 00b612f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b612ac bytes 819a42f9
+ 00b612f0 bytes 81ba42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fe5ee15da57c32fcdaed46e7429460f"></a>

### [`00b61308`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61308.md) → [`00b6134c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6134c.md) _ZN8firebase4auth20additional_user_info11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b61368",
      "incomplete_value": false,
      "site": "00b6136c",
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
      "definition_site": "00b61324",
      "incomplete_value": false,
      "site": "00b61328",
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
      "definition_site": "00b61378",
      "incomplete_value": true,
      "site": "00b61384",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b61334",
      "incomplete_value": true,
      "site": "00b61340",
      "value": [
        "LOAD",
        "8",
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
      "00b61368",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b61378",
      "DATA",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61368",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b61378",
      "DATA",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61328`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61308.md#insn-00b61328) · [`00b61324`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61308.md#insn-00b61324) · [`00b61330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61308.md#insn-00b61330)
- 新版 `00b6136c`（命令位置の公開資料なし） · `00b61368`（命令位置の公開資料なし） · `00b61374`（命令位置の公開資料なし）

~~~diff
- 00b61328 ["INT_ADD", "register:40f0:8", ["const:b61328:8", "const:4:8"]]
- 00b61328 ["CALL", null, ["callee:00bde180:8"]]
+ 00b6136c ["INT_ADD", "register:40f0:8", ["const:b6136c:8", "const:4:8"]]
+ 00b6136c ["CALL", null, ["callee:00bde180:8"]]
- 00b61328 bytes 82f30194
+ 00b6136c bytes 85f30194
- 00b61324 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b61324 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b61324 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b61324 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b61368 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b61368 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61368 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61368 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b61324 bytes 00501791
+ 00b61368 bytes 001c1591
- 00b61330 ["COPY", "tmp:0:8", ["const:540:8"]]
- 00b61330 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b61330 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b61330 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b61374 ["COPY", "tmp:0:8", ["const:580:8"]]
+ 00b61374 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61374 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61374 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b61330 bytes 08011591
+ 00b61374 bytes 08011691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff8cdad9c3a8c32d27f7fc025fa3df25"></a>

### [`00b61344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61344.md) → [`00b61388`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61388.md) _ZN8firebase4auth20additional_user_info13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b613c8",
      "incomplete_value": true,
      "site": "00b613c8",
      "value": [
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
      "definition_site": "00b61384",
      "incomplete_value": true,
      "site": "00b61384",
      "value": [
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
      "definition_site": "00b613a4",
      "incomplete_value": true,
      "site": "00b613a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61360",
      "incomplete_value": true,
      "site": "00b61360",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b613ac",
      "incomplete_value": false,
      "site": "00b613c0",
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
            "const:74:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61368",
      "incomplete_value": false,
      "site": "00b6137c",
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
            "const:76:8"
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
      "00b6139c",
      "READ",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ],
    [
      "00b613ac",
      "PARAM",
      [
        "storage",
        "0029c076",
        null,
        "string"
      ]
    ],
    [
      "00b613c8",
      "WRITE",
      [
        "storage",
        "010a1530",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6139c",
      "READ",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ],
    [
      "00b613ac",
      "PARAM",
      [
        "storage",
        "0029c074",
        null,
        "string"
      ]
    ],
    [
      "00b613c8",
      "WRITE",
      [
        "storage",
        "010a1570",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6137c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61344.md#insn-00b6137c) · [`00b61384`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61344.md#insn-00b61384) · [`00b61358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61344.md#insn-00b61358)
- 新版 `00b613c0`（命令位置の公開資料なし） · `00b613c8`（命令位置の公開資料なし） · `00b6139c`（命令位置の公開資料なし）

~~~diff
- 00b6137c ["INT_ADD", "register:40f0:8", ["const:b6137c:8", "const:4:8"]]
- 00b6137c ["CALL", null, ["callee:00bde090:8"]]
+ 00b613c0 ["INT_ADD", "register:40f0:8", ["const:b613c0:8", "const:4:8"]]
+ 00b613c0 ["CALL", null, ["callee:00bde090:8"]]
- 00b6137c bytes 31f30194
+ 00b613c0 bytes 34f30194
- 00b61384 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00b61384 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b613c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
+ 00b613c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61384 bytes 809a02f9
+ 00b613c8 bytes 80ba02f9
- 00b61358 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:530:8"]]
- 00b61358 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6139c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:570:8"]]
+ 00b6139c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61358 bytes 819a42f9
+ 00b6139c bytes 81ba42f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b268c372b11944fcea35201c830ed67"></a>

### [`00b613b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613b4.md) → [`00b613f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b613f8.md) _ZN8firebase4auth20additional_user_info10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b61414",
      "incomplete_value": false,
      "site": "00b61418",
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
      "definition_site": "00b613d0",
      "incomplete_value": false,
      "site": "00b613d4",
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
      "definition_site": "00b61424",
      "incomplete_value": true,
      "site": "00b61430",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b613e0",
      "incomplete_value": true,
      "site": "00b613ec",
      "value": [
        "LOAD",
        "8",
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
      "00b61414",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b61424",
      "DATA",
      [
        "storage",
        "010a1558",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b61414",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b61424",
      "DATA",
      [
        "storage",
        "010a1598",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b613d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613b4.md#insn-00b613d4) · [`00b613d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613b4.md#insn-00b613d0) · [`00b613dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613b4.md#insn-00b613dc)
- 新版 `00b61418`（命令位置の公開資料なし） · `00b61414`（命令位置の公開資料なし） · `00b61420`（命令位置の公開資料なし）

~~~diff
- 00b613d4 ["INT_ADD", "register:40f0:8", ["const:b613d4:8", "const:4:8"]]
- 00b613d4 ["CALL", null, ["callee:00bde180:8"]]
+ 00b61418 ["INT_ADD", "register:40f0:8", ["const:b61418:8", "const:4:8"]]
+ 00b61418 ["CALL", null, ["callee:00bde180:8"]]
- 00b613d4 bytes 57f30194
+ 00b61418 bytes 5af30194
- 00b613d0 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b613d0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b613d0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b613d0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b61414 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b61414 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61414 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61414 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b613d0 bytes 00fc1991
+ 00b61414 bytes 00c81791
- 00b613dc ["COPY", "tmp:0:8", ["const:558:8"]]
- 00b613dc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b613dc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b613dc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b61420 ["COPY", "tmp:0:8", ["const:598:8"]]
+ 00b61420 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61420 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61420 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b613dc bytes 08611591
+ 00b61420 bytes 08611691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58e0fa1e28eab6841d948a8b2f15cada"></a>

### [`00b613f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613f0.md) → [`00b61434`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61434.md) _ZN8firebase4auth27api_not_available_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

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
      "definition_site": "00b61460",
      "incomplete_value": true,
      "site": "00b61460",
      "value": [
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
      "definition_site": "00b6141c",
      "incomplete_value": true,
      "site": "00b6141c",
      "value": [
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
      "definition_site": "00b61448",
      "incomplete_value": true,
      "site": "00b61448",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61404",
      "incomplete_value": true,
      "site": "00b61404",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61454",
      "incomplete_value": false,
      "site": "00b61458",
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
            "const:739:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61410",
      "incomplete_value": false,
      "site": "00b61414",
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
            "const:7c6:8"
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
      "00b61444",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61454",
      "PARAM",
      [
        "storage",
        "002977c6",
        null,
        "string"
      ]
    ],
    [
      "00b61460",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61444",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61454",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00b61460",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61414`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613f0.md#insn-00b61414) · [`00b6141c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613f0.md#insn-00b6141c) · [`00b61400`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b613f0.md#insn-00b61400)
- 新版 `00b61458`（命令位置の公開資料なし） · `00b61460`（命令位置の公開資料なし） · `00b61444`（命令位置の公開資料なし）

~~~diff
- 00b61414 ["INT_ADD", "register:40f0:8", ["const:b61414:8", "const:4:8"]]
- 00b61414 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61458 ["INT_ADD", "register:40f0:8", ["const:b61458:8", "const:4:8"]]
+ 00b61458 ["CALL", null, ["callee:00bde090:8"]]
- 00b61414 bytes 0bf30194
+ 00b61458 bytes 0ef30194
- 00b6141c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00b6141c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61460 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b61460 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6141c bytes 60b202f9
+ 00b61460 bytes 60d202f9
- 00b61400 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00b61400 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61444 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b61444 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61400 bytes 68b242f9
+ 00b61444 bytes 68d242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a8831abbac46cb145af36cac646fe83"></a>

### [`00b61430`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61430.md) → [`00b61474`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61474.md) _ZN8firebase4auth27api_not_available_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9a

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
      "definition_site": "00b614a0",
      "incomplete_value": true,
      "site": "00b614a0",
      "value": [
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
      "definition_site": "00b6145c",
      "incomplete_value": true,
      "site": "00b6145c",
      "value": [
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
      "definition_site": "00b61488",
      "incomplete_value": true,
      "site": "00b61488",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61444",
      "incomplete_value": true,
      "site": "00b61444",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61490",
      "incomplete_value": false,
      "site": "00b61498",
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
            "const:739:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6144c",
      "incomplete_value": false,
      "site": "00b61454",
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
            "const:7c6:8"
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
      "00b61484",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61490",
      "PARAM",
      [
        "storage",
        "002977c6",
        null,
        "string"
      ]
    ],
    [
      "00b614a0",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61484",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61490",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00b614a0",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61454`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61430.md#insn-00b61454) · [`00b6145c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61430.md#insn-00b6145c) · [`00b61440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61430.md#insn-00b61440)
- 新版 `00b61498`（命令位置の公開資料なし） · `00b614a0`（命令位置の公開資料なし） · `00b61484`（命令位置の公開資料なし）

~~~diff
- 00b61454 ["INT_ADD", "register:40f0:8", ["const:b61454:8", "const:4:8"]]
- 00b61454 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61498 ["INT_ADD", "register:40f0:8", ["const:b61498:8", "const:4:8"]]
+ 00b61498 ["CALL", null, ["callee:00bde090:8"]]
- 00b61454 bytes fbf20194
+ 00b61498 bytes fef20194
- 00b6145c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00b6145c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b614a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b614a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6145c bytes 60b202f9
+ 00b614a0 bytes 60d202f9
- 00b61440 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00b61440 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61484 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b61484 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61440 bytes 68b242f9
+ 00b61484 bytes 68d242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ba132de47ae31a1b2b328d30c49e6b3a"></a>

### [`00b61470`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61470.md) → [`00b614b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b614b4.md) _ZN8firebase4auth27api_not_available_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b614e4",
      "incomplete_value": true,
      "site": "00b614e4",
      "value": [
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
      "definition_site": "00b614a0",
      "incomplete_value": true,
      "site": "00b614a0",
      "value": [
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
      "definition_site": "00b614c8",
      "incomplete_value": true,
      "site": "00b614c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61484",
      "incomplete_value": true,
      "site": "00b61484",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b614d4",
      "incomplete_value": false,
      "site": "00b614dc",
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
            "const:739:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61490",
      "incomplete_value": false,
      "site": "00b61498",
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
            "const:7c6:8"
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
      "00b614c4",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b614d4",
      "PARAM",
      [
        "storage",
        "002977c6",
        null,
        "string"
      ]
    ],
    [
      "00b614e4",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b614c4",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b614d4",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00b614e4",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61470.md#insn-00b61498) · [`00b614a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61470.md#insn-00b614a0) · [`00b61480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61470.md#insn-00b61480)
- 新版 `00b614dc`（命令位置の公開資料なし） · `00b614e4`（命令位置の公開資料なし） · `00b614c4`（命令位置の公開資料なし）

~~~diff
- 00b61498 ["INT_ADD", "register:40f0:8", ["const:b61498:8", "const:4:8"]]
- 00b61498 ["CALL", null, ["callee:00bde090:8"]]
+ 00b614dc ["INT_ADD", "register:40f0:8", ["const:b614dc:8", "const:4:8"]]
+ 00b614dc ["CALL", null, ["callee:00bde090:8"]]
- 00b61498 bytes eaf20194
+ 00b614dc bytes edf20194
- 00b614a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00b614a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b614e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b614e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b614a0 bytes 60b202f9
+ 00b614e4 bytes 60d202f9
- 00b61480 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00b61480 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b614c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b614c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61480 bytes 68b242f9
+ 00b614c4 bytes 68d242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a46e73f2754c1b4a3c82f71aaa3a11c"></a>

### [`00b614b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b614b4.md) → [`00b614f8`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b614f8.md) _ZN8firebase4auth27api_not_available_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b61528",
      "incomplete_value": true,
      "site": "00b61528",
      "value": [
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
      "definition_site": "00b614e4",
      "incomplete_value": true,
      "site": "00b614e4",
      "value": [
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
      "definition_site": "00b6150c",
      "incomplete_value": true,
      "site": "00b6150c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b614c8",
      "incomplete_value": true,
      "site": "00b614c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61514",
      "incomplete_value": false,
      "site": "00b61520",
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
            "const:739:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b614d0",
      "incomplete_value": false,
      "site": "00b614dc",
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
            "const:7c6:8"
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
      "00b61508",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61514",
      "PARAM",
      [
        "storage",
        "002977c6",
        null,
        "string"
      ]
    ],
    [
      "00b61528",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61508",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61514",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00b61528",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b614dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b614b4.md#insn-00b614dc) · [`00b614e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b614b4.md#insn-00b614e4) · [`00b614c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b614b4.md#insn-00b614c4)
- 新版 `00b61520`（命令位置の公開資料なし） · `00b61528`（命令位置の公開資料なし） · `00b61508`（命令位置の公開資料なし）

~~~diff
- 00b614dc ["INT_ADD", "register:40f0:8", ["const:b614dc:8", "const:4:8"]]
- 00b614dc ["CALL", null, ["callee:00bde090:8"]]
+ 00b61520 ["INT_ADD", "register:40f0:8", ["const:b61520:8", "const:4:8"]]
+ 00b61520 ["CALL", null, ["callee:00bde090:8"]]
- 00b614dc bytes d9f20194
+ 00b61520 bytes dcf20194
- 00b614e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00b614e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61528 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b61528 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b614e4 bytes 60b202f9
+ 00b61528 bytes 60d202f9
- 00b614c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:560:8"]]
- 00b614c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61508 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5a0:8"]]
+ 00b61508 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b614c4 bytes 68b242f9
+ 00b61508 bytes 68d242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05205ff03c9541bdaf80accf044b0139"></a>

### [`00b61504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61504.md) → [`00b61548`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61548.md) _ZN8firebase4auth27api_not_available_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b615a0",
      "incomplete_value": true,
      "site": "00b615a0",
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
      "definition_site": "00b6155c",
      "incomplete_value": true,
      "site": "00b6155c",
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
      "definition_site": "00b6157c",
      "incomplete_value": true,
      "site": "00b61588",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:5a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61538",
      "incomplete_value": true,
      "site": "00b61544",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b6155c",
      "READ",
      [
        "storage",
        "010a1568",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6157c",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b615a0",
      "WRITE",
      [
        "storage",
        "010a1568",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6155c",
      "READ",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6157c",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b615a0",
      "WRITE",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61504.md#insn-00b61518) · [`00b61544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61504.md#insn-00b61544) · [`00b6155c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61504.md#insn-00b6155c)
- 新版 `00b6155c`（命令位置の公開資料なし） · `00b61588`（命令位置の公開資料なし） · `00b615a0`（命令位置の公開資料なし）

~~~diff
- 00b61518 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:568:8"]]
- 00b61518 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b61518 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6155c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5a8:8"]]
+ 00b6155c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6155c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b61518 bytes a8a25539
+ 00b6155c bytes a8a25639
- 00b61544 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61544 ["INT_ADD", "register:40f0:8", ["const:b61544:8", "const:4:8"]]
- 00b61544 ["CALLIND", null, ["register:0:8"]]
+ 00b61588 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b61588 ["INT_ADD", "register:40f0:8", ["const:b61588:8", "const:4:8"]]
+ 00b61588 ["CALLIND", null, ["register:0:8"]]
- 00b61544 bytes 00013fd6
+ 00b61588 bytes 00013fd6
- 00b6155c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b6155c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:568:8"]]
- 00b6155c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b615a0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b615a0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5a8:8"]]
+ 00b615a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b6155c bytes a0a21539
+ 00b615a0 bytes a0a21639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83ffe35b13a7bb8b8c6f7e423fddd6a9"></a>

### [`00b61570`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61570.md) → [`00b615b4`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b615b4.md) _ZN8firebase4auth27api_not_available_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b615f0",
      "incomplete_value": true,
      "site": "00b615f0",
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
      "definition_site": "00b615ac",
      "incomplete_value": true,
      "site": "00b615ac",
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
      "definition_site": "00b61610",
      "incomplete_value": true,
      "site": "00b61610",
      "value": [
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
      "definition_site": "00b615cc",
      "incomplete_value": true,
      "site": "00b615cc",
      "value": [
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
      "definition_site": "00b615cc",
      "incomplete_value": true,
      "site": "00b615cc",
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
      "definition_site": "00b61588",
      "incomplete_value": true,
      "site": "00b61588",
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
      "00b615c8",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b615d4",
      "READ",
      [
        "storage",
        "010a1568",
        null,
        "undefined1"
      ]
    ],
    [
      "00b615f0",
      "WRITE",
      [
        "storage",
        "010a1568",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b615c8",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b615d4",
      "READ",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b615f0",
      "WRITE",
      [
        "storage",
        "010a15a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61584`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61570.md#insn-00b61584) · [`00b615ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61570.md#insn-00b615ac) · [`00b615c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61570.md#insn-00b615c8)
- 新版 `00b615c8`（命令位置の公開資料なし） · `00b615f0`（命令位置の公開資料なし） · `00b6160c`（命令位置の公開資料なし）

~~~diff
- 00b61584 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00b61584 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b615c8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
+ 00b615c8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61584 bytes 81b242f9
+ 00b615c8 bytes 81d242f9
- 00b615ac ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b615ac ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b615ac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:568:8"]]
- 00b615ac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b615f0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b615f0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b615f0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5a8:8"]]
+ 00b615f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b615ac bytes bfa21539
+ 00b615f0 bytes bfa21639
- 00b615c8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b615c8 ["INT_ADD", "register:40f0:8", ["const:b615c8:8", "const:4:8"]]
- 00b615c8 ["CALLIND", null, ["register:0:8"]]
+ 00b6160c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6160c ["INT_ADD", "register:40f0:8", ["const:b6160c:8", "const:4:8"]]
+ 00b6160c ["CALLIND", null, ["register:0:8"]]
- 00b615c8 bytes 00013fd6
+ 00b6160c bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9e7ad15d951587b5b2117fa272450b7e"></a>

### [`00b615e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b615e0.md) → [`00b61624`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61624.md) _ZN8firebase4auth27api_not_available_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b61664",
      "incomplete_value": true,
      "site": "00b61664",
      "value": [
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
      "definition_site": "00b61620",
      "incomplete_value": true,
      "site": "00b61620",
      "value": [
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
      "definition_site": "00b61640",
      "incomplete_value": true,
      "site": "00b61640",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b615fc",
      "incomplete_value": true,
      "site": "00b615fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61648",
      "incomplete_value": false,
      "site": "00b6165c",
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
            "const:739:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61604",
      "incomplete_value": false,
      "site": "00b61618",
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
            "const:7c6:8"
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
      "00b61638",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61648",
      "PARAM",
      [
        "storage",
        "002977c6",
        null,
        "string"
      ]
    ],
    [
      "00b61664",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61638",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61648",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00b61664",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61618`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b615e0.md#insn-00b61618) · [`00b61620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b615e0.md#insn-00b61620) · [`00b615f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b615e0.md#insn-00b615f4)
- 新版 `00b6165c`（命令位置の公開資料なし） · `00b61664`（命令位置の公開資料なし） · `00b61638`（命令位置の公開資料なし）

~~~diff
- 00b61618 ["INT_ADD", "register:40f0:8", ["const:b61618:8", "const:4:8"]]
- 00b61618 ["CALL", null, ["callee:00bde090:8"]]
+ 00b6165c ["INT_ADD", "register:40f0:8", ["const:b6165c:8", "const:4:8"]]
+ 00b6165c ["CALL", null, ["callee:00bde090:8"]]
- 00b61618 bytes 8af20194
+ 00b6165c bytes 8df20194
- 00b61620 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00b61620 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61664 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
+ 00b61664 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61620 bytes 80b202f9
+ 00b61664 bytes 80d202f9
- 00b615f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00b615f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61638 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
+ 00b61638 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b615f4 bytes 81b242f9
+ 00b61638 bytes 81d242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70bf0f1449ec805c4f080cc887123b49"></a>

### [`00b61650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61650.md) → [`00b61694`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61694.md) _ZN8firebase4auth27api_not_available_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b616b0",
      "incomplete_value": false,
      "site": "00b616b4",
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
      "definition_site": "00b6166c",
      "incomplete_value": false,
      "site": "00b61670",
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
      "definition_site": "00b616c0",
      "incomplete_value": true,
      "site": "00b616cc",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6167c",
      "incomplete_value": true,
      "site": "00b61688",
      "value": [
        "LOAD",
        "8",
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
      "00b616b0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b616c0",
      "DATA",
      [
        "storage",
        "010a1570",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b616b0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b616c0",
      "DATA",
      [
        "storage",
        "010a15b0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61670`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61650.md#insn-00b61670) · [`00b6166c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61650.md#insn-00b6166c) · [`00b61678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61650.md#insn-00b61678)
- 新版 `00b616b4`（命令位置の公開資料なし） · `00b616b0`（命令位置の公開資料なし） · `00b616bc`（命令位置の公開資料なし）

~~~diff
- 00b61670 ["INT_ADD", "register:40f0:8", ["const:b61670:8", "const:4:8"]]
- 00b61670 ["CALL", null, ["callee:00bde180:8"]]
+ 00b616b4 ["INT_ADD", "register:40f0:8", ["const:b616b4:8", "const:4:8"]]
+ 00b616b4 ["CALL", null, ["callee:00bde180:8"]]
- 00b61670 bytes b0f20194
+ 00b616b4 bytes b3f20194
- 00b6166c ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b6166c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6166c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6166c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b616b0 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b616b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b616b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b616b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6166c bytes 00501791
+ 00b616b0 bytes 001c1591
- 00b61678 ["COPY", "tmp:0:8", ["const:570:8"]]
- 00b61678 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b61678 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b61678 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b616bc ["COPY", "tmp:0:8", ["const:5b0:8"]]
+ 00b616bc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b616bc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b616bc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b61678 bytes 08c11591
+ 00b616bc bytes 08c11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d4fc75fcb116b636b8f58338db33f182"></a>

### [`00b6168c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6168c.md) → [`00b616d0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b616d0.md) _ZN8firebase4auth27api_not_available_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b61710",
      "incomplete_value": true,
      "site": "00b61710",
      "value": [
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
      "definition_site": "00b616cc",
      "incomplete_value": true,
      "site": "00b616cc",
      "value": [
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
      "definition_site": "00b616ec",
      "incomplete_value": true,
      "site": "00b616ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b616a8",
      "incomplete_value": true,
      "site": "00b616a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b616f4",
      "incomplete_value": false,
      "site": "00b61708",
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
            "const:739:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b616b0",
      "incomplete_value": false,
      "site": "00b616c4",
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
            "const:7c6:8"
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
      "00b616e4",
      "READ",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ],
    [
      "00b616f4",
      "PARAM",
      [
        "storage",
        "002977c6",
        null,
        "string"
      ]
    ],
    [
      "00b61710",
      "WRITE",
      [
        "storage",
        "010a1560",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b616e4",
      "READ",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b616f4",
      "PARAM",
      [
        "storage",
        "00297739",
        null,
        "string"
      ]
    ],
    [
      "00b61710",
      "WRITE",
      [
        "storage",
        "010a15a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b616c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6168c.md#insn-00b616c4) · [`00b616cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6168c.md#insn-00b616cc) · [`00b616a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6168c.md#insn-00b616a0)
- 新版 `00b61708`（命令位置の公開資料なし） · `00b61710`（命令位置の公開資料なし） · `00b616e4`（命令位置の公開資料なし）

~~~diff
- 00b616c4 ["INT_ADD", "register:40f0:8", ["const:b616c4:8", "const:4:8"]]
- 00b616c4 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61708 ["INT_ADD", "register:40f0:8", ["const:b61708:8", "const:4:8"]]
+ 00b61708 ["CALL", null, ["callee:00bde090:8"]]
- 00b616c4 bytes 5ff20194
+ 00b61708 bytes 62f20194
- 00b616cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00b616cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61710 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
+ 00b61710 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b616cc bytes 80b202f9
+ 00b61710 bytes 80d202f9
- 00b616a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:560:8"]]
- 00b616a0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b616e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5a0:8"]]
+ 00b616e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b616a0 bytes 81b242f9
+ 00b616e4 bytes 81d242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4703bdf888838d840c0fb4fb8386d7a2"></a>

### [`00b616fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b616fc.md) → [`00b61740`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61740.md) _ZN8firebase4auth27api_not_available_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b6175c",
      "incomplete_value": false,
      "site": "00b61760",
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
      "definition_site": "00b61718",
      "incomplete_value": false,
      "site": "00b6171c",
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
      "definition_site": "00b6176c",
      "incomplete_value": true,
      "site": "00b61778",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b61728",
      "incomplete_value": true,
      "site": "00b61734",
      "value": [
        "LOAD",
        "8",
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
      "00b6175c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6176c",
      "DATA",
      [
        "storage",
        "010a1578",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6175c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b6176c",
      "DATA",
      [
        "storage",
        "010a15b8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6171c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b616fc.md#insn-00b6171c) · [`00b61718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b616fc.md#insn-00b61718) · [`00b61724`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b616fc.md#insn-00b61724)
- 新版 `00b61760`（命令位置の公開資料なし） · `00b6175c`（命令位置の公開資料なし） · `00b61768`（命令位置の公開資料なし）

~~~diff
- 00b6171c ["INT_ADD", "register:40f0:8", ["const:b6171c:8", "const:4:8"]]
- 00b6171c ["CALL", null, ["callee:00bde180:8"]]
+ 00b61760 ["INT_ADD", "register:40f0:8", ["const:b61760:8", "const:4:8"]]
+ 00b61760 ["CALL", null, ["callee:00bde180:8"]]
- 00b6171c bytes 85f20194
+ 00b61760 bytes 88f20194
- 00b61718 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b61718 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b61718 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b61718 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6175c ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b6175c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6175c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6175c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b61718 bytes 00fc1991
+ 00b6175c bytes 00c81791
- 00b61724 ["COPY", "tmp:0:8", ["const:578:8"]]
- 00b61724 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b61724 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b61724 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b61768 ["COPY", "tmp:0:8", ["const:5b8:8"]]
+ 00b61768 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61768 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61768 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b61724 bytes 08e11591
+ 00b61768 bytes 08e11691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19e7083b88d4cf3f835747eb8107959a"></a>

### [`00b61738`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61738.md) → [`00b6177c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6177c.md) _ZN8firebase4auth21action_code_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b617a8",
      "incomplete_value": true,
      "site": "00b617a8",
      "value": [
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
      "definition_site": "00b61764",
      "incomplete_value": true,
      "site": "00b61764",
      "value": [
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
      "definition_site": "00b61790",
      "incomplete_value": true,
      "site": "00b61790",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6174c",
      "incomplete_value": true,
      "site": "00b6174c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b6179c",
      "incomplete_value": true,
      "site": "00b617a0",
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
            "const:4fa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61758",
      "incomplete_value": true,
      "site": "00b6175c",
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
            "const:587:8"
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
      "00b6178c",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6179c",
      "PARAM",
      [
        "storage",
        "00295587",
        null,
        "string"
      ]
    ],
    [
      "00b617a8",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6178c",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6179c",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ],
    [
      "00b617a8",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6175c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61738.md#insn-00b6175c) · [`00b61764`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61738.md#insn-00b61764) · [`00b61748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61738.md#insn-00b61748)
- 新版 `00b617a0`（命令位置の公開資料なし） · `00b617a8`（命令位置の公開資料なし） · `00b6178c`（命令位置の公開資料なし）

~~~diff
- 00b6175c ["INT_ADD", "register:40f0:8", ["const:b6175c:8", "const:4:8"]]
- 00b6175c ["CALL", null, ["callee:00bde090:8"]]
+ 00b617a0 ["INT_ADD", "register:40f0:8", ["const:b617a0:8", "const:4:8"]]
+ 00b617a0 ["CALL", null, ["callee:00bde090:8"]]
- 00b6175c bytes 39f20194
+ 00b617a0 bytes 3cf20194
- 00b61764 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b61764 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b617a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b617a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61764 bytes 60c202f9
+ 00b617a8 bytes 60e202f9
- 00b61748 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b61748 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6178c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b6178c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61748 bytes 68c242f9
+ 00b6178c bytes 68e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c298a89f04526a8f814b1290e271a624"></a>

### [`00b61778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61778.md) → [`00b617bc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b617bc.md) _ZN8firebase4auth21action_code_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b617e8",
      "incomplete_value": true,
      "site": "00b617e8",
      "value": [
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
      "definition_site": "00b617a4",
      "incomplete_value": true,
      "site": "00b617a4",
      "value": [
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
      "definition_site": "00b617d0",
      "incomplete_value": true,
      "site": "00b617d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6178c",
      "incomplete_value": true,
      "site": "00b6178c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b617d8",
      "incomplete_value": false,
      "site": "00b617e0",
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
            "const:4fa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61794",
      "incomplete_value": false,
      "site": "00b6179c",
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
            "const:587:8"
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
      "00b617cc",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b617d8",
      "PARAM",
      [
        "storage",
        "00295587",
        null,
        "string"
      ]
    ],
    [
      "00b617e8",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b617cc",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b617d8",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ],
    [
      "00b617e8",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6179c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61778.md#insn-00b6179c) · [`00b617a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61778.md#insn-00b617a4) · [`00b61788`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61778.md#insn-00b61788)
- 新版 `00b617e0`（命令位置の公開資料なし） · `00b617e8`（命令位置の公開資料なし） · `00b617cc`（命令位置の公開資料なし）

~~~diff
- 00b6179c ["INT_ADD", "register:40f0:8", ["const:b6179c:8", "const:4:8"]]
- 00b6179c ["CALL", null, ["callee:00bde090:8"]]
+ 00b617e0 ["INT_ADD", "register:40f0:8", ["const:b617e0:8", "const:4:8"]]
+ 00b617e0 ["CALL", null, ["callee:00bde090:8"]]
- 00b6179c bytes 29f20194
+ 00b617e0 bytes 2cf20194
- 00b617a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b617a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b617e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b617e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b617a4 bytes 60c202f9
+ 00b617e8 bytes 60e202f9
- 00b61788 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b61788 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b617cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b617cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b61788 bytes 68c242f9
+ 00b617cc bytes 68e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-712863300e59a5b562702b2187c40648"></a>

### [`00b617b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617b8.md) → [`00b617fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b617fc.md) _ZN8firebase4auth21action_code_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

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
      "definition_site": "00b6182c",
      "incomplete_value": true,
      "site": "00b6182c",
      "value": [
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
      "definition_site": "00b617e8",
      "incomplete_value": true,
      "site": "00b617e8",
      "value": [
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
      "definition_site": "00b61810",
      "incomplete_value": true,
      "site": "00b61810",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b617cc",
      "incomplete_value": true,
      "site": "00b617cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b6181c",
      "incomplete_value": false,
      "site": "00b61824",
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
            "const:4fa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b617d8",
      "incomplete_value": false,
      "site": "00b617e0",
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
            "const:587:8"
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
      "00b6180c",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6181c",
      "PARAM",
      [
        "storage",
        "00295587",
        null,
        "string"
      ]
    ],
    [
      "00b6182c",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6180c",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6181c",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ],
    [
      "00b6182c",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b617e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617b8.md#insn-00b617e0) · [`00b617e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617b8.md#insn-00b617e8) · [`00b617c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617b8.md#insn-00b617c8)
- 新版 `00b61824`（命令位置の公開資料なし） · `00b6182c`（命令位置の公開資料なし） · `00b6180c`（命令位置の公開資料なし）

~~~diff
- 00b617e0 ["INT_ADD", "register:40f0:8", ["const:b617e0:8", "const:4:8"]]
- 00b617e0 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61824 ["INT_ADD", "register:40f0:8", ["const:b61824:8", "const:4:8"]]
+ 00b61824 ["CALL", null, ["callee:00bde090:8"]]
- 00b617e0 bytes 18f20194
+ 00b61824 bytes 1bf20194
- 00b617e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b617e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6182c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b6182c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b617e8 bytes 60c202f9
+ 00b6182c bytes 60e202f9
- 00b617c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b617c8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6180c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b6180c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b617c8 bytes 68c242f9
+ 00b6180c bytes 68e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6c4aa69439461c653ff4bc604785117"></a>

### [`00b617fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617fc.md) → [`00b61840`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61840.md) _ZN8firebase4auth21action_code_exception10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b61870",
      "incomplete_value": true,
      "site": "00b61870",
      "value": [
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
      "definition_site": "00b6182c",
      "incomplete_value": true,
      "site": "00b6182c",
      "value": [
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
      "definition_site": "00b61854",
      "incomplete_value": true,
      "site": "00b61854",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61810",
      "incomplete_value": true,
      "site": "00b61810",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b6185c",
      "incomplete_value": false,
      "site": "00b61868",
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
            "const:4fa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61818",
      "incomplete_value": false,
      "site": "00b61824",
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
            "const:587:8"
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
      "00b61850",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6185c",
      "PARAM",
      [
        "storage",
        "00295587",
        null,
        "string"
      ]
    ],
    [
      "00b61870",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61850",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6185c",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ],
    [
      "00b61870",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61824`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617fc.md#insn-00b61824) · [`00b6182c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617fc.md#insn-00b6182c) · [`00b6180c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b617fc.md#insn-00b6180c)
- 新版 `00b61868`（命令位置の公開資料なし） · `00b61870`（命令位置の公開資料なし） · `00b61850`（命令位置の公開資料なし）

~~~diff
- 00b61824 ["INT_ADD", "register:40f0:8", ["const:b61824:8", "const:4:8"]]
- 00b61824 ["CALL", null, ["callee:00bde090:8"]]
+ 00b61868 ["INT_ADD", "register:40f0:8", ["const:b61868:8", "const:4:8"]]
+ 00b61868 ["CALL", null, ["callee:00bde090:8"]]
- 00b61824 bytes 07f20194
+ 00b61868 bytes 0af20194
- 00b6182c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b6182c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61870 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b61870 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6182c bytes 60c202f9
+ 00b61870 bytes 60e202f9
- 00b6180c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:580:8"]]
- 00b6180c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61850 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:5c0:8"]]
+ 00b61850 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6180c bytes 68c242f9
+ 00b61850 bytes 68e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46b8cbcd313f6f0e6123f7c581bbaa99"></a>

### [`00b6184c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6184c.md) → [`00b61890`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61890.md) _ZN8firebase4auth21action_code_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b618e8",
      "incomplete_value": true,
      "site": "00b618e8",
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
      "definition_site": "00b618a4",
      "incomplete_value": true,
      "site": "00b618a4",
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b618c4",
      "incomplete_value": true,
      "site": "00b618d0",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:5c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b61880",
      "incomplete_value": true,
      "site": "00b6188c",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:580:8"
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
      "00b618a4",
      "READ",
      [
        "storage",
        "010a1588",
        null,
        "undefined1"
      ]
    ],
    [
      "00b618c4",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b618e8",
      "WRITE",
      [
        "storage",
        "010a1588",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b618a4",
      "READ",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b618c4",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b618e8",
      "WRITE",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61860`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6184c.md#insn-00b61860) · [`00b6188c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6184c.md#insn-00b6188c) · [`00b618a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b6184c.md#insn-00b618a4)
- 新版 `00b618a4`（命令位置の公開資料なし） · `00b618d0`（命令位置の公開資料なし） · `00b618e8`（命令位置の公開資料なし）

~~~diff
- 00b61860 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:588:8"]]
- 00b61860 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b61860 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b618a4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:5c8:8"]]
+ 00b618a4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b618a4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b61860 bytes a8225639
+ 00b618a4 bytes a8225739
- 00b6188c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6188c ["INT_ADD", "register:40f0:8", ["const:b6188c:8", "const:4:8"]]
- 00b6188c ["CALLIND", null, ["register:0:8"]]
+ 00b618d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b618d0 ["INT_ADD", "register:40f0:8", ["const:b618d0:8", "const:4:8"]]
+ 00b618d0 ["CALLIND", null, ["register:0:8"]]
- 00b6188c bytes 00013fd6
+ 00b618d0 bytes 00013fd6
- 00b618a4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b618a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:588:8"]]
- 00b618a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b618e8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b618e8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:5c8:8"]]
+ 00b618e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b618a4 bytes a0221639
+ 00b618e8 bytes a0221739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8eb7a82cb8d456f4b94cf9294cf406cb"></a>

### [`00b618b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b618b8.md) → [`00b618fc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b618fc.md) _ZN8firebase4auth21action_code_exception12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b61938",
      "incomplete_value": true,
      "site": "00b61938",
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
      "definition_site": "00b618f4",
      "incomplete_value": true,
      "site": "00b618f4",
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
      "definition_site": "00b61958",
      "incomplete_value": true,
      "site": "00b61958",
      "value": [
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
      "definition_site": "00b61914",
      "incomplete_value": true,
      "site": "00b61914",
      "value": [
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
      "definition_site": "00b61914",
      "incomplete_value": true,
      "site": "00b61914",
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
      "definition_site": "00b618d0",
      "incomplete_value": true,
      "site": "00b618d0",
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
      "00b61910",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6191c",
      "READ",
      [
        "storage",
        "010a1588",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61938",
      "WRITE",
      [
        "storage",
        "010a1588",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b61910",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6191c",
      "READ",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b61938",
      "WRITE",
      [
        "storage",
        "010a15c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b618cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b618b8.md#insn-00b618cc) · [`00b618f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b618b8.md#insn-00b618f4) · [`00b61910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b618b8.md#insn-00b61910)
- 新版 `00b61910`（命令位置の公開資料なし） · `00b61938`（命令位置の公開資料なし） · `00b61954`（命令位置の公開資料なし）

~~~diff
- 00b618cc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00b618cc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61910 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00b61910 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b618cc bytes 81c242f9
+ 00b61910 bytes 81e242f9
- 00b618f4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b618f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b618f4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:588:8"]]
- 00b618f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b61938 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b61938 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b61938 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:5c8:8"]]
+ 00b61938 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b618f4 bytes bf221639
+ 00b61938 bytes bf221739
- 00b61910 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b61910 ["INT_ADD", "register:40f0:8", ["const:b61910:8", "const:4:8"]]
- 00b61910 ["CALLIND", null, ["register:0:8"]]
+ 00b61954 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b61954 ["INT_ADD", "register:40f0:8", ["const:b61954:8", "const:4:8"]]
+ 00b61954 ["CALLIND", null, ["register:0:8"]]
- 00b61910 bytes 00013fd6
+ 00b61954 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19203e2b75c3c5e305f87648c97b52ec"></a>

### [`00b61928`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61928.md) → [`00b6196c`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b6196c.md) _ZN8firebase4auth21action_code_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0x44` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde090`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde090.md) [`00bde0b0`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde0b0.md)

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
      "definition_site": "00b619ac",
      "incomplete_value": true,
      "site": "00b619ac",
      "value": [
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
      "definition_site": "00b61968",
      "incomplete_value": true,
      "site": "00b61968",
      "value": [
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
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b61980",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61990",
      "PARAM",
      [
        "storage",
        "00295587",
        null,
        "string"
      ]
    ],
    [
      "00b619ac",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61980",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61990",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ],
    [
      "00b619ac",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61968`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61928.md#insn-00b61968) · [`00b6193c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61928.md#insn-00b6193c) · [`00b6194c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61928.md#insn-00b6194c)
- 新版 `00b619ac`（命令位置の公開資料なし） · `00b61980`（命令位置の公開資料なし） · `00b61990`（命令位置の公開資料なし）

~~~diff
- 00b61968 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00b61968 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b619ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00b619ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61968 bytes 80c202f9
+ 00b619ac bytes 80e202f9
- 00b6193c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00b6193c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61980 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00b61980 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6193c bytes 81c242f9
+ 00b61980 bytes 81e242f9
- 00b6194c ["COPY", "tmp:0:8", ["const:587:8"]]
- 00b6194c ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00b6194c ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00b6194c ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00b61990 ["COPY", "tmp:0:8", ["const:4fa:8"]]
+ 00b61990 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00b61990 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00b61990 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00b6194c bytes 631c1691
+ 00b61990 bytes 63e81391
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-69a97d6fcf225ebc32c6e4d3cfb70cbf"></a>

### [`00b61998`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61998.md) → [`00b619dc`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b619dc.md) _ZN8firebase4auth21action_code_exception11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b619f8",
      "incomplete_value": false,
      "site": "00b619fc",
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
      "definition_site": "00b619b4",
      "incomplete_value": false,
      "site": "00b619b8",
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
      "definition_site": "00b61a08",
      "incomplete_value": true,
      "site": "00b61a14",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b619c4",
      "incomplete_value": true,
      "site": "00b619d0",
      "value": [
        "LOAD",
        "8",
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
      "00b619f8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b61a08",
      "DATA",
      [
        "storage",
        "010a1590",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b619f8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b61a08",
      "DATA",
      [
        "storage",
        "010a15d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b619b8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61998.md#insn-00b619b8) · [`00b619b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61998.md#insn-00b619b4) · [`00b619c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61998.md#insn-00b619c0)
- 新版 `00b619fc`（命令位置の公開資料なし） · `00b619f8`（命令位置の公開資料なし） · `00b61a04`（命令位置の公開資料なし）

~~~diff
- 00b619b8 ["INT_ADD", "register:40f0:8", ["const:b619b8:8", "const:4:8"]]
- 00b619b8 ["CALL", null, ["callee:00bde180:8"]]
+ 00b619fc ["INT_ADD", "register:40f0:8", ["const:b619fc:8", "const:4:8"]]
+ 00b619fc ["CALL", null, ["callee:00bde180:8"]]
- 00b619b8 bytes def10194
+ 00b619fc bytes e1f10194
- 00b619b4 ["COPY", "tmp:0:8", ["const:5d4:8"]]
- 00b619b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b619b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b619b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b619f8 ["COPY", "tmp:0:8", ["const:547:8"]]
+ 00b619f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b619f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b619f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b619b4 bytes 00501791
+ 00b619f8 bytes 001c1591
- 00b619c0 ["COPY", "tmp:0:8", ["const:590:8"]]
- 00b619c0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b619c0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b619c0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b61a04 ["COPY", "tmp:0:8", ["const:5d0:8"]]
+ 00b61a04 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61a04 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61a04 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b619c0 bytes 08411691
+ 00b61a04 bytes 08411791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-147ab12f36d94ffc49bad7b6cc57cb55"></a>

### [`00b619d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b619d4.md) → [`00b61a18`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61a18.md) _ZN8firebase4auth21action_code_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b61a58",
      "incomplete_value": true,
      "site": "00b61a58",
      "value": [
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
      "definition_site": "00b61a14",
      "incomplete_value": true,
      "site": "00b61a14",
      "value": [
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
      "definition_site": "00b61a34",
      "incomplete_value": true,
      "site": "00b61a34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b619f0",
      "incomplete_value": true,
      "site": "00b619f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
      "definition_site": "00b61a3c",
      "incomplete_value": false,
      "site": "00b61a50",
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
            "const:4fa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b619f8",
      "incomplete_value": false,
      "site": "00b61a0c",
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
            "const:587:8"
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
      "00b61a2c",
      "READ",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61a3c",
      "PARAM",
      [
        "storage",
        "00295587",
        null,
        "string"
      ]
    ],
    [
      "00b61a58",
      "WRITE",
      [
        "storage",
        "010a1580",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b61a2c",
      "READ",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b61a3c",
      "PARAM",
      [
        "storage",
        "002954fa",
        null,
        "string"
      ]
    ],
    [
      "00b61a58",
      "WRITE",
      [
        "storage",
        "010a15c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61a0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b619d4.md#insn-00b61a0c) · [`00b61a14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b619d4.md#insn-00b61a14) · [`00b619e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b619d4.md#insn-00b619e8)
- 新版 `00b61a50`（命令位置の公開資料なし） · `00b61a58`（命令位置の公開資料なし） · `00b61a2c`（命令位置の公開資料なし）

~~~diff
- 00b61a0c ["INT_ADD", "register:40f0:8", ["const:b61a0c:8", "const:4:8"]]
- 00b61a0c ["CALL", null, ["callee:00bde090:8"]]
+ 00b61a50 ["INT_ADD", "register:40f0:8", ["const:b61a50:8", "const:4:8"]]
+ 00b61a50 ["CALL", null, ["callee:00bde090:8"]]
- 00b61a0c bytes 8df10194
+ 00b61a50 bytes 90f10194
- 00b61a14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00b61a14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b61a58 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00b61a58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b61a14 bytes 80c202f9
+ 00b61a58 bytes 80e202f9
- 00b619e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:580:8"]]
- 00b619e8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b61a2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:5c0:8"]]
+ 00b61a2c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b619e8 bytes 81c242f9
+ 00b61a2c bytes 81e242f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39af613648f08ea9f66386ea578baff4"></a>

### [`00b61a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61a44.md) → [`00b61a88`](../../../../reference/15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b61/00b61a88.md) _ZN8firebase4auth21action_code_exception10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b61aa4",
      "incomplete_value": false,
      "site": "00b61aa8",
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
      "definition_site": "00b61a60",
      "incomplete_value": false,
      "site": "00b61a64",
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
      "definition_site": "00b61ab4",
      "incomplete_value": true,
      "site": "00b61ac0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b61a70",
      "incomplete_value": true,
      "site": "00b61a7c",
      "value": [
        "LOAD",
        "8",
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
      "00b61aa4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b61ab4",
      "DATA",
      [
        "storage",
        "010a1598",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b61aa4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b61ab4",
      "DATA",
      [
        "storage",
        "010a15d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b61a64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61a44.md#insn-00b61a64) · [`00b61a60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61a44.md#insn-00b61a60) · [`00b61a6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b61/00b61a44.md#insn-00b61a6c)
- 新版 `00b61aa8`（命令位置の公開資料なし） · `00b61aa4`（命令位置の公開資料なし） · `00b61ab0`（命令位置の公開資料なし）

~~~diff
- 00b61a64 ["INT_ADD", "register:40f0:8", ["const:b61a64:8", "const:4:8"]]
- 00b61a64 ["CALL", null, ["callee:00bde180:8"]]
+ 00b61aa8 ["INT_ADD", "register:40f0:8", ["const:b61aa8:8", "const:4:8"]]
+ 00b61aa8 ["CALL", null, ["callee:00bde180:8"]]
- 00b61a64 bytes b3f10194
+ 00b61aa8 bytes b6f10194
- 00b61a60 ["COPY", "tmp:0:8", ["const:67f:8"]]
- 00b61a60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b61a60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b61a60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b61aa4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
+ 00b61aa4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61aa4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b61aa4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b61a60 bytes 00fc1991
+ 00b61aa4 bytes 00c81791
- 00b61a6c ["COPY", "tmp:0:8", ["const:598:8"]]
- 00b61a6c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b61a6c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b61a6c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b61ab0 ["COPY", "tmp:0:8", ["const:5d8:8"]]
+ 00b61ab0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61ab0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b61ab0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b61a6c bytes 08611691
+ 00b61ab0 bytes 08611791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

