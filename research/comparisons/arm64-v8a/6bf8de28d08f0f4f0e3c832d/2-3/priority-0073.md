# v16.0.2 → v16.0.3 · 最優先の変更候補 (73)

[一覧の目次](README.md)

<a id="compare-938486defe8390364568259085464142"></a>

### [`00b46500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46500.md) → [`00b474f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b474f4.md) _ZN8firebase4util10uribuilder11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b47510",
      "incomplete_value": false,
      "site": "00b47514",
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
      "definition_site": "00b4651c",
      "incomplete_value": false,
      "site": "00b46520",
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
      "definition_site": "00b47520",
      "incomplete_value": true,
      "site": "00b4752c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4652c",
      "incomplete_value": true,
      "site": "00b46538",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b47510",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b47520",
      "DATA",
      [
        "storage",
        "01125808",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47510",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b47520",
      "DATA",
      [
        "storage",
        "011267c8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46520`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46500.md#insn-00b46520) · [`00b4651c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46500.md#insn-00b4651c) · [`00b46524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46500.md#insn-00b46524)
- 新版 [`00b47514`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b474f4.md#insn-00b47514) · [`00b47510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b474f4.md#insn-00b47510) · [`00b47518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b474f4.md#insn-00b47518)

~~~diff
- 00b46520 ["INT_ADD", "register:40f0:8", ["const:b46520:8", "const:4:8"]]
- 00b46520 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b47514 ["INT_ADD", "register:40f0:8", ["const:b47514:8", "const:4:8"]]
+ 00b47514 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b46520 bytes ec520494
+ 00b47514 bytes e3520494
- 00b4651c ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4651c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4651c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4651c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47510 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b47510 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47510 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47510 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4651c bytes 002c0c91
+ 00b47510 bytes 008c1191
- 00b46524 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b47518 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b46524 bytes e82e00f0
+ 00b47518 bytes e82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-131e35b96bd40d45f77113afe4bb696f"></a>

### [`00b4653c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b4653c.md) → [`00b47530`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47530.md) _ZN8firebase4util10uribuilder13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b47570",
      "incomplete_value": true,
      "site": "00b47570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7b8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4657c",
      "incomplete_value": true,
      "site": "00b4657c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:7f8:8"
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
      "definition_site": "00b4754c",
      "incomplete_value": true,
      "site": "00b4754c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46558",
      "incomplete_value": true,
      "site": "00b46558",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47554",
      "incomplete_value": false,
      "site": "00b47568",
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
            "const:388:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46560",
      "incomplete_value": false,
      "site": "00b46574",
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
            "const:2b1:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47544",
      "READ",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47554",
      "PARAM",
      [
        "storage",
        "002af2b1",
        null,
        "string"
      ]
    ],
    [
      "00b47570",
      "WRITE",
      [
        "storage",
        "011257f8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47544",
      "READ",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47554",
      "PARAM",
      [
        "storage",
        "002af388",
        null,
        "string"
      ]
    ],
    [
      "00b47570",
      "WRITE",
      [
        "storage",
        "011267b8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b4653c.md#insn-00b46574) · [`00b4657c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b4653c.md#insn-00b4657c) · [`00b46548`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b4653c.md#insn-00b46548)
- 新版 [`00b47568`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47530.md#insn-00b47568) · [`00b47570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47530.md#insn-00b47570) · [`00b4753c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47530.md#insn-00b4753c)

~~~diff
- 00b46574 ["INT_ADD", "register:40f0:8", ["const:b46574:8", "const:4:8"]]
- 00b46574 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47568 ["INT_ADD", "register:40f0:8", ["const:b47568:8", "const:4:8"]]
+ 00b47568 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b46574 bytes 9b520494
+ 00b47568 bytes 92520494
- 00b4657c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7f8:8"]]
- 00b4657c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47570 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7b8:8"]]
+ 00b47570 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4657c bytes 80fe03f9
+ 00b47570 bytes 80de03f9
- 00b46548 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4753c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b46548 bytes f42e00f0
+ 00b4753c bytes f42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-003526fbced42b6777d0c4c24d68b664"></a>

### [`00b465ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b465ac.md) → [`00b475a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b475a0.md) _ZN8firebase4util10uribuilder10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b475bc",
      "incomplete_value": false,
      "site": "00b475c0",
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
      "definition_site": "00b465c8",
      "incomplete_value": false,
      "site": "00b465cc",
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
      "definition_site": "00b475cc",
      "incomplete_value": true,
      "site": "00b475d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b465d8",
      "incomplete_value": true,
      "site": "00b465e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b475bc",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b475cc",
      "DATA",
      [
        "storage",
        "01125820",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b475bc",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b475cc",
      "DATA",
      [
        "storage",
        "011267e0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b465cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b465ac.md#insn-00b465cc) · [`00b465c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b465ac.md#insn-00b465c8) · [`00b465d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b465ac.md#insn-00b465d0)
- 新版 [`00b475c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b475a0.md#insn-00b475c0) · [`00b475bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b475a0.md#insn-00b475bc) · [`00b475c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b475a0.md#insn-00b475c4)

~~~diff
- 00b465cc ["INT_ADD", "register:40f0:8", ["const:b465cc:8", "const:4:8"]]
- 00b465cc ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b475c0 ["INT_ADD", "register:40f0:8", ["const:b475c0:8", "const:4:8"]]
+ 00b475c0 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b465cc bytes c1520494
+ 00b475c0 bytes b8520494
- 00b465c8 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b465c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b465c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b465c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b475bc ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b475bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b475bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b475bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b465c8 bytes 00341591
+ 00b475bc bytes 00681891
- 00b465d0 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b475c4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b465d0 bytes e82e00f0
+ 00b475c4 bytes e82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d5414da3638947e8c575066edf2c098"></a>

### [`00b465e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b465e8.md) → [`00b475dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b475dc.md) _ZN8firebase4util3url19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
      "definition_site": "00b47608",
      "incomplete_value": true,
      "site": "00b47608",
      "value": [
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
    "old": {
      "definition_site": "00b46614",
      "incomplete_value": true,
      "site": "00b46614",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b475f0",
      "incomplete_value": true,
      "site": "00b475f0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b465fc",
      "incomplete_value": true,
      "site": "00b465fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b475fc",
      "incomplete_value": false,
      "site": "00b47600",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:1ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46608",
      "incomplete_value": false,
      "site": "00b4660c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:cd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b475ec",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b475fc",
      "PARAM",
      [
        "storage",
        "002bd0cd",
        null,
        "string"
      ]
    ],
    [
      "00b47608",
      "WRITE",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b475ec",
      "READ",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b475fc",
      "PARAM",
      [
        "storage",
        "002bd1ab",
        null,
        "string"
      ]
    ],
    [
      "00b47608",
      "WRITE",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4660c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b465e8.md#insn-00b4660c) · [`00b46614`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b465e8.md#insn-00b46614) · [`00b465f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b465e8.md#insn-00b465f4)
- 新版 [`00b47600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b475dc.md#insn-00b47600) · [`00b47608`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b475dc.md#insn-00b47608) · [`00b475e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b475dc.md#insn-00b475e8)

~~~diff
- 00b4660c ["INT_ADD", "register:40f0:8", ["const:b4660c:8", "const:4:8"]]
- 00b4660c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47600 ["INT_ADD", "register:40f0:8", ["const:b47600:8", "const:4:8"]]
+ 00b47600 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4660c bytes 75520494
+ 00b47600 bytes 6c520494
- 00b46614 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00b46614 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47608 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
+ 00b47608 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46614 bytes 601604f9
+ 00b47608 bytes 60f603f9
- 00b465f4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b475e8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b465f4 bytes f32e00f0
+ 00b475e8 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dc633eaee70df8f4cc01702e51c9ff9"></a>

### [`00b46628`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46628.md) → [`00b4761c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4761c.md) _ZN8firebase4util3url19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b47648",
      "incomplete_value": true,
      "site": "00b47648",
      "value": [
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
    "old": {
      "definition_site": "00b46654",
      "incomplete_value": true,
      "site": "00b46654",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47630",
      "incomplete_value": true,
      "site": "00b47630",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4663c",
      "incomplete_value": true,
      "site": "00b4663c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47638",
      "incomplete_value": false,
      "site": "00b47640",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:1ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46644",
      "incomplete_value": false,
      "site": "00b4664c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:cd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4762c",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47638",
      "PARAM",
      [
        "storage",
        "002bd0cd",
        null,
        "string"
      ]
    ],
    [
      "00b47648",
      "WRITE",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4762c",
      "READ",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47638",
      "PARAM",
      [
        "storage",
        "002bd1ab",
        null,
        "string"
      ]
    ],
    [
      "00b47648",
      "WRITE",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4664c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46628.md#insn-00b4664c) · [`00b46654`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46628.md#insn-00b46654) · [`00b46634`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46628.md#insn-00b46634)
- 新版 [`00b47640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4761c.md#insn-00b47640) · [`00b47648`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4761c.md#insn-00b47648) · [`00b47628`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4761c.md#insn-00b47628)

~~~diff
- 00b4664c ["INT_ADD", "register:40f0:8", ["const:b4664c:8", "const:4:8"]]
- 00b4664c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47640 ["INT_ADD", "register:40f0:8", ["const:b47640:8", "const:4:8"]]
+ 00b47640 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4664c bytes 65520494
+ 00b47640 bytes 5c520494
- 00b46654 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00b46654 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47648 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
+ 00b47648 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46654 bytes 601604f9
+ 00b47648 bytes 60f603f9
- 00b46634 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47628 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b46634 bytes f32e00f0
+ 00b47628 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b023923a874f1848f649d49027f5f128"></a>

### [`00b46668`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46668.md) → [`00b4765c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4765c.md) _ZN8firebase4util3url10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4768c",
      "incomplete_value": true,
      "site": "00b4768c",
      "value": [
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
    "old": {
      "definition_site": "00b46698",
      "incomplete_value": true,
      "site": "00b46698",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47670",
      "incomplete_value": true,
      "site": "00b47670",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4667c",
      "incomplete_value": true,
      "site": "00b4667c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4767c",
      "incomplete_value": false,
      "site": "00b47684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:1ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46688",
      "incomplete_value": false,
      "site": "00b46690",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:cd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4766c",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4767c",
      "PARAM",
      [
        "storage",
        "002bd0cd",
        null,
        "string"
      ]
    ],
    [
      "00b4768c",
      "WRITE",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4766c",
      "READ",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4767c",
      "PARAM",
      [
        "storage",
        "002bd1ab",
        null,
        "string"
      ]
    ],
    [
      "00b4768c",
      "WRITE",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46690`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46668.md#insn-00b46690) · [`00b46698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46668.md#insn-00b46698) · [`00b46674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46668.md#insn-00b46674)
- 新版 [`00b47684`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4765c.md#insn-00b47684) · [`00b4768c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4765c.md#insn-00b4768c) · [`00b47668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4765c.md#insn-00b47668)

~~~diff
- 00b46690 ["INT_ADD", "register:40f0:8", ["const:b46690:8", "const:4:8"]]
- 00b46690 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47684 ["INT_ADD", "register:40f0:8", ["const:b47684:8", "const:4:8"]]
+ 00b47684 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b46690 bytes 54520494
+ 00b47684 bytes 4b520494
- 00b46698 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00b46698 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4768c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
+ 00b4768c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46698 bytes 601604f9
+ 00b4768c bytes 60f603f9
- 00b46674 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47668 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b46674 bytes f32e00f0
+ 00b47668 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37ee806525c77baf55a85bac365cffde"></a>

### [`00b466ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b466ac.md) → [`00b476a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b476a0.md) _ZN8firebase4util3url10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b476d0",
      "incomplete_value": true,
      "site": "00b476d0",
      "value": [
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
    "old": {
      "definition_site": "00b466dc",
      "incomplete_value": true,
      "site": "00b466dc",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b476b4",
      "incomplete_value": true,
      "site": "00b476b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b466c0",
      "incomplete_value": true,
      "site": "00b466c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b476bc",
      "incomplete_value": false,
      "site": "00b476c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:1ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b466c8",
      "incomplete_value": false,
      "site": "00b466d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:cd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b476b0",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b476bc",
      "PARAM",
      [
        "storage",
        "002bd0cd",
        null,
        "string"
      ]
    ],
    [
      "00b476d0",
      "WRITE",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b476b0",
      "READ",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b476bc",
      "PARAM",
      [
        "storage",
        "002bd1ab",
        null,
        "string"
      ]
    ],
    [
      "00b476d0",
      "WRITE",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b466d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b466ac.md#insn-00b466d4) · [`00b466dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b466ac.md#insn-00b466dc) · [`00b466b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b466ac.md#insn-00b466b8)
- 新版 [`00b476c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b476a0.md#insn-00b476c8) · [`00b476d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b476a0.md#insn-00b476d0) · [`00b476ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b476a0.md#insn-00b476ac)

~~~diff
- 00b466d4 ["INT_ADD", "register:40f0:8", ["const:b466d4:8", "const:4:8"]]
- 00b466d4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b476c8 ["INT_ADD", "register:40f0:8", ["const:b476c8:8", "const:4:8"]]
+ 00b476c8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b466d4 bytes 43520494
+ 00b476c8 bytes 3a520494
- 00b466dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:828:8"]]
- 00b466dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b476d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:7e8:8"]]
+ 00b476d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b466dc bytes 601604f9
+ 00b476d0 bytes 60f603f9
- 00b466b8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b476ac ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b466b8 bytes f32e00f0
+ 00b476ac bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-351a5c22792223ed474cbb1fce2aef67"></a>

### [`00b466fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b466fc.md) → [`00b476f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b476f0.md) _ZN8firebase4util3url15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b47778",
      "incomplete_value": true,
      "site": "00b47778",
      "value": [
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
    "old": {
      "definition_site": "00b46784",
      "incomplete_value": true,
      "site": "00b46784",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47724",
      "incomplete_value": true,
      "site": "00b47730",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:7e8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46730",
      "incomplete_value": true,
      "site": "00b4673c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:828:8"
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
      "00b47704",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47724",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47778",
      "WRITE",
      [
        "storage",
        "01125830",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47704",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47724",
      "READ",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47778",
      "WRITE",
      [
        "storage",
        "011267f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4673c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b466fc.md#insn-00b4673c) · [`00b46784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b466fc.md#insn-00b46784) · [`00b4670c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b466fc.md#insn-00b4670c)
- 新版 [`00b47730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b476f0.md#insn-00b47730) · [`00b47778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b476f0.md#insn-00b47778) · [`00b47700`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b476f0.md#insn-00b47700)

~~~diff
- 00b4673c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4673c ["INT_ADD", "register:40f0:8", ["const:b4673c:8", "const:4:8"]]
- 00b4673c ["CALLIND", null, ["register:0:8"]]
+ 00b47730 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47730 ["INT_ADD", "register:40f0:8", ["const:b47730:8", "const:4:8"]]
+ 00b47730 ["CALLIND", null, ["register:0:8"]]
- 00b4673c bytes 00013fd6
+ 00b47730 bytes 00013fd6
- 00b46784 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b46784 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:830:8"]]
- 00b46784 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b47778 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b47778 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:7f0:8"]]
+ 00b47778 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b46784 bytes a0c22039
+ 00b47778 bytes a0c21f39
- 00b4670c ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b47700 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4670c bytes f52e00f0
+ 00b47700 bytes f52e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef8940a8172fdcc9952d1a65ca8610e0"></a>

### [`00b46798`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46798.md) → [`00b4778c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4778c.md) _ZN8firebase4util3url12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b477c8",
      "incomplete_value": true,
      "site": "00b477c8",
      "value": [
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
    "old": {
      "definition_site": "00b467d4",
      "incomplete_value": true,
      "site": "00b467d4",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47818",
      "incomplete_value": true,
      "site": "00b47818",
      "value": [
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
    "old": {
      "definition_site": "00b46824",
      "incomplete_value": true,
      "site": "00b46824",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b477a4",
      "incomplete_value": true,
      "site": "00b477a4",
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
      "definition_site": "00b467b0",
      "incomplete_value": true,
      "site": "00b467b0",
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
      "00b477a0",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b477ac",
      "READ",
      [
        "storage",
        "01125830",
        null,
        "undefined1"
      ]
    ],
    [
      "00b477c8",
      "WRITE",
      [
        "storage",
        "01125830",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b477a0",
      "READ",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b477ac",
      "READ",
      [
        "storage",
        "011267f0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b477c8",
      "WRITE",
      [
        "storage",
        "011267f0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b467d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46798.md#insn-00b467d4) · [`00b46820`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46798.md#insn-00b46820) · [`00b46824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46798.md#insn-00b46824)
- 新版 [`00b477c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4778c.md#insn-00b477c8) · [`00b47814`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4778c.md#insn-00b47814) · [`00b47818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4778c.md#insn-00b47818)

~~~diff
- 00b467d4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b467d4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b467d4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:830:8"]]
- 00b467d4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b477c8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b477c8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b477c8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:7f0:8"]]
+ 00b477c8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b467d4 bytes bfc22039
+ 00b477c8 bytes bfc21f39
- 00b46820 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46820 ["INT_ADD", "register:40f0:8", ["const:b46820:8", "const:4:8"]]
- 00b46820 ["CALLIND", null, ["register:0:8"]]
+ 00b47814 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47814 ["INT_ADD", "register:40f0:8", ["const:b47814:8", "const:4:8"]]
+ 00b47814 ["CALLIND", null, ["register:0:8"]]
- 00b46820 bytes 00013fd6
+ 00b47814 bytes 00013fd6
- 00b46824 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
- 00b46824 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b46824 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b47818 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e8:8"]]
+ 00b47818 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b47818 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b46824 bytes 9f1604f9
+ 00b47818 bytes 9ff603f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3b912fcfccd5350e6533c70ca7d6505b"></a>

### [`00b46838`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46838.md) → [`00b4782c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4782c.md) _ZN8firebase4util3url14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4786c",
      "incomplete_value": true,
      "site": "00b4786c",
      "value": [
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
    "old": {
      "definition_site": "00b46878",
      "incomplete_value": true,
      "site": "00b46878",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47848",
      "incomplete_value": true,
      "site": "00b47848",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46854",
      "incomplete_value": true,
      "site": "00b46854",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47850",
      "incomplete_value": false,
      "site": "00b47864",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:1ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4685c",
      "incomplete_value": false,
      "site": "00b46870",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:cd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47840",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47850",
      "PARAM",
      [
        "storage",
        "002bd0cd",
        null,
        "string"
      ]
    ],
    [
      "00b4786c",
      "WRITE",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47840",
      "READ",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47850",
      "PARAM",
      [
        "storage",
        "002bd1ab",
        null,
        "string"
      ]
    ],
    [
      "00b4786c",
      "WRITE",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46838.md#insn-00b46870) · [`00b46878`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46838.md#insn-00b46878) · [`00b46844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46838.md#insn-00b46844)
- 新版 [`00b47864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4782c.md#insn-00b47864) · [`00b4786c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4782c.md#insn-00b4786c) · [`00b47838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4782c.md#insn-00b47838)

~~~diff
- 00b46870 ["INT_ADD", "register:40f0:8", ["const:b46870:8", "const:4:8"]]
- 00b46870 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47864 ["INT_ADD", "register:40f0:8", ["const:b47864:8", "const:4:8"]]
+ 00b47864 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b46870 bytes dc510494
+ 00b47864 bytes d3510494
- 00b46878 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
- 00b46878 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4786c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e8:8"]]
+ 00b4786c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46878 bytes 801604f9
+ 00b4786c bytes 80f603f9
- 00b46844 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b47838 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b46844 bytes f42e00f0
+ 00b47838 bytes f42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-161ee92cf5bc5fb4b0d193c364a088ad"></a>

### [`00b468a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b468a8.md) → [`00b4789c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4789c.md) _ZN8firebase4util3url11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b478b8",
      "incomplete_value": false,
      "site": "00b478bc",
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
      "definition_site": "00b468c4",
      "incomplete_value": false,
      "site": "00b468c8",
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
      "definition_site": "00b478c8",
      "incomplete_value": true,
      "site": "00b478d4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b468d4",
      "incomplete_value": true,
      "site": "00b468e0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b478b8",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b478c8",
      "DATA",
      [
        "storage",
        "01125838",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b478b8",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b478c8",
      "DATA",
      [
        "storage",
        "011267f8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b468c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b468a8.md#insn-00b468c8) · [`00b468c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b468a8.md#insn-00b468c4) · [`00b468cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b468a8.md#insn-00b468cc)
- 新版 [`00b478bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4789c.md#insn-00b478bc) · [`00b478b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4789c.md#insn-00b478b8) · [`00b478c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b4789c.md#insn-00b478c0)

~~~diff
- 00b468c8 ["INT_ADD", "register:40f0:8", ["const:b468c8:8", "const:4:8"]]
- 00b468c8 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b478bc ["INT_ADD", "register:40f0:8", ["const:b478bc:8", "const:4:8"]]
+ 00b478bc ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b468c8 bytes 02520494
+ 00b478bc bytes f9510494
- 00b468c4 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b468c4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b468c4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b468c4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b478b8 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b478b8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b478b8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b478b8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b468c4 bytes 002c0c91
+ 00b478b8 bytes 008c1191
- 00b468cc ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b478c0 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b468cc bytes e82e00f0
+ 00b478c0 bytes e82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-85a2e15154dcd4c051b213e8a1a444e9"></a>

### [`00b468e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b468e4.md) → [`00b478d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b478d8.md) _ZN8firebase4util3url13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b47918",
      "incomplete_value": true,
      "site": "00b47918",
      "value": [
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
    "old": {
      "definition_site": "00b46924",
      "incomplete_value": true,
      "site": "00b46924",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b478f4",
      "incomplete_value": true,
      "site": "00b478f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46900",
      "incomplete_value": true,
      "site": "00b46900",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b478fc",
      "incomplete_value": false,
      "site": "00b47910",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:1ab:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46908",
      "incomplete_value": false,
      "site": "00b4691c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bd000:8"
          ],
          [
            "leaf",
            "const:cd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b478ec",
      "READ",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ],
    [
      "00b478fc",
      "PARAM",
      [
        "storage",
        "002bd0cd",
        null,
        "string"
      ]
    ],
    [
      "00b47918",
      "WRITE",
      [
        "storage",
        "01125828",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b478ec",
      "READ",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b478fc",
      "PARAM",
      [
        "storage",
        "002bd1ab",
        null,
        "string"
      ]
    ],
    [
      "00b47918",
      "WRITE",
      [
        "storage",
        "011267e8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4691c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b468e4.md#insn-00b4691c) · [`00b46924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b468e4.md#insn-00b46924) · [`00b468f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b468e4.md#insn-00b468f0)
- 新版 [`00b47910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b478d8.md#insn-00b47910) · [`00b47918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b478d8.md#insn-00b47918) · [`00b478e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b478d8.md#insn-00b478e4)

~~~diff
- 00b4691c ["INT_ADD", "register:40f0:8", ["const:b4691c:8", "const:4:8"]]
- 00b4691c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47910 ["INT_ADD", "register:40f0:8", ["const:b47910:8", "const:4:8"]]
+ 00b47910 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4691c bytes b1510494
+ 00b47910 bytes a8510494
- 00b46924 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:828:8"]]
- 00b46924 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47918 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:7e8:8"]]
+ 00b47918 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46924 bytes 801604f9
+ 00b47918 bytes 80f603f9
- 00b468f0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b478e4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b468f0 bytes f42e00f0
+ 00b478e4 bytes f42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-db25ceca94769a6df1681da9ae611bc7"></a>

### [`00b46954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46954.md) → [`00b47948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47948.md) _ZN8firebase4util3url10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b47964",
      "incomplete_value": false,
      "site": "00b47968",
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
      "definition_site": "00b46970",
      "incomplete_value": false,
      "site": "00b46974",
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
      "definition_site": "00b47974",
      "incomplete_value": true,
      "site": "00b47980",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b46980",
      "incomplete_value": true,
      "site": "00b4698c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b47964",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b47974",
      "DATA",
      [
        "storage",
        "01125848",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b47964",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b47974",
      "DATA",
      [
        "storage",
        "01126808",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46974`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46954.md#insn-00b46974) · [`00b46970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46954.md#insn-00b46970) · [`00b46978`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46954.md#insn-00b46978)
- 新版 [`00b47968`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47948.md#insn-00b47968) · [`00b47964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47948.md#insn-00b47964) · [`00b4796c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47948.md#insn-00b4796c)

~~~diff
- 00b46974 ["INT_ADD", "register:40f0:8", ["const:b46974:8", "const:4:8"]]
- 00b46974 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b47968 ["INT_ADD", "register:40f0:8", ["const:b47968:8", "const:4:8"]]
+ 00b47968 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b46974 bytes d7510494
+ 00b47968 bytes ce510494
- 00b46970 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b46970 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b46970 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b46970 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47964 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b47964 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47964 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47964 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b46970 bytes 00341591
+ 00b47964 bytes 00681891
- 00b46978 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4796c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b46978 bytes e82e00f0
+ 00b4796c bytes e82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea891fab6195ede06eff45a3105a97fd"></a>

### [`00b46990`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46990.md) → [`00b47984`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47984.md) _ZN8firebase4util18file_output_stream19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "definition_site": "00b479b0",
      "incomplete_value": true,
      "site": "00b479b0",
      "value": [
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
    "old": {
      "definition_site": "00b469bc",
      "incomplete_value": true,
      "site": "00b469bc",
      "value": [
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
      "definition_site": "00b47998",
      "incomplete_value": true,
      "site": "00b47998",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b469a4",
      "incomplete_value": true,
      "site": "00b469a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b479a4",
      "incomplete_value": false,
      "site": "00b479a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:5af:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b469b0",
      "incomplete_value": false,
      "site": "00b469b4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47994",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b479a4",
      "PARAM",
      [
        "storage",
        "002b04d8",
        null,
        "string"
      ]
    ],
    [
      "00b479b0",
      "WRITE",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47994",
      "READ",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b479a4",
      "PARAM",
      [
        "storage",
        "002b05af",
        null,
        "string"
      ]
    ],
    [
      "00b479b0",
      "WRITE",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b469b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46990.md#insn-00b469b4) · [`00b469bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46990.md#insn-00b469bc) · [`00b4699c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46990.md#insn-00b4699c)
- 新版 [`00b479a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47984.md#insn-00b479a8) · [`00b479b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47984.md#insn-00b479b0) · [`00b47990`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47984.md#insn-00b47990)

~~~diff
- 00b469b4 ["INT_ADD", "register:40f0:8", ["const:b469b4:8", "const:4:8"]]
- 00b469b4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b479a8 ["INT_ADD", "register:40f0:8", ["const:b479a8:8", "const:4:8"]]
+ 00b479a8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b469b4 bytes 8b510494
+ 00b479a8 bytes 82510494
- 00b469bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00b469bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b479b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00b479b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b469bc bytes 602a04f9
+ 00b479b0 bytes 600a04f9
- 00b4699c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47990 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4699c bytes f32e00f0
+ 00b47990 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0d4d842d6e88c562790073bd7d688f9f"></a>

### [`00b469d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b469d0.md) → [`00b479c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b479c4.md) _ZN8firebase4util18file_output_stream19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorI

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
      "definition_site": "00b479f0",
      "incomplete_value": true,
      "site": "00b479f0",
      "value": [
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
    "old": {
      "definition_site": "00b469fc",
      "incomplete_value": true,
      "site": "00b469fc",
      "value": [
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
      "definition_site": "00b479d8",
      "incomplete_value": true,
      "site": "00b479d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b469e4",
      "incomplete_value": true,
      "site": "00b469e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b479e0",
      "incomplete_value": false,
      "site": "00b479e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:5af:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b469ec",
      "incomplete_value": false,
      "site": "00b469f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b479d4",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b479e0",
      "PARAM",
      [
        "storage",
        "002b04d8",
        null,
        "string"
      ]
    ],
    [
      "00b479f0",
      "WRITE",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b479d4",
      "READ",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b479e0",
      "PARAM",
      [
        "storage",
        "002b05af",
        null,
        "string"
      ]
    ],
    [
      "00b479f0",
      "WRITE",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b469f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b469d0.md#insn-00b469f4) · [`00b469fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b469d0.md#insn-00b469fc) · [`00b469dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b469d0.md#insn-00b469dc)
- 新版 [`00b479e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b479c4.md#insn-00b479e8) · [`00b479f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b479c4.md#insn-00b479f0) · [`00b479d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b479c4.md#insn-00b479d0)

~~~diff
- 00b469f4 ["INT_ADD", "register:40f0:8", ["const:b469f4:8", "const:4:8"]]
- 00b469f4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b479e8 ["INT_ADD", "register:40f0:8", ["const:b479e8:8", "const:4:8"]]
+ 00b479e8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b469f4 bytes 7b510494
+ 00b479e8 bytes 72510494
- 00b469fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00b469fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b479f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00b479f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b469fc bytes 602a04f9
+ 00b479f0 bytes 600a04f9
- 00b469dc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b479d0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b469dc bytes f32e00f0
+ 00b479d0 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea8f0928dabd56157f72035e8386ea08"></a>

### [`00b46a10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46a10.md) → [`00b47a04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47a04.md) _ZN8firebase4util18file_output_stream10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b47a34",
      "incomplete_value": true,
      "site": "00b47a34",
      "value": [
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
    "old": {
      "definition_site": "00b46a40",
      "incomplete_value": true,
      "site": "00b46a40",
      "value": [
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
      "definition_site": "00b47a18",
      "incomplete_value": true,
      "site": "00b47a18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46a24",
      "incomplete_value": true,
      "site": "00b46a24",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47a24",
      "incomplete_value": false,
      "site": "00b47a2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:5af:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46a30",
      "incomplete_value": false,
      "site": "00b46a38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47a14",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47a24",
      "PARAM",
      [
        "storage",
        "002b04d8",
        null,
        "string"
      ]
    ],
    [
      "00b47a34",
      "WRITE",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47a14",
      "READ",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47a24",
      "PARAM",
      [
        "storage",
        "002b05af",
        null,
        "string"
      ]
    ],
    [
      "00b47a34",
      "WRITE",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46a38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46a10.md#insn-00b46a38) · [`00b46a40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46a10.md#insn-00b46a40) · [`00b46a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46a10.md#insn-00b46a1c)
- 新版 [`00b47a2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47a04.md#insn-00b47a2c) · [`00b47a34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47a04.md#insn-00b47a34) · [`00b47a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47a04.md#insn-00b47a10)

~~~diff
- 00b46a38 ["INT_ADD", "register:40f0:8", ["const:b46a38:8", "const:4:8"]]
- 00b46a38 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47a2c ["INT_ADD", "register:40f0:8", ["const:b47a2c:8", "const:4:8"]]
+ 00b47a2c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b46a38 bytes 6a510494
+ 00b47a2c bytes 61510494
- 00b46a40 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00b46a40 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47a34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00b47a34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46a40 bytes 602a04f9
+ 00b47a34 bytes 600a04f9
- 00b46a1c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47a10 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b46a1c bytes f32e00f0
+ 00b47a10 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eabe3ef93bcf33072aced2d83e04a4da"></a>

### [`00b46a54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46a54.md) → [`00b47a48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47a48.md) _ZN8firebase4util18file_output_stream10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b47a78",
      "incomplete_value": true,
      "site": "00b47a78",
      "value": [
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
    "old": {
      "definition_site": "00b46a84",
      "incomplete_value": true,
      "site": "00b46a84",
      "value": [
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
      "definition_site": "00b47a5c",
      "incomplete_value": true,
      "site": "00b47a5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46a68",
      "incomplete_value": true,
      "site": "00b46a68",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b46a68"
      ],
      [
        "FALL_THROUGH",
        "00b47a5c"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b47a5c",
      "incomplete_value": true,
      "site": "00b47a78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46a68",
      "incomplete_value": true,
      "site": "00b46a84",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b47a58",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47a64",
      "PARAM",
      [
        "storage",
        "002b04d8",
        null,
        "string"
      ]
    ],
    [
      "00b47a78",
      "WRITE",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47a58",
      "READ",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47a64",
      "PARAM",
      [
        "storage",
        "002b05af",
        null,
        "string"
      ]
    ],
    [
      "00b47a78",
      "WRITE",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46a84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46a54.md#insn-00b46a84) · [`00b46a60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46a54.md#insn-00b46a60) · [`00b46a64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46a54.md#insn-00b46a64)
- 新版 [`00b47a78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47a48.md#insn-00b47a78) · [`00b47a54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47a48.md#insn-00b47a54) · [`00b47a58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47a48.md#insn-00b47a58)

~~~diff
- 00b46a84 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00b46a84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47a78 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00b47a78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46a84 bytes 602a04f9
+ 00b47a78 bytes 600a04f9
- 00b46a60 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47a54 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b46a60 bytes f32e00f0
+ 00b47a54 bytes f32e00f0
- 00b46a64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:850:8"]]
- 00b46a64 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47a58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:810:8"]]
+ 00b47a58 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46a64 bytes 682a44f9
+ 00b47a58 bytes 680a44f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8b7112052458d483246ac119113d4910"></a>

### [`00b46aa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46aa4.md) → [`00b47a98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47a98.md) _ZN8firebase4util18file_output_stream15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b47b20",
      "incomplete_value": true,
      "site": "00b47b20",
      "value": [
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
    "old": {
      "definition_site": "00b46b2c",
      "incomplete_value": true,
      "site": "00b46b2c",
      "value": [
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
      "definition_site": "00b47acc",
      "incomplete_value": true,
      "site": "00b47ad8",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:810:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46ad8",
      "incomplete_value": true,
      "site": "00b46ae4",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b47aac",
      "READ",
      [
        "storage",
        "01125858",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47acc",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47b20",
      "WRITE",
      [
        "storage",
        "01125858",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47aac",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47acc",
      "READ",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47b20",
      "WRITE",
      [
        "storage",
        "01126818",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46ae4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46aa4.md#insn-00b46ae4) · [`00b46b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46aa4.md#insn-00b46b2c) · [`00b46ab4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46aa4.md#insn-00b46ab4)
- 新版 [`00b47ad8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47a98.md#insn-00b47ad8) · [`00b47b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47a98.md#insn-00b47b20) · [`00b47aa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47a98.md#insn-00b47aa8)

~~~diff
- 00b46ae4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46ae4 ["INT_ADD", "register:40f0:8", ["const:b46ae4:8", "const:4:8"]]
- 00b46ae4 ["CALLIND", null, ["register:0:8"]]
+ 00b47ad8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47ad8 ["INT_ADD", "register:40f0:8", ["const:b47ad8:8", "const:4:8"]]
+ 00b47ad8 ["CALLIND", null, ["register:0:8"]]
- 00b46ae4 bytes 00013fd6
+ 00b47ad8 bytes 00013fd6
- 00b46b2c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b46b2c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:858:8"]]
- 00b46b2c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b47b20 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b47b20 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:818:8"]]
+ 00b47b20 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b46b2c bytes a0622139
+ 00b47b20 bytes a0622039
- 00b46ab4 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b47aa8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b46ab4 bytes f52e00f0
+ 00b47aa8 bytes f52e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7df8061bb27ed82c844eebfd4cea9fc5"></a>

### [`00b46b40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46b40.md) → [`00b47b34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47b34.md) _ZN8firebase4util18file_output_stream12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

- 旧版 呼出元 0件  · 呼出先 0件 
- 新版 呼出元 0件  · 呼出先 0件 

変更の種類 branch_value, call_argument_candidate, constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `branch_value` 1件, `call_argument_candidate` 1件, `store_destination` 2件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b47b70",
      "incomplete_value": true,
      "site": "00b47b70",
      "value": [
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
    "old": {
      "definition_site": "00b46b7c",
      "incomplete_value": true,
      "site": "00b46b7c",
      "value": [
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
      "definition_site": "00b47bc0",
      "incomplete_value": true,
      "site": "00b47bc0",
      "value": [
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
    "old": {
      "definition_site": "00b46bcc",
      "incomplete_value": true,
      "site": "00b46bcc",
      "value": [
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
      "definition_site": "00b47b4c",
      "incomplete_value": true,
      "site": "00b47b4c",
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
      "definition_site": "00b46b58",
      "incomplete_value": true,
      "site": "00b46b58",
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
      "00b47b48",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47b54",
      "READ",
      [
        "storage",
        "01125858",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47b70",
      "WRITE",
      [
        "storage",
        "01125858",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47b48",
      "READ",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47b54",
      "READ",
      [
        "storage",
        "01126818",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47b70",
      "WRITE",
      [
        "storage",
        "01126818",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46b7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46b40.md#insn-00b46b7c) · [`00b46bc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46b40.md#insn-00b46bc8) · [`00b46bcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46b40.md#insn-00b46bcc)
- 新版 [`00b47b70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47b34.md#insn-00b47b70) · [`00b47bbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47b34.md#insn-00b47bbc) · [`00b47bc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47b34.md#insn-00b47bc0)

~~~diff
- 00b46b7c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b46b7c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b46b7c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:858:8"]]
- 00b46b7c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b47b70 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b47b70 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b47b70 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:818:8"]]
+ 00b47b70 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b46b7c bytes bf622139
+ 00b47b70 bytes bf622039
- 00b46bc8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46bc8 ["INT_ADD", "register:40f0:8", ["const:b46bc8:8", "const:4:8"]]
- 00b46bc8 ["CALLIND", null, ["register:0:8"]]
+ 00b47bbc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47bbc ["INT_ADD", "register:40f0:8", ["const:b47bbc:8", "const:4:8"]]
+ 00b47bbc ["CALLIND", null, ["register:0:8"]]
- 00b46bc8 bytes 00013fd6
+ 00b47bbc bytes 00013fd6
- 00b46bcc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
- 00b46bcc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b46bcc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b47bc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
+ 00b47bc0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b47bc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b46bcc bytes 9f2a04f9
+ 00b47bc0 bytes 9f0a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fcecb85a0b2dde4325e70bff1a4944ef"></a>

### [`00b46be0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46be0.md) → [`00b47bd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47bd4.md) _ZN8firebase4util18file_output_stream14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b47c14",
      "incomplete_value": true,
      "site": "00b47c14",
      "value": [
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
    "old": {
      "definition_site": "00b46c20",
      "incomplete_value": true,
      "site": "00b46c20",
      "value": [
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
      "definition_site": "00b47bf0",
      "incomplete_value": true,
      "site": "00b47bf0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46bfc",
      "incomplete_value": true,
      "site": "00b46bfc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47bf8",
      "incomplete_value": false,
      "site": "00b47c0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:5af:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46c04",
      "incomplete_value": false,
      "site": "00b46c18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47be8",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47bf8",
      "PARAM",
      [
        "storage",
        "002b04d8",
        null,
        "string"
      ]
    ],
    [
      "00b47c14",
      "WRITE",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47be8",
      "READ",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47bf8",
      "PARAM",
      [
        "storage",
        "002b05af",
        null,
        "string"
      ]
    ],
    [
      "00b47c14",
      "WRITE",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46be0.md#insn-00b46c18) · [`00b46c20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46be0.md#insn-00b46c20) · [`00b46bec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46be0.md#insn-00b46bec)
- 新版 [`00b47c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47bd4.md#insn-00b47c0c) · [`00b47c14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47bd4.md#insn-00b47c14) · [`00b47be0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47bd4.md#insn-00b47be0)

~~~diff
- 00b46c18 ["INT_ADD", "register:40f0:8", ["const:b46c18:8", "const:4:8"]]
- 00b46c18 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47c0c ["INT_ADD", "register:40f0:8", ["const:b47c0c:8", "const:4:8"]]
+ 00b47c0c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b46c18 bytes f2500494
+ 00b47c0c bytes e9500494
- 00b46c20 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
- 00b46c20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47c14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
+ 00b47c14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46c20 bytes 802a04f9
+ 00b47c14 bytes 800a04f9
- 00b46bec ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b47be0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b46bec bytes f42e00f0
+ 00b47be0 bytes f42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-379adbff437475532d6d4e34bf27320c"></a>

### [`00b46c50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46c50.md) → [`00b47c44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47c44.md) _ZN8firebase4util18file_output_stream11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b47c60",
      "incomplete_value": false,
      "site": "00b47c64",
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
      "definition_site": "00b46c6c",
      "incomplete_value": false,
      "site": "00b46c70",
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
      "definition_site": "00b47c70",
      "incomplete_value": true,
      "site": "00b47c7c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b46c7c",
      "incomplete_value": true,
      "site": "00b46c88",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b47c60",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b47c70",
      "DATA",
      [
        "storage",
        "01125860",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47c60",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b47c70",
      "DATA",
      [
        "storage",
        "01126820",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46c70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46c50.md#insn-00b46c70) · [`00b46c6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46c50.md#insn-00b46c6c) · [`00b46c74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46c50.md#insn-00b46c74)
- 新版 [`00b47c64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47c44.md#insn-00b47c64) · [`00b47c60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47c44.md#insn-00b47c60) · [`00b47c68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47c44.md#insn-00b47c68)

~~~diff
- 00b46c70 ["INT_ADD", "register:40f0:8", ["const:b46c70:8", "const:4:8"]]
- 00b46c70 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b47c64 ["INT_ADD", "register:40f0:8", ["const:b47c64:8", "const:4:8"]]
+ 00b47c64 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b46c70 bytes 18510494
+ 00b47c64 bytes 0f510494
- 00b46c6c ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b46c6c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b46c6c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b46c6c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47c60 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b47c60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47c60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47c60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b46c6c bytes 002c0c91
+ 00b47c60 bytes 008c1191
- 00b46c74 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b47c68 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b46c74 bytes e82e00f0
+ 00b47c68 bytes e82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-947674fb1f0541fdc039ba4d7967b534"></a>

### [`00b46c8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46c8c.md) → [`00b47c80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47c80.md) _ZN8firebase4util18file_output_stream13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b47cc0",
      "incomplete_value": true,
      "site": "00b47cc0",
      "value": [
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
    "old": {
      "definition_site": "00b46ccc",
      "incomplete_value": true,
      "site": "00b46ccc",
      "value": [
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
      "definition_site": "00b47c9c",
      "incomplete_value": true,
      "site": "00b47c9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46ca8",
      "incomplete_value": true,
      "site": "00b46ca8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47ca4",
      "incomplete_value": false,
      "site": "00b47cb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:5af:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46cb0",
      "incomplete_value": false,
      "site": "00b46cc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b0000:8"
          ],
          [
            "leaf",
            "const:4d8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47c94",
      "READ",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47ca4",
      "PARAM",
      [
        "storage",
        "002b04d8",
        null,
        "string"
      ]
    ],
    [
      "00b47cc0",
      "WRITE",
      [
        "storage",
        "01125850",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47c94",
      "READ",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47ca4",
      "PARAM",
      [
        "storage",
        "002b05af",
        null,
        "string"
      ]
    ],
    [
      "00b47cc0",
      "WRITE",
      [
        "storage",
        "01126810",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46c8c.md#insn-00b46cc4) · [`00b46ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46c8c.md#insn-00b46ccc) · [`00b46c98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46c8c.md#insn-00b46c98)
- 新版 [`00b47cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47c80.md#insn-00b47cb8) · [`00b47cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47c80.md#insn-00b47cc0) · [`00b47c8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47c80.md#insn-00b47c8c)

~~~diff
- 00b46cc4 ["INT_ADD", "register:40f0:8", ["const:b46cc4:8", "const:4:8"]]
- 00b46cc4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47cb8 ["INT_ADD", "register:40f0:8", ["const:b47cb8:8", "const:4:8"]]
+ 00b47cb8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b46cc4 bytes c7500494
+ 00b47cb8 bytes be500494
- 00b46ccc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:850:8"]]
- 00b46ccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47cc0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:810:8"]]
+ 00b47cc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46ccc bytes 802a04f9
+ 00b47cc0 bytes 800a04f9
- 00b46c98 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b47c8c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b46c98 bytes f42e00f0
+ 00b47c8c bytes f42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-789dabb087f2198ef5b012f03a9d422a"></a>

### [`00b46cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46cfc.md) → [`00b47cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47cf0.md) _ZN8firebase4util18file_output_stream10GetFieldIdENS1_5FieldE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b47d1c",
      "incomplete_value": true,
      "site": "00b47d28",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b46d28",
      "incomplete_value": true,
      "site": "00b46d34",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b47d0c",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b47d1c",
      "DATA",
      [
        "storage",
        "01125878",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b47d0c",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b47d1c",
      "DATA",
      [
        "storage",
        "01126838",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46d18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46cfc.md#insn-00b46d18) · [`00b46d1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46cfc.md#insn-00b46d1c) · [`00b46d20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46cfc.md#insn-00b46d20)
- 新版 [`00b47d0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47cf0.md#insn-00b47d0c) · [`00b47d10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47cf0.md#insn-00b47d10) · [`00b47d14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47cf0.md#insn-00b47d14)

~~~diff
- 00b46d18 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b46d18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b46d18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b46d18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b47d0c ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b47d0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47d0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b47d0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b46d18 bytes 00341591
+ 00b47d0c bytes 00681891
- 00b46d1c ["INT_ADD", "register:40f0:8", ["const:b46d1c:8", "const:4:8"]]
- 00b46d1c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b47d10 ["INT_ADD", "register:40f0:8", ["const:b47d10:8", "const:4:8"]]
+ 00b47d10 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b46d1c bytes ed500494
+ 00b47d10 bytes e4500494
- 00b46d20 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b47d14 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b46d20 bytes e82e00f0
+ 00b47d14 bytes e82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8014f82813a77951e629a9faebb87c68"></a>

### [`00b46d38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46d38.md) → [`00b47d2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47d2c.md) _ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

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
      "definition_site": "00b47d58",
      "incomplete_value": true,
      "site": "00b47d58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46d64",
      "incomplete_value": true,
      "site": "00b46d64",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47d40",
      "incomplete_value": true,
      "site": "00b47d40",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46d4c",
      "incomplete_value": true,
      "site": "00b46d4c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47d4c",
      "incomplete_value": false,
      "site": "00b47d50",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:ad1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46d58",
      "incomplete_value": false,
      "site": "00b46d5c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:a02:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47d3c",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47d4c",
      "PARAM",
      [
        "storage",
        "002b8a02",
        null,
        "string"
      ]
    ],
    [
      "00b47d58",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47d3c",
      "READ",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47d4c",
      "PARAM",
      [
        "storage",
        "002b8ad1",
        null,
        "string"
      ]
    ],
    [
      "00b47d58",
      "WRITE",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46d5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46d38.md#insn-00b46d5c) · [`00b46d64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46d38.md#insn-00b46d64) · [`00b46d44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46d38.md#insn-00b46d44)
- 新版 [`00b47d50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47d2c.md#insn-00b47d50) · [`00b47d58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47d2c.md#insn-00b47d58) · [`00b47d38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47d2c.md#insn-00b47d38)

~~~diff
- 00b46d5c ["INT_ADD", "register:40f0:8", ["const:b46d5c:8", "const:4:8"]]
- 00b46d5c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47d50 ["INT_ADD", "register:40f0:8", ["const:b47d50:8", "const:4:8"]]
+ 00b47d50 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b46d5c bytes a1500494
+ 00b47d50 bytes 98500494
- 00b46d64 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b46d64 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47d58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:840:8"]]
+ 00b47d58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46d64 bytes 604204f9
+ 00b47d58 bytes 602204f9
- 00b46d44 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47d38 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b46d44 bytes f32e00f0
+ 00b47d38 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0e4b7d4f2cfc9972f3f0210127882ce9"></a>

### [`00b46d78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46d78.md) → [`00b47d6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47d6c.md) _ZN8firebase4util16dex_class_loader19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9

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
      "definition_site": "00b47d98",
      "incomplete_value": true,
      "site": "00b47d98",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46da4",
      "incomplete_value": true,
      "site": "00b46da4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47d80",
      "incomplete_value": true,
      "site": "00b47d80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46d8c",
      "incomplete_value": true,
      "site": "00b46d8c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47d88",
      "incomplete_value": false,
      "site": "00b47d90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:ad1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46d94",
      "incomplete_value": false,
      "site": "00b46d9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:a02:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47d7c",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47d88",
      "PARAM",
      [
        "storage",
        "002b8a02",
        null,
        "string"
      ]
    ],
    [
      "00b47d98",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47d7c",
      "READ",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47d88",
      "PARAM",
      [
        "storage",
        "002b8ad1",
        null,
        "string"
      ]
    ],
    [
      "00b47d98",
      "WRITE",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46d9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46d78.md#insn-00b46d9c) · [`00b46da4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46d78.md#insn-00b46da4) · [`00b46d84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46d78.md#insn-00b46d84)
- 新版 [`00b47d90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47d6c.md#insn-00b47d90) · [`00b47d98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47d6c.md#insn-00b47d98) · [`00b47d78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47d6c.md#insn-00b47d78)

~~~diff
- 00b46d9c ["INT_ADD", "register:40f0:8", ["const:b46d9c:8", "const:4:8"]]
- 00b46d9c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47d90 ["INT_ADD", "register:40f0:8", ["const:b47d90:8", "const:4:8"]]
+ 00b47d90 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b46d9c bytes 91500494
+ 00b47d90 bytes 88500494
- 00b46da4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b46da4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47d98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:840:8"]]
+ 00b47d98 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46da4 bytes 604204f9
+ 00b47d98 bytes 602204f9
- 00b46d84 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47d78 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b46d84 bytes f32e00f0
+ 00b47d78 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-225f7140ff3cc06d6bac34a1ba05fd5f"></a>

### [`00b46db8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46db8.md) → [`00b47dac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47dac.md) _ZN8firebase4util16dex_class_loader10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b47ddc",
      "incomplete_value": true,
      "site": "00b47ddc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46de8",
      "incomplete_value": true,
      "site": "00b46de8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47dc0",
      "incomplete_value": true,
      "site": "00b47dc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46dcc",
      "incomplete_value": true,
      "site": "00b46dcc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47dcc",
      "incomplete_value": false,
      "site": "00b47dd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:ad1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46dd8",
      "incomplete_value": false,
      "site": "00b46de0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:a02:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47dbc",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47dcc",
      "PARAM",
      [
        "storage",
        "002b8a02",
        null,
        "string"
      ]
    ],
    [
      "00b47ddc",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47dbc",
      "READ",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47dcc",
      "PARAM",
      [
        "storage",
        "002b8ad1",
        null,
        "string"
      ]
    ],
    [
      "00b47ddc",
      "WRITE",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46de0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46db8.md#insn-00b46de0) · [`00b46de8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46db8.md#insn-00b46de8) · [`00b46dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46db8.md#insn-00b46dc4)
- 新版 [`00b47dd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47dac.md#insn-00b47dd4) · [`00b47ddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47dac.md#insn-00b47ddc) · [`00b47db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47dac.md#insn-00b47db8)

~~~diff
- 00b46de0 ["INT_ADD", "register:40f0:8", ["const:b46de0:8", "const:4:8"]]
- 00b46de0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47dd4 ["INT_ADD", "register:40f0:8", ["const:b47dd4:8", "const:4:8"]]
+ 00b47dd4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b46de0 bytes 80500494
+ 00b47dd4 bytes 77500494
- 00b46de8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b46de8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47ddc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:840:8"]]
+ 00b47ddc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46de8 bytes 604204f9
+ 00b47ddc bytes 602204f9
- 00b46dc4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47db8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b46dc4 bytes f32e00f0
+ 00b47db8 bytes f32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f736277fac03234d56e795ff0c0e5a85"></a>

### [`00b46dfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46dfc.md) → [`00b47df0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47df0.md) _ZN8firebase4util16dex_class_loader10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b47e20",
      "incomplete_value": true,
      "site": "00b47e20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46e2c",
      "incomplete_value": true,
      "site": "00b46e2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:880:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b47e04",
      "incomplete_value": true,
      "site": "00b47e04",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46e10",
      "incomplete_value": true,
      "site": "00b46e10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b46e10"
      ],
      [
        "FALL_THROUGH",
        "00b47e04"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b47e04",
      "incomplete_value": true,
      "site": "00b47e20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46e10",
      "incomplete_value": true,
      "site": "00b46e2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b47e00",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47e0c",
      "PARAM",
      [
        "storage",
        "002b8a02",
        null,
        "string"
      ]
    ],
    [
      "00b47e20",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47e00",
      "READ",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47e0c",
      "PARAM",
      [
        "storage",
        "002b8ad1",
        null,
        "string"
      ]
    ],
    [
      "00b47e20",
      "WRITE",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46e2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46dfc.md#insn-00b46e2c) · [`00b46e08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46dfc.md#insn-00b46e08) · [`00b46e0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46dfc.md#insn-00b46e0c)
- 新版 [`00b47e20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47df0.md#insn-00b47e20) · [`00b47dfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47df0.md#insn-00b47dfc) · [`00b47e00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47df0.md#insn-00b47e00)

~~~diff
- 00b46e2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b46e2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47e20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:840:8"]]
+ 00b47e20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46e2c bytes 604204f9
+ 00b47e20 bytes 602204f9
- 00b46e08 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b47dfc ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b46e08 bytes f32e00f0
+ 00b47dfc bytes f32e00f0
- 00b46e0c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:880:8"]]
- 00b46e0c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b47e00 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:840:8"]]
+ 00b47e00 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b46e0c bytes 684244f9
+ 00b47e00 bytes 682244f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-70a9beeaa1846f28eece2e05124b27d0"></a>

### [`00b46e4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46e4c.md) → [`00b47e40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47e40.md) _ZN8firebase4util16dex_class_loader15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b47ec8",
      "incomplete_value": true,
      "site": "00b47ec8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46ed4",
      "incomplete_value": true,
      "site": "00b46ed4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:888:8"
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
      "definition_site": "00b47e74",
      "incomplete_value": true,
      "site": "00b47e80",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:840:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46e80",
      "incomplete_value": true,
      "site": "00b46e8c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:880:8"
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
      "00b47e54",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47e74",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47ec8",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47e54",
      "READ",
      [
        "storage",
        "01126848",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47e74",
      "READ",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47ec8",
      "WRITE",
      [
        "storage",
        "01126848",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46e8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46e4c.md#insn-00b46e8c) · [`00b46ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46e4c.md#insn-00b46ed4) · [`00b46e5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46e4c.md#insn-00b46e5c)
- 新版 [`00b47e80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47e40.md#insn-00b47e80) · [`00b47ec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47e40.md#insn-00b47ec8) · [`00b47e50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47e40.md#insn-00b47e50)

~~~diff
- 00b46e8c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46e8c ["INT_ADD", "register:40f0:8", ["const:b46e8c:8", "const:4:8"]]
- 00b46e8c ["CALLIND", null, ["register:0:8"]]
+ 00b47e80 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47e80 ["INT_ADD", "register:40f0:8", ["const:b47e80:8", "const:4:8"]]
+ 00b47e80 ["CALLIND", null, ["register:0:8"]]
- 00b46e8c bytes 00013fd6
+ 00b47e80 bytes 00013fd6
- 00b46ed4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b46ed4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:888:8"]]
- 00b46ed4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b47ec8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b47ec8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:848:8"]]
+ 00b47ec8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b46ed4 bytes a0222239
+ 00b47ec8 bytes a0222139
- 00b46e5c ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b47e50 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b46e5c bytes f52e00f0
+ 00b47e50 bytes f52e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0833763cdf280228bb409407f6237d95"></a>

### [`00b46ee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46ee8.md) → [`00b47edc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47edc.md) _ZN8firebase4util16dex_class_loader12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b47f18",
      "incomplete_value": true,
      "site": "00b47f18",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46f24",
      "incomplete_value": true,
      "site": "00b46f24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:888:8"
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
      "definition_site": "00b47f68",
      "incomplete_value": true,
      "site": "00b47f68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46f74",
      "incomplete_value": true,
      "site": "00b46f74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:880:8"
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
      "definition_site": "00b47ef4",
      "incomplete_value": true,
      "site": "00b47ef4",
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
      "definition_site": "00b46f00",
      "incomplete_value": true,
      "site": "00b46f00",
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
      "00b47ef0",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47efc",
      "READ",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47f18",
      "WRITE",
      [
        "storage",
        "01125888",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b47ef0",
      "READ",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47efc",
      "READ",
      [
        "storage",
        "01126848",
        null,
        "undefined1"
      ]
    ],
    [
      "00b47f18",
      "WRITE",
      [
        "storage",
        "01126848",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46f24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46ee8.md#insn-00b46f24) · [`00b46f70`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46ee8.md#insn-00b46f70) · [`00b46f74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46ee8.md#insn-00b46f74)
- 新版 [`00b47f18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47edc.md#insn-00b47f18) · [`00b47f64`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47edc.md#insn-00b47f64) · [`00b47f68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47edc.md#insn-00b47f68)

~~~diff
- 00b46f24 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b46f24 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b46f24 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:888:8"]]
- 00b46f24 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b47f18 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b47f18 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b47f18 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:848:8"]]
+ 00b47f18 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b46f24 bytes bf222239
+ 00b47f18 bytes bf222139
- 00b46f70 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b46f70 ["INT_ADD", "register:40f0:8", ["const:b46f70:8", "const:4:8"]]
- 00b46f70 ["CALLIND", null, ["register:0:8"]]
+ 00b47f64 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b47f64 ["INT_ADD", "register:40f0:8", ["const:b47f64:8", "const:4:8"]]
+ 00b47f64 ["CALLIND", null, ["register:0:8"]]
- 00b46f70 bytes 00013fd6
+ 00b47f64 bytes 00013fd6
- 00b46f74 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
- 00b46f74 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b46f74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b47f68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:840:8"]]
+ 00b47f68 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b47f68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b46f74 bytes 9f4204f9
+ 00b47f68 bytes 9f2204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-753300d0bbdaf83fc64f58f70ad5f37e"></a>

### [`00b46f88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46f88.md) → [`00b47f7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47f7c.md) _ZN8firebase4util16dex_class_loader14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b47fbc",
      "incomplete_value": true,
      "site": "00b47fbc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46fc8",
      "incomplete_value": true,
      "site": "00b46fc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:880:8"
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
      "definition_site": "00b47f98",
      "incomplete_value": true,
      "site": "00b47f98",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46fa4",
      "incomplete_value": true,
      "site": "00b46fa4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b47fa0",
      "incomplete_value": false,
      "site": "00b47fb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:ad1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b46fac",
      "incomplete_value": false,
      "site": "00b46fc0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:a02:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b47f90",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47fa0",
      "PARAM",
      [
        "storage",
        "002b8a02",
        null,
        "string"
      ]
    ],
    [
      "00b47fbc",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b47f90",
      "READ",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ],
    [
      "00b47fa0",
      "PARAM",
      [
        "storage",
        "002b8ad1",
        null,
        "string"
      ]
    ],
    [
      "00b47fbc",
      "WRITE",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b46fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46f88.md#insn-00b46fc0) · [`00b46fc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46f88.md#insn-00b46fc8) · [`00b46f94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46f88.md#insn-00b46f94)
- 新版 [`00b47fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47f7c.md#insn-00b47fb4) · [`00b47fbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47f7c.md#insn-00b47fbc) · [`00b47f88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47f7c.md#insn-00b47f88)

~~~diff
- 00b46fc0 ["INT_ADD", "register:40f0:8", ["const:b46fc0:8", "const:4:8"]]
- 00b46fc0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b47fb4 ["INT_ADD", "register:40f0:8", ["const:b47fb4:8", "const:4:8"]]
+ 00b47fb4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b46fc0 bytes 08500494
+ 00b47fb4 bytes ff4f0494
- 00b46fc8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
- 00b46fc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b47fbc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:840:8"]]
+ 00b47fbc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b46fc8 bytes 804204f9
+ 00b47fbc bytes 802204f9
- 00b46f94 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b47f88 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b46f94 bytes f42e00f0
+ 00b47f88 bytes f42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c2073248a2c3671c7aa4a38a4cc87372"></a>

### [`00b46ff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46ff8.md) → [`00b47fec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47fec.md) _ZN8firebase4util16dex_class_loader11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b48008",
      "incomplete_value": true,
      "site": "00b4800c",
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
            "const:463:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47014",
      "incomplete_value": true,
      "site": "00b47018",
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
      "definition_site": "00b48018",
      "incomplete_value": true,
      "site": "00b48024",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b47024",
      "incomplete_value": true,
      "site": "00b47030",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b48008",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b48018",
      "DATA",
      [
        "storage",
        "01125890",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48008",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b48018",
      "DATA",
      [
        "storage",
        "01126850",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47018`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46ff8.md#insn-00b47018) · [`00b47014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46ff8.md#insn-00b47014) · [`00b4701c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b46/00b46ff8.md#insn-00b4701c)
- 新版 [`00b4800c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47fec.md#insn-00b4800c) · [`00b48008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47fec.md#insn-00b48008) · [`00b48010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b47/00b47fec.md#insn-00b48010)

~~~diff
- 00b47018 ["INT_ADD", "register:40f0:8", ["const:b47018:8", "const:4:8"]]
- 00b47018 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4800c ["INT_ADD", "register:40f0:8", ["const:b4800c:8", "const:4:8"]]
+ 00b4800c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b47018 bytes 2e500494
+ 00b4800c bytes 25500494
- 00b47014 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b47014 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47014 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47014 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b48008 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b48008 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48008 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48008 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47014 bytes 002c0c91
+ 00b48008 bytes 008c1191
- 00b4701c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b48010 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4701c bytes e82e00d0
+ 00b48010 bytes e82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-33f82d544f12366422cf556376777586"></a>

### [`00b47034`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47034.md) → [`00b48028`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48028.md) _ZN8firebase4util16dex_class_loader13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48068",
      "incomplete_value": true,
      "site": "00b48068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:840:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47074",
      "incomplete_value": true,
      "site": "00b47074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:880:8"
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
      "definition_site": "00b48044",
      "incomplete_value": true,
      "site": "00b48044",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47050",
      "incomplete_value": true,
      "site": "00b47050",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4804c",
      "incomplete_value": false,
      "site": "00b48060",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:ad1:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47058",
      "incomplete_value": false,
      "site": "00b4706c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b8000:8"
          ],
          [
            "leaf",
            "const:a02:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4803c",
      "READ",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4804c",
      "PARAM",
      [
        "storage",
        "002b8a02",
        null,
        "string"
      ]
    ],
    [
      "00b48068",
      "WRITE",
      [
        "storage",
        "01125880",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4803c",
      "READ",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4804c",
      "PARAM",
      [
        "storage",
        "002b8ad1",
        null,
        "string"
      ]
    ],
    [
      "00b48068",
      "WRITE",
      [
        "storage",
        "01126840",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4706c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47034.md#insn-00b4706c) · [`00b47074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47034.md#insn-00b47074) · [`00b47040`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47034.md#insn-00b47040)
- 新版 [`00b48060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48028.md#insn-00b48060) · [`00b48068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48028.md#insn-00b48068) · [`00b48034`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48028.md#insn-00b48034)

~~~diff
- 00b4706c ["INT_ADD", "register:40f0:8", ["const:b4706c:8", "const:4:8"]]
- 00b4706c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48060 ["INT_ADD", "register:40f0:8", ["const:b48060:8", "const:4:8"]]
+ 00b48060 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4706c bytes dd4f0494
+ 00b48060 bytes d44f0494
- 00b47074 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:880:8"]]
- 00b47074 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48068 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:840:8"]]
+ 00b48068 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47074 bytes 804204f9
+ 00b48068 bytes 802204f9
- 00b47040 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b48034 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b47040 bytes f42e00d0
+ 00b48034 bytes f42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e5dfa92f8de4bce37f62f5fd19dbd3db"></a>

### [`00b470a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b470a4.md) → [`00b48098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48098.md) _ZN8firebase4util16dex_class_loader10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b480b4",
      "incomplete_value": true,
      "site": "00b480b8",
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
            "const:61a:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b470c0",
      "incomplete_value": true,
      "site": "00b470c4",
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
      "definition_site": "00b480c4",
      "incomplete_value": true,
      "site": "00b480d0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b470d0",
      "incomplete_value": true,
      "site": "00b470dc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b480b4",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b480c4",
      "DATA",
      [
        "storage",
        "011258a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b480b4",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b480c4",
      "DATA",
      [
        "storage",
        "01126860",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b470c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b470a4.md#insn-00b470c4) · [`00b470c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b470a4.md#insn-00b470c0) · [`00b470c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b470a4.md#insn-00b470c8)
- 新版 [`00b480b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48098.md#insn-00b480b8) · [`00b480b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48098.md#insn-00b480b4) · [`00b480bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48098.md#insn-00b480bc)

~~~diff
- 00b470c4 ["INT_ADD", "register:40f0:8", ["const:b470c4:8", "const:4:8"]]
- 00b470c4 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b480b8 ["INT_ADD", "register:40f0:8", ["const:b480b8:8", "const:4:8"]]
+ 00b480b8 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b470c4 bytes 03500494
+ 00b480b8 bytes fa4f0494
- 00b470c0 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b470c0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b470c0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b470c0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b480b4 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b480b4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b480b4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b480b4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b470c0 bytes 00341591
+ 00b480b4 bytes 00681891
- 00b470c8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b480bc ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b470c8 bytes e82e00d0
+ 00b480bc bytes e82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-09a0b5b7c63c8228bded3d088985c397"></a>

### [`00b470e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b470e0.md) → [`00b480d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b480d4.md) _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0

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
      "definition_site": "00b48100",
      "incomplete_value": true,
      "site": "00b48100",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4710c",
      "incomplete_value": true,
      "site": "00b4710c",
      "value": [
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
      "definition_site": "00b480e8",
      "incomplete_value": true,
      "site": "00b480e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b470f4",
      "incomplete_value": true,
      "site": "00b470f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b480f4",
      "incomplete_value": true,
      "site": "00b480f8",
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
            "const:9cc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47100",
      "incomplete_value": true,
      "site": "00b47104",
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
            "const:8fd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b480e4",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b480f4",
      "PARAM",
      [
        "storage",
        "002b58fd",
        null,
        "string"
      ]
    ],
    [
      "00b48100",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b480e4",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b480f4",
      "PARAM",
      [
        "storage",
        "002b59cc",
        null,
        "string"
      ]
    ],
    [
      "00b48100",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b470e0.md#insn-00b47104) · [`00b4710c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b470e0.md#insn-00b4710c) · [`00b470ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b470e0.md#insn-00b470ec)
- 新版 [`00b480f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b480d4.md#insn-00b480f8) · [`00b48100`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b480d4.md#insn-00b48100) · [`00b480e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b480d4.md#insn-00b480e0)

~~~diff
- 00b47104 ["INT_ADD", "register:40f0:8", ["const:b47104:8", "const:4:8"]]
- 00b47104 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b480f8 ["INT_ADD", "register:40f0:8", ["const:b480f8:8", "const:4:8"]]
+ 00b480f8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47104 bytes b74f0494
+ 00b480f8 bytes ae4f0494
- 00b4710c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b4710c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48100 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
+ 00b48100 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4710c bytes 605604f9
+ 00b48100 bytes 603604f9
- 00b470ec ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b480e0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b470ec bytes f32e00d0
+ 00b480e0 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf0a17e98b8e892df5fbe4f55a158a9b"></a>

### [`00b47120`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47120.md) → [`00b48114`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48114.md) _ZN8firebase4util9resources19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

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
      "definition_site": "00b48140",
      "incomplete_value": true,
      "site": "00b48140",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4714c",
      "incomplete_value": true,
      "site": "00b4714c",
      "value": [
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
      "definition_site": "00b48128",
      "incomplete_value": true,
      "site": "00b48128",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47134",
      "incomplete_value": true,
      "site": "00b47134",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b47134"
      ],
      [
        "FALL_THROUGH",
        "00b48128"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b48128",
      "incomplete_value": true,
      "site": "00b48140",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47134",
      "incomplete_value": true,
      "site": "00b4714c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b48124",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48130",
      "PARAM",
      [
        "storage",
        "002b58fd",
        null,
        "string"
      ]
    ],
    [
      "00b48140",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48124",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48130",
      "PARAM",
      [
        "storage",
        "002b59cc",
        null,
        "string"
      ]
    ],
    [
      "00b48140",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4714c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47120.md#insn-00b4714c) · [`00b4712c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47120.md#insn-00b4712c) · [`00b47130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47120.md#insn-00b47130)
- 新版 [`00b48140`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48114.md#insn-00b48140) · [`00b48120`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48114.md#insn-00b48120) · [`00b48124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48114.md#insn-00b48124)

~~~diff
- 00b4714c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b4714c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48140 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
+ 00b48140 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4714c bytes 605604f9
+ 00b48140 bytes 603604f9
- 00b4712c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48120 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4712c bytes f32e00d0
+ 00b48120 bytes f32e00d0
- 00b47130 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b47130 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b48124 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
+ 00b48124 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b47130 bytes 685644f9
+ 00b48124 bytes 683644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c8200963f1020fe2e147688af7f83810"></a>

### [`00b47160`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47160.md) → [`00b48154`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48154.md) _ZN8firebase4util9resources10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b48184",
      "incomplete_value": true,
      "site": "00b48184",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47190",
      "incomplete_value": true,
      "site": "00b47190",
      "value": [
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
      "definition_site": "00b48168",
      "incomplete_value": true,
      "site": "00b48168",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47174",
      "incomplete_value": true,
      "site": "00b47174",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48174",
      "incomplete_value": false,
      "site": "00b4817c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:9cc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47180",
      "incomplete_value": false,
      "site": "00b47188",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:8fd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48164",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48174",
      "PARAM",
      [
        "storage",
        "002b58fd",
        null,
        "string"
      ]
    ],
    [
      "00b48184",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48164",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48174",
      "PARAM",
      [
        "storage",
        "002b59cc",
        null,
        "string"
      ]
    ],
    [
      "00b48184",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47188`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47160.md#insn-00b47188) · [`00b47190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47160.md#insn-00b47190) · [`00b4716c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47160.md#insn-00b4716c)
- 新版 [`00b4817c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48154.md#insn-00b4817c) · [`00b48184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48154.md#insn-00b48184) · [`00b48160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48154.md#insn-00b48160)

~~~diff
- 00b47188 ["INT_ADD", "register:40f0:8", ["const:b47188:8", "const:4:8"]]
- 00b47188 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4817c ["INT_ADD", "register:40f0:8", ["const:b4817c:8", "const:4:8"]]
+ 00b4817c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47188 bytes 964f0494
+ 00b4817c bytes 8d4f0494
- 00b47190 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b47190 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48184 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
+ 00b48184 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47190 bytes 605604f9
+ 00b48184 bytes 603604f9
- 00b4716c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48160 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4716c bytes f32e00d0
+ 00b48160 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16eb6e97d30922db5c173a9bf32af9ef"></a>

### [`00b471a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b471a4.md) → [`00b48198`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48198.md) _ZN8firebase4util9resources10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b481c8",
      "incomplete_value": true,
      "site": "00b481c8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b471d4",
      "incomplete_value": true,
      "site": "00b471d4",
      "value": [
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
      "definition_site": "00b481ac",
      "incomplete_value": true,
      "site": "00b481ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b471b8",
      "incomplete_value": true,
      "site": "00b471b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b481b4",
      "incomplete_value": false,
      "site": "00b481c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:9cc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b471c0",
      "incomplete_value": false,
      "site": "00b471cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:8fd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b481a8",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b481b4",
      "PARAM",
      [
        "storage",
        "002b58fd",
        null,
        "string"
      ]
    ],
    [
      "00b481c8",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b481a8",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b481b4",
      "PARAM",
      [
        "storage",
        "002b59cc",
        null,
        "string"
      ]
    ],
    [
      "00b481c8",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b471cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b471a4.md#insn-00b471cc) · [`00b471d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b471a4.md#insn-00b471d4) · [`00b471b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b471a4.md#insn-00b471b0)
- 新版 [`00b481c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48198.md#insn-00b481c0) · [`00b481c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48198.md#insn-00b481c8) · [`00b481a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48198.md#insn-00b481a4)

~~~diff
- 00b471cc ["INT_ADD", "register:40f0:8", ["const:b471cc:8", "const:4:8"]]
- 00b471cc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b481c0 ["INT_ADD", "register:40f0:8", ["const:b481c0:8", "const:4:8"]]
+ 00b481c0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b471cc bytes 854f0494
+ 00b481c0 bytes 7c4f0494
- 00b471d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8a8:8"]]
- 00b471d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b481c8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:868:8"]]
+ 00b481c8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b471d4 bytes 605604f9
+ 00b481c8 bytes 603604f9
- 00b471b0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b481a4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b471b0 bytes f32e00d0
+ 00b481a4 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f14e869650c7470e69abe8d43719b32e"></a>

### [`00b471f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b471f4.md) → [`00b481e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b481e8.md) _ZN8firebase4util9resources15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b48270",
      "incomplete_value": true,
      "site": "00b48270",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4727c",
      "incomplete_value": true,
      "site": "00b4727c",
      "value": [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4821c",
      "incomplete_value": true,
      "site": "00b48228",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:868:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47228",
      "incomplete_value": true,
      "site": "00b47234",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8a8:8"
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
      "00b481fc",
      "READ",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4821c",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48270",
      "WRITE",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b481fc",
      "READ",
      [
        "storage",
        "01126870",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4821c",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48270",
      "WRITE",
      [
        "storage",
        "01126870",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47234`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b471f4.md#insn-00b47234) · [`00b4727c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b471f4.md#insn-00b4727c) · [`00b47204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b471f4.md#insn-00b47204)
- 新版 [`00b48228`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b481e8.md#insn-00b48228) · [`00b48270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b481e8.md#insn-00b48270) · [`00b481f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b481e8.md#insn-00b481f8)

~~~diff
- 00b47234 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47234 ["INT_ADD", "register:40f0:8", ["const:b47234:8", "const:4:8"]]
- 00b47234 ["CALLIND", null, ["register:0:8"]]
+ 00b48228 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48228 ["INT_ADD", "register:40f0:8", ["const:b48228:8", "const:4:8"]]
+ 00b48228 ["CALLIND", null, ["register:0:8"]]
- 00b47234 bytes 00013fd6
+ 00b48228 bytes 00013fd6
- 00b4727c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4727c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8b0:8"]]
- 00b4727c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b48270 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b48270 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:870:8"]]
+ 00b48270 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4727c bytes a0c22239
+ 00b48270 bytes a0c22139
- 00b47204 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b481f8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b47204 bytes f52e00d0
+ 00b481f8 bytes f52e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3da611424928eac9f2fad9460f64aa63"></a>

### [`00b47290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47290.md) → [`00b48284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48284.md) _ZN8firebase4util9resources12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b482c0",
      "incomplete_value": true,
      "site": "00b482c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:870:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b472cc",
      "incomplete_value": true,
      "site": "00b472cc",
      "value": [
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
    "kind": "store_destination",
    "new": {
      "definition_site": "00b48310",
      "incomplete_value": true,
      "site": "00b48310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4731c",
      "incomplete_value": true,
      "site": "00b4731c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      "definition_site": "00b4829c",
      "incomplete_value": true,
      "site": "00b4829c",
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
      "definition_site": "00b472a8",
      "incomplete_value": true,
      "site": "00b472a8",
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
      "00b48298",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b482a4",
      "READ",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b482c0",
      "WRITE",
      [
        "storage",
        "011258b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48298",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b482a4",
      "READ",
      [
        "storage",
        "01126870",
        null,
        "undefined1"
      ]
    ],
    [
      "00b482c0",
      "WRITE",
      [
        "storage",
        "01126870",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b472cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47290.md#insn-00b472cc) · [`00b47318`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47290.md#insn-00b47318) · [`00b4731c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47290.md#insn-00b4731c)
- 新版 [`00b482c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48284.md#insn-00b482c0) · [`00b4830c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48284.md#insn-00b4830c) · [`00b48310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48284.md#insn-00b48310)

~~~diff
- 00b472cc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b472cc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b472cc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8b0:8"]]
- 00b472cc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b482c0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b482c0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b482c0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:870:8"]]
+ 00b482c0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b472cc bytes bfc22239
+ 00b482c0 bytes bfc22139
- 00b47318 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47318 ["INT_ADD", "register:40f0:8", ["const:b47318:8", "const:4:8"]]
- 00b47318 ["CALLIND", null, ["register:0:8"]]
+ 00b4830c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4830c ["INT_ADD", "register:40f0:8", ["const:b4830c:8", "const:4:8"]]
+ 00b4830c ["CALLIND", null, ["register:0:8"]]
- 00b47318 bytes 00013fd6
+ 00b4830c bytes 00013fd6
- 00b4731c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b4731c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4731c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b48310 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:868:8"]]
+ 00b48310 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b48310 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4731c bytes 9f5604f9
+ 00b48310 bytes 9f3604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-74345169ce1bd61c5875ed3bd8ed8eaa"></a>

### [`00b47330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47330.md) → [`00b48324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48324.md) _ZN8firebase4util9resources14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48364",
      "incomplete_value": true,
      "site": "00b48364",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47370",
      "incomplete_value": true,
      "site": "00b47370",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      "definition_site": "00b48340",
      "incomplete_value": true,
      "site": "00b48340",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4734c",
      "incomplete_value": true,
      "site": "00b4734c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48348",
      "incomplete_value": false,
      "site": "00b4835c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:9cc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47354",
      "incomplete_value": false,
      "site": "00b47368",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:8fd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48338",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48348",
      "PARAM",
      [
        "storage",
        "002b58fd",
        null,
        "string"
      ]
    ],
    [
      "00b48364",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48338",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48348",
      "PARAM",
      [
        "storage",
        "002b59cc",
        null,
        "string"
      ]
    ],
    [
      "00b48364",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47330.md#insn-00b47368) · [`00b47370`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47330.md#insn-00b47370) · [`00b4733c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47330.md#insn-00b4733c)
- 新版 [`00b4835c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48324.md#insn-00b4835c) · [`00b48364`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48324.md#insn-00b48364) · [`00b48330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48324.md#insn-00b48330)

~~~diff
- 00b47368 ["INT_ADD", "register:40f0:8", ["const:b47368:8", "const:4:8"]]
- 00b47368 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4835c ["INT_ADD", "register:40f0:8", ["const:b4835c:8", "const:4:8"]]
+ 00b4835c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47368 bytes 1e4f0494
+ 00b4835c bytes 154f0494
- 00b47370 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b47370 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48364 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:868:8"]]
+ 00b48364 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47370 bytes 805604f9
+ 00b48364 bytes 803604f9
- 00b4733c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b48330 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4733c bytes f42e00d0
+ 00b48330 bytes f42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f55b675ed25defc39f37c1c4e292770b"></a>

### [`00b473a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b473a0.md) → [`00b48394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48394.md) _ZN8firebase4util9resources11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b483b0",
      "incomplete_value": false,
      "site": "00b483b4",
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
      "definition_site": "00b473bc",
      "incomplete_value": false,
      "site": "00b473c0",
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
      "definition_site": "00b483c0",
      "incomplete_value": true,
      "site": "00b483cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b473cc",
      "incomplete_value": true,
      "site": "00b473d8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b483b0",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b483c0",
      "DATA",
      [
        "storage",
        "011258b8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b483b0",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b483c0",
      "DATA",
      [
        "storage",
        "01126878",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b473c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b473a0.md#insn-00b473c0) · [`00b473bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b473a0.md#insn-00b473bc) · [`00b473c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b473a0.md#insn-00b473c4)
- 新版 [`00b483b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48394.md#insn-00b483b4) · [`00b483b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48394.md#insn-00b483b0) · [`00b483b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48394.md#insn-00b483b8)

~~~diff
- 00b473c0 ["INT_ADD", "register:40f0:8", ["const:b473c0:8", "const:4:8"]]
- 00b473c0 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b483b4 ["INT_ADD", "register:40f0:8", ["const:b483b4:8", "const:4:8"]]
+ 00b483b4 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b473c0 bytes 444f0494
+ 00b483b4 bytes 3b4f0494
- 00b473bc ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b473bc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b473bc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b473bc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b483b0 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b483b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b483b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b483b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b473bc bytes 002c0c91
+ 00b483b0 bytes 008c1191
- 00b473c4 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b483b8 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b473c4 bytes e82e00d0
+ 00b483b8 bytes e82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-93f9edd7dd59c9cf16d7ddbacbf91f05"></a>

### [`00b473dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b473dc.md) → [`00b483d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b483d0.md) _ZN8firebase4util9resources13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48410",
      "incomplete_value": true,
      "site": "00b48410",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:868:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4741c",
      "incomplete_value": true,
      "site": "00b4741c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8a8:8"
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
      "definition_site": "00b483ec",
      "incomplete_value": true,
      "site": "00b483ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b473f8",
      "incomplete_value": true,
      "site": "00b473f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b483f4",
      "incomplete_value": false,
      "site": "00b48408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:9cc:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47400",
      "incomplete_value": false,
      "site": "00b47414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b5000:8"
          ],
          [
            "leaf",
            "const:8fd:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b483e4",
      "READ",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b483f4",
      "PARAM",
      [
        "storage",
        "002b58fd",
        null,
        "string"
      ]
    ],
    [
      "00b48410",
      "WRITE",
      [
        "storage",
        "011258a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b483e4",
      "READ",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ],
    [
      "00b483f4",
      "PARAM",
      [
        "storage",
        "002b59cc",
        null,
        "string"
      ]
    ],
    [
      "00b48410",
      "WRITE",
      [
        "storage",
        "01126868",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b473dc.md#insn-00b47414) · [`00b4741c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b473dc.md#insn-00b4741c) · [`00b473e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b473dc.md#insn-00b473e8)
- 新版 [`00b48408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b483d0.md#insn-00b48408) · [`00b48410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b483d0.md#insn-00b48410) · [`00b483dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b483d0.md#insn-00b483dc)

~~~diff
- 00b47414 ["INT_ADD", "register:40f0:8", ["const:b47414:8", "const:4:8"]]
- 00b47414 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48408 ["INT_ADD", "register:40f0:8", ["const:b48408:8", "const:4:8"]]
+ 00b48408 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47414 bytes f34e0494
+ 00b48408 bytes ea4e0494
- 00b4741c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8a8:8"]]
- 00b4741c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48410 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:868:8"]]
+ 00b48410 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4741c bytes 805604f9
+ 00b48410 bytes 803604f9
- 00b473e8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b483dc ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b473e8 bytes f42e00d0
+ 00b483dc bytes f42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9dcea08641831fefcdea9e0d50df3ed5"></a>

### [`00b4744c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4744c.md) → [`00b48440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48440.md) _ZN8firebase4util9resources10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4845c",
      "incomplete_value": false,
      "site": "00b48460",
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
      "definition_site": "00b47468",
      "incomplete_value": false,
      "site": "00b4746c",
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
      "definition_site": "00b4846c",
      "incomplete_value": true,
      "site": "00b48478",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b47478",
      "incomplete_value": true,
      "site": "00b47484",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4845c",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4846c",
      "DATA",
      [
        "storage",
        "011258c0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4845c",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4846c",
      "DATA",
      [
        "storage",
        "01126880",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4746c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4744c.md#insn-00b4746c) · [`00b47468`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4744c.md#insn-00b47468) · [`00b47470`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4744c.md#insn-00b47470)
- 新版 [`00b48460`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48440.md#insn-00b48460) · [`00b4845c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48440.md#insn-00b4845c) · [`00b48464`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48440.md#insn-00b48464)

~~~diff
- 00b4746c ["INT_ADD", "register:40f0:8", ["const:b4746c:8", "const:4:8"]]
- 00b4746c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b48460 ["INT_ADD", "register:40f0:8", ["const:b48460:8", "const:4:8"]]
+ 00b48460 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4746c bytes 194f0494
+ 00b48460 bytes 104f0494
- 00b47468 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b47468 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47468 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47468 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4845c ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4845c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4845c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4845c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47468 bytes 00341591
+ 00b4845c bytes 00681891
- 00b47470 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b48464 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b47470 bytes e82e00d0
+ 00b48464 bytes e82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-416721b57ba413d2f44eab212b03a0dd"></a>

### [`00b47488`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47488.md) → [`00b4847c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b4847c.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

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
      "definition_site": "00b484a8",
      "incomplete_value": true,
      "site": "00b484a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b474b4",
      "incomplete_value": true,
      "site": "00b474b4",
      "value": [
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
      "definition_site": "00b48490",
      "incomplete_value": true,
      "site": "00b48490",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4749c",
      "incomplete_value": true,
      "site": "00b4749c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4849c",
      "incomplete_value": false,
      "site": "00b484a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:65b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b474a8",
      "incomplete_value": false,
      "site": "00b474ac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:57d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4848c",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4849c",
      "PARAM",
      [
        "storage",
        "002be57d",
        null,
        "string"
      ]
    ],
    [
      "00b484a8",
      "WRITE",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4848c",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4849c",
      "PARAM",
      [
        "storage",
        "002be65b",
        null,
        "string"
      ]
    ],
    [
      "00b484a8",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b474ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47488.md#insn-00b474ac) · [`00b474b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47488.md#insn-00b474b4) · [`00b47494`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47488.md#insn-00b47494)
- 新版 [`00b484a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b4847c.md#insn-00b484a0) · [`00b484a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b4847c.md#insn-00b484a8) · [`00b48488`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b4847c.md#insn-00b48488)

~~~diff
- 00b474ac ["INT_ADD", "register:40f0:8", ["const:b474ac:8", "const:4:8"]]
- 00b474ac ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b484a0 ["INT_ADD", "register:40f0:8", ["const:b484a0:8", "const:4:8"]]
+ 00b484a0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b474ac bytes cd4e0494
+ 00b484a0 bytes c44e0494
- 00b474b4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00b474b4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b484a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b484a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b474b4 bytes 606604f9
+ 00b484a8 bytes 604604f9
- 00b47494 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48488 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b47494 bytes f32e00d0
+ 00b48488 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-978cda7aab40c9b36d586848749e5982"></a>

### [`00b474c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b474c8.md) → [`00b484bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b484bc.md) _ZN8firebase4util8activity19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b484e8",
      "incomplete_value": true,
      "site": "00b484e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b474f4",
      "incomplete_value": true,
      "site": "00b474f4",
      "value": [
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
      "definition_site": "00b484d0",
      "incomplete_value": true,
      "site": "00b484d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b474dc",
      "incomplete_value": true,
      "site": "00b474dc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b484d8",
      "incomplete_value": false,
      "site": "00b484e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:65b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b474e4",
      "incomplete_value": false,
      "site": "00b474ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:57d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b484cc",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b484d8",
      "PARAM",
      [
        "storage",
        "002be57d",
        null,
        "string"
      ]
    ],
    [
      "00b484e8",
      "WRITE",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b484cc",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b484d8",
      "PARAM",
      [
        "storage",
        "002be65b",
        null,
        "string"
      ]
    ],
    [
      "00b484e8",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b474ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b474c8.md#insn-00b474ec) · [`00b474f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b474c8.md#insn-00b474f4) · [`00b474d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b474c8.md#insn-00b474d4)
- 新版 [`00b484e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b484bc.md#insn-00b484e0) · [`00b484e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b484bc.md#insn-00b484e8) · [`00b484c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b484bc.md#insn-00b484c8)

~~~diff
- 00b474ec ["INT_ADD", "register:40f0:8", ["const:b474ec:8", "const:4:8"]]
- 00b474ec ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b484e0 ["INT_ADD", "register:40f0:8", ["const:b484e0:8", "const:4:8"]]
+ 00b484e0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b474ec bytes bd4e0494
+ 00b484e0 bytes b44e0494
- 00b474f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00b474f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b484e8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b484e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b474f4 bytes 606604f9
+ 00b484e8 bytes 604604f9
- 00b474d4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b484c8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b474d4 bytes f32e00d0
+ 00b484c8 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d3099fa84e960ab1cf4f3be3bbdd056a"></a>

### [`00b47508`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47508.md) → [`00b484fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b484fc.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4852c",
      "incomplete_value": true,
      "site": "00b4852c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47538",
      "incomplete_value": true,
      "site": "00b47538",
      "value": [
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
      "definition_site": "00b48510",
      "incomplete_value": true,
      "site": "00b48510",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4751c",
      "incomplete_value": true,
      "site": "00b4751c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4851c",
      "incomplete_value": false,
      "site": "00b48524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:65b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47528",
      "incomplete_value": false,
      "site": "00b47530",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:57d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4850c",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4851c",
      "PARAM",
      [
        "storage",
        "002be57d",
        null,
        "string"
      ]
    ],
    [
      "00b4852c",
      "WRITE",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4850c",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4851c",
      "PARAM",
      [
        "storage",
        "002be65b",
        null,
        "string"
      ]
    ],
    [
      "00b4852c",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47530`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47508.md#insn-00b47530) · [`00b47538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47508.md#insn-00b47538) · [`00b47514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47508.md#insn-00b47514)
- 新版 [`00b48524`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b484fc.md#insn-00b48524) · [`00b4852c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b484fc.md#insn-00b4852c) · [`00b48508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b484fc.md#insn-00b48508)

~~~diff
- 00b47530 ["INT_ADD", "register:40f0:8", ["const:b47530:8", "const:4:8"]]
- 00b47530 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48524 ["INT_ADD", "register:40f0:8", ["const:b48524:8", "const:4:8"]]
+ 00b48524 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47530 bytes ac4e0494
+ 00b48524 bytes a34e0494
- 00b47538 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00b47538 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4852c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b4852c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47538 bytes 606604f9
+ 00b4852c bytes 604604f9
- 00b47514 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48508 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b47514 bytes f32e00d0
+ 00b48508 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bd25377d7c5027d2f84e117470c0246a"></a>

### [`00b4754c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4754c.md) → [`00b48540`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48540.md) _ZN8firebase4util8activity10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48570",
      "incomplete_value": true,
      "site": "00b48570",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4757c",
      "incomplete_value": true,
      "site": "00b4757c",
      "value": [
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
      "definition_site": "00b48554",
      "incomplete_value": true,
      "site": "00b48554",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47560",
      "incomplete_value": true,
      "site": "00b47560",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4855c",
      "incomplete_value": false,
      "site": "00b48568",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:65b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47568",
      "incomplete_value": false,
      "site": "00b47574",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:57d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48550",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4855c",
      "PARAM",
      [
        "storage",
        "002be57d",
        null,
        "string"
      ]
    ],
    [
      "00b48570",
      "WRITE",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48550",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4855c",
      "PARAM",
      [
        "storage",
        "002be65b",
        null,
        "string"
      ]
    ],
    [
      "00b48570",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47574`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4754c.md#insn-00b47574) · [`00b4757c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4754c.md#insn-00b4757c) · [`00b47558`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4754c.md#insn-00b47558)
- 新版 [`00b48568`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48540.md#insn-00b48568) · [`00b48570`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48540.md#insn-00b48570) · [`00b4854c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48540.md#insn-00b4854c)

~~~diff
- 00b47574 ["INT_ADD", "register:40f0:8", ["const:b47574:8", "const:4:8"]]
- 00b47574 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48568 ["INT_ADD", "register:40f0:8", ["const:b48568:8", "const:4:8"]]
+ 00b48568 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47574 bytes 9b4e0494
+ 00b48568 bytes 924e0494
- 00b4757c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8c8:8"]]
- 00b4757c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48570 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:888:8"]]
+ 00b48570 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4757c bytes 606604f9
+ 00b48570 bytes 604604f9
- 00b47558 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4854c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b47558 bytes f32e00d0
+ 00b4854c bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-19a7bbe76603f6dd0580ea359d304d67"></a>

### [`00b4759c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4759c.md) → [`00b48590`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48590.md) _ZN8firebase4util8activity15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b48618",
      "incomplete_value": true,
      "site": "00b48618",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47624",
      "incomplete_value": true,
      "site": "00b47624",
      "value": [
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
      "definition_site": "00b485c4",
      "incomplete_value": true,
      "site": "00b485d0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:888:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b475d0",
      "incomplete_value": true,
      "site": "00b475dc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b485a4",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b485c4",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48618",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b485a4",
      "READ",
      [
        "storage",
        "01126890",
        null,
        "undefined1"
      ]
    ],
    [
      "00b485c4",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48618",
      "WRITE",
      [
        "storage",
        "01126890",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b475dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4759c.md#insn-00b475dc) · [`00b47624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4759c.md#insn-00b47624) · [`00b475ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b4759c.md#insn-00b475ac)
- 新版 [`00b485d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48590.md#insn-00b485d0) · [`00b48618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48590.md#insn-00b48618) · [`00b485a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48590.md#insn-00b485a0)

~~~diff
- 00b475dc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b475dc ["INT_ADD", "register:40f0:8", ["const:b475dc:8", "const:4:8"]]
- 00b475dc ["CALLIND", null, ["register:0:8"]]
+ 00b485d0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b485d0 ["INT_ADD", "register:40f0:8", ["const:b485d0:8", "const:4:8"]]
+ 00b485d0 ["CALLIND", null, ["register:0:8"]]
- 00b475dc bytes 00013fd6
+ 00b485d0 bytes 00013fd6
- 00b47624 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b47624 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8d0:8"]]
- 00b47624 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b48618 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b48618 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:890:8"]]
+ 00b48618 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b47624 bytes a0422339
+ 00b48618 bytes a0422239
- 00b475ac ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b485a0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b475ac bytes f52e00d0
+ 00b485a0 bytes f52e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4dc3cf1d1f6f366f7a523be0cb6b9c05"></a>

### [`00b47638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47638.md) → [`00b4862c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b4862c.md) _ZN8firebase4util8activity12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b48668",
      "incomplete_value": true,
      "site": "00b48668",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:890:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47674",
      "incomplete_value": true,
      "site": "00b47674",
      "value": [
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
      "definition_site": "00b486b8",
      "incomplete_value": true,
      "site": "00b486b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b476c4",
      "incomplete_value": true,
      "site": "00b476c4",
      "value": [
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
      "definition_site": "00b48644",
      "incomplete_value": true,
      "site": "00b48644",
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
      "definition_site": "00b47650",
      "incomplete_value": true,
      "site": "00b47650",
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
      "00b48640",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4864c",
      "READ",
      [
        "storage",
        "011258d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48668",
      "WRITE",
      [
        "storage",
        "011258d0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48640",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4864c",
      "READ",
      [
        "storage",
        "01126890",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48668",
      "WRITE",
      [
        "storage",
        "01126890",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47674`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47638.md#insn-00b47674) · [`00b476c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47638.md#insn-00b476c0) · [`00b476c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47638.md#insn-00b476c4)
- 新版 [`00b48668`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b4862c.md#insn-00b48668) · [`00b486b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b4862c.md#insn-00b486b4) · [`00b486b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b4862c.md#insn-00b486b8)

~~~diff
- 00b47674 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b47674 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b47674 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8d0:8"]]
- 00b47674 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b48668 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b48668 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b48668 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:890:8"]]
+ 00b48668 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b47674 bytes bf422339
+ 00b48668 bytes bf422239
- 00b476c0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b476c0 ["INT_ADD", "register:40f0:8", ["const:b476c0:8", "const:4:8"]]
- 00b476c0 ["CALLIND", null, ["register:0:8"]]
+ 00b486b4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b486b4 ["INT_ADD", "register:40f0:8", ["const:b486b4:8", "const:4:8"]]
+ 00b486b4 ["CALLIND", null, ["register:0:8"]]
- 00b476c0 bytes 00013fd6
+ 00b486b4 bytes 00013fd6
- 00b476c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
- 00b476c4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b476c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b486b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
+ 00b486b8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b486b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b476c4 bytes 9f6604f9
+ 00b486b8 bytes 9f4604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-00536ac2a13ed06eb7a9a4e65c4fc5ea"></a>

### [`00b476d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b476d8.md) → [`00b486cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b486cc.md) _ZN8firebase4util8activity14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4870c",
      "incomplete_value": true,
      "site": "00b4870c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47718",
      "incomplete_value": true,
      "site": "00b47718",
      "value": [
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
      "definition_site": "00b486e8",
      "incomplete_value": true,
      "site": "00b486e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b476f4",
      "incomplete_value": true,
      "site": "00b476f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b486f0",
      "incomplete_value": false,
      "site": "00b48704",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:65b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b476fc",
      "incomplete_value": false,
      "site": "00b47710",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:57d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b486e0",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b486f0",
      "PARAM",
      [
        "storage",
        "002be57d",
        null,
        "string"
      ]
    ],
    [
      "00b4870c",
      "WRITE",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b486e0",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b486f0",
      "PARAM",
      [
        "storage",
        "002be65b",
        null,
        "string"
      ]
    ],
    [
      "00b4870c",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b476d8.md#insn-00b47710) · [`00b47718`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b476d8.md#insn-00b47718) · [`00b476e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b476d8.md#insn-00b476e4)
- 新版 [`00b48704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b486cc.md#insn-00b48704) · [`00b4870c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b486cc.md#insn-00b4870c) · [`00b486d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b486cc.md#insn-00b486d8)

~~~diff
- 00b47710 ["INT_ADD", "register:40f0:8", ["const:b47710:8", "const:4:8"]]
- 00b47710 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48704 ["INT_ADD", "register:40f0:8", ["const:b48704:8", "const:4:8"]]
+ 00b48704 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47710 bytes 344e0494
+ 00b48704 bytes 2b4e0494
- 00b47718 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
- 00b47718 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4870c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
+ 00b4870c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47718 bytes 806604f9
+ 00b4870c bytes 804604f9
- 00b476e4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b486d8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b476e4 bytes f42e00d0
+ 00b486d8 bytes f42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-26b79f2d6e04e79fdda45d779961020a"></a>

### [`00b47748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47748.md) → [`00b4873c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b4873c.md) _ZN8firebase4util8activity11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b620`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b620.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5c5f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c5f0.md) · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b48758",
      "incomplete_value": false,
      "site": "00b4875c",
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
      "definition_site": "00b47764",
      "incomplete_value": false,
      "site": "00b47768",
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
      "definition_site": "00b48768",
      "incomplete_value": true,
      "site": "00b48774",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b47774",
      "incomplete_value": true,
      "site": "00b47780",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b48758",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b48768",
      "DATA",
      [
        "storage",
        "011258d8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b48758",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b48768",
      "DATA",
      [
        "storage",
        "01126898",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47768`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47748.md#insn-00b47768) · [`00b47764`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47748.md#insn-00b47764) · [`00b4776c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47748.md#insn-00b4776c)
- 新版 [`00b4875c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b4873c.md#insn-00b4875c) · [`00b48758`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b4873c.md#insn-00b48758) · [`00b48760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b4873c.md#insn-00b48760)

~~~diff
- 00b47768 ["INT_ADD", "register:40f0:8", ["const:b47768:8", "const:4:8"]]
- 00b47768 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4875c ["INT_ADD", "register:40f0:8", ["const:b4875c:8", "const:4:8"]]
+ 00b4875c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b47768 bytes 5a4e0494
+ 00b4875c bytes 514e0494
- 00b47764 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b47764 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47764 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47764 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b48758 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b48758 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48758 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48758 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47764 bytes 002c0c91
+ 00b48758 bytes 008c1191
- 00b4776c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b48760 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4776c bytes e82e00d0
+ 00b48760 bytes e82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0b3c3d800518737e7727901ea9518b82"></a>

### [`00b47784`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47784.md) → [`00b48778`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48778.md) _ZN8firebase4util8activity13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b487b8",
      "incomplete_value": true,
      "site": "00b487b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:888:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b477c4",
      "incomplete_value": true,
      "site": "00b477c4",
      "value": [
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
      "definition_site": "00b48794",
      "incomplete_value": true,
      "site": "00b48794",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b477a0",
      "incomplete_value": true,
      "site": "00b477a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4879c",
      "incomplete_value": false,
      "site": "00b487b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:65b:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b477a8",
      "incomplete_value": false,
      "site": "00b477bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2be000:8"
          ],
          [
            "leaf",
            "const:57d:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4878c",
      "READ",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4879c",
      "PARAM",
      [
        "storage",
        "002be57d",
        null,
        "string"
      ]
    ],
    [
      "00b487b8",
      "WRITE",
      [
        "storage",
        "011258c8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4878c",
      "READ",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4879c",
      "PARAM",
      [
        "storage",
        "002be65b",
        null,
        "string"
      ]
    ],
    [
      "00b487b8",
      "WRITE",
      [
        "storage",
        "01126888",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b477bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47784.md#insn-00b477bc) · [`00b477c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47784.md#insn-00b477c4) · [`00b47790`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47784.md#insn-00b47790)
- 新版 [`00b487b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48778.md#insn-00b487b0) · [`00b487b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48778.md#insn-00b487b8) · [`00b48784`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48778.md#insn-00b48784)

~~~diff
- 00b477bc ["INT_ADD", "register:40f0:8", ["const:b477bc:8", "const:4:8"]]
- 00b477bc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b487b0 ["INT_ADD", "register:40f0:8", ["const:b487b0:8", "const:4:8"]]
+ 00b487b0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b477bc bytes 094e0494
+ 00b487b0 bytes 004e0494
- 00b477c4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8c8:8"]]
- 00b477c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b487b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:888:8"]]
+ 00b487b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b477c4 bytes 806604f9
+ 00b487b8 bytes 804604f9
- 00b47790 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b48784 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b47790 bytes f42e00d0
+ 00b48784 bytes f42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8c906d8af83e28fc758d3ab63441e774"></a>

### [`00b477f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b477f4.md) → [`00b487e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b487e8.md) _ZN8firebase4util8activity10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b48804",
      "incomplete_value": false,
      "site": "00b48808",
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
      "definition_site": "00b47810",
      "incomplete_value": false,
      "site": "00b47814",
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
      "definition_site": "00b48814",
      "incomplete_value": true,
      "site": "00b48820",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b47820",
      "incomplete_value": true,
      "site": "00b4782c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b48804",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b48814",
      "DATA",
      [
        "storage",
        "01125928",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b48804",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b48814",
      "DATA",
      [
        "storage",
        "011268e8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47814`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b477f4.md#insn-00b47814) · [`00b47810`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b477f4.md#insn-00b47810) · [`00b47818`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b477f4.md#insn-00b47818)
- 新版 [`00b48808`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b487e8.md#insn-00b48808) · [`00b48804`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b487e8.md#insn-00b48804) · [`00b4880c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b487e8.md#insn-00b4880c)

~~~diff
- 00b47814 ["INT_ADD", "register:40f0:8", ["const:b47814:8", "const:4:8"]]
- 00b47814 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b48808 ["INT_ADD", "register:40f0:8", ["const:b48808:8", "const:4:8"]]
+ 00b48808 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b47814 bytes 2f4e0494
+ 00b48808 bytes 264e0494
- 00b47810 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b47810 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47810 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47810 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b48804 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b48804 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48804 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48804 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47810 bytes 00341591
+ 00b48804 bytes 00681891
- 00b47818 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4880c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b47818 bytes e82e00d0
+ 00b4880c bytes e82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c35cd0f0b822e05cb16813ea3bbbaded"></a>

### [`00b47830`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47830.md) → [`00b48824`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48824.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00b48850",
      "incomplete_value": true,
      "site": "00b48850",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4785c",
      "incomplete_value": true,
      "site": "00b4785c",
      "value": [
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
      "definition_site": "00b48838",
      "incomplete_value": true,
      "site": "00b48838",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47844",
      "incomplete_value": true,
      "site": "00b47844",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48844",
      "incomplete_value": false,
      "site": "00b48848",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47850",
      "incomplete_value": false,
      "site": "00b47854",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48834",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48844",
      "PARAM",
      [
        "storage",
        "002a70b8",
        null,
        "string"
      ]
    ],
    [
      "00b48850",
      "WRITE",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48834",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48844",
      "PARAM",
      [
        "storage",
        "002a7210",
        null,
        "string"
      ]
    ],
    [
      "00b48850",
      "WRITE",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47854`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47830.md#insn-00b47854) · [`00b4785c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47830.md#insn-00b4785c) · [`00b4783c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47830.md#insn-00b4783c)
- 新版 [`00b48848`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48824.md#insn-00b48848) · [`00b48850`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48824.md#insn-00b48850) · [`00b48830`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48824.md#insn-00b48830)

~~~diff
- 00b47854 ["INT_ADD", "register:40f0:8", ["const:b47854:8", "const:4:8"]]
- 00b47854 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48848 ["INT_ADD", "register:40f0:8", ["const:b48848:8", "const:4:8"]]
+ 00b48848 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47854 bytes e34d0494
+ 00b48848 bytes da4d0494
- 00b4785c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00b4785c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48850 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
+ 00b48850 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4785c bytes 609a04f9
+ 00b48850 bytes 607a04f9
- 00b4783c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48830 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4783c bytes f32e00d0
+ 00b48830 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6d405ad9d9e6201237b38be712f1ab36"></a>

### [`00b47870`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47870.md) → [`00b48864`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48864.md) _ZN8firebase4util10array_list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b48890",
      "incomplete_value": true,
      "site": "00b48890",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4789c",
      "incomplete_value": true,
      "site": "00b4789c",
      "value": [
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
      "definition_site": "00b48878",
      "incomplete_value": true,
      "site": "00b48878",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47884",
      "incomplete_value": true,
      "site": "00b47884",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48880",
      "incomplete_value": false,
      "site": "00b48888",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4788c",
      "incomplete_value": false,
      "site": "00b47894",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48874",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48880",
      "PARAM",
      [
        "storage",
        "002a70b8",
        null,
        "string"
      ]
    ],
    [
      "00b48890",
      "WRITE",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48874",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48880",
      "PARAM",
      [
        "storage",
        "002a7210",
        null,
        "string"
      ]
    ],
    [
      "00b48890",
      "WRITE",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47870.md#insn-00b47894) · [`00b4789c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47870.md#insn-00b4789c) · [`00b4787c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47870.md#insn-00b4787c)
- 新版 [`00b48888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48864.md#insn-00b48888) · [`00b48890`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48864.md#insn-00b48890) · [`00b48870`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48864.md#insn-00b48870)

~~~diff
- 00b47894 ["INT_ADD", "register:40f0:8", ["const:b47894:8", "const:4:8"]]
- 00b47894 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48888 ["INT_ADD", "register:40f0:8", ["const:b48888:8", "const:4:8"]]
+ 00b48888 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47894 bytes d34d0494
+ 00b48888 bytes ca4d0494
- 00b4789c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00b4789c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48890 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
+ 00b48890 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4789c bytes 609a04f9
+ 00b48890 bytes 607a04f9
- 00b4787c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48870 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4787c bytes f32e00d0
+ 00b48870 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef698e0c808c26129f62d31e2cfa789b"></a>

### [`00b478b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b478b0.md) → [`00b488a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b488a4.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b488d4",
      "incomplete_value": true,
      "site": "00b488d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b478e0",
      "incomplete_value": true,
      "site": "00b478e0",
      "value": [
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
      "definition_site": "00b488b8",
      "incomplete_value": true,
      "site": "00b488b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b478c4",
      "incomplete_value": true,
      "site": "00b478c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b488c4",
      "incomplete_value": false,
      "site": "00b488cc",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b478d0",
      "incomplete_value": false,
      "site": "00b478d8",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b488b4",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b488c4",
      "PARAM",
      [
        "storage",
        "002a70b8",
        null,
        "string"
      ]
    ],
    [
      "00b488d4",
      "WRITE",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b488b4",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b488c4",
      "PARAM",
      [
        "storage",
        "002a7210",
        null,
        "string"
      ]
    ],
    [
      "00b488d4",
      "WRITE",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b478d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b478b0.md#insn-00b478d8) · [`00b478e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b478b0.md#insn-00b478e0) · [`00b478bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b478b0.md#insn-00b478bc)
- 新版 [`00b488cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b488a4.md#insn-00b488cc) · [`00b488d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b488a4.md#insn-00b488d4) · [`00b488b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b488a4.md#insn-00b488b0)

~~~diff
- 00b478d8 ["INT_ADD", "register:40f0:8", ["const:b478d8:8", "const:4:8"]]
- 00b478d8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b488cc ["INT_ADD", "register:40f0:8", ["const:b488cc:8", "const:4:8"]]
+ 00b488cc ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b478d8 bytes c24d0494
+ 00b488cc bytes b94d0494
- 00b478e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00b478e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b488d4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
+ 00b488d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b478e0 bytes 609a04f9
+ 00b488d4 bytes 607a04f9
- 00b478bc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b488b0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b478bc bytes f32e00d0
+ 00b488b0 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ce2c07013b1f8a995a88d84711a2f2d2"></a>

### [`00b478f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b478f4.md) → [`00b488e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b488e8.md) _ZN8firebase4util10array_list10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48918",
      "incomplete_value": true,
      "site": "00b48918",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47924",
      "incomplete_value": true,
      "site": "00b47924",
      "value": [
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
      "definition_site": "00b488fc",
      "incomplete_value": true,
      "site": "00b488fc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47908",
      "incomplete_value": true,
      "site": "00b47908",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48904",
      "incomplete_value": false,
      "site": "00b48910",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47910",
      "incomplete_value": false,
      "site": "00b4791c",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b488f8",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48904",
      "PARAM",
      [
        "storage",
        "002a70b8",
        null,
        "string"
      ]
    ],
    [
      "00b48918",
      "WRITE",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b488f8",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48904",
      "PARAM",
      [
        "storage",
        "002a7210",
        null,
        "string"
      ]
    ],
    [
      "00b48918",
      "WRITE",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4791c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b478f4.md#insn-00b4791c) · [`00b47924`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b478f4.md#insn-00b47924) · [`00b47900`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b478f4.md#insn-00b47900)
- 新版 [`00b48910`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b488e8.md#insn-00b48910) · [`00b48918`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b488e8.md#insn-00b48918) · [`00b488f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b488e8.md#insn-00b488f4)

~~~diff
- 00b4791c ["INT_ADD", "register:40f0:8", ["const:b4791c:8", "const:4:8"]]
- 00b4791c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48910 ["INT_ADD", "register:40f0:8", ["const:b48910:8", "const:4:8"]]
+ 00b48910 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4791c bytes b14d0494
+ 00b48910 bytes a84d0494
- 00b47924 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:930:8"]]
- 00b47924 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48918 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:8f0:8"]]
+ 00b48918 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47924 bytes 609a04f9
+ 00b48918 bytes 607a04f9
- 00b47900 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b488f4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b47900 bytes f32e00d0
+ 00b488f4 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5db7a218ded525ecb6bf0c4d15af708e"></a>

### [`00b47944`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47944.md) → [`00b48938`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48938.md) _ZN8firebase4util10array_list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b489c0",
      "incomplete_value": true,
      "site": "00b489c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b479cc",
      "incomplete_value": true,
      "site": "00b479cc",
      "value": [
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
      "definition_site": "00b4896c",
      "incomplete_value": true,
      "site": "00b48978",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:8f0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47978",
      "incomplete_value": true,
      "site": "00b47984",
      "value": [
        "LOAD",
        "8",
        [
          [
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
      "00b4894c",
      "READ",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4896c",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b489c0",
      "WRITE",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4894c",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4896c",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b489c0",
      "WRITE",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47984`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47944.md#insn-00b47984) · [`00b479cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47944.md#insn-00b479cc) · [`00b47954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47944.md#insn-00b47954)
- 新版 [`00b48978`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48938.md#insn-00b48978) · [`00b489c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48938.md#insn-00b489c0) · [`00b48948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48938.md#insn-00b48948)

~~~diff
- 00b47984 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47984 ["INT_ADD", "register:40f0:8", ["const:b47984:8", "const:4:8"]]
- 00b47984 ["CALLIND", null, ["register:0:8"]]
+ 00b48978 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48978 ["INT_ADD", "register:40f0:8", ["const:b48978:8", "const:4:8"]]
+ 00b48978 ["CALLIND", null, ["register:0:8"]]
- 00b47984 bytes 00013fd6
+ 00b48978 bytes 00013fd6
- 00b479cc ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b479cc ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:938:8"]]
- 00b479cc ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b489c0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b489c0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:8f8:8"]]
+ 00b489c0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b479cc bytes a0e22439
+ 00b489c0 bytes a0e22339
- 00b47954 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b48948 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b47954 bytes f52e00d0
+ 00b48948 bytes f52e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e24d14e7d1e98cd771ff205ab6f52bf2"></a>

### [`00b479e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b479e0.md) → [`00b489d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b489d4.md) _ZN8firebase4util10array_list12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b48a10",
      "incomplete_value": true,
      "site": "00b48a10",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:8f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47a1c",
      "incomplete_value": true,
      "site": "00b47a1c",
      "value": [
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
      "definition_site": "00b48a60",
      "incomplete_value": true,
      "site": "00b48a60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47a6c",
      "incomplete_value": true,
      "site": "00b47a6c",
      "value": [
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
      "definition_site": "00b489ec",
      "incomplete_value": true,
      "site": "00b489ec",
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
      "definition_site": "00b479f8",
      "incomplete_value": true,
      "site": "00b479f8",
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
      "00b489e8",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b489f4",
      "READ",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48a10",
      "WRITE",
      [
        "storage",
        "01125938",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b489e8",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b489f4",
      "READ",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48a10",
      "WRITE",
      [
        "storage",
        "011268f8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47a1c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b479e0.md#insn-00b47a1c) · [`00b47a68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b479e0.md#insn-00b47a68) · [`00b47a6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b479e0.md#insn-00b47a6c)
- 新版 [`00b48a10`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b489d4.md#insn-00b48a10) · [`00b48a5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b489d4.md#insn-00b48a5c) · [`00b48a60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b489d4.md#insn-00b48a60)

~~~diff
- 00b47a1c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b47a1c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b47a1c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:938:8"]]
- 00b47a1c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b48a10 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b48a10 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b48a10 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:8f8:8"]]
+ 00b48a10 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b47a1c bytes bfe22439
+ 00b48a10 bytes bfe22339
- 00b47a68 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47a68 ["INT_ADD", "register:40f0:8", ["const:b47a68:8", "const:4:8"]]
- 00b47a68 ["CALLIND", null, ["register:0:8"]]
+ 00b48a5c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48a5c ["INT_ADD", "register:40f0:8", ["const:b48a5c:8", "const:4:8"]]
+ 00b48a5c ["CALLIND", null, ["register:0:8"]]
- 00b47a68 bytes 00013fd6
+ 00b48a5c bytes 00013fd6
- 00b47a6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
- 00b47a6c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b47a6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b48a60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f0:8"]]
+ 00b48a60 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b48a60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b47a6c bytes 9f9a04f9
+ 00b48a60 bytes 9f7a04f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f8499318aaeea29762a2176cde2b60c"></a>

### [`00b47a80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47a80.md) → [`00b48a74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48a74.md) _ZN8firebase4util10array_list14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48ab4",
      "incomplete_value": true,
      "site": "00b48ab4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47ac0",
      "incomplete_value": true,
      "site": "00b47ac0",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48a90",
      "incomplete_value": true,
      "site": "00b48a90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47a9c",
      "incomplete_value": true,
      "site": "00b47a9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48a98",
      "incomplete_value": false,
      "site": "00b48aac",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47aa4",
      "incomplete_value": false,
      "site": "00b47ab8",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48a88",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48a98",
      "PARAM",
      [
        "storage",
        "002a70b8",
        null,
        "string"
      ]
    ],
    [
      "00b48ab4",
      "WRITE",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48a88",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48a98",
      "PARAM",
      [
        "storage",
        "002a7210",
        null,
        "string"
      ]
    ],
    [
      "00b48ab4",
      "WRITE",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47ab8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47a80.md#insn-00b47ab8) · [`00b47ac0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47a80.md#insn-00b47ac0) · [`00b47a8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47a80.md#insn-00b47a8c)
- 新版 [`00b48aac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48a74.md#insn-00b48aac) · [`00b48ab4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48a74.md#insn-00b48ab4) · [`00b48a80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48a74.md#insn-00b48a80)

~~~diff
- 00b47ab8 ["INT_ADD", "register:40f0:8", ["const:b47ab8:8", "const:4:8"]]
- 00b47ab8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48aac ["INT_ADD", "register:40f0:8", ["const:b48aac:8", "const:4:8"]]
+ 00b48aac ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47ab8 bytes 4a4d0494
+ 00b48aac bytes 414d0494
- 00b47ac0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
- 00b47ac0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48ab4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f0:8"]]
+ 00b48ab4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47ac0 bytes 809a04f9
+ 00b48ab4 bytes 807a04f9
- 00b47a8c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b48a80 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b47a8c bytes f42e00d0
+ 00b48a80 bytes f42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1f5b72a33f12d9c223e9ed3a80e4a8c5"></a>

### [`00b47af0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47af0.md) → [`00b48ae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ae4.md) _ZN8firebase4util10array_list11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5af80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5af80.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5bf50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bf50.md) · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b48b00",
      "incomplete_value": false,
      "site": "00b48b04",
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
      "definition_site": "00b47b0c",
      "incomplete_value": false,
      "site": "00b47b10",
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
      "definition_site": "00b48b10",
      "incomplete_value": true,
      "site": "00b48b1c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b47b1c",
      "incomplete_value": true,
      "site": "00b47b28",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b48b00",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b48b10",
      "DATA",
      [
        "storage",
        "01125940",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48b00",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b48b10",
      "DATA",
      [
        "storage",
        "01126900",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47b10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47af0.md#insn-00b47b10) · [`00b47b0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47af0.md#insn-00b47b0c) · [`00b47b14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47af0.md#insn-00b47b14)
- 新版 [`00b48b04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ae4.md#insn-00b48b04) · [`00b48b00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ae4.md#insn-00b48b00) · [`00b48b08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ae4.md#insn-00b48b08)

~~~diff
- 00b47b10 ["INT_ADD", "register:40f0:8", ["const:b47b10:8", "const:4:8"]]
- 00b47b10 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b48b04 ["INT_ADD", "register:40f0:8", ["const:b48b04:8", "const:4:8"]]
+ 00b48b04 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b47b10 bytes 704d0494
+ 00b48b04 bytes 674d0494
- 00b47b0c ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b47b0c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47b0c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47b0c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b48b00 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b48b00 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48b00 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48b00 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47b0c bytes 002c0c91
+ 00b48b00 bytes 008c1191
- 00b47b14 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b48b08 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b47b14 bytes e82e00d0
+ 00b48b08 bytes e82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6f8b77796ac416d77cfe51a38546bb56"></a>

### [`00b47b2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47b2c.md) → [`00b48b20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48b20.md) _ZN8firebase4util10array_list13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48b60",
      "incomplete_value": true,
      "site": "00b48b60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:8f0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47b6c",
      "incomplete_value": true,
      "site": "00b47b6c",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48b3c",
      "incomplete_value": true,
      "site": "00b48b3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47b48",
      "incomplete_value": true,
      "site": "00b47b48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48b44",
      "incomplete_value": false,
      "site": "00b48b58",
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
            "const:210:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47b50",
      "incomplete_value": false,
      "site": "00b47b64",
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
            "const:b8:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48b34",
      "READ",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48b44",
      "PARAM",
      [
        "storage",
        "002a70b8",
        null,
        "string"
      ]
    ],
    [
      "00b48b60",
      "WRITE",
      [
        "storage",
        "01125930",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48b34",
      "READ",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48b44",
      "PARAM",
      [
        "storage",
        "002a7210",
        null,
        "string"
      ]
    ],
    [
      "00b48b60",
      "WRITE",
      [
        "storage",
        "011268f0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47b64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47b2c.md#insn-00b47b64) · [`00b47b6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47b2c.md#insn-00b47b6c) · [`00b47b38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47b2c.md#insn-00b47b38)
- 新版 [`00b48b58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48b20.md#insn-00b48b58) · [`00b48b60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48b20.md#insn-00b48b60) · [`00b48b2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48b20.md#insn-00b48b2c)

~~~diff
- 00b47b64 ["INT_ADD", "register:40f0:8", ["const:b47b64:8", "const:4:8"]]
- 00b47b64 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48b58 ["INT_ADD", "register:40f0:8", ["const:b48b58:8", "const:4:8"]]
+ 00b48b58 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47b64 bytes 1f4d0494
+ 00b48b58 bytes 164d0494
- 00b47b6c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:930:8"]]
- 00b47b6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48b60 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:8f0:8"]]
+ 00b48b60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47b6c bytes 809a04f9
+ 00b48b60 bytes 807a04f9
- 00b47b38 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b48b2c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b47b38 bytes f42e00d0
+ 00b48b2c bytes f42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7e4e47e381241ae43a2ee89ce5168a27"></a>

### [`00b47b9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47b9c.md) → [`00b48b90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48b90.md) _ZN8firebase4util10array_list10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b48bac",
      "incomplete_value": false,
      "site": "00b48bb0",
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
      "definition_site": "00b47bb8",
      "incomplete_value": false,
      "site": "00b47bbc",
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
      "definition_site": "00b48bbc",
      "incomplete_value": true,
      "site": "00b48bc8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b47bc8",
      "incomplete_value": true,
      "site": "00b47bd4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b48bac",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b48bbc",
      "DATA",
      [
        "storage",
        "01125958",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b48bac",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b48bbc",
      "DATA",
      [
        "storage",
        "01126918",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47bbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47b9c.md#insn-00b47bbc) · [`00b47bb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47b9c.md#insn-00b47bb8) · [`00b47bc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47b9c.md#insn-00b47bc0)
- 新版 [`00b48bb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48b90.md#insn-00b48bb0) · [`00b48bac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48b90.md#insn-00b48bac) · [`00b48bb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48b90.md#insn-00b48bb4)

~~~diff
- 00b47bbc ["INT_ADD", "register:40f0:8", ["const:b47bbc:8", "const:4:8"]]
- 00b47bbc ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b48bb0 ["INT_ADD", "register:40f0:8", ["const:b48bb0:8", "const:4:8"]]
+ 00b48bb0 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b47bbc bytes 454d0494
+ 00b48bb0 bytes 3c4d0494
- 00b47bb8 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b47bb8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47bb8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47bb8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b48bac ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b48bac ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48bac ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48bac ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47bb8 bytes 00341591
+ 00b48bac bytes 00681891
- 00b47bc0 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b48bb4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b47bc0 bytes e82e00d0
+ 00b48bb4 bytes e82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dc8d4fcf6d197440fde72be2d3431931"></a>

### [`00b47bd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47bd8.md) → [`00b48bcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48bcc.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b48bf8",
      "incomplete_value": true,
      "site": "00b48bf8",
      "value": [
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
      "definition_site": "00b47c04",
      "incomplete_value": true,
      "site": "00b47c04",
      "value": [
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
      "definition_site": "00b48be0",
      "incomplete_value": true,
      "site": "00b48be0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47bec",
      "incomplete_value": true,
      "site": "00b47bec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48bec",
      "incomplete_value": false,
      "site": "00b48bf0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47bf8",
      "incomplete_value": false,
      "site": "00b47bfc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:76a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48bdc",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48bec",
      "PARAM",
      [
        "storage",
        "002bf76a",
        null,
        "string"
      ]
    ],
    [
      "00b48bf8",
      "WRITE",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48bdc",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48bec",
      "PARAM",
      [
        "storage",
        "002bf848",
        null,
        "string"
      ]
    ],
    [
      "00b48bf8",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47bfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47bd8.md#insn-00b47bfc) · [`00b47c04`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47bd8.md#insn-00b47c04) · [`00b47be4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47bd8.md#insn-00b47be4)
- 新版 [`00b48bf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48bcc.md#insn-00b48bf0) · [`00b48bf8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48bcc.md#insn-00b48bf8) · [`00b48bd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48bcc.md#insn-00b48bd8)

~~~diff
- 00b47bfc ["INT_ADD", "register:40f0:8", ["const:b47bfc:8", "const:4:8"]]
- 00b47bfc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48bf0 ["INT_ADD", "register:40f0:8", ["const:b48bf0:8", "const:4:8"]]
+ 00b48bf0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47bfc bytes f94c0494
+ 00b48bf0 bytes f04c0494
- 00b47c04 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00b47c04 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48bf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b48bf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47c04 bytes 60b204f9
+ 00b48bf8 bytes 609204f9
- 00b47be4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48bd8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b47be4 bytes f32e00d0
+ 00b48bd8 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f80e5072fc914b8f5fa2c9b65b5eae25"></a>

### [`00b47c18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c18.md) → [`00b48c0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48c0c.md) _ZN8firebase4util21asset_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocat

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
      "definition_site": "00b48c38",
      "incomplete_value": true,
      "site": "00b48c38",
      "value": [
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
      "definition_site": "00b47c44",
      "incomplete_value": true,
      "site": "00b47c44",
      "value": [
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
      "definition_site": "00b48c20",
      "incomplete_value": true,
      "site": "00b48c20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47c2c",
      "incomplete_value": true,
      "site": "00b47c2c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48c28",
      "incomplete_value": false,
      "site": "00b48c30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47c34",
      "incomplete_value": false,
      "site": "00b47c3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:76a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48c1c",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48c28",
      "PARAM",
      [
        "storage",
        "002bf76a",
        null,
        "string"
      ]
    ],
    [
      "00b48c38",
      "WRITE",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48c1c",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48c28",
      "PARAM",
      [
        "storage",
        "002bf848",
        null,
        "string"
      ]
    ],
    [
      "00b48c38",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47c3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c18.md#insn-00b47c3c) · [`00b47c44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c18.md#insn-00b47c44) · [`00b47c24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c18.md#insn-00b47c24)
- 新版 [`00b48c30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48c0c.md#insn-00b48c30) · [`00b48c38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48c0c.md#insn-00b48c38) · [`00b48c18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48c0c.md#insn-00b48c18)

~~~diff
- 00b47c3c ["INT_ADD", "register:40f0:8", ["const:b47c3c:8", "const:4:8"]]
- 00b47c3c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48c30 ["INT_ADD", "register:40f0:8", ["const:b48c30:8", "const:4:8"]]
+ 00b48c30 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47c3c bytes e94c0494
+ 00b48c30 bytes e04c0494
- 00b47c44 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00b47c44 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48c38 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b48c38 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47c44 bytes 60b204f9
+ 00b48c38 bytes 609204f9
- 00b47c24 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48c18 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b47c24 bytes f32e00d0
+ 00b48c18 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bef71e4fcc95e2f11b2410e942a176b7"></a>

### [`00b47c58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c58.md) → [`00b48c4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48c4c.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b48c7c",
      "incomplete_value": true,
      "site": "00b48c7c",
      "value": [
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
      "definition_site": "00b47c88",
      "incomplete_value": true,
      "site": "00b47c88",
      "value": [
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
      "definition_site": "00b48c60",
      "incomplete_value": true,
      "site": "00b48c60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47c6c",
      "incomplete_value": true,
      "site": "00b47c6c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48c6c",
      "incomplete_value": false,
      "site": "00b48c74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47c78",
      "incomplete_value": false,
      "site": "00b47c80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:76a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48c5c",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48c6c",
      "PARAM",
      [
        "storage",
        "002bf76a",
        null,
        "string"
      ]
    ],
    [
      "00b48c7c",
      "WRITE",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48c5c",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48c6c",
      "PARAM",
      [
        "storage",
        "002bf848",
        null,
        "string"
      ]
    ],
    [
      "00b48c7c",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47c80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c58.md#insn-00b47c80) · [`00b47c88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c58.md#insn-00b47c88) · [`00b47c64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c58.md#insn-00b47c64)
- 新版 [`00b48c74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48c4c.md#insn-00b48c74) · [`00b48c7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48c4c.md#insn-00b48c7c) · [`00b48c58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48c4c.md#insn-00b48c58)

~~~diff
- 00b47c80 ["INT_ADD", "register:40f0:8", ["const:b47c80:8", "const:4:8"]]
- 00b47c80 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48c74 ["INT_ADD", "register:40f0:8", ["const:b48c74:8", "const:4:8"]]
+ 00b48c74 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47c80 bytes d84c0494
+ 00b48c74 bytes cf4c0494
- 00b47c88 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00b47c88 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48c7c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b48c7c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47c88 bytes 60b204f9
+ 00b48c7c bytes 609204f9
- 00b47c64 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48c58 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b47c64 bytes f32e00d0
+ 00b48c58 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e7f4cca29c0de5d7665e3c10678e8740"></a>

### [`00b47c9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c9c.md) → [`00b48c90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48c90.md) _ZN8firebase4util21asset_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48cc0",
      "incomplete_value": true,
      "site": "00b48cc0",
      "value": [
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
      "definition_site": "00b47ccc",
      "incomplete_value": true,
      "site": "00b47ccc",
      "value": [
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
      "definition_site": "00b48ca4",
      "incomplete_value": true,
      "site": "00b48ca4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47cb0",
      "incomplete_value": true,
      "site": "00b47cb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48cac",
      "incomplete_value": false,
      "site": "00b48cb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47cb8",
      "incomplete_value": false,
      "site": "00b47cc4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:76a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48ca0",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48cac",
      "PARAM",
      [
        "storage",
        "002bf76a",
        null,
        "string"
      ]
    ],
    [
      "00b48cc0",
      "WRITE",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48ca0",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48cac",
      "PARAM",
      [
        "storage",
        "002bf848",
        null,
        "string"
      ]
    ],
    [
      "00b48cc0",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47cc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c9c.md#insn-00b47cc4) · [`00b47ccc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c9c.md#insn-00b47ccc) · [`00b47ca8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47c9c.md#insn-00b47ca8)
- 新版 [`00b48cb8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48c90.md#insn-00b48cb8) · [`00b48cc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48c90.md#insn-00b48cc0) · [`00b48c9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48c90.md#insn-00b48c9c)

~~~diff
- 00b47cc4 ["INT_ADD", "register:40f0:8", ["const:b47cc4:8", "const:4:8"]]
- 00b47cc4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48cb8 ["INT_ADD", "register:40f0:8", ["const:b48cb8:8", "const:4:8"]]
+ 00b48cb8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47cc4 bytes c74c0494
+ 00b48cb8 bytes be4c0494
- 00b47ccc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:960:8"]]
- 00b47ccc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48cc0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:920:8"]]
+ 00b48cc0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47ccc bytes 60b204f9
+ 00b48cc0 bytes 609204f9
- 00b47ca8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48c9c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b47ca8 bytes f32e00d0
+ 00b48c9c bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bf40b84a1310b45ed11150376d9e3e53"></a>

### [`00b47cec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47cec.md) → [`00b48ce0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ce0.md) _ZN8firebase4util21asset_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b48d68",
      "incomplete_value": true,
      "site": "00b48d68",
      "value": [
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
      "definition_site": "00b47d74",
      "incomplete_value": true,
      "site": "00b47d74",
      "value": [
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
      "definition_site": "00b48d14",
      "incomplete_value": true,
      "site": "00b48d20",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47d20",
      "incomplete_value": true,
      "site": "00b47d2c",
      "value": [
        "LOAD",
        "8",
        [
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
      "00b48cf4",
      "READ",
      [
        "storage",
        "01125968",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48d14",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48d68",
      "WRITE",
      [
        "storage",
        "01125968",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48cf4",
      "READ",
      [
        "storage",
        "01126928",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48d14",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48d68",
      "WRITE",
      [
        "storage",
        "01126928",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47d2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47cec.md#insn-00b47d2c) · [`00b47d74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47cec.md#insn-00b47d74) · [`00b47cfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47cec.md#insn-00b47cfc)
- 新版 [`00b48d20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ce0.md#insn-00b48d20) · [`00b48d68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ce0.md#insn-00b48d68) · [`00b48cf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ce0.md#insn-00b48cf0)

~~~diff
- 00b47d2c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47d2c ["INT_ADD", "register:40f0:8", ["const:b47d2c:8", "const:4:8"]]
- 00b47d2c ["CALLIND", null, ["register:0:8"]]
+ 00b48d20 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48d20 ["INT_ADD", "register:40f0:8", ["const:b48d20:8", "const:4:8"]]
+ 00b48d20 ["CALLIND", null, ["register:0:8"]]
- 00b47d2c bytes 00013fd6
+ 00b48d20 bytes 00013fd6
- 00b47d74 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b47d74 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:968:8"]]
- 00b47d74 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b48d68 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b48d68 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:928:8"]]
+ 00b48d68 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b47d74 bytes a0a22539
+ 00b48d68 bytes a0a22439
- 00b47cfc ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b48cf0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b47cfc bytes f52e00d0
+ 00b48cf0 bytes f52e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-761bfe9f13bb57067bb9b7cef5de156c"></a>

### [`00b47d88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47d88.md) → [`00b48d7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48d7c.md) _ZN8firebase4util21asset_file_descriptor12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b48db8",
      "incomplete_value": true,
      "site": "00b48db8",
      "value": [
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
      "definition_site": "00b47dc4",
      "incomplete_value": true,
      "site": "00b47dc4",
      "value": [
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
      "definition_site": "00b48e08",
      "incomplete_value": true,
      "site": "00b48e08",
      "value": [
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
      "definition_site": "00b47e14",
      "incomplete_value": true,
      "site": "00b47e14",
      "value": [
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
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48df8",
      "incomplete_value": true,
      "site": "00b48e04",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:920:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47e04",
      "incomplete_value": true,
      "site": "00b47e10",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:960:8"
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
      "00b48d90",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48d9c",
      "READ",
      [
        "storage",
        "01125968",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48db8",
      "WRITE",
      [
        "storage",
        "01125968",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b48d90",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48d9c",
      "READ",
      [
        "storage",
        "01126928",
        null,
        "undefined1"
      ]
    ],
    [
      "00b48db8",
      "WRITE",
      [
        "storage",
        "01126928",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47dc4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47d88.md#insn-00b47dc4) · [`00b47e10`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47d88.md#insn-00b47e10) · [`00b47e14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47d88.md#insn-00b47e14)
- 新版 [`00b48db8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48d7c.md#insn-00b48db8) · [`00b48e04`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48d7c.md#insn-00b48e04) · [`00b48e08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48d7c.md#insn-00b48e08)

~~~diff
- 00b47dc4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b47dc4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b47dc4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:968:8"]]
- 00b47dc4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b48db8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b48db8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b48db8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:928:8"]]
+ 00b48db8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b47dc4 bytes bfa22539
+ 00b48db8 bytes bfa22439
- 00b47e10 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b47e10 ["INT_ADD", "register:40f0:8", ["const:b47e10:8", "const:4:8"]]
- 00b47e10 ["CALLIND", null, ["register:0:8"]]
+ 00b48e04 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b48e04 ["INT_ADD", "register:40f0:8", ["const:b48e04:8", "const:4:8"]]
+ 00b48e04 ["CALLIND", null, ["register:0:8"]]
- 00b47e10 bytes 00013fd6
+ 00b48e04 bytes 00013fd6
- 00b47e14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
- 00b47e14 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b47e14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b48e08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00b48e08 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b48e08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b47e14 bytes 9fb204f9
+ 00b48e08 bytes 9f9204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3f9e9b701322711a6049c9c92b18e787"></a>

### [`00b47e28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47e28.md) → [`00b48e1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48e1c.md) _ZN8firebase4util21asset_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48e5c",
      "incomplete_value": true,
      "site": "00b48e5c",
      "value": [
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
      "definition_site": "00b47e68",
      "incomplete_value": true,
      "site": "00b47e68",
      "value": [
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
      "definition_site": "00b48e38",
      "incomplete_value": true,
      "site": "00b48e38",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47e44",
      "incomplete_value": true,
      "site": "00b47e44",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48e40",
      "incomplete_value": false,
      "site": "00b48e54",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47e4c",
      "incomplete_value": false,
      "site": "00b47e60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:76a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48e30",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48e40",
      "PARAM",
      [
        "storage",
        "002bf76a",
        null,
        "string"
      ]
    ],
    [
      "00b48e5c",
      "WRITE",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48e30",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48e40",
      "PARAM",
      [
        "storage",
        "002bf848",
        null,
        "string"
      ]
    ],
    [
      "00b48e5c",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47e60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47e28.md#insn-00b47e60) · [`00b47e68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47e28.md#insn-00b47e68) · [`00b47e34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47e28.md#insn-00b47e34)
- 新版 [`00b48e54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48e1c.md#insn-00b48e54) · [`00b48e5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48e1c.md#insn-00b48e5c) · [`00b48e28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48e1c.md#insn-00b48e28)

~~~diff
- 00b47e60 ["INT_ADD", "register:40f0:8", ["const:b47e60:8", "const:4:8"]]
- 00b47e60 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48e54 ["INT_ADD", "register:40f0:8", ["const:b48e54:8", "const:4:8"]]
+ 00b48e54 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47e60 bytes 604c0494
+ 00b48e54 bytes 574c0494
- 00b47e68 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
- 00b47e68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48e5c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00b48e5c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47e68 bytes 80b204f9
+ 00b48e5c bytes 809204f9
- 00b47e34 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b48e28 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b47e34 bytes f42e00d0
+ 00b48e28 bytes f42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-695c034d2f7ec5e763c77d667e911aaf"></a>

### [`00b47e98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47e98.md) → [`00b48e8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48e8c.md) _ZN8firebase4util21asset_file_descriptor11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b48ea8",
      "incomplete_value": false,
      "site": "00b48eac",
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
      "definition_site": "00b47eb4",
      "incomplete_value": false,
      "site": "00b47eb8",
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
      "definition_site": "00b48eb8",
      "incomplete_value": true,
      "site": "00b48ec4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b47ec4",
      "incomplete_value": true,
      "site": "00b47ed0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b48ea8",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b48eb8",
      "DATA",
      [
        "storage",
        "01125970",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b48ea8",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b48eb8",
      "DATA",
      [
        "storage",
        "01126930",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47eb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47e98.md#insn-00b47eb8) · [`00b47eb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47e98.md#insn-00b47eb4) · [`00b47ebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47e98.md#insn-00b47ebc)
- 新版 [`00b48eac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48e8c.md#insn-00b48eac) · [`00b48ea8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48e8c.md#insn-00b48ea8) · [`00b48eb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48e8c.md#insn-00b48eb0)

~~~diff
- 00b47eb8 ["INT_ADD", "register:40f0:8", ["const:b47eb8:8", "const:4:8"]]
- 00b47eb8 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b48eac ["INT_ADD", "register:40f0:8", ["const:b48eac:8", "const:4:8"]]
+ 00b48eac ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b47eb8 bytes 864c0494
+ 00b48eac bytes 7d4c0494
- 00b47eb4 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b47eb4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47eb4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47eb4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b48ea8 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b48ea8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48ea8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48ea8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47eb4 bytes 002c0c91
+ 00b48ea8 bytes 008c1191
- 00b47ebc ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b48eb0 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b47ebc bytes e82e00d0
+ 00b48eb0 bytes e82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-507107e726df47ff4e017c4dd9b60303"></a>

### [`00b47ed4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47ed4.md) → [`00b48ec8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ec8.md) _ZN8firebase4util21asset_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b48f08",
      "incomplete_value": true,
      "site": "00b48f08",
      "value": [
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
      "definition_site": "00b47f14",
      "incomplete_value": true,
      "site": "00b47f14",
      "value": [
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
      "definition_site": "00b48ee4",
      "incomplete_value": true,
      "site": "00b48ee4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47ef0",
      "incomplete_value": true,
      "site": "00b47ef0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48eec",
      "incomplete_value": false,
      "site": "00b48f00",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:848:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47ef8",
      "incomplete_value": false,
      "site": "00b47f0c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2bf000:8"
          ],
          [
            "leaf",
            "const:76a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48edc",
      "READ",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48eec",
      "PARAM",
      [
        "storage",
        "002bf76a",
        null,
        "string"
      ]
    ],
    [
      "00b48f08",
      "WRITE",
      [
        "storage",
        "01125960",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48edc",
      "READ",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48eec",
      "PARAM",
      [
        "storage",
        "002bf848",
        null,
        "string"
      ]
    ],
    [
      "00b48f08",
      "WRITE",
      [
        "storage",
        "01126920",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47f0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47ed4.md#insn-00b47f0c) · [`00b47f14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47ed4.md#insn-00b47f14) · [`00b47ee0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47ed4.md#insn-00b47ee0)
- 新版 [`00b48f00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ec8.md#insn-00b48f00) · [`00b48f08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ec8.md#insn-00b48f08) · [`00b48ed4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ec8.md#insn-00b48ed4)

~~~diff
- 00b47f0c ["INT_ADD", "register:40f0:8", ["const:b47f0c:8", "const:4:8"]]
- 00b47f0c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48f00 ["INT_ADD", "register:40f0:8", ["const:b48f00:8", "const:4:8"]]
+ 00b48f00 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47f0c bytes 354c0494
+ 00b48f00 bytes 2c4c0494
- 00b47f14 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:960:8"]]
- 00b47f14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48f08 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:920:8"]]
+ 00b48f08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47f14 bytes 80b204f9
+ 00b48f08 bytes 809204f9
- 00b47ee0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b48ed4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b47ee0 bytes f42e00d0
+ 00b48ed4 bytes f42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c3555d9be44c253827a34c6411b8255a"></a>

### [`00b47f44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47f44.md) → [`00b48f38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48f38.md) _ZN8firebase4util21asset_file_descriptor10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b48f54",
      "incomplete_value": false,
      "site": "00b48f58",
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
      "definition_site": "00b47f60",
      "incomplete_value": false,
      "site": "00b47f64",
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
      "definition_site": "00b48f64",
      "incomplete_value": true,
      "site": "00b48f70",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b47f70",
      "incomplete_value": true,
      "site": "00b47f7c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b48f54",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b48f64",
      "DATA",
      [
        "storage",
        "01125978",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b48f54",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b48f64",
      "DATA",
      [
        "storage",
        "01126938",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47f64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47f44.md#insn-00b47f64) · [`00b47f60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47f44.md#insn-00b47f60) · [`00b47f68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47f44.md#insn-00b47f68)
- 新版 [`00b48f58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48f38.md#insn-00b48f58) · [`00b48f54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48f38.md#insn-00b48f54) · [`00b48f5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48f38.md#insn-00b48f5c)

~~~diff
- 00b47f64 ["INT_ADD", "register:40f0:8", ["const:b47f64:8", "const:4:8"]]
- 00b47f64 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b48f58 ["INT_ADD", "register:40f0:8", ["const:b48f58:8", "const:4:8"]]
+ 00b48f58 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b47f64 bytes 5b4c0494
+ 00b48f58 bytes 524c0494
- 00b47f60 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b47f60 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b47f60 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b47f60 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b48f54 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b48f54 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48f54 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b48f54 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b47f60 bytes 00341591
+ 00b48f54 bytes 00681891
- 00b47f68 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b48f5c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b47f68 bytes e82e00d0
+ 00b48f5c bytes e82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c82fb58be67f1581a82fea6497ee467"></a>

### [`00b47f80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47f80.md) → [`00b48f74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48f74.md) _ZN8firebase4util13boolean_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00b48fa0",
      "incomplete_value": true,
      "site": "00b48fa0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47fac",
      "incomplete_value": true,
      "site": "00b47fac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48f88",
      "incomplete_value": true,
      "site": "00b48f88",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47f94",
      "incomplete_value": true,
      "site": "00b47f94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48f94",
      "incomplete_value": false,
      "site": "00b48f98",
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
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47fa0",
      "incomplete_value": false,
      "site": "00b47fa4",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48f84",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48f94",
      "PARAM",
      [
        "storage",
        "002a83a0",
        null,
        "string"
      ]
    ],
    [
      "00b48fa0",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48f84",
      "READ",
      [
        "storage",
        "01126940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48f94",
      "PARAM",
      [
        "storage",
        "002a84f8",
        null,
        "string"
      ]
    ],
    [
      "00b48fa0",
      "WRITE",
      [
        "storage",
        "01126940",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47fa4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47f80.md#insn-00b47fa4) · [`00b47fac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47f80.md#insn-00b47fac) · [`00b47f8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47f80.md#insn-00b47f8c)
- 新版 [`00b48f98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48f74.md#insn-00b48f98) · [`00b48fa0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48f74.md#insn-00b48fa0) · [`00b48f80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48f74.md#insn-00b48f80)

~~~diff
- 00b47fa4 ["INT_ADD", "register:40f0:8", ["const:b47fa4:8", "const:4:8"]]
- 00b47fa4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48f98 ["INT_ADD", "register:40f0:8", ["const:b48f98:8", "const:4:8"]]
+ 00b48f98 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47fa4 bytes 0f4c0494
+ 00b48f98 bytes 064c0494
- 00b47fac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
- 00b47fac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48fa0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
+ 00b48fa0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47fac bytes 60c204f9
+ 00b48fa0 bytes 60a204f9
- 00b47f8c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48f80 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b47f8c bytes f32e00d0
+ 00b48f80 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cf331f0b30acb59ee672b0a2fec87447"></a>

### [`00b47fc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47fc0.md) → [`00b48fb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48fb4.md) _ZN8firebase4util13boolean_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00b48fe0",
      "incomplete_value": true,
      "site": "00b48fe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47fec",
      "incomplete_value": true,
      "site": "00b47fec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b48fc8",
      "incomplete_value": true,
      "site": "00b48fc8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47fd4",
      "incomplete_value": true,
      "site": "00b47fd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b48fd0",
      "incomplete_value": false,
      "site": "00b48fd8",
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
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b47fdc",
      "incomplete_value": false,
      "site": "00b47fe4",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b48fc4",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48fd0",
      "PARAM",
      [
        "storage",
        "002a83a0",
        null,
        "string"
      ]
    ],
    [
      "00b48fe0",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b48fc4",
      "READ",
      [
        "storage",
        "01126940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b48fd0",
      "PARAM",
      [
        "storage",
        "002a84f8",
        null,
        "string"
      ]
    ],
    [
      "00b48fe0",
      "WRITE",
      [
        "storage",
        "01126940",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b47fe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47fc0.md#insn-00b47fe4) · [`00b47fec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47fc0.md#insn-00b47fec) · [`00b47fcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b47/00b47fc0.md#insn-00b47fcc)
- 新版 [`00b48fd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48fb4.md#insn-00b48fd8) · [`00b48fe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48fb4.md#insn-00b48fe0) · [`00b48fc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48fb4.md#insn-00b48fc0)

~~~diff
- 00b47fe4 ["INT_ADD", "register:40f0:8", ["const:b47fe4:8", "const:4:8"]]
- 00b47fe4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b48fd8 ["INT_ADD", "register:40f0:8", ["const:b48fd8:8", "const:4:8"]]
+ 00b48fd8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b47fe4 bytes ff4b0494
+ 00b48fd8 bytes f64b0494
- 00b47fec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
- 00b47fec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b48fe0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
+ 00b48fe0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b47fec bytes 60c204f9
+ 00b48fe0 bytes 60a204f9
- 00b47fcc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b48fc0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b47fcc bytes f32e00d0
+ 00b48fc0 bytes f32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-07c322b6ac2a5c60cb0999d628dccb6c"></a>

### [`00b48000`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48000.md) → [`00b48ff4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ff4.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b49024",
      "incomplete_value": true,
      "site": "00b49024",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48030",
      "incomplete_value": true,
      "site": "00b48030",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b49008",
      "incomplete_value": true,
      "site": "00b49008",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48014",
      "incomplete_value": true,
      "site": "00b48014",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49014",
      "incomplete_value": false,
      "site": "00b4901c",
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
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48020",
      "incomplete_value": false,
      "site": "00b48028",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49004",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49014",
      "PARAM",
      [
        "storage",
        "002a83a0",
        null,
        "string"
      ]
    ],
    [
      "00b49024",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49004",
      "READ",
      [
        "storage",
        "01126940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49014",
      "PARAM",
      [
        "storage",
        "002a84f8",
        null,
        "string"
      ]
    ],
    [
      "00b49024",
      "WRITE",
      [
        "storage",
        "01126940",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48028`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48000.md#insn-00b48028) · [`00b48030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48000.md#insn-00b48030) · [`00b4800c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48000.md#insn-00b4800c)
- 新版 [`00b4901c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ff4.md#insn-00b4901c) · [`00b49024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ff4.md#insn-00b49024) · [`00b49000`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b48/00b48ff4.md#insn-00b49000)

~~~diff
- 00b48028 ["INT_ADD", "register:40f0:8", ["const:b48028:8", "const:4:8"]]
- 00b48028 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4901c ["INT_ADD", "register:40f0:8", ["const:b4901c:8", "const:4:8"]]
+ 00b4901c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48028 bytes ee4b0494
+ 00b4901c bytes e54b0494
- 00b48030 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
- 00b48030 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49024 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
+ 00b49024 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48030 bytes 60c204f9
+ 00b49024 bytes 60a204f9
- 00b4800c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49000 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4800c bytes f32e00b0
+ 00b49000 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-141a99a16c5c1bb2bc06d027eec5bac1"></a>

### [`00b48044`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48044.md) → [`00b49038`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49038.md) _ZN8firebase4util13boolean_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b49068",
      "incomplete_value": true,
      "site": "00b49068",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48074",
      "incomplete_value": true,
      "site": "00b48074",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:980:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4904c",
      "incomplete_value": true,
      "site": "00b4904c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48058",
      "incomplete_value": true,
      "site": "00b48058",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49054",
      "incomplete_value": false,
      "site": "00b49060",
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
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48060",
      "incomplete_value": false,
      "site": "00b4806c",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49048",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49054",
      "PARAM",
      [
        "storage",
        "002a83a0",
        null,
        "string"
      ]
    ],
    [
      "00b49068",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49048",
      "READ",
      [
        "storage",
        "01126940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49054",
      "PARAM",
      [
        "storage",
        "002a84f8",
        null,
        "string"
      ]
    ],
    [
      "00b49068",
      "WRITE",
      [
        "storage",
        "01126940",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4806c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48044.md#insn-00b4806c) · [`00b48074`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48044.md#insn-00b48074) · [`00b48050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48044.md#insn-00b48050)
- 新版 [`00b49060`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49038.md#insn-00b49060) · [`00b49068`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49038.md#insn-00b49068) · [`00b49044`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49038.md#insn-00b49044)

~~~diff
- 00b4806c ["INT_ADD", "register:40f0:8", ["const:b4806c:8", "const:4:8"]]
- 00b4806c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b49060 ["INT_ADD", "register:40f0:8", ["const:b49060:8", "const:4:8"]]
+ 00b49060 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4806c bytes dd4b0494
+ 00b49060 bytes d44b0494
- 00b48074 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:980:8"]]
- 00b48074 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49068 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:940:8"]]
+ 00b49068 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48074 bytes 60c204f9
+ 00b49068 bytes 60a204f9
- 00b48050 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49044 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b48050 bytes f32e00b0
+ 00b49044 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-87fe23b52cf01aa7e5698478caa9d3c4"></a>

### [`00b48094`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48094.md) → [`00b49088`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49088.md) _ZN8firebase4util13boolean_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b49110",
      "incomplete_value": true,
      "site": "00b49110",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4811c",
      "incomplete_value": true,
      "site": "00b4811c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:988:8"
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
      "definition_site": "00b490bc",
      "incomplete_value": true,
      "site": "00b490c8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:940:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b480c8",
      "incomplete_value": true,
      "site": "00b480d4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:980:8"
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
      "00b4909c",
      "READ",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ],
    [
      "00b490bc",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49110",
      "WRITE",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4909c",
      "READ",
      [
        "storage",
        "01126948",
        null,
        "undefined1"
      ]
    ],
    [
      "00b490bc",
      "READ",
      [
        "storage",
        "01126940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49110",
      "WRITE",
      [
        "storage",
        "01126948",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b480d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48094.md#insn-00b480d4) · [`00b4811c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48094.md#insn-00b4811c) · [`00b480a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48094.md#insn-00b480a4)
- 新版 [`00b490c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49088.md#insn-00b490c8) · [`00b49110`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49088.md#insn-00b49110) · [`00b49098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49088.md#insn-00b49098)

~~~diff
- 00b480d4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b480d4 ["INT_ADD", "register:40f0:8", ["const:b480d4:8", "const:4:8"]]
- 00b480d4 ["CALLIND", null, ["register:0:8"]]
+ 00b490c8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b490c8 ["INT_ADD", "register:40f0:8", ["const:b490c8:8", "const:4:8"]]
+ 00b490c8 ["CALLIND", null, ["register:0:8"]]
- 00b480d4 bytes 00013fd6
+ 00b490c8 bytes 00013fd6
- 00b4811c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4811c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:988:8"]]
- 00b4811c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b49110 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b49110 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:948:8"]]
+ 00b49110 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4811c bytes a0222639
+ 00b49110 bytes a0222539
- 00b480a4 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b49098 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b480a4 bytes f52e00b0
+ 00b49098 bytes f52e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-610d608a0fa1bfa3092c37b27ef09ebf"></a>

### [`00b48130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48130.md) → [`00b49124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49124.md) _ZN8firebase4util13boolean_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b49160",
      "incomplete_value": true,
      "site": "00b49160",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:948:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4816c",
      "incomplete_value": true,
      "site": "00b4816c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:988:8"
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
      "definition_site": "00b491b0",
      "incomplete_value": true,
      "site": "00b491b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b481bc",
      "incomplete_value": true,
      "site": "00b481bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "definition_site": "00b4913c",
      "incomplete_value": true,
      "site": "00b4913c",
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
      "definition_site": "00b48148",
      "incomplete_value": true,
      "site": "00b48148",
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
      "00b49138",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49144",
      "READ",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49160",
      "WRITE",
      [
        "storage",
        "01125988",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49138",
      "READ",
      [
        "storage",
        "01126940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49144",
      "READ",
      [
        "storage",
        "01126948",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49160",
      "WRITE",
      [
        "storage",
        "01126948",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4816c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48130.md#insn-00b4816c) · [`00b481b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48130.md#insn-00b481b8) · [`00b481bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48130.md#insn-00b481bc)
- 新版 [`00b49160`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49124.md#insn-00b49160) · [`00b491ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49124.md#insn-00b491ac) · [`00b491b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49124.md#insn-00b491b0)

~~~diff
- 00b4816c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4816c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4816c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:988:8"]]
- 00b4816c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b49160 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b49160 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b49160 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:948:8"]]
+ 00b49160 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4816c bytes bf222639
+ 00b49160 bytes bf222539
- 00b481b8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b481b8 ["INT_ADD", "register:40f0:8", ["const:b481b8:8", "const:4:8"]]
- 00b481b8 ["CALLIND", null, ["register:0:8"]]
+ 00b491ac ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b491ac ["INT_ADD", "register:40f0:8", ["const:b491ac:8", "const:4:8"]]
+ 00b491ac ["CALLIND", null, ["register:0:8"]]
- 00b481b8 bytes 00013fd6
+ 00b491ac bytes 00013fd6
- 00b481bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
- 00b481bc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b481bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b491b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:940:8"]]
+ 00b491b0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b491b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b481bc bytes 9fc204f9
+ 00b491b0 bytes 9fa204f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12724be6433ddb496461409c589caf4c"></a>

### [`00b481d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b481d0.md) → [`00b491c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b491c4.md) _ZN8firebase4util13boolean_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b49204",
      "incomplete_value": true,
      "site": "00b49204",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48210",
      "incomplete_value": true,
      "site": "00b48210",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "definition_site": "00b491e0",
      "incomplete_value": true,
      "site": "00b491e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b481ec",
      "incomplete_value": true,
      "site": "00b481ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b491e8",
      "incomplete_value": false,
      "site": "00b491fc",
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
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b481f4",
      "incomplete_value": false,
      "site": "00b48208",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b491d8",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b491e8",
      "PARAM",
      [
        "storage",
        "002a83a0",
        null,
        "string"
      ]
    ],
    [
      "00b49204",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b491d8",
      "READ",
      [
        "storage",
        "01126940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b491e8",
      "PARAM",
      [
        "storage",
        "002a84f8",
        null,
        "string"
      ]
    ],
    [
      "00b49204",
      "WRITE",
      [
        "storage",
        "01126940",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48208`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b481d0.md#insn-00b48208) · [`00b48210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b481d0.md#insn-00b48210) · [`00b481dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b481d0.md#insn-00b481dc)
- 新版 [`00b491fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b491c4.md#insn-00b491fc) · [`00b49204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b491c4.md#insn-00b49204) · [`00b491d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b491c4.md#insn-00b491d0)

~~~diff
- 00b48208 ["INT_ADD", "register:40f0:8", ["const:b48208:8", "const:4:8"]]
- 00b48208 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b491fc ["INT_ADD", "register:40f0:8", ["const:b491fc:8", "const:4:8"]]
+ 00b491fc ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48208 bytes 764b0494
+ 00b491fc bytes 6d4b0494
- 00b48210 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
- 00b48210 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49204 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:940:8"]]
+ 00b49204 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48210 bytes 80c204f9
+ 00b49204 bytes 80a204f9
- 00b481dc ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b491d0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b481dc bytes f42e00b0
+ 00b491d0 bytes f42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-25fdc1c262d66e3110084b809eb4d989"></a>

### [`00b48240`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48240.md) → [`00b49234`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49234.md) _ZN8firebase4util13boolean_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b390`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b390.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5c360`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c360.md) · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b49250",
      "incomplete_value": false,
      "site": "00b49254",
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
      "definition_site": "00b4825c",
      "incomplete_value": false,
      "site": "00b48260",
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
      "definition_site": "00b49260",
      "incomplete_value": true,
      "site": "00b4926c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4826c",
      "incomplete_value": true,
      "site": "00b48278",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b49250",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b49260",
      "DATA",
      [
        "storage",
        "01125990",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49250",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b49260",
      "DATA",
      [
        "storage",
        "01126950",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48260`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48240.md#insn-00b48260) · [`00b4825c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48240.md#insn-00b4825c) · [`00b48264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48240.md#insn-00b48264)
- 新版 [`00b49254`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49234.md#insn-00b49254) · [`00b49250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49234.md#insn-00b49250) · [`00b49258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49234.md#insn-00b49258)

~~~diff
- 00b48260 ["INT_ADD", "register:40f0:8", ["const:b48260:8", "const:4:8"]]
- 00b48260 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b49254 ["INT_ADD", "register:40f0:8", ["const:b49254:8", "const:4:8"]]
+ 00b49254 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b48260 bytes 9c4b0494
+ 00b49254 bytes 934b0494
- 00b4825c ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4825c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4825c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4825c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b49250 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b49250 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49250 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b49250 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4825c bytes 002c0c91
+ 00b49250 bytes 008c1191
- 00b48264 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b49258 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b48264 bytes e82e00b0
+ 00b49258 bytes e82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c03b68c27245ab9c074e418c2c1b057a"></a>

### [`00b4827c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b4827c.md) → [`00b49270`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49270.md) _ZN8firebase4util13boolean_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b492b0",
      "incomplete_value": true,
      "site": "00b492b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:940:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b482bc",
      "incomplete_value": true,
      "site": "00b482bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:980:8"
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
      "definition_site": "00b4928c",
      "incomplete_value": true,
      "site": "00b4928c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48298",
      "incomplete_value": true,
      "site": "00b48298",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49294",
      "incomplete_value": false,
      "site": "00b492a8",
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
            "const:4f8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b482a0",
      "incomplete_value": false,
      "site": "00b482b4",
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
            "const:3a0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49284",
      "READ",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49294",
      "PARAM",
      [
        "storage",
        "002a83a0",
        null,
        "string"
      ]
    ],
    [
      "00b492b0",
      "WRITE",
      [
        "storage",
        "01125980",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49284",
      "READ",
      [
        "storage",
        "01126940",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49294",
      "PARAM",
      [
        "storage",
        "002a84f8",
        null,
        "string"
      ]
    ],
    [
      "00b492b0",
      "WRITE",
      [
        "storage",
        "01126940",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b482b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b4827c.md#insn-00b482b4) · [`00b482bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b4827c.md#insn-00b482bc) · [`00b48288`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b4827c.md#insn-00b48288)
- 新版 [`00b492a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49270.md#insn-00b492a8) · [`00b492b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49270.md#insn-00b492b0) · [`00b4927c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49270.md#insn-00b4927c)

~~~diff
- 00b482b4 ["INT_ADD", "register:40f0:8", ["const:b482b4:8", "const:4:8"]]
- 00b482b4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b492a8 ["INT_ADD", "register:40f0:8", ["const:b492a8:8", "const:4:8"]]
+ 00b492a8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b482b4 bytes 4b4b0494
+ 00b492a8 bytes 424b0494
- 00b482bc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:980:8"]]
- 00b482bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b492b0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:940:8"]]
+ 00b492b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b482bc bytes 80c204f9
+ 00b492b0 bytes 80a204f9
- 00b48288 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4927c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b48288 bytes f42e00b0
+ 00b4927c bytes f42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d030f36c441c9b6dd0ca8702e659495b"></a>

### [`00b482ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b482ec.md) → [`00b492e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b492e0.md) _ZN8firebase4util13boolean_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b492fc",
      "incomplete_value": false,
      "site": "00b49300",
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
      "definition_site": "00b48308",
      "incomplete_value": false,
      "site": "00b4830c",
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
      "definition_site": "00b4930c",
      "incomplete_value": true,
      "site": "00b49318",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b48318",
      "incomplete_value": true,
      "site": "00b48324",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b492fc",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4930c",
      "DATA",
      [
        "storage",
        "011259a0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b492fc",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4930c",
      "DATA",
      [
        "storage",
        "01126960",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4830c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b482ec.md#insn-00b4830c) · [`00b48308`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b482ec.md#insn-00b48308) · [`00b48310`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b482ec.md#insn-00b48310)
- 新版 [`00b49300`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b492e0.md#insn-00b49300) · [`00b492fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b492e0.md#insn-00b492fc) · [`00b49304`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b492e0.md#insn-00b49304)

~~~diff
- 00b4830c ["INT_ADD", "register:40f0:8", ["const:b4830c:8", "const:4:8"]]
- 00b4830c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b49300 ["INT_ADD", "register:40f0:8", ["const:b49300:8", "const:4:8"]]
+ 00b49300 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4830c bytes 714b0494
+ 00b49300 bytes 684b0494
- 00b48308 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b48308 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b48308 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b48308 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b492fc ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b492fc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b492fc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b492fc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b48308 bytes 00341591
+ 00b492fc bytes 00681891
- 00b48310 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b49304 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b48310 bytes e82e00b0
+ 00b49304 bytes e82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a8ced8c8abaf369fc4124e7d217501cc"></a>

### [`00b48328`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48328.md) → [`00b4931c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4931c.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
      "definition_site": "00b49348",
      "incomplete_value": true,
      "site": "00b49348",
      "value": [
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
      "definition_site": "00b48354",
      "incomplete_value": true,
      "site": "00b48354",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b49330",
      "incomplete_value": true,
      "site": "00b49330",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4833c",
      "incomplete_value": true,
      "site": "00b4833c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4933c",
      "incomplete_value": false,
      "site": "00b49340",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:a25:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48348",
      "incomplete_value": false,
      "site": "00b4834c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:947:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4932c",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4933c",
      "PARAM",
      [
        "storage",
        "002b9947",
        null,
        "string"
      ]
    ],
    [
      "00b49348",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4932c",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4933c",
      "PARAM",
      [
        "storage",
        "002b9a25",
        null,
        "string"
      ]
    ],
    [
      "00b49348",
      "WRITE",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4834c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48328.md#insn-00b4834c) · [`00b48354`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48328.md#insn-00b48354) · [`00b48334`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48328.md#insn-00b48334)
- 新版 [`00b49340`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4931c.md#insn-00b49340) · [`00b49348`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4931c.md#insn-00b49348) · [`00b49328`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4931c.md#insn-00b49328)

~~~diff
- 00b4834c ["INT_ADD", "register:40f0:8", ["const:b4834c:8", "const:4:8"]]
- 00b4834c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b49340 ["INT_ADD", "register:40f0:8", ["const:b49340:8", "const:4:8"]]
+ 00b49340 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4834c bytes 254b0494
+ 00b49340 bytes 1c4b0494
- 00b48354 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b48354 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49348 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00b49348 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48354 bytes 60d604f9
+ 00b49348 bytes 60b604f9
- 00b48334 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49328 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b48334 bytes f32e00b0
+ 00b49328 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-bb3be0789df8b46029c5291d693ccd1b"></a>

### [`00b48368`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48368.md) → [`00b4935c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4935c.md) _ZN8firebase4util6bundle19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 branch_value, constant, operands_and_dependencies, store_condition, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

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
      "definition_site": "00b49388",
      "incomplete_value": true,
      "site": "00b49388",
      "value": [
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
      "definition_site": "00b48394",
      "incomplete_value": true,
      "site": "00b48394",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b49370",
      "incomplete_value": true,
      "site": "00b49370",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4837c",
      "incomplete_value": true,
      "site": "00b4837c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b4837c"
      ],
      [
        "FALL_THROUGH",
        "00b49370"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b49370",
      "incomplete_value": true,
      "site": "00b49388",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4837c",
      "incomplete_value": true,
      "site": "00b48394",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b4936c",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49378",
      "PARAM",
      [
        "storage",
        "002b9947",
        null,
        "string"
      ]
    ],
    [
      "00b49388",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4936c",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49378",
      "PARAM",
      [
        "storage",
        "002b9a25",
        null,
        "string"
      ]
    ],
    [
      "00b49388",
      "WRITE",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48394`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48368.md#insn-00b48394) · [`00b48374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48368.md#insn-00b48374) · [`00b48378`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48368.md#insn-00b48378)
- 新版 [`00b49388`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4935c.md#insn-00b49388) · [`00b49368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4935c.md#insn-00b49368) · [`00b4936c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4935c.md#insn-00b4936c)

~~~diff
- 00b48394 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b48394 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49388 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00b49388 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48394 bytes 60d604f9
+ 00b49388 bytes 60b604f9
- 00b48374 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49368 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b48374 bytes f32e00b0
+ 00b49368 bytes f32e00b0
- 00b48378 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b48378 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4936c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00b4936c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b48378 bytes 68d644f9
+ 00b4936c bytes 68b644f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-68fd4f16e5c9609c3ccdc4aede8aa46c"></a>

### [`00b483a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b483a8.md) → [`00b4939c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4939c.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b493cc",
      "incomplete_value": true,
      "site": "00b493cc",
      "value": [
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
      "definition_site": "00b483d8",
      "incomplete_value": true,
      "site": "00b483d8",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b493b0",
      "incomplete_value": true,
      "site": "00b493b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b483bc",
      "incomplete_value": true,
      "site": "00b483bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b493bc",
      "incomplete_value": false,
      "site": "00b493c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:a25:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b483c8",
      "incomplete_value": false,
      "site": "00b483d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:947:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b493ac",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b493bc",
      "PARAM",
      [
        "storage",
        "002b9947",
        null,
        "string"
      ]
    ],
    [
      "00b493cc",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b493ac",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b493bc",
      "PARAM",
      [
        "storage",
        "002b9a25",
        null,
        "string"
      ]
    ],
    [
      "00b493cc",
      "WRITE",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b483d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b483a8.md#insn-00b483d0) · [`00b483d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b483a8.md#insn-00b483d8) · [`00b483b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b483a8.md#insn-00b483b4)
- 新版 [`00b493c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4939c.md#insn-00b493c4) · [`00b493cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4939c.md#insn-00b493cc) · [`00b493a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4939c.md#insn-00b493a8)

~~~diff
- 00b483d0 ["INT_ADD", "register:40f0:8", ["const:b483d0:8", "const:4:8"]]
- 00b483d0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b493c4 ["INT_ADD", "register:40f0:8", ["const:b493c4:8", "const:4:8"]]
+ 00b493c4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b483d0 bytes 044b0494
+ 00b493c4 bytes fb4a0494
- 00b483d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b483d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b493cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00b493cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b483d8 bytes 60d604f9
+ 00b493cc bytes 60b604f9
- 00b483b4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b493a8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b483b4 bytes f32e00b0
+ 00b493a8 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-83bb79b4334b5bd7f10c233531e00b3c"></a>

### [`00b483ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b483ec.md) → [`00b493e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b493e0.md) _ZN8firebase4util6bundle10CacheClassEP7_JNIEnvP8_jobject

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b49410",
      "incomplete_value": true,
      "site": "00b49410",
      "value": [
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
      "definition_site": "00b4841c",
      "incomplete_value": true,
      "site": "00b4841c",
      "value": [
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
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b493f4",
      "incomplete_value": true,
      "site": "00b493f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48400",
      "incomplete_value": true,
      "site": "00b48400",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b493fc",
      "incomplete_value": false,
      "site": "00b49408",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:a25:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48408",
      "incomplete_value": false,
      "site": "00b48414",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:947:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b493f0",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b493fc",
      "PARAM",
      [
        "storage",
        "002b9947",
        null,
        "string"
      ]
    ],
    [
      "00b49410",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b493f0",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b493fc",
      "PARAM",
      [
        "storage",
        "002b9a25",
        null,
        "string"
      ]
    ],
    [
      "00b49410",
      "WRITE",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48414`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b483ec.md#insn-00b48414) · [`00b4841c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b483ec.md#insn-00b4841c) · [`00b483f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b483ec.md#insn-00b483f8)
- 新版 [`00b49408`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b493e0.md#insn-00b49408) · [`00b49410`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b493e0.md#insn-00b49410) · [`00b493ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b493e0.md#insn-00b493ec)

~~~diff
- 00b48414 ["INT_ADD", "register:40f0:8", ["const:b48414:8", "const:4:8"]]
- 00b48414 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b49408 ["INT_ADD", "register:40f0:8", ["const:b49408:8", "const:4:8"]]
+ 00b49408 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48414 bytes f34a0494
+ 00b49408 bytes ea4a0494
- 00b4841c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9a8:8"]]
- 00b4841c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49410 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:968:8"]]
+ 00b49410 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4841c bytes 60d604f9
+ 00b49410 bytes 60b604f9
- 00b483f8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b493ec ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b483f8 bytes f32e00b0
+ 00b493ec bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa8cb4d4aa4bca4acc1c3cf86f6cef09"></a>

### [`00b4843c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b4843c.md) → [`00b49430`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49430.md) _ZN8firebase4util6bundle15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b494b8",
      "incomplete_value": true,
      "site": "00b494b8",
      "value": [
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
      "definition_site": "00b484c4",
      "incomplete_value": true,
      "site": "00b484c4",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49464",
      "incomplete_value": true,
      "site": "00b49470",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:968:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48470",
      "incomplete_value": true,
      "site": "00b4847c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9a8:8"
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
      "00b49444",
      "READ",
      [
        "storage",
        "011259b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49464",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b494b8",
      "WRITE",
      [
        "storage",
        "011259b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49444",
      "READ",
      [
        "storage",
        "01126970",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49464",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b494b8",
      "WRITE",
      [
        "storage",
        "01126970",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4847c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b4843c.md#insn-00b4847c) · [`00b484c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b4843c.md#insn-00b484c4) · [`00b4844c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b4843c.md#insn-00b4844c)
- 新版 [`00b49470`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49430.md#insn-00b49470) · [`00b494b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49430.md#insn-00b494b8) · [`00b49440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49430.md#insn-00b49440)

~~~diff
- 00b4847c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4847c ["INT_ADD", "register:40f0:8", ["const:b4847c:8", "const:4:8"]]
- 00b4847c ["CALLIND", null, ["register:0:8"]]
+ 00b49470 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49470 ["INT_ADD", "register:40f0:8", ["const:b49470:8", "const:4:8"]]
+ 00b49470 ["CALLIND", null, ["register:0:8"]]
- 00b4847c bytes 00013fd6
+ 00b49470 bytes 00013fd6
- 00b484c4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b484c4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9b0:8"]]
- 00b484c4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b494b8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b494b8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:970:8"]]
+ 00b494b8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b484c4 bytes a0c22639
+ 00b494b8 bytes a0c22539
- 00b4844c ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b49440 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4844c bytes f52e00b0
+ 00b49440 bytes f52e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a2bff687aa8a786cb4da7172e879a3a1"></a>

### [`00b484d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b484d8.md) → [`00b494cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b494cc.md) _ZN8firebase4util6bundle12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b49508",
      "incomplete_value": true,
      "site": "00b49508",
      "value": [
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
      "definition_site": "00b48514",
      "incomplete_value": true,
      "site": "00b48514",
      "value": [
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
    "ordinal": 5,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b49558",
      "incomplete_value": true,
      "site": "00b49558",
      "value": [
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
    "old": {
      "definition_site": "00b48564",
      "incomplete_value": true,
      "site": "00b48564",
      "value": [
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
    "kind": "branch_value",
    "new": {
      "definition_site": "00b494e4",
      "incomplete_value": true,
      "site": "00b494e4",
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
      "definition_site": "00b484f0",
      "incomplete_value": true,
      "site": "00b484f0",
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
      "00b494e0",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b494ec",
      "READ",
      [
        "storage",
        "011259b0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49508",
      "WRITE",
      [
        "storage",
        "011259b0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b494e0",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b494ec",
      "READ",
      [
        "storage",
        "01126970",
        null,
        "undefined1"
      ]
    ],
    [
      "00b49508",
      "WRITE",
      [
        "storage",
        "01126970",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48514`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b484d8.md#insn-00b48514) · [`00b48560`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b484d8.md#insn-00b48560) · [`00b48564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b484d8.md#insn-00b48564)
- 新版 [`00b49508`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b494cc.md#insn-00b49508) · [`00b49554`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b494cc.md#insn-00b49554) · [`00b49558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b494cc.md#insn-00b49558)

~~~diff
- 00b48514 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b48514 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b48514 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9b0:8"]]
- 00b48514 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b49508 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b49508 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b49508 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:970:8"]]
+ 00b49508 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b48514 bytes bfc22639
+ 00b49508 bytes bfc22539
- 00b48560 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48560 ["INT_ADD", "register:40f0:8", ["const:b48560:8", "const:4:8"]]
- 00b48560 ["CALLIND", null, ["register:0:8"]]
+ 00b49554 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49554 ["INT_ADD", "register:40f0:8", ["const:b49554:8", "const:4:8"]]
+ 00b49554 ["CALLIND", null, ["register:0:8"]]
- 00b48560 bytes 00013fd6
+ 00b49554 bytes 00013fd6
- 00b48564 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00b48564 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b48564 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b49558 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
+ 00b49558 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b49558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b48564 bytes 9fd604f9
+ 00b49558 bytes 9fb604f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9fb046757eb7a480336a915dd6a47f14"></a>

### [`00b48578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48578.md) → [`00b4956c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4956c.md) _ZN8firebase4util6bundle14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b495ac",
      "incomplete_value": true,
      "site": "00b495ac",
      "value": [
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
    "old": {
      "definition_site": "00b485b8",
      "incomplete_value": true,
      "site": "00b485b8",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b49588",
      "incomplete_value": true,
      "site": "00b49588",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48594",
      "incomplete_value": true,
      "site": "00b48594",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49590",
      "incomplete_value": false,
      "site": "00b495a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:a25:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4859c",
      "incomplete_value": false,
      "site": "00b485b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:947:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b49580",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49590",
      "PARAM",
      [
        "storage",
        "002b9947",
        null,
        "string"
      ]
    ],
    [
      "00b495ac",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b49580",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49590",
      "PARAM",
      [
        "storage",
        "002b9a25",
        null,
        "string"
      ]
    ],
    [
      "00b495ac",
      "WRITE",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b485b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48578.md#insn-00b485b0) · [`00b485b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48578.md#insn-00b485b8) · [`00b48584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48578.md#insn-00b48584)
- 新版 [`00b495a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4956c.md#insn-00b495a4) · [`00b495ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4956c.md#insn-00b495ac) · [`00b49578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b4956c.md#insn-00b49578)

~~~diff
- 00b485b0 ["INT_ADD", "register:40f0:8", ["const:b485b0:8", "const:4:8"]]
- 00b485b0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b495a4 ["INT_ADD", "register:40f0:8", ["const:b495a4:8", "const:4:8"]]
+ 00b495a4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b485b0 bytes 8c4a0494
+ 00b495a4 bytes 834a0494
- 00b485b8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00b485b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b495ac ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
+ 00b495ac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b485b8 bytes 80d604f9
+ 00b495ac bytes 80b604f9
- 00b48584 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b49578 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b48584 bytes f42e00b0
+ 00b49578 bytes f42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-03449f1d223d3cd92c2199d35f964b69"></a>

### [`00b485e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b485e8.md) → [`00b495dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b495dc.md) _ZN8firebase4util6bundle11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b060`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b060.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5c030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c030.md) · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b495f8",
      "incomplete_value": false,
      "site": "00b495fc",
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
      "definition_site": "00b48604",
      "incomplete_value": false,
      "site": "00b48608",
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
      "definition_site": "00b49608",
      "incomplete_value": true,
      "site": "00b49614",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b48614",
      "incomplete_value": true,
      "site": "00b48620",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b495f8",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b49608",
      "DATA",
      [
        "storage",
        "011259b8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b495f8",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b49608",
      "DATA",
      [
        "storage",
        "01126978",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48608`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b485e8.md#insn-00b48608) · [`00b48604`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b485e8.md#insn-00b48604) · [`00b4860c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b485e8.md#insn-00b4860c)
- 新版 [`00b495fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b495dc.md#insn-00b495fc) · [`00b495f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b495dc.md#insn-00b495f8) · [`00b49600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b495dc.md#insn-00b49600)

~~~diff
- 00b48608 ["INT_ADD", "register:40f0:8", ["const:b48608:8", "const:4:8"]]
- 00b48608 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b495fc ["INT_ADD", "register:40f0:8", ["const:b495fc:8", "const:4:8"]]
+ 00b495fc ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b48608 bytes b24a0494
+ 00b495fc bytes a94a0494
- 00b48604 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b48604 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b48604 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b48604 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b495f8 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b495f8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b495f8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b495f8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b48604 bytes 002c0c91
+ 00b495f8 bytes 008c1191
- 00b4860c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b49600 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4860c bytes e82e00b0
+ 00b49600 bytes e82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-05d3fb236086332f6c8480f6d94b8f29"></a>

### [`00b48624`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48624.md) → [`00b49618`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49618.md) _ZN8firebase4util6bundle13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b49658",
      "incomplete_value": true,
      "site": "00b49658",
      "value": [
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
    "old": {
      "definition_site": "00b48664",
      "incomplete_value": true,
      "site": "00b48664",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b49634",
      "incomplete_value": true,
      "site": "00b49634",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48640",
      "incomplete_value": true,
      "site": "00b48640",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4963c",
      "incomplete_value": false,
      "site": "00b49650",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:a25:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48648",
      "incomplete_value": false,
      "site": "00b4865c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b9000:8"
          ],
          [
            "leaf",
            "const:947:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4962c",
      "READ",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4963c",
      "PARAM",
      [
        "storage",
        "002b9947",
        null,
        "string"
      ]
    ],
    [
      "00b49658",
      "WRITE",
      [
        "storage",
        "011259a8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4962c",
      "READ",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4963c",
      "PARAM",
      [
        "storage",
        "002b9a25",
        null,
        "string"
      ]
    ],
    [
      "00b49658",
      "WRITE",
      [
        "storage",
        "01126968",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4865c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48624.md#insn-00b4865c) · [`00b48664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48624.md#insn-00b48664) · [`00b48630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48624.md#insn-00b48630)
- 新版 [`00b49650`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49618.md#insn-00b49650) · [`00b49658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49618.md#insn-00b49658) · [`00b49624`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49618.md#insn-00b49624)

~~~diff
- 00b4865c ["INT_ADD", "register:40f0:8", ["const:b4865c:8", "const:4:8"]]
- 00b4865c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b49650 ["INT_ADD", "register:40f0:8", ["const:b49650:8", "const:4:8"]]
+ 00b49650 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4865c bytes 614a0494
+ 00b49650 bytes 584a0494
- 00b48664 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9a8:8"]]
- 00b48664 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49658 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:968:8"]]
+ 00b49658 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48664 bytes 80d604f9
+ 00b49658 bytes 80b604f9
- 00b48630 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b49624 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b48630 bytes f42e00b0
+ 00b49624 bytes f42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c59d3a409e2ef180a71cfa106211c6de"></a>

### [`00b48694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48694.md) → [`00b49688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49688.md) _ZN8firebase4util6bundle10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b496a4",
      "incomplete_value": false,
      "site": "00b496a8",
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
      "definition_site": "00b486b0",
      "incomplete_value": false,
      "site": "00b486b4",
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
      "definition_site": "00b496b4",
      "incomplete_value": true,
      "site": "00b496c0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b486c0",
      "incomplete_value": true,
      "site": "00b486cc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b496a4",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b496b4",
      "DATA",
      [
        "storage",
        "01125a00",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b496a4",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b496b4",
      "DATA",
      [
        "storage",
        "011269c0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b486b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48694.md#insn-00b486b4) · [`00b486b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48694.md#insn-00b486b0) · [`00b486b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48694.md#insn-00b486b8)
- 新版 [`00b496a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49688.md#insn-00b496a8) · [`00b496a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49688.md#insn-00b496a4) · [`00b496ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49688.md#insn-00b496ac)

~~~diff
- 00b486b4 ["INT_ADD", "register:40f0:8", ["const:b486b4:8", "const:4:8"]]
- 00b486b4 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b496a8 ["INT_ADD", "register:40f0:8", ["const:b496a8:8", "const:4:8"]]
+ 00b496a8 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b486b4 bytes 874a0494
+ 00b496a8 bytes 7e4a0494
- 00b486b0 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b486b0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b486b0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b486b0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b496a4 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b496a4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b496a4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b496a4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b486b0 bytes 00341591
+ 00b496a4 bytes 00681891
- 00b486b8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b496ac ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b486b8 bytes e82e00b0
+ 00b496ac bytes e82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-543e0adedbabe7d3fc2d663afa03bba7"></a>

### [`00b486d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b486d0.md) → [`00b496c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b496c4.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

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
      "definition_site": "00b496f0",
      "incomplete_value": true,
      "site": "00b496f0",
      "value": [
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
      "definition_site": "00b486fc",
      "incomplete_value": true,
      "site": "00b486fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b496d8",
      "incomplete_value": true,
      "site": "00b496d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b486e4",
      "incomplete_value": true,
      "site": "00b486e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b496e4",
      "incomplete_value": false,
      "site": "00b496e8",
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
      "definition_site": "00b486f0",
      "incomplete_value": false,
      "site": "00b486f4",
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
      "00b496d4",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b496e4",
      "PARAM",
      [
        "storage",
        "002a5feb",
        null,
        "string"
      ]
    ],
    [
      "00b496f0",
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
      "00b496d4",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b496e4",
      "PARAM",
      [
        "storage",
        "002a6143",
        null,
        "string"
      ]
    ],
    [
      "00b496f0",
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

- 旧版 [`00b486f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b486d0.md#insn-00b486f4) · [`00b486fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b486d0.md#insn-00b486fc) · [`00b486dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b486d0.md#insn-00b486dc)
- 新版 [`00b496e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b496c4.md#insn-00b496e8) · [`00b496f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b496c4.md#insn-00b496f0) · [`00b496d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b496c4.md#insn-00b496d0)

~~~diff
- 00b486f4 ["INT_ADD", "register:40f0:8", ["const:b486f4:8", "const:4:8"]]
- 00b486f4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b496e8 ["INT_ADD", "register:40f0:8", ["const:b496e8:8", "const:4:8"]]
+ 00b496e8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b486f4 bytes 3b4a0494
+ 00b496e8 bytes 324a0494
- 00b486fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
- 00b486fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b496f0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00b496f0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b486fc bytes 600605f9
+ 00b496f0 bytes 60e604f9
- 00b486dc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b496d0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b486dc bytes f32e00b0
+ 00b496d0 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cda19ea4737d0832db799d3dfb10a793"></a>

### [`00b48710`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48710.md) → [`00b49704`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49704.md) _ZN8firebase4util10byte_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b49730",
      "incomplete_value": true,
      "site": "00b49730",
      "value": [
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
      "definition_site": "00b4873c",
      "incomplete_value": true,
      "site": "00b4873c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b49718",
      "incomplete_value": true,
      "site": "00b49718",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48724",
      "incomplete_value": true,
      "site": "00b48724",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49720",
      "incomplete_value": false,
      "site": "00b49728",
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
      "definition_site": "00b4872c",
      "incomplete_value": false,
      "site": "00b48734",
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
      "00b49714",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49720",
      "PARAM",
      [
        "storage",
        "002a5feb",
        null,
        "string"
      ]
    ],
    [
      "00b49730",
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
      "00b49714",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49720",
      "PARAM",
      [
        "storage",
        "002a6143",
        null,
        "string"
      ]
    ],
    [
      "00b49730",
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

- 旧版 [`00b48734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48710.md#insn-00b48734) · [`00b4873c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48710.md#insn-00b4873c) · [`00b4871c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48710.md#insn-00b4871c)
- 新版 [`00b49728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49704.md#insn-00b49728) · [`00b49730`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49704.md#insn-00b49730) · [`00b49710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49704.md#insn-00b49710)

~~~diff
- 00b48734 ["INT_ADD", "register:40f0:8", ["const:b48734:8", "const:4:8"]]
- 00b48734 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b49728 ["INT_ADD", "register:40f0:8", ["const:b49728:8", "const:4:8"]]
+ 00b49728 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48734 bytes 2b4a0494
+ 00b49728 bytes 224a0494
- 00b4873c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
- 00b4873c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49730 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00b49730 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4873c bytes 600605f9
+ 00b49730 bytes 60e604f9
- 00b4871c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49710 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4871c bytes f32e00b0
+ 00b49710 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c5b02955ae167562f53db50a80708512"></a>

### [`00b48750`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48750.md) → [`00b49744`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49744.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b49774",
      "incomplete_value": true,
      "site": "00b49774",
      "value": [
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
      "definition_site": "00b48780",
      "incomplete_value": true,
      "site": "00b48780",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b49758",
      "incomplete_value": true,
      "site": "00b49758",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48764",
      "incomplete_value": true,
      "site": "00b48764",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49764",
      "incomplete_value": false,
      "site": "00b4976c",
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
      "definition_site": "00b48770",
      "incomplete_value": false,
      "site": "00b48778",
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
      "00b49754",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49764",
      "PARAM",
      [
        "storage",
        "002a5feb",
        null,
        "string"
      ]
    ],
    [
      "00b49774",
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
      "00b49754",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49764",
      "PARAM",
      [
        "storage",
        "002a6143",
        null,
        "string"
      ]
    ],
    [
      "00b49774",
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

- 旧版 [`00b48778`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48750.md#insn-00b48778) · [`00b48780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48750.md#insn-00b48780) · [`00b4875c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48750.md#insn-00b4875c)
- 新版 [`00b4976c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49744.md#insn-00b4976c) · [`00b49774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49744.md#insn-00b49774) · [`00b49750`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49744.md#insn-00b49750)

~~~diff
- 00b48778 ["INT_ADD", "register:40f0:8", ["const:b48778:8", "const:4:8"]]
- 00b48778 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4976c ["INT_ADD", "register:40f0:8", ["const:b4976c:8", "const:4:8"]]
+ 00b4976c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48778 bytes 1a4a0494
+ 00b4976c bytes 114a0494
- 00b48780 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
- 00b48780 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49774 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00b49774 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48780 bytes 600605f9
+ 00b49774 bytes 60e604f9
- 00b4875c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49750 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4875c bytes f32e00b0
+ 00b49750 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-37e677a35333c8c27c7ee386802aaeb4"></a>

### [`00b48794`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48794.md) → [`00b49788`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49788.md) _ZN8firebase4util10byte_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b497b8",
      "incomplete_value": true,
      "site": "00b497b8",
      "value": [
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
      "definition_site": "00b487c4",
      "incomplete_value": true,
      "site": "00b487c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:a08:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4979c",
      "incomplete_value": true,
      "site": "00b4979c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b487a8",
      "incomplete_value": true,
      "site": "00b487a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b497a4",
      "incomplete_value": false,
      "site": "00b497b0",
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
      "definition_site": "00b487b0",
      "incomplete_value": false,
      "site": "00b487bc",
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
      "00b49798",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b497a4",
      "PARAM",
      [
        "storage",
        "002a5feb",
        null,
        "string"
      ]
    ],
    [
      "00b497b8",
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
      "00b49798",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b497a4",
      "PARAM",
      [
        "storage",
        "002a6143",
        null,
        "string"
      ]
    ],
    [
      "00b497b8",
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

- 旧版 [`00b487bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48794.md#insn-00b487bc) · [`00b487c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48794.md#insn-00b487c4) · [`00b487a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48794.md#insn-00b487a0)
- 新版 [`00b497b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49788.md#insn-00b497b0) · [`00b497b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49788.md#insn-00b497b8) · [`00b49794`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49788.md#insn-00b49794)

~~~diff
- 00b487bc ["INT_ADD", "register:40f0:8", ["const:b487bc:8", "const:4:8"]]
- 00b487bc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b497b0 ["INT_ADD", "register:40f0:8", ["const:b497b0:8", "const:4:8"]]
+ 00b497b0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b487bc bytes 094a0494
+ 00b497b0 bytes 004a0494
- 00b487c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:a08:8"]]
- 00b487c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b497b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:9c8:8"]]
+ 00b497b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b487c4 bytes 600605f9
+ 00b497b8 bytes 60e604f9
- 00b487a0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b49794 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b487a0 bytes f32e00b0
+ 00b49794 bytes f32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5e209aa05de27edcf2cea46954df452e"></a>

### [`00b487e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b487e4.md) → [`00b497d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b497d8.md) _ZN8firebase4util10byte_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b49860",
      "incomplete_value": true,
      "site": "00b49860",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4886c",
      "incomplete_value": true,
      "site": "00b4886c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "definition_site": "00b4980c",
      "incomplete_value": true,
      "site": "00b49818",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:9c8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b48818",
      "incomplete_value": true,
      "site": "00b48824",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:a08:8"
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
      "00b497ec",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4980c",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49860",
      "WRITE",
      [
        "storage",
        "01125a10",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b497ec",
      "READ",
      [
        "storage",
        "011269d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4980c",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49860",
      "WRITE",
      [
        "storage",
        "011269d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b48824`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b487e4.md#insn-00b48824) · [`00b4886c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b487e4.md#insn-00b4886c) · [`00b487f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b487e4.md#insn-00b487f4)
- 新版 [`00b49818`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b497d8.md#insn-00b49818) · [`00b49860`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b497d8.md#insn-00b49860) · [`00b497e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b497d8.md#insn-00b497e8)

~~~diff
- 00b48824 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b48824 ["INT_ADD", "register:40f0:8", ["const:b48824:8", "const:4:8"]]
- 00b48824 ["CALLIND", null, ["register:0:8"]]
+ 00b49818 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b49818 ["INT_ADD", "register:40f0:8", ["const:b49818:8", "const:4:8"]]
+ 00b49818 ["CALLIND", null, ["register:0:8"]]
- 00b48824 bytes 00013fd6
+ 00b49818 bytes 00013fd6
- 00b4886c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4886c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:a10:8"]]
- 00b4886c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b49860 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b49860 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:9d0:8"]]
+ 00b49860 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4886c bytes a0422839
+ 00b49860 bytes a0422739
- 00b487f4 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b497e8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b487f4 bytes f52e00b0
+ 00b497e8 bytes f52e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80cabe8e24e3ed5570fed3e7ae029f36"></a>

### [`00b48880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48880.md) → [`00b49874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49874.md) _ZN8firebase4util10byte_class12ReleaseClassEP7_JNIEnv

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b498b0",
      "incomplete_value": true,
      "site": "00b498b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:9d0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b488bc",
      "incomplete_value": true,
      "site": "00b488bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:a10:8"
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
      "definition_site": "00b49900",
      "incomplete_value": true,
      "site": "00b49900",
      "value": [
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
      "definition_site": "00b4890c",
      "incomplete_value": true,
      "site": "00b4890c",
      "value": [
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
    "ordinal": 6,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4988c",
      "incomplete_value": true,
      "site": "00b4988c",
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
      "definition_site": "00b48898",
      "incomplete_value": true,
      "site": "00b48898",
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
      "00b49888",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49894",
      "READ",
      [
        "storage",
        "01125a10",
        null,
        "undefined1"
      ]
    ],
    [
      "00b498b0",
      "WRITE",
      [
        "storage",
        "01125a10",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b49888",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49894",
      "READ",
      [
        "storage",
        "011269d0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b498b0",
      "WRITE",
      [
        "storage",
        "011269d0",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b488bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48880.md#insn-00b488bc) · [`00b4890c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48880.md#insn-00b4890c) · [`00b48890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48880.md#insn-00b48890)
- 新版 [`00b498b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49874.md#insn-00b498b0) · [`00b49900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49874.md#insn-00b49900) · [`00b49884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49874.md#insn-00b49884)

~~~diff
- 00b488bc ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b488bc ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b488bc ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:a10:8"]]
- 00b488bc ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b498b0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b498b0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b498b0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:9d0:8"]]
+ 00b498b0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b488bc bytes bf422839
+ 00b498b0 bytes bf422739
- 00b4890c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a08:8"]]
- 00b4890c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4890c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b49900 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9c8:8"]]
+ 00b49900 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b49900 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4890c bytes 9f0605f9
+ 00b49900 bytes 9fe604f9
- 00b48890 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b49884 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b48890 bytes f42e00b0
+ 00b49884 bytes f42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9cdd8e4a6e44d0cbda05976229e1865e"></a>

### [`00b48920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48920.md) → [`00b49914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49914.md) _ZN8firebase4util10byte_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b49954",
      "incomplete_value": true,
      "site": "00b49954",
      "value": [
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
      "definition_site": "00b48960",
      "incomplete_value": true,
      "site": "00b48960",
      "value": [
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
      "definition_site": "00b49930",
      "incomplete_value": true,
      "site": "00b49930",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4893c",
      "incomplete_value": true,
      "site": "00b4893c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b49938",
      "incomplete_value": false,
      "site": "00b4994c",
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
      "definition_site": "00b48944",
      "incomplete_value": false,
      "site": "00b48958",
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
      "00b49928",
      "READ",
      [
        "storage",
        "01125a08",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49938",
      "PARAM",
      [
        "storage",
        "002a5feb",
        null,
        "string"
      ]
    ],
    [
      "00b49954",
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
      "00b49928",
      "READ",
      [
        "storage",
        "011269c8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b49938",
      "PARAM",
      [
        "storage",
        "002a6143",
        null,
        "string"
      ]
    ],
    [
      "00b49954",
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

- 旧版 [`00b48958`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48920.md#insn-00b48958) · [`00b48960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48920.md#insn-00b48960) · [`00b4892c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b48/00b48920.md#insn-00b4892c)
- 新版 [`00b4994c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49914.md#insn-00b4994c) · [`00b49954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49914.md#insn-00b49954) · [`00b49920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b49/00b49914.md#insn-00b49920)

~~~diff
- 00b48958 ["INT_ADD", "register:40f0:8", ["const:b48958:8", "const:4:8"]]
- 00b48958 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4994c ["INT_ADD", "register:40f0:8", ["const:b4994c:8", "const:4:8"]]
+ 00b4994c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b48958 bytes a2490494
+ 00b4994c bytes 99490494
- 00b48960 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:a08:8"]]
- 00b48960 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b49954 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:9c8:8"]]
+ 00b49954 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b48960 bytes 800605f9
+ 00b49954 bytes 80e604f9
- 00b4892c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b49920 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4892c bytes f42e00b0
+ 00b49920 bytes f42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

