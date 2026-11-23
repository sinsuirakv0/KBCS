# v15.7.2 → v15.7.3 · 最優先の変更候補 (71)

[一覧の目次](README.md)

<a id="compare-31191fd485f0c114e1d64feeff9fca18"></a>

### [`00b637c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b637c0.md) → [`00b63888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63888.md) _ZN8firebase4auth27too_many_requests_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b638b8",
      "incomplete_value": true,
      "site": "00b638b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b637f0",
      "incomplete_value": true,
      "site": "00b637f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00b6389c",
      "incomplete_value": true,
      "site": "00b6389c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b637d4",
      "incomplete_value": true,
      "site": "00b637d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b638a8",
      "incomplete_value": false,
      "site": "00b638b0",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b637e0",
      "incomplete_value": false,
      "site": "00b637e8",
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
            "const:127:8"
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
      "00b63898",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b638a8",
      "PARAM",
      [
        "storage",
        "002a5127",
        null,
        "string"
      ]
    ],
    [
      "00b638b8",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63898",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b638a8",
      "PARAM",
      [
        "storage",
        "002a5120",
        null,
        "string"
      ]
    ],
    [
      "00b638b8",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b637e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b637c0.md#insn-00b637e8) · [`00b637f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b637c0.md#insn-00b637f0) · [`00b637d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b637c0.md#insn-00b637d0)
- 新版 `00b638b0`（命令位置の公開資料なし） · `00b638b8`（命令位置の公開資料なし） · `00b63898`（命令位置の公開資料なし）

~~~diff
- 00b637e8 ["INT_ADD", "register:40f0:8", ["const:b637e8:8", "const:4:8"]]
- 00b637e8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b638b0 ["INT_ADD", "register:40f0:8", ["const:b638b0:8", "const:4:8"]]
+ 00b638b0 ["CALL", null, ["callee:00bde040:8"]]
- 00b637e8 bytes eae90194
+ 00b638b0 bytes e4e90194
- 00b637f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b637f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b638b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b638b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b637f0 bytes 600203f9
+ 00b638b8 bytes 606203f9
- 00b637d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b637d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63898 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b63898 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b637d0 bytes 680243f9
+ 00b63898 bytes 686243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-330fb8de11dd22df53473306e5dfc1c2"></a>

### [`00b63804`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63804.md) → [`00b638cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b638cc.md) _ZN8firebase4auth27too_many_requests_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b638fc",
      "incomplete_value": true,
      "site": "00b638fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63834",
      "incomplete_value": true,
      "site": "00b63834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00b638e0",
      "incomplete_value": true,
      "site": "00b638e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63818",
      "incomplete_value": true,
      "site": "00b63818",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b638e8",
      "incomplete_value": false,
      "site": "00b638f4",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63820",
      "incomplete_value": false,
      "site": "00b6382c",
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
            "const:127:8"
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
      "00b638dc",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b638e8",
      "PARAM",
      [
        "storage",
        "002a5127",
        null,
        "string"
      ]
    ],
    [
      "00b638fc",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b638dc",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b638e8",
      "PARAM",
      [
        "storage",
        "002a5120",
        null,
        "string"
      ]
    ],
    [
      "00b638fc",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6382c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63804.md#insn-00b6382c) · [`00b63834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63804.md#insn-00b63834) · [`00b63814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63804.md#insn-00b63814)
- 新版 `00b638f4`（命令位置の公開資料なし） · `00b638fc`（命令位置の公開資料なし） · `00b638dc`（命令位置の公開資料なし）

~~~diff
- 00b6382c ["INT_ADD", "register:40f0:8", ["const:b6382c:8", "const:4:8"]]
- 00b6382c ["CALL", null, ["callee:00bde040:8"]]
+ 00b638f4 ["INT_ADD", "register:40f0:8", ["const:b638f4:8", "const:4:8"]]
+ 00b638f4 ["CALL", null, ["callee:00bde040:8"]]
- 00b6382c bytes d9e90194
+ 00b638f4 bytes d3e90194
- 00b63834 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b63834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b638fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b638fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63834 bytes 600203f9
+ 00b638fc bytes 606203f9
- 00b63814 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:600:8"]]
- 00b63814 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b638dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
+ 00b638dc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63814 bytes 680243f9
+ 00b638dc bytes 686243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4233067a7576cae02a02232e50377788"></a>

### [`00b63854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63854.md) → [`00b6391c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b6391c.md) _ZN8firebase4auth27too_many_requests_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b63974",
      "incomplete_value": true,
      "site": "00b63974",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b638ac",
      "incomplete_value": true,
      "site": "00b638ac",
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
            "const:608:8"
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
      "definition_site": "00b63950",
      "incomplete_value": true,
      "site": "00b6395c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63888",
      "incomplete_value": true,
      "site": "00b63894",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:600:8"
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
      "00b63930",
      "READ",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63950",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63974",
      "WRITE",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b63930",
      "READ",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63950",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63974",
      "WRITE",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63894`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63854.md#insn-00b63894) · [`00b638ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63854.md#insn-00b638ac) · [`00b63868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63854.md#insn-00b63868)
- 新版 `00b6395c`（命令位置の公開資料なし） · `00b63974`（命令位置の公開資料なし） · `00b63930`（命令位置の公開資料なし）

~~~diff
- 00b63894 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63894 ["INT_ADD", "register:40f0:8", ["const:b63894:8", "const:4:8"]]
- 00b63894 ["CALLIND", null, ["register:0:8"]]
+ 00b6395c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b6395c ["INT_ADD", "register:40f0:8", ["const:b6395c:8", "const:4:8"]]
+ 00b6395c ["CALLIND", null, ["register:0:8"]]
- 00b63894 bytes 00013fd6
+ 00b6395c bytes 00013fd6
- 00b638ac ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b638ac ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:608:8"]]
- 00b638ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b63974 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b63974 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6c8:8"]]
+ 00b63974 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b638ac bytes a0221839
+ 00b63974 bytes a0221b39
- 00b63868 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:608:8"]]
- 00b63868 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b63868 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b63930 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6c8:8"]]
+ 00b63930 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b63930 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b63868 bytes a8225839
+ 00b63930 bytes a8225b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59697b47e1a5b3a3fbccc8503c748828"></a>

### [`00b638c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b638c0.md) → [`00b63988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63988.md) _ZN8firebase4auth27too_many_requests_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b639c4",
      "incomplete_value": true,
      "site": "00b639c4",
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
            "const:6c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b638fc",
      "incomplete_value": true,
      "site": "00b638fc",
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
            "const:608:8"
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
      "definition_site": "00b639e4",
      "incomplete_value": true,
      "site": "00b639e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6391c",
      "incomplete_value": true,
      "site": "00b6391c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00b639a0",
      "incomplete_value": true,
      "site": "00b639a0",
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
      "definition_site": "00b638d8",
      "incomplete_value": true,
      "site": "00b638d8",
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
      "00b6399c",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b639a8",
      "READ",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ],
    [
      "00b639c4",
      "WRITE",
      [
        "storage",
        "010a1608",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6399c",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b639a8",
      "READ",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b639c4",
      "WRITE",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b638fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b638c0.md#insn-00b638fc) · [`00b63918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b638c0.md#insn-00b63918) · [`00b6391c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b638c0.md#insn-00b6391c)
- 新版 `00b639c4`（命令位置の公開資料なし） · `00b639e0`（命令位置の公開資料なし） · `00b639e4`（命令位置の公開資料なし）

~~~diff
- 00b638fc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b638fc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b638fc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:608:8"]]
- 00b638fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b639c4 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b639c4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b639c4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6c8:8"]]
+ 00b639c4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b638fc bytes bf221839
+ 00b639c4 bytes bf221b39
- 00b63918 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63918 ["INT_ADD", "register:40f0:8", ["const:b63918:8", "const:4:8"]]
- 00b63918 ["CALLIND", null, ["register:0:8"]]
+ 00b639e0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b639e0 ["INT_ADD", "register:40f0:8", ["const:b639e0:8", "const:4:8"]]
+ 00b639e0 ["CALLIND", null, ["register:0:8"]]
- 00b63918 bytes 00013fd6
+ 00b639e0 bytes 00013fd6
- 00b6391c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
- 00b6391c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b6391c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b639e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00b639e4 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b639e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b6391c bytes 9f0203f9
+ 00b639e4 bytes 9f6203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f5978f381293be0860881d4d3613d3fe"></a>

### [`00b63930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63930.md) → [`00b639f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b639f8.md) _ZN8firebase4auth27too_many_requests_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b63a38",
      "incomplete_value": true,
      "site": "00b63a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63970",
      "incomplete_value": true,
      "site": "00b63970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00b63a14",
      "incomplete_value": true,
      "site": "00b63a14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6394c",
      "incomplete_value": true,
      "site": "00b6394c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63a1c",
      "incomplete_value": false,
      "site": "00b63a30",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63954",
      "incomplete_value": false,
      "site": "00b63968",
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
            "const:127:8"
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
      "00b63a0c",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63a1c",
      "PARAM",
      [
        "storage",
        "002a5127",
        null,
        "string"
      ]
    ],
    [
      "00b63a38",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63a0c",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63a1c",
      "PARAM",
      [
        "storage",
        "002a5120",
        null,
        "string"
      ]
    ],
    [
      "00b63a38",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63930.md#insn-00b63968) · [`00b63970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63930.md#insn-00b63970) · [`00b63944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63930.md#insn-00b63944)
- 新版 `00b63a30`（命令位置の公開資料なし） · `00b63a38`（命令位置の公開資料なし） · `00b63a0c`（命令位置の公開資料なし）

~~~diff
- 00b63968 ["INT_ADD", "register:40f0:8", ["const:b63968:8", "const:4:8"]]
- 00b63968 ["CALL", null, ["callee:00bde040:8"]]
+ 00b63a30 ["INT_ADD", "register:40f0:8", ["const:b63a30:8", "const:4:8"]]
+ 00b63a30 ["CALL", null, ["callee:00bde040:8"]]
- 00b63968 bytes 8ae90194
+ 00b63a30 bytes 84e90194
- 00b63970 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
- 00b63970 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63a38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00b63a38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63970 bytes 800203f9
+ 00b63a38 bytes 806203f9
- 00b63944 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
- 00b63944 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63a0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00b63a0c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63944 bytes 810243f9
+ 00b63a0c bytes 816243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26ac77698de10efb0be58fc86a89486e"></a>

### [`00b639a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b639a0.md) → [`00b63a68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63a68.md) _ZN8firebase4auth27too_many_requests_exception11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b63a84",
      "incomplete_value": false,
      "site": "00b63a88",
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
    "old": {
      "definition_site": "00b639bc",
      "incomplete_value": false,
      "site": "00b639c0",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b63a94",
      "incomplete_value": true,
      "site": "00b63aa0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b639cc",
      "incomplete_value": true,
      "site": "00b639d8",
      "value": [
        "LOAD",
        "8",
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
      "00b63a84",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b63a94",
      "DATA",
      [
        "storage",
        "010a1610",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b63a84",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b63a94",
      "DATA",
      [
        "storage",
        "010a16d0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b639c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b639a0.md#insn-00b639c0) · [`00b639bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b639a0.md#insn-00b639bc) · [`00b639c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b639a0.md#insn-00b639c8)
- 新版 `00b63a88`（命令位置の公開資料なし） · `00b63a84`（命令位置の公開資料なし） · `00b63a90`（命令位置の公開資料なし）

~~~diff
- 00b639c0 ["INT_ADD", "register:40f0:8", ["const:b639c0:8", "const:4:8"]]
- 00b639c0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b63a88 ["INT_ADD", "register:40f0:8", ["const:b63a88:8", "const:4:8"]]
+ 00b63a88 ["CALL", null, ["callee:00bde130:8"]]
- 00b639c0 bytes b0e90194
+ 00b63a88 bytes aae90194
- 00b639bc ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b639bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b639bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b639bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b63a84 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b63a84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63a84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63a84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b639bc bytes 001c1591
+ 00b63a84 bytes 00501791
- 00b639c8 ["COPY", "tmp:0:8", ["const:610:8"]]
- 00b639c8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b639c8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b639c8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b63a90 ["COPY", "tmp:0:8", ["const:6d0:8"]]
+ 00b63a90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63a90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63a90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b639c8 bytes 08411891
+ 00b63a90 bytes 08411b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e54b76cd960cc8f006c07aac7ef72efb"></a>

### [`00b639dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b639dc.md) → [`00b63aa4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63aa4.md) _ZN8firebase4auth27too_many_requests_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b63ae4",
      "incomplete_value": true,
      "site": "00b63ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63a1c",
      "incomplete_value": true,
      "site": "00b63a1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:600:8"
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
      "definition_site": "00b63ac0",
      "incomplete_value": true,
      "site": "00b63ac0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b639f8",
      "incomplete_value": true,
      "site": "00b639f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63ac8",
      "incomplete_value": false,
      "site": "00b63adc",
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
            "const:120:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63a00",
      "incomplete_value": false,
      "site": "00b63a14",
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
            "const:127:8"
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
      "00b63ab8",
      "READ",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63ac8",
      "PARAM",
      [
        "storage",
        "002a5127",
        null,
        "string"
      ]
    ],
    [
      "00b63ae4",
      "WRITE",
      [
        "storage",
        "010a1600",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63ab8",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63ac8",
      "PARAM",
      [
        "storage",
        "002a5120",
        null,
        "string"
      ]
    ],
    [
      "00b63ae4",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b639dc.md#insn-00b63a14) · [`00b63a1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b639dc.md#insn-00b63a1c) · [`00b639f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b639dc.md#insn-00b639f0)
- 新版 `00b63adc`（命令位置の公開資料なし） · `00b63ae4`（命令位置の公開資料なし） · `00b63ab8`（命令位置の公開資料なし）

~~~diff
- 00b63a14 ["INT_ADD", "register:40f0:8", ["const:b63a14:8", "const:4:8"]]
- 00b63a14 ["CALL", null, ["callee:00bde040:8"]]
+ 00b63adc ["INT_ADD", "register:40f0:8", ["const:b63adc:8", "const:4:8"]]
+ 00b63adc ["CALL", null, ["callee:00bde040:8"]]
- 00b63a14 bytes 5fe90194
+ 00b63adc bytes 59e90194
- 00b63a1c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
- 00b63a1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63ae4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00b63ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63a1c bytes 800203f9
+ 00b63ae4 bytes 806203f9
- 00b639f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:600:8"]]
- 00b639f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63ab8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
+ 00b63ab8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b639f0 bytes 810243f9
+ 00b63ab8 bytes 816243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f80e43407d9cf50787aed2abda20264"></a>

### [`00b63a88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63a88.md) → [`00b63b50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b50.md) _ZN8firebase4auth18firebase_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b63b7c",
      "incomplete_value": true,
      "site": "00b63b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63ab4",
      "incomplete_value": true,
      "site": "00b63ab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00b63b64",
      "incomplete_value": true,
      "site": "00b63b64",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63a9c",
      "incomplete_value": true,
      "site": "00b63a9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63b70",
      "incomplete_value": false,
      "site": "00b63b74",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63aa8",
      "incomplete_value": false,
      "site": "00b63aac",
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
            "const:483:8"
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
      "00b63b60",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63b70",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ],
    [
      "00b63b7c",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63b60",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63b70",
      "PARAM",
      [
        "storage",
        "00293510",
        null,
        "string"
      ]
    ],
    [
      "00b63b7c",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63a88.md#insn-00b63aac) · [`00b63ab4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63a88.md#insn-00b63ab4) · [`00b63a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63a88.md#insn-00b63a98)
- 新版 `00b63b74`（命令位置の公開資料なし） · `00b63b7c`（命令位置の公開資料なし） · `00b63b60`（命令位置の公開資料なし）

~~~diff
- 00b63aac ["INT_ADD", "register:40f0:8", ["const:b63aac:8", "const:4:8"]]
- 00b63aac ["CALL", null, ["callee:00bde040:8"]]
+ 00b63b74 ["INT_ADD", "register:40f0:8", ["const:b63b74:8", "const:4:8"]]
+ 00b63b74 ["CALL", null, ["callee:00bde040:8"]]
- 00b63aac bytes 39e90194
+ 00b63b74 bytes 33e90194
- 00b63ab4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b63ab4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63b7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
+ 00b63b7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63ab4 bytes 601203f9
+ 00b63b7c bytes 607203f9
- 00b63a98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b63a98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63b60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
+ 00b63b60 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63a98 bytes 681243f9
+ 00b63b60 bytes 687243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5768c8cacfdf5f3c5b24d7d5db8d2b3a"></a>

### [`00b63ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63ac8.md) → [`00b63b90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63b90.md) _ZN8firebase4auth18firebase_exception19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b63bbc",
      "incomplete_value": true,
      "site": "00b63bbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63af4",
      "incomplete_value": true,
      "site": "00b63af4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00b63ba4",
      "incomplete_value": true,
      "site": "00b63ba4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63adc",
      "incomplete_value": true,
      "site": "00b63adc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63bac",
      "incomplete_value": false,
      "site": "00b63bb4",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63ae4",
      "incomplete_value": false,
      "site": "00b63aec",
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
            "const:483:8"
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
      "00b63ba0",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63bac",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ],
    [
      "00b63bbc",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63ba0",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63bac",
      "PARAM",
      [
        "storage",
        "00293510",
        null,
        "string"
      ]
    ],
    [
      "00b63bbc",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63ac8.md#insn-00b63aec) · [`00b63af4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63ac8.md#insn-00b63af4) · [`00b63ad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63ac8.md#insn-00b63ad8)
- 新版 `00b63bb4`（命令位置の公開資料なし） · `00b63bbc`（命令位置の公開資料なし） · `00b63ba0`（命令位置の公開資料なし）

~~~diff
- 00b63aec ["INT_ADD", "register:40f0:8", ["const:b63aec:8", "const:4:8"]]
- 00b63aec ["CALL", null, ["callee:00bde040:8"]]
+ 00b63bb4 ["INT_ADD", "register:40f0:8", ["const:b63bb4:8", "const:4:8"]]
+ 00b63bb4 ["CALL", null, ["callee:00bde040:8"]]
- 00b63aec bytes 29e90194
+ 00b63bb4 bytes 23e90194
- 00b63af4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b63af4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63bbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
+ 00b63bbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63af4 bytes 601203f9
+ 00b63bbc bytes 607203f9
- 00b63ad8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b63ad8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63ba0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
+ 00b63ba0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63ad8 bytes 681243f9
+ 00b63ba0 bytes 687243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d9f910816ac715e68d334fae7ea215aa"></a>

### [`00b63b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63b08.md) → [`00b63bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63bd0.md) _ZN8firebase4auth18firebase_exception10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63b38"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b63c00"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b63be4",
      "incomplete_value": true,
      "site": "00b63be4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63b1c",
      "incomplete_value": true,
      "site": "00b63b1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b63be0",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63be4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b63b3c"
      ]
    ],
    [
      "unmatched:00b63b28",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b63be0",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63be4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b63c04"
      ]
    ],
    [
      "00b63bf0",
      "PARAM",
      [
        "storage",
        "00293510",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63b08.md#insn-00b63b30) · [`00b63b38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63b08.md#insn-00b63b38) · [`00b63b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63b08.md#insn-00b63b48)

~~~diff
- 00b63b30 ["INT_ADD", "register:40f0:8", ["const:b63b30:8", "const:4:8"]]
- 00b63b30 ["CALL", null, ["callee:00bde040:8"]]
- 00b63b30 bytes 18e90194
- 00b63b38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b63b38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63b38 bytes 601203f9
- 00b63b48 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b63b48 ["RETURN", null, ["register:0:8"]]
- 00b63b48 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98fc89aa9f6ee50f1942bf69ce2f4ae7"></a>

### [`00b63b4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63b4c.md) → [`00b63c14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63c14.md) _ZN8firebase4auth18firebase_exception10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b63c44",
      "incomplete_value": true,
      "site": "00b63c44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63b7c",
      "incomplete_value": true,
      "site": "00b63b7c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:620:8"
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
      "definition_site": "00b63c28",
      "incomplete_value": true,
      "site": "00b63c28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63b60",
      "incomplete_value": true,
      "site": "00b63b60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b63c30",
      "incomplete_value": false,
      "site": "00b63c3c",
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
            "const:510:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63b68",
      "incomplete_value": false,
      "site": "00b63b74",
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
            "const:483:8"
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
      "00b63c24",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63c30",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ],
    [
      "00b63c44",
      "WRITE",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63c24",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63c30",
      "PARAM",
      [
        "storage",
        "00293510",
        null,
        "string"
      ]
    ],
    [
      "00b63c44",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63b74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63b4c.md#insn-00b63b74) · [`00b63b7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63b4c.md#insn-00b63b7c) · [`00b63b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63b4c.md#insn-00b63b5c)
- 新版 `00b63c3c`（命令位置の公開資料なし） · `00b63c44`（命令位置の公開資料なし） · `00b63c24`（命令位置の公開資料なし）

~~~diff
- 00b63b74 ["INT_ADD", "register:40f0:8", ["const:b63b74:8", "const:4:8"]]
- 00b63b74 ["CALL", null, ["callee:00bde040:8"]]
+ 00b63c3c ["INT_ADD", "register:40f0:8", ["const:b63c3c:8", "const:4:8"]]
+ 00b63c3c ["CALL", null, ["callee:00bde040:8"]]
- 00b63b74 bytes 07e90194
+ 00b63c3c bytes 01e90194
- 00b63b7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b63b7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b63c44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
+ 00b63c44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63b7c bytes 601203f9
+ 00b63c44 bytes 607203f9
- 00b63b5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:620:8"]]
- 00b63b5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b63c24 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
+ 00b63c24 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b63b5c bytes 681243f9
+ 00b63c24 bytes 687243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2316641b4d3e8506ed347643ff2e81c4"></a>

### [`00b63b9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63b9c.md) → [`00b63c64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63c64.md) _ZN8firebase4auth18firebase_exception15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b63cbc",
      "incomplete_value": true,
      "site": "00b63cbc",
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
            "const:6e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63bf4",
      "incomplete_value": true,
      "site": "00b63bf4",
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
            "const:628:8"
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
      "definition_site": "00b63c98",
      "incomplete_value": true,
      "site": "00b63ca4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b63bd0",
      "incomplete_value": true,
      "site": "00b63bdc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:620:8"
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
      "00b63c78",
      "READ",
      [
        "storage",
        "010a1628",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63c98",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63cbc",
      "WRITE",
      [
        "storage",
        "010a1628",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b63c78",
      "READ",
      [
        "storage",
        "010a16e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b63c98",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63cbc",
      "WRITE",
      [
        "storage",
        "010a16e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63bdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63b9c.md#insn-00b63bdc) · [`00b63bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63b9c.md#insn-00b63bf4) · [`00b63bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63b9c.md#insn-00b63bb0)
- 新版 `00b63ca4`（命令位置の公開資料なし） · `00b63cbc`（命令位置の公開資料なし） · `00b63c78`（命令位置の公開資料なし）

~~~diff
- 00b63bdc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b63bdc ["INT_ADD", "register:40f0:8", ["const:b63bdc:8", "const:4:8"]]
- 00b63bdc ["CALLIND", null, ["register:0:8"]]
+ 00b63ca4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b63ca4 ["INT_ADD", "register:40f0:8", ["const:b63ca4:8", "const:4:8"]]
+ 00b63ca4 ["CALLIND", null, ["register:0:8"]]
- 00b63bdc bytes 00013fd6
+ 00b63ca4 bytes 00013fd6
- 00b63bf4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b63bf4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:628:8"]]
- 00b63bf4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b63cbc ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b63cbc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6e8:8"]]
+ 00b63cbc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b63bf4 bytes a0a21839
+ 00b63cbc bytes a0a21b39
- 00b63bb0 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:628:8"]]
- 00b63bb0 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b63bb0 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b63c78 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6e8:8"]]
+ 00b63c78 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b63c78 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b63bb0 bytes a8a25839
+ 00b63c78 bytes a8a25b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-71fa5e9361327231ff2c098465da0882"></a>

### [`00b63c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63c08.md) → [`00b63cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63cd0.md) _ZN8firebase4auth18firebase_exception12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 7件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63c08"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63c0c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63c0c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b63c08",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b63c0c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b63c10",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b63cd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b63cd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b63cd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63c08.md#insn-00b63c08) · [`00b63c0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63c08.md#insn-00b63c0c) · [`00b63c10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63c08.md#insn-00b63c10)

~~~diff
- 00b63c08 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b63c08 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b63c08 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b63c08 bytes f50f1df8
- 00b63c0c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b63c0c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b63c0c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b63c0c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b63c0c bytes f44f01a9
- 00b63c10 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b63c10 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b63c10 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b63c10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b63c10 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3d0ff1ccce094a9769809f836e79cc05"></a>

### [`00b63c78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63c78.md) → [`00b63d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63d40.md) _ZN8firebase4auth18firebase_exception14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63c78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63c78"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63c7c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b63c78",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b63c7c",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b63c8c",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b63d40",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b63d44",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b63d54",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63c78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63c78.md#insn-00b63c78) · [`00b63c7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63c78.md#insn-00b63c7c) · [`00b63c94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63c78.md#insn-00b63c94)

~~~diff
- 00b63c78 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b63c78 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b63c78 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b63c78 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b63c78 bytes f44fbea9
- 00b63c7c ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b63c7c ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b63c7c ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b63c7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b63c7c bytes fd7b01a9
- 00b63c94 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b63c94 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b63c94 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab9df8365260ace59e94ef65d946200b"></a>

### [`00b63d24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63d24.md) → [`00b63dec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63dec.md) _ZN8firebase4auth18firebase_exception13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63d64"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b63e2c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63d40"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b63d38",
      "READ",
      [
        "storage",
        "010a1620",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b63d40",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b63e30"
      ]
    ],
    [
      "unmatched:00b63d48",
      "PARAM",
      [
        "storage",
        "00293483",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b63e00",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b63e08",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b63e30"
      ]
    ],
    [
      "00b63e10",
      "PARAM",
      [
        "storage",
        "00293510",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63d40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63d24.md#insn-00b63d40) · [`00b63d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63d24.md#insn-00b63d5c) · [`00b63d64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63d24.md#insn-00b63d64)
- 新版 `00b63e24`（命令位置の公開資料なし）

~~~diff
- 00b63d40 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b63d40 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b63d40 bytes 410100b5
- 00b63d5c ["INT_ADD", "register:40f0:8", ["const:b63d5c:8", "const:4:8"]]
- 00b63d5c ["CALL", null, ["callee:00bde040:8"]]
+ 00b63e24 ["INT_ADD", "register:40f0:8", ["const:b63e24:8", "const:4:8"]]
+ 00b63e24 ["CALL", null, ["callee:00bde040:8"]]
- 00b63d5c bytes 8de80194
+ 00b63e24 bytes 87e80194
- 00b63d64 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:620:8"]]
- 00b63d64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b63d64 bytes 801203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8904b7fc2136f6792b3a56c5479b4aa2"></a>

### [`00b63d94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63d94.md) → [`00b63e5c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63e5c.md) _ZN8firebase4auth18firebase_exception10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b63e78",
      "incomplete_value": false,
      "site": "00b63e7c",
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
    "old": {
      "definition_site": "00b63db0",
      "incomplete_value": false,
      "site": "00b63db4",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b63e88",
      "incomplete_value": true,
      "site": "00b63e94",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b63dc0",
      "incomplete_value": true,
      "site": "00b63dcc",
      "value": [
        "LOAD",
        "8",
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
      "00b63e78",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b63e88",
      "DATA",
      [
        "storage",
        "010a1638",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b63e78",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b63e88",
      "DATA",
      [
        "storage",
        "010a16f8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63db4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63d94.md#insn-00b63db4) · [`00b63db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63d94.md#insn-00b63db0) · [`00b63dbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63d94.md#insn-00b63dbc)
- 新版 `00b63e7c`（命令位置の公開資料なし） · `00b63e78`（命令位置の公開資料なし） · `00b63e84`（命令位置の公開資料なし）

~~~diff
- 00b63db4 ["INT_ADD", "register:40f0:8", ["const:b63db4:8", "const:4:8"]]
- 00b63db4 ["CALL", null, ["callee:00bde130:8"]]
+ 00b63e7c ["INT_ADD", "register:40f0:8", ["const:b63e7c:8", "const:4:8"]]
+ 00b63e7c ["CALL", null, ["callee:00bde130:8"]]
- 00b63db4 bytes b3e80194
+ 00b63e7c bytes ade80194
- 00b63db0 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b63db0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b63db0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b63db0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b63e78 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b63e78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63e78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b63e78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b63db0 bytes 00c81791
+ 00b63e78 bytes 00fc1991
- 00b63dbc ["COPY", "tmp:0:8", ["const:638:8"]]
- 00b63dbc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b63dbc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b63dbc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b63e84 ["COPY", "tmp:0:8", ["const:6f8:8"]]
+ 00b63e84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63e84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b63e84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b63dbc bytes 08e11891
+ 00b63e84 bytes 08e11b91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-89a9ef60dc5a4ef0ccc56d35fba08d5f"></a>

### [`00b63dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63dd0.md) → [`00b63e98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b63/00b63e98.md) _ZN8firebase4auth20CacheCommonMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0b90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0b90.md) · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 1件 [`00be0c40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c40.md) · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 28.57% / 新版 28.57%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 19件, `store_condition` 1件, `unresolved_branch_alignment` 25件, `unresolved_call_alignment` 19件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 13件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63dd0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63dd4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b63dd4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b63dd0",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b63dd4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b63dd8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b63e98",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b63e9c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b63ea0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b63dd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63dd0.md#insn-00b63dd0) · [`00b63dd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63dd0.md#insn-00b63dd4) · [`00b63dd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b63/00b63dd0.md#insn-00b63dd8)

~~~diff
- 00b63dd0 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b63dd0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b63dd0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b63dd0 bytes f50f1df8
- 00b63dd4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b63dd4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b63dd4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b63dd4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b63dd4 bytes f44f01a9
- 00b63dd8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b63dd8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b63dd8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b63dd8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b63dd8 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fbce49fb3842f95c738210a502356370"></a>

### [`00b6432c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b6432c.md) → [`00b643f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b643f4.md) _ZN8firebase4auth20ReleaseCommonClassesEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0ba0.md) · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00be0c50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0c50.md) · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 46.26% / 新版 46.26%

CFGの説明率　旧版 22.22% / 新版 22.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 15件, `unresolved_call_alignment` 27件, `unresolved_store_alignment` 21件

アドレスに依存する影響 `branch_value` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6432c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64330"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b64330"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6432c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b64330",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b64334",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b643f4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00b643f8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b643fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6432c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b6432c.md#insn-00b6432c) · [`00b64330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b6432c.md#insn-00b64330) · [`00b64334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b6432c.md#insn-00b64334)

~~~diff
- 00b6432c ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00b6432c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00b6432c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6432c bytes f50f1df8
- 00b64330 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b64330 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b64330 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b64330 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b64330 bytes f44f01a9
- 00b64334 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b64334 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b64334 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00b64334 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b64334 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-693a8d44cd358cadee5a59c1d3324c59"></a>

### [`00b647c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b647c4.md) → [`00b6488c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b6488c.md) _ZN8firebase4auth22ErrorCodeFromExceptionEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c80.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bdb080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb080.md) [`00bdb100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb100.md)
- 新版 呼出元 1件 [`00be0d30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d30.md) · 呼出先 10件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bdb130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb130.md) [`00bdb1b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb1b0.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 73.21% / 新版 73.21%

CFGの説明率　旧版 88.16% / 新版 85.90%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 41件

アドレスに依存する影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b647c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b647c8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b647cc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b647c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b647cc",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b647d0",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b64890",
      "WRITE",
      [
        "storage",
        "Stack[-0x60]",
        null,
        null
      ]
    ],
    [
      "00b64894",
      "WRITE",
      [
        "storage",
        "Stack[-0x50]",
        null,
        null
      ]
    ],
    [
      "00b64898",
      "WRITE",
      [
        "storage",
        "Stack[-0x40]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b647c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b647c4.md#insn-00b647c8) · [`00b647cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b647c4.md#insn-00b647cc) · [`00b647d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b647c4.md#insn-00b647d0)

~~~diff
- 00b647c8 ["COPY", "tmp:0:8", ["register:40e0:8"]]
- 00b647c8 ["COPY", "tmp:1:8", ["register:40d8:8"]]
- 00b647c8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:180:8"]]
- 00b647c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b647c8 bytes fc6f18a9
- 00b647cc ["COPY", "tmp:0:8", ["register:40d0:8"]]
- 00b647cc ["COPY", "tmp:1:8", ["register:40c8:8"]]
- 00b647cc ["INT_ADD", "tmp:2:8", ["register:8:8", "const:190:8"]]
- 00b647cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b647cc bytes fa6719a9
- 00b647d0 ["COPY", "tmp:0:8", ["register:40c0:8"]]
- 00b647d0 ["COPY", "tmp:1:8", ["register:40b8:8"]]
- 00b647d0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:1a0:8"]]
- 00b647d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b647d0 bytes f85f1aa9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f8223d247a849510b2a47b03be7c811"></a>

### [`00b64df8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64df8.md) → [`00b64ec0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b64/00b64ec0.md) _ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 11件 [`00b5e694`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5e694.md) [`00b5ee5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5ee5c.md) [`00b5f0cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f0cc.md) [`00b5f258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f258.md) [`00b5f4e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f4e4.md) · 呼出先 11件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddaa0.md) [`00bddac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddac0.md) [`00bddae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddae0.md)
- 新版 呼出元 11件 [`00b5e75c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5e75c.md) [`00b5ef24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5ef24.md) [`00b5f194`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f194.md) [`00b5f320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f320.md) [`00b5f5ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5f5ac.md) · 呼出先 11件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb50.md) [`00bddb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb70.md) [`00bddb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb90.md)

変更の種類 call_argument_candidate, constant, operands_and_dependencies

命令の説明率　旧版 98.08% / 新版 98.08%

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
      "definition_site": "00b64f14",
      "incomplete_value": true,
      "site": "00b64f20",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b64e4c",
      "incomplete_value": true,
      "site": "00b64e58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:450:8"
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
      "definition_site": "00b64fb0",
      "incomplete_value": true,
      "site": "00b64fbc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:518:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b64ee8",
      "incomplete_value": true,
      "site": "00b64ef4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b64f14",
      "READ",
      [
        "storage",
        "010a1450",
        null,
        "undefined8"
      ]
    ],
    [
      "00b64fb0",
      "READ",
      [
        "storage",
        "010a1458",
        null,
        "undefined8"
      ]
    ],
    [
      "00b64ff0",
      "READ",
      [
        "storage",
        "010a1460",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b64f14",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "00b64fb0",
      "READ",
      [
        "storage",
        "010a1518",
        null,
        "undefined8"
      ]
    ],
    [
      "00b64ff0",
      "READ",
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

- 旧版 [`00b64e58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64df8.md#insn-00b64e58) · [`00b64ef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64df8.md#insn-00b64ef4) · [`00b64e3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64df8.md#insn-00b64e3c)
- 新版 `00b64f20`（命令位置の公開資料なし） · `00b64fbc`（命令位置の公開資料なし） · `00b64f04`（命令位置の公開資料なし）

~~~diff
- 00b64e58 ["INT_ADD", "register:40f0:8", ["const:b64e58:8", "const:4:8"]]
- 00b64e58 ["CALL", null, ["callee:0047495c:8"]]
+ 00b64f20 ["INT_ADD", "register:40f0:8", ["const:b64f20:8", "const:4:8"]]
+ 00b64f20 ["CALL", null, ["callee:0047495c:8"]]
- 00b64e58 bytes c13ee497
+ 00b64f20 bytes 8f3ee497
- 00b64ef4 ["INT_ADD", "register:40f0:8", ["const:b64ef4:8", "const:4:8"]]
- 00b64ef4 ["CALL", null, ["callee:0047495c:8"]]
+ 00b64fbc ["INT_ADD", "register:40f0:8", ["const:b64fbc:8", "const:4:8"]]
+ 00b64fbc ["CALL", null, ["callee:0047495c:8"]]
- 00b64ef4 bytes 9a3ee497
+ 00b64fbc bytes 683ee497
- 00b64e3c ["INT_ADD", "register:40f0:8", ["const:b64e3c:8", "const:4:8"]]
- 00b64e3c ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b64f04 ["INT_ADD", "register:40f0:8", ["const:b64f04:8", "const:4:8"]]
+ 00b64f04 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b64e3c bytes b1e40194
+ 00b64f04 bytes abe40194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ab35117684cfa44bf2542200557abcb3"></a>

### [`00b64fc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64fc0.md) → [`00b65088`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65088.md) _ZN8firebase4auth22ReadAdditionalUserInfoEP7_JNIEnvP8_jobjectPNS0_18AdditionalUserInfoE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c90.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddaa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddaa0.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 1件 [`00be0d40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d40.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddb50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb50.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, constant, control_flow, control_flow_count, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 94.44% / 新版 94.44%

CFGの説明率　旧版 50.00% / 新版 50.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65090"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b650e0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65158"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b650c0",
      "READ",
      [
        "storage",
        "010a1480",
        null,
        "undefined8"
      ]
    ],
    [
      "00b650dc",
      "READ",
      [
        "storage",
        "010a1488",
        null,
        "undefined8"
      ]
    ],
    [
      "00b650f8",
      "READ",
      [
        "storage",
        "010a1490",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b650c0",
      "READ",
      [
        "storage",
        "010a1540",
        null,
        "undefined8"
      ]
    ],
    [
      "00b650dc",
      "READ",
      [
        "storage",
        "010a1548",
        null,
        "undefined8"
      ]
    ],
    [
      "00b650f8",
      "READ",
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

- 旧版 [`00b65004`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64fc0.md#insn-00b65004) · [`00b65090`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64fc0.md#insn-00b65090) · [`00b650cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b64/00b64fc0.md#insn-00b650cc)
- 新版 `00b650cc`（命令位置の公開資料なし） · `00b65194`（命令位置の公開資料なし）

~~~diff
- 00b65004 ["INT_ADD", "register:40f0:8", ["const:b65004:8", "const:4:8"]]
- 00b65004 ["CALL", null, ["callee:0047495c:8"]]
+ 00b650cc ["INT_ADD", "register:40f0:8", ["const:b650cc:8", "const:4:8"]]
+ 00b650cc ["CALL", null, ["callee:0047495c:8"]]
- 00b65004 bytes 563ee497
+ 00b650cc bytes 243ee497
- 00b65090 ["INT_ADD", "tmp:0:8", ["register:8:8", "const:30:8"]]
- 00b65090 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:8"]]
- 00b65090 bytes e81b00f9
- 00b650cc ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b650cc ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b650cc ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b650cc ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
+ 00b65194 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b65194 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b65194 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b65194 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:1:1"]]
- 00b650cc bytes e8050036
+ 00b65194 bytes e8050036
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7640dbec94c5ec17150c36b240ba8b16"></a>

### [`00b65208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65208.md) → [`00b652d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b652d0.md) _ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00b5eaa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5e/00b5eaa8.md) [`00b707d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b70/00b707d0.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bddac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddac0.md) [`00bddae0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddae0.md) [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 2件 [`00b5eb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5e/00b5eb70.md) [`00b70898`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b70/00b70898.md) · 呼出先 7件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bddb70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb70.md) [`00bddb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb90.md) [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 92.86% / 新版 92.86%

CFGの説明率　旧版 46.67% / 新版 46.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65310",
      "incomplete_value": true,
      "site": "00b65314",
      "value": [
        "live",
        "register:4040:8"
      ]
    },
    "old": {
      "definition_site": "00b65248",
      "incomplete_value": true,
      "site": "00b6524c",
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
      "definition_site": "00b65324",
      "incomplete_value": true,
      "site": "00b65330",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00b6525c",
      "incomplete_value": true,
      "site": "00b65268",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:450:8"
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
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b652c4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65324",
      "READ",
      [
        "storage",
        "010a1450",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b652c4",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ],
  "added": [
    [
      "00b65324",
      "READ",
      [
        "storage",
        "010a1510",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6538c",
      "COMPUTED_CALL",
      [
        "unresolved_target",
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6524c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65208.md#insn-00b6524c) · [`00b65250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65208.md#insn-00b65250) · [`00b65268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65208.md#insn-00b65268)
- 新版 `00b65314`（命令位置の公開資料なし） · `00b65318`（命令位置の公開資料なし） · `00b65330`（命令位置の公開資料なし）

~~~diff
- 00b6524c ["INT_ADD", "register:40f0:8", ["const:b6524c:8", "const:4:8"]]
- 00b6524c ["CALL", null, ["callee:00bde1b0:8"]]
+ 00b65314 ["INT_ADD", "register:40f0:8", ["const:b65314:8", "const:4:8"]]
+ 00b65314 ["CALL", null, ["callee:00bde1b0:8"]]
- 00b6524c bytes ade30194
+ 00b65314 bytes a7e30194
- 00b65250 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
- 00b65250 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
+ 00b65318 ["INT_EQUAL", "tmp:0:1", ["register:40b0:8", "const:0:8"]]
+ 00b65318 ["CBRANCH", null, ["local:b9:8", "tmp:0:1"]]
- 00b65250 bytes f60300b4
+ 00b65318 bytes f60300b4
- 00b65268 ["INT_ADD", "register:40f0:8", ["const:b65268:8", "const:4:8"]]
- 00b65268 ["CALL", null, ["callee:0047495c:8"]]
+ 00b65330 ["INT_ADD", "register:40f0:8", ["const:b65330:8", "const:4:8"]]
+ 00b65330 ["CALL", null, ["callee:0047495c:8"]]
- 00b65268 bytes bd3de497
+ 00b65330 bytes 8b3de497
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c39d36f579846e61ab6031f58440ec1"></a>

### [`00b65334`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65334.md) → [`00b653fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b653fc.md) _ZN8firebase4auth18AdditionalUserInfoaSEOS1_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00be0c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c70.md) · 呼出先 3件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdee70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdee70.md) [`00be0c60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00be0/00be0c60.md)
- 新版 呼出元 1件 [`00be0d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d20.md) · 呼出先 3件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdef20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef20.md) [`00be0d10`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00be0/00be0d10.md)

変更の種類 branch_condition_or_target, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, unresolved_branch_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 94.29% / 新版 94.29%

CFGの説明率　旧版 41.18% / 新版 38.89%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_condition` 5件, `unresolved_branch_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65410"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b654d8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65414"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b65414",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b654f0"
      ]
    ]
  ],
  "added": [
    [
      "00b654dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b654f0"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65350`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65334.md#insn-00b65350) · [`00b65358`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65334.md#insn-00b65358) · [`00b65410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65334.md#insn-00b65410)
- 新版 `00b65418`（命令位置の公開資料なし） · `00b65420`（命令位置の公開資料なし）

~~~diff
- 00b65350 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
- 00b65350 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
- 00b65350 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
- 00b65350 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
+ 00b65418 ["INT_RIGHT", "tmp:0:4", ["register:4040:4", "const:0:4"]]
+ 00b65418 ["INT_AND", "tmp:1:4", ["tmp:0:4", "const:1:4"]]
+ 00b65418 ["INT_EQUAL", "tmp:2:1", ["tmp:1:4", "const:0:4"]]
+ 00b65418 ["INT_EQUAL", "tmp:3:1", ["tmp:2:1", "const:0:1"]]
- 00b65350 bytes 68000037
+ 00b65418 bytes 68000037
- 00b65358 ["BRANCH", null, ["local:b4:8"]]
+ 00b65420 ["BRANCH", null, ["local:b5:8"]]
- 00b65358 bytes 09000014
+ 00b65420 bytes 09000014
- 00b65410 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:8:8"]]
- 00b65410 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4050:8"]]
- 00b65410 bytes ca0600f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-259d4ea6fd285f0f1f6de8ba7f7ed500"></a>

### [`00b6544c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b6544c.md) → [`00b65514`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65514.md) _ZN8firebase4auth10credential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65478"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65540"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b65528",
      "incomplete_value": true,
      "site": "00b65528",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65460",
      "incomplete_value": true,
      "site": "00b65460",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b65524",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65528",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6547c"
      ]
    ],
    [
      "unmatched:00b6546c",
      "PARAM",
      [
        "storage",
        "002a903f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65524",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65528",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65544"
      ]
    ],
    [
      "00b65534",
      "PARAM",
      [
        "storage",
        "002a8fab",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65460`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b6544c.md#insn-00b65460) · [`00b65470`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b6544c.md#insn-00b65470) · [`00b65478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b6544c.md#insn-00b65478)
- 新版 `00b65528`（命令位置の公開資料なし）

~~~diff
- 00b65460 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b65460 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b65528 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b65528 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b65460 bytes e80000b5
+ 00b65528 bytes e80000b5
- 00b65470 ["INT_ADD", "register:40f0:8", ["const:b65470:8", "const:4:8"]]
- 00b65470 ["CALL", null, ["callee:00bde040:8"]]
- 00b65470 bytes c8e20194
- 00b65478 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b65478 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65478 bytes 602203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b918a9c4c307885743589b46a157d4dd"></a>

### [`00b6548c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b6548c.md) → [`00b65554`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65554.md) _ZN8firebase4auth10credential19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b65580",
      "incomplete_value": true,
      "site": "00b65580",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:700:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b654b8",
      "incomplete_value": true,
      "site": "00b654b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:640:8"
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
      "definition_site": "00b65568",
      "incomplete_value": true,
      "site": "00b65568",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b654a0",
      "incomplete_value": true,
      "site": "00b654a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65570",
      "incomplete_value": false,
      "site": "00b65578",
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
            "const:fab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b654a8",
      "incomplete_value": false,
      "site": "00b654b0",
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
            "const:3f:8"
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
      "00b65564",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65570",
      "PARAM",
      [
        "storage",
        "002a903f",
        null,
        "string"
      ]
    ],
    [
      "00b65580",
      "WRITE",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65564",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65570",
      "PARAM",
      [
        "storage",
        "002a8fab",
        null,
        "string"
      ]
    ],
    [
      "00b65580",
      "WRITE",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b654b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b6548c.md#insn-00b654b0) · [`00b654b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b6548c.md#insn-00b654b8) · [`00b6549c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b6548c.md#insn-00b6549c)
- 新版 `00b65578`（命令位置の公開資料なし） · `00b65580`（命令位置の公開資料なし） · `00b65564`（命令位置の公開資料なし）

~~~diff
- 00b654b0 ["INT_ADD", "register:40f0:8", ["const:b654b0:8", "const:4:8"]]
- 00b654b0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b65578 ["INT_ADD", "register:40f0:8", ["const:b65578:8", "const:4:8"]]
+ 00b65578 ["CALL", null, ["callee:00bde040:8"]]
- 00b654b0 bytes b8e20194
+ 00b65578 bytes b2e20194
- 00b654b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b654b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65580 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
+ 00b65580 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b654b8 bytes 602203f9
+ 00b65580 bytes 608203f9
- 00b6549c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b6549c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65564 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
+ 00b65564 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6549c bytes 682243f9
+ 00b65564 bytes 688243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f98e2386da0f9df80f9b29fcfdc593b3"></a>

### [`00b654cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b654cc.md) → [`00b65594`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65594.md) _ZN8firebase4auth10credential10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b654fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b655c4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b655a8",
      "incomplete_value": true,
      "site": "00b655a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b654e0",
      "incomplete_value": true,
      "site": "00b654e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b655a4",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b655a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b65500"
      ]
    ],
    [
      "unmatched:00b654ec",
      "PARAM",
      [
        "storage",
        "002a903f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b655a4",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b655a8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b655c8"
      ]
    ],
    [
      "00b655b4",
      "PARAM",
      [
        "storage",
        "002a8fab",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b654e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b654cc.md#insn-00b654e0) · [`00b654f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b654cc.md#insn-00b654f4) · [`00b654fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b654cc.md#insn-00b654fc)
- 新版 `00b655a8`（命令位置の公開資料なし）

~~~diff
- 00b654e0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b654e0 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b655a8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b655a8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b654e0 bytes 080100b5
+ 00b655a8 bytes 080100b5
- 00b654f4 ["INT_ADD", "register:40f0:8", ["const:b654f4:8", "const:4:8"]]
- 00b654f4 ["CALL", null, ["callee:00bde040:8"]]
- 00b654f4 bytes a7e20194
- 00b654fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b654fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b654fc bytes 602203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b65dd1f101a8d30e27421a7e04c49ff"></a>

### [`00b65510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65510.md) → [`00b655d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b655d8.md) _ZN8firebase4auth10credential10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 64.71% / 新版 64.71%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65540"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65608"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b655ec",
      "incomplete_value": true,
      "site": "00b655ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65524",
      "incomplete_value": true,
      "site": "00b65524",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b655e8",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b655ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b65544"
      ]
    ],
    [
      "unmatched:00b6552c",
      "PARAM",
      [
        "storage",
        "002a903f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b655e8",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b655ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6560c"
      ]
    ],
    [
      "00b655f4",
      "PARAM",
      [
        "storage",
        "002a8fab",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65524`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65510.md#insn-00b65524) · [`00b65538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65510.md#insn-00b65538) · [`00b65540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65510.md#insn-00b65540)
- 新版 `00b655ec`（命令位置の公開資料なし） · `00b65600`（命令位置の公開資料なし）

~~~diff
- 00b65524 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b65524 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b655ec ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b655ec ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b65524 bytes 080100b5
+ 00b655ec bytes 080100b5
- 00b65538 ["INT_ADD", "register:40f0:8", ["const:b65538:8", "const:4:8"]]
- 00b65538 ["CALL", null, ["callee:00bde040:8"]]
+ 00b65600 ["INT_ADD", "register:40f0:8", ["const:b65600:8", "const:4:8"]]
+ 00b65600 ["CALL", null, ["callee:00bde040:8"]]
- 00b65538 bytes 96e20194
+ 00b65600 bytes 90e20194
- 00b65540 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:640:8"]]
- 00b65540 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65540 bytes 602203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1641f32ce27bee02ea3ef45674dbd723"></a>

### [`00b65560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65560.md) → [`00b65628`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65628.md) _ZN8firebase4auth10credential15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 92.59% / 新版 92.59%

CFGの説明率　旧版 50.00% / 新版 40.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b65680",
      "incomplete_value": true,
      "site": "00b65680",
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
            "const:708:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b655b8",
      "incomplete_value": true,
      "site": "00b655b8",
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
            "const:648:8"
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
      "definition_site": "00b6565c",
      "incomplete_value": true,
      "site": "00b65668",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:700:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65594",
      "incomplete_value": true,
      "site": "00b655a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:640:8"
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
      "00b6563c",
      "READ",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6565c",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65680",
      "WRITE",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6563c",
      "READ",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6565c",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65680",
      "WRITE",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b655a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65560.md#insn-00b655a0) · [`00b655b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65560.md#insn-00b655b8) · [`00b65574`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65560.md#insn-00b65574)
- 新版 `00b65668`（命令位置の公開資料なし） · `00b65680`（命令位置の公開資料なし） · `00b6563c`（命令位置の公開資料なし）

~~~diff
- 00b655a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b655a0 ["INT_ADD", "register:40f0:8", ["const:b655a0:8", "const:4:8"]]
- 00b655a0 ["CALLIND", null, ["register:0:8"]]
+ 00b65668 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65668 ["INT_ADD", "register:40f0:8", ["const:b65668:8", "const:4:8"]]
+ 00b65668 ["CALLIND", null, ["register:0:8"]]
- 00b655a0 bytes 00013fd6
+ 00b65668 bytes 00013fd6
- 00b655b8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b655b8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:648:8"]]
- 00b655b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b65680 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b65680 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:708:8"]]
+ 00b65680 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b655b8 bytes a0221939
+ 00b65680 bytes a0221c39
- 00b65574 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:648:8"]]
- 00b65574 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b65574 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6563c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:708:8"]]
+ 00b6563c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6563c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b65574 bytes a8225939
+ 00b6563c bytes a8225c39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fef5975bb3c5ef602ad3a75678ea2de5"></a>

### [`00b655cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b655cc.md) → [`00b65694`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65694.md) _ZN8firebase4auth10credential12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

CFGの説明率　旧版 16.67% / 新版 14.29%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65608"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65628"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b656d0"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b656a8",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "00b656ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6562c"
      ]
    ],
    [
      "00b656b4",
      "READ",
      [
        "storage",
        "010a1648",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b656a8",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b656ac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b656f4"
      ]
    ],
    [
      "00b656b4",
      "READ",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b655cc.md#insn-00b65608) · [`00b65610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b655cc.md#insn-00b65610) · [`00b65624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b655cc.md#insn-00b65624)

~~~diff
- 00b65608 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b65608 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b65608 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:648:8"]]
- 00b65608 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b65608 bytes bf221939
- 00b65610 ["INT_ADD", "register:40f0:8", ["const:b65610:8", "const:4:8"]]
- 00b65610 ["CALL", null, ["callee:00bde090:8"]]
- 00b65610 bytes 74e20194
- 00b65624 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65624 ["INT_ADD", "register:40f0:8", ["const:b65624:8", "const:4:8"]]
- 00b65624 ["CALLIND", null, ["register:0:8"]]
- 00b65624 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c87ea1bb1d0078788ae2cdb685805e65"></a>

### [`00b6563c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b6563c.md) → [`00b65704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65704.md) _ZN8firebase4auth10credential14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6563c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b6563c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65640"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b6563c",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b65640",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b65650",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65704",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b65708",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b65718",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6563c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b6563c.md#insn-00b6563c) · [`00b65640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b6563c.md#insn-00b65640) · [`00b65658`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b6563c.md#insn-00b65658)

~~~diff
- 00b6563c ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00b6563c ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00b6563c ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b6563c ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b6563c bytes f44fbea9
- 00b65640 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b65640 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b65640 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b65640 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b65640 bytes fd7b01a9
- 00b65658 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b65658 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b65658 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e1c33d463559cc4ab5cb887e9c1afc7"></a>

### [`00b656ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b656ac.md) → [`00b65774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65774.md) _ZN8firebase4auth10credential11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b65790",
      "incomplete_value": false,
      "site": "00b65794",
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
    "old": {
      "definition_site": "00b656c8",
      "incomplete_value": false,
      "site": "00b656cc",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b657a0",
      "incomplete_value": true,
      "site": "00b657ac",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b656d8",
      "incomplete_value": true,
      "site": "00b656e4",
      "value": [
        "LOAD",
        "8",
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
      "00b65790",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b657a0",
      "DATA",
      [
        "storage",
        "010a1650",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65790",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b657a0",
      "DATA",
      [
        "storage",
        "010a1710",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b656cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b656ac.md#insn-00b656cc) · [`00b656c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b656ac.md#insn-00b656c8) · [`00b656d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b656ac.md#insn-00b656d4)
- 新版 `00b65794`（命令位置の公開資料なし） · `00b65790`（命令位置の公開資料なし） · `00b6579c`（命令位置の公開資料なし）

~~~diff
- 00b656cc ["INT_ADD", "register:40f0:8", ["const:b656cc:8", "const:4:8"]]
- 00b656cc ["CALL", null, ["callee:00bde130:8"]]
+ 00b65794 ["INT_ADD", "register:40f0:8", ["const:b65794:8", "const:4:8"]]
+ 00b65794 ["CALL", null, ["callee:00bde130:8"]]
- 00b656cc bytes 6de20194
+ 00b65794 bytes 67e20194
- 00b656c8 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b656c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b656c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b656c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65790 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b65790 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65790 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65790 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b656c8 bytes 001c1591
+ 00b65790 bytes 00501791
- 00b656d4 ["COPY", "tmp:0:8", ["const:650:8"]]
- 00b656d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b656d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b656d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b6579c ["COPY", "tmp:0:8", ["const:710:8"]]
+ 00b6579c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6579c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b6579c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b656d4 bytes 08411991
+ 00b6579c bytes 08411c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00516d8ffe5a87f3caf7d209770f9841"></a>

### [`00b656e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b656e8.md) → [`00b657b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b657b0.md) _ZN8firebase4auth10credential13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65728"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b657f0"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65704"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b656fc",
      "READ",
      [
        "storage",
        "010a1640",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65704",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b657f4"
      ]
    ],
    [
      "unmatched:00b6570c",
      "PARAM",
      [
        "storage",
        "002a903f",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b657c4",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b657cc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b657f4"
      ]
    ],
    [
      "00b657d4",
      "PARAM",
      [
        "storage",
        "002a8fab",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b656e8.md#insn-00b65704) · [`00b65720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b656e8.md#insn-00b65720) · [`00b65728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b656e8.md#insn-00b65728)
- 新版 `00b657e8`（命令位置の公開資料なし）

~~~diff
- 00b65704 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b65704 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00b65704 bytes 410100b5
- 00b65720 ["INT_ADD", "register:40f0:8", ["const:b65720:8", "const:4:8"]]
- 00b65720 ["CALL", null, ["callee:00bde040:8"]]
+ 00b657e8 ["INT_ADD", "register:40f0:8", ["const:b657e8:8", "const:4:8"]]
+ 00b657e8 ["CALL", null, ["callee:00bde040:8"]]
- 00b65720 bytes 1ce20194
+ 00b657e8 bytes 16e20194
- 00b65728 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:640:8"]]
- 00b65728 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65728 bytes 802203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e3048f96f6584fe86239d038e61133c"></a>

### [`00b65794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65794.md) → [`00b6585c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b6585c.md) _ZN8firebase4auth9emailcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b65888",
      "incomplete_value": true,
      "site": "00b65888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b657c0",
      "incomplete_value": true,
      "site": "00b657c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "definition_site": "00b65870",
      "incomplete_value": true,
      "site": "00b65870",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b657a8",
      "incomplete_value": true,
      "site": "00b657a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6587c",
      "incomplete_value": false,
      "site": "00b65880",
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
            "const:18f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b657b4",
      "incomplete_value": false,
      "site": "00b657b8",
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
            "const:102:8"
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
      "00b6586c",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6587c",
      "PARAM",
      [
        "storage",
        "0029c102",
        null,
        "string"
      ]
    ],
    [
      "00b65888",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6586c",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6587c",
      "PARAM",
      [
        "storage",
        "0029c18f",
        null,
        "string"
      ]
    ],
    [
      "00b65888",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b657b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65794.md#insn-00b657b8) · [`00b657c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65794.md#insn-00b657c0) · [`00b657a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65794.md#insn-00b657a4)
- 新版 `00b65880`（命令位置の公開資料なし） · `00b65888`（命令位置の公開資料なし） · `00b6586c`（命令位置の公開資料なし）

~~~diff
- 00b657b8 ["INT_ADD", "register:40f0:8", ["const:b657b8:8", "const:4:8"]]
- 00b657b8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b65880 ["INT_ADD", "register:40f0:8", ["const:b65880:8", "const:4:8"]]
+ 00b65880 ["CALL", null, ["callee:00bde040:8"]]
- 00b657b8 bytes f6e10194
+ 00b65880 bytes f0e10194
- 00b657c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b657c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65888 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
+ 00b65888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b657c0 bytes 603203f9
+ 00b65888 bytes 609203f9
- 00b657a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b657a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6586c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
+ 00b6586c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b657a4 bytes 683243f9
+ 00b6586c bytes 689243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3404ed61679b1a162505d4edc98686af"></a>

### [`00b657d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b657d4.md) → [`00b6589c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b6589c.md) _ZN8firebase4auth9emailcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 43.75% / 新版 43.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65800"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b658c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b658b0",
      "incomplete_value": true,
      "site": "00b658b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b657e8",
      "incomplete_value": true,
      "site": "00b657e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b658ac",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b658b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b65804"
      ]
    ],
    [
      "unmatched:00b657f0",
      "PARAM",
      [
        "storage",
        "0029c102",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b658ac",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b658b0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b658cc"
      ]
    ],
    [
      "00b658b8",
      "PARAM",
      [
        "storage",
        "0029c18f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b657f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b657d4.md#insn-00b657f8) · [`00b65800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b657d4.md#insn-00b65800) · [`00b65810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b657d4.md#insn-00b65810)

~~~diff
- 00b657f8 ["INT_ADD", "register:40f0:8", ["const:b657f8:8", "const:4:8"]]
- 00b657f8 ["CALL", null, ["callee:00bde040:8"]]
- 00b657f8 bytes e6e10194
- 00b65800 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b65800 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65800 bytes 603203f9
- 00b65810 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b65810 ["RETURN", null, ["register:0:8"]]
- 00b65810 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-84512f0a18d5b36e405dbb9151d5c9ad"></a>

### [`00b65814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65814.md) → [`00b658dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b658dc.md) _ZN8firebase4auth9emailcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65844"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b6590c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b658f0",
      "incomplete_value": true,
      "site": "00b658f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65828",
      "incomplete_value": true,
      "site": "00b65828",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b658ec",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b658f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b65848"
      ]
    ],
    [
      "unmatched:00b65834",
      "PARAM",
      [
        "storage",
        "0029c102",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b658ec",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b658f0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65910"
      ]
    ],
    [
      "00b658fc",
      "PARAM",
      [
        "storage",
        "0029c18f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6583c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65814.md#insn-00b6583c) · [`00b65844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65814.md#insn-00b65844) · [`00b65854`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65814.md#insn-00b65854)

~~~diff
- 00b6583c ["INT_ADD", "register:40f0:8", ["const:b6583c:8", "const:4:8"]]
- 00b6583c ["CALL", null, ["callee:00bde040:8"]]
- 00b6583c bytes d5e10194
- 00b65844 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b65844 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65844 bytes 603203f9
- 00b65854 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b65854 ["RETURN", null, ["register:0:8"]]
- 00b65854 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dcb439d3da8e7dd88e12bbd749d57c94"></a>

### [`00b65858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65858.md) → [`00b65920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65920.md) _ZN8firebase4auth9emailcred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b65950",
      "incomplete_value": true,
      "site": "00b65950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65888",
      "incomplete_value": true,
      "site": "00b65888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "definition_site": "00b65934",
      "incomplete_value": true,
      "site": "00b65934",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6586c",
      "incomplete_value": true,
      "site": "00b6586c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6593c",
      "incomplete_value": false,
      "site": "00b65948",
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
            "const:18f:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65874",
      "incomplete_value": false,
      "site": "00b65880",
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
            "const:102:8"
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
      "00b65930",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6593c",
      "PARAM",
      [
        "storage",
        "0029c102",
        null,
        "string"
      ]
    ],
    [
      "00b65950",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65930",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6593c",
      "PARAM",
      [
        "storage",
        "0029c18f",
        null,
        "string"
      ]
    ],
    [
      "00b65950",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65858.md#insn-00b65880) · [`00b65888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65858.md#insn-00b65888) · [`00b65868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65858.md#insn-00b65868)
- 新版 `00b65948`（命令位置の公開資料なし） · `00b65950`（命令位置の公開資料なし） · `00b65930`（命令位置の公開資料なし）

~~~diff
- 00b65880 ["INT_ADD", "register:40f0:8", ["const:b65880:8", "const:4:8"]]
- 00b65880 ["CALL", null, ["callee:00bde040:8"]]
+ 00b65948 ["INT_ADD", "register:40f0:8", ["const:b65948:8", "const:4:8"]]
+ 00b65948 ["CALL", null, ["callee:00bde040:8"]]
- 00b65880 bytes c4e10194
+ 00b65948 bytes bee10194
- 00b65888 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b65888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
+ 00b65950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65888 bytes 603203f9
+ 00b65950 bytes 609203f9
- 00b65868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:660:8"]]
- 00b65868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65930 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
+ 00b65930 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65868 bytes 683243f9
+ 00b65930 bytes 689243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b1749d89f9f06a30f13744d42b8a8d4"></a>

### [`00b658a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b658a8.md) → [`00b65970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65970.md) _ZN8firebase4auth9emailcred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 call, call_count, constant, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 81.48% / 新版 81.48%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b659c8",
      "incomplete_value": true,
      "site": "00b659c8",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65900",
      "incomplete_value": true,
      "site": "00b65900",
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
            "const:668:8"
          ]
        ]
      ]
    },
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00b658e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": {
      "site": "00b659b0"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b65984",
      "READ",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b658dc",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b659c8",
      "WRITE",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b65984",
      "READ",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ],
    [
      "00b659a4",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b659c8",
      "WRITE",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b658e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b658a8.md#insn-00b658e8) · [`00b65900`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b658a8.md#insn-00b65900)
- 新版 `00b659c8`（命令位置の公開資料なし） · `00b659b0`（命令位置の公開資料なし）

~~~diff
- 00b658e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b658e8 ["INT_ADD", "register:40f0:8", ["const:b658e8:8", "const:4:8"]]
- 00b658e8 ["CALLIND", null, ["register:0:8"]]
- 00b658e8 bytes 00013fd6
- 00b65900 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b65900 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:668:8"]]
- 00b65900 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b659c8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b659c8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:728:8"]]
+ 00b659c8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b65900 bytes a0a21939
+ 00b659c8 bytes a0a21c39
+ 00b659b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b659b0 ["INT_ADD", "register:40f0:8", ["const:b659b0:8", "const:4:8"]]
+ 00b659b0 ["CALLIND", null, ["register:0:8"]]
+ 00b659b0 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-521f9bab8e4303490ffaea616d257e10"></a>

### [`00b65914`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65914.md) → [`00b659dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b659dc.md) _ZN8firebase4auth9emailcred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b65a18",
      "incomplete_value": true,
      "site": "00b65a18",
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
            "const:728:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65950",
      "incomplete_value": true,
      "site": "00b65950",
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
            "const:668:8"
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
      "definition_site": "00b65a38",
      "incomplete_value": true,
      "site": "00b65a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65970",
      "incomplete_value": true,
      "site": "00b65970",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "definition_site": "00b659f4",
      "incomplete_value": true,
      "site": "00b659f4",
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
      "definition_site": "00b6592c",
      "incomplete_value": true,
      "site": "00b6592c",
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
      "00b659f0",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b659fc",
      "READ",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65a18",
      "WRITE",
      [
        "storage",
        "010a1668",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b659f0",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b659fc",
      "READ",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65a18",
      "WRITE",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65914.md#insn-00b65950) · [`00b6596c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65914.md#insn-00b6596c) · [`00b65970`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65914.md#insn-00b65970)
- 新版 `00b65a18`（命令位置の公開資料なし） · `00b65a34`（命令位置の公開資料なし） · `00b65a38`（命令位置の公開資料なし）

~~~diff
- 00b65950 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b65950 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b65950 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:668:8"]]
- 00b65950 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b65a18 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b65a18 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b65a18 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:728:8"]]
+ 00b65a18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b65950 bytes bfa21939
+ 00b65a18 bytes bfa21c39
- 00b6596c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6596c ["INT_ADD", "register:40f0:8", ["const:b6596c:8", "const:4:8"]]
- 00b6596c ["CALLIND", null, ["register:0:8"]]
+ 00b65a34 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65a34 ["INT_ADD", "register:40f0:8", ["const:b65a34:8", "const:4:8"]]
+ 00b65a34 ["CALLIND", null, ["register:0:8"]]
- 00b6596c bytes 00013fd6
+ 00b65a34 bytes 00013fd6
- 00b65970 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
- 00b65970 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b65970 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b65a38 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
+ 00b65a38 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b65a38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b65970 bytes 9f3203f9
+ 00b65a38 bytes 9f9203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9664fdda8aa9115f21554bd84e584500"></a>

### [`00b65984`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65984.md) → [`00b65a4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65a4c.md) _ZN8firebase4auth9emailcred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 4件, `store_condition` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b65a8c",
      "incomplete_value": true,
      "site": "00b65a8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:720:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b659c4",
      "incomplete_value": true,
      "site": "00b659c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:660:8"
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
      "definition_site": "00b65a68",
      "incomplete_value": true,
      "site": "00b65a68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b659a0",
      "incomplete_value": true,
      "site": "00b659a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65a74",
      "incomplete_value": true,
      "site": "00b65a84",
      "value": [
        "live",
        "register:4098:8"
      ]
    },
    "old": null,
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
      "00b65a60",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65a70",
      "PARAM",
      [
        "storage",
        "0029c102",
        null,
        "string"
      ]
    ],
    [
      "00b65a8c",
      "WRITE",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65a60",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65a70",
      "PARAM",
      [
        "storage",
        "0029c18f",
        null,
        "string"
      ]
    ],
    [
      "00b65a8c",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b659bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65984.md#insn-00b659bc) · [`00b659c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65984.md#insn-00b659c4) · [`00b65998`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65984.md#insn-00b65998)
- 新版 `00b65a84`（命令位置の公開資料なし） · `00b65a8c`（命令位置の公開資料なし） · `00b65a60`（命令位置の公開資料なし）

~~~diff
- 00b659bc ["INT_ADD", "register:40f0:8", ["const:b659bc:8", "const:4:8"]]
- 00b659bc ["CALL", null, ["callee:00bde040:8"]]
+ 00b65a84 ["INT_ADD", "register:40f0:8", ["const:b65a84:8", "const:4:8"]]
+ 00b65a84 ["CALL", null, ["callee:00bde040:8"]]
- 00b659bc bytes 75e10194
+ 00b65a84 bytes 6fe10194
- 00b659c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
- 00b659c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65a8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
+ 00b65a8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b659c4 bytes 803203f9
+ 00b65a8c bytes 809203f9
- 00b65998 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
- 00b65998 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65a60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
+ 00b65a60 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65998 bytes 813243f9
+ 00b65a60 bytes 819243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67544100650f3a48fbb60bf1efb6c4c1"></a>

### [`00b659f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b659f4.md) → [`00b65abc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65abc.md) _ZN8firebase4auth9emailcred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b65ad8",
      "incomplete_value": false,
      "site": "00b65adc",
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
    "old": {
      "definition_site": "00b65a10",
      "incomplete_value": false,
      "site": "00b65a14",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b65ae8",
      "incomplete_value": true,
      "site": "00b65af4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b65a20",
      "incomplete_value": true,
      "site": "00b65a2c",
      "value": [
        "LOAD",
        "8",
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
      "00b65ad8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b65ae8",
      "DATA",
      [
        "storage",
        "010a1670",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65ad8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b65ae8",
      "DATA",
      [
        "storage",
        "010a1730",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65a14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b659f4.md#insn-00b65a14) · [`00b65a10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b659f4.md#insn-00b65a10) · [`00b65a1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b659f4.md#insn-00b65a1c)
- 新版 `00b65adc`（命令位置の公開資料なし） · `00b65ad8`（命令位置の公開資料なし） · `00b65ae4`（命令位置の公開資料なし）

~~~diff
- 00b65a14 ["INT_ADD", "register:40f0:8", ["const:b65a14:8", "const:4:8"]]
- 00b65a14 ["CALL", null, ["callee:00bde130:8"]]
+ 00b65adc ["INT_ADD", "register:40f0:8", ["const:b65adc:8", "const:4:8"]]
+ 00b65adc ["CALL", null, ["callee:00bde130:8"]]
- 00b65a14 bytes 9be10194
+ 00b65adc bytes 95e10194
- 00b65a10 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b65a10 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65a10 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65a10 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65ad8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b65ad8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65ad8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65ad8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65a10 bytes 001c1591
+ 00b65ad8 bytes 00501791
- 00b65a1c ["COPY", "tmp:0:8", ["const:670:8"]]
- 00b65a1c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b65a1c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b65a1c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b65ae4 ["COPY", "tmp:0:8", ["const:730:8"]]
+ 00b65ae4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65ae4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65ae4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b65a1c bytes 08c11991
+ 00b65ae4 bytes 08c11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edbe04e618c35628af10543d65451ce1"></a>

### [`00b65a30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65a30.md) → [`00b65af8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65af8.md) _ZN8firebase4auth9emailcred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65a70"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b65b38"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65a4c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b65a44",
      "READ",
      [
        "storage",
        "010a1660",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b65a4c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65b3c"
      ]
    ],
    [
      "unmatched:00b65a54",
      "PARAM",
      [
        "storage",
        "0029c102",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b65b0c",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65b14",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b65b3c"
      ]
    ],
    [
      "00b65b1c",
      "PARAM",
      [
        "storage",
        "0029c18f",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65a4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65a30.md#insn-00b65a4c) · [`00b65a68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65a30.md#insn-00b65a68) · [`00b65a70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65a30.md#insn-00b65a70)
- 新版 `00b65b30`（命令位置の公開資料なし）

~~~diff
- 00b65a4c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b65a4c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b65a4c bytes 410100b5
- 00b65a68 ["INT_ADD", "register:40f0:8", ["const:b65a68:8", "const:4:8"]]
- 00b65a68 ["CALL", null, ["callee:00bde040:8"]]
+ 00b65b30 ["INT_ADD", "register:40f0:8", ["const:b65b30:8", "const:4:8"]]
+ 00b65b30 ["CALL", null, ["callee:00bde040:8"]]
- 00b65a68 bytes 4ae10194
+ 00b65b30 bytes 44e10194
- 00b65a70 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:660:8"]]
- 00b65a70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65a70 bytes 803203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-de250bb9770afcc9a5a3717c5b71938b"></a>

### [`00b65aa0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65aa0.md) → [`00b65b68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65b68.md) _ZN8firebase4auth9emailcred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b65b84",
      "incomplete_value": false,
      "site": "00b65b88",
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
    "old": {
      "definition_site": "00b65abc",
      "incomplete_value": false,
      "site": "00b65ac0",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b65b94",
      "incomplete_value": true,
      "site": "00b65ba0",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b65acc",
      "incomplete_value": true,
      "site": "00b65ad8",
      "value": [
        "LOAD",
        "8",
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
      "00b65b84",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b65b94",
      "DATA",
      [
        "storage",
        "010a1678",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b65b84",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b65b94",
      "DATA",
      [
        "storage",
        "010a1738",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ac0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65aa0.md#insn-00b65ac0) · [`00b65abc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65aa0.md#insn-00b65abc) · [`00b65ac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65aa0.md#insn-00b65ac8)
- 新版 `00b65b88`（命令位置の公開資料なし） · `00b65b84`（命令位置の公開資料なし） · `00b65b90`（命令位置の公開資料なし）

~~~diff
- 00b65ac0 ["INT_ADD", "register:40f0:8", ["const:b65ac0:8", "const:4:8"]]
- 00b65ac0 ["CALL", null, ["callee:00bde130:8"]]
+ 00b65b88 ["INT_ADD", "register:40f0:8", ["const:b65b88:8", "const:4:8"]]
+ 00b65b88 ["CALL", null, ["callee:00bde130:8"]]
- 00b65ac0 bytes 70e10194
+ 00b65b88 bytes 6ae10194
- 00b65abc ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b65abc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65abc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65abc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65b84 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b65b84 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65b84 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65b84 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65abc bytes 00c81791
+ 00b65b84 bytes 00fc1991
- 00b65ac8 ["COPY", "tmp:0:8", ["const:678:8"]]
- 00b65ac8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b65ac8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b65ac8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b65b90 ["COPY", "tmp:0:8", ["const:738:8"]]
+ 00b65b90 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65b90 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65b90 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b65ac8 bytes 08e11991
+ 00b65b90 bytes 08e11c91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-507506e7c425086fdb0866a7377594e4"></a>

### [`00b65adc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65adc.md) → [`00b65ba4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65ba4.md) _ZN8firebase4auth12facebookcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b65bd0",
      "incomplete_value": true,
      "site": "00b65bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65b08",
      "incomplete_value": true,
      "site": "00b65b08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "definition_site": "00b65bb8",
      "incomplete_value": true,
      "site": "00b65bb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65af0",
      "incomplete_value": true,
      "site": "00b65af0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65bc4",
      "incomplete_value": false,
      "site": "00b65bc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:3e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65afc",
      "incomplete_value": false,
      "site": "00b65b00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:3ea:8"
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
      "00b65bb4",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65bc4",
      "PARAM",
      [
        "storage",
        "002ac3ea",
        null,
        "string"
      ]
    ],
    [
      "00b65bd0",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65bb4",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65bc4",
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      "00b65bd0",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65b00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65adc.md#insn-00b65b00) · [`00b65b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65adc.md#insn-00b65b08) · [`00b65aec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65adc.md#insn-00b65aec)
- 新版 `00b65bc8`（命令位置の公開資料なし） · `00b65bd0`（命令位置の公開資料なし） · `00b65bb4`（命令位置の公開資料なし）

~~~diff
- 00b65b00 ["INT_ADD", "register:40f0:8", ["const:b65b00:8", "const:4:8"]]
- 00b65b00 ["CALL", null, ["callee:00bde040:8"]]
+ 00b65bc8 ["INT_ADD", "register:40f0:8", ["const:b65bc8:8", "const:4:8"]]
+ 00b65bc8 ["CALL", null, ["callee:00bde040:8"]]
- 00b65b00 bytes 24e10194
+ 00b65bc8 bytes 1ee10194
- 00b65b08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b65b08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65bd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b65bd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65b08 bytes 604203f9
+ 00b65bd0 bytes 60a203f9
- 00b65aec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b65aec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65bb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b65bb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65aec bytes 684243f9
+ 00b65bb4 bytes 68a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-497e551b9077db3c4cf57221bbf67be3"></a>

### [`00b65b1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65b1c.md) → [`00b65be4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65be4.md) _ZN8firebase4auth12facebookcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b65c10",
      "incomplete_value": true,
      "site": "00b65c10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65b48",
      "incomplete_value": true,
      "site": "00b65b48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "definition_site": "00b65bf8",
      "incomplete_value": true,
      "site": "00b65bf8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65b30",
      "incomplete_value": true,
      "site": "00b65b30",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65c00",
      "incomplete_value": false,
      "site": "00b65c08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:3e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65b38",
      "incomplete_value": false,
      "site": "00b65b40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:3ea:8"
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
      "00b65bf4",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c00",
      "PARAM",
      [
        "storage",
        "002ac3ea",
        null,
        "string"
      ]
    ],
    [
      "00b65c10",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65bf4",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c00",
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      "00b65c10",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65b40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65b1c.md#insn-00b65b40) · [`00b65b48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65b1c.md#insn-00b65b48) · [`00b65b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65b1c.md#insn-00b65b2c)
- 新版 `00b65c08`（命令位置の公開資料なし） · `00b65c10`（命令位置の公開資料なし） · `00b65bf4`（命令位置の公開資料なし）

~~~diff
- 00b65b40 ["INT_ADD", "register:40f0:8", ["const:b65b40:8", "const:4:8"]]
- 00b65b40 ["CALL", null, ["callee:00bde040:8"]]
+ 00b65c08 ["INT_ADD", "register:40f0:8", ["const:b65c08:8", "const:4:8"]]
+ 00b65c08 ["CALL", null, ["callee:00bde040:8"]]
- 00b65b40 bytes 14e10194
+ 00b65c08 bytes 0ee10194
- 00b65b48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b65b48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65c10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b65c10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65b48 bytes 604203f9
+ 00b65c10 bytes 60a203f9
- 00b65b2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b65b2c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65bf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b65bf4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65b2c bytes 684243f9
+ 00b65bf4 bytes 68a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1d822dd8fc5bd5a1b342ea24503f38c"></a>

### [`00b65b5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65b5c.md) → [`00b65c24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65c24.md) _ZN8firebase4auth12facebookcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b65c54",
      "incomplete_value": true,
      "site": "00b65c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65b8c",
      "incomplete_value": true,
      "site": "00b65b8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "definition_site": "00b65c38",
      "incomplete_value": true,
      "site": "00b65c38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65b70",
      "incomplete_value": true,
      "site": "00b65b70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65c44",
      "incomplete_value": false,
      "site": "00b65c4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:3e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65b7c",
      "incomplete_value": false,
      "site": "00b65b84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:3ea:8"
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
      "00b65c34",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c44",
      "PARAM",
      [
        "storage",
        "002ac3ea",
        null,
        "string"
      ]
    ],
    [
      "00b65c54",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65c34",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c44",
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      "00b65c54",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65b84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65b5c.md#insn-00b65b84) · [`00b65b8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65b5c.md#insn-00b65b8c) · [`00b65b6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65b5c.md#insn-00b65b6c)
- 新版 `00b65c4c`（命令位置の公開資料なし） · `00b65c54`（命令位置の公開資料なし） · `00b65c34`（命令位置の公開資料なし）

~~~diff
- 00b65b84 ["INT_ADD", "register:40f0:8", ["const:b65b84:8", "const:4:8"]]
- 00b65b84 ["CALL", null, ["callee:00bde040:8"]]
+ 00b65c4c ["INT_ADD", "register:40f0:8", ["const:b65c4c:8", "const:4:8"]]
+ 00b65c4c ["CALL", null, ["callee:00bde040:8"]]
- 00b65b84 bytes 03e10194
+ 00b65c4c bytes fde00194
- 00b65b8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b65b8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65c54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b65c54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65b8c bytes 604203f9
+ 00b65c54 bytes 60a203f9
- 00b65b6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b65b6c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65c34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b65c34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65b6c bytes 684243f9
+ 00b65c34 bytes 68a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e9fc6de44b73e92561da5e21229f2bb"></a>

### [`00b65ba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ba0.md) → [`00b65c68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65c68.md) _ZN8firebase4auth12facebookcred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b65c98",
      "incomplete_value": true,
      "site": "00b65c98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65bd0",
      "incomplete_value": true,
      "site": "00b65bd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "definition_site": "00b65c7c",
      "incomplete_value": true,
      "site": "00b65c7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65bb4",
      "incomplete_value": true,
      "site": "00b65bb4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65c84",
      "incomplete_value": false,
      "site": "00b65c90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:3e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65bbc",
      "incomplete_value": false,
      "site": "00b65bc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:3ea:8"
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
      "00b65c78",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c84",
      "PARAM",
      [
        "storage",
        "002ac3ea",
        null,
        "string"
      ]
    ],
    [
      "00b65c98",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65c78",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65c84",
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      "00b65c98",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65bc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ba0.md#insn-00b65bc8) · [`00b65bd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ba0.md#insn-00b65bd0) · [`00b65bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ba0.md#insn-00b65bb0)
- 新版 `00b65c90`（命令位置の公開資料なし） · `00b65c98`（命令位置の公開資料なし） · `00b65c78`（命令位置の公開資料なし）

~~~diff
- 00b65bc8 ["INT_ADD", "register:40f0:8", ["const:b65bc8:8", "const:4:8"]]
- 00b65bc8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b65c90 ["INT_ADD", "register:40f0:8", ["const:b65c90:8", "const:4:8"]]
+ 00b65c90 ["CALL", null, ["callee:00bde040:8"]]
- 00b65bc8 bytes f2e00194
+ 00b65c90 bytes ece00194
- 00b65bd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b65bd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65c98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b65c98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65bd0 bytes 604203f9
+ 00b65c98 bytes 60a203f9
- 00b65bb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:680:8"]]
- 00b65bb0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65c78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:740:8"]]
+ 00b65c78 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65bb0 bytes 684243f9
+ 00b65c78 bytes 68a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5067cd19ae3f1748759a7c4a3ff2f93f"></a>

### [`00b65bf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65bf0.md) → [`00b65cb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65cb8.md) _ZN8firebase4auth12facebookcred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b65d10",
      "incomplete_value": true,
      "site": "00b65d10",
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
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c48",
      "incomplete_value": true,
      "site": "00b65c48",
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
            "const:688:8"
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
      "definition_site": "00b65cec",
      "incomplete_value": true,
      "site": "00b65cf8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:740:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c24",
      "incomplete_value": true,
      "site": "00b65c30",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:680:8"
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
      "00b65ccc",
      "READ",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65cec",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d10",
      "WRITE",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b65ccc",
      "READ",
      [
        "storage",
        "010a1748",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65cec",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d10",
      "WRITE",
      [
        "storage",
        "010a1748",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65c30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65bf0.md#insn-00b65c30) · [`00b65c48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65bf0.md#insn-00b65c48) · [`00b65c04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65bf0.md#insn-00b65c04)
- 新版 `00b65cf8`（命令位置の公開資料なし） · `00b65d10`（命令位置の公開資料なし） · `00b65ccc`（命令位置の公開資料なし）

~~~diff
- 00b65c30 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65c30 ["INT_ADD", "register:40f0:8", ["const:b65c30:8", "const:4:8"]]
- 00b65c30 ["CALLIND", null, ["register:0:8"]]
+ 00b65cf8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65cf8 ["INT_ADD", "register:40f0:8", ["const:b65cf8:8", "const:4:8"]]
+ 00b65cf8 ["CALLIND", null, ["register:0:8"]]
- 00b65c30 bytes 00013fd6
+ 00b65cf8 bytes 00013fd6
- 00b65c48 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b65c48 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:688:8"]]
- 00b65c48 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b65d10 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b65d10 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:748:8"]]
+ 00b65d10 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b65c48 bytes a0221a39
+ 00b65d10 bytes a0221d39
- 00b65c04 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:688:8"]]
- 00b65c04 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b65c04 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b65ccc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:748:8"]]
+ 00b65ccc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b65ccc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b65c04 bytes a8225a39
+ 00b65ccc bytes a8225d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-578824944ca74ebad33bb6411e5746d1"></a>

### [`00b65c5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65c5c.md) → [`00b65d24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65d24.md) _ZN8firebase4auth12facebookcred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b65d60",
      "incomplete_value": true,
      "site": "00b65d60",
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
            "const:748:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65c98",
      "incomplete_value": true,
      "site": "00b65c98",
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
            "const:688:8"
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
      "definition_site": "00b65d80",
      "incomplete_value": true,
      "site": "00b65d80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65cb8",
      "incomplete_value": true,
      "site": "00b65cb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "definition_site": "00b65d3c",
      "incomplete_value": true,
      "site": "00b65d3c",
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
      "definition_site": "00b65c74",
      "incomplete_value": true,
      "site": "00b65c74",
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
      "00b65d38",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d44",
      "READ",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65d60",
      "WRITE",
      [
        "storage",
        "010a1688",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b65d38",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65d44",
      "READ",
      [
        "storage",
        "010a1748",
        null,
        "undefined1"
      ]
    ],
    [
      "00b65d60",
      "WRITE",
      [
        "storage",
        "010a1748",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65c5c.md#insn-00b65c98) · [`00b65cb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65c5c.md#insn-00b65cb4) · [`00b65cb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65c5c.md#insn-00b65cb8)
- 新版 `00b65d60`（命令位置の公開資料なし） · `00b65d7c`（命令位置の公開資料なし） · `00b65d80`（命令位置の公開資料なし）

~~~diff
- 00b65c98 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b65c98 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b65c98 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:688:8"]]
- 00b65c98 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b65d60 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b65d60 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b65d60 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:748:8"]]
+ 00b65d60 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b65c98 bytes bf221a39
+ 00b65d60 bytes bf221d39
- 00b65cb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65cb4 ["INT_ADD", "register:40f0:8", ["const:b65cb4:8", "const:4:8"]]
- 00b65cb4 ["CALLIND", null, ["register:0:8"]]
+ 00b65d7c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b65d7c ["INT_ADD", "register:40f0:8", ["const:b65d7c:8", "const:4:8"]]
+ 00b65d7c ["CALLIND", null, ["register:0:8"]]
- 00b65cb4 bytes 00013fd6
+ 00b65d7c bytes 00013fd6
- 00b65cb8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00b65cb8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b65cb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b65d80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
+ 00b65d80 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b65d80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b65cb8 bytes 9f4203f9
+ 00b65d80 bytes 9fa203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dc42bd32d958789c01e794cbffd2ba0"></a>

### [`00b65ccc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ccc.md) → [`00b65d94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65d94.md) _ZN8firebase4auth12facebookcred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b65dd4",
      "incomplete_value": true,
      "site": "00b65dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d0c",
      "incomplete_value": true,
      "site": "00b65d0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "definition_site": "00b65db0",
      "incomplete_value": true,
      "site": "00b65db0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65ce8",
      "incomplete_value": true,
      "site": "00b65ce8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65db8",
      "incomplete_value": false,
      "site": "00b65dcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:3e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65cf0",
      "incomplete_value": false,
      "site": "00b65d04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:3ea:8"
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
      "00b65da8",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65db8",
      "PARAM",
      [
        "storage",
        "002ac3ea",
        null,
        "string"
      ]
    ],
    [
      "00b65dd4",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65da8",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65db8",
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      "00b65dd4",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65d04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ccc.md#insn-00b65d04) · [`00b65d0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ccc.md#insn-00b65d0c) · [`00b65ce0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ccc.md#insn-00b65ce0)
- 新版 `00b65dcc`（命令位置の公開資料なし） · `00b65dd4`（命令位置の公開資料なし） · `00b65da8`（命令位置の公開資料なし）

~~~diff
- 00b65d04 ["INT_ADD", "register:40f0:8", ["const:b65d04:8", "const:4:8"]]
- 00b65d04 ["CALL", null, ["callee:00bde040:8"]]
+ 00b65dcc ["INT_ADD", "register:40f0:8", ["const:b65dcc:8", "const:4:8"]]
+ 00b65dcc ["CALL", null, ["callee:00bde040:8"]]
- 00b65d04 bytes a3e00194
+ 00b65dcc bytes 9de00194
- 00b65d0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00b65d0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65dd4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
+ 00b65dd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65d0c bytes 804203f9
+ 00b65dd4 bytes 80a203f9
- 00b65ce0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00b65ce0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65da8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
+ 00b65da8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65ce0 bytes 814243f9
+ 00b65da8 bytes 81a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bae8b75e1322932cb6c3d0a8e9ba164"></a>

### [`00b65d3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65d3c.md) → [`00b65e04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65e04.md) _ZN8firebase4auth12facebookcred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b65e20",
      "incomplete_value": false,
      "site": "00b65e24",
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
    "old": {
      "definition_site": "00b65d58",
      "incomplete_value": false,
      "site": "00b65d5c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b65e30",
      "incomplete_value": true,
      "site": "00b65e3c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b65d68",
      "incomplete_value": true,
      "site": "00b65d74",
      "value": [
        "LOAD",
        "8",
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
      "00b65e20",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b65e30",
      "DATA",
      [
        "storage",
        "010a1690",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65e20",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b65e30",
      "DATA",
      [
        "storage",
        "010a1750",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65d5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65d3c.md#insn-00b65d5c) · [`00b65d58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65d3c.md#insn-00b65d58) · [`00b65d64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65d3c.md#insn-00b65d64)
- 新版 `00b65e24`（命令位置の公開資料なし） · `00b65e20`（命令位置の公開資料なし） · `00b65e2c`（命令位置の公開資料なし）

~~~diff
- 00b65d5c ["INT_ADD", "register:40f0:8", ["const:b65d5c:8", "const:4:8"]]
- 00b65d5c ["CALL", null, ["callee:00bde130:8"]]
+ 00b65e24 ["INT_ADD", "register:40f0:8", ["const:b65e24:8", "const:4:8"]]
+ 00b65e24 ["CALL", null, ["callee:00bde130:8"]]
- 00b65d5c bytes c9e00194
+ 00b65e24 bytes c3e00194
- 00b65d58 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b65d58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65d58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65d58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65e20 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b65e20 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65e20 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65e20 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65d58 bytes 001c1591
+ 00b65e20 bytes 00501791
- 00b65d64 ["COPY", "tmp:0:8", ["const:690:8"]]
- 00b65d64 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b65d64 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b65d64 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b65e2c ["COPY", "tmp:0:8", ["const:750:8"]]
+ 00b65e2c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65e2c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65e2c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b65d64 bytes 08411a91
+ 00b65e2c bytes 08411d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-195f7fb396432b2388e720bc912eca0e"></a>

### [`00b65d78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65d78.md) → [`00b65e40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65e40.md) _ZN8firebase4auth12facebookcred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b65e80",
      "incomplete_value": true,
      "site": "00b65e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:740:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65db8",
      "incomplete_value": true,
      "site": "00b65db8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:680:8"
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
      "definition_site": "00b65e5c",
      "incomplete_value": true,
      "site": "00b65e5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d94",
      "incomplete_value": true,
      "site": "00b65d94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b65e64",
      "incomplete_value": false,
      "site": "00b65e78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:3e1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65d9c",
      "incomplete_value": false,
      "site": "00b65db0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ac000:8"
          ],
          [
            "leaf",
            "const:3ea:8"
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
      "00b65e54",
      "READ",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65e64",
      "PARAM",
      [
        "storage",
        "002ac3ea",
        null,
        "string"
      ]
    ],
    [
      "00b65e80",
      "WRITE",
      [
        "storage",
        "010a1680",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65e54",
      "READ",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65e64",
      "PARAM",
      [
        "storage",
        "002ac3e1",
        null,
        "string"
      ]
    ],
    [
      "00b65e80",
      "WRITE",
      [
        "storage",
        "010a1740",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65db0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65d78.md#insn-00b65db0) · [`00b65db8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65d78.md#insn-00b65db8) · [`00b65d8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65d78.md#insn-00b65d8c)
- 新版 `00b65e78`（命令位置の公開資料なし） · `00b65e80`（命令位置の公開資料なし） · `00b65e54`（命令位置の公開資料なし）

~~~diff
- 00b65db0 ["INT_ADD", "register:40f0:8", ["const:b65db0:8", "const:4:8"]]
- 00b65db0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b65e78 ["INT_ADD", "register:40f0:8", ["const:b65e78:8", "const:4:8"]]
+ 00b65e78 ["CALL", null, ["callee:00bde040:8"]]
- 00b65db0 bytes 78e00194
+ 00b65e78 bytes 72e00194
- 00b65db8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00b65db8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65e80 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
+ 00b65e80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65db8 bytes 804203f9
+ 00b65e80 bytes 80a203f9
- 00b65d8c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:680:8"]]
- 00b65d8c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65e54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:740:8"]]
+ 00b65e54 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65d8c bytes 814243f9
+ 00b65e54 bytes 81a243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b51757c0cf31973567b291848fc1964f"></a>

### [`00b65de8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65de8.md) → [`00b65eb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65eb0.md) _ZN8firebase4auth12facebookcred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b65ecc",
      "incomplete_value": false,
      "site": "00b65ed0",
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
    "old": {
      "definition_site": "00b65e04",
      "incomplete_value": false,
      "site": "00b65e08",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b65edc",
      "incomplete_value": true,
      "site": "00b65ee8",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b65e14",
      "incomplete_value": true,
      "site": "00b65e20",
      "value": [
        "LOAD",
        "8",
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
      "00b65ecc",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b65edc",
      "DATA",
      [
        "storage",
        "010a1698",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b65ecc",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b65edc",
      "DATA",
      [
        "storage",
        "010a1758",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65e08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65de8.md#insn-00b65e08) · [`00b65e04`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65de8.md#insn-00b65e04) · [`00b65e10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65de8.md#insn-00b65e10)
- 新版 `00b65ed0`（命令位置の公開資料なし） · `00b65ecc`（命令位置の公開資料なし） · `00b65ed8`（命令位置の公開資料なし）

~~~diff
- 00b65e08 ["INT_ADD", "register:40f0:8", ["const:b65e08:8", "const:4:8"]]
- 00b65e08 ["CALL", null, ["callee:00bde130:8"]]
+ 00b65ed0 ["INT_ADD", "register:40f0:8", ["const:b65ed0:8", "const:4:8"]]
+ 00b65ed0 ["CALL", null, ["callee:00bde130:8"]]
- 00b65e08 bytes 9ee00194
+ 00b65ed0 bytes 98e00194
- 00b65e04 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b65e04 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b65e04 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b65e04 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b65ecc ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b65ecc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65ecc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b65ecc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b65e04 bytes 00c81791
+ 00b65ecc bytes 00fc1991
- 00b65e10 ["COPY", "tmp:0:8", ["const:698:8"]]
- 00b65e10 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b65e10 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b65e10 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b65ed8 ["COPY", "tmp:0:8", ["const:758:8"]]
+ 00b65ed8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65ed8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b65ed8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b65e10 bytes 08611a91
+ 00b65ed8 bytes 08611d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-318eb1db25854fbb56e61c79bd45111b"></a>

### [`00b65e24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65e24.md) → [`00b65eec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65eec.md) _ZN8firebase4auth10githubcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b65f18",
      "incomplete_value": true,
      "site": "00b65f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e50",
      "incomplete_value": true,
      "site": "00b65e50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "00b65f00",
      "incomplete_value": true,
      "site": "00b65f00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e38",
      "incomplete_value": true,
      "site": "00b65e38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b65e38"
      ],
      [
        "FALL_THROUGH",
        "00b65f00"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b65f00",
      "incomplete_value": true,
      "site": "00b65f18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e38",
      "incomplete_value": true,
      "site": "00b65e50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b65efc",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65f18",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65efc",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65f18",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65e50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65e24.md#insn-00b65e50) · [`00b65e34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65e24.md#insn-00b65e34) · [`00b65e48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65e24.md#insn-00b65e48)
- 新版 `00b65f18`（命令位置の公開資料なし） · `00b65efc`（命令位置の公開資料なし） · `00b65f10`（命令位置の公開資料なし）

~~~diff
- 00b65e50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b65e50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65f18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b65f18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65e50 bytes 605203f9
+ 00b65f18 bytes 60b203f9
- 00b65e34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b65e34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65efc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b65efc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65e34 bytes 685243f9
+ 00b65efc bytes 68b243f9
- 00b65e48 ["INT_ADD", "register:40f0:8", ["const:b65e48:8", "const:4:8"]]
- 00b65e48 ["CALL", null, ["callee:00bde040:8"]]
+ 00b65f10 ["INT_ADD", "register:40f0:8", ["const:b65f10:8", "const:4:8"]]
+ 00b65f10 ["CALL", null, ["callee:00bde040:8"]]
- 00b65e48 bytes 52e00194
+ 00b65f10 bytes 4ce00194
~~~


<a id="compare-01dbb33b84166f5ea9606666dfaeaed6"></a>

### [`00b65e64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65e64.md) → [`00b65f2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65f2c.md) _ZN8firebase4auth10githubcred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b65f58",
      "incomplete_value": true,
      "site": "00b65f58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e90",
      "incomplete_value": true,
      "site": "00b65e90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "00b65f40",
      "incomplete_value": true,
      "site": "00b65f40",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e78",
      "incomplete_value": true,
      "site": "00b65e78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b65e78"
      ],
      [
        "FALL_THROUGH",
        "00b65f40"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b65f40",
      "incomplete_value": true,
      "site": "00b65f58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65e78",
      "incomplete_value": true,
      "site": "00b65e90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b65f3c",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65f58",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65f3c",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65f58",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65e90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65e64.md#insn-00b65e90) · [`00b65e74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65e64.md#insn-00b65e74) · [`00b65e88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65e64.md#insn-00b65e88)
- 新版 `00b65f58`（命令位置の公開資料なし） · `00b65f3c`（命令位置の公開資料なし） · `00b65f50`（命令位置の公開資料なし）

~~~diff
- 00b65e90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b65e90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65f58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b65f58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65e90 bytes 605203f9
+ 00b65f58 bytes 60b203f9
- 00b65e74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b65e74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65f3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b65f3c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65e74 bytes 685243f9
+ 00b65f3c bytes 68b243f9
- 00b65e88 ["INT_ADD", "register:40f0:8", ["const:b65e88:8", "const:4:8"]]
- 00b65e88 ["CALL", null, ["callee:00bde040:8"]]
+ 00b65f50 ["INT_ADD", "register:40f0:8", ["const:b65f50:8", "const:4:8"]]
+ 00b65f50 ["CALL", null, ["callee:00bde040:8"]]
- 00b65e88 bytes 42e00194
+ 00b65f50 bytes 3ce00194
~~~


<a id="compare-c3fecf0ace2c6c1b2eb93e44e7bb9e0f"></a>

### [`00b65ea4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ea4.md) → [`00b65f6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65f6c.md) _ZN8firebase4auth10githubcred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b65f9c",
      "incomplete_value": true,
      "site": "00b65f9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65ed4",
      "incomplete_value": true,
      "site": "00b65ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "00b65f80",
      "incomplete_value": true,
      "site": "00b65f80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65eb8",
      "incomplete_value": true,
      "site": "00b65eb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b65eb8"
      ],
      [
        "FALL_THROUGH",
        "00b65f80"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b65f80",
      "incomplete_value": true,
      "site": "00b65f9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65eb8",
      "incomplete_value": true,
      "site": "00b65ed4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b65f7c",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65f9c",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65f7c",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65f9c",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65ed4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ea4.md#insn-00b65ed4) · [`00b65eb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ea4.md#insn-00b65eb4) · [`00b65ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ea4.md#insn-00b65ecc)
- 新版 `00b65f9c`（命令位置の公開資料なし） · `00b65f7c`（命令位置の公開資料なし） · `00b65f94`（命令位置の公開資料なし）

~~~diff
- 00b65ed4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b65ed4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65f9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b65f9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65ed4 bytes 605203f9
+ 00b65f9c bytes 60b203f9
- 00b65eb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b65eb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65f7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b65f7c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65eb4 bytes 685243f9
+ 00b65f7c bytes 68b243f9
- 00b65ecc ["INT_ADD", "register:40f0:8", ["const:b65ecc:8", "const:4:8"]]
- 00b65ecc ["CALL", null, ["callee:00bde040:8"]]
+ 00b65f94 ["INT_ADD", "register:40f0:8", ["const:b65f94:8", "const:4:8"]]
+ 00b65f94 ["CALL", null, ["callee:00bde040:8"]]
- 00b65ecc bytes 31e00194
+ 00b65f94 bytes 2be00194
~~~


<a id="compare-c63d70beeb8f7bbe6e1e03300b37c9fa"></a>

### [`00b65ee8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ee8.md) → [`00b65fb0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b65/00b65fb0.md) _ZN8firebase4auth10githubcred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b65fe0",
      "incomplete_value": true,
      "site": "00b65fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f18",
      "incomplete_value": true,
      "site": "00b65f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "00b65fc4",
      "incomplete_value": true,
      "site": "00b65fc4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65efc",
      "incomplete_value": true,
      "site": "00b65efc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b65efc"
      ],
      [
        "FALL_THROUGH",
        "00b65fc4"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b65fc4",
      "incomplete_value": true,
      "site": "00b65fe0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65efc",
      "incomplete_value": true,
      "site": "00b65f18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b65fc0",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65fe0",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b65fc0",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b65fe0",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65f18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ee8.md#insn-00b65f18) · [`00b65ef8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ee8.md#insn-00b65ef8) · [`00b65f10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65ee8.md#insn-00b65f10)
- 新版 `00b65fe0`（命令位置の公開資料なし） · `00b65fc0`（命令位置の公開資料なし） · `00b65fd8`（命令位置の公開資料なし）

~~~diff
- 00b65f18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b65f18 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b65fe0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b65fe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b65f18 bytes 605203f9
+ 00b65fe0 bytes 60b203f9
- 00b65ef8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6a0:8"]]
- 00b65ef8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b65fc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:760:8"]]
+ 00b65fc0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b65ef8 bytes 685243f9
+ 00b65fc0 bytes 68b243f9
- 00b65f10 ["INT_ADD", "register:40f0:8", ["const:b65f10:8", "const:4:8"]]
- 00b65f10 ["CALL", null, ["callee:00bde040:8"]]
+ 00b65fd8 ["INT_ADD", "register:40f0:8", ["const:b65fd8:8", "const:4:8"]]
+ 00b65fd8 ["CALL", null, ["callee:00bde040:8"]]
- 00b65f10 bytes 20e00194
+ 00b65fd8 bytes 1ae00194
~~~


<a id="compare-3b3b34a5c6a1301a3f92a28c177874a6"></a>

### [`00b65f38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65f38.md) → [`00b66000`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66000.md) _ZN8firebase4auth10githubcred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b66058",
      "incomplete_value": true,
      "site": "00b66058",
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
            "const:768:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f90",
      "incomplete_value": true,
      "site": "00b65f90",
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
            "const:6a8:8"
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
      "definition_site": "00b66034",
      "incomplete_value": true,
      "site": "00b66040",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:760:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b65f6c",
      "incomplete_value": true,
      "site": "00b65f78",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6a0:8"
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
      "00b66014",
      "READ",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66034",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66058",
      "WRITE",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b66014",
      "READ",
      [
        "storage",
        "010a1768",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66034",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66058",
      "WRITE",
      [
        "storage",
        "010a1768",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65f78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65f38.md#insn-00b65f78) · [`00b65f90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65f38.md#insn-00b65f90) · [`00b65f4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65f38.md#insn-00b65f4c)
- 新版 `00b66040`（命令位置の公開資料なし） · `00b66058`（命令位置の公開資料なし） · `00b66014`（命令位置の公開資料なし）

~~~diff
- 00b65f78 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b65f78 ["INT_ADD", "register:40f0:8", ["const:b65f78:8", "const:4:8"]]
- 00b65f78 ["CALLIND", null, ["register:0:8"]]
+ 00b66040 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66040 ["INT_ADD", "register:40f0:8", ["const:b66040:8", "const:4:8"]]
+ 00b66040 ["CALLIND", null, ["register:0:8"]]
- 00b65f78 bytes 00013fd6
+ 00b66040 bytes 00013fd6
- 00b65f90 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b65f90 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6a8:8"]]
- 00b65f90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b66058 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b66058 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:768:8"]]
+ 00b66058 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b65f90 bytes a0a21a39
+ 00b66058 bytes a0a21d39
- 00b65f4c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6a8:8"]]
- 00b65f4c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b65f4c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b66014 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:768:8"]]
+ 00b66014 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b66014 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b65f4c bytes a8a25a39
+ 00b66014 bytes a8a25d39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7897dc6930ec61be6508baf67eea4852"></a>

### [`00b65fa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65fa4.md) → [`00b6606c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6606c.md) _ZN8firebase4auth10githubcred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b65fe0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66000"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b660a8"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66080",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6608c",
      "READ",
      [
        "storage",
        "010a16a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66094",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b65fe4"
      ]
    ]
  ],
  "added": [
    [
      "00b66080",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6608c",
      "READ",
      [
        "storage",
        "010a1768",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66094",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b660ac"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b65fbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65fa4.md#insn-00b65fbc) · [`00b65fe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65fa4.md#insn-00b65fe0) · [`00b65fe8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b65/00b65fa4.md#insn-00b65fe8)
- 新版 `00b66084`（命令位置の公開資料なし）

~~~diff
- 00b65fbc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b65fbc ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b66084 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b66084 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b65fbc bytes 410200b4
+ 00b66084 bytes 410200b4
- 00b65fe0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b65fe0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b65fe0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6a8:8"]]
- 00b65fe0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b65fe0 bytes bfa21a39
- 00b65fe8 ["INT_ADD", "register:40f0:8", ["const:b65fe8:8", "const:4:8"]]
- 00b65fe8 ["CALL", null, ["callee:00bde090:8"]]
- 00b65fe8 bytes fedf0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-31aa63cfa3b425ddc0a96fd0195373bb"></a>

### [`00b66014`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66014.md) → [`00b660dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b660dc.md) _ZN8firebase4auth10githubcred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b6611c",
      "incomplete_value": true,
      "site": "00b6611c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:760:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66054",
      "incomplete_value": true,
      "site": "00b66054",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6a0:8"
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
      "definition_site": "00b660f8",
      "incomplete_value": true,
      "site": "00b660f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66030",
      "incomplete_value": true,
      "site": "00b66030",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b66030"
      ],
      [
        "FALL_THROUGH",
        "00b660f8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b660f8",
      "incomplete_value": true,
      "site": "00b6611c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66030",
      "incomplete_value": true,
      "site": "00b66054",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b660f0",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6611c",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66130",
      "PARAM",
      [
        "storage",
        "00c12310",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b660f0",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6611c",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66130",
      "PARAM",
      [
        "storage",
        "00c123c0",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66014.md#insn-00b66054) · [`00b66028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66014.md#insn-00b66028) · [`00b6604c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66014.md#insn-00b6604c)
- 新版 `00b6611c`（命令位置の公開資料なし） · `00b660f0`（命令位置の公開資料なし） · `00b66114`（命令位置の公開資料なし）

~~~diff
- 00b66054 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
- 00b66054 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6611c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
+ 00b6611c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66054 bytes 805203f9
+ 00b6611c bytes 80b203f9
- 00b66028 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
- 00b66028 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b660f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:760:8"]]
+ 00b660f0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66028 bytes 815243f9
+ 00b660f0 bytes 81b243f9
- 00b6604c ["INT_ADD", "register:40f0:8", ["const:b6604c:8", "const:4:8"]]
- 00b6604c ["CALL", null, ["callee:00bde040:8"]]
+ 00b66114 ["INT_ADD", "register:40f0:8", ["const:b66114:8", "const:4:8"]]
+ 00b66114 ["CALL", null, ["callee:00bde040:8"]]
- 00b6604c bytes d1df0194
+ 00b66114 bytes cbdf0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-945c93932106a2665c143afb728d1c1b"></a>

### [`00b66084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66084.md) → [`00b6614c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6614c.md) _ZN8firebase4auth10githubcred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b66168",
      "incomplete_value": false,
      "site": "00b6616c",
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
    "old": {
      "definition_site": "00b660a0",
      "incomplete_value": false,
      "site": "00b660a4",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b66178",
      "incomplete_value": true,
      "site": "00b66184",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b660b0",
      "incomplete_value": true,
      "site": "00b660bc",
      "value": [
        "LOAD",
        "8",
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
      "00b66168",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b66178",
      "DATA",
      [
        "storage",
        "010a16b0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b66168",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b66178",
      "DATA",
      [
        "storage",
        "010a1770",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b660a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66084.md#insn-00b660a4) · [`00b660a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66084.md#insn-00b660a0) · [`00b660ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66084.md#insn-00b660ac)
- 新版 `00b6616c`（命令位置の公開資料なし） · `00b66168`（命令位置の公開資料なし） · `00b66174`（命令位置の公開資料なし）

~~~diff
- 00b660a4 ["INT_ADD", "register:40f0:8", ["const:b660a4:8", "const:4:8"]]
- 00b660a4 ["CALL", null, ["callee:00bde130:8"]]
+ 00b6616c ["INT_ADD", "register:40f0:8", ["const:b6616c:8", "const:4:8"]]
+ 00b6616c ["CALL", null, ["callee:00bde130:8"]]
- 00b660a4 bytes f7df0194
+ 00b6616c bytes f1df0194
- 00b660a0 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b660a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b660a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b660a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66168 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b66168 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66168 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66168 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b660a0 bytes 001c1591
+ 00b66168 bytes 00501791
- 00b660ac ["COPY", "tmp:0:8", ["const:6b0:8"]]
- 00b660ac ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b660ac ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b660ac ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b66174 ["COPY", "tmp:0:8", ["const:770:8"]]
+ 00b66174 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66174 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66174 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b660ac bytes 08c11a91
+ 00b66174 bytes 08c11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-afdb9bf93186c5b00464d6f97f0ee323"></a>

### [`00b660c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b660c0.md) → [`00b66188`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66188.md) _ZN8firebase4auth10githubcred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66100"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b661c8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b660dc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b660d4",
      "READ",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b660dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b661cc"
      ]
    ],
    [
      "unmatched:00b66100",
      "WRITE",
      [
        "storage",
        "010a16a0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6619c",
      "READ",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ],
    [
      "00b661a4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b661cc"
      ]
    ],
    [
      "00b661c8",
      "WRITE",
      [
        "storage",
        "010a1760",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b660dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b660c0.md#insn-00b660dc) · [`00b660f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b660c0.md#insn-00b660f8) · [`00b66100`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b660c0.md#insn-00b66100)
- 新版 `00b661c0`（命令位置の公開資料なし）

~~~diff
- 00b660dc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b660dc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b660dc bytes 410100b5
- 00b660f8 ["INT_ADD", "register:40f0:8", ["const:b660f8:8", "const:4:8"]]
- 00b660f8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b661c0 ["INT_ADD", "register:40f0:8", ["const:b661c0:8", "const:4:8"]]
+ 00b661c0 ["CALL", null, ["callee:00bde040:8"]]
- 00b660f8 bytes a6df0194
+ 00b661c0 bytes a0df0194
- 00b66100 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6a0:8"]]
- 00b66100 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66100 bytes 805203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6496ef923d53bcb2a94258f2c3df3fcb"></a>

### [`00b66130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66130.md) → [`00b661f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b661f8.md) _ZN8firebase4auth10githubcred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b66214",
      "incomplete_value": false,
      "site": "00b66218",
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
    "old": {
      "definition_site": "00b6614c",
      "incomplete_value": false,
      "site": "00b66150",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b66224",
      "incomplete_value": true,
      "site": "00b66230",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b6615c",
      "incomplete_value": true,
      "site": "00b66168",
      "value": [
        "LOAD",
        "8",
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
      "00b66214",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b66224",
      "DATA",
      [
        "storage",
        "010a16b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b66214",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b66224",
      "DATA",
      [
        "storage",
        "010a1778",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66150`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66130.md#insn-00b66150) · [`00b6614c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66130.md#insn-00b6614c) · [`00b66158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66130.md#insn-00b66158)
- 新版 `00b66218`（命令位置の公開資料なし） · `00b66214`（命令位置の公開資料なし） · `00b66220`（命令位置の公開資料なし）

~~~diff
- 00b66150 ["INT_ADD", "register:40f0:8", ["const:b66150:8", "const:4:8"]]
- 00b66150 ["CALL", null, ["callee:00bde130:8"]]
+ 00b66218 ["INT_ADD", "register:40f0:8", ["const:b66218:8", "const:4:8"]]
+ 00b66218 ["CALL", null, ["callee:00bde130:8"]]
- 00b66150 bytes ccdf0194
+ 00b66218 bytes c6df0194
- 00b6614c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b6614c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b6614c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b6614c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66214 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b66214 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66214 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66214 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b6614c bytes 00c81791
+ 00b66214 bytes 00fc1991
- 00b66158 ["COPY", "tmp:0:8", ["const:6b8:8"]]
- 00b66158 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b66158 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b66158 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b66220 ["COPY", "tmp:0:8", ["const:778:8"]]
+ 00b66220 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66220 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66220 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b66158 bytes 08e11a91
+ 00b66220 bytes 08e11d91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b74a57798eb78e18548b1628be5b2a4c"></a>

### [`00b6616c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6616c.md) → [`00b66234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66234.md) _ZN8firebase4auth10googlecred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 68.75% / 新版 68.75%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66198"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b66260"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66248",
      "incomplete_value": true,
      "site": "00b66248",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66180",
      "incomplete_value": true,
      "site": "00b66180",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b66244",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66248",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6619c"
      ]
    ],
    [
      "unmatched:00b66198",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66244",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66248",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b66264"
      ]
    ],
    [
      "00b66260",
      "WRITE",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6616c.md#insn-00b66198) · [`00b661a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6616c.md#insn-00b661a8)
- 新版 `00b66260`（命令位置の公開資料なし）

~~~diff
- 00b66198 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b66198 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66198 bytes 606203f9
- 00b661a8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b661a8 ["RETURN", null, ["register:0:8"]]
- 00b661a8 bytes c0035fd6
+ 00b66260 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b66260 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66260 bytes 60c203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fea322d7a35e97db359de2c54803d19"></a>

### [`00b661ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b661ac.md) → [`00b66274`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66274.md) _ZN8firebase4auth10googlecred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b661ac"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b661b0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b661b0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b661ac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b661b0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b66284",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66274",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b66278",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b66284",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b661ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b661ac.md#insn-00b661ac) · [`00b661b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b661ac.md#insn-00b661b0) · [`00b661c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b661ac.md#insn-00b661c0)
- 新版 `00b66288`（命令位置の公開資料なし）

~~~diff
- 00b661ac ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b661ac ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b661ac ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b661ac bytes f30f1ef8
- 00b661b0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b661b0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b661b0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b661b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b661b0 bytes fd7b01a9
- 00b661c0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b661c0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b66288 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b66288 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b661c0 bytes e80000b5
+ 00b66288 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72206ec180b8cabf25622850700063cd"></a>

### [`00b661ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b661ec.md) → [`00b662b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b662b4.md) _ZN8firebase4auth10googlecred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b662e4",
      "incomplete_value": true,
      "site": "00b662e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6621c",
      "incomplete_value": true,
      "site": "00b6621c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "definition_site": "00b662c8",
      "incomplete_value": true,
      "site": "00b662c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66200",
      "incomplete_value": true,
      "site": "00b66200",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b66200"
      ],
      [
        "FALL_THROUGH",
        "00b662c8"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b662c8",
      "incomplete_value": true,
      "site": "00b662e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66200",
      "incomplete_value": true,
      "site": "00b6621c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b662c4",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b662e4",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b662c4",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b662e4",
      "WRITE",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6621c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b661ec.md#insn-00b6621c) · [`00b661fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b661ec.md#insn-00b661fc) · [`00b66214`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b661ec.md#insn-00b66214)
- 新版 `00b662e4`（命令位置の公開資料なし） · `00b662c4`（命令位置の公開資料なし） · `00b662dc`（命令位置の公開資料なし）

~~~diff
- 00b6621c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b6621c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b662e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b662e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6621c bytes 606203f9
+ 00b662e4 bytes 60c203f9
- 00b661fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b661fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b662c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b662c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b661fc bytes 686243f9
+ 00b662c4 bytes 68c243f9
- 00b66214 ["INT_ADD", "register:40f0:8", ["const:b66214:8", "const:4:8"]]
- 00b66214 ["CALL", null, ["callee:00bde040:8"]]
+ 00b662dc ["INT_ADD", "register:40f0:8", ["const:b662dc:8", "const:4:8"]]
+ 00b662dc ["CALL", null, ["callee:00bde040:8"]]
- 00b66214 bytes 5fdf0194
+ 00b662dc bytes 59df0194
~~~


<a id="compare-9612ec75219ac14b2586bed9ff5dfa48"></a>

### [`00b66230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66230.md) → [`00b662f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b662f8.md) _ZN8firebase4auth10googlecred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66260"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b66328"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b6630c",
      "incomplete_value": true,
      "site": "00b6630c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66244",
      "incomplete_value": true,
      "site": "00b66244",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b66308",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6630c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b66264"
      ]
    ],
    [
      "unmatched:00b66260",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66308",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6630c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b6632c"
      ]
    ],
    [
      "00b66328",
      "WRITE",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66260`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66230.md#insn-00b66260) · [`00b66270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66230.md#insn-00b66270)
- 新版 `00b66328`（命令位置の公開資料なし）

~~~diff
- 00b66260 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6c0:8"]]
- 00b66260 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66260 bytes 606203f9
- 00b66270 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b66270 ["RETURN", null, ["register:0:8"]]
- 00b66270 bytes c0035fd6
+ 00b66328 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:780:8"]]
+ 00b66328 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66328 bytes 60c203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5bf69abac529826b5aba782315a46e0a"></a>

### [`00b66280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66280.md) → [`00b66348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66348.md) _ZN8firebase4auth10googlecred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b663a0",
      "incomplete_value": true,
      "site": "00b663a0",
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
            "const:788:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b662d8",
      "incomplete_value": true,
      "site": "00b662d8",
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
            "const:6c8:8"
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
      "definition_site": "00b6637c",
      "incomplete_value": true,
      "site": "00b66388",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:780:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b662b4",
      "incomplete_value": true,
      "site": "00b662c0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6c0:8"
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
      "00b6635c",
      "READ",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6637c",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b663a0",
      "WRITE",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b6635c",
      "READ",
      [
        "storage",
        "010a1788",
        null,
        "undefined1"
      ]
    ],
    [
      "00b6637c",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b663a0",
      "WRITE",
      [
        "storage",
        "010a1788",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b662c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66280.md#insn-00b662c0) · [`00b662d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66280.md#insn-00b662d8) · [`00b66294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66280.md#insn-00b66294)
- 新版 `00b66388`（命令位置の公開資料なし） · `00b663a0`（命令位置の公開資料なし） · `00b6635c`（命令位置の公開資料なし）

~~~diff
- 00b662c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b662c0 ["INT_ADD", "register:40f0:8", ["const:b662c0:8", "const:4:8"]]
- 00b662c0 ["CALLIND", null, ["register:0:8"]]
+ 00b66388 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66388 ["INT_ADD", "register:40f0:8", ["const:b66388:8", "const:4:8"]]
+ 00b66388 ["CALLIND", null, ["register:0:8"]]
- 00b662c0 bytes 00013fd6
+ 00b66388 bytes 00013fd6
- 00b662d8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b662d8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6c8:8"]]
- 00b662d8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b663a0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b663a0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:788:8"]]
+ 00b663a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b662d8 bytes a0221b39
+ 00b663a0 bytes a0221e39
- 00b66294 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6c8:8"]]
- 00b66294 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b66294 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b6635c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:788:8"]]
+ 00b6635c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b6635c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b66294 bytes a8225b39
+ 00b6635c bytes a8225e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c9524aa385fa909c802d9f4f17540e1c"></a>

### [`00b662ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b662ec.md) → [`00b663b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b663b4.md) _ZN8firebase4auth10googlecred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66328"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66348"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b663f0"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b663c8",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b663d4",
      "READ",
      [
        "storage",
        "010a16c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b663dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b6632c"
      ]
    ]
  ],
  "added": [
    [
      "00b663c8",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b663d4",
      "READ",
      [
        "storage",
        "010a1788",
        null,
        "undefined1"
      ]
    ],
    [
      "00b663dc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b663f4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b662ec.md#insn-00b66304) · [`00b66328`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b662ec.md#insn-00b66328) · [`00b66330`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b662ec.md#insn-00b66330)
- 新版 `00b663cc`（命令位置の公開資料なし）

~~~diff
- 00b66304 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b66304 ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00b663cc ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b663cc ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b66304 bytes 410200b4
+ 00b663cc bytes 410200b4
- 00b66328 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b66328 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b66328 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6c8:8"]]
- 00b66328 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b66328 bytes bf221b39
- 00b66330 ["INT_ADD", "register:40f0:8", ["const:b66330:8", "const:4:8"]]
- 00b66330 ["CALL", null, ["callee:00bde090:8"]]
- 00b66330 bytes 2cdf0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ed852e37122bfb35d0e8ab13c04f98af"></a>

### [`00b6635c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6635c.md) → [`00b66424`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66424.md) _ZN8firebase4auth10googlecred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b66464",
      "incomplete_value": true,
      "site": "00b66464",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6639c",
      "incomplete_value": true,
      "site": "00b6639c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "definition_site": "00b66440",
      "incomplete_value": true,
      "site": "00b66440",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66378",
      "incomplete_value": true,
      "site": "00b66378",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b66378"
      ],
      [
        "FALL_THROUGH",
        "00b66440"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b66440",
      "incomplete_value": true,
      "site": "00b66464",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66378",
      "incomplete_value": true,
      "site": "00b6639c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b66438",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66464",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66478",
      "PARAM",
      [
        "storage",
        "00c12328",
        null,
        "pointer"
      ]
    ]
  ],
  "added": [
    [
      "00b66438",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66464",
      "WRITE",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66478",
      "PARAM",
      [
        "storage",
        "00c123d8",
        null,
        "pointer"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6639c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6635c.md#insn-00b6639c) · [`00b66370`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6635c.md#insn-00b66370) · [`00b66394`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6635c.md#insn-00b66394)
- 新版 `00b66464`（命令位置の公開資料なし） · `00b66438`（命令位置の公開資料なし） · `00b6645c`（命令位置の公開資料なし）

~~~diff
- 00b6639c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00b6639c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66464 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00b66464 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b6639c bytes 806203f9
+ 00b66464 bytes 80c203f9
- 00b66370 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00b66370 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66438 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00b66438 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66370 bytes 816243f9
+ 00b66438 bytes 81c243f9
- 00b66394 ["INT_ADD", "register:40f0:8", ["const:b66394:8", "const:4:8"]]
- 00b66394 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6645c ["INT_ADD", "register:40f0:8", ["const:b6645c:8", "const:4:8"]]
+ 00b6645c ["CALL", null, ["callee:00bde040:8"]]
- 00b66394 bytes ffde0194
+ 00b6645c bytes f9de0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-758dcf59ef10a6415bc84d06725e22e6"></a>

### [`00b66408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66408.md) → [`00b664d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b664d0.md) _ZN8firebase4auth10googlecred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b66510",
      "incomplete_value": true,
      "site": "00b66510",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:780:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66448",
      "incomplete_value": true,
      "site": "00b66448",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6c0:8"
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
      "definition_site": "00b664ec",
      "incomplete_value": true,
      "site": "00b664ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66424",
      "incomplete_value": true,
      "site": "00b66424",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b66424"
      ],
      [
        "FALL_THROUGH",
        "00b664ec"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b664ec",
      "incomplete_value": true,
      "site": "00b66510",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66424",
      "incomplete_value": true,
      "site": "00b66448",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b664e4",
      "READ",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66510",
      "WRITE",
      [
        "storage",
        "010a16c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66528",
      "PARAM",
      [
        "storage",
        "010a16d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b664e4",
      "READ",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66510",
      "WRITE",
      [
        "storage",
        "010a1780",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66528",
      "PARAM",
      [
        "storage",
        "010a1798",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66448`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66408.md#insn-00b66448) · [`00b6641c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66408.md#insn-00b6641c) · [`00b66440`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66408.md#insn-00b66440)
- 新版 `00b66510`（命令位置の公開資料なし） · `00b664e4`（命令位置の公開資料なし） · `00b66508`（命令位置の公開資料なし）

~~~diff
- 00b66448 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00b66448 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66510 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00b66510 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66448 bytes 806203f9
+ 00b66510 bytes 80c203f9
- 00b6641c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6c0:8"]]
- 00b6641c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b664e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:780:8"]]
+ 00b664e4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6641c bytes 816243f9
+ 00b664e4 bytes 81c243f9
- 00b66440 ["INT_ADD", "register:40f0:8", ["const:b66440:8", "const:4:8"]]
- 00b66440 ["CALL", null, ["callee:00bde040:8"]]
+ 00b66508 ["INT_ADD", "register:40f0:8", ["const:b66508:8", "const:4:8"]]
+ 00b66508 ["CALL", null, ["callee:00bde040:8"]]
- 00b66440 bytes d4de0194
+ 00b66508 bytes cede0194
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d2dc534687512bdd3fc285b34265d4d0"></a>

### [`00b66478`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66478.md) → [`00b66540`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66540.md) _ZN8firebase4auth10googlecred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b6655c",
      "incomplete_value": false,
      "site": "00b66560",
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
    "old": {
      "definition_site": "00b66494",
      "incomplete_value": false,
      "site": "00b66498",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b6656c",
      "incomplete_value": true,
      "site": "00b66578",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b664a4",
      "incomplete_value": true,
      "site": "00b664b0",
      "value": [
        "LOAD",
        "8",
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
      "00b6655c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b6656c",
      "DATA",
      [
        "storage",
        "010a16d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b6655c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b6656c",
      "DATA",
      [
        "storage",
        "010a1798",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66498`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66478.md#insn-00b66498) · [`00b66494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66478.md#insn-00b66494) · [`00b664a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66478.md#insn-00b664a0)
- 新版 `00b66560`（命令位置の公開資料なし） · `00b6655c`（命令位置の公開資料なし） · `00b66568`（命令位置の公開資料なし）

~~~diff
- 00b66498 ["INT_ADD", "register:40f0:8", ["const:b66498:8", "const:4:8"]]
- 00b66498 ["CALL", null, ["callee:00bde130:8"]]
+ 00b66560 ["INT_ADD", "register:40f0:8", ["const:b66560:8", "const:4:8"]]
+ 00b66560 ["CALL", null, ["callee:00bde130:8"]]
- 00b66498 bytes fade0194
+ 00b66560 bytes f4de0194
- 00b66494 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b66494 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66494 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66494 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b6655c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b6655c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6655c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b6655c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66494 bytes 00c81791
+ 00b6655c bytes 00fc1991
- 00b664a0 ["COPY", "tmp:0:8", ["const:6d8:8"]]
- 00b664a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b664a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b664a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b66568 ["COPY", "tmp:0:8", ["const:798:8"]]
+ 00b66568 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66568 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66568 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b664a0 bytes 08611b91
+ 00b66568 bytes 08611e91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28e070f13796d8e1304dd9614f611b99"></a>

### [`00b664f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b664f4.md) → [`00b665bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b665bc.md) _ZN8firebase4auth13playgamescred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b665e8",
      "incomplete_value": true,
      "site": "00b665e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66520",
      "incomplete_value": true,
      "site": "00b66520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "00b665d0",
      "incomplete_value": true,
      "site": "00b665d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66508",
      "incomplete_value": true,
      "site": "00b66508",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b665d8",
      "incomplete_value": false,
      "site": "00b665e0",
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
            "const:fed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66510",
      "incomplete_value": false,
      "site": "00b66518",
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
            "const:ff4:8"
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
      "00b665cc",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b665d8",
      "PARAM",
      [
        "storage",
        "002a2ff4",
        null,
        "string"
      ]
    ],
    [
      "00b665e8",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b665cc",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b665d8",
      "PARAM",
      [
        "storage",
        "002a2fed",
        null,
        "string"
      ]
    ],
    [
      "00b665e8",
      "WRITE",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66518`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b664f4.md#insn-00b66518) · [`00b66520`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b664f4.md#insn-00b66520) · [`00b66504`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b664f4.md#insn-00b66504)
- 新版 `00b665e0`（命令位置の公開資料なし） · `00b665e8`（命令位置の公開資料なし） · `00b665cc`（命令位置の公開資料なし）

~~~diff
- 00b66518 ["INT_ADD", "register:40f0:8", ["const:b66518:8", "const:4:8"]]
- 00b66518 ["CALL", null, ["callee:00bde040:8"]]
+ 00b665e0 ["INT_ADD", "register:40f0:8", ["const:b665e0:8", "const:4:8"]]
+ 00b665e0 ["CALL", null, ["callee:00bde040:8"]]
- 00b66518 bytes 9ede0194
+ 00b665e0 bytes 98de0194
- 00b66520 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b66520 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b665e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00b665e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66520 bytes 607203f9
+ 00b665e8 bytes 60d203f9
- 00b66504 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b66504 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b665cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00b665cc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66504 bytes 687243f9
+ 00b665cc bytes 68d243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4bdfd4465f9b8d261f980fb10251059b"></a>

### [`00b66534`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66534.md) → [`00b665fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b665fc.md) _ZN8firebase4auth13playgamescred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b6662c",
      "incomplete_value": true,
      "site": "00b6662c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66564",
      "incomplete_value": true,
      "site": "00b66564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "00b66610",
      "incomplete_value": true,
      "site": "00b66610",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66548",
      "incomplete_value": true,
      "site": "00b66548",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6661c",
      "incomplete_value": false,
      "site": "00b66624",
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
            "const:fed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66554",
      "incomplete_value": false,
      "site": "00b6655c",
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
            "const:ff4:8"
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
      "00b6660c",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6661c",
      "PARAM",
      [
        "storage",
        "002a2ff4",
        null,
        "string"
      ]
    ],
    [
      "00b6662c",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6660c",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6661c",
      "PARAM",
      [
        "storage",
        "002a2fed",
        null,
        "string"
      ]
    ],
    [
      "00b6662c",
      "WRITE",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6655c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66534.md#insn-00b6655c) · [`00b66564`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66534.md#insn-00b66564) · [`00b66544`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66534.md#insn-00b66544)
- 新版 `00b66624`（命令位置の公開資料なし） · `00b6662c`（命令位置の公開資料なし） · `00b6660c`（命令位置の公開資料なし）

~~~diff
- 00b6655c ["INT_ADD", "register:40f0:8", ["const:b6655c:8", "const:4:8"]]
- 00b6655c ["CALL", null, ["callee:00bde040:8"]]
+ 00b66624 ["INT_ADD", "register:40f0:8", ["const:b66624:8", "const:4:8"]]
+ 00b66624 ["CALL", null, ["callee:00bde040:8"]]
- 00b6655c bytes 8dde0194
+ 00b66624 bytes 87de0194
- 00b66564 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b66564 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b6662c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00b6662c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66564 bytes 607203f9
+ 00b6662c bytes 60d203f9
- 00b66544 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b66544 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6660c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7a0:8"]]
+ 00b6660c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66544 bytes 687243f9
+ 00b6660c bytes 68d243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0bf0e27e5fbe0280c17a289ed35655e4"></a>

### [`00b66578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66578.md) → [`00b66640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66640.md) _ZN8firebase4auth13playgamescred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 33.33% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 3件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b665a8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b66670"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66654",
      "incomplete_value": true,
      "site": "00b66654",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6658c",
      "incomplete_value": true,
      "site": "00b6658c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b66650",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b66594",
      "PARAM",
      [
        "storage",
        "002a2ff4",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00b665a8",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66650",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6665c",
      "PARAM",
      [
        "storage",
        "002a2fed",
        null,
        "string"
      ]
    ],
    [
      "00b66670",
      "WRITE",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6658c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66578.md#insn-00b6658c) · [`00b665a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66578.md#insn-00b665a0) · [`00b665a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66578.md#insn-00b665a8)
- 新版 `00b66654`（命令位置の公開資料なし） · `00b66668`（命令位置の公開資料なし）

~~~diff
- 00b6658c ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b6658c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00b66654 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b66654 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6658c bytes 080100b5
+ 00b66654 bytes 080100b5
- 00b665a0 ["INT_ADD", "register:40f0:8", ["const:b665a0:8", "const:4:8"]]
- 00b665a0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b66668 ["INT_ADD", "register:40f0:8", ["const:b66668:8", "const:4:8"]]
+ 00b66668 ["CALL", null, ["callee:00bde040:8"]]
- 00b665a0 bytes 7cde0194
+ 00b66668 bytes 76de0194
- 00b665a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:6e0:8"]]
- 00b665a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b665a8 bytes 607203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-94a0df7f136224ddddfef5bc6f35850a"></a>

### [`00b665c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b665c8.md) → [`00b66690`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66690.md) _ZN8firebase4auth13playgamescred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b666e8",
      "incomplete_value": true,
      "site": "00b666e8",
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
            "const:7a8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66620",
      "incomplete_value": true,
      "site": "00b66620",
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
            "const:6e8:8"
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
      "definition_site": "00b666c4",
      "incomplete_value": true,
      "site": "00b666d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7a0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b665fc",
      "incomplete_value": true,
      "site": "00b66608",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:6e0:8"
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
      "00b666a4",
      "READ",
      [
        "storage",
        "010a16e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b666c4",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b666e8",
      "WRITE",
      [
        "storage",
        "010a16e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b666a4",
      "READ",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b666c4",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b666e8",
      "WRITE",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66608`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b665c8.md#insn-00b66608) · [`00b66620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b665c8.md#insn-00b66620) · [`00b665dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b665c8.md#insn-00b665dc)
- 新版 `00b666d0`（命令位置の公開資料なし） · `00b666e8`（命令位置の公開資料なし） · `00b666a4`（命令位置の公開資料なし）

~~~diff
- 00b66608 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66608 ["INT_ADD", "register:40f0:8", ["const:b66608:8", "const:4:8"]]
- 00b66608 ["CALLIND", null, ["register:0:8"]]
+ 00b666d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b666d0 ["INT_ADD", "register:40f0:8", ["const:b666d0:8", "const:4:8"]]
+ 00b666d0 ["CALLIND", null, ["register:0:8"]]
- 00b66608 bytes 00013fd6
+ 00b666d0 bytes 00013fd6
- 00b66620 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b66620 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:6e8:8"]]
- 00b66620 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b666e8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b666e8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7a8:8"]]
+ 00b666e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b66620 bytes a0a21b39
+ 00b666e8 bytes a0a21e39
- 00b665dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:6e8:8"]]
- 00b665dc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b665dc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b666a4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7a8:8"]]
+ 00b666a4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b666a4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b665dc bytes a8a25b39
+ 00b666a4 bytes a8a25e39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-60f089d96030b1feccdc73b923cee1b0"></a>

### [`00b66634`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66634.md) → [`00b666fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b666fc.md) _ZN8firebase4auth13playgamescred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 82.14% / 新版 82.14%

CFGの説明率　旧版 57.14% / 新版 66.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66670"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b66758",
      "incomplete_value": true,
      "site": "00b66758",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66690",
      "incomplete_value": true,
      "site": "00b66690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6e0:8"
          ]
        ]
      ]
    },
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b66738"
    },
    "old": null
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b66710",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6671c",
      "READ",
      [
        "storage",
        "010a16e8",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00b66670",
      "WRITE",
      [
        "storage",
        "010a16e8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b66710",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6671c",
      "READ",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66738",
      "WRITE",
      [
        "storage",
        "010a17a8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b6664c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66634.md#insn-00b6664c) · [`00b6666c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66634.md#insn-00b6666c) · [`00b66670`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66634.md#insn-00b66670)
- 新版 `00b66714`（命令位置の公開資料なし）

~~~diff
- 00b6664c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b6664c ["CBRANCH", null, ["local:b5:8", "tmp:0:1"]]
+ 00b66714 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00b66714 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00b6664c bytes 410200b4
+ 00b66714 bytes 410200b4
- 00b6666c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b6666c ["INT_ADD", "register:40f0:8", ["const:b6666c:8", "const:4:8"]]
- 00b6666c ["CALLIND", null, ["register:0:8"]]
- 00b6666c bytes 00013fd6
- 00b66670 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b66670 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b66670 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:6e8:8"]]
- 00b66670 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b66670 bytes bfa21b39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d146177d15dbfec3201fd7ed30f4fa7b"></a>

### [`00b666a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b666a4.md) → [`00b6676c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b6676c.md) _ZN8firebase4auth13playgamescred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b667ac",
      "incomplete_value": true,
      "site": "00b667ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b666e4",
      "incomplete_value": true,
      "site": "00b666e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "00b66788",
      "incomplete_value": true,
      "site": "00b66788",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b666c0",
      "incomplete_value": true,
      "site": "00b666c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66790",
      "incomplete_value": false,
      "site": "00b667a4",
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
            "const:fed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b666c8",
      "incomplete_value": false,
      "site": "00b666dc",
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
            "const:ff4:8"
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
      "00b66780",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66790",
      "PARAM",
      [
        "storage",
        "002a2ff4",
        null,
        "string"
      ]
    ],
    [
      "00b667ac",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66780",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66790",
      "PARAM",
      [
        "storage",
        "002a2fed",
        null,
        "string"
      ]
    ],
    [
      "00b667ac",
      "WRITE",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b666dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b666a4.md#insn-00b666dc) · [`00b666e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b666a4.md#insn-00b666e4) · [`00b666b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b666a4.md#insn-00b666b8)
- 新版 `00b667a4`（命令位置の公開資料なし） · `00b667ac`（命令位置の公開資料なし） · `00b66780`（命令位置の公開資料なし）

~~~diff
- 00b666dc ["INT_ADD", "register:40f0:8", ["const:b666dc:8", "const:4:8"]]
- 00b666dc ["CALL", null, ["callee:00bde040:8"]]
+ 00b667a4 ["INT_ADD", "register:40f0:8", ["const:b667a4:8", "const:4:8"]]
+ 00b667a4 ["CALL", null, ["callee:00bde040:8"]]
- 00b666dc bytes 2dde0194
+ 00b667a4 bytes 27de0194
- 00b666e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
- 00b666e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b667ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
+ 00b667ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b666e4 bytes 807203f9
+ 00b667ac bytes 80d203f9
- 00b666b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
- 00b666b8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66780 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
+ 00b66780 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b666b8 bytes 817243f9
+ 00b66780 bytes 81d243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4e7ae34a1eee8ca8e16cb8a807e176c9"></a>

### [`00b66750`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66750.md) → [`00b66818`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66818.md) _ZN8firebase4auth13playgamescred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b66858",
      "incomplete_value": true,
      "site": "00b66858",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7a0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66790",
      "incomplete_value": true,
      "site": "00b66790",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:6e0:8"
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
      "definition_site": "00b66834",
      "incomplete_value": true,
      "site": "00b66834",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6676c",
      "incomplete_value": true,
      "site": "00b6676c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b6683c",
      "incomplete_value": false,
      "site": "00b66850",
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
            "const:fed:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66774",
      "incomplete_value": false,
      "site": "00b66788",
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
            "const:ff4:8"
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
      "00b6682c",
      "READ",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6683c",
      "PARAM",
      [
        "storage",
        "002a2ff4",
        null,
        "string"
      ]
    ],
    [
      "00b66858",
      "WRITE",
      [
        "storage",
        "010a16e0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b6682c",
      "READ",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b6683c",
      "PARAM",
      [
        "storage",
        "002a2fed",
        null,
        "string"
      ]
    ],
    [
      "00b66858",
      "WRITE",
      [
        "storage",
        "010a17a0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66788`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66750.md#insn-00b66788) · [`00b66790`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66750.md#insn-00b66790) · [`00b66764`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66750.md#insn-00b66764)
- 新版 `00b66850`（命令位置の公開資料なし） · `00b66858`（命令位置の公開資料なし） · `00b6682c`（命令位置の公開資料なし）

~~~diff
- 00b66788 ["INT_ADD", "register:40f0:8", ["const:b66788:8", "const:4:8"]]
- 00b66788 ["CALL", null, ["callee:00bde040:8"]]
+ 00b66850 ["INT_ADD", "register:40f0:8", ["const:b66850:8", "const:4:8"]]
+ 00b66850 ["CALL", null, ["callee:00bde040:8"]]
- 00b66788 bytes 02de0194
+ 00b66850 bytes fcdd0194
- 00b66790 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
- 00b66790 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66858 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
+ 00b66858 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66790 bytes 807203f9
+ 00b66858 bytes 80d203f9
- 00b66764 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:6e0:8"]]
- 00b66764 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b6682c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7a0:8"]]
+ 00b6682c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66764 bytes 817243f9
+ 00b6682c bytes 81d243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-829ac8b88bdd0cc118a168806305dcee"></a>

### [`00b667fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b667fc.md) → [`00b668c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b668c4.md) _ZN8firebase4auth11twittercred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b668f0",
      "incomplete_value": true,
      "site": "00b668f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66828",
      "incomplete_value": true,
      "site": "00b66828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00b668d8",
      "incomplete_value": true,
      "site": "00b668d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66810",
      "incomplete_value": true,
      "site": "00b66810",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b668e4",
      "incomplete_value": false,
      "site": "00b668e8",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6681c",
      "incomplete_value": false,
      "site": "00b66820",
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
            "const:53b:8"
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
      "00b668d4",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b668e4",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00b668f0",
      "WRITE",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b668d4",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b668e4",
      "PARAM",
      [
        "storage",
        "002925c8",
        null,
        "string"
      ]
    ],
    [
      "00b668f0",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66820`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b667fc.md#insn-00b66820) · [`00b66828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b667fc.md#insn-00b66828) · [`00b6680c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b667fc.md#insn-00b6680c)
- 新版 `00b668e8`（命令位置の公開資料なし） · `00b668f0`（命令位置の公開資料なし） · `00b668d4`（命令位置の公開資料なし）

~~~diff
- 00b66820 ["INT_ADD", "register:40f0:8", ["const:b66820:8", "const:4:8"]]
- 00b66820 ["CALL", null, ["callee:00bde040:8"]]
+ 00b668e8 ["INT_ADD", "register:40f0:8", ["const:b668e8:8", "const:4:8"]]
+ 00b668e8 ["CALL", null, ["callee:00bde040:8"]]
- 00b66820 bytes dcdd0194
+ 00b668e8 bytes d6dd0194
- 00b66828 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b66828 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b668f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b668f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66828 bytes 608203f9
+ 00b668f0 bytes 60e203f9
- 00b6680c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b6680c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b668d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b668d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6680c bytes 688243f9
+ 00b668d4 bytes 68e243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-173b631950e0a99026ecb43660dc8651"></a>

### [`00b6683c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6683c.md) → [`00b66904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66904.md) _ZN8firebase4auth11twittercred19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b66930",
      "incomplete_value": true,
      "site": "00b66930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66868",
      "incomplete_value": true,
      "site": "00b66868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00b66918",
      "incomplete_value": true,
      "site": "00b66918",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66850",
      "incomplete_value": true,
      "site": "00b66850",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66920",
      "incomplete_value": false,
      "site": "00b66928",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66858",
      "incomplete_value": false,
      "site": "00b66860",
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
            "const:53b:8"
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
      "00b66914",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66920",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00b66930",
      "WRITE",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66914",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66920",
      "PARAM",
      [
        "storage",
        "002925c8",
        null,
        "string"
      ]
    ],
    [
      "00b66930",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66860`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6683c.md#insn-00b66860) · [`00b66868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6683c.md#insn-00b66868) · [`00b6684c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6683c.md#insn-00b6684c)
- 新版 `00b66928`（命令位置の公開資料なし） · `00b66930`（命令位置の公開資料なし） · `00b66914`（命令位置の公開資料なし）

~~~diff
- 00b66860 ["INT_ADD", "register:40f0:8", ["const:b66860:8", "const:4:8"]]
- 00b66860 ["CALL", null, ["callee:00bde040:8"]]
+ 00b66928 ["INT_ADD", "register:40f0:8", ["const:b66928:8", "const:4:8"]]
+ 00b66928 ["CALL", null, ["callee:00bde040:8"]]
- 00b66860 bytes ccdd0194
+ 00b66928 bytes c6dd0194
- 00b66868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b66868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66930 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b66930 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66868 bytes 608203f9
+ 00b66930 bytes 60e203f9
- 00b6684c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b6684c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66914 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b66914 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6684c bytes 688243f9
+ 00b66914 bytes 68e243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffc0306ba578e48d668e82e843a4ca53"></a>

### [`00b6687c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6687c.md) → [`00b66944`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66944.md) _ZN8firebase4auth11twittercred10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b66974",
      "incomplete_value": true,
      "site": "00b66974",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b668ac",
      "incomplete_value": true,
      "site": "00b668ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00b66958",
      "incomplete_value": true,
      "site": "00b66958",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66890",
      "incomplete_value": true,
      "site": "00b66890",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66964",
      "incomplete_value": false,
      "site": "00b6696c",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b6689c",
      "incomplete_value": false,
      "site": "00b668a4",
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
            "const:53b:8"
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
      "00b66954",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66964",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00b66974",
      "WRITE",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66954",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66964",
      "PARAM",
      [
        "storage",
        "002925c8",
        null,
        "string"
      ]
    ],
    [
      "00b66974",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b668a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6687c.md#insn-00b668a4) · [`00b668ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6687c.md#insn-00b668ac) · [`00b6688c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6687c.md#insn-00b6688c)
- 新版 `00b6696c`（命令位置の公開資料なし） · `00b66974`（命令位置の公開資料なし） · `00b66954`（命令位置の公開資料なし）

~~~diff
- 00b668a4 ["INT_ADD", "register:40f0:8", ["const:b668a4:8", "const:4:8"]]
- 00b668a4 ["CALL", null, ["callee:00bde040:8"]]
+ 00b6696c ["INT_ADD", "register:40f0:8", ["const:b6696c:8", "const:4:8"]]
+ 00b6696c ["CALL", null, ["callee:00bde040:8"]]
- 00b668a4 bytes bbdd0194
+ 00b6696c bytes b5dd0194
- 00b668ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b668ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66974 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b66974 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b668ac bytes 608203f9
+ 00b66974 bytes 60e203f9
- 00b6688c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b6688c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66954 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b66954 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b6688c bytes 688243f9
+ 00b66954 bytes 68e243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6981f8ec2c0af1baf1ee13906381d2af"></a>

### [`00b668c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b668c0.md) → [`00b66988`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66988.md) _ZN8firebase4auth11twittercred10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b669b8",
      "incomplete_value": true,
      "site": "00b669b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b668f0",
      "incomplete_value": true,
      "site": "00b668f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00b6699c",
      "incomplete_value": true,
      "site": "00b6699c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b668d4",
      "incomplete_value": true,
      "site": "00b668d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b669a4",
      "incomplete_value": false,
      "site": "00b669b0",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b668dc",
      "incomplete_value": false,
      "site": "00b668e8",
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
            "const:53b:8"
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
      "00b66998",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b669a4",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00b669b8",
      "WRITE",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66998",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b669a4",
      "PARAM",
      [
        "storage",
        "002925c8",
        null,
        "string"
      ]
    ],
    [
      "00b669b8",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b668e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b668c0.md#insn-00b668e8) · [`00b668f0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b668c0.md#insn-00b668f0) · [`00b668d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b668c0.md#insn-00b668d0)
- 新版 `00b669b0`（命令位置の公開資料なし） · `00b669b8`（命令位置の公開資料なし） · `00b66998`（命令位置の公開資料なし）

~~~diff
- 00b668e8 ["INT_ADD", "register:40f0:8", ["const:b668e8:8", "const:4:8"]]
- 00b668e8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b669b0 ["INT_ADD", "register:40f0:8", ["const:b669b0:8", "const:4:8"]]
+ 00b669b0 ["CALL", null, ["callee:00bde040:8"]]
- 00b668e8 bytes aadd0194
+ 00b669b0 bytes a4dd0194
- 00b668f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b668f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b669b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b669b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b668f0 bytes 608203f9
+ 00b669b8 bytes 60e203f9
- 00b668d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:700:8"]]
- 00b668d0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66998 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7c0:8"]]
+ 00b66998 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b668d0 bytes 688243f9
+ 00b66998 bytes 68e243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-18f1ad00efd816a085372f24c4322c78"></a>

### [`00b66910`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66910.md) → [`00b669d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b669d8.md) _ZN8firebase4auth11twittercred15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b66a30",
      "incomplete_value": true,
      "site": "00b66a30",
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
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66968",
      "incomplete_value": true,
      "site": "00b66968",
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
            "const:708:8"
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
      "definition_site": "00b66a0c",
      "incomplete_value": true,
      "site": "00b66a18",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7c0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66944",
      "incomplete_value": true,
      "site": "00b66950",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:700:8"
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
      "00b669ec",
      "READ",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66a0c",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66a30",
      "WRITE",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b669ec",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66a0c",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66a30",
      "WRITE",
      [
        "storage",
        "010a17c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66950`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66910.md#insn-00b66950) · [`00b66968`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66910.md#insn-00b66968) · [`00b66924`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66910.md#insn-00b66924)
- 新版 `00b66a18`（命令位置の公開資料なし） · `00b66a30`（命令位置の公開資料なし） · `00b669ec`（命令位置の公開資料なし）

~~~diff
- 00b66950 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66950 ["INT_ADD", "register:40f0:8", ["const:b66950:8", "const:4:8"]]
- 00b66950 ["CALLIND", null, ["register:0:8"]]
+ 00b66a18 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66a18 ["INT_ADD", "register:40f0:8", ["const:b66a18:8", "const:4:8"]]
+ 00b66a18 ["CALLIND", null, ["register:0:8"]]
- 00b66950 bytes 00013fd6
+ 00b66a18 bytes 00013fd6
- 00b66968 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b66968 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:708:8"]]
- 00b66968 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b66a30 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b66a30 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7c8:8"]]
+ 00b66a30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b66968 bytes a0221c39
+ 00b66a30 bytes a0221f39
- 00b66924 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:708:8"]]
- 00b66924 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b66924 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b669ec ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7c8:8"]]
+ 00b669ec ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b669ec ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b66924 bytes a8225c39
+ 00b669ec bytes a8225f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c067a6ba465f66f935544d8496fdd0ff"></a>

### [`00b6697c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6697c.md) → [`00b66a44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66a44.md) _ZN8firebase4auth11twittercred12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b66a80",
      "incomplete_value": true,
      "site": "00b66a80",
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
            "const:7c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b669b8",
      "incomplete_value": true,
      "site": "00b669b8",
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
            "const:708:8"
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
      "definition_site": "00b66aa0",
      "incomplete_value": true,
      "site": "00b66aa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b669d8",
      "incomplete_value": true,
      "site": "00b669d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00b66a5c",
      "incomplete_value": true,
      "site": "00b66a5c",
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
      "definition_site": "00b66994",
      "incomplete_value": true,
      "site": "00b66994",
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
      "00b66a58",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66a64",
      "READ",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66a80",
      "WRITE",
      [
        "storage",
        "010a1708",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b66a58",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66a64",
      "READ",
      [
        "storage",
        "010a17c8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66a80",
      "WRITE",
      [
        "storage",
        "010a17c8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b669b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6697c.md#insn-00b669b8) · [`00b669d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6697c.md#insn-00b669d4) · [`00b669d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b6697c.md#insn-00b669d8)
- 新版 `00b66a80`（命令位置の公開資料なし） · `00b66a9c`（命令位置の公開資料なし） · `00b66aa0`（命令位置の公開資料なし）

~~~diff
- 00b669b8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b669b8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b669b8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:708:8"]]
- 00b669b8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b66a80 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b66a80 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b66a80 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7c8:8"]]
+ 00b66a80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b669b8 bytes bf221c39
+ 00b66a80 bytes bf221f39
- 00b669d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b669d4 ["INT_ADD", "register:40f0:8", ["const:b669d4:8", "const:4:8"]]
- 00b669d4 ["CALLIND", null, ["register:0:8"]]
+ 00b66a9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66a9c ["INT_ADD", "register:40f0:8", ["const:b66a9c:8", "const:4:8"]]
+ 00b66a9c ["CALLIND", null, ["register:0:8"]]
- 00b669d4 bytes 00013fd6
+ 00b66a9c bytes 00013fd6
- 00b669d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
- 00b669d8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b669d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b66aa0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
+ 00b66aa0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b66aa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b669d8 bytes 9f8203f9
+ 00b66aa0 bytes 9fe203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-758f9b89710e2ced90dea317b6f7c3e5"></a>

### [`00b669ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b669ec.md) → [`00b66ab4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66ab4.md) _ZN8firebase4auth11twittercred14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

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
      "definition_site": "00b66af4",
      "incomplete_value": true,
      "site": "00b66af4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66a2c",
      "incomplete_value": true,
      "site": "00b66a2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00b66ad0",
      "incomplete_value": true,
      "site": "00b66ad0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66a08",
      "incomplete_value": true,
      "site": "00b66a08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66ad8",
      "incomplete_value": false,
      "site": "00b66aec",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66a10",
      "incomplete_value": false,
      "site": "00b66a24",
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
            "const:53b:8"
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
      "00b66ac8",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66ad8",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00b66af4",
      "WRITE",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66ac8",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66ad8",
      "PARAM",
      [
        "storage",
        "002925c8",
        null,
        "string"
      ]
    ],
    [
      "00b66af4",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66a24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b669ec.md#insn-00b66a24) · [`00b66a2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b669ec.md#insn-00b66a2c) · [`00b66a00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b669ec.md#insn-00b66a00)
- 新版 `00b66aec`（命令位置の公開資料なし） · `00b66af4`（命令位置の公開資料なし） · `00b66ac8`（命令位置の公開資料なし）

~~~diff
- 00b66a24 ["INT_ADD", "register:40f0:8", ["const:b66a24:8", "const:4:8"]]
- 00b66a24 ["CALL", null, ["callee:00bde040:8"]]
+ 00b66aec ["INT_ADD", "register:40f0:8", ["const:b66aec:8", "const:4:8"]]
+ 00b66aec ["CALL", null, ["callee:00bde040:8"]]
- 00b66a24 bytes 5bdd0194
+ 00b66aec bytes 55dd0194
- 00b66a2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
- 00b66a2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66af4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
+ 00b66af4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66a2c bytes 808203f9
+ 00b66af4 bytes 80e203f9
- 00b66a00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
- 00b66a00 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66ac8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
+ 00b66ac8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66a00 bytes 818243f9
+ 00b66ac8 bytes 81e243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-200f55720070bb58de90a6987e8106cd"></a>

### [`00b66a5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66a5c.md) → [`00b66b24`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66b24.md) _ZN8firebase4auth11twittercred11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b66b40",
      "incomplete_value": false,
      "site": "00b66b44",
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
    "old": {
      "definition_site": "00b66a78",
      "incomplete_value": false,
      "site": "00b66a7c",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b66b50",
      "incomplete_value": true,
      "site": "00b66b5c",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b66a88",
      "incomplete_value": true,
      "site": "00b66a94",
      "value": [
        "LOAD",
        "8",
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
      "00b66b40",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b66b50",
      "DATA",
      [
        "storage",
        "010a1710",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66b40",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b66b50",
      "DATA",
      [
        "storage",
        "010a17d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66a7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66a5c.md#insn-00b66a7c) · [`00b66a78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66a5c.md#insn-00b66a78) · [`00b66a84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66a5c.md#insn-00b66a84)
- 新版 `00b66b44`（命令位置の公開資料なし） · `00b66b40`（命令位置の公開資料なし） · `00b66b4c`（命令位置の公開資料なし）

~~~diff
- 00b66a7c ["INT_ADD", "register:40f0:8", ["const:b66a7c:8", "const:4:8"]]
- 00b66a7c ["CALL", null, ["callee:00bde130:8"]]
+ 00b66b44 ["INT_ADD", "register:40f0:8", ["const:b66b44:8", "const:4:8"]]
+ 00b66b44 ["CALL", null, ["callee:00bde130:8"]]
- 00b66a7c bytes 81dd0194
+ 00b66b44 bytes 7bdd0194
- 00b66a78 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b66a78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66a78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66a78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66b40 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b66b40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66b40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66b40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66a78 bytes 001c1591
+ 00b66b40 bytes 00501791
- 00b66a84 ["COPY", "tmp:0:8", ["const:710:8"]]
- 00b66a84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b66a84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b66a84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b66b4c ["COPY", "tmp:0:8", ["const:7d0:8"]]
+ 00b66b4c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66b4c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66b4c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b66a84 bytes 08411c91
+ 00b66b4c bytes 08411f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-24fa1f5c619ebb9316019208dfeba1a7"></a>

### [`00b66a98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66a98.md) → [`00b66b60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66b60.md) _ZN8firebase4auth11twittercred13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b66ba0",
      "incomplete_value": true,
      "site": "00b66ba0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7c0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ad8",
      "incomplete_value": true,
      "site": "00b66ad8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:700:8"
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
      "definition_site": "00b66b7c",
      "incomplete_value": true,
      "site": "00b66b7c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ab4",
      "incomplete_value": true,
      "site": "00b66ab4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66b84",
      "incomplete_value": false,
      "site": "00b66b98",
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
            "const:5c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66abc",
      "incomplete_value": false,
      "site": "00b66ad0",
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
            "const:53b:8"
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
      "00b66b74",
      "READ",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66b84",
      "PARAM",
      [
        "storage",
        "0029253b",
        null,
        "string"
      ]
    ],
    [
      "00b66ba0",
      "WRITE",
      [
        "storage",
        "010a1700",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66b74",
      "READ",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66b84",
      "PARAM",
      [
        "storage",
        "002925c8",
        null,
        "string"
      ]
    ],
    [
      "00b66ba0",
      "WRITE",
      [
        "storage",
        "010a17c0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66ad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66a98.md#insn-00b66ad0) · [`00b66ad8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66a98.md#insn-00b66ad8) · [`00b66aac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66a98.md#insn-00b66aac)
- 新版 `00b66b98`（命令位置の公開資料なし） · `00b66ba0`（命令位置の公開資料なし） · `00b66b74`（命令位置の公開資料なし）

~~~diff
- 00b66ad0 ["INT_ADD", "register:40f0:8", ["const:b66ad0:8", "const:4:8"]]
- 00b66ad0 ["CALL", null, ["callee:00bde040:8"]]
+ 00b66b98 ["INT_ADD", "register:40f0:8", ["const:b66b98:8", "const:4:8"]]
+ 00b66b98 ["CALL", null, ["callee:00bde040:8"]]
- 00b66ad0 bytes 30dd0194
+ 00b66b98 bytes 2add0194
- 00b66ad8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
- 00b66ad8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66ba0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
+ 00b66ba0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66ad8 bytes 808203f9
+ 00b66ba0 bytes 80e203f9
- 00b66aac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:700:8"]]
- 00b66aac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66b74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7c0:8"]]
+ 00b66b74 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66aac bytes 818243f9
+ 00b66b74 bytes 81e243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0af069834d584984c1681f002cb2fe94"></a>

### [`00b66b08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66b08.md) → [`00b66bd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66bd0.md) _ZN8firebase4auth11twittercred10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b66bec",
      "incomplete_value": false,
      "site": "00b66bf0",
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
    "old": {
      "definition_site": "00b66b24",
      "incomplete_value": false,
      "site": "00b66b28",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b66bfc",
      "incomplete_value": true,
      "site": "00b66c08",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b66b34",
      "incomplete_value": true,
      "site": "00b66b40",
      "value": [
        "LOAD",
        "8",
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
      "00b66bec",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00b66bfc",
      "DATA",
      [
        "storage",
        "010a1718",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b66bec",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00b66bfc",
      "DATA",
      [
        "storage",
        "010a17d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66b28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66b08.md#insn-00b66b28) · [`00b66b24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66b08.md#insn-00b66b24) · [`00b66b30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66b08.md#insn-00b66b30)
- 新版 `00b66bf0`（命令位置の公開資料なし） · `00b66bec`（命令位置の公開資料なし） · `00b66bf8`（命令位置の公開資料なし）

~~~diff
- 00b66b28 ["INT_ADD", "register:40f0:8", ["const:b66b28:8", "const:4:8"]]
- 00b66b28 ["CALL", null, ["callee:00bde130:8"]]
+ 00b66bf0 ["INT_ADD", "register:40f0:8", ["const:b66bf0:8", "const:4:8"]]
+ 00b66bf0 ["CALL", null, ["callee:00bde130:8"]]
- 00b66b28 bytes 56dd0194
+ 00b66bf0 bytes 50dd0194
- 00b66b24 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00b66b24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66b24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66b24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66bec ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00b66bec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66bec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66bec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66b24 bytes 00c81791
+ 00b66bec bytes 00fc1991
- 00b66b30 ["COPY", "tmp:0:8", ["const:718:8"]]
- 00b66b30 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b66b30 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b66b30 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b66bf8 ["COPY", "tmp:0:8", ["const:7d8:8"]]
+ 00b66bf8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66bf8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66bf8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b66b30 bytes 08611c91
+ 00b66bf8 bytes 08611f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73368cfecc850b3706cee0fd2cec53b8"></a>

### [`00b66b44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66b44.md) → [`00b66c0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c0c.md) _ZN8firebase4auth13oauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b66c38",
      "incomplete_value": true,
      "site": "00b66c38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66b70",
      "incomplete_value": true,
      "site": "00b66b70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "definition_site": "00b66c20",
      "incomplete_value": true,
      "site": "00b66c20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66b58",
      "incomplete_value": true,
      "site": "00b66b58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66c2c",
      "incomplete_value": false,
      "site": "00b66c30",
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
            "const:fd7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66b64",
      "incomplete_value": false,
      "site": "00b66b68",
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
            "const:6b:8"
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
      "00b66c1c",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66c2c",
      "PARAM",
      [
        "storage",
        "002a906b",
        null,
        "string"
      ]
    ],
    [
      "00b66c38",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66c1c",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66c2c",
      "PARAM",
      [
        "storage",
        "002a8fd7",
        null,
        "string"
      ]
    ],
    [
      "00b66c38",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66b68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66b44.md#insn-00b66b68) · [`00b66b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66b44.md#insn-00b66b70) · [`00b66b54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66b44.md#insn-00b66b54)
- 新版 `00b66c30`（命令位置の公開資料なし） · `00b66c38`（命令位置の公開資料なし） · `00b66c1c`（命令位置の公開資料なし）

~~~diff
- 00b66b68 ["INT_ADD", "register:40f0:8", ["const:b66b68:8", "const:4:8"]]
- 00b66b68 ["CALL", null, ["callee:00bde040:8"]]
+ 00b66c30 ["INT_ADD", "register:40f0:8", ["const:b66c30:8", "const:4:8"]]
+ 00b66c30 ["CALL", null, ["callee:00bde040:8"]]
- 00b66b68 bytes 0add0194
+ 00b66c30 bytes 04dd0194
- 00b66b70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b66b70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66c38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b66c38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66b70 bytes 609203f9
+ 00b66c38 bytes 60f203f9
- 00b66b54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b66b54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66c1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b66c1c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66b54 bytes 689243f9
+ 00b66c1c bytes 68f243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b35daf47bdecd2b9f101ea003cf29d7"></a>

### [`00b66b84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66b84.md) → [`00b66c4c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c4c.md) _ZN8firebase4auth13oauthprovider19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b66c78",
      "incomplete_value": true,
      "site": "00b66c78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66bb0",
      "incomplete_value": true,
      "site": "00b66bb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "definition_site": "00b66c60",
      "incomplete_value": true,
      "site": "00b66c60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66b98",
      "incomplete_value": true,
      "site": "00b66b98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66c68",
      "incomplete_value": false,
      "site": "00b66c70",
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
            "const:fd7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ba0",
      "incomplete_value": false,
      "site": "00b66ba8",
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
            "const:6b:8"
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
      "00b66c5c",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66c68",
      "PARAM",
      [
        "storage",
        "002a906b",
        null,
        "string"
      ]
    ],
    [
      "00b66c78",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66c5c",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66c68",
      "PARAM",
      [
        "storage",
        "002a8fd7",
        null,
        "string"
      ]
    ],
    [
      "00b66c78",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66ba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66b84.md#insn-00b66ba8) · [`00b66bb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66b84.md#insn-00b66bb0) · [`00b66b94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66b84.md#insn-00b66b94)
- 新版 `00b66c70`（命令位置の公開資料なし） · `00b66c78`（命令位置の公開資料なし） · `00b66c5c`（命令位置の公開資料なし）

~~~diff
- 00b66ba8 ["INT_ADD", "register:40f0:8", ["const:b66ba8:8", "const:4:8"]]
- 00b66ba8 ["CALL", null, ["callee:00bde040:8"]]
+ 00b66c70 ["INT_ADD", "register:40f0:8", ["const:b66c70:8", "const:4:8"]]
+ 00b66c70 ["CALL", null, ["callee:00bde040:8"]]
- 00b66ba8 bytes fadc0194
+ 00b66c70 bytes f4dc0194
- 00b66bb0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b66bb0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66c78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b66c78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66bb0 bytes 609203f9
+ 00b66c78 bytes 60f203f9
- 00b66b94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b66b94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66c5c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b66c5c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66b94 bytes 689243f9
+ 00b66c5c bytes 68f243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96118583e9b98faa9c6d423ae3846f50"></a>

### [`00b66bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66bc4.md) → [`00b66c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66c8c.md) _ZN8firebase4auth13oauthprovider10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b66cbc",
      "incomplete_value": true,
      "site": "00b66cbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66bf4",
      "incomplete_value": true,
      "site": "00b66bf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "definition_site": "00b66ca0",
      "incomplete_value": true,
      "site": "00b66ca0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66bd8",
      "incomplete_value": true,
      "site": "00b66bd8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66cac",
      "incomplete_value": false,
      "site": "00b66cb4",
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
            "const:fd7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66be4",
      "incomplete_value": false,
      "site": "00b66bec",
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
            "const:6b:8"
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
      "00b66c9c",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66cac",
      "PARAM",
      [
        "storage",
        "002a906b",
        null,
        "string"
      ]
    ],
    [
      "00b66cbc",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66c9c",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66cac",
      "PARAM",
      [
        "storage",
        "002a8fd7",
        null,
        "string"
      ]
    ],
    [
      "00b66cbc",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66bec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66bc4.md#insn-00b66bec) · [`00b66bf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66bc4.md#insn-00b66bf4) · [`00b66bd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66bc4.md#insn-00b66bd4)
- 新版 `00b66cb4`（命令位置の公開資料なし） · `00b66cbc`（命令位置の公開資料なし） · `00b66c9c`（命令位置の公開資料なし）

~~~diff
- 00b66bec ["INT_ADD", "register:40f0:8", ["const:b66bec:8", "const:4:8"]]
- 00b66bec ["CALL", null, ["callee:00bde040:8"]]
+ 00b66cb4 ["INT_ADD", "register:40f0:8", ["const:b66cb4:8", "const:4:8"]]
+ 00b66cb4 ["CALL", null, ["callee:00bde040:8"]]
- 00b66bec bytes e9dc0194
+ 00b66cb4 bytes e3dc0194
- 00b66bf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b66bf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66cbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b66cbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66bf4 bytes 609203f9
+ 00b66cbc bytes 60f203f9
- 00b66bd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b66bd4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66c9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b66c9c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66bd4 bytes 689243f9
+ 00b66c9c bytes 68f243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-224d90c102f1f8ddf59972079ecc7ccb"></a>

### [`00b66c08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66c08.md) → [`00b66cd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66cd0.md) _ZN8firebase4auth13oauthprovider10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

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
      "definition_site": "00b66d00",
      "incomplete_value": true,
      "site": "00b66d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66c38",
      "incomplete_value": true,
      "site": "00b66c38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "definition_site": "00b66ce4",
      "incomplete_value": true,
      "site": "00b66ce4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66c1c",
      "incomplete_value": true,
      "site": "00b66c1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b66cec",
      "incomplete_value": false,
      "site": "00b66cf8",
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
            "const:fd7:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66c24",
      "incomplete_value": false,
      "site": "00b66c30",
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
            "const:6b:8"
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
      "00b66ce0",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66cec",
      "PARAM",
      [
        "storage",
        "002a906b",
        null,
        "string"
      ]
    ],
    [
      "00b66d00",
      "WRITE",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66ce0",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66cec",
      "PARAM",
      [
        "storage",
        "002a8fd7",
        null,
        "string"
      ]
    ],
    [
      "00b66d00",
      "WRITE",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66c30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66c08.md#insn-00b66c30) · [`00b66c38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66c08.md#insn-00b66c38) · [`00b66c18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66c08.md#insn-00b66c18)
- 新版 `00b66cf8`（命令位置の公開資料なし） · `00b66d00`（命令位置の公開資料なし） · `00b66ce0`（命令位置の公開資料なし）

~~~diff
- 00b66c30 ["INT_ADD", "register:40f0:8", ["const:b66c30:8", "const:4:8"]]
- 00b66c30 ["CALL", null, ["callee:00bde040:8"]]
+ 00b66cf8 ["INT_ADD", "register:40f0:8", ["const:b66cf8:8", "const:4:8"]]
+ 00b66cf8 ["CALL", null, ["callee:00bde040:8"]]
- 00b66c30 bytes d8dc0194
+ 00b66cf8 bytes d2dc0194
- 00b66c38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b66c38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b66d00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b66d00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66c38 bytes 609203f9
+ 00b66d00 bytes 60f203f9
- 00b66c18 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:720:8"]]
- 00b66c18 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b66ce0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e0:8"]]
+ 00b66ce0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b66c18 bytes 689243f9
+ 00b66ce0 bytes 68f243f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b2f6522ec10008ce30a85271646af5f"></a>

### [`00b66c58`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66c58.md) → [`00b66d20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66d20.md) _ZN8firebase4auth13oauthprovider15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b66d78",
      "incomplete_value": true,
      "site": "00b66d78",
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
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66cb0",
      "incomplete_value": true,
      "site": "00b66cb0",
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
            "const:728:8"
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
      "definition_site": "00b66d54",
      "incomplete_value": true,
      "site": "00b66d60",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66c8c",
      "incomplete_value": true,
      "site": "00b66c98",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:720:8"
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
      "00b66d34",
      "READ",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66d54",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66d78",
      "WRITE",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b66d34",
      "READ",
      [
        "storage",
        "010a17e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66d54",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66d78",
      "WRITE",
      [
        "storage",
        "010a17e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66c98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66c58.md#insn-00b66c98) · [`00b66cb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66c58.md#insn-00b66cb0) · [`00b66c6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66c58.md#insn-00b66c6c)
- 新版 `00b66d60`（命令位置の公開資料なし） · `00b66d78`（命令位置の公開資料なし） · `00b66d34`（命令位置の公開資料なし）

~~~diff
- 00b66c98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66c98 ["INT_ADD", "register:40f0:8", ["const:b66c98:8", "const:4:8"]]
- 00b66c98 ["CALLIND", null, ["register:0:8"]]
+ 00b66d60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66d60 ["INT_ADD", "register:40f0:8", ["const:b66d60:8", "const:4:8"]]
+ 00b66d60 ["CALLIND", null, ["register:0:8"]]
- 00b66c98 bytes 00013fd6
+ 00b66d60 bytes 00013fd6
- 00b66cb0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b66cb0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:728:8"]]
- 00b66cb0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b66d78 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b66d78 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7e8:8"]]
+ 00b66d78 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b66cb0 bytes a0a21c39
+ 00b66d78 bytes a0a21f39
- 00b66c6c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:728:8"]]
- 00b66c6c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00b66c6c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00b66d34 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:7e8:8"]]
+ 00b66d34 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00b66d34 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00b66c6c bytes a8a25c39
+ 00b66d34 bytes a8a25f39
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26ea848589ebef0a9a69cd02f70b616d"></a>

### [`00b66cc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66cc4.md) → [`00b66d8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66d8c.md) _ZN8firebase4auth13oauthprovider12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddfe0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde090`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde090.md)

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
      "definition_site": "00b66dc8",
      "incomplete_value": true,
      "site": "00b66dc8",
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
            "const:7e8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66d00",
      "incomplete_value": true,
      "site": "00b66d00",
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
            "const:728:8"
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
      "definition_site": "00b66de8",
      "incomplete_value": true,
      "site": "00b66de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7e0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66d20",
      "incomplete_value": true,
      "site": "00b66d20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:720:8"
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
      "definition_site": "00b66da4",
      "incomplete_value": true,
      "site": "00b66da4",
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
      "definition_site": "00b66cdc",
      "incomplete_value": true,
      "site": "00b66cdc",
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
      "00b66da0",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66dac",
      "READ",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66dc8",
      "WRITE",
      [
        "storage",
        "010a1728",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b66da0",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66dac",
      "READ",
      [
        "storage",
        "010a17e8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b66dc8",
      "WRITE",
      [
        "storage",
        "010a17e8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66d00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66cc4.md#insn-00b66d00) · [`00b66d1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66cc4.md#insn-00b66d1c) · [`00b66d20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66cc4.md#insn-00b66d20)
- 新版 `00b66dc8`（命令位置の公開資料なし） · `00b66de4`（命令位置の公開資料なし） · `00b66de8`（命令位置の公開資料なし）

~~~diff
- 00b66d00 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b66d00 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b66d00 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:728:8"]]
- 00b66d00 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b66dc8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b66dc8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b66dc8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7e8:8"]]
+ 00b66dc8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b66d00 bytes bfa21c39
+ 00b66dc8 bytes bfa21f39
- 00b66d1c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b66d1c ["INT_ADD", "register:40f0:8", ["const:b66d1c:8", "const:4:8"]]
- 00b66d1c ["CALLIND", null, ["register:0:8"]]
+ 00b66de4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b66de4 ["INT_ADD", "register:40f0:8", ["const:b66de4:8", "const:4:8"]]
+ 00b66de4 ["CALLIND", null, ["register:0:8"]]
- 00b66d1c bytes 00013fd6
+ 00b66de4 bytes 00013fd6
- 00b66d20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
- 00b66d20 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b66d20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b66de8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e0:8"]]
+ 00b66de8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b66de8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b66d20 bytes 9f9203f9
+ 00b66de8 bytes 9ff203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5c61c9d1f64db0bdc234259993f6249c"></a>

### [`00b66d34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66d34.md) → [`00b66dfc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66dfc.md) _ZN8firebase4auth13oauthprovider14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66d74"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b66e3c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66d50"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b66d48",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b66d50",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b66e40"
      ]
    ],
    [
      "unmatched:00b66d58",
      "PARAM",
      [
        "storage",
        "002a906b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b66e10",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66e18",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b66e40"
      ]
    ],
    [
      "00b66e20",
      "PARAM",
      [
        "storage",
        "002a8fd7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66d50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66d34.md#insn-00b66d50) · [`00b66d6c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66d34.md#insn-00b66d6c) · [`00b66d74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66d34.md#insn-00b66d74)
- 新版 `00b66e34`（命令位置の公開資料なし）

~~~diff
- 00b66d50 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b66d50 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66d50 bytes 410100b5
- 00b66d6c ["INT_ADD", "register:40f0:8", ["const:b66d6c:8", "const:4:8"]]
- 00b66d6c ["CALL", null, ["callee:00bde040:8"]]
+ 00b66e34 ["INT_ADD", "register:40f0:8", ["const:b66e34:8", "const:4:8"]]
+ 00b66e34 ["CALL", null, ["callee:00bde040:8"]]
- 00b66d6c bytes 89dc0194
+ 00b66e34 bytes 83dc0194
- 00b66d74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
- 00b66d74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66d74 bytes 809203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e08ac47d1f103e986665995aff5d8af"></a>

### [`00b66da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66da4.md) → [`00b66e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66e6c.md) _ZN8firebase4auth13oauthprovider11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00b66e88",
      "incomplete_value": false,
      "site": "00b66e8c",
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
    "old": {
      "definition_site": "00b66dc0",
      "incomplete_value": false,
      "site": "00b66dc4",
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
    "ordinal": 0,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b66e98",
      "incomplete_value": true,
      "site": "00b66ea4",
      "value": [
        "LOAD",
        "8",
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
      "definition_site": "00b66dd0",
      "incomplete_value": true,
      "site": "00b66ddc",
      "value": [
        "LOAD",
        "8",
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
      "00b66e88",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00b66e98",
      "DATA",
      [
        "storage",
        "010a1730",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66e88",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00b66e98",
      "DATA",
      [
        "storage",
        "010a17f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66dc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66da4.md#insn-00b66dc4) · [`00b66dc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66da4.md#insn-00b66dc0) · [`00b66dcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66da4.md#insn-00b66dcc)
- 新版 `00b66e8c`（命令位置の公開資料なし） · `00b66e88`（命令位置の公開資料なし） · `00b66e94`（命令位置の公開資料なし）

~~~diff
- 00b66dc4 ["INT_ADD", "register:40f0:8", ["const:b66dc4:8", "const:4:8"]]
- 00b66dc4 ["CALL", null, ["callee:00bde130:8"]]
+ 00b66e8c ["INT_ADD", "register:40f0:8", ["const:b66e8c:8", "const:4:8"]]
+ 00b66e8c ["CALL", null, ["callee:00bde130:8"]]
- 00b66dc4 bytes afdc0194
+ 00b66e8c bytes a9dc0194
- 00b66dc0 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00b66dc0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b66dc0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b66dc0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b66e88 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00b66e88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66e88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b66e88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b66dc0 bytes 001c1591
+ 00b66e88 bytes 00501791
- 00b66dcc ["COPY", "tmp:0:8", ["const:730:8"]]
- 00b66dcc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00b66dcc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00b66dcc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00b66e94 ["COPY", "tmp:0:8", ["const:7f0:8"]]
+ 00b66e94 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66e94 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00b66e94 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00b66dcc bytes 08c11c91
+ 00b66e94 bytes 08c11f91
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b6bc0b13bde8a5aad0978c9af2be95dd"></a>

### [`00b66de0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66de0.md) → [`00b66ea8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66ea8.md) _ZN8firebase4auth13oauthprovider13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 71.43% / 新版 71.43%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件, `unresolved_branch_alignment` 1件, `unresolved_store_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66e20"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b66ee8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66dfc"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b66df4",
      "READ",
      [
        "storage",
        "010a1720",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00b66dfc",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b66eec"
      ]
    ],
    [
      "unmatched:00b66e04",
      "PARAM",
      [
        "storage",
        "002a906b",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b66ebc",
      "READ",
      [
        "storage",
        "010a17e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66ec4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b66eec"
      ]
    ],
    [
      "00b66ecc",
      "PARAM",
      [
        "storage",
        "002a8fd7",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66dfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66de0.md#insn-00b66dfc) · [`00b66e18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66de0.md#insn-00b66e18) · [`00b66e20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66de0.md#insn-00b66e20)
- 新版 `00b66ee0`（命令位置の公開資料なし）

~~~diff
- 00b66dfc ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00b66dfc ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66dfc bytes 410100b5
- 00b66e18 ["INT_ADD", "register:40f0:8", ["const:b66e18:8", "const:4:8"]]
- 00b66e18 ["CALL", null, ["callee:00bde040:8"]]
+ 00b66ee0 ["INT_ADD", "register:40f0:8", ["const:b66ee0:8", "const:4:8"]]
+ 00b66ee0 ["CALL", null, ["callee:00bde040:8"]]
- 00b66e18 bytes 5edc0194
+ 00b66ee0 bytes 58dc0194
- 00b66e20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:720:8"]]
- 00b66e20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66e20 bytes 809203f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-418306e4ea4ee098b64cf5ba6e991c38"></a>

### [`00b66e8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66e8c.md) → [`00b66f54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f54.md) _ZN8firebase4auth8timeunit19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS_4

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 50.00% / 新版 50.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66eb8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b66f80"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66f68",
      "incomplete_value": true,
      "site": "00b66f68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66ea0",
      "incomplete_value": true,
      "site": "00b66ea0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b66f64",
      "READ",
      [
        "storage",
        "010a1750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66f68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b66ebc"
      ]
    ],
    [
      "unmatched:00b66eac",
      "PARAM",
      [
        "storage",
        "002a3027",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b66f64",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66f68",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b66f84"
      ]
    ],
    [
      "00b66f74",
      "PARAM",
      [
        "storage",
        "002a3020",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66eb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66e8c.md#insn-00b66eb0) · [`00b66eb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66e8c.md#insn-00b66eb8) · [`00b66ec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66e8c.md#insn-00b66ec8)

~~~diff
- 00b66eb0 ["INT_ADD", "register:40f0:8", ["const:b66eb0:8", "const:4:8"]]
- 00b66eb0 ["CALL", null, ["callee:00bde040:8"]]
- 00b66eb0 bytes 38dc0194
- 00b66eb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00b66eb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66eb8 bytes 60aa03f9
- 00b66ec8 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b66ec8 ["RETURN", null, ["register:0:8"]]
- 00b66ec8 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3ee93ad0e3bbe49cda86cc8ee0b2705b"></a>

### [`00b66ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66ecc.md) → [`00b66f94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66f94.md) _ZN8firebase4auth8timeunit19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 25.00% / 新版 25.00%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 4件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66ecc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66ed0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66ed0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00b66ecc",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00b66ed0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b66fa4",
      "READ",
      [
        "storage",
        "010a1750",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b66f94",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00b66f98",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00b66fa4",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66ecc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66ecc.md#insn-00b66ecc) · [`00b66ed0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66ecc.md#insn-00b66ed0) · [`00b66ee0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66ecc.md#insn-00b66ee0)
- 新版 `00b66fa8`（命令位置の公開資料なし）

~~~diff
- 00b66ecc ["COPY", "tmp:0:8", ["register:4098:8"]]
- 00b66ecc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00b66ecc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00b66ecc bytes f30f1ef8
- 00b66ed0 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00b66ed0 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00b66ed0 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00b66ed0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00b66ed0 bytes fd7b01a9
- 00b66ee0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00b66ee0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00b66fa8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00b66fa8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00b66ee0 bytes e80000b5
+ 00b66fa8 bytes e80000b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-577a90029ec8c57f79e11f39602d855a"></a>

### [`00b66f0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66f0c.md) → [`00b66fd4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b66/00b66fd4.md) _ZN8firebase4auth8timeunit10CacheClassEP7_JNIEnvP8_jobjectNS_4util16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment, unresolved_store_alignment

命令の説明率　旧版 47.06% / 新版 47.06%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_return_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00b66f3c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00b67004"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b66fe8",
      "incomplete_value": true,
      "site": "00b66fe8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b66f20",
      "incomplete_value": true,
      "site": "00b66f20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00b66fe4",
      "READ",
      [
        "storage",
        "010a1750",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66fe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00b66f40"
      ]
    ],
    [
      "unmatched:00b66f2c",
      "PARAM",
      [
        "storage",
        "002a3027",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00b66fe4",
      "READ",
      [
        "storage",
        "010a1810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b66fe8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00b67008"
      ]
    ],
    [
      "00b66ff4",
      "PARAM",
      [
        "storage",
        "002a3020",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b66f34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66f0c.md#insn-00b66f34) · [`00b66f3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66f0c.md#insn-00b66f3c) · [`00b66f4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b66/00b66f0c.md#insn-00b66f4c)

~~~diff
- 00b66f34 ["INT_ADD", "register:40f0:8", ["const:b66f34:8", "const:4:8"]]
- 00b66f34 ["CALL", null, ["callee:00bde040:8"]]
- 00b66f34 bytes 17dc0194
- 00b66f3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:750:8"]]
- 00b66f3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b66f3c bytes 60aa03f9
- 00b66f4c ["COPY", "register:0:8", ["register:40f0:8"]]
- 00b66f4c ["RETURN", null, ["register:0:8"]]
- 00b66f4c bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

