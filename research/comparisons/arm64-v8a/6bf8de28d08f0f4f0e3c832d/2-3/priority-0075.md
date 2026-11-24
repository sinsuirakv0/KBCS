# v16.0.2 → v16.0.3 · 最優先の変更候補 (75)

[一覧の目次](README.md)

<a id="compare-22f557322fc9eda924bdbb374672ba91"></a>

### [`00b4adb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4adb0.md) → [`00b4bda4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bda4.md) _ZN8firebase4util11float_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4bde4",
      "incomplete_value": true,
      "site": "00b4bde4",
      "value": [
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
      "definition_site": "00b4adf0",
      "incomplete_value": true,
      "site": "00b4adf0",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4bdc0",
      "incomplete_value": true,
      "site": "00b4bdc0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4adcc",
      "incomplete_value": true,
      "site": "00b4adcc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4bdc8",
      "incomplete_value": false,
      "site": "00b4bddc",
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
      "definition_site": "00b4add4",
      "incomplete_value": false,
      "site": "00b4ade8",
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
      "00b4bdb8",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bdc8",
      "PARAM",
      [
        "storage",
        "002a95af",
        null,
        "string"
      ]
    ],
    [
      "00b4bde4",
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
      "00b4bdb8",
      "READ",
      [
        "storage",
        "01126ba8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bdc8",
      "PARAM",
      [
        "storage",
        "002a967c",
        null,
        "string"
      ]
    ],
    [
      "00b4bde4",
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

- 旧版 [`00b4ade8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4adb0.md#insn-00b4ade8) · [`00b4adf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4adb0.md#insn-00b4adf0) · [`00b4adbc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4adb0.md#insn-00b4adbc)
- 新版 [`00b4bddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bda4.md#insn-00b4bddc) · [`00b4bde4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bda4.md#insn-00b4bde4) · [`00b4bdb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bda4.md#insn-00b4bdb0)

~~~diff
- 00b4ade8 ["INT_ADD", "register:40f0:8", ["const:b4ade8:8", "const:4:8"]]
- 00b4ade8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4bddc ["INT_ADD", "register:40f0:8", ["const:b4bddc:8", "const:4:8"]]
+ 00b4bddc ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4ade8 bytes 7e400494
+ 00b4bddc bytes 75400494
- 00b4adf0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
- 00b4adf0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bde4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ba8:8"]]
+ 00b4bde4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4adf0 bytes 80f605f9
+ 00b4bde4 bytes 80d605f9
- 00b4adbc ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4bdb0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4adbc bytes d42e00f0
+ 00b4bdb0 bytes d42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-458c920098f0ca9d26732070773c1a9e"></a>

### [`00b4ae20`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ae20.md) → [`00b4be14`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4be14.md) _ZN8firebase4util11float_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b4be30",
      "incomplete_value": false,
      "site": "00b4be34",
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
      "definition_site": "00b4ae3c",
      "incomplete_value": false,
      "site": "00b4ae40",
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
      "definition_site": "00b4be40",
      "incomplete_value": true,
      "site": "00b4be4c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4ae4c",
      "incomplete_value": true,
      "site": "00b4ae58",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4be30",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4be40",
      "DATA",
      [
        "storage",
        "01125bf8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4be30",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4be40",
      "DATA",
      [
        "storage",
        "01126bb8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ae40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ae20.md#insn-00b4ae40) · [`00b4ae3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ae20.md#insn-00b4ae3c) · [`00b4ae44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ae20.md#insn-00b4ae44)
- 新版 [`00b4be34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4be14.md#insn-00b4be34) · [`00b4be30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4be14.md#insn-00b4be30) · [`00b4be38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4be14.md#insn-00b4be38)

~~~diff
- 00b4ae40 ["INT_ADD", "register:40f0:8", ["const:b4ae40:8", "const:4:8"]]
- 00b4ae40 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4be34 ["INT_ADD", "register:40f0:8", ["const:b4be34:8", "const:4:8"]]
+ 00b4be34 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4ae40 bytes a4400494
+ 00b4be34 bytes 9b400494
- 00b4ae3c ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4ae3c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ae3c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4ae3c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4be30 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4be30 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4be30 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4be30 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4ae3c bytes 002c0c91
+ 00b4be30 bytes 008c1191
- 00b4ae44 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4be38 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4ae44 bytes c82e00f0
+ 00b4be38 bytes c82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ef9532bded960f89a6e13bce0b925e88"></a>

### [`00b4ae5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ae5c.md) → [`00b4be50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4be50.md) _ZN8firebase4util11float_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4be90",
      "incomplete_value": true,
      "site": "00b4be90",
      "value": [
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
      "definition_site": "00b4ae9c",
      "incomplete_value": true,
      "site": "00b4ae9c",
      "value": [
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
    "ordinal": 4,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4be6c",
      "incomplete_value": true,
      "site": "00b4be6c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ae78",
      "incomplete_value": true,
      "site": "00b4ae78",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4be74",
      "incomplete_value": false,
      "site": "00b4be88",
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
      "definition_site": "00b4ae80",
      "incomplete_value": false,
      "site": "00b4ae94",
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
      "00b4be64",
      "READ",
      [
        "storage",
        "01125be8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4be74",
      "PARAM",
      [
        "storage",
        "002a95af",
        null,
        "string"
      ]
    ],
    [
      "00b4be90",
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
      "00b4be64",
      "READ",
      [
        "storage",
        "01126ba8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4be74",
      "PARAM",
      [
        "storage",
        "002a967c",
        null,
        "string"
      ]
    ],
    [
      "00b4be90",
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

- 旧版 [`00b4ae94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ae5c.md#insn-00b4ae94) · [`00b4ae9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ae5c.md#insn-00b4ae9c) · [`00b4ae68`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4ae5c.md#insn-00b4ae68)
- 新版 [`00b4be88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4be50.md#insn-00b4be88) · [`00b4be90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4be50.md#insn-00b4be90) · [`00b4be5c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4be50.md#insn-00b4be5c)

~~~diff
- 00b4ae94 ["INT_ADD", "register:40f0:8", ["const:b4ae94:8", "const:4:8"]]
- 00b4ae94 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4be88 ["INT_ADD", "register:40f0:8", ["const:b4be88:8", "const:4:8"]]
+ 00b4be88 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4ae94 bytes 53400494
+ 00b4be88 bytes 4a400494
- 00b4ae9c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:be8:8"]]
- 00b4ae9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4be90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ba8:8"]]
+ 00b4be90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ae9c bytes 80f605f9
+ 00b4be90 bytes 80d605f9
- 00b4ae68 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4be5c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4ae68 bytes d42e00f0
+ 00b4be5c bytes d42e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6e0357b7b1adbcb79863d79d710db2e9"></a>

### [`00b4aecc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aecc.md) → [`00b4bec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bec0.md) _ZN8firebase4util11float_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4bedc",
      "incomplete_value": true,
      "site": "00b4bee0",
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
      "definition_site": "00b4aee8",
      "incomplete_value": true,
      "site": "00b4aeec",
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
      "definition_site": "00b4beec",
      "incomplete_value": true,
      "site": "00b4bef8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4aef8",
      "incomplete_value": true,
      "site": "00b4af04",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4bedc",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4beec",
      "DATA",
      [
        "storage",
        "01125c08",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4bedc",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4beec",
      "DATA",
      [
        "storage",
        "01126bc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aeec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aecc.md#insn-00b4aeec) · [`00b4aee8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aecc.md#insn-00b4aee8) · [`00b4aef0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4aecc.md#insn-00b4aef0)
- 新版 [`00b4bee0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bec0.md#insn-00b4bee0) · [`00b4bedc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bec0.md#insn-00b4bedc) · [`00b4bee4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bec0.md#insn-00b4bee4)

~~~diff
- 00b4aeec ["INT_ADD", "register:40f0:8", ["const:b4aeec:8", "const:4:8"]]
- 00b4aeec ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4bee0 ["INT_ADD", "register:40f0:8", ["const:b4bee0:8", "const:4:8"]]
+ 00b4bee0 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4aeec bytes 79400494
+ 00b4bee0 bytes 70400494
- 00b4aee8 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b4aee8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4aee8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4aee8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4bedc ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4bedc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bedc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4bedc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4aee8 bytes 00341591
+ 00b4bedc bytes 00681891
- 00b4aef0 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4bee4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4aef0 bytes c82e00f0
+ 00b4bee4 bytes c82e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-79246123935d29238a2e0ee0d3ad931d"></a>

### [`00b4af08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af08.md) → [`00b4befc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4befc.md) _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

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
      "definition_site": "00b4bf28",
      "incomplete_value": true,
      "site": "00b4bf28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4af34",
      "incomplete_value": true,
      "site": "00b4af34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4bf10",
      "incomplete_value": true,
      "site": "00b4bf10",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4af1c",
      "incomplete_value": true,
      "site": "00b4af1c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4bf1c",
      "incomplete_value": false,
      "site": "00b4bf20",
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
            "const:8e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4af28",
      "incomplete_value": false,
      "site": "00b4af2c",
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
            "const:78a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4bf0c",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bf1c",
      "PARAM",
      [
        "storage",
        "002a678a",
        null,
        "string"
      ]
    ],
    [
      "00b4bf28",
      "WRITE",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bf0c",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bf1c",
      "PARAM",
      [
        "storage",
        "002a68e2",
        null,
        "string"
      ]
    ],
    [
      "00b4bf28",
      "WRITE",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4af2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af08.md#insn-00b4af2c) · [`00b4af34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af08.md#insn-00b4af34) · [`00b4af14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af08.md#insn-00b4af14)
- 新版 [`00b4bf20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4befc.md#insn-00b4bf20) · [`00b4bf28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4befc.md#insn-00b4bf28) · [`00b4bf08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4befc.md#insn-00b4bf08)

~~~diff
- 00b4af2c ["INT_ADD", "register:40f0:8", ["const:b4af2c:8", "const:4:8"]]
- 00b4af2c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4bf20 ["INT_ADD", "register:40f0:8", ["const:b4bf20:8", "const:4:8"]]
+ 00b4bf20 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4af2c bytes 2d400494
+ 00b4bf20 bytes 24400494
- 00b4af34 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
- 00b4af34 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bf28 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bd0:8"]]
+ 00b4bf28 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4af34 bytes 600a06f9
+ 00b4bf28 bytes 60ea05f9
- 00b4af14 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4bf08 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4af14 bytes d32e00f0
+ 00b4bf08 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-14d29ce3dd63dd0aa11f5ff788f7072c"></a>

### [`00b4af48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af48.md) → [`00b4bf3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bf3c.md) _ZN8firebase4util8hash_map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4bf68",
      "incomplete_value": true,
      "site": "00b4bf68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4af74",
      "incomplete_value": true,
      "site": "00b4af74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4bf50",
      "incomplete_value": true,
      "site": "00b4bf50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4af5c",
      "incomplete_value": true,
      "site": "00b4af5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4bf58",
      "incomplete_value": false,
      "site": "00b4bf60",
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
            "const:8e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4af64",
      "incomplete_value": false,
      "site": "00b4af6c",
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
            "const:78a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4bf4c",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bf58",
      "PARAM",
      [
        "storage",
        "002a678a",
        null,
        "string"
      ]
    ],
    [
      "00b4bf68",
      "WRITE",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bf4c",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bf58",
      "PARAM",
      [
        "storage",
        "002a68e2",
        null,
        "string"
      ]
    ],
    [
      "00b4bf68",
      "WRITE",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4af6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af48.md#insn-00b4af6c) · [`00b4af74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af48.md#insn-00b4af74) · [`00b4af54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af48.md#insn-00b4af54)
- 新版 [`00b4bf60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bf3c.md#insn-00b4bf60) · [`00b4bf68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bf3c.md#insn-00b4bf68) · [`00b4bf48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bf3c.md#insn-00b4bf48)

~~~diff
- 00b4af6c ["INT_ADD", "register:40f0:8", ["const:b4af6c:8", "const:4:8"]]
- 00b4af6c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4bf60 ["INT_ADD", "register:40f0:8", ["const:b4bf60:8", "const:4:8"]]
+ 00b4bf60 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4af6c bytes 1d400494
+ 00b4bf60 bytes 14400494
- 00b4af74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
- 00b4af74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bf68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bd0:8"]]
+ 00b4bf68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4af74 bytes 600a06f9
+ 00b4bf68 bytes 60ea05f9
- 00b4af54 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4bf48 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4af54 bytes d32e00f0
+ 00b4bf48 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-21cb6492c013cba569c64bbc8b7edad2"></a>

### [`00b4af88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af88.md) → [`00b4bf7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bf7c.md) _ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4bfac",
      "incomplete_value": true,
      "site": "00b4bfac",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4afb8",
      "incomplete_value": true,
      "site": "00b4afb8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4bf90",
      "incomplete_value": true,
      "site": "00b4bf90",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4af9c",
      "incomplete_value": true,
      "site": "00b4af9c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4bf9c",
      "incomplete_value": false,
      "site": "00b4bfa4",
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
            "const:8e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4afa8",
      "incomplete_value": false,
      "site": "00b4afb0",
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
            "const:78a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4bf8c",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bf9c",
      "PARAM",
      [
        "storage",
        "002a678a",
        null,
        "string"
      ]
    ],
    [
      "00b4bfac",
      "WRITE",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bf8c",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bf9c",
      "PARAM",
      [
        "storage",
        "002a68e2",
        null,
        "string"
      ]
    ],
    [
      "00b4bfac",
      "WRITE",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4afb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af88.md#insn-00b4afb0) · [`00b4afb8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af88.md#insn-00b4afb8) · [`00b4af94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4af88.md#insn-00b4af94)
- 新版 [`00b4bfa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bf7c.md#insn-00b4bfa4) · [`00b4bfac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bf7c.md#insn-00b4bfac) · [`00b4bf88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bf7c.md#insn-00b4bf88)

~~~diff
- 00b4afb0 ["INT_ADD", "register:40f0:8", ["const:b4afb0:8", "const:4:8"]]
- 00b4afb0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4bfa4 ["INT_ADD", "register:40f0:8", ["const:b4bfa4:8", "const:4:8"]]
+ 00b4bfa4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4afb0 bytes 0c400494
+ 00b4bfa4 bytes 03400494
- 00b4afb8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
- 00b4afb8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bfac ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bd0:8"]]
+ 00b4bfac ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4afb8 bytes 600a06f9
+ 00b4bfac bytes 60ea05f9
- 00b4af94 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4bf88 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4af94 bytes d32e00f0
+ 00b4bf88 bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b213e544ec20cbb3520d6ab0ea85dee2"></a>

### [`00b4afcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4afcc.md) → [`00b4bfc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bfc0.md) _ZN8firebase4util8hash_map10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4bff0",
      "incomplete_value": true,
      "site": "00b4bff0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4affc",
      "incomplete_value": true,
      "site": "00b4affc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4bfd4",
      "incomplete_value": true,
      "site": "00b4bfd4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4afe0",
      "incomplete_value": true,
      "site": "00b4afe0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4bfdc",
      "incomplete_value": false,
      "site": "00b4bfe8",
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
            "const:8e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4afe8",
      "incomplete_value": false,
      "site": "00b4aff4",
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
            "const:78a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4bfd0",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bfdc",
      "PARAM",
      [
        "storage",
        "002a678a",
        null,
        "string"
      ]
    ],
    [
      "00b4bff0",
      "WRITE",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4bfd0",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4bfdc",
      "PARAM",
      [
        "storage",
        "002a68e2",
        null,
        "string"
      ]
    ],
    [
      "00b4bff0",
      "WRITE",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4aff4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4afcc.md#insn-00b4aff4) · [`00b4affc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4afcc.md#insn-00b4affc) · [`00b4afd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4a/00b4afcc.md#insn-00b4afd8)
- 新版 [`00b4bfe8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bfc0.md#insn-00b4bfe8) · [`00b4bff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bfc0.md#insn-00b4bff0) · [`00b4bfcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4b/00b4bfc0.md#insn-00b4bfcc)

~~~diff
- 00b4aff4 ["INT_ADD", "register:40f0:8", ["const:b4aff4:8", "const:4:8"]]
- 00b4aff4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4bfe8 ["INT_ADD", "register:40f0:8", ["const:b4bfe8:8", "const:4:8"]]
+ 00b4bfe8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4aff4 bytes fb3f0494
+ 00b4bfe8 bytes f23f0494
- 00b4affc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c10:8"]]
- 00b4affc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4bff0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bd0:8"]]
+ 00b4bff0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4affc bytes 600a06f9
+ 00b4bff0 bytes 60ea05f9
- 00b4afd8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4bfcc ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4afd8 bytes d32e00f0
+ 00b4bfcc bytes d32e00f0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-426d4b14ced02d835bbc8a5f648454a5"></a>

### [`00b4b01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b01c.md) → [`00b4c010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c010.md) _ZN8firebase4util8hash_map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4c098",
      "incomplete_value": true,
      "site": "00b4c098",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b0a4",
      "incomplete_value": true,
      "site": "00b4b0a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c18:8"
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
      "definition_site": "00b4c044",
      "incomplete_value": true,
      "site": "00b4c050",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b050",
      "incomplete_value": true,
      "site": "00b4b05c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c10:8"
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
      "00b4c024",
      "READ",
      [
        "storage",
        "01125c18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c044",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c098",
      "WRITE",
      [
        "storage",
        "01125c18",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c024",
      "READ",
      [
        "storage",
        "01126bd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c044",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c098",
      "WRITE",
      [
        "storage",
        "01126bd8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b05c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b01c.md#insn-00b4b05c) · [`00b4b0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b01c.md#insn-00b4b0a4) · [`00b4b02c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b01c.md#insn-00b4b02c)
- 新版 [`00b4c050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c010.md#insn-00b4c050) · [`00b4c098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c010.md#insn-00b4c098) · [`00b4c020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c010.md#insn-00b4c020)

~~~diff
- 00b4b05c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b05c ["INT_ADD", "register:40f0:8", ["const:b4b05c:8", "const:4:8"]]
- 00b4b05c ["CALLIND", null, ["register:0:8"]]
+ 00b4c050 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c050 ["INT_ADD", "register:40f0:8", ["const:b4c050:8", "const:4:8"]]
+ 00b4c050 ["CALLIND", null, ["register:0:8"]]
- 00b4b05c bytes 00013fd6
+ 00b4c050 bytes 00013fd6
- 00b4b0a4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4b0a4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c18:8"]]
- 00b4b0a4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4c098 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4c098 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:bd8:8"]]
+ 00b4c098 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4b0a4 bytes a0623039
+ 00b4c098 bytes a0622f39
- 00b4b02c ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4c020 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4b02c bytes d52e00d0
+ 00b4c020 bytes d52e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-23c1f7b4d5920a5984b2d0ff54ff33d0"></a>

### [`00b4b0b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b0b8.md) → [`00b4c0ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c0ac.md) _ZN8firebase4util8hash_map12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4c0e8",
      "incomplete_value": true,
      "site": "00b4c0e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:bd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b0f4",
      "incomplete_value": true,
      "site": "00b4b0f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c18:8"
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
      "definition_site": "00b4c138",
      "incomplete_value": true,
      "site": "00b4c138",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b144",
      "incomplete_value": true,
      "site": "00b4b144",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "definition_site": "00b4c0c4",
      "incomplete_value": true,
      "site": "00b4c0c4",
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
      "definition_site": "00b4b0d0",
      "incomplete_value": true,
      "site": "00b4b0d0",
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
      "00b4c0c0",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c0cc",
      "READ",
      [
        "storage",
        "01125c18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c0e8",
      "WRITE",
      [
        "storage",
        "01125c18",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c0c0",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c0cc",
      "READ",
      [
        "storage",
        "01126bd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c0e8",
      "WRITE",
      [
        "storage",
        "01126bd8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b0f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b0b8.md#insn-00b4b0f4) · [`00b4b140`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b0b8.md#insn-00b4b140) · [`00b4b144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b0b8.md#insn-00b4b144)
- 新版 [`00b4c0e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c0ac.md#insn-00b4c0e8) · [`00b4c134`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c0ac.md#insn-00b4c134) · [`00b4c138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c0ac.md#insn-00b4c138)

~~~diff
- 00b4b0f4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4b0f4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4b0f4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c18:8"]]
- 00b4b0f4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4c0e8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4c0e8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4c0e8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:bd8:8"]]
+ 00b4c0e8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4b0f4 bytes bf623039
+ 00b4c0e8 bytes bf622f39
- 00b4b140 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b140 ["INT_ADD", "register:40f0:8", ["const:b4b140:8", "const:4:8"]]
- 00b4b140 ["CALLIND", null, ["register:0:8"]]
+ 00b4c134 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c134 ["INT_ADD", "register:40f0:8", ["const:b4c134:8", "const:4:8"]]
+ 00b4c134 ["CALLIND", null, ["register:0:8"]]
- 00b4b140 bytes 00013fd6
+ 00b4c134 bytes 00013fd6
- 00b4b144 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
- 00b4b144 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4b144 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4c138 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bd0:8"]]
+ 00b4c138 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4c138 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4b144 bytes 9f0a06f9
+ 00b4c138 bytes 9fea05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f9d352a011c3b5637f1079c2c010e09d"></a>

### [`00b4b158`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b158.md) → [`00b4c14c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c14c.md) _ZN8firebase4util8hash_map14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4c18c",
      "incomplete_value": true,
      "site": "00b4c18c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b198",
      "incomplete_value": true,
      "site": "00b4b198",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "definition_site": "00b4c168",
      "incomplete_value": true,
      "site": "00b4c168",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b174",
      "incomplete_value": true,
      "site": "00b4b174",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c170",
      "incomplete_value": false,
      "site": "00b4c184",
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
            "const:8e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b17c",
      "incomplete_value": false,
      "site": "00b4b190",
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
            "const:78a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c160",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c170",
      "PARAM",
      [
        "storage",
        "002a678a",
        null,
        "string"
      ]
    ],
    [
      "00b4c18c",
      "WRITE",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c160",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c170",
      "PARAM",
      [
        "storage",
        "002a68e2",
        null,
        "string"
      ]
    ],
    [
      "00b4c18c",
      "WRITE",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b158.md#insn-00b4b190) · [`00b4b198`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b158.md#insn-00b4b198) · [`00b4b164`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b158.md#insn-00b4b164)
- 新版 [`00b4c184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c14c.md#insn-00b4c184) · [`00b4c18c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c14c.md#insn-00b4c18c) · [`00b4c158`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c14c.md#insn-00b4c158)

~~~diff
- 00b4b190 ["INT_ADD", "register:40f0:8", ["const:b4b190:8", "const:4:8"]]
- 00b4b190 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4c184 ["INT_ADD", "register:40f0:8", ["const:b4c184:8", "const:4:8"]]
+ 00b4c184 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4b190 bytes 943f0494
+ 00b4c184 bytes 8b3f0494
- 00b4b198 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
- 00b4b198 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c18c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bd0:8"]]
+ 00b4c18c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b198 bytes 800a06f9
+ 00b4c18c bytes 80ea05f9
- 00b4b164 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4c158 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4b164 bytes d42e00d0
+ 00b4c158 bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e8b5ae0d9b47208a9d976bd9e0ca42f6"></a>

### [`00b4b1c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b1c8.md) → [`00b4c1bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c1bc.md) _ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b080`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b080.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5c050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c050.md) · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4c1d8",
      "incomplete_value": false,
      "site": "00b4c1dc",
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
      "definition_site": "00b4b1e4",
      "incomplete_value": false,
      "site": "00b4b1e8",
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
      "definition_site": "00b4c1e8",
      "incomplete_value": true,
      "site": "00b4c1f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4b1f4",
      "incomplete_value": true,
      "site": "00b4b200",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4c1d8",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4c1e8",
      "DATA",
      [
        "storage",
        "01125c20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c1d8",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4c1e8",
      "DATA",
      [
        "storage",
        "01126be0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b1e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b1c8.md#insn-00b4b1e8) · [`00b4b1e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b1c8.md#insn-00b4b1e4) · [`00b4b1ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b1c8.md#insn-00b4b1ec)
- 新版 [`00b4c1dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c1bc.md#insn-00b4c1dc) · [`00b4c1d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c1bc.md#insn-00b4c1d8) · [`00b4c1e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c1bc.md#insn-00b4c1e0)

~~~diff
- 00b4b1e8 ["INT_ADD", "register:40f0:8", ["const:b4b1e8:8", "const:4:8"]]
- 00b4b1e8 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4c1dc ["INT_ADD", "register:40f0:8", ["const:b4c1dc:8", "const:4:8"]]
+ 00b4c1dc ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4b1e8 bytes ba3f0494
+ 00b4c1dc bytes b13f0494
- 00b4b1e4 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4b1e4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b1e4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b1e4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c1d8 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4c1d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c1d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c1d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b1e4 bytes 002c0c91
+ 00b4c1d8 bytes 008c1191
- 00b4b1ec ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4c1e0 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4b1ec bytes c82e00d0
+ 00b4c1e0 bytes c82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-fc9244cfecaed094a749671162a5f8c2"></a>

### [`00b4b204`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b204.md) → [`00b4c1f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c1f8.md) _ZN8firebase4util8hash_map13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4c238",
      "incomplete_value": true,
      "site": "00b4c238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:bd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b244",
      "incomplete_value": true,
      "site": "00b4b244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c10:8"
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
      "definition_site": "00b4c214",
      "incomplete_value": true,
      "site": "00b4c214",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b220",
      "incomplete_value": true,
      "site": "00b4b220",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c21c",
      "incomplete_value": false,
      "site": "00b4c230",
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
            "const:8e2:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b228",
      "incomplete_value": false,
      "site": "00b4b23c",
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
            "const:78a:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c20c",
      "READ",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c21c",
      "PARAM",
      [
        "storage",
        "002a678a",
        null,
        "string"
      ]
    ],
    [
      "00b4c238",
      "WRITE",
      [
        "storage",
        "01125c10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c20c",
      "READ",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c21c",
      "PARAM",
      [
        "storage",
        "002a68e2",
        null,
        "string"
      ]
    ],
    [
      "00b4c238",
      "WRITE",
      [
        "storage",
        "01126bd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b204.md#insn-00b4b23c) · [`00b4b244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b204.md#insn-00b4b244) · [`00b4b210`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b204.md#insn-00b4b210)
- 新版 [`00b4c230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c1f8.md#insn-00b4c230) · [`00b4c238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c1f8.md#insn-00b4c238) · [`00b4c204`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c1f8.md#insn-00b4c204)

~~~diff
- 00b4b23c ["INT_ADD", "register:40f0:8", ["const:b4b23c:8", "const:4:8"]]
- 00b4b23c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4c230 ["INT_ADD", "register:40f0:8", ["const:b4c230:8", "const:4:8"]]
+ 00b4c230 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4b23c bytes 693f0494
+ 00b4c230 bytes 603f0494
- 00b4b244 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c10:8"]]
- 00b4b244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c238 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bd0:8"]]
+ 00b4c238 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b244 bytes 800a06f9
+ 00b4c238 bytes 80ea05f9
- 00b4b210 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4c204 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4b210 bytes d42e00d0
+ 00b4c204 bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1a0ac6df96f36059ac378ebe2b2b454c"></a>

### [`00b4b274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b274.md) → [`00b4c268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c268.md) _ZN8firebase4util8hash_map10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4c284",
      "incomplete_value": false,
      "site": "00b4c288",
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
      "definition_site": "00b4b290",
      "incomplete_value": false,
      "site": "00b4b294",
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
      "definition_site": "00b4c294",
      "incomplete_value": true,
      "site": "00b4c2a0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4b2a0",
      "incomplete_value": true,
      "site": "00b4b2ac",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4c284",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4c294",
      "DATA",
      [
        "storage",
        "01125c28",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4c284",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4c294",
      "DATA",
      [
        "storage",
        "01126be8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b294`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b274.md#insn-00b4b294) · [`00b4b290`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b274.md#insn-00b4b290) · [`00b4b298`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b274.md#insn-00b4b298)
- 新版 [`00b4c288`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c268.md#insn-00b4c288) · [`00b4c284`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c268.md#insn-00b4c284) · [`00b4c28c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c268.md#insn-00b4c28c)

~~~diff
- 00b4b294 ["INT_ADD", "register:40f0:8", ["const:b4b294:8", "const:4:8"]]
- 00b4b294 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4c288 ["INT_ADD", "register:40f0:8", ["const:b4c288:8", "const:4:8"]]
+ 00b4c288 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4b294 bytes 8f3f0494
+ 00b4c288 bytes 863f0494
- 00b4b290 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b4b290 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b290 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b290 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c284 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4c284 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c284 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c284 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b290 bytes 00341591
+ 00b4c284 bytes 00681891
- 00b4b298 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4c28c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4b298 bytes c82e00d0
+ 00b4c28c bytes c82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-baf5985cc42771d125cb0dc5a959aff3"></a>

### [`00b4b2b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b2b0.md) → [`00b4c2a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c2a4.md) _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00b4c2d0",
      "incomplete_value": true,
      "site": "00b4c2d0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b2dc",
      "incomplete_value": true,
      "site": "00b4b2dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4c2b8",
      "incomplete_value": true,
      "site": "00b4c2b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b2c4",
      "incomplete_value": true,
      "site": "00b4b2c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c2c4",
      "incomplete_value": false,
      "site": "00b4c2c8",
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
            "const:52e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b2d0",
      "incomplete_value": false,
      "site": "00b4b2d4",
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
            "const:3d6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c2b4",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c2c4",
      "PARAM",
      [
        "storage",
        "002a83d6",
        null,
        "string"
      ]
    ],
    [
      "00b4c2d0",
      "WRITE",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c2b4",
      "READ",
      [
        "storage",
        "01126bf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c2c4",
      "PARAM",
      [
        "storage",
        "002a852e",
        null,
        "string"
      ]
    ],
    [
      "00b4c2d0",
      "WRITE",
      [
        "storage",
        "01126bf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b2d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b2b0.md#insn-00b4b2d4) · [`00b4b2dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b2b0.md#insn-00b4b2dc) · [`00b4b2bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b2b0.md#insn-00b4b2bc)
- 新版 [`00b4c2c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c2a4.md#insn-00b4c2c8) · [`00b4c2d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c2a4.md#insn-00b4c2d0) · [`00b4c2b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c2a4.md#insn-00b4c2b0)

~~~diff
- 00b4b2d4 ["INT_ADD", "register:40f0:8", ["const:b4b2d4:8", "const:4:8"]]
- 00b4b2d4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4c2c8 ["INT_ADD", "register:40f0:8", ["const:b4c2c8:8", "const:4:8"]]
+ 00b4c2c8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4b2d4 bytes 433f0494
+ 00b4c2c8 bytes 3a3f0494
- 00b4b2dc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
- 00b4b2dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c2d0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bf0:8"]]
+ 00b4c2d0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b2dc bytes 601a06f9
+ 00b4c2d0 bytes 60fa05f9
- 00b4b2bc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4c2b0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4b2bc bytes d32e00d0
+ 00b4c2b0 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-df388617774315a76174d7bd367468c4"></a>

### [`00b4b2f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b2f0.md) → [`00b4c2e4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c2e4.md) _ZN8firebase4util13integer_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EE

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
      "definition_site": "00b4c310",
      "incomplete_value": true,
      "site": "00b4c310",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b31c",
      "incomplete_value": true,
      "site": "00b4b31c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4c2f8",
      "incomplete_value": true,
      "site": "00b4c2f8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b304",
      "incomplete_value": true,
      "site": "00b4b304",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c300",
      "incomplete_value": false,
      "site": "00b4c308",
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
            "const:52e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b30c",
      "incomplete_value": false,
      "site": "00b4b314",
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
            "const:3d6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c2f4",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c300",
      "PARAM",
      [
        "storage",
        "002a83d6",
        null,
        "string"
      ]
    ],
    [
      "00b4c310",
      "WRITE",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c2f4",
      "READ",
      [
        "storage",
        "01126bf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c300",
      "PARAM",
      [
        "storage",
        "002a852e",
        null,
        "string"
      ]
    ],
    [
      "00b4c310",
      "WRITE",
      [
        "storage",
        "01126bf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b314`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b2f0.md#insn-00b4b314) · [`00b4b31c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b2f0.md#insn-00b4b31c) · [`00b4b2fc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b2f0.md#insn-00b4b2fc)
- 新版 [`00b4c308`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c2e4.md#insn-00b4c308) · [`00b4c310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c2e4.md#insn-00b4c310) · [`00b4c2f0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c2e4.md#insn-00b4c2f0)

~~~diff
- 00b4b314 ["INT_ADD", "register:40f0:8", ["const:b4b314:8", "const:4:8"]]
- 00b4b314 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4c308 ["INT_ADD", "register:40f0:8", ["const:b4c308:8", "const:4:8"]]
+ 00b4c308 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4b314 bytes 333f0494
+ 00b4c308 bytes 2a3f0494
- 00b4b31c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
- 00b4b31c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c310 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bf0:8"]]
+ 00b4c310 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b31c bytes 601a06f9
+ 00b4c310 bytes 60fa05f9
- 00b4b2fc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4c2f0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4b2fc bytes d32e00d0
+ 00b4c2f0 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a840e9ae2ca17bae055f6ed8dc544ef5"></a>

### [`00b4b330`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b330.md) → [`00b4c324`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c324.md) _ZN8firebase4util13integer_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4c354",
      "incomplete_value": true,
      "site": "00b4c354",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b360",
      "incomplete_value": true,
      "site": "00b4b360",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c30:8"
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
      "definition_site": "00b4c344",
      "incomplete_value": true,
      "site": "00b4c34c",
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
            "const:52e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b350",
      "incomplete_value": true,
      "site": "00b4b358",
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
            "const:3d6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c334",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c344",
      "PARAM",
      [
        "storage",
        "002a83d6",
        null,
        "string"
      ]
    ],
    [
      "00b4c354",
      "WRITE",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c334",
      "READ",
      [
        "storage",
        "01126bf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c344",
      "PARAM",
      [
        "storage",
        "002a852e",
        null,
        "string"
      ]
    ],
    [
      "00b4c354",
      "WRITE",
      [
        "storage",
        "01126bf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b358`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b330.md#insn-00b4b358) · [`00b4b360`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b330.md#insn-00b4b360) · [`00b4b33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b330.md#insn-00b4b33c)
- 新版 [`00b4c34c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c324.md#insn-00b4c34c) · [`00b4c354`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c324.md#insn-00b4c354) · [`00b4c330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c324.md#insn-00b4c330)

~~~diff
- 00b4b358 ["INT_ADD", "register:40f0:8", ["const:b4b358:8", "const:4:8"]]
- 00b4b358 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4c34c ["INT_ADD", "register:40f0:8", ["const:b4c34c:8", "const:4:8"]]
+ 00b4c34c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4b358 bytes 223f0494
+ 00b4c34c bytes 193f0494
- 00b4b360 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
- 00b4b360 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c354 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bf0:8"]]
+ 00b4c354 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b360 bytes 601a06f9
+ 00b4c354 bytes 60fa05f9
- 00b4b33c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4c330 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4b33c bytes d32e00d0
+ 00b4c330 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ece1b82c20cfeea7475864556eb88ccc"></a>

### [`00b4b374`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b374.md) → [`00b4c368`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c368.md) _ZN8firebase4util13integer_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4c398",
      "incomplete_value": true,
      "site": "00b4c398",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b3a4",
      "incomplete_value": true,
      "site": "00b4b3a4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c30:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4c37c",
      "incomplete_value": true,
      "site": "00b4c37c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b388",
      "incomplete_value": true,
      "site": "00b4b388",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c384",
      "incomplete_value": false,
      "site": "00b4c390",
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
            "const:52e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b390",
      "incomplete_value": false,
      "site": "00b4b39c",
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
            "const:3d6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c378",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c384",
      "PARAM",
      [
        "storage",
        "002a83d6",
        null,
        "string"
      ]
    ],
    [
      "00b4c398",
      "WRITE",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c378",
      "READ",
      [
        "storage",
        "01126bf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c384",
      "PARAM",
      [
        "storage",
        "002a852e",
        null,
        "string"
      ]
    ],
    [
      "00b4c398",
      "WRITE",
      [
        "storage",
        "01126bf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b39c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b374.md#insn-00b4b39c) · [`00b4b3a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b374.md#insn-00b4b3a4) · [`00b4b380`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b374.md#insn-00b4b380)
- 新版 [`00b4c390`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c368.md#insn-00b4c390) · [`00b4c398`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c368.md#insn-00b4c398) · [`00b4c374`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c368.md#insn-00b4c374)

~~~diff
- 00b4b39c ["INT_ADD", "register:40f0:8", ["const:b4b39c:8", "const:4:8"]]
- 00b4b39c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4c390 ["INT_ADD", "register:40f0:8", ["const:b4c390:8", "const:4:8"]]
+ 00b4c390 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4b39c bytes 113f0494
+ 00b4c390 bytes 083f0494
- 00b4b3a4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c30:8"]]
- 00b4b3a4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c398 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:bf0:8"]]
+ 00b4c398 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b3a4 bytes 601a06f9
+ 00b4c398 bytes 60fa05f9
- 00b4b380 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4c374 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4b380 bytes d32e00d0
+ 00b4c374 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7a804a577ef4718f09293de8a88d3d6"></a>

### [`00b4b3c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b3c4.md) → [`00b4c3b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c3b8.md) _ZN8firebase4util13integer_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed` · `unresolved_reference_or_flow`

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
      "definition_site": "00b4c440",
      "incomplete_value": true,
      "site": "00b4c440",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b44c",
      "incomplete_value": true,
      "site": "00b4b44c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "definition_site": "00b4c3ec",
      "incomplete_value": true,
      "site": "00b4c3f8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:bf0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b3f8",
      "incomplete_value": true,
      "site": "00b4b404",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c30:8"
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
      "00b4c3cc",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c3ec",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c440",
      "WRITE",
      [
        "storage",
        "01125c38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c3cc",
      "READ",
      [
        "storage",
        "01126bf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c3ec",
      "READ",
      [
        "storage",
        "01126bf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c440",
      "WRITE",
      [
        "storage",
        "01126bf8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b404`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b3c4.md#insn-00b4b404) · [`00b4b44c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b3c4.md#insn-00b4b44c) · [`00b4b3d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b3c4.md#insn-00b4b3d4)
- 新版 [`00b4c3f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c3b8.md#insn-00b4c3f8) · [`00b4c440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c3b8.md#insn-00b4c440) · [`00b4c3c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c3b8.md#insn-00b4c3c8)

~~~diff
- 00b4b404 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b404 ["INT_ADD", "register:40f0:8", ["const:b4b404:8", "const:4:8"]]
- 00b4b404 ["CALLIND", null, ["register:0:8"]]
+ 00b4c3f8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c3f8 ["INT_ADD", "register:40f0:8", ["const:b4c3f8:8", "const:4:8"]]
+ 00b4c3f8 ["CALLIND", null, ["register:0:8"]]
- 00b4b404 bytes 00013fd6
+ 00b4c3f8 bytes 00013fd6
- 00b4b44c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4b44c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c38:8"]]
- 00b4b44c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4c440 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4c440 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:bf8:8"]]
+ 00b4c440 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4b44c bytes a0e23039
+ 00b4c440 bytes a0e22f39
- 00b4b3d4 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4c3c8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4b3d4 bytes d52e00d0
+ 00b4c3c8 bytes d52e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-598f98330d5ff98a3f2d83cd2ebdadd8"></a>

### [`00b4b460`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b460.md) → [`00b4c454`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c454.md) _ZN8firebase4util13integer_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4c490",
      "incomplete_value": true,
      "site": "00b4c490",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:bf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b49c",
      "incomplete_value": true,
      "site": "00b4b49c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c38:8"
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
      "definition_site": "00b4c4e0",
      "incomplete_value": true,
      "site": "00b4c4e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b4ec",
      "incomplete_value": true,
      "site": "00b4b4ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c30:8"
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
      "definition_site": "00b4c46c",
      "incomplete_value": true,
      "site": "00b4c46c",
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
      "definition_site": "00b4b478",
      "incomplete_value": true,
      "site": "00b4b478",
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
      "00b4c468",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c474",
      "READ",
      [
        "storage",
        "01125c38",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c490",
      "WRITE",
      [
        "storage",
        "01125c38",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c468",
      "READ",
      [
        "storage",
        "01126bf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c474",
      "READ",
      [
        "storage",
        "01126bf8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c490",
      "WRITE",
      [
        "storage",
        "01126bf8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b49c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b460.md#insn-00b4b49c) · [`00b4b4e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b460.md#insn-00b4b4e8) · [`00b4b4ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b460.md#insn-00b4b4ec)
- 新版 [`00b4c490`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c454.md#insn-00b4c490) · [`00b4c4dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c454.md#insn-00b4c4dc) · [`00b4c4e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c454.md#insn-00b4c4e0)

~~~diff
- 00b4b49c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4b49c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4b49c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c38:8"]]
- 00b4b49c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4c490 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4c490 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4c490 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:bf8:8"]]
+ 00b4c490 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4b49c bytes bfe23039
+ 00b4c490 bytes bfe22f39
- 00b4b4e8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b4e8 ["INT_ADD", "register:40f0:8", ["const:b4b4e8:8", "const:4:8"]]
- 00b4b4e8 ["CALLIND", null, ["register:0:8"]]
+ 00b4c4dc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c4dc ["INT_ADD", "register:40f0:8", ["const:b4c4dc:8", "const:4:8"]]
+ 00b4c4dc ["CALLIND", null, ["register:0:8"]]
- 00b4b4e8 bytes 00013fd6
+ 00b4c4dc bytes 00013fd6
- 00b4b4ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c30:8"]]
- 00b4b4ec ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4b4ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4c4e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bf0:8"]]
+ 00b4c4e0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4c4e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4b4ec bytes 9f1a06f9
+ 00b4c4e0 bytes 9ffa05f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2fac5215ea550d2c4c9286ba66a6ae47"></a>

### [`00b4b500`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b500.md) → [`00b4c4f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c4f4.md) _ZN8firebase4util13integer_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4c534",
      "incomplete_value": true,
      "site": "00b4c534",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b540",
      "incomplete_value": true,
      "site": "00b4b540",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c30:8"
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
      "definition_site": "00b4c510",
      "incomplete_value": true,
      "site": "00b4c510",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b51c",
      "incomplete_value": true,
      "site": "00b4b51c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c518",
      "incomplete_value": false,
      "site": "00b4c52c",
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
            "const:52e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b524",
      "incomplete_value": false,
      "site": "00b4b538",
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
            "const:3d6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c508",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c518",
      "PARAM",
      [
        "storage",
        "002a83d6",
        null,
        "string"
      ]
    ],
    [
      "00b4c534",
      "WRITE",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c508",
      "READ",
      [
        "storage",
        "01126bf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c518",
      "PARAM",
      [
        "storage",
        "002a852e",
        null,
        "string"
      ]
    ],
    [
      "00b4c534",
      "WRITE",
      [
        "storage",
        "01126bf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b500.md#insn-00b4b538) · [`00b4b540`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b500.md#insn-00b4b540) · [`00b4b50c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b500.md#insn-00b4b50c)
- 新版 [`00b4c52c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c4f4.md#insn-00b4c52c) · [`00b4c534`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c4f4.md#insn-00b4c534) · [`00b4c500`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c4f4.md#insn-00b4c500)

~~~diff
- 00b4b538 ["INT_ADD", "register:40f0:8", ["const:b4b538:8", "const:4:8"]]
- 00b4b538 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4c52c ["INT_ADD", "register:40f0:8", ["const:b4c52c:8", "const:4:8"]]
+ 00b4c52c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4b538 bytes aa3e0494
+ 00b4c52c bytes a13e0494
- 00b4b540 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c30:8"]]
- 00b4b540 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c534 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bf0:8"]]
+ 00b4c534 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b540 bytes 801a06f9
+ 00b4c534 bytes 80fa05f9
- 00b4b50c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4c500 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4b50c bytes d42e00d0
+ 00b4c500 bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4c86fe906dfd1cb737306374e8f9a8d5"></a>

### [`00b4b570`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b570.md) → [`00b4c564`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c564.md) _ZN8firebase4util13integer_class11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b4c580",
      "incomplete_value": false,
      "site": "00b4c584",
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
      "definition_site": "00b4b58c",
      "incomplete_value": false,
      "site": "00b4b590",
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
      "definition_site": "00b4c590",
      "incomplete_value": true,
      "site": "00b4c59c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4b59c",
      "incomplete_value": true,
      "site": "00b4b5a8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4c580",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4c590",
      "DATA",
      [
        "storage",
        "01125c40",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4c580",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4c590",
      "DATA",
      [
        "storage",
        "01126c00",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b590`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b570.md#insn-00b4b590) · [`00b4b58c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b570.md#insn-00b4b58c) · [`00b4b594`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b570.md#insn-00b4b594)
- 新版 [`00b4c584`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c564.md#insn-00b4c584) · [`00b4c580`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c564.md#insn-00b4c580) · [`00b4c588`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c564.md#insn-00b4c588)

~~~diff
- 00b4b590 ["INT_ADD", "register:40f0:8", ["const:b4b590:8", "const:4:8"]]
- 00b4b590 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4c584 ["INT_ADD", "register:40f0:8", ["const:b4c584:8", "const:4:8"]]
+ 00b4c584 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4b590 bytes d03e0494
+ 00b4c584 bytes c73e0494
- 00b4b58c ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4b58c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b58c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b58c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c580 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4c580 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c580 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c580 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b58c bytes 002c0c91
+ 00b4c580 bytes 008c1191
- 00b4b594 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4c588 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4b594 bytes c82e00d0
+ 00b4c588 bytes c82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ff4cdb021ae23f1622bf377f1fa5890e"></a>

### [`00b4b5ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b5ac.md) → [`00b4c5a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c5a0.md) _ZN8firebase4util13integer_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4c5e0",
      "incomplete_value": true,
      "site": "00b4c5e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:bf0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b5ec",
      "incomplete_value": true,
      "site": "00b4b5ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c30:8"
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
      "definition_site": "00b4c5bc",
      "incomplete_value": true,
      "site": "00b4c5bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b5c8",
      "incomplete_value": true,
      "site": "00b4b5c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c5c4",
      "incomplete_value": false,
      "site": "00b4c5d8",
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
            "const:52e:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b5d0",
      "incomplete_value": false,
      "site": "00b4b5e4",
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
            "const:3d6:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c5b4",
      "READ",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c5c4",
      "PARAM",
      [
        "storage",
        "002a83d6",
        null,
        "string"
      ]
    ],
    [
      "00b4c5e0",
      "WRITE",
      [
        "storage",
        "01125c30",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c5b4",
      "READ",
      [
        "storage",
        "01126bf0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c5c4",
      "PARAM",
      [
        "storage",
        "002a852e",
        null,
        "string"
      ]
    ],
    [
      "00b4c5e0",
      "WRITE",
      [
        "storage",
        "01126bf0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b5ac.md#insn-00b4b5e4) · [`00b4b5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b5ac.md#insn-00b4b5ec) · [`00b4b5b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b5ac.md#insn-00b4b5b8)
- 新版 [`00b4c5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c5a0.md#insn-00b4c5d8) · [`00b4c5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c5a0.md#insn-00b4c5e0) · [`00b4c5ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c5a0.md#insn-00b4c5ac)

~~~diff
- 00b4b5e4 ["INT_ADD", "register:40f0:8", ["const:b4b5e4:8", "const:4:8"]]
- 00b4b5e4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4c5d8 ["INT_ADD", "register:40f0:8", ["const:b4c5d8:8", "const:4:8"]]
+ 00b4c5d8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4b5e4 bytes 7f3e0494
+ 00b4c5d8 bytes 763e0494
- 00b4b5ec ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c30:8"]]
- 00b4b5ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c5e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:bf0:8"]]
+ 00b4c5e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b5ec bytes 801a06f9
+ 00b4c5e0 bytes 80fa05f9
- 00b4b5b8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4c5ac ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4b5b8 bytes d42e00d0
+ 00b4c5ac bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0583f9499dc6f38bcc40a40b985e9f10"></a>

### [`00b4b61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b61c.md) → [`00b4c610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c610.md) _ZN8firebase4util13integer_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4c62c",
      "incomplete_value": false,
      "site": "00b4c630",
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
      "definition_site": "00b4b638",
      "incomplete_value": false,
      "site": "00b4b63c",
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
      "definition_site": "00b4c63c",
      "incomplete_value": true,
      "site": "00b4c648",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4b648",
      "incomplete_value": true,
      "site": "00b4b654",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4c62c",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4c63c",
      "DATA",
      [
        "storage",
        "01125c50",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4c62c",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4c63c",
      "DATA",
      [
        "storage",
        "01126c10",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b63c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b61c.md#insn-00b4b63c) · [`00b4b638`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b61c.md#insn-00b4b638) · [`00b4b640`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b61c.md#insn-00b4b640)
- 新版 [`00b4c630`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c610.md#insn-00b4c630) · [`00b4c62c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c610.md#insn-00b4c62c) · [`00b4c634`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c610.md#insn-00b4c634)

~~~diff
- 00b4b63c ["INT_ADD", "register:40f0:8", ["const:b4b63c:8", "const:4:8"]]
- 00b4b63c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4c630 ["INT_ADD", "register:40f0:8", ["const:b4c630:8", "const:4:8"]]
+ 00b4c630 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4b63c bytes a53e0494
+ 00b4c630 bytes 9c3e0494
- 00b4b638 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b4b638 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b638 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b638 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c62c ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4c62c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c62c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c62c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b638 bytes 00341591
+ 00b4c62c bytes 00681891
- 00b4b640 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4c634 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4b640 bytes c82e00d0
+ 00b4c634 bytes c82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cc64e3157c38dbb0ae50ad4826107754"></a>

### [`00b4b658`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b658.md) → [`00b4c64c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c64c.md) _ZN8firebase4util6intent19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16

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
      "definition_site": "00b4c678",
      "incomplete_value": true,
      "site": "00b4c678",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b684",
      "incomplete_value": true,
      "site": "00b4b684",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4c660",
      "incomplete_value": true,
      "site": "00b4c660",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b66c",
      "incomplete_value": true,
      "site": "00b4b66c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c66c",
      "incomplete_value": false,
      "site": "00b4c670",
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
            "const:aaf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b678",
      "incomplete_value": false,
      "site": "00b4b67c",
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
            "const:9e4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c65c",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c66c",
      "PARAM",
      [
        "storage",
        "002a29e4",
        null,
        "string"
      ]
    ],
    [
      "00b4c678",
      "WRITE",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c65c",
      "READ",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c66c",
      "PARAM",
      [
        "storage",
        "002a2aaf",
        null,
        "string"
      ]
    ],
    [
      "00b4c678",
      "WRITE",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b67c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b658.md#insn-00b4b67c) · [`00b4b684`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b658.md#insn-00b4b684) · [`00b4b664`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b658.md#insn-00b4b664)
- 新版 [`00b4c670`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c64c.md#insn-00b4c670) · [`00b4c678`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c64c.md#insn-00b4c678) · [`00b4c658`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c64c.md#insn-00b4c658)

~~~diff
- 00b4b67c ["INT_ADD", "register:40f0:8", ["const:b4b67c:8", "const:4:8"]]
- 00b4b67c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4c670 ["INT_ADD", "register:40f0:8", ["const:b4c670:8", "const:4:8"]]
+ 00b4c670 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4b67c bytes 593e0494
+ 00b4c670 bytes 503e0494
- 00b4b684 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
- 00b4b684 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c678 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c18:8"]]
+ 00b4c678 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b684 bytes 602e06f9
+ 00b4c678 bytes 600e06f9
- 00b4b664 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4c658 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4b664 bytes d32e00d0
+ 00b4c658 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3c40e4578355ca79c1ce458c5e5dcb8b"></a>

### [`00b4b698`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b698.md) → [`00b4c68c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c68c.md) _ZN8firebase4util6intent19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4c6b8",
      "incomplete_value": true,
      "site": "00b4c6b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b6c4",
      "incomplete_value": true,
      "site": "00b4b6c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4c6a0",
      "incomplete_value": true,
      "site": "00b4c6a0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b6ac",
      "incomplete_value": true,
      "site": "00b4b6ac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c6a8",
      "incomplete_value": false,
      "site": "00b4c6b0",
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
            "const:aaf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b6b4",
      "incomplete_value": false,
      "site": "00b4b6bc",
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
            "const:9e4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c69c",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c6a8",
      "PARAM",
      [
        "storage",
        "002a29e4",
        null,
        "string"
      ]
    ],
    [
      "00b4c6b8",
      "WRITE",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c69c",
      "READ",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c6a8",
      "PARAM",
      [
        "storage",
        "002a2aaf",
        null,
        "string"
      ]
    ],
    [
      "00b4c6b8",
      "WRITE",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b6bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b698.md#insn-00b4b6bc) · [`00b4b6c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b698.md#insn-00b4b6c4) · [`00b4b6a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b698.md#insn-00b4b6a4)
- 新版 [`00b4c6b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c68c.md#insn-00b4c6b0) · [`00b4c6b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c68c.md#insn-00b4c6b8) · [`00b4c698`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c68c.md#insn-00b4c698)

~~~diff
- 00b4b6bc ["INT_ADD", "register:40f0:8", ["const:b4b6bc:8", "const:4:8"]]
- 00b4b6bc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4c6b0 ["INT_ADD", "register:40f0:8", ["const:b4c6b0:8", "const:4:8"]]
+ 00b4c6b0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4b6bc bytes 493e0494
+ 00b4c6b0 bytes 403e0494
- 00b4b6c4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
- 00b4b6c4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c6b8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c18:8"]]
+ 00b4c6b8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b6c4 bytes 602e06f9
+ 00b4c6b8 bytes 600e06f9
- 00b4b6a4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4c698 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4b6a4 bytes d32e00d0
+ 00b4c698 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-c16936fb8e316617e8f27a251e978a07"></a>

### [`00b4b6d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b6d8.md) → [`00b4c6cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c6cc.md) _ZN8firebase4util6intent10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4c6fc",
      "incomplete_value": true,
      "site": "00b4c6fc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b708",
      "incomplete_value": true,
      "site": "00b4b708",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4c6e0",
      "incomplete_value": true,
      "site": "00b4c6e0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b6ec",
      "incomplete_value": true,
      "site": "00b4b6ec",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c6ec",
      "incomplete_value": false,
      "site": "00b4c6f4",
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
            "const:aaf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b6f8",
      "incomplete_value": false,
      "site": "00b4b700",
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
            "const:9e4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c6dc",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c6ec",
      "PARAM",
      [
        "storage",
        "002a29e4",
        null,
        "string"
      ]
    ],
    [
      "00b4c6fc",
      "WRITE",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c6dc",
      "READ",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c6ec",
      "PARAM",
      [
        "storage",
        "002a2aaf",
        null,
        "string"
      ]
    ],
    [
      "00b4c6fc",
      "WRITE",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b700`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b6d8.md#insn-00b4b700) · [`00b4b708`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b6d8.md#insn-00b4b708) · [`00b4b6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b6d8.md#insn-00b4b6e4)
- 新版 [`00b4c6f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c6cc.md#insn-00b4c6f4) · [`00b4c6fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c6cc.md#insn-00b4c6fc) · [`00b4c6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c6cc.md#insn-00b4c6d8)

~~~diff
- 00b4b700 ["INT_ADD", "register:40f0:8", ["const:b4b700:8", "const:4:8"]]
- 00b4b700 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4c6f4 ["INT_ADD", "register:40f0:8", ["const:b4c6f4:8", "const:4:8"]]
+ 00b4c6f4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4b700 bytes 383e0494
+ 00b4c6f4 bytes 2f3e0494
- 00b4b708 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
- 00b4b708 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c6fc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c18:8"]]
+ 00b4c6fc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b708 bytes 602e06f9
+ 00b4c6fc bytes 600e06f9
- 00b4b6e4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4c6d8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4b6e4 bytes d32e00d0
+ 00b4c6d8 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2d232b24414977ad2efa461b488b304b"></a>

### [`00b4b71c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b71c.md) → [`00b4c710`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c710.md) _ZN8firebase4util6intent10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4c740",
      "incomplete_value": true,
      "site": "00b4c740",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b74c",
      "incomplete_value": true,
      "site": "00b4b74c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4c724",
      "incomplete_value": true,
      "site": "00b4c724",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b730",
      "incomplete_value": true,
      "site": "00b4b730",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c72c",
      "incomplete_value": false,
      "site": "00b4c738",
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
            "const:aaf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b738",
      "incomplete_value": false,
      "site": "00b4b744",
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
            "const:9e4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c720",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c72c",
      "PARAM",
      [
        "storage",
        "002a29e4",
        null,
        "string"
      ]
    ],
    [
      "00b4c740",
      "WRITE",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c720",
      "READ",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c72c",
      "PARAM",
      [
        "storage",
        "002a2aaf",
        null,
        "string"
      ]
    ],
    [
      "00b4c740",
      "WRITE",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b744`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b71c.md#insn-00b4b744) · [`00b4b74c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b71c.md#insn-00b4b74c) · [`00b4b728`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b71c.md#insn-00b4b728)
- 新版 [`00b4c738`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c710.md#insn-00b4c738) · [`00b4c740`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c710.md#insn-00b4c740) · [`00b4c71c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c710.md#insn-00b4c71c)

~~~diff
- 00b4b744 ["INT_ADD", "register:40f0:8", ["const:b4b744:8", "const:4:8"]]
- 00b4b744 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4c738 ["INT_ADD", "register:40f0:8", ["const:b4c738:8", "const:4:8"]]
+ 00b4c738 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4b744 bytes 273e0494
+ 00b4c738 bytes 1e3e0494
- 00b4b74c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
- 00b4b74c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c740 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c18:8"]]
+ 00b4c740 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b74c bytes 602e06f9
+ 00b4c740 bytes 600e06f9
- 00b4b728 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4c71c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4b728 bytes d32e00d0
+ 00b4c71c bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-716466e6a280c30f5c6853063409e653"></a>

### [`00b4b76c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b76c.md) → [`00b4c760`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c760.md) _ZN8firebase4util6intent15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4c7e8",
      "incomplete_value": true,
      "site": "00b4c7e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b7f4",
      "incomplete_value": true,
      "site": "00b4b7f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "definition_site": "00b4c794",
      "incomplete_value": true,
      "site": "00b4c7a0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c18:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b7a0",
      "incomplete_value": true,
      "site": "00b4b7ac",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c58:8"
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
      "00b4c774",
      "READ",
      [
        "storage",
        "01125c60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c794",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c7e8",
      "WRITE",
      [
        "storage",
        "01125c60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c774",
      "READ",
      [
        "storage",
        "01126c20",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c794",
      "READ",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c7e8",
      "WRITE",
      [
        "storage",
        "01126c20",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b7ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b76c.md#insn-00b4b7ac) · [`00b4b7f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b76c.md#insn-00b4b7f4) · [`00b4b77c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b76c.md#insn-00b4b77c)
- 新版 [`00b4c7a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c760.md#insn-00b4c7a0) · [`00b4c7e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c760.md#insn-00b4c7e8) · [`00b4c770`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c760.md#insn-00b4c770)

~~~diff
- 00b4b7ac ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b7ac ["INT_ADD", "register:40f0:8", ["const:b4b7ac:8", "const:4:8"]]
- 00b4b7ac ["CALLIND", null, ["register:0:8"]]
+ 00b4c7a0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c7a0 ["INT_ADD", "register:40f0:8", ["const:b4c7a0:8", "const:4:8"]]
+ 00b4c7a0 ["CALLIND", null, ["register:0:8"]]
- 00b4b7ac bytes 00013fd6
+ 00b4c7a0 bytes 00013fd6
- 00b4b7f4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4b7f4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c60:8"]]
- 00b4b7f4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4c7e8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4c7e8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c20:8"]]
+ 00b4c7e8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4b7f4 bytes a0823139
+ 00b4c7e8 bytes a0823039
- 00b4b77c ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4c770 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4b77c bytes d52e00d0
+ 00b4c770 bytes d52e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5ea9c76acff80df0a6dd2095be4c9dcb"></a>

### [`00b4b808`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b808.md) → [`00b4c7fc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c7fc.md) _ZN8firebase4util6intent12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4c838",
      "incomplete_value": true,
      "site": "00b4c838",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c20:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b844",
      "incomplete_value": true,
      "site": "00b4b844",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c60:8"
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
      "definition_site": "00b4c888",
      "incomplete_value": true,
      "site": "00b4c888",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b894",
      "incomplete_value": true,
      "site": "00b4b894",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "definition_site": "00b4c814",
      "incomplete_value": true,
      "site": "00b4c814",
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
      "definition_site": "00b4b820",
      "incomplete_value": true,
      "site": "00b4b820",
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
      "00b4c810",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c81c",
      "READ",
      [
        "storage",
        "01125c60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c838",
      "WRITE",
      [
        "storage",
        "01125c60",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4c810",
      "READ",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c81c",
      "READ",
      [
        "storage",
        "01126c20",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4c838",
      "WRITE",
      [
        "storage",
        "01126c20",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b844`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b808.md#insn-00b4b844) · [`00b4b890`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b808.md#insn-00b4b890) · [`00b4b894`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b808.md#insn-00b4b894)
- 新版 [`00b4c838`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c7fc.md#insn-00b4c838) · [`00b4c884`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c7fc.md#insn-00b4c884) · [`00b4c888`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c7fc.md#insn-00b4c888)

~~~diff
- 00b4b844 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4b844 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4b844 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c60:8"]]
- 00b4b844 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4c838 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4c838 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4c838 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c20:8"]]
+ 00b4c838 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4b844 bytes bf823139
+ 00b4c838 bytes bf823039
- 00b4b890 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4b890 ["INT_ADD", "register:40f0:8", ["const:b4b890:8", "const:4:8"]]
- 00b4b890 ["CALLIND", null, ["register:0:8"]]
+ 00b4c884 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4c884 ["INT_ADD", "register:40f0:8", ["const:b4c884:8", "const:4:8"]]
+ 00b4c884 ["CALLIND", null, ["register:0:8"]]
- 00b4b890 bytes 00013fd6
+ 00b4c884 bytes 00013fd6
- 00b4b894 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
- 00b4b894 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4b894 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4c888 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c18:8"]]
+ 00b4c888 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4c888 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4b894 bytes 9f2e06f9
+ 00b4c888 bytes 9f0e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ea6924f09e56921308e988836a779d08"></a>

### [`00b4b8a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b8a8.md) → [`00b4c89c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c89c.md) _ZN8firebase4util6intent14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4c8dc",
      "incomplete_value": true,
      "site": "00b4c8dc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b8e8",
      "incomplete_value": true,
      "site": "00b4b8e8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "definition_site": "00b4c8b8",
      "incomplete_value": true,
      "site": "00b4c8b8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b8c4",
      "incomplete_value": true,
      "site": "00b4b8c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c8c0",
      "incomplete_value": false,
      "site": "00b4c8d4",
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
            "const:aaf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b8cc",
      "incomplete_value": false,
      "site": "00b4b8e0",
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
            "const:9e4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c8b0",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c8c0",
      "PARAM",
      [
        "storage",
        "002a29e4",
        null,
        "string"
      ]
    ],
    [
      "00b4c8dc",
      "WRITE",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c8b0",
      "READ",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c8c0",
      "PARAM",
      [
        "storage",
        "002a2aaf",
        null,
        "string"
      ]
    ],
    [
      "00b4c8dc",
      "WRITE",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b8a8.md#insn-00b4b8e0) · [`00b4b8e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b8a8.md#insn-00b4b8e8) · [`00b4b8b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b8a8.md#insn-00b4b8b4)
- 新版 [`00b4c8d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c89c.md#insn-00b4c8d4) · [`00b4c8dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c89c.md#insn-00b4c8dc) · [`00b4c8a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c89c.md#insn-00b4c8a8)

~~~diff
- 00b4b8e0 ["INT_ADD", "register:40f0:8", ["const:b4b8e0:8", "const:4:8"]]
- 00b4b8e0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4c8d4 ["INT_ADD", "register:40f0:8", ["const:b4c8d4:8", "const:4:8"]]
+ 00b4c8d4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4b8e0 bytes c03d0494
+ 00b4c8d4 bytes b73d0494
- 00b4b8e8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
- 00b4b8e8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c8dc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c18:8"]]
+ 00b4c8dc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b8e8 bytes 802e06f9
+ 00b4c8dc bytes 800e06f9
- 00b4b8b4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4c8a8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4b8b4 bytes d42e00d0
+ 00b4c8a8 bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f27a67c83ffa9e1735a17e68d817d440"></a>

### [`00b4b918`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b918.md) → [`00b4c90c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c90c.md) _ZN8firebase4util6intent11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b600`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b600.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5c5d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c5d0.md) · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4c928",
      "incomplete_value": false,
      "site": "00b4c92c",
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
      "definition_site": "00b4b934",
      "incomplete_value": false,
      "site": "00b4b938",
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
      "definition_site": "00b4c938",
      "incomplete_value": true,
      "site": "00b4c944",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4b944",
      "incomplete_value": true,
      "site": "00b4b950",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4c928",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4c938",
      "DATA",
      [
        "storage",
        "01125c68",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4c928",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4c938",
      "DATA",
      [
        "storage",
        "01126c28",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b938`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b918.md#insn-00b4b938) · [`00b4b934`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b918.md#insn-00b4b934) · [`00b4b93c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b918.md#insn-00b4b93c)
- 新版 [`00b4c92c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c90c.md#insn-00b4c92c) · [`00b4c928`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c90c.md#insn-00b4c928) · [`00b4c930`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c90c.md#insn-00b4c930)

~~~diff
- 00b4b938 ["INT_ADD", "register:40f0:8", ["const:b4b938:8", "const:4:8"]]
- 00b4b938 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4c92c ["INT_ADD", "register:40f0:8", ["const:b4c92c:8", "const:4:8"]]
+ 00b4c92c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4b938 bytes e63d0494
+ 00b4c92c bytes dd3d0494
- 00b4b934 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4b934 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b934 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b934 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c928 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4c928 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c928 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c928 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b934 bytes 002c0c91
+ 00b4c928 bytes 008c1191
- 00b4b93c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4c930 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4b93c bytes c82e00d0
+ 00b4c930 bytes c82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-80ae53d30d13ea9a93293f54cd0ea429"></a>

### [`00b4b954`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b954.md) → [`00b4c948`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c948.md) _ZN8firebase4util6intent13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4c988",
      "incomplete_value": true,
      "site": "00b4c988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c18:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b994",
      "incomplete_value": true,
      "site": "00b4b994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c58:8"
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
      "definition_site": "00b4c964",
      "incomplete_value": true,
      "site": "00b4c964",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b970",
      "incomplete_value": true,
      "site": "00b4b970",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4c96c",
      "incomplete_value": false,
      "site": "00b4c980",
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
            "const:aaf:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4b978",
      "incomplete_value": false,
      "site": "00b4b98c",
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
            "const:9e4:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4c95c",
      "READ",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c96c",
      "PARAM",
      [
        "storage",
        "002a29e4",
        null,
        "string"
      ]
    ],
    [
      "00b4c988",
      "WRITE",
      [
        "storage",
        "01125c58",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4c95c",
      "READ",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4c96c",
      "PARAM",
      [
        "storage",
        "002a2aaf",
        null,
        "string"
      ]
    ],
    [
      "00b4c988",
      "WRITE",
      [
        "storage",
        "01126c18",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b954.md#insn-00b4b98c) · [`00b4b994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b954.md#insn-00b4b994) · [`00b4b960`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b954.md#insn-00b4b960)
- 新版 [`00b4c980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c948.md#insn-00b4c980) · [`00b4c988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c948.md#insn-00b4c988) · [`00b4c954`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c948.md#insn-00b4c954)

~~~diff
- 00b4b98c ["INT_ADD", "register:40f0:8", ["const:b4b98c:8", "const:4:8"]]
- 00b4b98c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4c980 ["INT_ADD", "register:40f0:8", ["const:b4c980:8", "const:4:8"]]
+ 00b4c980 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4b98c bytes 953d0494
+ 00b4c980 bytes 8c3d0494
- 00b4b994 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
- 00b4b994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4c988 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c18:8"]]
+ 00b4c988 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4b994 bytes 802e06f9
+ 00b4c988 bytes 800e06f9
- 00b4b960 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4c954 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4b960 bytes d42e00d0
+ 00b4c954 bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cceff6404cf655972f265e0a3571c28d"></a>

### [`00b4b9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b9c4.md) → [`00b4c9b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c9b8.md) _ZN8firebase4util6intent10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4c9d4",
      "incomplete_value": false,
      "site": "00b4c9d8",
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
      "definition_site": "00b4b9e0",
      "incomplete_value": false,
      "site": "00b4b9e4",
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
      "definition_site": "00b4c9e4",
      "incomplete_value": true,
      "site": "00b4c9f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4b9f0",
      "incomplete_value": true,
      "site": "00b4b9fc",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4c9d4",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4c9e4",
      "DATA",
      [
        "storage",
        "01125c90",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4c9d4",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4c9e4",
      "DATA",
      [
        "storage",
        "01126c50",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4b9e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b9c4.md#insn-00b4b9e4) · [`00b4b9e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b9c4.md#insn-00b4b9e0) · [`00b4b9e8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4b9c4.md#insn-00b4b9e8)
- 新版 [`00b4c9d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c9b8.md#insn-00b4c9d8) · [`00b4c9d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c9b8.md#insn-00b4c9d4) · [`00b4c9dc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c9b8.md#insn-00b4c9dc)

~~~diff
- 00b4b9e4 ["INT_ADD", "register:40f0:8", ["const:b4b9e4:8", "const:4:8"]]
- 00b4b9e4 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4c9d8 ["INT_ADD", "register:40f0:8", ["const:b4c9d8:8", "const:4:8"]]
+ 00b4c9d8 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4b9e4 bytes bb3d0494
+ 00b4c9d8 bytes b23d0494
- 00b4b9e0 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b4b9e0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b9e0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4b9e0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4c9d4 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4c9d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c9d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4c9d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4b9e0 bytes 00341591
+ 00b4c9d4 bytes 00681891
- 00b4b9e8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4c9dc ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4b9e8 bytes c82e00d0
+ 00b4c9dc bytes c82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2c551ebc15b940eb219bcb23ba8b7b9"></a>

### [`00b4ba00`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba00.md) → [`00b4c9f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c9f4.md) _ZN8firebase4util8iterable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

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
      "definition_site": "00b4ca20",
      "incomplete_value": true,
      "site": "00b4ca20",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ba2c",
      "incomplete_value": true,
      "site": "00b4ba2c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4ca08",
      "incomplete_value": true,
      "site": "00b4ca08",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ba14",
      "incomplete_value": true,
      "site": "00b4ba14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ca14",
      "incomplete_value": false,
      "site": "00b4ca18",
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
            "const:969:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ba20",
      "incomplete_value": false,
      "site": "00b4ba24",
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
            "const:929:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ca04",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ca14",
      "PARAM",
      [
        "storage",
        "0029f929",
        null,
        "string"
      ]
    ],
    [
      "00b4ca20",
      "WRITE",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ca04",
      "READ",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ca14",
      "PARAM",
      [
        "storage",
        "0029f969",
        null,
        "string"
      ]
    ],
    [
      "00b4ca20",
      "WRITE",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ba24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba00.md#insn-00b4ba24) · [`00b4ba2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba00.md#insn-00b4ba2c) · [`00b4ba0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba00.md#insn-00b4ba0c)
- 新版 [`00b4ca18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c9f4.md#insn-00b4ca18) · [`00b4ca20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c9f4.md#insn-00b4ca20) · [`00b4ca00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4c9f4.md#insn-00b4ca00)

~~~diff
- 00b4ba24 ["INT_ADD", "register:40f0:8", ["const:b4ba24:8", "const:4:8"]]
- 00b4ba24 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4ca18 ["INT_ADD", "register:40f0:8", ["const:b4ca18:8", "const:4:8"]]
+ 00b4ca18 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4ba24 bytes 6f3d0494
+ 00b4ca18 bytes 663d0494
- 00b4ba2c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c98:8"]]
- 00b4ba2c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ca20 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00b4ca20 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ba2c bytes 604e06f9
+ 00b4ca20 bytes 602e06f9
- 00b4ba0c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4ca00 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4ba0c bytes d32e00d0
+ 00b4ca00 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a11a8699f05c169a3a967d841419f9f5"></a>

### [`00b4ba40`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba40.md) → [`00b4ca34`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ca34.md) _ZN8firebase4util8iterable19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4ca60",
      "incomplete_value": true,
      "site": "00b4ca60",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ba6c",
      "incomplete_value": true,
      "site": "00b4ba6c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4ca48",
      "incomplete_value": true,
      "site": "00b4ca48",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ba54",
      "incomplete_value": true,
      "site": "00b4ba54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ca50",
      "incomplete_value": false,
      "site": "00b4ca58",
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
            "const:969:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ba5c",
      "incomplete_value": false,
      "site": "00b4ba64",
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
            "const:929:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ca44",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ca50",
      "PARAM",
      [
        "storage",
        "0029f929",
        null,
        "string"
      ]
    ],
    [
      "00b4ca60",
      "WRITE",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ca44",
      "READ",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ca50",
      "PARAM",
      [
        "storage",
        "0029f969",
        null,
        "string"
      ]
    ],
    [
      "00b4ca60",
      "WRITE",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ba64`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba40.md#insn-00b4ba64) · [`00b4ba6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba40.md#insn-00b4ba6c) · [`00b4ba4c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba40.md#insn-00b4ba4c)
- 新版 [`00b4ca58`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ca34.md#insn-00b4ca58) · [`00b4ca60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ca34.md#insn-00b4ca60) · [`00b4ca40`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ca34.md#insn-00b4ca40)

~~~diff
- 00b4ba64 ["INT_ADD", "register:40f0:8", ["const:b4ba64:8", "const:4:8"]]
- 00b4ba64 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4ca58 ["INT_ADD", "register:40f0:8", ["const:b4ca58:8", "const:4:8"]]
+ 00b4ca58 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4ba64 bytes 5f3d0494
+ 00b4ca58 bytes 563d0494
- 00b4ba6c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c98:8"]]
- 00b4ba6c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ca60 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00b4ca60 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ba6c bytes 604e06f9
+ 00b4ca60 bytes 602e06f9
- 00b4ba4c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4ca40 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4ba4c bytes d32e00d0
+ 00b4ca40 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-493dd77fe108af1e2dbe248838d4a5a1"></a>

### [`00b4ba80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba80.md) → [`00b4ca74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ca74.md) _ZN8firebase4util8iterable10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4caa4",
      "incomplete_value": true,
      "site": "00b4caa4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bab0",
      "incomplete_value": true,
      "site": "00b4bab0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4ca88",
      "incomplete_value": true,
      "site": "00b4ca88",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ba94",
      "incomplete_value": true,
      "site": "00b4ba94",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ca94",
      "incomplete_value": false,
      "site": "00b4ca9c",
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
            "const:969:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4baa0",
      "incomplete_value": false,
      "site": "00b4baa8",
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
            "const:929:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ca84",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ca94",
      "PARAM",
      [
        "storage",
        "0029f929",
        null,
        "string"
      ]
    ],
    [
      "00b4caa4",
      "WRITE",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ca84",
      "READ",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ca94",
      "PARAM",
      [
        "storage",
        "0029f969",
        null,
        "string"
      ]
    ],
    [
      "00b4caa4",
      "WRITE",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4baa8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba80.md#insn-00b4baa8) · [`00b4bab0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba80.md#insn-00b4bab0) · [`00b4ba8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4ba80.md#insn-00b4ba8c)
- 新版 [`00b4ca9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ca74.md#insn-00b4ca9c) · [`00b4caa4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ca74.md#insn-00b4caa4) · [`00b4ca80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ca74.md#insn-00b4ca80)

~~~diff
- 00b4baa8 ["INT_ADD", "register:40f0:8", ["const:b4baa8:8", "const:4:8"]]
- 00b4baa8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4ca9c ["INT_ADD", "register:40f0:8", ["const:b4ca9c:8", "const:4:8"]]
+ 00b4ca9c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4baa8 bytes 4e3d0494
+ 00b4ca9c bytes 453d0494
- 00b4bab0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c98:8"]]
- 00b4bab0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4caa4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00b4caa4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bab0 bytes 604e06f9
+ 00b4caa4 bytes 602e06f9
- 00b4ba8c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4ca80 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4ba8c bytes d32e00d0
+ 00b4ca80 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-ffad476bb8595e833627480ac420a09f"></a>

### [`00b4bac4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bac4.md) → [`00b4cab8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cab8.md) _ZN8firebase4util8iterable10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4cae8",
      "incomplete_value": true,
      "site": "00b4cae8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4baf4",
      "incomplete_value": true,
      "site": "00b4baf4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c98:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4cacc",
      "incomplete_value": true,
      "site": "00b4cacc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bad8",
      "incomplete_value": true,
      "site": "00b4bad8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4cad4",
      "incomplete_value": false,
      "site": "00b4cae0",
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
            "const:969:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bae0",
      "incomplete_value": false,
      "site": "00b4baec",
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
            "const:929:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4cac8",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cad4",
      "PARAM",
      [
        "storage",
        "0029f929",
        null,
        "string"
      ]
    ],
    [
      "00b4cae8",
      "WRITE",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cac8",
      "READ",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cad4",
      "PARAM",
      [
        "storage",
        "0029f969",
        null,
        "string"
      ]
    ],
    [
      "00b4cae8",
      "WRITE",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4baec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bac4.md#insn-00b4baec) · [`00b4baf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bac4.md#insn-00b4baf4) · [`00b4bad0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bac4.md#insn-00b4bad0)
- 新版 [`00b4cae0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cab8.md#insn-00b4cae0) · [`00b4cae8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cab8.md#insn-00b4cae8) · [`00b4cac4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cab8.md#insn-00b4cac4)

~~~diff
- 00b4baec ["INT_ADD", "register:40f0:8", ["const:b4baec:8", "const:4:8"]]
- 00b4baec ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4cae0 ["INT_ADD", "register:40f0:8", ["const:b4cae0:8", "const:4:8"]]
+ 00b4cae0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4baec bytes 3d3d0494
+ 00b4cae0 bytes 343d0494
- 00b4baf4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c98:8"]]
- 00b4baf4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cae8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c58:8"]]
+ 00b4cae8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4baf4 bytes 604e06f9
+ 00b4cae8 bytes 602e06f9
- 00b4bad0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4cac4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4bad0 bytes d32e00d0
+ 00b4cac4 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7de9d754f0fdbd7c1c3e454801100f4f"></a>

### [`00b4bb14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bb14.md) → [`00b4cb08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cb08.md) _ZN8firebase4util8iterable15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4cb90",
      "incomplete_value": true,
      "site": "00b4cb90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bb9c",
      "incomplete_value": true,
      "site": "00b4bb9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "definition_site": "00b4cb3c",
      "incomplete_value": true,
      "site": "00b4cb48",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c58:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bb48",
      "incomplete_value": true,
      "site": "00b4bb54",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c98:8"
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
      "00b4cb1c",
      "READ",
      [
        "storage",
        "01125ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cb3c",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cb90",
      "WRITE",
      [
        "storage",
        "01125ca0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4cb1c",
      "READ",
      [
        "storage",
        "01126c60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cb3c",
      "READ",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cb90",
      "WRITE",
      [
        "storage",
        "01126c60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bb54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bb14.md#insn-00b4bb54) · [`00b4bb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bb14.md#insn-00b4bb9c) · [`00b4bb24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bb14.md#insn-00b4bb24)
- 新版 [`00b4cb48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cb08.md#insn-00b4cb48) · [`00b4cb90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cb08.md#insn-00b4cb90) · [`00b4cb18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cb08.md#insn-00b4cb18)

~~~diff
- 00b4bb54 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4bb54 ["INT_ADD", "register:40f0:8", ["const:b4bb54:8", "const:4:8"]]
- 00b4bb54 ["CALLIND", null, ["register:0:8"]]
+ 00b4cb48 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4cb48 ["INT_ADD", "register:40f0:8", ["const:b4cb48:8", "const:4:8"]]
+ 00b4cb48 ["CALLIND", null, ["register:0:8"]]
- 00b4bb54 bytes 00013fd6
+ 00b4cb48 bytes 00013fd6
- 00b4bb9c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4bb9c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ca0:8"]]
- 00b4bb9c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4cb90 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4cb90 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c60:8"]]
+ 00b4cb90 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4bb9c bytes a0823239
+ 00b4cb90 bytes a0823139
- 00b4bb24 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4cb18 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4bb24 bytes d52e00d0
+ 00b4cb18 bytes d52e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0dee755ab16179cd21a10c45b9b5a59f"></a>

### [`00b4bbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bbb0.md) → [`00b4cba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cba4.md) _ZN8firebase4util8iterable12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4cbe0",
      "incomplete_value": true,
      "site": "00b4cbe0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c60:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bbec",
      "incomplete_value": true,
      "site": "00b4bbec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ca0:8"
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
      "definition_site": "00b4cc30",
      "incomplete_value": true,
      "site": "00b4cc30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bc3c",
      "incomplete_value": true,
      "site": "00b4bc3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "definition_site": "00b4cbbc",
      "incomplete_value": true,
      "site": "00b4cbbc",
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
      "definition_site": "00b4bbc8",
      "incomplete_value": true,
      "site": "00b4bbc8",
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
      "00b4cbb8",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cbc4",
      "READ",
      [
        "storage",
        "01125ca0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cbe0",
      "WRITE",
      [
        "storage",
        "01125ca0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4cbb8",
      "READ",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cbc4",
      "READ",
      [
        "storage",
        "01126c60",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cbe0",
      "WRITE",
      [
        "storage",
        "01126c60",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bbec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bbb0.md#insn-00b4bbec) · [`00b4bc38`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bbb0.md#insn-00b4bc38) · [`00b4bc3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bbb0.md#insn-00b4bc3c)
- 新版 [`00b4cbe0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cba4.md#insn-00b4cbe0) · [`00b4cc2c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cba4.md#insn-00b4cc2c) · [`00b4cc30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cba4.md#insn-00b4cc30)

~~~diff
- 00b4bbec ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4bbec ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4bbec ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ca0:8"]]
- 00b4bbec ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4cbe0 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4cbe0 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4cbe0 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c60:8"]]
+ 00b4cbe0 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4bbec bytes bf823239
+ 00b4cbe0 bytes bf823139
- 00b4bc38 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4bc38 ["INT_ADD", "register:40f0:8", ["const:b4bc38:8", "const:4:8"]]
- 00b4bc38 ["CALLIND", null, ["register:0:8"]]
+ 00b4cc2c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4cc2c ["INT_ADD", "register:40f0:8", ["const:b4cc2c:8", "const:4:8"]]
+ 00b4cc2c ["CALLIND", null, ["register:0:8"]]
- 00b4bc38 bytes 00013fd6
+ 00b4cc2c bytes 00013fd6
- 00b4bc3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
- 00b4bc3c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4bc3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4cc30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00b4cc30 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4cc30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4bc3c bytes 9f4e06f9
+ 00b4cc30 bytes 9f2e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-92aed53372da01fbf9f2e185f11b882e"></a>

### [`00b4bc50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bc50.md) → [`00b4cc44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cc44.md) _ZN8firebase4util8iterable14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4cc84",
      "incomplete_value": true,
      "site": "00b4cc84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bc90",
      "incomplete_value": true,
      "site": "00b4bc90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "definition_site": "00b4cc60",
      "incomplete_value": true,
      "site": "00b4cc60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bc6c",
      "incomplete_value": true,
      "site": "00b4bc6c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4cc68",
      "incomplete_value": false,
      "site": "00b4cc7c",
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
            "const:969:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bc74",
      "incomplete_value": false,
      "site": "00b4bc88",
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
            "const:929:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4cc58",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc68",
      "PARAM",
      [
        "storage",
        "0029f929",
        null,
        "string"
      ]
    ],
    [
      "00b4cc84",
      "WRITE",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cc58",
      "READ",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cc68",
      "PARAM",
      [
        "storage",
        "0029f969",
        null,
        "string"
      ]
    ],
    [
      "00b4cc84",
      "WRITE",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bc88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bc50.md#insn-00b4bc88) · [`00b4bc90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bc50.md#insn-00b4bc90) · [`00b4bc5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bc50.md#insn-00b4bc5c)
- 新版 [`00b4cc7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cc44.md#insn-00b4cc7c) · [`00b4cc84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cc44.md#insn-00b4cc84) · [`00b4cc50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cc44.md#insn-00b4cc50)

~~~diff
- 00b4bc88 ["INT_ADD", "register:40f0:8", ["const:b4bc88:8", "const:4:8"]]
- 00b4bc88 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4cc7c ["INT_ADD", "register:40f0:8", ["const:b4cc7c:8", "const:4:8"]]
+ 00b4cc7c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4bc88 bytes d63c0494
+ 00b4cc7c bytes cd3c0494
- 00b4bc90 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
- 00b4bc90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cc84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00b4cc84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bc90 bytes 804e06f9
+ 00b4cc84 bytes 802e06f9
- 00b4bc5c ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4cc50 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4bc5c bytes d42e00d0
+ 00b4cc50 bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7bdddf27770f31ba41de178c577afd96"></a>

### [`00b4bcc0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bcc0.md) → [`00b4ccb4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ccb4.md) _ZN8firebase4util8iterable11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b4ccd0",
      "incomplete_value": false,
      "site": "00b4ccd4",
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
      "definition_site": "00b4bcdc",
      "incomplete_value": false,
      "site": "00b4bce0",
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
      "definition_site": "00b4cce0",
      "incomplete_value": true,
      "site": "00b4ccec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4bcec",
      "incomplete_value": true,
      "site": "00b4bcf8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4ccd0",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4cce0",
      "DATA",
      [
        "storage",
        "01125ca8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4ccd0",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4cce0",
      "DATA",
      [
        "storage",
        "01126c68",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bce0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bcc0.md#insn-00b4bce0) · [`00b4bcdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bcc0.md#insn-00b4bcdc) · [`00b4bce4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bcc0.md#insn-00b4bce4)
- 新版 [`00b4ccd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ccb4.md#insn-00b4ccd4) · [`00b4ccd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ccb4.md#insn-00b4ccd0) · [`00b4ccd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ccb4.md#insn-00b4ccd8)

~~~diff
- 00b4bce0 ["INT_ADD", "register:40f0:8", ["const:b4bce0:8", "const:4:8"]]
- 00b4bce0 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4ccd4 ["INT_ADD", "register:40f0:8", ["const:b4ccd4:8", "const:4:8"]]
+ 00b4ccd4 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4bce0 bytes fc3c0494
+ 00b4ccd4 bytes f33c0494
- 00b4bcdc ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4bcdc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bcdc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bcdc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4ccd0 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4ccd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ccd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4ccd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4bcdc bytes 002c0c91
+ 00b4ccd0 bytes 008c1191
- 00b4bce4 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4ccd8 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4bce4 bytes c82e00d0
+ 00b4ccd8 bytes c82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8e089d479589f327b5ad0ce1a99f4172"></a>

### [`00b4bcfc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bcfc.md) → [`00b4ccf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ccf0.md) _ZN8firebase4util8iterable13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4cd30",
      "incomplete_value": true,
      "site": "00b4cd30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c58:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bd3c",
      "incomplete_value": true,
      "site": "00b4bd3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c98:8"
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
      "definition_site": "00b4cd0c",
      "incomplete_value": true,
      "site": "00b4cd0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bd18",
      "incomplete_value": true,
      "site": "00b4bd18",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4cd14",
      "incomplete_value": false,
      "site": "00b4cd28",
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
            "const:969:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bd20",
      "incomplete_value": false,
      "site": "00b4bd34",
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
            "const:929:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4cd04",
      "READ",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cd14",
      "PARAM",
      [
        "storage",
        "0029f929",
        null,
        "string"
      ]
    ],
    [
      "00b4cd30",
      "WRITE",
      [
        "storage",
        "01125c98",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cd04",
      "READ",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cd14",
      "PARAM",
      [
        "storage",
        "0029f969",
        null,
        "string"
      ]
    ],
    [
      "00b4cd30",
      "WRITE",
      [
        "storage",
        "01126c58",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bd34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bcfc.md#insn-00b4bd34) · [`00b4bd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bcfc.md#insn-00b4bd3c) · [`00b4bd08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bcfc.md#insn-00b4bd08)
- 新版 [`00b4cd28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ccf0.md#insn-00b4cd28) · [`00b4cd30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ccf0.md#insn-00b4cd30) · [`00b4ccfc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ccf0.md#insn-00b4ccfc)

~~~diff
- 00b4bd34 ["INT_ADD", "register:40f0:8", ["const:b4bd34:8", "const:4:8"]]
- 00b4bd34 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4cd28 ["INT_ADD", "register:40f0:8", ["const:b4cd28:8", "const:4:8"]]
+ 00b4cd28 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4bd34 bytes ab3c0494
+ 00b4cd28 bytes a23c0494
- 00b4bd3c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c98:8"]]
- 00b4bd3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cd30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c58:8"]]
+ 00b4cd30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bd3c bytes 804e06f9
+ 00b4cd30 bytes 802e06f9
- 00b4bd08 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4ccfc ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4bd08 bytes d42e00d0
+ 00b4ccfc bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d7e86ef490dc43707fd92d9d57d54d10"></a>

### [`00b4bd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bd6c.md) → [`00b4cd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cd60.md) _ZN8firebase4util8iterable10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4cd7c",
      "incomplete_value": false,
      "site": "00b4cd80",
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
      "definition_site": "00b4bd88",
      "incomplete_value": false,
      "site": "00b4bd8c",
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
      "definition_site": "00b4cd8c",
      "incomplete_value": true,
      "site": "00b4cd98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4bd98",
      "incomplete_value": true,
      "site": "00b4bda4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4cd7c",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4cd8c",
      "DATA",
      [
        "storage",
        "01125cb0",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4cd7c",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4cd8c",
      "DATA",
      [
        "storage",
        "01126c70",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bd8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bd6c.md#insn-00b4bd8c) · [`00b4bd88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bd6c.md#insn-00b4bd88) · [`00b4bd90`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bd6c.md#insn-00b4bd90)
- 新版 [`00b4cd80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cd60.md#insn-00b4cd80) · [`00b4cd7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cd60.md#insn-00b4cd7c) · [`00b4cd84`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cd60.md#insn-00b4cd84)

~~~diff
- 00b4bd8c ["INT_ADD", "register:40f0:8", ["const:b4bd8c:8", "const:4:8"]]
- 00b4bd8c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4cd80 ["INT_ADD", "register:40f0:8", ["const:b4cd80:8", "const:4:8"]]
+ 00b4cd80 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4bd8c bytes d13c0494
+ 00b4cd80 bytes c83c0494
- 00b4bd88 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b4bd88 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bd88 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4bd88 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4cd7c ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4cd7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cd7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4cd7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4bd88 bytes 00341591
+ 00b4cd7c bytes 00681891
- 00b4bd90 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4cd84 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4bd90 bytes c82e00d0
+ 00b4cd84 bytes c82e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-172a2a04fd66bfb016551cb4cd78790e"></a>

### [`00b4bda8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bda8.md) → [`00b4cd9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cd9c.md) _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_

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
      "definition_site": "00b4cdc8",
      "incomplete_value": true,
      "site": "00b4cdc8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bdd4",
      "incomplete_value": true,
      "site": "00b4bdd4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4cdb0",
      "incomplete_value": true,
      "site": "00b4cdb0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bdbc",
      "incomplete_value": true,
      "site": "00b4bdbc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4cdbc",
      "incomplete_value": false,
      "site": "00b4cdc0",
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
            "const:253:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bdc8",
      "incomplete_value": false,
      "site": "00b4bdcc",
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
            "const:fb:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4cdac",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cdbc",
      "PARAM",
      [
        "storage",
        "002a70fb",
        null,
        "string"
      ]
    ],
    [
      "00b4cdc8",
      "WRITE",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cdac",
      "READ",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cdbc",
      "PARAM",
      [
        "storage",
        "002a7253",
        null,
        "string"
      ]
    ],
    [
      "00b4cdc8",
      "WRITE",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bdcc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bda8.md#insn-00b4bdcc) · [`00b4bdd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bda8.md#insn-00b4bdd4) · [`00b4bdb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bda8.md#insn-00b4bdb4)
- 新版 [`00b4cdc0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cd9c.md#insn-00b4cdc0) · [`00b4cdc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cd9c.md#insn-00b4cdc8) · [`00b4cda8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cd9c.md#insn-00b4cda8)

~~~diff
- 00b4bdcc ["INT_ADD", "register:40f0:8", ["const:b4bdcc:8", "const:4:8"]]
- 00b4bdcc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4cdc0 ["INT_ADD", "register:40f0:8", ["const:b4cdc0:8", "const:4:8"]]
+ 00b4cdc0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4bdcc bytes 853c0494
+ 00b4cdc0 bytes 7c3c0494
- 00b4bdd4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb8:8"]]
- 00b4bdd4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4cdc8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c78:8"]]
+ 00b4cdc8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4bdd4 bytes 605e06f9
+ 00b4cdc8 bytes 603e06f9
- 00b4bdb4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4cda8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4bdb4 bytes d32e00d0
+ 00b4cda8 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e3cd2b42ecd81b3001a4aca778341e73"></a>

### [`00b4bde8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bde8.md) → [`00b4cddc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cddc.md) _ZN8firebase4util8iterator19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4ce08",
      "incomplete_value": true,
      "site": "00b4ce08",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4be14",
      "incomplete_value": true,
      "site": "00b4be14",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4cdf0",
      "incomplete_value": true,
      "site": "00b4cdf0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bdfc",
      "incomplete_value": true,
      "site": "00b4bdfc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4cdf8",
      "incomplete_value": false,
      "site": "00b4ce00",
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
            "const:253:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4be04",
      "incomplete_value": false,
      "site": "00b4be0c",
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
            "const:fb:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4cdec",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cdf8",
      "PARAM",
      [
        "storage",
        "002a70fb",
        null,
        "string"
      ]
    ],
    [
      "00b4ce08",
      "WRITE",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4cdec",
      "READ",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cdf8",
      "PARAM",
      [
        "storage",
        "002a7253",
        null,
        "string"
      ]
    ],
    [
      "00b4ce08",
      "WRITE",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4be0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bde8.md#insn-00b4be0c) · [`00b4be14`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bde8.md#insn-00b4be14) · [`00b4bdf4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bde8.md#insn-00b4bdf4)
- 新版 [`00b4ce00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cddc.md#insn-00b4ce00) · [`00b4ce08`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cddc.md#insn-00b4ce08) · [`00b4cde8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cddc.md#insn-00b4cde8)

~~~diff
- 00b4be0c ["INT_ADD", "register:40f0:8", ["const:b4be0c:8", "const:4:8"]]
- 00b4be0c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4ce00 ["INT_ADD", "register:40f0:8", ["const:b4ce00:8", "const:4:8"]]
+ 00b4ce00 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4be0c bytes 753c0494
+ 00b4ce00 bytes 6c3c0494
- 00b4be14 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb8:8"]]
- 00b4be14 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ce08 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c78:8"]]
+ 00b4ce08 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4be14 bytes 605e06f9
+ 00b4ce08 bytes 603e06f9
- 00b4bdf4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4cde8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4bdf4 bytes d32e00d0
+ 00b4cde8 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e05924a518960c22571a3209bf461b1b"></a>

### [`00b4be28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4be28.md) → [`00b4ce1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ce1c.md) _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4ce4c",
      "incomplete_value": true,
      "site": "00b4ce4c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4be58",
      "incomplete_value": true,
      "site": "00b4be58",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4ce30",
      "incomplete_value": true,
      "site": "00b4ce30",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4be3c",
      "incomplete_value": true,
      "site": "00b4be3c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ce3c",
      "incomplete_value": false,
      "site": "00b4ce44",
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
            "const:253:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4be48",
      "incomplete_value": false,
      "site": "00b4be50",
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
            "const:fb:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ce2c",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ce3c",
      "PARAM",
      [
        "storage",
        "002a70fb",
        null,
        "string"
      ]
    ],
    [
      "00b4ce4c",
      "WRITE",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ce2c",
      "READ",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ce3c",
      "PARAM",
      [
        "storage",
        "002a7253",
        null,
        "string"
      ]
    ],
    [
      "00b4ce4c",
      "WRITE",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4be50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4be28.md#insn-00b4be50) · [`00b4be58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4be28.md#insn-00b4be58) · [`00b4be34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4be28.md#insn-00b4be34)
- 新版 [`00b4ce44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ce1c.md#insn-00b4ce44) · [`00b4ce4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ce1c.md#insn-00b4ce4c) · [`00b4ce28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ce1c.md#insn-00b4ce28)

~~~diff
- 00b4be50 ["INT_ADD", "register:40f0:8", ["const:b4be50:8", "const:4:8"]]
- 00b4be50 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4ce44 ["INT_ADD", "register:40f0:8", ["const:b4ce44:8", "const:4:8"]]
+ 00b4ce44 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4be50 bytes 643c0494
+ 00b4ce44 bytes 5b3c0494
- 00b4be58 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb8:8"]]
- 00b4be58 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ce4c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c78:8"]]
+ 00b4ce4c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4be58 bytes 605e06f9
+ 00b4ce4c bytes 603e06f9
- 00b4be34 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4ce28 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4be34 bytes d32e00d0
+ 00b4ce28 bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-16ca82f0ba3821db475aa2fd98754703"></a>

### [`00b4be6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4be6c.md) → [`00b4ce60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ce60.md) _ZN8firebase4util8iterator10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4ce90",
      "incomplete_value": true,
      "site": "00b4ce90",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4be9c",
      "incomplete_value": true,
      "site": "00b4be9c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cb8:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4ce74",
      "incomplete_value": true,
      "site": "00b4ce74",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4be80",
      "incomplete_value": true,
      "site": "00b4be80",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4ce7c",
      "incomplete_value": false,
      "site": "00b4ce88",
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
            "const:253:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4be88",
      "incomplete_value": false,
      "site": "00b4be94",
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
            "const:fb:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4ce70",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ce7c",
      "PARAM",
      [
        "storage",
        "002a70fb",
        null,
        "string"
      ]
    ],
    [
      "00b4ce90",
      "WRITE",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4ce70",
      "READ",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ce7c",
      "PARAM",
      [
        "storage",
        "002a7253",
        null,
        "string"
      ]
    ],
    [
      "00b4ce90",
      "WRITE",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4be94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4be6c.md#insn-00b4be94) · [`00b4be9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4be6c.md#insn-00b4be9c) · [`00b4be78`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4be6c.md#insn-00b4be78)
- 新版 [`00b4ce88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ce60.md#insn-00b4ce88) · [`00b4ce90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ce60.md#insn-00b4ce90) · [`00b4ce6c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ce60.md#insn-00b4ce6c)

~~~diff
- 00b4be94 ["INT_ADD", "register:40f0:8", ["const:b4be94:8", "const:4:8"]]
- 00b4be94 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4ce88 ["INT_ADD", "register:40f0:8", ["const:b4ce88:8", "const:4:8"]]
+ 00b4ce88 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4be94 bytes 533c0494
+ 00b4ce88 bytes 4a3c0494
- 00b4be9c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cb8:8"]]
- 00b4be9c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4ce90 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:c78:8"]]
+ 00b4ce90 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4be9c bytes 605e06f9
+ 00b4ce90 bytes 603e06f9
- 00b4be78 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4ce6c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4be78 bytes d32e00d0
+ 00b4ce6c bytes d32e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-eabf524fe2e1fb001a4ac0420c9579ca"></a>

### [`00b4bebc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bebc.md) → [`00b4ceb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ceb0.md) _ZN8firebase4util8iterator15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4cf38",
      "incomplete_value": true,
      "site": "00b4cf38",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bf44",
      "incomplete_value": true,
      "site": "00b4bf44",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      "definition_site": "00b4cee4",
      "incomplete_value": true,
      "site": "00b4cef0",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:c78:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bef0",
      "incomplete_value": true,
      "site": "00b4befc",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cb8:8"
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
      "00b4cec4",
      "READ",
      [
        "storage",
        "01125cc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cee4",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cf38",
      "WRITE",
      [
        "storage",
        "01125cc0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4cec4",
      "READ",
      [
        "storage",
        "01126c80",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cee4",
      "READ",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cf38",
      "WRITE",
      [
        "storage",
        "01126c80",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4befc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bebc.md#insn-00b4befc) · [`00b4bf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bebc.md#insn-00b4bf44) · [`00b4becc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bebc.md#insn-00b4becc)
- 新版 [`00b4cef0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ceb0.md#insn-00b4cef0) · [`00b4cf38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ceb0.md#insn-00b4cf38) · [`00b4cec0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4ceb0.md#insn-00b4cec0)

~~~diff
- 00b4befc ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4befc ["INT_ADD", "register:40f0:8", ["const:b4befc:8", "const:4:8"]]
- 00b4befc ["CALLIND", null, ["register:0:8"]]
+ 00b4cef0 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4cef0 ["INT_ADD", "register:40f0:8", ["const:b4cef0:8", "const:4:8"]]
+ 00b4cef0 ["CALLIND", null, ["register:0:8"]]
- 00b4befc bytes 00013fd6
+ 00b4cef0 bytes 00013fd6
- 00b4bf44 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4bf44 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:cc0:8"]]
- 00b4bf44 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4cf38 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4cf38 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:c80:8"]]
+ 00b4cf38 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4bf44 bytes a0023339
+ 00b4cf38 bytes a0023239
- 00b4becc ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4cec0 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4becc bytes d52e00d0
+ 00b4cec0 bytes d52e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0ff905bb98c2ea7fed91ba645405713b"></a>

### [`00b4bf58`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bf58.md) → [`00b4cf4c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cf4c.md) _ZN8firebase4util8iterator12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4cf88",
      "incomplete_value": true,
      "site": "00b4cf88",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:c80:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bf94",
      "incomplete_value": true,
      "site": "00b4bf94",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:cc0:8"
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
      "definition_site": "00b4cfd8",
      "incomplete_value": true,
      "site": "00b4cfd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4bfe4",
      "incomplete_value": true,
      "site": "00b4bfe4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cb8:8"
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
      "definition_site": "00b4cf64",
      "incomplete_value": true,
      "site": "00b4cf64",
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
      "definition_site": "00b4bf70",
      "incomplete_value": true,
      "site": "00b4bf70",
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
      "00b4cf60",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cf6c",
      "READ",
      [
        "storage",
        "01125cc0",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cf88",
      "WRITE",
      [
        "storage",
        "01125cc0",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4cf60",
      "READ",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4cf6c",
      "READ",
      [
        "storage",
        "01126c80",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4cf88",
      "WRITE",
      [
        "storage",
        "01126c80",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4bf94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bf58.md#insn-00b4bf94) · [`00b4bfe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bf58.md#insn-00b4bfe0) · [`00b4bfe4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bf58.md#insn-00b4bfe4)
- 新版 [`00b4cf88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cf4c.md#insn-00b4cf88) · [`00b4cfd4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cf4c.md#insn-00b4cfd4) · [`00b4cfd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cf4c.md#insn-00b4cfd8)

~~~diff
- 00b4bf94 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4bf94 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4bf94 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:cc0:8"]]
- 00b4bf94 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4cf88 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4cf88 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4cf88 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:c80:8"]]
+ 00b4cf88 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4bf94 bytes bf023339
+ 00b4cf88 bytes bf023239
- 00b4bfe0 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4bfe0 ["INT_ADD", "register:40f0:8", ["const:b4bfe0:8", "const:4:8"]]
- 00b4bfe0 ["CALLIND", null, ["register:0:8"]]
+ 00b4cfd4 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4cfd4 ["INT_ADD", "register:40f0:8", ["const:b4cfd4:8", "const:4:8"]]
+ 00b4cfd4 ["CALLIND", null, ["register:0:8"]]
- 00b4bfe0 bytes 00013fd6
+ 00b4cfd4 bytes 00013fd6
- 00b4bfe4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb8:8"]]
- 00b4bfe4 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4bfe4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4cfd8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c78:8"]]
+ 00b4cfd8 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4cfd8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4bfe4 bytes 9f5e06f9
+ 00b4cfd8 bytes 9f3e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-f58919ad7dc0a54a07a3a332543d97f7"></a>

### [`00b4bff8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bff8.md) → [`00b4cfec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cfec.md) _ZN8firebase4util8iterator14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d02c",
      "incomplete_value": true,
      "site": "00b4d02c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c038",
      "incomplete_value": true,
      "site": "00b4c038",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cb8:8"
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
      "definition_site": "00b4d008",
      "incomplete_value": true,
      "site": "00b4d008",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c014",
      "incomplete_value": true,
      "site": "00b4c014",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d010",
      "incomplete_value": false,
      "site": "00b4d024",
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
            "const:253:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c01c",
      "incomplete_value": false,
      "site": "00b4c030",
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
            "const:fb:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d000",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d010",
      "PARAM",
      [
        "storage",
        "002a70fb",
        null,
        "string"
      ]
    ],
    [
      "00b4d02c",
      "WRITE",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d000",
      "READ",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d010",
      "PARAM",
      [
        "storage",
        "002a7253",
        null,
        "string"
      ]
    ],
    [
      "00b4d02c",
      "WRITE",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bff8.md#insn-00b4c030) · [`00b4c038`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bff8.md#insn-00b4c038) · [`00b4c004`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4b/00b4bff8.md#insn-00b4c004)
- 新版 [`00b4d024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cfec.md#insn-00b4d024) · [`00b4d02c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cfec.md#insn-00b4d02c) · [`00b4cff8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4c/00b4cfec.md#insn-00b4cff8)

~~~diff
- 00b4c030 ["INT_ADD", "register:40f0:8", ["const:b4c030:8", "const:4:8"]]
- 00b4c030 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d024 ["INT_ADD", "register:40f0:8", ["const:b4d024:8", "const:4:8"]]
+ 00b4d024 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c030 bytes ec3b0494
+ 00b4d024 bytes e33b0494
- 00b4c038 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb8:8"]]
- 00b4c038 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d02c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c78:8"]]
+ 00b4d02c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c038 bytes 805e06f9
+ 00b4d02c bytes 803e06f9
- 00b4c004 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4cff8 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4c004 bytes d42e00b0
+ 00b4cff8 bytes d42e00d0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4fc7e9702536c3079ffa0f6b68baa2e3"></a>

### [`00b4c068`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c068.md) → [`00b4d05c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d05c.md) _ZN8firebase4util8iterator11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b630`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b630.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5c600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c600.md) · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4d078",
      "incomplete_value": false,
      "site": "00b4d07c",
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
      "definition_site": "00b4c084",
      "incomplete_value": false,
      "site": "00b4c088",
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
      "definition_site": "00b4d088",
      "incomplete_value": true,
      "site": "00b4d094",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4c094",
      "incomplete_value": true,
      "site": "00b4c0a0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4d078",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4d088",
      "DATA",
      [
        "storage",
        "01125cc8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d078",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4d088",
      "DATA",
      [
        "storage",
        "01126c88",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c088`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c068.md#insn-00b4c088) · [`00b4c084`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c068.md#insn-00b4c084) · [`00b4c08c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c068.md#insn-00b4c08c)
- 新版 [`00b4d07c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d05c.md#insn-00b4d07c) · [`00b4d078`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d05c.md#insn-00b4d078) · [`00b4d080`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d05c.md#insn-00b4d080)

~~~diff
- 00b4c088 ["INT_ADD", "register:40f0:8", ["const:b4c088:8", "const:4:8"]]
- 00b4c088 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4d07c ["INT_ADD", "register:40f0:8", ["const:b4d07c:8", "const:4:8"]]
+ 00b4d07c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4c088 bytes 123c0494
+ 00b4d07c bytes 093c0494
- 00b4c084 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4c084 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c084 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c084 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d078 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4d078 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d078 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d078 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4c084 bytes 002c0c91
+ 00b4d078 bytes 008c1191
- 00b4c08c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4d080 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4c08c bytes c82e00b0
+ 00b4d080 bytes c82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1e690aad7f59145e684693e6689b2fd6"></a>

### [`00b4c0a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c0a4.md) → [`00b4d098`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d098.md) _ZN8firebase4util8iterator13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d0d8",
      "incomplete_value": true,
      "site": "00b4d0d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:c78:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c0e4",
      "incomplete_value": true,
      "site": "00b4c0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cb8:8"
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
      "definition_site": "00b4d0b4",
      "incomplete_value": true,
      "site": "00b4d0b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c0c0",
      "incomplete_value": true,
      "site": "00b4c0c0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d0bc",
      "incomplete_value": false,
      "site": "00b4d0d0",
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
            "const:253:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c0c8",
      "incomplete_value": false,
      "site": "00b4c0dc",
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
            "const:fb:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d0ac",
      "READ",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d0bc",
      "PARAM",
      [
        "storage",
        "002a70fb",
        null,
        "string"
      ]
    ],
    [
      "00b4d0d8",
      "WRITE",
      [
        "storage",
        "01125cb8",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d0ac",
      "READ",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d0bc",
      "PARAM",
      [
        "storage",
        "002a7253",
        null,
        "string"
      ]
    ],
    [
      "00b4d0d8",
      "WRITE",
      [
        "storage",
        "01126c78",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c0a4.md#insn-00b4c0dc) · [`00b4c0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c0a4.md#insn-00b4c0e4) · [`00b4c0b0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c0a4.md#insn-00b4c0b0)
- 新版 [`00b4d0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d098.md#insn-00b4d0d0) · [`00b4d0d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d098.md#insn-00b4d0d8) · [`00b4d0a4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d098.md#insn-00b4d0a4)

~~~diff
- 00b4c0dc ["INT_ADD", "register:40f0:8", ["const:b4c0dc:8", "const:4:8"]]
- 00b4c0dc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d0d0 ["INT_ADD", "register:40f0:8", ["const:b4d0d0:8", "const:4:8"]]
+ 00b4d0d0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c0dc bytes c13b0494
+ 00b4d0d0 bytes b83b0494
- 00b4c0e4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cb8:8"]]
- 00b4c0e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d0d8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:c78:8"]]
+ 00b4d0d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c0e4 bytes 805e06f9
+ 00b4d0d8 bytes 803e06f9
- 00b4c0b0 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4d0a4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4c0b0 bytes d42e00b0
+ 00b4d0a4 bytes d42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12134f0ddeefc9967f29c4375b6e0cf2"></a>

### [`00b4c114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c114.md) → [`00b4d108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d108.md) _ZN8firebase4util8iterator10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4d124",
      "incomplete_value": false,
      "site": "00b4d128",
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
      "definition_site": "00b4c130",
      "incomplete_value": false,
      "site": "00b4c134",
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
      "definition_site": "00b4d134",
      "incomplete_value": true,
      "site": "00b4d140",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4c140",
      "incomplete_value": true,
      "site": "00b4c14c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4d124",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4d134",
      "DATA",
      [
        "storage",
        "01125cd8",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d124",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4d134",
      "DATA",
      [
        "storage",
        "01126c98",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c134`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c114.md#insn-00b4c134) · [`00b4c130`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c114.md#insn-00b4c130) · [`00b4c138`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c114.md#insn-00b4c138)
- 新版 [`00b4d128`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d108.md#insn-00b4d128) · [`00b4d124`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d108.md#insn-00b4d124) · [`00b4d12c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d108.md#insn-00b4d12c)

~~~diff
- 00b4c134 ["INT_ADD", "register:40f0:8", ["const:b4c134:8", "const:4:8"]]
- 00b4c134 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4d128 ["INT_ADD", "register:40f0:8", ["const:b4d128:8", "const:4:8"]]
+ 00b4d128 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4c134 bytes e73b0494
+ 00b4d128 bytes de3b0494
- 00b4c130 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b4c130 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c130 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c130 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d124 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4d124 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d124 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d124 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4c130 bytes 00341591
+ 00b4d124 bytes 00681891
- 00b4c138 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4d12c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4c138 bytes c82e00b0
+ 00b4d12c bytes c82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-7ff9cf9cb26043f05e7f78da8ccf5fa7"></a>

### [`00b4c150`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c150.md) → [`00b4d144`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d144.md) _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cl

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
      "definition_site": "00b4d170",
      "incomplete_value": true,
      "site": "00b4d170",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c17c",
      "incomplete_value": true,
      "site": "00b4c17c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d158",
      "incomplete_value": true,
      "site": "00b4d158",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c164",
      "incomplete_value": true,
      "site": "00b4c164",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d164",
      "incomplete_value": false,
      "site": "00b4d168",
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
            "const:97c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c170",
      "incomplete_value": false,
      "site": "00b4c174",
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
            "const:93c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d154",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d164",
      "PARAM",
      [
        "storage",
        "0029f93c",
        null,
        "string"
      ]
    ],
    [
      "00b4d170",
      "WRITE",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d154",
      "READ",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d164",
      "PARAM",
      [
        "storage",
        "0029f97c",
        null,
        "string"
      ]
    ],
    [
      "00b4d170",
      "WRITE",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c174`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c150.md#insn-00b4c174) · [`00b4c17c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c150.md#insn-00b4c17c) · [`00b4c15c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c150.md#insn-00b4c15c)
- 新版 [`00b4d168`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d144.md#insn-00b4d168) · [`00b4d170`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d144.md#insn-00b4d170) · [`00b4d150`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d144.md#insn-00b4d150)

~~~diff
- 00b4c174 ["INT_ADD", "register:40f0:8", ["const:b4c174:8", "const:4:8"]]
- 00b4c174 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d168 ["INT_ADD", "register:40f0:8", ["const:b4d168:8", "const:4:8"]]
+ 00b4d168 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c174 bytes 9b3b0494
+ 00b4d168 bytes 923b0494
- 00b4c17c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ce0:8"]]
- 00b4c17c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d170 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca0:8"]]
+ 00b4d170 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c17c bytes 607206f9
+ 00b4d170 bytes 605206f9
- 00b4c15c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4d150 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4c15c bytes d32e00b0
+ 00b4d150 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-56b857d73e9d33eedcc785dcc6794479"></a>

### [`00b4c190`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c190.md) → [`00b4d184`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d184.md) _ZN8firebase4util4list19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4d1b0",
      "incomplete_value": true,
      "site": "00b4d1b0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c1bc",
      "incomplete_value": true,
      "site": "00b4c1bc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d198",
      "incomplete_value": true,
      "site": "00b4d198",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c1a4",
      "incomplete_value": true,
      "site": "00b4c1a4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d1a0",
      "incomplete_value": false,
      "site": "00b4d1a8",
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
            "const:97c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c1ac",
      "incomplete_value": false,
      "site": "00b4c1b4",
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
            "const:93c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d194",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d1a0",
      "PARAM",
      [
        "storage",
        "0029f93c",
        null,
        "string"
      ]
    ],
    [
      "00b4d1b0",
      "WRITE",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d194",
      "READ",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d1a0",
      "PARAM",
      [
        "storage",
        "0029f97c",
        null,
        "string"
      ]
    ],
    [
      "00b4d1b0",
      "WRITE",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c1b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c190.md#insn-00b4c1b4) · [`00b4c1bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c190.md#insn-00b4c1bc) · [`00b4c19c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c190.md#insn-00b4c19c)
- 新版 [`00b4d1a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d184.md#insn-00b4d1a8) · [`00b4d1b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d184.md#insn-00b4d1b0) · [`00b4d190`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d184.md#insn-00b4d190)

~~~diff
- 00b4c1b4 ["INT_ADD", "register:40f0:8", ["const:b4c1b4:8", "const:4:8"]]
- 00b4c1b4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d1a8 ["INT_ADD", "register:40f0:8", ["const:b4d1a8:8", "const:4:8"]]
+ 00b4d1a8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c1b4 bytes 8b3b0494
+ 00b4d1a8 bytes 823b0494
- 00b4c1bc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ce0:8"]]
- 00b4c1bc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d1b0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca0:8"]]
+ 00b4d1b0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c1bc bytes 607206f9
+ 00b4d1b0 bytes 605206f9
- 00b4c19c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4d190 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4c19c bytes d32e00b0
+ 00b4d190 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a35cf97e3ee0379505ffdffa40627a32"></a>

### [`00b4c1d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c1d0.md) → [`00b4d1c4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d1c4.md) _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4d1f4",
      "incomplete_value": true,
      "site": "00b4d1f4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c200",
      "incomplete_value": true,
      "site": "00b4c200",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d1d8",
      "incomplete_value": true,
      "site": "00b4d1d8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c1e4",
      "incomplete_value": true,
      "site": "00b4c1e4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d1e4",
      "incomplete_value": false,
      "site": "00b4d1ec",
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
            "const:97c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c1f0",
      "incomplete_value": false,
      "site": "00b4c1f8",
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
            "const:93c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d1d4",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d1e4",
      "PARAM",
      [
        "storage",
        "0029f93c",
        null,
        "string"
      ]
    ],
    [
      "00b4d1f4",
      "WRITE",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d1d4",
      "READ",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d1e4",
      "PARAM",
      [
        "storage",
        "0029f97c",
        null,
        "string"
      ]
    ],
    [
      "00b4d1f4",
      "WRITE",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c1f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c1d0.md#insn-00b4c1f8) · [`00b4c200`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c1d0.md#insn-00b4c200) · [`00b4c1dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c1d0.md#insn-00b4c1dc)
- 新版 [`00b4d1ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d1c4.md#insn-00b4d1ec) · [`00b4d1f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d1c4.md#insn-00b4d1f4) · [`00b4d1d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d1c4.md#insn-00b4d1d0)

~~~diff
- 00b4c1f8 ["INT_ADD", "register:40f0:8", ["const:b4c1f8:8", "const:4:8"]]
- 00b4c1f8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d1ec ["INT_ADD", "register:40f0:8", ["const:b4d1ec:8", "const:4:8"]]
+ 00b4d1ec ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c1f8 bytes 7a3b0494
+ 00b4d1ec bytes 713b0494
- 00b4c200 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ce0:8"]]
- 00b4c200 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d1f4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca0:8"]]
+ 00b4d1f4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c200 bytes 607206f9
+ 00b4d1f4 bytes 605206f9
- 00b4c1dc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4d1d0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4c1dc bytes d32e00b0
+ 00b4d1d0 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-997c534cd7fc4a083ff695dc67e91deb"></a>

### [`00b4c214`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c214.md) → [`00b4d208`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d208.md) _ZN8firebase4util4list10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d238",
      "incomplete_value": true,
      "site": "00b4d238",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c244",
      "incomplete_value": true,
      "site": "00b4c244",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:ce0:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d21c",
      "incomplete_value": true,
      "site": "00b4d21c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c228",
      "incomplete_value": true,
      "site": "00b4c228",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d224",
      "incomplete_value": false,
      "site": "00b4d230",
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
            "const:97c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c230",
      "incomplete_value": false,
      "site": "00b4c23c",
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
            "const:93c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d218",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d224",
      "PARAM",
      [
        "storage",
        "0029f93c",
        null,
        "string"
      ]
    ],
    [
      "00b4d238",
      "WRITE",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d218",
      "READ",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d224",
      "PARAM",
      [
        "storage",
        "0029f97c",
        null,
        "string"
      ]
    ],
    [
      "00b4d238",
      "WRITE",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c23c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c214.md#insn-00b4c23c) · [`00b4c244`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c214.md#insn-00b4c244) · [`00b4c220`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c214.md#insn-00b4c220)
- 新版 [`00b4d230`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d208.md#insn-00b4d230) · [`00b4d238`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d208.md#insn-00b4d238) · [`00b4d214`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d208.md#insn-00b4d214)

~~~diff
- 00b4c23c ["INT_ADD", "register:40f0:8", ["const:b4c23c:8", "const:4:8"]]
- 00b4c23c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d230 ["INT_ADD", "register:40f0:8", ["const:b4d230:8", "const:4:8"]]
+ 00b4d230 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c23c bytes 693b0494
+ 00b4d230 bytes 603b0494
- 00b4c244 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ce0:8"]]
- 00b4c244 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d238 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:ca0:8"]]
+ 00b4d238 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c244 bytes 607206f9
+ 00b4d238 bytes 605206f9
- 00b4c220 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4d214 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4c220 bytes d32e00b0
+ 00b4d214 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-cbf1dd583fb656a5dbfc5e9fa7eee671"></a>

### [`00b4c258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c258.md) → [`00b4d24c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d24c.md) _ZN8firebase4util4list8GetClassEv

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
      "definition_site": "00b4d250",
      "incomplete_value": true,
      "site": "00b4d254",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ca0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c25c",
      "incomplete_value": true,
      "site": "00b4c260",
      "value": [
        "LOAD",
        "8",
        [
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
                "const:ce0:8"
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
      "00b4d250",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d250",
      "READ",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c258`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c258.md#insn-00b4c258) · [`00b4c25c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c258.md#insn-00b4c25c)
- 新版 [`00b4d24c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d24c.md#insn-00b4d24c) · [`00b4d250`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d24c.md#insn-00b4d250)

~~~diff
- 00b4c258 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4d24c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4c258 bytes c82e00b0
+ 00b4d24c bytes c82e00b0
- 00b4c25c ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ce0:8"]]
- 00b4c25c ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4d250 ["INT_ADD", "tmp:0:8", ["register:4040:8", "const:ca0:8"]]
+ 00b4d250 ["LOAD", "register:4000:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4c25c bytes 007146f9
+ 00b4d250 bytes 005146f9
~~~


<a id="compare-701d0818a2cc59578439a77cbd87e001"></a>

### [`00b4c264`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c264.md) → [`00b4d258`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d258.md) _ZN8firebase4util4list15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4d2e0",
      "incomplete_value": true,
      "site": "00b4d2e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c2ec",
      "incomplete_value": true,
      "site": "00b4c2ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "definition_site": "00b4d28c",
      "incomplete_value": true,
      "site": "00b4d298",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ca0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c298",
      "incomplete_value": true,
      "site": "00b4c2a4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:ce0:8"
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
      "00b4d26c",
      "READ",
      [
        "storage",
        "01125ce8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d28c",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d2e0",
      "WRITE",
      [
        "storage",
        "01125ce8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d26c",
      "READ",
      [
        "storage",
        "01126ca8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d28c",
      "READ",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d2e0",
      "WRITE",
      [
        "storage",
        "01126ca8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c2a4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c264.md#insn-00b4c2a4) · [`00b4c2ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c264.md#insn-00b4c2ec) · [`00b4c274`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c264.md#insn-00b4c274)
- 新版 [`00b4d298`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d258.md#insn-00b4d298) · [`00b4d2e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d258.md#insn-00b4d2e0) · [`00b4d268`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d258.md#insn-00b4d268)

~~~diff
- 00b4c2a4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c2a4 ["INT_ADD", "register:40f0:8", ["const:b4c2a4:8", "const:4:8"]]
- 00b4c2a4 ["CALLIND", null, ["register:0:8"]]
+ 00b4d298 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d298 ["INT_ADD", "register:40f0:8", ["const:b4d298:8", "const:4:8"]]
+ 00b4d298 ["CALLIND", null, ["register:0:8"]]
- 00b4c2a4 bytes 00013fd6
+ 00b4d298 bytes 00013fd6
- 00b4c2ec ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4c2ec ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ce8:8"]]
- 00b4c2ec ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4d2e0 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4d2e0 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:ca8:8"]]
+ 00b4d2e0 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4c2ec bytes a0a23339
+ 00b4d2e0 bytes a0a23239
- 00b4c274 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4d268 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4c274 bytes d52e00b0
+ 00b4d268 bytes d52e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d802fe898bb14c6c9d2819e389417e8c"></a>

### [`00b4c300`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c300.md) → [`00b4d2f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d2f4.md) _ZN8firebase4util4list12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4d330",
      "incomplete_value": true,
      "site": "00b4d330",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ca8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c33c",
      "incomplete_value": true,
      "site": "00b4c33c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:ce8:8"
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
      "definition_site": "00b4d380",
      "incomplete_value": true,
      "site": "00b4d380",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c38c",
      "incomplete_value": true,
      "site": "00b4c38c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "definition_site": "00b4d30c",
      "incomplete_value": true,
      "site": "00b4d30c",
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
      "definition_site": "00b4c318",
      "incomplete_value": true,
      "site": "00b4c318",
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
      "00b4d308",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d314",
      "READ",
      [
        "storage",
        "01125ce8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d330",
      "WRITE",
      [
        "storage",
        "01125ce8",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d308",
      "READ",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d314",
      "READ",
      [
        "storage",
        "01126ca8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d330",
      "WRITE",
      [
        "storage",
        "01126ca8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c33c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c300.md#insn-00b4c33c) · [`00b4c388`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c300.md#insn-00b4c388) · [`00b4c38c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c300.md#insn-00b4c38c)
- 新版 [`00b4d330`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d2f4.md#insn-00b4d330) · [`00b4d37c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d2f4.md#insn-00b4d37c) · [`00b4d380`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d2f4.md#insn-00b4d380)

~~~diff
- 00b4c33c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4c33c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4c33c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ce8:8"]]
- 00b4c33c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4d330 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4d330 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4d330 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:ca8:8"]]
+ 00b4d330 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4c33c bytes bfa23339
+ 00b4d330 bytes bfa23239
- 00b4c388 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c388 ["INT_ADD", "register:40f0:8", ["const:b4c388:8", "const:4:8"]]
- 00b4c388 ["CALLIND", null, ["register:0:8"]]
+ 00b4d37c ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d37c ["INT_ADD", "register:40f0:8", ["const:b4d37c:8", "const:4:8"]]
+ 00b4d37c ["CALLIND", null, ["register:0:8"]]
- 00b4c388 bytes 00013fd6
+ 00b4d37c bytes 00013fd6
- 00b4c38c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ce0:8"]]
- 00b4c38c ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4c38c ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4d380 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca0:8"]]
+ 00b4d380 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4d380 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4c38c bytes 9f7206f9
+ 00b4d380 bytes 9f5206f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e97ca3d0b9363f0eff58e019c9e87253"></a>

### [`00b4c3a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c3a0.md) → [`00b4d394`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d394.md) _ZN8firebase4util4list14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d3d4",
      "incomplete_value": true,
      "site": "00b4d3d4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c3e0",
      "incomplete_value": true,
      "site": "00b4c3e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "definition_site": "00b4d3b0",
      "incomplete_value": true,
      "site": "00b4d3b0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c3bc",
      "incomplete_value": true,
      "site": "00b4c3bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d3b8",
      "incomplete_value": false,
      "site": "00b4d3cc",
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
            "const:97c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c3c4",
      "incomplete_value": false,
      "site": "00b4c3d8",
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
            "const:93c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d3a8",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d3b8",
      "PARAM",
      [
        "storage",
        "0029f93c",
        null,
        "string"
      ]
    ],
    [
      "00b4d3d4",
      "WRITE",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d3a8",
      "READ",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d3b8",
      "PARAM",
      [
        "storage",
        "0029f97c",
        null,
        "string"
      ]
    ],
    [
      "00b4d3d4",
      "WRITE",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c3d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c3a0.md#insn-00b4c3d8) · [`00b4c3e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c3a0.md#insn-00b4c3e0) · [`00b4c3ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c3a0.md#insn-00b4c3ac)
- 新版 [`00b4d3cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d394.md#insn-00b4d3cc) · [`00b4d3d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d394.md#insn-00b4d3d4) · [`00b4d3a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d394.md#insn-00b4d3a0)

~~~diff
- 00b4c3d8 ["INT_ADD", "register:40f0:8", ["const:b4c3d8:8", "const:4:8"]]
- 00b4c3d8 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d3cc ["INT_ADD", "register:40f0:8", ["const:b4d3cc:8", "const:4:8"]]
+ 00b4d3cc ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c3d8 bytes 023b0494
+ 00b4d3cc bytes f93a0494
- 00b4c3e0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ce0:8"]]
- 00b4c3e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d3d4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca0:8"]]
+ 00b4d3d4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c3e0 bytes 807206f9
+ 00b4d3d4 bytes 805206f9
- 00b4c3ac ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4d3a0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4c3ac bytes d42e00b0
+ 00b4d3a0 bytes d42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-d97e1b6fda030aeca036a1028e0ba81c"></a>

### [`00b4c410`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c410.md) → [`00b4d404`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d404.md) _ZN8firebase4util4list11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b5f0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b5f0.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5c5c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c5c0.md) · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4d420",
      "incomplete_value": false,
      "site": "00b4d424",
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
      "definition_site": "00b4c42c",
      "incomplete_value": false,
      "site": "00b4c430",
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
      "definition_site": "00b4d430",
      "incomplete_value": true,
      "site": "00b4d43c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4c43c",
      "incomplete_value": true,
      "site": "00b4c448",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4d420",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4d430",
      "DATA",
      [
        "storage",
        "01125cf0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d420",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4d430",
      "DATA",
      [
        "storage",
        "01126cb0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c430`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c410.md#insn-00b4c430) · [`00b4c42c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c410.md#insn-00b4c42c) · [`00b4c434`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c410.md#insn-00b4c434)
- 新版 [`00b4d424`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d404.md#insn-00b4d424) · [`00b4d420`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d404.md#insn-00b4d420) · [`00b4d428`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d404.md#insn-00b4d428)

~~~diff
- 00b4c430 ["INT_ADD", "register:40f0:8", ["const:b4c430:8", "const:4:8"]]
- 00b4c430 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4d424 ["INT_ADD", "register:40f0:8", ["const:b4d424:8", "const:4:8"]]
+ 00b4d424 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4c430 bytes 283b0494
+ 00b4d424 bytes 1f3b0494
- 00b4c42c ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4c42c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c42c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c42c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d420 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4d420 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d420 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d420 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4c42c bytes 002c0c91
+ 00b4d420 bytes 008c1191
- 00b4c434 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4d428 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4c434 bytes c82e00b0
+ 00b4d428 bytes c82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a5445081a9ca3a1d8d9a823192a4a8af"></a>

### [`00b4c44c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c44c.md) → [`00b4d440`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d440.md) _ZN8firebase4util4list13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d480",
      "incomplete_value": true,
      "site": "00b4d480",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ca0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c48c",
      "incomplete_value": true,
      "site": "00b4c48c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:ce0:8"
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
      "definition_site": "00b4d45c",
      "incomplete_value": true,
      "site": "00b4d45c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c468",
      "incomplete_value": true,
      "site": "00b4c468",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d464",
      "incomplete_value": false,
      "site": "00b4d478",
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
            "const:97c:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c470",
      "incomplete_value": false,
      "site": "00b4c484",
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
            "const:93c:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d454",
      "READ",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d464",
      "PARAM",
      [
        "storage",
        "0029f93c",
        null,
        "string"
      ]
    ],
    [
      "00b4d480",
      "WRITE",
      [
        "storage",
        "01125ce0",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d454",
      "READ",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d464",
      "PARAM",
      [
        "storage",
        "0029f97c",
        null,
        "string"
      ]
    ],
    [
      "00b4d480",
      "WRITE",
      [
        "storage",
        "01126ca0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c484`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c44c.md#insn-00b4c484) · [`00b4c48c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c44c.md#insn-00b4c48c) · [`00b4c458`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c44c.md#insn-00b4c458)
- 新版 [`00b4d478`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d440.md#insn-00b4d478) · [`00b4d480`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d440.md#insn-00b4d480) · [`00b4d44c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d440.md#insn-00b4d44c)

~~~diff
- 00b4c484 ["INT_ADD", "register:40f0:8", ["const:b4c484:8", "const:4:8"]]
- 00b4c484 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d478 ["INT_ADD", "register:40f0:8", ["const:b4d478:8", "const:4:8"]]
+ 00b4d478 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c484 bytes d73a0494
+ 00b4d478 bytes ce3a0494
- 00b4c48c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ce0:8"]]
- 00b4c48c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d480 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:ca0:8"]]
+ 00b4d480 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c48c bytes 807206f9
+ 00b4d480 bytes 805206f9
- 00b4c458 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4d44c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4c458 bytes d42e00b0
+ 00b4d44c bytes d42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-672910b01935b8519bd7aae45b10cbe1"></a>

### [`00b4c4bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c4bc.md) → [`00b4d4b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d4b0.md) _ZN8firebase4util4list10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4d4cc",
      "incomplete_value": false,
      "site": "00b4d4d0",
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
      "definition_site": "00b4c4d8",
      "incomplete_value": false,
      "site": "00b4c4dc",
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
      "definition_site": "00b4d4dc",
      "incomplete_value": true,
      "site": "00b4d4e8",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4c4e8",
      "incomplete_value": true,
      "site": "00b4c4f4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4d4cc",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4d4dc",
      "DATA",
      [
        "storage",
        "01125d08",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d4cc",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4d4dc",
      "DATA",
      [
        "storage",
        "01126cc8",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c4dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c4bc.md#insn-00b4c4dc) · [`00b4c4d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c4bc.md#insn-00b4c4d8) · [`00b4c4e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c4bc.md#insn-00b4c4e0)
- 新版 [`00b4d4d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d4b0.md#insn-00b4d4d0) · [`00b4d4cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d4b0.md#insn-00b4d4cc) · [`00b4d4d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d4b0.md#insn-00b4d4d4)

~~~diff
- 00b4c4dc ["INT_ADD", "register:40f0:8", ["const:b4c4dc:8", "const:4:8"]]
- 00b4c4dc ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4d4d0 ["INT_ADD", "register:40f0:8", ["const:b4d4d0:8", "const:4:8"]]
+ 00b4d4d0 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4c4dc bytes fd3a0494
+ 00b4d4d0 bytes f43a0494
- 00b4c4d8 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b4c4d8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c4d8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c4d8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d4cc ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4d4cc ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d4cc ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d4cc ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4c4d8 bytes 00341591
+ 00b4d4cc bytes 00681891
- 00b4c4e0 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4d4d4 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4c4e0 bytes c82e00b0
+ 00b4d4d4 bytes c82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-715c3f38408a4e55cc99eb66fb6021ef"></a>

### [`00b4c4f8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c4f8.md) → [`00b4d4ec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d4ec.md) _ZN8firebase4util10long_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEEN

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4d518",
      "incomplete_value": true,
      "site": "00b4d518",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c524",
      "incomplete_value": true,
      "site": "00b4c524",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d500",
      "incomplete_value": true,
      "site": "00b4d500",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c50c",
      "incomplete_value": true,
      "site": "00b4c50c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d50c",
      "incomplete_value": false,
      "site": "00b4d510",
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
            "const:b27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c518",
      "incomplete_value": false,
      "site": "00b4c51c",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d4fc",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d50c",
      "PARAM",
      [
        "storage",
        "002b8a58",
        null,
        "string"
      ]
    ],
    [
      "00b4d518",
      "WRITE",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d4fc",
      "READ",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d50c",
      "PARAM",
      [
        "storage",
        "002b8b27",
        null,
        "string"
      ]
    ],
    [
      "00b4d518",
      "WRITE",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c51c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c4f8.md#insn-00b4c51c) · [`00b4c524`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c4f8.md#insn-00b4c524) · [`00b4c504`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c4f8.md#insn-00b4c504)
- 新版 [`00b4d510`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d4ec.md#insn-00b4d510) · [`00b4d518`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d4ec.md#insn-00b4d518) · [`00b4d4f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d4ec.md#insn-00b4d4f8)

~~~diff
- 00b4c51c ["INT_ADD", "register:40f0:8", ["const:b4c51c:8", "const:4:8"]]
- 00b4c51c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d510 ["INT_ADD", "register:40f0:8", ["const:b4d510:8", "const:4:8"]]
+ 00b4d510 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c51c bytes b13a0494
+ 00b4d510 bytes a83a0494
- 00b4c524 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d10:8"]]
- 00b4c524 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d518 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00b4d518 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c524 bytes 608a06f9
+ 00b4d518 bytes 606a06f9
- 00b4c504 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4d4f8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4c504 bytes d32e00b0
+ 00b4d4f8 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3e34754ca00c701b62d4ba3dc01e50bc"></a>

### [`00b4c538`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c538.md) → [`00b4d52c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d52c.md) _ZN8firebase4util10long_class19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

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
      "definition_site": "00b4d558",
      "incomplete_value": true,
      "site": "00b4d558",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c564",
      "incomplete_value": true,
      "site": "00b4c564",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d540",
      "incomplete_value": true,
      "site": "00b4d540",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c54c",
      "incomplete_value": true,
      "site": "00b4c54c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d548",
      "incomplete_value": false,
      "site": "00b4d550",
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
            "const:b27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c554",
      "incomplete_value": false,
      "site": "00b4c55c",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d53c",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d548",
      "PARAM",
      [
        "storage",
        "002b8a58",
        null,
        "string"
      ]
    ],
    [
      "00b4d558",
      "WRITE",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d53c",
      "READ",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d548",
      "PARAM",
      [
        "storage",
        "002b8b27",
        null,
        "string"
      ]
    ],
    [
      "00b4d558",
      "WRITE",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c55c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c538.md#insn-00b4c55c) · [`00b4c564`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c538.md#insn-00b4c564) · [`00b4c544`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c538.md#insn-00b4c544)
- 新版 [`00b4d550`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d52c.md#insn-00b4d550) · [`00b4d558`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d52c.md#insn-00b4d558) · [`00b4d538`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d52c.md#insn-00b4d538)

~~~diff
- 00b4c55c ["INT_ADD", "register:40f0:8", ["const:b4c55c:8", "const:4:8"]]
- 00b4c55c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d550 ["INT_ADD", "register:40f0:8", ["const:b4d550:8", "const:4:8"]]
+ 00b4d550 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c55c bytes a13a0494
+ 00b4d550 bytes 983a0494
- 00b4c564 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d10:8"]]
- 00b4c564 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d558 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00b4d558 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c564 bytes 608a06f9
+ 00b4d558 bytes 606a06f9
- 00b4c544 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4d538 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4c544 bytes d32e00b0
+ 00b4d538 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-39c0c6e21211a453c9ed27766ddd1d27"></a>

### [`00b4c578`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c578.md) → [`00b4d56c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d56c.md) _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4d59c",
      "incomplete_value": true,
      "site": "00b4d59c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c5a8",
      "incomplete_value": true,
      "site": "00b4c5a8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d580",
      "incomplete_value": true,
      "site": "00b4d580",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c58c",
      "incomplete_value": true,
      "site": "00b4c58c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d58c",
      "incomplete_value": false,
      "site": "00b4d594",
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
            "const:b27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c598",
      "incomplete_value": false,
      "site": "00b4c5a0",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d57c",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d58c",
      "PARAM",
      [
        "storage",
        "002b8a58",
        null,
        "string"
      ]
    ],
    [
      "00b4d59c",
      "WRITE",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d57c",
      "READ",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d58c",
      "PARAM",
      [
        "storage",
        "002b8b27",
        null,
        "string"
      ]
    ],
    [
      "00b4d59c",
      "WRITE",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c5a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c578.md#insn-00b4c5a0) · [`00b4c5a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c578.md#insn-00b4c5a8) · [`00b4c584`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c578.md#insn-00b4c584)
- 新版 [`00b4d594`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d56c.md#insn-00b4d594) · [`00b4d59c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d56c.md#insn-00b4d59c) · [`00b4d578`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d56c.md#insn-00b4d578)

~~~diff
- 00b4c5a0 ["INT_ADD", "register:40f0:8", ["const:b4c5a0:8", "const:4:8"]]
- 00b4c5a0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d594 ["INT_ADD", "register:40f0:8", ["const:b4d594:8", "const:4:8"]]
+ 00b4d594 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c5a0 bytes 903a0494
+ 00b4d594 bytes 873a0494
- 00b4c5a8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d10:8"]]
- 00b4c5a8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d59c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00b4d59c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c5a8 bytes 608a06f9
+ 00b4d59c bytes 606a06f9
- 00b4c584 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4d578 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4c584 bytes d32e00b0
+ 00b4d578 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e398d309a9d1f822ffdf8a99c2197a1d"></a>

### [`00b4c5bc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c5bc.md) → [`00b4d5b0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d5b0.md) _ZN8firebase4util10long_class10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d5e0",
      "incomplete_value": true,
      "site": "00b4d5e0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c5ec",
      "incomplete_value": true,
      "site": "00b4c5ec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d10:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d5c4",
      "incomplete_value": true,
      "site": "00b4d5c4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c5d0",
      "incomplete_value": true,
      "site": "00b4c5d0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d5cc",
      "incomplete_value": false,
      "site": "00b4d5d8",
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
            "const:b27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c5d8",
      "incomplete_value": false,
      "site": "00b4c5e4",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d5c0",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d5cc",
      "PARAM",
      [
        "storage",
        "002b8a58",
        null,
        "string"
      ]
    ],
    [
      "00b4d5e0",
      "WRITE",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d5c0",
      "READ",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d5cc",
      "PARAM",
      [
        "storage",
        "002b8b27",
        null,
        "string"
      ]
    ],
    [
      "00b4d5e0",
      "WRITE",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c5e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c5bc.md#insn-00b4c5e4) · [`00b4c5ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c5bc.md#insn-00b4c5ec) · [`00b4c5c8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c5bc.md#insn-00b4c5c8)
- 新版 [`00b4d5d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d5b0.md#insn-00b4d5d8) · [`00b4d5e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d5b0.md#insn-00b4d5e0) · [`00b4d5bc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d5b0.md#insn-00b4d5bc)

~~~diff
- 00b4c5e4 ["INT_ADD", "register:40f0:8", ["const:b4c5e4:8", "const:4:8"]]
- 00b4c5e4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d5d8 ["INT_ADD", "register:40f0:8", ["const:b4d5d8:8", "const:4:8"]]
+ 00b4d5d8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c5e4 bytes 7f3a0494
+ 00b4d5d8 bytes 763a0494
- 00b4c5ec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d10:8"]]
- 00b4c5ec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d5e0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cd0:8"]]
+ 00b4d5e0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c5ec bytes 608a06f9
+ 00b4d5e0 bytes 606a06f9
- 00b4c5c8 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4d5bc ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4c5c8 bytes d32e00b0
+ 00b4d5bc bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9a07f7fb8e7a43718b9731d2f75c6ba5"></a>

### [`00b4c60c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c60c.md) → [`00b4d600`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d600.md) _ZN8firebase4util10long_class15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4d688",
      "incomplete_value": true,
      "site": "00b4d688",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c694",
      "incomplete_value": true,
      "site": "00b4c694",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d18:8"
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
      "definition_site": "00b4d634",
      "incomplete_value": true,
      "site": "00b4d640",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cd0:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c640",
      "incomplete_value": true,
      "site": "00b4c64c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d10:8"
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
      "00b4d614",
      "READ",
      [
        "storage",
        "01125d18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d634",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d688",
      "WRITE",
      [
        "storage",
        "01125d18",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d614",
      "READ",
      [
        "storage",
        "01126cd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d634",
      "READ",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d688",
      "WRITE",
      [
        "storage",
        "01126cd8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c64c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c60c.md#insn-00b4c64c) · [`00b4c694`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c60c.md#insn-00b4c694) · [`00b4c61c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c60c.md#insn-00b4c61c)
- 新版 [`00b4d640`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d600.md#insn-00b4d640) · [`00b4d688`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d600.md#insn-00b4d688) · [`00b4d610`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d600.md#insn-00b4d610)

~~~diff
- 00b4c64c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c64c ["INT_ADD", "register:40f0:8", ["const:b4c64c:8", "const:4:8"]]
- 00b4c64c ["CALLIND", null, ["register:0:8"]]
+ 00b4d640 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d640 ["INT_ADD", "register:40f0:8", ["const:b4d640:8", "const:4:8"]]
+ 00b4d640 ["CALLIND", null, ["register:0:8"]]
- 00b4c64c bytes 00013fd6
+ 00b4d640 bytes 00013fd6
- 00b4c694 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4c694 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d18:8"]]
- 00b4c694 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4d688 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4d688 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:cd8:8"]]
+ 00b4d688 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4c694 bytes a0623439
+ 00b4d688 bytes a0623339
- 00b4c61c ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4d610 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4c61c bytes d52e00b0
+ 00b4d610 bytes d52e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9b95ac2cce85a59679622a27b2be2ffc"></a>

### [`00b4c6a8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c6a8.md) → [`00b4d69c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d69c.md) _ZN8firebase4util10long_class12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4d6d8",
      "incomplete_value": true,
      "site": "00b4d6d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:cd8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c6e4",
      "incomplete_value": true,
      "site": "00b4c6e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d18:8"
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
      "definition_site": "00b4d728",
      "incomplete_value": true,
      "site": "00b4d728",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c734",
      "incomplete_value": true,
      "site": "00b4c734",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "definition_site": "00b4d6b4",
      "incomplete_value": true,
      "site": "00b4d6b4",
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
      "definition_site": "00b4c6c0",
      "incomplete_value": true,
      "site": "00b4c6c0",
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
      "00b4d6b0",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d6bc",
      "READ",
      [
        "storage",
        "01125d18",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d6d8",
      "WRITE",
      [
        "storage",
        "01125d18",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d6b0",
      "READ",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d6bc",
      "READ",
      [
        "storage",
        "01126cd8",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d6d8",
      "WRITE",
      [
        "storage",
        "01126cd8",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c6e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c6a8.md#insn-00b4c6e4) · [`00b4c730`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c6a8.md#insn-00b4c730) · [`00b4c734`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c6a8.md#insn-00b4c734)
- 新版 [`00b4d6d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d69c.md#insn-00b4d6d8) · [`00b4d724`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d69c.md#insn-00b4d724) · [`00b4d728`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d69c.md#insn-00b4d728)

~~~diff
- 00b4c6e4 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4c6e4 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4c6e4 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d18:8"]]
- 00b4c6e4 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4d6d8 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4d6d8 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4d6d8 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:cd8:8"]]
+ 00b4d6d8 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4c6e4 bytes bf623439
+ 00b4d6d8 bytes bf623339
- 00b4c730 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c730 ["INT_ADD", "register:40f0:8", ["const:b4c730:8", "const:4:8"]]
- 00b4c730 ["CALLIND", null, ["register:0:8"]]
+ 00b4d724 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d724 ["INT_ADD", "register:40f0:8", ["const:b4d724:8", "const:4:8"]]
+ 00b4d724 ["CALLIND", null, ["register:0:8"]]
- 00b4c730 bytes 00013fd6
+ 00b4d724 bytes 00013fd6
- 00b4c734 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d10:8"]]
- 00b4c734 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4c734 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4d728 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
+ 00b4d728 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4d728 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4c734 bytes 9f8a06f9
+ 00b4d728 bytes 9f6a06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-98c7ee54f8052210f75c9b99fda7e9a3"></a>

### [`00b4c748`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c748.md) → [`00b4d73c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d73c.md) _ZN8firebase4util10long_class14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d77c",
      "incomplete_value": true,
      "site": "00b4d77c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c788",
      "incomplete_value": true,
      "site": "00b4c788",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "definition_site": "00b4d758",
      "incomplete_value": true,
      "site": "00b4d758",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c764",
      "incomplete_value": true,
      "site": "00b4c764",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d760",
      "incomplete_value": false,
      "site": "00b4d774",
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
            "const:b27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c76c",
      "incomplete_value": false,
      "site": "00b4c780",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d750",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d760",
      "PARAM",
      [
        "storage",
        "002b8a58",
        null,
        "string"
      ]
    ],
    [
      "00b4d77c",
      "WRITE",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d750",
      "READ",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d760",
      "PARAM",
      [
        "storage",
        "002b8b27",
        null,
        "string"
      ]
    ],
    [
      "00b4d77c",
      "WRITE",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c780`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c748.md#insn-00b4c780) · [`00b4c788`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c748.md#insn-00b4c788) · [`00b4c754`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c748.md#insn-00b4c754)
- 新版 [`00b4d774`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d73c.md#insn-00b4d774) · [`00b4d77c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d73c.md#insn-00b4d77c) · [`00b4d748`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d73c.md#insn-00b4d748)

~~~diff
- 00b4c780 ["INT_ADD", "register:40f0:8", ["const:b4c780:8", "const:4:8"]]
- 00b4c780 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d774 ["INT_ADD", "register:40f0:8", ["const:b4d774:8", "const:4:8"]]
+ 00b4d774 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c780 bytes 183a0494
+ 00b4d774 bytes 0f3a0494
- 00b4c788 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d10:8"]]
- 00b4c788 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d77c ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
+ 00b4d77c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c788 bytes 808a06f9
+ 00b4d77c bytes 806a06f9
- 00b4c754 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4d748 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4c754 bytes d42e00b0
+ 00b4d748 bytes d42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6dbee0adef3d3bec4324401f4b322146"></a>

### [`00b4c7b8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c7b8.md) → [`00b4d7ac`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d7ac.md) _ZN8firebase4util10long_class11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b340`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b340.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5c310`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c310.md) · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4d7c8",
      "incomplete_value": false,
      "site": "00b4d7cc",
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
      "definition_site": "00b4c7d4",
      "incomplete_value": false,
      "site": "00b4c7d8",
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
      "definition_site": "00b4d7d8",
      "incomplete_value": true,
      "site": "00b4d7e4",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4c7e4",
      "incomplete_value": true,
      "site": "00b4c7f0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4d7c8",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4d7d8",
      "DATA",
      [
        "storage",
        "01125d20",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d7c8",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4d7d8",
      "DATA",
      [
        "storage",
        "01126ce0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c7d8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c7b8.md#insn-00b4c7d8) · [`00b4c7d4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c7b8.md#insn-00b4c7d4) · [`00b4c7dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c7b8.md#insn-00b4c7dc)
- 新版 [`00b4d7cc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d7ac.md#insn-00b4d7cc) · [`00b4d7c8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d7ac.md#insn-00b4d7c8) · [`00b4d7d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d7ac.md#insn-00b4d7d0)

~~~diff
- 00b4c7d8 ["INT_ADD", "register:40f0:8", ["const:b4c7d8:8", "const:4:8"]]
- 00b4c7d8 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4d7cc ["INT_ADD", "register:40f0:8", ["const:b4d7cc:8", "const:4:8"]]
+ 00b4d7cc ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4c7d8 bytes 3e3a0494
+ 00b4d7cc bytes 353a0494
- 00b4c7d4 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4c7d4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c7d4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c7d4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d7c8 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4d7c8 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d7c8 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d7c8 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4c7d4 bytes 002c0c91
+ 00b4d7c8 bytes 008c1191
- 00b4c7dc ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4d7d0 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4c7dc bytes c82e00b0
+ 00b4d7d0 bytes c82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-edaad84b50515c8ea773c891241a3141"></a>

### [`00b4c7f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c7f4.md) → [`00b4d7e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d7e8.md) _ZN8firebase4util10long_class13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d828",
      "incomplete_value": true,
      "site": "00b4d828",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cd0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c834",
      "incomplete_value": true,
      "site": "00b4c834",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d10:8"
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
      "definition_site": "00b4d804",
      "incomplete_value": true,
      "site": "00b4d804",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c810",
      "incomplete_value": true,
      "site": "00b4c810",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d80c",
      "incomplete_value": false,
      "site": "00b4d820",
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
            "const:b27:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c818",
      "incomplete_value": false,
      "site": "00b4c82c",
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
            "const:a58:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d7fc",
      "READ",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d80c",
      "PARAM",
      [
        "storage",
        "002b8a58",
        null,
        "string"
      ]
    ],
    [
      "00b4d828",
      "WRITE",
      [
        "storage",
        "01125d10",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d7fc",
      "READ",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d80c",
      "PARAM",
      [
        "storage",
        "002b8b27",
        null,
        "string"
      ]
    ],
    [
      "00b4d828",
      "WRITE",
      [
        "storage",
        "01126cd0",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c82c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c7f4.md#insn-00b4c82c) · [`00b4c834`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c7f4.md#insn-00b4c834) · [`00b4c800`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c7f4.md#insn-00b4c800)
- 新版 [`00b4d820`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d7e8.md#insn-00b4d820) · [`00b4d828`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d7e8.md#insn-00b4d828) · [`00b4d7f4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d7e8.md#insn-00b4d7f4)

~~~diff
- 00b4c82c ["INT_ADD", "register:40f0:8", ["const:b4c82c:8", "const:4:8"]]
- 00b4c82c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d820 ["INT_ADD", "register:40f0:8", ["const:b4d820:8", "const:4:8"]]
+ 00b4d820 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c82c bytes ed390494
+ 00b4d820 bytes e4390494
- 00b4c834 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d10:8"]]
- 00b4c834 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d828 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cd0:8"]]
+ 00b4d828 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c834 bytes 808a06f9
+ 00b4d828 bytes 806a06f9
- 00b4c800 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4d7f4 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4c800 bytes d42e00b0
+ 00b4d7f4 bytes d42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2d1b4003a8f5d53fdfddb8daa5a0290"></a>

### [`00b4c864`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c864.md) → [`00b4d858`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d858.md) _ZN8firebase4util10long_class10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4d874",
      "incomplete_value": false,
      "site": "00b4d878",
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
      "definition_site": "00b4c880",
      "incomplete_value": false,
      "site": "00b4c884",
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
      "definition_site": "00b4d884",
      "incomplete_value": true,
      "site": "00b4d890",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4c890",
      "incomplete_value": true,
      "site": "00b4c89c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4d874",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4d884",
      "DATA",
      [
        "storage",
        "01125d30",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4d874",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4d884",
      "DATA",
      [
        "storage",
        "01126cf0",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c884`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c864.md#insn-00b4c884) · [`00b4c880`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c864.md#insn-00b4c880) · [`00b4c888`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c864.md#insn-00b4c888)
- 新版 [`00b4d878`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d858.md#insn-00b4d878) · [`00b4d874`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d858.md#insn-00b4d874) · [`00b4d87c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d858.md#insn-00b4d87c)

~~~diff
- 00b4c884 ["INT_ADD", "register:40f0:8", ["const:b4c884:8", "const:4:8"]]
- 00b4c884 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4d878 ["INT_ADD", "register:40f0:8", ["const:b4d878:8", "const:4:8"]]
+ 00b4d878 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4c884 bytes 133a0494
+ 00b4d878 bytes 0a3a0494
- 00b4c880 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b4c880 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c880 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4c880 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4d874 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4d874 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d874 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4d874 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4c880 bytes 00341591
+ 00b4d874 bytes 00681891
- 00b4c888 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4d87c ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4c888 bytes c82e00b0
+ 00b4d87c bytes c82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e6724734a7d1cca518556b76b1aff249"></a>

### [`00b4c8a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c8a0.md) → [`00b4d894`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d894.md) _ZN8firebase4util3map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
      "definition_site": "00b4d8c0",
      "incomplete_value": true,
      "site": "00b4d8c0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c8cc",
      "incomplete_value": true,
      "site": "00b4c8cc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d8a8",
      "incomplete_value": true,
      "site": "00b4d8a8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c8b4",
      "incomplete_value": true,
      "site": "00b4c8b4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d8b4",
      "incomplete_value": false,
      "site": "00b4d8b8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:655:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c8c0",
      "incomplete_value": false,
      "site": "00b4c8c4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:57e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d8a4",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d8b4",
      "PARAM",
      [
        "storage",
        "002b157e",
        null,
        "string"
      ]
    ],
    [
      "00b4d8c0",
      "WRITE",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d8a4",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d8b4",
      "PARAM",
      [
        "storage",
        "002b1655",
        null,
        "string"
      ]
    ],
    [
      "00b4d8c0",
      "WRITE",
      [
        "storage",
        "01126cf8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c8c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c8a0.md#insn-00b4c8c4) · [`00b4c8cc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c8a0.md#insn-00b4c8cc) · [`00b4c8ac`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c8a0.md#insn-00b4c8ac)
- 新版 [`00b4d8b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d894.md#insn-00b4d8b8) · [`00b4d8c0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d894.md#insn-00b4d8c0) · [`00b4d8a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d894.md#insn-00b4d8a0)

~~~diff
- 00b4c8c4 ["INT_ADD", "register:40f0:8", ["const:b4c8c4:8", "const:4:8"]]
- 00b4c8c4 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d8b8 ["INT_ADD", "register:40f0:8", ["const:b4d8b8:8", "const:4:8"]]
+ 00b4d8b8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c8c4 bytes c7390494
+ 00b4d8b8 bytes be390494
- 00b4c8cc ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d38:8"]]
- 00b4c8cc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d8c0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf8:8"]]
+ 00b4d8c0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c8cc bytes 609e06f9
+ 00b4d8c0 bytes 607e06f9
- 00b4c8ac ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4d8a0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4c8ac bytes d32e00b0
+ 00b4d8a0 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-b2ddc2c5896e701ab9613ae67e8badcf"></a>

### [`00b4c8e0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c8e0.md) → [`00b4d8d4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d8d4.md) _ZN8firebase4util3map19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4d900",
      "incomplete_value": true,
      "site": "00b4d900",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c90c",
      "incomplete_value": true,
      "site": "00b4c90c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d8e8",
      "incomplete_value": true,
      "site": "00b4d8e8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c8f4",
      "incomplete_value": true,
      "site": "00b4c8f4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d8f0",
      "incomplete_value": false,
      "site": "00b4d8f8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:655:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c8fc",
      "incomplete_value": false,
      "site": "00b4c904",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:57e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d8e4",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d8f0",
      "PARAM",
      [
        "storage",
        "002b157e",
        null,
        "string"
      ]
    ],
    [
      "00b4d900",
      "WRITE",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d8e4",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d8f0",
      "PARAM",
      [
        "storage",
        "002b1655",
        null,
        "string"
      ]
    ],
    [
      "00b4d900",
      "WRITE",
      [
        "storage",
        "01126cf8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c904`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c8e0.md#insn-00b4c904) · [`00b4c90c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c8e0.md#insn-00b4c90c) · [`00b4c8ec`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c8e0.md#insn-00b4c8ec)
- 新版 [`00b4d8f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d8d4.md#insn-00b4d8f8) · [`00b4d900`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d8d4.md#insn-00b4d900) · [`00b4d8e0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d8d4.md#insn-00b4d8e0)

~~~diff
- 00b4c904 ["INT_ADD", "register:40f0:8", ["const:b4c904:8", "const:4:8"]]
- 00b4c904 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d8f8 ["INT_ADD", "register:40f0:8", ["const:b4d8f8:8", "const:4:8"]]
+ 00b4d8f8 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c904 bytes b7390494
+ 00b4d8f8 bytes ae390494
- 00b4c90c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d38:8"]]
- 00b4c90c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d900 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf8:8"]]
+ 00b4d900 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c90c bytes 609e06f9
+ 00b4d900 bytes 607e06f9
- 00b4c8ec ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4d8e0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4c8ec bytes d32e00b0
+ 00b4d8e0 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-546208551cadbfe27019e3d6d83b259f"></a>

### [`00b4c920`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c920.md) → [`00b4d914`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d914.md) _ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4d944",
      "incomplete_value": true,
      "site": "00b4d944",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c950",
      "incomplete_value": true,
      "site": "00b4c950",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d928",
      "incomplete_value": true,
      "site": "00b4d928",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c934",
      "incomplete_value": true,
      "site": "00b4c934",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d934",
      "incomplete_value": false,
      "site": "00b4d93c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:655:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c940",
      "incomplete_value": false,
      "site": "00b4c948",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:57e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d924",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d934",
      "PARAM",
      [
        "storage",
        "002b157e",
        null,
        "string"
      ]
    ],
    [
      "00b4d944",
      "WRITE",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d924",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d934",
      "PARAM",
      [
        "storage",
        "002b1655",
        null,
        "string"
      ]
    ],
    [
      "00b4d944",
      "WRITE",
      [
        "storage",
        "01126cf8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c948`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c920.md#insn-00b4c948) · [`00b4c950`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c920.md#insn-00b4c950) · [`00b4c92c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c920.md#insn-00b4c92c)
- 新版 [`00b4d93c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d914.md#insn-00b4d93c) · [`00b4d944`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d914.md#insn-00b4d944) · [`00b4d920`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d914.md#insn-00b4d920)

~~~diff
- 00b4c948 ["INT_ADD", "register:40f0:8", ["const:b4c948:8", "const:4:8"]]
- 00b4c948 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d93c ["INT_ADD", "register:40f0:8", ["const:b4d93c:8", "const:4:8"]]
+ 00b4d93c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c948 bytes a6390494
+ 00b4d93c bytes 9d390494
- 00b4c950 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d38:8"]]
- 00b4c950 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d944 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf8:8"]]
+ 00b4d944 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c950 bytes 609e06f9
+ 00b4d944 bytes 607e06f9
- 00b4c92c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4d920 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4c92c bytes d32e00b0
+ 00b4d920 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-4395d302d6b68c5dfe3232271e53d307"></a>

### [`00b4c964`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c964.md) → [`00b4d958`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d958.md) _ZN8firebase4util3map10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4d988",
      "incomplete_value": true,
      "site": "00b4d988",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c994",
      "incomplete_value": true,
      "site": "00b4c994",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d38:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4d96c",
      "incomplete_value": true,
      "site": "00b4d96c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c978",
      "incomplete_value": true,
      "site": "00b4c978",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4d974",
      "incomplete_value": false,
      "site": "00b4d980",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:655:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c980",
      "incomplete_value": false,
      "site": "00b4c98c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:57e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4d968",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d974",
      "PARAM",
      [
        "storage",
        "002b157e",
        null,
        "string"
      ]
    ],
    [
      "00b4d988",
      "WRITE",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4d968",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4d974",
      "PARAM",
      [
        "storage",
        "002b1655",
        null,
        "string"
      ]
    ],
    [
      "00b4d988",
      "WRITE",
      [
        "storage",
        "01126cf8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c98c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c964.md#insn-00b4c98c) · [`00b4c994`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c964.md#insn-00b4c994) · [`00b4c970`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c964.md#insn-00b4c970)
- 新版 [`00b4d980`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d958.md#insn-00b4d980) · [`00b4d988`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d958.md#insn-00b4d988) · [`00b4d964`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d958.md#insn-00b4d964)

~~~diff
- 00b4c98c ["INT_ADD", "register:40f0:8", ["const:b4c98c:8", "const:4:8"]]
- 00b4c98c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4d980 ["INT_ADD", "register:40f0:8", ["const:b4d980:8", "const:4:8"]]
+ 00b4d980 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4c98c bytes 95390494
+ 00b4d980 bytes 8c390494
- 00b4c994 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d38:8"]]
- 00b4c994 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4d988 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:cf8:8"]]
+ 00b4d988 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4c994 bytes 609e06f9
+ 00b4d988 bytes 607e06f9
- 00b4c970 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4d964 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4c970 bytes d32e00b0
+ 00b4d964 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-a787fddcc2e7c523f93b2478eec286a4"></a>

### [`00b4c9b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c9b4.md) → [`00b4d9a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d9a8.md) _ZN8firebase4util3map15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4da30",
      "incomplete_value": true,
      "site": "00b4da30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ca3c",
      "incomplete_value": true,
      "site": "00b4ca3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d40:8"
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
      "definition_site": "00b4d9dc",
      "incomplete_value": true,
      "site": "00b4d9e8",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:cf8:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4c9e8",
      "incomplete_value": true,
      "site": "00b4c9f4",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d38:8"
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
      "00b4d9bc",
      "READ",
      [
        "storage",
        "01125d40",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d9dc",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4da30",
      "WRITE",
      [
        "storage",
        "01125d40",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4d9bc",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4d9dc",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4da30",
      "WRITE",
      [
        "storage",
        "01126d00",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4c9f4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c9b4.md#insn-00b4c9f4) · [`00b4ca3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c9b4.md#insn-00b4ca3c) · [`00b4c9c4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4c9b4.md#insn-00b4c9c4)
- 新版 [`00b4d9e8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d9a8.md#insn-00b4d9e8) · [`00b4da30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d9a8.md#insn-00b4da30) · [`00b4d9b8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4d9a8.md#insn-00b4d9b8)

~~~diff
- 00b4c9f4 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4c9f4 ["INT_ADD", "register:40f0:8", ["const:b4c9f4:8", "const:4:8"]]
- 00b4c9f4 ["CALLIND", null, ["register:0:8"]]
+ 00b4d9e8 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4d9e8 ["INT_ADD", "register:40f0:8", ["const:b4d9e8:8", "const:4:8"]]
+ 00b4d9e8 ["CALLIND", null, ["register:0:8"]]
- 00b4c9f4 bytes 00013fd6
+ 00b4d9e8 bytes 00013fd6
- 00b4ca3c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4ca3c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d40:8"]]
- 00b4ca3c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4da30 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4da30 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d00:8"]]
+ 00b4da30 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4ca3c bytes a0023539
+ 00b4da30 bytes a0023439
- 00b4c9c4 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4d9b8 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4c9c4 bytes d52e00b0
+ 00b4d9b8 bytes d52e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-58b03829d5491af774cefbe2f742ce91"></a>

### [`00b4ca50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ca50.md) → [`00b4da44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4da44.md) _ZN8firebase4util3map12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4da80",
      "incomplete_value": true,
      "site": "00b4da80",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d00:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ca8c",
      "incomplete_value": true,
      "site": "00b4ca8c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d40:8"
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
      "definition_site": "00b4dad0",
      "incomplete_value": true,
      "site": "00b4dad0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cadc",
      "incomplete_value": true,
      "site": "00b4cadc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "definition_site": "00b4da5c",
      "incomplete_value": true,
      "site": "00b4da5c",
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
      "definition_site": "00b4ca68",
      "incomplete_value": true,
      "site": "00b4ca68",
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
      "00b4da58",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4da64",
      "READ",
      [
        "storage",
        "01125d40",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4da80",
      "WRITE",
      [
        "storage",
        "01125d40",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4da58",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4da64",
      "READ",
      [
        "storage",
        "01126d00",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4da80",
      "WRITE",
      [
        "storage",
        "01126d00",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ca8c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ca50.md#insn-00b4ca8c) · [`00b4cad8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ca50.md#insn-00b4cad8) · [`00b4cadc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ca50.md#insn-00b4cadc)
- 新版 [`00b4da80`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4da44.md#insn-00b4da80) · [`00b4dacc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4da44.md#insn-00b4dacc) · [`00b4dad0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4da44.md#insn-00b4dad0)

~~~diff
- 00b4ca8c ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4ca8c ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4ca8c ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d40:8"]]
- 00b4ca8c ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4da80 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4da80 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4da80 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d00:8"]]
+ 00b4da80 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4ca8c bytes bf023539
+ 00b4da80 bytes bf023439
- 00b4cad8 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4cad8 ["INT_ADD", "register:40f0:8", ["const:b4cad8:8", "const:4:8"]]
- 00b4cad8 ["CALLIND", null, ["register:0:8"]]
+ 00b4dacc ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4dacc ["INT_ADD", "register:40f0:8", ["const:b4dacc:8", "const:4:8"]]
+ 00b4dacc ["CALLIND", null, ["register:0:8"]]
- 00b4cad8 bytes 00013fd6
+ 00b4dacc bytes 00013fd6
- 00b4cadc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d38:8"]]
- 00b4cadc ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4cadc ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4dad0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf8:8"]]
+ 00b4dad0 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4dad0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4cadc bytes 9f9e06f9
+ 00b4dad0 bytes 9f7e06f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0a4db912ff617b965b8267000e02df9c"></a>

### [`00b4caf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4caf0.md) → [`00b4dae4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dae4.md) _ZN8firebase4util3map14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4db24",
      "incomplete_value": true,
      "site": "00b4db24",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cb30",
      "incomplete_value": true,
      "site": "00b4cb30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "definition_site": "00b4db00",
      "incomplete_value": true,
      "site": "00b4db00",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cb0c",
      "incomplete_value": true,
      "site": "00b4cb0c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4db08",
      "incomplete_value": false,
      "site": "00b4db1c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:655:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cb14",
      "incomplete_value": false,
      "site": "00b4cb28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "leaf",
            "const:2b1000:8"
          ],
          [
            "leaf",
            "const:57e:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4daf8",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db08",
      "PARAM",
      [
        "storage",
        "002b157e",
        null,
        "string"
      ]
    ],
    [
      "00b4db24",
      "WRITE",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4daf8",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4db08",
      "PARAM",
      [
        "storage",
        "002b1655",
        null,
        "string"
      ]
    ],
    [
      "00b4db24",
      "WRITE",
      [
        "storage",
        "01126cf8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cb28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4caf0.md#insn-00b4cb28) · [`00b4cb30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4caf0.md#insn-00b4cb30) · [`00b4cafc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4caf0.md#insn-00b4cafc)
- 新版 [`00b4db1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dae4.md#insn-00b4db1c) · [`00b4db24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dae4.md#insn-00b4db24) · [`00b4daf0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dae4.md#insn-00b4daf0)

~~~diff
- 00b4cb28 ["INT_ADD", "register:40f0:8", ["const:b4cb28:8", "const:4:8"]]
- 00b4cb28 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4db1c ["INT_ADD", "register:40f0:8", ["const:b4db1c:8", "const:4:8"]]
+ 00b4db1c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4cb28 bytes 2e390494
+ 00b4db1c bytes 25390494
- 00b4cb30 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d38:8"]]
- 00b4cb30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4db24 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf8:8"]]
+ 00b4db24 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cb30 bytes 809e06f9
+ 00b4db24 bytes 807e06f9
- 00b4cafc ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4daf0 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4cafc bytes d42e00b0
+ 00b4daf0 bytes d42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-61e8bd2a7fd8887fe42194b02cfbcbd8"></a>

### [`00b4cb60`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cb60.md) → [`00b4db54`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4db54.md) _ZN8firebase4util3map11GetMethodIdENS1_6MethodE

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 1件 [`00c5b050`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b050.md) · 呼出先 1件 [`00c5b0d0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5b/00c5b0d0.md)
- 新版 呼出元 1件 [`00c5c020`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c020.md) · 呼出先 1件 [`00c5c0a0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5c/00c5c0a0.md)

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
      "definition_site": "00b4db70",
      "incomplete_value": false,
      "site": "00b4db74",
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
      "definition_site": "00b4cb7c",
      "incomplete_value": false,
      "site": "00b4cb80",
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
      "definition_site": "00b4db80",
      "incomplete_value": true,
      "site": "00b4db8c",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4cb8c",
      "incomplete_value": true,
      "site": "00b4cb98",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4db70",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4db80",
      "DATA",
      [
        "storage",
        "01125d48",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4db70",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4db80",
      "DATA",
      [
        "storage",
        "01126d08",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cb80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cb60.md#insn-00b4cb80) · [`00b4cb7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cb60.md#insn-00b4cb7c) · [`00b4cb84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cb60.md#insn-00b4cb84)
- 新版 [`00b4db74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4db54.md#insn-00b4db74) · [`00b4db70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4db54.md#insn-00b4db70) · [`00b4db78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4db54.md#insn-00b4db78)

~~~diff
- 00b4cb80 ["INT_ADD", "register:40f0:8", ["const:b4cb80:8", "const:4:8"]]
- 00b4cb80 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4db74 ["INT_ADD", "register:40f0:8", ["const:b4db74:8", "const:4:8"]]
+ 00b4db74 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4cb80 bytes 54390494
+ 00b4db74 bytes 4b390494
- 00b4cb7c ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4cb7c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cb7c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cb7c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4db70 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4db70 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4db70 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4db70 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4cb7c bytes 002c0c91
+ 00b4db70 bytes 008c1191
- 00b4cb84 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4db78 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4cb84 bytes c82e00b0
+ 00b4db78 bytes c82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5d32a45255c308e78c4af6cf6d53467a"></a>

### [`00b4cb9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cb9c.md) → [`00b4db90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4db90.md) _ZN8firebase4util3map13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4dbd0",
      "incomplete_value": true,
      "site": "00b4dbd0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:cf8:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cbdc",
      "incomplete_value": true,
      "site": "00b4cbdc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d38:8"
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
      "definition_site": "00b4dbac",
      "incomplete_value": true,
      "site": "00b4dbac",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cbb8",
      "incomplete_value": true,
      "site": "00b4cbb8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
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
        "00b4cbb8"
      ],
      [
        "FALL_THROUGH",
        "00b4dbac"
      ]
    ],
    "kind": "store_condition",
    "new": {
      "definition_site": "00b4dbac",
      "incomplete_value": true,
      "site": "00b4dbd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cbb8",
      "incomplete_value": true,
      "site": "00b4cbdc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
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
      "00b4dba4",
      "READ",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dbb4",
      "PARAM",
      [
        "storage",
        "002b157e",
        null,
        "string"
      ]
    ],
    [
      "00b4dbd0",
      "WRITE",
      [
        "storage",
        "01125d38",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dba4",
      "READ",
      [
        "storage",
        "01126cf8",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dbb4",
      "PARAM",
      [
        "storage",
        "002b1655",
        null,
        "string"
      ]
    ],
    [
      "00b4dbd0",
      "WRITE",
      [
        "storage",
        "01126cf8",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cbdc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cb9c.md#insn-00b4cbdc) · [`00b4cba8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cb9c.md#insn-00b4cba8) · [`00b4cbb0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cb9c.md#insn-00b4cbb0)
- 新版 [`00b4dbd0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4db90.md#insn-00b4dbd0) · [`00b4db9c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4db90.md#insn-00b4db9c) · [`00b4dba4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4db90.md#insn-00b4dba4)

~~~diff
- 00b4cbdc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d38:8"]]
- 00b4cbdc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dbd0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf8:8"]]
+ 00b4dbd0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cbdc bytes 809e06f9
+ 00b4dbd0 bytes 807e06f9
- 00b4cba8 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4db9c ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4cba8 bytes d42e00b0
+ 00b4db9c bytes d42e00b0
- 00b4cbb0 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d38:8"]]
- 00b4cbb0 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4dba4 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:cf8:8"]]
+ 00b4dba4 ["LOAD", "register:4008:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cbb0 bytes 819e46f9
+ 00b4dba4 bytes 817e46f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-12be63f1630cf529d454f6c8cfc8aea4"></a>

### [`00b4cc0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cc0c.md) → [`00b4dc00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dc00.md) _ZN8firebase4util3map10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4dc1c",
      "incomplete_value": false,
      "site": "00b4dc20",
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
      "definition_site": "00b4cc28",
      "incomplete_value": false,
      "site": "00b4cc2c",
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
      "definition_site": "00b4dc2c",
      "incomplete_value": true,
      "site": "00b4dc38",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4cc38",
      "incomplete_value": true,
      "site": "00b4cc44",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4dc1c",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4dc2c",
      "DATA",
      [
        "storage",
        "01125d60",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4dc1c",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4dc2c",
      "DATA",
      [
        "storage",
        "01126d20",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cc2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cc0c.md#insn-00b4cc2c) · [`00b4cc28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cc0c.md#insn-00b4cc28) · [`00b4cc30`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cc0c.md#insn-00b4cc30)
- 新版 [`00b4dc20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dc00.md#insn-00b4dc20) · [`00b4dc1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dc00.md#insn-00b4dc1c) · [`00b4dc24`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dc00.md#insn-00b4dc24)

~~~diff
- 00b4cc2c ["INT_ADD", "register:40f0:8", ["const:b4cc2c:8", "const:4:8"]]
- 00b4cc2c ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4dc20 ["INT_ADD", "register:40f0:8", ["const:b4dc20:8", "const:4:8"]]
+ 00b4dc20 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4cc2c bytes 29390494
+ 00b4dc20 bytes 20390494
- 00b4cc28 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b4cc28 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cc28 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cc28 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4dc1c ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4dc1c ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4dc1c ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4dc1c ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4cc28 bytes 00341591
+ 00b4dc1c bytes 00681891
- 00b4cc30 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4dc24 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4cc30 bytes c82e00b0
+ 00b4dc24 bytes c82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9ef34464c7771a6bb206204ee8cf87e5"></a>

### [`00b4cc48`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cc48.md) → [`00b4dc3c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dc3c.md) _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

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
      "definition_site": "00b4dc68",
      "incomplete_value": true,
      "site": "00b4dc68",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cc74",
      "incomplete_value": true,
      "site": "00b4cc74",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4dc50",
      "incomplete_value": true,
      "site": "00b4dc50",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cc5c",
      "incomplete_value": true,
      "site": "00b4cc5c",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4dc5c",
      "incomplete_value": false,
      "site": "00b4dc60",
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
            "const:bad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cc68",
      "incomplete_value": false,
      "site": "00b4cc6c",
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
            "const:ae2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4dc4c",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dc5c",
      "PARAM",
      [
        "storage",
        "002a3ae2",
        null,
        "string"
      ]
    ],
    [
      "00b4dc68",
      "WRITE",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dc4c",
      "READ",
      [
        "storage",
        "01126d28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dc5c",
      "PARAM",
      [
        "storage",
        "002a3bad",
        null,
        "string"
      ]
    ],
    [
      "00b4dc68",
      "WRITE",
      [
        "storage",
        "01126d28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cc6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cc48.md#insn-00b4cc6c) · [`00b4cc74`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cc48.md#insn-00b4cc74) · [`00b4cc54`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cc48.md#insn-00b4cc54)
- 新版 [`00b4dc60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dc3c.md#insn-00b4dc60) · [`00b4dc68`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dc3c.md#insn-00b4dc68) · [`00b4dc48`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dc3c.md#insn-00b4dc48)

~~~diff
- 00b4cc6c ["INT_ADD", "register:40f0:8", ["const:b4cc6c:8", "const:4:8"]]
- 00b4cc6c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4dc60 ["INT_ADD", "register:40f0:8", ["const:b4dc60:8", "const:4:8"]]
+ 00b4dc60 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4cc6c bytes dd380494
+ 00b4dc60 bytes d4380494
- 00b4cc74 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d68:8"]]
- 00b4cc74 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dc68 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d28:8"]]
+ 00b4dc68 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cc74 bytes 60b606f9
+ 00b4dc68 bytes 609606f9
- 00b4cc54 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4dc48 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4cc54 bytes d32e00b0
+ 00b4dc48 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-aa8af8f93a22800e42a091b12421abc1"></a>

### [`00b4cc88`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cc88.md) → [`00b4dc7c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dc7c.md) _ZN8firebase4util22parcel_file_descriptor19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9alloca

採用 · 移動量 `+0xff4` · 根拠 `symbol` · `raw_instruction_pcode` · `limited` · 参照 `changed`

- 旧版 呼出元 0件  · 呼出先 1件 [`00c5afe0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c5a/00c5afe0.md)
- 新版 呼出元 0件  · 呼出先 1件 [`00c5bfb0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c5b/00c5bfb0.md)

変更の種類 constant, operands_and_dependencies, store_destination

命令の説明率　旧版 87.50% / 新版 87.50%

CFGの説明率　旧版 100.00% / 新版 100.00%

正規化の根拠 `recorded_reference_targets` · `pc_relative_address_generation` · `matched_instruction_sites`

優先判定に残った影響 `store_destination` 1件

~~~json
[
  {
    "confidence": "limited",
    "kind": "store_destination",
    "new": {
      "definition_site": "00b4dca8",
      "incomplete_value": true,
      "site": "00b4dca8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ccb4",
      "incomplete_value": true,
      "site": "00b4ccb4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "00b4dc8c",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dc98",
      "PARAM",
      [
        "storage",
        "002a3ae2",
        null,
        "string"
      ]
    ],
    [
      "00b4dca8",
      "WRITE",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dc8c",
      "READ",
      [
        "storage",
        "01126d28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dc98",
      "PARAM",
      [
        "storage",
        "002a3bad",
        null,
        "string"
      ]
    ],
    [
      "00b4dca8",
      "WRITE",
      [
        "storage",
        "01126d28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ccb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cc88.md#insn-00b4ccb4) · [`00b4cc94`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cc88.md#insn-00b4cc94) · [`00b4cc98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cc88.md#insn-00b4cc98)
- 新版 [`00b4dca8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dc7c.md#insn-00b4dca8) · [`00b4dc88`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dc7c.md#insn-00b4dc88) · [`00b4dc8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dc7c.md#insn-00b4dc8c)

~~~diff
- 00b4ccb4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d68:8"]]
- 00b4ccb4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dca8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d28:8"]]
+ 00b4dca8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ccb4 bytes 60b606f9
+ 00b4dca8 bytes 609606f9
- 00b4cc94 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4dc88 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4cc94 bytes d32e00b0
+ 00b4dc88 bytes d32e00b0
- 00b4cc98 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d68:8"]]
- 00b4cc98 ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
+ 00b4dc8c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d28:8"]]
+ 00b4dc8c ["LOAD", "register:4040:8", ["const:1b1:8", "tmp:0:8"]]
- 00b4cc98 bytes 68b646f9
+ 00b4dc8c bytes 689646f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-0fe1951a00694b47f1bcb98b9f9b6aa6"></a>

### [`00b4ccc8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ccc8.md) → [`00b4dcbc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dcbc.md) _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4dcec",
      "incomplete_value": true,
      "site": "00b4dcec",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ccf8",
      "incomplete_value": true,
      "site": "00b4ccf8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4dcd0",
      "incomplete_value": true,
      "site": "00b4dcd0",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ccdc",
      "incomplete_value": true,
      "site": "00b4ccdc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4dcdc",
      "incomplete_value": false,
      "site": "00b4dce4",
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
            "const:bad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cce8",
      "incomplete_value": false,
      "site": "00b4ccf0",
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
            "const:ae2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4dccc",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dcdc",
      "PARAM",
      [
        "storage",
        "002a3ae2",
        null,
        "string"
      ]
    ],
    [
      "00b4dcec",
      "WRITE",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dccc",
      "READ",
      [
        "storage",
        "01126d28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dcdc",
      "PARAM",
      [
        "storage",
        "002a3bad",
        null,
        "string"
      ]
    ],
    [
      "00b4dcec",
      "WRITE",
      [
        "storage",
        "01126d28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ccf0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ccc8.md#insn-00b4ccf0) · [`00b4ccf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ccc8.md#insn-00b4ccf8) · [`00b4ccd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ccc8.md#insn-00b4ccd4)
- 新版 [`00b4dce4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dcbc.md#insn-00b4dce4) · [`00b4dcec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dcbc.md#insn-00b4dcec) · [`00b4dcc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dcbc.md#insn-00b4dcc8)

~~~diff
- 00b4ccf0 ["INT_ADD", "register:40f0:8", ["const:b4ccf0:8", "const:4:8"]]
- 00b4ccf0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4dce4 ["INT_ADD", "register:40f0:8", ["const:b4dce4:8", "const:4:8"]]
+ 00b4dce4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4ccf0 bytes bc380494
+ 00b4dce4 bytes b3380494
- 00b4ccf8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d68:8"]]
- 00b4ccf8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dcec ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d28:8"]]
+ 00b4dcec ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ccf8 bytes 60b606f9
+ 00b4dcec bytes 609606f9
- 00b4ccd4 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4dcc8 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4ccd4 bytes d32e00b0
+ 00b4dcc8 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dd267d76b23f6c7eeeb6653dae3c585a"></a>

### [`00b4cd0c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cd0c.md) → [`00b4dd00`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dd00.md) _ZN8firebase4util22parcel_file_descriptor10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4dd30",
      "incomplete_value": true,
      "site": "00b4dd30",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cd3c",
      "incomplete_value": true,
      "site": "00b4cd3c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d68:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4dd14",
      "incomplete_value": true,
      "site": "00b4dd14",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cd20",
      "incomplete_value": true,
      "site": "00b4cd20",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4dd1c",
      "incomplete_value": false,
      "site": "00b4dd28",
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
            "const:bad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cd28",
      "incomplete_value": false,
      "site": "00b4cd34",
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
            "const:ae2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4dd10",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dd1c",
      "PARAM",
      [
        "storage",
        "002a3ae2",
        null,
        "string"
      ]
    ],
    [
      "00b4dd30",
      "WRITE",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dd10",
      "READ",
      [
        "storage",
        "01126d28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4dd1c",
      "PARAM",
      [
        "storage",
        "002a3bad",
        null,
        "string"
      ]
    ],
    [
      "00b4dd30",
      "WRITE",
      [
        "storage",
        "01126d28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cd34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cd0c.md#insn-00b4cd34) · [`00b4cd3c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cd0c.md#insn-00b4cd3c) · [`00b4cd18`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cd0c.md#insn-00b4cd18)
- 新版 [`00b4dd28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dd00.md#insn-00b4dd28) · [`00b4dd30`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dd00.md#insn-00b4dd30) · [`00b4dd0c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dd00.md#insn-00b4dd0c)

~~~diff
- 00b4cd34 ["INT_ADD", "register:40f0:8", ["const:b4cd34:8", "const:4:8"]]
- 00b4cd34 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4dd28 ["INT_ADD", "register:40f0:8", ["const:b4dd28:8", "const:4:8"]]
+ 00b4dd28 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4cd34 bytes ab380494
+ 00b4dd28 bytes a2380494
- 00b4cd3c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d68:8"]]
- 00b4cd3c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4dd30 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d28:8"]]
+ 00b4dd30 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cd3c bytes 60b606f9
+ 00b4dd30 bytes 609606f9
- 00b4cd18 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4dd0c ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4cd18 bytes d32e00b0
+ 00b4dd0c bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-2c82f2d9930df90a8d210b3abd620106"></a>

### [`00b4cd5c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cd5c.md) → [`00b4dd50`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dd50.md) _ZN8firebase4util22parcel_file_descriptor15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4ddd8",
      "incomplete_value": true,
      "site": "00b4ddd8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cde4",
      "incomplete_value": true,
      "site": "00b4cde4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "definition_site": "00b4dd84",
      "incomplete_value": true,
      "site": "00b4dd90",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d28:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cd90",
      "incomplete_value": true,
      "site": "00b4cd9c",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d68:8"
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
      "00b4dd64",
      "READ",
      [
        "storage",
        "01125d70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4dd84",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ddd8",
      "WRITE",
      [
        "storage",
        "01125d70",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4dd64",
      "READ",
      [
        "storage",
        "01126d30",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4dd84",
      "READ",
      [
        "storage",
        "01126d28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4ddd8",
      "WRITE",
      [
        "storage",
        "01126d30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cd9c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cd5c.md#insn-00b4cd9c) · [`00b4cde4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cd5c.md#insn-00b4cde4) · [`00b4cd6c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cd5c.md#insn-00b4cd6c)
- 新版 [`00b4dd90`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dd50.md#insn-00b4dd90) · [`00b4ddd8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dd50.md#insn-00b4ddd8) · [`00b4dd60`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dd50.md#insn-00b4dd60)

~~~diff
- 00b4cd9c ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4cd9c ["INT_ADD", "register:40f0:8", ["const:b4cd9c:8", "const:4:8"]]
- 00b4cd9c ["CALLIND", null, ["register:0:8"]]
+ 00b4dd90 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4dd90 ["INT_ADD", "register:40f0:8", ["const:b4dd90:8", "const:4:8"]]
+ 00b4dd90 ["CALLIND", null, ["register:0:8"]]
- 00b4cd9c bytes 00013fd6
+ 00b4dd90 bytes 00013fd6
- 00b4cde4 ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4cde4 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d70:8"]]
- 00b4cde4 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4ddd8 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4ddd8 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d30:8"]]
+ 00b4ddd8 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4cde4 bytes a0c23539
+ 00b4ddd8 bytes a0c23439
- 00b4cd6c ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4dd60 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4cd6c bytes d52e00b0
+ 00b4dd60 bytes d52e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-1121d6dfa1c22bd1b47be7b1d076f1e7"></a>

### [`00b4cdf8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cdf8.md) → [`00b4ddec`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4ddec.md) _ZN8firebase4util22parcel_file_descriptor12ReleaseClassEP7_JNIEnv

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
      "definition_site": "00b4de28",
      "incomplete_value": true,
      "site": "00b4de28",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d30:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ce34",
      "incomplete_value": true,
      "site": "00b4ce34",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d70:8"
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
      "definition_site": "00b4de78",
      "incomplete_value": true,
      "site": "00b4de78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ce84",
      "incomplete_value": true,
      "site": "00b4ce84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "definition_site": "00b4de04",
      "incomplete_value": true,
      "site": "00b4de04",
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
      "definition_site": "00b4ce10",
      "incomplete_value": true,
      "site": "00b4ce10",
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
      "00b4de00",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de0c",
      "READ",
      [
        "storage",
        "01125d70",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4de28",
      "WRITE",
      [
        "storage",
        "01125d70",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4de00",
      "READ",
      [
        "storage",
        "01126d28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4de0c",
      "READ",
      [
        "storage",
        "01126d30",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4de28",
      "WRITE",
      [
        "storage",
        "01126d30",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ce34`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cdf8.md#insn-00b4ce34) · [`00b4ce80`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cdf8.md#insn-00b4ce80) · [`00b4ce84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cdf8.md#insn-00b4ce84)
- 新版 [`00b4de28`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4ddec.md#insn-00b4de28) · [`00b4de74`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4ddec.md#insn-00b4de74) · [`00b4de78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4ddec.md#insn-00b4de78)

~~~diff
- 00b4ce34 ["COPY", "tmp:0:4", ["const:0:4"]]
- 00b4ce34 ["COPY", "tmp:1:4", ["tmp:0:4"]]
- 00b4ce34 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d70:8"]]
- 00b4ce34 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
+ 00b4de28 ["COPY", "tmp:0:4", ["const:0:4"]]
+ 00b4de28 ["COPY", "tmp:1:4", ["tmp:0:4"]]
+ 00b4de28 ["INT_ADD", "tmp:2:8", ["register:40a8:8", "const:d30:8"]]
+ 00b4de28 ["STORE", null, ["const:1b1:8", "tmp:2:8", "tmp:1:1"]]
- 00b4ce34 bytes bfc23539
+ 00b4de28 bytes bfc23439
- 00b4ce80 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4ce80 ["INT_ADD", "register:40f0:8", ["const:b4ce80:8", "const:4:8"]]
- 00b4ce80 ["CALLIND", null, ["register:0:8"]]
+ 00b4de74 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4de74 ["INT_ADD", "register:40f0:8", ["const:b4de74:8", "const:4:8"]]
+ 00b4de74 ["CALLIND", null, ["register:0:8"]]
- 00b4ce80 bytes 00013fd6
+ 00b4de74 bytes 00013fd6
- 00b4ce84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
- 00b4ce84 ["COPY", "tmp:1:8", ["const:0:8"]]
- 00b4ce84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
+ 00b4de78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
+ 00b4de78 ["COPY", "tmp:1:8", ["const:0:8"]]
+ 00b4de78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "tmp:1:8"]]
- 00b4ce84 bytes 9fb606f9
+ 00b4de78 bytes 9f9606f9
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-9627da94bda8d68f1649ea67eeff1f47"></a>

### [`00b4ce98`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ce98.md) → [`00b4de8c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4de8c.md) _ZN8firebase4util22parcel_file_descriptor14CacheMethodIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4decc",
      "incomplete_value": true,
      "site": "00b4decc",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ced8",
      "incomplete_value": true,
      "site": "00b4ced8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "definition_site": "00b4dea8",
      "incomplete_value": true,
      "site": "00b4dea8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4ceb4",
      "incomplete_value": true,
      "site": "00b4ceb4",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4deb0",
      "incomplete_value": false,
      "site": "00b4dec4",
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
            "const:bad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cebc",
      "incomplete_value": false,
      "site": "00b4ced0",
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
            "const:ae2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4dea0",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4deb0",
      "PARAM",
      [
        "storage",
        "002a3ae2",
        null,
        "string"
      ]
    ],
    [
      "00b4decc",
      "WRITE",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dea0",
      "READ",
      [
        "storage",
        "01126d28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4deb0",
      "PARAM",
      [
        "storage",
        "002a3bad",
        null,
        "string"
      ]
    ],
    [
      "00b4decc",
      "WRITE",
      [
        "storage",
        "01126d28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4ced0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ce98.md#insn-00b4ced0) · [`00b4ced8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ce98.md#insn-00b4ced8) · [`00b4cea4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4ce98.md#insn-00b4cea4)
- 新版 [`00b4dec4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4de8c.md#insn-00b4dec4) · [`00b4decc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4de8c.md#insn-00b4decc) · [`00b4de98`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4de8c.md#insn-00b4de98)

~~~diff
- 00b4ced0 ["INT_ADD", "register:40f0:8", ["const:b4ced0:8", "const:4:8"]]
- 00b4ced0 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4dec4 ["INT_ADD", "register:40f0:8", ["const:b4dec4:8", "const:4:8"]]
+ 00b4dec4 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4ced0 bytes 44380494
+ 00b4dec4 bytes 3b380494
- 00b4ced8 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
- 00b4ced8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4decc ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
+ 00b4decc ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4ced8 bytes 80b606f9
+ 00b4decc bytes 809606f9
- 00b4cea4 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4de98 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4cea4 bytes d42e00b0
+ 00b4de98 bytes d42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-dff0deeaa5ebee87c402e9e39066c244"></a>

### [`00b4cf08`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cf08.md) → [`00b4defc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4defc.md) _ZN8firebase4util22parcel_file_descriptor11GetMethodIdENS1_6MethodE

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
      "definition_site": "00b4df18",
      "incomplete_value": false,
      "site": "00b4df1c",
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
      "definition_site": "00b4cf24",
      "incomplete_value": false,
      "site": "00b4cf28",
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
      "definition_site": "00b4df28",
      "incomplete_value": true,
      "site": "00b4df34",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4cf34",
      "incomplete_value": true,
      "site": "00b4cf40",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4df18",
      "PARAM",
      [
        "storage",
        "002a830b",
        null,
        "string"
      ]
    ],
    [
      "00b4df28",
      "DATA",
      [
        "storage",
        "01125d78",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4df18",
      "PARAM",
      [
        "storage",
        "002a8463",
        null,
        "string"
      ]
    ],
    [
      "00b4df28",
      "DATA",
      [
        "storage",
        "01126d38",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cf28`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cf08.md#insn-00b4cf28) · [`00b4cf24`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cf08.md#insn-00b4cf24) · [`00b4cf2c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cf08.md#insn-00b4cf2c)
- 新版 [`00b4df1c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4defc.md#insn-00b4df1c) · [`00b4df18`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4defc.md#insn-00b4df18) · [`00b4df20`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4defc.md#insn-00b4df20)

~~~diff
- 00b4cf28 ["INT_ADD", "register:40f0:8", ["const:b4cf28:8", "const:4:8"]]
- 00b4cf28 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4df1c ["INT_ADD", "register:40f0:8", ["const:b4df1c:8", "const:4:8"]]
+ 00b4df1c ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4cf28 bytes 6a380494
+ 00b4df1c bytes 61380494
- 00b4cf24 ["COPY", "tmp:0:8", ["const:30b:8"]]
- 00b4cf24 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cf24 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cf24 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4df18 ["COPY", "tmp:0:8", ["const:463:8"]]
+ 00b4df18 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4df18 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4df18 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4cf24 bytes 002c0c91
+ 00b4df18 bytes 008c1191
- 00b4cf2c ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4df20 ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4cf2c bytes c82e00b0
+ 00b4df20 bytes c82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-8a00bb2c8c569234f1c432b0cee06ab2"></a>

### [`00b4cf44`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cf44.md) → [`00b4df38`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4df38.md) _ZN8firebase4util22parcel_file_descriptor13CacheFieldIdsEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4df78",
      "incomplete_value": true,
      "site": "00b4df78",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d28:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cf84",
      "incomplete_value": true,
      "site": "00b4cf84",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a0:8"
          ],
          [
            "leaf",
            "const:d68:8"
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
      "definition_site": "00b4df54",
      "incomplete_value": true,
      "site": "00b4df54",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cf60",
      "incomplete_value": true,
      "site": "00b4cf60",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4df5c",
      "incomplete_value": false,
      "site": "00b4df70",
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
            "const:bad:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4cf68",
      "incomplete_value": false,
      "site": "00b4cf7c",
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
            "const:ae2:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4df4c",
      "READ",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4df5c",
      "PARAM",
      [
        "storage",
        "002a3ae2",
        null,
        "string"
      ]
    ],
    [
      "00b4df78",
      "WRITE",
      [
        "storage",
        "01125d68",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4df4c",
      "READ",
      [
        "storage",
        "01126d28",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4df5c",
      "PARAM",
      [
        "storage",
        "002a3bad",
        null,
        "string"
      ]
    ],
    [
      "00b4df78",
      "WRITE",
      [
        "storage",
        "01126d28",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cf7c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cf44.md#insn-00b4cf7c) · [`00b4cf84`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cf44.md#insn-00b4cf84) · [`00b4cf50`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cf44.md#insn-00b4cf50)
- 新版 [`00b4df70`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4df38.md#insn-00b4df70) · [`00b4df78`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4df38.md#insn-00b4df78) · [`00b4df44`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4df38.md#insn-00b4df44)

~~~diff
- 00b4cf7c ["INT_ADD", "register:40f0:8", ["const:b4cf7c:8", "const:4:8"]]
- 00b4cf7c ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4df70 ["INT_ADD", "register:40f0:8", ["const:b4df70:8", "const:4:8"]]
+ 00b4df70 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4cf7c bytes 19380494
+ 00b4df70 bytes 10380494
- 00b4cf84 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d68:8"]]
- 00b4cf84 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4df78 ["INT_ADD", "tmp:0:8", ["register:40a0:8", "const:d28:8"]]
+ 00b4df78 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4cf84 bytes 80b606f9
+ 00b4df78 bytes 809606f9
- 00b4cf50 ["COPY", "register:40a0:8", ["const:1125000:8"]]
+ 00b4df44 ["COPY", "register:40a0:8", ["const:1126000:8"]]
- 00b4cf50 bytes d42e00b0
+ 00b4df44 bytes d42e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-e131eb2f691fcfae5380b4b9bf285d12"></a>

### [`00b4cfb4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cfb4.md) → [`00b4dfa8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dfa8.md) _ZN8firebase4util22parcel_file_descriptor10GetFieldIdENS1_5FieldE

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
      "definition_site": "00b4dfc4",
      "incomplete_value": false,
      "site": "00b4dfc8",
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
      "definition_site": "00b4cfd0",
      "incomplete_value": false,
      "site": "00b4cfd4",
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
      "definition_site": "00b4dfd4",
      "incomplete_value": true,
      "site": "00b4dfe0",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "definition_site": "00b4cfe0",
      "incomplete_value": true,
      "site": "00b4cfec",
      "value": [
        "LOAD",
        "8",
        [
          [
            "leaf",
            "const:1b1:8"
          ],
          [
            "INT_ADD",
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
      "00b4dfc4",
      "PARAM",
      [
        "storage",
        "002a954d",
        null,
        "string"
      ]
    ],
    [
      "00b4dfd4",
      "DATA",
      [
        "storage",
        "01125d80",
        null,
        null
      ]
    ]
  ],
  "added": [
    [
      "00b4dfc4",
      "PARAM",
      [
        "storage",
        "002a961a",
        null,
        "string"
      ]
    ],
    [
      "00b4dfd4",
      "DATA",
      [
        "storage",
        "01126d40",
        null,
        null
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4cfd4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cfb4.md#insn-00b4cfd4) · [`00b4cfd0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cfb4.md#insn-00b4cfd0) · [`00b4cfd8`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cfb4.md#insn-00b4cfd8)
- 新版 [`00b4dfc8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dfa8.md#insn-00b4dfc8) · [`00b4dfc4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dfa8.md#insn-00b4dfc4) · [`00b4dfcc`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dfa8.md#insn-00b4dfcc)

~~~diff
- 00b4cfd4 ["INT_ADD", "register:40f0:8", ["const:b4cfd4:8", "const:4:8"]]
- 00b4cfd4 ["CALL", null, ["callee:00c5c0a0:8"]]
+ 00b4dfc8 ["INT_ADD", "register:40f0:8", ["const:b4dfc8:8", "const:4:8"]]
+ 00b4dfc8 ["CALL", null, ["callee:00c5c0a0:8"]]
- 00b4cfd4 bytes 3f380494
+ 00b4dfc8 bytes 36380494
- 00b4cfd0 ["COPY", "tmp:0:8", ["const:54d:8"]]
- 00b4cfd0 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cfd0 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
- 00b4cfd0 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
+ 00b4dfc4 ["COPY", "tmp:0:8", ["const:61a:8"]]
+ 00b4dfc4 ["INT_CARRY", "register:105:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4dfc4 ["INT_SCARRY", "register:106:1", ["register:4000:8", "tmp:0:8"]]
+ 00b4dfc4 ["INT_ADD", "tmp:1:8", ["register:4000:8", "tmp:0:8"]]
- 00b4cfd0 bytes 00341591
+ 00b4dfc4 bytes 00681891
- 00b4cfd8 ["COPY", "register:4040:8", ["const:1125000:8"]]
+ 00b4dfcc ["COPY", "register:4040:8", ["const:1126000:8"]]
- 00b4cfd8 bytes c82e00b0
+ 00b4dfcc bytes c82e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-6fc9c73201e7e74f0db3de4f4b278e77"></a>

### [`00b4cff0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cff0.md) → [`00b4dfe4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dfe4.md) _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEENS0_16Cla

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
      "definition_site": "00b4e010",
      "incomplete_value": true,
      "site": "00b4e010",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d01c",
      "incomplete_value": true,
      "site": "00b4d01c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4dff8",
      "incomplete_value": true,
      "site": "00b4dff8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d004",
      "incomplete_value": true,
      "site": "00b4d004",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4e004",
      "incomplete_value": false,
      "site": "00b4e008",
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
            "const:602:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d010",
      "incomplete_value": false,
      "site": "00b4d014",
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
            "const:52b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4dff4",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e004",
      "PARAM",
      [
        "storage",
        "002b052b",
        null,
        "string"
      ]
    ],
    [
      "00b4e010",
      "WRITE",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4dff4",
      "READ",
      [
        "storage",
        "01126d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e004",
      "PARAM",
      [
        "storage",
        "002b0602",
        null,
        "string"
      ]
    ],
    [
      "00b4e010",
      "WRITE",
      [
        "storage",
        "01126d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d014`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cff0.md#insn-00b4d014) · [`00b4d01c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cff0.md#insn-00b4d01c) · [`00b4cffc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4c/00b4cff0.md#insn-00b4cffc)
- 新版 [`00b4e008`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dfe4.md#insn-00b4e008) · [`00b4e010`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dfe4.md#insn-00b4e010) · [`00b4dff0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4d/00b4dfe4.md#insn-00b4dff0)

~~~diff
- 00b4d014 ["INT_ADD", "register:40f0:8", ["const:b4d014:8", "const:4:8"]]
- 00b4d014 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4e008 ["INT_ADD", "register:40f0:8", ["const:b4e008:8", "const:4:8"]]
+ 00b4e008 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4d014 bytes f3370494
+ 00b4e008 bytes ea370494
- 00b4d01c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
- 00b4d01c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e010 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
+ 00b4e010 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d01c bytes 60c606f9
+ 00b4e010 bytes 60a606f9
- 00b4cffc ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4dff0 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4cffc bytes d32e00b0
+ 00b4dff0 bytes d32e00b0
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-3416efa874b6bc05c145e61465019689"></a>

### [`00b4d030`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d030.md) → [`00b4e024`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e024.md) _ZN8firebase4util3set19CacheClassFromFilesEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS6_9allocatorIS9_EEEE

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
      "definition_site": "00b4e050",
      "incomplete_value": true,
      "site": "00b4e050",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d05c",
      "incomplete_value": true,
      "site": "00b4d05c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4e038",
      "incomplete_value": true,
      "site": "00b4e038",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d044",
      "incomplete_value": true,
      "site": "00b4d044",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4e040",
      "incomplete_value": false,
      "site": "00b4e048",
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
            "const:602:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d04c",
      "incomplete_value": false,
      "site": "00b4d054",
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
            "const:52b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4e034",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e040",
      "PARAM",
      [
        "storage",
        "002b052b",
        null,
        "string"
      ]
    ],
    [
      "00b4e050",
      "WRITE",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e034",
      "READ",
      [
        "storage",
        "01126d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e040",
      "PARAM",
      [
        "storage",
        "002b0602",
        null,
        "string"
      ]
    ],
    [
      "00b4e050",
      "WRITE",
      [
        "storage",
        "01126d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d054`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d030.md#insn-00b4d054) · [`00b4d05c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d030.md#insn-00b4d05c) · [`00b4d03c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d030.md#insn-00b4d03c)
- 新版 [`00b4e048`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e024.md#insn-00b4e048) · [`00b4e050`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e024.md#insn-00b4e050) · [`00b4e030`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e024.md#insn-00b4e030)

~~~diff
- 00b4d054 ["INT_ADD", "register:40f0:8", ["const:b4d054:8", "const:4:8"]]
- 00b4d054 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4e048 ["INT_ADD", "register:40f0:8", ["const:b4e048:8", "const:4:8"]]
+ 00b4e048 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4d054 bytes e3370494
+ 00b4e048 bytes da370494
- 00b4d05c ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
- 00b4d05c ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e050 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
+ 00b4e050 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d05c bytes 60c606f9
+ 00b4e050 bytes 60a606f9
- 00b4d03c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4e030 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4d03c bytes d32e0090
+ 00b4e030 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-72bffcdd42ea32cdf643b100bee22040"></a>

### [`00b4d070`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d070.md) → [`00b4e064`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e064.md) _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobjectNS0_16ClassRequirementE

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
      "definition_site": "00b4e094",
      "incomplete_value": true,
      "site": "00b4e094",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d0a0",
      "incomplete_value": true,
      "site": "00b4d0a0",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4e078",
      "incomplete_value": true,
      "site": "00b4e078",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d084",
      "incomplete_value": true,
      "site": "00b4d084",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4e084",
      "incomplete_value": false,
      "site": "00b4e08c",
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
            "const:602:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d090",
      "incomplete_value": false,
      "site": "00b4d098",
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
            "const:52b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4e074",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e084",
      "PARAM",
      [
        "storage",
        "002b052b",
        null,
        "string"
      ]
    ],
    [
      "00b4e094",
      "WRITE",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e074",
      "READ",
      [
        "storage",
        "01126d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e084",
      "PARAM",
      [
        "storage",
        "002b0602",
        null,
        "string"
      ]
    ],
    [
      "00b4e094",
      "WRITE",
      [
        "storage",
        "01126d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d098`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d070.md#insn-00b4d098) · [`00b4d0a0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d070.md#insn-00b4d0a0) · [`00b4d07c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d070.md#insn-00b4d07c)
- 新版 [`00b4e08c`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e064.md#insn-00b4e08c) · [`00b4e094`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e064.md#insn-00b4e094) · [`00b4e070`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e064.md#insn-00b4e070)

~~~diff
- 00b4d098 ["INT_ADD", "register:40f0:8", ["const:b4d098:8", "const:4:8"]]
- 00b4d098 ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4e08c ["INT_ADD", "register:40f0:8", ["const:b4e08c:8", "const:4:8"]]
+ 00b4e08c ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4d098 bytes d2370494
+ 00b4e08c bytes c9370494
- 00b4d0a0 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
- 00b4d0a0 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e094 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
+ 00b4e094 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d0a0 bytes 60c606f9
+ 00b4e094 bytes 60a606f9
- 00b4d07c ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4e070 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4d07c bytes d32e0090
+ 00b4e070 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-15200cef833f3510cbfc400b6cc7645f"></a>

### [`00b4d0b4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d0b4.md) → [`00b4e0a8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e0a8.md) _ZN8firebase4util3set10CacheClassEP7_JNIEnvP8_jobject

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
      "definition_site": "00b4e0d8",
      "incomplete_value": true,
      "site": "00b4e0d8",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d48:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d0e4",
      "incomplete_value": true,
      "site": "00b4d0e4",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:4098:8"
          ],
          [
            "leaf",
            "const:d88:8"
          ]
        ]
      ]
    },
    "ordinal": 3,
    "slot": 1
  },
  {
    "confidence": "limited",
    "kind": "branch_value",
    "new": {
      "definition_site": "00b4e0bc",
      "incomplete_value": true,
      "site": "00b4e0bc",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d0c8",
      "incomplete_value": true,
      "site": "00b4d0c8",
      "value": [
        "INT_NOTEQUAL",
        "1",
        [
          [
            "LOAD",
            "8",
            [
              [
                "leaf",
                "const:1b1:8"
              ],
              "INT_ADD"
            ]
          ],
          [
            "leaf",
            "const:0:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 0
  },
  {
    "confidence": "limited",
    "kind": "call_argument_candidate",
    "new": {
      "definition_site": "00b4e0c4",
      "incomplete_value": false,
      "site": "00b4e0d0",
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
            "const:602:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d0d0",
      "incomplete_value": false,
      "site": "00b4d0dc",
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
            "const:52b:8"
          ]
        ]
      ]
    },
    "ordinal": 0,
    "slot": 4
  }
]
~~~


参照の変更（対応した命令位置）

~~~json
{
  "removed": [
    [
      "00b4e0b8",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e0c4",
      "PARAM",
      [
        "storage",
        "002b052b",
        null,
        "string"
      ]
    ],
    [
      "00b4e0d8",
      "WRITE",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ]
  ],
  "added": [
    [
      "00b4e0b8",
      "READ",
      [
        "storage",
        "01126d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e0c4",
      "PARAM",
      [
        "storage",
        "002b0602",
        null,
        "string"
      ]
    ],
    [
      "00b4e0d8",
      "WRITE",
      [
        "storage",
        "01126d48",
        null,
        "undefined8"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d0dc`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d0b4.md#insn-00b4d0dc) · [`00b4d0e4`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d0b4.md#insn-00b4d0e4) · [`00b4d0c0`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d0b4.md#insn-00b4d0c0)
- 新版 [`00b4e0d0`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e0a8.md#insn-00b4e0d0) · [`00b4e0d8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e0a8.md#insn-00b4e0d8) · [`00b4e0b4`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e0a8.md#insn-00b4e0b4)

~~~diff
- 00b4d0dc ["INT_ADD", "register:40f0:8", ["const:b4d0dc:8", "const:4:8"]]
- 00b4d0dc ["CALL", null, ["callee:00c5bfb0:8"]]
+ 00b4e0d0 ["INT_ADD", "register:40f0:8", ["const:b4e0d0:8", "const:4:8"]]
+ 00b4e0d0 ["CALL", null, ["callee:00c5bfb0:8"]]
- 00b4d0dc bytes c1370494
+ 00b4e0d0 bytes b8370494
- 00b4d0e4 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d88:8"]]
- 00b4d0e4 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
+ 00b4e0d8 ["INT_ADD", "tmp:0:8", ["register:4098:8", "const:d48:8"]]
+ 00b4e0d8 ["STORE", null, ["const:1b1:8", "tmp:0:8", "register:4000:8"]]
- 00b4d0e4 bytes 60c606f9
+ 00b4e0d8 bytes 60a606f9
- 00b4d0c0 ["COPY", "register:4098:8", ["const:1125000:8"]]
+ 00b4e0b4 ["COPY", "register:4098:8", ["const:1126000:8"]]
- 00b4d0c0 bytes d32e0090
+ 00b4e0b4 bytes d32e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

<a id="compare-5f3c116640c8eaa860d54f64e6c10f1a"></a>

### [`00b4d104`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d104.md) → [`00b4e0f8`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e0f8.md) _ZN8firebase4util3set15RegisterNativesEP7_JNIEnvPK15JNINativeMethodm

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
      "definition_site": "00b4e180",
      "incomplete_value": true,
      "site": "00b4e180",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d50:8"
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d18c",
      "incomplete_value": true,
      "site": "00b4d18c",
      "value": [
        "INT_ADD",
        "8",
        [
          [
            "live",
            "register:40a8:8"
          ],
          [
            "leaf",
            "const:d90:8"
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
      "definition_site": "00b4e12c",
      "incomplete_value": true,
      "site": "00b4e138",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d48:8"
              ]
            ]
          ]
        ]
      ]
    },
    "old": {
      "definition_site": "00b4d138",
      "incomplete_value": true,
      "site": "00b4d144",
      "value": [
        "LOAD",
        "8",
        [
          [
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
                "const:d88:8"
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
      "00b4e10c",
      "READ",
      [
        "storage",
        "01125d90",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4e12c",
      "READ",
      [
        "storage",
        "01125d88",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e180",
      "WRITE",
      [
        "storage",
        "01125d90",
        null,
        "undefined1"
      ]
    ]
  ],
  "added": [
    [
      "00b4e10c",
      "READ",
      [
        "storage",
        "01126d50",
        null,
        "undefined1"
      ]
    ],
    [
      "00b4e12c",
      "READ",
      [
        "storage",
        "01126d48",
        null,
        "undefined8"
      ]
    ],
    [
      "00b4e180",
      "WRITE",
      [
        "storage",
        "01126d50",
        null,
        "undefined1"
      ]
    ]
  ]
}
~~~


#### 変更候補の命令位置

- 旧版 [`00b4d144`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d104.md#insn-00b4d144) · [`00b4d18c`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d104.md#insn-00b4d18c) · [`00b4d114`](../../../../reference/16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b4d/00b4d104.md#insn-00b4d114)
- 新版 [`00b4e138`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e0f8.md#insn-00b4e138) · [`00b4e180`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e0f8.md#insn-00b4e180) · [`00b4e108`](../../../../reference/16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b4e/00b4e0f8.md#insn-00b4e108)

~~~diff
- 00b4d144 ["COPY", "register:0:8", ["register:4040:8"]]
- 00b4d144 ["INT_ADD", "register:40f0:8", ["const:b4d144:8", "const:4:8"]]
- 00b4d144 ["CALLIND", null, ["register:0:8"]]
+ 00b4e138 ["COPY", "register:0:8", ["register:4040:8"]]
+ 00b4e138 ["INT_ADD", "register:40f0:8", ["const:b4e138:8", "const:4:8"]]
+ 00b4e138 ["CALLIND", null, ["register:0:8"]]
- 00b4d144 bytes 00013fd6
+ 00b4e138 bytes 00013fd6
- 00b4d18c ["COPY", "tmp:0:4", ["register:4000:4"]]
- 00b4d18c ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d90:8"]]
- 00b4d18c ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
+ 00b4e180 ["COPY", "tmp:0:4", ["register:4000:4"]]
+ 00b4e180 ["INT_ADD", "tmp:1:8", ["register:40a8:8", "const:d50:8"]]
+ 00b4e180 ["STORE", null, ["const:1b1:8", "tmp:1:8", "tmp:0:1"]]
- 00b4d18c bytes a0423639
+ 00b4e180 bytes a0423539
- 00b4d114 ["COPY", "register:40a8:8", ["const:1125000:8"]]
+ 00b4e108 ["COPY", "register:40a8:8", ["const:1126000:8"]]
- 00b4d114 bytes d52e0090
+ 00b4e108 bytes d52e0090
~~~


全命令差分は構造索引を使い `matcher.logic_detail` でこのペアだけ展開できます。

