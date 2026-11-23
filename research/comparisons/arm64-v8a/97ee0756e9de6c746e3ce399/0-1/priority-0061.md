# v15.7.2 → v15.7.3 · 最優先の変更候補 (61)

[一覧の目次](README.md)

<a id="compare-c993134b5f5b06a7cdd4cc0e43fbba51"></a>

### [`00aec168`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec168.md) → [`00aec230`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec230.md) _ZN8firebase4util4list10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00aec184",
      "incomplete_value": false,
      "site": "00aec188",
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
    "old": {
      "definition_site": "00aec194",
      "incomplete_value": true,
      "site": "00aec1a0",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aec24c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aec25c",
      "DATA",
      [
        "storage",
        "010a0848",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aec24c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aec25c",
      "DATA",
      [
        "storage",
        "010a0908",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec188`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec168.md#insn-00aec188) · [`00aec184`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec168.md#insn-00aec184) · [`00aec190`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec168.md#insn-00aec190)
- 新版 [`00aec250`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec230.md#insn-00aec250) · [`00aec24c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec230.md#insn-00aec24c) · [`00aec258`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec230.md#insn-00aec258)

~~~diff
- 00aec188 ["INT_ADD", "register:40f0:8", ["const:aec188:8", "const:4:8"]]
- 00aec188 ["CALL", null, ["callee:00bde130:8"]]
+ 00aec250 ["INT_ADD", "register:40f0:8", ["const:aec250:8", "const:4:8"]]
+ 00aec250 ["CALL", null, ["callee:00bde130:8"]]
- 00aec188 bytes bec70394
+ 00aec250 bytes b8c70394
- 00aec184 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aec184 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec184 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec184 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aec24c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00aec24c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec24c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec24c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec184 bytes 00c81791
+ 00aec24c bytes 00fc1991
- 00aec190 ["COPY", "tmp:0:8", ["const:848:8"]]
- 00aec190 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aec190 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aec190 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aec258 ["COPY", "tmp:0:8", ["const:908:8"]]
+ 00aec258 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec258 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec258 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aec190 bytes 08212191
+ 00aec258 bytes 08212491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6936861429b09f90e226caff5b534e41"></a>

### [`00aec1a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec1a4.md) → [`00aec26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec26c.md) _ZN8firebase4util10long_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
    "old": {
      "definition_site": "00aec1d0",
      "incomplete_value": true,
      "site": "00aec1d0",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aec1b8",
      "incomplete_value": true,
      "site": "00aec1b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aec1c4",
      "incomplete_value": false,
      "site": "00aec1c8",
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
            "const:dea:8"
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
      "00aec27c",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec28c",
      "PARAM",
      [
        "storage",
        "002a7dea",
        null,
        "string"
      ]
    ],
    [
      "00aec298",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec27c",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec28c",
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      "00aec298",
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec1c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec1a4.md#insn-00aec1c8) · [`00aec1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec1a4.md#insn-00aec1d0) · [`00aec1b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec1a4.md#insn-00aec1b4)
- 新版 [`00aec290`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec26c.md#insn-00aec290) · [`00aec298`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec26c.md#insn-00aec298) · [`00aec27c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec26c.md#insn-00aec27c)

~~~diff
- 00aec1c8 ["INT_ADD", "register:40f0:8", ["const:aec1c8:8", "const:4:8"]]
- 00aec1c8 ["CALL", null, ["callee:00bde040:8"]]
+ 00aec290 ["INT_ADD", "register:40f0:8", ["const:aec290:8", "const:4:8"]]
+ 00aec290 ["CALL", null, ["callee:00bde040:8"]]
- 00aec1c8 bytes 72c70394
+ 00aec290 bytes 6cc70394
- 00aec1d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00aec1d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec298 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
+ 00aec298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec1d0 bytes 602a04f9
+ 00aec298 bytes 608a04f9
- 00aec1b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00aec1b4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec27c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
+ 00aec27c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec1b4 bytes 682a44f9
+ 00aec27c bytes 688a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a8bed3c4165d40d6aafd0e7272f47a4"></a>

### [`00aec1e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec1e4.md) → [`00aec2ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ac.md) _ZN8firebase4util10long_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aec210",
      "incomplete_value": true,
      "site": "00aec210",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aec1f8",
      "incomplete_value": true,
      "site": "00aec1f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aec200",
      "incomplete_value": false,
      "site": "00aec208",
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
            "const:dea:8"
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
      "00aec2bc",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec2c8",
      "PARAM",
      [
        "storage",
        "002a7dea",
        null,
        "string"
      ]
    ],
    [
      "00aec2d8",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec2bc",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec2c8",
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      "00aec2d8",
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec208`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec1e4.md#insn-00aec208) · [`00aec210`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec1e4.md#insn-00aec210) · [`00aec1f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec1e4.md#insn-00aec1f4)
- 新版 [`00aec2d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ac.md#insn-00aec2d0) · [`00aec2d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ac.md#insn-00aec2d8) · [`00aec2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ac.md#insn-00aec2bc)

~~~diff
- 00aec208 ["INT_ADD", "register:40f0:8", ["const:aec208:8", "const:4:8"]]
- 00aec208 ["CALL", null, ["callee:00bde040:8"]]
+ 00aec2d0 ["INT_ADD", "register:40f0:8", ["const:aec2d0:8", "const:4:8"]]
+ 00aec2d0 ["CALL", null, ["callee:00bde040:8"]]
- 00aec208 bytes 62c70394
+ 00aec2d0 bytes 5cc70394
- 00aec210 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00aec210 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec2d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
+ 00aec2d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec210 bytes 602a04f9
+ 00aec2d8 bytes 608a04f9
- 00aec1f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00aec1f4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec2bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
+ 00aec2bc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec1f4 bytes 682a44f9
+ 00aec2bc bytes 688a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-75dec754d4df6e4d494357d79816238e"></a>

### [`00aec224`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec224.md) → [`00aec2ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ec.md) _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
    "old": {
      "definition_site": "00aec254",
      "incomplete_value": true,
      "site": "00aec254",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aec238",
      "incomplete_value": true,
      "site": "00aec238",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
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
            "const:d56:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aec244",
      "incomplete_value": false,
      "site": "00aec24c",
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
            "const:dea:8"
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
      "00aec2fc",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec30c",
      "PARAM",
      [
        "storage",
        "002a7dea",
        null,
        "string"
      ]
    ],
    [
      "00aec31c",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec2fc",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec24c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec224.md#insn-00aec24c) · [`00aec254`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec224.md#insn-00aec254) · [`00aec234`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec224.md#insn-00aec234)
- 新版 [`00aec314`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ec.md#insn-00aec314) · [`00aec31c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ec.md#insn-00aec31c) · [`00aec2fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec2ec.md#insn-00aec2fc)

~~~diff
- 00aec24c ["INT_ADD", "register:40f0:8", ["const:aec24c:8", "const:4:8"]]
- 00aec24c ["CALL", null, ["callee:00bde040:8"]]
+ 00aec314 ["INT_ADD", "register:40f0:8", ["const:aec314:8", "const:4:8"]]
+ 00aec314 ["CALL", null, ["callee:00bde040:8"]]
- 00aec24c bytes 51c70394
+ 00aec314 bytes 4bc70394
- 00aec254 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00aec254 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec31c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
+ 00aec31c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec254 bytes 602a04f9
+ 00aec31c bytes 608a04f9
- 00aec234 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00aec234 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec2fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
+ 00aec2fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec234 bytes 682a44f9
+ 00aec2fc bytes 688a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9975ce03ac567a44da6fd5a71dec60d6"></a>

### [`00aec268`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec268.md) → [`00aec330`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec330.md) _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobject

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
            "const:850:8"
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
      "definition_site": "00aec27c",
      "incomplete_value": true,
      "site": "00aec27c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aec284",
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
            "const:dea:8"
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
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec34c",
      "PARAM",
      [
        "storage",
        "002a7dea",
        null,
        "string"
      ]
    ],
    [
      "00aec360",
      "WRITE",
      [
        "storage",
        "010a0850",
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
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec34c",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec290`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec268.md#insn-00aec290) · [`00aec298`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec268.md#insn-00aec298) · [`00aec278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec268.md#insn-00aec278)
- 新版 [`00aec358`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec330.md#insn-00aec358) · [`00aec360`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec330.md#insn-00aec360) · [`00aec340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec330.md#insn-00aec340)

~~~diff
- 00aec290 ["INT_ADD", "register:40f0:8", ["const:aec290:8", "const:4:8"]]
- 00aec290 ["CALL", null, ["callee:00bde040:8"]]
+ 00aec358 ["INT_ADD", "register:40f0:8", ["const:aec358:8", "const:4:8"]]
+ 00aec358 ["CALL", null, ["callee:00bde040:8"]]
- 00aec290 bytes 40c70394
+ 00aec358 bytes 3ac70394
- 00aec298 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00aec298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec360 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
+ 00aec360 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec298 bytes 602a04f9
+ 00aec360 bytes 608a04f9
- 00aec278 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00aec278 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec340 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
+ 00aec340 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec278 bytes 682a44f9
+ 00aec340 bytes 688a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6affa00415c5d729d5d583fcd988f0e3"></a>

### [`00aec2b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec2b8.md) → [`00aec380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec380.md) _ZN8firebase4util10long_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
    "old": {
      "definition_site": "00aec340",
      "incomplete_value": true,
      "site": "00aec340",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aec2ec",
      "incomplete_value": true,
      "site": "00aec2f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:850:8"
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
      "00aec394",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec3b4",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec408",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aec394",
      "READ",
      [
        "storage",
        "010a0918",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec3b4",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec408",
      "WRITE",
      [
        "storage",
        "010a0918",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec2f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec2b8.md#insn-00aec2f8) · [`00aec340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec2b8.md#insn-00aec340) · [`00aec2cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec2b8.md#insn-00aec2cc)
- 新版 [`00aec3c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec380.md#insn-00aec3c0) · [`00aec408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec380.md#insn-00aec408) · [`00aec394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec380.md#insn-00aec394)

~~~diff
- 00aec2f8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec2f8 ["INT_ADD", "register:40f0:8", ["const:aec2f8:8", "const:4:8"]]
- 00aec2f8 ["CALLIND", null, ["register:0:8"]]
+ 00aec3c0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aec3c0 ["INT_ADD", "register:40f0:8", ["const:aec3c0:8", "const:4:8"]]
+ 00aec3c0 ["CALLIND", null, ["register:0:8"]]
- 00aec2f8 bytes 00013fd6
+ 00aec3c0 bytes 00013fd6
- 00aec340 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aec340 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:858:8"]]
- 00aec340 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aec408 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aec408 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:918:8"]]
+ 00aec408 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aec340 bytes a0622139
+ 00aec408 bytes a0622439
- 00aec2cc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:858:8"]]
- 00aec2cc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aec2cc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aec394 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:918:8"]]
+ 00aec394 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aec394 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aec2cc bytes a8626139
+ 00aec394 bytes a8626439
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f4338f5a804b9ac9199d84b8171896fc"></a>

### [`00aec354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec354.md) → [`00aec41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec41c.md) _ZN8firebase4util10long_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies, store_destination

命令の説明率　旧版 92.50% / 新版 92.50%

CFGの説明率　旧版 77.78% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00aec390",
      "incomplete_value": true,
      "site": "00aec390",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00aec3e0",
      "incomplete_value": true,
      "site": "00aec3e0",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aec36c",
      "incomplete_value": true,
      "site": "00aec36c",
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
      "00aec430",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec43c",
      "READ",
      [
        "storage",
        "010a0858",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec458",
      "WRITE",
      [
        "storage",
        "010a0858",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aec430",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec43c",
      "READ",
      [
        "storage",
        "010a0918",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec458",
      "WRITE",
      [
        "storage",
        "010a0918",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec36c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec354.md#insn-00aec36c) · [`00aec390`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec354.md#insn-00aec390) · [`00aec3dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec354.md#insn-00aec3dc)
- 新版 [`00aec434`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec41c.md#insn-00aec434) · [`00aec458`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec41c.md#insn-00aec458) · [`00aec4a4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec41c.md#insn-00aec4a4)

~~~diff
- 00aec36c ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aec36c ["CBRANCH", null, ["local:b6:8", "tmp:0:1"]]
+ 00aec434 ["INT_EQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
+ 00aec434 ["CBRANCH", null, ["local:b7:8", "tmp:0:1"]]
- 00aec36c bytes c10300b4
+ 00aec434 bytes c10300b4
- 00aec390 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aec390 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aec390 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:858:8"]]
- 00aec390 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aec458 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aec458 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aec458 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:918:8"]]
+ 00aec458 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aec390 bytes bf622139
+ 00aec458 bytes bf622439
- 00aec3dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec3dc ["INT_ADD", "register:40f0:8", ["const:aec3dc:8", "const:4:8"]]
- 00aec3dc ["CALLIND", null, ["register:0:8"]]
+ 00aec4a4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aec4a4 ["INT_ADD", "register:40f0:8", ["const:aec4a4:8", "const:4:8"]]
+ 00aec4a4 ["CALLIND", null, ["register:0:8"]]
- 00aec3dc bytes 00013fd6
+ 00aec4a4 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f3a63e1e076620154114106c2474659e"></a>

### [`00aec3f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec3f4.md) → [`00aec4bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec4bc.md) _ZN8firebase4util10long_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aec434",
      "incomplete_value": true,
      "site": "00aec434",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aec410",
      "incomplete_value": true,
      "site": "00aec410",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aec418",
      "incomplete_value": false,
      "site": "00aec42c",
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
            "const:dea:8"
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
      "00aec4d0",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec4e0",
      "PARAM",
      [
        "storage",
        "002a7dea",
        null,
        "string"
      ]
    ],
    [
      "00aec4fc",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec4d0",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec4e0",
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      "00aec4fc",
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec42c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec3f4.md#insn-00aec42c) · [`00aec434`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec3f4.md#insn-00aec434) · [`00aec408`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec3f4.md#insn-00aec408)
- 新版 [`00aec4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec4bc.md#insn-00aec4f4) · [`00aec4fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec4bc.md#insn-00aec4fc) · [`00aec4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec4bc.md#insn-00aec4d0)

~~~diff
- 00aec42c ["INT_ADD", "register:40f0:8", ["const:aec42c:8", "const:4:8"]]
- 00aec42c ["CALL", null, ["callee:00bde040:8"]]
+ 00aec4f4 ["INT_ADD", "register:40f0:8", ["const:aec4f4:8", "const:4:8"]]
+ 00aec4f4 ["CALL", null, ["callee:00bde040:8"]]
- 00aec42c bytes d9c60394
+ 00aec4f4 bytes d3c60394
- 00aec434 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
- 00aec434 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec4fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
+ 00aec4fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec434 bytes 802a04f9
+ 00aec4fc bytes 808a04f9
- 00aec408 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
- 00aec408 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec4d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
+ 00aec4d0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec408 bytes 812a44f9
+ 00aec4d0 bytes 818a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4f44404a5041da5d98eae695706282a9"></a>

### [`00aec4a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec4a0.md) → [`00aec568`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec568.md) _ZN8firebase4util10long_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
    "old": {
      "definition_site": "00aec4e0",
      "incomplete_value": true,
      "site": "00aec4e0",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aec4bc",
      "incomplete_value": true,
      "site": "00aec4bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aec4c4",
      "incomplete_value": false,
      "site": "00aec4d8",
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
            "const:dea:8"
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
      "00aec57c",
      "READ",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec58c",
      "PARAM",
      [
        "storage",
        "002a7dea",
        null,
        "string"
      ]
    ],
    [
      "00aec5a8",
      "WRITE",
      [
        "storage",
        "010a0850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec57c",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec58c",
      "PARAM",
      [
        "storage",
        "002a7d56",
        null,
        "string"
      ]
    ],
    [
      "00aec5a8",
      "WRITE",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec4d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec4a0.md#insn-00aec4d8) · [`00aec4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec4a0.md#insn-00aec4e0) · [`00aec4b4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec4a0.md#insn-00aec4b4)
- 新版 [`00aec5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec568.md#insn-00aec5a0) · [`00aec5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec568.md#insn-00aec5a8) · [`00aec57c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec568.md#insn-00aec57c)

~~~diff
- 00aec4d8 ["INT_ADD", "register:40f0:8", ["const:aec4d8:8", "const:4:8"]]
- 00aec4d8 ["CALL", null, ["callee:00bde040:8"]]
+ 00aec5a0 ["INT_ADD", "register:40f0:8", ["const:aec5a0:8", "const:4:8"]]
+ 00aec5a0 ["CALL", null, ["callee:00bde040:8"]]
- 00aec4d8 bytes aec60394
+ 00aec5a0 bytes a8c60394
- 00aec4e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
- 00aec4e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec5a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
+ 00aec5a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec4e0 bytes 802a04f9
+ 00aec5a8 bytes 808a04f9
- 00aec4b4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
- 00aec4b4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec57c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
+ 00aec57c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec4b4 bytes 812a44f9
+ 00aec57c bytes 818a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4ea8b79faa99bf97e51364e4dc3e8dc"></a>

### [`00aec510`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec510.md) → [`00aec5d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec5d8.md) _ZN8firebase4util10long_class10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00aec52c",
      "incomplete_value": false,
      "site": "00aec530",
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
    "old": {
      "definition_site": "00aec53c",
      "incomplete_value": true,
      "site": "00aec548",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aec5f4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aec604",
      "DATA",
      [
        "storage",
        "010a0870",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aec5f4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aec604",
      "DATA",
      [
        "storage",
        "010a0930",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec530`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec510.md#insn-00aec530) · [`00aec52c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec510.md#insn-00aec52c) · [`00aec538`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec510.md#insn-00aec538)
- 新版 [`00aec5f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec5d8.md#insn-00aec5f8) · [`00aec5f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec5d8.md#insn-00aec5f4) · [`00aec600`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec5d8.md#insn-00aec600)

~~~diff
- 00aec530 ["INT_ADD", "register:40f0:8", ["const:aec530:8", "const:4:8"]]
- 00aec530 ["CALL", null, ["callee:00bde130:8"]]
+ 00aec5f8 ["INT_ADD", "register:40f0:8", ["const:aec5f8:8", "const:4:8"]]
+ 00aec5f8 ["CALL", null, ["callee:00bde130:8"]]
- 00aec530 bytes d4c60394
+ 00aec5f8 bytes cec60394
- 00aec52c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aec52c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec52c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec52c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aec5f4 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00aec5f4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec5f4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec5f4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec52c bytes 00c81791
+ 00aec5f4 bytes 00fc1991
- 00aec538 ["COPY", "tmp:0:8", ["const:870:8"]]
- 00aec538 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aec538 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aec538 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aec600 ["COPY", "tmp:0:8", ["const:930:8"]]
+ 00aec600 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec600 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec600 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aec538 bytes 08c12191
+ 00aec600 bytes 08c12491
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73187ce9fdb7c720fe9cbc506d0e6eb0"></a>

### [`00aec54c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec54c.md) → [`00aec614`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec614.md) _ZN8firebase4util3map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
    "old": {
      "definition_site": "00aec578",
      "incomplete_value": true,
      "site": "00aec578",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:878:8"
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
    "old": {
      "definition_site": "00aec560",
      "incomplete_value": true,
      "site": "00aec560",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aec56c",
      "incomplete_value": false,
      "site": "00aec570",
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
      "00aec624",
      "READ",
      [
        "storage",
        "010a0878",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec634",
      "PARAM",
      [
        "storage",
        "002a0e6d",
        null,
        "string"
      ]
    ],
    [
      "00aec640",
      "WRITE",
      [
        "storage",
        "010a0878",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec624",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec634",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ],
    [
      "00aec640",
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec54c.md#insn-00aec570) · [`00aec578`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec54c.md#insn-00aec578) · [`00aec55c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec54c.md#insn-00aec55c)
- 新版 [`00aec638`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec614.md#insn-00aec638) · [`00aec640`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec614.md#insn-00aec640) · [`00aec624`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec614.md#insn-00aec624)

~~~diff
- 00aec570 ["INT_ADD", "register:40f0:8", ["const:aec570:8", "const:4:8"]]
- 00aec570 ["CALL", null, ["callee:00bde040:8"]]
+ 00aec638 ["INT_ADD", "register:40f0:8", ["const:aec638:8", "const:4:8"]]
+ 00aec638 ["CALL", null, ["callee:00bde040:8"]]
- 00aec570 bytes 88c60394
+ 00aec638 bytes 82c60394
- 00aec578 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:878:8"]]
- 00aec578 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec640 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
+ 00aec640 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec578 bytes 603e04f9
+ 00aec640 bytes 609e04f9
- 00aec55c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:878:8"]]
- 00aec55c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec624 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
+ 00aec624 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec55c bytes 683e44f9
+ 00aec624 bytes 689e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c491b8db4c86035a13e4642eec4f8a5"></a>

### [`00aec58c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec58c.md) → [`00aec654`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec654.md) _ZN8firebase4util3map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aec5b8",
      "incomplete_value": true,
      "site": "00aec5b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:878:8"
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
    "old": {
      "definition_site": "00aec5a0",
      "incomplete_value": true,
      "site": "00aec5a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aec5a8",
      "incomplete_value": false,
      "site": "00aec5b0",
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
      "00aec664",
      "READ",
      [
        "storage",
        "010a0878",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec670",
      "PARAM",
      [
        "storage",
        "002a0e6d",
        null,
        "string"
      ]
    ],
    [
      "00aec680",
      "WRITE",
      [
        "storage",
        "010a0878",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec664",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec670",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ],
    [
      "00aec680",
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec5b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec58c.md#insn-00aec5b0) · [`00aec5b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec58c.md#insn-00aec5b8) · [`00aec59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec58c.md#insn-00aec59c)
- 新版 [`00aec678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec654.md#insn-00aec678) · [`00aec680`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec654.md#insn-00aec680) · [`00aec664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec654.md#insn-00aec664)

~~~diff
- 00aec5b0 ["INT_ADD", "register:40f0:8", ["const:aec5b0:8", "const:4:8"]]
- 00aec5b0 ["CALL", null, ["callee:00bde040:8"]]
+ 00aec678 ["INT_ADD", "register:40f0:8", ["const:aec678:8", "const:4:8"]]
+ 00aec678 ["CALL", null, ["callee:00bde040:8"]]
- 00aec5b0 bytes 78c60394
+ 00aec678 bytes 72c60394
- 00aec5b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:878:8"]]
- 00aec5b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec680 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
+ 00aec680 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec5b8 bytes 603e04f9
+ 00aec680 bytes 609e04f9
- 00aec59c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:878:8"]]
- 00aec59c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec664 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
+ 00aec664 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec59c bytes 683e44f9
+ 00aec664 bytes 689e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fb8a4a18bbf1560dbdf2a048a161d1d2"></a>

### [`00aec610`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec610.md) → [`00aec6d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec6d8.md) _ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobject

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
            "const:878:8"
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
      "definition_site": "00aec624",
      "incomplete_value": true,
      "site": "00aec624",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aec62c",
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
      "00aec6e8",
      "READ",
      [
        "storage",
        "010a0878",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec6f4",
      "PARAM",
      [
        "storage",
        "002a0e6d",
        null,
        "string"
      ]
    ],
    [
      "00aec708",
      "WRITE",
      [
        "storage",
        "010a0878",
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
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec6f4",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec638`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec610.md#insn-00aec638) · [`00aec640`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec610.md#insn-00aec640) · [`00aec620`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec610.md#insn-00aec620)
- 新版 [`00aec700`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec6d8.md#insn-00aec700) · [`00aec708`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec6d8.md#insn-00aec708) · [`00aec6e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec6d8.md#insn-00aec6e8)

~~~diff
- 00aec638 ["INT_ADD", "register:40f0:8", ["const:aec638:8", "const:4:8"]]
- 00aec638 ["CALL", null, ["callee:00bde040:8"]]
+ 00aec700 ["INT_ADD", "register:40f0:8", ["const:aec700:8", "const:4:8"]]
+ 00aec700 ["CALL", null, ["callee:00bde040:8"]]
- 00aec638 bytes 56c60394
+ 00aec700 bytes 50c60394
- 00aec640 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:878:8"]]
- 00aec640 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aec708 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
+ 00aec708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec640 bytes 603e04f9
+ 00aec708 bytes 609e04f9
- 00aec620 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:878:8"]]
- 00aec620 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aec6e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:938:8"]]
+ 00aec6e8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec620 bytes 683e44f9
+ 00aec6e8 bytes 689e44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8616ebf1de949ceeb278923eaa246ebd"></a>

### [`00aec660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec660.md) → [`00aec728`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec728.md) _ZN8firebase4util3map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination

命令の説明率　旧版 94.87% / 新版 94.87%

CFGの説明率　旧版 50.00% / 新版 57.14%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00aec6e8",
      "incomplete_value": true,
      "site": "00aec6e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:880:8"
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
    "old": {
      "definition_site": "00aec694",
      "incomplete_value": true,
      "site": "00aec6a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:878:8"
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
      "00aec73c",
      "READ",
      [
        "storage",
        "010a0880",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00aec694",
      "READ",
      [
        "storage",
        "010a0878",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec7b0",
      "WRITE",
      [
        "storage",
        "010a0880",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aec73c",
      "READ",
      [
        "storage",
        "010a0940",
        null,
        "undefined1"
      ]
    ],
    [
      "00aec75c",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec7b0",
      "WRITE",
      [
        "storage",
        "010a0940",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec6a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec660.md#insn-00aec6a0) · [`00aec6e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec660.md#insn-00aec6e8) · [`00aec674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec660.md#insn-00aec674)
- 新版 [`00aec768`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec728.md#insn-00aec768) · [`00aec7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec728.md#insn-00aec7b0) · [`00aec73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec728.md#insn-00aec73c)

~~~diff
- 00aec6a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aec6a0 ["INT_ADD", "register:40f0:8", ["const:aec6a0:8", "const:4:8"]]
- 00aec6a0 ["CALLIND", null, ["register:0:8"]]
+ 00aec768 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aec768 ["INT_ADD", "register:40f0:8", ["const:aec768:8", "const:4:8"]]
+ 00aec768 ["CALLIND", null, ["register:0:8"]]
- 00aec6a0 bytes 00013fd6
+ 00aec768 bytes 00013fd6
- 00aec6e8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aec6e8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:880:8"]]
- 00aec6e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aec7b0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aec7b0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:940:8"]]
+ 00aec7b0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aec6e8 bytes a0022239
+ 00aec7b0 bytes a0022539
- 00aec674 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:880:8"]]
- 00aec674 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aec674 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aec73c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:940:8"]]
+ 00aec73c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aec73c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aec674 bytes a8026239
+ 00aec73c bytes a8026539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-96ec0f4cd07483063968823ff19b07da"></a>

### [`00aec6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec6fc.md) → [`00aec7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec7c4.md) _ZN8firebase4util3map12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_store_alignment

命令の説明率　旧版 82.50% / 新版 82.50%

CFGの説明率　旧版 77.78% / 新版 70.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 2件, `unresolved_store_alignment` 5件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec6fc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec700"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec700"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec6fc",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aec700",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aec704",
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
      "00aec7c4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aec7c8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aec7cc",
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

- 旧版 [`00aec6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec6fc.md#insn-00aec6fc) · [`00aec700`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec6fc.md#insn-00aec700) · [`00aec704`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec6fc.md#insn-00aec704)

~~~diff
- 00aec6fc ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00aec6fc ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aec6fc ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aec6fc bytes f50f1df8
- 00aec700 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aec700 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aec700 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aec700 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aec700 bytes f44f01a9
- 00aec704 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aec704 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aec704 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aec704 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aec704 bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-926f093f4603827f9b9b1c28b1ae6caf"></a>

### [`00aec79c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec79c.md) → [`00aec864`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec864.md) _ZN8firebase4util3map14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

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
      "site": "00aec7dc"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aec8a4"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec7b8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec7b0",
      "READ",
      [
        "storage",
        "010a0878",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aec7b8",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aec8a8"
      ]
    ],
    [
      "unmatched:00aec7c0",
      "PARAM",
      [
        "storage",
        "002a0e6d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aec878",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec880",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aec8a8"
      ]
    ],
    [
      "00aec888",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec7b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec79c.md#insn-00aec7b8) · [`00aec7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec79c.md#insn-00aec7d4) · [`00aec7dc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec79c.md#insn-00aec7dc)
- 新版 [`00aec89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec864.md#insn-00aec89c)

~~~diff
- 00aec7b8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aec7b8 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aec7b8 bytes 410100b5
- 00aec7d4 ["INT_ADD", "register:40f0:8", ["const:aec7d4:8", "const:4:8"]]
- 00aec7d4 ["CALL", null, ["callee:00bde040:8"]]
+ 00aec89c ["INT_ADD", "register:40f0:8", ["const:aec89c:8", "const:4:8"]]
+ 00aec89c ["CALL", null, ["callee:00bde040:8"]]
- 00aec7d4 bytes efc50394
+ 00aec89c bytes e9c50394
- 00aec7dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:878:8"]]
- 00aec7dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec7dc bytes 803e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-393d48d6fd0e49e1cf46af90137978b0"></a>

### [`00aec80c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec80c.md) → [`00aec8d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec8d4.md) _ZN8firebase4util3map11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde000`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde000.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde0b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde0b0.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
    "old": {
      "definition_site": "00aec828",
      "incomplete_value": false,
      "site": "00aec82c",
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
    "old": {
      "definition_site": "00aec838",
      "incomplete_value": true,
      "site": "00aec844",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aec8f0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aec900",
      "DATA",
      [
        "storage",
        "010a0888",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aec8f0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aec900",
      "DATA",
      [
        "storage",
        "010a0948",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec82c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec80c.md#insn-00aec82c) · [`00aec828`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec80c.md#insn-00aec828) · [`00aec834`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec80c.md#insn-00aec834)
- 新版 [`00aec8f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec8d4.md#insn-00aec8f4) · [`00aec8f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec8d4.md#insn-00aec8f0) · [`00aec8fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec8d4.md#insn-00aec8fc)

~~~diff
- 00aec82c ["INT_ADD", "register:40f0:8", ["const:aec82c:8", "const:4:8"]]
- 00aec82c ["CALL", null, ["callee:00bde130:8"]]
+ 00aec8f4 ["INT_ADD", "register:40f0:8", ["const:aec8f4:8", "const:4:8"]]
+ 00aec8f4 ["CALL", null, ["callee:00bde130:8"]]
- 00aec82c bytes 15c60394
+ 00aec8f4 bytes 0fc60394
- 00aec828 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aec828 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec828 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec828 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aec8f0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aec8f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec8f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec8f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec828 bytes 001c1591
+ 00aec8f0 bytes 00501791
- 00aec834 ["COPY", "tmp:0:8", ["const:888:8"]]
- 00aec834 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aec834 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aec834 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aec8fc ["COPY", "tmp:0:8", ["const:948:8"]]
+ 00aec8fc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec8fc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec8fc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aec834 bytes 08212291
+ 00aec8fc bytes 08212591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e4122ee120468f7eb8471555df97c4d8"></a>

### [`00aec848`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec848.md) → [`00aec910`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec910.md) _ZN8firebase4util3map13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00aec888"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aec950"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec864"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aec85c",
      "READ",
      [
        "storage",
        "010a0878",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aec864",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aec954"
      ]
    ],
    [
      "unmatched:00aec86c",
      "PARAM",
      [
        "storage",
        "002a0e6d",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aec924",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec92c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aec954"
      ]
    ],
    [
      "00aec934",
      "PARAM",
      [
        "storage",
        "002a0efa",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec864`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec848.md#insn-00aec864) · [`00aec880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec848.md#insn-00aec880) · [`00aec888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec848.md#insn-00aec888)
- 新版 [`00aec948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec910.md#insn-00aec948)

~~~diff
- 00aec864 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aec864 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aec864 bytes 410100b5
- 00aec880 ["INT_ADD", "register:40f0:8", ["const:aec880:8", "const:4:8"]]
- 00aec880 ["CALL", null, ["callee:00bde040:8"]]
+ 00aec948 ["INT_ADD", "register:40f0:8", ["const:aec948:8", "const:4:8"]]
+ 00aec948 ["CALL", null, ["callee:00bde040:8"]]
- 00aec880 bytes c4c50394
+ 00aec948 bytes bec50394
- 00aec888 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:878:8"]]
- 00aec888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec888 bytes 803e04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c4e63162c3265898fea659037e8fc2d"></a>

### [`00aec8b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec8b8.md) → [`00aec980`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec980.md) _ZN8firebase4util3map10GetFieldIdENS1_5FieldE

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
    "old": {
      "definition_site": "00aec8d4",
      "incomplete_value": false,
      "site": "00aec8d8",
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
    "old": {
      "definition_site": "00aec8e4",
      "incomplete_value": true,
      "site": "00aec8f0",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aec99c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aec9ac",
      "DATA",
      [
        "storage",
        "010a08a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aec99c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aec9ac",
      "DATA",
      [
        "storage",
        "010a0960",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec8d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec8b8.md#insn-00aec8d8) · [`00aec8d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec8b8.md#insn-00aec8d4) · [`00aec8e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec8b8.md#insn-00aec8e0)
- 新版 [`00aec9a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec980.md#insn-00aec9a0) · [`00aec99c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec980.md#insn-00aec99c) · [`00aec9a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec980.md#insn-00aec9a8)

~~~diff
- 00aec8d8 ["INT_ADD", "register:40f0:8", ["const:aec8d8:8", "const:4:8"]]
- 00aec8d8 ["CALL", null, ["callee:00bde130:8"]]
+ 00aec9a0 ["INT_ADD", "register:40f0:8", ["const:aec9a0:8", "const:4:8"]]
+ 00aec9a0 ["CALL", null, ["callee:00bde130:8"]]
- 00aec8d8 bytes eac50394
+ 00aec9a0 bytes e4c50394
- 00aec8d4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aec8d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aec8d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aec8d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aec99c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00aec99c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec99c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aec99c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aec8d4 bytes 00c81791
+ 00aec99c bytes 00fc1991
- 00aec8e0 ["COPY", "tmp:0:8", ["const:8a0:8"]]
- 00aec8e0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aec8e0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aec8e0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aec9a8 ["COPY", "tmp:0:8", ["const:960:8"]]
+ 00aec9a8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec9a8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aec9a8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aec8e0 bytes 08812291
+ 00aec9a8 bytes 08812591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03e4e70ffc87ee6bb00bdec476b03d24"></a>

### [`00aec8f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec8f4.md) → [`00aec9bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9bc.md) _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

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
      "site": "00aec920"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aec9e8"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aec908",
      "incomplete_value": true,
      "site": "00aec908",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00aec9cc",
      "READ",
      [
        "storage",
        "010a08a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec9d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aec924"
      ]
    ],
    [
      "unmatched:00aec914",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aec9cc",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      "00aec9d0",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aec9ec"
      ]
    ],
    [
      "00aec9dc",
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec918`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec8f4.md#insn-00aec918) · [`00aec920`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec8f4.md#insn-00aec920) · [`00aec930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec8f4.md#insn-00aec930)

~~~diff
- 00aec918 ["INT_ADD", "register:40f0:8", ["const:aec918:8", "const:4:8"]]
- 00aec918 ["CALL", null, ["callee:00bde040:8"]]
- 00aec918 bytes 9ec50394
- 00aec920 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00aec920 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec920 bytes 605604f9
- 00aec930 ["COPY", "register:0:8", ["register:40f0:8"]]
- 00aec930 ["RETURN", null, ["register:0:8"]]
- 00aec930 bytes c0035fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f08218670053417b1c366f22c03d8b23"></a>

### [`00aec934`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec934.md) → [`00aec9fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9fc.md) _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

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
    "old": {
      "definition_site": "00aec960",
      "incomplete_value": true,
      "site": "00aec960",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
    "old": {
      "definition_site": "00aec948",
      "incomplete_value": true,
      "site": "00aec948",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aec950",
      "incomplete_value": false,
      "site": "00aec958",
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
      "00aeca0c",
      "READ",
      [
        "storage",
        "010a08a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeca18",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      "00aeca28",
      "WRITE",
      [
        "storage",
        "010a08a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeca0c",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeca18",
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ],
    [
      "00aeca28",
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec958`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec934.md#insn-00aec958) · [`00aec960`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec934.md#insn-00aec960) · [`00aec944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec934.md#insn-00aec944)
- 新版 [`00aeca20`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9fc.md#insn-00aeca20) · [`00aeca28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9fc.md#insn-00aeca28) · [`00aeca0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aec9fc.md#insn-00aeca0c)

~~~diff
- 00aec958 ["INT_ADD", "register:40f0:8", ["const:aec958:8", "const:4:8"]]
- 00aec958 ["CALL", null, ["callee:00bde040:8"]]
+ 00aeca20 ["INT_ADD", "register:40f0:8", ["const:aeca20:8", "const:4:8"]]
+ 00aeca20 ["CALL", null, ["callee:00bde040:8"]]
- 00aec958 bytes 8ec50394
+ 00aeca20 bytes 88c50394
- 00aec960 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00aec960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aeca28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00aeca28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec960 bytes 605604f9
+ 00aeca28 bytes 60b604f9
- 00aec944 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00aec944 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aeca0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00aeca0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aec944 bytes 685644f9
+ 00aeca0c bytes 68b644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-709e855c2edf2715475a5adda01ec7a1"></a>

### [`00aec974`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec974.md) → [`00aeca3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca3c.md) _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec9a4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aeca6c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aec988",
      "incomplete_value": true,
      "site": "00aec988",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00aeca4c",
      "READ",
      [
        "storage",
        "010a08a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aec994",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aec99c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00aeca4c",
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
      "00aeca64",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec988`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec974.md#insn-00aec988) · [`00aec99c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec974.md#insn-00aec99c) · [`00aec9a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec974.md#insn-00aec9a4)
- 新版 [`00aeca50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca3c.md#insn-00aeca50)

~~~diff
- 00aec988 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aec988 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
+ 00aeca50 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00aeca50 ["CBRANCH", null, ["local:b4:8", "tmp:0:1"]]
- 00aec988 bytes 080100b5
+ 00aeca50 bytes 080100b5
- 00aec99c ["INT_ADD", "register:40f0:8", ["const:aec99c:8", "const:4:8"]]
- 00aec99c ["CALL", null, ["callee:00bde040:8"]]
- 00aec99c bytes 7dc50394
- 00aec9a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00aec9a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec9a4 bytes 605604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f701af12ffebff278fdcee2297efb507"></a>

### [`00aec9b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec9b8.md) → [`00aeca80`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca80.md) _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 88.24% / 新版 88.24%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aec9e8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aecab0"
    },
    "old": null
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
      "definition_site": "00aec9cc",
      "incomplete_value": true,
      "site": "00aec9cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00aeca90",
      "READ",
      [
        "storage",
        "010a08a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aec9d4",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aec9e8",
      "WRITE",
      [
        "storage",
        "010a08a8",
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
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeca9c",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aec9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec9b8.md#insn-00aec9cc) · [`00aec9e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec9b8.md#insn-00aec9e0) · [`00aec9e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aec9b8.md#insn-00aec9e8)
- 新版 [`00aeca94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca80.md#insn-00aeca94) · [`00aecaa8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeca80.md#insn-00aecaa8)

~~~diff
- 00aec9cc ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aec9cc ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aeca94 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00aeca94 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aec9cc bytes 080100b5
+ 00aeca94 bytes 080100b5
- 00aec9e0 ["INT_ADD", "register:40f0:8", ["const:aec9e0:8", "const:4:8"]]
- 00aec9e0 ["CALL", null, ["callee:00bde040:8"]]
+ 00aecaa8 ["INT_ADD", "register:40f0:8", ["const:aecaa8:8", "const:4:8"]]
+ 00aecaa8 ["CALL", null, ["callee:00bde040:8"]]
- 00aec9e0 bytes 6cc50394
+ 00aecaa8 bytes 66c50394
- 00aec9e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00aec9e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aec9e8 bytes 605604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5074f7ca632e49ccfa06412caab05882"></a>

### [`00aeca08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeca08.md) → [`00aecad0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecad0.md) _ZN8firebase4util22parcel_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, call, call_count, cfg_edge_inventory, constant, control_flow, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment

命令の説明率　旧版 74.36% / 新版 74.36%

CFGの説明率　旧版 33.33% / 新版 37.50%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件, `unresolved_call_alignment` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
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
    "old": {
      "definition_site": "00aeca90",
      "incomplete_value": true,
      "site": "00aeca90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:8b0:8"
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
      "site": "00aeca48"
    }
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeca5c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aecae4",
      "READ",
      [
        "storage",
        "010a08b0",
        null,
        "undefined1"
      ]
    ],
    [
      "unmatched:00aeca3c",
      "READ",
      [
        "storage",
        "010a08a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecb58",
      "WRITE",
      [
        "storage",
        "010a08b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aecae4",
      "READ",
      [
        "storage",
        "010a0970",
        null,
        "undefined1"
      ]
    ],
    [
      "00aecb04",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecb58",
      "WRITE",
      [
        "storage",
        "010a0970",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeca48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeca08.md#insn-00aeca48) · [`00aeca5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeca08.md#insn-00aeca5c) · [`00aeca90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeca08.md#insn-00aeca90)
- 新版 [`00aecb58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecad0.md#insn-00aecb58)

~~~diff
- 00aeca48 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeca48 ["INT_ADD", "register:40f0:8", ["const:aeca48:8", "const:4:8"]]
- 00aeca48 ["CALLIND", null, ["register:0:8"]]
- 00aeca48 bytes 00013fd6
- 00aeca5c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeca5c ["INT_ADD", "register:40f0:8", ["const:aeca5c:8", "const:4:8"]]
- 00aeca5c ["CALLIND", null, ["register:0:8"]]
- 00aeca5c bytes 00013fd6
- 00aeca90 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aeca90 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8b0:8"]]
- 00aeca90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aecb58 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aecb58 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:970:8"]]
+ 00aecb58 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aeca90 bytes a0c22239
+ 00aecb58 bytes a0c22539
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-867e5a7d332169d81777c5b5e54f23c3"></a>

### [`00aecaa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecaa4.md) → [`00aecb6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecb6c.md) _ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 72.50% / 新版 72.50%

CFGの説明率　旧版 18.18% / 新版 20.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `store_destination` 1件, `unresolved_call_alignment` 1件, `unresolved_store_alignment` 6件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aecaa4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aecaa8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aecaa8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aecaa4",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aecaa8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aecaac",
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
      "00aecb6c",
      "WRITE",
      [
        "storage",
        "Stack[-0x30]",
        null,
        null
      ]
    ],
    [
      "00aecb70",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aecb74",
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

- 旧版 [`00aecaa4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecaa4.md#insn-00aecaa4) · [`00aecaa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecaa4.md#insn-00aecaa8) · [`00aecaac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecaa4.md#insn-00aecaac)

~~~diff
- 00aecaa4 ["COPY", "tmp:0:8", ["register:40a8:8"]]
- 00aecaa4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffd0:8"]]
- 00aecaa4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aecaa4 bytes f50f1df8
- 00aecaa8 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aecaa8 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aecaa8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aecaa8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aecaa8 bytes f44f01a9
- 00aecaac ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aecaac ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aecaac ["INT_ADD", "tmp:2:8", ["register:8:8", "const:20:8"]]
- 00aecaac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aecaac bytes fd7b02a9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a032e3a8f215d5057b345b63c1ce18a2"></a>

### [`00aecb44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecb44.md) → [`00aecc0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc0c.md) _ZN8firebase4util22parcel_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, call_argument_candidate, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 67.86% / 新版 67.86%

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
      "site": "00aecb84"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aecc4c"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aecb60"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aecb58",
      "READ",
      [
        "storage",
        "010a08a8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aecb60",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aecc50"
      ]
    ],
    [
      "unmatched:00aecb68",
      "PARAM",
      [
        "storage",
        "002941d3",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aecc20",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecc28",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aecc50"
      ]
    ],
    [
      "00aecc30",
      "PARAM",
      [
        "storage",
        "00294260",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecb44.md#insn-00aecb60) · [`00aecb7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecb44.md#insn-00aecb7c) · [`00aecb84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecb44.md#insn-00aecb84)
- 新版 [`00aecc44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc0c.md#insn-00aecc44)

~~~diff
- 00aecb60 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aecb60 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aecb60 bytes 410100b5
- 00aecb7c ["INT_ADD", "register:40f0:8", ["const:aecb7c:8", "const:4:8"]]
- 00aecb7c ["CALL", null, ["callee:00bde040:8"]]
+ 00aecc44 ["INT_ADD", "register:40f0:8", ["const:aecc44:8", "const:4:8"]]
+ 00aecc44 ["CALL", null, ["callee:00bde040:8"]]
- 00aecb7c bytes 05c50394
+ 00aecc44 bytes ffc40394
- 00aecb84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00aecb84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecb84 bytes 805604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-550da9837e690ec62ea00e7733ee8fa8"></a>

### [`00aecbb4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecbb4.md) → [`00aecc7c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc7c.md) _ZN8firebase4util22parcel_file_descriptor11GetMethodIdENS1_6MethodE

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
    "old": {
      "definition_site": "00aecbd0",
      "incomplete_value": false,
      "site": "00aecbd4",
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
    "old": {
      "definition_site": "00aecbe0",
      "incomplete_value": true,
      "site": "00aecbec",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aecc98",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aecca8",
      "DATA",
      [
        "storage",
        "010a08b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aecc98",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aecca8",
      "DATA",
      [
        "storage",
        "010a0978",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecbd4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecbb4.md#insn-00aecbd4) · [`00aecbd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecbb4.md#insn-00aecbd0) · [`00aecbdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecbb4.md#insn-00aecbdc)
- 新版 [`00aecc9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc7c.md#insn-00aecc9c) · [`00aecc98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc7c.md#insn-00aecc98) · [`00aecca4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecc7c.md#insn-00aecca4)

~~~diff
- 00aecbd4 ["INT_ADD", "register:40f0:8", ["const:aecbd4:8", "const:4:8"]]
- 00aecbd4 ["CALL", null, ["callee:00bde130:8"]]
+ 00aecc9c ["INT_ADD", "register:40f0:8", ["const:aecc9c:8", "const:4:8"]]
+ 00aecc9c ["CALL", null, ["callee:00bde130:8"]]
- 00aecbd4 bytes 2bc50394
+ 00aecc9c bytes 25c50394
- 00aecbd0 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aecbd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aecbd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aecbd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aecc98 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aecc98 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aecc98 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aecc98 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aecbd0 bytes 001c1591
+ 00aecc98 bytes 00501791
- 00aecbdc ["COPY", "tmp:0:8", ["const:8b8:8"]]
- 00aecbdc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aecbdc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aecbdc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aecca4 ["COPY", "tmp:0:8", ["const:978:8"]]
+ 00aecca4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aecca4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aecca4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aecbdc bytes 08e12291
+ 00aecca4 bytes 08e12591
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e5cc80c4527c8adf6bf612f9b6e5f31"></a>

### [`00aecbf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecbf0.md) → [`00aeccb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aeccb8.md) _ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00bddf70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf70.md) [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00bde020`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde020.md) [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_store_alignment

命令の説明率　旧版 53.57% / 新版 53.57%

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
      "site": "00aecbf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aecbf0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aecbf4"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aecbf0",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aecbf4",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aecc04",
      "READ",
      [
        "storage",
        "010a08a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aeccb8",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aeccbc",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aecccc",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecbf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecbf0.md#insn-00aecbf0) · [`00aecbf4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecbf0.md#insn-00aecbf4) · [`00aecc0c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecbf0.md#insn-00aecc0c)

~~~diff
- 00aecbf0 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aecbf0 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aecbf0 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aecbf0 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aecbf0 bytes f44fbea9
- 00aecbf4 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aecbf4 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aecbf4 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aecbf4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aecbf4 bytes fd7b01a9
- 00aecc0c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aecc0c ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aecc0c bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cbd124299ec00ee6100090f552e98c3"></a>

### [`00aecc9c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecc9c.md) → [`00aecd64`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecd64.md) _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 75.00% / 新版 75.00%

CFGの説明率　旧版 25.00% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aeccc8"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aecd90"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aeccb0",
      "incomplete_value": true,
      "site": "00aeccb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00aecd74",
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aeccbc",
      "PARAM",
      [
        "storage",
        "0029ff32",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aeccc0",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00aecd74",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecd84",
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      "00aecd88",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeccb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecc9c.md#insn-00aeccb0) · [`00aeccc0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecc9c.md#insn-00aeccc0) · [`00aeccc8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecc9c.md#insn-00aeccc8)
- 新版 [`00aecd78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecd64.md#insn-00aecd78)

~~~diff
- 00aeccb0 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aeccb0 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aecd78 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00aecd78 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aeccb0 bytes e80000b5
+ 00aecd78 bytes e80000b5
- 00aeccc0 ["INT_ADD", "register:40f0:8", ["const:aeccc0:8", "const:4:8"]]
- 00aeccc0 ["CALL", null, ["callee:00bde040:8"]]
- 00aeccc0 bytes b4c40394
- 00aeccc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00aeccc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeccc8 bytes 606604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-323a174726694e610ef43a6d1be04f1a"></a>

### [`00aeccdc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeccdc.md) → [`00aecda4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecda4.md) _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
    "old": {
      "definition_site": "00aecd08",
      "incomplete_value": true,
      "site": "00aecd08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
    "old": {
      "definition_site": "00aeccf0",
      "incomplete_value": true,
      "site": "00aeccf0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
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
    "old": {
      "definition_site": "00aeccf8",
      "incomplete_value": false,
      "site": "00aecd00",
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
            "const:f32:8"
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
      "00aecdb4",
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecdc0",
      "PARAM",
      [
        "storage",
        "0029ff32",
        null,
        "string"
      ]
    ],
    [
      "00aecdd0",
      "WRITE",
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
      "00aecdb4",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecdc0",
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      "00aecdd0",
      "WRITE",
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

- 旧版 [`00aecd00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeccdc.md#insn-00aecd00) · [`00aecd08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeccdc.md#insn-00aecd08) · [`00aeccec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeccdc.md#insn-00aeccec)
- 新版 [`00aecdc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecda4.md#insn-00aecdc8) · [`00aecdd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecda4.md#insn-00aecdd0) · [`00aecdb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecda4.md#insn-00aecdb4)

~~~diff
- 00aecd00 ["INT_ADD", "register:40f0:8", ["const:aecd00:8", "const:4:8"]]
- 00aecd00 ["CALL", null, ["callee:00bde040:8"]]
+ 00aecdc8 ["INT_ADD", "register:40f0:8", ["const:aecdc8:8", "const:4:8"]]
+ 00aecdc8 ["CALL", null, ["callee:00bde040:8"]]
- 00aecd00 bytes a4c40394
+ 00aecdc8 bytes 9ec40394
- 00aecd08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00aecd08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aecdd0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
+ 00aecdd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecd08 bytes 606604f9
+ 00aecdd0 bytes 60c604f9
- 00aeccec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00aeccec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aecdb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
+ 00aecdb4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aeccec bytes 686644f9
+ 00aecdb4 bytes 68c644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fecec2368226fac118abdebf88274e8a"></a>

### [`00aecd1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecd1c.md) → [`00aecde4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecde4.md) _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 1件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md)

変更の種類 branch_condition_or_target, branch_value, call, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 70.59% / 新版 70.59%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_call_alignment` 1件, `unresolved_store_alignment` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aecd4c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aece14"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
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
    "old": {
      "definition_site": "00aecd30",
      "incomplete_value": true,
      "site": "00aecd30",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
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
      "00aecdf4",
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aecd3c",
      "PARAM",
      [
        "storage",
        "0029ff32",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00aecd44",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ],
  "added": [
    [
      "00aecdf4",
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
      "00aece0c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde040"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecd30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecd1c.md#insn-00aecd30) · [`00aecd44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecd1c.md#insn-00aecd44) · [`00aecd4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecd1c.md#insn-00aecd4c)
- 新版 [`00aecdf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecde4.md#insn-00aecdf8)

~~~diff
- 00aecd30 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
- 00aecd30 ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
+ 00aecdf8 ["INT_NOTEQUAL", "tmp:0:1", ["register:4040:8", "const:0:8"]]
+ 00aecdf8 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aecd30 bytes 080100b5
+ 00aecdf8 bytes 080100b5
- 00aecd44 ["INT_ADD", "register:40f0:8", ["const:aecd44:8", "const:4:8"]]
- 00aecd44 ["CALL", null, ["callee:00bde040:8"]]
- 00aecd44 bytes 93c40394
- 00aecd4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00aecd4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecd4c bytes 606604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-157bba7cbfcdc13df17a4e000d7a307e"></a>

### [`00aecd60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecd60.md) → [`00aece28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece28.md) _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobject

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
            "const:988:8"
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
            "const:8c8:8"
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
      "definition_site": "00aecd74",
      "incomplete_value": true,
      "site": "00aecd74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aece44",
      "incomplete_value": false,
      "site": "00aece50",
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
    "old": {
      "definition_site": "00aecd7c",
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
            "const:f32:8"
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
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aece44",
      "PARAM",
      [
        "storage",
        "0029ff32",
        null,
        "string"
      ]
    ],
    [
      "00aece58",
      "WRITE",
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
      "00aece44",
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
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecd88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecd60.md#insn-00aecd88) · [`00aecd90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecd60.md#insn-00aecd90) · [`00aecd70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecd60.md#insn-00aecd70)
- 新版 [`00aece50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece28.md#insn-00aece50) · [`00aece58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece28.md#insn-00aece58) · [`00aece38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece28.md#insn-00aece38)

~~~diff
- 00aecd88 ["INT_ADD", "register:40f0:8", ["const:aecd88:8", "const:4:8"]]
- 00aecd88 ["CALL", null, ["callee:00bde040:8"]]
+ 00aece50 ["INT_ADD", "register:40f0:8", ["const:aece50:8", "const:4:8"]]
+ 00aece50 ["CALL", null, ["callee:00bde040:8"]]
- 00aecd88 bytes 82c40394
+ 00aece50 bytes 7cc40394
- 00aecd90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00aecd90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aece58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
+ 00aece58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecd90 bytes 606604f9
+ 00aece58 bytes 60c604f9
- 00aecd70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00aecd70 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aece38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
+ 00aece38 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aecd70 bytes 686644f9
+ 00aece38 bytes 68c644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-af04985af54d07bec91bb2b6af96dcab"></a>

### [`00aecdb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecdb0.md) → [`00aece78`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece78.md) _ZN8firebase4util3set15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aecf00",
      "incomplete_value": true,
      "site": "00aecf00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aece38",
      "incomplete_value": true,
      "site": "00aece38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:8d0:8"
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
      "definition_site": "00aeceac",
      "incomplete_value": true,
      "site": "00aeceb8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecde4",
      "incomplete_value": true,
      "site": "00aecdf0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8c8:8"
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
      "00aece8c",
      "READ",
      [
        "storage",
        "010a08d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeceac",
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecf00",
      "WRITE",
      [
        "storage",
        "010a08d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aece8c",
      "READ",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeceac",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecf00",
      "WRITE",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecdf0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecdb0.md#insn-00aecdf0) · [`00aece38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecdb0.md#insn-00aece38) · [`00aecdc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecdb0.md#insn-00aecdc4)
- 新版 [`00aeceb8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece78.md#insn-00aeceb8) · [`00aecf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece78.md#insn-00aecf00) · [`00aece8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aece78.md#insn-00aece8c)

~~~diff
- 00aecdf0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aecdf0 ["INT_ADD", "register:40f0:8", ["const:aecdf0:8", "const:4:8"]]
- 00aecdf0 ["CALLIND", null, ["register:0:8"]]
+ 00aeceb8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aeceb8 ["INT_ADD", "register:40f0:8", ["const:aeceb8:8", "const:4:8"]]
+ 00aeceb8 ["CALLIND", null, ["register:0:8"]]
- 00aecdf0 bytes 00013fd6
+ 00aeceb8 bytes 00013fd6
- 00aece38 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aece38 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8d0:8"]]
- 00aece38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aecf00 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aecf00 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:990:8"]]
+ 00aecf00 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aece38 bytes a0422339
+ 00aecf00 bytes a0422639
- 00aecdc4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8d0:8"]]
- 00aecdc4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aecdc4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aece8c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:990:8"]]
+ 00aece8c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aece8c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aecdc4 bytes a8426339
+ 00aece8c bytes a8426639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cda75b8b4252add1c98e2c0f7811580"></a>

### [`00aece4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aece4c.md) → [`00aecf14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecf14.md) _ZN8firebase4util3set12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aecf50",
      "incomplete_value": true,
      "site": "00aecf50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:990:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aece88",
      "incomplete_value": true,
      "site": "00aece88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:8d0:8"
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
      "definition_site": "00aecfa0",
      "incomplete_value": true,
      "site": "00aecfa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeced8",
      "incomplete_value": true,
      "site": "00aeced8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "definition_site": "00aecf2c",
      "incomplete_value": true,
      "site": "00aecf2c",
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
      "definition_site": "00aece64",
      "incomplete_value": true,
      "site": "00aece64",
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
      "00aecf28",
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecf34",
      "READ",
      [
        "storage",
        "010a08d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aecf50",
      "WRITE",
      [
        "storage",
        "010a08d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aecf28",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecf34",
      "READ",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ],
    [
      "00aecf50",
      "WRITE",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aece88`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aece4c.md#insn-00aece88) · [`00aeced4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aece4c.md#insn-00aeced4) · [`00aeced8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aece4c.md#insn-00aeced8)
- 新版 [`00aecf50`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecf14.md#insn-00aecf50) · [`00aecf9c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecf14.md#insn-00aecf9c) · [`00aecfa0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecf14.md#insn-00aecfa0)

~~~diff
- 00aece88 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aece88 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aece88 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8d0:8"]]
- 00aece88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aecf50 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aecf50 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aecf50 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:990:8"]]
+ 00aecf50 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aece88 bytes bf422339
+ 00aecf50 bytes bf422639
- 00aeced4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aeced4 ["INT_ADD", "register:40f0:8", ["const:aeced4:8", "const:4:8"]]
- 00aeced4 ["CALLIND", null, ["register:0:8"]]
+ 00aecf9c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aecf9c ["INT_ADD", "register:40f0:8", ["const:aecf9c:8", "const:4:8"]]
+ 00aecf9c ["CALLIND", null, ["register:0:8"]]
- 00aeced4 bytes 00013fd6
+ 00aecf9c bytes 00013fd6
- 00aeced8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
- 00aeced8 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aeced8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aecfa0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
+ 00aecfa0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aecfa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aeced8 bytes 9f6604f9
+ 00aecfa0 bytes 9fc604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37bf33b33588a143b5298182f815119b"></a>

### [`00aeceec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeceec.md) → [`00aecfb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecfb4.md) _ZN8firebase4util3set14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aecff4",
      "incomplete_value": true,
      "site": "00aecff4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecf2c",
      "incomplete_value": true,
      "site": "00aecf2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "definition_site": "00aecfd0",
      "incomplete_value": true,
      "site": "00aecfd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecf08",
      "incomplete_value": true,
      "site": "00aecf08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aecfd8",
      "incomplete_value": false,
      "site": "00aecfec",
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
    "old": {
      "definition_site": "00aecf10",
      "incomplete_value": false,
      "site": "00aecf24",
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
            "const:f32:8"
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
      "00aecfc8",
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecfd8",
      "PARAM",
      [
        "storage",
        "0029ff32",
        null,
        "string"
      ]
    ],
    [
      "00aecff4",
      "WRITE",
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
      "00aecfc8",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aecfd8",
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      "00aecff4",
      "WRITE",
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

- 旧版 [`00aecf24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeceec.md#insn-00aecf24) · [`00aecf2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeceec.md#insn-00aecf2c) · [`00aecf00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aeceec.md#insn-00aecf00)
- 新版 [`00aecfec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecfb4.md#insn-00aecfec) · [`00aecff4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecfb4.md#insn-00aecff4) · [`00aecfc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecfb4.md#insn-00aecfc8)

~~~diff
- 00aecf24 ["INT_ADD", "register:40f0:8", ["const:aecf24:8", "const:4:8"]]
- 00aecf24 ["CALL", null, ["callee:00bde040:8"]]
+ 00aecfec ["INT_ADD", "register:40f0:8", ["const:aecfec:8", "const:4:8"]]
+ 00aecfec ["CALL", null, ["callee:00bde040:8"]]
- 00aecf24 bytes 1bc40394
+ 00aecfec bytes 15c40394
- 00aecf2c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
- 00aecf2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aecff4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
+ 00aecff4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecf2c bytes 806604f9
+ 00aecff4 bytes 80c604f9
- 00aecf00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
- 00aecf00 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aecfc8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
+ 00aecfc8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aecf00 bytes 816644f9
+ 00aecfc8 bytes 81c644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f7e51882f7ea6fcca2d3ea06959fed6a"></a>

### [`00aecf5c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecf5c.md) → [`00aed024`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed024.md) _ZN8firebase4util3set11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00bde580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde580.md) · 呼出先 1件 [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde630`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde630.md) · 呼出先 1件 [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

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
      "definition_site": "00aed040",
      "incomplete_value": false,
      "site": "00aed044",
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
      "definition_site": "00aecf78",
      "incomplete_value": false,
      "site": "00aecf7c",
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
      "definition_site": "00aed050",
      "incomplete_value": true,
      "site": "00aed05c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00aecf88",
      "incomplete_value": true,
      "site": "00aecf94",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aed040",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aed050",
      "DATA",
      [
        "storage",
        "010a08d8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed040",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aed050",
      "DATA",
      [
        "storage",
        "010a0998",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aecf7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecf5c.md#insn-00aecf7c) · [`00aecf78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecf5c.md#insn-00aecf78) · [`00aecf84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecf5c.md#insn-00aecf84)
- 新版 [`00aed044`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed024.md#insn-00aed044) · [`00aed040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed024.md#insn-00aed040) · [`00aed04c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed024.md#insn-00aed04c)

~~~diff
- 00aecf7c ["INT_ADD", "register:40f0:8", ["const:aecf7c:8", "const:4:8"]]
- 00aecf7c ["CALL", null, ["callee:00bde130:8"]]
+ 00aed044 ["INT_ADD", "register:40f0:8", ["const:aed044:8", "const:4:8"]]
+ 00aed044 ["CALL", null, ["callee:00bde130:8"]]
- 00aecf7c bytes 41c40394
+ 00aed044 bytes 3bc40394
- 00aecf78 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aecf78 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aecf78 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aecf78 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aed040 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aed040 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed040 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed040 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aecf78 bytes 001c1591
+ 00aed040 bytes 00501791
- 00aecf84 ["COPY", "tmp:0:8", ["const:8d8:8"]]
- 00aecf84 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aecf84 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aecf84 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aed04c ["COPY", "tmp:0:8", ["const:998:8"]]
+ 00aed04c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed04c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed04c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aecf84 bytes 08612391
+ 00aed04c bytes 08612691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-984a4f1fdc3761928078e625a1c6e5ee"></a>

### [`00aecf98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecf98.md) → [`00aed060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed060.md) _ZN8firebase4util3set13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aed0a0",
      "incomplete_value": true,
      "site": "00aed0a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:988:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecfd8",
      "incomplete_value": true,
      "site": "00aecfd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8c8:8"
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
      "definition_site": "00aed07c",
      "incomplete_value": true,
      "site": "00aed07c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aecfb4",
      "incomplete_value": true,
      "site": "00aecfb4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed084",
      "incomplete_value": false,
      "site": "00aed098",
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
    "old": {
      "definition_site": "00aecfbc",
      "incomplete_value": false,
      "site": "00aecfd0",
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
            "const:f32:8"
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
      "00aed074",
      "READ",
      [
        "storage",
        "010a08c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed084",
      "PARAM",
      [
        "storage",
        "0029ff32",
        null,
        "string"
      ]
    ],
    [
      "00aed0a0",
      "WRITE",
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
      "00aed074",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed084",
      "PARAM",
      [
        "storage",
        "0029ffbf",
        null,
        "string"
      ]
    ],
    [
      "00aed0a0",
      "WRITE",
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

- 旧版 [`00aecfd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecf98.md#insn-00aecfd0) · [`00aecfd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecf98.md#insn-00aecfd8) · [`00aecfac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aec/00aecf98.md#insn-00aecfac)
- 新版 [`00aed098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed060.md#insn-00aed098) · [`00aed0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed060.md#insn-00aed0a0) · [`00aed074`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed060.md#insn-00aed074)

~~~diff
- 00aecfd0 ["INT_ADD", "register:40f0:8", ["const:aecfd0:8", "const:4:8"]]
- 00aecfd0 ["CALL", null, ["callee:00bde040:8"]]
+ 00aed098 ["INT_ADD", "register:40f0:8", ["const:aed098:8", "const:4:8"]]
+ 00aed098 ["CALL", null, ["callee:00bde040:8"]]
- 00aecfd0 bytes f0c30394
+ 00aed098 bytes eac30394
- 00aecfd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
- 00aecfd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed0a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
+ 00aed0a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aecfd8 bytes 806604f9
+ 00aed0a0 bytes 80c604f9
- 00aecfac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
- 00aecfac ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed074 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
+ 00aed074 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aecfac bytes 816644f9
+ 00aed074 bytes 81c644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aff6398d3958663fc3c39fd27ba97f62"></a>

### [`00aed008`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed008.md) → [`00aed0d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed0d0.md) _ZN8firebase4util3set10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aed0ec",
      "incomplete_value": false,
      "site": "00aed0f0",
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
      "definition_site": "00aed024",
      "incomplete_value": false,
      "site": "00aed028",
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
      "definition_site": "00aed0fc",
      "incomplete_value": true,
      "site": "00aed108",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00aed034",
      "incomplete_value": true,
      "site": "00aed040",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aed0ec",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aed0fc",
      "DATA",
      [
        "storage",
        "010a08e0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aed0ec",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aed0fc",
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

- 旧版 [`00aed028`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed008.md#insn-00aed028) · [`00aed024`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed008.md#insn-00aed024) · [`00aed030`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed008.md#insn-00aed030)
- 新版 [`00aed0f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed0d0.md#insn-00aed0f0) · [`00aed0ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed0d0.md#insn-00aed0ec) · [`00aed0f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed0d0.md#insn-00aed0f8)

~~~diff
- 00aed028 ["INT_ADD", "register:40f0:8", ["const:aed028:8", "const:4:8"]]
- 00aed028 ["CALL", null, ["callee:00bde130:8"]]
+ 00aed0f0 ["INT_ADD", "register:40f0:8", ["const:aed0f0:8", "const:4:8"]]
+ 00aed0f0 ["CALL", null, ["callee:00bde130:8"]]
- 00aed028 bytes 16c40394
+ 00aed0f0 bytes 10c40394
- 00aed024 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aed024 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed024 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed024 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aed0ec ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00aed0ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed0ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed0ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed024 bytes 00c81791
+ 00aed0ec bytes 00fc1991
- 00aed030 ["COPY", "tmp:0:8", ["const:8e0:8"]]
- 00aed030 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aed030 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aed030 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aed0f8 ["COPY", "tmp:0:8", ["const:9a0:8"]]
+ 00aed0f8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed0f8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed0f8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aed030 bytes 08812391
+ 00aed0f8 bytes 08812691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a20633821cd4d4020a671e6a65dd02b4"></a>

### [`00aed044`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed044.md) → [`00aed10c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed10c.md) _ZN8firebase4util11short_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aed138",
      "incomplete_value": true,
      "site": "00aed138",
      "value": [
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
      "definition_site": "00aed070",
      "incomplete_value": true,
      "site": "00aed070",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "00aed120",
      "incomplete_value": true,
      "site": "00aed120",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed058",
      "incomplete_value": true,
      "site": "00aed058",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed12c",
      "incomplete_value": false,
      "site": "00aed130",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:395:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed064",
      "incomplete_value": false,
      "site": "00aed068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:429:8"
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
      "00aed11c",
      "READ",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed12c",
      "PARAM",
      [
        "storage",
        "002ae429",
        null,
        "string"
      ]
    ],
    [
      "00aed138",
      "WRITE",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed11c",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed12c",
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      "00aed138",
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

- 旧版 [`00aed068`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed044.md#insn-00aed068) · [`00aed070`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed044.md#insn-00aed070) · [`00aed054`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed044.md#insn-00aed054)
- 新版 [`00aed130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed10c.md#insn-00aed130) · [`00aed138`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed10c.md#insn-00aed138) · [`00aed11c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed10c.md#insn-00aed11c)

~~~diff
- 00aed068 ["INT_ADD", "register:40f0:8", ["const:aed068:8", "const:4:8"]]
- 00aed068 ["CALL", null, ["callee:00bde040:8"]]
+ 00aed130 ["INT_ADD", "register:40f0:8", ["const:aed130:8", "const:4:8"]]
+ 00aed130 ["CALL", null, ["callee:00bde040:8"]]
- 00aed068 bytes cac30394
+ 00aed130 bytes c4c30394
- 00aed070 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00aed070 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed138 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aed138 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed070 bytes 607604f9
+ 00aed138 bytes 60d604f9
- 00aed054 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00aed054 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed11c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aed11c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed054 bytes 687644f9
+ 00aed11c bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-746a66e3204c34f0570d6e1319979698"></a>

### [`00aed084`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed084.md) → [`00aed14c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed14c.md) _ZN8firebase4util11short_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aed178",
      "incomplete_value": true,
      "site": "00aed178",
      "value": [
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
      "definition_site": "00aed0b0",
      "incomplete_value": true,
      "site": "00aed0b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "00aed160",
      "incomplete_value": true,
      "site": "00aed160",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed098",
      "incomplete_value": true,
      "site": "00aed098",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed168",
      "incomplete_value": false,
      "site": "00aed170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:395:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed0a0",
      "incomplete_value": false,
      "site": "00aed0a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:429:8"
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
      "00aed15c",
      "READ",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed168",
      "PARAM",
      [
        "storage",
        "002ae429",
        null,
        "string"
      ]
    ],
    [
      "00aed178",
      "WRITE",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed15c",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed168",
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      "00aed178",
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

- 旧版 [`00aed0a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed084.md#insn-00aed0a8) · [`00aed0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed084.md#insn-00aed0b0) · [`00aed094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed084.md#insn-00aed094)
- 新版 [`00aed170`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed14c.md#insn-00aed170) · [`00aed178`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed14c.md#insn-00aed178) · [`00aed15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed14c.md#insn-00aed15c)

~~~diff
- 00aed0a8 ["INT_ADD", "register:40f0:8", ["const:aed0a8:8", "const:4:8"]]
- 00aed0a8 ["CALL", null, ["callee:00bde040:8"]]
+ 00aed170 ["INT_ADD", "register:40f0:8", ["const:aed170:8", "const:4:8"]]
+ 00aed170 ["CALL", null, ["callee:00bde040:8"]]
- 00aed0a8 bytes bac30394
+ 00aed170 bytes b4c30394
- 00aed0b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00aed0b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed178 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aed178 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed0b0 bytes 607604f9
+ 00aed178 bytes 60d604f9
- 00aed094 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00aed094 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed15c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aed15c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed094 bytes 687644f9
+ 00aed15c bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f6f2989564af9b3cd9c585fe72172392"></a>

### [`00aed0c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed0c4.md) → [`00aed18c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed18c.md) _ZN8firebase4util11short_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00aed1bc",
      "incomplete_value": true,
      "site": "00aed1bc",
      "value": [
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
      "definition_site": "00aed0f4",
      "incomplete_value": true,
      "site": "00aed0f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "00aed1a0",
      "incomplete_value": true,
      "site": "00aed1a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed0d8",
      "incomplete_value": true,
      "site": "00aed0d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed1ac",
      "incomplete_value": false,
      "site": "00aed1b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:395:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed0e4",
      "incomplete_value": false,
      "site": "00aed0ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:429:8"
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
      "00aed19c",
      "READ",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed1ac",
      "PARAM",
      [
        "storage",
        "002ae429",
        null,
        "string"
      ]
    ],
    [
      "00aed1bc",
      "WRITE",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed19c",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed1ac",
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      "00aed1bc",
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

- 旧版 [`00aed0ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed0c4.md#insn-00aed0ec) · [`00aed0f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed0c4.md#insn-00aed0f4) · [`00aed0d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed0c4.md#insn-00aed0d4)
- 新版 [`00aed1b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed18c.md#insn-00aed1b4) · [`00aed1bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed18c.md#insn-00aed1bc) · [`00aed19c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed18c.md#insn-00aed19c)

~~~diff
- 00aed0ec ["INT_ADD", "register:40f0:8", ["const:aed0ec:8", "const:4:8"]]
- 00aed0ec ["CALL", null, ["callee:00bde040:8"]]
+ 00aed1b4 ["INT_ADD", "register:40f0:8", ["const:aed1b4:8", "const:4:8"]]
+ 00aed1b4 ["CALL", null, ["callee:00bde040:8"]]
- 00aed0ec bytes a9c30394
+ 00aed1b4 bytes a3c30394
- 00aed0f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00aed0f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed1bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aed1bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed0f4 bytes 607604f9
+ 00aed1bc bytes 60d604f9
- 00aed0d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00aed0d4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed19c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aed19c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed0d4 bytes 687644f9
+ 00aed19c bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aed0f139268af75b0972530b7fb5075e"></a>

### [`00aed108`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed108.md) → [`00aed1d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed1d0.md) _ZN8firebase4util11short_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aed200",
      "incomplete_value": true,
      "site": "00aed200",
      "value": [
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
      "definition_site": "00aed138",
      "incomplete_value": true,
      "site": "00aed138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "00aed1e4",
      "incomplete_value": true,
      "site": "00aed1e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed11c",
      "incomplete_value": true,
      "site": "00aed11c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed1ec",
      "incomplete_value": false,
      "site": "00aed1f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:395:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed124",
      "incomplete_value": false,
      "site": "00aed130",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:429:8"
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
      "00aed1e0",
      "READ",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed1ec",
      "PARAM",
      [
        "storage",
        "002ae429",
        null,
        "string"
      ]
    ],
    [
      "00aed200",
      "WRITE",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed1e0",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed1ec",
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      "00aed200",
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

- 旧版 [`00aed130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed108.md#insn-00aed130) · [`00aed138`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed108.md#insn-00aed138) · [`00aed118`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed108.md#insn-00aed118)
- 新版 [`00aed1f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed1d0.md#insn-00aed1f8) · [`00aed200`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed1d0.md#insn-00aed200) · [`00aed1e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed1d0.md#insn-00aed1e0)

~~~diff
- 00aed130 ["INT_ADD", "register:40f0:8", ["const:aed130:8", "const:4:8"]]
- 00aed130 ["CALL", null, ["callee:00bde040:8"]]
+ 00aed1f8 ["INT_ADD", "register:40f0:8", ["const:aed1f8:8", "const:4:8"]]
+ 00aed1f8 ["CALL", null, ["callee:00bde040:8"]]
- 00aed130 bytes 98c30394
+ 00aed1f8 bytes 92c30394
- 00aed138 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00aed138 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed200 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aed200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed138 bytes 607604f9
+ 00aed200 bytes 60d604f9
- 00aed118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8e8:8"]]
- 00aed118 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed1e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
+ 00aed1e0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed118 bytes 687644f9
+ 00aed1e0 bytes 68d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-53b67efd5dc90dd24c7a533a615f3a3f"></a>

### [`00aed158`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed158.md) → [`00aed220`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed220.md) _ZN8firebase4util11short_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aed2a8",
      "incomplete_value": true,
      "site": "00aed2a8",
      "value": [
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
      "definition_site": "00aed1e0",
      "incomplete_value": true,
      "site": "00aed1e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "definition_site": "00aed254",
      "incomplete_value": true,
      "site": "00aed260",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "definition_site": "00aed18c",
      "incomplete_value": true,
      "site": "00aed198",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8e8:8"
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
      "00aed234",
      "READ",
      [
        "storage",
        "010a08f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed254",
      "READ",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed2a8",
      "WRITE",
      [
        "storage",
        "010a08f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aed234",
      "READ",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed254",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed2a8",
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

- 旧版 [`00aed198`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed158.md#insn-00aed198) · [`00aed1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed158.md#insn-00aed1e0) · [`00aed16c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed158.md#insn-00aed16c)
- 新版 [`00aed260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed220.md#insn-00aed260) · [`00aed2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed220.md#insn-00aed2a8) · [`00aed234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed220.md#insn-00aed234)

~~~diff
- 00aed198 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed198 ["INT_ADD", "register:40f0:8", ["const:aed198:8", "const:4:8"]]
- 00aed198 ["CALLIND", null, ["register:0:8"]]
+ 00aed260 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aed260 ["INT_ADD", "register:40f0:8", ["const:aed260:8", "const:4:8"]]
+ 00aed260 ["CALLIND", null, ["register:0:8"]]
- 00aed198 bytes 00013fd6
+ 00aed260 bytes 00013fd6
- 00aed1e0 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aed1e0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8f0:8"]]
- 00aed1e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aed2a8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aed2a8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9b0:8"]]
+ 00aed2a8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aed1e0 bytes a0c22339
+ 00aed2a8 bytes a0c22639
- 00aed16c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:8f0:8"]]
- 00aed16c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aed16c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aed234 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b0:8"]]
+ 00aed234 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aed234 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aed16c bytes a8c26339
+ 00aed234 bytes a8c26639
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37a9a1a2d4a442655e244554cfb52202"></a>

### [`00aed1f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed1f4.md) → [`00aed2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed2bc.md) _ZN8firebase4util11short_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aed2f8",
      "incomplete_value": true,
      "site": "00aed2f8",
      "value": [
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
      "definition_site": "00aed230",
      "incomplete_value": true,
      "site": "00aed230",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:8f0:8"
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
      "definition_site": "00aed348",
      "incomplete_value": true,
      "site": "00aed348",
      "value": [
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
      "definition_site": "00aed280",
      "incomplete_value": true,
      "site": "00aed280",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "00aed2d4",
      "incomplete_value": true,
      "site": "00aed2d4",
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
      "definition_site": "00aed20c",
      "incomplete_value": true,
      "site": "00aed20c",
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
      "00aed2d0",
      "READ",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed2dc",
      "READ",
      [
        "storage",
        "010a08f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed2f8",
      "WRITE",
      [
        "storage",
        "010a08f0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aed2d0",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed2dc",
      "READ",
      [
        "storage",
        "010a09b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed2f8",
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

- 旧版 [`00aed230`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed1f4.md#insn-00aed230) · [`00aed27c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed1f4.md#insn-00aed27c) · [`00aed280`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed1f4.md#insn-00aed280)
- 新版 [`00aed2f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed2bc.md#insn-00aed2f8) · [`00aed344`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed2bc.md#insn-00aed344) · [`00aed348`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed2bc.md#insn-00aed348)

~~~diff
- 00aed230 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aed230 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aed230 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8f0:8"]]
- 00aed230 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aed2f8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aed2f8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aed2f8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9b0:8"]]
+ 00aed2f8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aed230 bytes bfc22339
+ 00aed2f8 bytes bfc22639
- 00aed27c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed27c ["INT_ADD", "register:40f0:8", ["const:aed27c:8", "const:4:8"]]
- 00aed27c ["CALLIND", null, ["register:0:8"]]
+ 00aed344 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aed344 ["INT_ADD", "register:40f0:8", ["const:aed344:8", "const:4:8"]]
+ 00aed344 ["CALLIND", null, ["register:0:8"]]
- 00aed27c bytes 00013fd6
+ 00aed344 bytes 00013fd6
- 00aed280 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
- 00aed280 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aed280 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aed348 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00aed348 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aed348 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aed280 bytes 9f7604f9
+ 00aed348 bytes 9fd604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-51c5309a5adb9ad17a6534b925794cac"></a>

### [`00aed294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed294.md) → [`00aed35c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed35c.md) _ZN8firebase4util11short_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aed39c",
      "incomplete_value": true,
      "site": "00aed39c",
      "value": [
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
      "definition_site": "00aed2d4",
      "incomplete_value": true,
      "site": "00aed2d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "00aed378",
      "incomplete_value": true,
      "site": "00aed378",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed2b0",
      "incomplete_value": true,
      "site": "00aed2b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed380",
      "incomplete_value": false,
      "site": "00aed394",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:395:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed2b8",
      "incomplete_value": false,
      "site": "00aed2cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:429:8"
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
      "00aed370",
      "READ",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed380",
      "PARAM",
      [
        "storage",
        "002ae429",
        null,
        "string"
      ]
    ],
    [
      "00aed39c",
      "WRITE",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed370",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed380",
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      "00aed39c",
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

- 旧版 [`00aed2cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed294.md#insn-00aed2cc) · [`00aed2d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed294.md#insn-00aed2d4) · [`00aed2a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed294.md#insn-00aed2a8)
- 新版 [`00aed394`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed35c.md#insn-00aed394) · [`00aed39c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed35c.md#insn-00aed39c) · [`00aed370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed35c.md#insn-00aed370)

~~~diff
- 00aed2cc ["INT_ADD", "register:40f0:8", ["const:aed2cc:8", "const:4:8"]]
- 00aed2cc ["CALL", null, ["callee:00bde040:8"]]
+ 00aed394 ["INT_ADD", "register:40f0:8", ["const:aed394:8", "const:4:8"]]
+ 00aed394 ["CALL", null, ["callee:00bde040:8"]]
- 00aed2cc bytes 31c30394
+ 00aed394 bytes 2bc30394
- 00aed2d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
- 00aed2d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed39c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00aed39c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed2d4 bytes 807604f9
+ 00aed39c bytes 80d604f9
- 00aed2a8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
- 00aed2a8 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed370 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00aed370 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed2a8 bytes 817644f9
+ 00aed370 bytes 81d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-480a181fe84ae553a8ed231e5534d548"></a>

### [`00aed304`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed304.md) → [`00aed3cc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed3cc.md) _ZN8firebase4util11short_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00aed3e8",
      "incomplete_value": false,
      "site": "00aed3ec",
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
      "definition_site": "00aed320",
      "incomplete_value": false,
      "site": "00aed324",
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
      "definition_site": "00aed3f8",
      "incomplete_value": true,
      "site": "00aed404",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00aed330",
      "incomplete_value": true,
      "site": "00aed33c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aed3e8",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aed3f8",
      "DATA",
      [
        "storage",
        "010a08f8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aed3e8",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aed3f8",
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

- 旧版 [`00aed324`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed304.md#insn-00aed324) · [`00aed320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed304.md#insn-00aed320) · [`00aed32c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed304.md#insn-00aed32c)
- 新版 [`00aed3ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed3cc.md#insn-00aed3ec) · [`00aed3e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed3cc.md#insn-00aed3e8) · [`00aed3f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed3cc.md#insn-00aed3f4)

~~~diff
- 00aed324 ["INT_ADD", "register:40f0:8", ["const:aed324:8", "const:4:8"]]
- 00aed324 ["CALL", null, ["callee:00bde130:8"]]
+ 00aed3ec ["INT_ADD", "register:40f0:8", ["const:aed3ec:8", "const:4:8"]]
+ 00aed3ec ["CALL", null, ["callee:00bde130:8"]]
- 00aed324 bytes 57c30394
+ 00aed3ec bytes 51c30394
- 00aed320 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aed320 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed320 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed320 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aed3e8 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aed3e8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed3e8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed3e8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed320 bytes 001c1591
+ 00aed3e8 bytes 00501791
- 00aed32c ["COPY", "tmp:0:8", ["const:8f8:8"]]
- 00aed32c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aed32c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aed32c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aed3f4 ["COPY", "tmp:0:8", ["const:9b8:8"]]
+ 00aed3f4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed3f4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed3f4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aed32c bytes 08e12391
+ 00aed3f4 bytes 08e12691
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b3cfa6c3b7e1a08f9cce9c5fcf8d8e5"></a>

### [`00aed340`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed340.md) → [`00aed408`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed408.md) _ZN8firebase4util11short_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aed448",
      "incomplete_value": true,
      "site": "00aed448",
      "value": [
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
      "definition_site": "00aed380",
      "incomplete_value": true,
      "site": "00aed380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8e8:8"
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
      "definition_site": "00aed424",
      "incomplete_value": true,
      "site": "00aed424",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed35c",
      "incomplete_value": true,
      "site": "00aed35c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed42c",
      "incomplete_value": false,
      "site": "00aed440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:395:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed364",
      "incomplete_value": false,
      "site": "00aed378",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2ae000:8"
          ],
          [
            "leaf",
            "const:429:8"
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
      "00aed41c",
      "READ",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed42c",
      "PARAM",
      [
        "storage",
        "002ae429",
        null,
        "string"
      ]
    ],
    [
      "00aed448",
      "WRITE",
      [
        "storage",
        "010a08e8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed41c",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed42c",
      "PARAM",
      [
        "storage",
        "002ae395",
        null,
        "string"
      ]
    ],
    [
      "00aed448",
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

- 旧版 [`00aed378`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed340.md#insn-00aed378) · [`00aed380`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed340.md#insn-00aed380) · [`00aed354`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed340.md#insn-00aed354)
- 新版 [`00aed440`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed408.md#insn-00aed440) · [`00aed448`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed408.md#insn-00aed448) · [`00aed41c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed408.md#insn-00aed41c)

~~~diff
- 00aed378 ["INT_ADD", "register:40f0:8", ["const:aed378:8", "const:4:8"]]
- 00aed378 ["CALL", null, ["callee:00bde040:8"]]
+ 00aed440 ["INT_ADD", "register:40f0:8", ["const:aed440:8", "const:4:8"]]
+ 00aed440 ["CALL", null, ["callee:00bde040:8"]]
- 00aed378 bytes 06c30394
+ 00aed440 bytes 00c30394
- 00aed380 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
- 00aed380 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed448 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00aed448 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed380 bytes 807604f9
+ 00aed448 bytes 80d604f9
- 00aed354 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8e8:8"]]
- 00aed354 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed41c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
+ 00aed41c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed354 bytes 817644f9
+ 00aed41c bytes 81d644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6480afee77a009bcc2eff6fb4c5db562"></a>

### [`00aed3b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed3b0.md) → [`00aed478`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed478.md) _ZN8firebase4util11short_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aed494",
      "incomplete_value": false,
      "site": "00aed498",
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
      "definition_site": "00aed3cc",
      "incomplete_value": false,
      "site": "00aed3d0",
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
      "definition_site": "00aed4a4",
      "incomplete_value": true,
      "site": "00aed4b0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00aed3dc",
      "incomplete_value": true,
      "site": "00aed3e8",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aed494",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aed4a4",
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
      "00aed494",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aed4a4",
      "DATA",
      [
        "storage",
        "010a09c8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed3d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed3b0.md#insn-00aed3d0) · [`00aed3cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed3b0.md#insn-00aed3cc) · [`00aed3d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed3b0.md#insn-00aed3d8)
- 新版 [`00aed498`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed478.md#insn-00aed498) · [`00aed494`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed478.md#insn-00aed494) · [`00aed4a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed478.md#insn-00aed4a0)

~~~diff
- 00aed3d0 ["INT_ADD", "register:40f0:8", ["const:aed3d0:8", "const:4:8"]]
- 00aed3d0 ["CALL", null, ["callee:00bde130:8"]]
+ 00aed498 ["INT_ADD", "register:40f0:8", ["const:aed498:8", "const:4:8"]]
+ 00aed498 ["CALL", null, ["callee:00bde130:8"]]
- 00aed3d0 bytes 2cc30394
+ 00aed498 bytes 26c30394
- 00aed3cc ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aed3cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed3cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed3cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aed494 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00aed494 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed494 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed494 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed3cc bytes 00c81791
+ 00aed494 bytes 00fc1991
- 00aed3d8 ["COPY", "tmp:0:8", ["const:908:8"]]
- 00aed3d8 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aed3d8 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aed3d8 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aed4a0 ["COPY", "tmp:0:8", ["const:9c8:8"]]
+ 00aed4a0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed4a0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed4a0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aed3d8 bytes 08212491
+ 00aed4a0 bytes 08212791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7263ea936dbbcfde531044e0dafc6060"></a>

### [`00aed3ec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed3ec.md) → [`00aed4b4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4b4.md) _ZN8firebase4util6string19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
      "definition_site": "00aed4e0",
      "incomplete_value": true,
      "site": "00aed4e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed418",
      "incomplete_value": true,
      "site": "00aed418",
      "value": [
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
      "definition_site": "00aed4c8",
      "incomplete_value": true,
      "site": "00aed4c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed400",
      "incomplete_value": true,
      "site": "00aed400",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed4d4",
      "incomplete_value": false,
      "site": "00aed4d8",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed40c",
      "incomplete_value": false,
      "site": "00aed410",
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
            "const:5c3:8"
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
      "00aed4c4",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed4d4",
      "PARAM",
      [
        "storage",
        "0029e5c3",
        null,
        "string"
      ]
    ],
    [
      "00aed4e0",
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
      "00aed4c4",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed4d4",
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      "00aed4e0",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed410`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed3ec.md#insn-00aed410) · [`00aed418`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed3ec.md#insn-00aed418) · [`00aed3fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed3ec.md#insn-00aed3fc)
- 新版 [`00aed4d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4b4.md#insn-00aed4d8) · [`00aed4e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4b4.md#insn-00aed4e0) · [`00aed4c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4b4.md#insn-00aed4c4)

~~~diff
- 00aed410 ["INT_ADD", "register:40f0:8", ["const:aed410:8", "const:4:8"]]
- 00aed410 ["CALL", null, ["callee:00bde040:8"]]
+ 00aed4d8 ["INT_ADD", "register:40f0:8", ["const:aed4d8:8", "const:4:8"]]
+ 00aed4d8 ["CALL", null, ["callee:00bde040:8"]]
- 00aed410 bytes e0c20394
+ 00aed4d8 bytes dac20394
- 00aed418 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aed418 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed4e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00aed4e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed418 bytes 608a04f9
+ 00aed4e0 bytes 60ea04f9
- 00aed3fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aed3fc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed4c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00aed4c4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed3fc bytes 688a44f9
+ 00aed4c4 bytes 68ea44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e453c75d584ecc3909540c202acabaa"></a>

### [`00aed42c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed42c.md) → [`00aed4f4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4f4.md) _ZN8firebase4util6string19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aed520",
      "incomplete_value": true,
      "site": "00aed520",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed458",
      "incomplete_value": true,
      "site": "00aed458",
      "value": [
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
      "definition_site": "00aed508",
      "incomplete_value": true,
      "site": "00aed508",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed440",
      "incomplete_value": true,
      "site": "00aed440",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed510",
      "incomplete_value": false,
      "site": "00aed518",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed448",
      "incomplete_value": false,
      "site": "00aed450",
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
            "const:5c3:8"
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
      "00aed504",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed510",
      "PARAM",
      [
        "storage",
        "0029e5c3",
        null,
        "string"
      ]
    ],
    [
      "00aed520",
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
      "00aed504",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed510",
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      "00aed520",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed450`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed42c.md#insn-00aed450) · [`00aed458`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed42c.md#insn-00aed458) · [`00aed43c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed42c.md#insn-00aed43c)
- 新版 [`00aed518`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4f4.md#insn-00aed518) · [`00aed520`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4f4.md#insn-00aed520) · [`00aed504`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed4f4.md#insn-00aed504)

~~~diff
- 00aed450 ["INT_ADD", "register:40f0:8", ["const:aed450:8", "const:4:8"]]
- 00aed450 ["CALL", null, ["callee:00bde040:8"]]
+ 00aed518 ["INT_ADD", "register:40f0:8", ["const:aed518:8", "const:4:8"]]
+ 00aed518 ["CALL", null, ["callee:00bde040:8"]]
- 00aed450 bytes d0c20394
+ 00aed518 bytes cac20394
- 00aed458 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aed458 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed520 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00aed520 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed458 bytes 608a04f9
+ 00aed520 bytes 60ea04f9
- 00aed43c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aed43c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed504 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00aed504 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed43c bytes 688a44f9
+ 00aed504 bytes 68ea44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b759b5f74b94c7e9b27807f125cc576"></a>

### [`00aed46c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed46c.md) → [`00aed534`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed534.md) _ZN8firebase4util6string10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00aed564",
      "incomplete_value": true,
      "site": "00aed564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed49c",
      "incomplete_value": true,
      "site": "00aed49c",
      "value": [
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
      "definition_site": "00aed548",
      "incomplete_value": true,
      "site": "00aed548",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed480",
      "incomplete_value": true,
      "site": "00aed480",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed554",
      "incomplete_value": false,
      "site": "00aed55c",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed48c",
      "incomplete_value": false,
      "site": "00aed494",
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
            "const:5c3:8"
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
      "00aed544",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed554",
      "PARAM",
      [
        "storage",
        "0029e5c3",
        null,
        "string"
      ]
    ],
    [
      "00aed564",
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
      "00aed544",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed554",
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      "00aed564",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed494`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed46c.md#insn-00aed494) · [`00aed49c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed46c.md#insn-00aed49c) · [`00aed47c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed46c.md#insn-00aed47c)
- 新版 [`00aed55c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed534.md#insn-00aed55c) · [`00aed564`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed534.md#insn-00aed564) · [`00aed544`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed534.md#insn-00aed544)

~~~diff
- 00aed494 ["INT_ADD", "register:40f0:8", ["const:aed494:8", "const:4:8"]]
- 00aed494 ["CALL", null, ["callee:00bde040:8"]]
+ 00aed55c ["INT_ADD", "register:40f0:8", ["const:aed55c:8", "const:4:8"]]
+ 00aed55c ["CALL", null, ["callee:00bde040:8"]]
- 00aed494 bytes bfc20394
+ 00aed55c bytes b9c20394
- 00aed49c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aed49c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed564 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00aed564 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed49c bytes 608a04f9
+ 00aed564 bytes 60ea04f9
- 00aed47c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aed47c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed544 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00aed544 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed47c bytes 688a44f9
+ 00aed544 bytes 68ea44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d1021ef80ea4d12f355112716e73c012"></a>

### [`00aed4b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed4b0.md) → [`00aed578`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed578.md) _ZN8firebase4util6string10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aed5a8",
      "incomplete_value": true,
      "site": "00aed5a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed4e0",
      "incomplete_value": true,
      "site": "00aed4e0",
      "value": [
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
      "definition_site": "00aed58c",
      "incomplete_value": true,
      "site": "00aed58c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed4c4",
      "incomplete_value": true,
      "site": "00aed4c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed594",
      "incomplete_value": false,
      "site": "00aed5a0",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed4cc",
      "incomplete_value": false,
      "site": "00aed4d8",
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
            "const:5c3:8"
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
      "00aed588",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed594",
      "PARAM",
      [
        "storage",
        "0029e5c3",
        null,
        "string"
      ]
    ],
    [
      "00aed5a8",
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
      "00aed588",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed594",
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      "00aed5a8",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed4d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed4b0.md#insn-00aed4d8) · [`00aed4e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed4b0.md#insn-00aed4e0) · [`00aed4c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed4b0.md#insn-00aed4c0)
- 新版 [`00aed5a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed578.md#insn-00aed5a0) · [`00aed5a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed578.md#insn-00aed5a8) · [`00aed588`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed578.md#insn-00aed588)

~~~diff
- 00aed4d8 ["INT_ADD", "register:40f0:8", ["const:aed4d8:8", "const:4:8"]]
- 00aed4d8 ["CALL", null, ["callee:00bde040:8"]]
+ 00aed5a0 ["INT_ADD", "register:40f0:8", ["const:aed5a0:8", "const:4:8"]]
+ 00aed5a0 ["CALL", null, ["callee:00bde040:8"]]
- 00aed4d8 bytes aec20394
+ 00aed5a0 bytes a8c20394
- 00aed4e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aed4e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed5a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00aed5a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed4e0 bytes 608a04f9
+ 00aed5a8 bytes 60ea04f9
- 00aed4c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:910:8"]]
- 00aed4c0 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed588 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9d0:8"]]
+ 00aed588 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed4c0 bytes 688a44f9
+ 00aed588 bytes 68ea44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d504d165092745677a8b7544f8049295"></a>

### [`00aed500`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed500.md) → [`00aed5c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed5c8.md) _ZN8firebase4util6string15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aed650",
      "incomplete_value": true,
      "site": "00aed650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed588",
      "incomplete_value": true,
      "site": "00aed588",
      "value": [
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
      "definition_site": "00aed5fc",
      "incomplete_value": true,
      "site": "00aed608",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9d0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed534",
      "incomplete_value": true,
      "site": "00aed540",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00aed5dc",
      "READ",
      [
        "storage",
        "010a0918",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed5fc",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed650",
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
      "00aed5dc",
      "READ",
      [
        "storage",
        "010a09d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed5fc",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed650",
      "WRITE",
      [
        "storage",
        "010a09d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed500.md#insn-00aed540) · [`00aed588`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed500.md#insn-00aed588) · [`00aed514`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed500.md#insn-00aed514)
- 新版 [`00aed608`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed5c8.md#insn-00aed608) · [`00aed650`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed5c8.md#insn-00aed650) · [`00aed5dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed5c8.md#insn-00aed5dc)

~~~diff
- 00aed540 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed540 ["INT_ADD", "register:40f0:8", ["const:aed540:8", "const:4:8"]]
- 00aed540 ["CALLIND", null, ["register:0:8"]]
+ 00aed608 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aed608 ["INT_ADD", "register:40f0:8", ["const:aed608:8", "const:4:8"]]
+ 00aed608 ["CALLIND", null, ["register:0:8"]]
- 00aed540 bytes 00013fd6
+ 00aed608 bytes 00013fd6
- 00aed588 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aed588 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:918:8"]]
- 00aed588 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aed650 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aed650 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9d8:8"]]
+ 00aed650 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aed588 bytes a0622439
+ 00aed650 bytes a0622739
- 00aed514 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:918:8"]]
- 00aed514 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aed514 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aed5dc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9d8:8"]]
+ 00aed5dc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aed5dc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aed514 bytes a8626439
+ 00aed5dc bytes a8626739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-daa703dc8ae91fdd652d42f16f0e02c5"></a>

### [`00aed59c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed59c.md) → [`00aed664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed664.md) _ZN8firebase4util6string12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aed6a0",
      "incomplete_value": true,
      "site": "00aed6a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9d8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed5d8",
      "incomplete_value": true,
      "site": "00aed5d8",
      "value": [
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
      "definition_site": "00aed6f0",
      "incomplete_value": true,
      "site": "00aed6f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed628",
      "incomplete_value": true,
      "site": "00aed628",
      "value": [
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
      "definition_site": "00aed67c",
      "incomplete_value": true,
      "site": "00aed67c",
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
      "definition_site": "00aed5b4",
      "incomplete_value": true,
      "site": "00aed5b4",
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
      "00aed678",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed684",
      "READ",
      [
        "storage",
        "010a0918",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed6a0",
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
      "00aed678",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed684",
      "READ",
      [
        "storage",
        "010a09d8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed6a0",
      "WRITE",
      [
        "storage",
        "010a09d8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed5d8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed59c.md#insn-00aed5d8) · [`00aed624`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed59c.md#insn-00aed624) · [`00aed628`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed59c.md#insn-00aed628)
- 新版 [`00aed6a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed664.md#insn-00aed6a0) · [`00aed6ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed664.md#insn-00aed6ec) · [`00aed6f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed664.md#insn-00aed6f0)

~~~diff
- 00aed5d8 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aed5d8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aed5d8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:918:8"]]
- 00aed5d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aed6a0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aed6a0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aed6a0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9d8:8"]]
+ 00aed6a0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aed5d8 bytes bf622439
+ 00aed6a0 bytes bf622739
- 00aed624 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed624 ["INT_ADD", "register:40f0:8", ["const:aed624:8", "const:4:8"]]
- 00aed624 ["CALLIND", null, ["register:0:8"]]
+ 00aed6ec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aed6ec ["INT_ADD", "register:40f0:8", ["const:aed6ec:8", "const:4:8"]]
+ 00aed6ec ["CALLIND", null, ["register:0:8"]]
- 00aed624 bytes 00013fd6
+ 00aed6ec bytes 00013fd6
- 00aed628 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00aed628 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aed628 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aed6f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
+ 00aed6f0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aed6f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aed628 bytes 9f8a04f9
+ 00aed6f0 bytes 9fea04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e0b33a34290602f2d4a9a48fd96bbe7a"></a>

### [`00aed63c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed63c.md) → [`00aed704`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed704.md) _ZN8firebase4util6string14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aed744",
      "incomplete_value": true,
      "site": "00aed744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed67c",
      "incomplete_value": true,
      "site": "00aed67c",
      "value": [
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
      "definition_site": "00aed720",
      "incomplete_value": true,
      "site": "00aed720",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed658",
      "incomplete_value": true,
      "site": "00aed658",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed728",
      "incomplete_value": false,
      "site": "00aed73c",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed660",
      "incomplete_value": false,
      "site": "00aed674",
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
            "const:5c3:8"
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
      "00aed718",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed728",
      "PARAM",
      [
        "storage",
        "0029e5c3",
        null,
        "string"
      ]
    ],
    [
      "00aed744",
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
      "00aed718",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed728",
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      "00aed744",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed63c.md#insn-00aed674) · [`00aed67c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed63c.md#insn-00aed67c) · [`00aed650`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed63c.md#insn-00aed650)
- 新版 [`00aed73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed704.md#insn-00aed73c) · [`00aed744`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed704.md#insn-00aed744) · [`00aed718`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed704.md#insn-00aed718)

~~~diff
- 00aed674 ["INT_ADD", "register:40f0:8", ["const:aed674:8", "const:4:8"]]
- 00aed674 ["CALL", null, ["callee:00bde040:8"]]
+ 00aed73c ["INT_ADD", "register:40f0:8", ["const:aed73c:8", "const:4:8"]]
+ 00aed73c ["CALL", null, ["callee:00bde040:8"]]
- 00aed674 bytes 47c20394
+ 00aed73c bytes 41c20394
- 00aed67c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00aed67c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed744 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
+ 00aed744 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed67c bytes 808a04f9
+ 00aed744 bytes 80ea04f9
- 00aed650 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00aed650 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed718 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
+ 00aed718 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed650 bytes 818a44f9
+ 00aed718 bytes 81ea44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6276062d5ec4c4bf7d2f48bc85e02737"></a>

### [`00aed6ac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed6ac.md) → [`00aed774`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed774.md) _ZN8firebase4util6string11GetMethodIdENS1_6MethodE

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
      "definition_site": "00aed790",
      "incomplete_value": false,
      "site": "00aed794",
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
      "definition_site": "00aed6c8",
      "incomplete_value": false,
      "site": "00aed6cc",
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
      "definition_site": "00aed7a0",
      "incomplete_value": true,
      "site": "00aed7ac",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00aed6d8",
      "incomplete_value": true,
      "site": "00aed6e4",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aed790",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aed7a0",
      "DATA",
      [
        "storage",
        "010a0920",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aed790",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aed7a0",
      "DATA",
      [
        "storage",
        "010a09e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed6cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed6ac.md#insn-00aed6cc) · [`00aed6c8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed6ac.md#insn-00aed6c8) · [`00aed6d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed6ac.md#insn-00aed6d4)
- 新版 [`00aed794`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed774.md#insn-00aed794) · [`00aed790`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed774.md#insn-00aed790) · [`00aed79c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed774.md#insn-00aed79c)

~~~diff
- 00aed6cc ["INT_ADD", "register:40f0:8", ["const:aed6cc:8", "const:4:8"]]
- 00aed6cc ["CALL", null, ["callee:00bde130:8"]]
+ 00aed794 ["INT_ADD", "register:40f0:8", ["const:aed794:8", "const:4:8"]]
+ 00aed794 ["CALL", null, ["callee:00bde130:8"]]
- 00aed6cc bytes 6dc20394
+ 00aed794 bytes 67c20394
- 00aed6c8 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aed6c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed6c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed6c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aed790 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aed790 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed790 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed790 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed6c8 bytes 001c1591
+ 00aed790 bytes 00501791
- 00aed6d4 ["COPY", "tmp:0:8", ["const:920:8"]]
- 00aed6d4 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aed6d4 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aed6d4 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aed79c ["COPY", "tmp:0:8", ["const:9e0:8"]]
+ 00aed79c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed79c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed79c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aed6d4 bytes 08812491
+ 00aed79c bytes 08812791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a4543a71b02199894c79d3dc52a02300"></a>

### [`00aed6e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed6e8.md) → [`00aed7b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed7b0.md) _ZN8firebase4util6string13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aed7f0",
      "incomplete_value": true,
      "site": "00aed7f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed728",
      "incomplete_value": true,
      "site": "00aed728",
      "value": [
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
      "definition_site": "00aed7cc",
      "incomplete_value": true,
      "site": "00aed7cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed704",
      "incomplete_value": true,
      "site": "00aed704",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed7d4",
      "incomplete_value": false,
      "site": "00aed7e8",
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
            "const:650:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed70c",
      "incomplete_value": false,
      "site": "00aed720",
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
            "const:5c3:8"
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
      "00aed7c4",
      "READ",
      [
        "storage",
        "010a0910",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed7d4",
      "PARAM",
      [
        "storage",
        "0029e5c3",
        null,
        "string"
      ]
    ],
    [
      "00aed7f0",
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
      "00aed7c4",
      "READ",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed7d4",
      "PARAM",
      [
        "storage",
        "0029e650",
        null,
        "string"
      ]
    ],
    [
      "00aed7f0",
      "WRITE",
      [
        "storage",
        "010a09d0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed720`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed6e8.md#insn-00aed720) · [`00aed728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed6e8.md#insn-00aed728) · [`00aed6fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed6e8.md#insn-00aed6fc)
- 新版 [`00aed7e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed7b0.md#insn-00aed7e8) · [`00aed7f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed7b0.md#insn-00aed7f0) · [`00aed7c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed7b0.md#insn-00aed7c4)

~~~diff
- 00aed720 ["INT_ADD", "register:40f0:8", ["const:aed720:8", "const:4:8"]]
- 00aed720 ["CALL", null, ["callee:00bde040:8"]]
+ 00aed7e8 ["INT_ADD", "register:40f0:8", ["const:aed7e8:8", "const:4:8"]]
+ 00aed7e8 ["CALL", null, ["callee:00bde040:8"]]
- 00aed720 bytes 1cc20394
+ 00aed7e8 bytes 16c20394
- 00aed728 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00aed728 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed7f0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
+ 00aed7f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed728 bytes 808a04f9
+ 00aed7f0 bytes 80ea04f9
- 00aed6fc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:910:8"]]
- 00aed6fc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed7c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9d0:8"]]
+ 00aed7c4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed6fc bytes 818a44f9
+ 00aed7c4 bytes 81ea44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e9f741811f80d549127cdbf2ab28943"></a>

### [`00aed758`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed758.md) → [`00aed820`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed820.md) _ZN8firebase4util6string10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aed83c",
      "incomplete_value": false,
      "site": "00aed840",
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
      "definition_site": "00aed774",
      "incomplete_value": false,
      "site": "00aed778",
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
      "definition_site": "00aed84c",
      "incomplete_value": true,
      "site": "00aed858",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00aed784",
      "incomplete_value": true,
      "site": "00aed790",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aed83c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aed84c",
      "DATA",
      [
        "storage",
        "010a0928",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aed83c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aed84c",
      "DATA",
      [
        "storage",
        "010a09e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed778`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed758.md#insn-00aed778) · [`00aed774`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed758.md#insn-00aed774) · [`00aed780`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed758.md#insn-00aed780)
- 新版 [`00aed840`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed820.md#insn-00aed840) · [`00aed83c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed820.md#insn-00aed83c) · [`00aed848`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed820.md#insn-00aed848)

~~~diff
- 00aed778 ["INT_ADD", "register:40f0:8", ["const:aed778:8", "const:4:8"]]
- 00aed778 ["CALL", null, ["callee:00bde130:8"]]
+ 00aed840 ["INT_ADD", "register:40f0:8", ["const:aed840:8", "const:4:8"]]
+ 00aed840 ["CALL", null, ["callee:00bde130:8"]]
- 00aed778 bytes 42c20394
+ 00aed840 bytes 3cc20394
- 00aed774 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aed774 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aed774 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aed774 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aed83c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00aed83c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed83c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aed83c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aed774 bytes 00c81791
+ 00aed83c bytes 00fc1991
- 00aed780 ["COPY", "tmp:0:8", ["const:928:8"]]
- 00aed780 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aed780 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aed780 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aed848 ["COPY", "tmp:0:8", ["const:9e8:8"]]
+ 00aed848 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed848 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aed848 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aed780 bytes 08a12491
+ 00aed848 bytes 08a12791
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd7b66d230c6fc9828bbcf5d6128bf9d"></a>

### [`00aed794`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed794.md) → [`00aed85c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed85c.md) _ZN8firebase4util9throwable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0

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
      "definition_site": "00aed888",
      "incomplete_value": true,
      "site": "00aed888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed7c0",
      "incomplete_value": true,
      "site": "00aed7c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "definition_site": "00aed870",
      "incomplete_value": true,
      "site": "00aed870",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed7a8",
      "incomplete_value": true,
      "site": "00aed7a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed87c",
      "incomplete_value": false,
      "site": "00aed880",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed7b4",
      "incomplete_value": false,
      "site": "00aed7b8",
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
            "const:c9e:8"
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
      "00aed86c",
      "READ",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed87c",
      "PARAM",
      [
        "storage",
        "002a8c9e",
        null,
        "string"
      ]
    ],
    [
      "00aed888",
      "WRITE",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed86c",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed87c",
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      "00aed888",
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed7b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed794.md#insn-00aed7b8) · [`00aed7c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed794.md#insn-00aed7c0) · [`00aed7a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed794.md#insn-00aed7a4)
- 新版 [`00aed880`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed85c.md#insn-00aed880) · [`00aed888`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed85c.md#insn-00aed888) · [`00aed86c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed85c.md#insn-00aed86c)

~~~diff
- 00aed7b8 ["INT_ADD", "register:40f0:8", ["const:aed7b8:8", "const:4:8"]]
- 00aed7b8 ["CALL", null, ["callee:00bde040:8"]]
+ 00aed880 ["INT_ADD", "register:40f0:8", ["const:aed880:8", "const:4:8"]]
+ 00aed880 ["CALL", null, ["callee:00bde040:8"]]
- 00aed7b8 bytes f6c10394
+ 00aed880 bytes f0c10394
- 00aed7c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00aed7c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed888 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 00aed888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed7c0 bytes 609a04f9
+ 00aed888 bytes 60fa04f9
- 00aed7a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00aed7a4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed86c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 00aed86c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed7a4 bytes 689a44f9
+ 00aed86c bytes 68fa44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5004ef800686bb9aad2dd638851794de"></a>

### [`00aed7d4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed7d4.md) → [`00aed89c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed89c.md) _ZN8firebase4util9throwable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aed8c8",
      "incomplete_value": true,
      "site": "00aed8c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed800",
      "incomplete_value": true,
      "site": "00aed800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "definition_site": "00aed8b0",
      "incomplete_value": true,
      "site": "00aed8b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed7e8",
      "incomplete_value": true,
      "site": "00aed7e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed8b8",
      "incomplete_value": false,
      "site": "00aed8c0",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed7f0",
      "incomplete_value": false,
      "site": "00aed7f8",
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
            "const:c9e:8"
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
      "00aed8ac",
      "READ",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed8b8",
      "PARAM",
      [
        "storage",
        "002a8c9e",
        null,
        "string"
      ]
    ],
    [
      "00aed8c8",
      "WRITE",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed8ac",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed8b8",
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      "00aed8c8",
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed7f8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed7d4.md#insn-00aed7f8) · [`00aed800`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed7d4.md#insn-00aed800) · [`00aed7e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed7d4.md#insn-00aed7e4)
- 新版 [`00aed8c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed89c.md#insn-00aed8c0) · [`00aed8c8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed89c.md#insn-00aed8c8) · [`00aed8ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed89c.md#insn-00aed8ac)

~~~diff
- 00aed7f8 ["INT_ADD", "register:40f0:8", ["const:aed7f8:8", "const:4:8"]]
- 00aed7f8 ["CALL", null, ["callee:00bde040:8"]]
+ 00aed8c0 ["INT_ADD", "register:40f0:8", ["const:aed8c0:8", "const:4:8"]]
+ 00aed8c0 ["CALL", null, ["callee:00bde040:8"]]
- 00aed7f8 bytes e6c10394
+ 00aed8c0 bytes e0c10394
- 00aed800 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00aed800 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed8c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 00aed8c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed800 bytes 609a04f9
+ 00aed8c8 bytes 60fa04f9
- 00aed7e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00aed7e4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed8ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 00aed8ac ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed7e4 bytes 689a44f9
+ 00aed8ac bytes 68fa44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f8d804cb93e98fe68c87a0275076684"></a>

### [`00aed814`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed814.md) → [`00aed8dc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed8dc.md) _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00aed90c",
      "incomplete_value": true,
      "site": "00aed90c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed844",
      "incomplete_value": true,
      "site": "00aed844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "definition_site": "00aed8f0",
      "incomplete_value": true,
      "site": "00aed8f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed828",
      "incomplete_value": true,
      "site": "00aed828",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed8fc",
      "incomplete_value": false,
      "site": "00aed904",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed834",
      "incomplete_value": false,
      "site": "00aed83c",
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
            "const:c9e:8"
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
      "00aed8ec",
      "READ",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed8fc",
      "PARAM",
      [
        "storage",
        "002a8c9e",
        null,
        "string"
      ]
    ],
    [
      "00aed90c",
      "WRITE",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed8ec",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed8fc",
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      "00aed90c",
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed814.md#insn-00aed83c) · [`00aed844`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed814.md#insn-00aed844) · [`00aed824`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed814.md#insn-00aed824)
- 新版 [`00aed904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed8dc.md#insn-00aed904) · [`00aed90c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed8dc.md#insn-00aed90c) · [`00aed8ec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed8dc.md#insn-00aed8ec)

~~~diff
- 00aed83c ["INT_ADD", "register:40f0:8", ["const:aed83c:8", "const:4:8"]]
- 00aed83c ["CALL", null, ["callee:00bde040:8"]]
+ 00aed904 ["INT_ADD", "register:40f0:8", ["const:aed904:8", "const:4:8"]]
+ 00aed904 ["CALL", null, ["callee:00bde040:8"]]
- 00aed83c bytes d5c10394
+ 00aed904 bytes cfc10394
- 00aed844 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00aed844 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed90c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 00aed90c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed844 bytes 609a04f9
+ 00aed90c bytes 60fa04f9
- 00aed824 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00aed824 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed8ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 00aed8ec ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed824 bytes 689a44f9
+ 00aed8ec bytes 68fa44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9110c29e66b0f4818b0d827148da6ec9"></a>

### [`00aed858`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed858.md) → [`00aed920`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed920.md) _ZN8firebase4util9throwable10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aed950",
      "incomplete_value": true,
      "site": "00aed950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed888",
      "incomplete_value": true,
      "site": "00aed888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "definition_site": "00aed934",
      "incomplete_value": true,
      "site": "00aed934",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed86c",
      "incomplete_value": true,
      "site": "00aed86c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aed93c",
      "incomplete_value": false,
      "site": "00aed948",
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
            "const:c0a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed874",
      "incomplete_value": false,
      "site": "00aed880",
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
            "const:c9e:8"
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
      "00aed930",
      "READ",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed93c",
      "PARAM",
      [
        "storage",
        "002a8c9e",
        null,
        "string"
      ]
    ],
    [
      "00aed950",
      "WRITE",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aed930",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed93c",
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ],
    [
      "00aed950",
      "WRITE",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed880`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed858.md#insn-00aed880) · [`00aed888`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed858.md#insn-00aed888) · [`00aed868`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed858.md#insn-00aed868)
- 新版 [`00aed948`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed920.md#insn-00aed948) · [`00aed950`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed920.md#insn-00aed950) · [`00aed930`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed920.md#insn-00aed930)

~~~diff
- 00aed880 ["INT_ADD", "register:40f0:8", ["const:aed880:8", "const:4:8"]]
- 00aed880 ["CALL", null, ["callee:00bde040:8"]]
+ 00aed948 ["INT_ADD", "register:40f0:8", ["const:aed948:8", "const:4:8"]]
+ 00aed948 ["CALL", null, ["callee:00bde040:8"]]
- 00aed880 bytes c4c10394
+ 00aed948 bytes bec10394
- 00aed888 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00aed888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aed950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 00aed950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aed888 bytes 609a04f9
+ 00aed950 bytes 60fa04f9
- 00aed868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00aed868 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aed930 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 00aed930 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aed868 bytes 689a44f9
+ 00aed930 bytes 68fa44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c21bd2463ce557f095e64874be7d1346"></a>

### [`00aed8a8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed8a8.md) → [`00aed970`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed970.md) _ZN8firebase4util9throwable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aed9f8",
      "incomplete_value": true,
      "site": "00aed9f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed930",
      "incomplete_value": true,
      "site": "00aed930",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:938:8"
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
      "definition_site": "00aed9a4",
      "incomplete_value": true,
      "site": "00aed9b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed8dc",
      "incomplete_value": true,
      "site": "00aed8e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:930:8"
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
      "00aed984",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed9a4",
      "READ",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed9f8",
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aed984",
      "READ",
      [
        "storage",
        "010a09f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aed9a4",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aed9f8",
      "WRITE",
      [
        "storage",
        "010a09f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed8e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed8a8.md#insn-00aed8e8) · [`00aed930`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed8a8.md#insn-00aed930) · [`00aed8bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed8a8.md#insn-00aed8bc)
- 新版 [`00aed9b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed970.md#insn-00aed9b0) · [`00aed9f8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed970.md#insn-00aed9f8) · [`00aed984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aed970.md#insn-00aed984)

~~~diff
- 00aed8e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed8e8 ["INT_ADD", "register:40f0:8", ["const:aed8e8:8", "const:4:8"]]
- 00aed8e8 ["CALLIND", null, ["register:0:8"]]
+ 00aed9b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aed9b0 ["INT_ADD", "register:40f0:8", ["const:aed9b0:8", "const:4:8"]]
+ 00aed9b0 ["CALLIND", null, ["register:0:8"]]
- 00aed8e8 bytes 00013fd6
+ 00aed9b0 bytes 00013fd6
- 00aed930 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aed930 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:938:8"]]
- 00aed930 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aed9f8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aed9f8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9f8:8"]]
+ 00aed9f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aed930 bytes a0e22439
+ 00aed9f8 bytes a0e22739
- 00aed8bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:938:8"]]
- 00aed8bc ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aed8bc ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aed984 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9f8:8"]]
+ 00aed984 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aed984 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aed8bc bytes a8e26439
+ 00aed984 bytes a8e26739
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7b52054aca8f2f9638df0d6b4678ab2"></a>

### [`00aed944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed944.md) → [`00aeda0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeda0c.md) _ZN8firebase4util9throwable12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aeda48",
      "incomplete_value": true,
      "site": "00aeda48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed980",
      "incomplete_value": true,
      "site": "00aed980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:938:8"
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
      "definition_site": "00aeda98",
      "incomplete_value": true,
      "site": "00aeda98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aed9d0",
      "incomplete_value": true,
      "site": "00aed9d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:930:8"
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
      "definition_site": "00aeda24",
      "incomplete_value": true,
      "site": "00aeda24",
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
      "definition_site": "00aed95c",
      "incomplete_value": true,
      "site": "00aed95c",
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
      "00aeda20",
      "READ",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeda2c",
      "READ",
      [
        "storage",
        "010a0938",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeda48",
      "WRITE",
      [
        "storage",
        "010a0938",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeda20",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeda2c",
      "READ",
      [
        "storage",
        "010a09f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeda48",
      "WRITE",
      [
        "storage",
        "010a09f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed980`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed944.md#insn-00aed980) · [`00aed9cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed944.md#insn-00aed9cc) · [`00aed9d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed944.md#insn-00aed9d0)
- 新版 [`00aeda48`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeda0c.md#insn-00aeda48) · [`00aeda94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeda0c.md#insn-00aeda94) · [`00aeda98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeda0c.md#insn-00aeda98)

~~~diff
- 00aed980 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aed980 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aed980 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:938:8"]]
- 00aed980 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aeda48 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aeda48 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aeda48 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9f8:8"]]
+ 00aeda48 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aed980 bytes bfe22439
+ 00aeda48 bytes bfe22739
- 00aed9cc ["COPY", "register:0:8", ["register:4040:8"]]
- 00aed9cc ["INT_ADD", "register:40f0:8", ["const:aed9cc:8", "const:4:8"]]
- 00aed9cc ["CALLIND", null, ["register:0:8"]]
+ 00aeda94 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aeda94 ["INT_ADD", "register:40f0:8", ["const:aeda94:8", "const:4:8"]]
+ 00aeda94 ["CALLIND", null, ["register:0:8"]]
- 00aed9cc bytes 00013fd6
+ 00aeda94 bytes 00013fd6
- 00aed9d0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
- 00aed9d0 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aed9d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aeda98 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
+ 00aeda98 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aeda98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aed9d0 bytes 9f9a04f9
+ 00aeda98 bytes 9ffa04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d46a797210b2b2ffdaa927a8c36406b"></a>

### [`00aed9e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed9e4.md) → [`00aedaac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedaac.md) _ZN8firebase4util9throwable14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "site": "00aed9e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed9e4"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aed9e8"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aed9e4",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aed9e8",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "unmatched:00aed9f8",
      "READ",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedaac",
      "WRITE",
      [
        "storage",
        "Stack[-0x20]",
        null,
        null
      ]
    ],
    [
      "00aedab0",
      "WRITE",
      [
        "storage",
        "Stack[-0x10]",
        null,
        null
      ]
    ],
    [
      "00aedac0",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aed9e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed9e4.md#insn-00aed9e4) · [`00aed9e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed9e4.md#insn-00aed9e8) · [`00aeda00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed9e4.md#insn-00aeda00)

~~~diff
- 00aed9e4 ["COPY", "tmp:0:8", ["register:40a0:8"]]
- 00aed9e4 ["COPY", "tmp:1:8", ["register:4098:8"]]
- 00aed9e4 ["INT_ADD", "register:8:8", ["register:8:8", "const:ffffffffffffffe0:8"]]
- 00aed9e4 ["STORE", null, ["const:1b1:8", "register:8:8", "tmp:0:8"]]
- 00aed9e4 bytes f44fbea9
- 00aed9e8 ["COPY", "tmp:0:8", ["register:40e8:8"]]
- 00aed9e8 ["COPY", "tmp:1:8", ["register:40f0:8"]]
- 00aed9e8 ["INT_ADD", "tmp:2:8", ["register:8:8", "const:10:8"]]
- 00aed9e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00aed9e8 bytes fd7b01a9
- 00aeda00 ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aeda00 ["CBRANCH", null, ["local:b2:8", "tmp:0:1"]]
- 00aeda00 bytes 410100b5
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-602f535b8c9b57f17b84019a8dbfabf7"></a>

### [`00aeda54`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeda54.md) → [`00aedb1c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb1c.md) _ZN8firebase4util9throwable11GetMethodIdENS1_6MethodE

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
      "definition_site": "00aedb38",
      "incomplete_value": false,
      "site": "00aedb3c",
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
      "definition_site": "00aeda70",
      "incomplete_value": false,
      "site": "00aeda74",
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
      "definition_site": "00aedb48",
      "incomplete_value": true,
      "site": "00aedb54",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00aeda80",
      "incomplete_value": true,
      "site": "00aeda8c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aedb38",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aedb48",
      "DATA",
      [
        "storage",
        "010a0940",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedb38",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aedb48",
      "DATA",
      [
        "storage",
        "010a0a00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeda74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeda54.md#insn-00aeda74) · [`00aeda70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeda54.md#insn-00aeda70) · [`00aeda7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeda54.md#insn-00aeda7c)
- 新版 [`00aedb3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb1c.md#insn-00aedb3c) · [`00aedb38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb1c.md#insn-00aedb38) · [`00aedb44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb1c.md#insn-00aedb44)

~~~diff
- 00aeda74 ["INT_ADD", "register:40f0:8", ["const:aeda74:8", "const:4:8"]]
- 00aeda74 ["CALL", null, ["callee:00bde130:8"]]
+ 00aedb3c ["INT_ADD", "register:40f0:8", ["const:aedb3c:8", "const:4:8"]]
+ 00aedb3c ["CALL", null, ["callee:00bde130:8"]]
- 00aeda74 bytes 83c10394
+ 00aedb3c bytes 7dc10394
- 00aeda70 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aeda70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aeda70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aeda70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aedb38 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aedb38 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedb38 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedb38 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aeda70 bytes 001c1591
+ 00aedb38 bytes 00501791
- 00aeda7c ["COPY", "tmp:0:8", ["const:940:8"]]
- 00aeda7c ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeda7c ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeda7c ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aedb44 ["COPY", "tmp:0:8", ["const:a00:8"]]
+ 00aedb44 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedb44 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedb44 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeda7c bytes 08012591
+ 00aedb44 bytes 08012891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3062b5c20dc7b57582ee7a833c10129"></a>

### [`00aeda90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeda90.md) → [`00aedb58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb58.md) _ZN8firebase4util9throwable13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "site": "00aedad0"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": {
      "site": "00aedb98"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00aedaac"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00aedaa4",
      "READ",
      [
        "storage",
        "010a0930",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00aedaac",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aedb9c"
      ]
    ],
    [
      "unmatched:00aedab4",
      "PARAM",
      [
        "storage",
        "002a8c9e",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00aedb6c",
      "READ",
      [
        "storage",
        "010a09f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedb74",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aedb9c"
      ]
    ],
    [
      "00aedb7c",
      "PARAM",
      [
        "storage",
        "002a8c0a",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedaac`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeda90.md#insn-00aedaac) · [`00aedac8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeda90.md#insn-00aedac8) · [`00aedad0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeda90.md#insn-00aedad0)
- 新版 [`00aedb90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedb58.md#insn-00aedb90)

~~~diff
- 00aedaac ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00aedaac ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00aedaac bytes 410100b5
- 00aedac8 ["INT_ADD", "register:40f0:8", ["const:aedac8:8", "const:4:8"]]
- 00aedac8 ["CALL", null, ["callee:00bde040:8"]]
+ 00aedb90 ["INT_ADD", "register:40f0:8", ["const:aedb90:8", "const:4:8"]]
+ 00aedb90 ["CALL", null, ["callee:00bde040:8"]]
- 00aedac8 bytes 32c10394
+ 00aedb90 bytes 2cc10394
- 00aedad0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
- 00aedad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedad0 bytes 809a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a9a3e2aa5cd81d5f0d84e33c1652b01a"></a>

### [`00aedb00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb00.md) → [`00aedbc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedbc8.md) _ZN8firebase4util9throwable10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aedbe4",
      "incomplete_value": false,
      "site": "00aedbe8",
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
      "definition_site": "00aedb1c",
      "incomplete_value": false,
      "site": "00aedb20",
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
      "definition_site": "00aedbf4",
      "incomplete_value": true,
      "site": "00aedc00",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00aedb2c",
      "incomplete_value": true,
      "site": "00aedb38",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aedbe4",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aedbf4",
      "DATA",
      [
        "storage",
        "010a0958",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aedbe4",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aedbf4",
      "DATA",
      [
        "storage",
        "010a0a18",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedb20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb00.md#insn-00aedb20) · [`00aedb1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb00.md#insn-00aedb1c) · [`00aedb28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb00.md#insn-00aedb28)
- 新版 [`00aedbe8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedbc8.md#insn-00aedbe8) · [`00aedbe4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedbc8.md#insn-00aedbe4) · [`00aedbf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedbc8.md#insn-00aedbf0)

~~~diff
- 00aedb20 ["INT_ADD", "register:40f0:8", ["const:aedb20:8", "const:4:8"]]
- 00aedb20 ["CALL", null, ["callee:00bde130:8"]]
+ 00aedbe8 ["INT_ADD", "register:40f0:8", ["const:aedbe8:8", "const:4:8"]]
+ 00aedbe8 ["CALL", null, ["callee:00bde130:8"]]
- 00aedb20 bytes 58c10394
+ 00aedbe8 bytes 52c10394
- 00aedb1c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aedb1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aedb1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aedb1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aedbe4 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00aedbe4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedbe4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedbe4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aedb1c bytes 00c81791
+ 00aedbe4 bytes 00fc1991
- 00aedb28 ["COPY", "tmp:0:8", ["const:958:8"]]
- 00aedb28 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aedb28 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aedb28 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aedbf0 ["COPY", "tmp:0:8", ["const:a18:8"]]
+ 00aedbf0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedbf0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedbf0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aedb28 bytes 08612591
+ 00aedbf0 bytes 08612891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ad7cb106f015f603dc098ca4db999d43"></a>

### [`00aedb3c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb3c.md) → [`00aedc04`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc04.md) _ZN8firebase4util3uri19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
      "definition_site": "00aedc30",
      "incomplete_value": true,
      "site": "00aedc30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedb68",
      "incomplete_value": true,
      "site": "00aedb68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "definition_site": "00aedc18",
      "incomplete_value": true,
      "site": "00aedc18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedb50",
      "incomplete_value": true,
      "site": "00aedb50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aedc24",
      "incomplete_value": false,
      "site": "00aedc28",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedb5c",
      "incomplete_value": false,
      "site": "00aedb60",
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
            "const:4f8:8"
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
      "00aedc14",
      "READ",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedc24",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00aedc30",
      "WRITE",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedc14",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedc24",
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      "00aedc30",
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedb60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb3c.md#insn-00aedb60) · [`00aedb68`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb3c.md#insn-00aedb68) · [`00aedb4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb3c.md#insn-00aedb4c)
- 新版 [`00aedc28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc04.md#insn-00aedc28) · [`00aedc30`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc04.md#insn-00aedc30) · [`00aedc14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc04.md#insn-00aedc14)

~~~diff
- 00aedb60 ["INT_ADD", "register:40f0:8", ["const:aedb60:8", "const:4:8"]]
- 00aedb60 ["CALL", null, ["callee:00bde040:8"]]
+ 00aedc28 ["INT_ADD", "register:40f0:8", ["const:aedc28:8", "const:4:8"]]
+ 00aedc28 ["CALL", null, ["callee:00bde040:8"]]
- 00aedb60 bytes 0cc10394
+ 00aedc28 bytes 06c10394
- 00aedb68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00aedb68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aedc30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
+ 00aedc30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedb68 bytes 60b204f9
+ 00aedc30 bytes 601205f9
- 00aedb4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00aedb4c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedc14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
+ 00aedc14 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedb4c bytes 68b244f9
+ 00aedc14 bytes 681245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9da4ad1e589b66d5e3abb9d81c1a7ae4"></a>

### [`00aedb7c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb7c.md) → [`00aedc44`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc44.md) _ZN8firebase4util3uri19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aedc70",
      "incomplete_value": true,
      "site": "00aedc70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedba8",
      "incomplete_value": true,
      "site": "00aedba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "definition_site": "00aedc58",
      "incomplete_value": true,
      "site": "00aedc58",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedb90",
      "incomplete_value": true,
      "site": "00aedb90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aedc60",
      "incomplete_value": false,
      "site": "00aedc68",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedb98",
      "incomplete_value": false,
      "site": "00aedba0",
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
            "const:4f8:8"
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
      "00aedc54",
      "READ",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedc60",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00aedc70",
      "WRITE",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedc54",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedc60",
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      "00aedc70",
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedba0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb7c.md#insn-00aedba0) · [`00aedba8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb7c.md#insn-00aedba8) · [`00aedb8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedb7c.md#insn-00aedb8c)
- 新版 [`00aedc68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc44.md#insn-00aedc68) · [`00aedc70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc44.md#insn-00aedc70) · [`00aedc54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc44.md#insn-00aedc54)

~~~diff
- 00aedba0 ["INT_ADD", "register:40f0:8", ["const:aedba0:8", "const:4:8"]]
- 00aedba0 ["CALL", null, ["callee:00bde040:8"]]
+ 00aedc68 ["INT_ADD", "register:40f0:8", ["const:aedc68:8", "const:4:8"]]
+ 00aedc68 ["CALL", null, ["callee:00bde040:8"]]
- 00aedba0 bytes fcc00394
+ 00aedc68 bytes f6c00394
- 00aedba8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00aedba8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aedc70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
+ 00aedc70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedba8 bytes 60b204f9
+ 00aedc70 bytes 601205f9
- 00aedb8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00aedb8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedc54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
+ 00aedc54 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedb8c bytes 68b244f9
+ 00aedc54 bytes 681245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-50be6e852c3ed834e6d275e66109b14b"></a>

### [`00aedbbc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedbbc.md) → [`00aedc84`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc84.md) _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00aedcb4",
      "incomplete_value": true,
      "site": "00aedcb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedbec",
      "incomplete_value": true,
      "site": "00aedbec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "definition_site": "00aedc98",
      "incomplete_value": true,
      "site": "00aedc98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedbd0",
      "incomplete_value": true,
      "site": "00aedbd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aedca4",
      "incomplete_value": false,
      "site": "00aedcac",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedbdc",
      "incomplete_value": false,
      "site": "00aedbe4",
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
            "const:4f8:8"
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
      "00aedc94",
      "READ",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedca4",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00aedcb4",
      "WRITE",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedc94",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedca4",
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      "00aedcb4",
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedbe4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedbbc.md#insn-00aedbe4) · [`00aedbec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedbbc.md#insn-00aedbec) · [`00aedbcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedbbc.md#insn-00aedbcc)
- 新版 [`00aedcac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc84.md#insn-00aedcac) · [`00aedcb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc84.md#insn-00aedcb4) · [`00aedc94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedc84.md#insn-00aedc94)

~~~diff
- 00aedbe4 ["INT_ADD", "register:40f0:8", ["const:aedbe4:8", "const:4:8"]]
- 00aedbe4 ["CALL", null, ["callee:00bde040:8"]]
+ 00aedcac ["INT_ADD", "register:40f0:8", ["const:aedcac:8", "const:4:8"]]
+ 00aedcac ["CALL", null, ["callee:00bde040:8"]]
- 00aedbe4 bytes ebc00394
+ 00aedcac bytes e5c00394
- 00aedbec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00aedbec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aedcb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
+ 00aedcb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedbec bytes 60b204f9
+ 00aedcb4 bytes 601205f9
- 00aedbcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00aedbcc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedc94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
+ 00aedc94 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedbcc bytes 68b244f9
+ 00aedc94 bytes 681245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb5e3c8676600fc6fc26f55f980ced16"></a>

### [`00aedc00`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedc00.md) → [`00aedcc8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedcc8.md) _ZN8firebase4util3uri10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aedcf8",
      "incomplete_value": true,
      "site": "00aedcf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedc30",
      "incomplete_value": true,
      "site": "00aedc30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "definition_site": "00aedcdc",
      "incomplete_value": true,
      "site": "00aedcdc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedc14",
      "incomplete_value": true,
      "site": "00aedc14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aedce4",
      "incomplete_value": false,
      "site": "00aedcf0",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedc1c",
      "incomplete_value": false,
      "site": "00aedc28",
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
            "const:4f8:8"
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
      "00aedcd8",
      "READ",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedce4",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00aedcf8",
      "WRITE",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedcd8",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedce4",
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      "00aedcf8",
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedc28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedc00.md#insn-00aedc28) · [`00aedc30`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedc00.md#insn-00aedc30) · [`00aedc10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedc00.md#insn-00aedc10)
- 新版 [`00aedcf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedcc8.md#insn-00aedcf0) · [`00aedcf8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedcc8.md#insn-00aedcf8) · [`00aedcd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedcc8.md#insn-00aedcd8)

~~~diff
- 00aedc28 ["INT_ADD", "register:40f0:8", ["const:aedc28:8", "const:4:8"]]
- 00aedc28 ["CALL", null, ["callee:00bde040:8"]]
+ 00aedcf0 ["INT_ADD", "register:40f0:8", ["const:aedcf0:8", "const:4:8"]]
+ 00aedcf0 ["CALL", null, ["callee:00bde040:8"]]
- 00aedc28 bytes dac00394
+ 00aedcf0 bytes d4c00394
- 00aedc30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00aedc30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aedcf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
+ 00aedcf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedc30 bytes 60b204f9
+ 00aedcf8 bytes 601205f9
- 00aedc10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00aedc10 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedcd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a20:8"]]
+ 00aedcd8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedc10 bytes 68b244f9
+ 00aedcd8 bytes 681245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6595fb5eb7dae2ed191bb55b99b19a56"></a>

### [`00aedc50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedc50.md) → [`00aedd18`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedd18.md) _ZN8firebase4util3uri15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aedda0",
      "incomplete_value": true,
      "site": "00aedda0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedcd8",
      "incomplete_value": true,
      "site": "00aedcd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "definition_site": "00aedd4c",
      "incomplete_value": true,
      "site": "00aedd58",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a20:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedc84",
      "incomplete_value": true,
      "site": "00aedc90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:960:8"
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
      "00aedd2c",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined1"
      ]
    ],
    [
      "00aedd4c",
      "READ",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedda0",
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aedd2c",
      "READ",
      [
        "storage",
        "010a0a28",
        null,
        "undefined1"
      ]
    ],
    [
      "00aedd4c",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedda0",
      "WRITE",
      [
        "storage",
        "010a0a28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedc90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedc50.md#insn-00aedc90) · [`00aedcd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedc50.md#insn-00aedcd8) · [`00aedc64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedc50.md#insn-00aedc64)
- 新版 [`00aedd58`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedd18.md#insn-00aedd58) · [`00aedda0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedd18.md#insn-00aedda0) · [`00aedd2c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedd18.md#insn-00aedd2c)

~~~diff
- 00aedc90 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aedc90 ["INT_ADD", "register:40f0:8", ["const:aedc90:8", "const:4:8"]]
- 00aedc90 ["CALLIND", null, ["register:0:8"]]
+ 00aedd58 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aedd58 ["INT_ADD", "register:40f0:8", ["const:aedd58:8", "const:4:8"]]
+ 00aedd58 ["CALLIND", null, ["register:0:8"]]
- 00aedc90 bytes 00013fd6
+ 00aedd58 bytes 00013fd6
- 00aedcd8 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aedcd8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:968:8"]]
- 00aedcd8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aedda0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aedda0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a28:8"]]
+ 00aedda0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aedcd8 bytes a0a22539
+ 00aedda0 bytes a0a22839
- 00aedc64 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:968:8"]]
- 00aedc64 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aedc64 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aedd2c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a28:8"]]
+ 00aedd2c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aedd2c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aedc64 bytes a8a26539
+ 00aedd2c bytes a8a26839
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bfa90bc350ec7058078b725f4be187cb"></a>

### [`00aedcec`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedcec.md) → [`00aeddb4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeddb4.md) _ZN8firebase4util3uri12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aeddf0",
      "incomplete_value": true,
      "site": "00aeddf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedd28",
      "incomplete_value": true,
      "site": "00aedd28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:968:8"
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
      "definition_site": "00aede40",
      "incomplete_value": true,
      "site": "00aede40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedd78",
      "incomplete_value": true,
      "site": "00aedd78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "definition_site": "00aeddcc",
      "incomplete_value": true,
      "site": "00aeddcc",
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
      "definition_site": "00aedd04",
      "incomplete_value": true,
      "site": "00aedd04",
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
      "00aeddc8",
      "READ",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeddd4",
      "READ",
      [
        "storage",
        "010a0968",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeddf0",
      "WRITE",
      [
        "storage",
        "010a0968",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aeddc8",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aeddd4",
      "READ",
      [
        "storage",
        "010a0a28",
        null,
        "undefined1"
      ]
    ],
    [
      "00aeddf0",
      "WRITE",
      [
        "storage",
        "010a0a28",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedd28`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedcec.md#insn-00aedd28) · [`00aedd74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedcec.md#insn-00aedd74) · [`00aedd78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedcec.md#insn-00aedd78)
- 新版 [`00aeddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeddb4.md#insn-00aeddf0) · [`00aede3c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeddb4.md#insn-00aede3c) · [`00aede40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aeddb4.md#insn-00aede40)

~~~diff
- 00aedd28 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aedd28 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aedd28 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:968:8"]]
- 00aedd28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aeddf0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aeddf0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aeddf0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a28:8"]]
+ 00aeddf0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aedd28 bytes bfa22539
+ 00aeddf0 bytes bfa22839
- 00aedd74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aedd74 ["INT_ADD", "register:40f0:8", ["const:aedd74:8", "const:4:8"]]
- 00aedd74 ["CALLIND", null, ["register:0:8"]]
+ 00aede3c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aede3c ["INT_ADD", "register:40f0:8", ["const:aede3c:8", "const:4:8"]]
+ 00aede3c ["CALLIND", null, ["register:0:8"]]
- 00aedd74 bytes 00013fd6
+ 00aede3c bytes 00013fd6
- 00aedd78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
- 00aedd78 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aedd78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aede40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
+ 00aede40 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aede40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aedd78 bytes 9fb204f9
+ 00aede40 bytes 9f1205f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c908841d5655c268cfe605f2cfec33a5"></a>

### [`00aedd8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedd8c.md) → [`00aede54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aede54.md) _ZN8firebase4util3uri14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aede94",
      "incomplete_value": true,
      "site": "00aede94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeddcc",
      "incomplete_value": true,
      "site": "00aeddcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "definition_site": "00aede70",
      "incomplete_value": true,
      "site": "00aede70",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedda8",
      "incomplete_value": true,
      "site": "00aedda8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aede78",
      "incomplete_value": false,
      "site": "00aede8c",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aeddb0",
      "incomplete_value": false,
      "site": "00aeddc4",
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
            "const:4f8:8"
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
      "00aede68",
      "READ",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      "00aede78",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00aede94",
      "WRITE",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aede68",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aede78",
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      "00aede94",
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aeddc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedd8c.md#insn-00aeddc4) · [`00aeddcc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedd8c.md#insn-00aeddcc) · [`00aedda0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedd8c.md#insn-00aedda0)
- 新版 [`00aede8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aede54.md#insn-00aede8c) · [`00aede94`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aede54.md#insn-00aede94) · [`00aede68`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aede54.md#insn-00aede68)

~~~diff
- 00aeddc4 ["INT_ADD", "register:40f0:8", ["const:aeddc4:8", "const:4:8"]]
- 00aeddc4 ["CALL", null, ["callee:00bde040:8"]]
+ 00aede8c ["INT_ADD", "register:40f0:8", ["const:aede8c:8", "const:4:8"]]
+ 00aede8c ["CALL", null, ["callee:00bde040:8"]]
- 00aeddc4 bytes 73c00394
+ 00aede8c bytes 6dc00394
- 00aeddcc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
- 00aeddcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aede94 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
+ 00aede94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aeddcc bytes 80b204f9
+ 00aede94 bytes 801205f9
- 00aedda0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
- 00aedda0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aede68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
+ 00aede68 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedda0 bytes 81b244f9
+ 00aede68 bytes 811245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f8668906b56c56a240573331ddd8f769"></a>

### [`00aeddfc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeddfc.md) → [`00aedec4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedec4.md) _ZN8firebase4util3uri11GetMethodIdENS1_6MethodE

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
      "definition_site": "00aedee0",
      "incomplete_value": false,
      "site": "00aedee4",
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
      "definition_site": "00aede18",
      "incomplete_value": false,
      "site": "00aede1c",
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
      "definition_site": "00aedef0",
      "incomplete_value": true,
      "site": "00aedefc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00aede28",
      "incomplete_value": true,
      "site": "00aede34",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aedee0",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aedef0",
      "DATA",
      [
        "storage",
        "010a0970",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedee0",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aedef0",
      "DATA",
      [
        "storage",
        "010a0a30",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aede1c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeddfc.md#insn-00aede1c) · [`00aede18`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeddfc.md#insn-00aede18) · [`00aede24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aeddfc.md#insn-00aede24)
- 新版 [`00aedee4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedec4.md#insn-00aedee4) · [`00aedee0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedec4.md#insn-00aedee0) · [`00aedeec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedec4.md#insn-00aedeec)

~~~diff
- 00aede1c ["INT_ADD", "register:40f0:8", ["const:aede1c:8", "const:4:8"]]
- 00aede1c ["CALL", null, ["callee:00bde130:8"]]
+ 00aedee4 ["INT_ADD", "register:40f0:8", ["const:aedee4:8", "const:4:8"]]
+ 00aedee4 ["CALL", null, ["callee:00bde130:8"]]
- 00aede1c bytes 99c00394
+ 00aedee4 bytes 93c00394
- 00aede18 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aede18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aede18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aede18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aedee0 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aedee0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedee0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedee0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aede18 bytes 001c1591
+ 00aedee0 bytes 00501791
- 00aede24 ["COPY", "tmp:0:8", ["const:970:8"]]
- 00aede24 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aede24 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aede24 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aedeec ["COPY", "tmp:0:8", ["const:a30:8"]]
+ 00aedeec ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedeec ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedeec ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aede24 bytes 08c12591
+ 00aedeec bytes 08c12891
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2640ae53939c617716efaf544e80859"></a>

### [`00aede38`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aede38.md) → [`00aedf00`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf00.md) _ZN8firebase4util3uri13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aedf40",
      "incomplete_value": true,
      "site": "00aedf40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aede78",
      "incomplete_value": true,
      "site": "00aede78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:960:8"
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
      "definition_site": "00aedf1c",
      "incomplete_value": true,
      "site": "00aedf1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aede54",
      "incomplete_value": true,
      "site": "00aede54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aedf24",
      "incomplete_value": false,
      "site": "00aedf38",
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
            "const:585:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aede5c",
      "incomplete_value": false,
      "site": "00aede70",
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
            "const:4f8:8"
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
      "00aedf14",
      "READ",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedf24",
      "PARAM",
      [
        "storage",
        "002974f8",
        null,
        "string"
      ]
    ],
    [
      "00aedf40",
      "WRITE",
      [
        "storage",
        "010a0960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aedf14",
      "READ",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedf24",
      "PARAM",
      [
        "storage",
        "00297585",
        null,
        "string"
      ]
    ],
    [
      "00aedf40",
      "WRITE",
      [
        "storage",
        "010a0a20",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aede70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aede38.md#insn-00aede70) · [`00aede78`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aede38.md#insn-00aede78) · [`00aede4c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aede38.md#insn-00aede4c)
- 新版 [`00aedf38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf00.md#insn-00aedf38) · [`00aedf40`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf00.md#insn-00aedf40) · [`00aedf14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf00.md#insn-00aedf14)

~~~diff
- 00aede70 ["INT_ADD", "register:40f0:8", ["const:aede70:8", "const:4:8"]]
- 00aede70 ["CALL", null, ["callee:00bde040:8"]]
+ 00aedf38 ["INT_ADD", "register:40f0:8", ["const:aedf38:8", "const:4:8"]]
+ 00aedf38 ["CALL", null, ["callee:00bde040:8"]]
- 00aede70 bytes 48c00394
+ 00aedf38 bytes 42c00394
- 00aede78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
- 00aede78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aedf40 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
+ 00aedf40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aede78 bytes 80b204f9
+ 00aedf40 bytes 801205f9
- 00aede4c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
- 00aede4c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedf14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a20:8"]]
+ 00aedf14 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aede4c bytes 81b244f9
+ 00aedf14 bytes 811245f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e370122037222f675d0b33c4b328c326"></a>

### [`00aedea8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedea8.md) → [`00aedf70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf70.md) _ZN8firebase4util3uri10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aedf8c",
      "incomplete_value": false,
      "site": "00aedf90",
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
      "definition_site": "00aedec4",
      "incomplete_value": false,
      "site": "00aedec8",
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
      "definition_site": "00aedf9c",
      "incomplete_value": true,
      "site": "00aedfa8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00aeded4",
      "incomplete_value": true,
      "site": "00aedee0",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aedf8c",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aedf9c",
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
      "00aedf8c",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aedf9c",
      "DATA",
      [
        "storage",
        "010a0a40",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedec8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedea8.md#insn-00aedec8) · [`00aedec4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedea8.md#insn-00aedec4) · [`00aeded0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedea8.md#insn-00aeded0)
- 新版 [`00aedf90`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf70.md#insn-00aedf90) · [`00aedf8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf70.md#insn-00aedf8c) · [`00aedf98`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedf70.md#insn-00aedf98)

~~~diff
- 00aedec8 ["INT_ADD", "register:40f0:8", ["const:aedec8:8", "const:4:8"]]
- 00aedec8 ["CALL", null, ["callee:00bde130:8"]]
+ 00aedf90 ["INT_ADD", "register:40f0:8", ["const:aedf90:8", "const:4:8"]]
+ 00aedf90 ["CALL", null, ["callee:00bde130:8"]]
- 00aedec8 bytes 6ec00394
+ 00aedf90 bytes 68c00394
- 00aedec4 ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aedec4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aedec4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aedec4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aedf8c ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00aedf8c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedf8c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aedf8c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aedec4 bytes 00c81791
+ 00aedf8c bytes 00fc1991
- 00aeded0 ["COPY", "tmp:0:8", ["const:980:8"]]
- 00aeded0 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aeded0 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aeded0 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aedf98 ["COPY", "tmp:0:8", ["const:a40:8"]]
+ 00aedf98 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedf98 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aedf98 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aeded0 bytes 08012691
+ 00aedf98 bytes 08012991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4112494e9d2ac7dc951273a9cfaa6601"></a>

### [`00aedee4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedee4.md) → [`00aedfac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfac.md) _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
      "definition_site": "00aedfd8",
      "incomplete_value": true,
      "site": "00aedfd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedf10",
      "incomplete_value": true,
      "site": "00aedf10",
      "value": [
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
      "definition_site": "00aedfc0",
      "incomplete_value": true,
      "site": "00aedfc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedef8",
      "incomplete_value": true,
      "site": "00aedef8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aedfcc",
      "incomplete_value": false,
      "site": "00aedfd0",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedf04",
      "incomplete_value": false,
      "site": "00aedf08",
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
            "const:cdf:8"
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
      "00aedfbc",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedfcc",
      "PARAM",
      [
        "storage",
        "0029dcdf",
        null,
        "string"
      ]
    ],
    [
      "00aedfd8",
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
      "00aedfbc",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aedfcc",
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      "00aedfd8",
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedf08`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedee4.md#insn-00aedf08) · [`00aedf10`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedee4.md#insn-00aedf10) · [`00aedef4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedee4.md#insn-00aedef4)
- 新版 [`00aedfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfac.md#insn-00aedfd0) · [`00aedfd8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfac.md#insn-00aedfd8) · [`00aedfbc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfac.md#insn-00aedfbc)

~~~diff
- 00aedf08 ["INT_ADD", "register:40f0:8", ["const:aedf08:8", "const:4:8"]]
- 00aedf08 ["CALL", null, ["callee:00bde040:8"]]
+ 00aedfd0 ["INT_ADD", "register:40f0:8", ["const:aedfd0:8", "const:4:8"]]
+ 00aedfd0 ["CALL", null, ["callee:00bde040:8"]]
- 00aedf08 bytes 22c00394
+ 00aedfd0 bytes 1cc00394
- 00aedf10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aedf10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aedfd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00aedfd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedf10 bytes 60c604f9
+ 00aedfd8 bytes 602605f9
- 00aedef4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aedef4 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedfbc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00aedfbc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedef4 bytes 68c644f9
+ 00aedfbc bytes 682645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dbea1896b652210580c99556e10fbcbe"></a>

### [`00aedf24`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedf24.md) → [`00aedfec`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfec.md) _ZN8firebase4util6object19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00aee018",
      "incomplete_value": true,
      "site": "00aee018",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedf50",
      "incomplete_value": true,
      "site": "00aedf50",
      "value": [
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
      "definition_site": "00aee000",
      "incomplete_value": true,
      "site": "00aee000",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedf38",
      "incomplete_value": true,
      "site": "00aedf38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aee008",
      "incomplete_value": false,
      "site": "00aee010",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedf40",
      "incomplete_value": false,
      "site": "00aedf48",
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
            "const:cdf:8"
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
      "00aedffc",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee008",
      "PARAM",
      [
        "storage",
        "0029dcdf",
        null,
        "string"
      ]
    ],
    [
      "00aee018",
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
      "00aedffc",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee008",
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      "00aee018",
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedf48`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedf24.md#insn-00aedf48) · [`00aedf50`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedf24.md#insn-00aedf50) · [`00aedf34`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedf24.md#insn-00aedf34)
- 新版 [`00aee010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfec.md#insn-00aee010) · [`00aee018`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfec.md#insn-00aee018) · [`00aedffc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aed/00aedfec.md#insn-00aedffc)

~~~diff
- 00aedf48 ["INT_ADD", "register:40f0:8", ["const:aedf48:8", "const:4:8"]]
- 00aedf48 ["CALL", null, ["callee:00bde040:8"]]
+ 00aee010 ["INT_ADD", "register:40f0:8", ["const:aee010:8", "const:4:8"]]
+ 00aee010 ["CALL", null, ["callee:00bde040:8"]]
- 00aedf48 bytes 12c00394
+ 00aee010 bytes 0cc00394
- 00aedf50 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aedf50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aee018 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00aee018 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedf50 bytes 60c604f9
+ 00aee018 bytes 602605f9
- 00aedf34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aedf34 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aedffc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00aedffc ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedf34 bytes 68c644f9
+ 00aedffc bytes 682645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ac739176891d96ecd7013b0615063cd2"></a>

### [`00aedf64`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedf64.md) → [`00aee02c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee02c.md) _ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00aee05c",
      "incomplete_value": true,
      "site": "00aee05c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedf94",
      "incomplete_value": true,
      "site": "00aedf94",
      "value": [
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
      "definition_site": "00aee040",
      "incomplete_value": true,
      "site": "00aee040",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedf78",
      "incomplete_value": true,
      "site": "00aedf78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aee04c",
      "incomplete_value": false,
      "site": "00aee054",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedf84",
      "incomplete_value": false,
      "site": "00aedf8c",
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
            "const:cdf:8"
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
      "00aee03c",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee04c",
      "PARAM",
      [
        "storage",
        "0029dcdf",
        null,
        "string"
      ]
    ],
    [
      "00aee05c",
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
      "00aee03c",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee04c",
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      "00aee05c",
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedf8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedf64.md#insn-00aedf8c) · [`00aedf94`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedf64.md#insn-00aedf94) · [`00aedf74`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedf64.md#insn-00aedf74)
- 新版 [`00aee054`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee02c.md#insn-00aee054) · [`00aee05c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee02c.md#insn-00aee05c) · [`00aee03c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee02c.md#insn-00aee03c)

~~~diff
- 00aedf8c ["INT_ADD", "register:40f0:8", ["const:aedf8c:8", "const:4:8"]]
- 00aedf8c ["CALL", null, ["callee:00bde040:8"]]
+ 00aee054 ["INT_ADD", "register:40f0:8", ["const:aee054:8", "const:4:8"]]
+ 00aee054 ["CALL", null, ["callee:00bde040:8"]]
- 00aedf8c bytes 01c00394
+ 00aee054 bytes fbbf0394
- 00aedf94 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aedf94 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aee05c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00aee05c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedf94 bytes 60c604f9
+ 00aee05c bytes 602605f9
- 00aedf74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aedf74 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aee03c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00aee03c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedf74 bytes 68c644f9
+ 00aee03c bytes 682645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d4414fad330da9bc395e61bc850eeff"></a>

### [`00aedfa8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedfa8.md) → [`00aee070`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee070.md) _ZN8firebase4util6object10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00aee0a0",
      "incomplete_value": true,
      "site": "00aee0a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedfd8",
      "incomplete_value": true,
      "site": "00aedfd8",
      "value": [
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
      "definition_site": "00aee084",
      "incomplete_value": true,
      "site": "00aee084",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedfbc",
      "incomplete_value": true,
      "site": "00aedfbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aee08c",
      "incomplete_value": false,
      "site": "00aee098",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aedfc4",
      "incomplete_value": false,
      "site": "00aedfd0",
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
            "const:cdf:8"
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
      "00aee080",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee08c",
      "PARAM",
      [
        "storage",
        "0029dcdf",
        null,
        "string"
      ]
    ],
    [
      "00aee0a0",
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
      "00aee080",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee08c",
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      "00aee0a0",
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aedfd0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedfa8.md#insn-00aedfd0) · [`00aedfd8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedfa8.md#insn-00aedfd8) · [`00aedfb8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedfa8.md#insn-00aedfb8)
- 新版 [`00aee098`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee070.md#insn-00aee098) · [`00aee0a0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee070.md#insn-00aee0a0) · [`00aee080`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee070.md#insn-00aee080)

~~~diff
- 00aedfd0 ["INT_ADD", "register:40f0:8", ["const:aedfd0:8", "const:4:8"]]
- 00aedfd0 ["CALL", null, ["callee:00bde040:8"]]
+ 00aee098 ["INT_ADD", "register:40f0:8", ["const:aee098:8", "const:4:8"]]
+ 00aee098 ["CALL", null, ["callee:00bde040:8"]]
- 00aedfd0 bytes f0bf0394
+ 00aee098 bytes eabf0394
- 00aedfd8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aedfd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aee0a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00aee0a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aedfd8 bytes 60c604f9
+ 00aee0a0 bytes 602605f9
- 00aedfb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:988:8"]]
- 00aedfb8 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aee080 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a48:8"]]
+ 00aee080 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00aedfb8 bytes 68c644f9
+ 00aee080 bytes 682645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fd4164daef4b6ab9629c7cbc01cd1795"></a>

### [`00aedff8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedff8.md) → [`00aee0c0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee0c0.md) _ZN8firebase4util6object15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aee148",
      "incomplete_value": true,
      "site": "00aee148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee080",
      "incomplete_value": true,
      "site": "00aee080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "definition_site": "00aee0f4",
      "incomplete_value": true,
      "site": "00aee100",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee02c",
      "incomplete_value": true,
      "site": "00aee038",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:988:8"
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
      "00aee0d4",
      "READ",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ],
    [
      "00aee0f4",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee148",
      "WRITE",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aee0d4",
      "READ",
      [
        "storage",
        "010a0a50",
        null,
        "undefined1"
      ]
    ],
    [
      "00aee0f4",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee148",
      "WRITE",
      [
        "storage",
        "010a0a50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee038`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedff8.md#insn-00aee038) · [`00aee080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedff8.md#insn-00aee080) · [`00aee00c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aedff8.md#insn-00aee00c)
- 新版 [`00aee100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee0c0.md#insn-00aee100) · [`00aee148`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee0c0.md#insn-00aee148) · [`00aee0d4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee0c0.md#insn-00aee0d4)

~~~diff
- 00aee038 ["COPY", "register:0:8", ["register:4040:8"]]
- 00aee038 ["INT_ADD", "register:40f0:8", ["const:aee038:8", "const:4:8"]]
- 00aee038 ["CALLIND", null, ["register:0:8"]]
+ 00aee100 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aee100 ["INT_ADD", "register:40f0:8", ["const:aee100:8", "const:4:8"]]
+ 00aee100 ["CALLIND", null, ["register:0:8"]]
- 00aee038 bytes 00013fd6
+ 00aee100 bytes 00013fd6
- 00aee080 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00aee080 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:990:8"]]
- 00aee080 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00aee148 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00aee148 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a50:8"]]
+ 00aee148 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00aee080 bytes a0422639
+ 00aee148 bytes a0422939
- 00aee00c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:990:8"]]
- 00aee00c ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
- 00aee00c ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
+ 00aee0d4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a50:8"]]
+ 00aee0d4 ["LOAD", "tmp:1:1", ["const:1b1:8", "tmp:0:8"]]
+ 00aee0d4 ["INT_ZEXT", "register:4040:8", ["tmp:1:1"]]
- 00aee00c bytes a8426639
+ 00aee0d4 bytes a8426939
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98a6d8be418ed2b08a9be6e85e8a0d60"></a>

### [`00aee094`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee094.md) → [`00aee15c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee15c.md) _ZN8firebase4util6object12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00aee198",
      "incomplete_value": true,
      "site": "00aee198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee0d0",
      "incomplete_value": true,
      "site": "00aee0d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:990:8"
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
      "definition_site": "00aee1e8",
      "incomplete_value": true,
      "site": "00aee1e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee120",
      "incomplete_value": true,
      "site": "00aee120",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:988:8"
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
      "definition_site": "00aee174",
      "incomplete_value": true,
      "site": "00aee174",
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
      "definition_site": "00aee0ac",
      "incomplete_value": true,
      "site": "00aee0ac",
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
      "00aee170",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee17c",
      "READ",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ],
    [
      "00aee198",
      "WRITE",
      [
        "storage",
        "010a0990",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aee170",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee17c",
      "READ",
      [
        "storage",
        "010a0a50",
        null,
        "undefined1"
      ]
    ],
    [
      "00aee198",
      "WRITE",
      [
        "storage",
        "010a0a50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee0d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee094.md#insn-00aee0d0) · [`00aee11c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee094.md#insn-00aee11c) · [`00aee120`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee094.md#insn-00aee120)
- 新版 [`00aee198`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee15c.md#insn-00aee198) · [`00aee1e4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee15c.md#insn-00aee1e4) · [`00aee1e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee15c.md#insn-00aee1e8)

~~~diff
- 00aee0d0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aee0d0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aee0d0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:990:8"]]
- 00aee0d0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aee198 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aee198 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aee198 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a50:8"]]
+ 00aee198 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aee0d0 bytes bf422639
+ 00aee198 bytes bf422939
- 00aee11c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aee11c ["INT_ADD", "register:40f0:8", ["const:aee11c:8", "const:4:8"]]
- 00aee11c ["CALLIND", null, ["register:0:8"]]
+ 00aee1e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aee1e4 ["INT_ADD", "register:40f0:8", ["const:aee1e4:8", "const:4:8"]]
+ 00aee1e4 ["CALLIND", null, ["register:0:8"]]
- 00aee11c bytes 00013fd6
+ 00aee1e4 bytes 00013fd6
- 00aee120 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00aee120 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aee120 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aee1e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
+ 00aee1e8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aee1e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aee120 bytes 9fc604f9
+ 00aee1e8 bytes 9f2605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-767807b94f1c0ca301554d204598f45d"></a>

### [`00aee134`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee134.md) → [`00aee1fc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee1fc.md) _ZN8firebase4util6object14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aee23c",
      "incomplete_value": true,
      "site": "00aee23c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee174",
      "incomplete_value": true,
      "site": "00aee174",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:988:8"
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
      "definition_site": "00aee218",
      "incomplete_value": true,
      "site": "00aee218",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee150",
      "incomplete_value": true,
      "site": "00aee150",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aee220",
      "incomplete_value": false,
      "site": "00aee234",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee158",
      "incomplete_value": false,
      "site": "00aee16c",
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
            "const:cdf:8"
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
      "00aee210",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee220",
      "PARAM",
      [
        "storage",
        "0029dcdf",
        null,
        "string"
      ]
    ],
    [
      "00aee23c",
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
      "00aee210",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee220",
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      "00aee23c",
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee16c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee134.md#insn-00aee16c) · [`00aee174`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee134.md#insn-00aee174) · [`00aee148`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee134.md#insn-00aee148)
- 新版 [`00aee234`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee1fc.md#insn-00aee234) · [`00aee23c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee1fc.md#insn-00aee23c) · [`00aee210`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee1fc.md#insn-00aee210)

~~~diff
- 00aee16c ["INT_ADD", "register:40f0:8", ["const:aee16c:8", "const:4:8"]]
- 00aee16c ["CALL", null, ["callee:00bde040:8"]]
+ 00aee234 ["INT_ADD", "register:40f0:8", ["const:aee234:8", "const:4:8"]]
+ 00aee234 ["CALL", null, ["callee:00bde040:8"]]
- 00aee16c bytes 89bf0394
+ 00aee234 bytes 83bf0394
- 00aee174 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00aee174 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aee23c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
+ 00aee23c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee174 bytes 80c604f9
+ 00aee23c bytes 802605f9
- 00aee148 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00aee148 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aee210 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
+ 00aee210 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aee148 bytes 81c644f9
+ 00aee210 bytes 812645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c1aaaee91fdc836f4c94ed733cd91ef9"></a>

### [`00aee1a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee1a4.md) → [`00aee26c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee26c.md) _ZN8firebase4util6object11GetMethodIdENS1_6MethodE

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
      "definition_site": "00aee288",
      "incomplete_value": false,
      "site": "00aee28c",
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
      "definition_site": "00aee1c0",
      "incomplete_value": false,
      "site": "00aee1c4",
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
      "definition_site": "00aee298",
      "incomplete_value": true,
      "site": "00aee2a4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00aee1d0",
      "incomplete_value": true,
      "site": "00aee1dc",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aee288",
      "PARAM",
      [
        "storage",
        "00298547",
        null,
        "string"
      ]
    ],
    [
      "00aee298",
      "DATA",
      [
        "storage",
        "010a0998",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aee288",
      "PARAM",
      [
        "storage",
        "002985d4",
        null,
        "string"
      ]
    ],
    [
      "00aee298",
      "DATA",
      [
        "storage",
        "010a0a58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee1c4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee1a4.md#insn-00aee1c4) · [`00aee1c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee1a4.md#insn-00aee1c0) · [`00aee1cc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee1a4.md#insn-00aee1cc)
- 新版 [`00aee28c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee26c.md#insn-00aee28c) · [`00aee288`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee26c.md#insn-00aee288) · [`00aee294`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee26c.md#insn-00aee294)

~~~diff
- 00aee1c4 ["INT_ADD", "register:40f0:8", ["const:aee1c4:8", "const:4:8"]]
- 00aee1c4 ["CALL", null, ["callee:00bde130:8"]]
+ 00aee28c ["INT_ADD", "register:40f0:8", ["const:aee28c:8", "const:4:8"]]
+ 00aee28c ["CALL", null, ["callee:00bde130:8"]]
- 00aee1c4 bytes afbf0394
+ 00aee28c bytes a9bf0394
- 00aee1c0 ["COPY", "tmp:0:8", ["const:547:8"]]
- 00aee1c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aee1c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aee1c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aee288 ["COPY", "tmp:0:8", ["const:5d4:8"]]
+ 00aee288 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aee288 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aee288 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aee1c0 bytes 001c1591
+ 00aee288 bytes 00501791
- 00aee1cc ["COPY", "tmp:0:8", ["const:998:8"]]
- 00aee1cc ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aee1cc ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aee1cc ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aee294 ["COPY", "tmp:0:8", ["const:a58:8"]]
+ 00aee294 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aee294 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aee294 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aee1cc bytes 08612691
+ 00aee294 bytes 08612991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d00e121df1f69927a07c7960bc1aaf5b"></a>

### [`00aee1e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee1e0.md) → [`00aee2a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee2a8.md) _ZN8firebase4util6object13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00aee2e8",
      "incomplete_value": true,
      "site": "00aee2e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee220",
      "incomplete_value": true,
      "site": "00aee220",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:988:8"
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
      "definition_site": "00aee2c4",
      "incomplete_value": true,
      "site": "00aee2c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee1fc",
      "incomplete_value": true,
      "site": "00aee1fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00aee2cc",
      "incomplete_value": false,
      "site": "00aee2e0",
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
            "const:d6c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee204",
      "incomplete_value": false,
      "site": "00aee218",
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
            "const:cdf:8"
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
      "00aee2bc",
      "READ",
      [
        "storage",
        "010a0988",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee2cc",
      "PARAM",
      [
        "storage",
        "0029dcdf",
        null,
        "string"
      ]
    ],
    [
      "00aee2e8",
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
      "00aee2bc",
      "READ",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee2cc",
      "PARAM",
      [
        "storage",
        "0029dd6c",
        null,
        "string"
      ]
    ],
    [
      "00aee2e8",
      "WRITE",
      [
        "storage",
        "010a0a48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee218`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee1e0.md#insn-00aee218) · [`00aee220`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee1e0.md#insn-00aee220) · [`00aee1f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee1e0.md#insn-00aee1f4)
- 新版 [`00aee2e0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee2a8.md#insn-00aee2e0) · [`00aee2e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee2a8.md#insn-00aee2e8) · [`00aee2bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee2a8.md#insn-00aee2bc)

~~~diff
- 00aee218 ["INT_ADD", "register:40f0:8", ["const:aee218:8", "const:4:8"]]
- 00aee218 ["CALL", null, ["callee:00bde040:8"]]
+ 00aee2e0 ["INT_ADD", "register:40f0:8", ["const:aee2e0:8", "const:4:8"]]
+ 00aee2e0 ["CALL", null, ["callee:00bde040:8"]]
- 00aee218 bytes 5ebf0394
+ 00aee2e0 bytes 58bf0394
- 00aee220 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00aee220 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00aee2e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
+ 00aee2e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee220 bytes 80c604f9
+ 00aee2e8 bytes 802605f9
- 00aee1f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:988:8"]]
- 00aee1f4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aee2bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a48:8"]]
+ 00aee2bc ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00aee1f4 bytes 81c644f9
+ 00aee2bc bytes 812645f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39c43a46a460fb9b197a018839ad4087"></a>

### [`00aee250`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee250.md) → [`00aee318`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee318.md) _ZN8firebase4util6object10GetFieldIdENS1_5FieldE

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
      "definition_site": "00aee334",
      "incomplete_value": false,
      "site": "00aee338",
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
      "definition_site": "00aee26c",
      "incomplete_value": false,
      "site": "00aee270",
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
      "definition_site": "00aee344",
      "incomplete_value": true,
      "site": "00aee350",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00aee27c",
      "incomplete_value": true,
      "site": "00aee288",
      "value": [
        "LOAD",
        "8",
        [
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
      "00aee334",
      "PARAM",
      [
        "storage",
        "002995f2",
        null,
        "string"
      ]
    ],
    [
      "00aee344",
      "DATA",
      [
        "storage",
        "010a09a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00aee334",
      "PARAM",
      [
        "storage",
        "0029967f",
        null,
        "string"
      ]
    ],
    [
      "00aee344",
      "DATA",
      [
        "storage",
        "010a0a60",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee270`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee250.md#insn-00aee270) · [`00aee26c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee250.md#insn-00aee26c) · [`00aee278`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee250.md#insn-00aee278)
- 新版 [`00aee338`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee318.md#insn-00aee338) · [`00aee334`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee318.md#insn-00aee334) · [`00aee340`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee318.md#insn-00aee340)

~~~diff
- 00aee270 ["INT_ADD", "register:40f0:8", ["const:aee270:8", "const:4:8"]]
- 00aee270 ["CALL", null, ["callee:00bde130:8"]]
+ 00aee338 ["INT_ADD", "register:40f0:8", ["const:aee338:8", "const:4:8"]]
+ 00aee338 ["CALL", null, ["callee:00bde130:8"]]
- 00aee270 bytes 84bf0394
+ 00aee338 bytes 7ebf0394
- 00aee26c ["COPY", "tmp:0:8", ["const:5f2:8"]]
- 00aee26c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00aee26c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00aee26c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00aee334 ["COPY", "tmp:0:8", ["const:67f:8"]]
+ 00aee334 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00aee334 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00aee334 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00aee26c bytes 00c81791
+ 00aee334 bytes 00fc1991
- 00aee278 ["COPY", "tmp:0:8", ["const:9a0:8"]]
- 00aee278 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
- 00aee278 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
- 00aee278 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
+ 00aee340 ["COPY", "tmp:0:8", ["const:a60:8"]]
+ 00aee340 ["INT_CARRY", "register:105:1", ["register:4040:8", "tmp:0:8"]]
+ 00aee340 ["INT_SCARRY", "register:106:1", ["register:4040:8", "tmp:0:8"]]
+ 00aee340 ["INT_ADD", "tmp:1:8", ["register:4040:8", "tmp:0:8"]]
- 00aee278 bytes 08812691
+ 00aee340 bytes 08812991
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b0dd8d04f0537221eabe3b613da161f"></a>

### [`00aee28c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee28c.md) → [`00aee354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee354.md) _ZN8firebase4util25InitializeActivityClassesEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde570`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde570.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00aee7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee7fc.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdb0b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdb0b0.md)
- 新版 呼出元 1件 [`00bde620`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde620.md) · 呼出先 9件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00aee8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee8c4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb160`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb160.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.08% / 新版 87.08%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 4件, `call_argument_candidate` 11件, `store_condition` 2件, `store_destination` 9件

アドレスに依存する影響 `branch_value` 1件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "bounded",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee380",
      "incomplete_value": false,
      "site": "00aee380",
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
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee2b8",
      "incomplete_value": false,
      "site": "00aee2b8",
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
            "const:9a8:8"
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
      "definition_site": "00aee3c4",
      "incomplete_value": true,
      "site": "00aee3c4",
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
      "definition_site": "00aee2fc",
      "incomplete_value": true,
      "site": "00aee2fc",
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
            "const:408:8"
          ]
        ]
      ]
    },
    "ordinal": 13,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee41c",
      "incomplete_value": true,
      "site": "00aee41c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:328:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee354",
      "incomplete_value": true,
      "site": "00aee354",
      "value": [
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
      "00aee374",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee380",
      "WRITE",
      [
        "storage",
        "010a09a8",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee398",
      "READ",
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
      "00aee374",
      "READ",
      [
        "storage",
        "010a0a68",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee380",
      "WRITE",
      [
        "storage",
        "010a0a68",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee398",
      "READ",
      [
        "storage",
        "010a04c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee2b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee28c.md#insn-00aee2b8) · [`00aee2e0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee28c.md#insn-00aee2e0) · [`00aee2f4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee28c.md#insn-00aee2f4)
- 新版 [`00aee380`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee354.md#insn-00aee380) · [`00aee3a8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee354.md#insn-00aee3a8) · [`00aee3bc`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee354.md#insn-00aee3bc)

~~~diff
- 00aee2b8 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:9a8:8"]]
- 00aee2b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00aee380 ["INT_ADD", "tmp:0:8", ["register:40b8:8", "const:a68:8"]]
+ 00aee380 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00aee2b8 bytes e8aa09b9
+ 00aee380 bytes e86a0ab9
- 00aee2e0 ["COPY", "tmp:0:8", ["const:342:8"]]
- 00aee2e0 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
- 00aee2e0 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
- 00aee2e0 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
+ 00aee3a8 ["COPY", "tmp:0:8", ["const:339:8"]]
+ 00aee3a8 ["INT_CARRY", "register:105:1", ["register:4018:8", "tmp:0:8"]]
+ 00aee3a8 ["INT_SCARRY", "register:106:1", ["register:4018:8", "tmp:0:8"]]
+ 00aee3a8 ["INT_ADD", "tmp:1:8", ["register:4018:8", "tmp:0:8"]]
- 00aee2e0 bytes 63080d91
+ 00aee3a8 bytes 63e40c91
- 00aee2f4 ["INT_ADD", "register:40f0:8", ["const:aee2f4:8", "const:4:8"]]
- 00aee2f4 ["CALL", null, ["callee:00bde040:8"]]
+ 00aee3bc ["INT_ADD", "register:40f0:8", ["const:aee3bc:8", "const:4:8"]]
+ 00aee3bc ["CALL", null, ["callee:00bde040:8"]]
- 00aee2f4 bytes 27bf0394
+ 00aee3bc bytes 21bf0394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1dfabaf1261a83a22cf7ae54fa618abd"></a>

### [`00aee64c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee64c.md) → [`00aee714`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee714.md) _ZN8firebase4util24TerminateActivityClassesEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00bde560`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde560.md) · 呼出先 2件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md)
- 新版 呼出元 1件 [`00bde610`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde610.md) · 呼出先 2件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.04% / 新版 87.04%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 3件, `store_destination` 6件

アドレスに依存する影響 `branch_value` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee748",
      "incomplete_value": true,
      "site": "00aee748",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee680",
      "incomplete_value": true,
      "site": "00aee680",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee778",
      "incomplete_value": true,
      "site": "00aee778",
      "value": [
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
      "definition_site": "00aee6b0",
      "incomplete_value": true,
      "site": "00aee6b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:410:8"
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
      "definition_site": "00aee7c8",
      "incomplete_value": true,
      "site": "00aee7c8",
      "value": [
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
      "definition_site": "00aee700",
      "incomplete_value": true,
      "site": "00aee700",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:408:8"
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
      "00aee728",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee738",
      "PARAM",
      [
        "storage",
        "002ac13c",
        null,
        "string"
      ]
    ],
    [
      "00aee740",
      "READ",
      [
        "storage",
        "010a09a8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00aee728",
      "READ",
      [
        "storage",
        "010a0a68",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee738",
      "PARAM",
      [
        "storage",
        "002ac133",
        null,
        "string"
      ]
    ],
    [
      "00aee740",
      "READ",
      [
        "storage",
        "010a0a68",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee674`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee64c.md#insn-00aee674) · [`00aee680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee64c.md#insn-00aee680) · [`00aee6b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee64c.md#insn-00aee6b0)
- 新版 [`00aee73c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee714.md#insn-00aee73c) · [`00aee748`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee714.md#insn-00aee748) · [`00aee778`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee714.md#insn-00aee778)

~~~diff
- 00aee674 ["INT_ADD", "register:40f0:8", ["const:aee674:8", "const:4:8"]]
- 00aee674 ["CALL", null, ["callee:00bde130:8"]]
+ 00aee73c ["INT_ADD", "register:40f0:8", ["const:aee73c:8", "const:4:8"]]
+ 00aee73c ["CALL", null, ["callee:00bde130:8"]]
- 00aee674 bytes 83be0394
+ 00aee73c bytes 7dbe0394
- 00aee680 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00aee680 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00aee748 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
+ 00aee748 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00aee680 bytes 88aa09b9
+ 00aee748 bytes 886a0ab9
- 00aee6b0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aee6b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aee6b0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:410:8"]]
- 00aee6b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00aee778 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00aee778 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00aee778 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4d0:8"]]
+ 00aee778 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aee6b0 bytes bf421039
+ 00aee778 bytes bf421339
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-993734240b802d09e2c339bfdd2f62cb"></a>

### [`00aee7fc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee7fc.md) → [`00aee8c4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee8c4.md) FUN_00aee8c4

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 1件 [`00aee28c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee28c.md) · 呼出先 1件 [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md)
- 新版 呼出元 1件 [`00aee354`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee354.md) · 呼出先 1件 [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 85.29% / 新版 85.29%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `store_destination` 1件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee940",
      "incomplete_value": true,
      "site": "00aee940",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a70:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee878",
      "incomplete_value": true,
      "site": "00aee878",
      "value": [
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
    "ordinal": 7,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00aee8e8",
      "incomplete_value": true,
      "site": "00aee8ec",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
      "definition_site": "00aee820",
      "incomplete_value": true,
      "site": "00aee824",
      "value": [
        "INT_EQUAL",
        "1",
        [
          [
            "INT_SUB",
            "8",
            [
              "LOAD",
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00aee914",
      "incomplete_value": true,
      "site": "00aee914",
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
      "definition_site": "00aee84c",
      "incomplete_value": true,
      "site": "00aee84c",
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
      "00aee8d8",
      "READ",
      [
        "storage",
        "010a09b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee908",
      "READ",
      [
        "storage",
        "010a09b0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee940",
      "WRITE",
      [
        "storage",
        "010a09b0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aee8d8",
      "READ",
      [
        "storage",
        "010a0a70",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee908",
      "READ",
      [
        "storage",
        "010a0a70",
        null,
        "undefined8"
      ]
    ],
    [
      "00aee940",
      "WRITE",
      [
        "storage",
        "010a0a70",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee878`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee7fc.md#insn-00aee878) · [`00aee810`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee7fc.md#insn-00aee810) · [`00aee83c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee7fc.md#insn-00aee83c)
- 新版 [`00aee940`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee8c4.md#insn-00aee940) · [`00aee8d8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee8c4.md#insn-00aee8d8) · [`00aee904`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee8c4.md#insn-00aee904)

~~~diff
- 00aee878 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b0:8"]]
- 00aee878 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aee878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00aee940 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a70:8"]]
+ 00aee940 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00aee940 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aee878 bytes bfda04f9
+ 00aee940 bytes bf3a05f9
- 00aee810 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b0:8"]]
- 00aee810 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
+ 00aee8d8 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a70:8"]]
+ 00aee8d8 ["LOAD", "register:4098:8", ["const:1b1:8", "tmp:0:8"]]
- 00aee810 bytes b3da44f9
+ 00aee8d8 bytes b33a45f9
- 00aee83c ["COPY", "register:0:8", ["register:4040:8"]]
- 00aee83c ["INT_ADD", "register:40f0:8", ["const:aee83c:8", "const:4:8"]]
- 00aee83c ["CALLIND", null, ["register:0:8"]]
+ 00aee904 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00aee904 ["INT_ADD", "register:40f0:8", ["const:aee904:8", "const:4:8"]]
+ 00aee904 ["CALLIND", null, ["register:0:8"]]
- 00aee83c bytes 00013fd6
+ 00aee904 bytes 00013fd6
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e1992a35121913546809bd5a1bdf3ec6"></a>

### [`00aee884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee884.md) → [`00aee94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee94c.md) _ZN8firebase4util10InitializeEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddf20`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf20.md) · 呼出先 13件 [`00aef908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aef/00aef908.md) [`00af0b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0b2c.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md)
- 新版 呼出元 1件 [`00bddfd0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddfd0.md) · 呼出先 13件 [`00aef9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aef/00aef9d0.md) [`00af0bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md)

変更の種類 branch_condition_or_target, branch_value, call_argument_candidate, constant, control_flow, local_def_use, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_condition, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 26.87% / 新版 26.87%

CFGの説明率　旧版 16.87% / 新版 16.87%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 44件, `store_condition` 3件, `store_destination` 10件, `unresolved_branch_alignment` 63件, `unresolved_call_alignment` 63件, `unresolved_store_alignment` 34件

アドレスに依存する影響 `branch_value` 7件, `store_condition` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00aee984",
      "incomplete_value": true,
      "site": "00aee984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00aee8bc",
      "incomplete_value": true,
      "site": "00aee8bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9b8:8"
          ]
        ]
      ]
    },
    "ordinal": 10,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee904"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aee95c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aee978",
      "READ",
      [
        "storage",
        "010a09b8",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee984",
      "WRITE",
      [
        "storage",
        "010a09b8",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee9a4",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00aee978",
      "READ",
      [
        "storage",
        "010a0a78",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee984",
      "WRITE",
      [
        "storage",
        "010a0a78",
        null,
        "undefined4"
      ]
    ],
    [
      "00aee9a4",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aee8bc`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee884.md#insn-00aee8bc) · [`00aee904`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee884.md#insn-00aee904) · [`00aee95c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee884.md#insn-00aee95c)
- 新版 [`00aee984`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee94c.md#insn-00aee984)

~~~diff
- 00aee8bc ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9b8:8"]]
- 00aee8bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00aee984 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a78:8"]]
+ 00aee984 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00aee8bc bytes a8ba09b9
+ 00aee984 bytes a87a0ab9
- 00aee904 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:470:8"]]
- 00aee904 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee904 bytes c03a02f9
- 00aee95c ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:4a0:8"]]
- 00aee95c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00aee95c bytes c05202f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee9379f31431cdfe9d3445a95939453f"></a>

### [`00aef908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aef/00aef908.md) → [`00aef9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aef/00aef9d0.md) FUN_00aef9d0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved`

- 旧版 呼出元 2件 [`00aee884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee884.md) [`00af0b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0b2c.md) · 呼出先 1件 [`00bde400`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde400.md)
- 新版 呼出元 2件 [`00aee94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee94c.md) [`00af0bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md) · 呼出先 1件 [`00bde4b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4b0.md)

変更の種類 branch_value, constant, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 13.26% / 新版 13.26%

CFGの説明率　旧版 10.71% / 新版 10.71%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `unresolved_branch_alignment` 94件, `unresolved_call_alignment` 165件, `unresolved_store_alignment` 67件

アドレスに依存する影響 `branch_value` 5件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef944"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef994"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00aef9c0"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00aef9e4",
      "READ",
      [
        "storage",
        "010a04a0",
        null,
        "undefined8"
      ]
    ],
    [
      "00aef9ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "unmatched:00aef998"
      ]
    ],
    [
      "00aef9f4",
      "READ",
      [
        "storage",
        "010a04a8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00aef9e4",
      "READ",
      [
        "storage",
        "010a0560",
        null,
        "undefined8"
      ]
    ],
    [
      "00aef9ec",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00aefa60"
      ]
    ],
    [
      "00aef9f4",
      "READ",
      [
        "storage",
        "010a0568",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00aef944`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aef/00aef908.md#insn-00aef944) · [`00aef994`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aef/00aef908.md#insn-00aef994) · [`00aef9c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aef/00aef908.md#insn-00aef9c0)

~~~diff
- 00aef944 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aef944 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aef944 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:4a8:8"]]
- 00aef944 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aef944 bytes bfa21239
- 00aef994 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:4a0:8"]]
- 00aef994 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00aef994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00aef994 bytes 9f5202f9
- 00aef9c0 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00aef9c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00aef9c0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:478:8"]]
- 00aef9c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00aef9c0 bytes bfe21139
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f89464525fbc50dc344a7664e8a20915"></a>

### [`00af0b2c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0b2c.md) → [`00af0bf4`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md) _ZN8firebase4util9TerminateEP7_JNIEnv

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 2件 [`00aee884`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aee/00aee884.md) [`00bde050`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde050.md) · 呼出先 10件 [`00aef908`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aef/00aef908.md) [`00bdaf60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf60.md) [`00bddf80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf80.md) [`00bde080`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde080.md) [`00bde2c0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde2c0.md)
- 新版 呼出元 2件 [`00aee94c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aee/00aee94c.md) [`00bde100`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde100.md) · 呼出先 10件 [`00aef9d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aef/00aef9d0.md) [`00bdb010`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb010.md) [`00bde030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde030.md) [`00bde130`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde130.md) [`00bde370`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde370.md)

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 88.57% / 新版 88.57%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 2件, `store_destination` 2件

アドレスに依存する影響 `branch_value` 2件, `call_argument_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af0c28",
      "incomplete_value": true,
      "site": "00af0c28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0b60",
      "incomplete_value": true,
      "site": "00af0b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9b8:8"
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
      "definition_site": "00af0c8c",
      "incomplete_value": true,
      "site": "00af0c8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af0bc4",
      "incomplete_value": true,
      "site": "00af0bc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9c0:8"
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
      "definition_site": "00af0c48",
      "incomplete_value": true,
      "site": "00af0c48",
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
      "definition_site": "00af0b80",
      "incomplete_value": true,
      "site": "00af0b80",
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
      "00af0c08",
      "READ",
      [
        "storage",
        "010a09b8",
        null,
        "undefined4"
      ]
    ],
    [
      "00af0c20",
      "READ",
      [
        "storage",
        "010a09b8",
        null,
        "undefined4"
      ]
    ],
    [
      "00af0c28",
      "WRITE",
      [
        "storage",
        "010a09b8",
        null,
        "undefined4"
      ]
    ]
  ],
  "added": [
    [
      "00af0c08",
      "READ",
      [
        "storage",
        "010a0a78",
        null,
        "undefined4"
      ]
    ],
    [
      "00af0c20",
      "READ",
      [
        "storage",
        "010a0a78",
        null,
        "undefined4"
      ]
    ],
    [
      "00af0c28",
      "WRITE",
      [
        "storage",
        "010a0a78",
        null,
        "undefined4"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0b60`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0b2c.md#insn-00af0b60) · [`00af0b98`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0b2c.md#insn-00af0b98) · [`00af0bc4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0b2c.md#insn-00af0bc4)
- 新版 [`00af0c28`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md#insn-00af0c28) · [`00af0c60`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md#insn-00af0c60) · [`00af0c8c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0bf4.md#insn-00af0c8c)

~~~diff
- 00af0b60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9b8:8"]]
- 00af0b60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
+ 00af0c28 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a78:8"]]
+ 00af0c28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4040:4"]]
- 00af0b60 bytes 88ba09b9
+ 00af0c28 bytes 887a0ab9
- 00af0b98 ["INT_ADD", "register:40f0:8", ["const:af0b98:8", "const:4:8"]]
- 00af0b98 ["CALL", null, ["callee:00bde7d0:8"]]
+ 00af0c60 ["INT_ADD", "register:40f0:8", ["const:af0c60:8", "const:4:8"]]
+ 00af0c60 ["CALL", null, ["callee:00bde7d0:8"]]
- 00af0b98 bytes e2b60394
+ 00af0c60 bytes dcb60394
- 00af0bc4 ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:9c0:8"]]
- 00af0bc4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00af0bc4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00af0c8c ["INT_ADD", "tmp:0:8", ["register:40a8:8", "const:a80:8"]]
+ 00af0c8c ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00af0c8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00af0bc4 bytes bfe204f9
+ 00af0c8c bytes bf4205f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3ff830b6d2515f0f42f0409ac759619"></a>

### [`00af0c44`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0c44.md) → [`00af0d0c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0d0c.md) _ZN8firebase4util18CacheEmbeddedFilesEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde420`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde420.md) · 呼出先 6件 [`0047495c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md) [`00bddd40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd40.md)
- 新版 呼出元 1件 [`00bde4d0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde4d0.md) · 呼出先 6件 [`0047495c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/0047495c.md) [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md) [`00bdddf0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bdddf0.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 63.18% / 新版 63.18%

CFGの説明率　旧版 6.56% / 新版 6.45%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 16件, `unresolved_branch_alignment` 11件, `unresolved_call_alignment` 22件, `unresolved_return_alignment` 1件

アドレスに依存する影響 `call_argument_candidate` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0c8c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0d34"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af0d88"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af0c68",
      "READ",
      [
        "storage",
        "010a0420",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af0c8c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af0d78"
      ]
    ],
    [
      "unmatched:00af0cc8",
      "PARAM",
      [
        "storage",
        "002a2ce2",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00af0d30",
      "READ",
      [
        "storage",
        "010a04e0",
        null,
        "undefined8"
      ]
    ],
    [
      "00af0d54",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af0d78"
      ]
    ],
    [
      "00af0d90",
      "PARAM",
      [
        "storage",
        "002a2cdb",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af0c70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0c44.md#insn-00af0c70) · [`00af0c84`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0c44.md#insn-00af0c84) · [`00af0c8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af0/00af0c44.md#insn-00af0c8c)
- 新版 [`00af0d38`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af0/00af0d0c.md#insn-00af0d38)

~~~diff
- 00af0c70 ["INT_ADD", "register:40f0:8", ["const:af0c70:8", "const:4:8"]]
- 00af0c70 ["CALL", null, ["callee:0047495c:8"]]
+ 00af0d38 ["INT_ADD", "register:40f0:8", ["const:af0d38:8", "const:4:8"]]
+ 00af0d38 ["CALL", null, ["callee:0047495c:8"]]
- 00af0c70 bytes 3b0fe697
+ 00af0d38 bytes 090fe697
- 00af0c84 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af0c84 ["INT_ADD", "register:40f0:8", ["const:af0c84:8", "const:4:8"]]
- 00af0c84 ["CALLIND", null, ["register:0:8"]]
- 00af0c84 bytes 00013fd6
- 00af0c8c ["CBRANCH", null, ["local:b2:8", "register:101:1"]]
- 00af0c8c bytes 20010054
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-806334f7e8ecbf9f92a364ab23330dd9"></a>

### [`00af10e4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af10e4.md) → [`00af11ac`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af11ac.md) _ZN8firebase4util17JavaThreadContext10InitializeEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bde3d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde3d0.md) · 呼出先 2件 [`00bddf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf90.md) [`00bddfb0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddfb0.md)
- 新版 呼出元 1件 [`00bde480`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde480.md) · 呼出先 2件 [`00bde040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde040.md) [`00bde060`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde060.md)

変更の種類 branch_condition_or_target, branch_value, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, store_destination, unresolved_branch_alignment, unresolved_call_alignment, unresolved_store_alignment

命令の説明率　旧版 63.44% / 新版 63.44%

CFGの説明率　旧版 31.58% / 新版 33.33%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 5件, `store_destination` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 2件, `unresolved_store_alignment` 2件

アドレスに依存する影響 `branch_value` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1130"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00af1298",
      "incomplete_value": true,
      "site": "00af1298",
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
            "const:380:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af11d0",
      "incomplete_value": true,
      "site": "00af11d0",
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
            "const:2c0:8"
          ]
        ]
      ]
    },
    "ordinal": 8,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af121c"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af1100",
      "READ",
      [
        "storage",
        "010a02b8",
        null,
        "undefined8"
      ]
    ],
    [
      "unmatched:00af110c",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af1200"
      ]
    ],
    [
      "unmatched:00af1114",
      "PARAM",
      [
        "storage",
        "002ad2fc",
        null,
        "string"
      ]
    ]
  ],
  "added": [
    [
      "00af11c8",
      "READ",
      [
        "storage",
        "010a0378",
        null,
        "undefined8"
      ]
    ],
    [
      "00af11d4",
      "CONDITIONAL_JUMP",
      [
        "local_branch",
        "00af1200"
      ]
    ],
    [
      "00af11dc",
      "PARAM",
      [
        "storage",
        "002ad2f3",
        null,
        "string"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af110c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af10e4.md#insn-00af110c) · [`00af1128`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af10e4.md#insn-00af1128) · [`00af1130`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af10e4.md#insn-00af1130)

~~~diff
- 00af110c ["INT_NOTEQUAL", "tmp:0:1", ["register:4008:8", "const:0:8"]]
- 00af110c ["CBRANCH", null, ["local:b3:8", "tmp:0:1"]]
- 00af110c bytes 610100b5
- 00af1128 ["INT_ADD", "register:40f0:8", ["const:af1128:8", "const:4:8"]]
- 00af1128 ["CALL", null, ["callee:00bde040:8"]]
- 00af1128 bytes 9ab30394
- 00af1130 ["INT_ADD", "tmp:0:8", ["register:40b0:8", "const:2b8:8"]]
- 00af1130 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00af1130 bytes c05e01f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9bcd279f42528fd114dd018b23c95253"></a>

### [`00af1258`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1258.md) → [`00af1320`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1320.md) _ZN8firebase4util15CancelCallbacksEP7_JNIEnvPKc

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 1件 [`00bddf80`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf80.md) · 呼出先 7件 [`00551e14`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00551/00551e14.md) [`00bdaf40`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf40.md) [`00bde1b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1b0.md) [`00bde660`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde660.md) [`00bde680`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde680.md)
- 新版 呼出元 1件 [`00bde030`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde030.md) · 呼出先 7件 [`00551e14`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00551/00551e14.md) [`00bdaff0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaff0.md) [`00bde260`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde260.md) [`00bde710`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde710.md) [`00bde730`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde730.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_branch_alignment, unresolved_call_alignment

命令の説明率　旧版 84.80% / 新版 84.80%

CFGの説明率　旧版 61.90% / 新版 63.41%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_branch_alignment` 1件, `unresolved_call_alignment` 3件

~~~json
[
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": null,
    "old": {
      "site": "00af128c"
    }
  },
  {
    "confidence": "limited",
    "kind": "branch_position_unpaired",
    "new": {
      "site": "00af1354"
    },
    "old": null
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1294"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af128c",
      "PARAM",
      [
        "storage",
        "002ac159",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00af1290",
      "PARAM",
      [
        "storage",
        "002ae3ab",
        null,
        "string"
      ]
    ],
    [
      "unmatched:00af1294",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde260"
      ]
    ]
  ],
  "added": [
    [
      "00af1354",
      "PARAM",
      [
        "storage",
        "002ac150",
        null,
        "string"
      ]
    ],
    [
      "00af1358",
      "PARAM",
      [
        "storage",
        "002ae317",
        null,
        "string"
      ]
    ],
    [
      "00af135c",
      "UNCONDITIONAL_CALL",
      [
        "mapped_function",
        "00bde260"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af128c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1258.md#insn-00af128c) · [`00af1294`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1258.md#insn-00af1294) · [`00af1320`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1258.md#insn-00af1320)
- 新版 [`00af13e8`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1320.md#insn-00af13e8)

~~~diff
- 00af128c ["COPY", "tmp:0:8", ["register:4040:8"]]
- 00af128c ["CBRANCH", null, ["const:2:4", "register:101:1"]]
- 00af128c ["COPY", "tmp:0:8", ["register:4008:8"]]
- 00af128c ["COPY", "register:4008:8", ["tmp:0:8"]]
- 00af128c bytes 0101819a
- 00af1294 ["INT_ADD", "register:40f0:8", ["const:af1294:8", "const:4:8"]]
- 00af1294 ["CALL", null, ["callee:00bde260:8"]]
- 00af1294 bytes c7b30394
- 00af1320 ["INT_ADD", "register:40f0:8", ["const:af1320:8", "const:4:8"]]
- 00af1320 ["CALL", null, ["callee:00bde730:8"]]
+ 00af13e8 ["INT_ADD", "register:40f0:8", ["const:af13e8:8", "const:4:8"]]
+ 00af13e8 ["CALL", null, ["callee:00bde730:8"]]
- 00af1320 bytes d8b40394
+ 00af13e8 bytes d2b40394
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e646e7e34189fbe96ba8b8c57b350fd6"></a>

### [`00af14e8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af14e8.md) → [`00af15b0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af15b0.md) FUN_00af15b0

採用 · 移動量 `+0xc8` · 根拠 `unique_code_and_context` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 2件 [`00ae4a8c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4a8c.md) [`00ae4da4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae4/00ae4da4.md) · 呼出先 2件 [`00bdaf90`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdaf90.md) [`00bde1d0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde1d0.md)
- 新版 呼出元 2件 [`00ae4b54`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4b54.md) [`00ae4e6c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4e6c.md) · 呼出先 2件 [`00bdb040`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdb040.md) [`00bde280`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde280.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, comparison, comparison_count, constant, control_flow, local_def_use, memory_read, memory_read_count, memory_write, memory_write_count, operands_and_dependencies, operation_sequence, unresolved_store_alignment

命令の説明率　旧版 76.32% / 新版 76.32%

CFGの説明率　旧版 0.00% / 新版 0.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 1件, `unresolved_store_alignment` 6件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af153c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af153c"
    }
  },
  {
    "confidence": "limited",
    "kind": "store_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1540"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "unmatched:00af153c",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af1540",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "unmatched:00af1544",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00af1604",
      "WRITE",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ],
    [
      "00af1608",
      "WRITE",
      [
        "storage",
        "Stack[-0x38]",
        null,
        null
      ]
    ],
    [
      "00af160c",
      "READ",
      [
        "storage",
        "Stack[-0x48]",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af153c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af14e8.md#insn-00af153c) · [`00af1540`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af14e8.md#insn-00af1540) · [`00af1554`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af14e8.md#insn-00af1554)

~~~diff
- 00af153c ["COPY", "tmp:0:8", ["register:4058:8"]]
- 00af153c ["COPY", "tmp:1:8", ["register:4050:8"]]
- 00af153c ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffc8:8"]]
- 00af153c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af153c bytes abab3ca9
- 00af1540 ["COPY", "tmp:0:8", ["register:4048:8"]]
- 00af1540 ["COPY", "tmp:1:8", ["register:4060:8"]]
- 00af1540 ["INT_ADD", "tmp:2:8", ["register:40e8:8", "const:ffffffffffffffd8:8"]]
- 00af1540 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:0:8"]]
- 00af1540 bytes a9b33da9
- 00af1554 ["INT_ADD", "tmp:0:8", ["register:40e8:8", "const:ffffffffffffffa0:8"]]
- 00af1554 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:5020:16"]]
- 00af1554 ["INT_ADD", "tmp:1:8", ["tmp:0:8", "const:10:8"]]
- 00af1554 ["STORE", null, ["const:1b1:8", "tmp:1:8", "register:5000:16"]]
- 00af1554 bytes a1033dad
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1057f5601a3806baf251394b9901503f"></a>

### [`00af1580`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1580.md) → [`00af1648`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1648.md) _ZN8firebase4util19StdVectorToJavaListEP7_JNIEnvRKNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA_EEE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `cfg_change`

- 旧版 呼出元 1件 [`00bde4a0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bde4a0.md) · 呼出先 2件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md)
- 新版 呼出元 1件 [`00bde550`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde550.md) · 呼出先 2件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md)

変更の種類 branch_condition_or_target, call_argument_candidate, cfg_edge_inventory, constant, control_flow, operands_and_dependencies

命令の説明率　旧版 95.45% / 新版 95.45%

CFGの説明率　旧版 73.33% / 新版 78.57%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af166c",
      "incomplete_value": true,
      "site": "00af1678",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00af15a4",
      "incomplete_value": true,
      "site": "00af15b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:470:8"
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
      "definition_site": "00af1670",
      "incomplete_value": true,
      "site": "00af1678",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:540:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af15a8",
      "incomplete_value": true,
      "site": "00af15b0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:480:8"
              ]
            ]
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
      "00af166c",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1670",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00af168c",
      "READ",
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
      "00af166c",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1670",
      "READ",
      [
        "storage",
        "010a0540",
        null,
        "undefined8"
      ]
    ],
    [
      "00af168c",
      "READ",
      [
        "storage",
        "010a0550",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af15b0`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1580.md#insn-00af15b0) · [`00af159c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1580.md#insn-00af159c) · [`00af15a4`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1580.md#insn-00af15a4)
- 新版 [`00af1678`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1648.md#insn-00af1678) · [`00af1664`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1648.md#insn-00af1664) · [`00af166c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1648.md#insn-00af166c)

~~~diff
- 00af15b0 ["INT_ADD", "register:40f0:8", ["const:af15b0:8", "const:4:8"]]
- 00af15b0 ["CALL", null, ["callee:0056681c:8"]]
+ 00af1678 ["INT_ADD", "register:40f0:8", ["const:af1678:8", "const:4:8"]]
+ 00af1678 ["CALL", null, ["callee:0056681c:8"]]
- 00af15b0 bytes 9bd4e997
+ 00af1678 bytes 69d4e997
- 00af159c ["COPY", "tmp:0:8", ["const:480:8"]]
- 00af159c ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
- 00af159c ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
- 00af159c ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
+ 00af1664 ["COPY", "tmp:0:8", ["const:540:8"]]
+ 00af1664 ["INT_CARRY", "register:105:1", ["register:40b0:8", "tmp:0:8"]]
+ 00af1664 ["INT_SCARRY", "register:106:1", ["register:40b0:8", "tmp:0:8"]]
+ 00af1664 ["INT_ADD", "tmp:1:8", ["register:40b0:8", "tmp:0:8"]]
- 00af159c bytes d6021291
+ 00af1664 bytes d6021591
- 00af15a4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:470:8"]]
- 00af15a4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00af166c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:530:8"]]
+ 00af166c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00af15a4 bytes 013942f9
+ 00af166c bytes 019942f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7b10260a63d6b511ef8952cb9481086c"></a>

### [`00af1688`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1688.md) → [`00af1750`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1750.md) _ZN8firebase4util25StdUnorderedSetToJavaListEP7_JNIEnvRKNSt6__ndk113unordered_setINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcE

採用 · 移動量 `+0xc8` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow` · `instruction_positions_unresolved` · `cfg_change`

- 旧版 呼出元 0件  · 呼出先 2件 [`00474b70`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00566/0056681c.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00474b70`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00474/00474b70.md) [`0056681c`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00566/0056681c.md)

変更の種類 branch_condition_or_target, call, call_argument_candidate, call_count, cfg_edge_inventory, constant, control_flow, control_flow_count, local_def_use, memory_read, memory_read_count, operands_and_dependencies, operation_sequence, unresolved_call_alignment, unresolved_return_alignment

命令の説明率　旧版 79.03% / 新版 79.03%

CFGの説明率　旧版 33.33% / 新版 16.67%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `call_argument_candidate` 6件, `unresolved_call_alignment` 4件, `unresolved_return_alignment` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00af1774",
      "incomplete_value": true,
      "site": "00af1780",
      "value": [
        "LOAD",
        "8",
        [
          [
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
    "old": {
      "definition_site": "00af16ac",
      "incomplete_value": true,
      "site": "00af16b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:470:8"
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
      "definition_site": "00af1778",
      "incomplete_value": true,
      "site": "00af1780",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:540:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00af16b0",
      "incomplete_value": true,
      "site": "00af16b8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:480:8"
              ]
            ]
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 3
  },
  {
    "confidence": "limited",
    "kind": "call_position_unpaired",
    "new": null,
    "old": {
      "site": "00af1710"
    }
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00af1774",
      "READ",
      [
        "storage",
        "010a0470",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1778",
      "READ",
      [
        "storage",
        "010a0480",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1790",
      "READ",
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
      "00af1774",
      "READ",
      [
        "storage",
        "010a0530",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1778",
      "READ",
      [
        "storage",
        "010a0540",
        null,
        "undefined8"
      ]
    ],
    [
      "00af1790",
      "READ",
      [
        "storage",
        "010a0550",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00af16b8`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1688.md#insn-00af16b8) · [`00af1710`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1688.md#insn-00af1710) · [`00af1728`](../../../../reference/15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af1/00af1688.md#insn-00af1728)
- 新版 [`00af1780`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1750.md#insn-00af1780) · [`00af17f0`](../../../../reference/15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00af1/00af1750.md#insn-00af17f0)

~~~diff
- 00af16b8 ["INT_ADD", "register:40f0:8", ["const:af16b8:8", "const:4:8"]]
- 00af16b8 ["CALL", null, ["callee:0056681c:8"]]
+ 00af1780 ["INT_ADD", "register:40f0:8", ["const:af1780:8", "const:4:8"]]
+ 00af1780 ["CALL", null, ["callee:0056681c:8"]]
- 00af16b8 bytes 59d4e997
+ 00af1780 bytes 27d4e997
- 00af1710 ["COPY", "register:0:8", ["register:4040:8"]]
- 00af1710 ["INT_ADD", "register:40f0:8", ["const:af1710:8", "const:4:8"]]
- 00af1710 ["CALLIND", null, ["register:0:8"]]
- 00af1710 bytes 00013fd6
- 00af1728 ["INT_ADD", "register:40f0:8", ["const:af1728:8", "const:4:8"]]
- 00af1728 ["CALL", null, ["callee:00474b70:8"]]
+ 00af17f0 ["INT_ADD", "register:40f0:8", ["const:af17f0:8", "const:4:8"]]
+ 00af17f0 ["CALL", null, ["callee:00474b70:8"]]
- 00af1728 bytes 120de697
+ 00af17f0 bytes e00ce697
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

