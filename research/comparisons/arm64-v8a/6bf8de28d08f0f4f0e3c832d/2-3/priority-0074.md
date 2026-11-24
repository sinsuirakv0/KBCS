# v16.0.2 → v16.0.3 · 最優先の変更候補 (74)

[一覧の目次](README.md)

<a id="compare-498262baeebe38c2da34d744ba10ac48"></a>

### [`00b48990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48990.md) → [`00b49984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49984.md) _ZN8firebase4util10byte_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b499a0",
      "incomplete_value": false,
      "site": "00b499a4",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b489ac",
      "incomplete_value": false,
      "site": "00b489b0",
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
            "const:30b:8"
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
      "definition_site": "00b499b0",
      "incomplete_value": true,
      "site": "00b499bc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b489bc",
      "incomplete_value": true,
      "site": "00b489c8",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b499a0",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b499b0",
      "DATA",
      [
        "storage",
        "01125a18",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b499a0",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b499b0",
      "DATA",
      [
        "storage",
        "011269d8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b489b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48990.md#insn-00b489b0) · [`00b489ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48990.md#insn-00b489ac) · [`00b489b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48990.md#insn-00b489b4)
- 新版 [`00b499a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49984.md#insn-00b499a4) · [`00b499a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49984.md#insn-00b499a0) · [`00b499a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49984.md#insn-00b499a8)

~~~diff
- 00b489b0 ["INT_ADD", "register:40f0:8", ["const:b489b0:8", "const:4:8"]]
- 00b489b0 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b499a4 ["INT_ADD", "register:40f0:8", ["const:b499a4:8", "const:4:8"]]
+ 00b499a4 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b489b0 bytes c8490494
+ 00b499a4 bytes bf490494
- 00b489ac ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b489ac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b489ac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b489ac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b499a0 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b499a0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b499a0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b499a0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b489ac bytes 002c0c91
+ 00b499a0 bytes 008c1191
- 00b489b4 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b499a8 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b489b4 bytes e82e00b0
+ 00b499a8 bytes e82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12366a0b4cf63ef73a6b92e1911c6679"></a>

### [`00b489cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b489cc.md) → [`00b499c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b499c0.md) _ZN8firebase4util10byte_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b49a00",
      "incomplete_value": true,
      "site": "00b49a00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:9c8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48a0c",
      "incomplete_value": true,
      "site": "00b48a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a08:8"
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
      "definition_site": "00b499dc",
      "incomplete_value": true,
      "site": "00b499dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b489e8",
      "incomplete_value": true,
      "site": "00b489e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b499e4",
      "incomplete_value": false,
      "site": "00b499f8",
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
            "const:143:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b489f0",
      "incomplete_value": false,
      "site": "00b48a04",
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
            "const:feb:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b499d4",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b499e4",
      "PARAM",
      [
        "storage",
        "002a5feb",
        null,
        "string"
      ]
    ],
    [
      "00b49a00",
      "WRITE",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b499d4",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b499e4",
      "PARAM",
      [
        "storage",
        "002a6143",
        null,
        "string"
      ]
    ],
    [
      "00b49a00",
      "WRITE",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b489cc.md#insn-00b48a04) · [`00b48a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b489cc.md#insn-00b48a0c) · [`00b489d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b489cc.md#insn-00b489d8)
- 新版 [`00b499f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b499c0.md#insn-00b499f8) · [`00b49a00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b499c0.md#insn-00b49a00) · [`00b499cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b499c0.md#insn-00b499cc)

~~~diff
- 00b48a04 ["INT_ADD", "register:40f0:8", ["const:b48a04:8", "const:4:8"]]
- 00b48a04 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b499f8 ["INT_ADD", "register:40f0:8", ["const:b499f8:8", "const:4:8"]]
+ 00b499f8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48a04 bytes 77490494
+ 00b499f8 bytes 6e490494
- 00b48a0c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a08:8"]]
- 00b48a0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49a00 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9c8:8"]]
+ 00b49a00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48a0c bytes 800605f9
+ 00b49a00 bytes 80e604f9
- 00b489d8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b499cc ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b489d8 bytes f42e00b0
+ 00b499cc bytes f42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-482c005b5a4a39765ead5a19837c7c5b"></a>

### [`00b48a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48a3c.md) → [`00b49a30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49a30.md) _ZN8firebase4util10byte_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b49a4c",
      "incomplete_value": false,
      "site": "00b49a50",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48a58",
      "incomplete_value": false,
      "site": "00b48a5c",
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
            "const:54d:8"
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
      "definition_site": "00b49a5c",
      "incomplete_value": true,
      "site": "00b49a68",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b48a68",
      "incomplete_value": true,
      "site": "00b48a74",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b49a4c",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b49a5c",
      "DATA",
      [
        "storage",
        "01125a28",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49a4c",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b49a5c",
      "DATA",
      [
        "storage",
        "011269e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48a5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48a3c.md#insn-00b48a5c) · [`00b48a58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48a3c.md#insn-00b48a58) · [`00b48a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48a3c.md#insn-00b48a60)
- 新版 [`00b49a50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49a30.md#insn-00b49a50) · [`00b49a4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49a30.md#insn-00b49a4c) · [`00b49a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49a30.md#insn-00b49a54)

~~~diff
- 00b48a5c ["INT_ADD", "register:40f0:8", ["const:b48a5c:8", "const:4:8"]]
- 00b48a5c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b49a50 ["INT_ADD", "register:40f0:8", ["const:b49a50:8", "const:4:8"]]
+ 00b49a50 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b48a5c bytes 9d490494
+ 00b49a50 bytes 94490494
- 00b48a58 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b48a58 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b48a58 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b48a58 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49a4c ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b49a4c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49a4c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49a4c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b48a58 bytes 00341591
+ 00b49a4c bytes 00681891
- 00b48a60 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b49a54 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b48a60 bytes e82e00b0
+ 00b49a54 bytes e82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7885bb299adcb62347d579f111465714"></a>

### [`00b48a78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48a78.md) → [`00b49a6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49a6c.md) _ZN8firebase4util15character_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b49a98",
      "incomplete_value": true,
      "site": "00b49a98",
      "value": [
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
      "definition_site": "00b48aa4",
      "incomplete_value": true,
      "site": "00b48aa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "definition_site": "00b49a8c",
      "incomplete_value": false,
      "site": "00b49a90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:e83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48a98",
      "incomplete_value": false,
      "site": "00b48a9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:da5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49a7c",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49a8c",
      "PARAM",
      [
        "storage",
        "002bbda5",
        null,
        "string"
      ]
    ],
    [
      "00b49a98",
      "WRITE",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49a7c",
      "READ",
      [
        "storage",
        "011269f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49a8c",
      "PARAM",
      [
        "storage",
        "002bbe83",
        null,
        "string"
      ]
    ],
    [
      "00b49a98",
      "WRITE",
      [
        "storage",
        "011269f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48a9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48a78.md#insn-00b48a9c) · [`00b48aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48a78.md#insn-00b48aa4) · [`00b48a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48a78.md#insn-00b48a84)
- 新版 [`00b49a90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49a6c.md#insn-00b49a90) · [`00b49a98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49a6c.md#insn-00b49a98) · [`00b49a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49a6c.md#insn-00b49a78)

~~~diff
- 00b48a9c ["INT_ADD", "register:40f0:8", ["const:b48a9c:8", "const:4:8"]]
- 00b48a9c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b49a90 ["INT_ADD", "register:40f0:8", ["const:b49a90:8", "const:4:8"]]
+ 00b49a90 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48a9c bytes 51490494
+ 00b49a90 bytes 48490494
- 00b48aa4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
- 00b48aa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49a98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 00b49a98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48aa4 bytes 601a05f9
+ 00b49a98 bytes 60fa04f9
- 00b48a84 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49a78 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b48a84 bytes f32e00b0
+ 00b49a78 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8f5444185d10e9d0d4963f872c18abbc"></a>

### [`00b48ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ab8.md) → [`00b49aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49aac.md) _ZN8firebase4util15character_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b49ad8",
      "incomplete_value": true,
      "site": "00b49ad8",
      "value": [
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
      "definition_site": "00b48ae4",
      "incomplete_value": true,
      "site": "00b48ae4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "definition_site": "00b49ac0",
      "incomplete_value": true,
      "site": "00b49ac0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48acc",
      "incomplete_value": true,
      "site": "00b48acc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49ac8",
      "incomplete_value": false,
      "site": "00b49ad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:e83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48ad4",
      "incomplete_value": false,
      "site": "00b48adc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:da5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49abc",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49ac8",
      "PARAM",
      [
        "storage",
        "002bbda5",
        null,
        "string"
      ]
    ],
    [
      "00b49ad8",
      "WRITE",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49abc",
      "READ",
      [
        "storage",
        "011269f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49ac8",
      "PARAM",
      [
        "storage",
        "002bbe83",
        null,
        "string"
      ]
    ],
    [
      "00b49ad8",
      "WRITE",
      [
        "storage",
        "011269f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48adc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ab8.md#insn-00b48adc) · [`00b48ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ab8.md#insn-00b48ae4) · [`00b48ac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ab8.md#insn-00b48ac4)
- 新版 [`00b49ad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49aac.md#insn-00b49ad0) · [`00b49ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49aac.md#insn-00b49ad8) · [`00b49ab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49aac.md#insn-00b49ab8)

~~~diff
- 00b48adc ["INT_ADD", "register:40f0:8", ["const:b48adc:8", "const:4:8"]]
- 00b48adc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b49ad0 ["INT_ADD", "register:40f0:8", ["const:b49ad0:8", "const:4:8"]]
+ 00b49ad0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48adc bytes 41490494
+ 00b49ad0 bytes 38490494
- 00b48ae4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
- 00b48ae4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49ad8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 00b49ad8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48ae4 bytes 601a05f9
+ 00b49ad8 bytes 60fa04f9
- 00b48ac4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49ab8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b48ac4 bytes f32e00b0
+ 00b49ab8 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5843fb7fd41ec5a2a71b0e4d164dd32b"></a>

### [`00b48af8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48af8.md) → [`00b49aec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49aec.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b49b1c",
      "incomplete_value": true,
      "site": "00b49b1c",
      "value": [
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
      "definition_site": "00b48b28",
      "incomplete_value": true,
      "site": "00b48b28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "definition_site": "00b49b00",
      "incomplete_value": true,
      "site": "00b49b00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48b0c",
      "incomplete_value": true,
      "site": "00b48b0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49b0c",
      "incomplete_value": false,
      "site": "00b49b14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:e83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48b18",
      "incomplete_value": false,
      "site": "00b48b20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:da5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49afc",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49b0c",
      "PARAM",
      [
        "storage",
        "002bbda5",
        null,
        "string"
      ]
    ],
    [
      "00b49b1c",
      "WRITE",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49afc",
      "READ",
      [
        "storage",
        "011269f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49b0c",
      "PARAM",
      [
        "storage",
        "002bbe83",
        null,
        "string"
      ]
    ],
    [
      "00b49b1c",
      "WRITE",
      [
        "storage",
        "011269f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48b20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48af8.md#insn-00b48b20) · [`00b48b28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48af8.md#insn-00b48b28) · [`00b48b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48af8.md#insn-00b48b04)
- 新版 [`00b49b14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49aec.md#insn-00b49b14) · [`00b49b1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49aec.md#insn-00b49b1c) · [`00b49af8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49aec.md#insn-00b49af8)

~~~diff
- 00b48b20 ["INT_ADD", "register:40f0:8", ["const:b48b20:8", "const:4:8"]]
- 00b48b20 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b49b14 ["INT_ADD", "register:40f0:8", ["const:b49b14:8", "const:4:8"]]
+ 00b49b14 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48b20 bytes 30490494
+ 00b49b14 bytes 27490494
- 00b48b28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
- 00b48b28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49b1c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 00b49b1c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48b28 bytes 601a05f9
+ 00b49b1c bytes 60fa04f9
- 00b48b04 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49af8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b48b04 bytes f32e00b0
+ 00b49af8 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59d328cc2acc796c1399e91a2e39d4d2"></a>

### [`00b48b3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48b3c.md) → [`00b49b30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49b30.md) _ZN8firebase4util15character_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b49b60",
      "incomplete_value": true,
      "site": "00b49b60",
      "value": [
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
      "definition_site": "00b48b6c",
      "incomplete_value": true,
      "site": "00b48b6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "definition_site": "00b49b44",
      "incomplete_value": true,
      "site": "00b49b44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48b50",
      "incomplete_value": true,
      "site": "00b48b50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49b4c",
      "incomplete_value": false,
      "site": "00b49b58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:e83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48b58",
      "incomplete_value": false,
      "site": "00b48b64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:da5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49b40",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49b4c",
      "PARAM",
      [
        "storage",
        "002bbda5",
        null,
        "string"
      ]
    ],
    [
      "00b49b60",
      "WRITE",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49b40",
      "READ",
      [
        "storage",
        "011269f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49b4c",
      "PARAM",
      [
        "storage",
        "002bbe83",
        null,
        "string"
      ]
    ],
    [
      "00b49b60",
      "WRITE",
      [
        "storage",
        "011269f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48b3c.md#insn-00b48b64) · [`00b48b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48b3c.md#insn-00b48b6c) · [`00b48b48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48b3c.md#insn-00b48b48)
- 新版 [`00b49b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49b30.md#insn-00b49b58) · [`00b49b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49b30.md#insn-00b49b60) · [`00b49b3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49b30.md#insn-00b49b3c)

~~~diff
- 00b48b64 ["INT_ADD", "register:40f0:8", ["const:b48b64:8", "const:4:8"]]
- 00b48b64 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b49b58 ["INT_ADD", "register:40f0:8", ["const:b49b58:8", "const:4:8"]]
+ 00b49b58 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48b64 bytes 1f490494
+ 00b49b58 bytes 16490494
- 00b48b6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a30:8"]]
- 00b48b6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49b60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9f0:8"]]
+ 00b49b60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48b6c bytes 601a05f9
+ 00b49b60 bytes 60fa04f9
- 00b48b48 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49b3c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b48b48 bytes f32e00b0
+ 00b49b3c bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61a96ea71d3b663948be6a80dc67335e"></a>

### [`00b48b8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48b8c.md) → [`00b49b80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49b80.md) _ZN8firebase4util15character_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b49c08",
      "incomplete_value": true,
      "site": "00b49c08",
      "value": [
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
      "definition_site": "00b48c14",
      "incomplete_value": true,
      "site": "00b48c14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a38:8"
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
      "definition_site": "00b49bb4",
      "incomplete_value": true,
      "site": "00b49bc0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "definition_site": "00b48bc0",
      "incomplete_value": true,
      "site": "00b48bcc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:a30:8"
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
      "00b49b94",
      "READ",
      [
        "storage",
        "01125a38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49bb4",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49c08",
      "WRITE",
      [
        "storage",
        "01125a38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49b94",
      "READ",
      [
        "storage",
        "011269f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49bb4",
      "READ",
      [
        "storage",
        "011269f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49c08",
      "WRITE",
      [
        "storage",
        "011269f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48b8c.md#insn-00b48bcc) · [`00b48c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48b8c.md#insn-00b48c14) · [`00b48b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48b8c.md#insn-00b48b9c)
- 新版 [`00b49bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49b80.md#insn-00b49bc0) · [`00b49c08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49b80.md#insn-00b49c08) · [`00b49b90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49b80.md#insn-00b49b90)

~~~diff
- 00b48bcc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48bcc ["INT_ADD", "register:40f0:8", ["const:b48bcc:8", "const:4:8"]]
- 00b48bcc ["CALLIND", null, ["register:0:8"]]
+ 00b49bc0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49bc0 ["INT_ADD", "register:40f0:8", ["const:b49bc0:8", "const:4:8"]]
+ 00b49bc0 ["CALLIND", null, ["register:0:8"]]
- 00b48bcc bytes 00013fd6
+ 00b49bc0 bytes 00013fd6
- 00b48c14 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b48c14 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a38:8"]]
- 00b48c14 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b49c08 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b49c08 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9f8:8"]]
+ 00b49c08 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b48c14 bytes a0e22839
+ 00b49c08 bytes a0e22739
- 00b48b9c ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b49b90 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b48b9c bytes f52e00b0
+ 00b49b90 bytes f52e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2cf424c17a77d6607cf60df80f03cbad"></a>

### [`00b48c28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48c28.md) → [`00b49c1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49c1c.md) _ZN8firebase4util15character_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b49c58",
      "incomplete_value": true,
      "site": "00b49c58",
      "value": [
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
      "definition_site": "00b48c64",
      "incomplete_value": true,
      "site": "00b48c64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a38:8"
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
      "definition_site": "00b49ca8",
      "incomplete_value": true,
      "site": "00b49ca8",
      "value": [
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
      "definition_site": "00b48cb4",
      "incomplete_value": true,
      "site": "00b48cb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "definition_site": "00b49c34",
      "incomplete_value": true,
      "site": "00b49c34",
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
      "definition_site": "00b48c40",
      "incomplete_value": true,
      "site": "00b48c40",
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
      "00b49c30",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49c3c",
      "READ",
      [
        "storage",
        "01125a38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49c58",
      "WRITE",
      [
        "storage",
        "01125a38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49c30",
      "READ",
      [
        "storage",
        "011269f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49c3c",
      "READ",
      [
        "storage",
        "011269f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49c58",
      "WRITE",
      [
        "storage",
        "011269f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48c28.md#insn-00b48c64) · [`00b48cb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48c28.md#insn-00b48cb0) · [`00b48cb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48c28.md#insn-00b48cb4)
- 新版 [`00b49c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49c1c.md#insn-00b49c58) · [`00b49ca4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49c1c.md#insn-00b49ca4) · [`00b49ca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49c1c.md#insn-00b49ca8)

~~~diff
- 00b48c64 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b48c64 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b48c64 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a38:8"]]
- 00b48c64 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b49c58 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b49c58 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b49c58 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9f8:8"]]
+ 00b49c58 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b48c64 bytes bfe22839
+ 00b49c58 bytes bfe22739
- 00b48cb0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48cb0 ["INT_ADD", "register:40f0:8", ["const:b48cb0:8", "const:4:8"]]
- 00b48cb0 ["CALLIND", null, ["register:0:8"]]
+ 00b49ca4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49ca4 ["INT_ADD", "register:40f0:8", ["const:b49ca4:8", "const:4:8"]]
+ 00b49ca4 ["CALLIND", null, ["register:0:8"]]
- 00b48cb0 bytes 00013fd6
+ 00b49ca4 bytes 00013fd6
- 00b48cb4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a30:8"]]
- 00b48cb4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b48cb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b49ca8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
+ 00b49ca8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b49ca8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b48cb4 bytes 9f1a05f9
+ 00b49ca8 bytes 9ffa04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4d6c13783ab1d6e24c8e3fce7a3b3423"></a>

### [`00b48cc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48cc8.md) → [`00b49cbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49cbc.md) _ZN8firebase4util15character_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b49cfc",
      "incomplete_value": true,
      "site": "00b49cfc",
      "value": [
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
      "definition_site": "00b48d08",
      "incomplete_value": true,
      "site": "00b48d08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "definition_site": "00b49cd8",
      "incomplete_value": true,
      "site": "00b49cd8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48ce4",
      "incomplete_value": true,
      "site": "00b48ce4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49ce0",
      "incomplete_value": false,
      "site": "00b49cf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:e83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48cec",
      "incomplete_value": false,
      "site": "00b48d00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bb000:8"
          ],
          [
            "leaf",
            "const:da5:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49cd0",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49ce0",
      "PARAM",
      [
        "storage",
        "002bbda5",
        null,
        "string"
      ]
    ],
    [
      "00b49cfc",
      "WRITE",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49cd0",
      "READ",
      [
        "storage",
        "011269f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49ce0",
      "PARAM",
      [
        "storage",
        "002bbe83",
        null,
        "string"
      ]
    ],
    [
      "00b49cfc",
      "WRITE",
      [
        "storage",
        "011269f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48cc8.md#insn-00b48d00) · [`00b48d08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48cc8.md#insn-00b48d08) · [`00b48cd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48cc8.md#insn-00b48cd4)
- 新版 [`00b49cf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49cbc.md#insn-00b49cf4) · [`00b49cfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49cbc.md#insn-00b49cfc) · [`00b49cc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49cbc.md#insn-00b49cc8)

~~~diff
- 00b48d00 ["INT_ADD", "register:40f0:8", ["const:b48d00:8", "const:4:8"]]
- 00b48d00 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b49cf4 ["INT_ADD", "register:40f0:8", ["const:b49cf4:8", "const:4:8"]]
+ 00b49cf4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48d00 bytes b8480494
+ 00b49cf4 bytes af480494
- 00b48d08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a30:8"]]
- 00b48d08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49cfc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
+ 00b49cfc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48d08 bytes 801a05f9
+ 00b49cfc bytes 80fa04f9
- 00b48cd4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b49cc8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b48cd4 bytes f42e00b0
+ 00b49cc8 bytes f42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b34dd4d9e41c3d0c4f36421998702d4"></a>

### [`00b48d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48d38.md) → [`00b49d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49d2c.md) _ZN8firebase4util15character_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b49d48",
      "incomplete_value": false,
      "site": "00b49d4c",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48d54",
      "incomplete_value": false,
      "site": "00b48d58",
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
            "const:30b:8"
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
      "definition_site": "00b49d58",
      "incomplete_value": true,
      "site": "00b49d64",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b48d64",
      "incomplete_value": true,
      "site": "00b48d70",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b49d48",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b49d58",
      "DATA",
      [
        "storage",
        "01125a40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49d48",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b49d58",
      "DATA",
      [
        "storage",
        "01126a00",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48d58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48d38.md#insn-00b48d58) · [`00b48d54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48d38.md#insn-00b48d54) · [`00b48d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48d38.md#insn-00b48d5c)
- 新版 [`00b49d4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49d2c.md#insn-00b49d4c) · [`00b49d48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49d2c.md#insn-00b49d48) · [`00b49d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49d2c.md#insn-00b49d50)

~~~diff
- 00b48d58 ["INT_ADD", "register:40f0:8", ["const:b48d58:8", "const:4:8"]]
- 00b48d58 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b49d4c ["INT_ADD", "register:40f0:8", ["const:b49d4c:8", "const:4:8"]]
+ 00b49d4c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b48d58 bytes de480494
+ 00b49d4c bytes d5480494
- 00b48d54 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b48d54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b48d54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b48d54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49d48 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b49d48 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49d48 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49d48 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b48d54 bytes 002c0c91
+ 00b49d48 bytes 008c1191
- 00b48d5c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b49d50 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b48d5c bytes e82e00b0
+ 00b49d50 bytes e82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21c33e3d5f9fb8ceb0f22c04b94b1c46"></a>

### [`00b48d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48d74.md) → [`00b49d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49d68.md) _ZN8firebase4util15character_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b49da8",
      "incomplete_value": true,
      "site": "00b49da8",
      "value": [
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
      "definition_site": "00b48db4",
      "incomplete_value": true,
      "site": "00b48db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a30:8"
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
      "definition_site": "00b49d84",
      "incomplete_value": true,
      "site": "00b49d84",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48d90",
      "incomplete_value": true,
      "site": "00b48d90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b48d90"
      ],
      [
        "FALL_THROUGH",
        "00b49d84"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b49d84",
      "incomplete_value": true,
      "site": "00b49da8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48d90",
      "incomplete_value": true,
      "site": "00b48db4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b49d7c",
      "READ",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49d8c",
      "PARAM",
      [
        "storage",
        "002bbda5",
        null,
        "string"
      ]
    ],
    [
      "00b49da8",
      "WRITE",
      [
        "storage",
        "01125a30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49d7c",
      "READ",
      [
        "storage",
        "011269f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49d8c",
      "PARAM",
      [
        "storage",
        "002bbe83",
        null,
        "string"
      ]
    ],
    [
      "00b49da8",
      "WRITE",
      [
        "storage",
        "011269f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48d74.md#insn-00b48db4) · [`00b48d80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48d74.md#insn-00b48d80) · [`00b48d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48d74.md#insn-00b48d88)
- 新版 [`00b49da8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49d68.md#insn-00b49da8) · [`00b49d74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49d68.md#insn-00b49d74) · [`00b49d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49d68.md#insn-00b49d7c)

~~~diff
- 00b48db4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a30:8"]]
- 00b48db4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49da8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
+ 00b49da8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48db4 bytes 801a05f9
+ 00b49da8 bytes 80fa04f9
- 00b48d80 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b49d74 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b48d80 bytes f42e00b0
+ 00b49d74 bytes f42e00b0
- 00b48d88 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a30:8"]]
- 00b48d88 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b49d7c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9f0:8"]]
+ 00b49d7c ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48d88 bytes 811a45f9
+ 00b49d7c bytes 81fa44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14cf00439ccb1f5cfee9d4d57c724800"></a>

### [`00b48de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48de4.md) → [`00b49dd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49dd8.md) _ZN8firebase4util15character_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b49df4",
      "incomplete_value": false,
      "site": "00b49df8",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48e00",
      "incomplete_value": false,
      "site": "00b48e04",
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
            "const:54d:8"
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
      "definition_site": "00b49e04",
      "incomplete_value": true,
      "site": "00b49e10",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b48e10",
      "incomplete_value": true,
      "site": "00b48e1c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b49df4",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b49e04",
      "DATA",
      [
        "storage",
        "01125a50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b49df4",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b49e04",
      "DATA",
      [
        "storage",
        "01126a10",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48e04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48de4.md#insn-00b48e04) · [`00b48e00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48de4.md#insn-00b48e00) · [`00b48e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48de4.md#insn-00b48e08)
- 新版 [`00b49df8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49dd8.md#insn-00b49df8) · [`00b49df4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49dd8.md#insn-00b49df4) · [`00b49dfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49dd8.md#insn-00b49dfc)

~~~diff
- 00b48e04 ["INT_ADD", "register:40f0:8", ["const:b48e04:8", "const:4:8"]]
- 00b48e04 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b49df8 ["INT_ADD", "register:40f0:8", ["const:b49df8:8", "const:4:8"]]
+ 00b49df8 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b48e04 bytes b3480494
+ 00b49df8 bytes aa480494
- 00b48e00 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b48e00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b48e00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b48e00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49df4 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b49df4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49df4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49df4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b48e00 bytes 00341591
+ 00b49df4 bytes 00681891
- 00b48e08 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b49dfc ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b48e08 bytes e82e00b0
+ 00b49dfc bytes e82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-47d2abd6e05f08ff91ceec4483a58fe2"></a>

### [`00b48e20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48e20.md) → [`00b49e14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49e14.md) _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b49e40",
      "incomplete_value": true,
      "site": "00b49e40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48e4c",
      "incomplete_value": true,
      "site": "00b48e4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "definition_site": "00b49e28",
      "incomplete_value": true,
      "site": "00b49e28",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48e34",
      "incomplete_value": true,
      "site": "00b48e34",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49e34",
      "incomplete_value": true,
      "site": "00b49e38",
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
            "const:50a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48e40",
      "incomplete_value": true,
      "site": "00b48e44",
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
            "const:3b2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49e24",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49e34",
      "PARAM",
      [
        "storage",
        "002a83b2",
        null,
        "string"
      ]
    ],
    [
      "00b49e40",
      "WRITE",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49e24",
      "READ",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49e34",
      "PARAM",
      [
        "storage",
        "002a850a",
        null,
        "string"
      ]
    ],
    [
      "00b49e40",
      "WRITE",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48e44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48e20.md#insn-00b48e44) · [`00b48e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48e20.md#insn-00b48e4c) · [`00b48e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48e20.md#insn-00b48e2c)
- 新版 [`00b49e38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49e14.md#insn-00b49e38) · [`00b49e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49e14.md#insn-00b49e40) · [`00b49e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49e14.md#insn-00b49e20)

~~~diff
- 00b48e44 ["INT_ADD", "register:40f0:8", ["const:b48e44:8", "const:4:8"]]
- 00b48e44 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b49e38 ["INT_ADD", "register:40f0:8", ["const:b49e38:8", "const:4:8"]]
+ 00b49e38 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48e44 bytes 67480494
+ 00b49e38 bytes 5e480494
- 00b48e4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a58:8"]]
- 00b48e4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49e40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
+ 00b49e40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48e4c bytes 602e05f9
+ 00b49e40 bytes 600e05f9
- 00b48e2c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49e20 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b48e2c bytes f32e00b0
+ 00b49e20 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ee48b4ce6b7de66e81cbfb1b5d2388ec"></a>

### [`00b48e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48e60.md) → [`00b49e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49e54.md) _ZN8firebase4util11class_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b49e80",
      "incomplete_value": true,
      "site": "00b49e80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48e8c",
      "incomplete_value": true,
      "site": "00b48e8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "definition_site": "00b49e68",
      "incomplete_value": true,
      "site": "00b49e68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48e74",
      "incomplete_value": true,
      "site": "00b48e74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49e70",
      "incomplete_value": false,
      "site": "00b49e78",
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
            "const:50a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48e7c",
      "incomplete_value": false,
      "site": "00b48e84",
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
            "const:3b2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49e64",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49e70",
      "PARAM",
      [
        "storage",
        "002a83b2",
        null,
        "string"
      ]
    ],
    [
      "00b49e80",
      "WRITE",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49e64",
      "READ",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49e70",
      "PARAM",
      [
        "storage",
        "002a850a",
        null,
        "string"
      ]
    ],
    [
      "00b49e80",
      "WRITE",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48e84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48e60.md#insn-00b48e84) · [`00b48e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48e60.md#insn-00b48e8c) · [`00b48e6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48e60.md#insn-00b48e6c)
- 新版 [`00b49e78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49e54.md#insn-00b49e78) · [`00b49e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49e54.md#insn-00b49e80) · [`00b49e60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49e54.md#insn-00b49e60)

~~~diff
- 00b48e84 ["INT_ADD", "register:40f0:8", ["const:b48e84:8", "const:4:8"]]
- 00b48e84 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b49e78 ["INT_ADD", "register:40f0:8", ["const:b49e78:8", "const:4:8"]]
+ 00b49e78 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48e84 bytes 57480494
+ 00b49e78 bytes 4e480494
- 00b48e8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a58:8"]]
- 00b48e8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49e80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
+ 00b49e80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48e8c bytes 602e05f9
+ 00b49e80 bytes 600e05f9
- 00b48e6c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49e60 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b48e6c bytes f32e00b0
+ 00b49e60 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fff1441f0d808ec1aea7b90508296b2c"></a>

### [`00b48ea0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ea0.md) → [`00b49e94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49e94.md) _ZN8firebase4util11class_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b49ec4",
      "incomplete_value": true,
      "site": "00b49ec4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48ed0",
      "incomplete_value": true,
      "site": "00b48ed0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "definition_site": "00b49ea8",
      "incomplete_value": true,
      "site": "00b49ea8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48eb4",
      "incomplete_value": true,
      "site": "00b48eb4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49eb4",
      "incomplete_value": false,
      "site": "00b49ebc",
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
            "const:50a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48ec0",
      "incomplete_value": false,
      "site": "00b48ec8",
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
            "const:3b2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49ea4",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49eb4",
      "PARAM",
      [
        "storage",
        "002a83b2",
        null,
        "string"
      ]
    ],
    [
      "00b49ec4",
      "WRITE",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49ea4",
      "READ",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49eb4",
      "PARAM",
      [
        "storage",
        "002a850a",
        null,
        "string"
      ]
    ],
    [
      "00b49ec4",
      "WRITE",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48ec8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ea0.md#insn-00b48ec8) · [`00b48ed0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ea0.md#insn-00b48ed0) · [`00b48eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ea0.md#insn-00b48eac)
- 新版 [`00b49ebc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49e94.md#insn-00b49ebc) · [`00b49ec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49e94.md#insn-00b49ec4) · [`00b49ea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49e94.md#insn-00b49ea0)

~~~diff
- 00b48ec8 ["INT_ADD", "register:40f0:8", ["const:b48ec8:8", "const:4:8"]]
- 00b48ec8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b49ebc ["INT_ADD", "register:40f0:8", ["const:b49ebc:8", "const:4:8"]]
+ 00b49ebc ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48ec8 bytes 46480494
+ 00b49ebc bytes 3d480494
- 00b48ed0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a58:8"]]
- 00b48ed0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49ec4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
+ 00b49ec4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48ed0 bytes 602e05f9
+ 00b49ec4 bytes 600e05f9
- 00b48eac ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49ea0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b48eac bytes f32e00b0
+ 00b49ea0 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-412f3db56157b75152a463ce018accf5"></a>

### [`00b48ee4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ee4.md) → [`00b49ed8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49ed8.md) _ZN8firebase4util11class_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b49f08",
      "incomplete_value": true,
      "site": "00b49f08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48f14",
      "incomplete_value": true,
      "site": "00b48f14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "definition_site": "00b49eec",
      "incomplete_value": true,
      "site": "00b49eec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48ef8",
      "incomplete_value": true,
      "site": "00b48ef8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49ef4",
      "incomplete_value": false,
      "site": "00b49f00",
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
            "const:50a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48f00",
      "incomplete_value": false,
      "site": "00b48f0c",
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
            "const:3b2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49ee8",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49ef4",
      "PARAM",
      [
        "storage",
        "002a83b2",
        null,
        "string"
      ]
    ],
    [
      "00b49f08",
      "WRITE",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49ee8",
      "READ",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49ef4",
      "PARAM",
      [
        "storage",
        "002a850a",
        null,
        "string"
      ]
    ],
    [
      "00b49f08",
      "WRITE",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ee4.md#insn-00b48f0c) · [`00b48f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ee4.md#insn-00b48f14) · [`00b48ef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48ee4.md#insn-00b48ef0)
- 新版 [`00b49f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49ed8.md#insn-00b49f00) · [`00b49f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49ed8.md#insn-00b49f08) · [`00b49ee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49ed8.md#insn-00b49ee4)

~~~diff
- 00b48f0c ["INT_ADD", "register:40f0:8", ["const:b48f0c:8", "const:4:8"]]
- 00b48f0c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b49f00 ["INT_ADD", "register:40f0:8", ["const:b49f00:8", "const:4:8"]]
+ 00b49f00 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48f0c bytes 35480494
+ 00b49f00 bytes 2c480494
- 00b48f14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a58:8"]]
- 00b48f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49f08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a18:8"]]
+ 00b49f08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48f14 bytes 602e05f9
+ 00b49f08 bytes 600e05f9
- 00b48ef0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49ee4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b48ef0 bytes f32e00b0
+ 00b49ee4 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b8b0c73da7407cb1cbaffdb89428285"></a>

### [`00b48f34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48f34.md) → [`00b49f28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49f28.md) _ZN8firebase4util11class_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b49fb0",
      "incomplete_value": true,
      "site": "00b49fb0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48fbc",
      "incomplete_value": true,
      "site": "00b48fbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
      "definition_site": "00b49f5c",
      "incomplete_value": true,
      "site": "00b49f68",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:a18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48f68",
      "incomplete_value": true,
      "site": "00b48f74",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:a58:8"
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
      "00b49f3c",
      "READ",
      [
        "storage",
        "01125a60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49f5c",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49fb0",
      "WRITE",
      [
        "storage",
        "01125a60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49f3c",
      "READ",
      [
        "storage",
        "01126a20",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49f5c",
      "READ",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49fb0",
      "WRITE",
      [
        "storage",
        "01126a20",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48f34.md#insn-00b48f74) · [`00b48fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48f34.md#insn-00b48fbc) · [`00b48f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48f34.md#insn-00b48f44)
- 新版 [`00b49f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49f28.md#insn-00b49f68) · [`00b49fb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49f28.md#insn-00b49fb0) · [`00b49f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49f28.md#insn-00b49f38)

~~~diff
- 00b48f74 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48f74 ["INT_ADD", "register:40f0:8", ["const:b48f74:8", "const:4:8"]]
- 00b48f74 ["CALLIND", null, ["register:0:8"]]
+ 00b49f68 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49f68 ["INT_ADD", "register:40f0:8", ["const:b49f68:8", "const:4:8"]]
+ 00b49f68 ["CALLIND", null, ["register:0:8"]]
- 00b48f74 bytes 00013fd6
+ 00b49f68 bytes 00013fd6
- 00b48fbc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b48fbc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a60:8"]]
- 00b48fbc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b49fb0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b49fb0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a20:8"]]
+ 00b49fb0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b48fbc bytes a0822939
+ 00b49fb0 bytes a0822839
- 00b48f44 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b49f38 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b48f44 bytes f52e00b0
+ 00b49f38 bytes f52e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-04bffa88293c6dfedaab182cdd59f22b"></a>

### [`00b48fd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48fd0.md) → [`00b49fc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49fc4.md) _ZN8firebase4util11class_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4a000",
      "incomplete_value": true,
      "site": "00b4a000",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4900c",
      "incomplete_value": true,
      "site": "00b4900c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a60:8"
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
      "definition_site": "00b4a050",
      "incomplete_value": true,
      "site": "00b4a050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4905c",
      "incomplete_value": true,
      "site": "00b4905c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "definition_site": "00b49fdc",
      "incomplete_value": true,
      "site": "00b49fdc",
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
      "definition_site": "00b48fe8",
      "incomplete_value": true,
      "site": "00b48fe8",
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
      "00b49fd8",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49fe4",
      "READ",
      [
        "storage",
        "01125a60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a000",
      "WRITE",
      [
        "storage",
        "01125a60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49fd8",
      "READ",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49fe4",
      "READ",
      [
        "storage",
        "01126a20",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a000",
      "WRITE",
      [
        "storage",
        "01126a20",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4900c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48fd0.md#insn-00b4900c) · [`00b49058`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48fd0.md#insn-00b49058) · [`00b4905c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48fd0.md#insn-00b4905c)
- 新版 [`00b4a000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49fc4.md#insn-00b4a000) · [`00b4a04c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49fc4.md#insn-00b4a04c) · [`00b4a050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49fc4.md#insn-00b4a050)

~~~diff
- 00b4900c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4900c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4900c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a60:8"]]
- 00b4900c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4a000 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4a000 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4a000 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a20:8"]]
+ 00b4a000 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4900c bytes bf822939
+ 00b4a000 bytes bf822839
- 00b49058 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49058 ["INT_ADD", "register:40f0:8", ["const:b49058:8", "const:4:8"]]
- 00b49058 ["CALLIND", null, ["register:0:8"]]
+ 00b4a04c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a04c ["INT_ADD", "register:40f0:8", ["const:b4a04c:8", "const:4:8"]]
+ 00b4a04c ["CALLIND", null, ["register:0:8"]]
- 00b49058 bytes 00013fd6
+ 00b4a04c bytes 00013fd6
- 00b4905c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a58:8"]]
- 00b4905c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4905c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4a050 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a18:8"]]
+ 00b4a050 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4a050 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4905c bytes 9f2e05f9
+ 00b4a050 bytes 9f0e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fabd2de7554484906189f6a8c0b3cdf8"></a>

### [`00b49070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49070.md) → [`00b4a064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a064.md) _ZN8firebase4util11class_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b4a0a4",
      "incomplete_value": true,
      "site": "00b4a0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b490b0",
      "incomplete_value": true,
      "site": "00b490b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "definition_site": "00b4a080",
      "incomplete_value": true,
      "site": "00b4a080",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4908c",
      "incomplete_value": true,
      "site": "00b4908c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a088",
      "incomplete_value": true,
      "site": "00b4a09c",
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
            "const:50a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49094",
      "incomplete_value": true,
      "site": "00b490a8",
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
            "const:3b2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a078",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a088",
      "PARAM",
      [
        "storage",
        "002a83b2",
        null,
        "string"
      ]
    ],
    [
      "00b4a0a4",
      "WRITE",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a078",
      "READ",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a088",
      "PARAM",
      [
        "storage",
        "002a850a",
        null,
        "string"
      ]
    ],
    [
      "00b4a0a4",
      "WRITE",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b490a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49070.md#insn-00b490a8) · [`00b490b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49070.md#insn-00b490b0) · [`00b4907c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49070.md#insn-00b4907c)
- 新版 [`00b4a09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a064.md#insn-00b4a09c) · [`00b4a0a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a064.md#insn-00b4a0a4) · [`00b4a070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a064.md#insn-00b4a070)

~~~diff
- 00b490a8 ["INT_ADD", "register:40f0:8", ["const:b490a8:8", "const:4:8"]]
- 00b490a8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a09c ["INT_ADD", "register:40f0:8", ["const:b4a09c:8", "const:4:8"]]
+ 00b4a09c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b490a8 bytes ce470494
+ 00b4a09c bytes c5470494
- 00b490b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a58:8"]]
- 00b490b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a0a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a18:8"]]
+ 00b4a0a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b490b0 bytes 802e05f9
+ 00b4a0a4 bytes 800e05f9
- 00b4907c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4a070 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4907c bytes f42e0090
+ 00b4a070 bytes f42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe3415fc3b2908c812a9d806988c8656"></a>

### [`00b490e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b490e0.md) → [`00b4a0d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a0d4.md) _ZN8firebase4util11class_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4a0f0",
      "incomplete_value": false,
      "site": "00b4a0f4",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b490fc",
      "incomplete_value": false,
      "site": "00b49100",
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
            "const:30b:8"
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
      "definition_site": "00b4a100",
      "incomplete_value": true,
      "site": "00b4a10c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b4910c",
      "incomplete_value": true,
      "site": "00b49118",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4a0f0",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4a100",
      "DATA",
      [
        "storage",
        "01125a68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a0f0",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4a100",
      "DATA",
      [
        "storage",
        "01126a28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49100`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b490e0.md#insn-00b49100) · [`00b490fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b490e0.md#insn-00b490fc) · [`00b49104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b490e0.md#insn-00b49104)
- 新版 [`00b4a0f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a0d4.md#insn-00b4a0f4) · [`00b4a0f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a0d4.md#insn-00b4a0f0) · [`00b4a0f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a0d4.md#insn-00b4a0f8)

~~~diff
- 00b49100 ["INT_ADD", "register:40f0:8", ["const:b49100:8", "const:4:8"]]
- 00b49100 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4a0f4 ["INT_ADD", "register:40f0:8", ["const:b4a0f4:8", "const:4:8"]]
+ 00b4a0f4 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b49100 bytes f4470494
+ 00b4a0f4 bytes eb470494
- 00b490fc ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b490fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b490fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b490fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a0f0 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4a0f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a0f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a0f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b490fc bytes 002c0c91
+ 00b4a0f0 bytes 008c1191
- 00b49104 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4a0f8 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b49104 bytes e82e0090
+ 00b4a0f8 bytes e82e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0cf709d325d3e841e11616fe431dbdc0"></a>

### [`00b4911c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4911c.md) → [`00b4a110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a110.md) _ZN8firebase4util11class_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4a150",
      "incomplete_value": true,
      "site": "00b4a150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4915c",
      "incomplete_value": true,
      "site": "00b4915c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a58:8"
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
      "definition_site": "00b4a12c",
      "incomplete_value": true,
      "site": "00b4a12c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49138",
      "incomplete_value": true,
      "site": "00b49138",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a134",
      "incomplete_value": false,
      "site": "00b4a148",
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
            "const:50a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49140",
      "incomplete_value": false,
      "site": "00b49154",
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
            "const:3b2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a124",
      "READ",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a134",
      "PARAM",
      [
        "storage",
        "002a83b2",
        null,
        "string"
      ]
    ],
    [
      "00b4a150",
      "WRITE",
      [
        "storage",
        "01125a58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a124",
      "READ",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a134",
      "PARAM",
      [
        "storage",
        "002a850a",
        null,
        "string"
      ]
    ],
    [
      "00b4a150",
      "WRITE",
      [
        "storage",
        "01126a18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4911c.md#insn-00b49154) · [`00b4915c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4911c.md#insn-00b4915c) · [`00b49128`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4911c.md#insn-00b49128)
- 新版 [`00b4a148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a110.md#insn-00b4a148) · [`00b4a150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a110.md#insn-00b4a150) · [`00b4a11c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a110.md#insn-00b4a11c)

~~~diff
- 00b49154 ["INT_ADD", "register:40f0:8", ["const:b49154:8", "const:4:8"]]
- 00b49154 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a148 ["INT_ADD", "register:40f0:8", ["const:b4a148:8", "const:4:8"]]
+ 00b4a148 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b49154 bytes a3470494
+ 00b4a148 bytes 9a470494
- 00b4915c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a58:8"]]
- 00b4915c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a150 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a18:8"]]
+ 00b4a150 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4915c bytes 802e05f9
+ 00b4a150 bytes 800e05f9
- 00b49128 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4a11c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b49128 bytes f42e0090
+ 00b4a11c bytes f42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0da3059d384e1a555294e52336ad0ec2"></a>

### [`00b4918c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4918c.md) → [`00b4a180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a180.md) _ZN8firebase4util11class_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4a19c",
      "incomplete_value": false,
      "site": "00b4a1a0",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b491a8",
      "incomplete_value": false,
      "site": "00b491ac",
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
            "const:54d:8"
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
      "definition_site": "00b4a1ac",
      "incomplete_value": true,
      "site": "00b4a1b8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b491b8",
      "incomplete_value": true,
      "site": "00b491c4",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4a19c",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4a1ac",
      "DATA",
      [
        "storage",
        "01125a78",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a19c",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4a1ac",
      "DATA",
      [
        "storage",
        "01126a38",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b491ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4918c.md#insn-00b491ac) · [`00b491a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4918c.md#insn-00b491a8) · [`00b491b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4918c.md#insn-00b491b0)
- 新版 [`00b4a1a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a180.md#insn-00b4a1a0) · [`00b4a19c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a180.md#insn-00b4a19c) · [`00b4a1a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a180.md#insn-00b4a1a4)

~~~diff
- 00b491ac ["INT_ADD", "register:40f0:8", ["const:b491ac:8", "const:4:8"]]
- 00b491ac ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4a1a0 ["INT_ADD", "register:40f0:8", ["const:b4a1a0:8", "const:4:8"]]
+ 00b4a1a0 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b491ac bytes c9470494
+ 00b4a1a0 bytes c0470494
- 00b491a8 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b491a8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b491a8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b491a8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a19c ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4a19c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a19c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a19c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b491a8 bytes 00341591
+ 00b4a19c bytes 00681891
- 00b491b0 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4a1a4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b491b0 bytes e82e0090
+ 00b4a1a4 bytes e82e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2b53033d03dc0c53802b9ba2a663c5db"></a>

### [`00b491c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b491c8.md) → [`00b4a1bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a1bc.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4a1e8",
      "incomplete_value": true,
      "site": "00b4a1e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b491f4",
      "incomplete_value": true,
      "site": "00b491f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "definition_site": "00b4a1d0",
      "incomplete_value": true,
      "site": "00b4a1d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b491dc",
      "incomplete_value": true,
      "site": "00b491dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a1dc",
      "incomplete_value": false,
      "site": "00b4a1e0",
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
            "const:3ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b491e8",
      "incomplete_value": false,
      "site": "00b491ec",
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
            "const:2e3:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a1cc",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a1dc",
      "PARAM",
      [
        "storage",
        "002af2e3",
        null,
        "string"
      ]
    ],
    [
      "00b4a1e8",
      "WRITE",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a1cc",
      "READ",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a1dc",
      "PARAM",
      [
        "storage",
        "002af3ba",
        null,
        "string"
      ]
    ],
    [
      "00b4a1e8",
      "WRITE",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b491ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b491c8.md#insn-00b491ec) · [`00b491f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b491c8.md#insn-00b491f4) · [`00b491d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b491c8.md#insn-00b491d4)
- 新版 [`00b4a1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a1bc.md#insn-00b4a1e0) · [`00b4a1e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a1bc.md#insn-00b4a1e8) · [`00b4a1c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a1bc.md#insn-00b4a1c8)

~~~diff
- 00b491ec ["INT_ADD", "register:40f0:8", ["const:b491ec:8", "const:4:8"]]
- 00b491ec ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a1e0 ["INT_ADD", "register:40f0:8", ["const:b4a1e0:8", "const:4:8"]]
+ 00b4a1e0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b491ec bytes 7d470494
+ 00b4a1e0 bytes 74470494
- 00b491f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a80:8"]]
- 00b491f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a1e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
+ 00b4a1e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b491f4 bytes 604205f9
+ 00b4a1e8 bytes 602205f9
- 00b491d4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4a1c8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b491d4 bytes f32e0090
+ 00b4a1c8 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bdaca9097d7de15740b9772e62153e1f"></a>

### [`00b49208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49208.md) → [`00b4a1fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a1fc.md) _ZN8firebase4util16content_resolver19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4a228",
      "incomplete_value": true,
      "site": "00b4a228",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49234",
      "incomplete_value": true,
      "site": "00b49234",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "definition_site": "00b4a210",
      "incomplete_value": true,
      "site": "00b4a210",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4921c",
      "incomplete_value": true,
      "site": "00b4921c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a218",
      "incomplete_value": false,
      "site": "00b4a220",
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
            "const:3ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49224",
      "incomplete_value": false,
      "site": "00b4922c",
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
            "const:2e3:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a20c",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a218",
      "PARAM",
      [
        "storage",
        "002af2e3",
        null,
        "string"
      ]
    ],
    [
      "00b4a228",
      "WRITE",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a20c",
      "READ",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a218",
      "PARAM",
      [
        "storage",
        "002af3ba",
        null,
        "string"
      ]
    ],
    [
      "00b4a228",
      "WRITE",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4922c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49208.md#insn-00b4922c) · [`00b49234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49208.md#insn-00b49234) · [`00b49214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49208.md#insn-00b49214)
- 新版 [`00b4a220`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a1fc.md#insn-00b4a220) · [`00b4a228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a1fc.md#insn-00b4a228) · [`00b4a208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a1fc.md#insn-00b4a208)

~~~diff
- 00b4922c ["INT_ADD", "register:40f0:8", ["const:b4922c:8", "const:4:8"]]
- 00b4922c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a220 ["INT_ADD", "register:40f0:8", ["const:b4a220:8", "const:4:8"]]
+ 00b4a220 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4922c bytes 6d470494
+ 00b4a220 bytes 64470494
- 00b49234 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a80:8"]]
- 00b49234 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a228 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
+ 00b4a228 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49234 bytes 604205f9
+ 00b4a228 bytes 602205f9
- 00b49214 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4a208 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b49214 bytes f32e0090
+ 00b4a208 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-436a5acb9055a7f58b7e109c137a7ffd"></a>

### [`00b49248`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49248.md) → [`00b4a23c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a23c.md) _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4a26c",
      "incomplete_value": true,
      "site": "00b4a26c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49278",
      "incomplete_value": true,
      "site": "00b49278",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "definition_site": "00b4a250",
      "incomplete_value": true,
      "site": "00b4a250",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4925c",
      "incomplete_value": true,
      "site": "00b4925c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a25c",
      "incomplete_value": false,
      "site": "00b4a264",
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
            "const:3ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49268",
      "incomplete_value": false,
      "site": "00b49270",
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
            "const:2e3:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a24c",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a25c",
      "PARAM",
      [
        "storage",
        "002af2e3",
        null,
        "string"
      ]
    ],
    [
      "00b4a26c",
      "WRITE",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a24c",
      "READ",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a25c",
      "PARAM",
      [
        "storage",
        "002af3ba",
        null,
        "string"
      ]
    ],
    [
      "00b4a26c",
      "WRITE",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49270`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49248.md#insn-00b49270) · [`00b49278`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49248.md#insn-00b49278) · [`00b49254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49248.md#insn-00b49254)
- 新版 [`00b4a264`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a23c.md#insn-00b4a264) · [`00b4a26c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a23c.md#insn-00b4a26c) · [`00b4a248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a23c.md#insn-00b4a248)

~~~diff
- 00b49270 ["INT_ADD", "register:40f0:8", ["const:b49270:8", "const:4:8"]]
- 00b49270 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a264 ["INT_ADD", "register:40f0:8", ["const:b4a264:8", "const:4:8"]]
+ 00b4a264 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b49270 bytes 5c470494
+ 00b4a264 bytes 53470494
- 00b49278 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a80:8"]]
- 00b49278 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a26c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
+ 00b4a26c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49278 bytes 604205f9
+ 00b4a26c bytes 602205f9
- 00b49254 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4a248 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b49254 bytes f32e0090
+ 00b4a248 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79ac7779b83733b033df4b29bb6fcd4b"></a>

### [`00b4928c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4928c.md) → [`00b4a280`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a280.md) _ZN8firebase4util16content_resolver10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4a2b0",
      "incomplete_value": true,
      "site": "00b4a2b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b492bc",
      "incomplete_value": true,
      "site": "00b492bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "definition_site": "00b4a294",
      "incomplete_value": true,
      "site": "00b4a294",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b492a0",
      "incomplete_value": true,
      "site": "00b492a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a29c",
      "incomplete_value": false,
      "site": "00b4a2a8",
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
            "const:3ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b492a8",
      "incomplete_value": false,
      "site": "00b492b4",
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
            "const:2e3:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a290",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a29c",
      "PARAM",
      [
        "storage",
        "002af2e3",
        null,
        "string"
      ]
    ],
    [
      "00b4a2b0",
      "WRITE",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a290",
      "READ",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a29c",
      "PARAM",
      [
        "storage",
        "002af3ba",
        null,
        "string"
      ]
    ],
    [
      "00b4a2b0",
      "WRITE",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b492b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4928c.md#insn-00b492b4) · [`00b492bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4928c.md#insn-00b492bc) · [`00b49298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4928c.md#insn-00b49298)
- 新版 [`00b4a2a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a280.md#insn-00b4a2a8) · [`00b4a2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a280.md#insn-00b4a2b0) · [`00b4a28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a280.md#insn-00b4a28c)

~~~diff
- 00b492b4 ["INT_ADD", "register:40f0:8", ["const:b492b4:8", "const:4:8"]]
- 00b492b4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a2a8 ["INT_ADD", "register:40f0:8", ["const:b4a2a8:8", "const:4:8"]]
+ 00b4a2a8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b492b4 bytes 4b470494
+ 00b4a2a8 bytes 42470494
- 00b492bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a80:8"]]
- 00b492bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a2b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a40:8"]]
+ 00b4a2b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b492bc bytes 604205f9
+ 00b4a2b0 bytes 602205f9
- 00b49298 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4a28c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b49298 bytes f32e0090
+ 00b4a28c bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3aa63a24cbf6112a400b45b9a11365f9"></a>

### [`00b492d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b492d0.md) → [`00b4a2c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a2c4.md) _ZN8firebase4util16content_resolver8GetClassEv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 constant, operands_and_dependencies, return_value_candidate

命令の説明率　旧版 66.67% / 新版 66.67%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `return_value_candidate` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "return_value_candidate",
    "new": {
      "definition_site": "00b4a2c8",
      "incomplete_value": true,
      "site": "00b4a2cc",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b492d4",
      "incomplete_value": true,
      "site": "00b492d8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:a80:8"
              ]
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
      "00b4a2c8",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a2c8",
      "READ",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b492d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b492d0.md#insn-00b492d0) · [`00b492d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b492d0.md#insn-00b492d4)
- 新版 [`00b4a2c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a2c4.md#insn-00b4a2c4) · [`00b4a2c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a2c4.md#insn-00b4a2c8)

~~~diff
- 00b492d0 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4a2c4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b492d0 bytes e82e0090
+ 00b4a2c4 bytes e82e0090
- 00b492d4 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a80:8"]]
- 00b492d4 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4a2c8 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:a40:8"]]
+ 00b4a2c8 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b492d4 bytes 004145f9
+ 00b4a2c8 bytes 002145f9
~~~


<a id="compare-f524a91f447eb95736a43a30dbe7fb50"></a>

### [`00b492dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b492dc.md) → [`00b4a2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a2d0.md) _ZN8firebase4util16content_resolver15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4a358",
      "incomplete_value": true,
      "site": "00b4a358",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49364",
      "incomplete_value": true,
      "site": "00b49364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "definition_site": "00b4a304",
      "incomplete_value": true,
      "site": "00b4a310",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:a40:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49310",
      "incomplete_value": true,
      "site": "00b4931c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:a80:8"
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
      "00b4a2e4",
      "READ",
      [
        "storage",
        "01125a88",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a304",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a358",
      "WRITE",
      [
        "storage",
        "01125a88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a2e4",
      "READ",
      [
        "storage",
        "01126a48",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a304",
      "READ",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a358",
      "WRITE",
      [
        "storage",
        "01126a48",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4931c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b492dc.md#insn-00b4931c) · [`00b49364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b492dc.md#insn-00b49364) · [`00b492ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b492dc.md#insn-00b492ec)
- 新版 [`00b4a310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a2d0.md#insn-00b4a310) · [`00b4a358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a2d0.md#insn-00b4a358) · [`00b4a2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a2d0.md#insn-00b4a2e0)

~~~diff
- 00b4931c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4931c ["INT_ADD", "register:40f0:8", ["const:b4931c:8", "const:4:8"]]
- 00b4931c ["CALLIND", null, ["register:0:8"]]
+ 00b4a310 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a310 ["INT_ADD", "register:40f0:8", ["const:b4a310:8", "const:4:8"]]
+ 00b4a310 ["CALLIND", null, ["register:0:8"]]
- 00b4931c bytes 00013fd6
+ 00b4a310 bytes 00013fd6
- 00b49364 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b49364 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a88:8"]]
- 00b49364 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4a358 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4a358 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a48:8"]]
+ 00b4a358 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b49364 bytes a0222a39
+ 00b4a358 bytes a0222939
- 00b492ec ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4a2e0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b492ec bytes f52e0090
+ 00b4a2e0 bytes f52e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0faf3b194116cff47d565958b8c1a62e"></a>

### [`00b49378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49378.md) → [`00b4a36c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a36c.md) _ZN8firebase4util16content_resolver12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4a3a8",
      "incomplete_value": true,
      "site": "00b4a3a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b493b4",
      "incomplete_value": true,
      "site": "00b493b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a88:8"
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
      "definition_site": "00b4a3f8",
      "incomplete_value": true,
      "site": "00b4a3f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49404",
      "incomplete_value": true,
      "site": "00b49404",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "definition_site": "00b4a384",
      "incomplete_value": true,
      "site": "00b4a384",
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
      "definition_site": "00b49390",
      "incomplete_value": true,
      "site": "00b49390",
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
      "00b4a380",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a38c",
      "READ",
      [
        "storage",
        "01125a88",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a3a8",
      "WRITE",
      [
        "storage",
        "01125a88",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a380",
      "READ",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a38c",
      "READ",
      [
        "storage",
        "01126a48",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a3a8",
      "WRITE",
      [
        "storage",
        "01126a48",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b493b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49378.md#insn-00b493b4) · [`00b49400`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49378.md#insn-00b49400) · [`00b49404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49378.md#insn-00b49404)
- 新版 [`00b4a3a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a36c.md#insn-00b4a3a8) · [`00b4a3f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a36c.md#insn-00b4a3f4) · [`00b4a3f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a36c.md#insn-00b4a3f8)

~~~diff
- 00b493b4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b493b4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b493b4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a88:8"]]
- 00b493b4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4a3a8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4a3a8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4a3a8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a48:8"]]
+ 00b4a3a8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b493b4 bytes bf222a39
+ 00b4a3a8 bytes bf222939
- 00b49400 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49400 ["INT_ADD", "register:40f0:8", ["const:b49400:8", "const:4:8"]]
- 00b49400 ["CALLIND", null, ["register:0:8"]]
+ 00b4a3f4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a3f4 ["INT_ADD", "register:40f0:8", ["const:b4a3f4:8", "const:4:8"]]
+ 00b4a3f4 ["CALLIND", null, ["register:0:8"]]
- 00b49400 bytes 00013fd6
+ 00b4a3f4 bytes 00013fd6
- 00b49404 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a80:8"]]
- 00b49404 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b49404 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4a3f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a40:8"]]
+ 00b4a3f8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4a3f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b49404 bytes 9f4205f9
+ 00b4a3f8 bytes 9f2205f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8faad05a25a6b87be38a90644d6bb235"></a>

### [`00b49418`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49418.md) → [`00b4a40c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a40c.md) _ZN8firebase4util16content_resolver14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b4a44c",
      "incomplete_value": true,
      "site": "00b4a44c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49458",
      "incomplete_value": true,
      "site": "00b49458",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "definition_site": "00b4a430",
      "incomplete_value": false,
      "site": "00b4a444",
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
            "const:3ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4943c",
      "incomplete_value": false,
      "site": "00b49450",
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
            "const:2e3:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a420",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a430",
      "PARAM",
      [
        "storage",
        "002af2e3",
        null,
        "string"
      ]
    ],
    [
      "00b4a44c",
      "WRITE",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a420",
      "READ",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a430",
      "PARAM",
      [
        "storage",
        "002af3ba",
        null,
        "string"
      ]
    ],
    [
      "00b4a44c",
      "WRITE",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49418.md#insn-00b49450) · [`00b49458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49418.md#insn-00b49458) · [`00b49424`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49418.md#insn-00b49424)
- 新版 [`00b4a444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a40c.md#insn-00b4a444) · [`00b4a44c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a40c.md#insn-00b4a44c) · [`00b4a418`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a40c.md#insn-00b4a418)

~~~diff
- 00b49450 ["INT_ADD", "register:40f0:8", ["const:b49450:8", "const:4:8"]]
- 00b49450 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a444 ["INT_ADD", "register:40f0:8", ["const:b4a444:8", "const:4:8"]]
+ 00b4a444 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b49450 bytes e4460494
+ 00b4a444 bytes db460494
- 00b49458 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a80:8"]]
- 00b49458 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a44c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a40:8"]]
+ 00b4a44c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49458 bytes 804205f9
+ 00b4a44c bytes 802205f9
- 00b49424 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4a418 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b49424 bytes f42e0090
+ 00b4a418 bytes f42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e31f0cb006940d995d8a52dc02d46712"></a>

### [`00b49488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49488.md) → [`00b4a47c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a47c.md) _ZN8firebase4util16content_resolver11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4a498",
      "incomplete_value": false,
      "site": "00b4a49c",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b494a4",
      "incomplete_value": false,
      "site": "00b494a8",
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
            "const:30b:8"
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
      "definition_site": "00b4a4a8",
      "incomplete_value": true,
      "site": "00b4a4b4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b494b4",
      "incomplete_value": true,
      "site": "00b494c0",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4a498",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4a4a8",
      "DATA",
      [
        "storage",
        "01125a90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a498",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4a4a8",
      "DATA",
      [
        "storage",
        "01126a50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b494a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49488.md#insn-00b494a8) · [`00b494a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49488.md#insn-00b494a4) · [`00b494ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49488.md#insn-00b494ac)
- 新版 [`00b4a49c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a47c.md#insn-00b4a49c) · [`00b4a498`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a47c.md#insn-00b4a498) · [`00b4a4a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a47c.md#insn-00b4a4a0)

~~~diff
- 00b494a8 ["INT_ADD", "register:40f0:8", ["const:b494a8:8", "const:4:8"]]
- 00b494a8 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4a49c ["INT_ADD", "register:40f0:8", ["const:b4a49c:8", "const:4:8"]]
+ 00b4a49c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b494a8 bytes 0a470494
+ 00b4a49c bytes 01470494
- 00b494a4 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b494a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b494a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b494a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a498 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4a498 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a498 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a498 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b494a4 bytes 002c0c91
+ 00b4a498 bytes 008c1191
- 00b494ac ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4a4a0 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b494ac bytes e82e0090
+ 00b4a4a0 bytes e82e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cfc614cdba44eb4d7aed58622c40f86c"></a>

### [`00b494c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b494c4.md) → [`00b4a4b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a4b8.md) _ZN8firebase4util16content_resolver13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4a4f8",
      "incomplete_value": true,
      "site": "00b4a4f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a40:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49504",
      "incomplete_value": true,
      "site": "00b49504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a80:8"
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
      "definition_site": "00b4a4d4",
      "incomplete_value": true,
      "site": "00b4a4d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b494e0",
      "incomplete_value": true,
      "site": "00b494e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a4dc",
      "incomplete_value": false,
      "site": "00b4a4f0",
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
            "const:3ba:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b494e8",
      "incomplete_value": false,
      "site": "00b494fc",
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
            "const:2e3:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a4cc",
      "READ",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a4dc",
      "PARAM",
      [
        "storage",
        "002af2e3",
        null,
        "string"
      ]
    ],
    [
      "00b4a4f8",
      "WRITE",
      [
        "storage",
        "01125a80",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a4cc",
      "READ",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a4dc",
      "PARAM",
      [
        "storage",
        "002af3ba",
        null,
        "string"
      ]
    ],
    [
      "00b4a4f8",
      "WRITE",
      [
        "storage",
        "01126a40",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b494fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b494c4.md#insn-00b494fc) · [`00b49504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b494c4.md#insn-00b49504) · [`00b494d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b494c4.md#insn-00b494d0)
- 新版 [`00b4a4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a4b8.md#insn-00b4a4f0) · [`00b4a4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a4b8.md#insn-00b4a4f8) · [`00b4a4c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a4b8.md#insn-00b4a4c4)

~~~diff
- 00b494fc ["INT_ADD", "register:40f0:8", ["const:b494fc:8", "const:4:8"]]
- 00b494fc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a4f0 ["INT_ADD", "register:40f0:8", ["const:b4a4f0:8", "const:4:8"]]
+ 00b4a4f0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b494fc bytes b9460494
+ 00b4a4f0 bytes b0460494
- 00b49504 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a80:8"]]
- 00b49504 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a4f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a40:8"]]
+ 00b4a4f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49504 bytes 804205f9
+ 00b4a4f8 bytes 802205f9
- 00b494d0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4a4c4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b494d0 bytes f42e0090
+ 00b4a4c4 bytes f42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea0dd7642547a87bbafd92c9e9ee4d4e"></a>

### [`00b49534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49534.md) → [`00b4a528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a528.md) _ZN8firebase4util16content_resolver10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4a544",
      "incomplete_value": false,
      "site": "00b4a548",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49550",
      "incomplete_value": false,
      "site": "00b49554",
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
            "const:54d:8"
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
      "definition_site": "00b4a554",
      "incomplete_value": true,
      "site": "00b4a560",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b49560",
      "incomplete_value": true,
      "site": "00b4956c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4a544",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4a554",
      "DATA",
      [
        "storage",
        "01125aa0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a544",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4a554",
      "DATA",
      [
        "storage",
        "01126a60",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49554`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49534.md#insn-00b49554) · [`00b49550`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49534.md#insn-00b49550) · [`00b49558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49534.md#insn-00b49558)
- 新版 [`00b4a548`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a528.md#insn-00b4a548) · [`00b4a544`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a528.md#insn-00b4a544) · [`00b4a54c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a528.md#insn-00b4a54c)

~~~diff
- 00b49554 ["INT_ADD", "register:40f0:8", ["const:b49554:8", "const:4:8"]]
- 00b49554 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4a548 ["INT_ADD", "register:40f0:8", ["const:b4a548:8", "const:4:8"]]
+ 00b4a548 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b49554 bytes df460494
+ 00b4a548 bytes d6460494
- 00b49550 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b49550 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b49550 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b49550 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a544 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4a544 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a544 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a544 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b49550 bytes 00341591
+ 00b4a544 bytes 00681891
- 00b49558 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4a54c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b49558 bytes e82e0090
+ 00b4a54c bytes e82e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c540494b0d24a608910fbe1851922b22"></a>

### [`00b49570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49570.md) → [`00b4a564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a564.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_1

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4a590",
      "incomplete_value": true,
      "site": "00b4a590",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4959c",
      "incomplete_value": true,
      "site": "00b4959c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "definition_site": "00b4a578",
      "incomplete_value": true,
      "site": "00b4a578",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49584",
      "incomplete_value": true,
      "site": "00b49584",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a584",
      "incomplete_value": false,
      "site": "00b4a588",
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
            "const:1aa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49590",
      "incomplete_value": false,
      "site": "00b49594",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a574",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a584",
      "PARAM",
      [
        "storage",
        "002ae0dd",
        null,
        "string"
      ]
    ],
    [
      "00b4a590",
      "WRITE",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a574",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a584",
      "PARAM",
      [
        "storage",
        "002ae1aa",
        null,
        "string"
      ]
    ],
    [
      "00b4a590",
      "WRITE",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49570.md#insn-00b49594) · [`00b4959c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49570.md#insn-00b4959c) · [`00b4957c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49570.md#insn-00b4957c)
- 新版 [`00b4a588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a564.md#insn-00b4a588) · [`00b4a590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a564.md#insn-00b4a590) · [`00b4a570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a564.md#insn-00b4a570)

~~~diff
- 00b49594 ["INT_ADD", "register:40f0:8", ["const:b49594:8", "const:4:8"]]
- 00b49594 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a588 ["INT_ADD", "register:40f0:8", ["const:b4a588:8", "const:4:8"]]
+ 00b4a588 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b49594 bytes 93460494
+ 00b4a588 bytes 8a460494
- 00b4959c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
- 00b4959c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a590 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
+ 00b4a590 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4959c bytes 605605f9
+ 00b4a590 bytes 603605f9
- 00b4957c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4a570 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4957c bytes f32e0090
+ 00b4a570 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05f2e8a6d7fac506588028471df800b5"></a>

### [`00b495b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b495b0.md) → [`00b4a5a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a5a4.md) _ZN8firebase4util7context19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4a5d0",
      "incomplete_value": true,
      "site": "00b4a5d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b495dc",
      "incomplete_value": true,
      "site": "00b495dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "definition_site": "00b4a5b8",
      "incomplete_value": true,
      "site": "00b4a5b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b495c4",
      "incomplete_value": true,
      "site": "00b495c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a5c0",
      "incomplete_value": false,
      "site": "00b4a5c8",
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
            "const:1aa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b495cc",
      "incomplete_value": false,
      "site": "00b495d4",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a5b4",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a5c0",
      "PARAM",
      [
        "storage",
        "002ae0dd",
        null,
        "string"
      ]
    ],
    [
      "00b4a5d0",
      "WRITE",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a5b4",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a5c0",
      "PARAM",
      [
        "storage",
        "002ae1aa",
        null,
        "string"
      ]
    ],
    [
      "00b4a5d0",
      "WRITE",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b495d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b495b0.md#insn-00b495d4) · [`00b495dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b495b0.md#insn-00b495dc) · [`00b495bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b495b0.md#insn-00b495bc)
- 新版 [`00b4a5c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a5a4.md#insn-00b4a5c8) · [`00b4a5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a5a4.md#insn-00b4a5d0) · [`00b4a5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a5a4.md#insn-00b4a5b0)

~~~diff
- 00b495d4 ["INT_ADD", "register:40f0:8", ["const:b495d4:8", "const:4:8"]]
- 00b495d4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a5c8 ["INT_ADD", "register:40f0:8", ["const:b4a5c8:8", "const:4:8"]]
+ 00b4a5c8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b495d4 bytes 83460494
+ 00b4a5c8 bytes 7a460494
- 00b495dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
- 00b495dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a5d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
+ 00b4a5d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b495dc bytes 605605f9
+ 00b4a5d0 bytes 603605f9
- 00b495bc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4a5b0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b495bc bytes f32e0090
+ 00b4a5b0 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f124efa4eabc59e627dfd41bed31b436"></a>

### [`00b495f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b495f0.md) → [`00b4a5e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a5e4.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4a614",
      "incomplete_value": true,
      "site": "00b4a614",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49620",
      "incomplete_value": true,
      "site": "00b49620",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "definition_site": "00b4a5f8",
      "incomplete_value": true,
      "site": "00b4a5f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49604",
      "incomplete_value": true,
      "site": "00b49604",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a604",
      "incomplete_value": false,
      "site": "00b4a60c",
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
            "const:1aa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49610",
      "incomplete_value": false,
      "site": "00b49618",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a5f4",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a604",
      "PARAM",
      [
        "storage",
        "002ae0dd",
        null,
        "string"
      ]
    ],
    [
      "00b4a614",
      "WRITE",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a5f4",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a604",
      "PARAM",
      [
        "storage",
        "002ae1aa",
        null,
        "string"
      ]
    ],
    [
      "00b4a614",
      "WRITE",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49618`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b495f0.md#insn-00b49618) · [`00b49620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b495f0.md#insn-00b49620) · [`00b495fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b495f0.md#insn-00b495fc)
- 新版 [`00b4a60c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a5e4.md#insn-00b4a60c) · [`00b4a614`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a5e4.md#insn-00b4a614) · [`00b4a5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a5e4.md#insn-00b4a5f0)

~~~diff
- 00b49618 ["INT_ADD", "register:40f0:8", ["const:b49618:8", "const:4:8"]]
- 00b49618 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a60c ["INT_ADD", "register:40f0:8", ["const:b4a60c:8", "const:4:8"]]
+ 00b4a60c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b49618 bytes 72460494
+ 00b4a60c bytes 69460494
- 00b49620 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
- 00b49620 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a614 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
+ 00b4a614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49620 bytes 605605f9
+ 00b4a614 bytes 603605f9
- 00b495fc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4a5f0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b495fc bytes f32e0090
+ 00b4a5f0 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dce6e8ce4743e1af3eea8e68088e327"></a>

### [`00b49634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49634.md) → [`00b4a628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a628.md) _ZN8firebase4util7context10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4a658",
      "incomplete_value": true,
      "site": "00b4a658",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a68:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49664",
      "incomplete_value": true,
      "site": "00b49664",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "definition_site": "00b4a63c",
      "incomplete_value": true,
      "site": "00b4a63c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49648",
      "incomplete_value": true,
      "site": "00b49648",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a644",
      "incomplete_value": false,
      "site": "00b4a650",
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
            "const:1aa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49650",
      "incomplete_value": false,
      "site": "00b4965c",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a638",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a644",
      "PARAM",
      [
        "storage",
        "002ae0dd",
        null,
        "string"
      ]
    ],
    [
      "00b4a658",
      "WRITE",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a638",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a644",
      "PARAM",
      [
        "storage",
        "002ae1aa",
        null,
        "string"
      ]
    ],
    [
      "00b4a658",
      "WRITE",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4965c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49634.md#insn-00b4965c) · [`00b49664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49634.md#insn-00b49664) · [`00b49640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49634.md#insn-00b49640)
- 新版 [`00b4a650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a628.md#insn-00b4a650) · [`00b4a658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a628.md#insn-00b4a658) · [`00b4a634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a628.md#insn-00b4a634)

~~~diff
- 00b4965c ["INT_ADD", "register:40f0:8", ["const:b4965c:8", "const:4:8"]]
- 00b4965c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a650 ["INT_ADD", "register:40f0:8", ["const:b4a650:8", "const:4:8"]]
+ 00b4a650 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4965c bytes 61460494
+ 00b4a650 bytes 58460494
- 00b49664 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:aa8:8"]]
- 00b49664 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a658 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a68:8"]]
+ 00b4a658 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49664 bytes 605605f9
+ 00b4a658 bytes 603605f9
- 00b49640 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4a634 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b49640 bytes f32e0090
+ 00b4a634 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fe01329c666196dd0ba58c7fa06e34a7"></a>

### [`00b49684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49684.md) → [`00b4a678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a678.md) _ZN8firebase4util7context15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4a700",
      "incomplete_value": true,
      "site": "00b4a700",
      "value": [
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
      "definition_site": "00b4970c",
      "incomplete_value": true,
      "site": "00b4970c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "definition_site": "00b4a6ac",
      "incomplete_value": true,
      "site": "00b4a6b8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:a68:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b496b8",
      "incomplete_value": true,
      "site": "00b496c4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:aa8:8"
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
      "00b4a68c",
      "READ",
      [
        "storage",
        "01125ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a6ac",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a700",
      "WRITE",
      [
        "storage",
        "01125ab0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a68c",
      "READ",
      [
        "storage",
        "01126a70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a6ac",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a700",
      "WRITE",
      [
        "storage",
        "01126a70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b496c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49684.md#insn-00b496c4) · [`00b4970c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49684.md#insn-00b4970c) · [`00b49694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49684.md#insn-00b49694)
- 新版 [`00b4a6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a678.md#insn-00b4a6b8) · [`00b4a700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a678.md#insn-00b4a700) · [`00b4a688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a678.md#insn-00b4a688)

~~~diff
- 00b496c4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b496c4 ["INT_ADD", "register:40f0:8", ["const:b496c4:8", "const:4:8"]]
- 00b496c4 ["CALLIND", null, ["register:0:8"]]
+ 00b4a6b8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a6b8 ["INT_ADD", "register:40f0:8", ["const:b4a6b8:8", "const:4:8"]]
+ 00b4a6b8 ["CALLIND", null, ["register:0:8"]]
- 00b496c4 bytes 00013fd6
+ 00b4a6b8 bytes 00013fd6
- 00b4970c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4970c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ab0:8"]]
- 00b4970c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4a700 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4a700 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a70:8"]]
+ 00b4a700 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4970c bytes a0c22a39
+ 00b4a700 bytes a0c22939
- 00b49694 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4a688 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b49694 bytes f52e0090
+ 00b4a688 bytes f52e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-822ee2e431330f7d918d46d0667052a3"></a>

### [`00b49720`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49720.md) → [`00b4a714`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a714.md) _ZN8firebase4util7context12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4a750",
      "incomplete_value": true,
      "site": "00b4a750",
      "value": [
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
      "definition_site": "00b4975c",
      "incomplete_value": true,
      "site": "00b4975c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ab0:8"
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
      "definition_site": "00b4a7a0",
      "incomplete_value": true,
      "site": "00b4a7a0",
      "value": [
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
      "definition_site": "00b497ac",
      "incomplete_value": true,
      "site": "00b497ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "definition_site": "00b4a72c",
      "incomplete_value": true,
      "site": "00b4a72c",
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
      "definition_site": "00b49738",
      "incomplete_value": true,
      "site": "00b49738",
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
      "00b4a728",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a734",
      "READ",
      [
        "storage",
        "01125ab0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a750",
      "WRITE",
      [
        "storage",
        "01125ab0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4a728",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a734",
      "READ",
      [
        "storage",
        "01126a70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4a750",
      "WRITE",
      [
        "storage",
        "01126a70",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4975c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49720.md#insn-00b4975c) · [`00b497a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49720.md#insn-00b497a8) · [`00b497ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49720.md#insn-00b497ac)
- 新版 [`00b4a750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a714.md#insn-00b4a750) · [`00b4a79c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a714.md#insn-00b4a79c) · [`00b4a7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a714.md#insn-00b4a7a0)

~~~diff
- 00b4975c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4975c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4975c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ab0:8"]]
- 00b4975c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4a750 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4a750 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4a750 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a70:8"]]
+ 00b4a750 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4975c bytes bfc22a39
+ 00b4a750 bytes bfc22939
- 00b497a8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b497a8 ["INT_ADD", "register:40f0:8", ["const:b497a8:8", "const:4:8"]]
- 00b497a8 ["CALLIND", null, ["register:0:8"]]
+ 00b4a79c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4a79c ["INT_ADD", "register:40f0:8", ["const:b4a79c:8", "const:4:8"]]
+ 00b4a79c ["CALLIND", null, ["register:0:8"]]
- 00b497a8 bytes 00013fd6
+ 00b4a79c bytes 00013fd6
- 00b497ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
- 00b497ac ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b497ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4a7a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
+ 00b4a7a0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4a7a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b497ac bytes 9f5605f9
+ 00b4a7a0 bytes 9f3605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74aa963b5fee3b178942f6b90cb655e1"></a>

### [`00b497c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b497c0.md) → [`00b4a7b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a7b4.md) _ZN8firebase4util7context14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b4a7f4",
      "incomplete_value": true,
      "site": "00b4a7f4",
      "value": [
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
      "definition_site": "00b49800",
      "incomplete_value": true,
      "site": "00b49800",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "definition_site": "00b4a7d0",
      "incomplete_value": true,
      "site": "00b4a7d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b497dc",
      "incomplete_value": true,
      "site": "00b497dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a7d8",
      "incomplete_value": false,
      "site": "00b4a7ec",
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
            "const:1aa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b497e4",
      "incomplete_value": false,
      "site": "00b497f8",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a7c8",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a7d8",
      "PARAM",
      [
        "storage",
        "002ae0dd",
        null,
        "string"
      ]
    ],
    [
      "00b4a7f4",
      "WRITE",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a7c8",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a7d8",
      "PARAM",
      [
        "storage",
        "002ae1aa",
        null,
        "string"
      ]
    ],
    [
      "00b4a7f4",
      "WRITE",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b497f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b497c0.md#insn-00b497f8) · [`00b49800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b497c0.md#insn-00b49800) · [`00b497cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b497c0.md#insn-00b497cc)
- 新版 [`00b4a7ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a7b4.md#insn-00b4a7ec) · [`00b4a7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a7b4.md#insn-00b4a7f4) · [`00b4a7c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a7b4.md#insn-00b4a7c0)

~~~diff
- 00b497f8 ["INT_ADD", "register:40f0:8", ["const:b497f8:8", "const:4:8"]]
- 00b497f8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a7ec ["INT_ADD", "register:40f0:8", ["const:b4a7ec:8", "const:4:8"]]
+ 00b4a7ec ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b497f8 bytes fa450494
+ 00b4a7ec bytes f1450494
- 00b49800 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
- 00b49800 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a7f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
+ 00b4a7f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49800 bytes 805605f9
+ 00b4a7f4 bytes 803605f9
- 00b497cc ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4a7c0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b497cc bytes f42e0090
+ 00b4a7c0 bytes f42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-67d197569653fbd102b641d9151d6408"></a>

### [`00b49830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49830.md) → [`00b4a824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a824.md) _ZN8firebase4util7context11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b610`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b610.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5c5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c5e0.md) · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4a840",
      "incomplete_value": false,
      "site": "00b4a844",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4984c",
      "incomplete_value": false,
      "site": "00b49850",
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
            "const:30b:8"
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
      "definition_site": "00b4a850",
      "incomplete_value": true,
      "site": "00b4a85c",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b4985c",
      "incomplete_value": true,
      "site": "00b49868",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4a840",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4a850",
      "DATA",
      [
        "storage",
        "01125ab8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a840",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4a850",
      "DATA",
      [
        "storage",
        "01126a78",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49850`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49830.md#insn-00b49850) · [`00b4984c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49830.md#insn-00b4984c) · [`00b49854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49830.md#insn-00b49854)
- 新版 [`00b4a844`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a824.md#insn-00b4a844) · [`00b4a840`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a824.md#insn-00b4a840) · [`00b4a848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a824.md#insn-00b4a848)

~~~diff
- 00b49850 ["INT_ADD", "register:40f0:8", ["const:b49850:8", "const:4:8"]]
- 00b49850 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4a844 ["INT_ADD", "register:40f0:8", ["const:b4a844:8", "const:4:8"]]
+ 00b4a844 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b49850 bytes 20460494
+ 00b4a844 bytes 17460494
- 00b4984c ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4984c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4984c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4984c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a840 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4a840 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a840 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a840 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4984c bytes 002c0c91
+ 00b4a840 bytes 008c1191
- 00b49854 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4a848 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b49854 bytes e82e0090
+ 00b4a848 bytes e82e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcfb9082e25970ddbf4a538771694357"></a>

### [`00b4986c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4986c.md) → [`00b4a860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a860.md) _ZN8firebase4util7context13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4a8a0",
      "incomplete_value": true,
      "site": "00b4a8a0",
      "value": [
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
      "definition_site": "00b498ac",
      "incomplete_value": true,
      "site": "00b498ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:aa8:8"
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
      "definition_site": "00b4a87c",
      "incomplete_value": true,
      "site": "00b4a87c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49888",
      "incomplete_value": true,
      "site": "00b49888",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a884",
      "incomplete_value": false,
      "site": "00b4a898",
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
            "const:1aa:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49890",
      "incomplete_value": false,
      "site": "00b498a4",
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
            "const:dd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a874",
      "READ",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a884",
      "PARAM",
      [
        "storage",
        "002ae0dd",
        null,
        "string"
      ]
    ],
    [
      "00b4a8a0",
      "WRITE",
      [
        "storage",
        "01125aa8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a874",
      "READ",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a884",
      "PARAM",
      [
        "storage",
        "002ae1aa",
        null,
        "string"
      ]
    ],
    [
      "00b4a8a0",
      "WRITE",
      [
        "storage",
        "01126a68",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b498a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4986c.md#insn-00b498a4) · [`00b498ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4986c.md#insn-00b498ac) · [`00b49878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b4986c.md#insn-00b49878)
- 新版 [`00b4a898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a860.md#insn-00b4a898) · [`00b4a8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a860.md#insn-00b4a8a0) · [`00b4a86c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a860.md#insn-00b4a86c)

~~~diff
- 00b498a4 ["INT_ADD", "register:40f0:8", ["const:b498a4:8", "const:4:8"]]
- 00b498a4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a898 ["INT_ADD", "register:40f0:8", ["const:b4a898:8", "const:4:8"]]
+ 00b4a898 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b498a4 bytes cf450494
+ 00b4a898 bytes c6450494
- 00b498ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:aa8:8"]]
- 00b498ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a8a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a68:8"]]
+ 00b4a8a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b498ac bytes 805605f9
+ 00b4a8a0 bytes 803605f9
- 00b49878 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4a86c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b49878 bytes f42e0090
+ 00b4a86c bytes f42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0f15759a46301347df05b60b84a3dc6d"></a>

### [`00b498dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b498dc.md) → [`00b4a8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a8d0.md) _ZN8firebase4util7context10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4a8ec",
      "incomplete_value": false,
      "site": "00b4a8f0",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b498f8",
      "incomplete_value": false,
      "site": "00b498fc",
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
            "const:54d:8"
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
      "definition_site": "00b4a8fc",
      "incomplete_value": true,
      "site": "00b4a908",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b49908",
      "incomplete_value": true,
      "site": "00b49914",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4a8ec",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4a8fc",
      "DATA",
      [
        "storage",
        "01125ad0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4a8ec",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4a8fc",
      "DATA",
      [
        "storage",
        "01126a90",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b498fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b498dc.md#insn-00b498fc) · [`00b498f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b498dc.md#insn-00b498f8) · [`00b49900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b498dc.md#insn-00b49900)
- 新版 [`00b4a8f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a8d0.md#insn-00b4a8f0) · [`00b4a8ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a8d0.md#insn-00b4a8ec) · [`00b4a8f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a8d0.md#insn-00b4a8f4)

~~~diff
- 00b498fc ["INT_ADD", "register:40f0:8", ["const:b498fc:8", "const:4:8"]]
- 00b498fc ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4a8f0 ["INT_ADD", "register:40f0:8", ["const:b4a8f0:8", "const:4:8"]]
+ 00b4a8f0 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b498fc bytes f5450494
+ 00b4a8f0 bytes ec450494
- 00b498f8 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b498f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b498f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b498f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4a8ec ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4a8ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a8ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4a8ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b498f8 bytes 00341591
+ 00b4a8ec bytes 00681891
- 00b49900 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4a8f4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b49900 bytes e82e0090
+ 00b4a8f4 bytes e82e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b62a1ce3c460d63189fe4bccccd91bd"></a>

### [`00b49918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49918.md) → [`00b4a90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a90c.md) _ZN8firebase4util6cursor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4a938",
      "incomplete_value": true,
      "site": "00b4a938",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49944",
      "incomplete_value": true,
      "site": "00b49944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "definition_site": "00b4a920",
      "incomplete_value": true,
      "site": "00b4a920",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4992c",
      "incomplete_value": true,
      "site": "00b4992c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a92c",
      "incomplete_value": false,
      "site": "00b4a930",
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
            "const:b95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49938",
      "incomplete_value": false,
      "site": "00b4993c",
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
            "const:aca:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a91c",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a92c",
      "PARAM",
      [
        "storage",
        "002a3aca",
        null,
        "string"
      ]
    ],
    [
      "00b4a938",
      "WRITE",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a91c",
      "READ",
      [
        "storage",
        "01126a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a92c",
      "PARAM",
      [
        "storage",
        "002a3b95",
        null,
        "string"
      ]
    ],
    [
      "00b4a938",
      "WRITE",
      [
        "storage",
        "01126a98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4993c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49918.md#insn-00b4993c) · [`00b49944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49918.md#insn-00b49944) · [`00b49924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49918.md#insn-00b49924)
- 新版 [`00b4a930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a90c.md#insn-00b4a930) · [`00b4a938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a90c.md#insn-00b4a938) · [`00b4a918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a90c.md#insn-00b4a918)

~~~diff
- 00b4993c ["INT_ADD", "register:40f0:8", ["const:b4993c:8", "const:4:8"]]
- 00b4993c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a930 ["INT_ADD", "register:40f0:8", ["const:b4a930:8", "const:4:8"]]
+ 00b4a930 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4993c bytes a9450494
+ 00b4a930 bytes a0450494
- 00b49944 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad8:8"]]
- 00b49944 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a938 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a98:8"]]
+ 00b4a938 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49944 bytes 606e05f9
+ 00b4a938 bytes 604e05f9
- 00b49924 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4a918 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b49924 bytes f32e0090
+ 00b4a918 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-461400fc229217f91486bdc08c88c1e5"></a>

### [`00b49958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49958.md) → [`00b4a94c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a94c.md) _ZN8firebase4util6cursor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4a978",
      "incomplete_value": true,
      "site": "00b4a978",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49984",
      "incomplete_value": true,
      "site": "00b49984",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "definition_site": "00b4a960",
      "incomplete_value": true,
      "site": "00b4a960",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4996c",
      "incomplete_value": true,
      "site": "00b4996c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a968",
      "incomplete_value": false,
      "site": "00b4a970",
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
            "const:b95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49974",
      "incomplete_value": false,
      "site": "00b4997c",
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
            "const:aca:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a95c",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a968",
      "PARAM",
      [
        "storage",
        "002a3aca",
        null,
        "string"
      ]
    ],
    [
      "00b4a978",
      "WRITE",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a95c",
      "READ",
      [
        "storage",
        "01126a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a968",
      "PARAM",
      [
        "storage",
        "002a3b95",
        null,
        "string"
      ]
    ],
    [
      "00b4a978",
      "WRITE",
      [
        "storage",
        "01126a98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4997c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49958.md#insn-00b4997c) · [`00b49984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49958.md#insn-00b49984) · [`00b49964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49958.md#insn-00b49964)
- 新版 [`00b4a970`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a94c.md#insn-00b4a970) · [`00b4a978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a94c.md#insn-00b4a978) · [`00b4a958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a94c.md#insn-00b4a958)

~~~diff
- 00b4997c ["INT_ADD", "register:40f0:8", ["const:b4997c:8", "const:4:8"]]
- 00b4997c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a970 ["INT_ADD", "register:40f0:8", ["const:b4a970:8", "const:4:8"]]
+ 00b4a970 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4997c bytes 99450494
+ 00b4a970 bytes 90450494
- 00b49984 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad8:8"]]
- 00b49984 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a978 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a98:8"]]
+ 00b4a978 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49984 bytes 606e05f9
+ 00b4a978 bytes 604e05f9
- 00b49964 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4a958 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b49964 bytes f32e0090
+ 00b4a958 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80defd831fd2facac0dd50b029d81de5"></a>

### [`00b49998`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49998.md) → [`00b4a98c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a98c.md) _ZN8firebase4util6cursor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4a9bc",
      "incomplete_value": true,
      "site": "00b4a9bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b499c8",
      "incomplete_value": true,
      "site": "00b499c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "definition_site": "00b4a9a0",
      "incomplete_value": true,
      "site": "00b4a9a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b499ac",
      "incomplete_value": true,
      "site": "00b499ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a9ac",
      "incomplete_value": false,
      "site": "00b4a9b4",
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
            "const:b95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b499b8",
      "incomplete_value": false,
      "site": "00b499c0",
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
            "const:aca:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a99c",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a9ac",
      "PARAM",
      [
        "storage",
        "002a3aca",
        null,
        "string"
      ]
    ],
    [
      "00b4a9bc",
      "WRITE",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a99c",
      "READ",
      [
        "storage",
        "01126a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a9ac",
      "PARAM",
      [
        "storage",
        "002a3b95",
        null,
        "string"
      ]
    ],
    [
      "00b4a9bc",
      "WRITE",
      [
        "storage",
        "01126a98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b499c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49998.md#insn-00b499c0) · [`00b499c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49998.md#insn-00b499c8) · [`00b499a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49998.md#insn-00b499a4)
- 新版 [`00b4a9b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a98c.md#insn-00b4a9b4) · [`00b4a9bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a98c.md#insn-00b4a9bc) · [`00b4a998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a98c.md#insn-00b4a998)

~~~diff
- 00b499c0 ["INT_ADD", "register:40f0:8", ["const:b499c0:8", "const:4:8"]]
- 00b499c0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a9b4 ["INT_ADD", "register:40f0:8", ["const:b4a9b4:8", "const:4:8"]]
+ 00b4a9b4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b499c0 bytes 88450494
+ 00b4a9b4 bytes 7f450494
- 00b499c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad8:8"]]
- 00b499c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4a9bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a98:8"]]
+ 00b4a9bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b499c8 bytes 606e05f9
+ 00b4a9bc bytes 604e05f9
- 00b499a4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4a998 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b499a4 bytes f32e0090
+ 00b4a998 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a57bcba3233ccb379aedbf551a70f659"></a>

### [`00b499dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b499dc.md) → [`00b4a9d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a9d0.md) _ZN8firebase4util6cursor10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4aa00",
      "incomplete_value": true,
      "site": "00b4aa00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49a0c",
      "incomplete_value": true,
      "site": "00b49a0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "definition_site": "00b4a9e4",
      "incomplete_value": true,
      "site": "00b4a9e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b499f0",
      "incomplete_value": true,
      "site": "00b499f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4a9ec",
      "incomplete_value": false,
      "site": "00b4a9f8",
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
            "const:b95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b499f8",
      "incomplete_value": false,
      "site": "00b49a04",
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
            "const:aca:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4a9e0",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a9ec",
      "PARAM",
      [
        "storage",
        "002a3aca",
        null,
        "string"
      ]
    ],
    [
      "00b4aa00",
      "WRITE",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4a9e0",
      "READ",
      [
        "storage",
        "01126a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4a9ec",
      "PARAM",
      [
        "storage",
        "002a3b95",
        null,
        "string"
      ]
    ],
    [
      "00b4aa00",
      "WRITE",
      [
        "storage",
        "01126a98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49a04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b499dc.md#insn-00b49a04) · [`00b49a0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b499dc.md#insn-00b49a0c) · [`00b499e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b499dc.md#insn-00b499e8)
- 新版 [`00b4a9f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a9d0.md#insn-00b4a9f8) · [`00b4aa00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a9d0.md#insn-00b4aa00) · [`00b4a9dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4a9d0.md#insn-00b4a9dc)

~~~diff
- 00b49a04 ["INT_ADD", "register:40f0:8", ["const:b49a04:8", "const:4:8"]]
- 00b49a04 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4a9f8 ["INT_ADD", "register:40f0:8", ["const:b4a9f8:8", "const:4:8"]]
+ 00b4a9f8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b49a04 bytes 77450494
+ 00b4a9f8 bytes 6e450494
- 00b49a0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad8:8"]]
- 00b49a0c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4aa00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a98:8"]]
+ 00b4aa00 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49a0c bytes 606e05f9
+ 00b4aa00 bytes 604e05f9
- 00b499e8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4a9dc ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b499e8 bytes f32e0090
+ 00b4a9dc bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-752a2330c8e5b031ac2342697e2adeff"></a>

### [`00b49a2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49a2c.md) → [`00b4aa20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4aa20.md) _ZN8firebase4util6cursor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4aaa8",
      "incomplete_value": true,
      "site": "00b4aaa8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49ab4",
      "incomplete_value": true,
      "site": "00b49ab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "00b4aa54",
      "incomplete_value": true,
      "site": "00b4aa60",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:a98:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49a60",
      "incomplete_value": true,
      "site": "00b49a6c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
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
      "00b4aa34",
      "READ",
      [
        "storage",
        "01125ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4aa54",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aaa8",
      "WRITE",
      [
        "storage",
        "01125ae0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4aa34",
      "READ",
      [
        "storage",
        "01126aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4aa54",
      "READ",
      [
        "storage",
        "01126a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aaa8",
      "WRITE",
      [
        "storage",
        "01126aa0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49a2c.md#insn-00b49a6c) · [`00b49ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49a2c.md#insn-00b49ab4) · [`00b49a3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49a2c.md#insn-00b49a3c)
- 新版 [`00b4aa60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4aa20.md#insn-00b4aa60) · [`00b4aaa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4aa20.md#insn-00b4aaa8) · [`00b4aa30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4aa20.md#insn-00b4aa30)

~~~diff
- 00b49a6c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49a6c ["INT_ADD", "register:40f0:8", ["const:b49a6c:8", "const:4:8"]]
- 00b49a6c ["CALLIND", null, ["register:0:8"]]
+ 00b4aa60 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4aa60 ["INT_ADD", "register:40f0:8", ["const:b4aa60:8", "const:4:8"]]
+ 00b4aa60 ["CALLIND", null, ["register:0:8"]]
- 00b49a6c bytes 00013fd6
+ 00b4aa60 bytes 00013fd6
- 00b49ab4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b49ab4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ae0:8"]]
- 00b49ab4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4aaa8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4aaa8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:aa0:8"]]
+ 00b4aaa8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b49ab4 bytes a0822b39
+ 00b4aaa8 bytes a0822a39
- 00b49a3c ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4aa30 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b49a3c bytes f52e0090
+ 00b4aa30 bytes f52e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ec091a733488cbd2c0c2f92e8f1ead55"></a>

### [`00b49ac8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49ac8.md) → [`00b4aabc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4aabc.md) _ZN8firebase4util6cursor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4aaf8",
      "incomplete_value": true,
      "site": "00b4aaf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:aa0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49b04",
      "incomplete_value": true,
      "site": "00b49b04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ae0:8"
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
      "definition_site": "00b4ab48",
      "incomplete_value": true,
      "site": "00b4ab48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49b54",
      "incomplete_value": true,
      "site": "00b49b54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "definition_site": "00b4aad4",
      "incomplete_value": true,
      "site": "00b4aad4",
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
      "definition_site": "00b49ae0",
      "incomplete_value": true,
      "site": "00b49ae0",
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
      "00b4aad0",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aadc",
      "READ",
      [
        "storage",
        "01125ae0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4aaf8",
      "WRITE",
      [
        "storage",
        "01125ae0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4aad0",
      "READ",
      [
        "storage",
        "01126a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4aadc",
      "READ",
      [
        "storage",
        "01126aa0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4aaf8",
      "WRITE",
      [
        "storage",
        "01126aa0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49b04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49ac8.md#insn-00b49b04) · [`00b49b50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49ac8.md#insn-00b49b50) · [`00b49b54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49ac8.md#insn-00b49b54)
- 新版 [`00b4aaf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4aabc.md#insn-00b4aaf8) · [`00b4ab44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4aabc.md#insn-00b4ab44) · [`00b4ab48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4aabc.md#insn-00b4ab48)

~~~diff
- 00b49b04 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b49b04 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b49b04 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ae0:8"]]
- 00b49b04 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4aaf8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4aaf8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4aaf8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:aa0:8"]]
+ 00b4aaf8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b49b04 bytes bf822b39
+ 00b4aaf8 bytes bf822a39
- 00b49b50 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49b50 ["INT_ADD", "register:40f0:8", ["const:b49b50:8", "const:4:8"]]
- 00b49b50 ["CALLIND", null, ["register:0:8"]]
+ 00b4ab44 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4ab44 ["INT_ADD", "register:40f0:8", ["const:b4ab44:8", "const:4:8"]]
+ 00b4ab44 ["CALLIND", null, ["register:0:8"]]
- 00b49b50 bytes 00013fd6
+ 00b4ab44 bytes 00013fd6
- 00b49b54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ad8:8"]]
- 00b49b54 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b49b54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4ab48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a98:8"]]
+ 00b4ab48 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4ab48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b49b54 bytes 9f6e05f9
+ 00b4ab48 bytes 9f4e05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f76cfd3b56dfe69974a26265fe29d1de"></a>

### [`00b49b68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49b68.md) → [`00b4ab5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ab5c.md) _ZN8firebase4util6cursor14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b4ab9c",
      "incomplete_value": true,
      "site": "00b4ab9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49ba8",
      "incomplete_value": true,
      "site": "00b49ba8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "definition_site": "00b4ab78",
      "incomplete_value": true,
      "site": "00b4ab78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49b84",
      "incomplete_value": true,
      "site": "00b49b84",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ab80",
      "incomplete_value": false,
      "site": "00b4ab94",
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
            "const:b95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49b8c",
      "incomplete_value": false,
      "site": "00b49ba0",
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
            "const:aca:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ab70",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab80",
      "PARAM",
      [
        "storage",
        "002a3aca",
        null,
        "string"
      ]
    ],
    [
      "00b4ab9c",
      "WRITE",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ab70",
      "READ",
      [
        "storage",
        "01126a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ab80",
      "PARAM",
      [
        "storage",
        "002a3b95",
        null,
        "string"
      ]
    ],
    [
      "00b4ab9c",
      "WRITE",
      [
        "storage",
        "01126a98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49ba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49b68.md#insn-00b49ba0) · [`00b49ba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49b68.md#insn-00b49ba8) · [`00b49b74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49b68.md#insn-00b49b74)
- 新版 [`00b4ab94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ab5c.md#insn-00b4ab94) · [`00b4ab9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ab5c.md#insn-00b4ab9c) · [`00b4ab68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ab5c.md#insn-00b4ab68)

~~~diff
- 00b49ba0 ["INT_ADD", "register:40f0:8", ["const:b49ba0:8", "const:4:8"]]
- 00b49ba0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4ab94 ["INT_ADD", "register:40f0:8", ["const:b4ab94:8", "const:4:8"]]
+ 00b4ab94 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b49ba0 bytes 10450494
+ 00b4ab94 bytes 07450494
- 00b49ba8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ad8:8"]]
- 00b49ba8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ab9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a98:8"]]
+ 00b4ab9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49ba8 bytes 806e05f9
+ 00b4ab9c bytes 804e05f9
- 00b49b74 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4ab68 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b49b74 bytes f42e0090
+ 00b4ab68 bytes f42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56d62a7b7b7cfec6150add2af78dc8f0"></a>

### [`00b49bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49bd8.md) → [`00b4abcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4abcc.md) _ZN8firebase4util6cursor11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4abe8",
      "incomplete_value": false,
      "site": "00b4abec",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49bf4",
      "incomplete_value": false,
      "site": "00b49bf8",
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
            "const:30b:8"
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
      "definition_site": "00b4abf8",
      "incomplete_value": true,
      "site": "00b4ac04",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b49c04",
      "incomplete_value": true,
      "site": "00b49c10",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4abe8",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4abf8",
      "DATA",
      [
        "storage",
        "01125ae8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4abe8",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4abf8",
      "DATA",
      [
        "storage",
        "01126aa8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49bf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49bd8.md#insn-00b49bf8) · [`00b49bf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49bd8.md#insn-00b49bf4) · [`00b49bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49bd8.md#insn-00b49bfc)
- 新版 [`00b4abec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4abcc.md#insn-00b4abec) · [`00b4abe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4abcc.md#insn-00b4abe8) · [`00b4abf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4abcc.md#insn-00b4abf0)

~~~diff
- 00b49bf8 ["INT_ADD", "register:40f0:8", ["const:b49bf8:8", "const:4:8"]]
- 00b49bf8 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4abec ["INT_ADD", "register:40f0:8", ["const:b4abec:8", "const:4:8"]]
+ 00b4abec ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b49bf8 bytes 36450494
+ 00b4abec bytes 2d450494
- 00b49bf4 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b49bf4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b49bf4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b49bf4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4abe8 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4abe8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4abe8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4abe8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b49bf4 bytes 002c0c91
+ 00b4abe8 bytes 008c1191
- 00b49bfc ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4abf0 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b49bfc bytes e82e0090
+ 00b4abf0 bytes e82e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fa6630cbd66079f65eb7e9b9d3ee36f9"></a>

### [`00b49c14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49c14.md) → [`00b4ac08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ac08.md) _ZN8firebase4util6cursor13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4ac48",
      "incomplete_value": true,
      "site": "00b4ac48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:a98:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49c54",
      "incomplete_value": true,
      "site": "00b49c54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ad8:8"
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
      "definition_site": "00b4ac24",
      "incomplete_value": true,
      "site": "00b4ac24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49c30",
      "incomplete_value": true,
      "site": "00b49c30",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ac2c",
      "incomplete_value": false,
      "site": "00b4ac40",
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
            "const:b95:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49c38",
      "incomplete_value": false,
      "site": "00b49c4c",
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
            "const:aca:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ac1c",
      "READ",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac2c",
      "PARAM",
      [
        "storage",
        "002a3aca",
        null,
        "string"
      ]
    ],
    [
      "00b4ac48",
      "WRITE",
      [
        "storage",
        "01125ad8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ac1c",
      "READ",
      [
        "storage",
        "01126a98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ac2c",
      "PARAM",
      [
        "storage",
        "002a3b95",
        null,
        "string"
      ]
    ],
    [
      "00b4ac48",
      "WRITE",
      [
        "storage",
        "01126a98",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49c4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49c14.md#insn-00b49c4c) · [`00b49c54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49c14.md#insn-00b49c54) · [`00b49c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49c14.md#insn-00b49c20)
- 新版 [`00b4ac40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ac08.md#insn-00b4ac40) · [`00b4ac48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ac08.md#insn-00b4ac48) · [`00b4ac14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ac08.md#insn-00b4ac14)

~~~diff
- 00b49c4c ["INT_ADD", "register:40f0:8", ["const:b49c4c:8", "const:4:8"]]
- 00b49c4c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4ac40 ["INT_ADD", "register:40f0:8", ["const:b4ac40:8", "const:4:8"]]
+ 00b4ac40 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b49c4c bytes e5440494
+ 00b4ac40 bytes dc440494
- 00b49c54 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ad8:8"]]
- 00b49c54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ac48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a98:8"]]
+ 00b4ac48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49c54 bytes 806e05f9
+ 00b4ac48 bytes 804e05f9
- 00b49c20 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4ac14 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b49c20 bytes f42e0090
+ 00b4ac14 bytes f42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-66ec5114d0654eab39ff5248ad017ef8"></a>

### [`00b49c84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49c84.md) → [`00b4ac78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ac78.md) _ZN8firebase4util6cursor10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4ac94",
      "incomplete_value": false,
      "site": "00b4ac98",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49ca0",
      "incomplete_value": false,
      "site": "00b49ca4",
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
            "const:54d:8"
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
      "definition_site": "00b4aca4",
      "incomplete_value": true,
      "site": "00b4acb0",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b49cb0",
      "incomplete_value": true,
      "site": "00b49cbc",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4ac94",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4aca4",
      "DATA",
      [
        "storage",
        "01125b08",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4ac94",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4aca4",
      "DATA",
      [
        "storage",
        "01126ac8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49ca4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49c84.md#insn-00b49ca4) · [`00b49ca0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49c84.md#insn-00b49ca0) · [`00b49ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49c84.md#insn-00b49ca8)
- 新版 [`00b4ac98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ac78.md#insn-00b4ac98) · [`00b4ac94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ac78.md#insn-00b4ac94) · [`00b4ac9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ac78.md#insn-00b4ac9c)

~~~diff
- 00b49ca4 ["INT_ADD", "register:40f0:8", ["const:b49ca4:8", "const:4:8"]]
- 00b49ca4 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4ac98 ["INT_ADD", "register:40f0:8", ["const:b4ac98:8", "const:4:8"]]
+ 00b4ac98 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b49ca4 bytes 0b450494
+ 00b4ac98 bytes 02450494
- 00b49ca0 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b49ca0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b49ca0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b49ca0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ac94 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4ac94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ac94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ac94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b49ca0 bytes 00341591
+ 00b4ac94 bytes 00681891
- 00b49ca8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4ac9c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b49ca8 bytes e82e0090
+ 00b4ac9c bytes e82e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-973ac7e1c7646178fc75b32e14dec316"></a>

### [`00b49cc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49cc0.md) → [`00b4acb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4acb4.md) _ZN8firebase4util4date19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4ace0",
      "incomplete_value": true,
      "site": "00b4ace0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49cec",
      "incomplete_value": true,
      "site": "00b49cec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "definition_site": "00b4acc8",
      "incomplete_value": true,
      "site": "00b4acc8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49cd4",
      "incomplete_value": true,
      "site": "00b49cd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4acd4",
      "incomplete_value": false,
      "site": "00b4acd8",
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
            "const:51a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49ce0",
      "incomplete_value": false,
      "site": "00b49ce4",
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
            "const:3c2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4acc4",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4acd4",
      "PARAM",
      [
        "storage",
        "002a83c2",
        null,
        "string"
      ]
    ],
    [
      "00b4ace0",
      "WRITE",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4acc4",
      "READ",
      [
        "storage",
        "01126ad0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4acd4",
      "PARAM",
      [
        "storage",
        "002a851a",
        null,
        "string"
      ]
    ],
    [
      "00b4ace0",
      "WRITE",
      [
        "storage",
        "01126ad0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49ce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49cc0.md#insn-00b49ce4) · [`00b49cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49cc0.md#insn-00b49cec) · [`00b49ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49cc0.md#insn-00b49ccc)
- 新版 [`00b4acd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4acb4.md#insn-00b4acd8) · [`00b4ace0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4acb4.md#insn-00b4ace0) · [`00b4acc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4acb4.md#insn-00b4acc0)

~~~diff
- 00b49ce4 ["INT_ADD", "register:40f0:8", ["const:b49ce4:8", "const:4:8"]]
- 00b49ce4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4acd8 ["INT_ADD", "register:40f0:8", ["const:b4acd8:8", "const:4:8"]]
+ 00b4acd8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b49ce4 bytes bf440494
+ 00b4acd8 bytes b6440494
- 00b49cec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b10:8"]]
- 00b49cec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ace0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad0:8"]]
+ 00b4ace0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49cec bytes 608a05f9
+ 00b4ace0 bytes 606a05f9
- 00b49ccc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4acc0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b49ccc bytes f32e0090
+ 00b4acc0 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-654078d22f1fc59bf283fd7708c1716c"></a>

### [`00b49d00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d00.md) → [`00b4acf4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4acf4.md) _ZN8firebase4util4date19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4ad20",
      "incomplete_value": true,
      "site": "00b4ad20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49d2c",
      "incomplete_value": true,
      "site": "00b49d2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "definition_site": "00b4ad08",
      "incomplete_value": true,
      "site": "00b4ad08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49d14",
      "incomplete_value": true,
      "site": "00b49d14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ad10",
      "incomplete_value": false,
      "site": "00b4ad18",
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
            "const:51a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49d1c",
      "incomplete_value": false,
      "site": "00b49d24",
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
            "const:3c2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ad04",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad10",
      "PARAM",
      [
        "storage",
        "002a83c2",
        null,
        "string"
      ]
    ],
    [
      "00b4ad20",
      "WRITE",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ad04",
      "READ",
      [
        "storage",
        "01126ad0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad10",
      "PARAM",
      [
        "storage",
        "002a851a",
        null,
        "string"
      ]
    ],
    [
      "00b4ad20",
      "WRITE",
      [
        "storage",
        "01126ad0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49d24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d00.md#insn-00b49d24) · [`00b49d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d00.md#insn-00b49d2c) · [`00b49d0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d00.md#insn-00b49d0c)
- 新版 [`00b4ad18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4acf4.md#insn-00b4ad18) · [`00b4ad20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4acf4.md#insn-00b4ad20) · [`00b4ad00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4acf4.md#insn-00b4ad00)

~~~diff
- 00b49d24 ["INT_ADD", "register:40f0:8", ["const:b49d24:8", "const:4:8"]]
- 00b49d24 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4ad18 ["INT_ADD", "register:40f0:8", ["const:b4ad18:8", "const:4:8"]]
+ 00b4ad18 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b49d24 bytes af440494
+ 00b4ad18 bytes a6440494
- 00b49d2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b10:8"]]
- 00b49d2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ad20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad0:8"]]
+ 00b4ad20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49d2c bytes 608a05f9
+ 00b4ad20 bytes 606a05f9
- 00b49d0c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4ad00 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b49d0c bytes f32e0090
+ 00b4ad00 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b11da211a744d1835f436215cb66b4e9"></a>

### [`00b49d40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d40.md) → [`00b4ad34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ad34.md) _ZN8firebase4util4date10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4ad64",
      "incomplete_value": true,
      "site": "00b4ad64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49d70",
      "incomplete_value": true,
      "site": "00b49d70",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "definition_site": "00b4ad48",
      "incomplete_value": true,
      "site": "00b4ad48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49d54",
      "incomplete_value": true,
      "site": "00b49d54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ad54",
      "incomplete_value": false,
      "site": "00b4ad5c",
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
            "const:51a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49d60",
      "incomplete_value": false,
      "site": "00b49d68",
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
            "const:3c2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ad44",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad54",
      "PARAM",
      [
        "storage",
        "002a83c2",
        null,
        "string"
      ]
    ],
    [
      "00b4ad64",
      "WRITE",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ad44",
      "READ",
      [
        "storage",
        "01126ad0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad54",
      "PARAM",
      [
        "storage",
        "002a851a",
        null,
        "string"
      ]
    ],
    [
      "00b4ad64",
      "WRITE",
      [
        "storage",
        "01126ad0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49d68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d40.md#insn-00b49d68) · [`00b49d70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d40.md#insn-00b49d70) · [`00b49d4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d40.md#insn-00b49d4c)
- 新版 [`00b4ad5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ad34.md#insn-00b4ad5c) · [`00b4ad64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ad34.md#insn-00b4ad64) · [`00b4ad40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ad34.md#insn-00b4ad40)

~~~diff
- 00b49d68 ["INT_ADD", "register:40f0:8", ["const:b49d68:8", "const:4:8"]]
- 00b49d68 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4ad5c ["INT_ADD", "register:40f0:8", ["const:b4ad5c:8", "const:4:8"]]
+ 00b4ad5c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b49d68 bytes 9e440494
+ 00b4ad5c bytes 95440494
- 00b49d70 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b10:8"]]
- 00b49d70 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ad64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad0:8"]]
+ 00b4ad64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49d70 bytes 608a05f9
+ 00b4ad64 bytes 606a05f9
- 00b49d4c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4ad40 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b49d4c bytes f32e0090
+ 00b4ad40 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cb970895c73ed5eab7247b1bd1565813"></a>

### [`00b49d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d84.md) → [`00b4ad78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ad78.md) _ZN8firebase4util4date10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4ada8",
      "incomplete_value": true,
      "site": "00b4ada8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49db4",
      "incomplete_value": true,
      "site": "00b49db4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "definition_site": "00b4ad8c",
      "incomplete_value": true,
      "site": "00b4ad8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49d98",
      "incomplete_value": true,
      "site": "00b49d98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ad94",
      "incomplete_value": false,
      "site": "00b4ada0",
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
            "const:51a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49da0",
      "incomplete_value": false,
      "site": "00b49dac",
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
            "const:3c2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ad88",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad94",
      "PARAM",
      [
        "storage",
        "002a83c2",
        null,
        "string"
      ]
    ],
    [
      "00b4ada8",
      "WRITE",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ad88",
      "READ",
      [
        "storage",
        "01126ad0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ad94",
      "PARAM",
      [
        "storage",
        "002a851a",
        null,
        "string"
      ]
    ],
    [
      "00b4ada8",
      "WRITE",
      [
        "storage",
        "01126ad0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49dac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d84.md#insn-00b49dac) · [`00b49db4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d84.md#insn-00b49db4) · [`00b49d90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49d84.md#insn-00b49d90)
- 新版 [`00b4ada0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ad78.md#insn-00b4ada0) · [`00b4ada8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ad78.md#insn-00b4ada8) · [`00b4ad84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ad78.md#insn-00b4ad84)

~~~diff
- 00b49dac ["INT_ADD", "register:40f0:8", ["const:b49dac:8", "const:4:8"]]
- 00b49dac ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4ada0 ["INT_ADD", "register:40f0:8", ["const:b4ada0:8", "const:4:8"]]
+ 00b4ada0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b49dac bytes 8d440494
+ 00b4ada0 bytes 84440494
- 00b49db4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b10:8"]]
- 00b49db4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ada8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ad0:8"]]
+ 00b4ada8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49db4 bytes 608a05f9
+ 00b4ada8 bytes 606a05f9
- 00b49d90 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4ad84 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b49d90 bytes f32e0090
+ 00b4ad84 bytes f32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a223d7894301c1e64eadcd6be93e8142"></a>

### [`00b49dd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49dd4.md) → [`00b4adc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4adc8.md) _ZN8firebase4util4date15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4ae50",
      "incomplete_value": true,
      "site": "00b4ae50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49e5c",
      "incomplete_value": true,
      "site": "00b49e5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "definition_site": "00b4adfc",
      "incomplete_value": true,
      "site": "00b4ae08",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:ad0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49e08",
      "incomplete_value": true,
      "site": "00b49e14",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
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
      "00b4addc",
      "READ",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4adfc",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae50",
      "WRITE",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4addc",
      "READ",
      [
        "storage",
        "01126ad8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4adfc",
      "READ",
      [
        "storage",
        "01126ad0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae50",
      "WRITE",
      [
        "storage",
        "01126ad8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49dd4.md#insn-00b49e14) · [`00b49e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49dd4.md#insn-00b49e5c) · [`00b49de4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49dd4.md#insn-00b49de4)
- 新版 [`00b4ae08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4adc8.md#insn-00b4ae08) · [`00b4ae50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4adc8.md#insn-00b4ae50) · [`00b4add8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4adc8.md#insn-00b4add8)

~~~diff
- 00b49e14 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49e14 ["INT_ADD", "register:40f0:8", ["const:b49e14:8", "const:4:8"]]
- 00b49e14 ["CALLIND", null, ["register:0:8"]]
+ 00b4ae08 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4ae08 ["INT_ADD", "register:40f0:8", ["const:b4ae08:8", "const:4:8"]]
+ 00b4ae08 ["CALLIND", null, ["register:0:8"]]
- 00b49e14 bytes 00013fd6
+ 00b4ae08 bytes 00013fd6
- 00b49e5c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b49e5c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b18:8"]]
- 00b49e5c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4ae50 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4ae50 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ad8:8"]]
+ 00b4ae50 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b49e5c bytes a0622c39
+ 00b4ae50 bytes a0622b39
- 00b49de4 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4add8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b49de4 bytes f52e0090
+ 00b4add8 bytes f52e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5aaea68660aeb8d8ce83b2174d916876"></a>

### [`00b49e70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49e70.md) → [`00b4ae64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ae64.md) _ZN8firebase4util4date12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4aea0",
      "incomplete_value": true,
      "site": "00b4aea0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ad8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49eac",
      "incomplete_value": true,
      "site": "00b49eac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b18:8"
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
      "definition_site": "00b4aef0",
      "incomplete_value": true,
      "site": "00b4aef0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49efc",
      "incomplete_value": true,
      "site": "00b49efc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "definition_site": "00b4ae7c",
      "incomplete_value": true,
      "site": "00b4ae7c",
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
      "definition_site": "00b49e88",
      "incomplete_value": true,
      "site": "00b49e88",
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
      "00b4ae78",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae84",
      "READ",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4aea0",
      "WRITE",
      [
        "storage",
        "01125b18",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4ae78",
      "READ",
      [
        "storage",
        "01126ad0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ae84",
      "READ",
      [
        "storage",
        "01126ad8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4aea0",
      "WRITE",
      [
        "storage",
        "01126ad8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49eac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49e70.md#insn-00b49eac) · [`00b49ef8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49e70.md#insn-00b49ef8) · [`00b49efc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49e70.md#insn-00b49efc)
- 新版 [`00b4aea0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ae64.md#insn-00b4aea0) · [`00b4aeec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ae64.md#insn-00b4aeec) · [`00b4aef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4ae64.md#insn-00b4aef0)

~~~diff
- 00b49eac ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b49eac ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b49eac ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b18:8"]]
- 00b49eac ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4aea0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4aea0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4aea0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ad8:8"]]
+ 00b4aea0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b49eac bytes bf622c39
+ 00b4aea0 bytes bf622b39
- 00b49ef8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b49ef8 ["INT_ADD", "register:40f0:8", ["const:b49ef8:8", "const:4:8"]]
- 00b49ef8 ["CALLIND", null, ["register:0:8"]]
+ 00b4aeec ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4aeec ["INT_ADD", "register:40f0:8", ["const:b4aeec:8", "const:4:8"]]
+ 00b4aeec ["CALLIND", null, ["register:0:8"]]
- 00b49ef8 bytes 00013fd6
+ 00b4aeec bytes 00013fd6
- 00b49efc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b10:8"]]
- 00b49efc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b49efc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4aef0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ad0:8"]]
+ 00b4aef0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4aef0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b49efc bytes 9f8a05f9
+ 00b4aef0 bytes 9f6a05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef1a84c8b09eb1830ec8ce674504c0ad"></a>

### [`00b49f10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49f10.md) → [`00b4af04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4af04.md) _ZN8firebase4util4date14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b4af44",
      "incomplete_value": true,
      "site": "00b4af44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49f50",
      "incomplete_value": true,
      "site": "00b49f50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "definition_site": "00b4af20",
      "incomplete_value": true,
      "site": "00b4af20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49f2c",
      "incomplete_value": true,
      "site": "00b49f2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4af28",
      "incomplete_value": false,
      "site": "00b4af3c",
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
            "const:51a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49f34",
      "incomplete_value": false,
      "site": "00b49f48",
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
            "const:3c2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4af18",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4af28",
      "PARAM",
      [
        "storage",
        "002a83c2",
        null,
        "string"
      ]
    ],
    [
      "00b4af44",
      "WRITE",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4af18",
      "READ",
      [
        "storage",
        "01126ad0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4af28",
      "PARAM",
      [
        "storage",
        "002a851a",
        null,
        "string"
      ]
    ],
    [
      "00b4af44",
      "WRITE",
      [
        "storage",
        "01126ad0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49f48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49f10.md#insn-00b49f48) · [`00b49f50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49f10.md#insn-00b49f50) · [`00b49f1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49f10.md#insn-00b49f1c)
- 新版 [`00b4af3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4af04.md#insn-00b4af3c) · [`00b4af44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4af04.md#insn-00b4af44) · [`00b4af10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4af04.md#insn-00b4af10)

~~~diff
- 00b49f48 ["INT_ADD", "register:40f0:8", ["const:b49f48:8", "const:4:8"]]
- 00b49f48 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4af3c ["INT_ADD", "register:40f0:8", ["const:b4af3c:8", "const:4:8"]]
+ 00b4af3c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b49f48 bytes 26440494
+ 00b4af3c bytes 1d440494
- 00b49f50 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b10:8"]]
- 00b49f50 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4af44 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ad0:8"]]
+ 00b4af44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49f50 bytes 808a05f9
+ 00b4af44 bytes 806a05f9
- 00b49f1c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4af10 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b49f1c bytes f42e0090
+ 00b4af10 bytes f42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5cf9a16fe3b401b72696e80a9bc080fc"></a>

### [`00b49f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49f80.md) → [`00b4af74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4af74.md) _ZN8firebase4util4date11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4af90",
      "incomplete_value": false,
      "site": "00b4af94",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49f9c",
      "incomplete_value": false,
      "site": "00b49fa0",
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
            "const:30b:8"
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
      "definition_site": "00b4afa0",
      "incomplete_value": true,
      "site": "00b4afac",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b49fac",
      "incomplete_value": true,
      "site": "00b49fb8",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4af90",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4afa0",
      "DATA",
      [
        "storage",
        "01125b20",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4af90",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4afa0",
      "DATA",
      [
        "storage",
        "01126ae0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49fa0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49f80.md#insn-00b49fa0) · [`00b49f9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49f80.md#insn-00b49f9c) · [`00b49fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49f80.md#insn-00b49fa4)
- 新版 [`00b4af94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4af74.md#insn-00b4af94) · [`00b4af90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4af74.md#insn-00b4af90) · [`00b4af98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4af74.md#insn-00b4af98)

~~~diff
- 00b49fa0 ["INT_ADD", "register:40f0:8", ["const:b49fa0:8", "const:4:8"]]
- 00b49fa0 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4af94 ["INT_ADD", "register:40f0:8", ["const:b4af94:8", "const:4:8"]]
+ 00b4af94 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b49fa0 bytes 4c440494
+ 00b4af94 bytes 43440494
- 00b49f9c ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b49f9c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b49f9c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b49f9c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4af90 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4af90 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4af90 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4af90 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b49f9c bytes 002c0c91
+ 00b4af90 bytes 008c1191
- 00b49fa4 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4af98 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b49fa4 bytes e82e0090
+ 00b4af98 bytes e82e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2f3897e9f2426cfc08fb801b29d8c32c"></a>

### [`00b49fbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49fbc.md) → [`00b4afb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4afb0.md) _ZN8firebase4util4date13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4aff0",
      "incomplete_value": true,
      "site": "00b4aff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ad0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49ffc",
      "incomplete_value": true,
      "site": "00b49ffc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b10:8"
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
      "definition_site": "00b4afcc",
      "incomplete_value": true,
      "site": "00b4afcc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49fd8",
      "incomplete_value": true,
      "site": "00b49fd8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4afd4",
      "incomplete_value": false,
      "site": "00b4afe8",
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
            "const:51a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b49fe0",
      "incomplete_value": false,
      "site": "00b49ff4",
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
            "const:3c2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4afc4",
      "READ",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4afd4",
      "PARAM",
      [
        "storage",
        "002a83c2",
        null,
        "string"
      ]
    ],
    [
      "00b4aff0",
      "WRITE",
      [
        "storage",
        "01125b10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4afc4",
      "READ",
      [
        "storage",
        "01126ad0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4afd4",
      "PARAM",
      [
        "storage",
        "002a851a",
        null,
        "string"
      ]
    ],
    [
      "00b4aff0",
      "WRITE",
      [
        "storage",
        "01126ad0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b49ff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49fbc.md#insn-00b49ff4) · [`00b49ffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49fbc.md#insn-00b49ffc) · [`00b49fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b49/00b49fbc.md#insn-00b49fc8)
- 新版 [`00b4afe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4afb0.md#insn-00b4afe8) · [`00b4aff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4afb0.md#insn-00b4aff0) · [`00b4afbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4a/00b4afb0.md#insn-00b4afbc)

~~~diff
- 00b49ff4 ["INT_ADD", "register:40f0:8", ["const:b49ff4:8", "const:4:8"]]
- 00b49ff4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4afe8 ["INT_ADD", "register:40f0:8", ["const:b4afe8:8", "const:4:8"]]
+ 00b4afe8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b49ff4 bytes fb430494
+ 00b4afe8 bytes f2430494
- 00b49ffc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b10:8"]]
- 00b49ffc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4aff0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ad0:8"]]
+ 00b4aff0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b49ffc bytes 808a05f9
+ 00b4aff0 bytes 806a05f9
- 00b49fc8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4afbc ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b49fc8 bytes f42e0090
+ 00b4afbc bytes f42e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bc9d5f0a604308a34ef88721cbb51410"></a>

### [`00b4a02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a02c.md) → [`00b4b020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b020.md) _ZN8firebase4util4date10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4b03c",
      "incomplete_value": false,
      "site": "00b4b040",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a048",
      "incomplete_value": false,
      "site": "00b4a04c",
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
            "const:54d:8"
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
      "definition_site": "00b4b04c",
      "incomplete_value": true,
      "site": "00b4b058",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b4a058",
      "incomplete_value": true,
      "site": "00b4a064",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4b03c",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4b04c",
      "DATA",
      [
        "storage",
        "01125b38",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b03c",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4b04c",
      "DATA",
      [
        "storage",
        "01126af8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a04c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a02c.md#insn-00b4a04c) · [`00b4a048`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a02c.md#insn-00b4a048) · [`00b4a050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a02c.md#insn-00b4a050)
- 新版 [`00b4b040`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b020.md#insn-00b4b040) · [`00b4b03c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b020.md#insn-00b4b03c) · [`00b4b044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b020.md#insn-00b4b044)

~~~diff
- 00b4a04c ["INT_ADD", "register:40f0:8", ["const:b4a04c:8", "const:4:8"]]
- 00b4a04c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4b040 ["INT_ADD", "register:40f0:8", ["const:b4b040:8", "const:4:8"]]
+ 00b4b040 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4a04c bytes 21440494
+ 00b4b040 bytes 18440494
- 00b4a048 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b4a048 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a048 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a048 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b03c ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4b03c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b03c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b03c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a048 bytes 00341591
+ 00b4b03c bytes 00681891
- 00b4a050 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4b044 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4a050 bytes c82e00f0
+ 00b4b044 bytes c82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0aafdb5ae51a61dd0150e57124f6c4a7"></a>

### [`00b4a068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a068.md) → [`00b4b05c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b05c.md) _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4b088",
      "incomplete_value": true,
      "site": "00b4b088",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a094",
      "incomplete_value": true,
      "site": "00b4a094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "definition_site": "00b4b070",
      "incomplete_value": true,
      "site": "00b4b070",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a07c",
      "incomplete_value": true,
      "site": "00b4a07c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b07c",
      "incomplete_value": false,
      "site": "00b4b080",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:d83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a088",
      "incomplete_value": false,
      "site": "00b4a08c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:cb4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b06c",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b07c",
      "PARAM",
      [
        "storage",
        "002b7cb4",
        null,
        "string"
      ]
    ],
    [
      "00b4b088",
      "WRITE",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b06c",
      "READ",
      [
        "storage",
        "01126b00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b07c",
      "PARAM",
      [
        "storage",
        "002b7d83",
        null,
        "string"
      ]
    ],
    [
      "00b4b088",
      "WRITE",
      [
        "storage",
        "01126b00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a068.md#insn-00b4a08c) · [`00b4a094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a068.md#insn-00b4a094) · [`00b4a074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a068.md#insn-00b4a074)
- 新版 [`00b4b080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b05c.md#insn-00b4b080) · [`00b4b088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b05c.md#insn-00b4b088) · [`00b4b068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b05c.md#insn-00b4b068)

~~~diff
- 00b4a08c ["INT_ADD", "register:40f0:8", ["const:b4a08c:8", "const:4:8"]]
- 00b4a08c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b080 ["INT_ADD", "register:40f0:8", ["const:b4b080:8", "const:4:8"]]
+ 00b4b080 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a08c bytes d5430494
+ 00b4b080 bytes cc430494
- 00b4a094 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b40:8"]]
- 00b4a094 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b088 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b00:8"]]
+ 00b4b088 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a094 bytes 60a205f9
+ 00b4b088 bytes 608205f9
- 00b4a074 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4b068 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4a074 bytes d32e00f0
+ 00b4b068 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c6afad2e9bdfab957e7d8221ef7e26f4"></a>

### [`00b4a0a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a0a8.md) → [`00b4b09c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b09c.md) _ZN8firebase4util12double_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4b0c8",
      "incomplete_value": true,
      "site": "00b4b0c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a0d4",
      "incomplete_value": true,
      "site": "00b4a0d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "definition_site": "00b4b0b0",
      "incomplete_value": true,
      "site": "00b4b0b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a0bc",
      "incomplete_value": true,
      "site": "00b4a0bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b0b8",
      "incomplete_value": false,
      "site": "00b4b0c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:d83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a0c4",
      "incomplete_value": false,
      "site": "00b4a0cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:cb4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b0ac",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b0b8",
      "PARAM",
      [
        "storage",
        "002b7cb4",
        null,
        "string"
      ]
    ],
    [
      "00b4b0c8",
      "WRITE",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b0ac",
      "READ",
      [
        "storage",
        "01126b00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b0b8",
      "PARAM",
      [
        "storage",
        "002b7d83",
        null,
        "string"
      ]
    ],
    [
      "00b4b0c8",
      "WRITE",
      [
        "storage",
        "01126b00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a0cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a0a8.md#insn-00b4a0cc) · [`00b4a0d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a0a8.md#insn-00b4a0d4) · [`00b4a0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a0a8.md#insn-00b4a0b4)
- 新版 [`00b4b0c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b09c.md#insn-00b4b0c0) · [`00b4b0c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b09c.md#insn-00b4b0c8) · [`00b4b0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b09c.md#insn-00b4b0a8)

~~~diff
- 00b4a0cc ["INT_ADD", "register:40f0:8", ["const:b4a0cc:8", "const:4:8"]]
- 00b4a0cc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b0c0 ["INT_ADD", "register:40f0:8", ["const:b4b0c0:8", "const:4:8"]]
+ 00b4b0c0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a0cc bytes c5430494
+ 00b4b0c0 bytes bc430494
- 00b4a0d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b40:8"]]
- 00b4a0d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b0c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b00:8"]]
+ 00b4b0c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a0d4 bytes 60a205f9
+ 00b4b0c8 bytes 608205f9
- 00b4a0b4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4b0a8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4a0b4 bytes d32e00f0
+ 00b4b0a8 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d36edc615c46c11ae1ae3c74b0530aa"></a>

### [`00b4a0e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a0e8.md) → [`00b4b0dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b0dc.md) _ZN8firebase4util12double_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4b10c",
      "incomplete_value": true,
      "site": "00b4b10c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a118",
      "incomplete_value": true,
      "site": "00b4a118",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "definition_site": "00b4b0f0",
      "incomplete_value": true,
      "site": "00b4b0f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a0fc",
      "incomplete_value": true,
      "site": "00b4a0fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b0fc",
      "incomplete_value": false,
      "site": "00b4b104",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:d83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a108",
      "incomplete_value": false,
      "site": "00b4a110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:cb4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b0ec",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b0fc",
      "PARAM",
      [
        "storage",
        "002b7cb4",
        null,
        "string"
      ]
    ],
    [
      "00b4b10c",
      "WRITE",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b0ec",
      "READ",
      [
        "storage",
        "01126b00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b0fc",
      "PARAM",
      [
        "storage",
        "002b7d83",
        null,
        "string"
      ]
    ],
    [
      "00b4b10c",
      "WRITE",
      [
        "storage",
        "01126b00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a110`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a0e8.md#insn-00b4a110) · [`00b4a118`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a0e8.md#insn-00b4a118) · [`00b4a0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a0e8.md#insn-00b4a0f4)
- 新版 [`00b4b104`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b0dc.md#insn-00b4b104) · [`00b4b10c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b0dc.md#insn-00b4b10c) · [`00b4b0e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b0dc.md#insn-00b4b0e8)

~~~diff
- 00b4a110 ["INT_ADD", "register:40f0:8", ["const:b4a110:8", "const:4:8"]]
- 00b4a110 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b104 ["INT_ADD", "register:40f0:8", ["const:b4b104:8", "const:4:8"]]
+ 00b4b104 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a110 bytes b4430494
+ 00b4b104 bytes ab430494
- 00b4a118 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b40:8"]]
- 00b4a118 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b10c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b00:8"]]
+ 00b4b10c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a118 bytes 60a205f9
+ 00b4b10c bytes 608205f9
- 00b4a0f4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4b0e8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4a0f4 bytes d32e00f0
+ 00b4b0e8 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-339d02f6ef6a0e2a3d912e3c7f3dffb6"></a>

### [`00b4a12c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a12c.md) → [`00b4b120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b120.md) _ZN8firebase4util12double_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4b150",
      "incomplete_value": true,
      "site": "00b4b150",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a15c",
      "incomplete_value": true,
      "site": "00b4a15c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "definition_site": "00b4b134",
      "incomplete_value": true,
      "site": "00b4b134",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a140",
      "incomplete_value": true,
      "site": "00b4a140",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b13c",
      "incomplete_value": false,
      "site": "00b4b148",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:d83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a148",
      "incomplete_value": false,
      "site": "00b4a154",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:cb4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b130",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b13c",
      "PARAM",
      [
        "storage",
        "002b7cb4",
        null,
        "string"
      ]
    ],
    [
      "00b4b150",
      "WRITE",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b130",
      "READ",
      [
        "storage",
        "01126b00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b13c",
      "PARAM",
      [
        "storage",
        "002b7d83",
        null,
        "string"
      ]
    ],
    [
      "00b4b150",
      "WRITE",
      [
        "storage",
        "01126b00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a154`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a12c.md#insn-00b4a154) · [`00b4a15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a12c.md#insn-00b4a15c) · [`00b4a138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a12c.md#insn-00b4a138)
- 新版 [`00b4b148`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b120.md#insn-00b4b148) · [`00b4b150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b120.md#insn-00b4b150) · [`00b4b12c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b120.md#insn-00b4b12c)

~~~diff
- 00b4a154 ["INT_ADD", "register:40f0:8", ["const:b4a154:8", "const:4:8"]]
- 00b4a154 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b148 ["INT_ADD", "register:40f0:8", ["const:b4b148:8", "const:4:8"]]
+ 00b4b148 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a154 bytes a3430494
+ 00b4b148 bytes 9a430494
- 00b4a15c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b40:8"]]
- 00b4a15c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b150 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b00:8"]]
+ 00b4b150 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a15c bytes 60a205f9
+ 00b4b150 bytes 608205f9
- 00b4a138 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4b12c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4a138 bytes d32e00f0
+ 00b4b12c bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d24fe836c73c7017f2dd8688ab5a49e6"></a>

### [`00b4a17c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a17c.md) → [`00b4b170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b170.md) _ZN8firebase4util12double_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4b1f8",
      "incomplete_value": true,
      "site": "00b4b1f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a204",
      "incomplete_value": true,
      "site": "00b4a204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "definition_site": "00b4b1a4",
      "incomplete_value": true,
      "site": "00b4b1b0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "definition_site": "00b4a1b0",
      "incomplete_value": true,
      "site": "00b4a1bc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:b40:8"
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
      "00b4b184",
      "READ",
      [
        "storage",
        "01125b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b1a4",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b1f8",
      "WRITE",
      [
        "storage",
        "01125b48",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b184",
      "READ",
      [
        "storage",
        "01126b08",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b1a4",
      "READ",
      [
        "storage",
        "01126b00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b1f8",
      "WRITE",
      [
        "storage",
        "01126b08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a17c.md#insn-00b4a1bc) · [`00b4a204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a17c.md#insn-00b4a204) · [`00b4a18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a17c.md#insn-00b4a18c)
- 新版 [`00b4b1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b170.md#insn-00b4b1b0) · [`00b4b1f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b170.md#insn-00b4b1f8) · [`00b4b180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b170.md#insn-00b4b180)

~~~diff
- 00b4a1bc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a1bc ["INT_ADD", "register:40f0:8", ["const:b4a1bc:8", "const:4:8"]]
- 00b4a1bc ["CALLIND", null, ["register:0:8"]]
+ 00b4b1b0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b1b0 ["INT_ADD", "register:40f0:8", ["const:b4b1b0:8", "const:4:8"]]
+ 00b4b1b0 ["CALLIND", null, ["register:0:8"]]
- 00b4a1bc bytes 00013fd6
+ 00b4b1b0 bytes 00013fd6
- 00b4a204 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4a204 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b48:8"]]
- 00b4a204 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4b1f8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4b1f8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b08:8"]]
+ 00b4b1f8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4a204 bytes a0222d39
+ 00b4b1f8 bytes a0222c39
- 00b4a18c ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4b180 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4a18c bytes d52e00f0
+ 00b4b180 bytes d52e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46a8a9e9f98499a53b2f95d626705baf"></a>

### [`00b4a218`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a218.md) → [`00b4b20c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b20c.md) _ZN8firebase4util12double_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4b248",
      "incomplete_value": true,
      "site": "00b4b248",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b08:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a254",
      "incomplete_value": true,
      "site": "00b4a254",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b48:8"
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
      "definition_site": "00b4b298",
      "incomplete_value": true,
      "site": "00b4b298",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a2a4",
      "incomplete_value": true,
      "site": "00b4a2a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "definition_site": "00b4b224",
      "incomplete_value": true,
      "site": "00b4b224",
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
      "definition_site": "00b4a230",
      "incomplete_value": true,
      "site": "00b4a230",
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
      "00b4b220",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b22c",
      "READ",
      [
        "storage",
        "01125b48",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b248",
      "WRITE",
      [
        "storage",
        "01125b48",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b220",
      "READ",
      [
        "storage",
        "01126b00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b22c",
      "READ",
      [
        "storage",
        "01126b08",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b248",
      "WRITE",
      [
        "storage",
        "01126b08",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a254`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a218.md#insn-00b4a254) · [`00b4a2a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a218.md#insn-00b4a2a0) · [`00b4a2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a218.md#insn-00b4a2a4)
- 新版 [`00b4b248`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b20c.md#insn-00b4b248) · [`00b4b294`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b20c.md#insn-00b4b294) · [`00b4b298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b20c.md#insn-00b4b298)

~~~diff
- 00b4a254 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4a254 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4a254 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b48:8"]]
- 00b4a254 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4b248 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4b248 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4b248 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b08:8"]]
+ 00b4b248 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4a254 bytes bf222d39
+ 00b4b248 bytes bf222c39
- 00b4a2a0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a2a0 ["INT_ADD", "register:40f0:8", ["const:b4a2a0:8", "const:4:8"]]
- 00b4a2a0 ["CALLIND", null, ["register:0:8"]]
+ 00b4b294 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b294 ["INT_ADD", "register:40f0:8", ["const:b4b294:8", "const:4:8"]]
+ 00b4b294 ["CALLIND", null, ["register:0:8"]]
- 00b4a2a0 bytes 00013fd6
+ 00b4b294 bytes 00013fd6
- 00b4a2a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b40:8"]]
- 00b4a2a4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4a2a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4b298 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b00:8"]]
+ 00b4b298 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4b298 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4a2a4 bytes 9fa205f9
+ 00b4b298 bytes 9f8205f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1b053f5d3cd32fbdd836a075aa5558e2"></a>

### [`00b4a2b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a2b8.md) → [`00b4b2ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b2ac.md) _ZN8firebase4util12double_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b4b2ec",
      "incomplete_value": true,
      "site": "00b4b2ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a2f8",
      "incomplete_value": true,
      "site": "00b4a2f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "definition_site": "00b4b2c8",
      "incomplete_value": true,
      "site": "00b4b2c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a2d4",
      "incomplete_value": true,
      "site": "00b4a2d4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b2d0",
      "incomplete_value": false,
      "site": "00b4b2e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:d83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a2dc",
      "incomplete_value": false,
      "site": "00b4a2f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:cb4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b2c0",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b2d0",
      "PARAM",
      [
        "storage",
        "002b7cb4",
        null,
        "string"
      ]
    ],
    [
      "00b4b2ec",
      "WRITE",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b2c0",
      "READ",
      [
        "storage",
        "01126b00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b2d0",
      "PARAM",
      [
        "storage",
        "002b7d83",
        null,
        "string"
      ]
    ],
    [
      "00b4b2ec",
      "WRITE",
      [
        "storage",
        "01126b00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a2b8.md#insn-00b4a2f0) · [`00b4a2f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a2b8.md#insn-00b4a2f8) · [`00b4a2c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a2b8.md#insn-00b4a2c4)
- 新版 [`00b4b2e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b2ac.md#insn-00b4b2e4) · [`00b4b2ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b2ac.md#insn-00b4b2ec) · [`00b4b2b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b2ac.md#insn-00b4b2b8)

~~~diff
- 00b4a2f0 ["INT_ADD", "register:40f0:8", ["const:b4a2f0:8", "const:4:8"]]
- 00b4a2f0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b2e4 ["INT_ADD", "register:40f0:8", ["const:b4b2e4:8", "const:4:8"]]
+ 00b4b2e4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a2f0 bytes 3c430494
+ 00b4b2e4 bytes 33430494
- 00b4a2f8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b40:8"]]
- 00b4a2f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b2ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b00:8"]]
+ 00b4b2ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a2f8 bytes 80a205f9
+ 00b4b2ec bytes 808205f9
- 00b4a2c4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4b2b8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4a2c4 bytes d42e00f0
+ 00b4b2b8 bytes d42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-46f35e9941924589235f8018dd073d70"></a>

### [`00b4a328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a328.md) → [`00b4b31c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b31c.md) _ZN8firebase4util12double_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b360.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5c330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c330.md) · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4b338",
      "incomplete_value": false,
      "site": "00b4b33c",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a344",
      "incomplete_value": false,
      "site": "00b4a348",
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
            "const:30b:8"
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
      "definition_site": "00b4b348",
      "incomplete_value": true,
      "site": "00b4b354",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b4a354",
      "incomplete_value": true,
      "site": "00b4a360",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4b338",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4b348",
      "DATA",
      [
        "storage",
        "01125b50",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b338",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4b348",
      "DATA",
      [
        "storage",
        "01126b10",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a348`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a328.md#insn-00b4a348) · [`00b4a344`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a328.md#insn-00b4a344) · [`00b4a34c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a328.md#insn-00b4a34c)
- 新版 [`00b4b33c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b31c.md#insn-00b4b33c) · [`00b4b338`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b31c.md#insn-00b4b338) · [`00b4b340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b31c.md#insn-00b4b340)

~~~diff
- 00b4a348 ["INT_ADD", "register:40f0:8", ["const:b4a348:8", "const:4:8"]]
- 00b4a348 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4b33c ["INT_ADD", "register:40f0:8", ["const:b4b33c:8", "const:4:8"]]
+ 00b4b33c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4a348 bytes 62430494
+ 00b4b33c bytes 59430494
- 00b4a344 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4a344 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a344 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a344 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b338 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4b338 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b338 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b338 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a344 bytes 002c0c91
+ 00b4b338 bytes 008c1191
- 00b4a34c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4b340 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4a34c bytes c82e00f0
+ 00b4b340 bytes c82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1c58993ee059738876ac01f0d5b61efc"></a>

### [`00b4a364`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a364.md) → [`00b4b358`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b358.md) _ZN8firebase4util12double_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4b398",
      "incomplete_value": true,
      "site": "00b4b398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a3a4",
      "incomplete_value": true,
      "site": "00b4a3a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b40:8"
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
      "definition_site": "00b4b374",
      "incomplete_value": true,
      "site": "00b4b374",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a380",
      "incomplete_value": true,
      "site": "00b4a380",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b37c",
      "incomplete_value": false,
      "site": "00b4b390",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:d83:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a388",
      "incomplete_value": false,
      "site": "00b4a39c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b7000:8"
          ],
          [
            "leaf",
            "const:cb4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b36c",
      "READ",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b37c",
      "PARAM",
      [
        "storage",
        "002b7cb4",
        null,
        "string"
      ]
    ],
    [
      "00b4b398",
      "WRITE",
      [
        "storage",
        "01125b40",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b36c",
      "READ",
      [
        "storage",
        "01126b00",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b37c",
      "PARAM",
      [
        "storage",
        "002b7d83",
        null,
        "string"
      ]
    ],
    [
      "00b4b398",
      "WRITE",
      [
        "storage",
        "01126b00",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a39c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a364.md#insn-00b4a39c) · [`00b4a3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a364.md#insn-00b4a3a4) · [`00b4a370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a364.md#insn-00b4a370)
- 新版 [`00b4b390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b358.md#insn-00b4b390) · [`00b4b398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b358.md#insn-00b4b398) · [`00b4b364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b358.md#insn-00b4b364)

~~~diff
- 00b4a39c ["INT_ADD", "register:40f0:8", ["const:b4a39c:8", "const:4:8"]]
- 00b4a39c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b390 ["INT_ADD", "register:40f0:8", ["const:b4b390:8", "const:4:8"]]
+ 00b4b390 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a39c bytes 11430494
+ 00b4b390 bytes 08430494
- 00b4a3a4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b40:8"]]
- 00b4a3a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b398 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b00:8"]]
+ 00b4b398 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a3a4 bytes 80a205f9
+ 00b4b398 bytes 808205f9
- 00b4a370 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4b364 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4a370 bytes d42e00f0
+ 00b4b364 bytes d42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-73ba1c0697a84c07e645a384e1cf491a"></a>

### [`00b4a3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a3d4.md) → [`00b4b3c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b3c8.md) _ZN8firebase4util12double_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4b3e4",
      "incomplete_value": false,
      "site": "00b4b3e8",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a3f0",
      "incomplete_value": false,
      "site": "00b4a3f4",
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
            "const:54d:8"
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
      "definition_site": "00b4b3f4",
      "incomplete_value": true,
      "site": "00b4b400",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b4a400",
      "incomplete_value": true,
      "site": "00b4a40c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4b3e4",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4b3f4",
      "DATA",
      [
        "storage",
        "01125b60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b3e4",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4b3f4",
      "DATA",
      [
        "storage",
        "01126b20",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a3f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a3d4.md#insn-00b4a3f4) · [`00b4a3f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a3d4.md#insn-00b4a3f0) · [`00b4a3f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a3d4.md#insn-00b4a3f8)
- 新版 [`00b4b3e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b3c8.md#insn-00b4b3e8) · [`00b4b3e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b3c8.md#insn-00b4b3e4) · [`00b4b3ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b3c8.md#insn-00b4b3ec)

~~~diff
- 00b4a3f4 ["INT_ADD", "register:40f0:8", ["const:b4a3f4:8", "const:4:8"]]
- 00b4a3f4 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4b3e8 ["INT_ADD", "register:40f0:8", ["const:b4b3e8:8", "const:4:8"]]
+ 00b4b3e8 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4a3f4 bytes 37430494
+ 00b4b3e8 bytes 2e430494
- 00b4a3f0 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b4a3f0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a3f0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a3f0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b3e4 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4b3e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b3e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b3e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a3f0 bytes 00341591
+ 00b4b3e4 bytes 00681891
- 00b4a3f8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4b3ec ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4a3f8 bytes c82e00f0
+ 00b4b3ec bytes c82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7a48720a24798349eddecbc6d476ac50"></a>

### [`00b4a410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a410.md) → [`00b4b404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b404.md) _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4b430",
      "incomplete_value": true,
      "site": "00b4b430",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a43c",
      "incomplete_value": true,
      "site": "00b4a43c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "definition_site": "00b4b418",
      "incomplete_value": true,
      "site": "00b4b418",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a424",
      "incomplete_value": true,
      "site": "00b4a424",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b424",
      "incomplete_value": false,
      "site": "00b4b428",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a430",
      "incomplete_value": false,
      "site": "00b4a434",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b51:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b414",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b424",
      "PARAM",
      [
        "storage",
        "002c1b51",
        null,
        "string"
      ]
    ],
    [
      "00b4b430",
      "WRITE",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b414",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b424",
      "PARAM",
      [
        "storage",
        "002c1b9b",
        null,
        "string"
      ]
    ],
    [
      "00b4b430",
      "WRITE",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a410.md#insn-00b4a434) · [`00b4a43c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a410.md#insn-00b4a43c) · [`00b4a41c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a410.md#insn-00b4a41c)
- 新版 [`00b4b428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b404.md#insn-00b4b428) · [`00b4b430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b404.md#insn-00b4b430) · [`00b4b410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b404.md#insn-00b4b410)

~~~diff
- 00b4a434 ["INT_ADD", "register:40f0:8", ["const:b4a434:8", "const:4:8"]]
- 00b4a434 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b428 ["INT_ADD", "register:40f0:8", ["const:b4b428:8", "const:4:8"]]
+ 00b4b428 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a434 bytes eb420494
+ 00b4b428 bytes e2420494
- 00b4a43c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b68:8"]]
- 00b4a43c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b430 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b28:8"]]
+ 00b4b430 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a43c bytes 60b605f9
+ 00b4b430 bytes 609605f9
- 00b4a41c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4b410 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4a41c bytes d32e00f0
+ 00b4b410 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b6894a699e02fadfd3f00d36b428b71"></a>

### [`00b4a450`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a450.md) → [`00b4b444`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b444.md) _ZN8firebase4util10enum_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4b470",
      "incomplete_value": true,
      "site": "00b4b470",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a47c",
      "incomplete_value": true,
      "site": "00b4a47c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "definition_site": "00b4b458",
      "incomplete_value": true,
      "site": "00b4b458",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a464",
      "incomplete_value": true,
      "site": "00b4a464",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b460",
      "incomplete_value": false,
      "site": "00b4b468",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a46c",
      "incomplete_value": false,
      "site": "00b4a474",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b51:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
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
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b460",
      "PARAM",
      [
        "storage",
        "002c1b51",
        null,
        "string"
      ]
    ],
    [
      "00b4b470",
      "WRITE",
      [
        "storage",
        "01125b68",
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
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b460",
      "PARAM",
      [
        "storage",
        "002c1b9b",
        null,
        "string"
      ]
    ],
    [
      "00b4b470",
      "WRITE",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a474`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a450.md#insn-00b4a474) · [`00b4a47c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a450.md#insn-00b4a47c) · [`00b4a45c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a450.md#insn-00b4a45c)
- 新版 [`00b4b468`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b444.md#insn-00b4b468) · [`00b4b470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b444.md#insn-00b4b470) · [`00b4b450`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b444.md#insn-00b4b450)

~~~diff
- 00b4a474 ["INT_ADD", "register:40f0:8", ["const:b4a474:8", "const:4:8"]]
- 00b4a474 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b468 ["INT_ADD", "register:40f0:8", ["const:b4b468:8", "const:4:8"]]
+ 00b4b468 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a474 bytes db420494
+ 00b4b468 bytes d2420494
- 00b4a47c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b68:8"]]
- 00b4a47c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b470 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b28:8"]]
+ 00b4b470 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a47c bytes 60b605f9
+ 00b4b470 bytes 609605f9
- 00b4a45c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4b450 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4a45c bytes d32e00f0
+ 00b4b450 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b9adc77a493b3751e36e32c07d4c5798"></a>

### [`00b4a490`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a490.md) → [`00b4b484`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b484.md) _ZN8firebase4util10enum_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4b4b4",
      "incomplete_value": true,
      "site": "00b4b4b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a4c0",
      "incomplete_value": true,
      "site": "00b4a4c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "definition_site": "00b4b498",
      "incomplete_value": true,
      "site": "00b4b498",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a4a4",
      "incomplete_value": true,
      "site": "00b4a4a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b4a4",
      "incomplete_value": false,
      "site": "00b4b4ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a4b0",
      "incomplete_value": false,
      "site": "00b4a4b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b51:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b494",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b4a4",
      "PARAM",
      [
        "storage",
        "002c1b51",
        null,
        "string"
      ]
    ],
    [
      "00b4b4b4",
      "WRITE",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b494",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b4a4",
      "PARAM",
      [
        "storage",
        "002c1b9b",
        null,
        "string"
      ]
    ],
    [
      "00b4b4b4",
      "WRITE",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a4b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a490.md#insn-00b4a4b8) · [`00b4a4c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a490.md#insn-00b4a4c0) · [`00b4a49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a490.md#insn-00b4a49c)
- 新版 [`00b4b4ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b484.md#insn-00b4b4ac) · [`00b4b4b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b484.md#insn-00b4b4b4) · [`00b4b490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b484.md#insn-00b4b490)

~~~diff
- 00b4a4b8 ["INT_ADD", "register:40f0:8", ["const:b4a4b8:8", "const:4:8"]]
- 00b4a4b8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b4ac ["INT_ADD", "register:40f0:8", ["const:b4b4ac:8", "const:4:8"]]
+ 00b4b4ac ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a4b8 bytes ca420494
+ 00b4b4ac bytes c1420494
- 00b4a4c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b68:8"]]
- 00b4a4c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b4b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b28:8"]]
+ 00b4b4b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a4c0 bytes 60b605f9
+ 00b4b4b4 bytes 609605f9
- 00b4a49c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4b490 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4a49c bytes d32e00f0
+ 00b4b490 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7f74d3310e3412eafe8e5622566e5b3d"></a>

### [`00b4a4d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a4d4.md) → [`00b4b4c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b4c8.md) _ZN8firebase4util10enum_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4b4f8",
      "incomplete_value": true,
      "site": "00b4b4f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a504",
      "incomplete_value": true,
      "site": "00b4a504",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "definition_site": "00b4b4dc",
      "incomplete_value": true,
      "site": "00b4b4dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a4e8",
      "incomplete_value": true,
      "site": "00b4a4e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b4e4",
      "incomplete_value": false,
      "site": "00b4b4f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a4f0",
      "incomplete_value": false,
      "site": "00b4a4fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b51:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b4d8",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b4e4",
      "PARAM",
      [
        "storage",
        "002c1b51",
        null,
        "string"
      ]
    ],
    [
      "00b4b4f8",
      "WRITE",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b4d8",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b4e4",
      "PARAM",
      [
        "storage",
        "002c1b9b",
        null,
        "string"
      ]
    ],
    [
      "00b4b4f8",
      "WRITE",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a4fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a4d4.md#insn-00b4a4fc) · [`00b4a504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a4d4.md#insn-00b4a504) · [`00b4a4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a4d4.md#insn-00b4a4e0)
- 新版 [`00b4b4f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b4c8.md#insn-00b4b4f0) · [`00b4b4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b4c8.md#insn-00b4b4f8) · [`00b4b4d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b4c8.md#insn-00b4b4d4)

~~~diff
- 00b4a4fc ["INT_ADD", "register:40f0:8", ["const:b4a4fc:8", "const:4:8"]]
- 00b4a4fc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b4f0 ["INT_ADD", "register:40f0:8", ["const:b4b4f0:8", "const:4:8"]]
+ 00b4b4f0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a4fc bytes b9420494
+ 00b4b4f0 bytes b0420494
- 00b4a504 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b68:8"]]
- 00b4a504 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b4f8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b28:8"]]
+ 00b4b4f8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a504 bytes 60b605f9
+ 00b4b4f8 bytes 609605f9
- 00b4a4e0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4b4d4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4a4e0 bytes d32e00f0
+ 00b4b4d4 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f67dbe5ba59bcf99101246d1d8e033e4"></a>

### [`00b4a524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a524.md) → [`00b4b518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b518.md) _ZN8firebase4util10enum_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4b5a0",
      "incomplete_value": true,
      "site": "00b4b5a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a5ac",
      "incomplete_value": true,
      "site": "00b4a5ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "definition_site": "00b4b54c",
      "incomplete_value": true,
      "site": "00b4b558",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
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
      "definition_site": "00b4a558",
      "incomplete_value": true,
      "site": "00b4a564",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:b68:8"
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
      "00b4b52c",
      "READ",
      [
        "storage",
        "01125b70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b54c",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b5a0",
      "WRITE",
      [
        "storage",
        "01125b70",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b52c",
      "READ",
      [
        "storage",
        "01126b30",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b54c",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b5a0",
      "WRITE",
      [
        "storage",
        "01126b30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a524.md#insn-00b4a564) · [`00b4a5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a524.md#insn-00b4a5ac) · [`00b4a534`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a524.md#insn-00b4a534)
- 新版 [`00b4b558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b518.md#insn-00b4b558) · [`00b4b5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b518.md#insn-00b4b5a0) · [`00b4b528`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b518.md#insn-00b4b528)

~~~diff
- 00b4a564 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a564 ["INT_ADD", "register:40f0:8", ["const:b4a564:8", "const:4:8"]]
- 00b4a564 ["CALLIND", null, ["register:0:8"]]
+ 00b4b558 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b558 ["INT_ADD", "register:40f0:8", ["const:b4b558:8", "const:4:8"]]
+ 00b4b558 ["CALLIND", null, ["register:0:8"]]
- 00b4a564 bytes 00013fd6
+ 00b4b558 bytes 00013fd6
- 00b4a5ac ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4a5ac ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b70:8"]]
- 00b4a5ac ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4b5a0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4b5a0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b30:8"]]
+ 00b4b5a0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4a5ac bytes a0c22d39
+ 00b4b5a0 bytes a0c22c39
- 00b4a534 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4b528 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4a534 bytes d52e00f0
+ 00b4b528 bytes d52e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a708a083aa083bb05233b77d8d90021"></a>

### [`00b4a5c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a5c0.md) → [`00b4b5b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b5b4.md) _ZN8firebase4util10enum_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4b5f0",
      "incomplete_value": true,
      "site": "00b4b5f0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a5fc",
      "incomplete_value": true,
      "site": "00b4a5fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b70:8"
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
      "definition_site": "00b4b640",
      "incomplete_value": true,
      "site": "00b4b640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a64c",
      "incomplete_value": true,
      "site": "00b4a64c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "definition_site": "00b4b5cc",
      "incomplete_value": true,
      "site": "00b4b5cc",
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
      "definition_site": "00b4a5d8",
      "incomplete_value": true,
      "site": "00b4a5d8",
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
      "00b4b5c8",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b5d4",
      "READ",
      [
        "storage",
        "01125b70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b5f0",
      "WRITE",
      [
        "storage",
        "01125b70",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b5c8",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b5d4",
      "READ",
      [
        "storage",
        "01126b30",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b5f0",
      "WRITE",
      [
        "storage",
        "01126b30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a5fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a5c0.md#insn-00b4a5fc) · [`00b4a648`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a5c0.md#insn-00b4a648) · [`00b4a64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a5c0.md#insn-00b4a64c)
- 新版 [`00b4b5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b5b4.md#insn-00b4b5f0) · [`00b4b63c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b5b4.md#insn-00b4b63c) · [`00b4b640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b5b4.md#insn-00b4b640)

~~~diff
- 00b4a5fc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4a5fc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4a5fc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b70:8"]]
- 00b4a5fc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4b5f0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4b5f0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4b5f0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b30:8"]]
+ 00b4b5f0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4a5fc bytes bfc22d39
+ 00b4b5f0 bytes bfc22c39
- 00b4a648 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a648 ["INT_ADD", "register:40f0:8", ["const:b4a648:8", "const:4:8"]]
- 00b4a648 ["CALLIND", null, ["register:0:8"]]
+ 00b4b63c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b63c ["INT_ADD", "register:40f0:8", ["const:b4b63c:8", "const:4:8"]]
+ 00b4b63c ["CALLIND", null, ["register:0:8"]]
- 00b4a648 bytes 00013fd6
+ 00b4b63c bytes 00013fd6
- 00b4a64c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b68:8"]]
- 00b4a64c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4a64c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4b640 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b28:8"]]
+ 00b4b640 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4b640 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4a64c bytes 9fb605f9
+ 00b4b640 bytes 9f9605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f89a45933cbfd85f44014dc7b8ec3c98"></a>

### [`00b4a660`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a660.md) → [`00b4b654`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b654.md) _ZN8firebase4util10enum_class14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b4b694",
      "incomplete_value": true,
      "site": "00b4b694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a6a0",
      "incomplete_value": true,
      "site": "00b4a6a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "definition_site": "00b4b670",
      "incomplete_value": true,
      "site": "00b4b670",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a67c",
      "incomplete_value": true,
      "site": "00b4a67c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b678",
      "incomplete_value": false,
      "site": "00b4b68c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a684",
      "incomplete_value": false,
      "site": "00b4a698",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b51:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b668",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b678",
      "PARAM",
      [
        "storage",
        "002c1b51",
        null,
        "string"
      ]
    ],
    [
      "00b4b694",
      "WRITE",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b668",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b678",
      "PARAM",
      [
        "storage",
        "002c1b9b",
        null,
        "string"
      ]
    ],
    [
      "00b4b694",
      "WRITE",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a660.md#insn-00b4a698) · [`00b4a6a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a660.md#insn-00b4a6a0) · [`00b4a66c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a660.md#insn-00b4a66c)
- 新版 [`00b4b68c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b654.md#insn-00b4b68c) · [`00b4b694`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b654.md#insn-00b4b694) · [`00b4b660`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b654.md#insn-00b4b660)

~~~diff
- 00b4a698 ["INT_ADD", "register:40f0:8", ["const:b4a698:8", "const:4:8"]]
- 00b4a698 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b68c ["INT_ADD", "register:40f0:8", ["const:b4b68c:8", "const:4:8"]]
+ 00b4b68c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a698 bytes 52420494
+ 00b4b68c bytes 49420494
- 00b4a6a0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b68:8"]]
- 00b4a6a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b694 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b28:8"]]
+ 00b4b694 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a6a0 bytes 80b605f9
+ 00b4b694 bytes 809605f9
- 00b4a66c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4b660 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4a66c bytes d42e00f0
+ 00b4b660 bytes d42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d95a01ac03af9917fd52b52b7944830a"></a>

### [`00b4a6d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a6d0.md) → [`00b4b6c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b6c4.md) _ZN8firebase4util10enum_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4b6e0",
      "incomplete_value": false,
      "site": "00b4b6e4",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a6ec",
      "incomplete_value": false,
      "site": "00b4a6f0",
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
            "const:30b:8"
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
      "definition_site": "00b4b6f0",
      "incomplete_value": true,
      "site": "00b4b6fc",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b4a6fc",
      "incomplete_value": true,
      "site": "00b4a708",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4b6e0",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4b6f0",
      "DATA",
      [
        "storage",
        "01125b78",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b6e0",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4b6f0",
      "DATA",
      [
        "storage",
        "01126b38",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a6f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a6d0.md#insn-00b4a6f0) · [`00b4a6ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a6d0.md#insn-00b4a6ec) · [`00b4a6f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a6d0.md#insn-00b4a6f4)
- 新版 [`00b4b6e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b6c4.md#insn-00b4b6e4) · [`00b4b6e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b6c4.md#insn-00b4b6e0) · [`00b4b6e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b6c4.md#insn-00b4b6e8)

~~~diff
- 00b4a6f0 ["INT_ADD", "register:40f0:8", ["const:b4a6f0:8", "const:4:8"]]
- 00b4a6f0 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4b6e4 ["INT_ADD", "register:40f0:8", ["const:b4b6e4:8", "const:4:8"]]
+ 00b4b6e4 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4a6f0 bytes 78420494
+ 00b4b6e4 bytes 6f420494
- 00b4a6ec ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4a6ec ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a6ec ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a6ec ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b6e0 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4b6e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b6e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b6e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a6ec bytes 002c0c91
+ 00b4b6e0 bytes 008c1191
- 00b4a6f4 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4b6e8 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4a6f4 bytes c82e00f0
+ 00b4b6e8 bytes c82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-77d0bb849e55dc28d5fe3da253bd561e"></a>

### [`00b4a70c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a70c.md) → [`00b4b700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b700.md) _ZN8firebase4util10enum_class13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4b740",
      "incomplete_value": true,
      "site": "00b4b740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a74c",
      "incomplete_value": true,
      "site": "00b4a74c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b68:8"
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
      "definition_site": "00b4b71c",
      "incomplete_value": true,
      "site": "00b4b71c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a728",
      "incomplete_value": true,
      "site": "00b4a728",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b724",
      "incomplete_value": false,
      "site": "00b4b738",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b9b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a730",
      "incomplete_value": false,
      "site": "00b4a744",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2c1000:8"
          ],
          [
            "leaf",
            "const:b51:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b714",
      "READ",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b724",
      "PARAM",
      [
        "storage",
        "002c1b51",
        null,
        "string"
      ]
    ],
    [
      "00b4b740",
      "WRITE",
      [
        "storage",
        "01125b68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b714",
      "READ",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b724",
      "PARAM",
      [
        "storage",
        "002c1b9b",
        null,
        "string"
      ]
    ],
    [
      "00b4b740",
      "WRITE",
      [
        "storage",
        "01126b28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a70c.md#insn-00b4a744) · [`00b4a74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a70c.md#insn-00b4a74c) · [`00b4a718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a70c.md#insn-00b4a718)
- 新版 [`00b4b738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b700.md#insn-00b4b738) · [`00b4b740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b700.md#insn-00b4b740) · [`00b4b70c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b700.md#insn-00b4b70c)

~~~diff
- 00b4a744 ["INT_ADD", "register:40f0:8", ["const:b4a744:8", "const:4:8"]]
- 00b4a744 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b738 ["INT_ADD", "register:40f0:8", ["const:b4b738:8", "const:4:8"]]
+ 00b4b738 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a744 bytes 27420494
+ 00b4b738 bytes 1e420494
- 00b4a74c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b68:8"]]
- 00b4a74c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b740 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b28:8"]]
+ 00b4b740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a74c bytes 80b605f9
+ 00b4b740 bytes 809605f9
- 00b4a718 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4b70c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4a718 bytes d42e00f0
+ 00b4b70c bytes d42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-28378355cf56ece1b7f78998a9fcda5b"></a>

### [`00b4a77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a77c.md) → [`00b4b770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b770.md) _ZN8firebase4util10enum_class10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4b78c",
      "incomplete_value": false,
      "site": "00b4b790",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a798",
      "incomplete_value": false,
      "site": "00b4a79c",
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
            "const:54d:8"
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
      "definition_site": "00b4b79c",
      "incomplete_value": true,
      "site": "00b4b7a8",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b4a7a8",
      "incomplete_value": true,
      "site": "00b4a7b4",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4b78c",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4b79c",
      "DATA",
      [
        "storage",
        "01125b88",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4b78c",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4b79c",
      "DATA",
      [
        "storage",
        "01126b48",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a79c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a77c.md#insn-00b4a79c) · [`00b4a798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a77c.md#insn-00b4a798) · [`00b4a7a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a77c.md#insn-00b4a7a0)
- 新版 [`00b4b790`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b770.md#insn-00b4b790) · [`00b4b78c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b770.md#insn-00b4b78c) · [`00b4b794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b770.md#insn-00b4b794)

~~~diff
- 00b4a79c ["INT_ADD", "register:40f0:8", ["const:b4a79c:8", "const:4:8"]]
- 00b4a79c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4b790 ["INT_ADD", "register:40f0:8", ["const:b4b790:8", "const:4:8"]]
+ 00b4b790 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4a79c bytes 4d420494
+ 00b4b790 bytes 44420494
- 00b4a798 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b4a798 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a798 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4a798 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4b78c ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4b78c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b78c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4b78c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4a798 bytes 00341591
+ 00b4b78c bytes 00681891
- 00b4a7a0 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4b794 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4a7a0 bytes c82e00f0
+ 00b4b794 bytes c82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b47f74de0dfd6c13cca4756254bc33d4"></a>

### [`00b4a7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a7b8.md) → [`00b4b7ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b7ac.md) _ZN8firebase4util4file19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4b7d8",
      "incomplete_value": true,
      "site": "00b4b7d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a7e4",
      "incomplete_value": true,
      "site": "00b4a7e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "definition_site": "00b4b7c0",
      "incomplete_value": true,
      "site": "00b4b7c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a7cc",
      "incomplete_value": true,
      "site": "00b4a7cc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b7cc",
      "incomplete_value": false,
      "site": "00b4b7d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:d85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a7d8",
      "incomplete_value": false,
      "site": "00b4a7dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:cb6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b7bc",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b7cc",
      "PARAM",
      [
        "storage",
        "002b6cb6",
        null,
        "string"
      ]
    ],
    [
      "00b4b7d8",
      "WRITE",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b7bc",
      "READ",
      [
        "storage",
        "01126b50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b7cc",
      "PARAM",
      [
        "storage",
        "002b6d85",
        null,
        "string"
      ]
    ],
    [
      "00b4b7d8",
      "WRITE",
      [
        "storage",
        "01126b50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a7b8.md#insn-00b4a7dc) · [`00b4a7e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a7b8.md#insn-00b4a7e4) · [`00b4a7c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a7b8.md#insn-00b4a7c4)
- 新版 [`00b4b7d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b7ac.md#insn-00b4b7d0) · [`00b4b7d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b7ac.md#insn-00b4b7d8) · [`00b4b7b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b7ac.md#insn-00b4b7b8)

~~~diff
- 00b4a7dc ["INT_ADD", "register:40f0:8", ["const:b4a7dc:8", "const:4:8"]]
- 00b4a7dc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b7d0 ["INT_ADD", "register:40f0:8", ["const:b4b7d0:8", "const:4:8"]]
+ 00b4b7d0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a7dc bytes 01420494
+ 00b4b7d0 bytes f8410494
- 00b4a7e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b90:8"]]
- 00b4a7e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b7d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b50:8"]]
+ 00b4b7d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a7e4 bytes 60ca05f9
+ 00b4b7d8 bytes 60aa05f9
- 00b4a7c4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4b7b8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4a7c4 bytes d32e00f0
+ 00b4b7b8 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f708b357ec6b0b10d1b13612d86c8f25"></a>

### [`00b4a7f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a7f8.md) → [`00b4b7ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b7ec.md) _ZN8firebase4util4file19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4b818",
      "incomplete_value": true,
      "site": "00b4b818",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a824",
      "incomplete_value": true,
      "site": "00b4a824",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "definition_site": "00b4b800",
      "incomplete_value": true,
      "site": "00b4b800",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a80c",
      "incomplete_value": true,
      "site": "00b4a80c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b808",
      "incomplete_value": false,
      "site": "00b4b810",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:d85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a814",
      "incomplete_value": false,
      "site": "00b4a81c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:cb6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b7fc",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b808",
      "PARAM",
      [
        "storage",
        "002b6cb6",
        null,
        "string"
      ]
    ],
    [
      "00b4b818",
      "WRITE",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b7fc",
      "READ",
      [
        "storage",
        "01126b50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b808",
      "PARAM",
      [
        "storage",
        "002b6d85",
        null,
        "string"
      ]
    ],
    [
      "00b4b818",
      "WRITE",
      [
        "storage",
        "01126b50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a81c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a7f8.md#insn-00b4a81c) · [`00b4a824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a7f8.md#insn-00b4a824) · [`00b4a804`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a7f8.md#insn-00b4a804)
- 新版 [`00b4b810`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b7ec.md#insn-00b4b810) · [`00b4b818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b7ec.md#insn-00b4b818) · [`00b4b7f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b7ec.md#insn-00b4b7f8)

~~~diff
- 00b4a81c ["INT_ADD", "register:40f0:8", ["const:b4a81c:8", "const:4:8"]]
- 00b4a81c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b810 ["INT_ADD", "register:40f0:8", ["const:b4b810:8", "const:4:8"]]
+ 00b4b810 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a81c bytes f1410494
+ 00b4b810 bytes e8410494
- 00b4a824 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b90:8"]]
- 00b4a824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b818 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b50:8"]]
+ 00b4b818 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a824 bytes 60ca05f9
+ 00b4b818 bytes 60aa05f9
- 00b4a804 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4b7f8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4a804 bytes d32e00f0
+ 00b4b7f8 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0411146891adfb41ff0e897a6eb227f5"></a>

### [`00b4a838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a838.md) → [`00b4b82c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b82c.md) _ZN8firebase4util4file10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4b85c",
      "incomplete_value": true,
      "site": "00b4b85c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a868",
      "incomplete_value": true,
      "site": "00b4a868",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "definition_site": "00b4b840",
      "incomplete_value": true,
      "site": "00b4b840",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a84c",
      "incomplete_value": true,
      "site": "00b4a84c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b84c",
      "incomplete_value": false,
      "site": "00b4b854",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:d85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a858",
      "incomplete_value": false,
      "site": "00b4a860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:cb6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b83c",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b84c",
      "PARAM",
      [
        "storage",
        "002b6cb6",
        null,
        "string"
      ]
    ],
    [
      "00b4b85c",
      "WRITE",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b83c",
      "READ",
      [
        "storage",
        "01126b50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b84c",
      "PARAM",
      [
        "storage",
        "002b6d85",
        null,
        "string"
      ]
    ],
    [
      "00b4b85c",
      "WRITE",
      [
        "storage",
        "01126b50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a860`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a838.md#insn-00b4a860) · [`00b4a868`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a838.md#insn-00b4a868) · [`00b4a844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a838.md#insn-00b4a844)
- 新版 [`00b4b854`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b82c.md#insn-00b4b854) · [`00b4b85c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b82c.md#insn-00b4b85c) · [`00b4b838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b82c.md#insn-00b4b838)

~~~diff
- 00b4a860 ["INT_ADD", "register:40f0:8", ["const:b4a860:8", "const:4:8"]]
- 00b4a860 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b854 ["INT_ADD", "register:40f0:8", ["const:b4b854:8", "const:4:8"]]
+ 00b4b854 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a860 bytes e0410494
+ 00b4b854 bytes d7410494
- 00b4a868 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b90:8"]]
- 00b4a868 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b85c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b50:8"]]
+ 00b4b85c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a868 bytes 60ca05f9
+ 00b4b85c bytes 60aa05f9
- 00b4a844 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4b838 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4a844 bytes d32e00f0
+ 00b4b838 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a1b635fbd5bcd3478143f052c68cef23"></a>

### [`00b4a87c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a87c.md) → [`00b4b870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b870.md) _ZN8firebase4util4file10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4b8a0",
      "incomplete_value": true,
      "site": "00b4b8a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a8ac",
      "incomplete_value": true,
      "site": "00b4a8ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "definition_site": "00b4b884",
      "incomplete_value": true,
      "site": "00b4b884",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a890",
      "incomplete_value": true,
      "site": "00b4a890",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4b88c",
      "incomplete_value": false,
      "site": "00b4b898",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:d85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a898",
      "incomplete_value": false,
      "site": "00b4a8a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:cb6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4b880",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b88c",
      "PARAM",
      [
        "storage",
        "002b6cb6",
        null,
        "string"
      ]
    ],
    [
      "00b4b8a0",
      "WRITE",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4b880",
      "READ",
      [
        "storage",
        "01126b50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b88c",
      "PARAM",
      [
        "storage",
        "002b6d85",
        null,
        "string"
      ]
    ],
    [
      "00b4b8a0",
      "WRITE",
      [
        "storage",
        "01126b50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a8a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a87c.md#insn-00b4a8a4) · [`00b4a8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a87c.md#insn-00b4a8ac) · [`00b4a888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a87c.md#insn-00b4a888)
- 新版 [`00b4b898`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b870.md#insn-00b4b898) · [`00b4b8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b870.md#insn-00b4b8a0) · [`00b4b87c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b870.md#insn-00b4b87c)

~~~diff
- 00b4a8a4 ["INT_ADD", "register:40f0:8", ["const:b4a8a4:8", "const:4:8"]]
- 00b4a8a4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4b898 ["INT_ADD", "register:40f0:8", ["const:b4b898:8", "const:4:8"]]
+ 00b4b898 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4a8a4 bytes cf410494
+ 00b4b898 bytes c6410494
- 00b4a8ac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b90:8"]]
- 00b4a8ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4b8a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:b50:8"]]
+ 00b4b8a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4a8ac bytes 60ca05f9
+ 00b4b8a0 bytes 60aa05f9
- 00b4a888 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4b87c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4a888 bytes d32e00f0
+ 00b4b87c bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd2dfdc865d19dd92e9f695a4384efd1"></a>

### [`00b4a8cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a8cc.md) → [`00b4b8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b8c0.md) _ZN8firebase4util4file15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4b948",
      "incomplete_value": true,
      "site": "00b4b948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a954",
      "incomplete_value": true,
      "site": "00b4a954",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b98:8"
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
      "definition_site": "00b4b8f4",
      "incomplete_value": true,
      "site": "00b4b900",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:b50:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a900",
      "incomplete_value": true,
      "site": "00b4a90c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
              ],
              [
                "leaf",
                "const:b90:8"
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
      "00b4b8d4",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b8f4",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b948",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b8d4",
      "READ",
      [
        "storage",
        "01126b58",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b8f4",
      "READ",
      [
        "storage",
        "01126b50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b948",
      "WRITE",
      [
        "storage",
        "01126b58",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a8cc.md#insn-00b4a90c) · [`00b4a954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a8cc.md#insn-00b4a954) · [`00b4a8dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a8cc.md#insn-00b4a8dc)
- 新版 [`00b4b900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b8c0.md#insn-00b4b900) · [`00b4b948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b8c0.md#insn-00b4b948) · [`00b4b8d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b8c0.md#insn-00b4b8d0)

~~~diff
- 00b4a90c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a90c ["INT_ADD", "register:40f0:8", ["const:b4a90c:8", "const:4:8"]]
- 00b4a90c ["CALLIND", null, ["register:0:8"]]
+ 00b4b900 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b900 ["INT_ADD", "register:40f0:8", ["const:b4b900:8", "const:4:8"]]
+ 00b4b900 ["CALLIND", null, ["register:0:8"]]
- 00b4a90c bytes 00013fd6
+ 00b4b900 bytes 00013fd6
- 00b4a954 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4a954 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b98:8"]]
- 00b4a954 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4b948 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4b948 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:b58:8"]]
+ 00b4b948 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4a954 bytes a0622e39
+ 00b4b948 bytes a0622d39
- 00b4a8dc ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4b8d0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4a8dc bytes d52e00f0
+ 00b4b8d0 bytes d52e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-34587011b1a0c1cbf53365b3c806b98d"></a>

### [`00b4a968`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a968.md) → [`00b4b95c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b95c.md) _ZN8firebase4util4file12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4b998",
      "incomplete_value": true,
      "site": "00b4b998",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a9a4",
      "incomplete_value": true,
      "site": "00b4a9a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:b98:8"
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
      "definition_site": "00b4b9e8",
      "incomplete_value": true,
      "site": "00b4b9e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4a9f4",
      "incomplete_value": true,
      "site": "00b4a9f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "definition_site": "00b4b974",
      "incomplete_value": true,
      "site": "00b4b974",
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
      "definition_site": "00b4a980",
      "incomplete_value": true,
      "site": "00b4a980",
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
      "00b4b970",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b97c",
      "READ",
      [
        "storage",
        "01125b98",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b998",
      "WRITE",
      [
        "storage",
        "01125b98",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4b970",
      "READ",
      [
        "storage",
        "01126b50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4b97c",
      "READ",
      [
        "storage",
        "01126b58",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4b998",
      "WRITE",
      [
        "storage",
        "01126b58",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4a9a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a968.md#insn-00b4a9a4) · [`00b4a9f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a968.md#insn-00b4a9f0) · [`00b4a9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4a968.md#insn-00b4a9f4)
- 新版 [`00b4b998`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b95c.md#insn-00b4b998) · [`00b4b9e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b95c.md#insn-00b4b9e4) · [`00b4b9e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b95c.md#insn-00b4b9e8)

~~~diff
- 00b4a9a4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4a9a4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4a9a4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b98:8"]]
- 00b4a9a4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4b998 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4b998 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4b998 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:b58:8"]]
+ 00b4b998 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4a9a4 bytes bf622e39
+ 00b4b998 bytes bf622d39
- 00b4a9f0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4a9f0 ["INT_ADD", "register:40f0:8", ["const:b4a9f0:8", "const:4:8"]]
- 00b4a9f0 ["CALLIND", null, ["register:0:8"]]
+ 00b4b9e4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4b9e4 ["INT_ADD", "register:40f0:8", ["const:b4b9e4:8", "const:4:8"]]
+ 00b4b9e4 ["CALLIND", null, ["register:0:8"]]
- 00b4a9f0 bytes 00013fd6
+ 00b4b9e4 bytes 00013fd6
- 00b4a9f4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b90:8"]]
- 00b4a9f4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4a9f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4b9e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b50:8"]]
+ 00b4b9e8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4b9e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4a9f4 bytes 9fca05f9
+ 00b4b9e8 bytes 9faa05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0378d82a2a8305d99a6c0cdb3515674f"></a>

### [`00b4aa08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aa08.md) → [`00b4b9fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b9fc.md) _ZN8firebase4util4file14CacheMethodIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md) [`00c5b000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b000.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md) [`00c5bfd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfd0.md)

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
      "definition_site": "00b4ba3c",
      "incomplete_value": true,
      "site": "00b4ba3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aa48",
      "incomplete_value": true,
      "site": "00b4aa48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "definition_site": "00b4ba18",
      "incomplete_value": true,
      "site": "00b4ba18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aa24",
      "incomplete_value": true,
      "site": "00b4aa24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ba20",
      "incomplete_value": false,
      "site": "00b4ba34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:d85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aa2c",
      "incomplete_value": false,
      "site": "00b4aa40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:cb6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ba10",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ba20",
      "PARAM",
      [
        "storage",
        "002b6cb6",
        null,
        "string"
      ]
    ],
    [
      "00b4ba3c",
      "WRITE",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ba10",
      "READ",
      [
        "storage",
        "01126b50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ba20",
      "PARAM",
      [
        "storage",
        "002b6d85",
        null,
        "string"
      ]
    ],
    [
      "00b4ba3c",
      "WRITE",
      [
        "storage",
        "01126b50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aa40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aa08.md#insn-00b4aa40) · [`00b4aa48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aa08.md#insn-00b4aa48) · [`00b4aa14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aa08.md#insn-00b4aa14)
- 新版 [`00b4ba34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b9fc.md#insn-00b4ba34) · [`00b4ba3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b9fc.md#insn-00b4ba3c) · [`00b4ba08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4b9fc.md#insn-00b4ba08)

~~~diff
- 00b4aa40 ["INT_ADD", "register:40f0:8", ["const:b4aa40:8", "const:4:8"]]
- 00b4aa40 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4ba34 ["INT_ADD", "register:40f0:8", ["const:b4ba34:8", "const:4:8"]]
+ 00b4ba34 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4aa40 bytes 68410494
+ 00b4ba34 bytes 5f410494
- 00b4aa48 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b90:8"]]
- 00b4aa48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ba3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b50:8"]]
+ 00b4ba3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4aa48 bytes 80ca05f9
+ 00b4ba3c bytes 80aa05f9
- 00b4aa14 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4ba08 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4aa14 bytes d42e00f0
+ 00b4ba08 bytes d42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1bd64678d2f40ad4674c422a67924d1f"></a>

### [`00b4aa78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aa78.md) → [`00b4ba6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4ba6c.md) _ZN8firebase4util4file11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b5e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b5e0.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5c5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c5b0.md) · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4ba88",
      "incomplete_value": false,
      "site": "00b4ba8c",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aa94",
      "incomplete_value": false,
      "site": "00b4aa98",
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
            "const:30b:8"
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
      "definition_site": "00b4ba98",
      "incomplete_value": true,
      "site": "00b4baa4",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b4aaa4",
      "incomplete_value": true,
      "site": "00b4aab0",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4ba88",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4ba98",
      "DATA",
      [
        "storage",
        "01125ba0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ba88",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4ba98",
      "DATA",
      [
        "storage",
        "01126b60",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aa98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aa78.md#insn-00b4aa98) · [`00b4aa94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aa78.md#insn-00b4aa94) · [`00b4aa9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aa78.md#insn-00b4aa9c)
- 新版 [`00b4ba8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4ba6c.md#insn-00b4ba8c) · [`00b4ba88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4ba6c.md#insn-00b4ba88) · [`00b4ba90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4ba6c.md#insn-00b4ba90)

~~~diff
- 00b4aa98 ["INT_ADD", "register:40f0:8", ["const:b4aa98:8", "const:4:8"]]
- 00b4aa98 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4ba8c ["INT_ADD", "register:40f0:8", ["const:b4ba8c:8", "const:4:8"]]
+ 00b4ba8c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4aa98 bytes 8e410494
+ 00b4ba8c bytes 85410494
- 00b4aa94 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4aa94 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4aa94 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4aa94 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ba88 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4ba88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ba88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ba88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4aa94 bytes 002c0c91
+ 00b4ba88 bytes 008c1191
- 00b4aa9c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4ba90 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4aa9c bytes c82e00f0
+ 00b4ba90 bytes c82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e71ff812138bd4bdb478427d82934c66"></a>

### [`00b4aab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aab4.md) → [`00b4baa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4baa8.md) _ZN8firebase4util4file13CacheFieldIdsEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 2件 [`00c5afc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afc0.md) [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 2件 [`00c5bf90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf90.md) [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4bae8",
      "incomplete_value": true,
      "site": "00b4bae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aaf4",
      "incomplete_value": true,
      "site": "00b4aaf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:b90:8"
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
      "definition_site": "00b4bac4",
      "incomplete_value": true,
      "site": "00b4bac4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aad0",
      "incomplete_value": true,
      "site": "00b4aad0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4bacc",
      "incomplete_value": false,
      "site": "00b4bae0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:d85:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aad8",
      "incomplete_value": false,
      "site": "00b4aaec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b6000:8"
          ],
          [
            "leaf",
            "const:cb6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4babc",
      "READ",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bacc",
      "PARAM",
      [
        "storage",
        "002b6cb6",
        null,
        "string"
      ]
    ],
    [
      "00b4bae8",
      "WRITE",
      [
        "storage",
        "01125b90",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4babc",
      "READ",
      [
        "storage",
        "01126b50",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bacc",
      "PARAM",
      [
        "storage",
        "002b6d85",
        null,
        "string"
      ]
    ],
    [
      "00b4bae8",
      "WRITE",
      [
        "storage",
        "01126b50",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aaec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aab4.md#insn-00b4aaec) · [`00b4aaf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aab4.md#insn-00b4aaf4) · [`00b4aac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aab4.md#insn-00b4aac0)
- 新版 [`00b4bae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4baa8.md#insn-00b4bae0) · [`00b4bae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4baa8.md#insn-00b4bae8) · [`00b4bab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4baa8.md#insn-00b4bab4)

~~~diff
- 00b4aaec ["INT_ADD", "register:40f0:8", ["const:b4aaec:8", "const:4:8"]]
- 00b4aaec ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4bae0 ["INT_ADD", "register:40f0:8", ["const:b4bae0:8", "const:4:8"]]
+ 00b4bae0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4aaec bytes 3d410494
+ 00b4bae0 bytes 34410494
- 00b4aaf4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b90:8"]]
- 00b4aaf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bae8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:b50:8"]]
+ 00b4bae8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4aaf4 bytes 80ca05f9
+ 00b4bae8 bytes 80aa05f9
- 00b4aac0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4bab4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4aac0 bytes d42e00f0
+ 00b4bab4 bytes d42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d18356d9bc8516e5a4cc39ead973d1f"></a>

### [`00b4ab24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ab24.md) → [`00b4bb18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bb18.md) _ZN8firebase4util4file10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4bb34",
      "incomplete_value": false,
      "site": "00b4bb38",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ab40",
      "incomplete_value": false,
      "site": "00b4ab44",
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
            "const:54d:8"
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
      "definition_site": "00b4bb44",
      "incomplete_value": true,
      "site": "00b4bb50",
      "value": [
        "LOAD",
        "8",
        [
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
      "definition_site": "00b4ab50",
      "incomplete_value": true,
      "site": "00b4ab5c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b4bb34",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4bb44",
      "DATA",
      [
        "storage",
        "01125be0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4bb34",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4bb44",
      "DATA",
      [
        "storage",
        "01126ba0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ab44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ab24.md#insn-00b4ab44) · [`00b4ab40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ab24.md#insn-00b4ab40) · [`00b4ab48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ab24.md#insn-00b4ab48)
- 新版 [`00b4bb38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bb18.md#insn-00b4bb38) · [`00b4bb34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bb18.md#insn-00b4bb34) · [`00b4bb3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bb18.md#insn-00b4bb3c)

~~~diff
- 00b4ab44 ["INT_ADD", "register:40f0:8", ["const:b4ab44:8", "const:4:8"]]
- 00b4ab44 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4bb38 ["INT_ADD", "register:40f0:8", ["const:b4bb38:8", "const:4:8"]]
+ 00b4bb38 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4ab44 bytes 63410494
+ 00b4bb38 bytes 5a410494
- 00b4ab40 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b4ab40 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ab40 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ab40 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4bb34 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4bb34 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bb34 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bb34 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4ab40 bytes 00341591
+ 00b4bb34 bytes 00681891
- 00b4ab48 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4bb3c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4ab48 bytes c82e00f0
+ 00b4bb3c bytes c82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3009dbb54f35825fb00411d81041c8c6"></a>

### [`00b4ab60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ab60.md) → [`00b4bb54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bb54.md) _ZN8firebase4util11float_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4bb80",
      "incomplete_value": true,
      "site": "00b4bb80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ab8c",
      "incomplete_value": true,
      "site": "00b4ab8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "definition_site": "00b4bb68",
      "incomplete_value": true,
      "site": "00b4bb68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ab74",
      "incomplete_value": true,
      "site": "00b4ab74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4bb74",
      "incomplete_value": false,
      "site": "00b4bb78",
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
            "const:67c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ab80",
      "incomplete_value": false,
      "site": "00b4ab84",
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
            "const:5af:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4bb64",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bb74",
      "PARAM",
      [
        "storage",
        "002a95af",
        null,
        "string"
      ]
    ],
    [
      "00b4bb80",
      "WRITE",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bb64",
      "READ",
      [
        "storage",
        "01126ba8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bb74",
      "PARAM",
      [
        "storage",
        "002a967c",
        null,
        "string"
      ]
    ],
    [
      "00b4bb80",
      "WRITE",
      [
        "storage",
        "01126ba8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ab84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ab60.md#insn-00b4ab84) · [`00b4ab8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ab60.md#insn-00b4ab8c) · [`00b4ab6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ab60.md#insn-00b4ab6c)
- 新版 [`00b4bb78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bb54.md#insn-00b4bb78) · [`00b4bb80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bb54.md#insn-00b4bb80) · [`00b4bb60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bb54.md#insn-00b4bb60)

~~~diff
- 00b4ab84 ["INT_ADD", "register:40f0:8", ["const:b4ab84:8", "const:4:8"]]
- 00b4ab84 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4bb78 ["INT_ADD", "register:40f0:8", ["const:b4bb78:8", "const:4:8"]]
+ 00b4bb78 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4ab84 bytes 17410494
+ 00b4bb78 bytes 0e410494
- 00b4ab8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be8:8"]]
- 00b4ab8c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bb80 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ba8:8"]]
+ 00b4bb80 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ab8c bytes 60f605f9
+ 00b4bb80 bytes 60d605f9
- 00b4ab6c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4bb60 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4ab6c bytes d32e00f0
+ 00b4bb60 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-59206ede186328135f82f5353df0b255"></a>

### [`00b4aba0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aba0.md) → [`00b4bb94`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bb94.md) _ZN8firebase4util11float_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4bbc0",
      "incomplete_value": true,
      "site": "00b4bbc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4abcc",
      "incomplete_value": true,
      "site": "00b4abcc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "definition_site": "00b4bba8",
      "incomplete_value": true,
      "site": "00b4bba8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4abb4",
      "incomplete_value": true,
      "site": "00b4abb4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4bbb0",
      "incomplete_value": false,
      "site": "00b4bbb8",
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
            "const:67c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4abbc",
      "incomplete_value": false,
      "site": "00b4abc4",
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
            "const:5af:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4bba4",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bbb0",
      "PARAM",
      [
        "storage",
        "002a95af",
        null,
        "string"
      ]
    ],
    [
      "00b4bbc0",
      "WRITE",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bba4",
      "READ",
      [
        "storage",
        "01126ba8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bbb0",
      "PARAM",
      [
        "storage",
        "002a967c",
        null,
        "string"
      ]
    ],
    [
      "00b4bbc0",
      "WRITE",
      [
        "storage",
        "01126ba8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4abc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aba0.md#insn-00b4abc4) · [`00b4abcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aba0.md#insn-00b4abcc) · [`00b4abac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aba0.md#insn-00b4abac)
- 新版 [`00b4bbb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bb94.md#insn-00b4bbb8) · [`00b4bbc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bb94.md#insn-00b4bbc0) · [`00b4bba0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bb94.md#insn-00b4bba0)

~~~diff
- 00b4abc4 ["INT_ADD", "register:40f0:8", ["const:b4abc4:8", "const:4:8"]]
- 00b4abc4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4bbb8 ["INT_ADD", "register:40f0:8", ["const:b4bbb8:8", "const:4:8"]]
+ 00b4bbb8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4abc4 bytes 07410494
+ 00b4bbb8 bytes fe400494
- 00b4abcc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be8:8"]]
- 00b4abcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bbc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ba8:8"]]
+ 00b4bbc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4abcc bytes 60f605f9
+ 00b4bbc0 bytes 60d605f9
- 00b4abac ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4bba0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4abac bytes d32e00f0
+ 00b4bba0 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2577f2d287f05e8ddfb6b455141e56e5"></a>

### [`00b4abe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4abe0.md) → [`00b4bbd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bbd4.md) _ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4bc04",
      "incomplete_value": true,
      "site": "00b4bc04",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ac10",
      "incomplete_value": true,
      "site": "00b4ac10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "definition_site": "00b4bbe8",
      "incomplete_value": true,
      "site": "00b4bbe8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4abf4",
      "incomplete_value": true,
      "site": "00b4abf4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4bbf4",
      "incomplete_value": false,
      "site": "00b4bbfc",
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
            "const:67c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ac00",
      "incomplete_value": false,
      "site": "00b4ac08",
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
            "const:5af:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4bbe4",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bbf4",
      "PARAM",
      [
        "storage",
        "002a95af",
        null,
        "string"
      ]
    ],
    [
      "00b4bc04",
      "WRITE",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bbe4",
      "READ",
      [
        "storage",
        "01126ba8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bbf4",
      "PARAM",
      [
        "storage",
        "002a967c",
        null,
        "string"
      ]
    ],
    [
      "00b4bc04",
      "WRITE",
      [
        "storage",
        "01126ba8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ac08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4abe0.md#insn-00b4ac08) · [`00b4ac10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4abe0.md#insn-00b4ac10) · [`00b4abec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4abe0.md#insn-00b4abec)
- 新版 [`00b4bbfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bbd4.md#insn-00b4bbfc) · [`00b4bc04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bbd4.md#insn-00b4bc04) · [`00b4bbe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bbd4.md#insn-00b4bbe0)

~~~diff
- 00b4ac08 ["INT_ADD", "register:40f0:8", ["const:b4ac08:8", "const:4:8"]]
- 00b4ac08 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4bbfc ["INT_ADD", "register:40f0:8", ["const:b4bbfc:8", "const:4:8"]]
+ 00b4bbfc ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4ac08 bytes f6400494
+ 00b4bbfc bytes ed400494
- 00b4ac10 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be8:8"]]
- 00b4ac10 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bc04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ba8:8"]]
+ 00b4bc04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ac10 bytes 60f605f9
+ 00b4bc04 bytes 60d605f9
- 00b4abec ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4bbe0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4abec bytes d32e00f0
+ 00b4bbe0 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-08bc02a448b311aff4cec0094f500f2b"></a>

### [`00b4ac24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ac24.md) → [`00b4bc18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bc18.md) _ZN8firebase4util11float_class10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4bc48",
      "incomplete_value": true,
      "site": "00b4bc48",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ac54",
      "incomplete_value": true,
      "site": "00b4ac54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "definition_site": "00b4bc2c",
      "incomplete_value": true,
      "site": "00b4bc2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ac38",
      "incomplete_value": true,
      "site": "00b4ac38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4bc34",
      "incomplete_value": false,
      "site": "00b4bc40",
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
            "const:67c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ac40",
      "incomplete_value": false,
      "site": "00b4ac4c",
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
            "const:5af:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4bc28",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bc34",
      "PARAM",
      [
        "storage",
        "002a95af",
        null,
        "string"
      ]
    ],
    [
      "00b4bc48",
      "WRITE",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bc28",
      "READ",
      [
        "storage",
        "01126ba8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bc34",
      "PARAM",
      [
        "storage",
        "002a967c",
        null,
        "string"
      ]
    ],
    [
      "00b4bc48",
      "WRITE",
      [
        "storage",
        "01126ba8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ac4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ac24.md#insn-00b4ac4c) · [`00b4ac54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ac24.md#insn-00b4ac54) · [`00b4ac30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ac24.md#insn-00b4ac30)
- 新版 [`00b4bc40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bc18.md#insn-00b4bc40) · [`00b4bc48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bc18.md#insn-00b4bc48) · [`00b4bc24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bc18.md#insn-00b4bc24)

~~~diff
- 00b4ac4c ["INT_ADD", "register:40f0:8", ["const:b4ac4c:8", "const:4:8"]]
- 00b4ac4c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4bc40 ["INT_ADD", "register:40f0:8", ["const:b4bc40:8", "const:4:8"]]
+ 00b4bc40 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4ac4c bytes e5400494
+ 00b4bc40 bytes dc400494
- 00b4ac54 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:be8:8"]]
- 00b4ac54 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bc48 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ba8:8"]]
+ 00b4bc48 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ac54 bytes 60f605f9
+ 00b4bc48 bytes 60d605f9
- 00b4ac30 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4bc24 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4ac30 bytes d32e00f0
+ 00b4bc24 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db8e17ac6d0175a942c4b5ebd3eabff2"></a>

### [`00b4ac74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ac74.md) → [`00b4bc68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bc68.md) _ZN8firebase4util11float_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4bcf0",
      "incomplete_value": true,
      "site": "00b4bcf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4acfc",
      "incomplete_value": true,
      "site": "00b4acfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
      "definition_site": "00b4bc9c",
      "incomplete_value": true,
      "site": "00b4bca8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1126000:8"
              ],
              [
                "leaf",
                "const:ba8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4aca8",
      "incomplete_value": true,
      "site": "00b4acb4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
            "8",
            [
              [
                "leaf",
                "const:1125000:8"
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
      "00b4bc7c",
      "READ",
      [
        "storage",
        "01125bf0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bc9c",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bcf0",
      "WRITE",
      [
        "storage",
        "01125bf0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4bc7c",
      "READ",
      [
        "storage",
        "01126bb0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bc9c",
      "READ",
      [
        "storage",
        "01126ba8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bcf0",
      "WRITE",
      [
        "storage",
        "01126bb0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4acb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ac74.md#insn-00b4acb4) · [`00b4acfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ac74.md#insn-00b4acfc) · [`00b4ac84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ac74.md#insn-00b4ac84)
- 新版 [`00b4bca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bc68.md#insn-00b4bca8) · [`00b4bcf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bc68.md#insn-00b4bcf0) · [`00b4bc78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bc68.md#insn-00b4bc78)

~~~diff
- 00b4acb4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4acb4 ["INT_ADD", "register:40f0:8", ["const:b4acb4:8", "const:4:8"]]
- 00b4acb4 ["CALLIND", null, ["register:0:8"]]
+ 00b4bca8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4bca8 ["INT_ADD", "register:40f0:8", ["const:b4bca8:8", "const:4:8"]]
+ 00b4bca8 ["CALLIND", null, ["register:0:8"]]
- 00b4acb4 bytes 00013fd6
+ 00b4bca8 bytes 00013fd6
- 00b4acfc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4acfc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:bf0:8"]]
- 00b4acfc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4bcf0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4bcf0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:bb0:8"]]
+ 00b4bcf0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4acfc bytes a0c22f39
+ 00b4bcf0 bytes a0c22e39
- 00b4ac84 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4bc78 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4ac84 bytes d52e00f0
+ 00b4bc78 bytes d52e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79c526a40d6326ecc2410807e45e6e21"></a>

### [`00b4ad10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ad10.md) → [`00b4bd04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bd04.md) _ZN8firebase4util11float_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4bd40",
      "incomplete_value": true,
      "site": "00b4bd40",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:bb0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ad4c",
      "incomplete_value": true,
      "site": "00b4ad4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:bf0:8"
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
      "definition_site": "00b4bd90",
      "incomplete_value": true,
      "site": "00b4bd90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ba8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ad9c",
      "incomplete_value": true,
      "site": "00b4ad9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:be8:8"
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
      "definition_site": "00b4bd1c",
      "incomplete_value": true,
      "site": "00b4bd1c",
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
      "definition_site": "00b4ad28",
      "incomplete_value": true,
      "site": "00b4ad28",
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
      "00b4bd18",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bd24",
      "READ",
      [
        "storage",
        "01125bf0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bd40",
      "WRITE",
      [
        "storage",
        "01125bf0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4bd18",
      "READ",
      [
        "storage",
        "01126ba8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bd24",
      "READ",
      [
        "storage",
        "01126bb0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4bd40",
      "WRITE",
      [
        "storage",
        "01126bb0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ad4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ad10.md#insn-00b4ad4c) · [`00b4ad98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ad10.md#insn-00b4ad98) · [`00b4ad9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ad10.md#insn-00b4ad9c)
- 新版 [`00b4bd40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bd04.md#insn-00b4bd40) · [`00b4bd8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bd04.md#insn-00b4bd8c) · [`00b4bd90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bd04.md#insn-00b4bd90)

~~~diff
- 00b4ad4c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4ad4c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4ad4c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:bf0:8"]]
- 00b4ad4c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4bd40 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4bd40 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4bd40 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:bb0:8"]]
+ 00b4bd40 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4ad4c bytes bfc22f39
+ 00b4bd40 bytes bfc22e39
- 00b4ad98 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4ad98 ["INT_ADD", "register:40f0:8", ["const:b4ad98:8", "const:4:8"]]
- 00b4ad98 ["CALLIND", null, ["register:0:8"]]
+ 00b4bd8c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4bd8c ["INT_ADD", "register:40f0:8", ["const:b4bd8c:8", "const:4:8"]]
+ 00b4bd8c ["CALLIND", null, ["register:0:8"]]
- 00b4ad98 bytes 00013fd6
+ 00b4bd8c bytes 00013fd6
- 00b4ad9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
- 00b4ad9c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4ad9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4bd90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ba8:8"]]
+ 00b4bd90 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4bd90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4ad9c bytes 9ff605f9
+ 00b4bd90 bytes 9fd605f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

